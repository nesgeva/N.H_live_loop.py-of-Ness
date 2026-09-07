#!/usr/bin/env python3
"""Small independent, read-only progress view for the N.H live loop."""

from __future__ import annotations

import argparse
import base64
import hashlib
import hmac
import json
import os
import re
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Callable
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
JOURNAL = ROOT / "nh_interview_state" / "nh_interview_journal.jsonl"
AUTH_KEY = ROOT / "nh_interview_state" / "nh_interview_authenticity.key"
LEASE = ROOT / "interview_ui" / ".nh_supervisor_state" / "supervisor_lease.json"
WORKER_HEALTH = ROOT / "interview_ui" / ".nh_supervisor_state" / "worker_health.json"
MAINTENANCE_PAUSE = ROOT / "interview_ui" / ".nh_supervisor_state" / "maintenance_pause.json"
PLAN = ROOT / "NH-GOVERNANCE" / "03_WORKFLOW" / "NH_REPLACEMENT_EIGHT_BUNDLE_DEPENDENCY_PLAN_v1_0_CANDIDATE.md"
CONTROLLER = ROOT / "controller" / "nh_loop.py"
CONTROLLER_REPO_PATH = "controller/nh_loop.py"
CONTROLLER_DIR = ROOT / "controller"
if str(CONTROLLER_DIR) not in sys.path:
    sys.path.insert(0, str(CONTROLLER_DIR))

from nh_supervisor import runtime as controller_runtime  # noqa: E402

PROVIDER_LABELS = {
    "local_codex_cli_chatgpt": "Codex",
    "local_claude_code_subscription": "Claude",
}

WORK_LABELS = {
    "gpt_question_validation": "validating the possible Ness questions",
    "gpt_question_coverage_review": "checking whether any genuine questions are missing",
    "codex_design_audit": "independently auditing the design candidate",
    "codex_next_package_selection": "selecting the next dependency-safe package",
    "codex_next_design_task_preparation": "preparing the next package task",
    "claude_initial_design": "drafting the design candidate",
    "claude_correction": "correcting the design candidate",
}

COMMAND_LABELS = {
    "dispatch-piece3-provider-review": "preparing or dispatching the current question review",
    "process-custodied-provider-result": "processing an already-saved provider result",
    "commit-piece3-provider-result": "recording the validated question result",
}


class ControllerIdentityReader:
    """Read the installed controller only when its filesystem identity changes."""

    def __init__(self, path: Path = CONTROLLER):
        self.path = path
        self._stat_identity: tuple[int, int, int, int] | None = None
        self._controller_identity: str | None = None
        self._lock = threading.Lock()

    def read(self) -> str:
        with self._lock:
            stat = self.path.stat()
            observed = (stat.st_dev, stat.st_ino, stat.st_size, stat.st_mtime_ns)
            if observed != self._stat_identity:
                self._controller_identity = (
                    controller_runtime.controller_executable_identity_of_file(
                        CONTROLLER_REPO_PATH, str(self.path)
                    )
                )
                self._stat_identity = observed
            assert self._controller_identity is not None
            return self._controller_identity


def _event_digest(event: dict[str, Any]) -> str:
    body = dict(event)
    body.pop("event_sha256", None)
    payload = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    return hashlib.sha256(payload).hexdigest()


class JournalTail:
    """Incrementally reads and verifies the authenticated journal chain."""

    def __init__(self, path: Path, auth_key_path: Path | None = None):
        self.path = path
        self._auth_key = auth_key_path.read_bytes() if auth_key_path else None
        self._lock = threading.Lock()
        self._identity: tuple[int, int] | None = None
        self._offset = 0
        self._partial = b""
        self._events: list[dict[str, Any]] = []
        self._error: str | None = None

    def read(self) -> tuple[list[dict[str, Any]], str | None]:
        with self._lock:
            try:
                stat = self.path.stat()
                identity = (stat.st_dev, stat.st_ino)
                if identity != self._identity or stat.st_size < self._offset:
                    self._identity = identity
                    self._offset = 0
                    self._partial = b""
                    self._events = []
                    self._error = None
                if stat.st_size == self._offset:
                    return list(self._events), self._error
                with self.path.open("rb") as handle:
                    handle.seek(self._offset)
                    chunk = handle.read()
                candidate = self._partial + chunk
                lines = candidate.split(b"\n")
                self._partial = lines.pop()
                new_events: list[dict[str, Any]] = []
                previous = self._events[-1] if self._events else None
                for raw in lines:
                    if not raw.strip():
                        continue
                    event = json.loads(raw)
                    if event.get("event_sha256") != _event_digest(event):
                        raise ValueError(f"event {event.get('event_seq')} has an invalid digest")
                    if self._auth_key is not None:
                        bound = {
                            key: value for key, value in event.items()
                            if key not in ("event_sha256", "event_auth_sha256")
                        }
                        material = json.dumps(
                            ["nh-interview-event-auth-v1", event.get("journal_version"), bound],
                            sort_keys=True, separators=(",", ":"), ensure_ascii=True,
                        ).encode()
                        expected_auth = hmac.new(self._auth_key, material, hashlib.sha256).hexdigest()
                        if not hmac.compare_digest(str(event.get("event_auth_sha256")), expected_auth):
                            raise ValueError(f"event {event.get('event_seq')} failed authentication")
                    if previous is not None:
                        if event.get("event_seq") != previous.get("event_seq", 0) + 1:
                            raise ValueError("journal event sequence is not contiguous")
                        if event.get("prev_event_sha256") != previous.get("event_sha256"):
                            raise ValueError("journal hash-chain link does not match")
                    new_events.append(event)
                    previous = event
                self._events.extend(new_events)
                self._offset += len(chunk)
                self._error = None
            except Exception as exc:  # keep the last verified projection available
                self._error = str(exc)
            return list(self._events), self._error


def _boot_id_sha256() -> str | None:
    try:
        # Match the existing N.H lease identity exactly: hash the raw proc bytes,
        # including the kernel-provided trailing newline.
        return hashlib.sha256(Path("/proc/sys/kernel/random/boot_id").read_bytes()).hexdigest()
    except OSError:
        return None


def exact_process_alive(pid: Any, start_ticks: Any, boot_hash: Any) -> bool:
    try:
        pid_number = int(pid)
        expected_ticks = int(start_ticks)
        if pid_number <= 0 or expected_ticks <= 0 or boot_hash != _boot_id_sha256():
            return False
        stat_text = Path(f"/proc/{pid_number}/stat").read_text()
        close_paren = stat_text.rfind(")")
        fields_after_name = stat_text[close_paren + 2 :].split()
        actual_ticks = int(fields_after_name[19])
        return actual_ticks == expected_ticks
    except (OSError, ValueError, TypeError, IndexError):
        return False


def process_elapsed_seconds(pid: Any, start_ticks: Any, boot_hash: Any) -> int | None:
    if not exact_process_alive(pid, start_ticks, boot_hash):
        return None
    try:
        uptime = float(Path("/proc/uptime").read_text().split()[0])
        ticks_per_second = os.sysconf("SC_CLK_TCK")
        return max(0, round(uptime - (int(start_ticks) / ticks_per_second)))
    except (OSError, ValueError, TypeError):
        return None


def bundle_for(package: str | None, plan_text: str) -> str:
    if not package:
        return "Not yet recorded"
    current: str | None = None
    for line in plan_text.splitlines():
        match = re.match(r"^### Bundle (\d+)\s+—\s+(.+)$", line)
        if match:
            current = f"Bundle {match.group(1)} — {match.group(2)}"
            continue
        if current and re.match(rf"^-\s+{re.escape(package)}\s+—", line):
            return current
    return "Not mapped in the current dependency plan"


def _read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text())
        return value if isinstance(value, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def _latest_package(events: list[dict[str, Any]]) -> str | None:
    for event in reversed(events):
        package = event.get("package_id") or event.get("package_key")
        if isinstance(package, str) and package and not package.startswith("nullpkg_"):
            return package
    return None


def _provider_requests(events: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    requests: dict[str, dict[str, Any]] = {}
    for event in events:
        request_id = event.get("provider_request_identity")
        if not request_id:
            continue
        record = requests.setdefault(request_id, {})
        kind = event.get("type")
        if kind == "provider_request_prepared":
            record["prepared"] = event
        elif kind == "provider_dispatch_begun":
            record["dispatch"] = event
        elif kind == "provider_result_custody_recorded":
            record["custody"] = event
        elif kind == "provider_request_terminal_recorded":
            record["terminal"] = event
        elif kind == "provider_request_reconciled":
            record["reconciliation"] = event
    return requests


def _active_operation(events: list[dict[str, Any]]) -> dict[str, Any] | None:
    completed = {
        event.get("supervisor_operation_id")
        for event in events
        if event.get("type") == "supervisor_operation_completed"
    }
    latest_started = next(
        (event for event in reversed(events) if event.get("type") == "supervisor_operation_started"),
        None,
    )
    if latest_started and latest_started.get("supervisor_operation_id") not in completed:
        return latest_started
    return None


def _pending_authorized_event(events: list[dict[str, Any]]) -> dict[str, Any] | None:
    authorization = next(
        (
            event for event in reversed(events)
            if event.get("type") == "piece3_provider_work_recorded"
            and isinstance(event.get("authorizes_event_type"), str)
        ),
        None,
    )
    if not authorization:
        return None
    authorized_type = authorization["authorizes_event_type"]
    if any(
        event.get("event_seq", 0) > authorization.get("event_seq", 0)
        and event.get("type") == authorized_type
        for event in events
    ):
        return None
    return authorization


def _needs_ness(events: list[dict[str, Any]]) -> tuple[str, bool, str | None, str | None]:
    resolved_uncertain_requests: set[str] = set()
    for event in reversed(events[-30:]):
        if (
            event.get("type") == "ness_transition_recovery_choice_recorded"
            and event.get("recovery_action") == "abandon_and_replace_once"
            and isinstance(event.get("provider_request_identity"), str)
        ):
            resolved_uncertain_requests.add(event["provider_request_identity"])
            continue
        record = event.get("dependency_record")
        record = record if isinstance(record, dict) else {}
        state = (
            event.get("next_workflow_state")
            or event.get("workflow_state")
            or record.get("next_workflow_state")
        )
        if state in {"NEEDS_NESS_DECISION", "WAITING_FOR_NESS", "READY_FOR_NESS_QUESTIONS"}:
            return "Yes — a genuine question is ready", True, "question", None
        if state == "READY_FOR_ACCEPTANCE":
            return "Yes — acceptance is required", True, "acceptance", None
        if state == "NEEDS_USER_ACTION":
            code = record.get("user_action_code") or event.get("user_action_code")
            if code == "provider_outcome_confirmation_required":
                request_identity = (
                    event.get("provider_request_identity")
                    or record.get("provider_request_identity")
                )
                if request_identity in resolved_uncertain_requests:
                    continue
                return (
                    "Yes — N.H is stopped because a provider outcome cannot be proved",
                    True,
                    "provider_reconciliation",
                    code,
                )
            return "Yes — an external action is required", True, "external_action", code
    return "No durable request for Ness is recorded", False, None, None


def _decoded_result(event: dict[str, Any] | None) -> dict[str, Any] | None:
    if not event or not isinstance(event.get("result_bytes_base64"), str):
        return None
    try:
        value = json.loads(base64.b64decode(event["result_bytes_base64"], validate=True))
        return value if isinstance(value, dict) else None
    except (ValueError, TypeError, json.JSONDecodeError):
        return None


def _human_issue_key(value: Any) -> str:
    return str(value).replace("_", " ").strip().capitalize()


def question_path(
    events: list[dict[str, Any]],
    provider: dict[str, Any] | None,
    provider_alive: bool,
    pending_result: bool,
    lease_current: bool,
    needs_ness_now: bool,
    restart_required: bool = False,
    worker_blocker: str | None = None,
    external_action_blocker: str | None = None,
) -> dict[str, Any]:
    """Project only journal-proved gates on the path to asking Ness."""
    package = _latest_package(events)
    scoped = [
        event for event in events
        if (event.get("package_id") or event.get("package_key")) == package
    ]
    validations = [event for event in scoped if event.get("type") == "validation_recorded"]
    latest_validation = validations[-1] if validations else None
    validation_custody = [
        event for event in scoped
        if event.get("type") == "provider_result_custody_recorded"
        and event.get("provider_kind") == "gpt_question_validation"
        and (
            latest_validation is None
            or event.get("event_seq", 0) < latest_validation.get("event_seq", 0)
        )
    ]
    validation_result_event = validation_custody[-1] if validation_custody else None
    validation_result = _decoded_result(validation_result_event)
    validated_count = None
    if latest_validation and validation_result:
        issues = validation_result.get("issues")
        if (
            validation_result.get("whole_check_complete") is True
            and validation_result.get("enumeration_complete") is True
            and isinstance(issues, list)
            and validation_result.get("total_issue_count") == len(issues)
        ):
            validated_count = len(issues)

    provisional_count = None
    provisional_count_event = None
    uncommitted_validation_custody = [
        event for event in scoped
        if event.get("type") == "provider_result_custody_recorded"
        and event.get("provider_kind") == "gpt_question_validation"
        and (
            latest_validation is None
            or event.get("event_seq", 0) > latest_validation.get("event_seq", 0)
        )
    ]
    if uncommitted_validation_custody:
        provisional_event = uncommitted_validation_custody[-1]
        provisional_result = _decoded_result(provisional_event)
        provisional_issues = provisional_result.get("issues") if provisional_result else None
        if (
            provisional_result
            and provisional_result.get("whole_check_complete") is True
            and provisional_result.get("enumeration_complete") is True
            and isinstance(provisional_issues, list)
            and provisional_result.get("total_issue_count") == len(provisional_issues)
        ):
            provisional_count = len(provisional_issues)
            provisional_count_event = provisional_event.get("event_seq")

    coverage_custody = [
        event for event in scoped
        if event.get("type") == "provider_result_custody_recorded"
        and event.get("provider_kind") == "gpt_question_coverage_review"
    ]
    coverage_result_event = coverage_custody[-1] if coverage_custody else None
    coverage_result = _decoded_result(coverage_result_event)
    coverage_request_id = coverage_result_event.get("provider_request_identity") if coverage_result_event else None
    coverage_processed_event = next(
        (
            event for event in reversed(scoped)
            if event.get("type") == "piece3_provider_work_recorded"
            and event.get("work_item_kind") == "coverage_review"
            and event.get("provider_request_identity") == coverage_request_id
        ),
        None,
    )
    coverage_commit_event = next(
        (
            event for event in reversed(scoped)
            if event.get("type") == "question_coverage_review_recorded"
            and coverage_processed_event
            and event.get("event_seq", 0) > coverage_processed_event.get("event_seq", 0)
        ),
        None,
    )
    possible_gaps: list[str] = []
    if (
        coverage_result
        and coverage_result.get("whole_check_complete") is True
        and coverage_result.get("coverage_review_complete") is True
        and isinstance(coverage_result.get("possible_gaps"), list)
    ):
        possible_gaps = [
            _human_issue_key(item.get("issue_key") or item.get("gap_key"))
            for item in coverage_result["possible_gaps"]
            if isinstance(item, dict) and (item.get("issue_key") or item.get("gap_key"))
        ]

    current_kind = provider.get("provider_kind") if provider else None
    current_is_validation = current_kind == "gpt_question_validation"
    current_is_coverage = current_kind == "gpt_question_coverage_review"
    current_blocked = bool(provider and not provider_alive)
    current_validation_after_coverage = bool(
        current_is_validation
        and coverage_processed_event
        and provider
        and provider.get("event_seq", 0) > coverage_processed_event.get("event_seq", 0)
    )
    coverage_after_validation = bool(
        latest_validation
        and coverage_result_event
        and coverage_result_event.get("event_seq", 0) > latest_validation.get("event_seq", 0)
    )

    if needs_ness_now:
        reason = "N.H has reached the durable Ness-decision boundary. The questions are ready to be asked."
    elif external_action_blocker:
        reason = external_action_blocker
    elif worker_blocker:
        reason = worker_blocker
    elif restart_required and provider_alive:
        reason = "The current provider step must finish normally. After it is durable, the older-controller worker must retire before a fresh worker can continue question preparation."
    elif restart_required:
        reason = "The running worker belongs to an older controller version. It must retire and release its lease before a fresh worker can continue question preparation."
    elif current_blocked:
        reason = "The recorded provider request is open, but its exact process is not alive. Question preparation is mechanically blocked until N.H reconciles it."
    elif current_is_coverage and provider_alive:
        prefix = f"The latest validated set contains {validated_count} questions, but " if validated_count is not None else ""
        reason = prefix + "Codex is still checking whether any genuine question areas are missing. N.H cannot ask Ness until that result is saved, processed, and clears the coverage gate."
    elif current_is_validation and provider_alive:
        reason = "Codex is validating the current possible questions. N.H cannot ask Ness until validation is recorded and the independent coverage gate also clears."
    elif pending_result:
        reason = "The provider result is safely saved, but N.H must process and record what it proves before the questions can be released."
    elif coverage_processed_event and not coverage_commit_event:
        gap_text = f" The review found {len(possible_gaps)} possible gap groups." if possible_gaps else ""
        reason = f"The coverage result was processed at event {coverage_processed_event.get('event_seq')}, but its finding is not yet durably committed.{gap_text} N.H cannot decide the next question gate until that recording completes."
    elif latest_validation and not coverage_after_validation:
        reason = "Question validation is recorded, but the required independent coverage review has not yet cleared this validated set."
    else:
        reason = "The authenticated journal does not yet prove that every required question-preparation gate has cleared."

    validation_status = "DONE" if latest_validation else "WAITING"
    validation_detail = "No validated question set is recorded yet."
    if latest_validation:
        validation_detail = f"Recorded at journal event {latest_validation.get('event_seq')}."
        if validated_count is not None:
            validation_detail += f" The authenticated result proves {validated_count} validated questions."
    if current_is_validation:
        validation_status = "BLOCKED" if current_blocked else "WORKING NOW"
        validation_detail = "Codex is validating the possible questions now." if not current_blocked else "The validation request is open, but its recorded provider process is not alive."

    coverage_status = "DONE" if coverage_after_validation else "WAITING"
    coverage_detail = (
        f"The coverage result entered durable custody at event {coverage_result_event.get('event_seq')}."
        if coverage_after_validation and coverage_result_event
        else "Independent coverage must check the latest validated question set."
    )
    if current_is_coverage:
        coverage_status = "BLOCKED" if current_blocked else "WORKING NOW"
        coverage_detail = "Codex is checking the latest validated set for missing genuine question areas." if not current_blocked else "The coverage request is open, but its recorded provider process is not alive."

    processing_status = "WAITING"
    processing_detail = "Depends on the current review result."
    if pending_result:
        processing_status = "WORKING NOW" if lease_current else "BLOCKED"
        processing_detail = "The result is saved and local N.H is processing it." if lease_current else "The result is saved, but no current live worker is proved to process it."
    elif needs_ness_now or coverage_processed_event:
        processing_status = "DONE"
        processing_detail = "The latest required review result was saved and processed."

    recording_status = "WAITING"
    recording_detail = "Depends on the current review result."
    if current_validation_after_coverage:
        recording_status = "DONE"
        recording_detail = f"N.H durably advanced from the processed coverage finding into the current validation request at event {provider.get('event_seq')}."
    elif coverage_commit_event:
        recording_status = "DONE"
        recording_detail = f"The coverage finding was durably recorded at event {coverage_commit_event.get('event_seq')}."
    elif coverage_processed_event:
        recording_status = "WORKING NOW" if lease_current else "BLOCKED"
        recording_detail = "Local N.H is durably recording the processed coverage finding." if lease_current else "The processed finding is ready, but no live worker is proved to record it."

    steps = [
        {"name": "Validate the possible questions", "status": validation_status, "detail": validation_detail},
        {"name": "Run the independent coverage review", "status": coverage_status, "detail": coverage_detail},
        {"name": "Save and process the current review result", "status": processing_status, "detail": processing_detail},
        {"name": "Durably record the coverage finding", "status": recording_status, "detail": recording_detail},
        {"name": "Resolve only genuinely missing question areas", "status": "CONDITIONAL", "detail": "Only required if a current or later review proves a real new gap."},
        {"name": "Reach the durable Ness-question-ready boundary", "status": "DONE" if needs_ness_now else "WAITING", "detail": "The durable boundary is recorded." if needs_ness_now else "N.H must durably prove that validation and coverage are complete."},
        {"name": "Ask Ness the genuine questions", "status": "READY" if needs_ness_now else "FINAL", "detail": "READY — N.H can ask Ness now." if needs_ness_now else "This is the final step after the durable question-ready boundary."},
    ]
    if current_validation_after_coverage:
        steps[0]["name"] = "Targeted validation unlocked by the last coverage finding"
        steps[1]["name"] = "Previous independent coverage review"
        steps.insert(
            4,
            {
                "name": "Check the updated question set for complete coverage",
                "status": "WAITING",
                "detail": "This depends on the current validation result. It is required only after that updated set is safely recorded.",
            },
        )
    if restart_required:
        steps.insert(
            0,
            {
                "name": "Recover from the controller change",
                "status": "WAITING" if provider_alive else "BLOCKED",
                "detail": (
                    "The current provider step is allowed to finish; then the old worker must retire without dispatching another operation."
                    if provider_alive
                    else "RESTART REQUIRED — the running worker belongs to an older controller version and must release its lease before a fresh worker starts."
                ),
            },
        )
    elif worker_blocker:
        steps.insert(
            0,
            {
                "name": "Recover the local N.H worker",
                "status": "BLOCKED",
                "detail": worker_blocker,
            },
        )
    if external_action_blocker:
        steps.insert(
            0,
            {
                "name": "Resolve the recorded durable external action",
                "status": "BLOCKED",
                "detail": external_action_blocker,
            },
        )

    if needs_ness_now:
        final_line = "Questions can be asked when: now — the durable Ness-question boundary is proved."
    elif external_action_blocker:
        final_line = (
            "Questions can be asked when: the recorded durable external action is resolved through the "
            "normal N.H external-action path — resuming a worker alone cannot cross this boundary — and "
            "only then can the remaining authenticated question gates finish and N.H reach the durable "
            "Ness-question-ready boundary."
        )
    elif restart_required:
        final_line = "Questions can be asked when: the older-controller worker has safely retired, one fresh current worker finishes the remaining authenticated question gates, and N.H reaches the durable Ness-question-ready boundary."
    elif worker_blocker:
        final_line = "Questions can be asked when: the recorded worker/recovery blocker is cleared safely, the remaining authenticated question gates finish, and N.H reaches the durable Ness-question-ready boundary."
    else:
        final_line = "Questions can be asked when: the current review is safely saved, processed, and durably recorded; any genuinely new gaps are resolved if the recorded finding requires it; and N.H reaches the durable Ness-question-ready boundary."

    gap_note = None
    if possible_gaps and coverage_result_event:
        if latest_validation and coverage_result_event.get("event_seq", 0) < latest_validation.get("event_seq", 0):
            gap_note = (
                f"The previous completed coverage result at event {coverage_result_event.get('event_seq')} "
                f"proved {len(possible_gaps)} possible gap groups. A later validation ran, so a subsequent "
                "coverage review must check whether they were resolved; this page does not assume they still remain."
            )
        elif current_validation_after_coverage:
            gap_note = (
                f"The latest completed coverage result at event {coverage_result_event.get('event_seq')} "
                f"proved {len(possible_gaps)} possible gap groups and was processed at event "
                f"{coverage_processed_event.get('event_seq')}. The current validation is checking the work "
                "unlocked by that finding; this page does not assume all groups still remain."
            )
        elif coverage_processed_event and not coverage_commit_event:
            gap_note = (
                f"The latest completed coverage result at event {coverage_result_event.get('event_seq')} "
                f"proved {len(possible_gaps)} possible gap groups and was processed at event "
                f"{coverage_processed_event.get('event_seq')}. Its finding is awaiting durable recording, "
                "so the next path still depends on that recorded result."
            )
        else:
            gap_note = (
                f"The latest completed coverage result at event {coverage_result_event.get('event_seq')} "
                f"proved {len(possible_gaps)} possible gap groups. N.H must process that result before it can "
                "determine which genuinely remain and what work, if any, they require."
            )
    result = {
        "reason_not_ready": reason,
        "steps": steps,
        "validated_question_count": validated_count,
        "validated_question_count_event": validation_result_event.get("event_seq") if validated_count is not None and validation_result_event else None,
        "provisional_question_count": provisional_count,
        "provisional_question_count_event": provisional_count_event,
        "previous_possible_gap_count": len(possible_gaps) if possible_gaps else None,
        "previous_possible_gap_event": coverage_result_event.get("event_seq") if possible_gaps and coverage_result_event else None,
        "previous_possible_gap_groups": possible_gaps,
        "possible_gap_note": gap_note,
        "coverage_complete": needs_ness_now,
        "ness_question_ready_record_exists": needs_ness_now,
        "questions_can_be_asked_when": final_line,
    }
    return result


def project_progress(
    events: list[dict[str, Any]],
    lease: dict[str, Any],
    plan_text: str,
    alive: Callable[[Any, Any, Any], bool] = exact_process_alive,
    elapsed: Callable[[Any, Any, Any], int | None] = process_elapsed_seconds,
    installed_controller_identity: str | None = None,
    worker_health: dict[str, Any] | None = None,
    maintenance_pause: dict[str, Any] | None = None,
) -> dict[str, Any]:
    latest = events[-1] if events else {}
    package = _latest_package(events)
    requests = _provider_requests(events)
    dispatched = [record for record in requests.values() if record.get("dispatch")]
    dispatched.sort(key=lambda item: item["dispatch"].get("event_seq", 0), reverse=True)
    latest_request = dispatched[0] if dispatched else {}
    provider = (
        latest_request.get("dispatch")
        if latest_request
        and not latest_request.get("terminal")
        and not latest_request.get("reconciliation")
        else None
    )
    processed_request_ids = {
        event.get("provider_request_identity")
        for event in events
        if event.get("type") == "piece3_provider_work_recorded"
    }
    pending_result = bool(
        latest_request.get("custody")
        and latest_request.get("dispatch", {}).get("provider_request_identity") not in processed_request_ids
    )
    operation = _active_operation(events)
    pending_authorization = _pending_authorized_event(events)

    lease_alive = alive(lease.get("pid"), lease.get("process_start_ticks"), lease.get("boot_id_sha256"))
    worker_health = worker_health or {}
    matching_health = bool(
        worker_health.get("pid") == lease.get("pid")
        and worker_health.get("run_id") == lease.get("run_id")
    )
    health_running = bool(
        matching_health
        and worker_health.get("status") == "running"
        and float(lease.get("expires_at_epoch", 0)) >= time.time()
    )
    lease_time_current = bool(
        (lease_alive or health_running)
        and float(lease.get("expires_at_epoch", 0)) >= time.time()
    )
    controller_binding_mismatch = bool(
        lease_alive
        and installed_controller_identity
        and lease.get("controller_executable_identity")
        and lease.get("controller_executable_identity")
        != installed_controller_identity
    )
    lease_current = bool(lease_time_current and not controller_binding_mismatch)
    maintenance_pause = maintenance_pause or {}
    worker_failed = bool(
        matching_health and worker_health.get("status") == "failed"
    )
    maintenance_active = maintenance_pause.get("pause_requested") is True
    worker_blocker = None
    if worker_failed:
        worker_blocker = "BLOCKED — the outer process is alive, but the real N.H work thread failed: %s" % (
            worker_health.get("detail") or "no further local work can run"
        )
        lease_current = False
    elif maintenance_active:
        worker_blocker = "MAINTENANCE PAUSE — automatic N.H scheduling is intentionally stopped."
        lease_current = False
    provider_alive = False
    worker_alive_for_seconds = (
        elapsed(lease.get("pid"), lease.get("process_start_ticks"), lease.get("boot_id_sha256"))
        if lease_alive else None
    )
    current_stage_duration_seconds: int | None = None
    current_stage_duration_basis = "not provable from the current durable record"
    actor = "Idle"
    doing = "No live N.H worker or provider is proved"
    stage = "No current work is recorded"
    next_step = "Start or recover the live loop through its normal N.H path"

    if provider:
        provider_alive = alive(
            provider.get("dispatch_pid"),
            provider.get("dispatch_process_start_ticks"),
            provider.get("dispatch_boot_id_sha256"),
        )
        # The progress view can run in a different process namespace from the
        # supervised worker.  In that case an exact PID lookup can be invisible
        # even while the matching worker is renewing its short lease.  A fresh,
        # matching running-health record is therefore also valid display-only
        # evidence that the currently open provider operation is still active.
        if not provider_alive and health_running and operation is not None:
            provider_alive = (
                provider.get("supervisor_operation_id")
                == operation.get("supervisor_operation_id")
            )
        label = PROVIDER_LABELS.get(provider.get("provider_endpoint_identity"), "Provider")
        work = WORK_LABELS.get(provider.get("provider_kind"), "performing the recorded provider task")
        if provider_alive:
            actor = label
            doing = "Provider is actively running"
            stage = f"Waiting for {label}"
            next_step = (
                "N.H will durably capture the provider exit/result and process it "
                f"when {label} finishes."
            )
            current_stage_duration_seconds = elapsed(
                provider.get("dispatch_pid"),
                provider.get("dispatch_process_start_ticks"),
                provider.get("dispatch_boot_id_sha256"),
            )
            if current_stage_duration_seconds is not None:
                current_stage_duration_basis = "current provider stage, from its exact recorded process identity"
        else:
            actor = "N.H recovery"
            doing = f"The {label} request is open, but its recorded process is not alive"
            stage = "Open provider request needs reconciliation"
            next_step = "N.H must use its normal recovery path before retrying"
    elif worker_failed:
        actor = "N.H recovery"
        doing = worker_blocker
        stage = "Work-thread recovery required"
        next_step = "Recover through the normal single-worker path; do not rerun saved provider work"
    elif maintenance_active:
        actor = "Paused"
        doing = worker_blocker
        stage = "Safe maintenance pause"
        next_step = "Resume with exactly one worker after maintenance is complete"
    elif controller_binding_mismatch:
        actor = "N.H recovery"
        doing = "RESTART REQUIRED — the running worker belongs to an older controller version"
        stage = "Controller-change recovery required"
        next_step = "The old worker must retire and release its lease before one fresh current worker starts"
    elif pending_result and lease_current:
        actor = "Local N.H"
        doing = "A provider result is safely saved and ready for local processing"
        stage = "Provider result saved"
        next_step = "Local N.H will process the already-saved result"
    elif pending_result:
        actor = "Idle"
        doing = "A provider result is safely saved, but no live worker is proved"
        stage = "Provider result saved"
        next_step = "A normal N.H worker can process the already-saved result"
    elif pending_authorization and lease_current:
        authorized_type = pending_authorization.get("authorizes_event_type")
        actor = "Local N.H"
        doing = "recording the processed coverage finding" if authorized_type == "question_coverage_review_recorded" else "recording the processed question result"
        stage = "Durable question-gate recording"
        next_step = f"Durably record {authorized_type}"
    elif pending_authorization:
        actor = "Idle"
        doing = "A processed question result is ready to be recorded, but no live worker is proved"
        stage = "Question-gate recording is waiting"
        next_step = f"A normal N.H worker must record {pending_authorization.get('authorizes_event_type')}"
    elif operation and lease_current:
        command = operation.get("supervisor_command")
        actor = "Local N.H"
        doing = COMMAND_LABELS.get(command, f"running {command or 'the current local operation'}")
        stage = "Local N.H work"
        next_step = "Finish and durably record the current local operation"
    elif lease_current:
        actor = "Local N.H"
        doing = "The live worker owns the loop and is preparing the next durable step"
        stage = "Local N.H work"
        next_step = "The next step will appear when N.H records it"
    elif operation:
        actor = "N.H recovery"
        command = operation.get("supervisor_command")
        doing = f"An unfinished local operation is recorded: {command}"
        stage = "Recorded operation has no proved live worker"
        next_step = "N.H must reconcile it through the normal recovery path"

    needs_text, needs_flag, needs_kind, needs_action_code = _needs_ness(events)
    # An older unresolved provider outcome or external action may remain durably recorded while
    # the controller has already moved on to a newer, proved-live provider
    # operation.  That older item is still pending recovery, but it is not the
    # current stage and must not make the live progress view say the whole loop
    # is stopped.
    if provider_alive and needs_kind in {"provider_reconciliation", "external_action"}:
        needs_text = "No current request for Ness — an earlier blocked item remains queued for recovery"
        needs_flag = False
        needs_kind = None
        needs_action_code = None
    question_ready = needs_kind == "question"
    external_action_blocker = None
    if needs_kind == "external_action":
        external_action_blocker = (
            "BLOCKED — N.H is stopped at a durable external-action boundary "
            f"({needs_action_code or 'external action required'}). That recorded action must be "
            "resolved through the normal N.H path; resuming a worker alone cannot cross this boundary."
        )
    if needs_kind == "provider_reconciliation":
        actor = "Waiting for Ness"
        doing = "N.H cannot prove the outcome of the launched provider request and will not duplicate it"
        stage = "Provider outcome reconciliation stopped"
        next_step = "N.H remains stopped until the exact uncertain request is resolved"
    elif needs_kind == "external_action":
        actor = "Waiting for Ness"
        doing = "A durable external-action boundary is recorded"
        stage = "External action required"
        next_step = "N.H remains stopped until the recorded action is resolved"
        if maintenance_active:
            doing = (
                "A durable external-action boundary is recorded; the safe maintenance pause "
                "is also active"
            )
            stage = "External action required — safe maintenance pause also active"
            next_step = (
                "N.H remains stopped until the recorded external action is resolved; resuming "
                "one worker after maintenance is not sufficient on its own"
            )
    result = {
        "bundle": bundle_for(package, plan_text),
        "package": package or "Not yet recorded",
        "stage": stage,
        "latest_event": latest.get("event_seq"),
        "latest_event_type": latest.get("type"),
        "actor": actor,
        "doing": doing,
        "needs_ness": needs_text,
        "needs_ness_now": needs_flag,
        "needs_ness_kind": needs_kind,
        "next": next_step,
        "worker_alive_for_seconds": worker_alive_for_seconds,
        "worker_alive_for_basis": "exact recorded worker process identity" if worker_alive_for_seconds is not None else "no live worker lifetime is proved",
        "current_stage_duration_seconds": current_stage_duration_seconds,
        "current_stage_duration_basis": current_stage_duration_basis,
        "worker_alive": lease_alive,
        "worker_lease_current": lease_current,
        "worker_controller_binding_current": not controller_binding_mismatch,
        "worker_restart_required": controller_binding_mismatch,
        "worker_thread_failed": worker_failed,
        "maintenance_pause_active": maintenance_active,
        "provider_alive": provider_alive,
        "provider_request_open": bool(provider),
        "bundle_seven_progress": bundle_seven_progress(events),
        "live_activity": bundle_seven_live_activity(events, package),
    }
    result["question_path"] = question_path(
        events,
        provider,
        provider_alive,
        pending_result,
        lease_current,
        question_ready,
        controller_binding_mismatch,
        (
            "BLOCKED — N.H is waiting at the durable provider-outcome reconciliation boundary."
            if needs_kind == "provider_reconciliation"
            else worker_blocker
        ),
        external_action_blocker,
    )
    return result


def bundle_seven_live_activity(
    events: list[dict[str, Any]], package_id: str | None
) -> dict[str, Any] | None:
    """Expose assigned sources and durable milestones, never model reasoning."""
    if not package_id:
        return None
    baseline = next(
        (event for event in reversed(events)
         if event.get("type") == "bundle_seven_baseline_recorded"),
        None,
    )
    package_record = next(
        (item for item in (baseline or {}).get("package_inventory", [])
         if item.get("package_id") == package_id),
        {},
    )
    labels = {
        "supervisor_operation_started": "Local step started",
        "provider_request_prepared": "External review prepared",
        "provider_dispatch_begun": "External reviewer started",
        "provider_result_custody_recorded": "Result received and preserved",
        "provider_request_terminal_recorded": "External review finished",
        "supervisor_operation_completed": "Local step completed",
        "piece3_provider_work_recorded": "Result passed local checks",
        "validation_recorded": "Package result saved",
    }
    timeline = [
        {"event": event.get("event_seq"), "label": labels[event.get("type")]}
        for event in events
        if event.get("package_id") == package_id and event.get("type") in labels
    ][-10:]
    return {
        "package_id": package_id,
        "package_title": package_record.get("package_title"),
        "assigned_source_paths": list(package_record.get("source_paths") or []),
        "focus_areas": list(package_record.get("still_open") or []),
        "timeline": timeline,
        "visibility_note": (
            "Shows assigned sources and recorded milestones. It cannot show "
            "private model reasoning or the exact sentence being read now."
        ),
    }


def bundle_seven_progress(events: list[dict[str, Any]]) -> dict[str, Any] | None:
    """Project only durable, package-level progress after the latest baseline."""
    baselines = [
        event
        for event in events
        if event.get("type") == "bundle_seven_baseline_recorded"
        and isinstance(event.get("package_inventory"), list)
    ]
    if not baselines:
        return None
    baseline = baselines[-1]
    baseline_seq = int(baseline.get("event_seq") or 0)
    package_ids = [
        item.get("package_id")
        for item in baseline["package_inventory"]
        if isinstance(item, dict) and isinstance(item.get("package_id"), str)
    ]
    package_ids = list(dict.fromkeys(package_ids))
    if not package_ids:
        return None
    validation_sets: dict[str, dict[str, Any]] = {}
    for event in events:
        if (
            event.get("type") != "validation_recorded"
            or int(event.get("event_seq") or 0) <= baseline_seq
            or event.get("package_scope_id") not in package_ids
            or not isinstance(event.get("validation_set_id"), str)
        ):
            continue
        record = validation_sets.setdefault(
            event["validation_set_id"],
            {
                "package_scope_id": event.get("package_scope_id"),
                "page_count": event.get("page_count"),
                "pages": set(),
                "enumeration_complete": False,
            },
        )
        if record["page_count"] != event.get("page_count"):
            continue
        if isinstance(event.get("page_index"), int):
            record["pages"].add(event["page_index"])
        if event.get("enumeration_complete") is True:
            record["enumeration_complete"] = True
    completed = {
        record["package_scope_id"]
        for record in validation_sets.values()
        if isinstance(record["page_count"], int)
        and record["page_count"] > 0
        and record["pages"] == set(range(1, record["page_count"] + 1))
        and record["enumeration_complete"]
    }
    total = len(package_ids)
    done = len(completed)
    return {
        "completed": done,
        "total": total,
        "percent": (done * 100) // total,
        "remaining": total - done,
    }


HTML = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>N.H Live Progress</title>
<style>
:root{color-scheme:dark;--bg:#090d12;--panel:#111822;--line:#253142;--text:#edf4ff;--muted:#94a5b9;--cyan:#63d9ff;--green:#64e3ae;--amber:#ffc66d}
*{box-sizing:border-box}body{margin:0;background:radial-gradient(circle at 20% 0,#122334 0,var(--bg) 42%);font:16px/1.45 system-ui,sans-serif;color:var(--text)}
main{max-width:1050px;margin:auto;padding:32px 20px 60px}header{display:flex;gap:16px;align-items:center;justify-content:space-between;margin-bottom:24px}h1{font-size:24px;margin:0}.live{color:var(--green);font-size:14px}.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}.card{background:color-mix(in srgb,var(--panel) 94%,transparent);border:1px solid var(--line);border-radius:14px;padding:17px 18px;min-height:100px}.wide{grid-column:1/-1}.label{color:var(--muted);text-transform:uppercase;letter-spacing:.08em;font-size:12px;margin-bottom:8px}.value{font-size:19px;font-weight:650;overflow-wrap:anywhere}.detail{color:var(--muted);font-size:13px;margin-top:7px}.working{color:var(--cyan)}.needed{color:var(--amber)}footer{color:var(--muted);font-size:12px;margin-top:18px}.error{color:#ff8d8d}.pulse{width:8px;height:8px;border-radius:50%;display:inline-block;background:var(--green);margin-right:7px;box-shadow:0 0 12px var(--green)}
.path{margin-top:24px;border-color:#3b6078}.path h2{font-size:21px;margin:0 0 6px;letter-spacing:.05em;color:var(--cyan)}.reason{color:var(--text);margin:18px 0;padding:13px;background:#0b121b;border-left:3px solid var(--amber)}.steps{display:grid;gap:10px}.step{display:grid;grid-template-columns:minmax(190px,1fr) minmax(170px,auto);gap:8px 16px;padding:13px 0;border-top:1px solid var(--line)}.step-name{font-weight:650}.status{justify-self:end;border:1px solid var(--line);border-radius:999px;padding:3px 9px;font-size:11px;font-weight:750;letter-spacing:.04em}.status.done{color:var(--green)}.status.working-now{color:var(--cyan)}.status.blocked{color:#ff8d8d}.status.conditional,.status.final{color:var(--amber)}.status.ready{color:var(--green);border-color:var(--green)}.step-detail{grid-column:1/-1;color:var(--muted);font-size:13px}.counts{display:flex;gap:12px;flex-wrap:wrap;margin:16px 0}.count{background:#0b121b;border:1px solid var(--line);border-radius:10px;padding:9px 12px}.gaps{color:var(--muted);font-size:13px}.final-line{margin-top:17px;padding:14px;border-left:3px solid var(--cyan);background:#0b121b;font-weight:650}.bundle-progress{margin:0 0 24px}.bar-track{height:18px;background:#0b121b;border:1px solid var(--line);border-radius:999px;overflow:hidden}.bar-fill{height:100%;width:0;background:linear-gradient(90deg,var(--cyan),var(--green));transition:width .35s ease}.bar-line{display:flex;justify-content:space-between;gap:12px;margin-bottom:10px}.bar-count{font-size:20px;font-weight:750}.bar-percent{color:var(--cyan);font-size:20px;font-weight:750}
@media(max-width:650px){.grid{grid-template-columns:1fr}.wide{grid-column:auto}header{align-items:flex-start;flex-direction:column}}
</style></head><body><main>
<header><div><h1>N.H Live Progress</h1><div class="detail">Independent read-only view</div></div><div class="live"><span class="pulse"></span><span id="connection">Connecting…</span></div></header>
<section class="card bundle-progress" id="bundleSevenProgress" hidden><div class="label">Bundle 7 progress</div><div class="bar-line"><span class="bar-count" id="bundleSevenCount">0 of 10 complete</span><span class="bar-percent" id="bundleSevenPercent">0%</span></div><div class="bar-track" role="progressbar" aria-label="Bundle 7 progress" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" id="bundleSevenBar"><div class="bar-fill" id="bundleSevenFill"></div></div><div class="detail" id="bundleSevenRemaining">10 parts remain</div></section>
<section class="grid">
<div class="card"><div class="label">Bundle</div><div class="value" id="bundle">—</div></div>
<div class="card"><div class="label">Package</div><div class="value" id="package">—</div></div>
<div class="card wide"><div class="label">Current stage</div><div class="value working" id="stage">—</div></div>
<div class="card"><div class="label">Who is working</div><div class="value" id="actor">—</div><div class="detail" id="doing">—</div></div>
<div class="card"><div class="label">Worker alive for</div><div class="value" id="workerAliveFor">Not available</div><div class="detail" id="workerAliveBasis">—</div></div>
<div class="card"><div class="label">Current stage duration</div><div class="value" id="stageDuration">Not available</div><div class="detail" id="stageDurationBasis">—</div></div>
<div class="card"><div class="label">Latest journal event</div><div class="value" id="event">—</div><div class="detail" id="eventType">—</div></div>
<div class="card"><div class="label">Does N.H need Ness?</div><div class="value" id="needs">—</div></div>
<div class="card wide"><div class="label">What comes next</div><div class="value" id="next">—</div></div>
</section>
<section class="card path" id="questionPath"><h2>PATH TO YOUR QUESTIONS</h2><div class="detail">What still has to happen before N.H is allowed to ask you this package's questions?</div><div class="reason" id="pathReason">Why you are not being asked yet: —</div><div class="counts" id="pathCounts"></div><div class="steps" id="pathSteps"></div><div class="gaps" id="pathGaps"></div><div class="final-line" id="pathFinal">Questions can be asked when: —</div></section>
<footer><span id="updated">Not updated yet</span> · This page never operates the loop, calls a provider, or acquires the worker lease. Bundle 7 percentage counts only durably completed parts.</footer>
</main><script>
const ids=["bundle","package","stage","actor","doing","next"];
let refreshing=false;
function duration(seconds){if(seconds===null||seconds===undefined)return "Not available";const h=Math.floor(seconds/3600),m=Math.floor((seconds%3600)/60),s=seconds%60;return h?`${h}h ${m}m ${s}s`:m?`${m}m ${s}s`:`${s}s`}
function addCount(parent,text){const item=document.createElement("div");item.className="count";item.textContent=text;parent.append(item)}
function showQuestionPath(path){document.getElementById("pathReason").textContent=`Why you are not being asked yet: ${path.reason_not_ready}`;const counts=document.getElementById("pathCounts");counts.replaceChildren();if(path.provisional_question_count!==null)addCount(counts,`Provisional questions: ${path.provisional_question_count} (event ${path.provisional_question_count_event})`);if(path.validated_question_count!==null)addCount(counts,`Validated questions: ${path.validated_question_count} (event ${path.validated_question_count_event})`);addCount(counts,`Coverage complete: ${path.coverage_complete?"YES":"NO"}`);addCount(counts,`Ness-question-ready record: ${path.ness_question_ready_record_exists?"YES":"NO"}`);if(path.previous_possible_gap_count!==null)addCount(counts,`Latest proved possible gap groups: ${path.previous_possible_gap_count} (event ${path.previous_possible_gap_event})`);const steps=document.getElementById("pathSteps");steps.replaceChildren();path.steps.forEach(value=>{const row=document.createElement("div");row.className="step";const name=document.createElement("div");name.className="step-name";name.textContent=value.name;const status=document.createElement("div");status.className=`status ${value.status.toLowerCase().replaceAll(" ","-")}`;status.textContent=value.status;const detail=document.createElement("div");detail.className="step-detail";detail.textContent=value.detail;row.append(name,status,detail);steps.append(row)});const gaps=document.getElementById("pathGaps");gaps.replaceChildren();if(path.possible_gap_note){const note=document.createElement("p");note.textContent=path.possible_gap_note;gaps.append(note);const list=document.createElement("ul");path.previous_possible_gap_groups.forEach(value=>{const item=document.createElement("li");item.textContent=value;list.append(item)});gaps.append(list)}document.getElementById("pathFinal").textContent=path.questions_can_be_asked_when}
function showBundleSevenProgress(p){const card=document.getElementById("bundleSevenProgress");card.hidden=!p;if(!p)return;document.getElementById("bundleSevenCount").textContent=`${p.completed} of ${p.total} complete`;document.getElementById("bundleSevenPercent").textContent=`${p.percent}%`;document.getElementById("bundleSevenRemaining").textContent=`${p.remaining} parts remain`;const bar=document.getElementById("bundleSevenBar");bar.setAttribute("aria-valuenow",p.percent);document.getElementById("bundleSevenFill").style.width=`${p.percent}%`}
async function refresh(){if(refreshing)return;refreshing=true;try{const response=await fetch("/api/progress",{cache:"no-store"});const d=await response.json();if(!response.ok)throw new Error(d.error||"unavailable");ids.forEach(id=>document.getElementById(id).textContent=d[id]??"—");document.getElementById("event").textContent=d.latest_event??"—";document.getElementById("eventType").textContent=d.latest_event_type??"—";document.getElementById("needs").textContent=d.needs_ness;document.getElementById("needs").className="value "+(d.needs_ness_now?"needed":"");document.getElementById("workerAliveFor").textContent=duration(d.worker_alive_for_seconds);document.getElementById("workerAliveBasis").textContent=d.worker_alive_for_basis;document.getElementById("stageDuration").textContent=duration(d.current_stage_duration_seconds);document.getElementById("stageDurationBasis").textContent=d.current_stage_duration_basis;showBundleSevenProgress(d.bundle_seven_progress);showQuestionPath(d.question_path);document.getElementById("connection").textContent="Updating automatically";document.getElementById("updated").textContent=`Updated ${new Date().toLocaleTimeString()}`;}catch(error){document.getElementById("connection").textContent="Progress data unavailable";document.getElementById("connection").className="error";}finally{refreshing=false}}
refresh();setInterval(refresh,2000);
</script></body></html>'''


class ProgressApplication:
    def __init__(self, journal: Path = JOURNAL, lease: Path = LEASE, plan: Path = PLAN,
                 auth_key: Path | None = AUTH_KEY, worker_health: Path = WORKER_HEALTH,
                 maintenance_pause: Path = MAINTENANCE_PAUSE):
        self.journal = JournalTail(journal, auth_key)
        self.lease_path = lease
        self.plan_text = plan.read_text()
        self.controller_identity = ControllerIdentityReader()
        self.worker_health_path = worker_health
        self.maintenance_pause_path = maintenance_pause

    def progress(self) -> tuple[dict[str, Any], int]:
        events, error = self.journal.read()
        if not events:
            return {"error": error or "No journal events are available"}, 503
        result = project_progress(
            events,
            _read_json(self.lease_path),
            self.plan_text,
            installed_controller_identity=self.controller_identity.read(),
            worker_health=_read_json(self.worker_health_path),
            maintenance_pause=_read_json(self.maintenance_pause_path),
        )
        result["journal_chain_ok"] = error is None
        result["journal_authentication_ok"] = error is None
        result["authenticated_event_seq"] = events[-1].get("event_seq") if error is None else None
        result["journal_error"] = error
        result["read_only"] = True
        result["controller_calls"] = 0
        result["generated_at_epoch"] = int(time.time())
        return result, 200


def make_handler(app: ProgressApplication) -> type[BaseHTTPRequestHandler]:
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:  # noqa: N802
            request_path = urlsplit(self.path).path
            if request_path in {"/", "/index.html", "/questions"}:
                self._send(200, "text/html; charset=utf-8", HTML.encode())
            elif request_path == "/api/progress":
                data, status = app.progress()
                self._send(status, "application/json", json.dumps(data).encode())
            elif request_path == "/api/health":
                self._send(200, "application/json", b'{"ok":true,"read_only":true,"controller_calls":0}')
            elif request_path == "/favicon.ico":
                self._send(204, "image/x-icon", b"")
            else:
                self._send(404, "application/json", b'{"error":"not found"}')

        def do_POST(self) -> None:  # noqa: N802
            self._send(405, "application/json", b'{"error":"read-only"}')

        do_PUT = do_POST
        do_PATCH = do_POST
        do_DELETE = do_POST

        def _send(self, status: int, content_type: str, body: bytes) -> None:
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, _format: str, *args: Any) -> None:
            return

    return Handler


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=42800)
    parser.add_argument("--no-open", action="store_true", help="accepted for service-launch compatibility")
    args = parser.parse_args()
    app = ProgressApplication()
    server = ThreadingHTTPServer((args.host, args.port), make_handler(app))
    print(f"N.H read-only progress view: http://{args.host}:{args.port}/", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()

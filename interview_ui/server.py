#!/usr/bin/env python3
"""Local browser interface for the N.H design interview.

The UI deliberately does not implement a second question system. It invokes the
existing controller commands, renders their controller-owned question forms, and
submits the exact answer envelope the controller already validates.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import threading
import time
import webbrowser
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Callable
from urllib.parse import urlparse

import supervisor


APP_DIR = Path(__file__).resolve().parent
ROOT_DIR = APP_DIR.parent
CONTROLLER_PATH = ROOT_DIR / "controller" / "nh_loop.py"
INTERVIEW_JOURNAL = ROOT_DIR / "nh_interview_state" / "nh_interview_journal.jsonl"
# SECTION 15. The private operational journal is an observation/recovery log.
# The browser never reads it as authority for workflow state, findings, PASS,
# candidate custody, questions, or acceptance readiness, so this path is
# declared only to state that it is deliberately NOT read here.
SUPERVISOR_PRIVATE_JOURNAL_NEVER_READ_AS_AUTHORITY = (
    APP_DIR / ".nh_supervisor_state" / "supervisor_events.jsonl"
)
STATIC_DIR = APP_DIR / "static"
MAX_REQUEST_BYTES = 32_768
CONTROLLER_TIMEOUT_SECONDS = 180

# The ordinary installation path remains the controller subprocess above.  A
# disposable rehearsal may explicitly inject one in-process controller runner
# and one journal path.  Once injected, refusal is final: run_controller never
# falls through to nh_loop.py, another credential store, or another workspace.
ControllerRunner = Callable[
    [str, dict[str, Any] | None], tuple[str, dict[str, Any]]
]
_CONTROLLER_RUNNER: ControllerRunner | None = None

# Browser tabs are not controller authority.  They may share one recent,
# read-only projection so a slow authenticated replay is never duplicated just
# because an automatic refresh arrived while another refresh was still being
# built.  The lock is process-local, mutates no N.H state and launches no work.
_UI_STATE_LOCK = threading.Lock()
_UI_STATE_CACHE: dict[str, Any] | None = None
_UI_STATE_CACHE_AT = 0.0
_UI_STATE_CACHE_TTL_SECONDS = 2.0


def configure_disposable_backend(
    runner: ControllerRunner, interview_journal: Path
) -> None:
    """Bind the UI to one disposable backend, with no subprocess fallback."""
    global _CONTROLLER_RUNNER, INTERVIEW_JOURNAL
    root = ROOT_DIR.resolve()
    journal = interview_journal.resolve()
    try:
        journal.relative_to(root)
    except ValueError as exc:
        raise ValueError(
            "the disposable browser journal must remain inside the disposable tree"
        ) from exc
    _CONTROLLER_RUNNER = runner
    INTERVIEW_JOURNAL = journal


PACKAGE_CONTEXTS = {
    "AUTHORITY_INTEGRITY_CONTROL_PLANE": {
        "plain_name": "Keeping N.H’s governing rules trustworthy",
        "technical_name": "Authority Integrity Control Plane",
        "framework": "Five Framework Capability Additions",
        "current_part": "Addition 1 of 5 — Authority Integrity Control Plane",
        "bundle": "Not decided yet",
        "purpose": (
            "Makes sure N.H checks the correct Master, decisions, and governing "
            "files before it does something—and stops if that authority cannot "
            "be trusted."
        ),
    },
}


class ControllerFailure(RuntimeError):
    def __init__(self, message: str, report: dict[str, Any] | None = None):
        super().__init__(message)
        self.report = report or {}


def parse_controller_report(output: str) -> dict[str, Any]:
    """Return the final JSON object emitted by an N.H controller command."""
    starts = [match.start() + 1 for match in re.finditer(r"\n\{", output)]
    if output.startswith("{"):
        starts.insert(0, 0)
    for start in reversed(starts):
        candidate = output[start:].strip()
        try:
            value = json.loads(candidate)
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            return value
    raise ControllerFailure("The N.H controller did not return its structured report.")


def controller_text_before_report(output: str) -> str:
    starts = [match.start() + 1 for match in re.finditer(r"\n\{", output)]
    for start in reversed(starts):
        try:
            value = json.loads(output[start:].strip())
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            return output[: start - 1]
    return output


def run_controller(
    command: str, payload: dict[str, Any] | None = None
) -> tuple[str, dict[str, Any]]:
    if _CONTROLLER_RUNNER is not None:
        # Deliberately no exception fallback.  The configured disposable
        # backend either answers this call or the browser fails closed.
        return _CONTROLLER_RUNNER(command, payload)
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    stdin = None if payload is None else json.dumps(payload, ensure_ascii=False)
    try:
        completed = subprocess.run(
            [sys.executable, "-B", str(CONTROLLER_PATH), command],
            cwd=str(CONTROLLER_PATH.parent),
            env=env,
            input=stdin,
            text=True,
            capture_output=True,
            timeout=CONTROLLER_TIMEOUT_SECONDS,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise ControllerFailure(
            "N.H took too long to answer. Nothing was assumed or submitted."
        ) from exc

    output = completed.stdout
    report = parse_controller_report(output)
    if completed.returncode != 0 or not report.get("ok"):
        errors = report.get("errors") or []
        message = errors[0] if errors else "The N.H controller refused this action safely."
        raise ControllerFailure(message, report)
    return output, report


def _controller_event_digest(event: dict[str, Any]) -> str:
    body = {key: value for key, value in event.items() if key != "event_sha256"}
    canonical = json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def read_journal_summaries(status: dict[str, Any]) -> list[dict[str, Any]]:
    """Read context only when it is the exact history the controller authenticated.

    ``interview-status`` verifies the HMAC key internally and returns the event
    count and tail. The UI then rechecks sequence, ordinary hash links/digests,
    count, and tail over the bytes it actually read. A rewrite between those two
    operations is refused rather than used for package context.
    """
    events: list[dict[str, Any]] = []
    try:
        lines = INTERVIEW_JOURNAL.read_text(encoding="utf-8").splitlines()
    except OSError:
        return events
    previous = None
    expected_count = status.get("interview_events")
    expected_tail = status.get("interview_last_event_sha256")
    if not isinstance(expected_count, int) or not isinstance(expected_tail, str):
        return []
    for index, line in enumerate(lines, start=1):
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(event, dict):
            return []
        if event.get("event_seq") != index:
            return []
        if event.get("prev_event_sha256") != previous:
            return []
        observed = event.get("event_sha256")
        if not isinstance(observed, str) or observed != _controller_event_digest(event):
            return []
        previous = observed
        events.append(
            {
                "event_seq": event.get("event_seq"),
                "type": event.get("type"),
                "package_key": event.get("package_key"),
                "candidate_path": event.get("candidate_path"),
            }
        )
    if len(events) != expected_count or previous != expected_tail:
        return []
    return events


def latest_candidate_path(events: list[dict[str, Any]]) -> str | None:
    for event in reversed(events):
        candidate = event.get("candidate_path")
        if isinstance(candidate, str) and candidate.startswith("05_ACTIVE_CANDIDATE/"):
            return candidate
    return None


def readable_package_name(candidate_path: str | None, package_key: str | None) -> str:
    if candidate_path:
        stem = Path(candidate_path).stem
        stem = re.sub(r"^NH_", "", stem)
        stem = re.sub(r"_v\d+(?:_\d+)?_CANDIDATE$", "", stem)
        stem = re.sub(r"_MECHANICAL_DESIGN$", "", stem)
        return stem.replace("_", " ").title()
    if package_key and package_key != "no_controlled_id_settled_yet":
        return package_key.replace("_", " ").title()
    return "Current N.H design package"


def build_package_context(status: dict[str, Any]) -> dict[str, Any]:
    events = read_journal_summaries(status)
    candidate_path = latest_candidate_path(events)
    upper_path = (candidate_path or "").upper()
    matched = next(
        (value for key, value in PACKAGE_CONTEXTS.items() if key in upper_path), None
    )
    technical_name = readable_package_name(
        candidate_path, status.get("validation_package_key")
    )
    if matched:
        plain_name = matched["plain_name"]
        technical_name = matched["technical_name"]
        purpose = matched["purpose"]
    else:
        plain_name = f"Shaping {technical_name}"
        purpose = (
            "This part is being designed so N.H can behave consistently and "
            "safely in real use."
        )
    return {
        "plain_name": plain_name,
        "technical_name": technical_name,
        "purpose": purpose,
        "framework": matched.get("framework") if matched else None,
        "current_part": matched.get("current_part") if matched else technical_name,
        # SECTION 15. Bundle placement is UNRESOLVED and is NEVER inferred by
        # filename: for this package the source-bound value remains exactly
        # "Not decided yet". No controlled component ID or Register ID is
        # invented, assigned, derived, guessed, or slugified; both remain OPEN.
        "bundle": supervisor.BUNDLE_PLACEMENT_DISPLAY,
        "bundle_placement": "UNRESOLVED",
        "controlled_component_id": None,
        "register_id": None,
        "controlled_component_id_state": "OPEN - NONE",
        "register_id_state": "OPEN - NONE",
        "candidate_path": candidate_path,
        "candidate_filename": Path(candidate_path).name if candidate_path else None,
        "package_key": status.get("validation_package_key"),
    }


def derive_stage(
    status: dict[str, Any],
    gate: dict[str, Any],
    supervisor_snapshot: supervisor.SupervisorSnapshot | None = None,
) -> dict[str, str | bool]:
    deliverable = int(status.get("deliverable_question_count") or 0)
    open_group = status.get("open_group_index") is not None
    if (
        (deliverable or open_group)
        and supervisor_snapshot is not None
        and supervisor_snapshot.authenticated
        and supervisor_snapshot.state == supervisor.WorkflowState.NEEDS_NESS_DECISION
    ):
        return {
            "code": "waiting_for_ness",
            "label": "Waiting for your answer",
            "summary": "A genuine choice is ready for you.",
            "why": "Only this specific part still needs a choice from you.",
            "needs_ness": True,
            "tone": "needs-you",
            "attention_kind": "decision",
        }
    if supervisor_snapshot is not None:
        state = supervisor_snapshot.state
        if (
            supervisor_snapshot.authenticated
            and state in {
                supervisor.WorkflowState.WORKING,
                supervisor.WorkflowState.WAITING_RECOVERING,
            }
            and (
                supervisor_snapshot.next_command
                in {"question-validation", "question-coverage-review"}
                or (
                    state == supervisor.WorkflowState.WAITING_RECOVERING
                    and supervisor_snapshot.next_command is None
                    and supervisor_snapshot.ness_question_binding is not None
                )
            )
        ):
            check = {
                "question-validation": "question validation",
                "question-coverage-review": "independent question coverage review",
            }.get(supervisor_snapshot.next_command, "a safe retry")
            return {
                "code": "checking_possible_ness_choice",
                "label": "Checking whether a real choice is needed",
                "summary": "N.H found something that may need your judgment and is still checking it.",
                "why": "The controller is running %s. No question or answer is needed from you yet." % check,
                "needs_ness": False,
                "tone": "working",
                "attention_kind": "none",
            }
        if (
            state
            in {
                supervisor.WorkflowState.WORKING,
                supervisor.WorkflowState.DIAGNOSING,
                supervisor.WorkflowState.WAITING_RECOVERING,
            }
            and not supervisor_snapshot.live_proved
        ):
            return {
                "code": "supervisor_inactive",
                "label": supervisor_snapshot.wording.get("headline"),
                "summary": supervisor_snapshot.wording.get("detail"),
                "why": "No live automatic-supervisor lease is currently proved. This is saved history, not a claim that work is running now.",
                "needs_ness": False,
                "tone": "stopped",
                "attention_kind": "none",
            }
        if state != supervisor.WorkflowState.IDLE:
            tone = "working"
            if state == supervisor.WorkflowState.READY_FOR_ACCEPTANCE:
                tone = "needs-you"
            elif state == supervisor.WorkflowState.NEEDS_USER_ACTION:
                tone = "needs-you"
            elif state == supervisor.WorkflowState.SAFETY_HOLD:
                tone = "stopped"
            elif state == supervisor.WorkflowState.WORKING:
                tone = "clear"
            why = supervisor_snapshot.wording.get("detail") or ""
            if state in {
                supervisor.WorkflowState.WORKING,
                supervisor.WorkflowState.DIAGNOSING,
                supervisor.WorkflowState.WAITING_RECOVERING,
            }:
                why = "Nothing needs your decision right now. The mechanical workflow remains responsible for the package."
            return {
                "code": state.value.lower(),
                "label": supervisor_snapshot.wording.get("headline"),
                "summary": supervisor_snapshot.wording.get("detail"),
                "why": why,
                "needs_ness": state
                in {
                    supervisor.WorkflowState.NEEDS_NESS_DECISION,
                    supervisor.WorkflowState.NEEDS_USER_ACTION,
                    supervisor.WorkflowState.READY_FOR_ACCEPTANCE,
                },
                "tone": tone,
                "attention_kind": supervisor_snapshot.attention_kind or "none",
            }
    if status.get("revalidation_required"):
        return {
            "code": "checking_answer",
            "label": "Checking your last answer",
            "summary": "N.H is re-checking what remains open after your answer.",
            "why": "Nothing else is needed from you while that check is running.",
            "needs_ness": False,
            "tone": "working",
            "attention_kind": "none",
        }
    if int(status.get("provisional_question_count") or 0):
        return {
            "code": "coverage_review",
            "label": "Independently checking possible questions",
            "summary": "A second check is making sure no question is missing or unnecessary.",
            "why": "You will only see a question after it passes that check.",
            "needs_ness": False,
            "tone": "working",
            "attention_kind": "none",
        }
    if int(status.get("routed_issues_awaiting_validation") or 0):
        return {
            "code": "question_validation",
            "label": "Checking whether a real choice is needed",
            "summary": "N.H is separating your decisions from mechanical design work.",
            "why": "You will not be asked unless the files prove that your judgment is required.",
            "needs_ness": False,
            "tone": "working",
            "attention_kind": "none",
        }
    if gate.get("mechanical_path_unlocked"):
        return {
            "code": "mechanical_design",
            "label": "Mechanical work is ready to continue",
            "summary": "The package needs no decision from you, but no supervised run is active yet.",
            "why": "Nothing needs your decision right now. Once the automatic supervisor is installed and started, it should handle the remaining work.",
            "needs_ness": False,
            "tone": "working",
            "attention_kind": "none",
        }
    return {
        "code": "checking_current_nh",
        "label": "Checking the current N.H design",
        "summary": "N.H is working out what is already settled and what is still open.",
        "why": "You will only be interrupted if a genuine meaning or policy choice remains.",
        "needs_ness": False,
        "tone": "working",
        "attention_kind": "none",
    }


def read_supervisor_view(
    status: dict[str, Any],
    gate: dict[str, Any],
    controller_supervisor_status: dict[str, Any] | None = None,
) -> tuple[supervisor.SupervisorSnapshot, list[dict[str, Any]], dict[str, Any]]:
    # The unkeyed local worker journal is deliberately absent from this path.
    # Only supervisor-status can re-prove authenticated audit, custody, pass and
    # lease facts strongly enough for the browser to claim them.
    # SECTION 15. The browser obtains workflow state and feed cards ONLY from a
    # fresh successful supervisor-status whose authentication/source-current
    # booleans are true. It never reads the private operational journal as
    # authority, never reads the anchored provider-result store as authority, and
    # never derives a card because an unkeyed digest happens to match.
    snapshot = supervisor.snapshot_from_supervisor_status(
        controller_supervisor_status or {}
    )
    feed = supervisor.change_feed_from_supervisor_status(
        controller_supervisor_status or {}
    )
    if not snapshot.authenticated:
        return snapshot, [], {
            "ok": True,
            "controller_authenticated": False,
            "run_active": False,
            "operational_journal_used_as_authority": False,
            "private_journal_read_as_authority": False,
            "message": (
                "No authenticated supervised run is active: supervisor-status is "
                "absent, refused, stale, or unproved, so no PASS, correction, or "
                "acceptance claim is shown."
            ),
            "records": None,
        }
    return snapshot, feed, {
        "ok": True,
        "controller_authenticated": True,
        "run_active": snapshot.live_proved,
        "operational_journal_used_as_authority": False,
        "private_journal_read_as_authority": False,
        "message": None,
        "records": len(feed),
    }


def read_loop_projection(controller_supervisor_status) -> dict[str, Any]:
    """v1_8 sections 21 / 24.10 -- ONE READ-ONLY render of the loop state.

    ``loop-status`` appends nothing, writes nothing, calls no provider, creates
    no candidate and mutates no Git state, so calling it here is safe for a
    page render.  It is consulted ONLY while the current package is genuinely
    terminal-accepted; at every other time the ordinary projection governs and
    nothing about the installed page changes.

    THE ACCEPTANCE GET AND POST PATHS ARE NOT TOUCHED (INV-ACCEPT).
    """
    if not isinstance(controller_supervisor_status, dict):
        return {}
    if controller_supervisor_status.get("workflow_state") != (
        "ACCEPTED_FOR_DESIGN_ONLY"
    ):
        return {}
    if controller_supervisor_status.get("acceptance_truth") != "PROVED_ACCEPTED":
        return {}
    try:
        _output, report = run_controller("loop-status")
    except ControllerFailure:
        return {}
    if not isinstance(report, dict) or not report.get("ok"):
        return {}
    # v1_8 section 21 -- BOTH FACTS COME FROM THE CONTROLLER.  The UI does not
    # re-derive either one from a list of loop-state names: doing so claimed
    # "N.H is choosing and preparing the next design package" at the event-84
    # start position, where no Q exists and nothing is running, and it dropped
    # back to "no next package started" whenever a real Q was merely waiting.
    return {
        "loop_state": report.get("loop_state"),
        "loop_next_command": report.get("loop_next_command"),
        "loop_detail": report.get("loop_detail"),
        # A real Q transition scope exists and Q is not yet established.
        "loop_transition_exists": bool(report.get("loop_transition_exists")),
        # The loop is genuinely doing continuation work right now, which the
        # controller only asserts under a PROVED LIVE LEASE.
        "loop_transition_working": bool(report.get("loop_transition_working")),
        "loop_lease_state": report.get("loop_lease_state"),
        "loop_transition_active": bool(report.get("loop_transition_exists")),
    }


def _build_ui_state_uncached() -> dict[str, Any]:
    _, status = run_controller("interview-status")
    _, gate = run_controller("interview-gate")
    controller_supervisor_status = None
    try:
        _, controller_supervisor_status = run_controller("supervisor-status")
    except ControllerFailure:
        # Repair31 does not have this command. Absence means no authenticated
        # supervisor claim, never a reason to reinterpret the local worker log.
        controller_supervisor_status = None
    # v1_8 -- the read-only loop projection, merged onto the report the
    # snapshot is built from.  It adds loop-level fields and CHANGES NO
    # package-level field.
    loop_projection = read_loop_projection(controller_supervisor_status)
    if loop_projection and isinstance(controller_supervisor_status, dict):
        controller_supervisor_status = dict(controller_supervisor_status)
        controller_supervisor_status.update(loop_projection)
    context = build_package_context(status)
    supervisor_snapshot, change_feed, supervisor_evidence = read_supervisor_view(
        status, gate, controller_supervisor_status
    )
    stage = derive_stage(status, gate, supervisor_snapshot)
    return {
        "ok": True,
        "context": context,
        "stage": stage,
        "tabs": [
            {"id": "your_decisions", "label": "Your decisions"},
            {"id": "whats_changing", "label": "What's changing"},
            {"id": "current_status", "label": "Current status"},
            {"id": "technical_details", "label": "Technical details"},
        ],
        "supervisor": supervisor_snapshot.as_dict(),
        "supervisor_evidence": supervisor_evidence,
        # Read-only, and never a claim that the transition is progress on the
        # accepted package.
        "loop": loop_projection,
        "change_feed": change_feed,
        "change_summary": supervisor.summary_from_feed(change_feed),
        "questions": {
            "ready": int(status.get("deliverable_question_count") or 0),
            "total": int(status.get("questions_total") or 0),
            "open_group_index": status.get("open_group_index"),
            "pending_total": int(status.get("pending_askable_total") or 0),
            "provisional": int(status.get("provisional_question_count") or 0),
        },
        "progress": {
            "answers_preserved": int(
                (status.get("interview_totals") or {}).get("answers_preserved") or 0
            ),
            "groups_presented": int(
                (status.get("interview_totals") or {}).get("groups_presented") or 0
            ),
        },
        "current_status": {
            "headline": supervisor_snapshot.wording.get("headline"),
            "detail": supervisor_snapshot.wording.get("detail"),
            "plain_language_dependency": supervisor_snapshot.plain_language_dependency,
            "user_action_code": supervisor_snapshot.user_action_code,
            "will_retry_by_itself": supervisor_snapshot.will_retry_by_itself,
            "provider_attempts_remaining_this_episode": (
                supervisor_snapshot.provider_attempts_remaining_this_episode
            ),
            "output_retries_remaining": supervisor_snapshot.output_retries_remaining,
            "availability_probes_remaining": (
                supervisor_snapshot.availability_probes_remaining
            ),
            "provider_request_unreconciled": (
                supervisor_snapshot.provider_request_unreconciled
            ),
            "unreconciled_note": (
                "N.H started one model request, cannot yet prove its outcome, and "
                "will not send it again."
                if supervisor_snapshot.provider_request_unreconciled
                else None
            ),
            # Whether the acceptance SURFACE is relevant at all.  Whether the
            # Accept action is ACTIONABLE is a separate question, answered only
            # by the controller's own offer projection at the offer route --
            # never here, and never by the browser.
            "acceptance_available": (
                supervisor_snapshot.state == supervisor.WorkflowState.READY_FOR_ACCEPTANCE
            ),
            "acceptance_truth": supervisor_snapshot.acceptance_truth,
            "accepted_for_design_only": supervisor_snapshot.accepted_for_design_only,
            "ness_acceptance_identity": supervisor_snapshot.ness_acceptance_identity,
            "ness_decision_clearance": supervisor_snapshot.ness_decision_clearance,
            "ness_answer_clarification": supervisor_snapshot.ness_answer_clarification,
            "ness_decision_cleared": supervisor_snapshot.ness_decision_cleared,
            "acceptance_note": (
                "Ready for acceptance is not acceptance. Acceptance records "
                "Ness's acceptance of this exact candidate for design-only "
                "status and nothing else."
            ),
        },
        "technical_details": supervisor_snapshot.technical,
        "technical": {
            "mode": status.get("mode"),
            "branch": status.get("source_branch"),
            "source_state": (status.get("source_head_sha") or "")[:12] or None,
            "validation_set": status.get("validation_set_id"),
            "coverage_review_current": gate.get("coverage_review_current"),
            "mechanical_path_unlocked": gate.get("mechanical_path_unlocked"),
            "journal_records": status.get("interview_events"),
            "authenticated_supervisor_records": supervisor_evidence.get("records"),
        },
    }


def build_ui_state() -> dict[str, Any]:
    """Return one recent projection, with at most one expensive replay at once."""
    global _UI_STATE_CACHE, _UI_STATE_CACHE_AT
    with _UI_STATE_LOCK:
        now = time.monotonic()
        if (
            _UI_STATE_CACHE is not None
            and now - _UI_STATE_CACHE_AT <= _UI_STATE_CACHE_TTL_SECONDS
        ):
            return _UI_STATE_CACHE
        state = _build_ui_state_uncached()
        _UI_STATE_CACHE = state
        _UI_STATE_CACHE_AT = time.monotonic()
        return state


QUESTION_HEADER_RE = re.compile(r"^QUESTION (\d+) of (\d+) in this group$")
OPTION_RE = re.compile(r"^\s{4}\[([^\]]+)\]\s+(.+)$")


def parse_question_forms(output: str) -> list[dict[str, Any]]:
    lines = controller_text_before_report(output).splitlines()
    questions: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    current_option: dict[str, Any] | None = None

    def finish() -> None:
        nonlocal current, current_option
        if current is not None:
            effect = current.get("effect", "")
            current["effect_sentences"] = [
                part.strip() for part in effect.split(";") if part.strip()
            ]
            questions.append(current)
        current = None
        current_option = None

    for line in lines:
        header = QUESTION_HEADER_RE.match(line)
        if header:
            finish()
            current = {
                "position": int(header.group(1)),
                "total": int(header.group(2)),
                "options": [],
            }
            continue
        if current is None:
            continue
        stripped = line.strip()
        if stripped.startswith("question id:"):
            current["question_id"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("form generation:"):
            current["form_generation"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("topic:"):
            current["topic"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("What I checked:"):
            current["checked"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("This is about:"):
            current["subject"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Already settled (kept as it is):"):
            current["settled"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Mechanical (mine, not yours):"):
            current["mechanical"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("What your answer changes in real use:"):
            current["effect"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("YOUR CHOICE:"):
            current["question"] = stripped.split(":", 1)[1].strip()
        else:
            option_match = OPTION_RE.match(line)
            if option_match:
                current_option = {
                    "option_id": option_match.group(1),
                    "meaning": option_match.group(2).strip(),
                    "consequences": [],
                    "other_effects": [],
                }
                current["options"].append(current_option)
            elif current_option and stripped.startswith("if you choose this:"):
                current_option["consequences"].append(
                    stripped.split(":", 1)[1].strip()
                )
            elif current_option and stripped.startswith("choosing this"):
                current_option["other_effects"].append(stripped)
    finish()
    return questions


def present_questions() -> dict[str, Any]:
    _, status = run_controller("interview-status")
    _, supervisor_status = run_controller("supervisor-status")
    ready = int(status.get("deliverable_question_count") or 0)
    interview_proved = bool(
        status.get("ok")
        and isinstance(status.get("interview_events"), int)
        and (
            status.get("interview_last_event_sha256") is None
            or isinstance(status.get("interview_last_event_sha256"), str)
        )
    )
    supervisor_proved = supervisor.report_is_proved(supervisor_status)
    if (
        not supervisor_proved
        or supervisor_status.get("workflow_state") != "NEEDS_NESS_DECISION"
        or not interview_proved
        or (not ready and status.get("open_group_index") is None)
    ):
        return {"ok": True, "questions": [], "stop_reason": "NOTHING_TO_PRESENT"}
    output, report = run_controller("next-question-group")
    return {
        "ok": True,
        "questions": parse_question_forms(output),
        "group": {
            "index": report.get("group_index"),
            "topic": report.get("next_group_topic"),
            "remaining": report.get("questions_still_pending_after_this_group"),
            "redelivered": bool(report.get("ness_question_redelivered")),
        },
        "stop_reason": report.get("interview_stop_reason"),
    }


def record_answer(payload: dict[str, Any]) -> dict[str, Any]:
    required = {"question_id", "form_generation", "answer_text"}
    allowed = required | {"answer_choice", "supersede_settled"}
    missing = sorted(required - set(payload))
    if missing:
        raise ControllerFailure("The answer is missing: %s." % ", ".join(missing))
    extra = sorted(set(payload) - allowed)
    if extra:
        raise ControllerFailure("The answer carries unsupported fields: %s." % ", ".join(extra))
    envelope = {
        "question_id": payload.get("question_id"),
        "form_generation": payload.get("form_generation"),
        "answer_text": payload.get("answer_text"),
        "answer_choice": payload.get("answer_choice"),
        "supersede_settled": bool(payload.get("supersede_settled", False)),
    }
    _, report = run_controller("record-ness-answer", envelope)
    return {
        "ok": True,
        "preserved": bool(report.get("ness_answer_recorded")),
        "question_id": report.get("answered_question_id"),
        "interpretation": report.get("controller_interpretation"),
        "consequences": report.get("mechanical_consequences"),
        "question_status": report.get("question_status_after"),
        "needs_revalidation": bool(report.get("revalidation_required")),
    }


# ---------------------------------------------------------------------------
# The acceptance surface.  The server is NOT acceptance authority: it checks
# Host, a strict Origin, the method, the content type, the size and the exact
# field set, hands the request to the controller, and renders the controller's
# answer.  It decides no acceptance, validates no binding of its own, holds no
# acceptance state, caches no offer as authority, and never falls back to
# another route when the controller refuses.
# ---------------------------------------------------------------------------
ACCEPTANCE_OFFER_PATH = supervisor.ACCEPTANCE_OFFER_ROUTE
ACCEPTANCE_RECORD_PATH = supervisor.ACCEPTANCE_RECORD_ROUTE


class AcceptanceRequestRefusal(ValueError):
    """A request-level refusal, named by the class the record will carry."""


def acceptance_offer() -> dict[str, Any]:
    """GET -- the controller's read-only projection, rendered and nothing else."""
    try:
        _output, report = run_controller("acceptance-offer")
    except ControllerFailure as exc:
        report = exc.report or {}
        if not report:
            raise
    return {
        "ok": True,
        "acceptance_actionable": bool(report.get("acceptance_actionable")),
        "acceptance_truth": report.get("acceptance_truth"),
        "reason": report.get("reason"),
        "workflow_state": report.get("workflow_state"),
        "acceptance_required": bool(report.get("acceptance_required")),
        "acceptance_offer_id": report.get("acceptance_offer_id"),
        "acceptance_offer_binding_sha256": report.get(
            "acceptance_offer_binding_sha256"
        ),
        "pre_click_head": report.get("pre_click_head"),
        "pre_click_head_digest_sha256": report.get("pre_click_head_digest_sha256"),
        "acceptance_scope_id": report.get("acceptance_scope_id"),
        "acceptance_scope_digest": report.get("acceptance_scope_digest"),
        "acceptance_scope_sentence": report.get("acceptance_scope_sentence"),
        "acceptance_scope_text": report.get("acceptance_scope_text"),
        "acceptance_fixed_meaning": report.get("acceptance_fixed_meaning"),
        "acceptance_non_authorizations": report.get("acceptance_non_authorizations")
        or [],
        "explanation_parts": report.get("explanation_parts") or [],
        "technical": report.get("technical") or {},
        "ness_acceptance_identity": report.get("ness_acceptance_identity"),
    }


def _acceptance_envelope(payload: dict[str, Any]) -> dict[str, Any]:
    """Section 16.3 -- the exact field set. No optional fields, ever.

    The controller enforces this again and never believes that the server did.
    """
    required = set(supervisor.ACCEPTANCE_POST_REQUIRED_FIELDS)
    missing = sorted(required - set(payload))
    if missing:
        raise AcceptanceRequestRefusal(
            "The acceptance request is missing: %s." % ", ".join(missing)
        )
    extra = sorted(set(payload) - required)
    if extra:
        raise AcceptanceRequestRefusal(
            "The acceptance request carries unsupported fields: %s." % ", ".join(extra)
        )
    if payload.get("ness_action_confirmed") is not True:
        raise AcceptanceRequestRefusal(
            "The acceptance request does not carry an explicit confirmation."
        )
    return {field: payload[field] for field in required}


def record_acceptance(payload: dict[str, Any]) -> dict[str, Any]:
    """POST -- invoke the controller with the EXACT displayed binding.

    The browser's values are passed through unaltered so the controller can
    detect a mismatch; the controller then recomputes everything under its own
    lock and believes none of them.
    """
    envelope = _acceptance_envelope(payload)
    try:
        _output, report = run_controller("record-ness-acceptance", envelope)
    except ControllerFailure as exc:
        report = exc.report or {}
        if not report:
            raise
    return {
        # HTTP success is NOT an acceptance claim.  The browser must refresh
        # and see the proved controller state before it says the word.
        "ok": True,
        "outcome": report.get("outcome"),
        "acceptance_truth": report.get("acceptance_truth"),
        "reason": report.get("reason"),
        "acceptance_events_appended": report.get("acceptance_events_appended"),
        "ness_acceptance_identity": report.get("ness_acceptance_identity"),
        "workflow_state": report.get("workflow_state"),
    }


def record_request_level_refusal() -> None:
    """Section 14 D3 -- ONE controller call, whose only effect is the record.

    A refused request is still a real operation, and Master V10 section 0B
    counts a rejection as a real thing that happened.  So the server refuses
    the request and then makes exactly one controller call so the refusal is
    permanently recorded -- passing NO rejected body, NO unvalidated field, and
    NO attacker-supplied text.  Where the journal or lock cannot safely record
    it, nothing is appended and the refusal is still reported.
    """
    try:
        run_controller("record-ness-acceptance", {})
    except ControllerFailure:
        # The controller refused, which is the point: the refusal record is its
        # only effect, and its refusal is not a second failure to report.
        return
    except Exception:  # noqa: BLE001 -- recording must never mask the refusal
        return


class InterviewHandler(BaseHTTPRequestHandler):
    server_version = "NHInterviewUI/1.0"

    def log_message(self, format_string: str, *args: Any) -> None:
        # Never log request bodies or query strings; answers belong in the
        # controller's authenticated journal, not in a web-server access log.
        path = urlparse(self.path).path
        sys.stderr.write("N.H UI %s %s\n" % (self.command, path))

    def _allowed_host(self) -> bool:
        host = self.headers.get("Host", "").split(":", 1)[0].strip("[]").lower()
        return host in {"127.0.0.1", "localhost", "::1"}

    def _strict_same_origin(self) -> bool:
        """Section 13.4 -- Origin present and EXACTLY equal to this server's own.

        This is in ADDITION to the localhost Host allow-list, never instead of
        it. The acceptance POST is the first state-changing request in this UI
        whose meaning is a governance act, and a localhost Host check alone
        does not stop a cross-origin page in the same browser from issuing a
        simple request to a local server.

        The expected origin is computed from this request's already-validated
        Host and this server's ACTUAL bound port -- one exact string, compared
        exactly. Missing, empty, "null", a wildcard, a mismatched scheme, a
        mismatched host and a mismatched port are all refused. There is no
        prefix, suffix or substring matching, and no allow-list of extra
        origins.
        """
        origin = self.headers.get("Origin")
        if not origin or origin.strip().lower() in {"null", "*"}:
            return False
        host = self.headers.get("Host", "").split(":", 1)[0].strip("[]").lower()
        if host not in {"127.0.0.1", "localhost", "::1"}:
            return False
        bracketed = "[%s]" % host if host == "::1" else host
        expected = "http://%s:%d" % (bracketed, self.server.server_port)
        return origin == expected

    def _security_headers(self, content_type: str) -> None:
        self.send_header("Content-Type", content_type)
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header(
            "Content-Security-Policy",
            "default-src 'self'; script-src 'self'; style-src 'self'; "
            "img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'",
        )

    def _send_bytes(
        self, data: bytes, content_type: str, status: HTTPStatus = HTTPStatus.OK
    ) -> None:
        self.send_response(status)
        self._security_headers(content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _send_json(
        self, value: dict[str, Any], status: HTTPStatus = HTTPStatus.OK
    ) -> None:
        data = json.dumps(value, ensure_ascii=False).encode("utf-8")
        self._send_bytes(data, "application/json; charset=utf-8", status)

    def _send_error_json(
        self, message: str, status: HTTPStatus, report: dict[str, Any] | None = None
    ) -> None:
        technical = None
        if report:
            technical = {
                "stop_reason": report.get("interview_stop_reason"),
                "errors": report.get("errors") or [],
            }
        self._send_json(
            {"ok": False, "message": message, "technical": technical}, status
        )

    def do_GET(self) -> None:
        if not self._allowed_host():
            self._send_error_json("This page is local-only.", HTTPStatus.FORBIDDEN)
            return
        path = urlparse(self.path).path
        if path == "/api/health":
            self._send_json({"ok": True, "service": "nh-interview-ui"})
            return
        if path == "/api/state":
            try:
                self._send_json(build_ui_state())
            except ControllerFailure as exc:
                self._send_error_json(
                    str(exc), HTTPStatus.SERVICE_UNAVAILABLE, exc.report
                )
            return
        if path == ACCEPTANCE_OFFER_PATH:
            # A READ. It computes the offer from freshly re-read authenticated
            # state and appends nothing, however many times it is read.
            try:
                self._send_json(acceptance_offer())
            except ControllerFailure as exc:
                self._send_error_json(
                    str(exc), HTTPStatus.SERVICE_UNAVAILABLE, exc.report
                )
            return
        if path == ACCEPTANCE_RECORD_PATH:
            # A GET or HEAD at the RECORD route is a wrong-method mutation
            # attempt. It is refused, mutates NO acceptance state, appends zero
            # acceptance events, and -- where the journal and lock can safely
            # be appended to -- receives exactly one operational refusal record,
            # which does move the journal and the head.
            record_request_level_refusal()
            self._send_error_json(
                "Recording an acceptance requires an explicit POST. Nothing was "
                "accepted and no acceptance state changed.",
                HTTPStatus.METHOD_NOT_ALLOWED,
            )
            return
        if path == "/favicon.ico":
            self._send_bytes(b"", "image/x-icon", HTTPStatus.NO_CONTENT)
            return
        files = {
            "/": ("index.html", "text/html; charset=utf-8"),
            "/index.html": ("index.html", "text/html; charset=utf-8"),
            "/styles.css": ("styles.css", "text/css; charset=utf-8"),
            "/app.js": ("app.js", "text/javascript; charset=utf-8"),
        }
        item = files.get(path)
        if item is None:
            self._send_error_json("Not found.", HTTPStatus.NOT_FOUND)
            return
        filename, content_type = item
        try:
            data = (STATIC_DIR / filename).read_bytes()
        except OSError:
            self._send_error_json(
                "The interface file is unavailable.", HTTPStatus.INTERNAL_SERVER_ERROR
            )
            return
        self._send_bytes(data, content_type)

    def _read_json_body(self) -> dict[str, Any]:
        content_type = self.headers.get("Content-Type", "")
        if not content_type.startswith("application/json"):
            raise ValueError("This action requires a JSON request.")
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError as exc:
            raise ValueError("The request length is invalid.") from exc
        if length <= 0 or length > MAX_REQUEST_BYTES:
            raise ValueError("The request is empty or too large.")
        try:
            value = json.loads(self.rfile.read(length).decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ValueError("The request is not valid JSON.") from exc
        if not isinstance(value, dict):
            raise ValueError("The request must be one JSON object.")
        return value

    def do_POST(self) -> None:
        if not self._allowed_host():
            self._send_error_json("This page is local-only.", HTTPStatus.FORBIDDEN)
            return
        path = urlparse(self.path).path
        if path == ACCEPTANCE_RECORD_PATH and not self._strict_same_origin():
            record_request_level_refusal()
            self._send_error_json(
                "This acceptance action must come from this page itself. "
                "Nothing was accepted.",
                HTTPStatus.FORBIDDEN,
            )
            return
        try:
            payload = self._read_json_body()
            if path == "/api/questions/present":
                self._send_json(present_questions())
            elif path == "/api/answers":
                self._send_json(record_answer(payload))
            elif path == ACCEPTANCE_RECORD_PATH:
                self._send_json(record_acceptance(payload))
            else:
                self._send_error_json("Not found.", HTTPStatus.NOT_FOUND)
        except AcceptanceRequestRefusal as exc:
            record_request_level_refusal()
            self._send_error_json(str(exc), HTTPStatus.BAD_REQUEST)
        except ValueError as exc:
            if path == ACCEPTANCE_RECORD_PATH:
                record_request_level_refusal()
            self._send_error_json(str(exc), HTTPStatus.BAD_REQUEST)
        except ControllerFailure as exc:
            self._send_error_json(str(exc), HTTPStatus.CONFLICT, exc.report)


def serve(*, port: int = 0, no_open: bool = False, stop_event=None) -> int:
    """Serve the already-configured UI on localhost."""
    if _CONTROLLER_RUNNER is None and not CONTROLLER_PATH.is_file():
        print("N.H controller not found: %s" % CONTROLLER_PATH, file=sys.stderr)
        return 1
    server = ThreadingHTTPServer(("127.0.0.1", port), InterviewHandler)
    url = "http://127.0.0.1:%d/" % server.server_port
    print("N.H interview page: %s" % url, flush=True)
    if not no_open:
        webbrowser.open(url)
    if stop_event is not None:
        def stop_when_requested():
            stop_event.wait()
            server.shutdown()

        threading.Thread(
            target=stop_when_requested,
            name="nh-interview-server-stop",
            daemon=True,
        ).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the local N.H interview page.")
    # Let the operating system choose a free port by default. The page opens
    # automatically, so Ness never has to find or manage that port herself.
    parser.add_argument("--port", type=int, default=0)
    parser.add_argument("--no-open", action="store_true")
    args = parser.parse_args()
    return serve(port=args.port, no_open=args.no_open)


if __name__ == "__main__":
    raise SystemExit(main())

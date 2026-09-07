#!/usr/bin/env python3
"""Section 11.7 -- the private local scheduling journal.

It is an observation/recovery log.  Its unkeyed hash chain detects damage but is
explicitly NOT authority for workflow state, audit, PASS, custody, result
custody, episodes, probes, scope generation, scope exhaustion, questions, or
acceptance readiness.  It stores no controller report, no finding text, no Ness
answer, no candidate or provider bytes, no facts object, and -- deliberately --
no ``supervisor_operation_id``, no ``unlock_evidence_*`` value, and no operation
envelope, pre-state, or input-envelope digest.
"""

from __future__ import annotations

import errno
import fcntl
import json
import os
import stat

from . import constants
from .canonical import canonical_json, is_hex64, is_real_int, sha256_hex

JOURNAL_BASENAME = "supervisor_events.jsonl"
LOCK_BASENAME = "supervisor_lease.json.lock"
ZERO_SHA256 = "0" * 64
MAX_RECORD_BYTES = 64_000

RECORD_KEYS = (
    "scheduling_journal_version",
    "retry_series_key",
    "dependency_identity",
    "dependency_identity_binding",
    "work_item_identity",
    "provider_availability_episode_identity",
    "attempt",
    "first_failure_epoch",
    "scheduled_at_epoch",
    "next_eligible_epoch",
    "delay_seconds",
    "maximum_delay_seconds",
    "output_retries_used",
    "availability_probes_used_this_closed_episode",
    "episode_exhaustion_observed_epoch",
    "episode_unlock_wait_until_epoch",
    "latest_probe_anchor_identity",
    "latest_probe_anchor_epoch",
    "next_probe_eligible_epoch",
    "post_operation_state_sha256",
)

BINDING_KEYS = (
    "controller_executable_identity",
    "source_binding_sha256",
    "package_scope_id",
    "candidate_path",
    "candidate_sha256",
    "candidate_bytes",
    "work_item_identity",
    "provider_availability_episode_identity",
    "retry_series_key",
    "controller_report_sha256",
)

# The fields the record list above deliberately omits.
FORBIDDEN_RECORD_KEYS = frozenset(
    (
        "supervisor_operation_id",
        "unlock_evidence_kind",
        "unlock_evidence_identity",
        "unlock_evidence_sha256",
        "operation_envelope",
        "pre_state_sha256",
        "input_envelope_sha256",
        "controller_report",
        "findings",
        "answer",
        "candidate_bytes_base64",
        "result_bytes_base64",
        "provider_outcome_facts",
        "probe_observation_facts",
        "token",
        "credential",
    )
)

RECORD_KINDS = (
    "workflow_state_changed",
    "controller_run_started",
    "controller_report_digest_observed",
    "controller_run_completed",
    "controller_run_reconciled",
    "controller_run_abandoned",
    "result_custody_observed",
    "probe_observed",
    "technical_backoff_scheduled",
    "technical_backoff_cleared",
    "episode_unlock_observed",
)


class SchedulingJournalError(RuntimeError):
    """The private scheduling journal is damaged, insecure, or of a bad version."""


def backoff_delay_seconds(attempt):
    return min(
        constants.BACKOFF_BASE_SECONDS * (2 ** (attempt - 1)), constants.BACKOFF_MAX_SECONDS
    )


class SchedulingJournal:
    """Anchored, locked, fsynced, read back, and never authority."""

    def __init__(self, state_dir):
        self.state_dir = str(state_dir)
        self._series = {}
        self._exhaustion_anchor = {}
        self._probe_anchor = {}
        self._records = []
        self._load()

    # -- storage ------------------------------------------------------------
    def _open_dir_fd(self, create=True):
        if create:
            os.makedirs(self.state_dir, mode=0o700, exist_ok=True)
        fd = os.open(self.state_dir, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        try:
            info = os.fstat(fd)
            if info.st_uid != os.geteuid():
                raise SchedulingJournalError("the state directory is not owner-only")
            if stat.S_IMODE(info.st_mode) != 0o700:
                raise SchedulingJournalError("the state directory is not mode 0700")
        except Exception:
            os.close(fd)
            raise
        return fd

    def _path(self):
        return os.path.join(self.state_dir, JOURNAL_BASENAME)

    def _load(self):
        try:
            fd = os.open(self._path(), os.O_RDONLY | os.O_NOFOLLOW)
        except OSError as exc:
            if exc.errno == errno.ENOENT:
                return
            raise SchedulingJournalError("the scheduling journal is unreadable: %s" % exc)
        try:
            info = os.fstat(fd)
            if not stat.S_ISREG(info.st_mode):
                raise SchedulingJournalError("the scheduling journal is not a regular file")
            if info.st_nlink != 1:
                raise SchedulingJournalError("the scheduling journal is multi-link")
            if stat.S_IMODE(info.st_mode) != 0o600:
                raise SchedulingJournalError("the scheduling journal is not mode 0600")
            if info.st_uid != os.geteuid():
                raise SchedulingJournalError("the scheduling journal is not owner-only")
            blob = b""
            while True:
                chunk = os.read(fd, 1 << 20)
                if not chunk:
                    break
                blob += chunk
        finally:
            os.close(fd)
        previous = ZERO_SHA256
        for line in blob.decode("utf-8").splitlines():
            if not line.strip():
                continue
            record = json.loads(line)
            self._validate(record, previous)
            previous = record["record_sha256"]
            self._records.append(record)
            self._apply(record)

    def _validate(self, record, previous):
        if not isinstance(record, dict):
            raise SchedulingJournalError("a scheduling record is not an object")
        required = {"kind", "payload", "binding", "prev_record_sha256", "record_sha256"}
        if set(record) != required:
            raise SchedulingJournalError("a scheduling record has the wrong key set")
        if record["kind"] not in RECORD_KINDS:
            raise SchedulingJournalError("unknown scheduling record kind")
        if record["prev_record_sha256"] != previous:
            raise SchedulingJournalError("the scheduling journal chain is broken")
        body = {key: value for key, value in record.items() if key != "record_sha256"}
        if sha256_hex(canonical_json(body)) != record["record_sha256"]:
            raise SchedulingJournalError("a scheduling record digest does not verify")
        payload = record["payload"]
        if not isinstance(payload, dict):
            raise SchedulingJournalError("a scheduling payload is not an object")
        version = payload.get("scheduling_journal_version")
        if version not in constants.SUPERVISOR_SCHEDULING_JOURNAL_SUPPORTED_VERSIONS:
            raise SchedulingJournalError(
                "scheduling journal version %r is refused, not migrated" % (version,)
            )
        intruder = sorted(FORBIDDEN_RECORD_KEYS & set(payload))
        if intruder:
            raise SchedulingJournalError(
                "the private scheduling journal may never store %s" % ", ".join(intruder)
            )
        if len(canonical_json(record).encode("utf-8")) > MAX_RECORD_BYTES:
            raise SchedulingJournalError("a scheduling record exceeds its byte bound")
        binding = record["binding"]
        if not isinstance(binding, dict) or set(binding) != set(BINDING_KEYS):
            raise SchedulingJournalError("a scheduling record has no exact binding object")

    def _apply(self, record):
        payload = record["payload"]
        key = payload.get("retry_series_key")
        if record["kind"] == "technical_backoff_scheduled" and key:
            self._series[key] = dict(payload)
        elif record["kind"] == "technical_backoff_cleared" and key:
            self._series.pop(key, None)
        episode = payload.get("provider_availability_episode_identity")
        if payload.get("episode_exhaustion_observed_epoch") is not None and episode:
            self._exhaustion_anchor.setdefault(
                episode, payload["episode_exhaustion_observed_epoch"]
            )
        anchor_identity = payload.get("latest_probe_anchor_identity")
        if anchor_identity and payload.get("latest_probe_anchor_epoch") is not None:
            existing = self._probe_anchor.get(anchor_identity)
            if existing is not None and existing != payload["latest_probe_anchor_epoch"]:
                raise SchedulingJournalError(
                    "a probe anchor was written twice with different values"
                )
            self._probe_anchor[anchor_identity] = payload["latest_probe_anchor_epoch"]
            if episode:
                self._probe_anchor[("episode", episode)] = payload[
                    "latest_probe_anchor_epoch"
                ]

    def append(self, kind, payload, binding):
        if kind not in RECORD_KINDS:
            raise SchedulingJournalError("unknown scheduling record kind %r" % (kind,))
        body = dict(payload)
        body.setdefault(
            "scheduling_journal_version", constants.SUPERVISOR_SCHEDULING_JOURNAL_VERSION
        )
        for key in RECORD_KEYS:
            body.setdefault(key, None)
        body["scheduling_journal_version"] = (
            constants.SUPERVISOR_SCHEDULING_JOURNAL_VERSION
        )
        extra = sorted(set(body) - set(RECORD_KEYS))
        if extra:
            raise SchedulingJournalError(
                "a scheduling payload may carry only its declared keys: %s"
                % ", ".join(extra)
            )
        binding_object = {key: binding.get(key) for key in BINDING_KEYS}

        dir_fd = self._open_dir_fd()
        try:
            lock_fd = os.open(
                LOCK_BASENAME, os.O_RDWR | os.O_CREAT | os.O_NOFOLLOW, 0o600, dir_fd=dir_fd
            )
            try:
                fcntl.flock(lock_fd, fcntl.LOCK_EX)
                # Section 11.7: the chain is built UNDER the lock, over the tail
                # this appender has just re-read from disk.  Building it before
                # the lock would let two appenders derive the same
                # prev_record_sha256 and leave a file whose chain does not
                # verify -- damage the reader would then refuse, losing both
                # records instead of keeping one valid chain.
                self._records = []
                self._series = {}
                self._exhaustion_anchor = {}
                self._probe_anchor = {}
                self._load()
                record = {
                    "kind": kind,
                    "payload": body,
                    "binding": binding_object,
                    "prev_record_sha256": (
                        self._records[-1]["record_sha256"]
                        if self._records
                        else ZERO_SHA256
                    ),
                }
                record["record_sha256"] = sha256_hex(canonical_json(record))
                self._validate(record, record["prev_record_sha256"])
                fd = os.open(
                    JOURNAL_BASENAME,
                    os.O_WRONLY | os.O_CREAT | os.O_APPEND | os.O_NOFOLLOW,
                    0o600,
                    dir_fd=dir_fd,
                )
                try:
                    os.write(fd, (canonical_json(record) + "\n").encode("utf-8"))
                    os.fsync(fd)
                finally:
                    os.close(fd)
                os.fsync(dir_fd)
            finally:
                os.close(lock_fd)
        finally:
            os.close(dir_fd)
        self._records.append(record)
        self._apply(record)
        return record

    # -- Section 11.7 scheduling ---------------------------------------------
    def series(self, retry_series_key):
        return self._series.get(retry_series_key)

    def series_keys(self):
        """Every retry series this private journal currently holds open."""
        return sorted(self._series)

    def schedule_backoff(self, retry_series_key, binding, now, *, dependency_identity=None,
                         dependency_identity_binding=None, work_item_identity=None,
                         episode_identity=None, output_retries_used=0,
                         post_operation_state_sha256=None):
        existing = self._series.get(retry_series_key)
        if existing is None:
            attempt = 1
            first_failure = int(now)
        else:
            attempt = existing["attempt"] + 1
            first_failure = existing["first_failure_epoch"]
        delay = backoff_delay_seconds(attempt)
        payload = {
            "retry_series_key": retry_series_key,
            "dependency_identity": dependency_identity,
            "dependency_identity_binding": dependency_identity_binding,
            "work_item_identity": work_item_identity,
            "provider_availability_episode_identity": episode_identity,
            "attempt": attempt,
            "first_failure_epoch": first_failure,
            "scheduled_at_epoch": int(now),
            "next_eligible_epoch": int(now) + delay,
            "delay_seconds": delay,
            "maximum_delay_seconds": constants.BACKOFF_MAX_SECONDS,
            "output_retries_used": output_retries_used,
            "post_operation_state_sha256": post_operation_state_sha256,
        }
        self.append("technical_backoff_scheduled", payload, binding)
        return payload

    def clear_series(self, retry_series_key, binding):
        self.append(
            "technical_backoff_cleared", {"retry_series_key": retry_series_key}, binding
        )

    def eligible(self, retry_series_key, now):
        series = self._series.get(retry_series_key)
        if series is None:
            return True
        if now < series["scheduled_at_epoch"]:
            # Backward wall-clock movement waits the maximum, never less.
            return False
        return now >= series["next_eligible_epoch"]

    def wait_seconds(self, retry_series_key, now):
        series = self._series.get(retry_series_key)
        if series is None:
            return 0
        if now < series["scheduled_at_epoch"]:
            return constants.BACKOFF_MAX_SECONDS
        return max(0, series["next_eligible_epoch"] - now)

    # -- anchors --------------------------------------------------------------
    def record_exhaustion_anchor(self, closed_episode_identity, now, binding=None):
        if closed_episode_identity in self._exhaustion_anchor:
            return self._exhaustion_anchor[closed_episode_identity]
        payload = {
            "provider_availability_episode_identity": closed_episode_identity,
            "episode_exhaustion_observed_epoch": int(now),
            "episode_unlock_wait_until_epoch": int(now)
            + constants.MIN_EPISODE_UNLOCK_WAIT_SECONDS,
        }
        self.append("episode_unlock_observed", payload, binding or {})
        return int(now)

    def record_probe_anchor(self, closed_episode_identity, probe_identity, now,
                            binding=None):
        if probe_identity in self._probe_anchor:
            return self._probe_anchor[probe_identity]
        payload = {
            "provider_availability_episode_identity": closed_episode_identity,
            "latest_probe_anchor_identity": probe_identity,
            "latest_probe_anchor_epoch": int(now),
            "next_probe_eligible_epoch": int(now)
            + constants.MIN_EPISODE_UNLOCK_WAIT_SECONDS,
        }
        self.append("probe_observed", payload, binding or {})
        return int(now)

    def episode_unlock_wait_until(self, closed_episode_identity, now):
        anchor = self._exhaustion_anchor.get(closed_episode_identity)
        if anchor is None:
            # Absence never shortens the wait: write the current clock and wait a
            # full interval.
            anchor = self.record_exhaustion_anchor(closed_episode_identity, now)
        return anchor + constants.MIN_EPISODE_UNLOCK_WAIT_SECONDS

    def next_probe_eligible_epoch(self, closed_episode_identity, now):
        anchor = self._probe_anchor.get(("episode", closed_episode_identity))
        if anchor is None:
            anchor = self._exhaustion_anchor.get(closed_episode_identity)
        if anchor is None:
            anchor = self.record_exhaustion_anchor(closed_episode_identity, now)
        return anchor + constants.MIN_EPISODE_UNLOCK_WAIT_SECONDS

    def unlock_wait_satisfied(self, closed_episode_identity, now):
        return now >= self.episode_unlock_wait_until(closed_episode_identity, now)

    def probe_spacing_satisfied(self, closed_episode_identity, now):
        return now >= self.next_probe_eligible_epoch(closed_episode_identity, now)

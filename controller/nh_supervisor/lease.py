#!/usr/bin/env python3
"""Sections 13.2-13.5 -- the one anchored supervisor lease.

Four exact states and no binary liveness.  ``INVALID_UNPROVED`` is the default:
a check reaches any other state only by positive proof, and an unproved lease is
never taken over, repaired, truncated, deleted, or overwritten.

This is production code shared by the controller (whose command preconditions
read the lease) and by the persistent worker (which owns it).  Every filesystem
operation is anchored: the directory descriptor is opened once and every file is
opened relative to it with ``O_NOFOLLOW``.
"""

from __future__ import annotations

import errno
import fcntl
import json
import os
import stat

from . import constants
from .canonical import canonical_json, is_hex64, is_real_int, sha256_hex

STATE_DIR_ENV = "NH_SUPERVISOR_STATE_DIR"
DEFAULT_STATE_DIR_NAME = ".nh_supervisor_state"

EVENTS_BASENAME = "supervisor_events.jsonl"
LEASE_BASENAME = "supervisor_lease.json"
LOCK_BASENAME = "supervisor_lease.json.lock"
RESULT_STORE_BASENAME = "provider_results"

LEASE_KEYS = (
    "lease_version",
    "run_id",
    "pid",
    "process_start_ticks",
    "boot_id_sha256",
    "controller_executable_identity",
    "package_scope_id",
    "source_binding_sha256",
    "acquired_at_epoch",
    "heartbeat_at_epoch",
    "expires_at_epoch",
)

LEASE_ID_LABEL = "NH_SUPERVISOR_LEASE_ID_V1"
LEASE_IDENTITY_KEYS = tuple(
    key
    for key in LEASE_KEYS
    if key not in ("run_id", "heartbeat_at_epoch", "expires_at_epoch")
)

MAX_LEASE_BYTES = 4096


class LeaseError(RuntimeError):
    """The lease could not be operated on safely."""


def resolve_state_dir(project_root, environ=None):
    """Section 13.2 -- the absolute ``NH_SUPERVISOR_STATE_DIR`` when set."""
    environ = os.environ if environ is None else environ
    configured = environ.get(STATE_DIR_ENV)
    if configured:
        if not os.path.isabs(configured):
            raise LeaseError("%s must be an absolute path" % STATE_DIR_ENV)
        return configured
    return os.path.join(
        os.path.realpath(str(project_root)), "interview_ui", DEFAULT_STATE_DIR_NAME
    )


def run_id_for(identity):
    material = {key: identity[key] for key in LEASE_IDENTITY_KEYS}
    return sha256_hex(canonical_json([LEASE_ID_LABEL, material]))


def read_process_start_ticks(pid, proc_root="/proc"):
    with open(os.path.join(proc_root, str(pid), "stat"), "rb") as handle:
        raw = handle.read()
    close = raw.rindex(b")")
    fields = raw[close + 2 :].split()
    return int(fields[19])


def boot_id_sha256(proc_root="/proc"):
    with open(os.path.join(proc_root, "sys", "kernel", "random", "boot_id"), "rb") as handle:
        return sha256_hex(handle.read())


class LeaseHooks:
    """Injection seam for ``/proc`` and boot-id reads (Section 16)."""

    def __init__(self, proc_root="/proc"):
        self.proc_root = proc_root

    def boot_id_sha256(self):
        return boot_id_sha256(self.proc_root)

    def process_start_ticks(self, pid):
        return read_process_start_ticks(pid, self.proc_root)

    def process_exists(self, pid):
        os.stat(os.path.join(self.proc_root, str(pid)))
        return True


class SupervisorLease:
    """The anchored lease file, its lock, and the four-state evaluation."""

    def __init__(self, state_dir, hooks=None, clock=None):
        self.state_dir = str(state_dir)
        self.hooks = hooks or LeaseHooks()
        self._clock = clock or (lambda: __import__("time").time())

    # -- anchored directory --------------------------------------------------
    def open_dir_fd(self, create=False):
        if create:
            os.makedirs(self.state_dir, mode=constants_state_dir_mode(), exist_ok=True)
            os.makedirs(
                os.path.join(self.state_dir, RESULT_STORE_BASENAME),
                mode=0o700,
                exist_ok=True,
            )
        fd = os.open(self.state_dir, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        try:
            info = os.fstat(fd)
            if not stat.S_ISDIR(info.st_mode):
                raise LeaseError("the supervisor state path is not a directory")
            if info.st_uid != os.geteuid():
                raise LeaseError("the supervisor state directory is not owned by this user")
            if stat.S_IMODE(info.st_mode) != 0o700:
                raise LeaseError("the supervisor state directory is not mode 0700")
        except Exception:
            os.close(fd)
            raise
        return fd

    def _open_locked(self, dir_fd):
        flags = os.O_RDWR | os.O_CREAT | os.O_NOFOLLOW
        fd = os.open(LOCK_BASENAME, flags, 0o600, dir_fd=dir_fd)
        try:
            fcntl.flock(fd, fcntl.LOCK_EX)
        except Exception:
            os.close(fd)
            raise
        return fd

    # -- Section 13.3 evaluation, S1-S13 in this exact order -----------------
    def evaluate(self, binding=None, now=None):
        """Return ``(state, lease_or_None, reason)``.  Writes nothing, ever."""
        now = self._clock() if now is None else now
        try:
            dir_fd = self.open_dir_fd()
        except Exception as exc:  # S1
            return "INVALID_UNPROVED", None, "S1: %s" % exc
        try:
            lock_fd = None
            try:
                lock_fd = self._open_locked(dir_fd)
            except Exception as exc:
                return "INVALID_UNPROVED", None, "S1 lock: %s" % exc
            try:
                return self._evaluate_locked(dir_fd, binding, now)
            finally:
                if lock_fd is not None:
                    os.close(lock_fd)
        finally:
            os.close(dir_fd)

    def _evaluate_locked(self, dir_fd, binding, now):
        # S2 -- open relative to the anchored descriptor with O_NOFOLLOW.
        try:
            fd = os.open(LEASE_BASENAME, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=dir_fd)
        except OSError as exc:
            if exc.errno == errno.ENOENT:
                return "ABSENT_PROVED", None, "S2: no lease exists"
            return "INVALID_UNPROVED", None, "S2: %s" % exc
        try:
            info = os.fstat(fd)
            # S3 -- file facts.
            if not stat.S_ISREG(info.st_mode):
                return "INVALID_UNPROVED", None, "S3: not a regular file"
            if info.st_nlink != 1:
                return "INVALID_UNPROVED", None, "S3: not a single-link file"
            if stat.S_IMODE(info.st_mode) != 0o600:
                return "INVALID_UNPROVED", None, "S3: not mode 0600"
            if info.st_uid != os.geteuid():
                return "INVALID_UNPROVED", None, "S3: wrong owner"
            if info.st_size > MAX_LEASE_BYTES:
                return "INVALID_UNPROVED", None, "S3: over the size bound"
            raw = os.read(fd, MAX_LEASE_BYTES + 1)
        except OSError as exc:
            return "INVALID_UNPROVED", None, "S3: %s" % exc
        finally:
            os.close(fd)

        # S4 -- parse.
        try:
            lease = json.loads(raw.decode("utf-8"))
        except Exception as exc:
            return "INVALID_UNPROVED", None, "S4: %s" % exc
        if not isinstance(lease, dict) or set(lease) != set(LEASE_KEYS):
            return "INVALID_UNPROVED", None, "S4: the lease has the wrong key set"

        # S5 -- version and field validity.
        if lease["lease_version"] != constants.LEASE_VERSION:
            return "INVALID_UNPROVED", None, "S5: wrong lease_version"
        if not is_real_int(lease["pid"]) or lease["pid"] <= 0:
            return "INVALID_UNPROVED", None, "S5: pid"
        if not is_real_int(lease["process_start_ticks"]) or lease["process_start_ticks"] < 0:
            return "INVALID_UNPROVED", None, "S5: process_start_ticks"
        for key in ("boot_id_sha256", "controller_executable_identity", "source_binding_sha256"):
            if not is_hex64(lease[key]):
                return "INVALID_UNPROVED", None, "S5: %s" % key
        if not isinstance(lease["package_scope_id"], str) or not lease["package_scope_id"]:
            return "INVALID_UNPROVED", None, "S5: package_scope_id"
        if not is_hex64(lease["run_id"]):
            return "INVALID_UNPROVED", None, "S5: run_id"
        for key in ("acquired_at_epoch", "heartbeat_at_epoch", "expires_at_epoch"):
            if not is_real_int(lease[key]) or lease[key] < 0:
                return "INVALID_UNPROVED", None, "S5: %s" % key

        # S6 -- run_id re-derivation.
        if run_id_for(lease) != lease["run_id"]:
            return "INVALID_UNPROVED", None, "S6: run_id does not re-derive"

        # S7 -- released sentinel.
        if lease["expires_at_epoch"] == 0 and (
            lease["heartbeat_at_epoch"] >= lease["acquired_at_epoch"]
        ):
            return "ABSENT_PROVED", lease, "S7: cleanly released"

        # S8 -- binding.
        if binding is not None:
            mismatch = any(
                lease[key] != binding.get(key)
                for key in (
                    "package_scope_id",
                    "source_binding_sha256",
                    "controller_executable_identity",
                )
            )
            if mismatch and now <= lease["expires_at_epoch"]:
                return "INVALID_UNPROVED", lease, "S8: binding mismatch before expiry"

        # S9 -- time ordering.
        if not (
            lease["acquired_at_epoch"]
            <= lease["heartbeat_at_epoch"]
            <= lease["expires_at_epoch"]
        ):
            return "INVALID_UNPROVED", lease, "S9: time ordering"
        if lease["expires_at_epoch"] - lease["heartbeat_at_epoch"] != (
            constants.LEASE_EXPIRY_SECONDS
        ):
            return "INVALID_UNPROVED", lease, "S9: expiry offset"
        if now < lease["acquired_at_epoch"] - constants.CLOCK_SKEW_TOLERANCE_SECONDS:
            return "INVALID_UNPROVED", lease, "S9: the clock is far behind acquisition"

        # S10 -- expiry.
        if now > lease["expires_at_epoch"]:
            return "EXPIRED_PROVED", lease, "S10: expired"

        # S11 -- boot identity.
        try:
            observed_boot = self.hooks.boot_id_sha256()
        except Exception as exc:
            return "INVALID_UNPROVED", lease, "S11: %s" % exc
        if observed_boot != lease["boot_id_sha256"]:
            return "INVALID_UNPROVED", lease, "S11: boot id mismatch before expiry"

        # S12 -- process identity.
        try:
            self.hooks.process_exists(lease["pid"])
        except FileNotFoundError:
            return "INVALID_UNPROVED", lease, "S12: the process is missing before expiry"
        except Exception as exc:
            return "INVALID_UNPROVED", lease, "S12: %s" % exc
        try:
            ticks = self.hooks.process_start_ticks(lease["pid"])
        except FileNotFoundError:
            return "INVALID_UNPROVED", lease, "S12: the process is missing before expiry"
        except Exception as exc:
            return "INVALID_UNPROVED", lease, "S12: %s" % exc
        if ticks != lease["process_start_ticks"]:
            return "INVALID_UNPROVED", lease, "S12: PID reuse"

        # S13.
        return "LIVE_PROVED", lease, "S13: proved"

    # -- Section 13.4 acquisition, takeover, release -------------------------
    def acquire(self, binding, now=None):
        """Return ``("ACQUIRED"|"RENEWED"|"BUSY"|"SAFETY_HOLD", lease_or_None)``."""
        now = int(self._clock() if now is None else now)
        dir_fd = self.open_dir_fd(create=True)
        try:
            lock_fd = self._open_locked(dir_fd)
            try:
                state, lease, _reason = self._evaluate_locked(dir_fd, binding, now)
                if state == "INVALID_UNPROVED":
                    return "SAFETY_HOLD", None
                if state == "LIVE_PROVED":
                    if lease["run_id"] == self._own_run_id(binding, lease):
                        renewed = dict(lease)
                        renewed["heartbeat_at_epoch"] = now
                        renewed["expires_at_epoch"] = now + constants.LEASE_EXPIRY_SECONDS
                        self._write(dir_fd, renewed)
                        return "RENEWED", renewed
                    return "BUSY", lease
                fresh = self._new_lease(binding, now)
                self._write(dir_fd, fresh)
                return "ACQUIRED", fresh
            finally:
                os.close(lock_fd)
        finally:
            os.close(dir_fd)

    def heartbeat(self, binding, now=None):
        now = int(self._clock() if now is None else now)
        dir_fd = self.open_dir_fd()
        try:
            lock_fd = self._open_locked(dir_fd)
            try:
                state, lease, _reason = self._evaluate_locked(dir_fd, binding, now)
                if state != "LIVE_PROVED":
                    return False, state
                if lease["run_id"] != self._own_run_id(binding, lease):
                    return False, "BUSY"
                renewed = dict(lease)
                renewed["heartbeat_at_epoch"] = now
                renewed["expires_at_epoch"] = now + constants.LEASE_EXPIRY_SECONDS
                self._write(dir_fd, renewed)
                return True, "LIVE_PROVED"
            finally:
                os.close(lock_fd)
        finally:
            os.close(dir_fd)

    def release(self, binding, now=None):
        now = int(self._clock() if now is None else now)
        dir_fd = self.open_dir_fd()
        try:
            lock_fd = self._open_locked(dir_fd)
            try:
                state, lease, _reason = self._evaluate_locked(dir_fd, binding, now)
                if state != "LIVE_PROVED" or lease is None:
                    return False
                if lease["run_id"] != self._own_run_id(binding, lease):
                    return False
                released = dict(lease)
                released["heartbeat_at_epoch"] = now
                released["expires_at_epoch"] = 0
                self._write(dir_fd, released)
                return True
            finally:
                os.close(lock_fd)
        finally:
            os.close(dir_fd)

    def _own_run_id(self, binding, lease):
        identity = {
            "lease_version": constants.LEASE_VERSION,
            "pid": binding["pid"],
            "process_start_ticks": binding["process_start_ticks"],
            "boot_id_sha256": binding["boot_id_sha256"],
            "controller_executable_identity": binding["controller_executable_identity"],
            "package_scope_id": binding["package_scope_id"],
            "source_binding_sha256": binding["source_binding_sha256"],
            "acquired_at_epoch": lease["acquired_at_epoch"],
        }
        return run_id_for(identity)

    def _new_lease(self, binding, now):
        identity = {
            "lease_version": constants.LEASE_VERSION,
            "pid": binding["pid"],
            "process_start_ticks": binding["process_start_ticks"],
            "boot_id_sha256": binding["boot_id_sha256"],
            "controller_executable_identity": binding["controller_executable_identity"],
            "package_scope_id": binding["package_scope_id"],
            "source_binding_sha256": binding["source_binding_sha256"],
            "acquired_at_epoch": now,
        }
        lease = dict(identity)
        lease["run_id"] = run_id_for(identity)
        lease["heartbeat_at_epoch"] = now
        lease["expires_at_epoch"] = now + constants.LEASE_EXPIRY_SECONDS
        return lease

    def _write(self, dir_fd, lease):
        payload = (json.dumps(lease, sort_keys=True, separators=(",", ":")) + "\n").encode(
            "utf-8"
        )
        temp = LEASE_BASENAME + ".new"
        try:
            os.unlink(temp, dir_fd=dir_fd)
        except FileNotFoundError:
            pass
        fd = os.open(
            temp, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600, dir_fd=dir_fd
        )
        try:
            os.write(fd, payload)
            os.fsync(fd)
        finally:
            os.close(fd)
        os.rename(temp, LEASE_BASENAME, src_dir_fd=dir_fd, dst_dir_fd=dir_fd)
        os.fsync(dir_fd)


def constants_state_dir_mode():
    return 0o700


# ---------------------------------------------------------------------------
# Section 13.5 -- the two gates, stated as literal predicates.
# ---------------------------------------------------------------------------
def new_work_start_gate(state, lease, own_run_id, binding, now):
    """Gate 1.  Requires the full 20-second margin."""
    if state != "LIVE_PROVED" or lease is None:
        return False, "the lease does not evaluate LIVE_PROVED"
    if lease["run_id"] != own_run_id:
        return False, "the lease is owned by another run"
    for key in (
        "package_scope_id",
        "source_binding_sha256",
        "controller_executable_identity",
    ):
        if lease[key] != binding.get(key):
            return False, "the package/source/executable binding changed"
    if lease["expires_at_epoch"] - now < constants.LEASE_START_MIN_REMAINING_SECONDS:
        return False, "less than the 20-second new-work margin remains"
    return True, "G1-G4 and the start margin hold"


IN_FLIGHT_CLOSURE_APPEND_TYPES = frozenset(
    (
        "provider_result_custody_recorded",
        "provider_request_terminal_recorded",
        "availability_probe_result_recorded",
        "provider_request_reconciled",
        "supervisor_operation_completed",
        # The Section 9.7 result-processing closure events for a result already
        # custodied.
        "mechanical_audit_recorded",
        "mechanical_audit_unusable_recorded",
        "correction_specification_recorded",
        "correction_diagnosis_recorded",
        "correction_diagnosis_rejected_recorded",
        "correction_diagnosis_validation_failed_recorded",
        "review_signal_recorded",
        "candidate_write_ahead_recorded",
        "candidate_write_ahead_aborted",
        "candidate_custody_recorded",
        "diagnosis_strategy_consumption_completed",
        "diagnosis_strategy_consumption_terminated",
        "mechanical_no_progress_recorded",
        "mechanical_change_explanation_recorded",
        "piece3_provider_work_recorded",
        "correction_batch_checkpoint_recorded",
        "semantic_scope_exhaustion_recorded",
    )
)


def in_flight_closure_append_gate(state, lease, own_run_id, binding, now):
    """Gate 2.  G1-G4 only; the 20-second margin is deliberately not required."""
    if state != "LIVE_PROVED" or lease is None:
        return False, "G1: the lease does not evaluate LIVE_PROVED"
    if lease["run_id"] != own_run_id:
        return False, "G2: the lease is owned by another run"
    if now > lease["expires_at_epoch"]:
        return False, "G3: the lease has expired"
    for key in (
        "package_scope_id",
        "source_binding_sha256",
        "controller_executable_identity",
    ):
        if lease[key] != binding.get(key):
            return False, "G4: the package/source/executable binding changed"
    return True, "G1-G4 hold"

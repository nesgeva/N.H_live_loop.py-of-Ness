#!/usr/bin/env python3
"""Launch exactly one real N.H supervisor worker beside the local browser.

This is the production entry point.  It never configures the disposable
backend, never imports rehearsal state, and never supplies a fake provider.
The browser keeps its ordinary real-controller path; only the worker's
controller subprocesses carry ``NH_SUPERVISOR_WORKER=1`` so the shared
``execute-next-claude-task`` name enters the supervisor transaction.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import threading
import time
from pathlib import Path
from types import SimpleNamespace
from typing import Callable

import server
import worker


APP_DIR = Path(__file__).resolve().parent
ROOT_DIR = APP_DIR.parent
CONTROLLER_DIR = ROOT_DIR / "controller"
CONTROLLER_PATH = CONTROLLER_DIR / "nh_loop.py"
CODEX_HOME = "/home/ness/.codex"
CODEX_CHATGPT_LOGIN_PROOF = "Logged in using ChatGPT"
CLAUDE_CONFIG_DIR = "/home/ness/.claude"
# Both verified provider executables resolve inside this one NVM bin directory.
# The launcher establishes it itself so a desktop-button process that never
# inherited NVM cannot resolve a different, unusable "codex"/"claude".
PROVIDER_BIN_DIR = "/home/ness/.nvm/versions/node/v24.18.0/bin"
WORKER_ENV = "NH_SUPERVISOR_WORKER"
PROVIDER_EXECUTION_BOUND_SECONDS = 3600
CONTROLLER_CLOSURE_GRACE_SECONDS = 300
WORKER_CONTROLLER_TIMEOUT_SECONDS = (
    PROVIDER_EXECUTION_BOUND_SECONDS + CONTROLLER_CLOSURE_GRACE_SECONDS
)
MAINTENANCE_PAUSE_BASENAME = "maintenance_pause.json"
WORKER_HEALTH_BASENAME = "worker_health.json"

if str(CONTROLLER_DIR) not in sys.path:
    sys.path.insert(0, str(CONTROLLER_DIR))

import nh_supervisor  # noqa: E402


class ProductionLaunchError(RuntimeError):
    """The real launcher could not prove a required production binding."""


def _state_dir():
    return Path(nh_supervisor.lease.resolve_state_dir(str(ROOT_DIR)))


def _atomic_state_record(path, value):
    """Write one small worker-owned state record atomically and durably."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(".%s.%d.tmp" % (path.name, os.getpid()))
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    fd = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(fd, "wb", closefd=True) as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        directory_fd = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    finally:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass


def maintenance_pause_path():
    return _state_dir() / MAINTENANCE_PAUSE_BASENAME


def worker_health_path():
    return _state_dir() / WORKER_HEALTH_BASENAME


def maintenance_pause_requested():
    """A scheduling gate only: it grants no controller or lease authority."""
    try:
        value = json.loads(maintenance_pause_path().read_text())
    except (OSError, ValueError):
        return False
    return value.get("record_version") == 1 and value.get("pause_requested") is True


def request_maintenance_pause():
    _atomic_state_record(
        maintenance_pause_path(),
        {
            "record_version": 1,
            "pause_requested": True,
            "requested_at_epoch": int(time.time()),
            "reason": "operator_authorized_live_loop_maintenance",
        },
    )


def clear_maintenance_pause():
    path = maintenance_pause_path()
    try:
        path.unlink()
    except FileNotFoundError:
        return
    directory_fd = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(directory_fd)
    finally:
        os.close(directory_fd)


def provider_environment(base=None):
    """Return the provider environment with the verified provider bin first on PATH."""
    env = dict(os.environ if base is None else base)
    inherited_path = env.get("PATH", "")
    env["PATH"] = (
        PROVIDER_BIN_DIR
        if not inherited_path
        else PROVIDER_BIN_DIR + os.pathsep + inherited_path
    )
    env["HOME"] = "/home/ness"
    env["CODEX_HOME"] = CODEX_HOME
    env["CLAUDE_CONFIG_DIR"] = CLAUDE_CONFIG_DIR
    return env


def second_model_provider():
    """The controller's SECOND-MODEL SWITCH (nh_loop.SECOND_MODEL_PROVIDER).

    Read from the controller module itself so the interface and the controller
    can never disagree about which program serves the checking roles.
    CONTROLLER_DIR is first on sys.path above.
    """
    import nh_loop
    return nh_loop.SECOND_MODEL_PROVIDER


def verify_provider_authentication(run=subprocess.run):
    """Verify auth kinds without returning, printing, or persisting credentials."""
    env = provider_environment()
    codex_state = "NOT_REQUIRED_SECOND_MODEL_CLAUDE"
    if second_model_provider() == "codex":
        try:
            codex = run(
                ["codex", "login", "status"],
                cwd=str(CONTROLLER_DIR), env=env, text=True,
                capture_output=True, timeout=30, check=False,
            )
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise ProductionLaunchError("Codex ChatGPT authentication could not be verified") from exc
        if codex.returncode != 0:
            raise ProductionLaunchError("Codex is not logged in through its current context")
        # The installed CLI reports this on stderr, not stdout, so BOTH streams are
        # read.  The proof is one whole stripped line equal to the exact current
        # ChatGPT status: a substring or a generic "logged in" would also accept an
        # API-key login, which is not the authorised route.
        reported = [
            line.strip()
            for stream in (codex.stdout, codex.stderr)
            for line in (stream or "").splitlines()
        ]
        if CODEX_CHATGPT_LOGIN_PROOF not in reported:
            raise ProductionLaunchError("Codex is not using the expected ChatGPT login context")
        codex_state = "CHATGPT_LOGIN"
    # SECOND-MODEL SWITCH (Ness, 2026-09-02): while the checking roles run on
    # Claude, a broken ChatGPT login must not block the interface.

    try:
        claude = run(
            ["claude", "auth", "status", "--json"],
            cwd=str(CONTROLLER_DIR), env=env, text=True,
            capture_output=True, timeout=30, check=False,
        )
        status = json.loads(claude.stdout)
    except (OSError, subprocess.TimeoutExpired, ValueError) as exc:
        raise ProductionLaunchError("Claude subscription authentication could not be verified") from exc
    if claude.returncode != 0 or status.get("loggedIn") is not True:
        raise ProductionLaunchError("Claude is not logged in through its current context")
    if status.get("authMethod") not in ("claude.ai", "subscription"):
        raise ProductionLaunchError("Claude is not using the expected subscription context")
    return {"codex": codex_state, "claude": "CURRENT_SUBSCRIPTION"}


class WorkerControllerRunner:
    """The worker-only real controller subprocess path.

    ``timeout`` bounds ONE controller command (one model call plus closure
    grace).  The one-shot Bundle Seven batch runs many model calls inside one
    controller command, so it is built by one_shot_batch_runner() with no
    timeout: liveness is proved by the lease heartbeat, not by this bound
    (2026-09-03 02:50: the 3900 s bound killed that batch mid-call).
    """

    def __init__(self, run=subprocess.run, timeout=WORKER_CONTROLLER_TIMEOUT_SECONDS):
        self._run = run
        self._timeout = timeout

    def __call__(self, command, payload=None):
        env = provider_environment()
        env[WORKER_ENV] = "1"
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        stdin = None if payload is None else json.dumps(payload, ensure_ascii=False)
        try:
            completed = self._run(
                [sys.executable, "-B", str(CONTROLLER_PATH), command],
                cwd=str(CONTROLLER_DIR), env=env, input=stdin, text=True,
                capture_output=True, timeout=self._timeout,
                check=False,
            )
        except subprocess.TimeoutExpired as exc:
            raise ProductionLaunchError("the real supervisor controller timed out") from exc
        report = server.parse_controller_report(completed.stdout)
        if completed.returncode != 0 or not report.get("ok"):
            errors = report.get("errors") or []
            raise ProductionLaunchError(
                errors[0] if errors else "the real supervisor controller refused"
            )
        return worker.CommandResult(command, report, completed.returncode)


def build_worker(runner, *, lease_factory=nh_supervisor.lease.SupervisorLease,
                 scheduling_factory=nh_supervisor.scheduling.SchedulingJournal,
                 initial_command="supervisor-status"):
    """Construct and acquire the single worker from authenticated controller facts."""
    if maintenance_pause_requested():
        raise ProductionLaunchError(
            "the live loop is in an explicit maintenance pause; no worker lease was acquired"
        )
    initial = runner(initial_command, None).report
    required = (
        "controller_executable_identity",
        "package_scope_id",
        "source_binding_sha256",
    )
    if any(not initial.get(key) for key in required):
        raise ProductionLaunchError(
            "supervisor-status did not provide the authenticated worker binding"
        )
    state_dir = nh_supervisor.lease.resolve_state_dir(str(ROOT_DIR))
    lease = lease_factory(state_dir)
    binding_object = SimpleNamespace(
        package_scope_id=initial["package_scope_id"],
        source_binding_sha256=initial["source_binding_sha256"],
    )
    binding = nh_supervisor.runtime.default_lease_binding(
        binding_object, initial["controller_executable_identity"]
    )
    if maintenance_pause_requested():
        raise ProductionLaunchError(
            "maintenance pause was requested before lease acquisition"
        )
    acquired, held = lease.acquire(binding)
    if acquired not in ("ACQUIRED", "RENEWED") or held is None:
        raise ProductionLaunchError(
            "the single-worker lease was not acquired (%s)" % acquired
        )
    scheduling = scheduling_factory(state_dir)
    return worker.SupervisorWorker(
        runner,
        scheduling=scheduling,
        lease=lease,
        lease_binding=binding,
        own_run_id=held["run_id"],
        binding={
            "controller_executable_identity": initial["controller_executable_identity"],
            "package_scope_id": initial["package_scope_id"],
            "source_binding_sha256": initial["source_binding_sha256"],
        },
    )


class ProductionSupervisorApp:
    """Own one worker, its heartbeat, and one browser server lifecycle."""

    def __init__(self, supervisor_worker, *, server_callable=server.serve):
        self.worker = supervisor_worker
        self.server_callable = server_callable
        self.stop_scheduling_event = threading.Event()
        self.heartbeat_stop_event = threading.Event()
        self.worker_thread = None
        self.heartbeat_thread = None
        self.retirement_complete_event = threading.Event()
        self._release_lock = threading.Lock()
        self._lease_released = False
        self.retirement_release_succeeded = False

    def _record_health(self, status, detail, *, error_type=None):
        _atomic_state_record(
            worker_health_path(),
            {
                "record_version": 1,
                "status": status,
                "detail": detail,
                "error_type": error_type,
                "recorded_at_epoch": int(time.time()),
                "pid": os.getpid(),
                "controller_executable_identity": self.worker.lease_binding.get(
                    "controller_executable_identity"
                ),
                "run_id": self.worker.own_run_id,
            },
        )

    def _release_once(self):
        with self._release_lock:
            if self._lease_released:
                return True
            released = self.worker.release()
            if released:
                self._lease_released = True
            return released

    def _retire_for_binding_change(self):
        """Stop renewal before releasing the old worker's exact lease."""
        self.stop_scheduling_event.set()
        self.heartbeat_stop_event.set()
        if (
            self.heartbeat_thread is not None
            and self.heartbeat_thread is not threading.current_thread()
            and self.heartbeat_thread.is_alive()
        ):
            self.heartbeat_thread.join()
        self.retirement_release_succeeded = self._release_once()
        self._record_health(
            "restart_required",
            "Controller changed; fresh worker required.",
        )
        self.retirement_complete_event.set()

    def _retire_for_maintenance(self):
        """Retire only between bounded steps; an in-flight step returns first."""
        self.stop_scheduling_event.set()
        self.heartbeat_stop_event.set()
        if (
            self.heartbeat_thread is not None
            and self.heartbeat_thread is not threading.current_thread()
            and self.heartbeat_thread.is_alive()
        ):
            self.heartbeat_thread.join()
        self.retirement_release_succeeded = self._release_once()
        self._record_health(
            "maintenance_paused",
            "Automatic scheduling is paused for authorized maintenance.",
        )
        self.retirement_complete_event.set()

    def _retire_after_worker_failure(self, exc):
        """A dead work thread may never leave a heartbeat claiming progress."""
        self.stop_scheduling_event.set()
        self.heartbeat_stop_event.set()
        if (
            self.heartbeat_thread is not None
            and self.heartbeat_thread is not threading.current_thread()
            and self.heartbeat_thread.is_alive()
        ):
            self.heartbeat_thread.join()
        self.retirement_release_succeeded = self._release_once()
        self._record_health(
            "failed",
            str(exc) or "the N.H work thread failed",
            error_type=type(exc).__name__,
        )
        self.retirement_complete_event.set()

    def _worker_loop(self):
        while not self.stop_scheduling_event.is_set() and not self.worker.stopped:
            if maintenance_pause_requested():
                self._retire_for_maintenance()
                return
            try:
                outcome = self.worker.step()
            except Exception as exc:  # noqa: BLE001 -- fail closed at lifecycle boundary
                self._retire_after_worker_failure(exc)
                return
            if outcome.action == worker.BINDING_CHANGE_RETIRE_ACTION:
                self._retire_for_binding_change()
                return
            # A pause requested while one bounded operation was in flight is
            # observed here, after that operation returned and before anything
            # else can be dispatched.
            if maintenance_pause_requested():
                self._retire_for_maintenance()
                return
            delay = outcome.next_delay_seconds
            if delay > 0:
                self.stop_scheduling_event.wait(
                    min(delay, nh_supervisor.constants.LEASE_HEARTBEAT_INTERVAL_SECONDS)
                )

    def _heartbeat_loop(self):
        interval = nh_supervisor.constants.LEASE_HEARTBEAT_INTERVAL_SECONDS
        while not self.heartbeat_stop_event.wait(interval):
            if not self.worker.heartbeat():
                self.stop_scheduling_event.set()
                return

    def run(self, *, port=0, no_open=False):
        self.worker_thread = threading.Thread(
            target=self._worker_loop, name="nh-supervisor-worker", daemon=True
        )
        self.heartbeat_thread = threading.Thread(
            target=self._heartbeat_loop, name="nh-supervisor-heartbeat", daemon=True
        )
        self._record_health("running", "The N.H work thread is running.")
        self.worker_thread.start()
        self.heartbeat_thread.start()
        try:
            return self.server_callable(
                port=port,
                no_open=no_open,
                stop_event=self.retirement_complete_event,
            )
        finally:
            # Stop scheduling, but keep renewing the lease until the one bounded
            # controller step already in flight has completed its terminal write.
            self.stop_scheduling_event.set()
            self.worker_thread.join()
            self.heartbeat_stop_event.set()
            self.heartbeat_thread.join()
            self._release_once()

    def run_one_controller_command(self, runner, command):
        """Keep the proved worker lease alive for one explicit operator command."""
        self.heartbeat_thread = threading.Thread(
            target=self._heartbeat_loop,
            name="nh-supervisor-heartbeat",
            daemon=True,
        )
        self._record_health("running", "The N.H one-shot work item is running.")
        self.heartbeat_thread.start()
        try:
            result = runner(command, None)
            self._record_health("completed", "The N.H one-shot work item completed.")
            return result.returncode
        except Exception as exc:
            self._record_health(
                "failed",
                str(exc) or "The N.H one-shot work item failed.",
                error_type=type(exc).__name__,
            )
            raise
        finally:
            self.heartbeat_stop_event.set()
            self.heartbeat_thread.join()
            self._release_once()


def one_shot_batch_runner(run=subprocess.run):
    """The runner for --bundle-seven-question-validation-once: no per-command bound."""
    return WorkerControllerRunner(run=run, timeout=None)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Run one real N.H supervisor worker and its local browser"
    )
    parser.add_argument("--port", type=int, default=0)
    parser.add_argument("--no-open", action="store_true")
    parser.add_argument("--request-maintenance-pause", action="store_true")
    parser.add_argument("--clear-maintenance-pause", action="store_true")
    parser.add_argument(
        "--bundle-seven-question-validation-once",
        action="store_true",
        help="run one complete Bundle Seven validation under the proved worker lease",
    )
    args = parser.parse_args(argv)
    if args.request_maintenance_pause and args.clear_maintenance_pause:
        raise ProductionLaunchError("choose request or clear maintenance pause, not both")
    if args.request_maintenance_pause:
        request_maintenance_pause()
        return 0
    if args.clear_maintenance_pause:
        clear_maintenance_pause()
        return 0
    verify_provider_authentication()
    runner = (
        one_shot_batch_runner()
        if args.bundle_seven_question_validation_once
        else WorkerControllerRunner()
    )
    supervisor_worker = build_worker(
        runner,
        initial_command=(
            "bundle-seven-supervisor-status"
            if args.bundle_seven_question_validation_once
            else "supervisor-status"
        ),
    )
    app = ProductionSupervisorApp(supervisor_worker)
    if args.bundle_seven_question_validation_once:
        return app.run_one_controller_command(
            runner, "bundle-seven-question-validation"
        )
    return app.run(
        port=args.port, no_open=args.no_open
    )


if __name__ == "__main__":
    raise SystemExit(main())

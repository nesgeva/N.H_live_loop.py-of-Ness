import threading
import time
import unittest
import sys
import os
import tempfile
from pathlib import Path
from unittest import mock

UI_DIR = Path(__file__).resolve().parent
if str(UI_DIR) not in sys.path:
    sys.path.insert(0, str(UI_DIR))

import production  # noqa: E402
import worker  # noqa: E402


OLD = "1" * 64
CURRENT = "2" * 64


def status(identity=OLD, *, state="WORKING", next_command="process-custodied-provider-result"):
    return {
        "command": "supervisor-status",
        "ok": True,
        "journal_authentication_proved": True,
        "authenticated_state_current": True,
        "source_state_current": True,
        "workflow_state": state,
        "next_command": next_command,
        "controller_executable_identity": identity,
        "package_scope_id": "A19",
        "source_binding_sha256": "a" * 64,
        "run_lease": {
            "lease_state": "INVALID_UNPROVED" if identity != OLD else "LIVE_PROVED",
            "live_proved": identity == OLD,
        },
    }


class FakeLease:
    def __init__(self):
        self.heartbeats = 0
        self.releases = 0
        self.released = threading.Event()

    def heartbeat(self, _binding, now=None):
        self.heartbeats += 1
        return True, "LIVE_PROVED"

    def release(self, _binding, now=None):
        self.releases += 1
        self.released.set()
        return True


class SequenceRunner:
    def __init__(self, reports, provider_block=None):
        self.reports = list(reports)
        self.calls = []
        self.provider_block = provider_block
        self.result_durable = threading.Event()

    def __call__(self, command, _payload=None):
        self.calls.append(command)
        if command == "supervisor-status":
            return worker.CommandResult(command, self.reports.pop(0))
        if self.provider_block is not None:
            self.provider_block.wait(2)
            self.result_durable.set()
        return worker.CommandResult(command, {"ok": True, "outcome": "completed"})


def make_worker(runner, lease):
    instance = worker.SupervisorWorker(
        runner,
        lease=lease,
        lease_binding={
            "controller_executable_identity": OLD,
            "package_scope_id": "A19",
            "source_binding_sha256": "a" * 64,
        },
        own_run_id="run-old",
    )
    instance.start_gate_open = lambda: (True, "open")
    return instance


class IdentityMismatchRetirementTests(unittest.TestCase):
    def run_app(self, instance):
        app = None

        def server_callable(**_kwargs):
            self.assertTrue(app.retirement_complete_event.wait(2))
            return 0

        app = production.ProductionSupervisorApp(
            instance, server_callable=server_callable
        )
        with tempfile.TemporaryDirectory() as folder, mock.patch.object(
            production, "worker_health_path", return_value=Path(folder) / "health.json"
        ), mock.patch.object(
            production, "maintenance_pause_requested", return_value=False
        ), mock.patch.object(
            production.nh_supervisor.constants,
            "LEASE_HEARTBEAT_INTERVAL_SECONDS",
            0.01,
        ):
            app.run(no_open=True)
        return app

    def test_matching_identity_runs_the_same_next_operation(self):
        lease = FakeLease()
        runner = SequenceRunner([status()])
        outcome = make_worker(runner, lease).step()
        self.assertEqual("ran_command", outcome.action)
        self.assertEqual(
            ["supervisor-status", "process-custodied-provider-result"], runner.calls
        )

    def test_one_shot_bundle_seven_command_keeps_and_releases_worker_lease(self):
        lease = FakeLease()
        runner = SequenceRunner([])
        instance = make_worker(runner, lease)
        app = production.ProductionSupervisorApp(instance)
        with tempfile.TemporaryDirectory() as folder, mock.patch.object(
            production, "worker_health_path", return_value=Path(folder) / "health.json"
        ), mock.patch.object(
            production.nh_supervisor.constants,
            "LEASE_HEARTBEAT_INTERVAL_SECONDS",
            0.01,
        ):
            code = app.run_one_controller_command(
                runner, "bundle-seven-question-validation"
            )
        self.assertEqual(0, code)
        self.assertEqual(["bundle-seven-question-validation"], runner.calls)
        self.assertEqual(1, lease.releases)

    def test_idle_mismatch_dispatches_nothing_and_retires_with_release(self):
        lease = FakeLease()
        runner = SequenceRunner(
            [status(CURRENT, state="SAFETY_HOLD", next_command=None)]
        )
        app = self.run_app(make_worker(runner, lease))
        self.assertEqual(["supervisor-status"], runner.calls)
        self.assertTrue(app.worker.stopped)
        self.assertTrue(app.heartbeat_stop_event.is_set())
        self.assertTrue(lease.released.is_set())
        self.assertTrue(app.retirement_release_succeeded)
        self.assertEqual(1, lease.releases)

    def test_mismatch_retires_even_when_source_currentness_is_false(self):
        """The binding change itself makes ordinary proved-status false."""
        lease = FakeLease()
        report = status(CURRENT, state="SAFETY_HOLD", next_command=None)
        report["source_state_current"] = False
        runner = SequenceRunner([report])
        app = self.run_app(make_worker(runner, lease))
        self.assertEqual(["supervisor-status"], runner.calls)
        self.assertTrue(app.worker.stopped)
        self.assertTrue(app.heartbeat_stop_event.is_set())
        self.assertTrue(lease.released.is_set())
        self.assertTrue(app.retirement_release_succeeded)

    def test_in_flight_step_finishes_before_retirement_and_no_next_dispatch(self):
        lease = FakeLease()
        provider_done = threading.Event()
        runner = SequenceRunner(
            [status(), status(CURRENT, state="SAFETY_HOLD", next_command=None)],
            provider_block=provider_done,
        )
        instance = make_worker(runner, lease)
        holder = {}

        def server_callable(**_kwargs):
            self.assertTrue(runner.provider_block is provider_done)
            provider_done.set()
            self.assertTrue(holder["app"].retirement_complete_event.wait(2))
            return 0

        app = production.ProductionSupervisorApp(
            instance, server_callable=server_callable
        )
        holder["app"] = app
        with tempfile.TemporaryDirectory() as folder, mock.patch.object(
            production, "worker_health_path", return_value=Path(folder) / "health.json"
        ), mock.patch.object(
            production, "maintenance_pause_requested", return_value=False
        ), mock.patch.object(
            production.nh_supervisor.constants,
            "LEASE_HEARTBEAT_INTERVAL_SECONDS",
            0.01,
        ):
            app.run(no_open=True)
        self.assertTrue(runner.result_durable.is_set())
        self.assertEqual(1, runner.calls.count("process-custodied-provider-result"))
        self.assertEqual(
            [
                "supervisor-status",
                "process-custodied-provider-result",
                "supervisor-status",
            ],
            runner.calls,
        )
        self.assertTrue(lease.released.is_set())

    def test_retired_worker_cannot_repeat_safety_hold_heartbeat_cycles(self):
        lease = FakeLease()
        runner = SequenceRunner(
            [status(CURRENT, state="SAFETY_HOLD", next_command=None)]
        )
        app = self.run_app(make_worker(runner, lease))
        calls = list(runner.calls)
        heartbeats = lease.heartbeats
        time.sleep(0.04)
        self.assertEqual(calls, runner.calls)
        self.assertEqual(heartbeats, lease.heartbeats)
        self.assertTrue(app.retirement_complete_event.is_set())

    def test_release_is_completed_before_a_fresh_owner_is_eligible(self):
        with tempfile.TemporaryDirectory() as folder:
            lease = production.nh_supervisor.lease.SupervisorLease(
                Path(folder) / "state"
            )
            hooks = production.nh_supervisor.lease.LeaseHooks()
            old_binding = {
                "pid": os.getpid(),
                "process_start_ticks": hooks.process_start_ticks(os.getpid()),
                "boot_id_sha256": hooks.boot_id_sha256(),
                "controller_executable_identity": OLD,
                "package_scope_id": "A19",
                "source_binding_sha256": "a" * 64,
            }
            current_binding = dict(old_binding)
            current_binding["controller_executable_identity"] = CURRENT
            self.assertEqual("ACQUIRED", lease.acquire(old_binding, now=100)[0])
            self.assertEqual(
                "SAFETY_HOLD", lease.acquire(current_binding, now=101)[0]
            )
            self.assertTrue(lease.release(old_binding, now=102))
            self.assertEqual("ACQUIRED", lease.acquire(current_binding, now=103)[0])

    def test_work_thread_failure_is_visible_and_releases_the_lease(self):
        lease = FakeLease()

        class FailingRunner(SequenceRunner):
            def __call__(self, command, payload=None):
                if command != "supervisor-status":
                    self.calls.append(command)
                    raise RuntimeError("proved work-thread failure")
                return super().__call__(command, payload)

        runner = FailingRunner([status()])
        instance = make_worker(runner, lease)
        app = None
        with tempfile.TemporaryDirectory() as folder:
            health = Path(folder) / "health.json"

            def server_callable(**_kwargs):
                self.assertTrue(app.retirement_complete_event.wait(2))
                return 0

            app = production.ProductionSupervisorApp(
                instance, server_callable=server_callable
            )
            with mock.patch.object(
                production, "worker_health_path", return_value=health
            ), mock.patch.object(
                production, "maintenance_pause_requested", return_value=False
            ), mock.patch.object(
                production.nh_supervisor.constants,
                "LEASE_HEARTBEAT_INTERVAL_SECONDS",
                0.01,
            ):
                app.run(no_open=True)
            record = __import__("json").loads(health.read_text())
        self.assertEqual(record["status"], "failed")
        self.assertIn("proved work-thread failure", record["detail"])
        self.assertTrue(lease.released.is_set())
        self.assertEqual(1, runner.calls.count("process-custodied-provider-result"))

    def test_maintenance_pause_waits_for_bounded_step_then_releases(self):
        lease = FakeLease()
        operation_done = threading.Event()
        runner = SequenceRunner([status()], provider_block=operation_done)
        instance = make_worker(runner, lease)
        app = None
        checks = iter([False, True])

        def pause_requested():
            return next(checks, True)

        with tempfile.TemporaryDirectory() as folder:
            health = Path(folder) / "health.json"

            def server_callable(**_kwargs):
                self.assertFalse(lease.released.is_set())
                operation_done.set()
                self.assertTrue(app.retirement_complete_event.wait(2))
                return 0

            app = production.ProductionSupervisorApp(
                instance, server_callable=server_callable
            )
            with mock.patch.object(
                production, "worker_health_path", return_value=health
            ), mock.patch.object(
                production,
                "maintenance_pause_requested",
                side_effect=pause_requested,
            ), mock.patch.object(
                production.nh_supervisor.constants,
                "LEASE_HEARTBEAT_INTERVAL_SECONDS",
                0.01,
            ):
                app.run(no_open=True)
            record = __import__("json").loads(health.read_text())
        self.assertTrue(runner.result_durable.is_set())
        self.assertEqual(1, runner.calls.count("process-custodied-provider-result"))
        self.assertEqual(record["status"], "maintenance_paused")
        self.assertTrue(lease.released.is_set())


if __name__ == "__main__":
    unittest.main()

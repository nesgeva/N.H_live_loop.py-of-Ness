import tempfile
import unittest
from pathlib import Path

import supervisor
import worker


def result(command, report, returncode=0):
    return worker.CommandResult(command, "output for " + command, report, returncode)


class FakeRunner:
    def __init__(
        self,
        execute_reports=None,
        diagnosis_reports=None,
        questions=0,
        recovery_outcome="WAIT",
    ):
        self.calls = []
        self.execute_reports = list(execute_reports or [])
        self.diagnosis_reports = list(diagnosis_reports or [])
        self.questions = questions
        self.workflow_state = "WORKING"
        self.next_command = "execute-next-claude-task"
        self.recovery_outcome = recovery_outcome
        self.event_seq = 20

    def supervisor_status(self):
        return {
            "command": "supervisor-status",
            "ok": True,
            "journal_authentication_proved": True,
            "authenticated_state_current": True,
            "source_state_current": True,
            "workflow_state": self.workflow_state,
            "next_command": self.next_command,
            "package_scope_id": "pkg_scope",
            "controller_executable_identity": "1" * 64,
            "source_binding_sha256": "a" * 64,
            "candidate_path": "05_ACTIVE_CANDIDATE/pkg_v1_5_CANDIDATE.md",
            "candidate_sha256": "c" * 64,
            "candidate_bytes": 100,
            "authenticated_event_seq": self.event_seq,
            "authenticated_tail_sha256": ("%x" % (self.event_seq % 16)) * 64,
            "state_recorded_at": "2026-08-18T00:00:00Z",
            "run_lease": {
                "live_proved": True,
                "run_id": "run_test",
                "expires_at": "2026-08-18T00:00:35Z",
            },
            "controller_confirmed_change_events": [],
        }

    def __call__(self, command, payload):
        self.calls.append(command)
        if command == "interview-status":
            return result(
                command,
                {
                    "ok": True,
                    "deliverable_question_count": self.questions,
                    "open_group_index": None,
                    "validation_package_scope_id": "pkg_scope",
                    "source_binding_sha256": "a" * 64,
                    "source_head_sha": "b" * 40,
                },
            )
        if command == "interview-gate":
            return result(command, {"ok": True, "mechanical_path_unlocked": True})
        if command == "supervisor-status":
            return result(command, self.supervisor_status())
        if command == "supervisor-operation-status":
            return result(
                command,
                {
                    "ok": True,
                    "command": command,
                    "recovery_outcome": self.recovery_outcome,
                    "recovered_workflow_state": (
                        "NEEDS_USER_ACTION"
                        if self.recovery_outcome == "NEEDS_USER_ACTION"
                        else "SAFETY_HOLD"
                        if self.recovery_outcome == "SAFETY_HOLD"
                        else "WORKING"
                    ),
                    "next_command": None,
                },
            )
        if command == "execute-next-claude-task":
            observed = self.execute_reports.pop(0)
            self.event_seq += 2
            if observed.report.get("stop_reason") == "CORRECTION_BATCH_LIMIT":
                self.workflow_state = "DIAGNOSING"
                self.next_command = "diagnose-next-correction-batch"
            elif observed.report.get("final_design_audit_verdict") == "PASS":
                self.workflow_state = "READY_FOR_ACCEPTANCE"
                self.next_command = None
            return observed
        if command == "diagnose-next-correction-batch":
            observed = self.diagnosis_reports.pop(0)
            self.event_seq += 2
            if observed.report.get("next_workflow_state") == "WORKING":
                self.workflow_state = "WORKING"
                self.next_command = "execute-next-claude-task"
            return observed
        raise AssertionError(command)


class WorkerTests(unittest.TestCase):
    def journal(self, tmp):
        return supervisor.DurableSupervisorJournal(Path(tmp) / "events.jsonl")

    def test_real_question_is_the_only_design_interruption(self):
        with tempfile.TemporaryDirectory() as tmp:
            runner = FakeRunner(questions=1)
            engine = worker.SupervisorWorker(runner, self.journal(tmp))
            outcome = engine.step()
            self.assertEqual(outcome.state, supervisor.WorkflowState.NEEDS_NESS_DECISION)
            self.assertNotIn("execute-next-claude-task", runner.calls)

    def test_batch_limit_flows_to_diagnosis_then_new_work(self):
        with tempfile.TemporaryDirectory() as tmp:
            blocked = result(
                "execute-next-claude-task",
                {
                    "ok": False,
                    "stop_reason": "CORRECTION_BATCH_LIMIT",
                    "final_design_audit_verdict": "BLOCKED",
                    "final_candidate_chain_verified": True,
                    "selected_package_scope_id": "pkg_scope",
                    "final_candidate_path": "05_ACTIVE_CANDIDATE/pkg_v1_5_CANDIDATE.md",
                    "final_candidate_sha256": "c" * 64,
                    "final_candidate_bytes": 100,
                    "audit_history": [],
                    "correction_history": [],
                },
                returncode=1,
            )
            diagnosed = result(
                "diagnose-next-correction-batch",
                {
                    "ok": True,
                    "stop_reason": "DIAGNOSIS_COMPLETE",
                    "next_workflow_state": "WORKING",
                    "selected_package_scope_id": "pkg_scope",
                },
            )
            runner = FakeRunner([blocked], [diagnosed])
            journal = self.journal(tmp)
            engine = worker.SupervisorWorker(runner, journal)
            first = engine.step()
            second = engine.step()
            self.assertEqual(first.state, supervisor.WorkflowState.DIAGNOSING)
            self.assertEqual(second.state, supervisor.WorkflowState.WORKING)
            self.assertIn("diagnose-next-correction-batch", runner.calls)
            self.assertEqual(supervisor.latest_snapshot(journal.read()).state, supervisor.WorkflowState.WORKING)

    def test_proved_pass_waits_for_explicit_acceptance(self):
        with tempfile.TemporaryDirectory() as tmp:
            passed = result(
                "execute-next-claude-task",
                {
                    "ok": True,
                    "stop_reason": "PASS",
                    "final_design_audit_verdict": "PASS",
                    "final_candidate_chain_verified": True,
                    "selected_package_scope_id": "pkg_scope",
                    "final_candidate_path": "05_ACTIVE_CANDIDATE/pkg_v1_6_CANDIDATE.md",
                    "final_candidate_sha256": "d" * 64,
                    "final_candidate_bytes": 120,
                    "audit_history": [],
                    "correction_history": [],
                },
            )
            runner = FakeRunner([passed])
            engine = worker.SupervisorWorker(runner, self.journal(tmp))
            outcome = engine.step()
            self.assertEqual(outcome.state, supervisor.WorkflowState.READY_FOR_ACCEPTANCE)
            self.assertEqual(outcome.action, "wait_for_explicit_acceptance")

    def test_interrupted_operation_is_not_blindly_retried(self):
        with tempfile.TemporaryDirectory() as tmp:
            journal = self.journal(tmp)
            journal.append(
                "controller_run_started",
                {
                    "operation_id": "op_incomplete",
                    "command": "execute-next-claude-task",
                    "operation_envelope": {
                        "supervisor_operation_id": "op_incomplete",
                        "supervisor_command": "execute-next-claude-task",
                        "controller_executable_identity": "1" * 64,
                        "package_scope_id": "pkg_scope",
                        "source_binding_sha256": "a" * 64,
                        "candidate_path": "05_ACTIVE_CANDIDATE/pkg_v1_5_CANDIDATE.md",
                        "candidate_sha256": "c" * 64,
                        "candidate_bytes": 100,
                        "pre_state_sha256": "b" * 64,
                        "input_envelope_sha256": "c" * 64,
                    },
                    "binding": {
                        "controller_executable_identity": "1" * 64,
                        "source_binding_sha256": "a" * 64,
                        "package_scope_id": "pkg_scope",
                        "candidate_path": "05_ACTIVE_CANDIDATE/pkg_v1_5_CANDIDATE.md",
                        "candidate_sha256": "c" * 64,
                        "candidate_bytes": 100,
                        "controller_report_sha256": "d" * 64,
                    },
                },
            )
            runner = FakeRunner()
            engine = worker.SupervisorWorker(runner, journal)
            outcome = engine.step()
            self.assertEqual(outcome.state, supervisor.WorkflowState.WAITING_RECOVERING)
            self.assertIn("supervisor-operation-status", runner.calls)
            self.assertNotIn("execute-next-claude-task", runner.calls)
            self.assertLess(
                runner.calls.index("supervisor-operation-status"),
                len(runner.calls),
            )

    def test_technical_failure_uses_backoff(self):
        with tempfile.TemporaryDirectory() as tmp:
            failed = result(
                "execute-next-claude-task",
                {
                    "ok": False,
                    "stop_reason": "CODEX_TECHNICAL_FAILURE",
                    "final_design_audit_verdict": None,
                    "final_candidate_chain_verified": True,
                    "audit_history": [],
                    "correction_history": [],
                },
                returncode=1,
            )
            runner = FakeRunner([failed])
            engine = worker.SupervisorWorker(
                runner,
                self.journal(tmp),
                recovery_base_seconds=3,
                recovery_max_seconds=30,
            )
            outcome = engine.step()
            self.assertEqual(outcome.state, supervisor.WorkflowState.WAITING_RECOVERING)
            self.assertEqual(outcome.next_delay_seconds, 3)

    def test_backoff_survives_restart_and_increments_after_retry(self):
        with tempfile.TemporaryDirectory() as tmp:
            failed_reports = [
                result(
                    "execute-next-claude-task",
                    {
                        "ok": False,
                        "stop_reason": "CODEX_TECHNICAL_FAILURE",
                        "final_design_audit_verdict": None,
                        "final_candidate_chain_verified": True,
                        "audit_history": [],
                        "correction_history": [],
                    },
                    returncode=1,
                )
                for _ in range(2)
            ]
            runner = FakeRunner(failed_reports)
            journal = self.journal(tmp)
            clock = [100.0]
            first_engine = worker.SupervisorWorker(
                runner,
                journal,
                recovery_base_seconds=3,
                recovery_max_seconds=30,
                now=lambda: clock[0],
            )
            first = first_engine.step()
            self.assertEqual(first.next_delay_seconds, 3)
            first_engine.lease.release()

            clock[0] = 101.0
            restarted = worker.SupervisorWorker(
                runner,
                journal,
                recovery_base_seconds=3,
                recovery_max_seconds=30,
                now=lambda: clock[0],
            )
            waiting = restarted.step()
            self.assertEqual(waiting.action, "wait_until_durable_retry_time")
            self.assertEqual(runner.calls.count("execute-next-claude-task"), 1)

            clock[0] = 103.0
            second = restarted.step()
            self.assertEqual(second.next_delay_seconds, 6)
            self.assertEqual(runner.calls.count("execute-next-claude-task"), 2)

    def test_exact_nonretrying_recovery_outcomes_do_not_schedule_backoff(self):
        for recovery_outcome, expected in (
            ("NEEDS_USER_ACTION", supervisor.WorkflowState.NEEDS_USER_ACTION),
            ("SAFETY_HOLD", supervisor.WorkflowState.SAFETY_HOLD),
        ):
            with self.subTest(recovery_outcome=recovery_outcome):
                with tempfile.TemporaryDirectory() as tmp:
                    journal = self.journal(tmp)
                    runner = FakeRunner(recovery_outcome=recovery_outcome)
                    status = runner.supervisor_status()
                    envelope = worker.operation_envelope(
                        "execute-next-claude-task",
                        {"validation_package_scope_id": "pkg_scope"},
                        status,
                    )
                    journal.append(
                        "controller_run_started",
                        {
                            "operation_id": envelope["supervisor_operation_id"],
                            "command": "execute-next-claude-task",
                            "operation_envelope": envelope,
                            "binding": supervisor.operational_binding(status),
                        },
                    )
                    outcome = worker.SupervisorWorker(runner, journal).step()
                    self.assertEqual(outcome.state, expected)
                    self.assertFalse(
                        any(
                            event["event_type"] == "technical_backoff_scheduled"
                            for event in journal.read()
                        )
                    )

    def test_possible_ness_signal_does_not_interrupt_before_piece3(self):
        with tempfile.TemporaryDirectory() as tmp:
            diagnosed = result(
                "diagnose-next-correction-batch",
                {
                    "ok": True,
                    "stop_reason": "QUESTION_VALIDATION_REQUIRED",
                    "piece3_question_validation_required": True,
                    "next_workflow_state": "QUESTION_VALIDATION",
                    "selected_package_scope_id": "pkg_scope",
                },
            )
            runner = FakeRunner([], [diagnosed])
            runner.workflow_state = "DIAGNOSING"
            runner.next_command = "diagnose-next-correction-batch"
            outcome = worker.SupervisorWorker(runner, self.journal(tmp)).step()
            self.assertEqual(outcome.state, supervisor.WorkflowState.WORKING)
            self.assertEqual(outcome.action, "continue_piece3_validation")


if __name__ == "__main__":
    unittest.main()

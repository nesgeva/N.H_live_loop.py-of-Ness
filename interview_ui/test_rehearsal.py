import tempfile
import unittest
from pathlib import Path
from unittest import mock

import server
import supervisor
import worker


def command_result(command, report, returncode=0):
    return worker.CommandResult(command, "verified output for " + command, report, returncode)


def blocked_finding(number):
    return {
        "title": "Mechanical recovery problem %d" % number,
        "explanation": "The design does not yet preserve one required recovery fact.",
        "candidate_evidence": "Exact candidate evidence %d" % number,
        "source_evidence": ["01_AUTHORITATIVE/example.md"],
        "severity": "IMPORTANT",
        "route": "claude_mechanical",
        "finding_ref": "f_%02d" % number,
        "plain_language_problem": "After a crash, N.H could lose track of recovery step %d." % number,
        "plain_language_impact": "N.H must remember that step instead of guessing after it restarts.",
    }


def audit(round_number, verdict, findings):
    return {
        "correction_round": round_number,
        "candidate_path": "05_ACTIVE_CANDIDATE/pkg_v1_%d_CANDIDATE.md" % round_number,
        "candidate_sha256": ("%x" % ((round_number % 15) + 1)) * 64,
        "candidate_bytes": 100 + round_number,
        "verdict": verdict,
        "highest_severity": "NONE" if verdict == "PASS" else "IMPORTANT",
        "ok": True,
        "findings": findings,
    }


def correction(round_number):
    return {
        "correction_round": round_number,
        "blocked_candidate_path": "05_ACTIVE_CANDIDATE/pkg_v1_%d_CANDIDATE.md" % (round_number - 1),
        "blocked_candidate_sha256": ("%x" % (((round_number - 1) % 15) + 1)) * 64,
        "next_candidate_path": "05_ACTIVE_CANDIDATE/pkg_v1_%d_CANDIDATE.md" % round_number,
        "new_candidate_sha256": ("%x" % ((round_number % 15) + 1)) * 64,
        "new_candidate_bytes": 100 + round_number,
        "correction_finding_count": 1,
        "correction_finding_refs": ["f_%02d" % round_number],
        "correction_specification_sha256": "e" * 64,
        "plain_language_change": "Claude made N.H save recovery step %d in the correction candidate." % round_number,
        "plain_language_impact": "This is intended to prevent that step from being lost after a crash.",
        "promoted": True,
        "custody_recorded": True,
    }


class RehearsalRunner:
    def __init__(self):
        self.execute_count = 0
        self.calls = []
        self.workflow_state = "WORKING"
        self.next_command = "execute-next-claude-task"
        self.change_events = []

    def _observe_report(self, report):
        for item in supervisor.change_feed_from_report(report):
            event = {
                "controller_authenticated": True,
                "recorded_at": "2026-08-18T00:00:%02dZ" % len(self.change_events),
                "id": "event-%d-%s" % (len(self.change_events) + 1, item["id"]),
                "kind": item["kind"],
                "title": item["title"],
                "what": item["what"],
                "why": item["why"],
                "status": item["status"],
                "technical": item["technical"],
            }
            self.change_events.append(event)

    def _supervisor_status(self):
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
            "candidate_path": "05_ACTIVE_CANDIDATE/pkg_v1_%d_CANDIDATE.md"
            % (6 if self.workflow_state == "READY_FOR_ACCEPTANCE" else 5),
            "candidate_sha256": ("7" if self.workflow_state == "READY_FOR_ACCEPTANCE" else "6") * 64,
            "candidate_bytes": 106 if self.workflow_state == "READY_FOR_ACCEPTANCE" else 105,
            "authenticated_event_seq": 50 + len(self.change_events),
            "authenticated_tail_sha256": (
                "%x" % ((50 + len(self.change_events)) % 16)
            ) * 64,
            "state_recorded_at": "2026-08-18T00:01:00Z",
            "run_lease": {
                "live_proved": self.workflow_state != "READY_FOR_ACCEPTANCE",
                "run_id": "run_rehearsal",
                "expires_at": "2026-08-18T00:01:35Z",
            },
            "controller_confirmed_change_events": list(self.change_events),
        }

    def __call__(self, command, payload):
        self.calls.append(command)
        if command == "interview-status":
            return command_result(
                command,
                {
                    "ok": True,
                    "deliverable_question_count": 0,
                    "open_group_index": None,
                    "validation_package_scope_id": "pkg_scope",
                    "source_binding_sha256": "a" * 64,
                    "source_head_sha": "b" * 40,
                },
            )
        if command == "interview-gate":
            return command_result(command, {"ok": True, "mechanical_path_unlocked": True})
        if command == "supervisor-status":
            return command_result(command, self._supervisor_status())
        if command == "diagnose-next-correction-batch":
            observed = command_result(
                command,
                {
                    "ok": True,
                    "stop_reason": "DIAGNOSIS_COMPLETE",
                    "next_workflow_state": "WORKING",
                    "selected_package_scope_id": "pkg_scope",
                    "diagnosis_strategy_sha256": "d" * 64,
                    "audit_history": [],
                    "correction_history": [],
                },
            )
            self.workflow_state = "WORKING"
            self.next_command = "execute-next-claude-task"
            return observed
        if command == "execute-next-claude-task":
            self.execute_count += 1
            if self.execute_count == 1:
                audits = [audit(number, "BLOCKED", [blocked_finding(number + 1)]) for number in range(6)]
                observed = command_result(
                    command,
                    {
                        "ok": True,
                        "stop_reason": "CORRECTION_BATCH_LIMIT",
                        "next_workflow_state": "DIAGNOSING",
                        "final_design_audit_verdict": "BLOCKED",
                        "final_candidate_chain_verified": True,
                        "selected_package_scope_id": "pkg_scope",
                        "final_candidate_path": "05_ACTIVE_CANDIDATE/pkg_v1_5_CANDIDATE.md",
                        "final_candidate_sha256": "6" * 64,
                        "final_candidate_bytes": 105,
                        "audit_history": audits,
                        "correction_history": [correction(number) for number in range(1, 6)],
                    },
                )
                self._observe_report(observed.report)
                self.workflow_state = "DIAGNOSING"
                self.next_command = "diagnose-next-correction-batch"
                return observed
            observed = command_result(
                command,
                {
                    "ok": True,
                    "stop_reason": "PASS",
                    "next_workflow_state": "READY_FOR_ACCEPTANCE",
                    "final_design_audit_verdict": "PASS",
                    "final_candidate_chain_verified": True,
                    "selected_package_scope_id": "pkg_scope",
                    "final_candidate_path": "05_ACTIVE_CANDIDATE/pkg_v1_6_CANDIDATE.md",
                    "final_candidate_sha256": "7" * 64,
                    "final_candidate_bytes": 106,
                    "audit_history": [
                        audit(5, "BLOCKED", [blocked_finding(6)]),
                        audit(6, "PASS", []),
                    ],
                    "correction_history": [correction(6)],
                },
            )
            self._observe_report(observed.report)
            self.workflow_state = "READY_FOR_ACCEPTANCE"
            self.next_command = None
            return observed
        raise AssertionError(command)


class FullLocalRehearsalTests(unittest.TestCase):
    def test_batch_diagnosis_continuation_feed_and_acceptance_transition(self):
        with tempfile.TemporaryDirectory() as tmp:
            journal_path = Path(tmp) / "supervisor.jsonl"
            journal = supervisor.DurableSupervisorJournal(journal_path)
            runner = RehearsalRunner()
            engine = worker.SupervisorWorker(runner, journal)

            first = engine.step()
            second = engine.step()
            third = engine.step()

            self.assertEqual(first.state, supervisor.WorkflowState.DIAGNOSING)
            self.assertEqual(second.state, supervisor.WorkflowState.WORKING)
            self.assertEqual(third.state, supervisor.WorkflowState.READY_FOR_ACCEPTANCE)
            self.assertEqual(runner.calls.count("execute-next-claude-task"), 2)
            self.assertEqual(runner.calls.count("diagnose-next-correction-batch"), 1)

            with mock.patch.object(server, "SUPERVISOR_JOURNAL", journal_path):
                proved_status = runner("supervisor-status", None).report
                snapshot, feed, evidence = server.read_supervisor_view(
                    {"deliverable_question_count": 0},
                    {"mechanical_path_unlocked": True},
                    proved_status,
                )

            self.assertTrue(evidence["controller_authenticated"])
            self.assertEqual(snapshot.state, supervisor.WorkflowState.READY_FOR_ACCEPTANCE)
            self.assertEqual(sum(item["kind"] == "candidate_changed" for item in feed), 6)
            self.assertEqual(sum(item["kind"] == "audit_passed" for item in feed), 1)
            self.assertTrue(all("fixed" not in item["what"].lower() for item in feed if item["kind"] == "candidate_changed"))
            summary = supervisor.summary_from_feed(feed)
            self.assertEqual(summary["corrections_made"], 6)
            self.assertIsNone(summary["policy_change_proved_absent"])


if __name__ == "__main__":
    unittest.main()

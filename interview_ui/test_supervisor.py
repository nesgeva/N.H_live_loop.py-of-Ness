import json
import os
import tempfile
import threading
import unittest
from pathlib import Path

import supervisor


def event_binding(report_sha="d" * 64):
    return {
        "controller_executable_identity": "1" * 64,
        "source_binding_sha256": "2" * 64,
        "package_scope_id": "pkg_scope",
        "candidate_path": "05_ACTIVE_CANDIDATE/test_v1_0_CANDIDATE.md",
        "candidate_sha256": "3" * 64,
        "candidate_bytes": 100,
        "controller_report_sha256": report_sha,
    }


class SupervisorStateTests(unittest.TestCase):
    def test_question_interrupts_mechanical_work(self):
        state = supervisor.workflow_state_from_reports(
            {"deliverable_question_count": 1, "open_group_index": None},
            {"mechanical_path_unlocked": True},
        )
        self.assertEqual(state, supervisor.WorkflowState.NEEDS_NESS_DECISION)

    def test_fifth_round_stop_enters_diagnosis(self):
        state = supervisor.workflow_state_from_reports(
            {"deliverable_question_count": 0, "open_group_index": None},
            {"mechanical_path_unlocked": True},
            {
                "stop_reason": "CORRECTION_ROUND_LIMIT",
                "final_design_audit_verdict": "BLOCKED",
                "final_candidate_chain_verified": True,
            },
        )
        self.assertEqual(state, supervisor.WorkflowState.DIAGNOSING)

    def test_only_terminally_proved_pass_is_ready_for_acceptance(self):
        base = {
            "stop_reason": "PASS",
            "final_design_audit_verdict": "PASS",
            "final_candidate_chain_verified": False,
        }
        state = supervisor.workflow_state_from_reports({}, {}, base)
        self.assertNotEqual(state, supervisor.WorkflowState.READY_FOR_ACCEPTANCE)
        base["final_candidate_chain_verified"] = True
        state = supervisor.workflow_state_from_reports({}, {}, base)
        self.assertEqual(state, supervisor.WorkflowState.READY_FOR_ACCEPTANCE)

    def test_technical_failure_waits_and_recovers(self):
        state = supervisor.workflow_state_from_reports(
            {}, {}, {"stop_reason": "CODEX_TECHNICAL_FAILURE"}
        )
        self.assertEqual(state, supervisor.WorkflowState.WAITING_RECOVERING)


class SupervisorJournalTests(unittest.TestCase):
    def test_journal_round_trip_and_snapshot(self):
        with tempfile.TemporaryDirectory() as tmp:
            journal = supervisor.DurableSupervisorJournal(Path(tmp) / "events.jsonl")
            journal.append(
                "workflow_state_changed",
                {
                    "state": "WORKING",
                    "reason": "test",
                    "identity": {
                        "candidate_path": "05_ACTIVE_CANDIDATE/test_v1_0_CANDIDATE.md",
                        "candidate_sha256": "a" * 64,
                    },
                    "binding": event_binding(),
                },
            )
            journal.append(
                "workflow_state_changed",
                {
                    "state": "DIAGNOSING",
                    "reason": "test",
                    "identity": {"report_sha256": "b" * 64},
                    "binding": event_binding("b" * 64),
                },
            )
            events = journal.read()
            self.assertEqual(len(events), 2)
            snapshot = supervisor.latest_snapshot(events)
            self.assertEqual(snapshot.state, supervisor.WorkflowState.DIAGNOSING)
            self.assertEqual(snapshot.candidate_sha256, "a" * 64)
            self.assertEqual(snapshot.report_sha256, "b" * 64)

    def test_tampering_is_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "events.jsonl"
            journal = supervisor.DurableSupervisorJournal(path)
            journal.append(
                "workflow_state_changed",
                {
                    "state": "WORKING",
                    "reason": "test",
                    "identity": {},
                    "binding": event_binding(),
                },
            )
            event = json.loads(path.read_text(encoding="utf-8"))
            event["payload"]["state"] = "READY_FOR_ACCEPTANCE"
            path.write_text(json.dumps(event) + "\n", encoding="utf-8")
            with self.assertRaises(supervisor.SupervisorJournalError):
                journal.read()

    def test_concurrent_appends_keep_one_valid_chain(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "events.jsonl"
            journals = [supervisor.DurableSupervisorJournal(path) for _ in range(8)]
            threads = [
                threading.Thread(
                    target=journal.append,
                    args=(
                        "workflow_state_changed",
                        {
                            "state": "WORKING",
                            "reason": "test",
                            "identity": {},
                            "binding": event_binding(),
                        },
                    ),
                )
                for journal in journals
            ]
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()
            events = supervisor.DurableSupervisorJournal(path).read()
            self.assertEqual(len(events), 8)
            self.assertEqual([event["event_seq"] for event in events], list(range(1, 9)))

    def test_insecure_preexisting_directory_is_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = Path(tmp) / "state"
            state.mkdir(mode=0o755)
            journal = supervisor.DurableSupervisorJournal(state / "events.jsonl")
            with self.assertRaises(supervisor.SupervisorJournalError):
                journal.append(
                    "workflow_state_changed",
                    {
                        "state": "WORKING",
                        "reason": "test",
                        "identity": {},
                        "binding": event_binding(),
                    },
                )

    def test_hard_linked_journal_is_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = Path(tmp) / "state"
            state.mkdir(mode=0o700)
            journal = supervisor.DurableSupervisorJournal(state / "events.jsonl")
            journal.append(
                "workflow_state_changed",
                {
                    "state": "WORKING",
                    "reason": "test",
                    "identity": {},
                    "binding": event_binding(),
                },
            )
            os.link(state / "events.jsonl", state / "second-link.jsonl")
            with self.assertRaises(supervisor.SupervisorJournalError):
                journal.read()

    def test_complete_controller_report_cannot_be_stored(self):
        with tempfile.TemporaryDirectory() as tmp:
            journal = supervisor.DurableSupervisorJournal(Path(tmp) / "events.jsonl")
            with self.assertRaises(supervisor.SupervisorJournalError):
                journal.append(
                    "controller_report_digest_observed",
                    {
                        "operation_id": "op_test",
                        "command": "execute-next-claude-task",
                        "returncode": 0,
                        "output_sha256": "a" * 64,
                        "identity": {},
                        "report_projection": {
                            "ok": True,
                            "complete_private_report": {"secret": "must not persist"},
                        },
                        "binding": event_binding(),
                    },
                )

    def test_installed_ascii_canonical_encoding_is_used(self):
        self.assertEqual(
            supervisor.canonical_json_bytes({"word": "café"}),
            b'{"word":"caf\\u00e9"}',
        )

    def test_old_local_journal_version_is_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "events.jsonl"
            event = {
                "journal_version": 1,
                "event_seq": 1,
                "event_type": "workflow_state_changed",
                "recorded_at": "2026-08-18T00:00:00Z",
                "prev_event_sha256": supervisor.ZERO_SHA256,
                "payload": {
                    "state": "WORKING",
                    "reason": "old encoding",
                    "identity": {},
                    "binding": event_binding(),
                },
            }
            event["event_sha256"] = supervisor.event_sha256(event)
            path.write_bytes(supervisor.canonical_json_bytes(event) + b"\n")
            path.chmod(0o600)
            with self.assertRaises(supervisor.SupervisorJournalError):
                supervisor.DurableSupervisorJournal(path).read()


class SupervisorLeaseTests(unittest.TestCase):
    def test_second_worker_cannot_take_a_live_lease_but_can_take_stale_lease(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = Path(tmp) / "state"
            clock = [100.0]
            ticks = {101: 11, 202: 22}
            first = supervisor.SupervisorLease(
                state / "supervisor_lease.json",
                now=lambda: clock[0],
                pid=101,
                start_ticks_reader=lambda pid: ticks[pid],
                boot_id_reader=lambda: "a" * 64,
            )
            second = supervisor.SupervisorLease(
                state / "supervisor_lease.json",
                now=lambda: clock[0],
                pid=202,
                start_ticks_reader=lambda pid: ticks[pid],
                boot_id_reader=lambda: "a" * 64,
            )
            self.assertTrue(first.acquire("pkg", "b" * 64, "c" * 64))
            self.assertFalse(second.acquire("pkg", "b" * 64, "c" * 64))
            clock[0] = 136.0
            self.assertTrue(second.acquire("pkg", "b" * 64, "c" * 64))

    def test_pid_reuse_or_reboot_invalidates_old_owner(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = Path(tmp) / "state"
            first = supervisor.SupervisorLease(
                state / "supervisor_lease.json",
                now=lambda: 100.0,
                pid=101,
                start_ticks_reader=lambda _pid: 11,
                boot_id_reader=lambda: "a" * 64,
            )
            self.assertTrue(first.acquire("pkg", "b" * 64, "c" * 64))
            replacement = supervisor.SupervisorLease(
                state / "supervisor_lease.json",
                now=lambda: 101.0,
                pid=101,
                start_ticks_reader=lambda _pid: 12,
                boot_id_reader=lambda: "d" * 64,
            )
            self.assertTrue(replacement.acquire("pkg", "b" * 64, "c" * 64))


class ChangeFeedTests(unittest.TestCase):
    def authenticated_status(self, events=None, active=True):
        return {
            "command": "supervisor-status",
            "ok": True,
            "journal_authentication_proved": True,
            "authenticated_state_current": True,
            "source_state_current": True,
            "workflow_state": "WORKING",
            "next_command": "execute-next-claude-task",
            "package_scope_id": "pkg_scope",
            "controller_executable_identity": "1" * 64,
            "source_binding_sha256": "2" * 64,
            "candidate_path": "05_ACTIVE_CANDIDATE/pkg_v1_0_CANDIDATE.md",
            "candidate_sha256": "a" * 64,
            "candidate_bytes": 100,
            "authenticated_event_seq": 10,
            "authenticated_tail_sha256": "4" * 64,
            "state_recorded_at": "2026-08-18T00:00:00Z",
            "run_lease": {
                "live_proved": active,
                "run_id": "run_test",
                "expires_at": "2026-08-18T00:00:35Z",
            },
            "controller_confirmed_change_events": events or [],
        }

    def test_status_requires_controller_authentication(self):
        report = self.authenticated_status()
        report["journal_authentication_proved"] = False
        with self.assertRaises(supervisor.SupervisorJournalError):
            supervisor.snapshot_from_supervisor_status(report)

    def test_unauthenticated_change_event_is_refused(self):
        event = {
            "controller_authenticated": False,
            "recorded_at": "2026-08-18T00:00:00Z",
            "id": "e1",
            "kind": "audit_passed",
            "title": "Fake pass",
            "what": "Fake",
            "why": "Fake",
            "status": "Fake",
            "technical": {},
        }
        with self.assertRaises(supervisor.SupervisorJournalError):
            supervisor.change_feed_from_supervisor_status(
                self.authenticated_status([event])
            )

    def test_authenticated_explanation_unavailable_fallback_makes_no_success_claim(self):
        event = {
            "controller_authenticated": True,
            "recorded_at": "2026-08-18T00:00:00Z",
            "id": "custody-fallback-1",
            "kind": "candidate_changed",
            "title": "A mechanical correction candidate was preserved",
            "what": (
                "N.H preserved a new correction candidate. A safe plain-language "
                "explanation is not currently available."
            ),
            "why": (
                "The exact parent, candidate, and technical difference are available "
                "below. No claim is made that the correction succeeded or that meaning or "
                "policy stayed unchanged."
            ),
            "status": "Waiting for or reporting the independent audit result",
            "technical": {
                "controller_event_seq": 11,
                "controller_event_sha256": "e" * 64,
                "candidate_path": "05_ACTIVE_CANDIDATE/pkg_v1_1_CANDIDATE.md",
                "candidate_sha256": "f" * 64,
            },
        }
        feed = supervisor.change_feed_from_supervisor_status(
            self.authenticated_status([event])
        )
        self.assertEqual(len(feed), 1)
        self.assertFalse(feed[0]["confirmed"])
        self.assertIn("No claim", feed[0]["why"])
        self.assertNotIn("fixed", feed[0]["why"].lower())

    def test_feed_never_claims_claude_fix_before_pass(self):
        report = {
            "audit_history": [
                {
                    "correction_round": 0,
                    "candidate_path": "05_ACTIVE_CANDIDATE/pkg_v1_0_CANDIDATE.md",
                    "candidate_sha256": "a" * 64,
                    "candidate_bytes": 100,
                    "verdict": "BLOCKED",
                    "ok": True,
                    "findings": [
                        {
                            "title": "Crash state is missing",
                            "severity": "IMPORTANT",
                            "route": "claude_mechanical",
                        }
                    ],
                },
                {
                    "correction_round": 1,
                    "candidate_path": "05_ACTIVE_CANDIDATE/pkg_v1_1_CANDIDATE.md",
                    "candidate_sha256": "b" * 64,
                    "candidate_bytes": 120,
                    "verdict": "BLOCKED",
                    "ok": True,
                    "findings": [],
                },
            ],
            "correction_history": [
                {
                    "correction_round": 1,
                    "blocked_candidate_path": "05_ACTIVE_CANDIDATE/pkg_v1_0_CANDIDATE.md",
                    "blocked_candidate_sha256": "a" * 64,
                    "next_candidate_path": "05_ACTIVE_CANDIDATE/pkg_v1_1_CANDIDATE.md",
                    "new_candidate_sha256": "b" * 64,
                    "new_candidate_bytes": 120,
                    "correction_finding_count": 1,
                    "promoted": True,
                    "custody_recorded": True,
                }
            ],
        }
        feed = supervisor.change_feed_from_report(report)
        correction = next(item for item in feed if item["kind"] == "candidate_changed")
        self.assertIn("intended to address", correction["what"])
        self.assertFalse(correction["confirmed"])
        self.assertNotIn("fixed", correction["what"].lower())

    def test_pass_card_is_explicitly_separate_from_acceptance(self):
        report = {
            "audit_history": [
                {
                    "correction_round": 2,
                    "candidate_path": "05_ACTIVE_CANDIDATE/pkg_v1_2_CANDIDATE.md",
                    "candidate_sha256": "c" * 64,
                    "candidate_bytes": 140,
                    "verdict": "PASS",
                    "highest_severity": "NONE",
                    "ok": True,
                    "findings": [],
                }
            ]
        }
        feed = supervisor.change_feed_from_report(report)
        self.assertEqual(feed[-1]["kind"], "audit_passed")
        self.assertIn("does not mean Ness accepted", feed[-1]["why"])


if __name__ == "__main__":
    unittest.main()

import base64
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from interview_ui.progress_view import HTML, JournalTail, bundle_for, bundle_seven_progress, project_progress, question_path


def event(seq, event_type, previous=None, **fields):
    value = {"event_seq": seq, "type": event_type, "prev_event_sha256": previous, **fields}
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    value["event_sha256"] = hashlib.sha256(raw).hexdigest()
    return value


class ProgressViewTests(unittest.TestCase):
    def test_bundle_seven_progress_counts_only_complete_saved_validation_sets(self):
        events = [
            {
                "type": "bundle_seven_baseline_recorded",
                "event_seq": 10,
                "package_inventory": [
                    {"package_id": "A17"},
                    {"package_id": "A19"},
                ],
            },
            {
                "type": "validation_recorded",
                "event_seq": 11,
                "package_scope_id": "A19",
                "validation_set_id": "partial",
                "page_index": 1,
                "page_count": 2,
                "enumeration_complete": True,
            },
            {
                "type": "validation_recorded",
                "event_seq": 12,
                "package_scope_id": "A17",
                "validation_set_id": "complete",
                "page_index": 1,
                "page_count": 1,
                "enumeration_complete": True,
            },
        ]
        self.assertEqual(
            {"completed": 1, "total": 2, "percent": 50, "remaining": 1},
            bundle_seven_progress(events),
        )
    def test_page_contains_question_path_and_unambiguous_time_labels(self):
        self.assertIn("PATH TO YOUR QUESTIONS", HTML)
        self.assertIn("Why you are not being asked yet:", HTML)
        self.assertIn("Questions can be asked when:", HTML)
        self.assertIn("Worker alive for", HTML)
        self.assertIn("Current stage duration", HTML)
        self.assertNotIn('class="label">Elapsed<', HTML)

    def test_journal_tail_reads_only_new_verified_events(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "journal.jsonl"
            first = event(1, "one")
            path.write_text(json.dumps(first) + "\n")
            tail = JournalTail(path)
            values, error = tail.read()
            self.assertIsNone(error)
            self.assertEqual([1], [item["event_seq"] for item in values])
            second = event(2, "two", first["event_sha256"])
            with path.open("a") as handle:
                handle.write(json.dumps(second) + "\n")
            values, error = tail.read()
            self.assertIsNone(error)
            self.assertEqual([1, 2], [item["event_seq"] for item in values])

    def test_invalid_append_does_not_replace_verified_projection(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "journal.jsonl"
            first = event(1, "one")
            path.write_text(json.dumps(first) + "\n")
            tail = JournalTail(path)
            tail.read()
            bad = event(2, "two", first["event_sha256"])
            bad["event_sha256"] = "bad"
            with path.open("a") as handle:
                handle.write(json.dumps(bad) + "\n")
            values, error = tail.read()
            self.assertEqual([1], [item["event_seq"] for item in values])
            self.assertIn("invalid digest", error)

    def test_authentication_failure_is_refused(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "journal.jsonl"
            key_path = Path(folder) / "key"
            key_path.write_bytes(b"k" * 32)
            value = {
                "journal_version": 9, "event_seq": 1, "type": "one",
                "prev_event_sha256": None, "event_auth_sha256": "0" * 64,
            }
            raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
            value["event_sha256"] = hashlib.sha256(raw).hexdigest()
            path.write_text(json.dumps(value) + "\n")
            values, error = JournalTail(path, key_path).read()
            self.assertEqual([], values)
            self.assertIn("failed authentication", error)

    def test_bundle_is_mapped_from_existing_plan(self):
        plan = "### Bundle 7 — Wonder and interface\n- A19 — World behavior.\n"
        self.assertEqual("Bundle 7 — Wonder and interface", bundle_for("A19", plan))

    def test_live_provider_is_shown_without_operating_it(self):
        values = [
            {"event_seq": 1, "type": "provider_dispatch_begun", "package_id": "A19",
             "provider_request_identity": "p1", "provider_endpoint_identity": "local_codex_cli_chatgpt",
             "provider_kind": "gpt_question_validation", "dispatch_pid": 10,
             "dispatch_process_start_ticks": 20, "dispatch_boot_id_sha256": "boot"}
        ]
        result = project_progress(values, {}, "### Bundle 7 — Wonder\n- A19 — World.\n",
                                  alive=lambda pid, *_: pid == 10, elapsed=lambda *_: 12)
        self.assertEqual("Codex", result["actor"])
        self.assertTrue(result["provider_request_open"])
        self.assertEqual(12, result["current_stage_duration_seconds"])
        self.assertIsNone(result["worker_alive_for_seconds"])

    def test_new_live_request_overrides_resolved_old_uncertainty(self):
        values = [
            {
                "event_seq": 999,
                "type": "provider_request_reconciled",
                "package_id": "A19",
                "provider_request_identity": "old",
                "next_workflow_state": "NEEDS_USER_ACTION",
                "dependency_record": {
                    "provider_request_identity": "old",
                    "user_action_code": "provider_outcome_confirmation_required",
                },
            },
            {
                "event_seq": 1001,
                "type": "ness_transition_recovery_choice_recorded",
                "package_id": "A19",
                "provider_request_identity": "old",
                "recovery_action": "abandon_and_replace_once",
            },
            {
                "event_seq": 1004,
                "type": "provider_dispatch_begun",
                "package_id": "A19",
                "provider_request_identity": "new",
                "provider_endpoint_identity": "local_codex_cli_chatgpt",
                "provider_kind": "gpt_question_validation",
                "dispatch_pid": 10,
                "dispatch_process_start_ticks": 20,
                "dispatch_boot_id_sha256": "boot",
            },
        ]
        result = project_progress(values, {}, "", alive=lambda pid, *_: pid == 10)
        self.assertEqual("Waiting for Codex", result["stage"])
        self.assertEqual("Codex", result["actor"])
        self.assertEqual("Provider is actively running", result["doing"])
        self.assertEqual("No durable request for Ness is recorded", result["needs_ness"])
        self.assertFalse(result["needs_ness_now"])
        self.assertEqual(
            "N.H will durably capture the provider exit/result and process it when Codex finishes.",
            result["next"],
        )
        self.assertEqual("WORKING NOW", result["question_path"]["steps"][0]["status"])

    def test_terminal_provider_is_not_reported_open(self):
        values = [
            {"event_seq": 1, "type": "provider_dispatch_begun", "package_id": "A19",
             "provider_request_identity": "p1"},
            {"event_seq": 2, "type": "provider_request_terminal_recorded", "package_id": "A19",
             "provider_request_identity": "p1"},
        ]
        result = project_progress(values, {}, "", alive=lambda *_: False)
        self.assertFalse(result["provider_request_open"])

    def test_fresh_matching_worker_health_keeps_current_provider_visible(self):
        values = [
            {"event_seq": 1, "type": "supervisor_operation_started",
             "supervisor_operation_id": "op", "package_id": "B29"},
            {"event_seq": 2, "type": "provider_dispatch_begun", "package_id": "B29",
             "supervisor_operation_id": "op", "provider_request_identity": "p1",
             "provider_endpoint_identity": "local_codex_cli_chatgpt",
             "provider_kind": "gpt_question_validation"},
        ]
        lease = {"pid": 4, "run_id": "run", "expires_at_epoch": 9999999999}
        health = {"pid": 4, "run_id": "run", "status": "running"}
        result = project_progress(
            values, lease, "", alive=lambda *_: False, worker_health=health
        )
        self.assertEqual("Waiting for Codex", result["stage"])
        self.assertEqual("Provider is actively running", result["doing"])

    def test_old_reconciliation_does_not_hide_new_live_provider(self):
        values = [
            {"event_seq": 1, "type": "provider_request_terminal_recorded",
             "package_id": "A22", "provider_request_identity": "old",
             "next_workflow_state": "NEEDS_USER_ACTION",
             "dependency_record": {
                 "provider_request_identity": "old",
                 "user_action_code": "provider_outcome_confirmation_required",
             }},
            {"event_seq": 2, "type": "supervisor_operation_started",
             "supervisor_operation_id": "new-op", "package_id": "B29"},
            {"event_seq": 3, "type": "provider_dispatch_begun", "package_id": "B29",
             "supervisor_operation_id": "new-op", "provider_request_identity": "new",
             "provider_endpoint_identity": "local_codex_cli_chatgpt",
             "provider_kind": "gpt_question_validation", "dispatch_pid": 10},
        ]
        result = project_progress(values, {}, "", alive=lambda pid, *_: pid == 10)
        self.assertEqual("Waiting for Codex", result["stage"])
        self.assertFalse(result["needs_ness_now"])

    def test_old_external_action_does_not_hide_new_live_provider(self):
        values = [
            {"event_seq": 1, "type": "provider_request_terminal_recorded",
             "package_id": "B-INT-10", "provider_request_identity": "old",
             "next_workflow_state": "NEEDS_USER_ACTION",
             "dependency_record": {
                 "user_action_code": "provider_local_process_failure_review_required",
             }},
            {"event_seq": 2, "type": "supervisor_operation_started",
             "supervisor_operation_id": "new-op", "package_id": "A22"},
            {"event_seq": 3, "type": "provider_dispatch_begun", "package_id": "A22",
             "supervisor_operation_id": "new-op", "provider_request_identity": "new",
             "provider_endpoint_identity": "local_codex_cli_chatgpt",
             "provider_kind": "gpt_question_validation", "dispatch_pid": 10},
        ]
        result = project_progress(values, {}, "", alive=lambda pid, *_: pid == 10)
        self.assertEqual("Waiting for Codex", result["stage"])
        self.assertFalse(result["needs_ness_now"])

    def test_old_unclosed_request_does_not_override_newer_terminal_request(self):
        values = [
            {"event_seq": 1, "type": "provider_dispatch_begun", "package_id": "A19",
             "provider_request_identity": "old"},
            {"event_seq": 2, "type": "provider_dispatch_begun", "package_id": "A19",
             "provider_request_identity": "new"},
            {"event_seq": 3, "type": "provider_request_terminal_recorded", "package_id": "A19",
             "provider_request_identity": "new"},
        ]
        result = project_progress(values, {}, "", alive=lambda *_: False)
        self.assertFalse(result["provider_request_open"])

    def test_elapsed_is_unavailable_without_exact_live_identity(self):
        values = [{"event_seq": 1, "type": "heartbeat", "package_id": "A19"}]
        lease = {"pid": 4, "process_start_ticks": 8, "boot_id_sha256": "x", "expires_at_epoch": 9999999999}
        result = project_progress(values, lease, "", alive=lambda *_: False, elapsed=lambda *_: 44)
        self.assertIsNone(result["worker_alive_for_seconds"])
        self.assertIsNone(result["current_stage_duration_seconds"])

    def test_worker_lifetime_is_separate_from_unproved_local_stage_duration(self):
        values = [{"event_seq": 1, "type": "heartbeat", "package_id": "A19"}]
        lease = {"pid": 4, "process_start_ticks": 8, "boot_id_sha256": "x", "expires_at_epoch": 9999999999}
        result = project_progress(values, lease, "", alive=lambda *_: True, elapsed=lambda *_: 90)
        self.assertEqual(90, result["worker_alive_for_seconds"])
        self.assertIsNone(result["current_stage_duration_seconds"])

    def test_controller_identity_mismatch_is_restart_required_not_working(self):
        values = [
            {"event_seq": 1, "type": "provider_dispatch_begun", "package_id": "A19",
             "provider_request_identity": "p1", "provider_kind": "gpt_question_coverage_review"},
            {"event_seq": 2, "type": "provider_result_custody_recorded", "package_id": "A19",
             "provider_request_identity": "p1", "provider_kind": "gpt_question_coverage_review"},
            {"event_seq": 3, "type": "provider_request_terminal_recorded", "package_id": "A19",
             "provider_request_identity": "p1"},
        ]
        lease = {
            "pid": 4, "process_start_ticks": 8, "boot_id_sha256": "x",
            "expires_at_epoch": 9999999999,
            "controller_executable_identity": "old",
        }
        result = project_progress(
            values, lease, "", alive=lambda *_: True,
            installed_controller_identity="current",
        )
        self.assertTrue(result["worker_restart_required"])
        self.assertFalse(result["worker_lease_current"])
        self.assertEqual("N.H recovery", result["actor"])
        self.assertIn("RESTART REQUIRED", result["doing"])
        self.assertEqual("BLOCKED", result["question_path"]["steps"][0]["status"])
        self.assertNotIn(
            "WORKING NOW",
            [step["status"] for step in result["question_path"]["steps"]],
        )

    def test_matching_controller_identity_keeps_normal_worker_projection(self):
        values = [{"event_seq": 1, "type": "heartbeat", "package_id": "A19"}]
        lease = {
            "pid": 4, "process_start_ticks": 8, "boot_id_sha256": "x",
            "expires_at_epoch": 9999999999,
            "controller_executable_identity": "same",
        }
        result = project_progress(
            values, lease, "", alive=lambda *_: True,
            installed_controller_identity="same",
        )
        self.assertFalse(result["worker_restart_required"])
        self.assertTrue(result["worker_lease_current"])
        self.assertEqual("Local N.H", result["actor"])

    def test_failed_work_thread_is_not_reported_as_working(self):
        values = [{"event_seq": 1, "type": "heartbeat", "package_id": "A19"}]
        lease = {
            "pid": 4, "run_id": "r1", "process_start_ticks": 8,
            "boot_id_sha256": "x", "expires_at_epoch": 9999999999,
            "controller_executable_identity": "same",
        }
        result = project_progress(
            values,
            lease,
            "",
            alive=lambda *_: True,
            installed_controller_identity="same",
            worker_health={
                "pid": 4,
                "run_id": "r1",
                "status": "failed",
                "detail": "the real work thread crashed",
            },
        )
        self.assertTrue(result["worker_thread_failed"])
        self.assertFalse(result["worker_lease_current"])
        self.assertEqual("Work-thread recovery required", result["stage"])
        self.assertEqual("BLOCKED", result["question_path"]["steps"][0]["status"])

    def test_maintenance_pause_is_shown_as_paused_not_working(self):
        values = [{"event_seq": 1, "type": "heartbeat", "package_id": "A19"}]
        result = project_progress(
            values,
            {},
            "",
            alive=lambda *_: False,
            maintenance_pause={"record_version": 1, "pause_requested": True},
        )
        self.assertTrue(result["maintenance_pause_active"])
        self.assertEqual("Safe maintenance pause", result["stage"])
        self.assertEqual("Paused", result["actor"])
        self.assertEqual("BLOCKED", result["question_path"]["steps"][0]["status"])

    def test_maintenance_pause_does_not_hide_a_durable_external_action_stop(self):
        values = [
            {"event_seq": 1156, "type": "provider_dispatch_begun", "package_id": "A19",
             "provider_request_identity": "pr1",
             "provider_endpoint_identity": "local_codex_cli_chatgpt",
             "provider_kind": "gpt_question_validation"},
            {"event_seq": 1157, "type": "provider_request_terminal_recorded", "package_id": "A19",
             "provider_request_identity": "pr1",
             "dependency_record": {
                 "dependency_class": "external_user_action_required",
                 "dependency_code": "provider_local_process_terminal_failure",
                 "next_workflow_state": "NEEDS_USER_ACTION",
                 "user_action_code": "provider_local_process_failure_review_required",
             }},
            {"event_seq": 1158, "type": "supervisor_operation_completed", "package_id": "A19"},
        ]
        result = project_progress(
            values,
            {},
            "",
            alive=lambda *_: False,
            maintenance_pause={"record_version": 1, "pause_requested": True},
        )
        self.assertTrue(result["maintenance_pause_active"])
        self.assertTrue(result["needs_ness_now"])
        self.assertEqual("external_action", result["needs_ness_kind"])
        self.assertIn("external action", result["needs_ness"])
        self.assertIn("maintenance pause", result["stage"].lower())
        self.assertIn("external action", result["stage"].lower())
        self.assertNotEqual(
            "Resume with exactly one worker after maintenance is complete", result["next"]
        )
        self.assertIn("external action", result["next"].lower())
        blocking_step = result["question_path"]["steps"][0]
        self.assertEqual("BLOCKED", blocking_step["status"])
        self.assertIn(
            "provider_local_process_failure_review_required", blocking_step["detail"]
        )
        self.assertIn(
            "provider_local_process_failure_review_required",
            result["question_path"]["reason_not_ready"],
        )
        self.assertNotIn(
            "Resume with exactly one worker",
            result["question_path"]["questions_can_be_asked_when"],
        )

    def test_question_path_shows_current_coverage_gate_and_proved_counts(self):
        validation = {
            "whole_check_complete": True, "enumeration_complete": True,
            "total_issue_count": 11, "issues": [{} for _ in range(11)],
        }
        coverage = {
            "whole_check_complete": True, "coverage_review_complete": True,
            "possible_gaps": [{"issue_key": "world_spatial_continuity"}],
        }
        values = [
            {"event_seq": 8, "type": "provider_result_custody_recorded", "package_id": "A19",
             "provider_kind": "gpt_question_coverage_review",
             "result_bytes_base64": base64.b64encode(json.dumps(coverage).encode()).decode()},
            {"event_seq": 10, "type": "provider_result_custody_recorded", "package_id": "A19",
             "provider_kind": "gpt_question_validation",
             "result_bytes_base64": base64.b64encode(json.dumps(validation).encode()).decode()},
            {"event_seq": 11, "type": "validation_recorded", "package_id": "A19"},
        ]
        provider = {"provider_kind": "gpt_question_coverage_review"}
        result = question_path(values, provider, True, False, True, False)
        self.assertEqual(11, result["validated_question_count"])
        self.assertEqual(1, result["previous_possible_gap_count"])
        self.assertEqual("WORKING NOW", result["steps"][1]["status"])
        self.assertEqual("CONDITIONAL", result["steps"][4]["status"])
        self.assertFalse(result["coverage_complete"])
        self.assertFalse(result["ness_question_ready_record_exists"])

    def test_question_path_surfaces_dead_provider_as_blocked(self):
        provider = {"provider_kind": "gpt_question_coverage_review"}
        result = question_path([], provider, False, False, False, False)
        self.assertIn("mechanically blocked", result["reason_not_ready"])
        self.assertEqual("BLOCKED", result["steps"][1]["status"])

    def test_latest_coverage_gaps_are_not_mislabeled_as_already_revalidated(self):
        coverage = {
            "whole_check_complete": True, "coverage_review_complete": True,
            "possible_gaps": [{"issue_key": "interaction_failure_safeguards"}],
        }
        values = [
            {"event_seq": 10, "type": "validation_recorded", "package_id": "A19"},
            {"event_seq": 11, "type": "provider_result_custody_recorded", "package_id": "A19",
             "provider_kind": "gpt_question_coverage_review",
             "result_bytes_base64": base64.b64encode(json.dumps(coverage).encode()).decode()},
        ]
        result = question_path(values, None, False, True, True, False)
        self.assertIn("must process that result", result["possible_gap_note"])
        self.assertNotIn("later validation ran", result["possible_gap_note"])

    def test_processed_coverage_waiting_for_commit_is_the_exact_current_gate(self):
        coverage = {
            "whole_check_complete": True, "coverage_review_complete": True,
            "possible_gaps": [{"issue_key": "interaction_failure_safeguards"}],
        }
        encoded = base64.b64encode(json.dumps(coverage).encode()).decode()
        values = [
            {"event_seq": 10, "type": "validation_recorded", "package_id": "A19"},
            {"event_seq": 11, "type": "provider_result_custody_recorded", "package_id": "A19",
             "provider_kind": "gpt_question_coverage_review", "provider_request_identity": "p1",
             "result_bytes_base64": encoded},
            {"event_seq": 12, "type": "piece3_provider_work_recorded", "package_id": "A19",
             "provider_request_identity": "p1", "work_item_kind": "coverage_review",
             "authorizes_event_type": "question_coverage_review_recorded"},
        ]
        result = question_path(values, None, False, False, True, False)
        self.assertEqual("WORKING NOW", result["steps"][3]["status"])
        self.assertIn("not yet durably committed", result["reason_not_ready"])
        self.assertIn("awaiting durable recording", result["possible_gap_note"])

    def test_new_validation_proves_the_prior_coverage_finding_advanced(self):
        coverage = {
            "whole_check_complete": True, "coverage_review_complete": True,
            "possible_gaps": [{"issue_key": "interaction_failure_safeguards"}],
        }
        values = [
            {"event_seq": 11, "type": "provider_result_custody_recorded", "package_id": "A19",
             "provider_kind": "gpt_question_coverage_review", "provider_request_identity": "p1",
             "result_bytes_base64": base64.b64encode(json.dumps(coverage).encode()).decode()},
            {"event_seq": 12, "type": "piece3_provider_work_recorded", "package_id": "A19",
             "provider_request_identity": "p1", "work_item_kind": "coverage_review",
             "authorizes_event_type": "question_coverage_review_recorded"},
        ]
        provider = {"event_seq": 14, "provider_kind": "gpt_question_validation"}
        result = question_path(values, provider, True, False, True, False)
        self.assertEqual("DONE", result["steps"][3]["status"])
        self.assertIn("current validation is checking", result["possible_gap_note"])

    def test_external_action_blocker_keeps_its_name_when_validation_follows_coverage(self):
        coverage = {
            "whole_check_complete": True, "coverage_review_complete": True,
            "possible_gaps": [{"issue_key": "interaction_failure_safeguards"}],
        }
        values = [
            {"event_seq": 11, "type": "provider_result_custody_recorded", "package_id": "A19",
             "provider_kind": "gpt_question_coverage_review", "provider_request_identity": "p1",
             "result_bytes_base64": base64.b64encode(json.dumps(coverage).encode()).decode()},
            {"event_seq": 12, "type": "piece3_provider_work_recorded", "package_id": "A19",
             "provider_request_identity": "p1", "work_item_kind": "coverage_review",
             "authorizes_event_type": "question_coverage_review_recorded"},
        ]
        provider = {"event_seq": 14, "provider_kind": "gpt_question_validation"}
        blocker = (
            "BLOCKED — N.H is stopped at a durable external-action boundary "
            "(provider_local_process_failure_review_required)."
        )
        result = question_path(
            values, provider, True, False, True, False,
            external_action_blocker=blocker,
        )
        steps = result["steps"]
        self.assertEqual("Resolve the recorded durable external action", steps[0]["name"])
        self.assertEqual("BLOCKED", steps[0]["status"])
        self.assertEqual(blocker, steps[0]["detail"])
        by_name = {step["name"]: step for step in steps}
        targeted = by_name["Targeted validation unlocked by the last coverage finding"]
        self.assertEqual("WORKING NOW", targeted["status"])
        self.assertNotEqual(blocker, targeted["detail"])
        previous_coverage = by_name["Previous independent coverage review"]
        self.assertNotEqual(blocker, previous_coverage["detail"])
        self.assertEqual(len(steps), len(by_name))
        self.assertEqual(
            "Check the updated question set for complete coverage",
            steps[steps.index(by_name["Durably record the coverage finding"]) + 1]["name"],
        )

    def test_uncommitted_complete_validation_result_is_counted_only_as_provisional(self):
        value = {
            "whole_check_complete": True, "enumeration_complete": True,
            "total_issue_count": 3, "issues": [{}, {}, {}],
        }
        values = [
            {"event_seq": 10, "type": "validation_recorded", "package_id": "A19"},
            {"event_seq": 11, "type": "provider_result_custody_recorded", "package_id": "A19",
             "provider_kind": "gpt_question_validation",
             "result_bytes_base64": base64.b64encode(json.dumps(value).encode()).decode()},
        ]
        result = question_path(values, None, False, True, True, False)
        self.assertEqual(3, result["provisional_question_count"])
        self.assertIsNone(result["validated_question_count"])

    def test_ready_boundary_uses_ready_final_status(self):
        result = question_path([], None, False, False, False, True)
        self.assertEqual("READY", result["steps"][-1]["status"])
        self.assertIn("can ask Ness now", result["steps"][-1]["detail"])


if __name__ == "__main__":
    unittest.main()

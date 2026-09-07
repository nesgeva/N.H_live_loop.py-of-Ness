import json
import unittest
from pathlib import Path
from unittest import mock

import server


class InterviewUiTests(unittest.TestCase):
    def test_browser_marks_typed_freeform_answers_as_explicit_own_words(self):
        source = (Path(__file__).parent / "static" / "app.js").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            'const NESS_OWN_WORDS_OPTION_ID = "ness_own_words";', source
        )
        self.assertIn("form.dataset.choice = NESS_OWN_WORDS_OPTION_ID", source)
        self.assertIn('interpretation === "selected_ness_own_words"', source)

    def test_browser_and_server_coalesce_expensive_status_refreshes(self):
        source = (Path(__file__).parent / "static" / "app.js").read_text(
            encoding="utf-8"
        )
        self.assertIn("let stateRefreshing = false;", source)
        self.assertIn("if (stateRefreshing) return stateRefreshPromise;", source)

        with mock.patch.object(server, "_UI_STATE_CACHE", None), mock.patch.object(
            server, "_UI_STATE_CACHE_AT", 0.0
        ), mock.patch.object(
            server, "_build_ui_state_uncached", return_value={"ok": True}
        ) as build:
            first = server.build_ui_state()
            second = server.build_ui_state()

        self.assertEqual({"ok": True}, first)
        self.assertEqual(first, second)
        build.assert_called_once_with()

    def test_parse_controller_report_uses_final_json(self):
        output = 'plain text\n{"ok": true, "command": "interview-status"}\n'
        self.assertEqual(server.parse_controller_report(output)["command"], "interview-status")

    def test_parse_question_form(self):
        output = """N.H design-loop next question group

QUESTION 1 of 1 in this group
  question id:     nq_123
  form generation: nfg_456
  topic:           Privacy behavior
  What I checked: 4 source files
  This is about: \"a source passage\" (from rules.md)
  Already settled (kept as it is): \"the existing rule\" (from master.md)
  Mechanical (mine, not yours): everything technical
  What your answer changes in real use: what N.H shows; when it stops
  YOUR CHOICE: What should happen?
  The options are:
    [O1] Keep it private
         if you choose this: nothing is shown
         choosing this changes nothing about any other question here
  Answer in your own words.
{"ok": true}
"""
        questions = server.parse_question_forms(output)
        self.assertEqual(len(questions), 1)
        self.assertEqual(questions[0]["question_id"], "nq_123")
        self.assertEqual(questions[0]["options"][0]["option_id"], "O1")
        self.assertEqual(
            questions[0]["effect_sentences"], ["what N.H shows", "when it stops"]
        )

    def test_mechanical_stage_does_not_need_ness(self):
        stage = server.derive_stage(
            {"deliverable_question_count": 0, "open_group_index": None},
            {"mechanical_path_unlocked": True},
        )
        self.assertEqual(stage["code"], "mechanical_design")
        self.assertFalse(stage["needs_ness"])

    def test_ready_question_is_prominent(self):
        snapshot = server.supervisor.snapshot_for_state(
            server.supervisor.WorkflowState.NEEDS_NESS_DECISION
        )
        stage = server.derive_stage(
            {"deliverable_question_count": 1, "open_group_index": None},
            {"mechanical_path_unlocked": False},
            snapshot,
        )
        self.assertEqual(stage["code"], "waiting_for_ness")
        self.assertTrue(stage["needs_ness"])

    def test_diagnosis_state_is_not_a_ness_question(self):
        snapshot = server.supervisor.snapshot_for_state(
            server.supervisor.WorkflowState.DIAGNOSING,
            controller_authenticated=True,
            run_active=True,
        )
        stage = server.derive_stage(
            {"deliverable_question_count": 0, "open_group_index": None},
            {"mechanical_path_unlocked": True},
            snapshot,
        )
        self.assertEqual(stage["code"], "diagnosing")
        self.assertFalse(stage["needs_ness"])

    def test_stale_working_state_is_described_as_inactive(self):
        snapshot = server.supervisor.snapshot_for_state(
            server.supervisor.WorkflowState.WORKING,
            controller_authenticated=True,
            run_active=False,
        )
        stage = server.derive_stage({}, {}, snapshot)
        self.assertEqual(stage["code"], "supervisor_inactive")
        self.assertIn("no current live supervisor lease", stage["summary"])

    def test_acceptance_state_needs_ness_but_is_not_a_question(self):
        snapshot = server.supervisor.snapshot_for_state(
            server.supervisor.WorkflowState.READY_FOR_ACCEPTANCE
        )
        stage = server.derive_stage({}, {}, snapshot)
        self.assertTrue(stage["needs_ness"])
        self.assertEqual(stage["attention_kind"], "acceptance")

if __name__ == "__main__":
    unittest.main()

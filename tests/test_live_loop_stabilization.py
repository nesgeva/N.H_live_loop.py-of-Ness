import base64
import contextlib
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
for directory in (ROOT / "controller", ROOT / "interview_ui"):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import nh_loop  # noqa: E402
from nh_supervisor import commands  # noqa: E402
from nh_supervisor import replay  # noqa: E402
from nh_supervisor import schema  # noqa: E402


@contextlib.contextmanager
def pinned_checkout(event_seq):
    """The N.H checkout EXACTLY as the interview history at ``event_seq`` saw it.

    frozen 2026-09-02: replay re-proves every recorded validation's source half
    against the live checkout (``replay_validation_event`` ->
    ``interview_source_reproof_context``), so a fixture cut at an old journal
    position rots as the checkout moves.  This rebuilds, in a DISPOSABLE copy,
    the checkout the latest validation at or before ``event_seq`` recorded: its
    branch and head_sha, plus exactly the untracked files that validation's own
    checked-source manifest names.  The copy is proved to hash to the
    validation's recorded ``source_binding_sha256`` through the installed
    ``read_source_binding`` before anything reads it, and ``nh_loop.NH_REPO_PATH``
    is redirected to it (the same test-only redirect the v1_8 harness uses) with
    the per-process re-proof cache dropped on entry and on exit.  Nothing here
    touches the real checkout, the real journal or a provider.
    """
    validation = None
    for line in (ROOT / "nh_interview_state" / "nh_interview_journal.jsonl").read_text(
        encoding="utf-8"
    ).splitlines():
        if not line.strip():
            continue
        event = json.loads(line)
        if (
            event.get("type") == "validation_recorded"
            and event.get("event_seq", 0) <= event_seq
        ):
            validation = event
    assert validation is not None, "no validation at or before event %d" % event_seq
    checked = set(validation["source_paths_checked"])
    with tempfile.TemporaryDirectory(dir="/tmp") as folder:
        repo = Path(folder) / "NH-GOVERNANCE"
        shutil.copytree(ROOT / "NH-GOVERNANCE", repo, symlinks=True)
        subprocess.run(
            ["git", "-C", str(repo), "checkout", "-q", "-B",
             validation["branch"], validation["head_sha"]],
            check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )
        listing = subprocess.run(
            ["git", "-C", str(repo), "status", "--porcelain=v1",
             "--untracked-files=all"],
            check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
        ).stdout
        for line in listing.splitlines():
            if line.startswith("?? ") and line[3:] not in checked:
                (repo / line[3:]).unlink()
        saved = nh_loop.NH_REPO_PATH
        nh_loop.NH_REPO_PATH = str(repo)
        nh_loop.reset_interview_source_reproof_cache()
        try:
            errors = []
            binding = nh_loop.read_source_binding("for the pinned checkout", errors)
            assert binding is not None, errors
            if binding["binding_sha256"] != validation["source_binding_sha256"]:
                raise unittest.SkipTest(
                    "the exact historical source snapshot for validation %d is "
                    "no longer available inside the repository"
                    % validation["event_seq"]
                )
            yield repo
        finally:
            nh_loop.NH_REPO_PATH = saved
            nh_loop.reset_interview_source_reproof_cache()


@contextlib.contextmanager
def copied_interview_at(event_seq):
    """Copy one authenticated journal prefix into an isolated state directory."""
    source_state = ROOT / "nh_interview_state"
    source_lines = (source_state / "nh_interview_journal.jsonl").read_text(
        encoding="utf-8"
    ).splitlines(keepends=True)
    selected = [
        line
        for line in source_lines
        if line.strip() and json.loads(line).get("event_seq", 0) <= event_seq
    ]
    events = [json.loads(line) for line in selected]
    assert events and events[-1]["event_seq"] == event_seq
    with tempfile.TemporaryDirectory(dir="/tmp") as folder:
        state = Path(folder) / "state"
        state.mkdir(mode=0o700)
        key = (source_state / "nh_interview_authenticity.key").read_bytes()
        key_path = state / "nh_interview_authenticity.key"
        key_path.write_bytes(key)
        key_path.chmod(0o600)
        journal = state / "nh_interview_journal.jsonl"
        journal.write_text("".join(selected), encoding="utf-8")
        journal.chmod(0o600)
        tail = events[-1]
        head = {
            "v": nh_loop.INTERVIEW_JOURNAL_HEAD_LABEL,
            "intent_generation": 1,
            "intent_number": 1,
            "intent_event_seq": event_seq,
            "intent_event_sha256": tail["event_sha256"],
            "committed_event_seq": event_seq,
            "committed_event_sha256": tail["event_sha256"],
        }
        head["head_auth_sha256"] = nh_loop.interview_journal_head_auth(key, head)
        head_path = state / "nh_interview_journal.head"
        head_path.write_text(
            nh_loop.interview_canonical_json(head) + "\n", encoding="utf-8"
        )
        head_path.chmod(0o600)
        with mock.patch.dict(
            os.environ, {nh_loop.INTERVIEW_STATE_DIR_ENV: str(state)}
        ):
            yield state, journal, events


class InitialQuestionReviewTests(unittest.TestCase):
    @staticmethod
    def _checkpoint_model_issue(issue_key):
        return {
            "standing_target_id": None,
            "issue_key": issue_key,
            "classification": "future_non_blocking",
            "topic_group": None,
            "question_intent_code": None,
            "subject_quote": None,
            "settled_basis_quote": None,
            "already_settled_note": "not already settled",
            "mechanical_note": "not mechanical",
            "still_open_note": "not open now",
            "why_ness_needed_note": "Ness is not needed now",
            "real_use_effect_note": "no current effect",
            "question_text": None,
            "user_facing_effects": [],
            "answer_effort": None,
            "dependency_key": None,
            "settled_answer_note": "future work only",
            "standing_witness": None,
            "options": None,
            "source_evidence": ["05_ACTIVE_CANDIDATE/a19.md"],
            "later_package_use": [],
        }

    @classmethod
    def _checkpoint_payload(cls):
        return {
            "package_id": "A19",
            "package_title": "Package A19",
            "whole_check_complete": True,
            "enumeration_complete": True,
            "source_paths_checked": ["05_ACTIVE_CANDIDATE/a19.md"],
            "page_index": 1,
            "page_count": 1,
            "total_issue_count": 2,
            "issues": [
                cls._checkpoint_model_issue("first_future_topic"),
                cls._checkpoint_model_issue("second_future_topic"),
            ],
            "unknowns": [],
        }

    @staticmethod
    def _checkpoint_scratchpad(folder):
        return {
            "path": os.path.join(folder, "validation-A19.json"),
            "sha256": "a" * 64,
            "bytes": 10,
            "package_scope_id": "A19",
            "source_binding_sha256": "b" * 64,
            "work_sha256": "c" * 64,
            "page_index": 1,
        }

    def test_first_custody_goes_to_coverage_not_a_second_full_validation(self):
        questions = {
            "q_initial": {
                "question_id": "q_initial",
                "package_scope_id": "A19",
                "first_custody_event_seq": 10,
                "retired": False,
                "_effective_answer": None,
            }
        }

        self.assertEqual([], nh_loop.first_custody_revalidation_claims(questions))

    def test_coverage_uses_one_complete_local_scratchpad(self):
        required_files = {
            "nh_master": {"matches": ["01_AUTHORITATIVE/master.md"]},
            "nh_decision_defaults": {"matches": ["01_AUTHORITATIVE/defaults.md"]},
            "cursorrules": {"matches": ["01_AUTHORITATIVE/cursorrules"]},
            "nh_project_companion": {"matches": ["01_AUTHORITATIVE/companion.md"]},
            "design_and_wiring_map": {"matches": ["02_WORKING_MAP/map.md"]},
        }
        blobs = {
            "01_AUTHORITATIVE/master.md": b"full master\n",
            "01_AUTHORITATIVE/defaults.md": b"full defaults\n",
            "02_WORKING_MAP/map.md": b"full map\n",
            "05_ACTIVE_CANDIDATE/a19.md": b"full A19 source\n",
            "04_ACCEPTED_STANDALONE_DESIGNS/evidence.md": b"full evidence\n",
        }
        errors = []
        source_paths = nh_loop.coverage_review_scratchpad_source_paths(
            required_files,
            "05_ACTIVE_CANDIDATE/a19.md",
            ["04_ACCEPTED_STANDALONE_DESIGNS/evidence.md"],
            {"by_path": blobs},
            errors,
        )
        self.assertEqual([], errors)

        self.assertEqual(sorted(blobs), source_paths)
        self.assertNotIn("01_AUTHORITATIVE/cursorrules", source_paths)
        self.assertNotIn("01_AUTHORITATIVE/companion.md", source_paths)

        inventory = {
            "inventory_is_complete": True,
            "every_classified_issue": [{"issue_key": "whole issue"}],
        }
        with tempfile.TemporaryDirectory(dir="/tmp") as folder, mock.patch.dict(
            os.environ,
            {nh_loop.INTERVIEW_STATE_DIR_ENV: os.path.join(folder, "state")},
        ):
            saved = nh_loop.build_coverage_review_scratchpad(
                "A19",
                "a" * 64,
                source_paths,
                {"by_path": blobs},
                inventory,
                ["full settled decision"],
                errors,
            )
            self.assertIsNotNone(saved)
            packet = json.loads(Path(saved["path"]).read_text(encoding="utf-8"))
            self.assertEqual(inventory, packet["completed_validation_inventory_complete"])
            retrieval = packet["source_retrieval_index"]
            self.assertEqual(
                sorted(blobs),
                [entry["path"] for entry in retrieval["source_manifest"]],
            )
            retrieved = retrieval["retrieved_exact_chunks"]
            self.assertEqual(
                ["full A19 source\n"],
                [
                    entry["content"]
                    for entry in retrieved
                    if "complete_package_source" in entry["selection_reasons"]
                ],
            )
            self.assertFalse(
                retrieval["retrieval_rule"].get("issue_term_sections_included", False)
            )
            self.assertTrue(
                retrieval["retrieval_rule"]["similarity_does_not_create_relationships"]
            )
            self.assertEqual(
                ["full settled decision"],
                packet["settled_ness_decisions_complete"],
            )
            self.assertEqual("a" * 64, packet["source_binding_sha256"])
            current_path = Path(saved["path"]).with_name("current-work.json")
            current = json.loads(current_path.read_text(encoding="utf-8"))
            self.assertEqual("input_saved", current["state"])
            self.assertEqual(saved["path"], current["complete_input"]["path"])
            self.assertIsNone(current["complete_result"])
            result_text = "full result\nשורה שנייה\n"
            result = nh_loop.save_coverage_review_scratchpad_result(
                saved, result_text, errors
            )
            self.assertEqual(
                result_text.encode("utf-8"), Path(result["path"]).read_bytes()
            )
            current = json.loads(current_path.read_text(encoding="utf-8"))
            self.assertEqual("result_saved", current["state"])
            self.assertEqual(result["path"], current["complete_result"]["path"])
            self.assertEqual(
                saved,
                nh_loop.build_coverage_review_scratchpad(
                    "A19",
                    "a" * 64,
                    source_paths,
                    {"by_path": blobs},
                    inventory,
                    ["full settled decision"],
                    errors,
                ),
            )
        self.assertEqual([], errors)

    def test_coverage_follows_explicit_links_not_similarity_or_file_size(self):
        blobs = {
            "05_ACTIVE_CANDIDATE/a19.md": (
                b"# A19\nA19 depends on \xc2\xa77M.\n## Detail\ncomplete package detail\n"
            ),
            "01_AUTHORITATIVE/master.md": (
                b"# Master\nsource identity\n"
                b"## \xc2\xa77M Display\nexplicitly linked behavior\n"
                b"## Similar words only\ninterface world visual behavior\n"
            ),
            "04_ACCEPTED_STANDALONE_DESIGNS/tiny.md": (
                b"# Tiny\nsource identity\n"
                b"## Unrelated\ninterface world visual behavior\n"
            ),
        }
        retrieval = nh_loop.build_coverage_retrieval_index(
            "A19",
            sorted(blobs),
            {"by_path": blobs},
            {"every_classified_issue": [{"issue_key": "interface world visual"}]},
            "05_ACTIVE_CANDIDATE/a19.md",
        )
        retrieved = retrieval["retrieved_exact_chunks"]
        selected_text = "\n".join(entry["content"] for entry in retrieved)
        self.assertIn("explicitly linked behavior", selected_text)
        self.assertNotIn("Similar words only", selected_text)
        self.assertNotIn("## Unrelated", selected_text)
        linked = next(
            entry for entry in retrieved if "explicitly linked behavior" in entry["content"]
        )
        self.assertIn("explicitly_referenced_section", linked["selection_reasons"])

    def test_question_validation_saves_the_same_exact_retrieval_input(self):
        blobs = {
            "05_ACTIVE_CANDIDATE/a19.md": b"# A19\nfull package source\n",
            "01_AUTHORITATIVE/master.md": (
                b"# Master\nidentity\n## A19\nexact related source\n"
                b"## Similar only\ninterface world visual\n"
            ),
        }
        errors = []
        with tempfile.TemporaryDirectory(dir="/tmp") as folder, mock.patch.dict(
            os.environ,
            {nh_loop.INTERVIEW_STATE_DIR_ENV: os.path.join(folder, "state")},
        ):
            saved = nh_loop.build_question_validation_scratchpad(
                "A19",
                "b" * 64,
                sorted(blobs),
                {"by_path": blobs},
                "05_ACTIVE_CANDIDATE/a19.md",
                errors,
            )
            self.assertIsNotNone(saved)
            packet = json.loads(Path(saved["path"]).read_text(encoding="utf-8"))
            self.assertEqual(
                nh_loop.QUESTION_VALIDATION_SCRATCHPAD_VERSION,
                packet["scratchpad_version"],
            )
            chunks = packet["source_retrieval_index"]["retrieved_exact_chunks"]
            self.assertIn("full package source", "\n".join(x["content"] for x in chunks))
            self.assertNotIn("Similar only", "\n".join(x["content"] for x in chunks))
            self.assertEqual("b" * 64, packet["source_binding_sha256"])
            current_path = Path(saved["path"]).with_name("current-work.json")
            current = json.loads(current_path.read_text(encoding="utf-8"))
            self.assertEqual("question_validation", current["stage"])
            self.assertEqual("input_saved", current["state"])
            self.assertEqual(saved["path"], current["complete_input"]["path"])
            self.assertIsNone(current["complete_result"])

            result_text = "complete question result\nשום דבר לא קוצר\n"
            result = nh_loop.save_question_validation_scratchpad_result(
                saved, result_text, errors
            )
            self.assertEqual(
                result_text.encode("utf-8"), Path(result["path"]).read_bytes()
            )
            current = json.loads(current_path.read_text(encoding="utf-8"))
            self.assertEqual("question_validation", current["stage"])
            self.assertEqual("result_saved", current["state"])
            self.assertEqual(result["path"], current["complete_result"]["path"])
            self.assertEqual(
                "validate_and_commit_question_validation_result",
                current["next_action"],
            )
            committed = (
                nh_loop.mark_question_validation_scratchpad_result_committed(
                    saved, errors
                )
            )
            self.assertIsNotNone(committed)
            current = json.loads(current_path.read_text(encoding="utf-8"))
            self.assertEqual("result_committed", current["state"])
            self.assertEqual(result["path"], current["complete_result"]["path"])
            self.assertEqual(
                "continue_from_committed_question_validation_result",
                current["next_action"],
            )
        self.assertEqual([], errors)
        self.assertIn(
            "Use only the exact local scratch pad",
            nh_loop.QUESTION_VALIDATION_PROMPT_HEAD,
        )
        self.assertNotIn(
            "Open and read the COMPLETE contents",
            nh_loop.QUESTION_VALIDATION_PROMPT_HEAD,
        )

    def test_provider_boundary_saves_complete_question_result_locally(self):
        text = json.dumps({"answer": "full result"}, sort_keys=True)
        scratchpad = {
            "path": "/tmp/validation-A19.json",
            "sha256": "a" * 64,
            "bytes": 10,
            "package_scope_id": "A19",
            "source_binding_sha256": "b" * 64,
        }
        frozen = {
            "controller_held_identity": {"package_scope_id": "A19"},
            "pagination": {"expected_page_index": 1},
            "source_binding": {"binding_sha256": "b" * 64},
            "questions": {},
            "routed_by_id": {},
        }
        precall = {
            "precall_source_requirement": {
                "package_binding": {"package_scope_id": "A19"},
                "relevant_closure": {"unresolved": []},
            },
            "journal_position": 1,
            "question_validation_scratchpad": scratchpad,
        }
        validated = {
            "page_index": 1,
            "unknowns": [],
            "_relevant_closure": {"unresolved": []},
        }
        errors = []
        with mock.patch.object(
            nh_loop, "validate_question_validation_payload", return_value=validated
        ), mock.patch.object(
            nh_loop, "prepare_validation_record", return_value={"prepared": True}
        ), mock.patch.object(
            nh_loop,
            "save_question_validation_scratchpad_result",
            return_value={"path": "/tmp/result", "sha256": "c" * 64, "bytes": 1},
        ) as save_result:
            result = nh_loop._continuation_question_validation_full_contract(
                text, frozen, precall, errors
            )
        self.assertEqual({"answer": "full result"}, result)
        save_result.assert_called_once_with(scratchpad, text, errors)
        self.assertEqual([], errors)

    def test_issue_progress_uses_structured_failure_scope_not_error_words(self):
        payload = self._checkpoint_payload()
        errors = []
        with tempfile.TemporaryDirectory(dir="/tmp") as folder:
            scratchpad = self._checkpoint_scratchpad(folder)
            saved = nh_loop.save_question_validation_issue_progress(
                scratchpad,
                json.dumps(payload),
                ["opaque failure with no question name or number"],
                {"global": False, "issue_indexes": {1}},
                "A19",
                1,
                errors,
            )
            self.assertIsNotNone(saved)
            self.assertEqual([0], [item["index"] for item in saved["locked_issues"]])
            self.assertEqual([1], saved["pending_issue_indexes"])
            loaded = nh_loop.read_question_validation_issue_progress(
                scratchpad, errors
            )
            self.assertEqual(saved, loaded)
        self.assertEqual([], errors)

    def test_global_failure_does_not_lock_new_questions(self):
        payload = self._checkpoint_payload()
        errors = []
        with tempfile.TemporaryDirectory(dir="/tmp") as folder:
            saved = nh_loop.save_question_validation_issue_progress(
                self._checkpoint_scratchpad(folder),
                json.dumps(payload),
                ["page-wide failure"],
                {"global": True, "issue_indexes": set()},
                "A19",
                1,
                errors,
            )
        self.assertIsNotNone(saved)
        self.assertEqual([], saved["locked_issues"])
        self.assertEqual([0, 1], saved["pending_issue_indexes"])
        self.assertEqual([], errors)

    def test_failure_keeps_an_explicitly_linked_group_pending(self):
        payload = self._checkpoint_payload()
        errors = []
        with tempfile.TemporaryDirectory(dir="/tmp") as folder, mock.patch.object(
            nh_loop,
            "question_validation_issue_components",
            return_value=[{0, 1}],
        ):
            saved = nh_loop.save_question_validation_issue_progress(
                self._checkpoint_scratchpad(folder),
                json.dumps(payload),
                ["one member of the linked group failed"],
                {"global": False, "issue_indexes": {1}},
                "A19",
                1,
                errors,
            )
        self.assertIsNotNone(saved)
        self.assertEqual([], saved["locked_issues"])
        self.assertEqual([0, 1], saved["pending_issue_indexes"])
        self.assertEqual([], errors)

    def test_retry_may_change_only_pending_questions(self):
        payload = self._checkpoint_payload()
        errors = []
        with tempfile.TemporaryDirectory(dir="/tmp") as folder:
            scratchpad = self._checkpoint_scratchpad(folder)
            progress = nh_loop.save_question_validation_issue_progress(
                scratchpad,
                json.dumps(payload),
                ["second issue failed"],
                {"global": False, "issue_indexes": {1}},
                "A19",
                1,
                errors,
            )
            scratchpad["issue_progress"] = progress
            corrected_pending = json.loads(json.dumps(payload))
            corrected_pending["issues"][1]["mechanical_note"] = "corrected pending"
            self.assertTrue(
                nh_loop.question_validation_retry_locks_hold(
                    scratchpad, json.dumps(corrected_pending), errors
                )
            )
            changed_locked = json.loads(json.dumps(corrected_pending))
            changed_locked["issues"][0]["mechanical_note"] = "changed locked"
            lock_errors = []
            self.assertFalse(
                nh_loop.question_validation_retry_locks_hold(
                    scratchpad, json.dumps(changed_locked), lock_errors
                )
            )
            self.assertTrue(lock_errors)
        self.assertEqual([], errors)

    def test_issue_progress_identity_separates_pages_and_work(self):
        with tempfile.TemporaryDirectory(dir="/tmp") as folder:
            first = self._checkpoint_scratchpad(folder)
            page_two = dict(first, page_index=2)
            other_work = dict(first, work_sha256="d" * 64)
            self.assertNotEqual(
                nh_loop.question_validation_issue_progress_path(first),
                nh_loop.question_validation_issue_progress_path(page_two),
            )
            self.assertNotEqual(
                nh_loop.question_validation_issue_progress_path(first),
                nh_loop.question_validation_issue_progress_path(other_work),
            )

    def test_full_validator_reports_issue_scope_without_message_parsing(self):
        frozen = {
            "controller_held_identity": {"package_scope_id": "A19"},
            "pagination": {"expected_page_index": 1},
        }
        precall = {
            "journal_position": 1,
            "precall_source_requirement": {"package_binding": {"bound": True}},
        }
        scopes = {"global": True, "issue_indexes": set()}
        errors = []

        def refuse(*args, **kwargs):
            kwargs["failure_scopes"].update(
                {"global": False, "issue_indexes": {1}}
            )
            errors.append("opaque validator failure")
            return None

        with mock.patch.object(
            nh_loop, "validate_question_validation_payload", side_effect=refuse
        ):
            result = nh_loop._prepare_question_validation_from_frozen(
                "{}", frozen, precall, {"_events": []}, errors, scopes
            )
        self.assertIsNone(result)
        self.assertEqual(False, scopes["global"])
        self.assertEqual({1}, scopes["issue_indexes"])

    def test_provider_failure_saves_only_the_independently_valid_question(self):
        payload = self._checkpoint_payload()
        frozen = {
            "controller_held_identity": {"package_scope_id": "A19"},
            "pagination": {"expected_page_index": 1},
            "questions": {},
            "routed_by_id": {},
        }
        errors = []
        with tempfile.TemporaryDirectory(dir="/tmp") as folder:
            scratchpad = self._checkpoint_scratchpad(folder)
            precall = {
                "journal_position": 1,
                "question_validation_scratchpad": scratchpad,
                "precall_source_requirement": {
                    "package_binding": {"bound": True},
                    "relevant_closure": {"package_id": "A19"},
                },
            }

            def reject(_text, _frozen, _precall, _state, target_errors, *, failure_scopes):
                failure_scopes.update({"global": False, "issue_indexes": {1}})
                target_errors.append("opaque issue failure")
                return None

            with mock.patch.object(
                nh_loop,
                "save_question_validation_scratchpad_result",
                return_value={"path": "saved", "sha256": "d" * 64, "bytes": 1},
            ), mock.patch.object(
                nh_loop,
                "_prepare_question_validation_from_frozen",
                side_effect=reject,
            ):
                result = nh_loop._continuation_question_validation_full_contract(
                    json.dumps(payload), frozen, precall, errors
                )
            self.assertIsNone(result)
            checkpoint = nh_loop.read_question_validation_issue_progress(
                scratchpad, []
            )
            self.assertEqual(
                [0], [entry["index"] for entry in checkpoint["locked_issues"]]
            )
            self.assertEqual([1], checkpoint["pending_issue_indexes"])
        self.assertEqual(["opaque issue failure"], errors)

    def test_commit_uses_frozen_material_without_reentering_full_command(self):
        value = {"answer": "saved"}
        scratchpad = {
            "path": "/tmp/validation-A19.json",
            "sha256": "a" * 64,
            "bytes": 10,
            "package_scope_id": "A19",
            "source_binding_sha256": "b" * 64,
        }
        precall = {
            "package_scope_id": "A19",
            "journal_position": 2,
            "question_validation_scratchpad": scratchpad,
            "validation_context": {
                "source_binding": {"binding_sha256": "b" * 64},
                "standing_chain_sha256": "c" * 64,
            },
        }
        state = {
            "_events": [{"event_seq": 1}],
            "standing_chain_sha256": "c" * 64,
        }
        errors = []
        with (
            mock.patch.object(
                nh_loop,
                "read_source_binding",
                return_value={"binding_sha256": "b" * 64},
            ),
            mock.patch.object(
                nh_loop,
                "read_interview_journal",
                return_value=("journal", state["_events"]),
            ),
            mock.patch.object(
                nh_loop, "replay_interview_state", return_value=dict(state)
            ),
            mock.patch.object(
                nh_loop,
                "_prepare_question_validation_from_frozen",
                return_value={"prepared": {"body": {"type": "validation_recorded"}}},
            ),
            mock.patch.object(
                nh_loop,
                "append_interview_event",
                return_value={"type": "validation_recorded"},
            ) as append,
            mock.patch.object(
                nh_loop,
                "save_question_validation_scratchpad_result",
                return_value={"path": "/tmp/result", "sha256": "d" * 64, "bytes": 1},
            ),
            mock.patch.object(
                nh_loop,
                "mark_question_validation_scratchpad_result_committed",
                return_value={"path": "current-work.json"},
            ),
            mock.patch.object(nh_loop, "command_question_validation") as old_part_b,
        ):
            result = nh_loop._continuation_piece3_commit(
                "A19",
                "question_validation",
                value,
                {"precall_requirement": precall},
                errors,
            )
        self.assertTrue(result["committed"])
        self.assertEqual([], errors)
        append.assert_called_once()
        old_part_b.assert_not_called()

    def test_reconstructed_input_pointer_is_restored_to_the_exact_committed_result(self):
        value = {"answer": "saved"}
        with tempfile.TemporaryDirectory(dir="/tmp") as folder:
            scratchpad = self._checkpoint_scratchpad(folder)
            precall = {
                "package_scope_id": "A19",
                "journal_position": 2,
                "question_validation_scratchpad": scratchpad,
                "validation_context": {
                    "source_binding": {"binding_sha256": "b" * 64},
                    "standing_chain_sha256": "c" * 64,
                },
            }
            state = {
                "_events": [{"event_seq": 1}],
                "standing_chain_sha256": "c" * 64,
            }
            errors = []
            nh_loop.write_ai_current_work_state(
                scratchpad, "question_validation", "input_saved", errors
            )
            with (
                mock.patch.object(
                    nh_loop,
                    "read_source_binding",
                    return_value={"binding_sha256": "b" * 64},
                ),
                mock.patch.object(
                    nh_loop,
                    "read_interview_journal",
                    return_value=("journal", state["_events"]),
                ),
                mock.patch.object(
                    nh_loop, "replay_interview_state", return_value=dict(state)
                ),
                mock.patch.object(
                    nh_loop,
                    "_prepare_question_validation_from_frozen",
                    return_value={"prepared": {"body": {"type": "validation_recorded"}}},
                ),
                mock.patch.object(
                    nh_loop,
                    "append_interview_event",
                    return_value={"type": "validation_recorded"},
                ),
            ):
                result = nh_loop._continuation_piece3_commit(
                    "A19",
                    "question_validation",
                    value,
                    {"precall_requirement": precall},
                    errors,
                )

            current = json.loads(
                Path(folder, "current-work.json").read_text(encoding="utf-8")
            )
            expected = nh_loop.nh_supervisor.canonical.canonical_json(value).encode(
                "utf-8"
            )
            self.assertTrue(result["committed"])
            self.assertTrue(result["scratchpad_pointer_updated"])
            self.assertEqual("result_committed", current["state"])
            self.assertEqual(hashlib.sha256(expected).hexdigest(), current["complete_result"]["sha256"])
            self.assertEqual([], errors)

    def test_committed_journal_event_is_not_reported_refused_when_pointer_update_fails(self):
        value = {"answer": "saved"}
        scratchpad = {
            "path": "/tmp/validation-A19.json",
            "sha256": "a" * 64,
            "bytes": 10,
            "package_scope_id": "A19",
            "source_binding_sha256": "b" * 64,
        }
        precall = {
            "package_scope_id": "A19",
            "journal_position": 2,
            "question_validation_scratchpad": scratchpad,
            "validation_context": {
                "source_binding": {"binding_sha256": "b" * 64},
                "standing_chain_sha256": "c" * 64,
            },
        }
        state = {
            "_events": [{"event_seq": 1}],
            "standing_chain_sha256": "c" * 64,
        }
        errors = []

        def pointer_failure(_scratchpad, pointer_errors):
            pointer_errors.append("pointer could not be updated")
            return None

        with (
            mock.patch.object(
                nh_loop,
                "read_source_binding",
                return_value={"binding_sha256": "b" * 64},
            ),
            mock.patch.object(
                nh_loop,
                "read_interview_journal",
                return_value=("journal", state["_events"]),
            ),
            mock.patch.object(
                nh_loop, "replay_interview_state", return_value=dict(state)
            ),
            mock.patch.object(
                nh_loop,
                "save_question_validation_scratchpad_result",
                return_value={"path": "/tmp/result", "sha256": "d" * 64, "bytes": 1},
            ),
            mock.patch.object(
                nh_loop,
                "_prepare_question_validation_from_frozen",
                return_value={"prepared": {"body": {"type": "validation_recorded"}}},
            ),
            mock.patch.object(
                nh_loop,
                "append_interview_event",
                return_value={"type": "validation_recorded"},
            ) as append,
            mock.patch.object(
                nh_loop,
                "mark_question_validation_scratchpad_result_committed",
                side_effect=pointer_failure,
            ),
        ):
            result = nh_loop._continuation_piece3_commit(
                "A19",
                "question_validation",
                value,
                {"precall_requirement": precall},
                errors,
            )

        self.assertTrue(result["committed"])
        self.assertFalse(result["scratchpad_pointer_updated"])
        self.assertEqual(["pointer could not be updated"], result["scratchpad_pointer_errors"])
        self.assertEqual([], errors)
        append.assert_called_once()

    def test_controller_selection_commit_survives_precall_pointer_rebuild(self):
        selection = {
            "package_scope_id": "A19",
            "package_id": "A19",
            "scope_root_path": "a19.md",
        }
        value = {"answer": "saved"}
        with tempfile.TemporaryDirectory(dir="/tmp") as folder:
            scratchpad = self._checkpoint_scratchpad(folder)
            precall = {
                "package_scope_id": "A19",
                "journal_position": 2,
                "question_validation_scratchpad": scratchpad,
                "validation_context": {
                    "source_binding": {"binding_sha256": "b" * 64},
                    "standing_chain_sha256": "c" * 64,
                },
            }
            nh_loop.save_question_validation_scratchpad_result(
                scratchpad,
                nh_loop.nh_supervisor.canonical.canonical_json(value),
                [],
            )
            events = [{"event_seq": 1}]
            context = SimpleNamespace(
                binding=SimpleNamespace(
                    package_scope_id="A19",
                    package_id="A19",
                    scope_root_path="a19.md",
                ),
                transition_facts={
                    "package_scope_id": "A19",
                    "continuation_selection": selection,
                    "scope_has_validation": False,
                    "scope_validation_complete": False,
                },
                journal=SimpleNamespace(read=lambda: events),
            )
            authorization = {
                "package_scope_id": "A19",
                "authorizes_event_type": "validation_recorded",
                "provider_request_identity": "request",
                "result_custody_identity": "custody",
                "work_item_identity": "work-id",
            }
            custody = {
                "work_item_kind": "question_validation",
                "provider_request_identity": "request",
                "result_custody_identity": "custody",
            }
            terminal = {"terminal_kind": "result_received"}
            situation = SimpleNamespace(candidate=object())

            class Scoped:
                def __init__(self, _events, _scope):
                    pass

                def unconsumed_piece3_authorization(self, _event_type):
                    return authorization

                def custody_event(self, _request_identity):
                    return custody

                def terminal_event(self, _request_identity):
                    return terminal

                def prepared_event(self, _request_identity):
                    return {"type": "provider_request_prepared"}

            completed = []
            operation = SimpleNamespace(
                appended=[],
                start=lambda: None,
                complete=completed.append,
            )

            def rebuild_precall(*_args):
                nh_loop.write_ai_current_work_state(
                    scratchpad, "question_validation", "input_saved", []
                )
                return precall

            adapter = SimpleNamespace(
                piece3_precall_requirement=rebuild_precall,
                piece3_commit=nh_loop._continuation_piece3_commit,
            )
            with (
                mock.patch.object(commands, "require_start_gate"),
                mock.patch.object(
                    commands,
                    "read_state",
                    return_value=(events, situation, "LIVE_PROVED", {}),
                ),
                mock.patch.object(commands, "refuse_on_contradiction"),
                mock.patch.object(commands.replay_mod, "Replay", Scoped),
                mock.patch.object(
                    commands.engine,
                    "custodied_bytes",
                    return_value=nh_loop.nh_supervisor.canonical.canonical_json(value).encode(
                        "utf-8"
                    ),
                ),
                mock.patch.object(commands, "_rebuild_work_item", return_value={}),
                mock.patch.object(commands, "build_envelope", return_value={}),
                mock.patch.object(commands.engine, "Operation", return_value=operation),
                mock.patch.object(commands, "_continuation_adapter", return_value=adapter),
                mock.patch.object(
                    nh_loop,
                    "read_source_binding",
                    return_value={"binding_sha256": "b" * 64},
                ),
                mock.patch.object(
                    nh_loop,
                    "read_interview_journal",
                    return_value=("journal", events),
                ),
                mock.patch.object(
                    nh_loop,
                    "replay_interview_state",
                    return_value={
                        "_events": events,
                        "standing_chain_sha256": "c" * 64,
                    },
                ),
                mock.patch.object(
                    nh_loop,
                    "_prepare_question_validation_from_frozen",
                    return_value={"prepared": {"body": {"type": "validation_recorded"}}},
                ),
                mock.patch.object(
                    nh_loop,
                    "append_interview_event",
                    return_value={"type": "validation_recorded"},
                ),
            ):
                result = commands.commit_piece3_provider_result_for_controller_selection(
                    context, selection
                )

            current = json.loads(
                Path(folder, "current-work.json").read_text(encoding="utf-8")
            )
            self.assertTrue(result.report["ok"])
            self.assertEqual(["ok"], completed)
            self.assertEqual("result_committed", current["state"])

    def test_unchecked_later_questions_remain_pending_across_sequential_form_failures(self):
        raw_payload = self._checkpoint_payload()
        raw_payload["issues"].append(self._checkpoint_model_issue("third_future_topic"))
        raw_payload["total_issue_count"] = 3
        issues = raw_payload["issues"]
        payload = dict(raw_payload, **{
            "_package_key": "A19",
            "_package_scope_id": "A19",
            "_manifest": {"manifest_sha256": "m", "paths": []},
            "_relevant_closure": {},
            "_package_source_binding": {},
        })
        pagination = {
            "segment_number": 1,
            "generation": 1,
            "previous_segment_id": None,
            "continuing": False,
            "set_started_at_event_seq": None,
            "validation_set_id": None,
            "enumeration_complete": False,
            "enumeration_seen_issue_keys": [],
            "enumeration_seen_target_ids": [],
            "recorded_issue_keys": [],
            "enumeration_seen_form_identities": [],
        }
        state = {"_events": [], "questions": {}, "routed_issues": {}}

        def composition(issue, *_args, **_kwargs):
            return {"issue_key": issue["issue_key"]}

        def form(composed, *_args):
            return [composed["issue_key"]]

        with (
            mock.patch.object(
                nh_loop,
                "interview_validation_set_id",
                return_value="validation-set",
            ),
            mock.patch.object(
                nh_loop,
                "question_validation_page_issue_contract",
                return_value={"required": 3},
            ),
            mock.patch.object(
                nh_loop, "standing_targets_requiring_account", return_value=set()
            ),
            mock.patch.object(
                nh_loop,
                "controller_held_standing_targets",
                return_value={},
            ),
            mock.patch.object(
                nh_loop,
                "screen_validated_issues",
                return_value={"asked": issues, "stripped": [], "refused": []},
            ),
            mock.patch.object(nh_loop, "question_peer_index_with_held", return_value={}),
            mock.patch.object(nh_loop, "build_question_composition", side_effect=composition),
            mock.patch.object(nh_loop, "build_ness_question_form", side_effect=form),
            mock.patch.object(nh_loop, "ness_form_identity", side_effect=lambda item: item["issue_key"]),
            mock.patch.object(
                nh_loop,
                "names_mechanism",
                side_effect=lambda text: (
                    ["mechanism"]
                    if text in ("second_future_topic", "third_future_topic")
                    else []
                ),
            ),
        ):
            first_scopes = {"global": False, "issue_indexes": set()}
            first_errors = []
            first = nh_loop.prepare_validation_record(
                payload,
                {"binding_sha256": "b", "branch": "main", "head_sha": "h"},
                pagination,
                state,
                first_errors,
                failure_scopes=first_scopes,
            )
            self.assertIsNone(first)
            self.assertEqual({1, 2}, first_scopes["issue_indexes"])
            with tempfile.TemporaryDirectory(dir="/tmp") as folder:
                scratchpad = self._checkpoint_scratchpad(folder)
                first_progress = nh_loop.save_question_validation_issue_progress(
                    scratchpad,
                    json.dumps(raw_payload),
                    first_errors,
                    first_scopes,
                    "A19",
                    1,
                    [],
                )
                self.assertEqual(
                    [0], [entry["index"] for entry in first_progress["locked_issues"]]
                )
                self.assertEqual([1, 2], first_progress["pending_issue_indexes"])

                issues[1]["issue_key"] = "second-fixed"
                second_scopes = {"global": False, "issue_indexes": set()}
                second_errors = []
                second = nh_loop.prepare_validation_record(
                    payload,
                    {"binding_sha256": "b", "branch": "main", "head_sha": "h"},
                    pagination,
                    state,
                    second_errors,
                    failure_scopes=second_scopes,
                )
                self.assertIsNone(second)
                self.assertEqual({2}, second_scopes["issue_indexes"])
                second_progress = nh_loop.save_question_validation_issue_progress(
                    scratchpad,
                    json.dumps(raw_payload),
                    second_errors,
                    second_scopes,
                    "A19",
                    1,
                    [],
                )
                self.assertEqual(
                    [0, 1],
                    [entry["index"] for entry in second_progress["locked_issues"]],
                )
                self.assertEqual([2], second_progress["pending_issue_indexes"])


class NessOwnWordsAnswerTests(unittest.TestCase):
    @classmethod
    def _event_1545_state(cls):
        events = [
            json.loads(line)
            for line in (ROOT / "nh_interview_state" / "nh_interview_journal.jsonl")
            .read_text(encoding="utf-8")
            .splitlines()
            if line.strip() and json.loads(line).get("event_seq", 0) <= 1545
        ]
        errors = []
        state = nh_loop.replay_interview_state(events, errors)
        if errors:
            raise AssertionError(errors)
        return events, state

    @staticmethod
    def _composition():
        return {
            "options": [
                {
                    "option_id": "yes",
                    "meaning_sentence": "Use the automatic behavior.",
                    "consequence_sentences": ["The automatic behavior is used."],
                    "also_settles": [],
                    "also_removes": [],
                    "unlocks_dependency_keys": [],
                    "unlocks_dependency_ids": [],
                },
                {
                    "option_id": "no",
                    "meaning_sentence": "Do not use the automatic behavior.",
                    "consequence_sentences": ["The automatic behavior is not used."],
                    "also_settles": [],
                    "also_removes": [],
                    "unlocks_dependency_keys": [],
                    "unlocks_dependency_ids": [],
                },
            ]
        }

    def test_explicit_own_words_choice_accepts_a_clear_unlisted_answer(self):
        interpretation = nh_loop.interpret_ness_answer(
            self._composition(),
            "N.H should understand the situation, choose, and let me override it.",
            nh_loop.NESS_OWN_WORDS_OPTION_ID,
        )

        self.assertEqual(
            nh_loop.INTERVIEW_INTERPRETATION_OWN_WORDS,
            interpretation["status"],
        )
        self.assertEqual(
            nh_loop.NESS_OWN_WORDS_OPTION_ID,
            interpretation["selected_option_id"],
        )
        self.assertTrue(nh_loop.interview_interpretation_settles(interpretation))

    def test_own_words_answer_infers_no_cross_question_effects(self):
        interpretation = nh_loop.interpret_ness_answer(
            self._composition(),
            "It depends on the full context, and my choice always wins.",
            nh_loop.NESS_OWN_WORDS_OPTION_ID,
        )

        consequences = nh_loop.derive_mechanical_consequences(
            self._composition(), interpretation
        )

        self.assertTrue(consequences["derived"])
        self.assertEqual([], consequences["settles_question_ids"])
        self.assertEqual([], consequences["removes_question_ids"])
        self.assertEqual([], consequences["satisfies_dependency_ids"])

    def test_unlisted_answer_without_explicit_choice_is_preserved_as_own_words(self):
        interpretation = nh_loop.interpret_ness_answer(
            self._composition(), "Something else entirely.", None
        )

        self.assertEqual(
            nh_loop.INTERVIEW_INTERPRETATION_OWN_WORDS,
            interpretation["status"],
        )
        self.assertEqual(
            nh_loop.NESS_OWN_WORDS_OPTION_ID,
            interpretation["selected_option_id"],
        )
        self.assertTrue(nh_loop.interview_interpretation_settles(interpretation))

    def test_question_form_makes_declared_options_non_exclusive_examples(self):
        composition = {
            "v": "nh-ness-question-composition-v4",
            "question_id": "q_test",
            "topic_name": "how you stay in control and correct it",
            "question_sentence": "When should N.H do this on its own?",
            "effect_sentences": ["what N.H actually does here"],
            "subject_quote": "a subject long enough to be a proved source quote",
            "subject_quote_path": "subject.md",
            "settled_basis_quote": "a settled rule long enough to be a proved quote",
            "settled_basis_quote_path": "settled.md",
            "checked_source": {
                "paths_checked": 2,
                "branch": "nh-design-loop",
                "head_sha_short": "0123456789ab",
            },
            "options": self._composition()["options"],
        }

        lines = nh_loop.build_ness_question_form(composition, 1, 1)

        self.assertIn(
            "  Some examples to help you think (not the only answers):", lines
        )
        self.assertIn(
            "  You may combine examples, make the rule depend on the situation, "
            "or give a different answer in your own words.",
            lines,
        )
        self.assertNotIn("  The options are:", lines)

    def test_every_controller_owned_question_sentence_is_mechanism_free(self):
        sentences = (
            list(nh_loop.NESS_QUESTION_INTENT_SENTENCES.values())
            + list(nh_loop.NESS_QUESTION_USER_FACING_EFFECT_SENTENCES.values())
            + list(nh_loop.NESS_OPTION_MEANING_SENTENCES.values())
            + list(nh_loop.NESS_OPTION_CONSEQUENCE_SENTENCES.values())
        )

        for sentence in sentences:
            self.assertEqual([], nh_loop.names_mechanism(sentence), sentence)

    def test_question_delivery_refuses_a_technical_subject_even_in_a_valid_form(self):
        composition = {
            "v": "nh-ness-question-composition-v4",
            "question_id": "q_test",
            "topic_name": "how N.H behaves automatically",
            "question_sentence": "When should N.H do this on its own, and when should it wait for you?",
            "effect_sentences": ["what N.H actually does here"],
            "subject_quote": "choose the REST API endpoint used by this feature",
            "subject_quote_path": "subject.md",
            "settled_basis_quote": "the current behaviour remains unchanged until Ness decides",
            "settled_basis_quote_path": "settled.md",
            "checked_source": {
                "paths_checked": 2,
                "branch": "nh-design-loop",
                "head_sha_short": "0123456789ab",
            },
            "options": self._composition()["options"],
        }
        lines = nh_loop.build_ness_question_form(composition, 1, 1)
        errors = []

        self.assertFalse(
            nh_loop.verify_ness_question_form(lines, composition, 1, 1, errors)
        )
        self.assertTrue(any("implementation machinery" in item for item in errors))

    def test_historical_v3_question_form_keeps_its_original_wording(self):
        composition = {
            "v": "nh-ness-question-composition-v3",
            "question_id": "q_test",
            "topic_name": "how you stay in control and correct it",
            "question_sentence": "When should N.H do this on its own?",
            "effect_sentences": ["what N.H actually does here"],
            "subject_quote": "a subject long enough to be a proved source quote",
            "subject_quote_path": "subject.md",
            "settled_basis_quote": "a settled rule long enough to be a proved quote",
            "settled_basis_quote_path": "settled.md",
            "checked_source": {
                "paths_checked": 2,
                "branch": "nh-design-loop",
                "head_sha_short": "0123456789ab",
            },
            "options": self._composition()["options"],
        }

        lines = nh_loop.build_ness_question_form(composition, 1, 1)

        self.assertIn("  The options are:", lines)
        self.assertNotIn(
            "  Some examples to help you think (not the only answers):", lines
        )

    def test_question_validation_prompt_forbids_false_binary_forms(self):
        prompt = nh_loop.QUESTION_VALIDATION_PROMPT_HEAD

        self.assertIn("They are examples, never an exhaustive answer form.", prompt)
        self.assertIn("Do not create a false binary.", prompt)
        self.assertIn("a combination, a context-dependent rule", prompt)

    def test_question_validation_reads_complete_scratchpad_and_proves_current_version(self):
        prompt = nh_loop.QUESTION_VALIDATION_PROMPT_HEAD

        self.assertIn("Use only the exact local scratch pad", prompt)
        self.assertIn("the current package source in full", prompt)
        self.assertIn("Use acceptance only when an exact included source", prompt)
        self.assertIn("Use supersession only when an exact included source", prompt)
        self.assertIn("A filename, number, date or folder never proves", prompt)
        self.assertIn("report it as unknown and do not guess", prompt)

    def test_every_source_reading_stage_uses_the_same_current_version_rule(self):
        repository_reading_prompts = (
            nh_loop.NEXT_PACKAGE_PROMPT,
            nh_loop.PREPARE_TASK_PROMPT_TAIL,
            nh_loop.DESIGN_AUDIT_PROMPT_TAIL_HEAD,
            nh_loop.bundle_seven_prompt(["one.md"]),
            nh_loop.bundle_seven_relationships_prompt(["one.md"], []),
        )

        for prompt in repository_reading_prompts:
            self.assertEqual(1, prompt.count(nh_loop.CURRENT_SOURCE_READING_RULES))
            self.assertIn("Open and read the COMPLETE contents", prompt)
            self.assertIn("A newer-looking name or date never proves acceptance", prompt)
            self.assertIn("Never infer supersession from version order", prompt)

        scratchpad_prompt = nh_loop.QUESTION_VALIDATION_PROMPT_HEAD
        self.assertIn("Use only the exact local scratch pad", scratchpad_prompt)
        self.assertIn("the current package source in full", scratchpad_prompt)
        self.assertIn(
            "Use acceptance only when an exact included source",
            scratchpad_prompt,
        )
        self.assertIn(
            "Use supersession only when an exact included source",
            scratchpad_prompt,
        )

        coverage_prompt = nh_loop.COVERAGE_REVIEW_PROMPT_HEAD
        self.assertIn("Use only the local coverage scratch pad", coverage_prompt)
        self.assertIn("the current package source in full", coverage_prompt)
        self.assertIn("Similarity, timing, shared words", coverage_prompt)

    def test_question_validation_prompt_matches_complete_answers_and_asks_only_gaps(self):
        prompt = nh_loop.QUESTION_VALIDATION_PROMPT_HEAD

        self.assertIn("COMPLETE-OR-GAP RULE", prompt)
        self.assertIn("by meaning rather than by identical wording", prompt)
        self.assertIn("If it settles the whole decision", prompt)
        self.assertIn("ask ONLY for the consequential missing part", prompt)
        self.assertIn("include that choice as its own genuinely_open_for_ness issue", prompt)

    def test_question_validation_prompt_requires_bundle_seven_baseline_before_questions(self):
        prompt = nh_loop.QUESTION_VALIDATION_PROMPT_HEAD

        self.assertIn("BUNDLE-SEVEN BASELINE BEFORE QUESTIONS", prompt)
        self.assertIn("current authenticated Bundle-Seven baseline", prompt)
        self.assertIn("Refuse to classify the package if that context is absent", prompt)
        self.assertIn("Do not present any question until the shared baseline is current", prompt)

    def test_question_validation_prompt_requires_same_scope_preserved_answer(self):
        prompt = nh_loop.QUESTION_VALIDATION_PROMPT_TAIL_HEAD

        self.assertIn(
            "preserved_ness_answers_currently_standing_in_selected_package_scope",
            prompt,
        )
        self.assertIn("exact package_scope_id selected for this call", prompt)
        self.assertIn("Do not infer a Ness answer from", prompt)
        self.assertIn("answer in another package scope", prompt)

    def test_question_validation_prompt_enforces_ness_diamond_rule(self):
        prompt = nh_loop.QUESTION_VALIDATION_PROMPT_HEAD

        self.assertIn("NESS DECISION BOUNDARY -- THE DIAMOND RULE", prompt)
        self.assertIn("The word technical does not make a decision mechanical", prompt)
        self.assertIn("Ness decides WHAT the system does", prompt)
        self.assertIn("including chat, physical interaction and VR", prompt)

    def test_question_validation_effects_include_visible_placement(self):
        self.assertIn(
            "what_shows_up_where", nh_loop.NESS_QUESTION_USER_FACING_EFFECTS
        )

    def test_question_validation_prompt_forbids_paraphrased_settled_quote(self):
        prompt = nh_loop.QUESTION_VALIDATION_PROMPT_TAIL

        self.assertIn("Never put a remembered Ness answer", prompt)
        self.assertIn("search the cited file for the complete literal string", prompt)

    def test_question_validation_prompt_forbids_duplicate_option_meanings(self):
        prompt = nh_loop.QUESTION_VALIDATION_PROMPT_TAIL

        self.assertIn("Every option in one issue must use a DISTINCT meaning code", prompt)
        self.assertIn("same meaning twice", prompt)

    def test_question_validation_prompt_requires_final_evidence_subset_check(self):
        prompt = nh_loop.QUESTION_VALIDATION_PROMPT_TAIL

        self.assertIn("FINAL PATH-SET CHECK", prompt)
        self.assertIn("compare every source_evidence entry", prompt)
        self.assertIn("baseline context is not checked evidence", prompt)

    def test_subject_key_match_accepts_english_possessive_in_source_passage(self):
        key = "external.actions.initiated.from.within.ness.world"

        self.assertTrue(
            nh_loop.subject_key_occurs_in(
                key, "external actions initiated from within Ness's World"
            )
        )
        self.assertTrue(
            nh_loop.subject_key_occurs_in(
                key, "external actions initiated from within Ness’s World"
            )
        )
        self.assertFalse(
            nh_loop.subject_key_occurs_in(
                key, "external actions initiated from within another world"
            )
        )

    def test_subject_key_match_accepts_bounded_grammar_words(self):
        self.assertTrue(
            nh_loop.subject_key_occurs_in(
                "opens.through.white.door", "whether it opens through a white door"
            )
        )
        self.assertTrue(
            nh_loop.subject_key_occurs_in(
                "recent.space.direct.door",
                "whether each recent space has its own direct door",
            )
        )
        self.assertTrue(
            nh_loop.subject_key_occurs_in(
                "stable.home.center",
                "Whether the world has a stable home or center depends on Ness's mood.",
            )
        )
        self.assertFalse(
            nh_loop.subject_key_occurs_in(
                "stable.home.center", "a stable home near a temporary control center"
            )
        )

    def test_subject_key_match_ignores_harmless_case_and_separator_changes(self):
        self.assertTrue(
            nh_loop.subject_key_occurs_in(
                "Emergency.Record", "Emergency Record records the active phone call."
            )
        )
        self.assertTrue(
            nh_loop.subject_key_occurs_in(
                "Sending.the.whole.call", "Sending the whole call"
            )
        )
        self.assertTrue(
            nh_loop.subject_key_occurs_in("Choose.parts", "Choose parts")
        )
        self.assertFalse(nh_loop.is_discriminating_subject_key("ness.speaks"))

    def test_subject_key_match_treats_nh_and_n_dot_h_as_the_same_name(self):
        self.assertTrue(
            nh_loop.subject_key_occurs_in(
                "what.is.sent.into.nh", "what is sent into N.H;"
            )
        )
        self.assertFalse(
            nh_loop.subject_key_occurs_in(
                "what.is.sent.into.nh", "what is sent into another system;"
            )
        )

    def test_question_validation_uses_bounded_durable_checkpoint_pages(self):
        """The page is bounded and the bound is enforced, whatever its size.

        The size itself is a throughput choice (24 was measured live), so this
        rehearsal pins the PROPERTY that matters -- a page is capped, balanced,
        and an inventory too big for its declared pages is refused outright --
        against whatever the constant currently is, not against one number.
        """
        per_page = nh_loop.QUESTION_VALIDATION_CHECKPOINT_ISSUES_PER_PAGE
        self.assertEqual(24, per_page)
        contract = nh_loop.question_validation_page_issue_contract(1, 3, 36, 0)
        self.assertEqual(
            {
                "issues_remaining": 36,
                "pages_remaining": 3,
                "maximum": per_page,
                "required": 12,
            },
            contract,
        )
        # More issues than the declared pages could ever carry: refused, not
        # silently overfilled onto the last page.
        self.assertIsNone(
            nh_loop.question_validation_page_issue_contract(
                1, 2, 2 * per_page + 1, 0
            )
        )

    def test_question_validation_compacts_bundle_baseline_to_selected_package(self):
        baseline = {
            "baseline_identity": "baseline-1",
            "package_inventory": [
                {"package_id": "A19", "feature_inventory": ["wanted"]},
                {"package_id": "A20", "feature_inventory": ["unrelated"]},
            ],
            "cross_package_relationships": [
                {"affected_package_ids": ["A19", "A20"], "summary": "keep"},
                {"affected_package_ids": ["A20", "A21"], "summary": "drop"},
            ],
            "source_manifest_sha256": "manifest-1",
        }

        compact = nh_loop.question_validation_bundle_seven_context(
            baseline, "A19"
        )

        self.assertEqual(
            [{"package_id": "A19", "feature_inventory": ["wanted"]}],
            compact["selected_package_inventory"],
        )
        self.assertEqual(
            [
                {
                    "affected_package_ids": ["A19", "A20"],
                    "summary": "keep",
                }
            ],
            compact["relationships_affecting_selected_package"],
        )
        self.assertEqual(
            500_000, nh_loop.QUESTION_VALIDATION_PROVIDER_PROMPT_MAX_CHARS
        )

    def test_question_validation_continuation_restarts_only_the_current_page(self):
        contract = nh_loop.question_validation_page_issue_contract(3, 4, 36, 18)
        self.assertEqual(18, contract["issues_remaining"])
        self.assertEqual(2, contract["pages_remaining"])
        self.assertEqual(9, contract["required"])
        # Never the whole remainder: one issue is held back so the declared
        # final page cannot be left empty.
        self.assertEqual(17, contract["maximum"])

    def test_long_codex_review_checkpoint_is_outside_the_reviewed_repository(self):
        spec = nh_loop.codex_review_checkpoint_spec(
            "question-validation", "read every source", "a" * 64
        )

        self.assertEqual(
            Path(nh_loop.NH_REPO_PATH).parent,
            Path(spec["path"]).parent.parent,
        )
        self.assertFalse(
            os.path.commonpath((nh_loop.NH_REPO_PATH, spec["path"]))
            == nh_loop.NH_REPO_PATH
        )

    def test_long_codex_review_checkpoint_resumes_only_the_exact_request(self):
        with tempfile.TemporaryDirectory() as directory, mock.patch.object(
            nh_loop, "CODEX_REVIEW_CHECKPOINT_ROOT", directory
        ):
            spec = nh_loop.codex_review_checkpoint_spec(
                "question-validation", "read every source", "a" * 64
            )
            errors = []
            thread_id = "019c1234-5678-7abc-9def-0123456789ab"

            self.assertTrue(
                nh_loop.write_codex_review_checkpoint(spec, thread_id, errors)
            )
            self.assertEqual(
                thread_id,
                nh_loop.read_codex_review_checkpoint(spec)["thread_id"],
            )
            changed = nh_loop.codex_review_checkpoint_spec(
                "question-validation", "read every changed source", "a" * 64
            )
            self.assertIsNone(nh_loop.read_codex_review_checkpoint(changed))
            self.assertEqual([], errors)

    def test_thread_started_checkpoint_accepts_only_an_exact_uuid_event(self):
        thread_id = "019c1234-5678-7abc-9def-0123456789ab"
        line = json.dumps(
            {"type": "thread.started", "thread_id": thread_id}
        ).encode("utf-8")

        self.assertEqual(thread_id, nh_loop.codex_thread_started_from_line(line))
        self.assertIsNone(
            nh_loop.codex_thread_started_from_line(
                b'{"type":"item.completed","thread_id":"not-a-thread"}'
            )
        )

    def test_coverage_review_rechecks_technical_labels_against_diamond_rule(self):
        prompt = nh_loop.COVERAGE_REVIEW_PROMPT_HEAD

        self.assertIn("Apply the DIAMOND RULE throughout this challenge", prompt)
        self.assertIn("a relationship Ness experiences across features or surfaces", prompt)
        self.assertIn("mechanics decide HOW to implement that settled behaviour", prompt)

    def test_next_package_navigation_uses_diamond_rule_before_mechanical_route(self):
        prompt = nh_loop.NEXT_PACKAGE_PROMPT

        self.assertIn("NESS DECISION BOUNDARY -- THE DIAMOND RULE", prompt)

    def test_bundle_eight_keeps_parallel_build_plan_draft_until_walkthrough(self):
        prompt = nh_loop.NEXT_PACKAGE_PROMPT

        self.assertIn(
            "BUNDLE 8 REVIEW, WALKTHROUGH AND PROVISIONAL BUILD-PLANNING ORDER",
            prompt,
        )
        self.assertIn("every feature, every bundle and every relationship", prompt)
        self.assertIn("remains a draft only", prompt)
        self.assertIn("whole system first and then feature by feature", prompt)

    def test_bundle_eight_build_plan_requires_verified_full_system_restore(self):
        prompt = nh_loop.NEXT_PACKAGE_PROMPT

        self.assertIn("post-build recovery deliverable", prompt)
        self.assertIn("complete working system, not source code alone", prompt)
        self.assertIn("Secrets remain separate and protected", prompt)
        self.assertIn("prove a clean restore", prompt)
        self.assertIn("route it to question-validation", prompt)


class NessAnswerBatchTests(unittest.TestCase):
    _composition = staticmethod(NessOwnWordsAnswerTests._composition)

    @classmethod
    def _event_1545_state(cls):
        return NessOwnWordsAnswerTests._event_1545_state()

    @staticmethod
    def _answer(question_id, generation, text):
        return {
            "question_id": question_id,
            "form_generation": generation,
            "answer_text": text,
            "answer_choice": None,
            "supersede_settled": False,
        }

    def test_batch_event_schema_exists_only_at_version_twelve(self):
        self.assertIsNone(
            nh_loop.interview_body_keys_for(11, "answer_batch_recorded")
        )
        self.assertEqual(
            nh_loop.INTERVIEW_VERSION12_CONTROLLER_EVENT_BODY_KEYS[
                "answer_batch_recorded"
            ],
            nh_loop.interview_body_keys_for(12, "answer_batch_recorded"),
        )

    def test_question_phase_reset_is_append_only_and_clears_current_questions(self):
        with copied_interview_at(2589) as (
            _state_dir,
            journal,
            events,
        ):
            before_errors = []
            before = nh_loop.replay_interview_state(events, before_errors)
            stdin = io.TextIOWrapper(
                io.BytesIO(
                    json.dumps(
                        {"confirm_reset_all_questions_and_answers": True}
                    ).encode("utf-8")
                )
            )
            with mock.patch.object(sys, "stdin", stdin), contextlib.redirect_stdout(
                io.StringIO()
            ):
                code = nh_loop.command_reset_question_phase()
            written = [
                json.loads(line)
                for line in journal.read_text(encoding="utf-8").splitlines()
                if line.strip()
            ]
            after_errors = []
            after = nh_loop.replay_interview_state(written, after_errors)

        self.assertEqual([], before_errors)
        self.assertTrue(before["questions"])
        self.assertEqual(nh_loop.EXIT_OK, code)
        self.assertEqual(len(events) + 1, len(written))
        self.assertEqual("question_phase_reset_recorded", written[-1]["type"])
        self.assertEqual([], after_errors)
        self.assertEqual({}, after["questions"])
        self.assertEqual([], after["answers"])
        self.assertEqual([], after["groups_presented"])
        self.assertEqual({}, after["routed_issues"])
        self.assertEqual({}, after["validation_sets"])
        self.assertEqual([], after["bundle_seven_baselines"])
        self.assertEqual([], after["bundle_seven_question_merges"])
        self.assertEqual(before["candidate_custody"], after["candidate_custody"])
        self.assertEqual(
            written[-1]["event_seq"],
            after["latest_question_phase_reset"]["event_seq"],
        )

    def test_question_phase_reset_schema_exists_only_at_version_twelve(self):
        self.assertIsNone(
            nh_loop.interview_body_keys_for(11, "question_phase_reset_recorded")
        )
        self.assertEqual(
            nh_loop.INTERVIEW_VERSION12_CONTROLLER_EVENT_BODY_KEYS[
                "question_phase_reset_recorded"
            ],
            nh_loop.interview_body_keys_for(12, "question_phase_reset_recorded"),
        )

    @staticmethod
    def _answers_for_group(events):
        errors = []
        state = nh_loop.replay_interview_state(events, errors)
        if errors:
            raise AssertionError(errors)
        group = state["open_group"]
        return [
            NessAnswerBatchTests._answer(
                question_id,
                group["form_generations"][question_id],
                "My exact answer for %s." % question_id,
            )
            for question_id in group["question_ids"]
        ]

    def test_complete_batch_is_one_durable_replayable_event(self):
        with pinned_checkout(1544), copied_interview_at(1544) as (
            _state_dir,
            journal,
            events,
        ):
            answers = self._answers_for_group(events)
            stdin = io.TextIOWrapper(
                io.BytesIO(json.dumps({"answers": answers}).encode("utf-8"))
            )
            with mock.patch.object(
                nh_loop, "NESS_OPEN_ANSWER_FORM_FIRST_EVENT_SEQ", 1545
            ), mock.patch.object(sys, "stdin", stdin), contextlib.redirect_stdout(
                io.StringIO()
            ):
                code = nh_loop.command_record_ness_answer_batch()
                written = [
                    json.loads(line)
                    for line in journal.read_text(encoding="utf-8").splitlines()
                    if line.strip()
                ]
                replay_errors = []
                replayed = nh_loop.replay_interview_state(written, replay_errors)

        self.assertEqual(nh_loop.EXIT_OK, code)
        self.assertEqual(len(events) + 1, len(written))
        self.assertEqual("answer_batch_recorded", written[-1]["type"])
        self.assertEqual(len(answers), written[-1]["answer_count"])
        self.assertEqual([], replay_errors)
        self.assertIsNotNone(replayed)
        batch_seq = written[-1]["event_seq"]
        for answer in answers:
            history = replayed["questions"][answer["question_id"]]["answer_history"]
            self.assertEqual(batch_seq, history[-1]["event_seq"])
            self.assertEqual(answer["answer_text"], history[-1]["ness_answer_exact"]["text"])

    def test_mid_line_failure_restores_old_tail_and_records_no_answers(self):
        with pinned_checkout(1544), copied_interview_at(1544) as (
            _state_dir,
            journal,
            events,
        ):
            answers = self._answers_for_group(events)
            original = journal.read_bytes()
            real_write = os.write
            failed = {"value": False}

            def fail_during_batch_write(fd, data):
                if not failed["value"] and b'"type":"answer_batch_recorded"' in data:
                    failed["value"] = True
                    real_write(fd, data[: max(1, len(data) // 2)])
                    raise OSError("injected answer-batch write failure")
                return real_write(fd, data)

            stdin = io.TextIOWrapper(
                io.BytesIO(json.dumps({"answers": answers}).encode("utf-8"))
            )
            with mock.patch.object(
                nh_loop, "NESS_OPEN_ANSWER_FORM_FIRST_EVENT_SEQ", 1545
            ), mock.patch.object(sys, "stdin", stdin), mock.patch.object(
                nh_loop.os, "write", side_effect=fail_during_batch_write
            ), contextlib.redirect_stdout(io.StringIO()):
                code = nh_loop.command_record_ness_answer_batch()
            restored = journal.read_bytes()
            replay_errors = []
            replayed = nh_loop.replay_interview_state(events, replay_errors)

        self.assertTrue(failed["value"])
        self.assertNotEqual(nh_loop.EXIT_OK, code)
        self.assertEqual(original, restored)
        self.assertEqual([], replay_errors)
        for answer in answers:
            self.assertEqual(
                [], replayed["questions"][answer["question_id"]]["answer_history"]
            )

    def test_partial_group_batch_is_refused_before_any_answer_write(self):
        answer = self._answer(
            "q_1111111111111111", "g_1111111111111111", "Only one answer."
        )
        state = {
            "open_group": {
                "question_ids": ["q_1111111111111111", "q_2222222222222222"],
            },
            "questions": {
                "q_1111111111111111": {
                    "status": nh_loop.INTERVIEW_STATUS_AWAITING_ANSWER,
                    "last_presented_generation": "g_1111111111111111",
                },
                "q_2222222222222222": {
                    "status": nh_loop.INTERVIEW_STATUS_AWAITING_ANSWER,
                    "last_presented_generation": "g_2222222222222222",
                },
            },
        }
        with mock.patch.object(
            nh_loop, "read_stdin_envelope", return_value={"answers": [answer]}
        ), mock.patch.object(
            nh_loop, "load_interview_for_command", return_value=state
        ), mock.patch.object(nh_loop.subprocess, "run") as run, contextlib.redirect_stdout(
            io.StringIO()
        ):
            code = nh_loop.command_record_ness_answer_batch()

        self.assertNotEqual(nh_loop.EXIT_OK, code)
        run.assert_not_called()

    def test_bundle_seven_prompt_requires_every_package_and_asks_nothing(self):
        prompt = nh_loop.bundle_seven_prompt(["one.md", "two.md"])

        for package_id, _title, _kind in nh_loop.BUNDLE_SEVEN_EXPECTED_PACKAGES:
            self.assertIn(package_id, prompt)
        self.assertIn("Do not ask Ness questions", prompt)
        self.assertIn("all Bundle Seven policy and mechanical packages together", prompt)
        self.assertIn("Apply the NESS DIAMOND RULE", prompt)
        self.assertIn("every relationship from Bundle Seven to Bundles 1-6 and 8", prompt)
        self.assertIn("Ness decides WHAT the system does", prompt)
        self.assertIn("character-for-character against the Required source paths list", prompt)
        self.assertIn("never cite a path outside that list", prompt)
        self.assertIn("Open and read the COMPLETE contents", prompt)
        self.assertIn("Never infer supersession from version order", prompt)
        self.assertIn(
            "excluded acceptance, closure, receipt, status, and work-process records",
            prompt,
        )
        self.assertIn("Byte-identical copies are one logical content identity", prompt)
        self.assertIn("do not block unrelated features", prompt)
        self.assertIn("question-validation stage can ask Ness", prompt)

    def test_music_system_is_the_last_bundle_seven_package_with_its_intake_root(self):
        self.assertEqual(
            "MUSIC_SYSTEM", nh_loop.BUNDLE_SEVEN_EXPECTED_PACKAGES[-1][0]
        )
        self.assertEqual(
            nh_loop.BUNDLE_SEVEN_DEFERRED_MUSIC_PATH,
            nh_loop.BUNDLE_SEVEN_EXPLICIT_SCOPE_ROOTS["MUSIC_SYSTEM"],
        )

    def test_bundle_seven_replay_accepts_original_and_current_package_inventories(self):
        current = [
            package_id
            for package_id, _title, _kind in nh_loop.BUNDLE_SEVEN_EXPECTED_PACKAGES
        ]
        legacy = list(nh_loop.BUNDLE_SEVEN_LEGACY_PACKAGE_IDS)

        self.assertTrue(
            nh_loop.bundle_seven_recorded_package_ids_are_supported(current)
        )
        self.assertTrue(
            nh_loop.bundle_seven_recorded_package_ids_are_supported(legacy)
        )
        self.assertFalse(
            nh_loop.bundle_seven_recorded_package_ids_are_supported(current[:-2])
        )
        self.assertFalse(
            nh_loop.bundle_seven_recorded_package_ids_are_supported(
                legacy[:-1] + [legacy[0]]
            )
        )

    def test_bundle_seven_feature_discovery_excludes_proof_and_non_feature_sources(self):
        paths = {
            "README.md": b"repository label",
            "01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md": b"master",
            "01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_3.md": b"current decisions",
            "01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md": b"old decisions",
            "01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md": b"archive",
            "01_AUTHORITATIVE/cursorrules": b"work safety rules",
            "06_OPERATIONAL_INSTRUCTIONS/NH_CLAUDE_PROJECT_INSTRUCTIONS_v1_2_CANDIDATE.md": b"Claude instructions",
            "04_ACCEPTED_STANDALONE_DESIGNS/NH_FEATURE.md": b"feature body",
            "05_ACTIVE_CANDIDATE/NH_CANDIDATE.md": b"candidate body",
            "04_ACCEPTED_STANDALONE_DESIGNS/NH_ACCEPTANCE_RECORD.md": b"proof",
            "04_ACCEPTED_STANDALONE_DESIGNS/NH_CLOSURE_RECORD.md": b"proof",
            "04_ACCEPTED_STANDALONE_DESIGNS/NH_RECEIPT.md": b"proof",
            nh_loop.BUNDLE_SEVEN_WORKFLOW_PATH: b"workflow body",
            nh_loop.BUNDLE_SEVEN_DEFERRED_MUSIC_PATH: b"later work",
        }
        index = {
            "by_path": paths,
            "category_of": {
                path: nh_loop.classify_repo_source_path(path) for path in paths
            },
        }

        selected = nh_loop.bundle_seven_feature_discovery_paths(index)

        self.assertIn(
            "04_ACCEPTED_STANDALONE_DESIGNS/NH_FEATURE.md", selected
        )
        self.assertIn(
            "05_ACTIVE_CANDIDATE/NH_CANDIDATE.md", selected
        )
        self.assertIn(
            "01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md", selected
        )
        self.assertIn(
            "01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_3.md", selected
        )
        self.assertIn(nh_loop.BUNDLE_SEVEN_WORKFLOW_PATH, selected)
        for excluded in (
            "README.md",
            "01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md",
            "01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md",
            "01_AUTHORITATIVE/cursorrules",
            "06_OPERATIONAL_INSTRUCTIONS/NH_CLAUDE_PROJECT_INSTRUCTIONS_v1_2_CANDIDATE.md",
        ):
            self.assertNotIn(excluded, selected)
        self.assertNotIn(
            "04_ACCEPTED_STANDALONE_DESIGNS/NH_ACCEPTANCE_RECORD.md", selected
        )
        self.assertNotIn(
            "04_ACCEPTED_STANDALONE_DESIGNS/NH_CLOSURE_RECORD.md", selected
        )
        self.assertNotIn(
            "04_ACCEPTED_STANDALONE_DESIGNS/NH_RECEIPT.md", selected
        )
        self.assertIn(nh_loop.BUNDLE_SEVEN_DEFERRED_MUSIC_PATH, selected)

    def test_bundle_seven_source_binding_keeps_music_intake_currentness(self):
        music_entry = "?? %s" % nh_loop.BUNDLE_SEVEN_DEFERRED_MUSIC_PATH
        binding = {
            "branch": "main",
            "head_sha": "h" * 40,
            "worktree_entries": [music_entry],
            "binding_sha256": "b" * 64,
            "clean": False,
        }

        self.assertIs(binding, nh_loop.bundle_seven_source_binding(binding))

    def test_bundle_seven_feature_discovery_excludes_proved_non_feature_work_records(self):
        feature = "05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_A19.md"
        paths = {feature: b"feature body"}
        paths.update(
            {
                path: b"full work-record body"
                for path in nh_loop.BUNDLE_SEVEN_NON_FEATURE_WORK_RECORD_PATHS
            }
        )
        index = {
            "by_path": paths,
            "category_of": {
                path: nh_loop.classify_repo_source_path(path) for path in paths
            },
        }

        selected = nh_loop.bundle_seven_feature_discovery_paths(index)

        self.assertEqual([feature], selected)

    def test_moved_non_feature_work_record_stays_out_of_feature_discovery(self):
        old = next(
            path
            for path in nh_loop.BUNDLE_SEVEN_NON_FEATURE_WORK_RECORD_PATHS
            if "POST_ACCEPTANCE_CONTINUATION" in path
            and "v1_9_CANDIDATE" in path
        )
        moved = "04_ACCEPTED_STANDALONE_DESIGNS/" + old.rsplit("/", 1)[-1]
        feature = "05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_A19.md"
        index = {
            "by_path": {moved: b"loop work record", feature: b"feature body"},
            "category_of": {
                moved: nh_loop.classify_repo_source_path(moved),
                feature: nh_loop.classify_repo_source_path(feature),
            },
        }

        self.assertEqual(
            [feature], nh_loop.bundle_seven_feature_discovery_paths(index)
        )

    def test_old_active_path_resolves_to_one_exact_moved_accepted_name(self):
        leaf = "NH_FEATURE_v1_0_CANDIDATE.md"
        moved = "04_ACCEPTED_STANDALONE_DESIGNS/" + leaf
        index = {
            "by_path": {moved: b"current bytes"},
            "by_basename": {leaf: {moved}},
            "by_stem": {},
            "category_of": {moved: "accepted_package"},
            "top_level": {"04_ACCEPTED_STANDALONE_DESIGNS", "05_ACTIVE_CANDIDATE"},
        }

        self.assertEqual(
            ({moved}, "resolved"),
            nh_loop.resolve_repository_reference(
                index, "05_ACTIVE_CANDIDATE/" + leaf
            ),
        )

    def test_only_exact_embedded_historical_identity_stops_blocking(self):
        missing = "05_ACTIVE_CANDIDATE/NH_OLD_v1_0_CANDIDATE.md"
        source = "04_ACCEPTED_STANDALONE_DESIGNS/NH_CURRENT.md"
        digest = b"a" * 64
        proved = {
            "by_path": {
                source: (
                    b"Historical predecessor `"
                    + missing.encode("utf-8")
                    + b"` preserved with SHA-256 `"
                    + digest
                    + b"`."
                )
            }
        }
        naked = {"by_path": {source: missing.encode("utf-8")}}

        self.assertFalse(
            nh_loop.closure_reference_is_material("A19", proved, source, missing)
        )
        self.assertTrue(
            nh_loop.closure_reference_is_material("A19", naked, source, missing)
        )

    def test_bundle_seven_feature_discovery_keeps_live_dual_model_handoff_feature(self):
        handoff = (
            "05_ACTIVE_CANDIDATE/"
            "NH_DECISION_PACKAGE_LIVE_DUAL_MODEL_HANDOFF_v1.md"
        )
        index = {
            "by_path": {handoff: b"full N.H feature body"},
            "category_of": {
                handoff: nh_loop.classify_repo_source_path(handoff),
            },
        }

        self.assertEqual(
            [handoff], nh_loop.bundle_seven_feature_discovery_paths(index)
        )

    def test_question_validation_prompt_block_names_each_selected_package(self):
        def requirement(package_id):
            return {
                "precall_basis": nh_loop.PRECALL_BASIS_BUNDLE_SEVEN_SELECTION,
                "package_key": package_id,
                "package_id": package_id,
                "package_scope_id": package_id,
                "scope_root_path": "05_ACTIVE_CANDIDATE/%s.md" % package_id,
            }

        a17 = nh_loop.controller_selected_package_prompt_block(requirement("A17"))
        a20 = nh_loop.controller_selected_package_prompt_block(requirement("A20"))

        self.assertEqual("A17", a17["package_id"])
        self.assertEqual("A17", a17["package_scope_id"])
        self.assertEqual("A20", a20["package_id"])
        self.assertEqual("A20", a20["package_scope_id"])
        self.assertNotEqual(a17, a20)

    @staticmethod
    def _bundle_seven_payload(paths):
        packages = []
        package_ids = [item[0] for item in nh_loop.BUNDLE_SEVEN_EXPECTED_PACKAGES]
        for package_id, title, kind in nh_loop.BUNDLE_SEVEN_EXPECTED_PACKAGES:
            primary_kind = nh_loop.BUNDLE_SEVEN_DIMENSION_KINDS[0]
            feature_inventory = [
                {
                    "feature_key": "%s.primary.feature" % package_id.lower(),
                    "feature_name": "Primary feature",
                    "feature_summary": "The feature is independently accounted for.",
                    "source_paths": [paths[0]],
                    "decision_dimensions": [
                        {
                            "dimension_key": "%s.%s" % (package_id.lower(), primary_kind),
                            "dimension_kind": primary_kind,
                            "status": "partial",
                            "summary": "One aspect is settled and one remains open.",
                            "decided_aspects": ["Existing decisions are preserved."],
                            "open_aspects": ["Only unresolved user-facing choices remain open."],
                            "source_paths": [paths[0]],
                        }
                    ],
                    "not_applicable_dimensions": [
                        {
                            "dimension_kind": dimension_kind,
                            "reason": "The cited source proves this dimension does not apply to this fixture feature.",
                            "source_paths": [paths[0]],
                        }
                        for dimension_kind in nh_loop.BUNDLE_SEVEN_DIMENSION_KINDS[1:]
                    ],
                }
            ]
            packages.append(
                {
                    "package_id": package_id,
                    "package_title": title,
                    "work_kind": kind,
                    "current_state_summary": "Current source state is accounted for.",
                    "feature_inventory": feature_inventory,
                    "connected_package_ids": [value for value in package_ids if value != package_id][:2],
                    "source_paths": [paths[0]],
                }
            )
        return {
            "schema_version": nh_loop.BUNDLE_SEVEN_REVIEW_SCHEMA_VERSION,
            "bundle_id": nh_loop.BUNDLE_SEVEN_ID,
            "review_complete": True,
            "source_paths_checked": sorted(paths),
            "packages": packages,
            "cross_package_relationships": [
                {
                    "relationship_key": "world.voice.connection",
                    "affected_package_ids": ["A19", "B29"],
                    "summary": "The World interface and voice pipeline share one user-facing boundary.",
                    "status": "partial",
                    "source_paths": [paths[0]],
                }
            ],
            "unknowns": [],
        }

    def test_bundle_seven_payload_requires_complete_inventory(self):
        paths = ["one.md", "two.md"]
        payload = self._bundle_seven_payload(paths)
        errors = []
        accepted = nh_loop.validate_bundle_seven_payload(
            json.dumps(payload), paths, errors
        )
        self.assertIsNotNone(accepted)
        self.assertEqual([], errors)
        self.assertEqual(
            ["Existing decisions are preserved."],
            accepted["packages"][0]["already_decided"],
        )
        self.assertEqual(
            ["Only unresolved user-facing choices remain open."],
            accepted["packages"][0]["still_open"],
        )

        payload["packages"].pop()
        errors = []
        self.assertIsNone(
            nh_loop.validate_bundle_seven_payload(json.dumps(payload), paths, errors)
        )
        self.assertTrue(errors)

    def test_bundle_seven_complete_review_with_caveats_is_accepted_and_recorded(self):
        # Ness, 2026-09-03 ("yes accept caveats"): a COMPLETE review may list what it
        # could not verify; the list is kept, not refused.  Incomplete is still refused.
        paths = ["one.md", "two.md"]
        payload = self._bundle_seven_payload(paths)
        payload["unknowns"] = ["No acceptance record exists for A20.", "The A17 audit PASS is not evidenced."]
        errors = []
        accepted = nh_loop.validate_bundle_seven_payload(json.dumps(payload), paths, errors)
        self.assertEqual([], errors)
        self.assertEqual(accepted["unknowns"], payload["unknowns"])

        payload["review_complete"] = False
        errors = []
        self.assertIsNone(nh_loop.validate_bundle_seven_payload(json.dumps(payload), paths, errors))
        self.assertTrue(any("did not declare itself complete" in e for e in errors), errors)

    def test_bundle_seven_compact_transport_expands_to_durable_inventory(self):
        paths = ["one.md", "two.md"]
        payload = self._bundle_seven_payload(paths)
        payload.pop("source_paths_checked")
        for package in payload["packages"]:
            compact = []
            for feature in package["feature_inventory"]:
                compact.append(
                    {
                        "feature_key": feature["feature_key"],
                        "feature_name": feature["feature_name"],
                        "feature_summary": feature["feature_summary"],
                        "source_paths": feature["source_paths"],
                        "dimension_statuses": {
                            kind: ("partial" if index == 0 else "not_applicable")
                            for index, kind in enumerate(nh_loop.BUNDLE_SEVEN_DIMENSION_KINDS)
                        },
                        "decided_aspects": [
                            {
                                "dimension_kind": nh_loop.BUNDLE_SEVEN_DIMENSION_KINDS[0],
                                "text": "Existing decisions are preserved.",
                            }
                        ],
                        "open_aspects": [
                            {
                                "dimension_kind": nh_loop.BUNDLE_SEVEN_DIMENSION_KINDS[0],
                                "text": "Only unresolved user-facing choices remain open.",
                            }
                        ],
                        "mechanical_or_not_applicable_reasons": [
                            {
                                "dimension_kind": kind,
                                "reason": "The cited source proves this does not apply.",
                            }
                            for kind in nh_loop.BUNDLE_SEVEN_DIMENSION_KINDS[1:]
                        ],
                    }
                )
            package["feature_inventory"] = compact
        errors = []

        accepted = nh_loop.validate_bundle_seven_payload(
            json.dumps(payload), paths, errors
        )

        self.assertEqual([], errors)
        self.assertIsNotNone(accepted)
        self.assertEqual(sorted(paths), accepted["source_paths_checked"])
        self.assertEqual(
            ["Existing decisions are preserved."],
            accepted["packages"][0]["already_decided"],
        )
        self.assertEqual(
            ["Only unresolved user-facing choices remain open."],
            accepted["packages"][0]["still_open"],
        )

    def test_bundle_seven_compact_transport_refuses_missing_dimension(self):
        paths = ["one.md"]
        payload = self._bundle_seven_payload(paths)
        payload.pop("source_paths_checked")
        feature = payload["packages"][0]["feature_inventory"][0]
        payload["packages"][0]["feature_inventory"] = [
            {
                "feature_key": feature["feature_key"],
                "feature_name": feature["feature_name"],
                "feature_summary": feature["feature_summary"],
                "source_paths": feature["source_paths"],
                "dimension_statuses": {},
                "decided_aspects": [],
                "open_aspects": [],
                "mechanical_or_not_applicable_reasons": [],
            }
        ]
        errors = []

        self.assertIsNone(
            nh_loop.validate_bundle_seven_payload(json.dumps(payload), paths, errors)
        )
        self.assertTrue(any("dimension-status inventory" in item for item in errors))

    def test_bundle_seven_question_plan_contains_every_package_and_feature(self):
        paths = ["one.md", "two.md"]
        payload = self._bundle_seven_payload(paths)
        baseline = {
            "baseline_identity": "b" * 64,
            "package_inventory": payload["packages"],
        }
        errors = []

        plan = nh_loop.bundle_seven_question_validation_plan(baseline, errors)

        self.assertEqual([], errors)
        self.assertEqual(11, plan["package_count"])
        self.assertEqual(
            [item[0] for item in nh_loop.BUNDLE_SEVEN_EXPECTED_PACKAGES],
            [item["package_id"] for item in plan["packages"]],
        )
        self.assertEqual(
            sum(len(package["feature_inventory"]) for package in payload["packages"]),
            plan["feature_count"],
        )

    def test_bundle_seven_question_plan_refuses_a19_only_inventory(self):
        payload = self._bundle_seven_payload(["one.md", "two.md"])
        errors = []

        plan = nh_loop.bundle_seven_question_validation_plan(
            {"package_inventory": [payload["packages"][1]]}, errors
        )

        self.assertIsNone(plan)
        self.assertTrue(any("exactly all eleven package ids" in item for item in errors))

    def test_bundle_seven_question_results_merge_the_packages_that_finished(self):
        payload = self._bundle_seven_payload(["one.md", "two.md"])
        plan = nh_loop.bundle_seven_question_validation_plan(
            {
                "baseline_identity": "b" * 64,
                "package_inventory": payload["packages"],
            },
            [],
        )
        results = [
            {
                "package_id": item["package_id"],
                "baseline_identity": plan["baseline_identity"],
                "enumeration_complete": True,
                "feature_keys_checked": item["feature_keys"],
                "questions": [
                    {"question_id": "q_%s" % item["package_id"].lower().replace("-", "_")}
                ],
            }
            for item in plan["packages"]
        ]
        errors = []

        merged = nh_loop.merge_bundle_seven_question_validation_results(
            plan, results, errors
        )

        self.assertEqual([], errors)
        self.assertEqual(len(plan["packages"]), merged["package_count"])
        self.assertEqual(len(plan["packages"]), len(merged["questions"]))

        # Ness, 2026-09-03 (section 2): nine of ten MERGE, and the record names the
        # nine; the tenth rejoins a later merge.  Zero packages is still refused.
        errors = []
        partial = nh_loop.merge_bundle_seven_question_validation_results(
            plan, results[:-1], errors
        )
        self.assertEqual([], errors)
        self.assertEqual(len(plan["packages"]) - 1, partial["package_count"])
        self.assertEqual(len(plan["packages"]) - 1, len(partial["questions"]))
        self.assertNotIn(plan["packages"][-1]["package_id"], partial["package_ids"])

        errors = []
        self.assertIsNone(
            nh_loop.merge_bundle_seven_question_validation_results(plan, [], errors)
        )
        self.assertTrue(any("no package" in item for item in errors))

    def test_bundle_seven_selection_is_bound_to_the_saved_ten_package_baseline(self):
        payload = self._bundle_seven_payload(
            [nh_loop.BUNDLE_SEVEN_WORKFLOW_PATH, "two.md"]
        )
        baseline = {
            "baseline_identity": "b" * 64,
            "package_inventory": payload["packages"],
        }
        errors = []

        selection = nh_loop.bundle_seven_question_validation_selection(
            baseline, "A17", errors
        )

        self.assertEqual([], errors)
        self.assertEqual("A17", selection["package_id"])
        self.assertEqual("A17", selection["package_scope_id"])
        self.assertEqual("b" * 64, selection["bundle_seven_baseline_identity"])

    def test_bundle_seven_selection_takes_precedence_over_old_a19_route(self):
        payload = self._bundle_seven_payload(
            [nh_loop.BUNDLE_SEVEN_WORKFLOW_PATH, "two.md"]
        )
        baseline = {
            "baseline_identity": "b" * 64,
            "package_inventory": payload["packages"],
        }
        selection = nh_loop.bundle_seven_question_validation_selection(
            baseline, "A17", []
        )
        state = {
            "latest_bundle_seven_baseline": baseline,
            "routed_issues": {
                "old_a19": {
                    "package_scope_id": "A19",
                    "package_id": "A19",
                    "package_key": "A19",
                    "status": "awaiting_question_validation",
                }
            },
        }
        errors = []

        held = nh_loop.controller_held_question_validation_package(
            state, errors, continuation_selection=selection
        )

        self.assertEqual([], errors)
        self.assertEqual("A17", held["package_id"])
        self.assertEqual(
            nh_loop.PRECALL_BASIS_BUNDLE_SEVEN_SELECTION,
            held["precall_basis"],
        )

    def test_b30_selection_uses_explicit_delegating_policy_root(self):
        root = nh_loop.BUNDLE_SEVEN_EXPLICIT_SCOPE_ROOTS["B30"]
        payload = self._bundle_seven_payload([root, "01_AUTHORITATIVE/AAA.md"])
        baseline = {
            "baseline_identity": "b" * 64,
            "package_inventory": payload["packages"],
        }
        errors = []

        selection = nh_loop.bundle_seven_question_validation_selection(
            baseline, "B30", errors
        )

        self.assertEqual([], errors)
        self.assertEqual(root, selection["scope_root_path"])

    def test_a19_selection_prefers_its_package_record_over_shared_workflow(self):
        root = (
            "05_ACTIVE_CANDIDATE/"
            "NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_"
            "WONDER_RUNTIME_v1.md"
        )
        payload = self._bundle_seven_payload(
            [nh_loop.BUNDLE_SEVEN_WORKFLOW_PATH, root]
        )
        next(
            item for item in payload["packages"] if item["package_id"] == "A19"
        )["source_paths"].append(root)
        baseline = {
            "baseline_identity": "b" * 64,
            "package_inventory": payload["packages"],
        }
        errors = []

        selection = nh_loop.bundle_seven_question_validation_selection(
            baseline, "A19", errors
        )

        self.assertEqual([], errors)
        self.assertEqual(root, selection["scope_root_path"])

    def test_selection_refuses_ambiguous_filename_fallback(self):
        payload = self._bundle_seven_payload(["one.md", "two.md"])
        baseline = {
            "baseline_identity": "b" * 64,
            "package_inventory": payload["packages"],
        }
        errors = []

        selection = nh_loop.bundle_seven_question_validation_selection(
            baseline, "A17", errors
        )

        self.assertIsNone(selection)
        self.assertTrue(any("refusing to choose" in item for item in errors))

    def test_bundle_seven_payload_refuses_feature_with_unaccounted_dimension(self):
        paths = ["one.md", "two.md"]
        payload = self._bundle_seven_payload(paths)
        payload["packages"][0]["feature_inventory"][0][
            "not_applicable_dimensions"
        ].pop()
        errors = []

        self.assertIsNone(
            nh_loop.validate_bundle_seven_payload(json.dumps(payload), paths, errors)
        )
        self.assertTrue(
            any("every decision dimension exactly once" in error for error in errors)
        )

    def test_bundle_seven_payload_refuses_partial_feature_marked_settled(self):
        paths = ["one.md", "two.md"]
        payload = self._bundle_seven_payload(paths)
        payload["packages"][0]["feature_inventory"][0]["decision_dimensions"][0][
            "status"
        ] = "settled"
        errors = []

        self.assertIsNone(
            nh_loop.validate_bundle_seven_payload(json.dumps(payload), paths, errors)
        )
        self.assertTrue(
            any("not fully settled" in error for error in errors)
        )

    def test_bundle_seven_payload_accepts_relationships_to_other_bundles(self):
        paths = ["one.md", "two.md"]
        payload = self._bundle_seven_payload(paths)
        payload["packages"][0]["connected_package_ids"].append("BUNDLE_5")
        payload["cross_package_relationships"].append(
            {
                "relationship_key": "world.privacy.bundle5",
                "affected_package_ids": ["A19", "BUNDLE_5"],
                "summary": "The Bundle Seven world experience uses Bundle Five privacy authority.",
                "status": "settled",
                "source_paths": [paths[0]],
            }
        )
        errors = []

        accepted = nh_loop.validate_bundle_seven_payload(
            json.dumps(payload), paths, errors
        )

        self.assertIsNotNone(accepted)
        self.assertEqual([], errors)

    def test_bundle_seven_relationship_cannot_omit_bundle_seven_target(self):
        paths = ["one.md", "two.md"]
        payload = self._bundle_seven_payload(paths)
        payload["cross_package_relationships"][0]["affected_package_ids"] = [
            "BUNDLE_5",
            "BUNDLE_8",
        ]
        errors = []

        accepted = nh_loop.validate_bundle_seven_payload(
            json.dumps(payload), paths, errors
        )

        self.assertIsNone(accepted)
        self.assertTrue(errors)

    def test_bundle_seven_event_schema_exists_only_at_current_version(self):
        kind = schema.BUNDLE_SEVEN_BASELINE_EVENT_TYPE
        self.assertIsNone(nh_loop.interview_body_keys_for(10, kind))
        self.assertEqual(
            schema.BUNDLE_SEVEN_BASELINE_BODY_KEYS,
            nh_loop.interview_body_keys_for(11, kind),
        )

    def test_bundle_seven_question_merge_has_a_separate_current_schema(self):
        kind = schema.BUNDLE_SEVEN_QUESTION_MERGE_EVENT_TYPE
        self.assertIsNone(nh_loop.interview_body_keys_for(10, kind))
        self.assertEqual(
            schema.BUNDLE_SEVEN_QUESTION_MERGE_BODY_KEYS,
            nh_loop.interview_body_keys_for(11, kind),
        )
        self.assertIn("package_validation_set_ids", schema.BUNDLE_SEVEN_QUESTION_MERGE_BODY_KEYS)
        self.assertIn("package_feature_keys_checked", schema.BUNDLE_SEVEN_QUESTION_MERGE_BODY_KEYS)

    def test_ness_question_form_keeps_settled_source_out_of_the_question(self):
        composition = {
            "v": "nh-ness-question-composition-v4",
            "question_id": "q_test",
            "topic_name": "how you stay in control and correct it",
            "question_sentence": "How should the remaining open part work?",
            "effect_sentences": ["what N.H actually does here"],
            "subject_quote": "a subject long enough to be a proved source quote",
            "subject_quote_path": "subject.md",
            "settled_basis_quote": "a settled rule long enough to be a proved quote",
            "settled_basis_quote_path": "settled.md",
            "checked_source": {
                "paths_checked": 2,
                "branch": "nh-design-loop",
                "head_sha_short": "0123456789ab",
            },
            "options": self._composition()["options"],
        }
        lines = nh_loop.build_ness_question_form(composition, 1, 1)

        rendered = "\n".join(lines)
        self.assertIn("SETTLED BOUNDARY:", rendered)
        self.assertIn("context, not a choice", rendered)
        self.assertIn("Do not ask Ness to decide it again", rendered)
        self.assertIn("ask only the remaining choice under YOUR CHOICE", rendered)

    def test_declared_option_behavior_is_unchanged(self):
        interpretation = nh_loop.interpret_ness_answer(
            self._composition(), "Use the automatic behavior.", None
        )

        self.assertEqual(
            nh_loop.INTERVIEW_INTERPRETATION_SELECTED,
            interpretation["status"],
        )
        self.assertEqual("yes", interpretation["selected_option_id"])

    @staticmethod
    def _batch_question(question_id, effective_answer=None):
        return {
            "question_id": question_id,
            "package_scope_id": "A19",
            "retired": False,
            "authority_reframe_required": False,
            "authority_reframe_currently_proved": False,
            "disposition": "ask_ness",
            "dependency_id": None,
            "_effective_answer": effective_answer,
        }

    @staticmethod
    def _own_words_entry(event_seq, question_id):
        return {
            "event_seq": event_seq,
            "question_id": question_id,
            "package_scope_id": "A19",
            "presented_group_event_seq": 1544,
            "controller_interpretation": {
                "status": nh_loop.INTERVIEW_INTERPRETATION_OWN_WORDS,
            },
        }

    def test_own_words_batch_does_not_revalidate_while_group_has_questions_left(self):
        answer = self._own_words_entry(1600, "q_one")
        questions = {
            "q_one": self._batch_question("q_one", answer),
            "q_two": self._batch_question("q_two"),
        }
        groups = {1544: {"question_ids": ["q_one", "q_two"]}}
        derived = {
            "settled_by_other": set(),
            "removed_by_other": set(),
            "satisfied_dependency_ids": set(),
        }

        self.assertEqual(
            [],
            nh_loop.own_words_batch_revalidation_claims(
                questions, groups, derived
            ),
        )

    def test_own_words_batch_requires_one_combined_check_when_group_is_complete(self):
        first = self._own_words_entry(1600, "q_one")
        second = self._own_words_entry(1601, "q_two")
        questions = {
            "q_one": self._batch_question("q_one", first),
            "q_two": self._batch_question("q_two", second),
        }
        groups = {1544: {"question_ids": ["q_one", "q_two"]}}
        derived = {
            "settled_by_other": set(),
            "removed_by_other": set(),
            "satisfied_dependency_ids": set(),
        }

        self.assertEqual(
            [
                {
                    "package_scope_id": "A19",
                    "after_seq": 1601,
                    "text": (
                        "Ness completed the presented own-words answer batch at "
                        "record 1601, so package \"A19\" now requires one "
                        "combined source/question validation before design or "
                        "another question group can proceed"
                    ),
                }
            ],
            nh_loop.own_words_batch_revalidation_claims(
                questions, groups, derived
            ),
        )

    def test_completed_group_waits_for_one_final_combined_check_while_questions_remain(self):
        answer = self._own_words_entry(1600, "q_one")
        questions = {
            "q_one": self._batch_question("q_one", answer),
            "q_later": self._batch_question("q_later"),
        }
        groups = {1544: {"question_ids": ["q_one"]}}
        derived = {
            "settled_by_other": set(),
            "removed_by_other": set(),
            "satisfied_dependency_ids": set(),
        }

        claims = nh_loop.own_words_batch_revalidation_claims(
            questions, groups, derived
        )

        self.assertEqual([], claims)

    @staticmethod
    def _delivery_clearance_state(answer_status=None):
        clearance = {
            "package_scope_id": "A19",
            "validation_set_id": "vs_a19",
            "validated_at_event_seq": 1698,
            "recorded_at_event_seq": 1735,
            "branch": "nh-design-loop",
            "head_sha": "1" * 40,
            "source_paths_checked": ["a19.md"],
            "coverage_manifest_sha256": "2" * 64,
        }
        events = [
            {
                "event_seq": 1735,
                "type": "question_coverage_review_recorded",
                "package_scope_id": "A19",
            },
            {
                "event_seq": 1736,
                "type": "supervisor_operation_completed",
                "package_scope_id": "A19",
                "operation_outcome": "ok",
                "supervisor_started_event_seq": 1734,
            },
            {
                "event_seq": 1737,
                "type": "group_presented",
                "package_scope_id": "A19",
            },
        ]
        if answer_status is not None:
            events.append(
                {
                    "event_seq": 1738,
                    "type": "answer_recorded",
                    "package_scope_id": "A19",
                    "superseded_settled": False,
                    "controller_interpretation": {"status": answer_status},
                    "mechanical_consequences": {
                        "derived": True,
                        "derived_by": "controller_from_explicit_ness_own_words",
                        "settles_question_ids": [],
                        "removes_question_ids": [],
                        "satisfies_dependency_ids": [],
                        "satisfies_dependency_keys": [],
                    },
                }
            )
        return {
            "coverage_clearances": {},
            "coverage_clearances_recorded": {"A19": clearance},
            "latest_complete_by_package": {
                "A19": {
                    "validation_set_id": "vs_a19",
                    "last_event_seq": 1698,
                }
            },
            "_events": events,
        }

    def test_own_words_answers_keep_prior_coverage_for_question_delivery_only(self):
        state = self._delivery_clearance_state(
            nh_loop.INTERVIEW_INTERPRETATION_OWN_WORDS
        )
        binding = {"branch": "nh-design-loop", "head_sha": "1" * 40}
        with mock.patch.object(
            nh_loop, "recompute_manifest_sha256", return_value="2" * 64
        ):
            self.assertEqual(
                set(), nh_loop.interview_coverage_cleared_scopes(state, binding, {})
            )
            self.assertEqual(
                {"A19"},
                nh_loop.interview_delivery_coverage_cleared_scopes(
                    state, binding, {}
                ),
            )

    def test_declared_option_answer_does_not_reuse_delivery_clearance(self):
        state = self._delivery_clearance_state(
            nh_loop.INTERVIEW_INTERPRETATION_SELECTED
        )
        binding = {"branch": "nh-design-loop", "head_sha": "1" * 40}
        with mock.patch.object(
            nh_loop, "recompute_manifest_sha256", return_value="2" * 64
        ):
            self.assertEqual(
                set(),
                nh_loop.interview_delivery_coverage_cleared_scopes(
                    state, binding, {}
                ),
            )

    def test_superseded_own_words_answer_keeps_delivery_clearance(self):
        state = self._delivery_clearance_state(
            nh_loop.INTERVIEW_INTERPRETATION_OWN_WORDS
        )
        state["_events"][-1]["superseded_settled"] = True
        binding = {"branch": "nh-design-loop", "head_sha": "1" * 40}
        with mock.patch.object(
            nh_loop, "recompute_manifest_sha256", return_value="2" * 64
        ):
            self.assertEqual(
                {"A19"},
                nh_loop.interview_delivery_coverage_cleared_scopes(
                    state, binding, {}
                ),
            )
            self.assertEqual(
                set(), nh_loop.interview_coverage_cleared_scopes(state, binding, {})
            )

    def test_routed_or_unknown_event_ends_delivery_clearance_exception(self):
        state = self._delivery_clearance_state(
            nh_loop.INTERVIEW_INTERPRETATION_OWN_WORDS
        )
        state["_events"].append(
            {
                "event_seq": 1739,
                "type": "routed_question_signal_recorded",
                "package_scope_id": "A19",
            }
        )
        binding = {"branch": "nh-design-loop", "head_sha": "1" * 40}
        with mock.patch.object(
            nh_loop, "recompute_manifest_sha256", return_value="2" * 64
        ):
            self.assertEqual(
                set(),
                nh_loop.interview_delivery_coverage_cleared_scopes(
                    state, binding, {}
                ),
            )

    def test_record_command_preserves_unmarked_own_words_without_provider_or_immediate_recheck(self):
        # frozen 2026-09-02 at journal event 1545: the answer boundary refuses a question whose validation set vs_8e109117 cannot be re-proved current against a moved checkout
        self.enterContext(pinned_checkout(1545))
        events, state = self._event_1545_state()
        question = state["questions"]["q_80423709fcd12ab5"]
        answer = "N.H should understand the situation, choose, and let me override it."
        envelope = {
            "question_id": question["question_id"],
            "form_generation": question["form_generation"],
            "answer_text": answer,
            "answer_choice": None,
            "supersede_settled": False,
        }

        with tempfile.TemporaryDirectory() as folder:
            key_path = ROOT / "nh_interview_state" / "nh_interview_authenticity.key"
            shutil.copy2(key_path, Path(folder) / key_path.name)
            journal_path = Path(folder) / "nh_interview_journal.jsonl"
            source_lines = (
                ROOT / "nh_interview_state" / "nh_interview_journal.jsonl"
            ).read_text(encoding="utf-8").splitlines(keepends=True)
            journal_path.write_text(
                "".join(
                    line
                    for line in source_lines
                    if line.strip() and json.loads(line).get("event_seq", 0) <= 1545
                ),
                encoding="utf-8",
            )
            journal_path.chmod(0o600)
            head = {
                "v": nh_loop.INTERVIEW_JOURNAL_HEAD_LABEL,
                "intent_generation": 1,
                "intent_number": 1,
                "intent_event_seq": events[-1]["event_seq"],
                "intent_event_sha256": events[-1]["event_sha256"],
                "committed_event_seq": events[-1]["event_seq"],
                "committed_event_sha256": events[-1]["event_sha256"],
            }
            head["head_auth_sha256"] = nh_loop.interview_journal_head_auth(
                key_path.read_bytes(), head
            )
            head_path = Path(folder) / "nh_interview_journal.head"
            head_path.write_text(
                json.dumps(head, sort_keys=True, separators=(",", ":")) + "\n",
                encoding="utf-8",
            )
            head_path.chmod(0o600)
            stdin = io.TextIOWrapper(io.BytesIO(json.dumps(envelope).encode("utf-8")))
            # This fixture truncates the real journal at 1545, so its synthetic
            # next event is 1546.  Move the migration boundary with the fixture
            # to exercise the new behavior without changing historical replay.
            with mock.patch.object(
                nh_loop, "NESS_OPEN_ANSWER_FORM_FIRST_EVENT_SEQ", 1546
            ):
                with mock.patch.dict(
                    os.environ, {nh_loop.INTERVIEW_STATE_DIR_ENV: folder}
                ), mock.patch.object(
                    sys, "stdin", stdin
                ), contextlib.redirect_stdout(io.StringIO()):
                    exit_code = nh_loop.command_record_ness_answer()
                written = [
                    json.loads(line)
                    for line in journal_path.read_text(encoding="utf-8").splitlines()
                    if line.strip()
                ]
                errors = []
                replayed = nh_loop.replay_interview_state(written, errors)

        self.assertEqual(nh_loop.EXIT_OK, exit_code)
        self.assertEqual([], errors)
        self.assertEqual("answer_recorded", written[-1]["type"])
        self.assertEqual(answer, written[-1]["ness_answer_exact"]["text"])
        self.assertEqual(
            nh_loop.INTERVIEW_INTERPRETATION_OWN_WORDS,
            written[-1]["controller_interpretation"]["status"],
        )
        self.assertNotIn("A19", replayed["revalidation_packages"])
        self.assertIsNone(replayed["open_group"])
        self.assertEqual(
            15,
            sum(
                question["status"] == nh_loop.INTERVIEW_STATUS_ELIGIBLE
                for question in replayed["questions"].values()
            ),
        )
        provider_types = {
            "provider_request_prepared",
            "provider_dispatch_begun",
            "provider_result_custody_recorded",
            "provider_request_terminal_recorded",
        }
        self.assertEqual(
            sum(event["type"] in provider_types for event in events),
            sum(event["type"] in provider_types for event in written),
        )


class ClarificationRevalidationScopeTests(unittest.TestCase):
    @staticmethod
    def _stale_state(questions):
        return {
            "questions": questions,
            "latest_complete_by_package": {
                "A19": {"validation_set_id": "vs_a19"},
                "A20": {"validation_set_id": "vs_a20"},
                "nullpkg_old_a": {"validation_set_id": "vs_old_a"},
                "nullpkg_old_b": {"validation_set_id": "vs_old_b"},
            },
            "revalidation_packages": frozenset(),
            "routed_issues": {},
            "validation_sets": {},
        }

    def test_current_clarification_selects_its_scope_over_unrelated_stale_scopes(self):
        state = self._stale_state(
            {
                "q_current": {
                    "question_id": "q_current",
                    "package_scope_id": "A19",
                    "status": nh_loop.INTERVIEW_STATUS_CLARIFICATION,
                    "answer_history": [{"event_seq": 1546}],
                }
            }
        )
        identity = {
            "package_scope_id": "A19",
            "scope_root_path": "05_ACTIVE_CANDIDATE/a19.md",
            "candidate_chain": [],
        }
        errors = []
        with mock.patch.object(
            nh_loop,
            "interview_unusable_validation_set_ids",
            return_value={"vs_old_a", "vs_old_b"},
        ), mock.patch.object(
            nh_loop,
            "build_authenticated_package_identity",
            return_value=identity,
        ) as build:
            selected = nh_loop.authenticated_revalidation_package_identity(
                state, object(), errors
            )

        self.assertEqual(identity, selected)
        self.assertEqual([], errors)
        build.assert_called_once_with("A19", None, mock.ANY, errors)

    def test_multiple_current_clarification_scopes_still_fail_closed(self):
        state = self._stale_state(
            {
                "q_a19": {
                    "package_scope_id": "A19",
                    "status": nh_loop.INTERVIEW_STATUS_CLARIFICATION,
                    "answer_history": [{"event_seq": 10}],
                },
                "q_a20": {
                    "package_scope_id": "A20",
                    "status": nh_loop.INTERVIEW_STATUS_CLARIFICATION,
                    "answer_history": [{"event_seq": 11}],
                },
            }
        )
        errors = []
        with mock.patch.object(
            nh_loop, "build_authenticated_package_identity"
        ) as build:
            selected = nh_loop.authenticated_revalidation_package_identity(
                state, object(), errors
            )

        self.assertIsNone(selected)
        self.assertTrue(any("current Ness clarifications" in item for item in errors))
        build.assert_not_called()

    def test_bundle_seven_baseline_cannot_be_narrowed_to_a19_clarification(self):
        state = self._stale_state(
            {
                "q_a19": {
                    "package_scope_id": "A19",
                    "status": nh_loop.INTERVIEW_STATUS_CLARIFICATION,
                    "answer_history": [{"event_seq": 1546}],
                }
            }
        )
        state["latest_bundle_seven_baseline"] = {
            "package_inventory": [
                {
                    "package_id": package_id,
                    "feature_inventory": [
                        {"feature_key": "feature.%s" % package_id.lower()}
                    ],
                }
                for package_id, _title, _kind in nh_loop.BUNDLE_SEVEN_EXPECTED_PACKAGES
            ]
        }
        errors = []
        with mock.patch.object(
            nh_loop, "build_authenticated_package_identity"
        ) as build:
            selected = nh_loop.authenticated_revalidation_package_identity(
                state, object(), errors
            )

        self.assertIsNone(selected)
        self.assertTrue(any("whole-Bundle Seven baseline" in item for item in errors))
        self.assertTrue(any("cannot select a one-package" in item for item in errors))
        build.assert_not_called()

    def test_unrelated_stale_scope_ambiguity_is_unchanged_without_clarification(self):
        state = self._stale_state({})
        errors = []
        with mock.patch.object(
            nh_loop,
            "interview_unusable_validation_set_ids",
            return_value={"vs_old_a", "vs_old_b"},
        ), mock.patch.object(
            nh_loop, "build_authenticated_package_identity"
        ) as build:
            selected = nh_loop.authenticated_revalidation_package_identity(
                state, object(), errors
            )

        self.assertIsNone(selected)
        self.assertTrue(any("2 package scopes" in item for item in errors))
        build.assert_not_called()


class TransitionRecoveryWithoutSelectionTests(unittest.TestCase):
    def test_event_1546_clarification_routes_validation_before_coverage(self):
        events = [
            json.loads(line)
            for line in (ROOT / "nh_interview_state" / "nh_interview_journal.jsonl")
            .read_text(encoding="utf-8")
            .splitlines()
            if line.strip() and json.loads(line).get("event_seq", 0) <= 1547
        ]
        errors = []
        state = nh_loop.replay_interview_state(events, errors)

        self.assertEqual([], errors)
        self.assertEqual(
            nh_loop.INTERVIEW_STATUS_CLARIFICATION,
            state["questions"]["q_80423709fcd12ab5"]["status"],
        )
        self.assertIn("A19", state["revalidation_packages"])

    def test_current_validation_supplies_recovery_facts_after_selection_stales(self):
        state = {
            "selection": None,
            "transition_evidence_binding": {
                "package_scope_id": "A19",
                "scope_root_path": "05_ACTIVE_CANDIDATE/a19.md",
                "package_id": "A19",
                "analysis": {"source_paths_checked": ["source-a.md"]},
            },
            "transition_scope": "A19",
            "routed_signal_refs": (),
            "prepared_target_path": None,
            "scope_has_validation": True,
            "validation_set_id": "vs_current",
            "piece3_standing_sha256": "a" * 64,
        }

        facts = nh_loop.transition_facts_from_state(state)

        self.assertEqual("A19", facts["package_scope_id"])
        self.assertEqual("05_ACTIVE_CANDIDATE/a19.md", facts["scope_root_path"])
        self.assertEqual(["source-a.md"], facts["required_source_paths"])
        self.assertTrue(facts["scope_has_validation"])

    def test_missing_selection_and_validation_binding_fails_closed(self):
        with self.assertRaises(nh_loop.nh_supervisor.engine.SupervisorRefusal):
            nh_loop.transition_facts_from_state(
                {
                    "selection": None,
                    "transition_evidence_binding": None,
                    "transition_scope": "A19",
                }
            )


class ExternalActionResolutionSchemaTests(unittest.TestCase):
    def test_resolution_event_exists_only_from_current_version_forward(self):
        event_type = schema.EXTERNAL_ACTION_RESOLUTION_EVENT_TYPE
        self.assertIsNone(nh_loop.interview_body_keys_for(9, event_type))
        self.assertEqual(
            schema.EXTERNAL_ACTION_RESOLUTION_BODY_KEYS,
            nh_loop.interview_body_keys_for(10, event_type),
        )
        self.assertEqual(
            schema.EXTERNAL_ACTION_RESOLUTION_BODY_KEYS,
            nh_loop.interview_body_keys_for(11, event_type),
        )
        self.assertEqual(12, nh_loop.INTERVIEW_JOURNAL_CURRENT_VERSION)

    def test_exact_historical_recovery_choices_supersede_their_old_manual_holds(self):
        events = [
            json.loads(line)
            for line in (ROOT / "nh_interview_state" / "nh_interview_journal.jsonl")
            .read_text(encoding="utf-8")
            .splitlines()
            if line.strip()
        ]
        scoped = replay.Replay(events, "A19")
        for event_seq in (989, 997):
            completion = scoped.by_seq(event_seq)
            self.assertIsNotNone(completion)
            self.assertTrue(
                commands._transition_safety_hold_superseded(
                    scoped, completion, completion["dependency_record"]
                ),
                "the later exact Ness recovery choice closes only this old hold",
            )


class QuestionAuthorityAuditTests(unittest.TestCase):
    ROOM_DECISION_PATH = (
        "05_ACTIVE_CANDIDATE/"
        "NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_WONDER_RUNTIME_v1.md"
    )
    ROOM_DECISION_QUOTE = "Ness or N.H may choose the starting form."
    ROOM_QUESTION_ID = "q_76f9deeab9207e80"

    @classmethod
    def event_1544_state(cls):
        events = [
            json.loads(line)
            for line in (ROOT / "nh_interview_state" / "nh_interview_journal.jsonl")
            .read_text(encoding="utf-8")
            .splitlines()
            if line.strip() and json.loads(line).get("event_seq", 0) <= 1544
        ]
        errors = []
        state = nh_loop.replay_interview_state(events, errors)
        if errors:
            raise AssertionError(errors)
        state["_events"] = events
        return events, state

    @classmethod
    def audit_input_outcomes(cls, state):
        outcomes = []
        for item in nh_loop.question_authority_inventory(state["questions"], "A19"):
            settled = item["question_id"] == cls.ROOM_QUESTION_ID
            outcomes.append(
                {
                    "question_id": item["question_id"],
                    "outcome": (
                        nh_loop.QUESTION_AUTHORITY_AUDIT_RETIRE_SETTLED
                        if settled
                        else nh_loop.QUESTION_AUTHORITY_AUDIT_KEEP
                    ),
                    "reason_code": (
                        "settled_by_later_direct_ness_decision"
                        if settled
                        else "genuinely_open_current_form"
                    ),
                    "evidence": (
                        {
                            "path": cls.ROOM_DECISION_PATH,
                            "quote": cls.ROOM_DECISION_QUOTE,
                        }
                        if settled
                        else None
                    ),
                    "merge_into_question_ids": [],
                }
            )
        return outcomes

    def test_authority_audit_schema_exists_only_at_version_11(self):
        kind = schema.QUESTION_AUTHORITY_AUDIT_EVENT_TYPE
        self.assertIsNone(nh_loop.interview_body_keys_for(10, kind))
        self.assertEqual(
            schema.QUESTION_AUTHORITY_AUDIT_BODY_KEYS,
            nh_loop.interview_body_keys_for(11, kind),
        )
        self.assertEqual(
            nh_loop.INTERVIEW_JOURNAL_CURRENT_VERSION,
            commands.constants.INTERVIEW_JOURNAL_CURRENT_VERSION,
        )
        self.assertEqual(
            nh_loop.INTERVIEW_JOURNAL_SUPPORTED_VERSIONS,
            commands.constants.INTERVIEW_JOURNAL_SUPPORTED_VERSIONS,
        )

    def test_exact_a19_authority_quote_retires_only_the_named_form(self):
        events, state = self.event_1544_state()
        complete = state["latest_complete_by_package"]["A19"]
        errors = []
        outcomes = nh_loop.prepare_question_authority_audit_outcomes(
            self.audit_input_outcomes(state), state, complete, events, errors
        )
        self.assertEqual([], errors)
        self.assertEqual(42, len(outcomes))
        clearance = state["coverage_clearances"]["A19"]
        body = {
            "package_key": complete["package_key"],
            "package_scope_id": "A19",
            "package_id": complete["package_id"],
            "branch": complete["branch"],
            "head_sha": complete["head_sha"],
            "source_binding_sha256": complete["source_binding_sha256"],
            "scope_root_path": clearance["scope_root_path"],
            "basis_validation_set_id": complete["validation_set_id"],
            "basis_validated_at_event_seq": complete["last_event_seq"],
            "basis_coverage_event_seq": clearance["recorded_at_event_seq"],
            "basis_group_event_seq": state["open_group"]["event_seq"],
            "audit_scope": "complete_current_question_inventory",
            "ness_action_confirmed": True,
            "question_inventory_sha256": nh_loop.question_authority_inventory_sha256(
                state["questions"], "A19"
            ),
            "question_count": 42,
            "audit_identity": None,
            "outcomes": outcomes,
            "event_seq": 1545,
        }
        body["audit_identity"] = nh_loop.question_authority_audit_identity(body)
        questions = json.loads(json.dumps(state["questions"]))
        routed = json.loads(json.dumps(state["routed_issues"]))
        audits = []
        errors = []
        delta = nh_loop.replay_question_authority_audit_event(
            body,
            events,
            questions,
            routed,
            state["validation_sets"],
            state["coverage_clearances_recorded"],
            state["question_state_moved_at"],
            state["open_group"],
            audits,
            errors,
        )
        self.assertEqual([], errors)
        self.assertIsNotNone(delta)
        self.assertTrue(questions[self.ROOM_QUESTION_ID]["retired"])
        self.assertFalse(questions["q_80423709fcd12ab5"]["retired"])
        self.assertEqual(1, len(audits))

    def test_authority_audit_can_bind_closed_triggering_group(self):
        """Answering the triggering form must not force a provider re-audit."""
        events, state = self.event_1544_state()
        complete = state["latest_complete_by_package"]["A19"]
        errors = []
        outcomes = nh_loop.prepare_question_authority_audit_outcomes(
            self.audit_input_outcomes(state), state, complete, events, errors
        )
        self.assertEqual([], errors)
        clearance = state["coverage_clearances"]["A19"]
        body = {
            "package_key": complete["package_key"],
            "package_scope_id": "A19",
            "package_id": complete["package_id"],
            "branch": complete["branch"],
            "head_sha": complete["head_sha"],
            "source_binding_sha256": complete["source_binding_sha256"],
            "scope_root_path": clearance["scope_root_path"],
            "basis_validation_set_id": complete["validation_set_id"],
            "basis_validated_at_event_seq": complete["last_event_seq"],
            "basis_coverage_event_seq": clearance["recorded_at_event_seq"],
            "basis_group_event_seq": state["open_group"]["event_seq"],
            "audit_scope": "complete_current_question_inventory",
            "ness_action_confirmed": True,
            "question_inventory_sha256": nh_loop.question_authority_inventory_sha256(
                state["questions"], "A19"
            ),
            "question_count": 42,
            "audit_identity": None,
            "outcomes": outcomes,
            "event_seq": 1545,
        }
        body["audit_identity"] = nh_loop.question_authority_audit_identity(body)
        questions = json.loads(json.dumps(state["questions"]))
        routed = json.loads(json.dumps(state["routed_issues"]))
        audits = []
        errors = []

        delta = nh_loop.replay_question_authority_audit_event(
            body,
            events,
            questions,
            routed,
            state["validation_sets"],
            state["coverage_clearances_recorded"],
            state["question_state_moved_at"],
            None,
            audits,
            errors,
        )

        self.assertEqual([], errors)
        self.assertIsNotNone(delta)
        self.assertEqual(1, len(audits))

    def test_provider_free_audit_may_resolve_coverage_overask_signal(self):
        """A coverage over-ask must not force another provider validation loop."""
        # frozen 2026-09-02 at journal event 1544: audit_current derives from the event-1518 validation set's source re-proof, which fails against a moved checkout
        self.enterContext(pinned_checkout(1544))
        events, state = self.event_1544_state()
        complete = state["latest_complete_by_package"]["A19"]
        errors = []
        outcomes = nh_loop.prepare_question_authority_audit_outcomes(
            self.audit_input_outcomes(state), state, complete, events, errors
        )
        self.assertEqual([], errors)
        clearance = state["coverage_clearances"]["A19"]
        challenged_question_id = "q_80423709fcd12ab5"
        signal_id = "rs_provider_free_overask"
        events = list(events) + [
            {
                "event_seq": 1545,
                "type": "review_signal_recorded",
                "package_scope_id": "A19",
                "routed_signal_id": signal_id,
                "signal_source": "question_coverage_review",
            }
        ]
        routed = json.loads(json.dumps(state["routed_issues"]))
        routed[signal_id] = {
            "package_scope_id": "A19",
            "challenges_question_id": challenged_question_id,
        }
        body = {
            "package_key": complete["package_key"],
            "package_scope_id": "A19",
            "package_id": complete["package_id"],
            "branch": complete["branch"],
            "head_sha": complete["head_sha"],
            "source_binding_sha256": complete["source_binding_sha256"],
            "scope_root_path": clearance["scope_root_path"],
            "basis_validation_set_id": complete["validation_set_id"],
            "basis_validated_at_event_seq": complete["last_event_seq"],
            "basis_coverage_event_seq": clearance["recorded_at_event_seq"],
            "basis_group_event_seq": state["open_group"]["event_seq"],
            "audit_scope": "complete_current_question_inventory",
            "ness_action_confirmed": True,
            "question_inventory_sha256": nh_loop.question_authority_inventory_sha256(
                state["questions"], "A19"
            ),
            "question_count": 42,
            "audit_identity": None,
            "outcomes": outcomes,
            "event_seq": 1546,
        }
        body["audit_identity"] = nh_loop.question_authority_audit_identity(body)
        audits = []
        errors = []

        delta = nh_loop.replay_question_authority_audit_event(
            body,
            events,
            json.loads(json.dumps(state["questions"])),
            routed,
            state["validation_sets"],
            state["coverage_clearances_recorded"],
            {**state["question_state_moved_at"], "A19": 1545},
            None,
            audits,
            errors,
        )

        self.assertEqual([], errors)
        self.assertIsNotNone(delta)
        self.assertTrue(routed[signal_id]["resolution_currently_proved"])
        self.assertEqual("validated", routed[signal_id]["status"])
        self.assertEqual(1546, routed[signal_id]["validated_at_event_seq"])
        self.assertFalse(nh_loop.routed_signal_still_blocking(routed[signal_id]))

    def test_malformed_nested_outcome_fails_closed_without_type_error(self):
        events, state = self.event_1544_state()
        complete = state["latest_complete_by_package"]["A19"]
        outcomes = self.audit_input_outcomes(state)
        outcomes[0]["question_id"] = []
        errors = []
        self.assertIsNone(
            nh_loop.prepare_question_authority_audit_outcomes(
                outcomes, state, complete, events, errors
            )
        )
        self.assertTrue(errors)

    def test_open_group_redelivery_excludes_a_withheld_reframe(self):
        # frozen 2026-09-02 at journal event 1544: the selector compares the frozen 1544 questions with read_source_binding(); a moved binding filters every question out before the reframe rule runs
        self.enterContext(pinned_checkout(1544))
        _events, state = self.event_1544_state()
        question = state["questions"][self.ROOM_QUESTION_ID]
        question["status"] = nh_loop.INTERVIEW_STATUS_AUTHORITY_REFRAME_REQUIRED
        question["authority_reframe_required"] = True
        question["authority_reframe_currently_proved"] = True
        errors = []
        binding = nh_loop.read_source_binding("for the focused selector test", errors)
        self.assertEqual([], errors)
        selection = nh_loop.select_next_question_group(state, binding, {})
        selected = [item["question_id"] for item in selection["questions"]]
        self.assertNotIn(self.ROOM_QUESTION_ID, selected)
        self.assertIn("q_80423709fcd12ab5", selected)
        self.assertIn(
            self.ROOM_QUESTION_ID,
            nh_loop.questions_no_longer_deliverable(
                [question], state, state["open_group"]["group_index"], True
            ),
        )

    def test_provider_free_command_appends_no_answer_or_provider_event(self):
        # frozen 2026-09-02 at journal event 1544: the command refuses when the basis validation's source binding is no longer the live one
        self.enterContext(pinned_checkout(1544))
        events, state = self.event_1544_state()
        complete = state["latest_complete_by_package"]["A19"]
        clearance = state["coverage_clearances"]["A19"]
        envelope = {
            "pre_audit_authenticated_event_seq": 1544,
            "pre_audit_authenticated_tail_sha256": events[-1]["event_sha256"],
            "package_scope_id": "A19",
            "basis_validation_set_id": complete["validation_set_id"],
            "basis_coverage_event_seq": clearance["recorded_at_event_seq"],
            "basis_group_event_seq": state["open_group"]["event_seq"],
            "ness_action_confirmed": True,
            "outcomes": self.audit_input_outcomes(state),
        }
        with tempfile.TemporaryDirectory() as folder:
            key_path = ROOT / "nh_interview_state" / "nh_interview_authenticity.key"
            shutil.copy2(key_path, Path(folder) / key_path.name)
            journal_path = Path(folder) / "nh_interview_journal.jsonl"
            source_lines = (
                ROOT / "nh_interview_state" / "nh_interview_journal.jsonl"
            ).read_text(encoding="utf-8").splitlines(keepends=True)
            journal_path.write_text(
                "".join(
                    line
                    for line in source_lines
                    if line.strip() and json.loads(line).get("event_seq", 0) <= 1544
                ),
                encoding="utf-8",
            )
            journal_path.chmod(0o600)
            head = {
                "v": nh_loop.INTERVIEW_JOURNAL_HEAD_LABEL,
                "intent_generation": 1,
                "intent_number": 1,
                "intent_event_seq": events[-1]["event_seq"],
                "intent_event_sha256": events[-1]["event_sha256"],
                "committed_event_seq": events[-1]["event_seq"],
                "committed_event_sha256": events[-1]["event_sha256"],
            }
            head["head_auth_sha256"] = nh_loop.interview_journal_head_auth(
                key_path.read_bytes(), head
            )
            head_path = Path(folder) / "nh_interview_journal.head"
            head_path.write_text(
                json.dumps(head, sort_keys=True, separators=(",", ":")) + "\n",
                encoding="utf-8",
            )
            head_path.chmod(0o600)
            stdin = io.TextIOWrapper(io.BytesIO(json.dumps(envelope).encode("utf-8")))
            with mock.patch.dict(
                os.environ, {nh_loop.INTERVIEW_STATE_DIR_ENV: folder}
            ), mock.patch.object(
                sys, "stdin", stdin
            ), contextlib.redirect_stdout(io.StringIO()):
                exit_code = nh_loop.command_record_question_authority_audit()
            self.assertEqual(nh_loop.EXIT_OK, exit_code)
            written = [
                json.loads(line)
                for line in (Path(folder) / "nh_interview_journal.jsonl")
                .read_text(encoding="utf-8")
                .splitlines()
                if line.strip()
            ]
        self.assertEqual(1545, written[-1]["event_seq"])
        self.assertEqual(schema.QUESTION_AUTHORITY_AUDIT_EVENT_TYPE, written[-1]["type"])
        before_answer_count = sum(event["type"] == "answer_recorded" for event in events)
        after_answer_count = sum(event["type"] == "answer_recorded" for event in written)
        self.assertEqual(before_answer_count, after_answer_count)
        provider_types = {
            "provider_request_prepared",
            "provider_request_dispatched",
            "provider_result_custody_recorded",
            "provider_request_terminal_recorded",
        }
        self.assertEqual(
            sum(event["type"] in provider_types for event in events),
            sum(event["type"] in provider_types for event in written),
        )


class ProviderOutputContractTests(unittest.TestCase):
    def test_ordinary_rest_of_the_world_does_not_name_rest_api_machinery(self):
        self.assertEqual(
            nh_loop.names_mechanism("visibility of the rest of the world"), []
        )

    def test_rest_api_is_still_caught_by_unambiguous_mechanism_terms(self):
        found = nh_loop.names_mechanism("choose a REST API endpoint")
        self.assertIn("api", found)
        self.assertIn("endpoint", found)

    def test_piece3_dispatch_sends_only_the_frozen_model_prompt(self):
        """Local validation operands stay bound, but are never sent to Codex."""
        local_only_marker = "LOCAL_VALIDATION_ONLY_" + ("x" * 1_100_000)
        for provider_kind in (
            "gpt_question_validation",
            "gpt_question_coverage_review",
        ):
            material = {
                "provider_kind": provider_kind,
                "prompt_inventory": {
                    "extra": {
                        "piece3_precall_requirement": {
                            "prompt": "EXACT FROZEN MODEL PROMPT",
                            "validation_context": {
                                "local_only": local_only_marker,
                            },
                        }
                    }
                },
                "required_inputs_inventory": {
                    "extra": {
                        "piece3_precall_requirement": {
                            "prompt": "EXACT FROZEN MODEL PROMPT",
                            "validation_context": {
                                "local_only": local_only_marker,
                            },
                        }
                    }
                },
            }
            prompt = nh_loop._supervisor_provider_prompt(material)
            self.assertEqual(prompt, "EXACT FROZEN MODEL PROMPT")
            self.assertNotIn("LOCAL_VALIDATION_ONLY_", prompt)

    def test_question_schema_requires_existing_effect_field_and_codes(self):
        schema = nh_loop.question_validation_model_output_schema()
        issue = schema["properties"]["issues"]["items"]
        self.assertIn("user_facing_effects", issue["required"])
        effects = issue["properties"]["user_facing_effects"]
        self.assertEqual(
            effects["items"]["enum"],
            sorted(nh_loop.NESS_QUESTION_USER_FACING_EFFECTS),
        )

    def test_question_schema_leaves_deterministic_bookkeeping_to_controller(self):
        schema = nh_loop.question_validation_model_output_schema()
        issue = schema["properties"]["issues"]["items"]
        option = issue["properties"]["options"]["anyOf"][1]["items"]
        self.assertNotIn("disposition", issue["required"])
        self.assertNotIn("disposition", issue["properties"])
        self.assertNotIn("option_id", option["required"])
        self.assertNotIn("option_id", option["properties"])

    def test_controller_derives_disposition_and_option_ids(self):
        payload = {
            "issues": [
                {
                    "classification": "genuinely_open_for_ness",
                    "disposition": "model_must_not_control_this",
                    "options": [
                        {"option_id": "model_a", "option_text": "first"},
                        {"option_id": "model_b", "option_text": "second"},
                    ],
                }
            ]
        }
        result = nh_loop.materialize_question_validation_controller_fields(payload)
        issue = result["issues"][0]
        self.assertEqual(
            nh_loop.QUESTION_VALIDATION_DISPOSITION_BY_CLASSIFICATION[
                "genuinely_open_for_ness"
            ],
            issue["disposition"],
        )
        self.assertEqual(
            ["choice_1", "choice_2"],
            [option["option_id"] for option in issue["options"]],
        )

    def test_controller_overrides_package_and_page_echoes(self):
        payload = {
            "package_id": "wrong_package",
            "page_index": 99,
            "issues": [],
        }
        result = nh_loop.materialize_question_validation_controller_fields(
            payload, package_id="A19", page_index=2
        )
        self.assertEqual("A19", result["package_id"])
        self.assertEqual(2, result["page_index"])

    def test_question_schema_uses_only_codex_supported_boundary_subset(self):
        schema = nh_loop.question_validation_model_output_schema()
        self.assertEqual([], nh_loop.codex_structured_output_schema_errors(schema))
        encoded = json.dumps(schema, sort_keys=True)
        for unsupported in ("$schema", "uniqueItems", "minimum", "maxItems"):
            self.assertNotIn('"%s"' % unsupported, encoded)

    def test_unsupported_output_schema_is_refused_before_process_launch(self):
        transport = nh_loop.NhCliProviderTransport(lambda: None)
        bad = nh_loop.question_validation_model_output_schema()
        bad["uniqueItems"] = True
        request = SimpleNamespace(
            provider_kind="gpt_question_validation",
            provider_endpoint_identity=nh_loop.SUPERVISOR_CODEX_ENDPOINT,
            provider_request_identity="pr_bad_schema",
        )
        with mock.patch.object(
            nh_loop, "question_validation_model_output_schema", return_value=bad
        ), mock.patch.object(nh_loop.subprocess, "Popen") as popen:
            with self.assertRaises(nh_loop.nh_supervisor.engine.SupervisorRefusal):
                transport._dispatch_codex(request, {}, prompt="unused")
        popen.assert_not_called()

    def test_question_dispatch_supplies_schema_without_a_provider_call(self):
        observed = {}

        class FakeProcess:
            pid = 99999999
            returncode = 0

            def __init__(self, argv, **kwargs):
                observed["argv"] = list(argv)
                observed["kwargs"] = kwargs
                schema_path = argv[argv.index("--output-schema") + 1]
                observed["schema_path"] = schema_path
                observed["schema"] = json.loads(Path(schema_path).read_text())

            def communicate(self, input=None, timeout=None):
                observed["input"] = input
                observed["timeout"] = timeout
                return b"", b""

        request = SimpleNamespace(
            provider_kind="gpt_question_validation",
            provider_endpoint_identity=nh_loop.SUPERVISOR_CODEX_ENDPOINT,
            provider_request_identity="pr_test",
            prompt_material_sha256="a" * 64,
            required_inputs_sha256="b" * 64,
        )
        with tempfile.TemporaryDirectory() as folder:
            transport = nh_loop.NhCliProviderTransport(
                lambda: SimpleNamespace(state_dir=folder)
            )
            inherited_parent_context = {
                "CODEX_SESSION_ID": "parent-session",
                "CODEX_THREAD_ID": "parent-thread",
                "CODEX_INTERNAL_ORIGINATOR_OVERRIDE": "codex_app",
                "CODEX_PERMISSION_PROFILE": "managed",
                "CODEX_SANDBOX_NETWORK_DISABLED": "1",
                "CODEX_CI": "1",
                "CODEX_SQLITE_HOME": "/tmp/parent-codex-sqlite",
            }
            # SECOND-MODEL SWITCH (2026-09-02): this proves the Codex-CLI form
            # (--output-schema temp file, parent-context scrubbing), so the
            # switch is held on "codex" here whatever the installed value is.
            with mock.patch.dict(
                os.environ, inherited_parent_context, clear=False
            ), mock.patch.object(nh_loop.subprocess, "Popen", FakeProcess), mock.patch.object(
                nh_loop, "SECOND_MODEL_PROVIDER", "codex"
            ):
                transport._dispatch_codex(request, {}, prompt="return the exact object")
        self.assertIn("--output-schema", observed["argv"])
        self.assertIn(
            "user_facing_effects",
            observed["schema"]["properties"]["issues"]["items"]["required"],
        )
        self.assertFalse(Path(observed["schema_path"]).exists())
        provider_env = observed["kwargs"]["env"]
        for name in nh_loop.CODEX_CHILD_ENVIRONMENT_EXCLUDED:
            self.assertNotIn(
                name,
                provider_env,
                "%s must not bind a nested provider to the parent Codex task"
                % name,
            )
        self.assertEqual("1", provider_env["CODEX_CI"])
        self.assertEqual(
            "/tmp/parent-codex-sqlite", provider_env["CODEX_SQLITE_HOME"]
        )
        self.assertEqual("/home/ness", provider_env["HOME"])
        self.assertEqual(transport.codex_home, provider_env["CODEX_HOME"])


class ExactReuseTests(unittest.TestCase):
    @staticmethod
    def index(blob):
        path = "05_ACTIVE_CANDIDATE/A19.md"
        return {
            "by_path": {path: blob},
            "by_basename": {"A19.md": {path}},
            "by_stem": {"A19": {path}},
            "by_category": {"active_candidate": {path}},
            "category_of": {path: "active_candidate"},
            "top_level": {"05_ACTIVE_CANDIDATE"},
            "unscannable": set(),
        }

    def test_reference_graph_reuses_only_exact_bound_source(self):
        with tempfile.TemporaryDirectory() as folder:
            cache = Path(folder) / "graph.json"
            calls = []

            def build(index):
                calls.append(index["by_path"].copy())
                paths = set(index["by_path"])
                return (
                    {path: set() for path in paths},
                    {path: set() for path in paths},
                    {},
                    {},
                )

            nh_loop._REFERENCE_GRAPH_MEMORY_CACHE.clear()
            with mock.patch.object(
                nh_loop,
                "repository_reference_graph_cache_path",
                side_effect=lambda identity=None: str(cache),
            ), mock.patch.object(
                nh_loop,
                "_build_repository_reference_graph_uncached",
                side_effect=build,
            ):
                first = nh_loop.build_repository_reference_graph(self.index(b"one"))
                nh_loop._REFERENCE_GRAPH_MEMORY_CACHE.clear()
                second = nh_loop.build_repository_reference_graph(self.index(b"one"))
                nh_loop._REFERENCE_GRAPH_MEMORY_CACHE.clear()
                third = nh_loop.build_repository_reference_graph(self.index(b"two"))
            self.assertEqual(first, second)
            self.assertEqual(2, len(calls), "unchanged bytes reuse; changed bytes rebuild")
            self.assertEqual(set(third[0]), {"05_ACTIVE_CANDIDATE/A19.md"})
            nh_loop._REFERENCE_GRAPH_MEMORY_CACHE.clear()

    def test_journal_bytes_are_authenticated_once_per_exact_snapshot(self):
        segments = [
            {
                "generation": 1,
                "number": 1,
                "basename": "nh_interview_journal.jsonl",
                "blob": b"first\n",
                "exists": True,
            }
        ]
        parsed = [{"event_seq": 1, "event_sha256": "a" * 64}]
        nh_loop._INTERVIEW_JOURNAL_PARSE_CACHE.clear()
        with mock.patch.object(
            nh_loop, "read_journal_segments", return_value=segments
        ), mock.patch.object(
            nh_loop, "parse_journal_segments", return_value=parsed
        ) as parser, mock.patch.object(
            nh_loop, "check_interview_journal_head", return_value=True
        ):
            self.assertEqual(
                nh_loop.parse_and_prove_interview_journal(1, b"k" * 32, []), parsed
            )
            first = nh_loop.parse_and_prove_interview_journal(1, b"k" * 32, [])
            first[0]["derived_replay_annotation"] = True
            second = nh_loop.parse_and_prove_interview_journal(1, b"k" * 32, [])
            self.assertEqual(second, parsed)
            self.assertNotIn("derived_replay_annotation", second[0])
            self.assertEqual(1, parser.call_count)
            segments[0]["blob"] = b"changed\n"
            nh_loop.parse_and_prove_interview_journal(1, b"k" * 32, [])
            self.assertEqual(2, parser.call_count)
        nh_loop._INTERVIEW_JOURNAL_PARSE_CACHE.clear()


PRESERVED_A19_RESULT = (
    ROOT
    / "interview_ui"
    / ".nh_supervisor_state"
    / "provider_results"
    / "pr_30e362b44323c2e3ea1e6cc65b843881ba77a06e9be844836aea58bab9ecefed.result.json"
)
PRESERVED_A19_SELECTION = {
    "package_scope_id": "A19",
    "package_id": "A19",
    "scope_root_path": (
        "05_ACTIVE_CANDIDATE/"
        "NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_WONDER_RUNTIME_v1.md"
    ),
}
PRESERVED_A19_STANDING_REFUSAL = (
    'issue "simulation.outputs.become.plans" stands on a bounded source record'
)


class AuthorityConflictPreflightTests(unittest.TestCase):
    def test_two_decision_defaults_claims_stop_preflight(self):
        with tempfile.TemporaryDirectory(dir="/tmp") as folder:
            repo = Path(folder) / "NH-GOVERNANCE"
            authority = repo / "01_AUTHORITATIVE"
            authority.mkdir(parents=True)
            (authority / nh_loop.NH_CURRENT_AUTHORITATIVE_DECISION_DEFAULTS).write_text(
                "configured authority\n", encoding="utf-8"
            )
            (authority / "NH_DECISION_DEFAULTS-S19_v2_2.md").write_text(
                "explicitly superseded historical authority\n", encoding="utf-8"
            )
            competing_name = "NH_DECISION_DEFAULTS-S19_v9_9.md"
            (authority / competing_name).write_text(
                "competing authority\n", encoding="utf-8"
            )

            def git_ok(_repo, args):
                if args == ["rev-parse", "--is-inside-work-tree"]:
                    return True, "true\n", None
                if args == ["rev-parse", "--abbrev-ref", "HEAD"]:
                    return True, nh_loop.REQUIRED_BRANCH + "\n", None
                if args == ["status", "--porcelain"]:
                    return True, "", None
                raise AssertionError(args)

            with (
                mock.patch.object(nh_loop, "NH_REPO_PATH", str(repo)),
                mock.patch.object(nh_loop, "run_git", side_effect=git_ok),
                mock.patch.object(nh_loop, "required_provider_executables", return_value=[]),
                mock.patch.object(nh_loop, "resolve_required_files", return_value=({}, True)),
            ):
                report, _lines, _error_lines = nh_loop.run_preflight_checks(
                    "authority-conflict-test"
                )

        self.assertFalse(report["ok"])
        self.assertEqual(1, len(report["competing_decision_defaults_artifacts"]))
        self.assertEqual(
            "01_AUTHORITATIVE/" + competing_name,
            report["competing_decision_defaults_artifacts"][0]["path"],
        )
        self.assertTrue(
            any("competing Decision Defaults claims" in error for error in report["errors"])
        )

    def test_explicitly_superseded_v2_2_is_historical_not_competing(self):
        with tempfile.TemporaryDirectory(dir="/tmp") as folder:
            authority = Path(folder) / "01_AUTHORITATIVE"
            authority.mkdir(parents=True)
            (authority / nh_loop.NH_CURRENT_AUTHORITATIVE_DECISION_DEFAULTS).write_text(
                "configured authority\n", encoding="utf-8"
            )
            (authority / "NH_DECISION_DEFAULTS-S19_v2_2.md").write_text(
                "historical predecessor\n", encoding="utf-8"
            )
            artifacts = nh_loop.competing_decision_defaults_artifacts(folder)

        self.assertEqual([], artifacts)


class PreservedQuestionValidationBoundaryTests(unittest.TestCase):
    """The exact preserved A19 reply, at the INSTALLED provider-result boundary.

    Nothing here writes: the interview journal is copied to a temporary
    directory, the preserved result object is read byte-for-byte, and no
    provider of any kind is contacted.
    """

    def setUp(self):
        self.folder = tempfile.TemporaryDirectory(dir="/tmp")
        self.addCleanup(self.folder.cleanup)
        state = Path(self.folder.name) / "interview_state"
        shutil.copytree(ROOT / "nh_interview_state", state)
        self.state = state
        # The installed resolver refuses a group/world-readable state directory.
        os.chmod(self.folder.name, 0o700)
        os.chmod(state, 0o700)
        self.env = mock.patch.dict(
            os.environ, {nh_loop.INTERVIEW_STATE_DIR_ENV: str(state)}
        )
        self.env.start()
        self.addCleanup(self.env.stop)
        # These provider-boundary tests exercise preserved answer semantics,
        # not authority-conflict discovery.  Give their preflight the one
        # controller-configured Defaults authority explicitly; the separate
        # authority-conflict test below keeps the real two-claim condition and
        # proves that it stops.
        self.single_defaults_authority = mock.patch.object(
            nh_loop, "competing_decision_defaults_artifacts", return_value=[]
        )
        self.single_defaults_authority.start()
        self.addCleanup(self.single_defaults_authority.stop)
        self.raw = PRESERVED_A19_RESULT.read_bytes()
        self.digest = hashlib.sha256(self.raw).hexdigest()
        self.addCleanup(self.assert_preserved_bytes_unchanged)

    def assert_preserved_bytes_unchanged(self):
        self.assertEqual(
            hashlib.sha256(PRESERVED_A19_RESULT.read_bytes()).hexdigest(),
            self.digest,
        )

    def frozen_precall(self, event_seq=1225):
        """The installed Part-A pre-call material, provider-free."""
        source_lines = (
            ROOT / "nh_interview_state" / "nh_interview_journal.jsonl"
        ).read_text().splitlines()
        events = [
            event
            for event in map(json.loads, source_lines)
            if event.get("event_seq", 0) <= event_seq
        ]
        tail = events[-1]
        (self.state / "nh_interview_journal.jsonl").write_text(
            "\n".join(json.dumps(event, sort_keys=True, separators=(",", ":")) for event in events)
            + "\n"
        )
        key = (self.state / "nh_interview_authenticity.key").read_bytes()
        head = {
            "v": nh_loop.INTERVIEW_JOURNAL_HEAD_LABEL,
            "intent_generation": 1,
            "intent_number": 1,
            "intent_event_seq": event_seq,
            "intent_event_sha256": tail["event_sha256"],
            "committed_event_seq": event_seq,
            "committed_event_sha256": tail["event_sha256"],
        }
        head["head_auth_sha256"] = nh_loop.interview_journal_head_auth(key, head)
        (self.state / "nh_interview_journal.head").write_text(
            nh_loop.interview_canonical_json(head) + "\n"
        )
        with contextlib.redirect_stdout(io.StringIO()):
            precall = nh_loop._continuation_piece3_precall_requirement(
                "A19", "question_validation", PRESERVED_A19_SELECTION
            )
        errors = []
        state = nh_loop.replay_interview_state(events, errors)
        self.assertIsNotNone(state, errors[:3])
        frozen = precall["validation_context"]
        frozen["pagination"] = nh_loop.interview_pagination_context(
            state, frozen["source_binding"]
        )
        frozen["questions"] = state["questions"]
        frozen["routed_by_id"] = state["routed_issues"]
        frozen["routed_signals"] = list(state["routed_issues"].values())
        precall["journal_position"] = len(events) + 1
        return precall

    def boundary(self, value, precall):
        errors = []
        with contextlib.redirect_stdout(io.StringIO()):
            outcome = nh_loop._continuation_question_validation_payload_contract(
                json.dumps(value, sort_keys=True),
                {"piece3_precall_requirement": precall},
                errors,
            )
        return outcome, errors

    def test_preserved_result_is_refused_by_the_provider_free_piece3_commit(self):
        """The durable failure this repair is about, reproduced exactly."""
        errors = []
        with contextlib.redirect_stdout(io.StringIO()):
            committed = nh_loop._continuation_piece3_commit(
                "A19",
                "question_validation",
                json.loads(self.raw),
                {"continuation_selection": PRESERVED_A19_SELECTION},
                errors,
            )
        self.assertIsNone(committed)
        self.assertTrue(errors)

    def test_standing_invalid_preserved_result_is_rejected_before_authorization(self):
        """The same refusal is knowable at the provider-result boundary."""
        self.enterContext(pinned_checkout(1225))
        outcome, errors = self.boundary(json.loads(self.raw), self.frozen_precall())
        self.assertIsNone(outcome)
        self.assertTrue(
            any(PRESERVED_A19_STANDING_REFUSAL in error for error in errors),
            errors[:3],
        )

    def test_b6d_refuses_the_preserved_reply_before_any_authorization(self):
        """B6d, the boundary that gates the Piece-3 authorization, says invalid."""
        self.enterContext(pinned_checkout(1225))
        context = SimpleNamespace(
            continuation_adapter=nh_loop.build_continuation_adapter(),
            _current_required_extra={
                "piece3_precall_requirement": self.frozen_precall()
            },
        )
        prepared = SimpleNamespace(work_item_kind="question_validation")
        with contextlib.redirect_stdout(io.StringIO()):
            schema_valid, admission = commands._validate_result(
                context, prepared, json.loads(self.raw), None
            )
        self.assertFalse(schema_valid)
        self.assertTrue(
            any(
                PRESERVED_A19_STANDING_REFUSAL in problem
                for problem in admission["schema_problems"]
            ),
            admission["schema_problems"][:3],
        )

    def test_event_1218_segment_shape_is_rejected_before_authorization(self):
        """The real page-2 drift is invalid before Piece-3 authorization."""
        # frozen 2026-09-02 at journal event 1225: the in-progress segment vs_c7e0962e was recorded at binding 96b64ec7; the pre-call reads the live binding, which has since moved
        self.enterContext(pinned_checkout(1225))
        events = [
            json.loads(line)
            for line in (ROOT / "nh_interview_state" / "nh_interview_journal.jsonl")
            .read_text()
            .splitlines()
        ]
        custody = next(event for event in events if event.get("event_seq") == 1218)
        value = json.loads(base64.b64decode(custody["result_bytes_base64"]))
        outcome, errors = self.boundary(value, self.frozen_precall(1225))
        self.assertIsNone(outcome)
        self.assertIn(
            "codex returned a page whose package, source state or declared "
            "segment shape does not match the segment already in progress: "
            "it is refused rather than merged",
            errors,
        )

    def test_event_1289_single_page_total_mismatch_is_rejected_before_authorization(self):
        """A complete page may not promise an issue it does not carry."""
        self.enterContext(pinned_checkout(1285))
        value = json.loads(
            (
                ROOT
                / "interview_ui/.nh_supervisor_state/provider_results"
                / "pr_4d5a269b49c1e8efd8403034cc1547cbed2c549a635054d4ca12322058d71fb6.result.json"
            ).read_text()
        )
        outcome, errors = self.boundary(value, self.frozen_precall(1285))
        self.assertIsNone(outcome)
        self.assertIn(
            "codex declared 41 issue(s) for this 1-page segment, but the "
            "complete pages carry 40: the segment is refused before authorization",
            errors,
        )

    def test_otherwise_valid_reply_still_passes_the_provider_boundary(self):
        """No weaker and no stronger acceptance: the rest of the reply passes."""
        # frozen 2026-09-02 at journal event 1225: same in-progress segment; page_count/total_issue_count come from the pagination context, which is empty under a moved binding
        self.enterContext(pinned_checkout(1225))
        events = [
            json.loads(line)
            for line in (ROOT / "nh_interview_state" / "nh_interview_journal.jsonl")
            .read_text()
            .splitlines()
        ]
        custody = next(event for event in events if event.get("event_seq") == 1218)
        value = json.loads(base64.b64decode(custody["result_bytes_base64"]))
        precall = self.frozen_precall(1225)
        pagination = precall["validation_context"]["pagination"]
        value["page_count"] = pagination["page_count"]
        value["total_issue_count"] = pagination["total_issue_count"]
        outcome, errors = self.boundary(value, precall)
        self.assertEqual(errors, [])
        self.assertIsNotNone(outcome)


class RefusedCommitClassificationTests(unittest.TestCase):
    def test_event_1655_shape_drift_is_preserved_but_not_applied(self):
        events = [
            json.loads(line)
            for line in (ROOT / "nh_interview_state" / "nh_interview_journal.jsonl")
            .read_text()
            .splitlines()
            if json.loads(line).get("event_seq", 0) <= 1655
        ]
        effect = events[-1]
        classification = nh_loop.interrupted_invalid_validation_effect(
            events, effect
        )
        self.assertEqual(
            classification["invalidity_kind"],
            "enumeration_complete_shape_drift",
        )
        self.assertTrue(classification["expected_enumeration_complete"])
        self.assertFalse(classification["recorded_enumeration_complete"])
        self.assertEqual(classification["operation_state"], "incomplete")

        errors = []
        state = nh_loop.replay_interview_state(events, errors)
        self.assertIsNotNone(state, errors[:3])
        record = state["validation_sets"][effect["validation_set_id"]]
        self.assertEqual(record["pages_recorded"], [1, 2])
        self.assertEqual(
            state["invalid_piece3_validation_effects"][-1], classification
        )

    def test_event_1296_is_preserved_but_cannot_become_question_standing(self):
        events = [
            json.loads(line)
            for line in (ROOT / "nh_interview_state" / "nh_interview_journal.jsonl")
            .read_text()
            .splitlines()
            if json.loads(line).get("event_seq", 0) <= 1296
        ]
        effect = events[-1]
        classification = nh_loop.interrupted_invalid_validation_effect(
            events, effect
        )
        self.assertEqual(classification["event_seq"], 1296)
        self.assertEqual(classification["declared_issue_count"], 41)
        self.assertEqual(classification["carried_issue_count"], 40)
        self.assertEqual(classification["operation_state"], "incomplete")

        errors = []
        state = nh_loop.replay_interview_state(events, errors)
        self.assertIsNotNone(state, errors)
        self.assertEqual(
            state["invalid_piece3_validation_effects"], [classification]
        )
        self.assertNotIn(
            effect["validation_set_id"], state["validation_sets"],
            "the preserved invalid event must not become question standing",
        )

    def test_only_refused_completion_keeps_the_invalid_effect_retired(self):
        events = [
            json.loads(line)
            for line in (ROOT / "nh_interview_state" / "nh_interview_journal.jsonl")
            .read_text()
            .splitlines()
            if json.loads(line).get("event_seq", 0) <= 1296
        ]
        effect = events[-1]
        refused = {
            "event_seq": 1297,
            "type": "supervisor_operation_completed",
            "supervisor_operation_id": (
                "op_aca461ae1d8b4e9b867210f5e546c032fa0d066c6bfe01be79175007fcb02dd2"
            ),
            "operation_outcome": "refused",
        }
        ok = dict(refused, operation_outcome="ok")
        self.assertEqual(
            nh_loop.interrupted_invalid_validation_effect(events + [refused], effect)[
                "operation_state"
            ],
            "refused",
        )
        self.assertIsNone(
            nh_loop.interrupted_invalid_validation_effect(events + [ok], effect)
        )

    def test_invalid_event_does_not_retire_the_prevalidation_binding(self):
        events = [
            json.loads(line)
            for line in (ROOT / "nh_interview_state" / "nh_interview_journal.jsonl")
            .read_text()
            .splitlines()
            if json.loads(line).get("event_seq", 0) <= 1296
        ]
        current = nh_loop.transition_current_validations(events, "A19")
        self.assertNotIn(1296, [event["event_seq"] for event in current])

    def test_full_validator_receives_reproved_precall_before_invalidity_claim(self):
        authorization = {
            "event_seq": 10,
            "provider_request_identity": "pr_saved",
            "work_item_identity": "wi_saved",
            "package_scope_id": "A19",
        }
        custody = {"provider_request_identity": "pr_saved"}

        class Scoped:
            def custody_event(self, request):
                return custody if request == "pr_saved" else None

            def scoped(self, kind):
                if kind == "supervisor_operation_completed":
                    return [{
                        "event_seq": 13,
                        "supervisor_command": "commit-piece3-provider-result",
                        "operation_outcome": "refused",
                        "work_item_identity": "wi_saved",
                        "supervisor_operation_id": "op_saved",
                    }]
                if kind == "supervisor_operation_started":
                    return [{
                        "event_seq": 12,
                        "supervisor_command": "commit-piece3-provider-result",
                        "work_item_identity": "wi_saved",
                        "supervisor_operation_id": "op_saved",
                    }]
                return []

        seen = {}

        def precall(scope, kind, selection):
            seen["precall"] = (scope, kind, selection)
            return {"coverage_validation_context": {"proved": True}}

        def validate(_text, extra, errors):
            seen["extra"] = extra
            return {"valid": True}

        adapter = SimpleNamespace(
            piece3_precall_requirement=precall,
            validate_question_validation_payload=validate,
            validate_question_coverage_review=validate,
        )
        with mock.patch.object(
            commands.engine, "custodied_bytes", return_value=b'{"ok":true}'
        ), mock.patch.object(commands, "_continuation_adapter", return_value=adapter):
            invalid = commands._piece3_schema_invalid_after_refused_commit(
                object(), Scoped(), authorization, "coverage_review", {"choice": 1}
            )
        self.assertFalse(invalid)
        self.assertEqual(
            seen["precall"], ("A19", "coverage_review", {"choice": 1})
        )
        self.assertIn("piece3_precall_requirement", seen["extra"])


class ValidationReplayCurrencyParityTests(unittest.TestCase):
    """A durable validation must replay against the same current standing."""

    def test_real_event_1570_replays_after_prior_current_resolutions_refresh(self):
        """The live pre-save check and authenticated replay must agree."""
        events = [
            json.loads(line)
            for line in (ROOT / "nh_interview_state" / "nh_interview_journal.jsonl")
            .read_text()
            .splitlines()
            if json.loads(line).get("event_seq", 0) <= 1570
        ]
        self.assertEqual(events[-1]["event_seq"], 1570)

        errors = []
        state = nh_loop.replay_interview_state(events, errors)

        self.assertIsNotNone(state, errors)
        self.assertEqual(errors, [])
        self.assertIn(
            events[-1]["validation_set_id"], state["validation_sets"]
        )


class QuestionValidationRetryFeedbackTests(unittest.TestCase):
    """The bounded retry must be able to reproduce the exact local errors."""

    def feedback(self, validator):
        terminal = {
            "event_seq": 20,
            "provider_kind": "gpt_question_validation",
            "terminal_kind": "result_invalid",
            "provider_request_identity": "pr_saved",
        }

        class Scoped:
            def custody_event(self, request):
                return {"provider_request_identity": request}

            def scoped(self, kind):
                if kind == "provider_request_terminal_recorded":
                    return [terminal]
                return []

        adapter = SimpleNamespace(
            piece3_precall_requirement=(
                lambda scope, kind, selection: {
                    "prompt": "PROMPT",
                    "validation_context": {"frozen": True},
                }
            ),
            validate_question_validation_payload=validator,
        )
        context = SimpleNamespace(journal=SimpleNamespace(read=lambda: []))
        with mock.patch.object(
            commands.engine, "custodied_bytes", return_value=b'{"ok":true}'
        ), mock.patch.object(commands.replay_mod, "Replay", lambda *a, **k: Scoped()):
            return commands._piece3_precall_with_retry_feedback(
                context,
                adapter,
                "A19",
                "question_validation",
                None,
                before_event_seq=30,
            )

    def test_retry_feedback_reproduces_errors_against_the_frozen_precall(self):
        seen = {}

        def validator(_text, extra, errors):
            seen["extra"] = extra
            errors.append("exact local error")
            return None

        precall = self.feedback(validator)
        self.assertIn(
            "validation_context",
            (seen["extra"].get("piece3_precall_requirement") or {}),
        )
        self.assertIn("exact local error", precall["prompt"])
        line = next(
            line
            for line in precall["prompt"].splitlines()
            if line.startswith("previous_rejection: ")
        )
        retry = json.loads(line.split(": ", 1)[1])
        self.assertEqual({"ok": True}, retry["previous_rejected_result"])
        self.assertEqual(["exact local error"], retry["local_validation_errors"])
        self.assertIn(
            "Use previous_rejected_result only as the exact edit base",
            precall["prompt"],
        )

    def test_now_valid_rejected_result_allows_one_fresh_bounded_request(self):
        def validator(_text, _extra, _errors):
            return {"ok": True}

        precall = self.feedback(validator)
        self.assertEqual("PROMPT", precall["prompt"])
        self.assertNotIn("BOUNDED OUTPUT RETRY", precall["prompt"])

    def test_retry_prompt_names_the_controller_locked_questions(self):
        terminal = {
            "event_seq": 20,
            "provider_kind": "gpt_question_validation",
            "terminal_kind": "result_invalid",
            "provider_request_identity": "pr_saved",
        }

        class Scoped:
            def custody_event(self, request):
                return {"provider_request_identity": request}

            def scoped(self, kind):
                return (
                    [terminal]
                    if kind == "provider_request_terminal_recorded"
                    else []
                )

        progress = {
            "locked_issues": [
                {"index": 0, "issue_key": "first_future_topic", "sha256": "a" * 64}
            ]
        }
        adapter = SimpleNamespace(
            piece3_precall_requirement=lambda *_args: {
                "prompt": "PROMPT",
                "question_validation_scratchpad": {"issue_progress": progress},
            },
            validate_question_validation_payload=(
                lambda _text, _extra, errors: errors.append("pending issue failed")
            ),
        )
        context = SimpleNamespace(journal=SimpleNamespace(read=lambda: []))
        with mock.patch.object(
            commands.engine, "custodied_bytes", return_value=b'{"ok":true}'
        ), mock.patch.object(commands.replay_mod, "Replay", lambda *a, **k: Scoped()):
            precall = commands._piece3_precall_with_retry_feedback(
                context,
                adapter,
                "A19",
                "question_validation",
                None,
                before_event_seq=30,
            )
        line = next(
            line
            for line in precall["prompt"].splitlines()
            if line.startswith("previous_rejection: ")
        )
        retry = json.loads(line.split(": ", 1)[1])
        self.assertEqual(
            [{"index": 0, "issue_key": "first_future_topic", "sha256": "a" * 64}],
            retry["locked_issue_positions"],
        )
        self.assertIn("MUST remain exactly unchanged", precall["prompt"])

    def test_refused_legacy_commit_retry_carries_the_reproduced_exact_error(self):
        terminal = {
            "event_seq": 20,
            "provider_kind": "gpt_question_validation",
            "terminal_kind": "result_received",
            "provider_request_identity": "pr_saved",
        }
        authorization = {
            "event_seq": 21,
            "type": "piece3_provider_work_recorded",
            "provider_request_identity": "pr_saved",
            "authorizes_event_type": "validation_recorded",
            "work_item_identity": "wi_saved",
        }
        start = {
            "event_seq": 22,
            "supervisor_command": "commit-piece3-provider-result",
            "supervisor_operation_id": "op_saved",
            "work_item_identity": "wi_saved",
        }
        completion = {
            "event_seq": 23,
            "supervisor_command": "commit-piece3-provider-result",
            "supervisor_operation_id": "op_saved",
            "operation_outcome": "refused",
            "work_item_identity": "wi_saved",
        }

        class Scoped:
            def custody_event(self, request):
                return {"provider_request_identity": request}

            def scoped(self, kind):
                return {
                    "provider_request_terminal_recorded": [terminal],
                    "piece3_provider_work_recorded": [authorization],
                    "supervisor_operation_started": [start],
                    "supervisor_operation_completed": [completion],
                }.get(kind, [])

        def validator(_text, _extra, errors):
            errors.append(
                "codex returned a page whose package, source state or declared "
                "segment shape does not match the segment already in progress"
            )
            return None

        adapter = SimpleNamespace(
            piece3_precall_requirement=lambda *_args: {"prompt": "PROMPT"},
            validate_question_validation_payload=validator,
        )
        context = SimpleNamespace(journal=SimpleNamespace(read=lambda: []))
        with mock.patch.object(
            commands.engine, "custodied_bytes", return_value=b'{"ok":true}'
        ), mock.patch.object(commands.replay_mod, "Replay", lambda *a, **k: Scoped()):
            precall = commands._piece3_precall_with_retry_feedback(
                context,
                adapter,
                "A19",
                "question_validation",
                None,
                before_event_seq=30,
            )
        self.assertIn("segment shape", precall["prompt"])
        self.assertIn("Preserve all otherwise-valid substantive issues", precall["prompt"])


class Piece3RetryCustodyOwnershipTests(unittest.TestCase):
    def test_exact_request_owner_selects_one_of_two_same_work_item_starts(self):
        events = [
            {
                "event_seq": 10,
                "type": "supervisor_operation_started",
                "supervisor_command": "dispatch-piece3-provider-review",
                "supervisor_operation_id": "op_first",
                "work_item_identity": "wi_same",
                "controller_executable_identity": "controller",
                "package_scope_id": "A19",
                "source_binding_sha256": "source",
                "candidate_path": "candidate",
                "candidate_sha256": "candidate-sha",
                "candidate_bytes": 10,
                "standing_before_sha256": "original-standing",
            },
            {
                "type": "provider_request_prepared",
                "supervisor_operation_id": "op_first",
                "provider_request_identity": "pr_first",
            },
            {
                "event_seq": 20,
                "type": "supervisor_operation_started",
                "supervisor_command": "dispatch-piece3-provider-review",
                "supervisor_operation_id": "op_retry",
                "work_item_identity": "wi_same",
                "controller_executable_identity": "controller",
                "package_scope_id": "A19",
                "source_binding_sha256": "source",
                "candidate_path": "candidate",
                "candidate_sha256": "candidate-sha",
                "candidate_bytes": 10,
                "standing_before_sha256": "later-operation-standing",
            },
            {
                "type": "provider_request_prepared",
                "supervisor_operation_id": "op_retry",
                "provider_request_identity": "pr_retry",
            },
            {
                "type": "provider_result_custody_recorded",
                "supervisor_operation_id": "op_retry",
                "provider_request_identity": "pr_retry",
            },
        ]
        state, start = commands._piece3_owning_start(
            SimpleNamespace(events=events), "wi_same", "pr_retry"
        )
        self.assertEqual(state, commands.SELECTION_OWNER_EXACT)
        self.assertEqual(start["supervisor_operation_id"], "op_retry")
        origin = commands._piece3_work_item_origin_start(
            SimpleNamespace(events=events), "wi_same", start
        )
        self.assertEqual(origin["supervisor_operation_id"], "op_first")
        self.assertEqual(origin["standing_before_sha256"], "original-standing")

    def test_reconciled_custody_keeps_original_dispatch_as_piece3_owner(self):
        events = [
            {
                "event_seq": 10,
                "type": "supervisor_operation_started",
                "supervisor_command": "dispatch-piece3-provider-review",
                "supervisor_operation_id": "op_dispatch",
                "work_item_identity": "wi_saved",
            },
            {
                "type": "provider_request_prepared",
                "supervisor_operation_id": "op_dispatch",
                "provider_request_identity": "pr_saved",
            },
            {
                "type": "provider_dispatch_begun",
                "supervisor_operation_id": "op_dispatch",
                "provider_request_identity": "pr_saved",
            },
            {
                "event_seq": 20,
                "type": "supervisor_operation_started",
                "supervisor_command": "reconcile-provider-request",
                "supervisor_operation_id": "op_reconcile",
                "work_item_identity": "wi_saved",
            },
            {
                "type": "provider_result_custody_recorded",
                "supervisor_operation_id": "op_reconcile",
                "provider_request_identity": "pr_saved",
            },
            {
                "type": "provider_request_terminal_recorded",
                "supervisor_operation_id": "op_reconcile",
                "provider_request_identity": "pr_saved",
            },
        ]
        state, start = commands._piece3_owning_start(
            SimpleNamespace(events=events), "wi_saved", "pr_saved"
        )
        self.assertEqual(state, commands.SELECTION_OWNER_EXACT)
        self.assertEqual(start["supervisor_operation_id"], "op_dispatch")

    def test_piece3_launch_owner_disagreement_still_fails_closed(self):
        events = [
            {
                "event_seq": 10,
                "type": "supervisor_operation_started",
                "supervisor_command": "dispatch-piece3-provider-review",
                "supervisor_operation_id": "op_one",
                "work_item_identity": "wi_saved",
            },
            {
                "event_seq": 11,
                "type": "supervisor_operation_started",
                "supervisor_command": "dispatch-piece3-provider-review",
                "supervisor_operation_id": "op_two",
                "work_item_identity": "wi_saved",
            },
            {
                "type": "provider_request_prepared",
                "supervisor_operation_id": "op_one",
                "provider_request_identity": "pr_saved",
            },
            {
                "type": "provider_dispatch_begun",
                "supervisor_operation_id": "op_two",
                "provider_request_identity": "pr_saved",
            },
        ]
        state, start = commands._piece3_owning_start(
            SimpleNamespace(events=events), "wi_saved", "pr_saved"
        )
        self.assertEqual(state, commands.SELECTION_OWNER_CONTRADICTION)
        self.assertIsNone(start)


class CoverageConvergenceTests(unittest.TestCase):
    """Provider-free novelty over the real A19 standing-target failure mode."""

    SOURCE = "96b64ec75876468bf51aa178ad6b76fb06e12fcfd92766353af56ad0800f2dde"
    WONDER = "st_16a371f850b2811763079cd54bde403f"
    CAMERA = "st_ae1eba654752dcc9188db5245f01c185"
    WONDER_QUESTION = "q_4e84250cdec54b5a"
    CAMERA_QUESTION = "q_822cce3aa7725b44"

    @staticmethod
    def gap(target, *, direction="over_ask", issue_key="q_changed", finding="changed"):
        return {
            "direction": direction,
            "issue_key": issue_key,
            "finding_key": finding,
            "signal_title": "different words for the same concern",
            "finding_evidence": ["the same settled boundary, restated"],
            "source_evidence": ["04_ACCEPTED_STANDALONE_DESIGNS/settled.md"],
            "_challenged_question": (
                {
                    "question_id": issue_key,
                    "package_scope_id": "A19",
                    "standing_target_id": target,
                }
                if direction == "over_ask"
                else None
            ),
        }

    @classmethod
    def state(cls):
        return {
            "routed_issues": {
                "old-wonder": {
                    "signal_source": nh_loop.REVIEW_SIGNAL_SOURCE_COVERAGE,
                    "package_scope_id": "A19",
                    "standing_target_id": cls.WONDER,
                    "challenges_question_id": cls.WONDER_QUESTION,
                    "source_binding_sha256": cls.SOURCE,
                    "recorded_at_event_seq": 1396,
                    "status": "validated",
                    "validated_at_event_seq": 1421,
                    "resolution_currently_proved": True,
                    "issue_key": "q_old_wording",
                    "finding_key": "wonder_plan_possibility_coexistence_settled",
                },
                "old-camera": {
                    "signal_source": nh_loop.REVIEW_SIGNAL_SOURCE_COVERAGE,
                    "package_scope_id": "A19",
                    "standing_target_id": cls.CAMERA,
                    "challenges_question_id": cls.CAMERA_QUESTION,
                    "source_binding_sha256": cls.SOURCE,
                    "recorded_at_event_seq": 1397,
                    "status": "validated",
                    "validated_at_event_seq": 1433,
                    "resolution_currently_proved": True,
                    "issue_key": "q_old_camera_key",
                    "finding_key": "camera_cross_context_privacy_already_settled",
                },
            }
        }

    @classmethod
    def complete(cls):
        return {
            "package_scope_id": "A19",
            "source_binding_sha256": cls.SOURCE,
            "last_event_seq": 1433,
        }

    def test_currently_stripped_concern_is_not_novel_after_rewording(self):
        gaps = [
            self.gap(self.WONDER, issue_key="q_new_wording", finding="new_key"),
            self.gap(self.CAMERA, issue_key="q_new_camera_key", finding="renamed"),
        ]
        novel, repeated = nh_loop.partition_novel_coverage_gaps(
            gaps, self.state(), self.complete()
        )
        self.assertEqual([], novel)
        self.assertEqual(gaps, repeated)

    def test_readmitted_overask_remains_novel(self):
        state = self.state()
        state["routed_issues"]["old-wonder"][
            "resolution_currently_proved"
        ] = False
        gap = self.gap(self.WONDER)
        novel, repeated = nh_loop.partition_novel_coverage_gaps(
            [gap], state, self.complete()
        )
        self.assertEqual([gap], novel)
        self.assertEqual([], repeated)

    def test_only_current_exact_strip_resolves_overask(self):
        signal = self.state()["routed_issues"]["old-wonder"]
        self.assertFalse(
            nh_loop.routed_validation_resolves_signal(
                signal,
                source_current=True,
                standing_witness_current=True,
                currently_proved_strip_targets=set(),
            ),
            "re-admission does not resolve an over-ask",
        )
        self.assertTrue(
            nh_loop.routed_validation_resolves_signal(
                signal,
                source_current=True,
                standing_witness_current=True,
                currently_proved_strip_targets={self.WONDER},
            ),
            "a current exact-witness strip resolves it",
        )
        self.assertFalse(
            nh_loop.routed_validation_resolves_signal(
                signal,
                source_current=False,
                standing_witness_current=True,
                currently_proved_strip_targets={self.WONDER},
            ),
            "a stale strip resolves nothing",
        )

    def test_real_a19_wonder_readmission_does_not_resolve_event_1396(self):
        events = [
            json.loads(line)
            for line in (ROOT / "nh_interview_state" / "nh_interview_journal.jsonl")
            .read_text(encoding="utf-8")
            .splitlines()
            if line.strip() and json.loads(line).get("event_seq", 0) <= 1446
        ]
        errors = []
        state = nh_loop.replay_interview_state(events, errors)
        self.assertEqual([], errors)
        complete = state["latest_complete_validation_set"]
        self.assertEqual(1433, complete["last_event_seq"])
        event = events[1445]
        gap = {
            "direction": nh_loop.COVERAGE_GAP_DIRECTION_OVER_ASK,
            **{key: event[key] for key in nh_loop.REVIEW_SIGNAL_KEYS},
            "_challenged_question": {
                "question_id": event["issue_key"],
                "package_scope_id": event["package_scope_id"],
                "standing_target_id": event["standing_target_id"],
            },
        }
        novel, repeated = nh_loop.partition_novel_coverage_gaps(
            [gap], state, complete
        )
        self.assertEqual([gap], novel)
        self.assertEqual([], repeated)
        handled = [
            signal
            for signal in state["routed_issues"].values()
            if signal.get("standing_target_id") == self.WONDER
            and signal.get("validated_at_event_seq") == 1421
        ]
        self.assertTrue(handled, "event 1396 was handled by the later validation")
        self.assertEqual(
            self.WONDER_QUESTION,
            handled[0].get("challenges_question_id"),
            "replay must retain which question coverage challenged",
        )
        self.assertFalse(
            handled[0]["resolution_currently_proved"],
            "the later validation re-admitted the question instead of stripping it",
        )
        self.assertEqual(
            "simulation.outputs",
            next(
                item["issue_key"]
                for item in complete["coverage_inventory"]
                if item.get("standing_target_id") == self.WONDER
            ),
            "the model's issue label changed but the standing target did not",
        )

    def test_real_a19_room_start_readmission_does_not_resolve_event_1395(self):
        events = [
            json.loads(line)
            for line in (ROOT / "nh_interview_state" / "nh_interview_journal.jsonl")
            .read_text(encoding="utf-8")
            .splitlines()
            if line.strip() and json.loads(line).get("event_seq", 0) <= 1395
        ]
        errors = []
        state = nh_loop.replay_interview_state(events, errors)
        self.assertEqual([], errors)
        complete = state["latest_complete_validation_set"]
        self.assertEqual(1383, complete["last_event_seq"])
        event = events[1394]
        gap = {
            "direction": nh_loop.COVERAGE_GAP_DIRECTION_OVER_ASK,
            **{key: event[key] for key in nh_loop.REVIEW_SIGNAL_KEYS},
            "_challenged_question": {
                "question_id": event["issue_key"],
                "package_scope_id": event["package_scope_id"],
                "standing_target_id": event["standing_target_id"],
            },
        }
        novel, repeated = nh_loop.partition_novel_coverage_gaps(
            [gap], state, complete
        )
        self.assertEqual([gap], novel)
        self.assertEqual([], repeated)
        signal = next(
            item
            for item in state["routed_issues"].values()
            if item.get("recorded_at_event_seq") == 1395
        )
        self.assertEqual(
            event["issue_key"], signal.get("challenges_question_id")
        )
        self.assertFalse(signal["resolution_currently_proved"])

    def test_real_a19_unresolved_camera_signal_is_not_suppressed_at_event_1445(self):
        events = [
            json.loads(line)
            for line in (ROOT / "nh_interview_state" / "nh_interview_journal.jsonl")
            .read_text(encoding="utf-8")
            .splitlines()
            if line.strip() and json.loads(line).get("event_seq", 0) <= 1445
        ]
        errors = []
        state = nh_loop.replay_interview_state(events, errors)
        self.assertEqual([], errors)
        complete = state["latest_complete_validation_set"]
        self.assertEqual(1433, complete["last_event_seq"])
        event = events[1444]
        gap = {
            "direction": nh_loop.COVERAGE_GAP_DIRECTION_OVER_ASK,
            **{key: event[key] for key in nh_loop.REVIEW_SIGNAL_KEYS},
            "_challenged_question": {
                "question_id": event["issue_key"],
                "package_scope_id": event["package_scope_id"],
                "standing_target_id": event["standing_target_id"],
            },
        }
        novel, repeated = nh_loop.partition_novel_coverage_gaps(
            [gap], state, complete
        )
        self.assertEqual([gap], novel)
        self.assertEqual([], repeated)

    def test_genuinely_new_related_concern_and_missing_gap_are_preserved(self):
        new_target = self.gap("st_genuinely_new", issue_key="q_new_dimension")
        missing = self.gap(
            None,
            direction=nh_loop.COVERAGE_GAP_DIRECTION_MISSING,
            issue_key="new.related.dimension",
        )
        novel, repeated = nh_loop.partition_novel_coverage_gaps(
            [new_target, missing], self.state(), self.complete()
        )
        self.assertEqual([new_target, missing], novel)
        self.assertEqual([], repeated)

    def test_changed_source_basis_requires_fresh_handling(self):
        complete = dict(self.complete(), source_binding_sha256="f" * 64)
        gap = self.gap(self.WONDER)
        novel, repeated = nh_loop.partition_novel_coverage_gaps(
            [gap], self.state(), complete
        )
        self.assertEqual([gap], novel)
        self.assertEqual([], repeated)

    def test_unresolved_prior_signal_does_not_suppress_provider_work(self):
        state = self.state()
        state["routed_issues"]["old-wonder"]["status"] = (
            "awaiting_question_validation"
        )
        state["routed_issues"]["old-wonder"]["validated_at_event_seq"] = None
        state["routed_issues"]["old-wonder"]["resolution_currently_proved"] = None
        gap = self.gap(self.WONDER)
        novel, repeated = nh_loop.partition_novel_coverage_gaps(
            [gap], state, self.complete()
        )
        self.assertEqual([gap], novel)
        self.assertEqual([], repeated)

    def test_restart_over_identical_evidence_is_stable_and_suppresses_dispatch(self):
        gaps = [self.gap(self.WONDER), self.gap(self.CAMERA)]
        first = nh_loop.partition_novel_coverage_gaps(
            gaps, self.state(), self.complete()
        )
        second = nh_loop.partition_novel_coverage_gaps(
            json.loads(json.dumps(gaps)),
            json.loads(json.dumps(self.state())),
            json.loads(json.dumps(self.complete())),
        )
        self.assertEqual(first, second)
        self.assertFalse(first[0], "no novel signal means no validation dispatch is owed")

    def test_latest_complete_inventory_refreshes_only_effectively_resolved_signals(self):
        """Ordinary signals refresh; re-admitted over-asks remain blocking."""
        # frozen 2026-09-02 at journal event 1531: the latest complete A19 set (last page at 1518) is re-proved against the checkout; a moved checkout marks it source_semantics_stale and the refresh skips the scope
        self.enterContext(pinned_checkout(1531))
        events = [
            json.loads(line)
            for line in (ROOT / "nh_interview_state" / "nh_interview_journal.jsonl")
            .read_text(encoding="utf-8")
            .splitlines()
            if line.strip() and json.loads(line).get("event_seq", 0) <= 1531
        ]
        errors = []
        state = nh_loop.replay_interview_state(events, errors)
        self.assertEqual([], errors)
        complete = state["latest_complete_by_package"]["A19"]
        self.assertEqual(1518, complete["last_event_seq"])
        blocking = [
            signal["routed_signal_id"]
            for signal in state["routed_issues"].values()
            if signal.get("package_scope_id") == "A19"
            and signal.get("challenges_question_id") is None
            and nh_loop.routed_signal_still_blocking(signal)
        ]
        self.assertEqual(
            [],
            blocking,
            "ordinary classified targets remain refreshable",
        )
        challenged = [
            signal
            for signal in state["routed_issues"].values()
            if signal.get("package_scope_id") == "A19"
            and signal.get("challenges_question_id") is not None
        ]
        self.assertTrue(challenged)
        self.assertTrue(
            all(nh_loop.routed_signal_still_blocking(signal) for signal in challenged),
            "end-of-replay refresh must not turn re-admission into resolution",
        )

    def test_current_coverage_and_real_questions_stop_before_another_dispatch(self):
        """COVERAGE-TO-NESS-STOP must be reachable while questions block work."""
        state = {
            "contradiction": None,
            "incomplete_operation": None,
            "open_request": None,
            "established_complete": False,
            "custody_unverifiable": False,
            "t1_custody_unverifiable": False,
            "stop_record": None,
            "selection": {
                "admitted_route": commands.SELECTION_ROUTE_QUESTION_VALIDATION
            },
            "t1_output_retry_exhausted": False,
            "piece3_no_progress": None,
            "t1_route_signal_owed": False,
            "transition_scope": "A19",
            "scope_validation_complete": True,
            "piece3_authorization": {"validation": None, "coverage": None},
            "piece3_custody_awaiting": {"validation": None, "coverage": None},
            "piece3_output_retry_exhausted": False,
        }
        context = SimpleNamespace(
            interview_gate_reader=lambda scope: {
                "unlocked": False,
                "reasons": [nh_loop.INTERVIEW_GATE_BLOCKING_QUESTIONS],
                "errors": [],
                "blocking_question_ids": ["q_real"],
                "coverage_review_current": True,
            }
        )
        position = commands.loop_position(context, state)
        self.assertEqual(commands.LOOP_NEEDS_NESS_DECISION, position["loop_state"])
        self.assertIsNone(position["loop_next_command"])

    def test_own_words_delivery_stops_before_provider_while_design_gate_stays_closed(self):
        state = {
            "contradiction": None,
            "incomplete_operation": None,
            "open_request": None,
            "established_complete": False,
            "custody_unverifiable": False,
            "t1_custody_unverifiable": False,
            "stop_record": None,
            "selection": {
                "admitted_route": commands.SELECTION_ROUTE_QUESTION_VALIDATION
            },
            "t1_output_retry_exhausted": False,
            "piece3_no_progress": None,
            "t1_route_signal_owed": False,
            "transition_scope": "A19",
            "scope_validation_complete": True,
            "piece3_authorization": {"validation": None, "coverage": None},
            "piece3_custody_awaiting": {"validation": None, "coverage": None},
            "piece3_output_retry_exhausted": False,
        }
        context = SimpleNamespace(
            interview_gate_reader=lambda scope: {
                "unlocked": False,
                "reasons": [
                    nh_loop.INTERVIEW_GATE_BLOCKING_QUESTIONS,
                    nh_loop.INTERVIEW_GATE_COVERAGE_REVIEW_REQUIRED,
                    nh_loop.INTERVIEW_GATE_DECISION_BINDING_UNPROVED,
                ],
                "errors": ["own-words answers are not yet mechanically bound"],
                "blocking_question_ids": ["q_next"],
                "authority_reframe_question_ids": [],
                "routing_signals_awaiting_validation": [],
                "coverage_review_current": False,
                "question_delivery_ready": True,
            }
        )

        position = commands.loop_position(context, state)

        self.assertEqual(commands.LOOP_NEEDS_NESS_DECISION, position["loop_state"])
        self.assertIsNone(position["loop_next_command"])

    def test_current_coverage_with_unresolved_signal_reenters_validation(self):
        """A routed concern is validated next; current coverage is not rerun."""
        state = {
            "contradiction": None,
            "incomplete_operation": None,
            "open_request": None,
            "established_complete": False,
            "custody_unverifiable": False,
            "t1_custody_unverifiable": False,
            "stop_record": None,
            "selection": {
                "admitted_route": commands.SELECTION_ROUTE_QUESTION_VALIDATION
            },
            "t1_output_retry_exhausted": False,
            "piece3_no_progress": None,
            "t1_route_signal_owed": False,
            "transition_scope": "A19",
            "scope_validation_complete": True,
            "piece3_authorization": {"validation": None, "coverage": None},
            "piece3_custody_awaiting": {"validation": None, "coverage": None},
            "piece3_output_retry_exhausted": False,
        }
        context = SimpleNamespace(
            interview_gate_reader=lambda scope: {
                "unlocked": False,
                "reasons": [
                    nh_loop.INTERVIEW_GATE_BLOCKING_QUESTIONS,
                    nh_loop.INTERVIEW_GATE_ROUTED_SIGNALS,
                ],
                "errors": [],
                "blocking_question_ids": ["q_real"],
                "routing_signals_awaiting_validation": ["rs_unresolved"],
                "coverage_review_current": True,
            }
        )

        position = commands.loop_position(context, state)

        self.assertEqual(
            commands.LOOP_PACKAGE_CLEARANCE_REQUIRED, position["loop_state"]
        )
        self.assertEqual("validation", position["piece3_stage"])
        self.assertEqual(
            "dispatch-piece3-provider-review", position["loop_next_command"]
        )

    def test_current_open_group_and_real_question_still_stop_for_ness(self):
        state = {
            "contradiction": None,
            "incomplete_operation": None,
            "open_request": None,
            "established_complete": False,
            "custody_unverifiable": False,
            "t1_custody_unverifiable": False,
            "stop_record": None,
            "selection": {
                "admitted_route": commands.SELECTION_ROUTE_QUESTION_VALIDATION
            },
            "t1_output_retry_exhausted": False,
            "piece3_no_progress": None,
            "t1_route_signal_owed": False,
            "transition_scope": "A19",
            "scope_validation_complete": True,
            "piece3_authorization": {"validation": None, "coverage": None},
            "piece3_custody_awaiting": {"validation": None, "coverage": None},
            "piece3_output_retry_exhausted": False,
        }
        context = SimpleNamespace(
            interview_gate_reader=lambda scope: {
                "unlocked": False,
                "reasons": [
                    nh_loop.INTERVIEW_GATE_OPEN_GROUP,
                    nh_loop.INTERVIEW_GATE_BLOCKING_QUESTIONS,
                ],
                "errors": [],
                "blocking_question_ids": ["q_real", "q_reframe"],
                "authority_reframe_question_ids": ["q_reframe"],
                "coverage_review_current": True,
            }
        )
        position = commands.loop_position(context, state)
        self.assertEqual(commands.LOOP_NEEDS_NESS_DECISION, position["loop_state"])
        self.assertIsNone(position["loop_next_command"])

    def test_reframe_only_boundary_does_not_dispatch_a_provider(self):
        state = {
            "contradiction": None,
            "incomplete_operation": None,
            "open_request": None,
            "established_complete": False,
            "custody_unverifiable": False,
            "t1_custody_unverifiable": False,
            "stop_record": None,
            "selection": {
                "admitted_route": commands.SELECTION_ROUTE_QUESTION_VALIDATION
            },
            "t1_output_retry_exhausted": False,
            "piece3_no_progress": None,
            "t1_route_signal_owed": False,
            "transition_scope": "A19",
            "scope_validation_complete": True,
            "piece3_authorization": {"validation": None, "coverage": None},
            "piece3_custody_awaiting": {"validation": None, "coverage": None},
            "piece3_output_retry_exhausted": False,
        }
        context = SimpleNamespace(
            interview_gate_reader=lambda scope: {
                "unlocked": False,
                "reasons": [nh_loop.INTERVIEW_GATE_BLOCKING_QUESTIONS],
                "errors": [],
                "blocking_question_ids": ["q_reframe"],
                "authority_reframe_question_ids": ["q_reframe"],
                "coverage_review_current": True,
            }
        )
        position = commands.loop_position(context, state)
        self.assertEqual(
            commands.LOOP_PACKAGE_CLEARANCE_REQUIRED, position["loop_state"]
        )
        self.assertIsNone(position["loop_next_command"])
        self.assertEqual(
            "question_authority_reframe_required", position["dependency_code"]
        )

    def test_saved_coverage_result_is_processed_before_the_ness_stop(self):
        """Durable custody is never stranded merely because questions are ready."""
        state = {
            "contradiction": None,
            "incomplete_operation": None,
            "open_request": None,
            "established_complete": False,
            "custody_unverifiable": False,
            "t1_custody_unverifiable": False,
            "stop_record": None,
            "selection": {
                "admitted_route": commands.SELECTION_ROUTE_QUESTION_VALIDATION
            },
            "t1_output_retry_exhausted": False,
            "piece3_no_progress": None,
            "t1_route_signal_owed": False,
            "transition_scope": "A19",
            "scope_validation_complete": True,
            "piece3_authorization": {"validation": None, "coverage": None},
            "piece3_custody_awaiting": {
                "validation": None,
                "coverage": {"provider_request_identity": "pr_saved"},
            },
            "piece3_output_retry_exhausted": False,
        }
        context = SimpleNamespace(
            interview_gate_reader=lambda scope: {
                "unlocked": False,
                "reasons": [
                    nh_loop.INTERVIEW_GATE_BLOCKING_QUESTIONS,
                    nh_loop.INTERVIEW_GATE_ROUTED_SIGNALS,
                ],
                "errors": [],
                "blocking_question_ids": ["q_real"],
                "routing_signals_awaiting_validation": ["rs_unresolved"],
                "coverage_review_current": True,
            }
        )
        position = commands.loop_position(context, state)
        self.assertEqual(commands.LOOP_PIECE3_RESULT_PENDING, position["loop_state"])
        self.assertEqual("coverage", position["piece3_stage"])
        self.assertEqual(
            "process-custodied-provider-result", position["loop_next_command"]
        )


class BundleSevenContinueAfterFailureTests(unittest.TestCase):
    def test_bundle_package_completion_requires_current_validation_and_review(self):
        validation = {
            "type": "validation_recorded",
            "event_seq": 11,
            "package_scope_id": "A17",
            "validation_set_id": "vs_a17",
        }
        complete = {
            "validation_set_id": "vs_a17",
            "first_event_seq": 11,
            "last_event_seq": 11,
        }
        state = {
            "_events": [validation],
            "latest_complete_by_package": {"A17": complete},
            "coverage_clearances": {
                "A17": {
                    "validation_set_id": "vs_a17",
                    "validated_at_event_seq": 11,
                }
            },
            "revalidation_packages": set(),
            "routed_issues": {},
            "incomplete_validation_set_ids": set(),
            "incomplete_enumeration_set_ids": set(),
            "stale_validation_set_ids": set(),
        }

        self.assertIs(
            complete,
            nh_loop.bundle_seven_package_review_complete(state, "A17", 10),
        )

        state["stale_validation_set_ids"] = {"vs_a17"}
        self.assertIsNone(
            nh_loop.bundle_seven_package_review_complete(state, "A17", 10)
        )
        state["stale_validation_set_ids"] = set()
        state["revalidation_packages"] = {"A17"}
        self.assertIsNone(
            nh_loop.bundle_seven_package_review_complete(state, "A17", 10)
        )
        state["revalidation_packages"] = set()
        state["routed_issues"] = {
            "later": {
                "package_scope_id": "A17",
                "status": "awaiting_question_validation",
                "recorded_at_event_seq": 12,
            }
        }
        state["_events"].append(
            {
                "type": "review_signal_recorded",
                "event_seq": 12,
                "package_scope_id": "A17",
                "routed_signal_id": "later",
            }
        )
        self.assertIsNone(
            nh_loop.bundle_seven_package_review_complete(state, "A17", 10)
        )

    def test_bundle_questions_stay_withheld_until_current_merge_exists(self):
        state = {
            "coverage_clearances": {"A17": {}},
            "coverage_clearances_recorded": {"A17": {}},
            "latest_complete_by_package": {},
            "_events": [],
            "bundle_seven_baselines": [{}],
        }
        binding = {"branch": "b", "head_sha": "h", "binding_sha256": "s"}
        with (
            mock.patch.object(
                nh_loop, "interview_coverage_cleared_scopes", return_value={"A17"}
            ),
            mock.patch.object(
                nh_loop, "current_bundle_seven_baseline", return_value={}
            ),
            mock.patch.object(
                nh_loop, "current_bundle_seven_question_merge", return_value=None
            ),
        ):
            self.assertEqual(
                set(),
                nh_loop.interview_delivery_coverage_cleared_scopes(
                    state, binding, {}
                ),
            )

        with (
            mock.patch.object(
                nh_loop, "interview_coverage_cleared_scopes", return_value={"A17"}
            ),
            mock.patch.object(
                nh_loop, "current_bundle_seven_baseline", return_value={}
            ),
            mock.patch.object(
                nh_loop,
                "current_bundle_seven_question_merge",
                # Ness, 2026-09-03 (section 2): a merge clears exactly the packages it
                # NAMES, so the stand-in names A17 instead of standing for all ten.
                return_value={"package_validation_set_ids": {"A17": "vs_a17"}},
            ),
        ):
            self.assertEqual(
                {"A17"},
                nh_loop.interview_delivery_coverage_cleared_scopes(
                    state, binding, {}
                ),
            )

    def test_mouth_authorization_is_one_bounded_source_record(self):
        text = (
            "**The mouth model:** produces declared dimensions. Authorization "
            "for mouth use does not require Ness to manually approve every "
            "individual invocation.\n"
        )
        units = nh_loop.parse_bounded_source_units(
            text.encode("utf-8"),
            "01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md",
        )
        matching = [
            unit
            for unit in units
            if "does not require Ness to manually approve every individual invocation"
            in unit["text"]
        ]
        self.assertEqual(1, len(matching))
        self.assertEqual("labelled_field", matching[0]["kind"])

    def test_bundle_seven_supervisor_status_uses_batch_control_anchor(self):
        context = SimpleNamespace(
            controller_executable_identity="c" * 64,
            binding=SimpleNamespace(
                package_scope_id="A17",
                source_binding_sha256="s" * 64,
            ),
        )
        output = io.StringIO()
        with mock.patch.object(
            nh_loop, "build_supervisor_context", return_value=context
        ) as build, contextlib.redirect_stdout(output):
            code = nh_loop.command_bundle_seven_supervisor_status()
        self.assertEqual(nh_loop.EXIT_OK, code)
        self.assertIs(
            nh_loop.bundle_seven_control_package_anchor,
            build.call_args.kwargs["control_anchor_resolver"],
        )
        report = json.loads(output.getvalue()[output.getvalue().index("{"):])
        self.assertTrue(report["ok"])
        self.assertEqual("A17", report["package_scope_id"])

    def test_bundle_context_ignores_validation_from_before_current_baseline(self):
        packages = [
            {
                "package_id": package_id,
                "source_paths": ["%s.md" % package_id.lower()],
                "feature_inventory": [{"feature_key": "%s.feature" % package_id.lower()}],
            }
            for package_id, _title, _work_kind in nh_loop.BUNDLE_SEVEN_EXPECTED_PACKAGES
        ]
        baseline = {
            "event_seq": 50,
            "baseline_identity": "b" * 64,
            "package_inventory": packages,
        }
        selection = nh_loop.bundle_seven_question_validation_selection(
            baseline, "A17", []
        )
        state = {
            "latest_bundle_seven_baseline": baseline,
            "_events": [
                {
                    "type": "validation_recorded",
                    "event_seq": 40,
                    "package_scope_id": "A17",
                    "validation_set_id": "old",
                }
            ],
            "routed_issues": {},
            "revalidation_packages": set(),
            "standing_chain_sha256": "s" * 64,
        }
        captured = {}

        def build(mode, facts, errors, control_context=None):
            captured.update(mode=mode, facts=facts, control=control_context)
            return "context"

        with mock.patch.object(nh_loop, "build_transition_context", side_effect=build):
            result = nh_loop.build_bundle_seven_question_validation_context(
                selection, state, [], control_context="control"
            )

        self.assertEqual("context", result)
        self.assertEqual("pre_validation", captured["mode"])
        self.assertFalse(captured["facts"]["scope_has_validation"])
        self.assertEqual(50, captured["facts"]["validation_after_event_seq"])
        self.assertEqual(selection, captured["facts"]["continuation_selection"])
        self.assertEqual(
            tuple(
                package_id
                for package_id, _title, _work_kind
                in nh_loop.BUNDLE_SEVEN_EXPECTED_PACKAGES
            ),
            captured["facts"]["bundle_seven_package_scope_ids"],
        )

    def test_bundle_context_keeps_incomplete_inventory_in_validation_mode(self):
        packages = [
            {
                "package_id": package_id,
                "source_paths": ["%s.md" % package_id.lower()],
                "feature_inventory": [
                    {"feature_key": "%s.feature" % package_id.lower()}
                ],
            }
            for package_id, _title, _work_kind in nh_loop.BUNDLE_SEVEN_EXPECTED_PACKAGES
        ]
        baseline = {
            "event_seq": 50,
            "baseline_identity": "b" * 64,
            "package_inventory": packages,
        }
        selection = nh_loop.bundle_seven_question_validation_selection(
            baseline, "A19", []
        )
        partial = {
            "type": "validation_recorded",
            "event_seq": 60,
            "package_scope_id": "A19",
            "validation_set_id": "partial-a19",
        }
        state = {
            "latest_bundle_seven_baseline": baseline,
            "_events": [partial],
            "routed_issues": {},
            "revalidation_packages": set(),
            "incomplete_validation_set_ids": {"partial-a19"},
            "incomplete_enumeration_set_ids": {"partial-a19"},
            "stale_validation_set_ids": set(),
            "standing_chain_sha256": "s" * 64,
        }
        captured = {}

        def build(mode, facts, errors, control_context=None):
            captured.update(mode=mode, facts=facts, control=control_context)
            return "context"

        with mock.patch.object(
            nh_loop,
            "transition_current_validations",
            return_value=[partial],
        ), mock.patch.object(
            nh_loop,
            "interview_unusable_validation_set_ids",
            return_value={"partial-a19"},
        ), mock.patch.object(
            nh_loop,
            "build_transition_context",
            side_effect=build,
        ):
            result = nh_loop.build_bundle_seven_question_validation_context(
                selection, state, [], control_context="control"
            )

        self.assertEqual("context", result)
        self.assertEqual("post_validation", captured["mode"])
        self.assertTrue(captured["facts"]["scope_has_validation"])
        self.assertFalse(captured["facts"]["scope_validation_complete"])
        self.assertEqual(
            "partial-a19", captured["facts"]["validation_set_id"]
        )

    def test_bundle_context_resumes_authorized_coverage_before_later_gap_signals(self):
        packages = [
            {
                "package_id": package_id,
                "source_paths": ["%s.md" % package_id.lower()],
                "feature_inventory": [
                    {"feature_key": "%s.feature" % package_id.lower()}
                ],
            }
            for package_id, _title, _work_kind in nh_loop.BUNDLE_SEVEN_EXPECTED_PACKAGES
        ]
        baseline = {
            "event_seq": 50,
            "baseline_identity": "b" * 64,
            "package_inventory": packages,
        }
        selection = nh_loop.bundle_seven_question_validation_selection(
            baseline, "A21", []
        )
        events = [
            {
                "type": "validation_recorded",
                "event_seq": 60,
                "package_scope_id": "A21",
                "validation_set_id": "current",
            },
            {
                "type": "piece3_provider_work_recorded",
                "event_seq": 70,
                "package_scope_id": "A21",
                "authorizes_event_type": "question_coverage_review_recorded",
            },
            {
                "type": "review_signal_recorded",
                "event_seq": 80,
                "package_scope_id": "A21",
                "routed_signal_id": "new-gap",
                "signal_source": "question_coverage_review",
            },
        ]
        state = {
            "latest_bundle_seven_baseline": baseline,
            "_events": events,
            "routed_issues": {
                "new-gap": {
                    "package_scope_id": "A21",
                    "recorded_at_event_seq": 80,
                    "status": "awaiting_question_validation",
                }
            },
            "revalidation_packages": set(),
            "standing_chain_sha256": "s" * 64,
        }
        captured = {}

        def build(mode, facts, errors, control_context=None):
            captured.update(mode=mode, facts=facts, control=control_context)
            return "context"

        with mock.patch.object(nh_loop, "build_transition_context", side_effect=build):
            result = nh_loop.build_bundle_seven_question_validation_context(
                selection, state, [], control_context="control"
            )

        self.assertEqual("context", result)
        self.assertEqual("post_validation", captured["mode"])
        self.assertTrue(captured["facts"]["scope_has_validation"])
        self.assertEqual(70, captured["facts"]["coverage_authorization_event_seq"])
        self.assertEqual((), captured["facts"]["routed_signal_refs"])

    def test_supervised_bundle_page_uses_dispatch_custody_authorization_commit(self):
        selection = {
            "package_scope_id": "A17",
            "package_id": "A17",
            "scope_root_path": "root.md",
            "source_paths": ["root.md"],
        }
        journal_state = {"tag": "initial"}

        class Journal:
            def read(self):
                return [journal_state["tag"]]

        context = mock.Mock()
        context.journal = Journal()
        context.transition_facts = {"scope_has_validation": False}
        custody = {
            "work_item_kind": "question_validation",
            "provider_request_identity": "request",
            "result_custody_identity": "custody",
        }
        authorization = {
            "provider_request_identity": "request",
            "result_custody_identity": "custody",
        }

        class Replay:
            def __init__(self, events, _scope):
                self.tag = events[0]

            def unconsumed_piece3_authorization(self, _event_type):
                return authorization if self.tag == "authorized" else None

            def custodied_results_awaiting_processing(self):
                return [custody] if self.tag == "dispatched" else []

            def open_provider_requests(self):
                return []

            def custody_event(self, _request_identity):
                return custody if self.tag == "authorized" else None

            def terminal_event(self, _request_identity):
                if self.tag != "authorized":
                    return None
                return {
                    "terminal_kind": "result_received",
                    "provider_request_identity": "request",
                }

        def dispatch(_context, _selection):
            journal_state["tag"] = "dispatched"
            return mock.Mock(report={"ok": True})

        def process(_context):
            journal_state["tag"] = "authorized"
            return mock.Mock(report={"ok": True})

        def commit(*_args, **_kwargs):
            journal_state["tag"] = "committed"
            return {"committed": True}

        with (
            mock.patch.object(
                nh_loop,
                "load_interview_for_command",
                return_value={
                    "latest_bundle_seven_baseline": {},
                    "_events": ["initial"],
                },
            ),
            mock.patch.object(
                nh_loop, "build_supervisor_context", return_value="control"
            ) as control_builder,
            mock.patch.object(
                nh_loop,
                "build_bundle_seven_question_validation_context",
                return_value=context,
            ),
            mock.patch.object(nh_loop.nh_supervisor.replay, "Replay", Replay),
            mock.patch.object(
                nh_loop.nh_supervisor.commands,
                "dispatch_piece3_provider_review_for_controller_selection",
                side_effect=dispatch,
            ) as dispatched,
            mock.patch.object(
                nh_loop.nh_supervisor.commands,
                "process_custodied_provider_result",
                side_effect=process,
            ) as processed,
            mock.patch.object(
                nh_loop.nh_supervisor.engine,
                "custodied_bytes",
                return_value=b'{"issues": []}',
            ),
            mock.patch.object(
                nh_loop.nh_supervisor.engine,
                "parse_result_bytes",
                return_value=({"issues": []}, None),
            ),
            mock.patch.object(
                nh_loop, "_continuation_piece3_commit", side_effect=commit
            ) as committed,
        ):
            errors = []
            ok, provider_calls = (
                nh_loop.run_supervised_bundle_seven_question_validation(
                    selection, errors
                )
            )

        self.assertTrue(ok)
        self.assertEqual([], errors)
        self.assertEqual(1, provider_calls)
        dispatched.assert_called_once()
        processed.assert_called_once()
        committed.assert_called_once()
        control_builder.assert_called_once_with(
            errors,
            control_anchor_resolver=nh_loop.bundle_seven_control_package_anchor,
        )

    def test_supervised_bundle_auto_runs_coverage_after_current_validation(self):
        selection = {
            "package_scope_id": "A17",
            "package_id": "A17",
            "scope_root_path": "root.md",
            "source_paths": ["root.md"],
        }
        journal_state = {"tag": "initial"}

        class Journal:
            def read(self):
                return [journal_state["tag"]]

        context = mock.Mock()
        context.journal = Journal()
        context.transition_facts = {"scope_has_validation": True}
        custody = {
            "work_item_kind": "coverage_review",
            "provider_request_identity": "request",
            "result_custody_identity": "custody",
        }
        authorization = {
            "provider_request_identity": "request",
            "result_custody_identity": "custody",
        }

        class Replay:
            def __init__(self, events, _scope):
                self.tag = events[0]

            def unconsumed_piece3_authorization(self, _event_type):
                return authorization if self.tag == "authorized" else None

            def custodied_results_awaiting_processing(self):
                return [custody] if self.tag == "dispatched" else []

            def open_provider_requests(self):
                return []

            def custody_event(self, _request_identity):
                return custody if self.tag == "authorized" else None

            def terminal_event(self, _request_identity):
                if self.tag != "authorized":
                    return None
                return {
                    "terminal_kind": "result_received",
                    "provider_request_identity": "request",
                }

        def dispatch(_context, _selection):
            journal_state["tag"] = "dispatched"
            return mock.Mock(report={"ok": True})

        def process(_context):
            journal_state["tag"] = "authorized"
            return mock.Mock(report={"ok": True})

        def commit(_context, _selection):
            journal_state["tag"] = "committed"
            return mock.Mock(report={"ok": True})

        with (
            mock.patch.object(
                nh_loop,
                "load_interview_for_command",
                return_value={
                    "latest_bundle_seven_baseline": {},
                    "_events": ["initial"],
                },
            ),
            mock.patch.object(nh_loop, "build_supervisor_context", return_value="control"),
            mock.patch.object(
                nh_loop,
                "build_bundle_seven_question_validation_context",
                return_value=context,
            ),
            mock.patch.object(nh_loop.nh_supervisor.replay, "Replay", Replay),
            mock.patch.object(
                nh_loop,
                "read_source_binding",
                return_value={"binding_sha256": "b" * 64},
            ),
            mock.patch.object(
                nh_loop, "bundle_seven_coverage_cycle_guard", return_value=True
            ) as cycle_guard,
            mock.patch.object(
                nh_loop.nh_supervisor.commands,
                "dispatch_piece3_provider_review_for_controller_selection",
                side_effect=dispatch,
            ),
            mock.patch.object(
                nh_loop.nh_supervisor.commands,
                "process_custodied_provider_result",
                side_effect=process,
            ),
            mock.patch.object(
                nh_loop.nh_supervisor.commands,
                "commit_piece3_provider_result_for_controller_selection",
                side_effect=commit,
            ) as committed,
        ):
            errors = []
            ok, provider_calls = nh_loop.run_supervised_bundle_seven_question_validation(
                selection, errors, work_item_kind="auto"
            )

        self.assertTrue(ok)
        self.assertEqual([], errors)
        self.assertEqual(1, provider_calls)
        committed.assert_called_once()
        cycle_guard.assert_called_once()

    def test_supervised_bundle_repeated_coverage_stops_before_dispatch(self):
        selection = {
            "package_scope_id": "B30",
            "package_id": "B30",
            "scope_root_path": "root.md",
            "source_paths": ["root.md"],
        }

        class Journal:
            def read(self):
                return ["initial"]

        context = mock.Mock()
        context.journal = Journal()
        context.transition_facts = {"scope_has_validation": True}

        class Replay:
            def __init__(self, _events, _scope):
                pass

            def unconsumed_piece3_authorization(self, _event_type):
                return None

            def custodied_results_awaiting_processing(self):
                return []

            def open_provider_requests(self):
                return []

        with (
            mock.patch.object(
                nh_loop,
                "load_interview_for_command",
                return_value={
                    "latest_bundle_seven_baseline": {},
                    "_events": ["initial"],
                },
            ),
            mock.patch.object(
                nh_loop, "build_supervisor_context", return_value="control"
            ),
            mock.patch.object(
                nh_loop,
                "build_bundle_seven_question_validation_context",
                return_value=context,
            ),
            mock.patch.object(nh_loop.nh_supervisor.replay, "Replay", Replay),
            mock.patch.object(
                nh_loop,
                "read_source_binding",
                return_value={"binding_sha256": "b" * 64},
            ),
            mock.patch.object(
                nh_loop, "bundle_seven_coverage_cycle_guard", return_value=False
            ) as cycle_guard,
            mock.patch.object(
                nh_loop.nh_supervisor.commands,
                "dispatch_piece3_provider_review_for_controller_selection",
            ) as dispatched,
        ):
            errors = []
            ok, provider_calls = nh_loop.run_supervised_bundle_seven_question_validation(
                selection, errors, work_item_kind="coverage_review"
            )

        self.assertFalse(ok)
        self.assertEqual(0, provider_calls)
        cycle_guard.assert_called_once()
        dispatched.assert_not_called()

    def test_preserved_b30_cycle_stops_rephrased_same_targets(self):
        events = [
            json.loads(line)
            for line in (ROOT / "nh_interview_state" / "nh_interview_journal.jsonl")
            .read_text(encoding="utf-8")
            .splitlines()
            if line.strip() and json.loads(line).get("event_seq", 0) <= 2466
        ]
        replay_errors = []
        state = nh_loop.replay_interview_state(events, replay_errors)
        source_binding = (
            "185fa4e889a5b8bd610bdd729b0df86d3d9d612d1da886d2d8e6e560012c3533"
        )
        errors = []
        repeated = nh_loop.bundle_seven_repeated_coverage_question_targets(
            events, state, "B30", source_binding, errors
        )

        self.assertEqual([], replay_errors)
        self.assertEqual([], errors)
        self.assertEqual(14, len(repeated))
        errors = []
        self.assertFalse(
            nh_loop.bundle_seven_coverage_cycle_guard(
                events, state, "B30", source_binding, errors
            )
        )
        self.assertTrue(any("stopped before another provider call" in e for e in errors))

    def test_preserved_b30_cycle_allows_retry_after_source_change(self):
        events = [
            json.loads(line)
            for line in (ROOT / "nh_interview_state" / "nh_interview_journal.jsonl")
            .read_text(encoding="utf-8")
            .splitlines()
            if line.strip() and json.loads(line).get("event_seq", 0) <= 2466
        ]
        state = nh_loop.replay_interview_state(events, [])
        errors = []

        self.assertTrue(
            nh_loop.bundle_seven_coverage_cycle_guard(
                events, state, "B30", "f" * 64, errors
            )
        )
        self.assertEqual([], errors)

    def test_controller_owned_piece3_dispatch_uses_coverage_after_validation(self):
        selection = {
            "package_scope_id": "A21",
            "package_id": "A21",
            "scope_root_path": "a21.md",
        }
        facts = {
            "package_scope_id": "A21",
            "continuation_selection": selection,
            "scope_has_validation": True,
            "scope_validation_complete": True,
        }
        context = SimpleNamespace(
            binding=SimpleNamespace(
                package_scope_id="A21",
                package_id="A21",
                scope_root_path="a21.md",
                source_binding_sha256="s" * 64,
            ),
            transition_facts=facts,
            journal=SimpleNamespace(read=lambda: [{"event_seq": 1}]),
        )
        situation = SimpleNamespace(
            candidate=object(),
            pending_custody=[],
            open_requests=[],
        )

        class Scoped:
            def __init__(self, _events, _scope):
                pass

            def unconsumed_piece3_authorization(self, _event_type):
                return None

        operation = SimpleNamespace(
            started_event={"event_seq": 7}, start=lambda: None
        )
        outcome = object()
        with (
            mock.patch.object(commands, "require_start_gate"),
            mock.patch.object(
                commands,
                "read_state",
                return_value=([{"event_seq": 1}], situation, "LIVE_PROVED", {}),
            ),
            mock.patch.object(commands, "refuse_on_contradiction"),
            mock.patch.object(commands.replay_mod, "Replay", Scoped),
            mock.patch.object(
                commands, "_piece3_bounded_retry_owner", return_value=None
            ),
            mock.patch.object(
                commands.engine,
                "piece3_work_item",
                return_value=({"kind": "coverage"}, "work-id"),
            ) as piece3,
            mock.patch.object(commands, "build_envelope", return_value={}),
            mock.patch.object(commands.engine, "Operation", return_value=operation),
            mock.patch.object(commands, "_continuation_adapter", return_value=object()),
            mock.patch.object(
                commands,
                "_piece3_precall_with_retry_feedback",
                return_value={"proved": True},
            ) as precall,
            mock.patch.object(commands, "_dispatch", return_value=outcome) as dispatch,
            mock.patch.object(
                commands, "_close_dispatch_operation", return_value="closed"
            ),
        ):
            result = commands.dispatch_piece3_provider_review_for_controller_selection(
                context, selection
            )

        self.assertEqual("closed", result)
        piece3.assert_called_once_with(
            context,
            situation.candidate,
            "coverage_review",
            transition_state=facts,
        )
        self.assertEqual("coverage_review", precall.call_args.args[3])
        self.assertEqual(
            "gpt_question_coverage_review",
            dispatch.call_args.kwargs["extra_prompt"]["specialized_prompt_kind"],
        )
        self.assertEqual(
            "coverage", dispatch.call_args.kwargs["extra_inputs"]["piece3_stage"]
        )

    def test_controller_owned_piece3_dispatch_continues_incomplete_validation(self):
        selection = {
            "package_scope_id": "A19",
            "package_id": "A19",
            "scope_root_path": "a19.md",
        }
        facts = {
            "package_scope_id": "A19",
            "continuation_selection": selection,
            "scope_has_validation": True,
            "scope_validation_complete": False,
            "validation_set_id": "partial-a19",
        }
        context = SimpleNamespace(
            binding=SimpleNamespace(
                package_scope_id="A19",
                package_id="A19",
                scope_root_path="a19.md",
                source_binding_sha256="s" * 64,
            ),
            transition_facts=facts,
            journal=SimpleNamespace(read=lambda: [{"event_seq": 1}]),
        )
        situation = SimpleNamespace(
            candidate=object(),
            pending_custody=[],
            open_requests=[],
        )

        class Scoped:
            def __init__(self, _events, _scope):
                pass

            def unconsumed_piece3_authorization(self, _event_type):
                return None

        operation = SimpleNamespace(
            started_event={"event_seq": 7}, start=lambda: None
        )
        outcome = object()
        with (
            mock.patch.object(commands, "require_start_gate"),
            mock.patch.object(
                commands,
                "read_state",
                return_value=([{"event_seq": 1}], situation, "LIVE_PROVED", {}),
            ),
            mock.patch.object(commands, "refuse_on_contradiction"),
            mock.patch.object(commands.replay_mod, "Replay", Scoped),
            mock.patch.object(
                commands, "_piece3_bounded_retry_owner", return_value=None
            ),
            mock.patch.object(
                commands.engine,
                "piece3_work_item",
                return_value=({"kind": "validation"}, "work-id"),
            ) as piece3,
            mock.patch.object(commands, "build_envelope", return_value={}),
            mock.patch.object(commands.engine, "Operation", return_value=operation),
            mock.patch.object(commands, "_continuation_adapter", return_value=object()),
            mock.patch.object(
                commands,
                "_piece3_precall_with_retry_feedback",
                return_value={"proved": True},
            ) as precall,
            mock.patch.object(commands, "_dispatch", return_value=outcome) as dispatch,
            mock.patch.object(
                commands, "_close_dispatch_operation", return_value="closed"
            ),
        ):
            result = commands.dispatch_piece3_provider_review_for_controller_selection(
                context, selection
            )

        self.assertEqual("closed", result)
        piece3.assert_called_once_with(
            context,
            situation.candidate,
            "question_validation",
            transition_state=facts,
        )
        self.assertEqual("question_validation", precall.call_args.args[3])
        self.assertEqual(
            "gpt_question_validation",
            dispatch.call_args.kwargs["extra_prompt"]["specialized_prompt_kind"],
        )
        self.assertEqual(
            "validation", dispatch.call_args.kwargs["extra_inputs"]["piece3_stage"]
        )

    def test_controller_owned_coverage_commit_wraps_part_b_in_operation(self):
        selection = {
            "package_scope_id": "A21",
            "package_id": "A21",
            "scope_root_path": "a21.md",
        }
        facts = {
            "package_scope_id": "A21",
            "continuation_selection": selection,
            "scope_has_validation": True,
        }
        context = SimpleNamespace(
            binding=SimpleNamespace(
                package_scope_id="A21",
                package_id="A21",
                scope_root_path="a21.md",
            ),
            transition_facts=facts,
        )
        authorization = {
            "package_scope_id": "A21",
            "authorizes_event_type": "question_coverage_review_recorded",
            "provider_request_identity": "request",
            "result_custody_identity": "custody",
            "work_item_identity": "work-id",
        }
        custody = {
            "work_item_kind": "coverage_review",
            "provider_request_identity": "request",
            "result_custody_identity": "custody",
        }
        terminal = {"terminal_kind": "result_received"}
        situation = SimpleNamespace(candidate=object())

        class Scoped:
            def __init__(self, _events, _scope):
                pass

            def unconsumed_piece3_authorization(self, _event_type):
                return authorization

            def custody_event(self, _request_identity):
                return custody

            def terminal_event(self, _request_identity):
                return terminal

            def prepared_event(self, _request_identity):
                return {"type": "provider_request_prepared"}

        completed = []
        operation = SimpleNamespace(
            appended=[],
            start=lambda: None,
            complete=completed.append,
        )
        piece3_commit = mock.Mock(return_value={"committed": True})
        adapter = SimpleNamespace(piece3_commit=piece3_commit)
        with (
            mock.patch.object(commands, "require_start_gate"),
            mock.patch.object(
                commands,
                "read_state",
                return_value=([{"event_seq": 1}], situation, "LIVE_PROVED", {}),
            ),
            mock.patch.object(commands, "refuse_on_contradiction"),
            mock.patch.object(commands.replay_mod, "Replay", Scoped),
            mock.patch.object(commands.engine, "custodied_bytes", return_value=b"{}"),
            mock.patch.object(commands.engine, "parse_result_bytes", return_value=({}, None)),
            mock.patch.object(commands, "_rebuild_work_item", return_value={"kind": "coverage"}),
            mock.patch.object(commands, "build_envelope", return_value={}),
            mock.patch.object(commands.engine, "Operation", return_value=operation),
            mock.patch.object(commands, "_continuation_adapter", return_value=adapter),
        ):
            result = commands.commit_piece3_provider_result_for_controller_selection(
                context, selection
            )

        self.assertTrue(result.report["ok"])
        self.assertEqual(["ok"], completed)
        self.assertEqual("coverage_review", piece3_commit.call_args.args[1])
        self.assertEqual(selection, piece3_commit.call_args.args[3]["continuation_selection"])

    def test_merged_bundle_audit_history_is_not_a_live_transition(self):
        events = [
            {
                "type": "validation_recorded",
                "event_seq": 10,
                "package_scope_id": "A17",
                "validation_set_id": "vs_a17",
            },
            {
                "type": "provider_request_prepared",
                "event_seq": 11,
                "package_scope_id": "A17",
            },
            {
                "type": schema.BUNDLE_SEVEN_QUESTION_MERGE_EVENT_TYPE,
                "event_seq": 20,
                "package_validation_set_ids": {"A17": "vs_a17"},
            },
            {
                "type": "provider_request_prepared",
                "event_seq": 21,
                "package_scope_id": "A20",
            },
        ]

        cutoffs = commands.merged_bundle_seven_audit_cutoffs(events)

        self.assertEqual({"A17": 20}, cutoffs)
        self.assertNotIn(
            "A17", commands.authenticated_q_evidence_scopes(
                [
                    {
                        "type": schema.NESS_CANDIDATE_ACCEPTANCE_EVENT_TYPE,
                        "event_seq": 1,
                        "package_scope_id": "P",
                    },
                    *events,
                ],
                "P",
            )
        )
        self.assertIn(
            "A20", commands.authenticated_q_evidence_scopes(
                [
                    {
                        "type": schema.NESS_CANDIDATE_ACCEPTANCE_EVENT_TYPE,
                        "event_seq": 1,
                        "package_scope_id": "P",
                    },
                    *events,
                ],
                "P",
            )
        )

    def test_bundle_seven_question_batch_is_not_ten_competing_transitions(self):
        events = [
            {
                "type": schema.NESS_CANDIDATE_ACCEPTANCE_EVENT_TYPE,
                "event_seq": 1,
                "package_scope_id": "P",
            },
            {
                "type": schema.BUNDLE_SEVEN_BASELINE_EVENT_TYPE,
                "event_seq": 2,
                "review_complete": True,
                "package_inventory": [
                    {"package_id": "A17"},
                    {"package_id": "A19"},
                    {"package_id": "MUSIC_SYSTEM"},
                ],
            },
            {
                "type": "validation_recorded",
                "event_seq": 3,
                "package_scope_id": "A17",
            },
            {
                "type": "provider_request_prepared",
                "event_seq": 4,
                "package_scope_id": "A19",
            },
            {
                "type": "provider_request_prepared",
                "event_seq": 5,
                "package_scope_id": "MUSIC_SYSTEM",
            },
        ]

        self.assertEqual(
            set(), commands.authenticated_q_evidence_scopes(events, "P")
        )
        self.assertEqual(
            {"A17", "A19", "MUSIC_SYSTEM"},
            commands.authenticated_q_evidence_scopes(
                events, "P", include_bundle_seven_audit_scopes=True
            ),
        )

    def test_malformed_bundle_seven_inventory_hides_nothing(self):
        events = [
            {
                "type": schema.NESS_CANDIDATE_ACCEPTANCE_EVENT_TYPE,
                "event_seq": 1,
                "package_scope_id": "P",
            },
            {
                "type": schema.BUNDLE_SEVEN_BASELINE_EVENT_TYPE,
                "event_seq": 2,
                "review_complete": True,
                "package_inventory": [
                    {"package_id": "A17"},
                    {"package_id": "A17"},
                ],
            },
            {
                "type": "validation_recorded",
                "event_seq": 3,
                "package_scope_id": "A17",
            },
        ]

        self.assertEqual(
            {"A17"}, commands.authenticated_q_evidence_scopes(events, "P")
        )

    def test_pagination_continues_only_the_selected_package_scope(self):
        def partial_record(scope, issue_key):
            return {
                "package_scope_id": scope,
                "source_binding_sha256": "binding",
                "complete": False,
                "pages_recorded": [1],
                "page_count": 2,
                "total_issue_count": 2,
                "issue_keys": [issue_key],
                "enumeration_complete": True,
                "enumeration_generation": 1,
                "segment_number": 1,
                "previous_segment_id": None,
                "first_event_seq": 10,
                "enumeration": {
                    "enumeration_id": "enum.%s" % scope,
                    "complete": False,
                    "seen_issue_keys": {issue_key},
                    "seen_target_ids": set(),
                    "seen_form_identities": set(),
                },
            }

        state = {
            "validation_set_order": ["vs_a17", "vs_a19"],
            "validation_sets": {
                "vs_a17": partial_record("A17", "a17.first"),
                "vs_a19": partial_record("A19", "a19.first"),
            },
            "revalidation_after_seq": {},
        }
        binding = {"binding_sha256": "binding"}

        a17 = nh_loop.interview_pagination_context(state, binding, "A17")
        a20 = nh_loop.interview_pagination_context(state, binding, "A20")

        self.assertEqual("vs_a17", a17["validation_set_id"])
        self.assertEqual(2, a17["expected_page_index"])
        self.assertIsNone(a20["validation_set_id"])
        self.assertEqual(1, a20["expected_page_index"])

    def test_one_package_failure_does_not_stop_the_next_package(self):
        baseline = {"event_seq": 10}
        plan = {
            # Ness, 2026-09-03 (section 2): the batch now MERGES the packages that
            # finished instead of stopping at the first failure, so this fixture
            # carries the plan keys that merge step reads.
            "baseline_identity": "b" * 64,
            "packages": [
                {"package_id": "A19", "feature_keys": ["a19.feature"]},
                {"package_id": "A20", "feature_keys": ["a20.feature"]},
            ],
            "package_count": 2,
            "feature_count": 2,
        }
        completed = set()
        dispatched = []
        progress = []

        def reload_state(_report, _errors):
            return {
                "latest_complete_by_package": {
                    package_id: {"first_event_seq": 11}
                    for package_id in completed
                },
                "_events": [],
                "standing_chain_sha256": "c" * 64,
            }

        def validate_package(selection, _errors, work_item_kind=None):
            package_id = selection["package_id"]
            dispatched.append((package_id, work_item_kind))
            if package_id == "A19":
                return False, 1
            completed.add(package_id)
            return True, 1

        with (
            mock.patch.object(
                nh_loop,
                "run_preflight_checks",
                return_value=({"ok": True, "errors": []}, [], []),
            ),
            mock.patch.object(nh_loop, "new_interview_report", return_value={}),
            mock.patch.object(
                nh_loop,
                "load_interview_for_command",
                return_value={
                    "latest_bundle_seven_baseline": baseline,
                    "validation_sets": {},
                },
            ),
            mock.patch.object(
                nh_loop,
                "bundle_seven_question_validation_plan",
                return_value=plan,
            ),
            mock.patch.object(
                nh_loop,
                "bundle_seven_question_validation_selection",
                side_effect=lambda _baseline, package_id, _errors: {
                    "package_id": package_id
                },
            ),
            mock.patch.object(
                nh_loop, "reload_interview_state", side_effect=reload_state
            ),
            mock.patch.object(
                nh_loop,
                "read_source_binding",
                return_value={"binding_sha256": "b", "branch": "nh-design-loop", "head_sha": "h"},
            ),
            # The merge of the packages that DID finish is exercised up to its append;
            # this test is about the loop continuing, so the append itself stops here.
            mock.patch.object(nh_loop, "append_interview_event", return_value=None),
            mock.patch.object(
                nh_loop, "current_bundle_seven_baseline", return_value=baseline
            ),
            mock.patch.object(
                nh_loop,
                "bundle_seven_package_review_complete",
                side_effect=lambda _state, package_id, _seq, _binding=None: (
                    {"validation_set_id": "vs_" + package_id}
                    if package_id in completed
                    else None
                ),
            ),
            mock.patch.object(
                nh_loop,
                "run_supervised_bundle_seven_question_validation",
                side_effect=validate_package,
            ),
            mock.patch.object(nh_loop, "finish_interview_command", return_value=1),
            mock.patch.object(nh_loop, "emit_live", side_effect=progress.append),
        ):
            nh_loop.command_bundle_seven_question_validation()

        self.assertEqual([("A19", "auto"), ("A20", "auto")], dispatched)
        self.assertEqual(
            "Bundle Seven [##########] 2/2 (100%); completed=1; issues=1",
            progress[-1],
        )

    def test_bundle_seven_progress_distinguishes_processed_from_completed(self):
        self.assertEqual(
            "Bundle Seven [###-------] 3/10 (30%); completed=2; issues=1",
            nh_loop.bundle_seven_progress_line(3, 10, 2, 1),
        )

    def test_bundle_seven_progress_rejects_unbalanced_counts(self):
        with self.assertRaisesRegex(ValueError, "do not balance"):
            nh_loop.bundle_seven_progress_line(3, 10, 3, 1)


class PublicPiece3LifecycleRepairTests(unittest.TestCase):
    def test_public_validation_reopens_authenticated_local_preparation(self):
        material = {
            "package_scope_id": "A19",
            "prompt": "saved prompt",
            "source_binding_sha256": "a" * 64,
        }
        selection = {"package_scope_id": "A19"}
        with (
            mock.patch.object(
                nh_loop,
                "load_ai_prepared_work",
                return_value=(material, "saved-request"),
            ),
            mock.patch.object(nh_loop, "command_question_validation") as part_a,
            mock.patch.object(
                nh_loop,
                "load_interview_for_command",
                return_value={"latest_bundle_seven_baseline": object()},
            ),
            mock.patch.object(
                nh_loop,
                "bundle_seven_question_validation_selection",
                return_value=selection,
            ),
            mock.patch.object(
                nh_loop,
                "run_supervised_bundle_seven_question_validation",
                return_value=(True, 0),
            ) as supervised,
            mock.patch.object(
                nh_loop, "codex_review_checkpoint_spec", return_value={}
            ),
            mock.patch.object(
                nh_loop, "clear_codex_review_checkpoint", return_value=True
            ),
            mock.patch.object(nh_loop, "reload_interview_state", return_value={}),
            mock.patch.object(nh_loop, "read_source_binding", return_value={}),
            mock.patch.object(nh_loop, "summarise_interview_state"),
            mock.patch.object(
                nh_loop, "finish_interview_command", return_value=nh_loop.EXIT_OK
            ),
        ):
            result = nh_loop.command_supervised_piece3("question_validation")

        self.assertEqual(nh_loop.EXIT_OK, result)
        part_a.assert_not_called()
        self.assertEqual(
            "saved-request",
            supervised.call_args.kwargs["prepared_request_identity"],
        )
        self.assertIs(
            material, supervised.call_args.kwargs["prepared_material"]
        )

    def test_obsolete_public_entry_points_are_removed(self):
        self.assertFalse(hasattr(nh_loop, "command_next_package"))
        self.assertFalse(hasattr(nh_loop, "command_prepare_next_claude_task"))
        self.assertNotIn("  next-package       ", nh_loop.USAGE)
        self.assertNotIn("  prepare-next-claude-task\n", nh_loop.USAGE)
        with mock.patch.object(nh_loop, "emit"), mock.patch.object(
            nh_loop, "command_supervisor"
        ) as supervisor, mock.patch.dict(os.environ, {}, clear=True):
            result = nh_loop.main(["nh_loop.py", "execute-next-claude-task"])
        self.assertEqual(nh_loop.EXIT_USAGE, result)
        supervisor.assert_not_called()

    def test_public_validation_routes_through_supervised_lifecycle(self):
        with mock.patch.object(
            nh_loop, "command_supervised_piece3", return_value=nh_loop.EXIT_OK
        ) as supervised, mock.patch.object(
            nh_loop, "run_codex_question_validation"
        ) as direct_provider:
            result = nh_loop.command_question_validation()

        self.assertEqual(nh_loop.EXIT_OK, result)
        supervised.assert_called_once_with("question_validation")
        direct_provider.assert_not_called()

    def test_public_coverage_routes_through_supervised_lifecycle(self):
        with mock.patch.object(
            nh_loop, "command_supervised_piece3", return_value=nh_loop.EXIT_OK
        ) as supervised:
            result = nh_loop.command_question_coverage_review()

        self.assertEqual(nh_loop.EXIT_OK, result)
        supervised.assert_called_once_with("coverage_review")

    def test_supervised_validation_resumes_only_exact_matching_checkpoint(self):
        observed = {}

        class FakeProcess:
            pid = 99999999
            returncode = 0

            def __init__(self, argv, **kwargs):
                observed["argv"] = list(argv)
                observed["kwargs"] = kwargs

            def communicate(self, input=None, timeout=None):
                observed["input"] = input
                observed["timeout"] = timeout
                return b"", b""

        source_binding = "a" * 64
        base_prompt = "the exact completed validation prompt"
        prompt = (
            base_prompt
            + nh_loop.QUESTION_VALIDATION_RETRY_FEEDBACK_MARKER
            + "the exact source quotation did not match\n"
        )
        thread_id = "019c1234-5678-7abc-9def-0123456789ab"
        request = SimpleNamespace(
            provider_kind="gpt_question_validation",
            provider_endpoint_identity=nh_loop.SUPERVISOR_CODEX_ENDPOINT,
            provider_request_identity="pr_resume_test",
            prompt_material_sha256="b" * 64,
            required_inputs_sha256="c" * 64,
        )
        material = {
            "package_binding": {"source_binding_sha256": source_binding}
        }
        with tempfile.TemporaryDirectory() as folder, mock.patch.object(
            nh_loop, "CODEX_REVIEW_CHECKPOINT_ROOT", folder
        ):
            checkpoint = nh_loop.codex_review_checkpoint_spec(
                "question-validation", base_prompt, source_binding
            )
            retry_checkpoint = nh_loop.codex_review_checkpoint_spec(
                "question-validation", prompt, source_binding
            )
            self.assertEqual(
                checkpoint["checkpoint_identity"],
                retry_checkpoint["checkpoint_identity"],
            )
            self.assertTrue(
                nh_loop.write_codex_review_checkpoint(checkpoint, thread_id, [])
            )
            transport = nh_loop.NhCliProviderTransport(
                lambda: SimpleNamespace(state_dir=folder)
            )
            with mock.patch.object(
                nh_loop.subprocess, "Popen", FakeProcess
            ), mock.patch.object(nh_loop, "SECOND_MODEL_PROVIDER", "codex"):
                transport._dispatch_codex(request, material, prompt=prompt)

        self.assertIn("resume", observed["argv"])
        self.assertIn(thread_id, observed["argv"])
        self.assertNotIn("--ephemeral", observed["argv"])
        self.assertIn(b"Continue the exact same read-only review", observed["input"])
        self.assertIn(
            b"the exact source quotation did not match", observed["input"]
        )
        self.assertNotIn(base_prompt.encode("utf-8"), observed["input"])

    def test_supervised_coverage_resumes_only_exact_matching_checkpoint(self):
        observed = {}

        class FakeProcess:
            pid = 99999999
            returncode = 0

            def __init__(self, argv, **kwargs):
                observed["argv"] = list(argv)

            def communicate(self, input=None, timeout=None):
                observed["input"] = input
                return b"", b""

        source_binding = "a" * 64
        base_prompt = "the exact completed coverage prompt"
        prompt = (
            base_prompt
            + nh_loop.QUESTION_VALIDATION_RETRY_FEEDBACK_MARKER
            + "the checked source list did not match\n"
        )
        thread_id = "019c1234-5678-7abc-9def-0123456789ab"
        request = SimpleNamespace(
            provider_kind="gpt_question_coverage_review",
            provider_endpoint_identity=nh_loop.SUPERVISOR_CODEX_ENDPOINT,
            provider_request_identity="pr_coverage_resume_test",
            prompt_material_sha256="b" * 64,
            required_inputs_sha256="c" * 64,
        )
        material = {
            "package_binding": {"source_binding_sha256": source_binding}
        }
        with tempfile.TemporaryDirectory() as folder, mock.patch.object(
            nh_loop, "CODEX_REVIEW_CHECKPOINT_ROOT", folder
        ):
            checkpoint = nh_loop.codex_review_checkpoint_spec(
                "question-coverage-review", base_prompt, source_binding
            )
            retry_checkpoint = nh_loop.codex_review_checkpoint_spec(
                "question-coverage-review", prompt, source_binding
            )
            self.assertEqual(
                checkpoint["checkpoint_identity"],
                retry_checkpoint["checkpoint_identity"],
            )
            self.assertTrue(
                nh_loop.write_codex_review_checkpoint(checkpoint, thread_id, [])
            )
            transport = nh_loop.NhCliProviderTransport(
                lambda: SimpleNamespace(state_dir=folder)
            )
            with mock.patch.object(
                nh_loop.subprocess, "Popen", FakeProcess
            ), mock.patch.object(nh_loop, "SECOND_MODEL_PROVIDER", "codex"):
                transport._dispatch_codex(request, material, prompt=prompt)

        self.assertIn("resume", observed["argv"])
        self.assertIn(thread_id, observed["argv"])
        self.assertNotIn("--ephemeral", observed["argv"])
        self.assertIn(b"Continue the exact same read-only review", observed["input"])
        self.assertIn(b"the checked source list did not match", observed["input"])
        self.assertNotIn(base_prompt.encode("utf-8"), observed["input"])

    def test_first_supervised_validation_saves_a_resumable_thread(self):
        observed = {}
        thread_id = "019c1234-5678-7abc-9def-0123456789ab"

        class FakeProcess:
            pid = 99999999
            returncode = 0

            def __init__(self, argv, **kwargs):
                observed["argv"] = list(argv)
                self.stdout = kwargs["stdout"]

            def communicate(self, input=None, timeout=None):
                observed["input"] = input
                self.stdout.write(
                    (
                        '{"type":"thread.started","thread_id":"%s"}\n'
                        % thread_id
                    ).encode("utf-8")
                )
                self.stdout.flush()
                return None

        source_binding = "a" * 64
        prompt = "the exact first validation prompt"
        request = SimpleNamespace(
            provider_kind="gpt_question_validation",
            provider_endpoint_identity=nh_loop.SUPERVISOR_CODEX_ENDPOINT,
            provider_request_identity="pr_first_checkpoint_test",
            prompt_material_sha256="b" * 64,
            required_inputs_sha256="c" * 64,
        )
        material = {
            "package_binding": {"source_binding_sha256": source_binding}
        }
        with tempfile.TemporaryDirectory() as folder:
            transport = nh_loop.NhCliProviderTransport(
                lambda: SimpleNamespace(state_dir=folder)
            )
            with mock.patch.object(
                nh_loop, "CODEX_REVIEW_CHECKPOINT_ROOT", folder
            ), mock.patch.object(
                nh_loop, "read_codex_review_checkpoint", return_value=None
            ), mock.patch.object(
                nh_loop, "write_codex_review_checkpoint", return_value=True
            ) as save_checkpoint, mock.patch.object(
                nh_loop.subprocess, "Popen", FakeProcess
            ), mock.patch.object(nh_loop, "SECOND_MODEL_PROVIDER", "codex"):
                transport._dispatch_codex(request, material, prompt=prompt)

        self.assertNotIn("--ephemeral", observed["argv"])
        self.assertEqual(prompt.encode("utf-8"), observed["input"])
        self.assertEqual(thread_id, save_checkpoint.call_args.args[1])


class PaginatedValidationBindingTests(unittest.TestCase):
    def test_precall_binding_keeps_the_exact_incomplete_validation_root(self):
        package_binding = {
            "binding_sha256": "b" * 64,
            "scope_root_path": "03_WORKFLOW/a19-root.md",
            "seed_paths": ["03_WORKFLOW/a19-root.md"],
        }
        closure = {
            "closure_sha256": "c" * 64,
            "paths": ["03_WORKFLOW/a19-root.md"],
        }
        identity = {
            "package_scope_id": "A19",
            "package_id": "A19",
            "package_key": "A19",
        }
        with mock.patch.object(
            nh_loop,
            "derive_package_source_binding",
            return_value=package_binding,
        ) as derive_binding, mock.patch.object(
            nh_loop,
            "derive_relevant_source_closure",
            return_value=closure,
        ):
            result = nh_loop.derive_precall_question_validation_source_requirement(
                identity,
                {"binding_sha256": "s" * 64},
                {"by_path": {}},
                [],
                [],
                authenticated_validation_set_id="vs_a19_page_1",
            )

        self.assertIsNotNone(result)
        self.assertEqual(
            {
                "package_scope_id": "A19",
                "validation_set_id": "vs_a19_page_1",
            },
            derive_binding.call_args.kwargs["authenticated_request"],
        )


if __name__ == "__main__":
    unittest.main()

"""Focused regressions for the 2026-09-04 major state/input audit repairs."""

import io
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
for directory in (ROOT, ROOT / "controller"):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import nh_loop  # noqa: E402


class CurrentPackageOrderingRegression(unittest.TestCase):
    def test_newer_established_anchor_wins_even_if_older_has_more_validations(self):
        events = [
            {"type": "validation_recorded", "package_scope_id": "older", "event_seq": 1},
            {"type": "validation_recorded", "package_scope_id": "older", "event_seq": 2},
            {"type": "validation_recorded", "package_scope_id": "older", "event_seq": 3},
            {"type": "validation_recorded", "package_scope_id": "newer", "event_seq": 4},
        ]

        def established(_events, scope, anchor, errors):
            return True, {"path": scope, "sha256": scope, "bytes": 1}

        with mock.patch.object(nh_loop, "scope_is_established", established):
            anchor, identity = nh_loop.current_package_anchor(events, [])
        self.assertEqual(anchor["package_scope_id"], "newer")
        self.assertEqual(identity["path"], "newer")


class BundleSevenRootRegression(unittest.TestCase):
    def baseline(self, selected_paths):
        packages = []
        for package_id, _title, _kind in nh_loop.BUNDLE_SEVEN_EXPECTED_PACKAGES:
            packages.append(
                {
                    "package_id": package_id,
                    "source_paths": (
                        list(selected_paths)
                        if package_id == "B30"
                        else ["%s.md" % package_id.lower().replace("-", "_")]
                    ),
                    "feature_inventory": [
                        {"feature_key": "%s.feature" % package_id.lower()}
                    ],
                }
            )
        return {"baseline_identity": "b" * 64, "package_inventory": packages}

    def test_shared_dependency_plan_is_root_not_alphabetical_authority_file(self):
        baseline = self.baseline(
            [
                "01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_3.md",
                nh_loop.BUNDLE_SEVEN_WORKFLOW_PATH,
                "01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md",
            ]
        )
        errors = []
        selection = nh_loop.bundle_seven_question_validation_selection(
            baseline, "B30", errors
        )
        self.assertEqual(errors, [])
        self.assertEqual(
            selection["scope_root_path"], nh_loop.BUNDLE_SEVEN_WORKFLOW_PATH
        )

    def test_question_selection_always_carries_current_authority_files(self):
        baseline = self.baseline([nh_loop.BUNDLE_SEVEN_WORKFLOW_PATH])
        baseline["source_paths_checked"] = list(
            nh_loop.BUNDLE_SEVEN_QUESTION_AUTHORITY_PATHS
        )
        errors = []
        selection = nh_loop.bundle_seven_question_validation_selection(
            baseline, "B30", errors
        )
        self.assertEqual(errors, [])
        self.assertTrue(
            set(nh_loop.BUNDLE_SEVEN_QUESTION_AUTHORITY_PATHS)
            <= set(selection["source_paths"])
        )

    def test_baseline_feature_discovery_need_not_read_separate_authority_files(self):
        baseline = self.baseline([nh_loop.BUNDLE_SEVEN_WORKFLOW_PATH])
        baseline["source_paths_checked"] = [nh_loop.BUNDLE_SEVEN_WORKFLOW_PATH]
        errors = []
        selection = nh_loop.bundle_seven_question_validation_selection(
            baseline, "B30", errors
        )
        self.assertEqual(errors, [])
        self.assertTrue(
            set(nh_loop.BUNDLE_SEVEN_QUESTION_AUTHORITY_PATHS)
            <= set(selection["source_paths"])
        )

    def test_shared_plan_is_root_when_package_local_sources_have_no_id_path(self):
        baseline = self.baseline(["01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md"])
        baseline["source_paths_checked"] = [nh_loop.BUNDLE_SEVEN_WORKFLOW_PATH]
        for package in baseline["package_inventory"]:
            if package["package_id"] == "A20":
                package["source_paths"] = [
                    "01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md"
                ]
        errors = []
        selection = nh_loop.bundle_seven_question_validation_selection(
            baseline, "A20", errors
        )
        self.assertEqual(errors, [])
        self.assertEqual(
            selection["scope_root_path"], nh_loop.BUNDLE_SEVEN_WORKFLOW_PATH
        )

    def test_ambiguous_source_list_without_shared_plan_refuses(self):
        baseline = self.baseline(["master.md", "defaults.md"])
        errors = []
        selection = nh_loop.bundle_seven_question_validation_selection(
            baseline, "B30", errors
        )
        self.assertIsNone(selection)
        self.assertTrue(any("no single controller-provable" in e for e in errors))


class RecoveryErrorPropagationRegression(unittest.TestCase):
    def test_unreadable_recorded_candidate_is_corrupt_not_in_transition(self):
        event = {
            "type": "validation_recorded",
            "package_scope_id": "scope-a",
            "event_seq": 1,
        }
        identity = {"path": "candidate", "sha256": "a" * 64, "bytes": 1}

        def unreadable(_facts, errors):
            errors.append("recorded candidate bytes do not match")
            return None, None

        errors = []
        with mock.patch.object(nh_loop, "authenticated_candidate_custody", return_value={}), \
             mock.patch.object(nh_loop, "validated_package_bound_candidate", return_value=identity), \
             mock.patch.object(nh_loop, "_supervisor_candidate_file", unreadable):
            scopes = nh_loop.nh_loop_established_scopes([event], errors)
        self.assertIsNone(scopes)
        self.assertIn("recorded candidate bytes do not match", errors)


class AuthenticatedUntrackedBaselineRegression(unittest.TestCase):
    def test_manifest_proved_untracked_path_is_admitted(self):
        events = [{
            "type": "validation_recorded",
            "package_scope_id": "scope-a",
            "event_seq": 1,
            "source_manifest_files": [
                {"path": "known.md", "sha256": "a" * 64, "bytes": 4}
            ],
        }]
        state = {"worktree_entries": ["?? known.md"]}
        live = {"path": "known.md", "sha256": "a" * 64, "bytes": 4}
        with mock.patch.object(nh_loop, "authenticated_candidate_custody", return_value={}), \
             mock.patch.object(nh_loop, "read_source_state", return_value=state), \
             mock.patch.object(nh_loop, "read_live_baseline_source_identity", return_value=live), \
             mock.patch.object(nh_loop, "validated_package_bound_candidate", return_value=None):
            allowed = nh_loop.authenticated_preexisting_candidate_paths(events, [])
        self.assertEqual(allowed, ("known.md",))

    def test_unknown_untracked_path_refuses_baseline(self):
        events = [{
            "type": "validation_recorded",
            "package_scope_id": "scope-a",
            "event_seq": 1,
            "source_manifest_files": [],
        }]
        state = {"worktree_entries": ["?? unknown.md"]}
        live = {"path": "unknown.md", "sha256": "b" * 64, "bytes": 4}
        errors = []
        with mock.patch.object(nh_loop, "authenticated_candidate_custody", return_value={}), \
             mock.patch.object(nh_loop, "read_source_state", return_value=state), \
             mock.patch.object(nh_loop, "read_live_baseline_source_identity", return_value=live), \
             mock.patch.object(nh_loop, "validated_package_bound_candidate", return_value=None):
            allowed = nh_loop.authenticated_preexisting_candidate_paths(events, errors)
        self.assertIsNone(allowed)
        self.assertTrue(any("no matching authenticated" in e for e in errors), errors)

    def test_bound_prover_reuses_the_exact_before_baseline_after_write(self):
        seen = []

        def boundary(_facts, *, allowed_preexisting_untracked_paths):
            seen.append(tuple(allowed_preexisting_untracked_paths))
            return []

        with mock.patch.object(
            nh_loop,
            "authenticated_preexisting_candidate_paths",
            return_value=("known.md",),
        ) as authenticate, mock.patch.object(
            nh_loop, "supervisor_write_boundary_prover", boundary
        ):
            prover = nh_loop.bound_supervisor_write_boundary_prover([], [])
            self.assertEqual(prover({"phase": "before", "candidate_path": "new.md"}), [])
            self.assertEqual(prover({"phase": "after", "candidate_path": "new.md"}), [])
        self.assertEqual(seen, [("known.md",), ("known.md",)])
        authenticate.assert_called_once()

    def test_recovery_after_excludes_only_its_pending_target(self):
        with mock.patch.object(
            nh_loop,
            "authenticated_preexisting_candidate_paths",
            return_value=("known.md",),
        ) as authenticate, mock.patch.object(
            nh_loop, "supervisor_write_boundary_prover", return_value=[]
        ):
            prover = nh_loop.bound_supervisor_write_boundary_prover([], [])
            self.assertEqual(prover({"phase": "after", "candidate_path": "pending.md"}), [])
        authenticate.assert_called_once_with(
            [], mock.ANY, excluded_paths=("pending.md",)
        )


class SupervisorInputRegression(unittest.TestCase):
    def test_invalid_supervisor_json_refuses_before_context_construction(self):
        emitted = []
        malformed = SimpleNamespace(buffer=io.BytesIO(b'{"broken":'))
        with mock.patch.object(nh_loop.sys, "stdin", malformed), \
             mock.patch.object(nh_loop, "build_supervisor_context") as build, \
             mock.patch.object(nh_loop, "emit", side_effect=lambda *args: emitted.append(args)):
            code = nh_loop.command_supervisor("supervisor-operation-status")
        self.assertEqual(code, nh_loop.EXIT_FAILED_CHECK)
        build.assert_not_called()
        self.assertTrue(
            any("not valid JSON" in e for e in emitted[0][0]["errors"]),
            emitted[0][0]["errors"],
        )

    def test_missing_supervisor_json_also_refuses_immediately(self):
        emitted = []
        missing = SimpleNamespace(buffer=io.BytesIO(b""))
        with mock.patch.object(nh_loop.sys, "stdin", missing), \
             mock.patch.object(nh_loop, "build_supervisor_context") as build, \
             mock.patch.object(nh_loop, "emit", side_effect=lambda *args: emitted.append(args)):
            code = nh_loop.command_supervisor("supervisor-operation-status")
        self.assertEqual(code, nh_loop.EXIT_FAILED_CHECK)
        build.assert_not_called()
        self.assertTrue(any("nothing was supplied" in e for e in emitted[0][0]["errors"]))


class StatusExitRegression(unittest.TestCase):
    def test_missing_repository_returns_failure_exit(self):
        with mock.patch.object(nh_loop, "NH_REPO_PATH", "/definitely/not/present"), \
             mock.patch.object(nh_loop, "emit"):
            code = nh_loop.command_status()
        self.assertEqual(code, nh_loop.EXIT_FAILED_CHECK)


if __name__ == "__main__":
    unittest.main()

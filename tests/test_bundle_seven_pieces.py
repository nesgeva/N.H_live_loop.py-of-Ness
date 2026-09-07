"""Bundle Seven baseline in pieces (Ness, 2026-09-02).

Under the Claude second-model form the whole-bundle baseline is produced as
eleven per-package reviews plus one relationships review, stitched by the
controller into the ONE payload validate_bundle_seven_payload() already checks.
The Codex form keeps its single call.
"""
import json
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
import tempfile  # noqa: E402

# Never let these tests write into the controller's persistent folders.
_SCRATCH = tempfile.TemporaryDirectory(prefix="nh_pieces_tests_")
_PATCHES = (
    mock.patch.object(nh_loop, "SECOND_MODEL_REPLY_CAPTURE_DIR", _SCRATCH.name + "/replies"),
    mock.patch.object(nh_loop, "CODEX_REVIEW_CHECKPOINT_ROOT", _SCRATCH.name + "/checkpoints"),
    mock.patch.object(nh_loop, "live_progress_log_path", lambda: _SCRATCH.name + "/diary.log"),
)


def setUpModule():
    for patch in _PATCHES:
        patch.start()


def tearDownModule():
    for patch in _PATCHES:
        patch.stop()
    _SCRATCH.cleanup()

PACKAGE_IDS = [item[0] for item in nh_loop.BUNDLE_SEVEN_EXPECTED_PACKAGES]
PATHS = ["05_ACTIVE_CANDIDATE/X_v1_0_CANDIDATE.md", "01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md"]


def package_piece(package_id, complete=True, unknowns=()):
    return json.dumps({
        "schema_version": nh_loop.BUNDLE_SEVEN_REVIEW_SCHEMA_VERSION,
        "bundle_id": nh_loop.BUNDLE_SEVEN_ID,
        "review_complete": complete,
        "packages": [{"package_id": package_id, "package_title": "t", "work_kind": "policy",
                      "current_state_summary": "s", "feature_inventory": [], "connected_package_ids": [],
                      "source_paths": PATHS[:1]}],
        "cross_package_relationships": [],
        "unknowns": list(unknowns),
    }, separators=(",", ":"))


def relationships_piece(complete=True):
    return json.dumps({
        "schema_version": nh_loop.BUNDLE_SEVEN_REVIEW_SCHEMA_VERSION,
        "bundle_id": nh_loop.BUNDLE_SEVEN_ID,
        "review_complete": complete,
        "cross_package_relationships": [{"relationship_key": "r1", "affected_package_ids": PACKAGE_IDS[:2],
                                         "summary": "x", "status": "open", "source_paths": PATHS[:1]}],
        "unknowns": [],
    }, separators=(",", ":"))


class Prompts(unittest.TestCase):
    def test_whole_bundle_prompt_is_unchanged_by_default(self):
        text = nh_loop.bundle_seven_prompt(PATHS, None)
        self.assertIn("packages must contain exactly one object for every required package", text)
        self.assertIn("Review all Bundle Seven policy and mechanical packages together", text)

    def test_per_package_prompt_scopes_to_one_package(self):
        text = nh_loop.bundle_seven_prompt(PATHS, None, only_package_id="A19")
        self.assertIn("ONLY package A19", text)
        self.assertIn("packages must contain exactly one object, for package A19 only", text)
        self.assertNotIn("for every required package", text)
        self.assertIn("cross_package_relationships must be an empty array", text)
        for pid in PACKAGE_IDS:
            self.assertIn(pid, text)  # the other nine stay listed as context

    def test_prompt_states_the_partial_decision_rule_on_both_forms(self):
        # Attempts 4 and 5 (2026-09-02/03): the checker wrote "partial" with only one side
        # ten times.  The prompt must say what to do when only one side exists.
        for text in (nh_loop.bundle_seven_prompt(PATHS, None), nh_loop.bundle_seven_prompt(PATHS, None, only_package_id="A19")):
            self.assertIn("Use partial ONLY when you can list at least one decided aspect AND at least one open aspect", text)
            self.assertIn("If you can list only decided text, the status is settled", text)
            self.assertIn("if you can list only open text, the status is open", text)

    def test_relationships_prompt_carries_the_compact_inventories(self):
        inventories = [json.loads(package_piece(p))["packages"][0] for p in PACKAGE_IDS]
        text = nh_loop.bundle_seven_relationships_prompt(PATHS, inventories)
        self.assertIn("cross_package_relationships", text)
        self.assertIn(json.dumps(inventories, ensure_ascii=False, sort_keys=True)[:60], text)
        self.assertIn("Do not return packages", text)


class Assembly(unittest.TestCase):
    def test_eleven_good_pieces_become_one_payload_in_plan_order(self):
        errors = []
        text = nh_loop.assemble_bundle_seven_pieces(
            {p: package_piece(p) for p in PACKAGE_IDS}, relationships_piece(), errors
        )
        self.assertEqual(errors, [])
        payload = json.loads(text)
        self.assertEqual([p["package_id"] for p in payload["packages"]], PACKAGE_IDS)
        self.assertEqual(payload["schema_version"], nh_loop.BUNDLE_SEVEN_REVIEW_SCHEMA_VERSION)
        self.assertEqual(payload["bundle_id"], nh_loop.BUNDLE_SEVEN_ID)
        self.assertIs(payload["review_complete"], True)
        self.assertEqual(len(payload["cross_package_relationships"]), 1)
        self.assertEqual(payload["unknowns"], [])
        self.assertNotIn("source_paths_checked", payload)

    def test_incomplete_piece_or_unknowns_propagate(self):
        pieces = {p: package_piece(p) for p in PACKAGE_IDS}
        pieces["A19"] = package_piece("A19", complete=False, unknowns=["a19 unresolved"])
        errors = []
        payload = json.loads(nh_loop.assemble_bundle_seven_pieces(pieces, relationships_piece(), errors))
        self.assertIs(payload["review_complete"], False)
        self.assertEqual(payload["unknowns"], ["a19 unresolved"])

    def test_wrong_or_missing_package_refuses(self):
        pieces = {p: package_piece(p) for p in PACKAGE_IDS}
        pieces["A19"] = package_piece("A20")
        errors = []
        self.assertIsNone(nh_loop.assemble_bundle_seven_pieces(pieces, relationships_piece(), errors))
        self.assertTrue(errors)
        pieces = {p: package_piece(p) for p in PACKAGE_IDS[:-1]}
        errors = []
        self.assertIsNone(nh_loop.assemble_bundle_seven_pieces(pieces, relationships_piece(), errors))
        self.assertTrue(errors)

    def test_non_json_piece_refuses(self):
        pieces = {p: package_piece(p) for p in PACKAGE_IDS}
        pieces["B30"] = "not json"
        errors = []
        self.assertIsNone(nh_loop.assemble_bundle_seven_pieces(pieces, relationships_piece(), errors))
        self.assertTrue(errors)


class RunInPieces(unittest.TestCase):
    def fake_launcher(self, replies, fail_on=None):
        calls = []

        def launcher(prompt, errors, checkpoint=None, output_schema=None):
            index = len(calls)
            calls.append(prompt)
            if fail_on is not None and index == fail_on:
                errors.append("claude exited with code 1")
                return True, 1, ""
            return True, 0, replies[index]
        return launcher, calls

    def envelope(self, text):
        return json.dumps({"type": "result", "subtype": "success", "is_error": False, "result": text})

    def test_eleven_calls_in_order_then_one_assembled_message(self):
        replies = [self.envelope(package_piece(p)) for p in PACKAGE_IDS] + [self.envelope(relationships_piece())]
        launcher, calls = self.fake_launcher(replies)
        errors = []
        with mock.patch.object(nh_loop, "SECOND_MODEL_PROVIDER", "claude"):
            invoked, code, message, count = nh_loop.run_bundle_seven_baseline_in_pieces(PATHS, None, errors, launcher=launcher)
        total = len(PACKAGE_IDS) + 1
        self.assertTrue(invoked); self.assertEqual(code, 0); self.assertEqual(count, total)
        self.assertEqual(errors, [])
        for pid, prompt in zip(PACKAGE_IDS, calls[:len(PACKAGE_IDS)]):
            self.assertIn("ONLY package %s" % pid, prompt)
        self.assertIn("Do not return packages", calls[len(PACKAGE_IDS)])
        self.assertEqual([p["package_id"] for p in json.loads(message)["packages"]], PACKAGE_IDS)

    def test_a_failed_piece_stops_early_and_yields_no_message(self):
        replies = [self.envelope(package_piece(p)) for p in PACKAGE_IDS] + [self.envelope(relationships_piece())]
        launcher, calls = self.fake_launcher(replies, fail_on=3)
        errors = []
        with mock.patch.object(nh_loop, "SECOND_MODEL_PROVIDER", "claude"):
            invoked, code, message, count = nh_loop.run_bundle_seven_baseline_in_pieces(PATHS, None, errors, launcher=launcher)
        self.assertTrue(invoked); self.assertEqual(code, 1); self.assertIsNone(message)
        self.assertEqual(count, 4); self.assertEqual(len(calls), 4)
        self.assertTrue(any("exited with code 1" in e for e in errors))


class CommandWiring(unittest.TestCase):
    def test_command_uses_pieces_only_on_the_claude_form(self):
        source = open(nh_loop.__file__, encoding="utf-8").read()
        start = source.index("def command_bundle_seven_baseline(")
        body = source[start:source.index("\ndef ", start + 10)]
        self.assertIn('if second_model_executable() == "claude":', body)
        self.assertIn("run_bundle_seven_baseline_in_pieces(", body)
        self.assertIn("run_codex_question_validation(", body)


class Progress(unittest.TestCase):
    def test_each_finished_piece_is_reported_with_its_reply(self):
        seen = []
        replies = [json.dumps({"type": "result", "subtype": "success", "is_error": False, "result": package_piece(p)}) for p in PACKAGE_IDS]
        replies.append(json.dumps({"type": "result", "subtype": "success", "is_error": False, "result": relationships_piece()}))
        calls = []

        def launcher(prompt, errors, checkpoint=None, output_schema=None):
            calls.append(prompt); return True, 0, replies[len(calls) - 1]

        with mock.patch.object(nh_loop, "SECOND_MODEL_PROVIDER", "claude"):
            nh_loop.run_bundle_seven_baseline_in_pieces(PATHS, None, [], launcher=launcher,
                                                        progress=lambda *a: seen.append(a))
        self.assertEqual([s[0] for s in seen], PACKAGE_IDS + ["relationships"])
        total = len(PACKAGE_IDS) + 1
        self.assertEqual([s[1] for s in seen], list(range(1, total + 1)))
        self.assertTrue(all(s[2] == total for s in seen))
        self.assertEqual(json.loads(seen[0][4])["packages"][0]["package_id"], PACKAGE_IDS[0])

    def test_default_progress_prints_and_saves(self):
        import io, os, tempfile
        with tempfile.TemporaryDirectory() as folder, mock.patch.object(
            nh_loop, "SECOND_MODEL_REPLY_CAPTURE_DIR", folder
        ), mock.patch("sys.stderr", new_callable=io.StringIO) as err:
            nh_loop.bundle_seven_piece_progress("A19", 2, 11, 42, "{}")
            files = os.listdir(folder)
        self.assertEqual(len(files), 1); self.assertTrue(files[0].startswith("piece-02-A19-"))
        self.assertIn("piece 2/11 done (A19) in 42s", err.getvalue())


class ShapeEnforcement(unittest.TestCase):
    def envelope(self, text):
        return json.dumps({"type": "result", "subtype": "success", "is_error": False, "result": text})

    def test_each_piece_call_carries_its_typed_schema(self):
        schemas = []
        replies = [self.envelope(package_piece(p)) for p in PACKAGE_IDS] + [self.envelope(relationships_piece())]

        def launcher(prompt, errors, checkpoint=None, output_schema=None):
            schemas.append(output_schema); return True, 0, replies[len(schemas) - 1]

        with mock.patch.object(nh_loop, "SECOND_MODEL_PROVIDER", "claude"):
            nh_loop.run_bundle_seven_baseline_in_pieces(PATHS, None, [], launcher=launcher, progress=lambda *a: None)
        self.assertEqual(len(schemas), len(PACKAGE_IDS) + 1)
        self.assertTrue(all(
            s is nh_loop.BUNDLE_SEVEN_PACKAGE_PIECE_SCHEMA
            for s in schemas[:len(PACKAGE_IDS)]
        ))
        self.assertIs(
            schemas[len(PACKAGE_IDS)],
            nh_loop.BUNDLE_SEVEN_RELATIONSHIPS_PIECE_SCHEMA,
        )
        pkg = nh_loop.BUNDLE_SEVEN_PACKAGE_PIECE_SCHEMA["properties"]["packages"]
        self.assertEqual((pkg["type"], pkg["minItems"], pkg["maxItems"]), ("array", 1, 1))

    def test_a_malformed_first_piece_fails_at_once(self):
        bad = json.dumps({"schema_version": nh_loop.BUNDLE_SEVEN_REVIEW_SCHEMA_VERSION, "bundle_id": nh_loop.BUNDLE_SEVEN_ID,
                          "review_complete": True, "packages": "[{\"package_id\": \"A17\"}]",
                          "cross_package_relationships": [], "unknowns": []})
        calls = []

        def launcher(prompt, errors, checkpoint=None, output_schema=None):
            calls.append(prompt); return True, 0, self.envelope(bad)

        errors = []
        with mock.patch.object(nh_loop, "SECOND_MODEL_PROVIDER", "claude"):
            invoked, code, message, count = nh_loop.run_bundle_seven_baseline_in_pieces(PATHS, None, errors, launcher=launcher, progress=lambda *a: None)
        self.assertIsNone(message); self.assertEqual(count, 1); self.assertEqual(len(calls), 1)
        self.assertTrue(any("packages array" in e for e in errors), errors)

    @staticmethod
    def feature_with_partials(sides):
        """One compact feature. sides maps dimension kind -> "both" | "decided" | "open";
        every other dimension is not_applicable with one reason."""
        kinds = nh_loop.BUNDLE_SEVEN_DIMENSION_KINDS
        return {
            "feature_key": "chat_presence_in_world", "feature_name": "n", "feature_summary": "s",
            "source_paths": PATHS[:1],
            "dimension_statuses": {k: ("partial" if k in sides else "not_applicable") for k in kinds},
            "decided_aspects": [{"dimension_kind": k, "text": "decided part"} for k, side in sides.items() if side in ("both", "decided")],
            "open_aspects": [{"dimension_kind": k, "text": "open part"} for k, side in sides.items() if side in ("both", "open")],
            "mechanical_or_not_applicable_reasons": [{"dimension_kind": k, "reason": "r"} for k in kinds if k not in sides],
        }

    @classmethod
    def feature_with_one_partial_dimension(cls, consistent):
        return cls.feature_with_partials({"cross_feature_relationships": "both" if consistent else "decided"})

    def run_with_first_piece_feature(self, feature):
        first = json.loads(package_piece(PACKAGE_IDS[0]))
        first["packages"][0]["feature_inventory"] = [feature]
        replies = [self.envelope(json.dumps(first, separators=(",", ":")))]
        replies += [self.envelope(package_piece(p)) for p in PACKAGE_IDS[1:]] + [self.envelope(relationships_piece())]
        calls = []

        def launcher(prompt, errors, checkpoint=None, output_schema=None):
            calls.append(prompt); return True, 0, replies[len(calls) - 1]

        errors = []
        with mock.patch.object(nh_loop, "SECOND_MODEL_PROVIDER", "claude"):
            invoked, code, message, count = nh_loop.run_bundle_seven_baseline_in_pieces(PATHS, None, errors, launcher=launcher, progress=lambda *a: None)
        return message, count, errors

    # Ness, 2026-09-03 00:45: "1 slip is a stupid overly strict rule. fix it to have 2-3 slips
    # allowed."  A slip is "partial" with only one side.  Up to BUNDLE_SEVEN_PARTIAL_SLIP_CAP
    # slips per package piece are relabeled by the rule the prompt states (decided-only ->
    # settled, open-only -> open) and recorded; one more refuses the piece at arrival.
    KINDS = nh_loop.BUNDLE_SEVEN_DIMENSION_KINDS

    def test_the_slip_cap_is_three_per_package(self):
        self.assertEqual(nh_loop.BUNDLE_SEVEN_PARTIAL_SLIP_CAP, 3)

    def test_up_to_three_one_sided_partials_are_relabeled_and_recorded(self):
        feature = self.feature_with_partials({self.KINDS[0]: "decided", self.KINDS[1]: "open", self.KINDS[2]: "decided", self.KINDS[3]: "both"})
        slips = []
        parsed, problem = nh_loop.compact_bundle_seven_feature_errors(feature, "A17", slips=slips)
        self.assertIsNone(problem)
        statuses = parsed[1]
        self.assertEqual((statuses[self.KINDS[0]], statuses[self.KINDS[1]], statuses[self.KINDS[2]], statuses[self.KINDS[3]]),
                         ("settled", "open", "settled", "partial"))
        self.assertEqual([(s["dimension_kind"], s["relabeled_to"]) for s in slips],
                         [(self.KINDS[0], "settled"), (self.KINDS[1], "open"), (self.KINDS[2], "settled")])
        self.assertTrue(all(s["package_id"] == "A17" and s["feature_key"] == "chat_presence_in_world" for s in slips))
        message, count, errors = self.run_with_first_piece_feature(feature)
        self.assertEqual(errors, []); self.assertEqual(
            count, len(PACKAGE_IDS) + 1
        ); self.assertIsNotNone(message)

    def test_a_fourth_one_sided_partial_in_one_package_is_refused_at_arrival(self):
        feature = self.feature_with_partials({k: "decided" for k in self.KINDS[:4]})
        message, count, errors = self.run_with_first_piece_feature(feature)
        self.assertIsNone(message)
        self.assertEqual(count, 1, "the over-cap first piece must stop the run before any later paid call")
        joined = " | ".join(errors)
        for name in ("4 one-sided partial", "at most 3", PACKAGE_IDS[0]):
            self.assertIn(name, joined, errors)

    def test_slips_are_counted_per_package_across_its_features(self):
        first = json.loads(package_piece(PACKAGE_IDS[0]))
        two = self.feature_with_partials({self.KINDS[0]: "open", self.KINDS[1]: "open"})
        other = dict(two, feature_key="second_feature")
        first["packages"][0]["feature_inventory"] = [two, other]  # 2 + 2 = 4 slips in one package
        slips = []
        piece, problem = nh_loop.bundle_seven_piece_shape_errors(json.dumps(first), PACKAGE_IDS[0], slips=slips)
        self.assertIsNone(piece); self.assertIn("4 one-sided partial", problem)

    def test_relabeled_dimensions_are_marked_in_the_expanded_baseline(self):
        feature = self.feature_with_partials({self.KINDS[0]: "open"})
        payload = json.loads(package_piece(PACKAGE_IDS[0]))
        payload["packages"][0]["feature_inventory"] = [feature]
        errors = []
        expanded = nh_loop.normalize_compact_bundle_seven_payload(payload, PATHS, errors)
        self.assertEqual(errors, [])
        dims = expanded["packages"][0]["feature_inventory"][0]["decision_dimensions"]
        relabeled = [d for d in dims if d["dimension_kind"] == self.KINDS[0]]
        self.assertEqual(len(relabeled), 1)
        self.assertEqual(relabeled[0]["status"], "open")
        self.assertIn("relabeled", relabeled[0]["summary"])
        self.assertIn("partial", relabeled[0]["summary"])

    def test_a_consistent_partial_dimension_passes_arrival(self):
        message, count, errors = self.run_with_first_piece_feature(self.feature_with_one_partial_dimension(consistent=True))
        self.assertEqual(errors, [])
        self.assertEqual(count, len(PACKAGE_IDS) + 1)
        self.assertIsNotNone(message)

    def test_launcher_accepts_a_schema_on_both_forms(self):
        record = []

        def run(argv, **kwargs):
            record.append(list(argv)); return SimpleNamespace(returncode=0, stdout=b"", stderr=b"")

        with mock.patch.object(nh_loop, "SECOND_MODEL_PROVIDER", "claude"), mock.patch.object(nh_loop.subprocess, "run", run):
            nh_loop.run_codex_question_validation("p", [], output_schema={"type": "object"})
        self.assertIn("--json-schema", record[-1])
        with mock.patch.object(nh_loop, "SECOND_MODEL_PROVIDER", "codex"), mock.patch.object(nh_loop.subprocess, "run", run):
            nh_loop.run_codex_question_validation("p", [], output_schema={"type": "object"})
        argv = record[-1]; self.assertIn("--output-schema", argv)
        import os
        self.assertFalse(os.path.exists(argv[argv.index("--output-schema") + 1]), "codex temp schema file is removed after the run")


class ResumableSavedPieces(unittest.TestCase):
    def envelope(self, text):
        return json.dumps({"type": "result", "subtype": "success", "is_error": False, "result": text})

    def replies(self):
        return [self.envelope(package_piece(p)) for p in PACKAGE_IDS] + [self.envelope(relationships_piece())]

    def make_launcher(self, replies, fail_at=None):
        """Replies are chosen by WHICH piece the prompt asks for, not by call order."""
        calls = []

        def launcher(prompt, errors, checkpoint=None, output_schema=None):
            index = len(calls); calls.append(prompt)
            if fail_at is not None and index == fail_at:
                errors.append("claude exited with code 1"); return True, 1, ""
            for position, pid in enumerate(PACKAGE_IDS):
                if "ONLY package %s" % pid in prompt:
                    return True, 0, replies[position]
            return True, 0, replies[len(PACKAGE_IDS)]
        return launcher, calls

    def run_once(self, root, launcher):
        errors = []
        with mock.patch.object(nh_loop, "SECOND_MODEL_PROVIDER", "claude"), mock.patch.object(
            nh_loop, "CODEX_REVIEW_CHECKPOINT_ROOT", root
        ):
            return nh_loop.run_bundle_seven_baseline_in_pieces(
                PATHS, None, errors, launcher=launcher, progress=lambda *a: None, cache_binding="b" * 64
            ) + (errors,)

    def test_every_finished_piece_is_saved_immediately_and_reused_next_time(self):
        import os, tempfile
        with tempfile.TemporaryDirectory() as root:
            launcher, calls = self.make_launcher(self.replies())
            invoked, code, message, count, errors = self.run_once(root, launcher)
            total = len(PACKAGE_IDS) + 1
            self.assertEqual((code, count), (0, total)); self.assertIsNotNone(message)
            with mock.patch.object(nh_loop, "CODEX_REVIEW_CHECKPOINT_ROOT", root):
                folder = nh_loop.bundle_seven_piece_cache_dir("b" * 64)
            self.assertTrue(folder.startswith(root))
            saved = sorted(os.listdir(folder))
            self.assertEqual(len(saved), total); self.assertIn("relationships.json", saved)
            self.assertEqual(oct(os.stat(os.path.join(folder, saved[0])).st_mode & 0o777), "0o600")
            launcher2, calls2 = self.make_launcher(self.replies())
            invoked, code, message2, count2, errors = self.run_once(root, launcher2)
            self.assertEqual((code, count2, len(calls2)), (0, 0, 0), "a rerun with nothing changed makes no provider call")
            self.assertEqual(message2, message)

    def test_a_failed_run_keeps_its_good_pieces_and_the_rerun_only_redoes_the_rest(self):
        import tempfile
        with tempfile.TemporaryDirectory() as root:
            launcher, calls = self.make_launcher(self.replies(), fail_at=6)
            invoked, code, message, count, errors = self.run_once(root, launcher)
            self.assertIsNone(message); self.assertEqual(count, 7)
            launcher2, calls2 = self.make_launcher(self.replies())
            invoked, code, message2, count2, errors = self.run_once(root, launcher2)
            self.assertIsNotNone(message2); self.assertEqual(
                count2, len(PACKAGE_IDS) + 1 - 6,
                "six saved pieces reused; the remaining pieces were made",
            )

    def test_a_different_source_binding_or_prompt_is_never_reused(self):
        import tempfile
        with tempfile.TemporaryDirectory() as root:
            launcher, calls = self.make_launcher(self.replies())
            self.run_once(root, launcher)
            other = []
            with mock.patch.object(nh_loop, "SECOND_MODEL_PROVIDER", "claude"), mock.patch.object(nh_loop, "CODEX_REVIEW_CHECKPOINT_ROOT", root):
                launcher2, calls2 = self.make_launcher(self.replies())
                nh_loop.run_bundle_seven_baseline_in_pieces(PATHS, None, other, launcher=launcher2, progress=lambda *a: None, cache_binding="c" * 64)
            self.assertEqual(
                len(calls2), len(PACKAGE_IDS) + 1,
                "another binding starts from zero",
            )
            with mock.patch.object(nh_loop, "SECOND_MODEL_PROVIDER", "claude"), mock.patch.object(nh_loop, "CODEX_REVIEW_CHECKPOINT_ROOT", root):
                launcher3, calls3 = self.make_launcher(self.replies())
                nh_loop.run_bundle_seven_baseline_in_pieces(PATHS + ["extra.md"], None, [], launcher=launcher3, progress=lambda *a: None, cache_binding="b" * 64)
            self.assertEqual(
                len(calls3), len(PACKAGE_IDS) + 1,
                "a changed prompt starts from zero",
            )

    def test_a_malformed_saved_piece_is_ignored_not_trusted(self):
        import os, tempfile
        with tempfile.TemporaryDirectory() as root:
            with mock.patch.object(nh_loop, "CODEX_REVIEW_CHECKPOINT_ROOT", root):
                d = nh_loop.bundle_seven_piece_cache_dir("b" * 64); os.makedirs(d)
                open(os.path.join(d, "A17.json"), "w").write("garbage")
            launcher, calls = self.make_launcher(self.replies())
            invoked, code, message, count, errors = self.run_once(root, launcher)
            self.assertEqual(count, len(PACKAGE_IDS) + 1); self.assertIsNotNone(message)

    def test_command_passes_the_source_binding_as_the_cache_key(self):
        source = open(nh_loop.__file__, encoding="utf-8").read()
        start = source.index("def command_bundle_seven_baseline(")
        body = source[start:source.index("\ndef ", start + 10)]
        self.assertIn('cache_binding=before["binding_sha256"]', body)


if __name__ == "__main__":
    unittest.main()

class DeclaredCaveats(unittest.TestCase):
    """Ness, 2026-09-03 01:30 ("yes accept caveats"): a checker that declares its review
    complete may list things it could not verify; they are recorded as caveats, not refused.
    An incomplete review is still refused."""

    def stitched(self, complete=True, unknowns=()):
        pieces = {p: package_piece(p) for p in PACKAGE_IDS}
        rel = json.loads(relationships_piece(complete=complete)); rel["unknowns"] = list(unknowns)
        errors = []
        text = nh_loop.assemble_bundle_seven_pieces(pieces, json.dumps(rel, separators=(",", ":")), errors)
        self.assertEqual(errors, []); return text

    # The accepted-with-caveats case needs the full durable fixture: see
    # tests/test_live_loop_stabilization.py::test_bundle_seven_complete_review_with_caveats_is_accepted_and_recorded

    def test_an_incomplete_review_is_still_refused(self):
        errors = []
        payload = nh_loop.validate_bundle_seven_payload(self.stitched(complete=False, unknowns=["x"]), PATHS, errors)
        self.assertIsNone(payload)
        self.assertTrue(any("did not declare itself complete" in e for e in errors), errors)

    def test_malformed_or_excessive_caveats_are_refused(self):
        for bad in ([{"not": "a string"}], ["ok", 5], ["x" * 2001], ["c%d" % i for i in range(nh_loop.BUNDLE_SEVEN_MAX_CAVEATS + 1)]):
            errors = []
            self.assertIsNone(nh_loop.validate_bundle_seven_payload(self.stitched(unknowns=bad), PATHS, errors), bad)
            self.assertTrue(any("caveat" in e for e in errors), errors)

class ScopeAwareCoverageTarget(unittest.TestCase):
    """Ness, 2026-09-03 (design section 1, "accepted"): when the batch names a package, the
    coverage review challenges THAT package's latest complete validation set, not the
    global latest.  Without a named package the old behaviour is unchanged."""

    def state(self):
        sets = {
            "vs_b30": {"validation_set_id": "vs_b30", "package_scope_id": "B30", "complete": True},
            "vs_a21_old": {"validation_set_id": "vs_a21_old", "package_scope_id": "A21", "complete": True},
            "vs_a21": {"validation_set_id": "vs_a21", "package_scope_id": "A21", "complete": True},
            "vs_a19": {"validation_set_id": "vs_a19", "package_scope_id": "A19", "complete": False},
        }
        return {"validation_sets": sets, "validation_set_order": ["vs_a21_old", "vs_b30", "vs_a19", "vs_a21"],
                "latest_complete_validation_set": sets["vs_a21"]}

    def test_a_named_package_gets_its_own_latest_complete_set(self):
        self.assertEqual(nh_loop.coverage_target_validation_set(self.state(), "B30")["validation_set_id"], "vs_b30")
        self.assertEqual(nh_loop.coverage_target_validation_set(self.state(), "A21")["validation_set_id"], "vs_a21")

    def test_no_named_package_keeps_the_global_latest(self):
        self.assertEqual(nh_loop.coverage_target_validation_set(self.state(), None)["validation_set_id"], "vs_a21")

    def test_a_package_without_a_complete_set_yields_none(self):
        self.assertIsNone(nh_loop.coverage_target_validation_set(self.state(), "A19"))
        self.assertIsNone(nh_loop.coverage_target_validation_set(self.state(), "B29"))

    def test_the_coverage_command_uses_the_named_package(self):
        import inspect
        src = inspect.getsource(nh_loop.command_question_coverage_review)
        self.assertIn("coverage_target_validation_set(", src)

class PartialMerge(unittest.TestCase):
    """Ness, 2026-09-03 (design section 2, "accepted. do it"): the merged inventory may hold
    fewer than ten packages, records which, and questions of those packages are deliverable;
    a skipped package rejoins in a later merge."""

    PLAN = {"baseline_identity": "bl1", "package_count": 3, "feature_count": 5,
            "packages": [{"package_id": "A17", "feature_keys": ["f1", "f2"]},
                         {"package_id": "A19", "feature_keys": ["f3"]},
                         {"package_id": "B30", "feature_keys": ["f4", "f5"]}]}

    def result(self, pid, keys, qs):
        return {"package_id": pid, "baseline_identity": "bl1", "enumeration_complete": True,
                "feature_keys_checked": keys, "questions": [{"question_id": q} for q in qs]}

    def test_a_subset_of_packages_merges_and_records_its_membership(self):
        errors = []
        merged = nh_loop.merge_bundle_seven_question_validation_results(
            self.PLAN, [self.result("B30", ["f4", "f5"], ["q1", "q2"])], errors)
        self.assertEqual(errors, [])
        self.assertEqual(merged["package_count"], 1)
        self.assertEqual(merged["package_ids"], ["B30"])
        self.assertEqual(merged["feature_count"], 2)
        self.assertEqual([q["question_id"] for q in merged["questions"]], ["q1", "q2"])

    def test_no_package_at_all_does_not_merge(self):
        errors = []
        self.assertIsNone(nh_loop.merge_bundle_seven_question_validation_results(self.PLAN, [], errors))
        self.assertTrue(errors)

    def test_replay_membership_rule_accepts_a_subset_and_refuses_junk(self):
        expected = ["A17", "A19", "B30"]
        sets = {"vs_b30": {"package_scope_id": "B30", "complete": True, "enumeration": {"complete": True}},
                "vs_a19": {"package_scope_id": "A19", "complete": False, "enumeration": {"complete": False}}}
        features = {"A17": {"f1", "f2"}, "A19": {"f3"}, "B30": {"f4", "f5"}}
        good = {"package_validation_set_ids": {"B30": "vs_b30"}, "package_feature_keys_checked": {"B30": ["f4", "f5"]},
                "package_count": 1, "feature_count": 2}
        self.assertIsNone(nh_loop.bundle_seven_merge_membership_error(good, expected, sets, features))
        incomplete = dict(good, package_validation_set_ids={"A19": "vs_a19"}, package_feature_keys_checked={"A19": ["f3"]}, feature_count=1)
        self.assertIn("incomplete", nh_loop.bundle_seven_merge_membership_error(incomplete, expected, sets, features))
        empty = dict(good, package_validation_set_ids={}, package_feature_keys_checked={}, package_count=0, feature_count=0)
        self.assertIsNotNone(nh_loop.bundle_seven_merge_membership_error(empty, expected, sets, features))
        stranger = dict(good, package_validation_set_ids={"ZZ": "vs_b30"}, package_feature_keys_checked={"ZZ": ["f4", "f5"]})
        self.assertIsNotNone(nh_loop.bundle_seven_merge_membership_error(stranger, expected, sets, features))
        wrong_count = dict(good, package_count=3)
        self.assertIn("counts", nh_loop.bundle_seven_merge_membership_error(wrong_count, expected, sets, features))

    def test_delivery_withholds_only_packages_outside_the_merge(self):
        bundle = {item[0] for item in nh_loop.BUNDLE_SEVEN_EXPECTED_PACKAGES}
        held = nh_loop.bundle_seven_packages_withheld_from_delivery({"package_validation_set_ids": {"B30": "vs_b30", "A17": "vs_a17"}})
        self.assertEqual(held, bundle - {"B30", "A17"})
        self.assertEqual(nh_loop.bundle_seven_packages_withheld_from_delivery(None), bundle)

    def test_the_batch_end_and_the_replay_use_the_shared_rules(self):
        import inspect
        self.assertIn("bundle_seven_merge_membership_error(", inspect.getsource(nh_loop.replay_interview_state))
        self.assertIn("bundle_seven_skipped_packages", inspect.getsource(nh_loop.command_bundle_seven_question_validation))

class OnlyOnePackage(unittest.TestCase):
    """Ness, 2026-09-03 ("rerun only 1 package ... i want to see that it works"): the batch
    can be limited to named packages so one cheap run proves the path before an hours-long
    one.  It only NARROWS the planned order; it invents nothing."""

    ORDER = ["A17", "A19", "B30"]

    def test_no_request_keeps_the_whole_order(self):
        errors = []
        self.assertEqual(nh_loop.bundle_seven_selected_package_order(self.ORDER, None, errors), self.ORDER)
        self.assertEqual(nh_loop.bundle_seven_selected_package_order(self.ORDER, "  ", errors), self.ORDER)
        self.assertEqual(errors, [])

    def test_named_packages_narrow_the_order_and_keep_plan_order(self):
        errors = []
        self.assertEqual(nh_loop.bundle_seven_selected_package_order(self.ORDER, "B30", errors), ["B30"])
        self.assertEqual(nh_loop.bundle_seven_selected_package_order(self.ORDER, "B30, A17", errors), ["A17", "B30"])
        self.assertEqual(errors, [])

    def test_an_unplanned_package_is_refused(self):
        errors = []
        self.assertIsNone(nh_loop.bundle_seven_selected_package_order(self.ORDER, "B30,NOPE", errors))
        self.assertTrue(any("NOPE" in item for item in errors), errors)

    def test_the_command_reads_the_limit(self):
        import inspect
        self.assertIn("bundle_seven_selected_package_order(", inspect.getsource(nh_loop.command_bundle_seven_question_validation))
        self.assertEqual(nh_loop.BUNDLE_SEVEN_ONLY_ENV, "NH_BUNDLE_SEVEN_ONLY")

class ContextRebuiltBeforeDispatch(unittest.TestCase):
    """B30, run 8 (2026-09-03 23:06): the batch built its supervisor context ONCE, then
    reconciled a stranded request (three appended events), then dispatched from that STALE
    context.  The work-item identity embeds the authenticated standing chain, so the
    recorded work item could not be re-derived when the result came back:
    "the custodied result names a work item this replay cannot re-derive".
    Any append before a dispatch must be followed by a rebuild."""

    def test_the_context_is_rebuilt_after_a_reconcile_and_before_the_dispatch(self):
        built = []
        order = []

        class Journal:
            def read(self):
                return []

        class Ctx:
            transition_facts = {"scope_has_validation": True}
            journal = Journal()
            provider = object()

        def build_ctx(selection, state, errors, control_context=None):
            built.append(state)
            return Ctx()

        class Scoped:
            def unconsumed_piece3_authorization(self, _kind):
                return None
            def custodied_results_awaiting_processing(self):
                return []
            def open_provider_requests(self):
                return [{"provider_request_identity": "pr_open"}] if len(order) == 0 else []

        def reconcile(_context):
            order.append("reconcile")
            return SimpleNamespace(report={"ok": True})

        def dispatch(_context, _selection):
            order.append("dispatch")
            raise nh_loop.nh_supervisor.engine.SupervisorRefusal("stop here")

        errors = []
        with (
            mock.patch.object(
                nh_loop,
                "load_interview_for_command",
                side_effect=lambda *a, **k: {"_events": []},
            ),
            mock.patch.object(nh_loop, "build_supervisor_context", return_value=object()),
            mock.patch.object(nh_loop, "build_bundle_seven_question_validation_context", side_effect=build_ctx),
            mock.patch.object(nh_loop.nh_supervisor.replay, "Replay", side_effect=lambda *a, **k: Scoped()),
            mock.patch.object(nh_loop.nh_supervisor.commands, "reconcile_provider_request", side_effect=reconcile),
            mock.patch.object(nh_loop.nh_supervisor.commands, "dispatch_piece3_provider_review_for_controller_selection", side_effect=dispatch),
        ):
            nh_loop.run_supervised_bundle_seven_question_validation(
                {"package_scope_id": "B30", "package_id": "B30"}, errors, work_item_kind="coverage_review"
            )

        self.assertEqual(order, ["reconcile", "dispatch"], order)
        self.assertGreaterEqual(
            len(built), 2,
            "the context must be rebuilt after the reconcile appended events, before dispatching",
        )

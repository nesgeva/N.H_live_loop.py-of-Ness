#!/usr/bin/env python3
"""OFFLINE rehearsals for the accepted N.H section 8.8 SOURCE-BINDING-CURRENTNESS design.

Source of obligations:
``INPUTS_READ_ONLY/
NH_LIVE_DESIGN_LOOP_SOURCE_BINDING_CURRENTNESS_MECHANICAL_DESIGN_v1_3_CANDIDATE.md``
SHA-256 5a49dd70765ecdfef97aa9cac0d4a0757ffe68842ef5d083397401df325c21bc,
230,807 bytes, 3,137 lines.  Section 24 rehearsal matrix R-SB1 through R-SB42.

EVERY rehearsal here runs OFFLINE, in a DISPOSABLE copy, against a DISPOSABLE
journal and checkout, or READ-ONLY against the copied real state.  None appends
to the copied real journal, none touches the LIVE workspace, and none contacts a
provider: the transport FAILS LOUDLY if reached.

The canonical v1_8 harness is REUSED WHOLESALE (section 6 anti-bloat -- no
parallel test system is created).  Everything imported below is that harness.
"""

from __future__ import annotations

import dataclasses
import json
import unittest
from types import SimpleNamespace

import os
import sys

sys.dont_write_bytecode = True

# The canonical v1_8 harness is a SIBLING module.  It is imported, never
# re-implemented (section 6 anti-bloat).
_TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _TESTS_DIR not in sys.path:
    sys.path.insert(0, _TESTS_DIR)

import test_post_acceptance_continuation_v1_8 as H  # noqa: E402

nh_loop = H.nh_loop
commands = H.commands
engine = H.engine
identity = H.identity
replay_mod = H.replay
schema = H.schema
from nh_supervisor import status as status_mod  # noqa: E402
from nh_supervisor.engine import SupervisorRefusal  # noqa: E402
from nh_supervisor.commands import LoopStop  # noqa: E402

SCOPE_P = H.SCOPE_P
SCOPE_Q = H.SCOPE_Q
ROOT_Q = H.ROOT_Q
TARGET_Q = H.TARGET_Q


# ===========================================================================
# Shared helpers.  Nothing here is a second implementation of anything: every
# derivation under test is the installed one.
# ===========================================================================
def live_scope_facts():
    """The copied REAL state's proved scope, read READ-ONLY.

    The real journal genuinely holds TWO complete validation sets of ONE scope
    -- anchor at event_seq 1 and effective at event_seq 6 -- so it is the
    honest fixture for every "two same-scope validations" case.
    """
    errors = []
    context = nh_loop.build_supervisor_context(errors)
    assert context is not None, errors
    events = context.journal.read()
    state = nh_loop.replay_interview_state(events, [])
    scope = context.binding.package_scope_id
    anchor = nh_loop.scope_anchor_validations(events)[scope]
    effective = nh_loop.effective_validation(state, events, scope)
    return context, events, state, scope, anchor, effective


def multi_validation_scope_facts():
    """A current, replayable scope that still has two complete validations."""
    errors = []
    control = nh_loop.build_supervisor_context(errors)
    assert control is not None, errors
    events = control.journal.read()
    state = nh_loop.replay_interview_state(events, [])
    anchors = nh_loop.scope_anchor_validations(events)
    counts = {}
    for event in events:
        if event.get("type") == "validation_recorded":
            scope = event.get("package_scope_id")
            counts[scope] = counts.get(scope, 0) + 1
    for scope in sorted(counts, key=lambda item: anchors[item]["event_seq"]):
        if counts[scope] < 2:
            continue
        anchor = anchors[scope]
        effective = nh_loop.effective_validation(state, events, scope)
        if effective is None or effective["event_seq"] == anchor["event_seq"]:
            continue
        transition_errors = []
        context = nh_loop.build_transition_context(
            "post_validation",
            {
                "package_scope_id": scope,
                "scope_root_path": anchor["package_source_binding"][
                    "scope_root_path"
                ],
            },
            transition_errors,
        )
        if context is not None:
            return context, events, state, scope, anchor, effective
    raise unittest.SkipTest(
        "the current authenticated journal has no replayable scope with two "
        "complete validations"
    )


def synthetic_validation(seq, scope, set_id, *, root="R.md", package_id=None,
                         package_key="no_controlled_id_settled_yet",
                         manifest="m" * 64, paths=("a.md",),
                         branch="nh-design-loop", head="h" * 40,
                         binding_sha="s" * 64):
    """One ``validation_recorded`` event, shaped exactly like a real one."""
    return {
        "type": "validation_recorded",
        "event_seq": seq,
        "package_scope_id": scope,
        "package_key": package_key,
        "package_id": package_id,
        "validation_set_id": set_id,
        "branch": branch,
        "head_sha": head,
        "source_binding_sha256": binding_sha,
        "source_manifest_sha256": manifest,
        "source_paths_checked": list(paths),
        "package_source_binding": {"scope_root_path": root},
    }


def synthetic_state(*sets):
    """A replayed-state stand-in carrying exactly these complete sets."""
    latest = {}
    for record in sets:
        latest[record["package_scope_id"]] = record
    return {
        "latest_complete_by_package": latest,
        "stale_validation_set_ids": frozenset(),
    }


def strip_comments_and_docstrings(text):
    """The CODE only.  Comments and string literals are removed, so a source
    sweep can never be satisfied -- or defeated -- by prose."""
    import io
    import tokenize
    out = []
    previous = tokenize.INDENT
    try:
        for token in tokenize.generate_tokens(io.StringIO(text).readline):
            kind, value = token.type, token.string
            if kind == tokenize.COMMENT:
                continue
            if kind == tokenize.STRING and previous in (
                tokenize.INDENT, tokenize.NEWLINE, tokenize.NL,
                tokenize.DEDENT,
            ):
                continue  # a docstring
            out.append(value)
            if kind not in (tokenize.NL, tokenize.NEWLINE):
                previous = kind
            else:
                previous = kind
    except (tokenize.TokenError, IndentationError):
        # A partial slice may not tokenize; fall back to a line sweep.
        return "\n".join(
            line.split("#", 1)[0] for line in text.split("\n")
        )
    return " ".join(out)


def complete_set(scope, set_id, first_seq, *, manifests=None):
    return {
        "package_scope_id": scope,
        "validation_set_id": set_id,
        "first_event_seq": first_seq,
        "page_manifests": manifests or {},
    }


# ===========================================================================
# R-SB1, R-SB2, R-SB8, R-SB9, R-SB25, R-SB26 -- THE EFFECTIVE VALIDATION.
# ===========================================================================
class EffectiveValidationRehearsals(unittest.TestCase):

    def test_R_SB1_single_validation_makes_effective_equal_the_anchor(self):
        """R-SB1 -- one set: effective(S) IS anchor(S), field for field."""
        event = synthetic_validation(1, SCOPE_P, "vs_only")
        events = [event]
        state = synthetic_state(complete_set(SCOPE_P, "vs_only", 1))
        anchor = nh_loop.scope_anchor_validations(events)[SCOPE_P]
        effective = nh_loop.effective_validation(state, events, SCOPE_P)
        self.assertIs(effective, anchor, "effective IS the anchor event itself")
        for field in ("package_scope_id", "package_key", "package_id",
                      "branch", "head_sha", "source_binding_sha256",
                      "source_manifest_sha256", "source_paths_checked",
                      "validation_set_id"):
            self.assertEqual(effective[field], anchor[field], field)
        # ZERO appends: the selector is a pure read over the event list.
        self.assertEqual(events, [event])

    def test_R_SB2_two_sets_move_only_the_EV_trio(self):
        """R-SB2 -- IA stays on the FIRST set; the EV trio comes from the SECOND.

        Proved on the copied REAL state, which genuinely holds two complete
        validation sets of one scope.
        """
        context, events, state, scope, anchor, effective = multi_validation_scope_facts()
        self.assertNotEqual(anchor["event_seq"], effective["event_seq"])
        self.assertLess(anchor["event_seq"], effective["event_seq"])
        binding = context.binding
        # ---- IA: unchanged, from the ANCHOR ----
        self.assertEqual(binding.package_scope_id, anchor["package_scope_id"])
        self.assertEqual(binding.package_key, anchor["package_key"])
        self.assertEqual(binding.package_id, anchor["package_id"])
        self.assertEqual(binding.scope_root_path,
                         anchor["package_source_binding"]["scope_root_path"])
        self.assertEqual(binding.branch, anchor["branch"])
        self.assertEqual(binding.head_sha, anchor["head_sha"])
        self.assertEqual(binding.source_binding_sha256,
                         anchor["source_binding_sha256"])
        self.assertEqual(binding.terminal_chain_sha256,
                         anchor["source_binding_sha256"])
        # ---- EV: MOVED, from the EFFECTIVE validation ----
        self.assertEqual(binding.source_manifest_sha256,
                         effective["source_manifest_sha256"])
        self.assertEqual(set(binding.required_source_paths),
                         set(effective["source_paths_checked"]))
        self.assertEqual(binding.validation_set_id,
                         effective["validation_set_id"])
        # ---- and the EV values are genuinely NOT the anchor's ----
        self.assertNotEqual(anchor["source_manifest_sha256"],
                            effective["source_manifest_sha256"])
        self.assertNotEqual(anchor["validation_set_id"],
                            effective["validation_set_id"])

    def test_R_SB8_a_different_scope_root_is_a_contradiction(self):
        """R-SB8 / F-3 -- same scope, different root: FAIL CLOSED."""
        anchor = synthetic_validation(1, SCOPE_P, "vs_1", root="A.md",
                                      package_id="pkg")
        later = synthetic_validation(9, SCOPE_P, "vs_2", root="B.md",
                                     package_id="pkg")
        errors = []
        self.assertFalse(
            nh_loop.effective_validation_compatible(anchor, later, errors)
        )
        self.assertTrue(errors)
        self.assertIn("CONTRADICTION", errors[0])
        self.assertIn("scope_root_path", errors[0])
        # Nothing is preferred, nothing dropped, nothing re-anchored.
        self.assertIn("neither is preferred", errors[0])

    def test_bundle_seven_legacy_shared_root_to_proved_package_root_is_compatible(self):
        workflow = nh_loop.BUNDLE_SEVEN_WORKFLOW_PATH
        package_root = (
            "05_ACTIVE_CANDIDATE/"
            "NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_"
            "WONDER_RUNTIME_v1.md"
        )
        anchor = synthetic_validation(
            1, "A19", "vs_old", root=workflow, package_id="A19",
            package_key="A19", paths=(workflow,),
        )
        effective = synthetic_validation(
            9, "A19", "vs_new", root=package_root, package_id="A19",
            package_key="A19", paths=(workflow, package_root),
        )
        errors = []

        self.assertTrue(
            nh_loop.effective_validation_compatible(anchor, effective, errors)
        )
        self.assertEqual([], errors)
        self.assertIs(
            nh_loop.scope_anchor_validations([anchor, effective])["A19"],
            anchor,
            "the migration is compatible but never re-anchors the scope",
        )

    def test_bundle_seven_legacy_root_transition_requires_both_checked_roots(self):
        workflow = nh_loop.BUNDLE_SEVEN_WORKFLOW_PATH
        package_root = "05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_A19.md"
        anchor = synthetic_validation(
            1, "A19", "vs_old", root=workflow, package_id="A19",
            package_key="A19", paths=(workflow,),
        )
        effective = synthetic_validation(
            9, "A19", "vs_new", root=package_root, package_id="A19",
            package_key="A19", paths=(package_root,),
        )
        errors = []

        self.assertFalse(
            nh_loop.effective_validation_compatible(anchor, effective, errors)
        )
        self.assertIn("CONTRADICTION", errors[0])

    def test_piece3_accepts_only_the_exact_proved_bundle_seven_root_migration(self):
        workflow = nh_loop.BUNDLE_SEVEN_WORKFLOW_PATH
        package_root = "05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_A19.md"
        selection = {
            "package_scope_id": "A19",
            "package_id": "A19",
            "scope_root_path": package_root,
        }
        context = SimpleNamespace(
            binding=SimpleNamespace(
                package_scope_id="A19",
                package_id="A19",
                scope_root_path=workflow,
            ),
            transition_facts={"package_scope_id": "A19"},
            bundle_seven_legacy_root_transition={
                "package_scope_id": "A19",
                "anchor_scope_root_path": workflow,
                "effective_scope_root_path": package_root,
            },
        )

        self.assertTrue(
            commands.piece3_selection_matches_proved_package_binding(
                context, selection
            )
        )
        context.bundle_seven_legacy_root_transition[
            "effective_scope_root_path"
        ] = "05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_A20.md"
        self.assertFalse(
            commands.piece3_selection_matches_proved_package_binding(
                context, selection
            )
        )

    def test_piece3_keeps_accepting_an_exact_root_match_without_migration(self):
        selection = {
            "package_scope_id": "A19",
            "package_id": "A19",
            "scope_root_path": "A.md",
        }
        context = SimpleNamespace(
            binding=SimpleNamespace(
                package_scope_id="A19",
                package_id="A19",
                scope_root_path="A.md",
            ),
            transition_facts={"package_scope_id": "A19"},
            bundle_seven_legacy_root_transition=None,
        )

        self.assertTrue(
            commands.piece3_selection_matches_proved_package_binding(
                context, selection
            )
        )

    def test_bundle_seven_explicit_workflow_root_never_uses_the_migration(self):
        workflow = nh_loop.BUNDLE_SEVEN_WORKFLOW_PATH
        package_root = "05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_B30.md"
        anchor = synthetic_validation(
            1, "B30", "vs_old", root=workflow, package_id="B30",
            package_key="B30", paths=(workflow,),
        )
        effective = synthetic_validation(
            9, "B30", "vs_new", root=package_root, package_id="B30",
            package_key="B30", paths=(workflow, package_root),
        )
        errors = []

        self.assertFalse(
            nh_loop.effective_validation_compatible(anchor, effective, errors)
        )
        self.assertIn("CONTRADICTION", errors[0])

    def test_R_SB8b_matching_identity_is_compatible(self):
        anchor = synthetic_validation(1, SCOPE_P, "vs_1", root="A.md")
        later = synthetic_validation(9, SCOPE_P, "vs_2", root="A.md")
        errors = []
        self.assertTrue(
            nh_loop.effective_validation_compatible(anchor, later, errors)
        )
        self.assertEqual(errors, [])

    def test_R_SB9_an_unprovable_newer_validation_stays_effective(self):
        """R-SB9 / F-11 SBC-NO-SILENT-FALLBACK -- no fallback to the anchor."""
        first = synthetic_validation(1, SCOPE_P, "vs_1")
        second = synthetic_validation(9, SCOPE_P, "vs_2", manifest="n" * 64)
        events = [first, second]
        state = synthetic_state(complete_set(SCOPE_P, "vs_2", 9))
        # Its source cannot be re-proved -- the replay says so.
        state["stale_validation_set_ids"] = frozenset({"vs_2"})
        effective = nh_loop.effective_validation(state, events, SCOPE_P)
        self.assertEqual(effective["validation_set_id"], "vs_2",
                         "the NEWER set REMAINS effective")
        self.assertEqual(effective["event_seq"], 9)
        verdict = nh_loop.package_source_family_a(
            state, SCOPE_P, None,
            complete_set(SCOPE_P, "vs_2", 9),
        )
        self.assertTrue(verdict["validation_set_stale"])
        self.assertFalse(verdict["source_state_current"])
        self.assertIsNotNone(verdict["source_currentness_reason"])

    def test_R_SB25_an_incomplete_set_is_never_effective(self):
        """R-SB25 -- only the replay's COMPLETE sets are eligible."""
        first = synthetic_validation(1, SCOPE_P, "vs_1")
        # vs_2 exists as an event but the replay never made it complete, so it
        # never reaches latest_complete_by_package.
        second = synthetic_validation(9, SCOPE_P, "vs_2")
        events = [first, second]
        state = synthetic_state(complete_set(SCOPE_P, "vs_1", 1))
        effective = nh_loop.effective_validation(state, events, SCOPE_P)
        self.assertEqual(effective["validation_set_id"], "vs_1")
        self.assertEqual(effective["event_seq"], 1,
                         "the previous COMPLETE set stays effective")

    def test_F1_no_complete_set_is_not_current_and_is_not_a_guess(self):
        """F-1 -- zero complete sets: NOT current, with the exact reason."""
        state = synthetic_state()
        self.assertIsNone(nh_loop.effective_validation(state, [], SCOPE_P))
        verdict = nh_loop.package_source_family_a(state, SCOPE_P, None, None)
        self.assertFalse(verdict["source_state_current"])
        self.assertEqual(verdict["source_currentness_reason"],
                         nh_loop.SOURCE_CURRENTNESS_NO_VALIDATION)
        self.assertEqual(verdict["custody_subtracted_paths"], [])

    def test_S6_2D_ordering_is_the_authenticated_event_seq_only(self):
        """section 6.2 D -- never a set-id string, filename, mtime or order."""
        # A LEXICALLY LATER id at an EARLIER seq must not win.
        low = synthetic_validation(2, SCOPE_P, "vs_zzz")
        high = synthetic_validation(8, SCOPE_P, "vs_aaa")
        events = [low, high]
        state = synthetic_state(complete_set(SCOPE_P, "vs_aaa", 8))
        effective = nh_loop.effective_validation(state, events, SCOPE_P)
        self.assertEqual(effective["validation_set_id"], "vs_aaa")
        self.assertEqual(effective["event_seq"], 8)


# ===========================================================================
# R-SB3..R-SB7, R-SB10, R-SB11, R-SB18, R-SB20, R-SB22, R-SB27, R-SB29,
# R-SB34 -- THE PROJECTION, THE STATUS REPORT, AND THE TWO FAMILIES.
# ===========================================================================
class CurrentnessProjectionRehearsals(unittest.TestCase):

    def test_R_SB3_the_validation_reproof_subtraction_is_reported_exactly(self):
        """R-SB3 -- custody_subtracted_paths names exactly what section 9 allowed.

        This case is about the VALIDATION REPROOF only.  A REQUEST FREEZE
        subtracts nothing (R-SB36).
        """
        _c, _e, _s, scope, _a, _ev = live_scope_facts()
        projection = nh_loop.package_source_currentness(scope)
        self.assertIsNotNone(projection)
        subtracted = projection["custody_subtracted_paths"]
        self.assertIsInstance(subtracted, list)
        # Whatever it names, it names ONLY authenticated custodied paths of
        # THIS scope -- never an unrelated file.
        errors = []
        chains = nh_loop.authenticated_candidate_custody(
            _c.journal.read(), errors
        )
        self.assertIsNotNone(chains, errors)
        chain = chains.get(scope) or {}
        custodied = {entry["path"] for entry in (chain.get("successors") or ())}
        for path in subtracted:
            self.assertIn(path, custodied,
                          "only authenticated custody of THIS scope is ever "
                          "subtracted")

    def test_R_SB4_R_SB5_R_SB6_drift_is_never_hidden(self):
        """R-SB4 / R-SB5 / R-SB6 -- a manifest that no longer re-derives is drift.

        An unrelated untracked file, a tracked or staged edit and a mutated
        custodied candidate all change the whole-listing digest, so the stored
        page manifest stops re-deriving.  The verdict is NOT CURRENT and the
        observed digest is NEVER adopted.
        """
        state = synthetic_state(complete_set(SCOPE_P, "vs_1", 1))
        drifted_set = complete_set(
            SCOPE_P, "vs_1", 1,
            manifests={1: {"checked_paths": ["a.md"],
                           "manifest_sha256": "stored-digest"}},
        )
        # A binding whose recomputation cannot reproduce the stored digest.
        verdict = nh_loop.package_source_family_a(
            state, SCOPE_P, {"branch": "b", "head_sha": "h",
                             "worktree_entries": [], "binding_sha256": "x"},
            drifted_set,
        )
        self.assertTrue(verdict["manifest_drifted"])
        self.assertFalse(verdict["source_state_current"])
        # The stored digest is preserved, never replaced by what was observed.
        self.assertEqual(
            drifted_set["page_manifests"][1]["manifest_sha256"], "stored-digest"
        )

    def test_R_SB7_an_aborted_write_ahead_is_never_custody(self):
        """R-SB7 -- an aborted intent is never subtracted; and a request freeze
        subtracts nothing at all, so it cannot be smuggled in there either."""
        source = H.read_text(CONTROLLER_DIR / "nh_loop.py") if False else \
            H.read_text(H.CONTROLLER_DIR / "nh_loop.py")
        # The installed suffix derivation reads COMMITTED custody only.
        marker = source.index("def custody_post_validation_suffix(")
        body = source[marker:source.index("\ndef custody_baseline_source_binding(")]
        self.assertNotIn("candidate_write_ahead_recorded", body,
                         "an aborted or pending intent is not custody")

    def test_R_SB10_R_SB22_no_re_anchor_and_ordering_is_untouched(self):
        """R-SB10 / R-SB22 -- CPB-CURRENT still orders by the ANCHOR's seq.

        A currentness update on a package with two validations re-anchors
        nothing: package_scope_id, the chain anchor, correction-round ownership
        and acceptance are all unchanged.
        """
        context, events, _s, scope, anchor, effective = multi_validation_scope_facts()
        # This scope remains keyed on its ANCHOR, not on E.
        again = nh_loop.scope_anchor_validations(events)[scope]
        self.assertEqual(again["event_seq"], anchor["event_seq"])
        self.assertEqual(again["validation_set_id"], anchor["validation_set_id"])
        self.assertEqual(again["package_scope_id"], scope)
        # The binding's identity half is the anchor's, though E is newer.
        self.assertEqual(context.binding.package_scope_id,
                         anchor["package_scope_id"])
        self.assertNotEqual(effective["validation_set_id"],
                            anchor["validation_set_id"])

    def test_R_SB29_a_chain_step_still_passes_under_the_corrected_binding(self):
        """R-SB29 -- the custody chain still authenticates, and the replay succeeds.

        A build that wrote the EFFECTIVE validation's branch / head_sha /
        source_binding_sha256 into the binding would make every chain step
        refuse and the WHOLE replay fail closed.  It does not.
        """
        context, events, state, scope, anchor, effective = multi_validation_scope_facts()
        self.assertIsNotNone(state, "the full replay succeeded")
        errors = []
        chains = nh_loop.authenticated_candidate_custody(events, errors)
        self.assertIsNotNone(chains, errors)
        self.assertEqual(errors, [])
        # The binding the chain is checked against is the ANCHOR's, and the
        # effective validation genuinely stands on a DIFFERENT source state.
        self.assertEqual(context.binding.source_binding_sha256,
                         anchor["source_binding_sha256"])
        self.assertNotEqual(anchor["source_binding_sha256"],
                            effective["source_binding_sha256"])

    def test_R_SB34_the_authorization_names_the_effective_validation(self):
        """R-SB34 -- on a revalidated package the binding names the set the
        Piece-3 gate is deciding about, never the anchor's."""
        context, _e, _s, scope, anchor, effective = multi_validation_scope_facts()
        clearance = nh_loop.evaluate_interview_clearance(scope)
        self.assertEqual(clearance["validation_set_id"],
                         effective["validation_set_id"])
        self.assertEqual(context.binding.validation_set_id,
                         effective["validation_set_id"])
        self.assertNotEqual(context.binding.validation_set_id,
                            anchor["validation_set_id"])

    def test_R_SB18_R_SB20_status_proves_it_and_demotes_nothing(self):
        """R-SB18 -- acceptance is reported BESIDE the verdict, never instead.
        R-SB20 -- zero provider calls from any currentness derivation."""
        before = H.journal_digest()
        report = H.run_live_copy("supervisor-status")
        after = H.journal_digest()
        self.assertEqual(before, after, "ZERO appends, byte-identical")
        self.assertTrue(report["ok"])
        self.assertEqual(report["acceptance_truth"], "PROVED_ACCEPTED")
        self.assertEqual(report["acceptance_disposition"],
                         "ACCEPTED_FOR_DESIGN_ONLY")
        self.assertEqual(report["workflow_state"], "ACCEPTED_FOR_DESIGN_ONLY")
        self.assertIs(report["source_state_current"], False)
        # ...and it is PROVED, not asserted: the projection is present.
        self.assertIn("source_currentness", report)
        projection = report["source_currentness"]
        self.assertIsNotNone(projection)
        self.assertIs(projection["source_state_current"], False)
        self.assertIsNotNone(projection["source_currentness_reason"])
        for key in ("anchor_validation_event_seq", "anchor_branch",
                    "anchor_head_sha", "anchor_source_binding_sha256",
                    "effective_validation_set_id",
                    "effective_validation_event_seq", "effective_branch",
                    "effective_head_sha", "effective_source_binding_sha256",
                    "effective_source_manifest_sha256",
                    "effective_required_source_paths", "live_branch",
                    "live_head_sha", "live_source_binding_sha256",
                    "custody_subtracted_paths"):
            self.assertIn(key, projection, key)

    def test_S13_2_status_declares_exactly_one_new_key(self):
        """section 13.2 SBC-STATUS-REPORTS -- EXACTLY ONE new top-level key, nested."""
        self.assertIn("source_currentness", status_mod.SUPERVISOR_STATUS_KEYS)
        # frozen 2026-09-02 at journal event 96: the pre-change capture
        # LIVE_SUPERVISOR_STATUS_BEFORE.json (sha256 4a7704e4..., taken at
        # authenticated_event_seq 96, controller db46a51) was never checked in
        # here; it is the v1_3 implementation workspace's capture, kept
        # byte-identical beside this file, and the status is re-run at the same
        # journal position it was taken at.
        self.enterContext(H.real_disposable_installation(event_seq=96))
        report = H.run_live_copy("supervisor-status")
        # The installed "must carry exactly its declared key set" rule still
        # holds, now covering one more key.
        self.assertEqual(
            sorted(set(status_mod.SUPERVISOR_STATUS_KEYS) - set(report)), []
        )
        self.assertIsInstance(report["source_currentness"], dict)
        # EXACTLY ONE key was added, measured against the LIVE pre-change
        # supervisor-status captured before any edit.
        baseline = json.loads(
            (H.TESTS_DIR / "LIVE_SUPERVISOR_STATUS_BEFORE.json").read_text()
        )
        added = sorted(set(report) - set(baseline))
        removed = sorted(set(baseline) - set(report))
        self.assertEqual(added, ["source_currentness"], added)
        self.assertEqual(removed, [], removed)

    def test_R_SB27_both_readers_share_ONE_family_A_verdict(self):
        """R-SB27 -- supervisor-status and the clearance's family A agree,
        from the SAME code path, and status carries NO question freshness."""
        _c, _e, _s, scope, _a, _ev = live_scope_facts()
        # BOTH readers are watched while they run.  Comparing two INDEPENDENTLY
        # derived answers afterwards would pass even on a build that carries a
        # second, advisory family-A path -- which is exactly what section 5.4 and
        # cursorrules section 1A forbid.  So the OWNER is instrumented instead.
        seen = []
        real = nh_loop.package_source_currentness

        def recording(scope_arg, **kwargs):
            result = real(scope_arg, **kwargs)
            projection = result[0] if isinstance(result, tuple) else result
            seen.append(("gate" if kwargs.get("with_internals") else "report",
                         None if projection is None
                         else projection["source_state_current"]))
            return result

        with mock.patch.object(nh_loop, "package_source_currentness", recording):
            errors = []
            context = nh_loop.build_supervisor_context(errors)
            self.assertIsNotNone(context, errors)
            report = commands.supervisor_status(context).report
            clearance = nh_loop.evaluate_interview_clearance(scope)

        kinds = {kind for kind, _ in seen}
        self.assertIn("report", kinds, "supervisor-status consumed the owner")
        self.assertIn("gate", kinds, "the enforced gate consumed the owner")
        verdicts = {verdict for _, verdict in seen}
        self.assertEqual(len(verdicts), 1,
                         "both readers got the SAME verdict from the SAME owner")
        self.assertEqual(report["source_state_current"], verdicts.pop())
        if not report["source_state_current"]:
            self.assertIn(nh_loop.INTERVIEW_GATE_SOURCE_DRIFT,
                          clearance["reasons"])
        # SBC-STATUS-IS-FAMILY-A-ONLY: no question-freshness fact is reported.
        self.assertNotIn("stale_question_ids", report)
        self.assertNotIn("stale_question_ids", report["source_currentness"])
        for value in report["source_currentness"].values():
            self.assertNotIsInstance(value, dict)
        # stale_question_ids is produced ONLY by the clearance.
        self.assertIn("stale_question_ids", clearance)

    def test_R_SB11_P_and_Q_are_separate_projections(self):
        """R-SB11 / section 12.3 -- neither projection is read as the other's."""
        _c, _e, _s, scope, _a, _ev = live_scope_facts()
        p = nh_loop.package_source_currentness(scope)
        self.assertEqual(p["package_scope_id"], scope)
        other = nh_loop.package_source_currentness("nullpkg_no_such_scope")
        self.assertEqual(other["package_scope_id"], "nullpkg_no_such_scope")
        self.assertFalse(other["source_state_current"])
        self.assertEqual(other["source_currentness_reason"],
                         nh_loop.SOURCE_CURRENTNESS_NO_VALIDATION)
        # P's verdict did not satisfy or contaminate the other scope's.
        self.assertNotEqual(p["effective_validation_set_id"],
                            other["effective_validation_set_id"])

    def test_R_SB15_R_SB16_restart_over_identical_evidence_is_identical(self):
        """R-SB15 / R-SB16 -- three derivations, byte-identical, ZERO appends."""
        _c, _e, _s, scope, _a, _ev = live_scope_facts()
        before = H.journal_digest()
        answers = []
        for _ in range(3):
            # NO manual reset.  The ONE owner opens its own fresh re-proof
            # episode for every read (section 5.1), so a rehearsal that reset the
            # cache here would MASK a build that reuses an earlier episode.
            answers.append(json.dumps(nh_loop.package_source_currentness(scope),
                                      sort_keys=True))
        self.assertEqual(len(set(answers)), 1, "identical evidence, identical answer")
        self.assertEqual(before, H.journal_digest(), "ZERO appends")

    def test_R_SB23_no_second_store_and_no_currentness_cache(self):
        """R-SB23 -- no stored flag, marker, pointer or cache-as-authority."""
        source = H.read_text(H.CONTROLLER_DIR / "nh_loop.py")
        marker = source.index("def package_source_currentness(")
        body = source[marker:source.index("\ndef evaluate_interview_clearance(")]
        for forbidden in ("journal.append", "append_interview_event",
                          "_CURRENTNESS_CACHE", "global ", "dispatch("):
            self.assertNotIn(forbidden, body, forbidden)
        # The projection is recomputed, never remembered: no module-level store
        # was introduced for it.
        self.assertNotIn("_SOURCE_CURRENTNESS", source)
        self.assertNotIn("current_transition_pointer", source)
        self.assertNotIn("handoff_complete_flag", source)


# ===========================================================================
# R-SB12..R-SB14, R-SB17, R-SB19, R-SB28, R-SB32, R-SB33, R-SB36, R-SB39,
# R-SB41 -- THE v6 ORDERING, THE CORRECTED OPERANDS, AND THE EMPTY SUBTRACTION.
# ===========================================================================
def rootless_selection(classification="waiting_on_another_choice"):
    """A legitimately ROOTLESS non-actionable T1 answer."""
    value = H.selection_object(classification=classification)
    value["package_source_path"] = None
    value["source_paths_checked"] = []
    return value


def waiting_journal(*, value=None, extra=None):
    """A journal holding ONE durable non-actionable T1 answer."""
    journal = H.accepted_journal()
    work_item_id, digest = H.selection_request_identities(extra=extra)
    H.custody_pair(
        journal,
        kind="next_package_selection",
        provider_kind="codex_next_package_selection",
        value=value if value is not None else rootless_selection(),
        scope=SCOPE_P,
        request="pr_wait",
        work_item_identity=work_item_id,
        required_inputs_sha256=digest,
        extra=extra,
    )
    return journal


class StalenessOperandRehearsals(unittest.TestCase):

    def test_R_SB32_R_SB41A_unchanged_source_does_not_wake_a_waiting_answer(self):
        """R-SB32 / R-SB41 A -- v6 ORDERING + CORRECTED OPERANDS, unchanged checkout.

        The staleness proof runs BEFORE the route decision, so the rootless
        waiting answer REACHES it.  With the source unchanged the COMPLETE
        reconstructed inventory digest EQUALS the durable
        required_inputs_sha256, so the result is NOT stale, it falls through to
        the installed non-selectable semantics, and the loop reports
        LOOP_WAITING_RECOVERING.  The corrected proof does not wake on nothing.
        """
        journal = waiting_journal()
        transport = H.LoudStubTransport()
        context = H.build_context(journal=journal, transport=transport)
        appends = journal.appends
        state = commands.post_acceptance_transition_state(context)
        report = commands.loop_position(context, state)
        self.assertIsNone(state["selection"], "a waiting answer is not selectable")
        self.assertIsNotNone(state["stop_record"])
        self.assertEqual(state["stop_record"]["loop_state"],
                         commands.LOOP_WAITING_RECOVERING,
                         "it reached the INSTALLED non-selectable semantics, "
                         "not the staleness stop")
        self.assertEqual(report["loop_state"], commands.LOOP_WAITING_RECOVERING)
        self.assertEqual(transport.calls, [], "ZERO provider calls")
        self.assertEqual(journal.appends, appends, "ZERO appends")

    def test_R_SB33_R_SB41B_a_material_source_change_wakes_it(self):
        """R-SB33 / R-SB41 B -- the SAME answer, a real material source change.

        The complete reconstructed digest now DIFFERS, so the saved result is
        STALE.  It is preserved, consumed by nothing, and the loop returns
        LOOP_SELECTION_REQUIRED / continue-design-loop -- exactly ONE fresh
        selection episode, never a cycle, with no provider call from the
        read-only derivation.
        """
        journal = waiting_journal()
        before = list(journal.events)
        appends = journal.appends
        adapter = H.StubAdapter()
        adapter.live_source_binding = H.STUB_CHANGED_SOURCE_BINDING
        transport = H.LoudStubTransport()
        context = H.build_context(journal=journal, transport=transport,
                                  adapter=adapter)
        state = commands.post_acceptance_transition_state(context)
        report = commands.loop_position(context, state)
        self.assertIsNone(state["selection"])
        self.assertEqual(state["stop_record"]["loop_state"],
                         commands.LOOP_SELECTION_REQUIRED)
        self.assertEqual(report["loop_state"], commands.LOOP_SELECTION_REQUIRED)
        self.assertEqual(report["loop_next_command"], "continue-design-loop")
        self.assertEqual(transport.calls, [], "ZERO provider calls")
        self.assertEqual(journal.appends, appends, "ZERO appends")
        self.assertEqual(journal.events, before, "history byte-identical")
        # CONVERGENCE (section 16.2): a request frozen against the source that
        # now stands reproduces exactly, so ONE episode settles it.
        fresh = waiting_journal(
            extra=H.stub_selection_extra(
                frozen_source_binding_sha256=H.STUB_CHANGED_SOURCE_BINDING
            )
        )
        context2 = H.build_context(journal=fresh, transport=H.LoudStubTransport(),
                                   adapter=adapter)
        state2 = commands.post_acceptance_transition_state(context2)
        self.assertEqual(state2["stop_record"]["loop_state"],
                         commands.LOOP_WAITING_RECOVERING,
                         "the fresh episode is NOT stale: it converged")

    def test_R_SB32b_staleness_is_proved_ABOVE_the_route_decision(self):
        """SBC-STALENESS-BEFORE-ROUTE -- the ORDERING itself, in the source.

        Proof 8 must sit AFTER the schema and classification / action-pairing
        proofs and BEFORE proof 3's route-selectability stop.
        """
        source = H.read_text(H.CONTROLLER_DIR / "nh_supervisor" / "commands.py")
        marker = source.index("def admit_selection(")
        body = source[marker:source.index("\ndef _is_coverage_failure(")]
        pairing = body.index("# 2 -- classification / action pairing")
        staleness = body.index("durable_inputs, rebuilt_inputs = staleness")
        route = body.index("if classification not in SELECTABLE_CLASSIFICATIONS:")
        self.assertLess(pairing, staleness, "staleness runs AFTER proof 2")
        self.assertLess(staleness, route, "staleness runs BEFORE proof 3")
        # And the OLD anchor-versus-raw-live comparison is GONE, not duplicated.
        self.assertNotIn("frozen != current_source", body)

    def test_R_SB36_a_request_freeze_subtracts_NOTHING(self):
        """R-SB36 / SBC-NO-REQUEST-FREEZE-SUBTRACTION -- the subtract set is EMPTY.

        In every state: no Q, Q admitted, Q's candidate committed, Q
        established, and custody of an unrelated scope.  Nothing is ever
        subtracted on ordering, sole visibility, filename similarity, root
        equality, scope equality or prose.
        """
        source = H.read_text(H.CONTROLLER_DIR / "nh_supervisor" / "commands.py")
        marker = source.index("def _controller_extra_reconstruction(")
        body = source[marker:source.index("\n# v1_8 section 12.3d E5")]
        # Measured on the CODE, never on the prose: comments and docstrings are
        # stripped before the sweep, so a comment SAYING "subtract nothing"
        # cannot mask a call that subtracts something.
        code = strip_comments_and_docstrings(body)
        for forbidden in ("t1_custody_lineage", "subtract",
                          "custody_post_validation_suffix",
                          "index_without_paths", "custody_baseline_source_binding",
                          "candidate_custody"):
            self.assertNotIn(forbidden, code, forbidden)
        # And no lineage function was added ANYWHERE.
        self.assertNotIn("def t1_custody_lineage",
                         H.read_text(H.CONTROLLER_DIR / "nh_loop.py"))
        self.assertNotIn("def t1_custody_lineage", source)
        # The T1 freeze is the LIVE binding, re-digested with NO subtraction.
        self.assertIn("current_source_binding", body)
        # And the projection reports an empty subtraction for a request freeze.
        for stage in ("selection_required", "clearance_required",
                      "task_preparation", "initial_pending", "handoff"):
            journal = H.staged_journal(stage)
            context = H.build_context(journal=journal)
            unscoped = replay_mod.Replay(journal.read())
            recon = commands._controller_extra_reconstruction(context, unscoped, {})
            extra = recon("pr_sel", "next_package_selection")
            if extra is None:
                continue
            self.assertEqual(sorted(extra),
                             ["frozen_source_binding_sha256",
                              "required_files_binding"],
                             "T1's extra is EXACTLY the two governed keys")

    def test_R_SB39_two_T1_lineages_share_root_and_scope_and_never_merge(self):
        """R-SB39 -- SAME ROOT / SAME SCOPE / DIFFERENT REQUEST LINEAGE.

        T_old cannot become admissible merely because root and scope match, and
        it never inherits T_new's downstream custody -- trivially, because
        NOTHING is ever subtracted from a request freeze.
        """
        journal = H.accepted_journal()
        # T_old, frozen against a source that has since moved.
        old_id, old_digest = H.selection_request_identities(
            extra=H.stub_selection_extra(
                frozen_source_binding_sha256="0" * 64
            )
        )
        H.custody_pair(
            journal, kind="next_package_selection",
            provider_kind="codex_next_package_selection",
            value=H.selection_object(root=ROOT_Q), scope=SCOPE_P,
            request="pr_old", work_item_identity=old_id,
            required_inputs_sha256=old_digest,
        )
        # T_new, frozen against the source that STANDS.  Same root, same scope.
        new_id, new_digest = H.selection_request_identities()
        H.custody_pair(
            journal, kind="next_package_selection",
            provider_kind="codex_next_package_selection",
            value=H.selection_object(root=ROOT_Q), scope=SCOPE_P,
            request="pr_new", work_item_identity=new_id,
            required_inputs_sha256=new_digest,
        )
        transport = H.LoudStubTransport()
        appends = journal.appends
        context = H.build_context(journal=journal, transport=transport)
        state = commands.post_acceptance_transition_state(context)
        # EXACTLY ONE is admissible -- T_new.  T_old is stale and stays stale.
        self.assertIsNotNone(state["selection"])
        self.assertEqual(state["selection_custody"]["provider_request_identity"],
                         "pr_new")
        self.assertIsNone(state["contradiction"],
                          "no len(admissible) > 1 contradiction is manufactured "
                          "by a wrongly-rescued T_old")
        self.assertEqual(state["transition_scope"],
                         state["selection"]["package_scope_id"])
        self.assertEqual(transport.calls, [], "ZERO provider calls")
        self.assertEqual(journal.appends, appends, "ZERO appends")

    def test_R_SB12_R_SB19_an_unchanged_freeze_is_reused_exactly(self):
        """R-SB12 / R-SB19 -- identical inputs reconstruct identically."""
        journal = H.accepted_journal()
        H.admitted_selection_state(journal)
        transport = H.LoudStubTransport()
        appends = journal.appends
        context = H.build_context(journal=journal, transport=transport)
        unscoped = replay_mod.Replay(journal.read())
        recon = commands._controller_extra_reconstruction(context, unscoped, {})
        extra = recon("pr_sel", "next_package_selection")
        durable, rebuilt = commands.required_inputs_staleness(
            context, unscoped, journal.read(), "pr_sel",
            "next_package_selection", extra,
        )
        self.assertIsNotNone(rebuilt)
        self.assertEqual(durable, rebuilt, "the SAME inventory at two times")
        state = commands.post_acceptance_transition_state(context)
        self.assertIsNotNone(state["selection"], "reused, not re-obtained")
        self.assertEqual(transport.calls, [])
        self.assertEqual(journal.appends, appends)

    def test_R_SB17_a_previous_ownership_request_is_stale_not_rewritten(self):
        """R-SB17 / section 16.1 SBC-MIGRATION-GENERIC -- generic over ANY such state."""
        journal = H.accepted_journal()
        # Frozen under the PREVIOUS ownership: the anchor's chain source
        # identity rather than the live source.
        old_extra = H.stub_selection_extra(
            frozen_source_binding_sha256=H.make_binding(SCOPE_P).source_binding_sha256
        )
        work_item_id, digest = H.selection_request_identities(extra=old_extra)
        H.custody_pair(
            journal, kind="next_package_selection",
            provider_kind="codex_next_package_selection",
            value=H.selection_object(), scope=SCOPE_P, request="pr_legacy",
            work_item_identity=work_item_id, required_inputs_sha256=digest,
        )
        before = list(journal.events)
        appends = journal.appends
        transport = H.LoudStubTransport()
        context = H.build_context(journal=journal, transport=transport)
        state = commands.post_acceptance_transition_state(context)
        report = commands.loop_position(context, state)
        self.assertIsNone(state["selection"], "stale under the current ownership")
        self.assertEqual(report["loop_state"], commands.LOOP_SELECTION_REQUIRED)
        self.assertEqual(report["loop_next_command"], "continue-design-loop")
        self.assertEqual(journal.events, before, "NO journal rewrite")
        self.assertEqual(journal.appends, appends, "NO append to discover it")
        self.assertEqual(transport.calls, [], "NO provider call")

    def test_R_SB28_a_moved_source_does_not_move_the_work_item(self):
        """R-SB28 / T1-EXHAUSTION-RESTART-STABLE -- identity, series and budget
        are unaffected by the live freeze."""
        self.assertIn("source_binding_sha256", identity.WORK_ITEM_KEYS)
        self.assertNotIn("frozen_source_binding_sha256", identity.WORK_ITEM_KEYS)
        self.assertNotIn("extra", identity.WORK_ITEM_KEYS)
        journal = H.accepted_journal()
        context = H.build_context(journal=journal)
        situation = status_mod.Situation(context, journal.read())
        _obj, first = engine.next_package_selection_work_item(
            context, situation.candidate
        )
        adapter = H.StubAdapter()
        adapter.live_source_binding = H.STUB_CHANGED_SOURCE_BINDING
        moved = H.build_context(journal=journal, adapter=adapter)
        situation2 = status_mod.Situation(moved, journal.read())
        _obj2, second = engine.next_package_selection_work_item(
            moved, situation2.candidate
        )
        self.assertEqual(first, second,
                         "the live source moved; work_item_identity did not")

    def test_R_SB14_R_SB24_the_derivation_is_re_run_never_remembered(self):
        """R-SB14 / R-SB24 -- the same generic rule; a moved journal is re-proved."""
        journal = waiting_journal()
        context = H.build_context(journal=journal)
        first = commands.post_acceptance_transition_state(context)
        self.assertEqual(first["stop_record"]["loop_state"],
                         commands.LOOP_WAITING_RECOVERING)
        # The source MOVES between derivations.  The second derivation re-proves
        # from the CURRENT evidence; the first report is never authority.
        adapter = H.StubAdapter()
        adapter.live_source_binding = H.STUB_CHANGED_SOURCE_BINDING
        moved = H.build_context(journal=journal, adapter=adapter)
        second = commands.post_acceptance_transition_state(moved)
        self.assertEqual(second["stop_record"]["loop_state"],
                         commands.LOOP_SELECTION_REQUIRED,
                         "no sticky wait; the SAME generic rule fired")
        # No root requirement was invented in either direction.
        self.assertIsNone(first["selection"])
        self.assertIsNone(second["selection"])


# ===========================================================================
# R-SB21, R-SB30, R-SB31, R-SB35, R-SB37, R-SB38, R-SB40, R-SB42 --
# PHASE OWNERSHIP, THE COMPLETED HANDOFF, FAMILY B, AND T4.
# ===========================================================================
class PhaseOwnershipAndHandoffRehearsals(unittest.TestCase):

    def test_R_SB42_admitted_T1_with_NO_Q_event_still_proves_Q(self):
        """R-SB42 (E1, the focused case) -- PHASE 1.

        P accepted; exactly ONE actionable T1 result fully admitted, proving Q;
        NO Q-scoped event of any kind.  transition_scope MUST be the admitted
        selection's Q scope, binding 2 MUST be constructible, the position MUST
        be LOOP_PACKAGE_CLEARANCE_REQUIRED / dispatch-piece3-provider-review,
        and NO second T1 and NO fabricated Q event may appear.
        """
        journal = H.accepted_journal()
        H.admitted_selection_state(journal)
        transport = H.LoudStubTransport()
        appends = journal.appends
        events_before = list(journal.events)
        context = H.build_context(journal=journal, transport=transport)

        # (3) -- NO Q-scoped evidence of any kind exists.
        self.assertEqual(
            commands.authenticated_q_evidence_scopes(journal.read(), SCOPE_P),
            set(),
            "no Q-scoped validation / prepared / write-ahead / custody exists",
        )

        answers = []
        for _ in range(3):  # re-run three times -> identical answer
            state = commands.post_acceptance_transition_state(context)
            report = commands.loop_position(context, state)
            answers.append((state["transition_scope"], report["loop_state"],
                            report["loop_next_command"]))
        self.assertEqual(len(set(answers)), 1, "identical on every re-derivation")

        state = commands.post_acceptance_transition_state(context)
        self.assertIsNotNone(state["selection"], "the selection remains ADMITTED")
        self.assertEqual(state["transition_scope"],
                         state["selection"]["package_scope_id"])
        self.assertEqual(state["transition_scope"], SCOPE_Q)
        self.assertFalse(state["scope_has_validation"])
        report = commands.loop_position(context, state)
        self.assertEqual(report["loop_state"],
                         commands.LOOP_PACKAGE_CLEARANCE_REQUIRED)
        self.assertEqual(report["loop_next_command"],
                         "dispatch-piece3-provider-review")
        # Binding 2 is CONSTRUCTIBLE from the admitted selection's proved facts.
        self.assertIsNone(state["validation_set_id"], "validation_set_id is null")
        # No second T1, no fabricated Q event, zero calls, zero appends.
        self.assertEqual(journal.events, events_before)
        self.assertEqual(journal.appends, appends)
        self.assertEqual(transport.calls, [])

    def test_R_SB42b_zero_admitted_selections_means_there_is_no_Q(self):
        """TB-NO-PREMATURE-Q / F-14d -- and that is NOT a failure."""
        journal = H.accepted_journal()
        context = H.build_context(journal=journal)
        state = commands.post_acceptance_transition_state(context)
        self.assertIsNone(state["transition_scope"])
        self.assertIsNone(state["contradiction"], "absence is not a contradiction")

    def test_R_SB30_R_SB40_a_completed_handoff_is_never_rewound(self):
        """R-SB30 / R-SB40 -- PHASE 2 and PHASE 3.

        Establish Q fully, prove LOOP_HANDOFF_COMPLETE, then make the
        historical T1 selection stale by a material source change.  The
        handoff stays complete, transition_scope is STILL derived (from the
        authenticated Q evidence), and NO fresh T1 request is opened.
        """
        journal = H.staged_journal("handoff")
        transport = H.LoudStubTransport()
        context = H.build_context(journal=journal, transport=transport,
                                  clearance=lambda scope: {"unlocked": True})
        state = commands.post_acceptance_transition_state(context)
        report = commands.loop_position(context, state)
        self.assertTrue(state["established_complete"])
        self.assertEqual(report["loop_state"], commands.LOOP_HANDOFF_COMPLETE)
        self.assertEqual(state["transition_scope"], SCOPE_Q)

        # Now a MATERIAL source change makes the historical T1 result stale.
        appends = journal.appends
        events_before = list(journal.events)
        adapter = H.StubAdapter()
        adapter.live_source_binding = H.STUB_CHANGED_SOURCE_BINDING
        answers = []
        for _ in range(3):  # restart and re-derive, three times
            moved = H.build_context(journal=journal, transport=transport,
                                    adapter=adapter,
                                    clearance=lambda scope: {"unlocked": True})
            after = commands.post_acceptance_transition_state(moved)
            after_report = commands.loop_position(moved, after)
            answers.append((after["established_complete"],
                            after["transition_scope"],
                            after_report["loop_state"],
                            after_report["loop_next_command"]))
        self.assertEqual(len(set(answers)), 1, "identical answer every time")
        established, scope_q, loop_state, next_command = answers[0]
        self.assertIsNone(commands.post_acceptance_transition_state(
            H.build_context(journal=journal, transport=transport, adapter=adapter,
                            clearance=lambda scope: {"unlocked": True})
        )["selection"], "the historical selection IS now stale")
        self.assertTrue(established, "establishment is journal truth")
        self.assertEqual(scope_q, SCOPE_Q,
                         "PHASE 2 keeps transition_scope derivable")
        self.assertEqual(loop_state, commands.LOOP_HANDOFF_COMPLETE,
                         "F-16 -- a completed handoff is NEVER rewound")
        self.assertIsNone(next_command, "no fresh T1 is opened")
        self.assertEqual(journal.events, events_before, "ZERO appends")
        self.assertEqual(journal.appends, appends)
        self.assertEqual(transport.calls, [], "ZERO provider calls")

    def test_R_SB40b_phase_2_survives_the_selection_but_grants_it_nothing(self):
        """section 8.6.3 -- phase 2 does NOT make a stale selection admissible."""
        journal = H.staged_journal("initial_design")
        adapter = H.StubAdapter()
        adapter.roots = {}          # the selected root is gone
        context = H.build_context(journal=journal, adapter=adapter,
                                  clearance=lambda scope: {"unlocked": True})
        state = commands.post_acceptance_transition_state(context)
        self.assertIsNone(state["selection"], "still not admissible")
        self.assertEqual(state["transition_scope"], SCOPE_Q, "but Q is proved")
        # Every branch that REQUIRES an admitted selection still requires one.
        with H.proved_acceptance():
            with self.assertRaises(SupervisorRefusal):
                commands.prepare_next_design_task(context)

    def test_R_SB_F17_phase_disagreement_fails_closed(self):
        """F-17 -- an admitted selection and Q evidence naming DIFFERENT scopes."""
        journal = H.accepted_journal()
        H.admitted_selection_state(journal)      # proves SCOPE_Q
        journal.append(
            {"type": "validation_recorded",
             "package_scope_id": "nullpkg_some_other_scope_entirely",
             "validation_set_id": "vs_other"}
        )
        transport = H.LoudStubTransport()
        appends = journal.appends
        context = H.build_context(journal=journal, transport=transport)
        state = commands.post_acceptance_transition_state(context)
        self.assertIsNotNone(state["contradiction"])
        self.assertIn("contradiction", state["contradiction"].lower())
        self.assertIsNone(state["transition_scope"], "nothing is derived")
        self.assertEqual(journal.appends, appends, "nothing is appended")
        self.assertEqual(transport.calls, [])

    def test_R_SB_F14b_two_Q_evidence_scopes_fail_closed(self):
        """F-14b -- more than one post-acceptance scope carries Q evidence."""
        journal = H.accepted_journal()
        for scope in ("nullpkg_scope_one", "nullpkg_scope_two"):
            journal.append({"type": "validation_recorded",
                            "package_scope_id": scope,
                            "validation_set_id": "vs_" + scope})
        context = H.build_context(journal=journal)
        state = commands.post_acceptance_transition_state(context)
        self.assertIsNotNone(state["contradiction"])
        self.assertIsNone(state["transition_scope"])

    def test_R_SB35_binding_3_keeps_Q_first_validations_IA_fields(self):
        """R-SB35 -- Q holds TWO complete same-scope validations.

        Proved on the copied REAL state, whose one scope genuinely holds two:
        the anchor at event_seq 1 and the effective set at event_seq 6.
        Binding 3 must keep the FIRST validation's IA fields, field for field,
        and take ONLY the EV trio from the later effective validation -- and
        the custody replay must still succeed.
        """
        _c, events, state, scope, anchor, effective = multi_validation_scope_facts()
        q_validations = [
            event for event in events
            if event["type"] == "validation_recorded"
            and event.get("package_scope_id") == scope
        ]
        self.assertGreater(len(q_validations), 1, "the scope has two validations")
        first = q_validations[0]
        self.assertEqual(first["event_seq"], anchor["event_seq"])

        errors = []
        transition = nh_loop.build_transition_context(
            "post_validation",
            {"package_scope_id": scope,
             "scope_root_path": anchor["package_source_binding"]["scope_root_path"]},
            errors,
        )
        self.assertIsNotNone(transition, errors)
        binding = transition.binding
        # ---- IA: Q's FIRST validation, field for field, UNCHANGED ----
        self.assertEqual(binding.package_scope_id, first["package_scope_id"])
        self.assertEqual(binding.package_key, first["package_key"])
        self.assertEqual(binding.package_id, first["package_id"])
        self.assertEqual(binding.scope_root_path,
                         first["package_source_binding"]["scope_root_path"])
        self.assertEqual(binding.branch, first["branch"])
        self.assertEqual(binding.head_sha, first["head_sha"])
        self.assertEqual(binding.source_binding_sha256,
                         first["source_binding_sha256"])
        self.assertEqual(binding.terminal_chain_sha256,
                         first["source_binding_sha256"])
        # ---- EV: ONLY these three, from the LATER effective validation ----
        self.assertEqual(binding.source_manifest_sha256,
                         effective["source_manifest_sha256"])
        self.assertEqual(set(binding.required_source_paths),
                         set(effective["source_paths_checked"]))
        self.assertEqual(binding.validation_set_id,
                         effective["validation_set_id"])
        self.assertNotEqual(first["validation_set_id"],
                            effective["validation_set_id"])
        # ---- round-zero is unchanged: Q's proved bound root ----
        self.assertEqual(transition.round_zero_candidate.candidate_path,
                         binding.scope_root_path)
        # ---- and the custody replay STILL SUCCEEDS ----
        chain_errors = []
        self.assertIsNotNone(
            nh_loop.authenticated_candidate_custody(events, chain_errors),
            chain_errors,
        )
        self.assertEqual(chain_errors, [])

    def test_R_SB37_source_current_while_a_blocking_question_is_stale(self):
        """R-SB37 -- FAMILY A true, FAMILY B blocking.  Both, at once, correctly.

        A package may be source-current while a blocking Ness question is
        stale.  In that state source_state_current is TRUE, the Piece-3 gate
        stays CLOSED, stale_question_ids names the question, and the installed
        INTERVIEW_GATE_SOURCE_DRIFT reason is still emitted from family B's own
        site.  This proves the family-A extraction weakened no Piece-3 safety.
        """
        # FAMILY A current: no set staleness, every page manifest re-derives.
        cache = {}
        state = synthetic_state(complete_set(SCOPE_P, "vs_1", 1))
        current_set = complete_set(
            SCOPE_P, "vs_1", 1,
            manifests={1: {"checked_paths": ["a.md"], "manifest_sha256": "M"}},
        )

        real_recompute = nh_loop.recompute_manifest_sha256
        real_fresh = nh_loop.interview_question_is_fresh
        try:
            # Every stored PAGE manifest re-derives -> family A is CURRENT.
            nh_loop.recompute_manifest_sha256 = (
                lambda paths, binding, errors: "M"
            )
            verdict = nh_loop.package_source_family_a(
                state, SCOPE_P, {"binding_sha256": "x"}, current_set
            )
            self.assertTrue(verdict["source_state_current"],
                            "FAMILY A is CURRENT")
            self.assertFalse(verdict["validation_set_stale"])
            self.assertFalse(verdict["manifest_drifted"])
            self.assertIsNone(verdict["source_currentness_reason"])
            # FAMILY B is a SEPARATE question over each question's OWN grounding.
            nh_loop.interview_question_is_fresh = (
                lambda question, binding, cache: False
            )
            self.assertFalse(
                nh_loop.interview_question_is_fresh({"question_id": "q1"},
                                                    None, {})
            )
        finally:
            nh_loop.recompute_manifest_sha256 = real_recompute
            nh_loop.interview_question_is_fresh = real_fresh

        # The two families are structurally separate in the installed gate:
        # family B's emit site is its own, and the projection never computes B.
        source = H.read_text(H.CONTROLLER_DIR / "nh_loop.py")
        marker = source.index("def package_source_family_a(")
        body = source[marker:source.index("\ndef package_source_currentness(")]
        for forbidden in ("interview_question_is_fresh", "stale_question_ids",
                          "INTERVIEW_BLOCKING_STATUSES"):
            self.assertNotIn(forbidden, body,
                             "family A must NOT absorb family B: " + forbidden)
        # ...and family B is still exactly where it was, with its own emit.
        gate = source[source.index("def evaluate_interview_clearance("):]
        self.assertIn("interview_question_is_fresh(question, freshness_binding, cache)",
                      gate)
        self.assertIn('clearance["stale_question_ids"] = stale', gate)
        self.assertIn("if drifted or stale:", gate)

    def test_R_SB37b_the_gate_still_closes_on_a_stale_question(self):
        """FAMILY B, end to end, on the copied real state: the gate is closed
        and stale_question_ids is produced ONLY here."""
        _c, _e, _s, scope, _a, _ev = live_scope_facts()
        clearance = nh_loop.evaluate_interview_clearance(scope)
        self.assertIn("stale_question_ids", clearance)
        self.assertIsInstance(clearance["stale_question_ids"], list)
        self.assertFalse(clearance["unlocked"], "the gate is CLOSED")
        report = H.run_live_copy("supervisor-status")
        self.assertNotIn("stale_question_ids", report)

    def test_R_SB38_T4_carries_a_COMPLETE_source_bearing_inventory(self):
        """R-SB38 -- T4 is NOT source-free.

        (a) unchanged, it reconstructs exactly; (b) changing ANY field that
        really participates -- a BASE field or frozen_source_binding_sha256 in
        its own extra -- makes it stale; (c) changing something that is NOT in
        the inventory manufactures NO staleness; (d) its stage extra still
        carries exactly prepared_target_path and prepared_specification_sha256.
        """
        journal = H.staged_journal("initial_pending")
        context = H.build_context(
            journal=journal,
            binding=H.make_binding(SCOPE_Q, root=ROOT_Q, validation_set_id="vs_q"),
            candidate=H.make_candidate(ROOT_Q),
            clearance=lambda scope: {"unlocked": True},
        )
        situation = status_mod.Situation(context, journal.read())
        work_item, _id = engine.initial_design_work_item(
            context, context.round_zero_candidate, TARGET_Q
        )
        base = engine.required_inputs_inventory(context, work_item, {})
        # (d) -- the BASE inventory is source-bearing for T4 too.
        for field in ("candidate_sha256", "candidate_bytes",
                      "source_binding_sha256", "source_manifest_sha256",
                      "settled_decision_binding_sha256",
                      "required_source_paths", "extra"):
            self.assertIn(field, base, field)
        spec = H.prepared_task_object()["mechanical_design_specification"] \
            if "mechanical_design_specification" in H.prepared_task_object() \
            else {"a": "specification"}
        extra = {
            "prepared_target_path": TARGET_Q,
            "prepared_specification_sha256": "s" * 64,
            "frozen_source_binding_sha256": "b" * 64,
        }
        original = engine.required_inputs_sha256(context, work_item, extra)
        # (a) -- unchanged, it reconstructs EXACTLY.
        self.assertEqual(original,
                         engine.required_inputs_sha256(context, work_item, extra))
        # (b) -- every BASE field that really participates moves the digest.
        for field, value in (
            ("source_manifest_sha256", "9" * 64),
            ("required_source_paths", frozenset({"x.md"})),
            ("settled_decision_binding_sha256", "8" * 64),
            ("source_binding_sha256", "7" * 64),
        ):
            moved = dataclasses.replace(context.binding, **{field: value})
            probe = H.build_context(
                journal=journal, binding=moved,
                candidate=H.make_candidate(ROOT_Q),
                clearance=lambda scope: {"unlocked": True},
            )
            probe_item, _pid = engine.initial_design_work_item(
                probe, probe.round_zero_candidate, TARGET_Q
            )
            self.assertNotEqual(
                original,
                engine.required_inputs_sha256(probe, probe_item, extra),
                "a change to %s MUST move the digest" % field,
            )
        # ...and so does the frozen source in T4's OWN extra.
        for key in ("frozen_source_binding_sha256", "prepared_target_path",
                    "prepared_specification_sha256"):
            moved_extra = dict(extra)
            moved_extra[key] = "changed"
            self.assertNotEqual(
                original,
                engine.required_inputs_sha256(context, work_item, moved_extra),
                "a change to extra.%s MUST move the digest" % key,
            )
        # (c) -- something that is NOT part of the inventory manufactures NONE.
        unchanged_probe = H.build_context(
            journal=journal,
            binding=dataclasses.replace(context.binding,
                                        coverage_review_event_seq=999),
            candidate=H.make_candidate(ROOT_Q),
            clearance=lambda scope: {"unlocked": True},
        )
        probe_item, _pid = engine.initial_design_work_item(
            unchanged_probe, unchanged_probe.round_zero_candidate, TARGET_Q
        )
        self.assertEqual(
            original,
            engine.required_inputs_sha256(unchanged_probe, probe_item, extra),
            "a NON-input manufactures no staleness",
        )

    def test_R_SB38b_every_kind_reconstructs_its_own_complete_extra(self):
        """section 21.2 -- the reconstruction is PER KIND, never kind-blind."""
        journal = H.staged_journal("initial_pending")
        context = H.build_context(
            journal=journal,
            binding=H.make_binding(SCOPE_Q, root=ROOT_Q, validation_set_id="vs_q"),
            candidate=H.make_candidate(ROOT_Q),
            clearance=lambda scope: {"unlocked": True},
        )
        unscoped = replay_mod.Replay(journal.read())
        facts = {
            "selection": {
                "analysis": H.selection_object(),
                "root_identity": {"sha256": "9" * 64, "bytes": 4096},
                "package_scope_id": SCOPE_Q,
            },
            "prepared_task": {
                "target_path": TARGET_Q,
                "specification": {"a": "specification"},
            },
        }
        recon = commands._controller_extra_reconstruction(context, unscoped, facts)
        expected = {
            "next_package_selection": {"required_files_binding",
                                       "frozen_source_binding_sha256"},
            "next_design_task_preparation": {
                "required_files_binding", "admitted_selection",
                "selected_root_identity", "selected_scope",
                "settled_decision_binding_sha256",
                "frozen_source_binding_sha256"},
            "initial_design": {"prepared_target_path",
                               "prepared_specification_sha256",
                               "frozen_source_binding_sha256"},
        }
        request_by_kind = {
            "next_package_selection": "pr_sel",
            "next_design_task_preparation": "pr_prep",
            "initial_design": "pr_init",
        }
        for kind, keys in expected.items():
            extra = recon(request_by_kind[kind], kind)
            self.assertIsNotNone(extra, kind)
            self.assertEqual(set(extra), keys, kind)
        # An UNKNOWN kind is never given another kind's shape.
        self.assertIsNone(recon("pr_sel", "design_audit"))

    def test_R_SB31_the_legacy_one_shot_fence_is_not_reopened(self):
        """R-SB31 / SEL-LEGACY-ONE-SHOT -- once consumed, consumed for ever."""
        journal = H.accepted_journal()
        H.admitted_selection_state(journal)
        context = H.build_context(journal=journal)
        state = commands.post_acceptance_transition_state(context)
        self.assertTrue(state["legacy_replacement_consumed"],
                        "a current-contract request exists, so it is consumed")
        # A material source change makes the selection stale; the fence holds.
        adapter = H.StubAdapter()
        adapter.live_source_binding = H.STUB_CHANGED_SOURCE_BINDING
        moved = H.build_context(journal=journal, adapter=adapter)
        after = commands.post_acceptance_transition_state(moved)
        self.assertIsNone(after["selection"], "stale")
        self.assertTrue(after["legacy_replacement_consumed"],
                        "SEL-LEGACY-ONE-SHOT is NOT reopened by staleness")

    def test_R_SB21_restart_at_every_phase_creates_no_duplicate_request(self):
        """R-SB21 -- an admitted unconsumed selection short-circuits T1."""
        for stage in ("selection_required", "clearance_required",
                      "piece3_pending", "piece3_commit", "task_preparation",
                      "initial_design", "initial_pending", "handoff"):
            with self.subTest(stage=stage):
                journal = H.staged_journal(stage)
                transport = H.LoudStubTransport()
                appends = journal.appends
                context = H.build_context(
                    journal=journal, transport=transport,
                    clearance=lambda scope: {"unlocked": True},
                )
                first = commands.post_acceptance_transition_state(context)
                second = commands.post_acceptance_transition_state(context)
                self.assertEqual(first["transition_scope"],
                                 second["transition_scope"])
                self.assertEqual(
                    commands.loop_position(context, first)["loop_state"],
                    commands.loop_position(context, second)["loop_state"],
                )
                self.assertEqual(journal.appends, appends, "ZERO appends")
                self.assertEqual(transport.calls, [], "ZERO provider calls")


# ===========================================================================
# The boundary sweep every case must additionally satisfy (section 24.3).
# ===========================================================================
class BoundarySweepRehearsals(unittest.TestCase):

    def test_no_new_event_type_body_key_state_or_command_was_added(self):
        """section 24.3 / section 19 -- NEW_* = 0, everywhere."""
        from nh_supervisor import constants, schema
        self.assertEqual(
            sorted(constants.SUPERVISOR_COMMANDS),
            sorted(commands.COMMAND_TABLE),
        )
        # Every outward state this design uses is ALREADY GOVERNED.
        for name in ("LOOP_SELECTION_REQUIRED", "LOOP_WAITING_RECOVERING",
                     "LOOP_HANDOFF_COMPLETE", "LOOP_SAFETY_HOLD",
                     "LOOP_PACKAGE_CLEARANCE_REQUIRED"):
            self.assertTrue(hasattr(commands, name), name)
        # No new event type was introduced by the correction.
        source = H.read_text(H.CONTROLLER_DIR / "nh_supervisor" / "commands.py")
        self.assertNotIn('"source_currentness_recorded"', source)
        self.assertNotIn('"package_source_currentness_recorded"', source)
        loop_source = H.read_text(H.CONTROLLER_DIR / "nh_loop.py")
        self.assertNotIn('"type": "source_currentness', loop_source)

    def test_the_currentness_derivation_never_appends_or_dispatches(self):
        """F-12 -- a derivation that would need to append is a wiring defect."""
        loop_source = H.read_text(H.CONTROLLER_DIR / "nh_loop.py")
        marker = loop_source.index("def package_source_currentness(")
        body = loop_source[marker:loop_source.index(
            "\ndef evaluate_interview_clearance("
        )]
        code = strip_comments_and_docstrings(body)
        for forbidden in ("append_interview_event", "dispatch", "provider",
                          "subprocess", "socket", "urlopen"):
            self.assertNotIn(forbidden, code, forbidden)


# ===========================================================================
# The three cases the matrix names that the groups above do not carry alone.
# ===========================================================================
class RemainingMatrixRehearsals(unittest.TestCase):

    def test_R_SB13_a_saved_actionable_selection_goes_stale_on_a_source_change(self):
        """R-SB13 -- a saved ACTIONABLE T1 result, then a material source change.

        STALE; history preserved BYTE-IDENTICALLY; LOOP_SELECTION_REQUIRED with
        continue-design-loop; ZERO provider calls from the read-only derivation.
        (R-SB33 / R-SB41 prove the same rule for a ROOTLESS non-actionable
        answer; this is the ordinary actionable one.)
        """
        journal = H.accepted_journal()
        H.admitted_selection_state(journal)
        before_events = json.dumps(journal.events, sort_keys=True)
        appends = journal.appends

        # Unchanged source: ADMITTED.
        transport = H.LoudStubTransport()
        context = H.build_context(journal=journal, transport=transport)
        state = commands.post_acceptance_transition_state(context)
        self.assertIsNotNone(state["selection"], "unchanged source -> admitted")

        # A MATERIAL source change.
        adapter = H.StubAdapter()
        adapter.live_source_binding = H.STUB_CHANGED_SOURCE_BINDING
        moved = H.build_context(journal=journal, transport=transport,
                                adapter=adapter)
        after = commands.post_acceptance_transition_state(moved)
        report = commands.loop_position(moved, after)
        self.assertIsNone(after["selection"], "STALE")
        self.assertEqual(after["stop_record"]["loop_state"],
                         commands.LOOP_SELECTION_REQUIRED)
        self.assertEqual(report["loop_state"], commands.LOOP_SELECTION_REQUIRED)
        self.assertEqual(report["loop_next_command"], "continue-design-loop")
        self.assertEqual(json.dumps(journal.events, sort_keys=True),
                         before_events, "history byte-identical")
        self.assertEqual(journal.appends, appends, "ZERO appends")
        self.assertEqual(transport.calls, [], "ZERO provider calls")

    def test_R_SB16_restart_after_a_changed_source_is_stable_three_times(self):
        """R-SB16 -- the SAME stale result each time; ZERO appends throughout."""
        journal = H.accepted_journal()
        H.admitted_selection_state(journal)
        appends = journal.appends
        before_events = json.dumps(journal.events, sort_keys=True)
        adapter = H.StubAdapter()
        adapter.live_source_binding = H.STUB_CHANGED_SOURCE_BINDING
        transport = H.LoudStubTransport()
        answers = []
        for _ in range(3):
            context = H.build_context(journal=journal, transport=transport,
                                      adapter=adapter)
            state = commands.post_acceptance_transition_state(context)
            report = commands.loop_position(context, state)
            answers.append(json.dumps(
                {"selection": state["selection"],
                 "stop": state["stop_record"],
                 "loop_state": report["loop_state"],
                 "next": report["loop_next_command"]},
                sort_keys=True, default=str,
            ))
        self.assertEqual(len(set(answers)), 1, "identical on every restart")
        self.assertIn("LOOP_SELECTION_REQUIRED", answers[0])
        self.assertEqual(journal.appends, appends, "ZERO appends")
        self.assertEqual(json.dumps(journal.events, sort_keys=True),
                         before_events)
        self.assertEqual(transport.calls, [], "ZERO provider calls")

    def test_R_SB26_a_repeated_validation_set_id_cannot_yield_two_effectives(self):
        """R-SB26 / section 6.2 E -- a repeated validation_set_id is a contradiction.

        The INSTALLED replay owns this rule and it is UNCHANGED: validation sets
        are keyed by ``validation_set_id``, and a second page claiming an
        existing id whose declared shape disagrees is REFUSED outright, so two
        distinct complete sets can never share one id.  ``effective_validation``
        therefore has exactly one record per scope to resolve, and it resolves
        it by the authenticated first-page ``event_seq`` alone.
        """
        source = H.read_text(H.CONTROLLER_DIR / "nh_loop.py")
        # The installed refusal is still present and still unchanged.
        self.assertIn(
            "does not match the pages already recorded for", source,
            "the installed duplicate/mismatched-set refusal is intact",
        )
        # latest_complete_by_package holds exactly ONE record per scope.
        first = synthetic_validation(1, SCOPE_P, "vs_dup")
        second = synthetic_validation(9, SCOPE_P, "vs_dup")
        events = [first, second]
        state = synthetic_state(complete_set(SCOPE_P, "vs_dup", 9))
        self.assertEqual(len(state["latest_complete_by_package"]), 1)
        effective = nh_loop.effective_validation(state, events, SCOPE_P)
        self.assertEqual(effective["event_seq"], 9,
                         "resolved by the authenticated first-page seq alone")
        # And a same-scope pair whose identity disagrees is a CONTRADICTION.
        errors = []
        self.assertFalse(nh_loop.effective_validation_compatible(
            synthetic_validation(1, SCOPE_P, "vs_dup", root="A.md"),
            synthetic_validation(9, SCOPE_P, "vs_dup", root="B.md"),
            errors,
        ))
        self.assertIn("CONTRADICTION", errors[0])


# ===========================================================================
# THE INDEPENDENT-AUDIT CORRECTION.
#
# Three rehearsals that FAIL on an implementation in which
# package_source_currentness() is not the ONE snapshot-consistent,
# fresh-per-read currentness owner.  Accepted v1.3 sections 5.1, 5.4, 8.2,
# 13.4, 13.5, 21.1.
# ===========================================================================
import shutil          # noqa: E402
import subprocess      # noqa: E402
import tempfile        # noqa: E402
from unittest import mock  # noqa: E402


class OneOwnerSnapshotAndFreshnessRehearsals(unittest.TestCase):

    # -- A -------------------------------------------------------------------
    def test_currentness_is_derived_from_the_SAME_locked_snapshot(self):
        """section 13.4 -- ONE authenticated snapshot for the WHOLE report.

        ``supervisor_status()`` locks snapshot A.  Any SECOND independent
        journal read would expose a different snapshot B.  The projection must
        derive from A -- so the report's authenticated_event_seq,
        authenticated_tail_sha256 and source_currentness all describe ONE
        snapshot.

        A build whose projection re-reads the journal for itself gets B here
        and FAILS this rehearsal.
        """
        errors = []
        context = nh_loop.build_supervisor_context(errors)
        self.assertIsNotNone(context, errors)
        _c, _e, _s, scope, _a, effective = live_scope_facts()

        # re-cut 2026-09-02 against journal head 2300, under section 13.4 as
        # AMENDED by Ness on 2026-09-02: the REPORT derives from snapshot A, while
        # the privileged binding is rebuilt from ONE independently authenticated
        # re-read (Repair 14).  So a second read is EXPECTED -- exactly one --
        # and what must never happen is that its content changes what the
        # report says.  Any independent read returns snapshot B: an EMPTY
        # journal.  locked_snapshot() goes through read_interview_journal_SNAPSHOT
        # and is untouched, so A is still what the report is built from.
        #
        # The stub's signature matches read_interview_journal(errors,
        # allow_tail_recovery=False), which the privileged reader calls with
        # BOTH arguments positional.  The old one-argument stub raised TypeError
        # inside the binding and the assertion below could never fail.
        second_reads = []

        def snapshot_B(errs, allow_tail_recovery=False):
            second_reads.append(1)
            return ("<snapshot B>", [])

        with mock.patch.object(nh_loop, "read_interview_journal", snapshot_B):
            report = commands.supervisor_status(context).report

        # Measured 2026-09-02 at head 2300: the projection reports the source as
        # moved since the validation and stops BEFORE the privileged re-read,
        # so no second read is observed here today.  On a current binding the
        # Repair 14 re-read happens exactly once.  Either way it is bounded.
        self.assertLessEqual(
            len(second_reads), 1,
            "at most ONE privileged independent re-read is taken (Repair 14)",
        )
        self.assertEqual(report["authenticated_event_seq"], len(_e), "snapshot A")
        projection = report["source_currentness"]
        self.assertIsNotNone(projection, "the projection was still produced")
        # Snapshot B would have produced NO effective validation at all.
        self.assertIsNotNone(projection["effective_validation_set_id"])
        self.assertEqual(projection["effective_validation_set_id"],
                         effective["validation_set_id"])
        self.assertEqual(projection["effective_validation_event_seq"],
                         effective["event_seq"])
        self.assertEqual(projection["package_scope_id"], scope)

    def test_an_unauthenticated_read_claims_no_currentness(self):
        """F-5 -- an unreadable journal proves nothing and is never 'current'."""
        errors = []
        context = nh_loop.build_supervisor_context(errors)
        self.assertIsNotNone(context, errors)

        class Broken:
            def __getattr__(self, name):
                raise AssertionError("no journal")

        with mock.patch.object(type(context.journal), "snapshot",
                               lambda self: (_ for _ in ()).throw(
                                   RuntimeError("unreadable"))):
            report = commands.supervisor_status(context).report
        self.assertFalse(report["journal_authentication_proved"])
        self.assertIs(report["source_state_current"], False)
        self.assertIsNone(report["source_currentness"])

    # -- B -------------------------------------------------------------------
    def test_the_enforced_gate_CONSUMES_the_one_currentness_owner(self):
        """sections 5.4 / 13.5 / 21.1 -- ONE owner, reported and enforced.

        ``evaluate_interview_clearance()`` must CONSUME
        ``package_source_currentness()`` for FAMILY A.  This is proved by
        REPLACING the owner and watching the enforced gate change with it --
        not by computing family A separately and comparing booleans afterwards.
        """
        _c, events, state, scope, _a, _ev = live_scope_facts()
        calls = []
        real = nh_loop.package_source_currentness

        def recording(scope_arg, **kwargs):
            calls.append((scope_arg, sorted(kwargs)))
            return real(scope_arg, **kwargs)

        with mock.patch.object(nh_loop, "package_source_currentness", recording):
            nh_loop.evaluate_interview_clearance(scope)
        self.assertTrue(calls, "the gate did NOT consume the projection owner")
        self.assertEqual(calls[0][0], scope, "for the scope it is deciding")
        self.assertIn("with_internals", calls[0][1])
        self.assertIn("events", calls[0][1], "handed the gate's OWN snapshot")
        self.assertIn("state", calls[0][1], "and its OWN replayed state")

        # Replace the OWNER's verdict; the ENFORCED gate must move with it.
        def owner_says(current):
            def fake(scope_arg, **kwargs):
                projection, internals = real(scope_arg, **kwargs)
                internals["family_a"] = dict(
                    internals["family_a"],
                    validation_set_stale=not current,
                    manifest_drifted=False,
                    source_state_current=current,
                    source_currentness_reason=(
                        None if current
                        else nh_loop.SOURCE_CURRENTNESS_VALIDATION_STALE
                    ),
                )
                return projection, internals
            return fake

        with mock.patch.object(nh_loop, "package_source_currentness",
                               owner_says(False)):
            stale_gate = nh_loop.evaluate_interview_clearance(scope)
        with mock.patch.object(nh_loop, "package_source_currentness",
                               owner_says(True)):
            current_gate = nh_loop.evaluate_interview_clearance(scope)

        self.assertIn(nh_loop.INTERVIEW_GATE_SOURCE_DRIFT,
                      stale_gate["reasons"],
                      "the owner said STALE; the enforced gate must say so")
        # With the owner reporting CURRENT, family A contributes no drift.  Any
        # remaining drift reason can only be FAMILY B's own emit.
        self.assertNotEqual(stale_gate["reasons"], current_gate["reasons"],
                            "the enforced gate tracks the owner's verdict")

    def test_FAMILY_B_stays_independent_and_still_closes_the_gate(self):
        """section 13.5 -- family A current, one blocking question stale: the gate
        is CLOSED, from FAMILY B's OWN site, and B was not weakened."""
        _c, _e, _s, scope, _a, _ev = live_scope_facts()
        real = nh_loop.package_source_currentness

        def always_current(scope_arg, **kwargs):
            projection, internals = real(scope_arg, **kwargs)
            if internals is not None:
                internals["family_a"] = dict(
                    internals["family_a"],
                    validation_set_stale=False,
                    manifest_drifted=False,
                    source_state_current=True,
                    source_currentness_reason=None,
                )
            return projection, internals

        with mock.patch.object(nh_loop, "package_source_currentness",
                               always_current):
            with mock.patch.object(nh_loop, "interview_question_is_fresh",
                                   lambda q, b, c: False):
                gate = nh_loop.evaluate_interview_clearance(scope)
        self.assertFalse(gate["unlocked"], "the Piece-3 gate stays CLOSED")
        if gate["blocking_question_ids"]:
            self.assertTrue(gate["stale_question_ids"],
                            "family B still names the stale question")
            self.assertIn(nh_loop.INTERVIEW_GATE_SOURCE_DRIFT, gate["reasons"],
                          "family B's OWN outward reason is still emitted")

    def test_family_B_reuses_the_projections_ONE_reconstruction(self):
        """section 8.2 'One reconstruction, not two.'"""
        _c, _e, _s, scope, _a, _ev = live_scope_facts()
        built = []
        real_custody = nh_loop.custody_effective_source_binding

        def counting(state, scope_arg, binding):
            built.append(scope_arg)
            return real_custody(state, scope_arg, binding)

        with mock.patch.object(nh_loop, "custody_effective_source_binding",
                               counting):
            nh_loop.evaluate_interview_clearance(scope)
        self.assertEqual(
            len([s for s in built if s == scope]), 1,
            "exactly ONE reconstruction is performed for the scope, and family "
            "B reuses it rather than computing a second",
        )

    # -- C -------------------------------------------------------------------
    def test_each_currentness_read_opens_a_FRESH_source_reproof_episode(self):
        """section 5.1 -- object L is recomputed on EVERY read.

        The caller must NOT have to remember to reset the process-cached source
        re-proof context.  A build that answers a currentness read from an
        episode an EARLIER context build populated FAILS this rehearsal.
        """
        _c, _e, _s, scope, _a, _ev = live_scope_facts()
        # Prime the cache exactly as an earlier replay / context build would.
        nh_loop.interview_source_reproof_context()
        primed = nh_loop._INTERVIEW_REPROOF_CACHE.get("context")
        self.assertIsNotNone(primed, "the cache is primed")
        primed["__stale_episode_marker__"] = True

        # NO manual reset by the caller.
        nh_loop.package_source_currentness(scope)

        after = nh_loop._INTERVIEW_REPROOF_CACHE.get("context")
        self.assertIsNotNone(after)
        self.assertIsNot(after, primed,
                         "the projection reused the EARLIER episode")
        self.assertNotIn("__stale_episode_marker__", after,
                         "the projection reused the EARLIER episode's bytes")

    def test_changed_source_bytes_are_seen_without_any_caller_reset(self):
        """section 5.1 -- a CHECKED source file's bytes change in place, same path.

        No filename change, and NO caller-side
        reset_interview_source_reproof_cache().  The next currentness read must
        observe the new bytes.
        """
        _c, _e, _s, scope, _a, _ev = live_scope_facts()
        saved_repo = nh_loop.NH_REPO_PATH
        temp = tempfile.mkdtemp(prefix="nh_sbc_", dir=str(H.SCRATCH_DIR))
        try:
            repo = os.path.join(temp, "NH-GOVERNANCE")
            shutil.copytree(saved_repo, repo)
            nh_loop.NH_REPO_PATH = repo

            # Prime the episode against the UNMODIFIED tree.
            nh_loop.interview_source_reproof_context()
            before_ctx = nh_loop._INTERVIEW_REPROOF_CACHE["context"]
            before_binding = before_ctx["binding_sha256"]
            before_index = set((before_ctx["index"] or {}).get("by_path") or ())
            self.assertIsNotNone(before_binding)

            # Change a CHECKED source file's BYTES IN PLACE.  Same path.
            target = os.path.join(repo, "01_AUTHORITATIVE", "cursorrules")
            self.assertTrue(os.path.isfile(target), target)
            with open(target, "a", encoding="utf-8") as handle:
                handle.write("\n<!-- disposable rehearsal byte change -->\n")

            # NO reset here.  This is the whole point.
            projection = nh_loop.package_source_currentness(scope)

            after_ctx = nh_loop._INTERVIEW_REPROOF_CACHE["context"]
            self.assertIsNot(after_ctx, before_ctx,
                             "the read reused the primed episode")
            self.assertNotEqual(
                after_ctx["binding_sha256"], before_binding,
                "the fresh episode did NOT observe the changed bytes",
            )
            self.assertIsNotNone(projection)
            self.assertFalse(projection["source_state_current"],
                             "a changed checked source is NOT current")
            self.assertIsNotNone(projection["source_currentness_reason"])
            self.assertEqual(
                set((after_ctx["index"] or {}).get("by_path") or ()),
                before_index,
                "the same paths -- only the BYTES moved",
            )
        finally:
            nh_loop.NH_REPO_PATH = saved_repo
            shutil.rmtree(temp, ignore_errors=True)
            nh_loop.reset_interview_source_reproof_cache()


class HistoricalSourceExclusionRehearsals(unittest.TestCase):
    """Archived candidates stay on disk but never enter live-loop source input."""

    def test_history_is_absent_while_master_accepted_and_active_remain(self):
        saved_repo = nh_loop.NH_REPO_PATH
        temp = tempfile.mkdtemp(prefix="nh_history_exclusion_", dir=str(H.SCRATCH_DIR))
        try:
            repo = os.path.join(temp, "NH-GOVERNANCE")
            paths = {
                "01_AUTHORITATIVE/MASTER.md": b"master",
                "04_ACCEPTED_STANDALONE_DESIGNS/ACCEPTED.md": b"accepted",
                "05_ACTIVE_CANDIDATE/ACTIVE.md": b"active",
                "99_HISTORICAL_CANDIDATES/OLD.md": b"old",
            }
            for rel, blob in paths.items():
                full = os.path.join(repo, rel)
                os.makedirs(os.path.dirname(full), exist_ok=True)
                with open(full, "wb") as handle:
                    handle.write(blob)
            nh_loop.NH_REPO_PATH = repo

            errors = []
            index = nh_loop.index_repository_documents(errors)
            self.assertIsNotNone(index, errors)
            self.assertIn("01_AUTHORITATIVE/MASTER.md", index["by_path"])
            self.assertIn(
                "04_ACCEPTED_STANDALONE_DESIGNS/ACCEPTED.md", index["by_path"]
            )
            self.assertIn("05_ACTIVE_CANDIDATE/ACTIVE.md", index["by_path"])
            self.assertNotIn(
                "99_HISTORICAL_CANDIDATES/OLD.md", index["by_path"]
            )

            inventory = nh_loop.repository_category_inventory(errors)
            self.assertIsNotNone(inventory, errors)
            self.assertNotIn("historical_candidate", inventory)

            names = nh_loop.find_files(repo, errors)
            self.assertNotIn("OLD.md", names)
            self.assertIn("MASTER.md", names)

            self.assertEqual(
                nh_loop.find_package_id_evidence("old"), [],
                "an identifier found only in archived history is not live evidence",
            )
        finally:
            nh_loop.NH_REPO_PATH = saved_repo
            shutil.rmtree(temp, ignore_errors=True)

    def test_fresh_provider_evidence_cannot_name_history(self):
        saved_repo = nh_loop.NH_REPO_PATH
        temp = tempfile.mkdtemp(prefix="nh_history_evidence_", dir=str(H.SCRATCH_DIR))
        try:
            repo = os.path.join(temp, "NH-GOVERNANCE")
            rel = "99_HISTORICAL_CANDIDATES/OLD.md"
            full = os.path.join(repo, rel)
            os.makedirs(os.path.dirname(full), exist_ok=True)
            with open(full, "wb") as handle:
                handle.write(b"old")
            nh_loop.NH_REPO_PATH = repo
            errors = []
            self.assertIsNone(nh_loop.validate_source_paths([rel], "test", errors))
            self.assertTrue(errors)
        finally:
            nh_loop.NH_REPO_PATH = saved_repo
            shutil.rmtree(temp, ignore_errors=True)

    def test_history_only_worktree_entries_do_not_change_live_source_state(self):
        porcelain = "\n".join(
            (
                "?? 99_HISTORICAL_CANDIDATES/OLD.md",
                "?? 05_ACTIVE_CANDIDATE/ACTIVE.md",
            )
        )
        with mock.patch.object(nh_loop, "read_head_sha", return_value="h" * 40):
            with mock.patch.object(
                nh_loop, "run_git", return_value=(True, porcelain, None)
            ):
                state = nh_loop.read_source_state("test", [])
        self.assertEqual(
            state["worktree_entries"], ["?? 05_ACTIVE_CANDIDATE/ACTIVE.md"]
        )

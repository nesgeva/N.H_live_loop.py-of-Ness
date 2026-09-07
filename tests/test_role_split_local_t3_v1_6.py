#!/usr/bin/env python3
"""OFFLINE rehearsals for the accepted N.H ROLE-SPLIT SUPERSESSION v1_6 design.

Source of obligations:
``NH-GOVERNANCE/05_ACTIVE_CANDIDATE/
NH_LIVE_DESIGN_LOOP_CLAUDE_DESIGN_CODEX_AUDIT_ROLE_SPLIT_SUPERSESSION_v1_6_CANDIDATE.md``
SHA-256 a498f24255946a0881a5cb47d8531271e20351e1db7f3527288a1d0fc9b29976.
Section 10 focused installation tests.

EVERY rehearsal here runs OFFLINE against a DISPOSABLE journal.  None appends to
the real journal, none touches the LIVE workspace, and none contacts a provider:
the transport FAILS LOUDLY the instant it is reached.

The canonical v1_8 harness is REUSED WHOLESALE.  No parallel test system, no
second journal, no second fixture family is created here.
"""

from __future__ import annotations

import base64
import copy
import json
import unittest

import os
import sys

sys.dont_write_bytecode = True

_TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
if _TESTS_DIR not in sys.path:
    sys.path.insert(0, _TESTS_DIR)

import test_post_acceptance_continuation_v1_8 as H  # noqa: E402

nh_loop = H.nh_loop
commands = H.commands
constants = H.constants
engine = H.engine
identity = H.identity
replay_mod = H.replay
SupervisorRefusal = H.SupervisorRefusal

MASTER_PATH = "01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md"
# A target the stub adapter does NOT report as a new candidate path -- the
# ordinary post-T4 situation, in which a historical prepared task is no longer
# re-admissible because its target has since been created.
OCCUPIED_TARGET = "05_ACTIVE_CANDIDATE/NH_ALREADY_WRITTEN_v9_9_CANDIDATE.md"

SCOPE_Q = H.SCOPE_Q
ROOT_Q = H.ROOT_Q
TARGET_Q = H.TARGET_Q


# ===========================================================================
# Local fixtures.  Each is one small arrangement over the SHARED harness.
# ===========================================================================
STOP_SIGNAL = {
    "issue_key": "initial_design_possible_ness_choice",
    "finding_key": "a" * 32,
    "signal_title": "The envelope leaves a real Ness choice unsettled",
    "finding_evidence": ["the envelope settles no policy for this mechanism"],
    "source_evidence": [MASTER_PATH],
}


def stop_result_body(signal=None):
    """The EXACT accepted three-key STOP result."""
    return {
        "result_schema_id": constants.INITIAL_DESIGN_STOP_RESULT_SCHEMA_ID,
        "result_schema_version": constants.INITIAL_DESIGN_STOP_RESULT_VERSION,
        "stop_review_signal": dict(signal or STOP_SIGNAL),
    }


def anchor_validation(journal, scope=SCOPE_Q, root=ROOT_Q):
    """Q's FIRST authenticated validation -- the IA anchor both sides read."""
    return journal.append(
        {
            "type": "validation_recorded",
            "package_scope_id": scope,
            "validation_set_id": "vs_q",
            "package_key": "no_controlled_id_settled_yet",
            "package_id": None,
            "package_source_binding": {"scope_root_path": root},
            "branch": "nh-design-loop",
            "head_sha": "a" * 40,
            "source_binding_sha256": "b" * 64,
        }
    )


def stop_custody(journal, *, scope=SCOPE_Q, request="pr_stop", value=None,
                 terminal_kind="result_received"):
    """One custodied initial-design result, inline, with its terminal."""
    payload = json.dumps(
        value if value is not None else stop_result_body(), sort_keys=True
    ).encode("utf-8")
    journal.append(
        {
            "type": "provider_request_prepared",
            "package_scope_id": scope,
            "provider_request_identity": request,
            "provider_kind": "claude_initial_design",
            "work_item_identity": "wi_init",
            "prompt_material_sha256": "1" * 64,
            "required_inputs_sha256": "2" * 64,
            "result_schema_id": constants.INITIAL_DESIGN_RESULT_SCHEMA_ID,
        }
    )
    journal.append(
        {
            "type": "provider_dispatch_begun",
            "package_scope_id": scope,
            "provider_request_identity": request,
            "provider_kind": "claude_initial_design",
        }
    )
    custody = journal.append(
        {
            "type": "provider_result_custody_recorded",
            "package_scope_id": scope,
            "provider_request_identity": request,
            "provider_kind": "claude_initial_design",
            "work_item_kind": "initial_design",
            "work_item_identity": "wi_init",
            "result_custody_identity": "rc_" + request,
            "result_location_kind": "inline_journal_bytes",
            "result_bytes_base64": base64.b64encode(payload).decode("ascii"),
            "result_byte_length": len(payload),
            "result_sha256": H.hashlib.sha256(payload).hexdigest(),
            "result_schema_valid": True,
            "result_origin": "local_completion",
            "result_schema_id": constants.INITIAL_DESIGN_RESULT_SCHEMA_ID,
        }
    )
    terminal = journal.append(
        {
            "type": "provider_request_terminal_recorded",
            "package_scope_id": scope,
            "provider_request_identity": request,
            "provider_kind": "claude_initial_design",
            "terminal_kind": terminal_kind,
            "result_custody_identity": "rc_" + request,
            "result_schema_valid": terminal_kind == "result_received",
        }
    )
    return custody, terminal


def expected_signal_record(scope=SCOPE_Q, signal=None, root=ROOT_Q):
    """The ONE shared expectation, through the ONE shared function."""
    return replay_mod.stop_closure_expected_record(
        scope,
        signal or STOP_SIGNAL,
        package_key="no_controlled_id_settled_yet",
        package_id=None,
        scope_root_path=root,
    )


def append_signal(journal, *, scope=SCOPE_Q, signal=None, overrides=None):
    """Append one review_signal_recorded matching the shared expectation."""
    body = dict(expected_signal_record(scope, signal))
    body.update(overrides or {})
    return journal.append(body)


def stop_context(journal, *, transport=None, clearance_unlocked=True):
    """A disposable Q-bound context able to process a custodied STOP."""
    context = H.build_context(
        SCOPE_Q,
        journal=journal,
        transport=transport or H.LoudStubTransport(),
        binding=H.make_binding(SCOPE_Q, root=ROOT_Q, validation_set_id="vs_q"),
        candidate=H.make_candidate(ROOT_Q),
        clearance=lambda scope_id: {"unlocked": clearance_unlocked},
    )
    context.review_signal_adapter = engine.ReviewSignalAdapter(
        validate_source_paths=nh_loop.spec_evidence_paths,
        validate_review_signal=nh_loop.validate_review_signal,
        record_review_signal=None,
    )
    return context


class RecordingSignalAdapter:
    """The recorder, stubbed to append EXACTLY what the installed one writes."""

    def __init__(self, journal, *, scope=SCOPE_Q, root=ROOT_Q, times=1,
                 overrides=None):
        self.journal = journal
        self.scope = scope
        self.root = root
        self.times = times
        self.overrides = overrides
        self.calls = 0
        self.validate_review_signal = nh_loop.validate_review_signal
        self.validate_source_paths = nh_loop.spec_evidence_paths

    def record_review_signal(self, signal, source, package_id, scope_id,
                             scope_root, candidate, errors, expected=None):
        self.calls += 1
        assert source == constants.STOP_REVIEW_SIGNAL_SOURCE
        assert candidate is None, "a STOP is bound to NO candidate"
        for _ in range(self.times):
            append_signal(
                self.journal, scope=scope_id, signal=signal,
                overrides=self.overrides,
            )
        return {"routed_signal_id": "recorded"}


# ===========================================================================
# section 10.1 -- LOCAL T3 AND THE CANONICAL ENVELOPE.
# ===========================================================================
class LocalT3Rehearsals(unittest.TestCase):

    def test_10_1_1_local_T3_makes_zero_provider_calls(self):
        """1 -- the command creates zero provider lifecycle records/calls."""
        journal = H.accepted_journal()
        binding = H.make_binding(SCOPE_Q, root=ROOT_Q, validation_set_id="vs_q")
        H.admitted_selection_state(
            journal, binding=binding, candidate=H.make_candidate(ROOT_Q)
        )
        transport = H.LoudStubTransport()
        context = H.build_context(
            SCOPE_Q, journal=journal, transport=transport, binding=binding,
            candidate=H.make_candidate(ROOT_Q),
            clearance=lambda scope_id: {"unlocked": True},
        )
        before = len(journal.events)
        with H.proved_acceptance():
            try:
                commands.prepare_next_design_task(context)
            except SupervisorRefusal:
                pass  # a NOT-READY refusal is a legitimate outcome here
        self.assertEqual(transport.calls, [], "local T3 contacts nobody")
        provider_types = {
            "provider_request_prepared", "provider_dispatch_begun",
            "provider_result_custody_recorded",
            "provider_request_terminal_recorded",
        }
        appended = [event["type"] for event in journal.events[before:]]
        self.assertEqual(
            [kind for kind in appended if kind in provider_types], [],
            "local T3 opens NO provider lifecycle record",
        )

    def test_10_1_1b_the_command_is_classified_provider_free(self):
        """section 5.1 -- retained in no 'may contact a provider' set."""
        self.assertNotIn(
            "prepare-next-design-task", constants.PROVIDER_DISPATCH_COMMANDS
        )
        self.assertNotIn(
            "prepare-next-design-task",
            constants.CONTINUATION_PROVIDER_CONTACTING_COMMANDS,
        )
        self.assertIn(
            "prepare-next-design-task",
            constants.CONTINUATION_PROVIDER_FREE_COMMANDS,
        )
        self.assertNotIn(
            "prepare-next-design-task", H.ui_worker.PROVIDER_CONTACTING_COMMANDS
        )
        # ...and it is STILL a real command and a real worker branch.
        self.assertIn("prepare-next-design-task", constants.SUPERVISOR_COMMANDS)
        self.assertIn("prepare-next-design-task", commands.COMMAND_TABLE)
        self.assertIn("prepare-next-design-task", H.ui_worker.WORKER_COMMANDS)

    def test_10_1_4a_the_envelope_carries_exactly_twelve_keys(self):
        """4a -- exactly its twelve keys; extra/missing/unprovable refuses."""
        self.assertEqual(len(constants.LOCAL_T3_ENVELOPE_KEYS), 12)
        self.assertEqual(len(set(constants.LOCAL_T3_ENVELOPE_KEYS)), 12)
        self.assertEqual(
            set(constants.LOCAL_T3_ENVELOPE_KEYS),
            {
                "envelope_version", "package", "package_root_identity",
                "authority_required_files_sha256", "source_currentness",
                "relevant_source_closure", "required_source_paths",
                "question_clearance", "settled_decision_binding_sha256",
                "unsatisfied_dependency_keys", "target", "work_boundary",
            },
        )

    def test_10_1_4a_extra_or_missing_field_refuses_the_position(self):
        """4a -- a widened or narrowed envelope is REFUSED, not accepted."""
        good = self.sample_envelope()
        for mutate, why in (
            (lambda e: e.update({"extra_field": 1}), "an extra key"),
            (lambda e: e.pop("work_boundary"), "a missing key"),
        ):
            envelope = copy.deepcopy(good)
            mutate(envelope)
            position, reason = self.derive_with(envelope)
            self.assertIsNone(position, "%s must refuse the envelope" % why)
            self.assertEqual(reason, commands.LOCAL_T3_NOT_READY_ENVELOPE, why)
        position, reason = self.derive_with(good)
        self.assertIsNotNone(position, "the exact twelve keys are accepted")
        self.assertIsNone(reason)

    def test_10_1_4a_unlocked_and_dependency_gates_fail_closed(self):
        """section 9.2 -- an un-unlocked clearance or any unsatisfied
        dependency refuses, rather than being carried as a false."""
        locked = copy.deepcopy(self.sample_envelope())
        locked["question_clearance"]["unlocked"] = False
        position, reason = self.derive_with(locked)
        self.assertIsNone(position)
        self.assertEqual(reason, commands.LOCAL_T3_NOT_READY_CLEARANCE)
        owed = copy.deepcopy(self.sample_envelope())
        owed["unsatisfied_dependency_keys"] = ["dep_a"]
        position, reason = self.derive_with(owed)
        self.assertIsNone(position)
        self.assertEqual(reason, commands.LOCAL_T3_NOT_READY_DEPENDENCY)

    # -- helpers ---------------------------------------------------------
    def sample_envelope(self, target=TARGET_Q):
        return {
            "envelope_version": constants.LOCAL_T3_ENVELOPE_SCHEMA_ID,
            "package": {
                "package_key": "no_controlled_id_settled_yet",
                "package_id": None,
                "package_scope_id": SCOPE_Q,
                "scope_root_path": ROOT_Q,
                "package_binding_sha256": "9" * 64,
            },
            "package_root_identity": [
                {"path": ROOT_Q, "sha256": "9" * 64, "bytes": 4096}
            ],
            "authority_required_files_sha256": "8" * 64,
            "source_currentness": {
                "anchor_source_binding_sha256": "b" * 64,
                "effective_validation_set_id": "vs_q",
                "effective_source_manifest_sha256": "d" * 64,
                "effective_source_binding_sha256": "b" * 64,
                "source_state_current": True,
            },
            "relevant_source_closure": {
                "closure_sha256": "7" * 64, "paths": [MASTER_PATH],
            },
            "required_source_paths": [MASTER_PATH],
            "question_clearance": {
                "unlocked": True,
                "validation_set_id": "vs_q",
                "coverage_review_validation_set_id": "vs_q",
                "coverage_review_current": True,
                "standing_chain_sha256": "e" * 64,
            },
            "settled_decision_binding_sha256": "c" * 64,
            "unsatisfied_dependency_keys": [],
            "target": {
                "target_path": target,
                "target_rule_id": constants.LOCAL_T3_INITIAL_TARGET_RULE_ID,
            },
            "work_boundary": {
                "one_file_only": True,
                "design_only": True,
                "build_vs_borrow_required": True,
            },
        }

    def derive_with(self, envelope, target=TARGET_Q):
        """Run the installed position derivation over a supplied envelope."""
        adapter = H.StubAdapter()
        adapter.build_local_task_envelope = (
            lambda *a, **k: copy.deepcopy(envelope)
        )
        adapter.derive_initial_target_path = lambda root, errors: target
        journal = H.accepted_journal()
        context = H.build_context(
            SCOPE_Q, journal=journal, adapter=adapter,
            binding=H.make_binding(SCOPE_Q, root=ROOT_Q, validation_set_id="vs_q"),
            candidate=H.make_candidate(ROOT_Q),
        )
        state = {
            "selection": {"scope_root_path": ROOT_Q},
            "transition_scope": SCOPE_Q,
        }
        return commands._derive_local_task_envelope_position(
            context, journal.read(), state
        )


class FirstTargetRehearsals(unittest.TestCase):
    """section 10.1 test 4 -- the ONE controller-derived first target."""

    def test_the_rule_strips_exactly_and_appends_the_fixed_component(self):
        errors = []
        target = nh_loop.derive_initial_target_path(
            "05_ACTIVE_CANDIDATE/NH_THING_v2_3_CANDIDATE.md", errors
        )
        self.assertEqual(
            target,
            "05_ACTIVE_CANDIDATE/NH_THING_NH_LIVE_LOOP_DESIGN_v1_0_CANDIDATE.md",
        )
        self.assertEqual(errors, [])

    def test_a_root_already_at_v1_0_does_not_derive_its_own_path(self):
        """A root named <stem>_v1_0_CANDIDATE.md derives the DESIGN name."""
        errors = []
        target = nh_loop.derive_initial_target_path(
            "05_ACTIVE_CANDIDATE/NH_OTHER_v1_0_CANDIDATE.md", errors
        )
        self.assertEqual(
            target,
            "05_ACTIVE_CANDIDATE/NH_OTHER_NH_LIVE_LOOP_DESIGN_v1_0_CANDIDATE.md",
        )
        self.assertNotEqual(target, "05_ACTIVE_CANDIDATE/NH_OTHER_v1_0_CANDIDATE.md")

    def test_a_non_md_root_and_an_empty_stem_both_stop(self):
        for root in ("05_ACTIVE_CANDIDATE/NH_THING", "05_ACTIVE_CANDIDATE/_v1_0_CANDIDATE.md"):
            errors = []
            self.assertIsNone(nh_loop.derive_initial_target_path(root, errors))
            self.assertTrue(errors, root)

    def test_an_appeared_target_refuses_rather_than_renaming(self):
        """An APPEARED target causes refusal, never renaming, never overwrite.

        The decision is the EXISTING gate's: is_new_candidate_path() owns
        containment, the no-symlink proof and target NON-EXISTENCE, and this
        rule stops when it says no rather than versioning around it.
        """
        installed = nh_loop.is_new_candidate_path
        try:
            nh_loop.is_new_candidate_path = lambda value: False
            errors = []
            self.assertIsNone(
                nh_loop.derive_initial_target_path(
                    "05_ACTIVE_CANDIDATE/NH_THING_v1_0_CANDIDATE.md", errors
                )
            )
            self.assertTrue(errors)
            self.assertIn("not a new", errors[-1])
        finally:
            nh_loop.is_new_candidate_path = installed
        # ...and with the real gate it derives exactly one safe path.
        errors = []
        self.assertTrue(
            nh_loop.derive_initial_target_path(
                "05_ACTIVE_CANDIDATE/NH_THING_v1_0_CANDIDATE.md", errors
            )
        )
        self.assertEqual(errors, [])

    def test_successor_versioning_is_not_redesigned(self):
        """The existing allocator is untouched and still owns corrections."""
        errors = []
        self.assertEqual(
            nh_loop.next_candidate_version_path(
                "05_ACTIVE_CANDIDATE/NH_THING_v1_0_CANDIDATE.md", errors
            ),
            "05_ACTIVE_CANDIDATE/NH_THING_v1_1_CANDIDATE.md",
        )
        self.assertTrue(
            nh_loop.is_exact_candidate_successor(
                "05_ACTIVE_CANDIDATE/NH_THING_v1_0_CANDIDATE.md",
                "05_ACTIVE_CANDIDATE/NH_THING_v1_1_CANDIDATE.md",
            )
        )


class T4BindingRehearsals(unittest.TestCase):
    """section 10.1 tests 4c, 4d, 4h -- the three objects, never collapsed."""

    def local_position(self):
        envelope = LocalT3Rehearsals().sample_envelope()
        return {
            "target_path": TARGET_Q,
            constants.LOCAL_TASK_ENVELOPE_PROMPT_KEY: envelope,
            constants.LOCAL_TASK_ENVELOPE_DIGEST_KEY: nh_loop.
            local_task_envelope_digest(envelope),
        }

    def context(self):
        return H.build_context(
            SCOPE_Q,
            binding=H.make_binding(SCOPE_Q, root=ROOT_Q, validation_set_id="vs_q"),
            candidate=H.make_candidate(ROOT_Q),
        )

    def test_10_1_4c_extra_inputs_is_exactly_three_keys(self):
        extra = commands._initial_design_extra_inputs(
            self.context(), self.local_position(), TARGET_Q
        )
        self.assertEqual(
            set(extra),
            {"prepared_target_path", "local_task_envelope_sha256",
             "frozen_source_binding_sha256"},
        )
        # Dropping the frozen source binding, or adding the complete envelope
        # as a fourth key, are BOTH failures of this contract.
        self.assertIn("frozen_source_binding_sha256", extra)
        self.assertNotIn(constants.LOCAL_TASK_ENVELOPE_PROMPT_KEY, extra)
        self.assertNotIn("prepared_specification_sha256", extra)

    def test_10_1_4d_prompt_extra_carries_the_exact_canonical_envelope(self):
        position = self.local_position()
        extra = commands._initial_design_prompt_extra(position)
        self.assertEqual(
            set(extra),
            {"specialized_prompt_kind", "prepared_target_path",
             "local_task_envelope"},
        )
        self.assertNotIn("mechanical_design_specification", extra)
        # NO-SECOND-ENVELOPE-REPRESENTATION: the SAME object the digest covers.
        self.assertEqual(
            extra["local_task_envelope"],
            position[constants.LOCAL_TASK_ENVELOPE_PROMPT_KEY],
        )
        self.assertEqual(
            nh_loop.local_task_envelope_digest(extra["local_task_envelope"]),
            position[constants.LOCAL_TASK_ENVELOPE_DIGEST_KEY],
        )

    def test_10_1_4h_the_two_digests_are_independent(self):
        """4h -- distinct, independently reconstructed, neither derived from
        the other; a mismatch in either ALONE refuses."""
        context = self.context()
        position = self.local_position()
        work_item = H.initial_work_item(context)
        inputs = commands._initial_design_extra_inputs(context, position, TARGET_Q)
        prompt = commands._initial_design_prompt_extra(position)
        required = engine.required_inputs_sha256(context, work_item, inputs)
        material = engine.prompt_material_sha256(
            "claude_initial_design", work_item, prompt
        )
        self.assertNotEqual(required, material)
        # The base inventory (object A) gains NOTHING from the envelope.
        base = engine.required_inputs_inventory(context, work_item, {})
        self.assertNotIn(constants.LOCAL_TASK_ENVELOPE_DIGEST_KEY, base)
        self.assertNotIn(constants.LOCAL_TASK_ENVELOPE_PROMPT_KEY, base)
        self.assertEqual(
            set(base),
            {"candidate_sha256", "candidate_bytes", "source_binding_sha256",
             "source_manifest_sha256", "settled_decision_binding_sha256",
             "required_source_paths", "extra"},
        )
        # required_inputs_sha256 is A PLUS B, and prompt_material_sha256 is C.
        moved_inputs = dict(inputs)
        moved_inputs[constants.LOCAL_TASK_ENVELOPE_DIGEST_KEY] = "0" * 64
        self.assertNotEqual(
            required, engine.required_inputs_sha256(context, work_item, moved_inputs)
        )
        moved_prompt = copy.deepcopy(prompt)
        moved_prompt["local_task_envelope"]["authority_required_files_sha256"] = "0" * 64
        self.assertNotEqual(
            material,
            engine.prompt_material_sha256(
                "claude_initial_design", work_item, moved_prompt
            ),
        )

    def test_10_1_4j_the_new_path_never_reads_the_retired_keys(self):
        """4j -- no new local-T3 operation reads, requires, defaults to, or
        fabricates the retired specification keys."""
        position = self.local_position()
        extra = commands._initial_design_extra_inputs(
            self.context(), position, TARGET_Q
        )
        prompt = commands._initial_design_prompt_extra(position)
        for retired in constants.OBSOLETE_SPECIFICATION_INPUT_KEYS:
            self.assertNotIn(retired, extra)
            self.assertNotIn(retired, prompt)
            self.assertNotIn(retired, position)


class EnvelopeIdentityBoundaryRehearsals(unittest.TestCase):
    """section 10.1 tests 4k, 4l, 4m, 4n -- ENVELOPE-IDENTITY-BOUNDARY."""

    def test_10_1_4m_no_envelope_identity_enters_work_item_identity(self):
        """4m -- not in WORK_ITEM_KEYS, not in the object, not in the matrix,
        and not in any parallel identity layer."""
        self.assertNotIn(
            constants.LOCAL_TASK_ENVELOPE_DIGEST_KEY, identity.WORK_ITEM_KEYS
        )
        self.assertNotIn(
            constants.LOCAL_TASK_ENVELOPE_PROMPT_KEY, identity.WORK_ITEM_KEYS
        )
        self.assertNotIn("source_manifest_sha256", identity.WORK_ITEM_KEYS)
        self.assertNotIn("required_source_paths", identity.WORK_ITEM_KEYS)
        self.assertNotIn("extra", identity.WORK_ITEM_KEYS)
        for row in identity.WORK_ITEM_MATRIX.values():
            self.assertNotIn(constants.LOCAL_TASK_ENVELOPE_DIGEST_KEY, row)
            self.assertNotIn(constants.LOCAL_TASK_ENVELOPE_PROMPT_KEY, row)
        context = H.build_context(
            SCOPE_Q,
            binding=H.make_binding(SCOPE_Q, root=ROOT_Q, validation_set_id="vs_q"),
            candidate=H.make_candidate(ROOT_Q),
        )
        obj, _id = engine.initial_design_work_item(
            context, context.round_zero_candidate, TARGET_Q
        )
        self.assertNotIn(constants.LOCAL_TASK_ENVELOPE_DIGEST_KEY, obj)
        self.assertNotIn(constants.LOCAL_TASK_ENVELOPE_PROMPT_KEY, obj)

    def test_10_1_4k_4n_envelope_only_movement_moves_request_not_work_item(self):
        """4k -- an EV/source change moves the envelope, its digest, BOTH
        request digests and the future provider-request identity, and leaves
        work_item_identity UNCHANGED.
        4n -- so the retry series and bounded output-retry budget cannot be
        reset, restarted or manufactured by envelope-only movement."""
        context = H.build_context(
            SCOPE_Q,
            binding=H.make_binding(SCOPE_Q, root=ROOT_Q, validation_set_id="vs_q"),
            candidate=H.make_candidate(ROOT_Q),
        )
        obj_before, id_before = engine.initial_design_work_item(
            context, context.round_zero_candidate, TARGET_Q
        )
        base = LocalT3Rehearsals().sample_envelope()
        moved = copy.deepcopy(base)
        # An EV source fact moves; every work-item-owned field is unchanged.
        moved["required_source_paths"] = ["01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md"]
        moved["source_currentness"]["effective_source_manifest_sha256"] = "0" * 64

        digest_before = nh_loop.local_task_envelope_digest(base)
        digest_after = nh_loop.local_task_envelope_digest(moved)
        self.assertNotEqual(digest_before, digest_after, "the envelope digest moves")

        def digests(envelope):
            position = {
                "target_path": TARGET_Q,
                constants.LOCAL_TASK_ENVELOPE_PROMPT_KEY: envelope,
                constants.LOCAL_TASK_ENVELOPE_DIGEST_KEY:
                    nh_loop.local_task_envelope_digest(envelope),
            }
            inputs = commands._initial_design_extra_inputs(
                context, position, TARGET_Q
            )
            prompt = commands._initial_design_prompt_extra(position)
            return (
                engine.required_inputs_sha256(context, obj_before, inputs),
                engine.prompt_material_sha256(
                    "claude_initial_design", obj_before, prompt
                ),
            )

        req_before, prompt_before = digests(base)
        req_after, prompt_after = digests(moved)
        self.assertNotEqual(req_before, req_after, "required_inputs_sha256 moves")
        self.assertNotEqual(prompt_before, prompt_after, "prompt_material_sha256 moves")

        # Both are inputs of provider_request_identity, so it moves too.
        def request_identity(prompt_digest, required_digest):
            return identity.derive(
                "provider_request_identity",
                {
                    "provider_kind": "claude_initial_design",
                    "provider_endpoint_identity": "ep",
                    "work_item_identity": id_before,
                    "provider_availability_episode_identity": "epi",
                    "provider_dispatch_serial": 1,
                    "prompt_material_sha256": prompt_digest,
                    "required_inputs_sha256": required_digest,
                },
            )

        self.assertNotEqual(
            request_identity(prompt_before, req_before),
            request_identity(prompt_after, req_after),
            "the future provider-request identity moves",
        )
        # ...and work_item_identity does NOT.
        _obj_after, id_after = engine.initial_design_work_item(
            context, context.round_zero_candidate, TARGET_Q
        )
        self.assertEqual(
            id_before, id_after,
            "envelope-only movement must NOT move work_item_identity",
        )
        self.assertEqual(obj_before, _obj_after, "nor the work-item object")

    def test_10_1_4l_a_moved_controlled_target_moves_work_item_identity(self):
        """4l -- for the EXISTING target_candidate_path rule, and through no
        new envelope-digest dependency."""
        context = H.build_context(
            SCOPE_Q,
            binding=H.make_binding(SCOPE_Q, root=ROOT_Q, validation_set_id="vs_q"),
            candidate=H.make_candidate(ROOT_Q),
        )
        _a, id_a = engine.initial_design_work_item(
            context, context.round_zero_candidate, TARGET_Q
        )
        _b, id_b = engine.initial_design_work_item(
            context, context.round_zero_candidate,
            "05_ACTIVE_CANDIDATE/NH_OTHER_TARGET_v1_0_CANDIDATE.md",
        )
        self.assertNotEqual(id_a, id_b)
        self.assertIn("target_candidate_path", identity.WORK_ITEM_KEYS)


class NoNewProviderBackedT3Rehearsals(unittest.TestCase):
    """section 10.1 test 4j / section 12.5 -- neither route can originate one."""

    def test_the_automatic_route_cannot_dispatch_T3(self):
        source = H.read_text(H.CONTROLLER_DIR / "nh_supervisor" / "commands.py")
        start = source.index("def prepare_next_design_task(context):")
        body = source[start:source.index("def execute_initial_design(context):")]
        self.assertNotIn("_dispatch(", body, "local T3 never dispatches")
        self.assertIn('"provider_calls": 0', body)

    def test_the_legacy_manual_route_fails_closed(self):
        """The one legacy origination branch no longer calls the launcher, and
        its HISTORICAL replay branch is preserved."""
        source = H.read_text(H.CONTROLLER_DIR / "nh_loop.py")
        # exactly ONE reference remains: the definition itself.
        self.assertEqual(source.count("run_codex_prepare_task("), 1)
        self.assertIn("def run_codex_prepare_task(", source)
        self.assertIn("longer originated by any path", source)
        # The historical stage-two replay path is untouched.
        self.assertIn("if stage_two_reply is not None:", source)
        # And the installed historical readers all remain.
        for name in (
            "def validate_prepared_task(", "def build_prepare_task_prompt(",
            "def finalize_claude_instruction(", "def run_design_task_preparation(",
        ):
            self.assertIn(name, source, name)


# ===========================================================================
# section 10.2 -- THE TWO CLAUDE RESULT ARMS.
# ===========================================================================
class ResultArmRehearsals(unittest.TestCase):

    def setUp(self):
        self.journal = H.accepted_journal()
        self.context = stop_context(self.journal)
        self.work_item = H.initial_work_item(self.context)
        self.context._current_work_item_obj = self.work_item
        self.position = T4BindingRehearsals().local_position()
        self.context._current_required_extra = (
            commands._initial_design_extra_inputs(
                self.context, self.position, TARGET_Q
            )
        )
        self.context._current_prompt_extra = commands._initial_design_prompt_extra(
            self.position
        )
        self.prepared = H.fake_prepared(
            self.context, "claude_initial_design",
            work_item=self.work_item,
            prompt_extra=self.context._current_prompt_extra,
            input_extra=self.context._current_required_extra,
        )

    def check(self, value):
        return commands._claude_initial_design_admission_checks(
            self.context, self.prepared, value
        )

    def test_10_2_7_the_STOP_arm_is_admitted_with_its_exact_three_keys(self):
        body = stop_result_body()
        self.assertEqual(
            set(body), set(constants.INITIAL_DESIGN_STOP_RESULT_KEYS)
        )
        self.assertEqual(self.check(body), [], "the exact STOP shape is admitted")
        # It carries NO candidate/explanation bytes at all.
        for forbidden in (
            "produced_candidate_path", "produced_candidate_sha256",
            "produced_candidate_bytes", "produced_candidate_payload_base64",
            "acceptance_explanation_content",
        ):
            self.assertNotIn(forbidden, body)

    def test_10_2_7_a_mixed_result_fails_and_creates_nothing(self):
        """Any candidate key beside a stop signal, or any stop signal beside a
        candidate key, remains INVALID."""
        mixed = stop_result_body()
        mixed["produced_candidate_path"] = TARGET_Q
        self.assertEqual(self.check(mixed), ["I1"])
        other = H.initial_design_result()
        other["stop_review_signal"] = dict(STOP_SIGNAL)
        self.assertEqual(self.check(other), ["I1"])
        self.assertIsNone(self.context._admitted_initial_design_payload)

    def test_10_2_7_a_neither_schema_fails_the_same_way(self):
        self.assertEqual(self.check({"anything": 1}), ["I1"])

    def test_10_2_7_the_STOP_schema_id_and_version_are_exact(self):
        body = stop_result_body()
        body["result_schema_id"] = constants.INITIAL_DESIGN_RESULT_SCHEMA_ID
        self.assertIn("I2", self.check(body))
        body = stop_result_body()
        body["result_schema_version"] = 2
        self.assertIn("I2", self.check(body))

    def test_10_2_7_an_invalid_signal_is_refused_by_the_installed_validator(self):
        body = stop_result_body({**STOP_SIGNAL, "finding_evidence": []})
        self.assertIn("I1", self.check(body))
        body = stop_result_body({**STOP_SIGNAL, "source_evidence": ["not/a/real.md"]})
        self.assertIn("I1", self.check(body))

    def test_10_2_6_the_CANDIDATE_arm_is_unchanged(self):
        """The existing contract still governs, key set and all."""
        self.assertEqual(
            set(constants.INITIAL_DESIGN_RESULT_KEYS),
            {"result_schema_id", "result_schema_version", "produced_candidate_path",
             "produced_candidate_sha256", "produced_candidate_bytes",
             "produced_candidate_payload_base64", "acceptance_explanation_content"},
        )
        # The two arms are disjoint apart from the two lifecycle keys.
        self.assertEqual(
            set(constants.INITIAL_DESIGN_RESULT_KEYS)
            & set(constants.INITIAL_DESIGN_STOP_RESULT_KEYS),
            {"result_schema_id", "result_schema_version"},
        )


# ===========================================================================
# section 10.2 -- STOP-CLOSURE-EXACT, all seven rules.
# ===========================================================================
class StopClosureRehearsals(unittest.TestCase):

    def journal_with_custody(self):
        journal = H.FakeJournal()
        anchor_validation(journal)
        custody, _terminal = stop_custody(journal)
        return journal, custody

    def state(self, journal, custody):
        return replay_mod.Replay(journal.read()).stop_closure_state(custody)

    def test_10_2_7a_a_pre_custody_identical_signal_does_NOT_close(self):
        """7a -- an identical signal that exists ONLY BEFORE the custody event
        is a different, earlier act, and counting it would fabricate a
        completion this STOP never received."""
        journal = H.FakeJournal()
        anchor_validation(journal)
        append_signal(journal)                      # BEFORE the custody
        custody, _t = stop_custody(journal)
        self.assertEqual(self.state(journal, custody), "owed")
        # ...and replay therefore still reports the custody as PENDING.
        pending = replay_mod.Replay(
            journal.read(), SCOPE_Q
        ).custodied_results_awaiting_processing()
        self.assertEqual(
            [event["work_item_kind"] for event in pending], ["initial_design"]
        )

    def test_10_2_7b_one_exact_post_custody_record_closes(self):
        """7b -- expected routed_signal_id AND full reconstructed material."""
        journal, custody = self.journal_with_custody()
        self.assertEqual(self.state(journal, custody), "owed")
        append_signal(journal)                      # AFTER the custody
        self.assertEqual(self.state(journal, custody), "durable")

    def test_10_2_7b_identity_match_with_material_mismatch_does_not_close(self):
        """RULE 3 -- matching issue key, finding key and scope is NOT enough."""
        journal, custody = self.journal_with_custody()
        append_signal(journal, overrides={"signal_title": "a different title"})
        # It is not an exact match, and it carries the same identity, so it is
        # CONFLICTING -- it fails closed rather than closing.
        self.assertEqual(self.state(journal, custody), "contradiction")

    def test_10_2_7b_a_different_scope_root_does_not_close(self):
        journal, custody = self.journal_with_custody()
        append_signal(journal, overrides={"scope_root_path": "05_ACTIVE_CANDIDATE/NH_ELSE_v1_0_CANDIDATE.md"})
        self.assertEqual(self.state(journal, custody), "contradiction")

    def test_10_2_7e_two_post_custody_matches_fail_closed(self):
        """7e -- the controller refuses rather than choosing between them."""
        journal, custody = self.journal_with_custody()
        append_signal(journal)
        append_signal(journal)
        self.assertEqual(self.state(journal, custody), "contradiction")
        # A contradiction is NEVER read as a completion.
        self.assertFalse(
            replay_mod.Replay(journal.read(), SCOPE_Q)._downstream_recorded(
                custody, {"terminal_kind": "result_received"}
            )
        )

    def test_10_2_missing_signal_keeps_the_custody_pending(self):
        journal, custody = self.journal_with_custody()
        self.assertEqual(self.state(journal, custody), "owed")
        pending = replay_mod.Replay(
            journal.read(), SCOPE_Q
        ).custodied_results_awaiting_processing()
        self.assertEqual(len(pending), 1)

    def test_10_2_a_closed_STOP_is_no_longer_pending_in_replay(self):
        """THE READ-SIDE HALF: the exact defect this rule exists to fix."""
        journal, custody = self.journal_with_custody()
        self.assertEqual(
            len(replay_mod.Replay(
                journal.read(), SCOPE_Q
            ).custodied_results_awaiting_processing()),
            1, "pending before the signal",
        )
        append_signal(journal)
        self.assertEqual(
            replay_mod.Replay(
                journal.read(), SCOPE_Q
            ).custodied_results_awaiting_processing(),
            [], "NOT pending after the exact post-custody signal",
        )

    def test_the_shared_rule_has_exactly_one_definition(self):
        """The processing side and the replay side call the SAME functions."""
        commands_source = H.read_text(H.CONTROLLER_DIR / "nh_supervisor" / "commands.py")
        # commands.py states no fingerprint/identity domain of its own for the
        # STOP route: the only occurrences belong to the pre-existing T1 route.
        self.assertIn("replay_mod.stop_closure_expected_record(", commands_source)
        self.assertIn("replay_mod.stop_closure_match_state(", commands_source)
        self.assertIn(
            "replay_mod.Replay(events).stop_closure_binding_fields(", commands_source
        )
        # And the read side calls the very same module-level functions.
        replay_source = H.read_text(H.CONTROLLER_DIR / "nh_supervisor" / "replay.py")
        self.assertIn("expected = stop_closure_expected_record(scope, signal, **fields)",
                      replay_source)
        self.assertIn("return stop_closure_match_state(self.events, expected, custody_seq)",
                      replay_source)

    def test_the_two_sides_agree_field_for_field(self):
        """One expectation, whichever side builds it."""
        journal, custody = self.journal_with_custody()
        context = stop_context(journal)
        from_commands = commands.stop_review_signal_expectation(
            context, journal.read(), STOP_SIGNAL
        )
        fields = replay_mod.Replay(journal.read()).stop_closure_binding_fields(SCOPE_Q)
        from_replay = replay_mod.stop_closure_expected_record(
            SCOPE_Q, STOP_SIGNAL, **fields
        )
        self.assertEqual(from_commands, from_replay)


class StopProcessingRehearsals(unittest.TestCase):
    """section 10.2 tests 7c, 7d, 7f -- the write side, ZERO providers."""

    def build(self, *, times=1, overrides=None, pre_signal=False):
        journal = H.FakeJournal()
        anchor_validation(journal)
        if pre_signal:
            append_signal(journal)
        custody, _terminal = stop_custody(journal)
        transport = H.LoudStubTransport()
        context = stop_context(journal, transport=transport)
        context.review_signal_adapter = RecordingSignalAdapter(
            journal, times=times, overrides=overrides
        )
        work_item = H.initial_work_item(context)
        context._current_work_item_obj = work_item
        position = T4BindingRehearsals().local_position()
        context._current_required_extra = commands._initial_design_extra_inputs(
            context, position, TARGET_Q
        )
        context._current_prompt_extra = commands._initial_design_prompt_extra(position)
        prepared = H.fake_prepared(
            context, "claude_initial_design", work_item=work_item,
            prompt_extra=context._current_prompt_extra,
            input_extra=context._current_required_extra,
        )
        situation = None
        operation = _FakeOperation()
        return journal, context, transport, prepared, custody, operation, situation

    def run_closure(self, journal, context, prepared, custody, operation, situation):
        return commands._close_custodied_initial_design_stop(
            context, operation, situation, prepared, custody, stop_result_body()
        )

    def test_10_2_7c_a_crash_before_any_signal_appends_exactly_one(self):
        """7c -- and reads it back."""
        journal, context, transport, prepared, custody, op, sit = self.build()
        before = journal.appends
        result = self.run_closure(journal, context, prepared, custody, op, sit)
        self.assertEqual(context.review_signal_adapter.calls, 1)
        self.assertEqual(journal.appends - before, 1, "EXACTLY one append")
        self.assertEqual(result.report["appends"], 1)
        self.assertEqual(result.report["provider_calls"], 0)
        self.assertEqual(result.report["stop_closure"], "recorded")
        self.assertEqual(transport.calls, [], "ZERO provider calls")
        # THE MANDATORY READBACK: the appended record re-proves the rule.
        self.assertEqual(
            replay_mod.Replay(journal.read()).stop_closure_state(custody), "durable"
        )

    def test_10_2_7d_a_restart_after_closure_appends_zero_and_reruns_zero(self):
        """7d -- append count ZERO, and CLAUDE IS NEVER RERUN."""
        journal, context, transport, prepared, custody, op, sit = self.build()
        self.run_closure(journal, context, prepared, custody, op, sit)
        calls_after_first = context.review_signal_adapter.calls
        appends_after_first = journal.appends
        # Re-enter, exactly as a restart does.
        op2 = _FakeOperation()
        result = self.run_closure(journal, context, prepared, custody, op2, sit)
        self.assertEqual(result.report["appends"], 0)
        self.assertEqual(result.report["stop_closure"], "already_durable")
        self.assertEqual(
            context.review_signal_adapter.calls, calls_after_first,
            "no second record_review_signal call",
        )
        self.assertEqual(journal.appends, appends_after_first, "ZERO further appends")
        self.assertEqual(transport.calls, [], "Claude is rerun ZERO times")

    def test_10_2_7e_a_recorder_that_appends_twice_fails_closed(self):
        journal, context, transport, prepared, custody, op, sit = self.build(times=2)
        with self.assertRaises(SupervisorRefusal):
            self.run_closure(journal, context, prepared, custody, op, sit)
        self.assertEqual(transport.calls, [])

    def test_the_readback_is_mandatory_not_optional(self):
        """An append that cannot be read back and re-proved is NOT a closure."""
        journal, context, transport, prepared, custody, op, sit = self.build(
            overrides={"signal_title": "drifted at write time"}
        )
        with self.assertRaises(SupervisorRefusal) as caught:
            self.run_closure(journal, context, prepared, custody, op, sit)
        self.assertIn("re-prove on readback", str(caught.exception))
        self.assertEqual(transport.calls, [])

    def test_a_pre_custody_signal_does_not_satisfy_the_owed_append(self):
        """7a on the WRITE side: the earlier act does not discharge the debt."""
        journal, context, transport, prepared, custody, op, sit = self.build(
            pre_signal=True
        )
        before = journal.appends
        result = self.run_closure(journal, context, prepared, custody, op, sit)
        self.assertEqual(journal.appends - before, 1, "it still appends once")
        self.assertEqual(result.report["appends"], 1)

    def test_10_2_7f_every_STOP_processing_position_contacts_nobody(self):
        for kwargs in ({}, {"times": 2}, {"pre_signal": True}):
            journal, context, transport, prepared, custody, op, sit = self.build(
                **kwargs
            )
            try:
                self.run_closure(journal, context, prepared, custody, op, sit)
            except SupervisorRefusal:
                pass
            self.assertEqual(transport.calls, [], kwargs)


class _FakeOperation:
    """The minimum operation surface the closure uses.  Appends nothing."""

    def __init__(self):
        self.appended = []
        self.outcome = None

    def complete(self, outcome, **_kwargs):
        self.outcome = outcome


# ===========================================================================
# section 10.3 -- HISTORICAL, RECOVERY AND COMPATIBILITY.
# ===========================================================================
class HistoricalCompatibilityRehearsals(unittest.TestCase):

    def test_10_3_12_historical_T3_reconstructs_its_own_specification_keys(self):
        """A historical prepared task keeps its ORIGINAL binding, unconverted."""
        context = H.build_context(
            SCOPE_Q,
            binding=H.make_binding(SCOPE_Q, root=ROOT_Q, validation_set_id="vs_q"),
            candidate=H.make_candidate(ROOT_Q),
        )
        historical = {"target_path": TARGET_Q, "specification": {"a": "specification"}}
        self.assertFalse(commands.is_local_task_envelope_position(historical))
        extra = commands._initial_design_extra_inputs(context, historical, TARGET_Q)
        self.assertEqual(
            set(extra),
            {"prepared_target_path", "prepared_specification_sha256",
             "frozen_source_binding_sha256"},
        )
        prompt = commands._initial_design_prompt_extra(historical)
        self.assertEqual(
            set(prompt),
            {"specialized_prompt_kind", "prepared_target_path",
             "mechanical_design_specification"},
        )
        self.assertEqual(prompt["mechanical_design_specification"], {"a": "specification"})

    def test_10_3_12_the_historical_registry_rows_all_remain(self):
        self.assertIn("next_design_task_preparation", constants.WORK_ITEM_KINDS)
        self.assertIn("codex_next_design_task_preparation", constants.PROVIDER_KINDS)
        self.assertEqual(
            constants.PROVIDER_KIND_BY_WORK_ITEM_KIND["next_design_task_preparation"],
            "codex_next_design_task_preparation",
        )
        self.assertEqual(
            constants.RESULT_SCHEMA_ID_BY_PROVIDER_KIND[
                "codex_next_design_task_preparation"
            ],
            "NH_NEXT_DESIGN_TASK_PREPARATION_LIFECYCLE_V1",
        )
        self.assertIn(
            "next_design_task_preparation",
            constants.CLOSED_BY_TERMINAL_ONLY_WORK_ITEM_KINDS,
        )

    def test_10_3_12_an_ordinary_CANDIDATE_custody_still_closes_the_old_way(self):
        """The installed candidate rules run UNCHANGED for a CANDIDATE result:
        pending until its own candidate transaction proves completion."""
        journal = H.FakeJournal()
        anchor_validation(journal)
        candidate_value = H.initial_design_result()
        custody, _t = stop_custody(journal, request="pr_cand", value=candidate_value)
        rep = replay_mod.Replay(journal.read(), SCOPE_Q)
        # It is NOT a STOP, so the STOP rule declines it entirely...
        self.assertIsNone(rep.stop_closure_state(custody))
        # ...and it is still PENDING, exactly as CLOSURE-INITIAL-PENDING says.
        self.assertEqual(
            [event["work_item_kind"]
             for event in rep.custodied_results_awaiting_processing()],
            ["initial_design"],
        )
        # A signal does NOT close a CANDIDATE custody.
        append_signal(journal)
        self.assertEqual(
            len(replay_mod.Replay(
                journal.read(), SCOPE_Q
            ).custodied_results_awaiting_processing()),
            1, "a CANDIDATE custody is never closed by a review signal",
        )

    def test_10_3_result_invalid_behaviour_is_unchanged(self):
        """A result_invalid terminal keeps its installed meaning."""
        journal = H.FakeJournal()
        anchor_validation(journal)
        custody, _t = stop_custody(
            journal, request="pr_bad", terminal_kind="result_invalid"
        )
        rep = replay_mod.Replay(journal.read(), SCOPE_Q)
        # The custody still exists and is still authenticated evidence.
        self.assertEqual(len(rep.scoped("provider_result_custody_recorded")), 1)
        self.assertEqual(
            rep.terminal_event("pr_bad")["terminal_kind"], "result_invalid"
        )

    def test_10_3_old_events_are_never_rewritten(self):
        """Every derivation here is a pure read: nothing mutates the journal."""
        journal = H.FakeJournal()
        anchor_validation(journal)
        custody, _t = stop_custody(journal)
        before = copy.deepcopy(journal.events)
        appends_before = journal.appends
        rep = replay_mod.Replay(journal.read(), SCOPE_Q)
        rep.stop_closure_state(custody)
        rep.custodied_results_awaiting_processing()
        rep.stop_closure_binding_fields(SCOPE_Q)
        self.assertEqual(journal.events, before, "no event was rewritten")
        self.assertEqual(journal.appends, appends_before, "nothing was appended")

    def test_10_3_an_anchored_STOP_is_structurally_impossible(self):
        """The dispatcher refuses a STOP body that could not be custodied
        inline, so the replay proof can always read a real one."""
        source = H.read_text(H.CONTROLLER_DIR / "nh_loop.py")
        self.assertIn("MAX_INLINE_RESULT_BYTES", source)
        body = json.dumps(stop_result_body(), sort_keys=True).encode("utf-8")
        self.assertLess(len(body), constants.MAX_INLINE_RESULT_BYTES)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()


# ===========================================================================
# INSTALLATION CORRECTION -- THE LOCAL-T3 STATE MACHINE, END TO END.
#
# v1_6 section 5.1 preserves this EXACT position:
#     LOOP_TASK_PREPARATION_REQUIRED
#       -> prepare-next-design-task
#       -> LOOP_INITIAL_DESIGN_REQUIRED
# and section 5.6 requires a NOT-READY position to report the EXACT EXISTING
# condition and launch nothing.
# ===========================================================================
class LocalT3StateMachineRehearsals(unittest.TestCase):

    def adapter_for(self, envelope, *, target=TARGET_Q):
        adapter = H.StubAdapter()
        adapter.build_local_task_envelope = (
            lambda *a, **k: copy.deepcopy(envelope) if envelope else None
        )
        adapter.derive_initial_target_path = lambda root, errors: target
        return adapter

    def complete_local_t3(self, journal, *, scope=SCOPE_Q, root=ROOT_Q,
                          sha="9" * 64, size=4096, operation="op_t3",
                          outcome="ok"):
        """One COMPLETED local-T3 operation, through the EXISTING machinery."""
        journal.append(
            {
                "type": "supervisor_operation_started",
                "supervisor_command": "prepare-next-design-task",
                "supervisor_operation_id": operation,
                "package_scope_id": scope,
                "candidate_path": root,
                "candidate_sha256": sha,
                "candidate_bytes": size,
                "work_item_identity": "wi_t3",
            }
        )
        journal.append(
            {
                "type": "supervisor_operation_completed",
                "supervisor_operation_id": operation,
                "operation_outcome": outcome,
                "package_scope_id": scope,
            }
        )

    def position(self, *, envelope=None, completed=False, transport=None,
                 complete_kwargs=None):
        """The derived transition state and loop position at the T3 boundary."""
        if envelope is None:
            envelope = LocalT3Rehearsals().sample_envelope()
        journal = H.staged_journal("task_preparation")
        if completed:
            self.complete_local_t3(journal, **(complete_kwargs or {}))
        transport = transport or H.LoudStubTransport()
        context = H.build_context(
            journal=journal,
            adapter=self.adapter_for(envelope),
            transport=transport,
            clearance=lambda scope: {"unlocked": True},
        )
        state = commands.post_acceptance_transition_state(
            context, reconstruct_extra=H.full_reconstructor()
        )
        loop = commands.loop_position(context, state)
        return journal, context, state, loop, transport

    # -- 1 -- BEFORE the local T3 run ------------------------------------
    def test_1_before_local_T3_the_loop_offers_prepare_next_design_task(self):
        """A cleared package with no completed local-T3 operation projects the
        ACCEPTED position -- the command is NOT skipped."""
        _j, _c, state, loop, _t = self.position(completed=False)
        self.assertTrue(
            state["local_task_envelope_derivable"],
            "the envelope is derivable...",
        )
        self.assertIsNone(state["prepared_task"], "...but that is NOT prepared")
        self.assertIsNone(state["local_t3_completed_event_seq"])
        self.assertEqual(loop["loop_state"], "LOOP_TASK_PREPARATION_REQUIRED")
        self.assertEqual(loop["loop_next_command"], "prepare-next-design-task")

    # -- 2 -- the command really exists in the state machine --------------
    def test_2_the_command_owns_only_its_ordinary_operation_records(self):
        journal = H.accepted_journal()
        binding = H.make_binding(SCOPE_Q, root=ROOT_Q, validation_set_id="vs_q")
        H.admitted_selection_state(
            journal, binding=binding, candidate=H.make_candidate(ROOT_Q)
        )
        transport = H.LoudStubTransport()
        context = H.build_context(
            SCOPE_Q, journal=journal, transport=transport, binding=binding,
            candidate=H.make_candidate(ROOT_Q),
            adapter=self.adapter_for(LocalT3Rehearsals().sample_envelope()),
            clearance=lambda scope_id: {"unlocked": True},
        )
        before = len(journal.events)
        with H.proved_acceptance():
            try:
                commands.prepare_next_design_task(context)
            except SupervisorRefusal:
                pass
        appended = [event["type"] for event in journal.events[before:]]
        self.assertEqual(transport.calls, [], "ZERO provider calls")
        self.assertEqual(
            [k for k in appended if k.startswith("provider_")], [],
            "NO provider lifecycle records",
        )
        self.assertTrue(
            set(appended) <= {
                "supervisor_operation_started", "supervisor_operation_completed",
            },
            appended,
        )

    # -- 3 -- AFTER local T3 completion -----------------------------------
    def test_3_after_completion_the_loop_offers_execute_initial_design(self):
        _j, _c, state, loop, _t = self.position(completed=True)
        self.assertIsNotNone(state["prepared_task"])
        self.assertIsNotNone(state["local_t3_completed_event_seq"])
        self.assertEqual(loop["loop_state"], "LOOP_INITIAL_DESIGN_REQUIRED")
        self.assertEqual(loop["loop_next_command"], "execute-initial-design")

    def test_3_the_reconstructed_envelope_and_digest_are_deterministic(self):
        """Identical current inputs reproduce the exact envelope and digest."""
        _j1, _c1, first, _l1, _t1 = self.position(completed=True)
        _j2, _c2, second, _l2, _t2 = self.position(completed=True)
        key = constants.LOCAL_TASK_ENVELOPE_PROMPT_KEY
        digest = constants.LOCAL_TASK_ENVELOPE_DIGEST_KEY
        self.assertEqual(first["prepared_task"][key], second["prepared_task"][key])
        self.assertEqual(
            first["prepared_task"][digest], second["prepared_task"][digest]
        )
        self.assertEqual(
            nh_loop.local_task_envelope_digest(first["prepared_task"][key]),
            first["prepared_task"][digest],
        )

    # -- 4 -- NO PHANTOM COMPLETION ---------------------------------------
    def test_4_a_derivable_envelope_alone_never_skips_T3(self):
        _j, _c, state, loop, _t = self.position(completed=False)
        self.assertTrue(state["local_task_envelope_derivable"])
        self.assertIsNone(state["prepared_task"])
        self.assertNotEqual(loop["loop_next_command"], "execute-initial-design")

    def test_4_a_foreign_or_stale_completion_does_not_unlock_this_one(self):
        for kwargs, why in (
            ({"scope": "nullpkg_someone_else"}, "another package"),
            ({"root": "05_ACTIVE_CANDIDATE/NH_OTHER_v1_0_CANDIDATE.md"},
             "another root"),
            ({"sha": "0" * 64}, "a moved root digest"),
            ({"size": 1}, "a moved root byte length"),
            ({"outcome": "safety_hold"}, "a non-ok outcome"),
        ):
            _j, _c, state, loop, _t = self.position(
                completed=True, complete_kwargs=kwargs
            )
            self.assertIsNone(state["prepared_task"], why)
            self.assertEqual(
                loop["loop_next_command"], "prepare-next-design-task", why
            )

    def test_4_an_unmatched_start_is_residue_and_never_a_completion(self):
        """A started-but-never-completed local T3 stays ordinary residue."""
        envelope = LocalT3Rehearsals().sample_envelope()
        journal = H.staged_journal("task_preparation")
        journal.append(
            {
                "type": "supervisor_operation_started",
                "supervisor_command": "prepare-next-design-task",
                "supervisor_operation_id": "op_orphan",
                "package_scope_id": SCOPE_Q,
                "candidate_path": ROOT_Q,
                "candidate_sha256": "9" * 64,
                "candidate_bytes": 4096,
            }
        )
        context = H.build_context(
            journal=journal, adapter=self.adapter_for(envelope),
            clearance=lambda scope: {"unlocked": True},
        )
        state = commands.post_acceptance_transition_state(
            context, reconstruct_extra=H.full_reconstructor()
        )
        self.assertIsNone(state["prepared_task"], "residue is not a completion")
        self.assertIsNone(
            commands.local_t3_phase_completed(
                journal.read(), SCOPE_Q, state["selection"]
            )
        )

    # -- 5 / 6 -- SOURCE CURRENTNESS --------------------------------------
    def test_5_stale_source_is_NOT_READY_and_never_reaches_T4(self):
        stale = LocalT3Rehearsals().sample_envelope()
        stale["source_currentness"]["source_state_current"] = False
        _j, _c, state, loop, transport = self.position(
            envelope=stale, completed=True
        )
        self.assertIsNone(state["prepared_task"], "stale source is NOT READY")
        self.assertEqual(
            state["local_task_envelope_not_ready"],
            commands.LOCAL_T3_NOT_READY_SOURCE,
        )
        self.assertEqual(loop["loop_state"], "LOOP_TASK_PREPARATION_REQUIRED")
        self.assertNotEqual(loop["loop_next_command"], "execute-initial-design")
        self.assertEqual(transport.calls, [], "ZERO provider calls")

    def test_5_a_missing_currentness_field_is_not_a_proved_false(self):
        """An owner that cannot supply the exact field leaves T3 NOT READY --
        the field is never silently defaulted in either direction."""
        absent = LocalT3Rehearsals().sample_envelope()
        del absent["source_currentness"]["source_state_current"]
        position, reason = LocalT3Rehearsals().derive_with(absent)
        self.assertIsNone(position)
        self.assertEqual(reason, commands.LOCAL_T3_NOT_READY_SOURCE)

    def test_5_a_false_is_carried_honestly_and_never_rewritten(self):
        stale = LocalT3Rehearsals().sample_envelope()
        stale["source_currentness"]["source_state_current"] = False
        _j, _c, state, _l, _t = self.position(envelope=stale, completed=True)
        # The fact stays false everywhere it is read; nothing revalidates it.
        self.assertFalse(stale["source_currentness"]["source_state_current"])
        self.assertIsNone(state["prepared_task"])

    def test_6_current_source_with_every_other_proof_is_READY(self):
        current = LocalT3Rehearsals().sample_envelope()
        self.assertTrue(current["source_currentness"]["source_state_current"])
        _j, _c, state, loop, _t = self.position(
            envelope=current, completed=True
        )
        self.assertIsNotNone(state["prepared_task"])
        self.assertIsNone(state["local_task_envelope_not_ready"])
        self.assertEqual(loop["loop_next_command"], "execute-initial-design")

    # -- 7 -- THE EXACT NOT-READY REASON ----------------------------------
    def test_7_each_condition_reports_its_own_existing_owner(self):
        cases = []
        stale = LocalT3Rehearsals().sample_envelope()
        stale["source_currentness"]["source_state_current"] = False
        cases.append((stale, TARGET_Q, commands.LOCAL_T3_NOT_READY_SOURCE))

        owed = LocalT3Rehearsals().sample_envelope()
        owed["unsatisfied_dependency_keys"] = ["dep_a"]
        cases.append((owed, TARGET_Q, commands.LOCAL_T3_NOT_READY_DEPENDENCY))

        locked = LocalT3Rehearsals().sample_envelope()
        locked["question_clearance"]["unlocked"] = False
        cases.append((locked, TARGET_Q, commands.LOCAL_T3_NOT_READY_CLEARANCE))

        # An occupied / unsafe target: the derivation yields no path at all.
        cases.append((LocalT3Rehearsals().sample_envelope(), None,
                      commands.LOCAL_T3_NOT_READY_TARGET))

        seen = set()
        for envelope, target, expected in cases:
            position, reason = LocalT3Rehearsals().derive_with(
                envelope, target=target
            )
            self.assertIsNone(position, expected)
            self.assertEqual(reason, expected)
            self.assertIn(reason, commands.LOCAL_T3_NOT_READY_REASONS)
            seen.add(reason)
        self.assertEqual(len(seen), 4, "the four conditions stay DISTINGUISHABLE")

    def test_7_the_generic_sentence_is_gone_and_no_question_is_invented(self):
        stale = LocalT3Rehearsals().sample_envelope()
        stale["source_currentness"]["source_state_current"] = False
        _j, _c, state, loop, _t = self.position(envelope=stale, completed=True)
        detail = loop.get("loop_detail") or ""
        self.assertIn("source", detail.lower())
        self.assertNotIn("missing, stale, ambiguous", detail)
        self.assertEqual(
            loop.get("local_task_preparation_not_ready"),
            commands.LOCAL_T3_NOT_READY_SOURCE,
        )
        # NOT a Ness-question route, and no signal was invented.
        self.assertNotEqual(loop["loop_state"], "LOOP_NEEDS_NESS_DECISION")
        self.assertEqual(
            [e for e in _j.events if e["type"] == "review_signal_recorded"], []
        )

    # -- 8 -- NO AUTOMATIC T3 SPIN ----------------------------------------
    def test_8_a_persistent_NOT_READY_offers_no_command_and_cannot_spin(self):
        """The worker is given NOTHING to run while the prerequisite stands, so
        no sequence of empty local-T3 operations can accumulate."""
        stale = LocalT3Rehearsals().sample_envelope()
        stale["source_currentness"]["source_state_current"] = False
        for _ in range(5):  # the worker re-reading the same unchanged state
            journal, _c, state, loop, transport = self.position(envelope=stale)
            self.assertEqual(loop["loop_state"], "LOOP_TASK_PREPARATION_REQUIRED")
            self.assertIsNone(
                loop["loop_next_command"],
                "a NOT-READY position offers NO command",
            )
            self.assertEqual(transport.calls, [])
            self.assertEqual(
                [e for e in journal.events
                 if e.get("supervisor_command") == "prepare-next-design-task"],
                [], "no local-T3 operation was appended by merely reading",
            )

    def test_8_a_ready_position_does_offer_the_command_exactly_once(self):
        """The contrast: when nothing blocks, the command IS offered -- and once
        its completion is durable the loop moves on rather than repeating it."""
        _j, _c, _s, before, _t = self.position(completed=False)
        self.assertEqual(before["loop_next_command"], "prepare-next-design-task")
        _j2, _c2, _s2, after, _t2 = self.position(completed=True)
        self.assertEqual(after["loop_next_command"], "execute-initial-design")

    # -- 9 -- RESTART ------------------------------------------------------
    def test_9_restart_reconstructs_the_same_envelope_with_no_store(self):
        """One valid completion; a fresh replay rebuilds the identical envelope
        from current authenticated facts, with no provider and no store."""
        envelope = LocalT3Rehearsals().sample_envelope()
        journal = H.staged_journal("task_preparation")
        self.complete_local_t3(journal)
        digests = []
        for _ in range(3):  # three independent "process restarts"
            transport = H.LoudStubTransport()
            context = H.build_context(
                journal=journal, adapter=self.adapter_for(envelope),
                transport=transport,
                clearance=lambda scope: {"unlocked": True},
            )
            state = commands.post_acceptance_transition_state(
                context, reconstruct_extra=H.full_reconstructor()
            )
            self.assertIsNotNone(state["prepared_task"])
            digests.append(
                state["prepared_task"][constants.LOCAL_TASK_ENVELOPE_DIGEST_KEY]
            )
            self.assertEqual(transport.calls, [])
        self.assertEqual(len(set(digests)), 1, "deterministic across restarts")
        # NO second completion is required merely because the process restarted.
        starts = [
            e for e in journal.events
            if e.get("supervisor_command") == "prepare-next-design-task"
        ]
        self.assertEqual(len(starts), 1, "exactly the one original completion")
        # And NO envelope store exists: the position carries the object only
        # because THIS derivation just rebuilt it.
        self.assertEqual(
            [e for e in journal.events
             if constants.LOCAL_TASK_ENVELOPE_PROMPT_KEY in e], [],
            "the envelope is never written to the journal",
        )

    # -- 10 -- SOURCE MOVES AFTER T3 --------------------------------------
    def test_10_an_old_completion_does_not_let_stale_source_reach_claude(self):
        """The completion proves only that the phase RAN.  Currentness is
        re-proved at every use, so source that goes stale afterwards closes the
        path to T4 again."""
        envelope = LocalT3Rehearsals().sample_envelope()
        journal = H.staged_journal("task_preparation")
        self.complete_local_t3(journal)

        def derive(env):
            transport = H.LoudStubTransport()
            context = H.build_context(
                journal=journal, adapter=self.adapter_for(env),
                transport=transport,
                clearance=lambda scope: {"unlocked": True},
            )
            state = commands.post_acceptance_transition_state(
                context, reconstruct_extra=H.full_reconstructor()
            )
            return state, commands.loop_position(context, state), transport

        state, loop, _t = derive(envelope)
        self.assertEqual(loop["loop_next_command"], "execute-initial-design")

        # ...now the source goes stale under the SAME durable completion.
        moved = copy.deepcopy(envelope)
        moved["source_currentness"]["source_state_current"] = False
        state, loop, transport = derive(moved)
        self.assertIsNone(state["prepared_task"], "T4 is unreachable again")
        self.assertEqual(
            state["local_task_envelope_not_ready"],
            commands.LOCAL_T3_NOT_READY_SOURCE,
        )
        self.assertNotEqual(loop["loop_next_command"], "execute-initial-design")
        self.assertEqual(transport.calls, [])

    def test_5_the_builder_itself_refuses_an_unsupplied_currentness_verdict(self):
        """The INSTALLED builder, not only the position derivation: if the
        accepted section 8.8 owner supplies no exact verdict, no envelope is
        built at all -- absence is never converted into a proved false."""
        installed = nh_loop.package_source_currentness
        projection = {
            "package_scope_id": SCOPE_Q,
            "contradiction": None,
            "anchor_source_binding_sha256": "b" * 64,
            "effective_validation_set_id": "vs_q",
            "effective_source_manifest_sha256": "d" * 64,
            "effective_source_binding_sha256": "b" * 64,
            "effective_required_source_paths": [MASTER_PATH],
            # NO source_state_current key at all.
        }
        try:
            nh_loop.package_source_currentness = (
                lambda scope, with_internals=False, **k: (
                    (dict(projection), {}) if with_internals else dict(projection)
                )
            )
            errors = []
            envelope = nh_loop.build_local_task_envelope(
                [], SCOPE_Q,
                authority_required_files_sha256="8" * 64,
                target_path=TARGET_Q, errors=errors,
            )
            self.assertIsNone(envelope, "no envelope is built")
            self.assertTrue(
                any("source_state_current" in message for message in errors),
                errors,
            )
        finally:
            nh_loop.package_source_currentness = installed

    def test_8_a_wiring_fact_never_suppresses_the_accepted_position(self):
        """Only a PROVED BLOCKING CONDITION about this package stops the loop.

        A context with no derivation seam bound proves nothing about whether the
        package is ready, so the accepted state-machine position is preserved
        and the command is still offered -- the command itself refuses if the
        seam really is missing.  Suppressing it here would change the projected
        position for a reason that says nothing about the package.
        """
        journal = H.staged_journal("task_preparation")
        context = H.build_context(          # the DEFAULT stub adapter: no seam
            journal=journal, clearance=lambda scope: {"unlocked": True}
        )
        state = commands.post_acceptance_transition_state(
            context, reconstruct_extra=H.full_reconstructor()
        )
        self.assertEqual(
            state["local_task_envelope_not_ready"], commands.LOCAL_T3_NOT_READY_SEAM
        )
        loop = commands.loop_position(context, state)
        self.assertEqual(loop["loop_state"], "LOOP_TASK_PREPARATION_REQUIRED")
        self.assertEqual(loop["loop_next_command"], "prepare-next-design-task")

    def test_8_the_blocking_set_is_exactly_the_package_conditions(self):
        self.assertEqual(
            commands.LOCAL_T3_BLOCKING_NOT_READY_REASONS,
            frozenset(
                {
                    commands.LOCAL_T3_NOT_READY_TARGET,
                    commands.LOCAL_T3_NOT_READY_AUTHORITY,
                    commands.LOCAL_T3_NOT_READY_ENVELOPE,
                    commands.LOCAL_T3_NOT_READY_SOURCE,
                    commands.LOCAL_T3_NOT_READY_CLEARANCE,
                    commands.LOCAL_T3_NOT_READY_DEPENDENCY,
                }
            ),
        )
        self.assertNotIn(
            commands.LOCAL_T3_NOT_READY_SEAM,
            commands.LOCAL_T3_BLOCKING_NOT_READY_REASONS,
        )
        self.assertNotIn(
            commands.LOCAL_T3_NOT_READY_SELECTION,
            commands.LOCAL_T3_BLOCKING_NOT_READY_REASONS,
        )
        self.assertTrue(
            commands.LOCAL_T3_BLOCKING_NOT_READY_REASONS
            <= set(commands.LOCAL_T3_NOT_READY_REASONS)
        )

    # -- section 8.1 -- HISTORICAL PROVIDER-BACKED T3 IS NOT A LOCAL COMPLETION -
    def complete_historical_t3(self, journal, *, scope=SCOPE_Q, root=ROOT_Q,
                               sha="9" * 64, size=4096, operation="op_old_t3",
                               request="pr_old_t3", name_the_operation=True,
                               stale_target=OCCUPIED_TARGET,
                               terminal_kind="result_invalid"):
        """A HISTORICAL provider-backed T3: same command, same scope, same root,
        successful completion -- and a REAL provider-request lifecycle inside it.

        The lifecycle triple is built by the SHARED harness builder, so these
        are genuine, complete, replayable historical records rather than a thin
        stand-in.  ``name_the_operation=False`` produces the case where the
        provider records do not carry the operation id, which the event-window
        binding must still catch.
        """
        journal.append(
            {
                "type": "supervisor_operation_started",
                "supervisor_command": "prepare-next-design-task",
                "supervisor_operation_id": operation,
                "package_scope_id": scope,
                "candidate_path": root,
                "candidate_sha256": sha,
                "candidate_bytes": size,
                "work_item_identity": "wi_old_t3",
            }
        )
        H.custody_pair(
            journal,
            kind="next_design_task_preparation",
            provider_kind="codex_next_design_task_preparation",
            value=H.prepared_task_object(target=stale_target),
            scope=scope,
            request=request,
            work_item_identity="wi_old_t3",
            terminal_kind=terminal_kind,
            supervisor_operation_id=operation if name_the_operation else None,
        )
        journal.append(
            {
                "type": "supervisor_operation_completed",
                "supervisor_operation_id": operation,
                "operation_outcome": "ok",
                "package_scope_id": scope,
            }
        )

    def test_8_1_a_genuine_local_T3_completion_unlocks_T4(self):
        """The control: no provider lifecycle inside it, so it IS local."""
        _j, _c, state, loop, transport = self.position(completed=True)
        self.assertIsNotNone(state["prepared_task"])
        self.assertEqual(loop["loop_next_command"], "execute-initial-design")
        self.assertEqual(transport.calls, [])

    def test_8_1_a_historical_provider_backed_T3_does_NOT_unlock_local_T3(self):
        """SAME command name, SAME scope, SAME root path/hash/bytes, and a
        successful completion -- and it still must not count."""
        envelope = LocalT3Rehearsals().sample_envelope()
        journal = H.staged_journal("task_preparation")
        self.complete_historical_t3(journal)
        transport = H.LoudStubTransport()
        context = H.build_context(
            journal=journal, adapter=self.adapter_for(envelope),
            transport=transport, clearance=lambda scope: {"unlocked": True},
        )
        state = commands.post_acceptance_transition_state(
            context, reconstruct_extra=H.full_reconstructor()
        )
        # THE POINT OF THE FIX: it is never read as a LOCAL-T3 completion.
        self.assertIsNone(
            commands.local_t3_phase_completed(
                journal.read(), SCOPE_Q, state["selection"]
            ),
            "a historical provider-backed T3 is never a local-T3 completion",
        )
        self.assertIsNone(state["local_t3_completed_event_seq"])
        self.assertIsNone(state["prepared_task"])
        # 5 -- and the loop therefore STILL exposes the local command.
        loop = commands.loop_position(context, state)
        self.assertEqual(loop["loop_state"], "LOOP_TASK_PREPARATION_REQUIRED")
        self.assertEqual(loop["loop_next_command"], "prepare-next-design-task")
        # 6 -- zero provider calls throughout.
        self.assertEqual(transport.calls, [])

    def test_8_1_the_provider_records_are_what_disqualify_it(self):
        """3 -- adding the historical provider lifecycle is exactly what makes
        the operation non-local; the same start/completion without it counts."""
        envelope = LocalT3Rehearsals().sample_envelope()

        def prepared_task_for(journal):
            context = H.build_context(
                journal=journal, adapter=self.adapter_for(envelope),
                clearance=lambda scope: {"unlocked": True},
            )
            state = commands.post_acceptance_transition_state(
                context, reconstruct_extra=H.full_reconstructor()
            )
            return state["prepared_task"]

        bare = H.staged_journal("task_preparation")
        self.complete_local_t3(bare, operation="op_same")
        self.assertIsNotNone(
            prepared_task_for(bare), "without provider records it IS local"
        )
        backed = H.staged_journal("task_preparation")
        self.complete_historical_t3(backed, operation="op_same")
        self.assertIsNone(
            prepared_task_for(backed), "with them it is NOT"
        )

    def test_8_1_the_event_window_catches_an_unnamed_provider_record(self):
        """Either installed binding is enough: a historical provider record
        that does not carry the operation id still stands inside the
        operation's own window, and still disqualifies it."""
        envelope = LocalT3Rehearsals().sample_envelope()
        journal = H.staged_journal("task_preparation")
        self.complete_historical_t3(journal, name_the_operation=False)
        context = H.build_context(
            journal=journal, adapter=self.adapter_for(envelope),
            clearance=lambda scope: {"unlocked": True},
        )
        state = commands.post_acceptance_transition_state(
            context, reconstruct_extra=H.full_reconstructor()
        )
        self.assertIsNone(state["prepared_task"])

    def test_8_1_a_LATER_unrelated_provider_record_does_not_disqualify(self):
        """The window is the operation's OWN.  A provider record appended after
        the completion belongs to a different operation and is not read as this
        one's -- the rule stays narrow rather than merely strict."""
        envelope = LocalT3Rehearsals().sample_envelope()
        journal = H.staged_journal("task_preparation")
        self.complete_local_t3(journal)
        journal.append(
            {
                "type": "provider_request_prepared",
                "package_scope_id": SCOPE_Q,
                "provider_request_identity": "pr_later",
                "provider_kind": "claude_initial_design",
                "supervisor_operation_id": "op_someone_else",
            }
        )
        context = H.build_context(
            journal=journal, adapter=self.adapter_for(envelope),
            clearance=lambda scope: {"unlocked": True},
        )
        state = commands.post_acceptance_transition_state(
            context, reconstruct_extra=H.full_reconstructor()
        )
        self.assertIsNotNone(state["prepared_task"])

    def test_8_1_historical_records_remain_preserved_and_replayable(self):
        """4 -- nothing is rewritten, converted or removed; the historical
        provider request replays under its ORIGINAL kind and semantics."""
        journal = H.staged_journal("task_preparation")
        before = copy.deepcopy(journal.events)
        self.complete_historical_t3(journal)
        appends = journal.appends
        context = H.build_context(
            journal=journal,
            adapter=self.adapter_for(LocalT3Rehearsals().sample_envelope()),
            clearance=lambda scope: {"unlocked": True},
        )
        commands.post_acceptance_transition_state(
            context, reconstruct_extra=H.full_reconstructor()
        )
        self.assertEqual(journal.appends, appends, "nothing was appended")
        self.assertEqual(
            journal.events[: len(before)], before, "nothing earlier was rewritten"
        )
        rep = replay_mod.Replay(journal.read(), SCOPE_Q)
        prepared = rep.prepared_event("pr_old_t3")
        self.assertIsNotNone(prepared, "the historical request still replays")
        self.assertEqual(
            prepared["provider_kind"], "codex_next_design_task_preparation"
        )
        self.assertEqual(
            prepared["result_schema_id"],
            "NH_NEXT_DESIGN_TASK_PREPARATION_LIFECYCLE_V1",
        )
        self.assertEqual(rep.provider_phase("pr_old_t3"), "terminal")
        custody = rep.custody_event("pr_old_t3")
        self.assertEqual(custody["work_item_kind"], "next_design_task_preparation")

    def test_8_1_an_admissible_historical_T3_stays_historical_not_local(self):
        """The other direction of section 8.1.  A historical provider-backed T3
        whose custody is still admissible legitimately yields a prepared
        position -- but a HISTORICAL one, carrying its own provider-produced
        specification.  It is never converted into a local envelope, and it is
        never counted as a local-T3 completion."""
        envelope = LocalT3Rehearsals().sample_envelope()
        journal = H.staged_journal("task_preparation")
        self.complete_historical_t3(
            journal, stale_target=TARGET_Q, terminal_kind="result_received"
        )
        transport = H.LoudStubTransport()
        context = H.build_context(
            journal=journal, adapter=self.adapter_for(envelope),
            transport=transport, clearance=lambda scope: {"unlocked": True},
        )
        state = commands.post_acceptance_transition_state(
            context, reconstruct_extra=H.full_reconstructor()
        )
        prepared = state["prepared_task"]
        self.assertIsNotNone(prepared, "the historical task is still admissible")
        # ORIGINAL MEANING: it carries the provider-produced specification and
        # is NOT a local envelope position.
        self.assertFalse(commands.is_local_task_envelope_position(prepared))
        self.assertIn("specification", prepared)
        self.assertNotIn(constants.LOCAL_TASK_ENVELOPE_PROMPT_KEY, prepared)
        self.assertNotIn(constants.LOCAL_TASK_ENVELOPE_DIGEST_KEY, prepared)
        # ...and no local-T3 completion was manufactured from it.
        self.assertIsNone(state["local_t3_completed_event_seq"])
        self.assertIsNone(
            commands.local_t3_phase_completed(
                journal.read(), SCOPE_Q, state["selection"]
            )
        )
        # Its T4 bindings therefore keep the HISTORICAL keys.
        extra = commands._initial_design_extra_inputs(
            context, prepared, prepared["target_path"]
        )
        self.assertIn("prepared_specification_sha256", extra)
        self.assertNotIn(constants.LOCAL_TASK_ENVELOPE_DIGEST_KEY, extra)
        self.assertEqual(transport.calls, [])

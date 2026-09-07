#!/usr/bin/env python3
"""Focused offline proof for the two provider-call merging changes."""

from __future__ import annotations

import base64
import hashlib
import inspect
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
for entry in (ROOT / "controller", ROOT / "interview_ui"):
    if str(entry) not in sys.path:
        sys.path.insert(0, str(entry))

import nh_loop  # noqa: E402
from nh_supervisor import auditresult, commands, constants, replay, status  # noqa: E402


def explanation_parts():
    return {
        key: "This clear package explanation uses ordinary words and states fact number %d."
        % index
        for index, key in enumerate(constants.EXPLANATION_CONTENT_PART_KEYS, 1)
    }


def operation_for(blocker_ref):
    return {
        "operation_kind": "add_test_requirement",
        "target_kind": "test_requirement",
        "target_anchor_identifier": "NH_TEST_REQUIREMENT_SET_V1",
        "target_identifier_mode": "canonical_addition_slot",
        "target_identifier": None,
        "target_field": None,
        "new_value_identifier": "result_usability",
        "blocker_ref": blocker_ref,
    }


def audit_value(*, blocked=True):
    candidate = "05_ACTIVE_CANDIDATE/NH_FOCUSED_TEST_v1_0_CANDIDATE.md"
    blocker = "f_one"
    findings = []
    mechanical = []
    if blocked:
        findings = [{
            "finding_ref": blocker,
            "severity": "IMPORTANT",
            "route": "claude_mechanical",
            "blocking": True,
            "sections": ["1"],
            "source_paths": [candidate],
            "proof": ["The focused evidence proves this blocker."],
            "smallest_correction": "Apply the complete correction supplied here.",
        }]
        mechanical = [blocker]
    return {
        "result_schema_id": "NH_DESIGN_AUDIT_RESULT_V2",
        "result_schema_version": 1,
        "whole_check_complete": True,
        "candidate_path": candidate,
        "candidate_sha256": "a" * 64,
        "candidate_bytes": 100,
        "reviewed_source_paths": [candidate],
        "verdict": "BLOCKED" if blocked else "PASS",
        "highest_severity": "IMPORTANT" if blocked else "NONE",
        "findings": findings,
        "mechanical_blocker_refs": mechanical,
        "review_required_blocker_refs": [],
        "mechanical_correction_specification": (
            {"finding_corrections": [{"finding_ref": blocker, "changes": ["Fix it fully."]}]}
            if blocked else None
        ),
        "normalized_correction_operations": (
            [operation_for(blocker)] if blocked else None
        ),
        "proposed_addition_names": [] if blocked else None,
        "bundle_placement": "UNRESOLVED",
        "controlled_component_id": None,
        "register_id": None,
        "implementation_authorized": False,
        "acceptance_claimed": False,
        "adoption_claimed": False,
        "installation_claimed": False,
        "authority_claimed": False,
        "plain_language_problem": "A real blocker remains.",
        "plain_language_impact": "The candidate cannot pass yet.",
        "summary": "Independent focused audit complete.",
    }


class ProviderCallMergingTests(unittest.TestCase):
    def test_blocked_audit_carries_complete_normalizable_correction(self):
        value = audit_value(blocked=True)
        self.assertEqual(auditresult.check_schema_valid(value), [])
        failed, _structural = auditresult.evaluate_usability(
            value,
            {key: value[key] for key in (
                "candidate_path", "candidate_sha256", "candidate_bytes"
            )},
            {value["candidate_path"]},
        )
        self.assertEqual(failed, [])
        situation = SimpleNamespace(blocking_finding_refs=["f_one"])
        normalized, errors = commands._embedded_audit_specification(
            SimpleNamespace(), situation, value
        )
        self.assertEqual(errors, [])
        self.assertEqual([item["blocker_ref"] for item in normalized], ["f_one"])

    def test_pass_audit_requires_null_correction_fields(self):
        value = audit_value(blocked=False)
        self.assertEqual(auditresult.check_schema_valid(value), [])
        value["normalized_correction_operations"] = []
        self.assertTrue(auditresult.check_schema_valid(value))

    def test_same_audit_provenance_records_runnable_specification(self):
        value = audit_value(blocked=True)
        situation = SimpleNamespace(
            candidate=SimpleNamespace(
                candidate_path=value["candidate_path"],
                candidate_sha256=value["candidate_sha256"],
                candidate_bytes=value["candidate_bytes"],
            ),
            replay=SimpleNamespace(correction_round_lifetime=lambda: 1),
        )
        binding = SimpleNamespace(
            package_scope_id="scope",
            source_binding_sha256="b" * 64,
        )
        context = SimpleNamespace(
            binding=binding,
            controller_executable_identity="controller",
            journal=SimpleNamespace(read=lambda: []),
        )
        appended = []
        operation_obj = SimpleNamespace(
            operation_id="operation",
            append=lambda kind, body: appended.append((kind, body)),
        )
        prepared = SimpleNamespace(
            work_item_identity="wi_audit",
            provider_kind="codex_design_audit",
            provider_request_identity="pr_audit",
            provider_availability_episode_identity="episode",
        )
        normalized, errors = commands._embedded_audit_specification(
            context, situation, value
        )
        self.assertEqual(errors, [])
        commands._append_embedded_audit_specification(
            context, operation_obj, situation, prepared,
            {"result_custody_identity": "custody"}, {"event_seq": 9},
            value, "audit", normalized,
        )
        self.assertEqual([kind for kind, _body in appended], [
            "correction_specification_recorded"
        ])
        self.assertEqual(appended[0][1]["provider_request_identity"], "pr_audit")
        self.assertEqual(appended[0][1]["provider_kind"], "codex_design_audit")

    def test_blocked_audit_custody_stays_recoverable_until_spec_is_durable(self):
        custody = {
            "work_item_kind": "design_audit",
            "result_schema_id": "NH_DESIGN_AUDIT_RESULT_V2",
            "provider_request_identity": "pr_audit",
        }
        terminal = {"terminal_kind": "result_received"}
        audit = {
            "type": "mechanical_audit_recorded",
            "provider_request_identity": "pr_audit",
            "audit_identity": "audit",
            "mechanical_blocker_refs": ["f_one"],
        }
        self.assertFalse(
            replay.Replay([audit])._downstream_recorded(custody, terminal)
        )
        specification = {
            "type": "correction_specification_recorded",
            "provider_request_identity": "pr_audit",
            "audit_identity": "audit",
        }
        self.assertTrue(
            replay.Replay([audit, specification])._downstream_recorded(
                custody, terminal
            )
        )

    def test_candidate_result_requires_same_call_explanation(self):
        payload = b"new candidate bytes"
        work_item = {
            "candidate_path": "X_v1_0_CANDIDATE.md",
            "candidate_sha256": "c" * 64,
            "candidate_bytes": 20,
            "target_candidate_path": "X_v1_1_CANDIDATE.md",
            "authorized_next_lifetime_round": 1,
            "authorized_batch_number": 1,
            "authorized_round_in_batch": 1,
            "correction_specification_sha256": "d" * 64,
            "blocking_finding_refs": ["f_one"],
        }
        value = {
            "result_schema_id": "NH_CLAUDE_CORRECTION_RESULT_V2",
            "result_schema_version": 1,
            "produced_candidate_path": work_item["target_candidate_path"],
            "produced_candidate_sha256": hashlib.sha256(payload).hexdigest(),
            "produced_candidate_bytes": len(payload),
            "produced_candidate_payload_base64": base64.b64encode(payload).decode("ascii"),
            "produced_lifetime_round": 1,
            "produced_batch_number": 1,
            "produced_round_in_batch": 1,
            "correction_specification_sha256": "d" * 64,
            "blocking_finding_refs": ["f_one"],
            "acceptance_explanation_content": explanation_parts(),
        }
        context = SimpleNamespace(_current_work_item_obj=work_item)
        self.assertEqual(commands._claude_admission_checks(context, None, value), [])
        value["acceptance_explanation_content"] = None
        self.assertIn("K9", commands._claude_admission_checks(context, None, value))

    def test_candidate_operation_records_bound_explanation_before_completion(self):
        appended = []
        operation_obj = SimpleNamespace(
            operation_id="operation",
            append=lambda kind, body: appended.append((kind, body)),
        )
        context = SimpleNamespace(
            journal=SimpleNamespace(read=lambda: []),
            binding=SimpleNamespace(
                package_scope_id="scope",
                source_binding_sha256="e" * 64,
            ),
        )
        candidate = SimpleNamespace(
            candidate_path="X_v1_1_CANDIDATE.md",
            candidate_sha256="f" * 64,
            candidate_bytes=123,
            parent_candidate_path="X_v1_0_CANDIDATE.md",
            parent_candidate_sha256="a" * 64,
            parent_candidate_bytes=100,
        )
        prepared = SimpleNamespace(
            work_item_identity="wi_claude",
            provider_kind="claude_correction",
            provider_request_identity="pr_claude",
        )
        outcome = commands._record_acceptance_explanation_content(
            context,
            operation_obj,
            candidate,
            prepared,
            {"result_custody_identity": "custody"},
            {"event_seq": 7},
            explanation_parts(),
        )
        self.assertEqual(
            outcome["outcome"], "content_stage_acceptance_explanation_recorded"
        )
        self.assertEqual([kind for kind, _body in appended], [
            "mechanical_change_explanation_recorded"
        ])
        body = appended[0][1]
        self.assertEqual(body["candidate_sha256"], "f" * 64)
        self.assertEqual(body["parent_candidate_sha256"], "a" * 64)
        self.assertEqual(body["provider_request_identity"], "pr_claude")

    def test_recovery_keeps_same_call_candidate_custody_open_until_prose_exists(self):
        custody = {
            "type": "provider_result_custody_recorded",
            "package_scope_id": "scope",
            "provider_request_identity": "pr_claude",
            "work_item_identity": "wi_claude",
            "work_item_kind": "correction_apply",
            "result_schema_id": "NH_CLAUDE_CORRECTION_RESULT_V2",
        }
        terminal = {"terminal_kind": "result_received"}
        completion = {
            "type": "diagnosis_strategy_consumption_completed",
            "package_scope_id": "scope",
            "provider_request_identity": "pr_claude",
        }
        without_prose = replay.Replay([completion], "scope")
        self.assertFalse(without_prose._downstream_recorded(custody, terminal))
        prose = {
            "type": "mechanical_change_explanation_recorded",
            "package_scope_id": "scope",
            "provider_request_identity": "pr_claude",
            "work_item_identity": "wi_claude",
            "explanation_stage": constants.EXPLANATION_STAGE_CONTENT,
            "explanation_content_digest": "a" * 64,
        }
        with_prose = replay.Replay([completion, prose], "scope")
        self.assertTrue(with_prose._downstream_recorded(custody, terminal))

    def test_transport_extracts_exact_six_parts_only(self):
        parts = explanation_parts()
        text = nh_loop.json.dumps(parts)
        self.assertEqual(nh_loop.extract_candidate_acceptance_explanation(text), parts)
        parts["extra"] = "not permitted"
        self.assertIsNone(
            nh_loop.extract_candidate_acceptance_explanation(nh_loop.json.dumps(parts))
        )

    def test_prompts_require_both_combined_results(self):
        claude_prompt = nh_loop._supervisor_provider_prompt({
            "provider_kind": "claude_correction",
            "candidate_acceptance_explanation_preparation": {"required_parts": []},
            "acceptance_explanation_preparation": None,
            "acceptance_explanation_under_audit": None,
        })
        self.assertIn("SAME-CALL ACCEPTANCE EXPLANATION", claude_prompt)
        self.assertIn("EXACTLY the six keys", claude_prompt)
        audit_prompt = nh_loop._supervisor_provider_prompt({
            "provider_kind": "codex_design_audit",
            "candidate_acceptance_explanation_preparation": None,
            "acceptance_explanation_preparation": None,
            "acceptance_explanation_under_audit": {"parts": explanation_parts()},
        })
        self.assertIn("AUDIT AND CORRECTION CONTRACT", audit_prompt)
        self.assertIn("complete Claude-ready correction", audit_prompt)
        self.assertIn("Review any acceptance_explanation_under_audit", audit_prompt)

    def test_acceptance_explanation_shows_the_whole_flow_and_connected_parts_in_layers(self):
        preparation = nh_loop.ACCEPTANCE_EXPLANATION_PREPARATION_INSTRUCTION
        audit = nh_loop.ACCEPTANCE_EXPLANATION_AUDIT_INSTRUCTION

        self.assertIn("start-to-finish real-use flow", preparation)
        self.assertIn("each material part", preparation)
        self.assertIn("how the parts connect", preparation)
        self.assertIn("do not overwhelm", preparation)
        self.assertIn("whole flow and the connected parts", audit)
        self.assertIn("understand without information overload", audit)

    def test_normal_scheduler_has_no_separate_call_launch_points(self):
        source = inspect.getsource(status.Situation._work_item)
        self.assertNotIn("correction_specification_work_item(", source)
        self.assertNotIn("acceptance_explanation_content_work_item(", source)


if __name__ == "__main__":
    unittest.main()

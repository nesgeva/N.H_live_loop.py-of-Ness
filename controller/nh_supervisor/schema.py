#!/usr/bin/env python3
"""Section 4.1 / 4.2 -- the exact supervisor-era journal schema.

The shorthand sets below are set notation only; this module expands them into
literal ``frozenset`` values exactly as Section 4.2 requires.  Nothing here
performs I/O.  ``build_version5_body_keys`` takes the installed version-4 body
key map and produces the version-5 map, so the two versions cannot drift and no
stored version-4 byte is ever rewritten.  ``build_version6_body_keys`` extends
that table with version 6, which is built FROM the version-5 rows and differs
from them by exactly one acceptance delta -- three registered types gain keys
and one new event-type name exists -- so version 5 is the FIRST
supervisor-capable version rather than the only one.  Version 4 and version 5
are never retrofitted: stored history stays readable against exactly its own
schemas.  Version 7 adds the single transition-choice row used to preserve an
explicit Ness choice between two already-proved live-loop operands.
"""

from __future__ import annotations

from . import constants

PACKAGE_SOURCE = frozenset(
    (
        "package_key",
        "package_scope_id",
        "package_id",
        "branch",
        "head_sha",
        "source_binding_sha256",
        "standing_before_sha256",
    )
)

CANDIDATE = frozenset(
    (
        "candidate_path",
        "candidate_sha256",
        "candidate_bytes",
        "correction_round_lifetime",
        "correction_batch_number",
        "correction_round_in_batch",
    )
)

PROVIDER_BINDING = frozenset(
    (
        "provider_kind",
        "provider_endpoint_identity",
        "provider_availability_episode_identity",
        "provider_availability_episode_generation",
        "provider_request_identity",
        "provider_dispatch_serial",
    )
)

DEPENDENCY_SLOT = frozenset(
    (
        "dependency_record",
        "dependency_identity",
        "dependency_carrier_event_seq",
        "dependency_occurrence_ordinal",
    )
)

OPERATION_BINDING = frozenset(
    (
        "controller_executable_identity",
        "package_scope_id",
        "source_binding_sha256",
        "candidate_path",
        "candidate_sha256",
        "candidate_bytes",
        "controller_report_sha256",
    )
)

# The three candidate events keep their version-4 body key set with
# ``correction_round`` removed and these three added (Section 4.1).
CANDIDATE_EVENT_TYPES = frozenset(
    (
        "candidate_write_ahead_recorded",
        "candidate_write_ahead_aborted",
        "candidate_custody_recorded",
    )
)
CANDIDATE_EVENT_ADDED_KEYS = frozenset(
    (
        "correction_round_lifetime",
        "correction_batch_number",
        "correction_round_in_batch",
    )
)
CANDIDATE_EVENT_REMOVED_KEY = "correction_round"

# The six non-candidate version-4 types keep their exact version-4 body key set.
VERSION4_NON_CANDIDATE_TYPES = frozenset(
    (
        "validation_recorded",
        "routed_issue_recorded",
        "review_signal_recorded",
        "question_coverage_review_recorded",
        "group_presented",
        "answer_recorded",
    )
)

# The two Piece-3 types whose appends require a Section 9.8 authorization.
PIECE3_AUTHORIZED_EVENT_TYPES = frozenset(
    ("validation_recorded", "question_coverage_review_recorded")
)


def _b(*parts):
    result = set()
    for part in parts:
        if isinstance(part, (set, frozenset)):
            result |= set(part)
        else:
            result |= set(part)
    return frozenset(result)


# ---------------------------------------------------------------------------
# Section 4.2 -- the supervisor-era event body schemas.  These types exist from
# version 5 onward; a version-4 event carrying one of them has no schema for
# its (journal_version, type) pair and fails closed.
# ---------------------------------------------------------------------------
SUPERVISOR_EVENT_BODY_KEYS = {
    "mechanical_audit_recorded": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        (
            "settled_decision_binding_sha256",
            "audit_identity",
            "verdict",
            "highest_severity",
            "findings",
            "mechanical_blocker_refs",
            "review_required_blocker_refs",
            "codex_invoked",
            "codex_exit_code",
            "audit_schema_valid",
            "audit_source_stable",
            "audit_usability_proved",
            "terminal_chain_sha256",
            "work_item_identity",
            "provider_kind",
            "provider_request_identity",
            "result_custody_identity",
            "provider_terminal_event_seq",
        ),
    ),
    "mechanical_audit_unusable_recorded": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        DEPENDENCY_SLOT,
        (
            "controller_executable_identity",
            "supervisor_operation_id",
            "work_item_identity",
            "provider_kind",
            "provider_request_identity",
            "provider_availability_episode_identity",
            "result_custody_identity",
            "result_custody_event_seq",
            "provider_terminal_event_seq",
            "provider_terminal_kind",
            "audit_usability_failure_class",
            "failed_audit_check_ids",
            "audit_result_facts_sha256",
            "output_retries_used",
            "output_retry_eligible",
            "next_workflow_state",
        ),
    ),
    "correction_batch_checkpoint_recorded": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        (
            "checkpoint_identity",
            "audit_identity",
            "blocking_finding_refs",
            "checkpoint_outcome",
        ),
    ),
    "mechanical_no_progress_recorded": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        (
            "no_progress_identity",
            "blocking_finding_refs",
            "correction_specification_sha256",
            "diagnosis_strategy_sha256",
            "strategy_novelty_key",
            "claude_result_facts_sha256",
            "diagnosis_required",
            "work_item_identity",
            "provider_kind",
            "provider_request_identity",
            "result_custody_identity",
            "provider_terminal_event_seq",
            "semantic_scope_key",
            "semantic_unlock_generation",
            "no_progress_ordinal_in_scope",
            "consumption_identity",
            "consumption_started_event_seq",
            "terminates_consumption",
        ),
    ),
    "correction_specification_recorded": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        (
            "controller_executable_identity",
            "supervisor_operation_id",
            "specification_identity",
            "work_item_identity",
            "provider_kind",
            "provider_request_identity",
            "provider_availability_episode_identity",
            "result_custody_identity",
            "provider_terminal_event_seq",
            "audit_identity",
            "blocking_finding_refs",
            "mechanical_correction_specification",
            "correction_specification_sha256",
            "normalized_correction_operations",
            "proposed_addition_names",
            "strategy_novelty_key",
            "authorized_next_lifetime_round",
            "authorized_batch_number",
            "authorized_round_in_batch",
            "next_workflow_state",
        ),
    ),
    "correction_diagnosis_recorded": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        DEPENDENCY_SLOT,
        (
            "diagnosis_trigger_type",
            "diagnosis_trigger_event_seq",
            "diagnosis_trigger_identity",
            "diagnosis_input_sha256",
            "diagnosis_result_sha256",
            "diagnosis_outcome",
            "source_paths_checked",
            "blocking_finding_refs",
            "root_cause_plain",
            "why_previous_approach_survived",
            "strategy_identity_material",
            "diagnosis_strategy_sha256",
            "strategy_novelty_key",
            "normalized_correction_operations",
            "proposed_addition_names",
            "mechanical_correction_specification",
            "correction_specification_sha256",
            "review_signal",
            "plain_language_problem",
            "plain_language_impact",
            "authorized_next_lifetime_round",
            "authorized_batch_number",
            "authorized_round_in_batch",
            "work_item_identity",
            "provider_kind",
            "provider_request_identity",
            "result_custody_identity",
            "provider_terminal_event_seq",
            "semantic_scope_key",
            "next_workflow_state",
        ),
    ),
    "correction_diagnosis_rejected_recorded": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        DEPENDENCY_SLOT,
        (
            "diagnosis_trigger_identity",
            "diagnosis_input_sha256",
            "diagnosis_result_sha256",
            "rejection_code",
            "rejected_strategy_novelty_key",
            "blocking_finding_refs",
            "trigger_rejection_ordinal",
            "trigger_diagnosis_attempt_ordinal",
            "work_item_identity",
            "provider_kind",
            "provider_request_identity",
            "result_custody_identity",
            "provider_terminal_event_seq",
            "semantic_scope_key",
            "semantic_scope_exhaustion_event_seq",
            "next_workflow_state",
        ),
    ),
    "correction_diagnosis_validation_failed_recorded": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        DEPENDENCY_SLOT,
        (
            "controller_executable_identity",
            "supervisor_operation_id",
            "diagnosis_trigger_identity",
            "diagnosis_input_sha256",
            "diagnosis_result_sha256",
            "work_item_identity",
            "provider_kind",
            "provider_request_identity",
            "provider_availability_episode_identity",
            "result_custody_identity",
            "provider_terminal_event_seq",
            "provider_terminal_kind",
            "validation_failure_class",
            "failed_validation_rule_ids",
            "blocking_finding_refs",
            "trigger_diagnosis_attempt_ordinal",
            "output_retries_used",
            "output_retry_eligible",
            "next_workflow_state",
        ),
    ),
    "diagnosis_strategy_consumption_started": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        (
            "consumption_identity",
            "diagnosis_event_seq",
            "diagnosis_event_sha256",
            "diagnosis_strategy_sha256",
            "strategy_novelty_key",
            "blocking_finding_refs",
            "correction_specification_sha256",
            "target_candidate_path",
            "authorized_next_lifetime_round",
            "authorized_batch_number",
            "authorized_round_in_batch",
            "work_item_identity",
            "consumption_authority_kind",
        ),
    ),
    "diagnosis_strategy_consumption_completed": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        (
            "consumption_identity",
            "consumption_started_event_seq",
            "diagnosis_event_seq",
            "diagnosis_event_sha256",
            "diagnosis_strategy_sha256",
            "strategy_novelty_key",
            "blocking_finding_refs",
            "correction_specification_sha256",
            "produced_candidate_path",
            "produced_candidate_sha256",
            "produced_candidate_bytes",
            "produced_lifetime_round",
            "produced_batch_number",
            "produced_round_in_batch",
            "work_item_identity",
            "provider_kind",
            "provider_request_identity",
            "result_custody_identity",
            "provider_terminal_event_seq",
            "custody_event_seq",
        ),
    ),
    "diagnosis_strategy_consumption_terminated": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        DEPENDENCY_SLOT,
        (
            "consumption_identity",
            "consumption_started_event_seq",
            "diagnosis_event_seq",
            "diagnosis_event_sha256",
            "diagnosis_strategy_sha256",
            "strategy_novelty_key",
            "blocking_finding_refs",
            "correction_specification_sha256",
            "work_item_identity",
            "provider_kind",
            "provider_request_identity",
            "result_custody_identity",
            "provider_terminal_event_seq",
            "termination_kind",
            "termination_evidence_event_seq",
            "termination_evidence_event_sha256",
            "next_workflow_state",
        ),
    ),
    "provider_request_prepared": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        PROVIDER_BINDING,
        (
            "controller_executable_identity",
            "supervisor_operation_id",
            "work_item_identity",
            "work_item_kind",
            "provider_capability_record_identity",
            "provider_capability_record_sha256",
            "provider_capability_source",
            "prompt_material_sha256",
            "required_inputs_sha256",
            "result_schema_id",
            "idempotency_key_sent",
            "consumption_identity",
        ),
    ),
    "provider_dispatch_begun": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        PROVIDER_BINDING,
        (
            "controller_executable_identity",
            "supervisor_operation_id",
            "work_item_identity",
            "provider_request_prepared_event_seq",
            "dispatch_transport",
            "dispatch_pid",
            "dispatch_process_start_ticks",
            "dispatch_boot_id_sha256",
        ),
    ),
    "provider_request_accepted": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        PROVIDER_BINDING,
        (
            "controller_executable_identity",
            "supervisor_operation_id",
            "work_item_identity",
            "provider_dispatch_begun_event_seq",
            "acceptance_authority",
            "provider_side_request_ref",
            "acceptance_evidence_sha256",
        ),
    ),
    "provider_result_custody_recorded": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        PROVIDER_BINDING,
        (
            "controller_executable_identity",
            "supervisor_operation_id",
            "work_item_identity",
            "work_item_kind",
            "provider_dispatch_begun_event_seq",
            "result_custody_identity",
            "result_origin",
            "result_location_kind",
            "result_location_id",
            "result_object_name",
            "result_bytes_base64",
            "result_byte_length",
            "result_sha256",
            "result_schema_id",
            "result_schema_version",
            "result_schema_valid",
            "custody_readback_proved",
            "consumption_identity",
            "custody_next_step",
        ),
    ),
    "provider_request_reconciled": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        PROVIDER_BINDING,
        DEPENDENCY_SLOT,
        (
            "controller_executable_identity",
            "supervisor_operation_id",
            "work_item_identity",
            "observed_phase_before",
            "lookup_supported",
            "lookup_authority",
            "lookup_performed",
            "reconciliation_outcome",
            "provider_side_request_ref",
            "lookup_evidence_sha256",
            "result_custody_identity",
            "next_workflow_state",
        ),
    ),
    "provider_request_terminal_recorded": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        PROVIDER_BINDING,
        DEPENDENCY_SLOT,
        (
            "controller_executable_identity",
            "supervisor_operation_id",
            "work_item_identity",
            "provider_dispatch_begun_event_seq",
            "terminal_kind",
            "terminal_evidence_kind",
            "result_custody_identity",
            "result_custody_event_seq",
            "provider_result_facts_sha256",
            "provider_outcome_facts",
            "provider_error_signal_token",
            "provider_error_classification_row_id",
            "provider_returncode",
            "result_schema_valid",
            "oversize_detection_kind",
            "observed_bytes_read",
            "declared_result_byte_length",
        ),
    ),
    "provider_availability_episode_exhausted_recorded": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        DEPENDENCY_SLOT,
        (
            "controller_executable_identity",
            "supervisor_operation_id",
            "work_item_identity",
            "provider_kind",
            "provider_endpoint_identity",
            "provider_availability_episode_identity",
            "provider_availability_episode_generation",
            "closed_attempt_count",
            "closed_attempt_request_identities",
            "all_attempts_terminal_proved",
            "open_consumption_identity",
            "provider_capability_record_identity",
            "provider_capability_record_sha256",
            "provider_capability_source",
            "person_route_reason",
            "user_action_code",
            "next_workflow_state",
        ),
    ),
    "availability_probe_begun": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        (
            "controller_executable_identity",
            "supervisor_operation_id",
            "work_item_identity",
            "provider_kind",
            "provider_endpoint_identity",
            "closed_episode_identity",
            "closed_episode_generation",
            "availability_probe_identity",
            "probe_serial",
            "probe_command_identity",
            "probe_input_sha256",
            "probe_is_non_generative",
            "probe_transport",
            "probe_pid",
            "probe_process_start_ticks",
            "probe_boot_id_sha256",
            "provider_capability_record_identity",
            "provider_capability_record_sha256",
        ),
    ),
    "availability_probe_result_recorded": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        DEPENDENCY_SLOT,
        (
            "controller_executable_identity",
            "supervisor_operation_id",
            "work_item_identity",
            "provider_kind",
            "provider_endpoint_identity",
            "closed_episode_identity",
            "availability_probe_identity",
            "availability_probe_begun_event_seq",
            "probe_outcome",
            "probe_observation_facts",
            "probe_classification_row_id",
            "probe_result_byte_length",
            "probe_result_sha256",
            "probe_result_facts_sha256",
            "next_workflow_state",
        ),
    ),
    "provider_availability_unlock_recorded": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        DEPENDENCY_SLOT,
        (
            "controller_executable_identity",
            "supervisor_operation_id",
            "work_item_identity",
            "provider_kind",
            "provider_endpoint_identity",
            "closed_episode_identity",
            "closed_episode_generation",
            "exhaustion_event_seq",
            "exhaustion_event_sha256",
            "exhaustion_person_route_reason",
            "outstanding_person_conditions_empty",
            "c11a_self_occurrence_carrier_event_seq",
            "c11a_self_occurrence_ordinal",
            "c11a_self_condition_satisfied",
            "unlock_invocation_kind",
            "unlock_evidence_kind",
            "unlock_evidence_identity",
            "unlock_evidence_sha256",
            "unlock_baseline_capability_record_sha256",
            "unlock_observed_capability_record_sha256",
            "unlock_probe_identity",
            "unlock_probe_result_event_seq",
            "unlock_probe_outcome",
            "unlock_wait_satisfied",
            "unlock_accepted",
            "opened_episode_generation",
            "opened_episode_identity",
            "resumed_consumption_identity",
            "user_action_code",
            "next_workflow_state",
        ),
    ),
    "semantic_scope_exhaustion_recorded": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        DEPENDENCY_SLOT,
        (
            "controller_executable_identity",
            "supervisor_operation_id",
            "work_item_identity",
            "scope_exhaustion_identity",
            "exhausted_semantic_scope_key",
            "exhausted_semantic_unlock_generation",
            "exhaustion_trigger_kind",
            "diagnosis_trigger_identity",
            "trigger_diagnosis_attempt_ordinal",
            "no_progress_rounds_in_scope",
            "exhausted_novelty_key_count",
            "capability_baseline",
            "capability_baseline_snapshot_sha256",
            "next_workflow_state",
        ),
    ),
    "semantic_scope_unlock_recorded": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        DEPENDENCY_SLOT,
        (
            "controller_executable_identity",
            "supervisor_operation_id",
            "work_item_identity",
            "exhausted_semantic_scope_key",
            "exhausted_no_progress_rounds",
            "exhausted_novelty_key_count",
            "baseline_exhaustion_event_seq",
            "baseline_exhaustion_event_sha256",
            "capability_baseline_snapshot_sha256",
            "capability_observed_snapshot",
            "capability_observed_snapshot_sha256",
            "changed_entry_count",
            "unlock_evidence_kind",
            "unlock_evidence_identity",
            "unlock_evidence_sha256",
            "unlock_evidence_baseline_sha256",
            "unlock_selection_rule_id",
            "prior_semantic_unlock_generation",
            "opened_semantic_unlock_generation",
            "opened_semantic_scope_key",
            "unlock_accepted",
            "next_workflow_state",
        ),
    ),
    "piece3_provider_work_recorded": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        (
            "controller_executable_identity",
            "supervisor_operation_id",
            "work_item_identity",
            "work_item_kind",
            "provider_kind",
            "provider_endpoint_identity",
            "provider_request_identity",
            "provider_availability_episode_identity",
            "result_custody_identity",
            "provider_terminal_event_seq",
            "authorizes_event_type",
            "routed_signal_refs",
            "validation_set_id",
            "piece3_standing_sha256",
            "result_schema_valid",
            "next_workflow_state",
        ),
    ),
    "mechanical_change_explanation_recorded": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        (
            "parent_candidate_path",
            "parent_candidate_sha256",
            "parent_candidate_bytes",
            "change_explanation_identity",
            "blocking_finding_refs",
            "correction_specification_sha256",
            "diff_sha256",
            "reviewer_result_sha256",
            "source_paths_checked",
            "plain_language_change",
            "plain_language_real_use_effect",
            "meaning_or_policy_changed",
            "changed_sections",
            "technical_summary",
            "work_item_identity",
            "provider_kind",
            "provider_request_identity",
            "result_custody_identity",
            "provider_terminal_event_seq",
        ),
    ),
    "mechanical_pass_recorded": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        (
            "pass_identity",
            "audit_identity",
            "terminal_chain_sha256",
            "settled_decision_binding_sha256",
            "validation_set_id",
            "coverage_review_event_seq",
            "no_pending_write_ahead",
            "frozen_envelope_clean",
            "no_open_provider_request",
            "no_open_result_custody",
            "no_open_availability_probe",
            "no_open_audit_usability_retry",
            "pass_outcome",
        ),
    ),
    "supervisor_operation_started": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        (
            "controller_executable_identity",
            "supervisor_operation_id",
            "supervisor_command",
            "work_item_identity",
            "pre_state_sha256",
            "input_envelope_sha256",
            "controller_report_sha256",
            "unlock_evidence_kind",
            "unlock_evidence_identity",
            "unlock_evidence_sha256",
        ),
    ),
    "supervisor_operation_completed": _b(
        PACKAGE_SOURCE,
        CANDIDATE,
        DEPENDENCY_SLOT,
        (
            "controller_executable_identity",
            "supervisor_operation_id",
            "supervisor_started_event_seq",
            "supervisor_command",
            "work_item_identity",
            "controller_returncode",
            "controller_report_sha256",
            "operation_outcome",
            "post_state_sha256",
            "retry_series_key",
        ),
    ),
}

# ---------------------------------------------------------------------------
# Section 4.2 -- the VERSION-6 delta.  Version 6 is the first body version that
# carries the accepted acceptance-record design.  It is built FROM the
# version-5 rows above so a type nobody changed cannot drift, and it changes
# exactly four rows: three ALREADY REGISTERED types gain keys, and one new
# event-type name exists for the first time.  Nothing below touches version 4
# or version 5 -- an acceptance key is never retrofitted into the schema a
# stored history is read against.
# ---------------------------------------------------------------------------

# Section 9.1 -- the one and only new authenticated event-type name.  It exists
# at version 6 and at no earlier version: the pair (5, this name) has no schema
# and therefore fails closed, exactly as an unknown pair must.
NESS_CANDIDATE_ACCEPTANCE_EVENT_TYPE = "ness_candidate_acceptance_recorded"

# Section 6.2 -- the eight fixed explanation parts, each present and nonempty.
# They are eight distinct keys because they are eight distinct required parts:
# a missing part is then a missing key, which the body-key check already
# refuses, rather than an empty stretch inside one blob nobody can see into.
EXPLANATION_PARTS = frozenset(
    (
        "explanation_part_1_what_this_package_does",
        "explanation_part_2_what_actually_changed",
        "explanation_part_3_what_changed_from_previous_candidate",
        "explanation_part_4_what_this_changes_for_nh_in_real_use",
        "explanation_part_5_what_did_not_change",
        "explanation_part_6_what_is_still_open",
        "explanation_part_7_audit_result",
        "explanation_part_8_what_clicking_accept_means",
    )
)

# Section 8.2 / 9.3 -- the COMPLETE pre-click authenticated head, field by
# field.  All eight installed head fields are carried; none is omitted and none
# is treated as a summary of the others, because a head can move in ways that
# leave any proper subset of them unchanged.  These prefixed body spellings
# name the same eight head fields the complete-head digest is taken over.
PRE_CLICK_HEAD_BODY_KEYS = frozenset(
    (
        "pre_click_head_v",
        "pre_click_head_intent_generation",
        "pre_click_head_intent_number",
        "pre_click_head_intent_event_seq",
        "pre_click_head_intent_event_sha256",
        "pre_click_head_committed_event_seq",
        "pre_click_head_committed_event_sha256",
        "pre_click_head_auth_sha256",
    )
)

# Section 14 Phase A step A3 -- the audit read the content stage's exact fixed
# prose, so the audit record says which bytes it read.
VERSION6_AUDIT_ADDED_KEYS = frozenset(("explanation_content_digest",))

# Section 7.4 / 7.6 -- what the EXISTING explanation carrier must additionally
# be able to hold to carry the two-stage acceptance explanation.  The
# correction-stage fields are kept, not replaced: one type, one key set per
# version, and later stage-specific validation is what requires the right
# values and the right explicit nulls for the stage a record declares.
#
# Deliberately absent, because the accepted design forbids them: a pass
# event_seq and a pass event_sha256 (Section 7.4a -- this record is appended
# BEFORE the pass event, so no honest value for either exists here), and a
# supervisor_operation_id (Section 7.1b -- no gate may claim to compare a field
# the installed records do not carry).  The candidate, package and source
# binding and the parent triple are already in the version-5 row.
VERSION6_EXPLANATION_ADDED_KEYS = _b(
    EXPLANATION_PARTS,
    (
        # Which stage this record is.  Required, never inferred: without it the
        # correction-stage and acceptance-stage records are indistinguishable.
        "explanation_stage",
        # Record identity, version, and the two digests.
        "explanation_record_identity",
        "explanation_version",
        "explanation_content_digest",
        "explanation_digest",
        # Audit binding -- a BACKWARD reference to an event that already
        # exists; explicit null at the content stage.
        "audit_identity",
        "audit_event_seq",
        "audit_event_sha256",
        # PASS binding -- the deterministic identity, and only that.
        "pass_identity",
        # The final stage's back-reference to its own content stage.
        "content_stage_explanation_record_identity",
        "content_stage_event_seq",
        "content_stage_event_sha256",
        # Section 7.6 -- an honest absence is a positive statement, so "there
        # is genuinely no predecessor" is a recorded value and never a silence.
        "predecessor_state",
        # The fixed acceptance-scope text actually shown, which is part 8.
        "acceptance_scope_id",
        "acceptance_scope_digest",
        # Section 7.5 -- supersession, or explicit null.
        "supersedes_explanation_identity",
        # Section 7.8 -- how the prose was produced.  The work item, provider
        # and result-custody identities of a draft are already carried by the
        # version-5 row, so only the honest kind is added.
        "preparation_kind",
    ),
)

# Section 19 -- the refusal carrier.  One appendable refusal is exactly one
# supervisor_operation_completed and zero supervisor_operation_started:
# supervisor_started_event_seq is written as present JSON null, which is the
# value the installed writer already emits when there is no start event, so no
# new shape is invented for it.  The refusal class maps onto the EXISTING
# operation_outcome vocabulary and adds no outcome value.  The record carries
# only what the controller itself proved -- never the rejected body, never an
# unvalidated field, never attacker-supplied text -- and the package/source and
# candidate binding it proved is already in the version-5 row.
VERSION6_OPERATION_COMPLETED_ADDED_KEYS = frozenset(
    (
        "acceptance_refusal_class",
        # The offer actually presented, where one validly was.  Where the
        # controller could prove nothing about the request, the class says so
        # and these carry null rather than an echoed value nobody proved.
        "acceptance_offer_id",
        "acceptance_offer_binding_sha256",
    )
)

# Section 8.2 / 9.3 -- the acceptance record's body.  It carries the whole
# binding set: no element of Section 8.2 may be absent.  It carries no
# dependency slot and no operation identity, because the accepted design gives
# it neither -- one successful click is one append and nothing else.
NESS_CANDIDATE_ACCEPTANCE_BODY_KEYS = _b(
    PACKAGE_SOURCE,
    CANDIDATE,
    PRE_CLICK_HEAD_BODY_KEYS,
    (
        "settled_decision_binding_sha256",
        # The exact final usable audit.
        "audit_identity",
        "audit_event_seq",
        "audit_event_sha256",
        # The exact mechanical_pass_recorded.  Here the pass event certainly
        # exists and its position is certainly known, which is why Section 7.4a
        # moves that position out of the explanation record and into this one.
        "pass_identity",
        "pass_event_seq",
        "pass_event_sha256",
        # The exact explanation that was shown.
        "explanation_record_identity",
        "explanation_version",
        "explanation_digest",
        "explanation_event_seq",
        "explanation_event_sha256",
        # The actual predecessor, or the honest "none stated" with nulls.
        "predecessor_state",
        "predecessor_candidate_path",
        "predecessor_candidate_sha256",
        "predecessor_candidate_bytes",
        # The fixed non-authorization text actually shown.
        "acceptance_scope_id",
        "acceptance_scope_digest",
        # The pre-click authenticated event tail.
        "pre_click_authenticated_event_seq",
        "pre_click_authenticated_tail_sha256",
        # Section 8.3a -- the canonical complete-head digest over exactly the
        # eight head fields above.  A convenience for exact comparison, never a
        # substitute for comparing every one of the eight.
        "pre_click_head_digest_sha256",
        "controller_executable_identity",
        "terminal_chain_sha256",
        # The act, and its result.
        "ness_acceptance_identity",
        "acceptance_disposition",
        "ness_browser_action",
        "acceptance_action_channel",
        "acceptance_offer_binding_sha256",
        "revalidation_outcome",
    ),
)

# The version-6 supervisor inventory: every version-5 row, the four rows the
# acceptance design changes, and nothing else.
VERSION6_SUPERVISOR_EVENT_BODY_KEYS = dict(SUPERVISOR_EVENT_BODY_KEYS)
VERSION6_SUPERVISOR_EVENT_BODY_KEYS.update(
    {
        "mechanical_audit_recorded": _b(
            SUPERVISOR_EVENT_BODY_KEYS["mechanical_audit_recorded"],
            VERSION6_AUDIT_ADDED_KEYS,
        ),
        "mechanical_change_explanation_recorded": _b(
            SUPERVISOR_EVENT_BODY_KEYS["mechanical_change_explanation_recorded"],
            VERSION6_EXPLANATION_ADDED_KEYS,
        ),
        "supervisor_operation_completed": _b(
            SUPERVISOR_EVENT_BODY_KEYS["supervisor_operation_completed"],
            VERSION6_OPERATION_COMPLETED_ADDED_KEYS,
        ),
        NESS_CANDIDATE_ACCEPTANCE_EVENT_TYPE: NESS_CANDIDATE_ACCEPTANCE_BODY_KEYS,
    }
)

NESS_TRANSITION_CHOICE_EVENT_TYPE = "ness_transition_choice_recorded"
NESS_TRANSITION_CHOICE_BODY_KEYS = frozenset(
    (
        "transition_choice_identity",
        "acceptance_event_seq",
        "acceptance_event_sha256",
        "pre_choice_authenticated_event_seq",
        "pre_choice_authenticated_tail_sha256",
        "ness_choice_exact",
        "ness_action_confirmed",
        "package_key",
        "package_scope_id",
        "package_id",
        "scope_root_path",
        "root_sha256",
        "root_bytes",
        "source_binding_sha256",
        "selected_result_custody_identity",
        "selected_result_custody_event_seq",
        "selected_result_custody_event_sha256",
        "selected_terminal_event_seq",
        "selected_terminal_event_sha256",
        "postponed_package_scope_id",
        "postponed_evidence_event_seq",
        "postponed_evidence_event_sha256",
        "controller_executable_identity",
        "standing_before_sha256",
    )
)

VERSION7_SUPERVISOR_EVENT_BODY_KEYS = dict(VERSION6_SUPERVISOR_EVENT_BODY_KEYS)
VERSION7_SUPERVISOR_EVENT_BODY_KEYS[NESS_TRANSITION_CHOICE_EVENT_TYPE] = (
    NESS_TRANSITION_CHOICE_BODY_KEYS
)

NESS_ROUTED_CHOICE_ANSWER_EVENT_TYPE = "ness_routed_choice_answer_recorded"
NESS_ROUTED_CHOICE_ANSWER_BODY_KEYS = frozenset(
    (
        "routed_choice_answer_identity",
        "transition_choice_identity",
        "transition_choice_event_seq",
        "transition_choice_event_sha256",
        "active_package_scope_id",
        "postponed_package_scope_id",
        "routed_signal_id",
        "routed_signal_event_seq",
        "routed_signal_event_sha256",
        "standing_target_id",
        "provider_request_identity",
        "provider_result_custody_identity",
        "provider_result_custody_event_seq",
        "provider_result_custody_event_sha256",
        "provider_result_sha256",
        "ness_answer_exact",
        "selected_option_id",
        "ness_action_confirmed",
        "pre_answer_authenticated_event_seq",
        "pre_answer_authenticated_tail_sha256",
        "controller_executable_identity",
        "standing_before_sha256",
    )
)

VERSION8_SUPERVISOR_EVENT_BODY_KEYS = dict(VERSION7_SUPERVISOR_EVENT_BODY_KEYS)
VERSION8_SUPERVISOR_EVENT_BODY_KEYS[NESS_ROUTED_CHOICE_ANSWER_EVENT_TYPE] = (
    NESS_ROUTED_CHOICE_ANSWER_BODY_KEYS
)

NESS_TRANSITION_RECOVERY_CHOICE_EVENT_TYPE = (
    "ness_transition_recovery_choice_recorded"
)
NESS_TRANSITION_RECOVERY_CHOICE_BODY_KEYS = frozenset(
    (
        "transition_recovery_choice_identity",
        "provider_request_identity",
        "provider_request_prepared_event_seq",
        "provider_request_prepared_event_sha256",
        "provider_dispatch_event_seq",
        "provider_dispatch_event_sha256",
        "provider_reconciliation_event_seq",
        "provider_reconciliation_event_sha256",
        "work_item_identity",
        "work_item_kind",
        "package_scope_id",
        "ness_choice_exact",
        "recovery_action",
        "ness_action_confirmed",
        "pre_choice_authenticated_event_seq",
        "pre_choice_authenticated_tail_sha256",
        "controller_executable_identity",
        "standing_before_sha256",
    )
)

VERSION9_SUPERVISOR_EVENT_BODY_KEYS = dict(VERSION8_SUPERVISOR_EVENT_BODY_KEYS)
VERSION9_SUPERVISOR_EVENT_BODY_KEYS[NESS_TRANSITION_RECOVERY_CHOICE_EVENT_TYPE] = (
    NESS_TRANSITION_RECOVERY_CHOICE_BODY_KEYS
)

EXTERNAL_ACTION_RESOLUTION_EVENT_TYPE = "external_action_resolution_recorded"
EXTERNAL_ACTION_RESOLUTION_BODY_KEYS = _b(
    PACKAGE_SOURCE,
    (
        "external_action_resolution_identity",
        "resolved_dependency_identity",
        "resolved_dependency_carrier_event_seq",
        "resolved_dependency_carrier_event_sha256",
        "resolved_dependency_code",
        "work_item_identity",
        "failed_provider_request_identity",
        "failed_provider_terminal_event_seq",
        "failed_provider_terminal_event_sha256",
        "resource_identity",
        "user_action_code",
        "external_action_evidence_kind",
        "normal_host_context_confirmed",
        "provider_cli_login_proved",
        "provider_state_writable_proved",
        "bounded_smoke_returncode",
        "bounded_smoke_agent_message",
        "bounded_smoke_turn_completed",
        "ness_action_exact",
        "ness_action_confirmed",
        "pre_action_authenticated_event_seq",
        "pre_action_authenticated_tail_sha256",
        "controller_executable_identity",
    ),
)

VERSION10_SUPERVISOR_EVENT_BODY_KEYS = dict(VERSION9_SUPERVISOR_EVENT_BODY_KEYS)
VERSION10_SUPERVISOR_EVENT_BODY_KEYS[EXTERNAL_ACTION_RESOLUTION_EVENT_TYPE] = (
    EXTERNAL_ACTION_RESOLUTION_BODY_KEYS
)

QUESTION_AUTHORITY_AUDIT_EVENT_TYPE = "question_authority_audit_recorded"
QUESTION_AUTHORITY_AUDIT_BODY_KEYS = _b(
    PACKAGE_SOURCE,
    (
        "scope_root_path",
        "basis_validation_set_id",
        "basis_validated_at_event_seq",
        "basis_coverage_event_seq",
        "basis_group_event_seq",
        "audit_scope",
        "ness_action_confirmed",
        "question_inventory_sha256",
        "question_count",
        "audit_identity",
        "outcomes",
    ),
)

# One standing-neutral, Bundle-Seven-wide source baseline.  It is deliberately
# not package-scoped: its purpose is to record the shared context that must be
# current before any one Bundle Seven package may be classified.  The later
# package validation remains the only question-creating stage.
BUNDLE_SEVEN_BASELINE_EVENT_TYPE = "bundle_seven_baseline_recorded"
BUNDLE_SEVEN_BASELINE_BODY_KEYS = frozenset(
    (
        "bundle_id",
        "baseline_identity",
        "review_schema_version",
        "review_complete",
        "package_inventory",
        "cross_package_relationships",
        "source_paths_checked",
        "source_paths_checked_count",
        "source_manifest_files",
        "source_manifest_sha256",
        "unknowns",
        "branch",
        "head_sha",
        "source_binding_sha256",
        "standing_before_sha256",
    )
)

BUNDLE_SEVEN_QUESTION_MERGE_EVENT_TYPE = "bundle_seven_question_merge_recorded"
BUNDLE_SEVEN_QUESTION_MERGE_BODY_KEYS = frozenset(
    (
        "bundle_id",
        "baseline_identity",
        "package_validation_set_ids",
        "package_feature_keys_checked",
        "merged_question_ids",
        "package_count",
        "feature_count",
        "question_count",
        "branch",
        "head_sha",
        "source_binding_sha256",
        "standing_before_sha256",
    )
)

VERSION11_SUPERVISOR_EVENT_BODY_KEYS = dict(VERSION10_SUPERVISOR_EVENT_BODY_KEYS)
VERSION11_SUPERVISOR_EVENT_BODY_KEYS[QUESTION_AUTHORITY_AUDIT_EVENT_TYPE] = (
    QUESTION_AUTHORITY_AUDIT_BODY_KEYS
)
VERSION11_SUPERVISOR_EVENT_BODY_KEYS[BUNDLE_SEVEN_BASELINE_EVENT_TYPE] = (
    BUNDLE_SEVEN_BASELINE_BODY_KEYS
)
VERSION11_SUPERVISOR_EVENT_BODY_KEYS[BUNDLE_SEVEN_QUESTION_MERGE_EVENT_TYPE] = (
    BUNDLE_SEVEN_QUESTION_MERGE_BODY_KEYS
)

# The version-5 supervisor type NAMES, which the acceptance type is not one of:
# version 5 gains no type and no key.
VERSION5_SUPERVISOR_EVENT_TYPES = frozenset(SUPERVISOR_EVENT_BODY_KEYS)

# The CURRENT supervisor type names.  A type name is
# version-agnostic on purpose: what refuses an acceptance event inside a
# version-5 history is the absence of a (5, type) SCHEMA ROW, not the absence
# of the name from this set.
SUPERVISOR_EVENT_TYPES = frozenset(VERSION11_SUPERVISOR_EVENT_BODY_KEYS)

# Events that carry a DEPENDENCY_SLOT at all.  The acceptance event is not one
# of them: the accepted design gives it no dependency slot, and it does not
# acquire one merely because other supervisor records have one.
EVENT_TYPES_WITH_DEPENDENCY_SLOT = frozenset(
    kind
    for kind, keys in VERSION11_SUPERVISOR_EVENT_BODY_KEYS.items()
    if DEPENDENCY_SLOT <= keys
)

# Section 2 -- events that may never create a feed card.  Section 9.7 puts the
# acceptance event in this set, and it lands there by construction: acceptance
# is displayed only from the replayed workflow state, never as a feed claim.
NON_FEED_SUPERVISOR_EVENT_TYPES = SUPERVISOR_EVENT_TYPES - frozenset(
    (
        "mechanical_audit_recorded",
        "mechanical_change_explanation_recorded",
        "mechanical_pass_recorded",
    )
)


def build_version5_body_keys(version4_body_keys):
    """Return ``{(version, type): frozenset(keys)}`` for versions 4 and 5.

    Version-4 rows are the installed sets, byte for byte.  Version-5 rows are:
    the six non-candidate version-4 types unchanged, the three candidate types
    with ``correction_round`` replaced by the three new keys, and every
    supervisor-era type.
    """
    table = {}
    for kind, keys in version4_body_keys.items():
        table[(4, kind)] = frozenset(keys)

    for kind, keys in version4_body_keys.items():
        if kind in CANDIDATE_EVENT_TYPES:
            upgraded = (frozenset(keys) - {CANDIDATE_EVENT_REMOVED_KEY}) | (
                CANDIDATE_EVENT_ADDED_KEYS
            )
            table[(5, kind)] = upgraded
        else:
            table[(5, kind)] = frozenset(keys)

    for kind, keys in SUPERVISOR_EVENT_BODY_KEYS.items():
        table[(5, kind)] = frozenset(keys)
    return table


def build_version6_body_keys(version4_body_keys):
    """Return ``{(version, type): frozenset(keys)}`` for versions 4, 5 AND 6.

    Version 6 is the FIRST body version that carries the acceptance design.  It
    starts as the exact version-5 table, so a type nobody changed cannot drift,
    and then exactly four rows are laid over it: the three already registered
    types that gain acceptance keys, and the one new acceptance type, which has
    a version-6 row and NO version-5 row.

    Version-4 and version-5 rows are returned exactly as
    ``build_version5_body_keys`` produced them; no stored byte of either is
    rewritten, no row of either is dropped, and no acceptance key is
    retrofitted into either.  A stored version-5 history therefore still
    validates against precisely the schema it was written under, and a
    version-5 event carrying the acceptance type has no schema for its pair and
    fails closed.
    """
    table = build_version5_body_keys(version4_body_keys)
    for (version, kind), keys in list(table.items()):
        if version == 5:
            table[(6, kind)] = keys
    for kind, keys in VERSION6_SUPERVISOR_EVENT_BODY_KEYS.items():
        table[(6, kind)] = keys
    return table


def build_version7_body_keys(version4_body_keys):
    """Return the unchanged version 4-6 rows plus the version-7 inventory."""
    table = build_version6_body_keys(version4_body_keys)
    for (version, kind), keys in list(table.items()):
        if version == 6:
            table[(7, kind)] = keys
    for kind, keys in VERSION7_SUPERVISOR_EVENT_BODY_KEYS.items():
        table[(7, kind)] = keys
    return table


def build_version8_body_keys(version4_body_keys):
    """Return the unchanged version 4-7 rows plus the version-8 inventory."""
    table = build_version7_body_keys(version4_body_keys)
    for (version, kind), keys in list(table.items()):
        if version == 7:
            table[(8, kind)] = keys
    for kind, keys in VERSION8_SUPERVISOR_EVENT_BODY_KEYS.items():
        table[(8, kind)] = keys
    return table


def build_version9_body_keys(version4_body_keys):
    """Return the unchanged version 4-8 rows plus the version-9 inventory."""
    table = build_version8_body_keys(version4_body_keys)
    for (version, kind), keys in list(table.items()):
        if version == 8:
            table[(9, kind)] = keys
    for kind, keys in VERSION9_SUPERVISOR_EVENT_BODY_KEYS.items():
        table[(9, kind)] = keys
    return table


def build_version10_body_keys(version4_body_keys):
    """Return the unchanged version 4-9 rows plus the version-10 inventory."""
    table = build_version9_body_keys(version4_body_keys)
    for (version, kind), keys in list(table.items()):
        if version == 9:
            table[(10, kind)] = keys
    for kind, keys in VERSION10_SUPERVISOR_EVENT_BODY_KEYS.items():
        table[(10, kind)] = keys
    return table


def build_version11_body_keys(version4_body_keys):
    """Return the unchanged version 4-10 rows plus the version-11 inventory."""
    table = build_version10_body_keys(version4_body_keys)
    for (version, kind), keys in list(table.items()):
        if version == 10:
            table[(11, kind)] = keys
    for kind, keys in VERSION11_SUPERVISOR_EVENT_BODY_KEYS.items():
        table[(11, kind)] = keys
    return table


def build_version12_body_keys(version4_body_keys, version12_controller_rows=None):
    """Return unchanged version 4-11 rows plus the version-12 inventory.

    ``version12_controller_rows`` carries controller-owned event types that do
    not belong to the supervisor protocol.  They exist only at version 12;
    copying them into an earlier row would silently retrofit a schema onto
    preserved history.
    """
    table = build_version11_body_keys(version4_body_keys)
    for (version, kind), keys in list(table.items()):
        if version == 11:
            table[(12, kind)] = keys
    for kind, keys in (version12_controller_rows or {}).items():
        table[(12, kind)] = frozenset(keys)
    return table


def version5_event_types(version4_event_types):
    # Version 5 means the version-5 supervisor names, never the current ones:
    # the acceptance type is a version-6 name and was never a version-5 one.
    return frozenset(version4_event_types) | VERSION5_SUPERVISOR_EVENT_TYPES


def dependency_slot_shape(body):
    """Return ``carrier``, ``reference``, ``none`` or ``contradiction``.

    Section 4.2d states exactly three literal shapes; anything else is a schema
    contradiction and fails closed.
    """
    record = body.get("dependency_record")
    identity = body.get("dependency_identity")
    carrier_seq = body.get("dependency_carrier_event_seq")
    ordinal = body.get("dependency_occurrence_ordinal")

    if record is None and identity is None and carrier_seq is None and ordinal is None:
        return "none"
    if (
        isinstance(record, dict)
        and isinstance(identity, str)
        and carrier_seq is None
        and ordinal == 1
    ):
        return "carrier"
    if (
        record is None
        and isinstance(identity, str)
        and isinstance(carrier_seq, int)
        and not isinstance(carrier_seq, bool)
        and isinstance(ordinal, int)
        and not isinstance(ordinal, bool)
        and ordinal >= 2
    ):
        return "reference"
    return "contradiction"


def empty_dependency_slot():
    return {
        "dependency_record": None,
        "dependency_identity": None,
        "dependency_carrier_event_seq": None,
        "dependency_occurrence_ordinal": None,
    }


# ---------------------------------------------------------------------------
# v1_8 section 24.3 -- RESULT-SCHEMA REGISTRATION FOR THE THREE NEW PROVIDER
# KINDS.  Provider-lifecycle schema ids ONLY.
#
# The registration below MUST NOT mutate the installed model-result key sets
# NEXT_PACKAGE_ANALYSIS_REQUIRED_KEYS or PREPARE_TASK_REQUIRED_KEYS, which stay
# exactly as installed (SEL-LIFECYCLE-METADATA-STAYS-OUTSIDE, P-23).  A
# result_schema_id registered for a provider kind is controller-owned lifecycle
# metadata carried on provider_request_prepared; it never becomes a
# model-authored result field for the four specialized contracts.
#
# No event body key set is changed here and NO EVENT TYPE IS ADDED (section
# 7.6).
# ---------------------------------------------------------------------------

# The two read-only review kinds carry the INSTALLED model contracts.  Their
# result_schema_id is lifecycle metadata and is deliberately marked as
# "not a model-authored contract" so nothing downstream can mistake it for one.
LIFECYCLE_ONLY_RESULT_SCHEMA_IDS = frozenset(
    (
        "NH_NEXT_PACKAGE_SELECTION_LIFECYCLE_V1",
        "NH_NEXT_DESIGN_TASK_PREPARATION_LIFECYCLE_V1",
    )
)

# v1_8 section 14.5a -- the candidate contract plus the acceptance explanation
# produced by that same Claude call.  It is NOT CLAUDE_RESULT_KEYS.
INITIAL_DESIGN_RESULT_SCHEMA = {
    "result_schema_id": constants.INITIAL_DESIGN_RESULT_SCHEMA_ID,
    "result_schema_version": 1,
    "required_keys": frozenset(constants.INITIAL_DESIGN_RESULT_KEYS),
}

RESULT_SCHEMA_BY_PROVIDER_KIND = dict(constants.RESULT_SCHEMA_ID_BY_PROVIDER_KIND)

# Asserted rather than assumed.
assert len(constants.INITIAL_DESIGN_RESULT_KEYS) == 7
assert set(constants.INITIAL_DESIGN_RESULT_KEYS) == {
    "result_schema_id",
    "result_schema_version",
    "produced_candidate_path",
    "produced_candidate_sha256",
    "produced_candidate_bytes",
    "produced_candidate_payload_base64",
    "acceptance_explanation_content",
}
# The five correction-specific keys are EXCLUDED and must stay excluded.
assert not (
    set(constants.INITIAL_DESIGN_RESULT_KEYS)
    & {
        "produced_lifetime_round",
        "produced_batch_number",
        "produced_round_in_batch",
        "correction_specification_sha256",
        "blocking_finding_refs",
    }
)
# Every provider kind has exactly one registered lifecycle schema id.
assert set(RESULT_SCHEMA_BY_PROVIDER_KIND) == set(constants.PROVIDER_KINDS)

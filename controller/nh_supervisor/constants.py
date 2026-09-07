#!/usr/bin/env python3
"""Literal controller-owned constants of the v1.13 automatic-supervisor protocol.

Every value here is stated by
``spec/NH_AUTOMATIC_SUPERVISOR_MECHANICAL_CHANGE_SPEC_v1_13_CANDIDATE.md``.
Nothing in this module is derived from a model, a clock, or a caller.  The
module is deliberately data-only: no I/O, no provider contact, no journal
access.
"""

from __future__ import annotations

# --------------------------------------------------------------------------
# Section 3 -- counter semantics.
# --------------------------------------------------------------------------
CORRECTION_BATCH_SIZE = 5

# --------------------------------------------------------------------------
# Section 4.1 -- journal version transition.
#
# Versions 4 through 11 remain readable and their stored bytes are never
# rewritten. New appends use version 12. Version 12 adds one append-only,
# all-or-nothing Ness answer-batch record; earlier version/type pairs are
# unchanged.
# --------------------------------------------------------------------------
INTERVIEW_JOURNAL_CURRENT_VERSION = 12
INTERVIEW_JOURNAL_SUPPORTED_VERSIONS = frozenset((4, 5, 6, 7, 8, 9, 10, 11, 12))

SUPERVISOR_PROTOCOL_VERSION = 1

# --------------------------------------------------------------------------
# Section 11.7 -- private scheduling journal.
# --------------------------------------------------------------------------
SUPERVISOR_SCHEDULING_JOURNAL_VERSION = 6
SUPERVISOR_SCHEDULING_JOURNAL_SUPPORTED_VERSIONS = frozenset((6,))

# --------------------------------------------------------------------------
# Bounded sizes and attempt caps (Sections 4.2, 4.8, 4.9a, 4.9b, 11.2b, 11.7,
# 11.9, 11.9b).
# --------------------------------------------------------------------------
MAX_NORMALIZED_OPERATIONS = 64
MAX_PROPOSED_ADDITION_NAMES = 64
MAX_CAPABILITY_REGISTRY_ENTRIES = 16
MAX_PROVIDER_ERROR_SIGNAL_MAP_ENTRIES = 64
MAX_RETRY_AFTER_SECONDS = 86400

MAX_INLINE_RESULT_BYTES = 65536
MAX_PROVIDER_RESULT_BYTES = 4194304
MAX_PROVIDER_RESULT_READ_LIMIT_BYTES = MAX_PROVIDER_RESULT_BYTES + 1
MAX_CANDIDATE_BYTES = 8 * 1024 * 1024

MAX_PROBE_RESULT_BYTES = 4096
MAX_PROBE_RESULT_READ_LIMIT_BYTES = MAX_PROBE_RESULT_BYTES + 1

MAX_PROVIDER_ATTEMPTS_PER_WORK_ITEM_EPISODE = 5
MAX_PROVIDER_OUTPUT_RETRIES_PER_EPISODE = 2
DIAGNOSIS_ATTEMPTS_PER_TRIGGER = 2
MAX_NO_PROGRESS_ROUNDS_PER_SEMANTIC_SCOPE = 3
MAX_AVAILABILITY_PROBES_PER_CLOSED_EPISODE = 3
MAX_AUTOMATIC_EPISODE_UNLOCKS_PER_WORK_ITEM = 3
MIN_EPISODE_UNLOCK_WAIT_SECONDS = 900

# Section 11.7 backoff.
BACKOFF_BASE_SECONDS = 15
BACKOFF_MAX_SECONDS = 900

# --------------------------------------------------------------------------
# Section 13.3 / 13.5 -- lease.
# --------------------------------------------------------------------------
LEASE_VERSION = 1
LEASE_HEARTBEAT_INTERVAL_SECONDS = 10
LEASE_EXPIRY_SECONDS = 35
LEASE_START_MIN_REMAINING_SECONDS = 20
LEASE_STOP_MARGIN_SECONDS = 5
CLOCK_SKEW_TOLERANCE_SECONDS = 5

LEASE_STATES = ("ABSENT_PROVED", "LIVE_PROVED", "EXPIRED_PROVED", "INVALID_UNPROVED")

# --------------------------------------------------------------------------
# Section 2 -- the eight public workflow states.
# --------------------------------------------------------------------------
# Section 2 -- the eight public workflow states, plus the ninth the accepted
# acceptance design adds.  The first eight are preserved in their exact
# installed order: the ninth is APPENDED, never inserted, so no stored report
# and no existing reader changes meaning.
WORKFLOW_STATES = (
    "IDLE",
    "WORKING",
    "DIAGNOSING",
    "WAITING_RECOVERING",
    "NEEDS_NESS_DECISION",
    "NEEDS_USER_ACTION",
    "SAFETY_HOLD",
    "READY_FOR_ACCEPTANCE",
    # Section 4.5 D4 / Section 17 -- terminal and non-running.  It exists only
    # after Ness explicitly performs the separately authorized acceptance
    # action, and it is projected only from the governed terminal truth of
    # Section 11.1 -- never from raw replay alone.
    "ACCEPTED_FOR_DESIGN_ONLY",
)
WORKFLOW_STATE_SET = frozenset(WORKFLOW_STATES)

# The eight states that existed before the acceptance design, asserted rather
# than assumed, so a later edit that reorders or drops one is caught here.
WORKFLOW_STATES_BEFORE_ACCEPTANCE = WORKFLOW_STATES[:8]
assert WORKFLOW_STATES_BEFORE_ACCEPTANCE == (
    "IDLE",
    "WORKING",
    "DIAGNOSING",
    "WAITING_RECOVERING",
    "NEEDS_NESS_DECISION",
    "NEEDS_USER_ACTION",
    "SAFETY_HOLD",
    "READY_FOR_ACCEPTANCE",
)

# --------------------------------------------------------------------------
# Section 4.4 -- work item kinds, Section 4.6 -- provider kinds.
# --------------------------------------------------------------------------
WORK_ITEM_KINDS = (
    "design_audit",
    "correction_specification",
    "correction_apply",
    "correction_diagnosis",
    "change_explanation_review",
    "question_validation",
    "coverage_review",
    # Section 14 Phase A step A2 -- ONE bounded preparation work item for the
    # acceptance explanation's parts 1-6.  It is a preparation kind and nothing
    # else: it decides no acceptance, records no PASS, produces no candidate
    # byte, and never writes parts 7 or 8.
    "acceptance_explanation_content",
    # v1_8 section 7.6 -- THREE post-acceptance continuation work-item kinds.
    # They are added inside this existing registry; no second registry, no
    # second dispatch table and no new journal event type is created.
    #   next_package_selection        T1 -- ONE bounded read-only selection review
    #   next_design_task_preparation  T3 -- ONE bounded read-only task-preparation review
    #   initial_design                T4 -- ONE bounded Claude initial design run
    "next_package_selection",
    "next_design_task_preparation",
    "initial_design",
)
WORK_ITEM_KIND_SET = frozenset(WORK_ITEM_KINDS)

# v1_8 section 7.6a CLOSURE-READONLY.  These two kinds owe NO downstream effect
# append: their custodied result IS the durable output, so a completed
# result_received terminal together with its custody record is itself the
# closure.  They are never routed through process-custodied-provider-result to
# manufacture an effect that did not happen.
CLOSED_BY_TERMINAL_ONLY_WORK_ITEM_KINDS = frozenset(
    ("next_package_selection", "next_design_task_preparation")
)

# v1_8 section 8.9.2 TB-CUSTODY-CLOSED-SET.  The ONLY work-item kinds a
# transition pending-custody bootstrap may ever discover.  The two read-only
# kinds above are deliberately absent: they are terminal-only closed.
TRANSITION_PENDING_CUSTODY_KINDS = frozenset(
    ("question_validation", "coverage_review", "initial_design")
)

PROVIDER_KINDS = (
    "codex_design_audit",
    "gpt_correction_specification",
    "claude_correction",
    "codex_correction_diagnosis",
    "codex_change_explanation_review",
    "gpt_question_validation",
    "gpt_question_coverage_review",
    # Section 7.8 -- model assistance for parts 1-6 is PREPARATION ONLY.  The
    # accepted design names no provider; Ness settled that Claude prepares the
    # prose and Codex independently audits the exact fixed bytes.
    "claude_acceptance_explanation",
    # v1_8 section 7.6 -- the three continuation provider kinds.
    "codex_next_package_selection",
    "codex_next_design_task_preparation",
    "claude_initial_design",
)
PROVIDER_KIND_SET = frozenset(PROVIDER_KINDS)

# The Section 4.6 bijection, in both directions.
PROVIDER_KIND_BY_WORK_ITEM_KIND = {
    "design_audit": "codex_design_audit",
    "correction_specification": "gpt_correction_specification",
    "correction_apply": "claude_correction",
    "correction_diagnosis": "codex_correction_diagnosis",
    "change_explanation_review": "codex_change_explanation_review",
    "question_validation": "gpt_question_validation",
    "coverage_review": "gpt_question_coverage_review",
    "acceptance_explanation_content": "claude_acceptance_explanation",
    "next_package_selection": "codex_next_package_selection",
    "next_design_task_preparation": "codex_next_design_task_preparation",
    "initial_design": "claude_initial_design",
}
WORK_ITEM_KIND_BY_PROVIDER_KIND = {
    value: key for key, value in PROVIDER_KIND_BY_WORK_ITEM_KIND.items()
}

RESULT_SCHEMA_ID_BY_PROVIDER_KIND = {
    # The audit now carries the complete correction specification whenever it
    # reports mechanical blockers.  The new lifecycle id keeps old custodied
    # V1 results unambiguous while preventing a second specification request.
    "codex_design_audit": "NH_DESIGN_AUDIT_RESULT_V2",
    "gpt_correction_specification": "NH_CORRECTION_SPECIFICATION_RESULT_V1",
    # Candidate-producing Claude calls now also carry parts 1-6 of the bound
    # acceptance explanation.  The controller binds those words to the exact
    # bytes it reads back from the disposable workspace.
    "claude_correction": "NH_CLAUDE_CORRECTION_RESULT_V2",
    "codex_correction_diagnosis": "NH_CORRECTION_DIAGNOSIS_RESULT_V1",
    "codex_change_explanation_review": "NH_CHANGE_EXPLANATION_RESULT_V1",
    "gpt_question_validation": "NH_QUESTION_VALIDATION_RESULT_V1",
    "gpt_question_coverage_review": "NH_QUESTION_COVERAGE_RESULT_V1",
    "claude_acceptance_explanation": "NH_ACCEPTANCE_EXPLANATION_CONTENT_RESULT_V1",
    # v1_8 sections 9.5a / 13.6a SEL-LIFECYCLE-METADATA-STAYS-OUTSIDE.  These
    # two ids are CONTROLLER-OWNED LIFECYCLE METADATA carried on
    # provider_request_prepared.  They are never injected into the installed
    # exact-key model contracts NEXT_PACKAGE_ANALYSIS_REQUIRED_KEYS or
    # PREPARE_TASK_REQUIRED_KEYS, whose validators refuse an extra key.
    "codex_next_package_selection": "NH_NEXT_PACKAGE_SELECTION_LIFECYCLE_V1",
    "codex_next_design_task_preparation": "NH_NEXT_DESIGN_TASK_PREPARATION_LIFECYCLE_V1",
    # v1_8 section 14.5a -- this one IS the model-authored contract's own id.
    "claude_initial_design": "NH_CLAUDE_INITIAL_DESIGN_RESULT_V2",
}
RESULT_SCHEMA_VERSION = 1

# v1_8 section 14.5a INIT-RESULT-KEYS -- the candidate fields plus the bound
# acceptance-explanation parts produced in the same call.  Deliberately NOT
# CLAUDE_RESULT_KEYS: the five correction-specific
# keys (produced_lifetime_round, produced_batch_number, produced_round_in_batch,
# correction_specification_sha256, blocking_finding_refs) have no truthful
# meaning for an initial design and are excluded.
INITIAL_DESIGN_RESULT_KEYS = (
    "result_schema_id",
    "result_schema_version",
    "produced_candidate_path",
    "produced_candidate_sha256",
    "produced_candidate_bytes",
    "produced_candidate_payload_base64",
    "acceptance_explanation_content",
)
INITIAL_DESIGN_RESULT_SCHEMA_ID = "NH_CLAUDE_INITIAL_DESIGN_RESULT_V2"

# --------------------------------------------------------------------------
# Accepted role-split v1_6 -- the PROVIDER-FREE LOCAL T3 constants.
#
# v1_6 section 5.3 fixes ONE canonical controller object under ONE version tag,
# whose top-level key set is EXACTLY these twelve keys, no more and no fewer.
# The tuple lives here ONCE so no call site can re-spell it, and every builder
# and every checker measures against this one declaration.
# --------------------------------------------------------------------------
LOCAL_T3_ENVELOPE_SCHEMA_ID = "NH_LOCAL_T3_TASK_ENVELOPE_V1"
LOCAL_T3_ENVELOPE_KEYS = (
    "envelope_version",
    "package",
    "package_root_identity",
    "authority_required_files_sha256",
    "source_currentness",
    "relevant_source_closure",
    "required_source_paths",
    "question_clearance",
    "settled_decision_binding_sha256",
    "unsatisfied_dependency_keys",
    "target",
    "work_boundary",
)
assert len(LOCAL_T3_ENVELOPE_KEYS) == 12
assert len(set(LOCAL_T3_ENVELOPE_KEYS)) == 12

# The exact fixed key sets of the four object-valued envelope fields.
LOCAL_T3_ENVELOPE_PACKAGE_KEYS = (
    "package_key",
    "package_id",
    "package_scope_id",
    "scope_root_path",
    "package_binding_sha256",
)
LOCAL_T3_ENVELOPE_SOURCE_CURRENTNESS_KEYS = (
    "anchor_source_binding_sha256",
    "effective_validation_set_id",
    "effective_source_manifest_sha256",
    "effective_source_binding_sha256",
    "source_state_current",
)
LOCAL_T3_ENVELOPE_RELEVANT_CLOSURE_KEYS = ("closure_sha256", "paths")
LOCAL_T3_ENVELOPE_QUESTION_CLEARANCE_KEYS = (
    "unlocked",
    "validation_set_id",
    "coverage_review_validation_set_id",
    "coverage_review_current",
    "standing_chain_sha256",
)
LOCAL_T3_ENVELOPE_TARGET_KEYS = ("target_path", "target_rule_id")
LOCAL_T3_ENVELOPE_WORK_BOUNDARY_KEYS = (
    "one_file_only",
    "design_only",
    "build_vs_borrow_required",
)

# v1_6 section 5.5 -- the fixed controller-owned first-target rule id.  It is a
# VALUE the envelope binds, never a second naming subsystem.
LOCAL_T3_INITIAL_TARGET_RULE_ID = "NH_LOCAL_T3_INITIAL_TARGET_V1"

# v1_6 section 5.4 -- the ONE narrow compatibility binding that replaces the
# provider-produced specification digest in T4's stage `extra_inputs`.
LOCAL_TASK_ENVELOPE_DIGEST_KEY = "local_task_envelope_sha256"
# v1_6 section 5.4b -- the ONE prompt-material key that replaces the removed
# model-authored `mechanical_design_specification`.
LOCAL_TASK_ENVELOPE_PROMPT_KEY = "local_task_envelope"

# v1_6 sections 5.4b.4 -- the two keys NO NEW local-T3 operation may read,
# require, default, or fabricate.  They remain fully readable for HISTORICAL
# records, which is why they are named here rather than deleted.
OBSOLETE_SPECIFICATION_INPUT_KEYS = (
    "prepared_specification_sha256",
    "mechanical_design_specification",
)

# v1_6 section 5.4a B -- T4's stage `extra_inputs`, EXACTLY three keys.
INITIAL_DESIGN_EXTRA_INPUT_KEYS = (
    "prepared_target_path",
    LOCAL_TASK_ENVELOPE_DIGEST_KEY,
    "frozen_source_binding_sha256",
)
# v1_6 section 5.4b T4-PROMPT-ENVELOPE -- T4's prompt `extra`, EXACTLY three keys.
INITIAL_DESIGN_EXTRA_PROMPT_KEYS = (
    "specialized_prompt_kind",
    "prepared_target_path",
    LOCAL_TASK_ENVELOPE_PROMPT_KEY,
)
assert len(INITIAL_DESIGN_EXTRA_INPUT_KEYS) == 3
assert len(INITIAL_DESIGN_EXTRA_PROMPT_KEYS) == 3
# NO-NEW-PATH-ON-OLD-SPECIFICATION, asserted rather than assumed.
assert not (set(INITIAL_DESIGN_EXTRA_INPUT_KEYS)
            & set(OBSOLETE_SPECIFICATION_INPUT_KEYS))
assert not (set(INITIAL_DESIGN_EXTRA_PROMPT_KEYS)
            & set(OBSOLETE_SPECIFICATION_INPUT_KEYS))

# v1_6 section 6.4 -- the SECOND, DISJOINT initial-design result shape.  It is a
# LOCAL result contract, held to the same exactness as INITIAL_DESIGN_RESULT_KEYS.
# It creates NO provider kind, NO lifecycle row and NO journal event type.
INITIAL_DESIGN_STOP_RESULT_KEYS = (
    "result_schema_id",
    "result_schema_version",
    "stop_review_signal",
)
INITIAL_DESIGN_STOP_RESULT_SCHEMA_ID = "NH_LOCAL_INITIAL_DESIGN_STOP_RESULT_V1"
INITIAL_DESIGN_STOP_RESULT_VERSION = 1
# The existing five-key review-signal object the STOP arm carries, named once so
# the read side and the write side cannot drift.  validate_review_signal() in
# nh_loop remains the ONE validator; this is not a second contract.
REVIEW_SIGNAL_KEYS = (
    "issue_key",
    "finding_key",
    "signal_title",
    "finding_evidence",
    "source_evidence",
)
# The two arms are MUTUALLY EXCLUSIVE and disjoint apart from the two lifecycle
# keys.  Asserted rather than assumed (v1_6 section 6.4).
assert (
    set(INITIAL_DESIGN_RESULT_KEYS) & set(INITIAL_DESIGN_STOP_RESULT_KEYS)
    == {"result_schema_id", "result_schema_version"}
)
assert INITIAL_DESIGN_STOP_RESULT_SCHEMA_ID != INITIAL_DESIGN_RESULT_SCHEMA_ID

# v1_6 section 6.5 -- the existing carrier and signal source a custodied STOP
# closes through.  Neither is new: the source string is the one nh_loop's
# REVIEW_SIGNAL_SOURCE_CLAUDE_STOP already carries.
STOP_REVIEW_SIGNAL_SOURCE = "claude_specification_stop_review"
STOP_CLOSURE_CARRIER_EVENT_TYPE = "review_signal_recorded"

# --------------------------------------------------------------------------
# Section 11.2 -- provider phases and terminal kinds.
# --------------------------------------------------------------------------
PROVIDER_PHASES = (
    "none",
    "prepared",
    "dispatch_begun",
    "accepted",
    "result_custodied",
    "terminal",
)
PROVIDER_PHASE_ORDER = {name: index for index, name in enumerate(PROVIDER_PHASES)}

TERMINAL_KINDS = (
    "result_received",
    "result_invalid",
    "result_oversize_uncustodied",
    "provider_error_retryable",
    "provider_error_terminal",
    "abandoned_absent_proved",
)
TERMINAL_KIND_SET = frozenset(TERMINAL_KINDS)

TERMINAL_EVIDENCE_KINDS = (
    "local_completion",
    "local_process_completion_diagnostics",
    "authoritative_lookup_retrieval",
    "local_classified_error",
    "local_bounded_read_limit_exceeded",
    "authoritative_absence_proof",
)

ACCEPTANCE_AUTHORITIES = ("none", "provider_request_ref", "idempotency_echo")

# Section 4.2b -- written reconciliation outcomes.
RECONCILIATION_OUTCOMES = (
    "absent_proved",
    "found_in_progress",
    "found_terminal",
    "found_terminal_result_oversize",
    "found_terminal_result_unavailable",
    "lookup_transiently_failed",
    "lookup_unsupported",
)
RECONCILIATION_OUTCOME_SET = frozenset(RECONCILIATION_OUTCOMES)

# Section 11.4 -- the read-only projection enum adds two derived values that are
# never written as reconciliation_outcome.
PROVIDER_RECONCILIATION_PROJECTION = RECONCILIATION_OUTCOMES + (
    "not_required",
    "contradiction",
)

# Section 11.2a -- provider result custody projection.
PROVIDER_RESULT_CUSTODY_STATES = (
    "not_required",
    "absent",
    "custodied_valid",
    "custodied_invalid",
    "oversize_not_custodied",
    "unverifiable",
    "contradiction",
)

RESULT_ORIGINS = ("local_completion", "authoritative_lookup_retrieval")
RESULT_LOCATION_KINDS = ("inline_journal_bytes", "anchored_result_object")

OVERSIZE_DETECTION_KINDS = ("declared_length_over_bound", "stream_exceeded_read_limit")

# Section 11.4 -- recovery outcomes.
RECOVERY_OUTCOMES = (
    "COMPLETED",
    "SAFE_TO_RESUME",
    "SAFE_TO_RETRY",
    "WAIT",
    "NEEDS_USER_ACTION",
    "SAFETY_HOLD",
)
RECOVERY_OUTCOME_SET = frozenset(RECOVERY_OUTCOMES)

# Section 11.1 -- operation outcomes.
OPERATION_OUTCOMES = (
    "ok",
    "dependency",
    "safety_hold",
    "needs_ness",
    "needs_user_action",
    "ready_for_acceptance",
)
OPERATION_OUTCOME_SET = frozenset(OPERATION_OUTCOMES)

# Section 11.4 -- candidate reconciliation projection.
CANDIDATE_RECONCILIATION_STATES = (
    "none",
    "pending_child_absent",
    "pending_child_exact",
    "custody_committed",
    "contradiction",
)

# Section 9.3 -- consumption reconciliation.
CONSUMPTION_RECONCILIATION_STATES = (
    "none",
    "open_awaiting_provider_reconciliation",
    "open_awaiting_result_processing",
    "open_awaiting_bounded_retry",
    "open_awaiting_provider_episode_unlock",
    "open_requires_closure",
    "closed_completed",
    "closed_terminated",
    "closed_no_progress",
    "contradiction",
)

CONSUMPTION_AUTHORITY_KINDS = ("diagnosis_strategy", "ordinary_specification")
TERMINATION_KINDS = (
    "provider_failure_known",
    "specification_stop_validated",
    "safety_termination",
)

# Section 7.6 -- diagnosis trigger state.
DIAGNOSIS_TRIGGER_STATES = (
    "none",
    "open",
    "consumed",
    "closed_no_safe_strategy",
    "closed_validation_failed",
    "closed_safety_hold",
    "closed_scope_exhausted",
    "contradiction",
)

DIAGNOSIS_TRIGGER_TYPES = ("exhausted_batch", "no_progress")

DIAGNOSIS_OUTCOMES = (
    "safe_new_mechanical_strategy",
    "possible_ness_choice",
    "temporary_technical_dependency",
    "external_user_action_required",
    "authority_or_safety_conflict",
    "no_currently_safe_strategy",
)

# Section 7.5 -- validation failure classes.
VALIDATION_FAILURE_CLASSES = (
    "result_schema_invalid",
    "result_oversize_uncustodied",
    "result_semantically_invalid",
    "authority_or_safety_contradiction",
)

DIAGNOSIS_REJECTION_CODES = ("novelty_key_already_exhausted",)

# Section 5.1 -- audit usability.
AUDIT_USABILITY_FAILURE_CLASSES = (
    "audit_binding_mismatch",
    "audit_verdict_inconsistent",
    "audit_findings_incomplete",
    "audit_finding_refs_inconsistent",
    "audit_source_reference_invalid",
    "audit_authority_overreach",
)
DESIGN_AUDIT_RESULT_USABILITY_STATES = (
    "none",
    "usable_proved",
    "unusable_recorded",
    "contradiction",
)

# Section 9.8 -- Piece-3 provider authorization projection.
PIECE3_PROVIDER_AUTHORIZATIONS = (
    "none",
    "authorized_validation_pending",
    "authorized_coverage_pending",
    "consumed",
    "contradiction",
)

# Section 11.2b -- availability probe.
PROBE_OUTCOMES = (
    "not_attempted",
    "succeeded",
    "failed",
    "unsupported",
    "unknown_after_interruption",
    "facts_unclassifiable",
)
AVAILABILITY_PROBE_STATES = (
    "none",
    "idle",
    "probe_begun_unknown",
    "succeeded",
    "failed",
    "unsupported",
    "unknown_after_interruption",
    "facts_unclassifiable",
    "bound_reached",
    "contradiction",
)

# Section 4.11c -- scope exhaustion trigger kinds.
SCOPE_EXHAUSTION_TRIGGER_KINDS = (
    "diagnosis_attempts_exhausted_no_new_strategy",
    "semantic_no_progress_bound_reached",
)

# Section 4.11 -- semantic unlock evidence kinds and selection rule ids.
SEMANTIC_UNLOCK_EVIDENCE_KINDS = (
    "accepted_ness_decision_record",
    "authenticated_capability_record_updated",
)
# D-2: fixed literal precedence, accepted Ness record FIRST.
SEMANTIC_UNLOCK_KIND_PRECEDENCE = (
    "accepted_ness_decision_record",
    "authenticated_capability_record_updated",
)
UNLOCK_SELECTION_RULE_IDS = {
    "authenticated_capability_record_updated": "NH_CAPABILITY_BASELINE_SELECTION_V1",
    "accepted_ness_decision_record": "NH_ACCEPTED_NESS_RECORD_V1",
}

# Section 11.9b -- episode unlock evidence kinds.
EPISODE_UNLOCK_EVIDENCE_KINDS = (
    "controller_probe_success",
    "authenticated_capability_record_updated",
    "accepted_ness_unlock_record",
)
UNLOCK_INVOCATION_KINDS = ("automatic_controller_evidence", "person_invoked")

# Section 11.9 -- person route reasons, in the fixed precedence order.
PERSON_ROUTE_REASONS = (
    "probe_capability_absent",
    "automatic_unlock_bound_reached",
    "provider_account_condition",
    "provider_credential_condition",
    "provider_quota_condition",
    "provider_non_transient_condition",
    "external_action_condition",
    "authority_or_safety_condition",
)

# --------------------------------------------------------------------------
# Section 4.5 / 11.8a -- dependency vocabulary.
# --------------------------------------------------------------------------
DEPENDENCY_RECORD_VERSION = 1

DEPENDENCY_CLASSES = (
    "temporary_provider_failure",
    "provider_outcome_unknown",
    "temporary_local_resource_failure",
    "temporary_source_access_failure",
    "external_user_action_required",
    "authority_or_safety_conflict",
    "no_currently_safe_strategy",
)

DEPENDENCY_IDENTITY_BINDINGS = (
    "work_item_bound",
    "episode_bound",
    "provider_request_bound",
)

RESOURCE_KINDS = (
    "provider_endpoint",
    "local_tool",
    "local_path",
    "source_repository",
    "interview_journal",
    "external_account",
    "capability_registry",
)

MODEL_ADMISSIBLE_RESOURCE_KINDS = frozenset(
    (
        "local_tool",
        "local_path",
        "source_repository",
        "interview_journal",
        "capability_registry",
    )
)

RETRY_MODES = (
    "automatic_backoff",
    "automatic_lookup_only",
    "automatic_bounded_output_retry",
    "automatic_probe_only",
    "no_automatic_retry_until_unlock_proved",
    "no_retry_fail_closed",
)

UNLOCK_PREDICATE_KINDS = (
    "time_and_probe_success",
    "authoritative_lookup_result_obtained",
    "named_external_action_observed",
    "source_binding_restored",
    "authenticated_capability_record_updated",
    "new_ness_decision_or_source_change",
    "manual_safety_review",
    "bounded_output_retry_budget_available",
    "provider_availability_unlock_proved",
)

UNLOCK_PREDICATE_PARAM_KEYS = frozenset(
    (
        "resource_identity",
        "provider_request_identity",
        "provider_availability_episode_identity",
        "availability_probe_identity",
        "work_item_identity",
        "package_scope_id",
        "source_binding_sha256",
        "candidate_sha256",
        "blocking_finding_refs",
        "semantic_scope_key",
        "semantic_unlock_generation",
        "scope_exhaustion_identity",
        "user_action_code",
        "retry_budget_remaining",
        "probe_budget_remaining",
        "evidence_event_seq",
    )
)

USER_ACTION_CODES = (
    "provider_account_unavailable",
    "provider_credential_expired",
    "provider_quota_exhausted",
    "provider_non_transient_error_proved",
    "provider_local_process_failure_review_required",
    "provider_outcome_confirmation_required",
    "provider_result_retrieval_required",
    "provider_repeatedly_unavailable",
    "external_dependency_absent",
)

# Section 11.8 -- the twelve controller-derived phase evidence conditions.
PHASE_EVIDENCE_CONDITIONS = (
    "dispatch_proved_never_begun",
    "in_flight_unknown_lookup_authoritative",
    "in_flight_unknown_lookup_best_effort",
    "in_flight_unknown_lookup_unsupported",
    "terminal_retryable_recorded",
    "terminal_non_transient_recorded",
    "terminal_result_invalid_recorded",
    "terminal_result_oversize_recorded",
    "terminal_result_received_recorded",
    "terminal_absent_proved_recorded",
    "provider_episode_scoped_no_open_request",
    "not_provider_scoped",
)

IN_FLIGHT_UNKNOWN_CONDITIONS = frozenset(
    (
        "in_flight_unknown_lookup_authoritative",
        "in_flight_unknown_lookup_best_effort",
        "in_flight_unknown_lookup_unsupported",
    )
)

# Section 11.8b -- the thirteen non-provider-scoped model symptom codes.
MODEL_SYMPTOM_CODES = (
    "local_tool_missing",
    "local_tool_failed",
    "local_path_unwritable",
    "local_lock_contended",
    "source_unreadable",
    "source_binding_unverifiable",
    "source_changed",
    "journal_contradiction",
    "authority_conflict",
    "capability_record_absent",
    "no_new_operation_set",
    "capability_change_required",
    "external_dependency_absent",
)
MODEL_SYMPTOM_CODE_SET = frozenset(MODEL_SYMPTOM_CODES)

# Codes v1.2 admitted from a model observation and v1.3+ refuses (V22).
FORBIDDEN_MODEL_SYMPTOM_CODES = frozenset(
    (
        "provider_unreachable",
        "provider_rate_limited",
        "provider_timeout",
        "provider_result_unparseable",
        "provider_account_unavailable",
        "provider_quota_exhausted",
        "provider_credential_expired",
    )
)

BOUNDED_OUTPUT_RETRY_BUDGET_VALUES = ("available", "exhausted", "not_applicable")

# Section 4.5 -- controlled local registries.
CONTROLLER_LOCAL_TOOL_IDS = (
    "git",
    "python3",
    "diff_tool",
    "hash_tool",
    "filesystem_lock",
)
CONTROLLER_ANCHORED_PATH_IDS = (
    "workspace_root",
    "state_dir",
    "scheduling_journal",
    "lease_file",
    "candidate_dir",
    "provider_result_store",
)

# --------------------------------------------------------------------------
# Section 11.3 -- provider capability contract.
# --------------------------------------------------------------------------
CAPABILITY_RECORD_VERSION = 1
LOOKUP_AUTHORITIES = ("none", "best_effort", "authoritative")
CAPABILITY_SOURCES = (
    "none",
    "accepted_ness_record",
    "controller_local_probe_of_documented_interface",
)
SIGNAL_MATCH_KINDS = ("http_status", "endpoint_error_code_digest")

PROVIDER_ERROR_SIGNAL_V1 = (
    "none_observed",
    "authentication_rejected",
    "authorization_revoked",
    "account_disabled",
    "payment_or_plan_required",
    "quota_exhausted",
    "rate_limited",
    "service_overloaded",
    "service_unavailable",
    "request_too_large",
    "request_rejected_invalid",
    "model_or_endpoint_absent",
    "internal_provider_error",
)
PROVIDER_ERROR_SIGNAL_SET = frozenset(PROVIDER_ERROR_SIGNAL_V1)

PROVIDER_ERROR_SIGNAL_DEFAULTS_V1 = {
    400: "request_rejected_invalid",
    401: "authentication_rejected",
    402: "payment_or_plan_required",
    403: "authorization_revoked",
    404: "model_or_endpoint_absent",
    405: "request_rejected_invalid",
    408: "service_overloaded",
    409: "request_rejected_invalid",
    413: "request_too_large",
    422: "request_rejected_invalid",
    429: "rate_limited",
    500: "internal_provider_error",
    501: "model_or_endpoint_absent",
    502: "service_unavailable",
    503: "service_unavailable",
    504: "service_unavailable",
    529: "service_overloaded",
}

PROBE_SIGNAL_V1 = (
    "available",
    "unavailable",
    "unauthorized",
    "quota_exhausted",
    "probe_unsupported_by_endpoint",
)
PROBE_SIGNAL_SET = frozenset(PROBE_SIGNAL_V1)

PROBE_SIGNAL_CLASS_V1 = {
    "available": "reachable_available",
    "unavailable": "answered_unavailable",
    "unauthorized": "answered_not_recovery",
    "quota_exhausted": "answered_not_recovery",
    "probe_unsupported_by_endpoint": "unsupported_by_endpoint",
}

PROBE_SIGNAL_HTTP_DEFAULTS_V1 = {
    401: "unauthorized",
    402: "unauthorized",
    403: "unauthorized",
    404: "probe_unsupported_by_endpoint",
    405: "probe_unsupported_by_endpoint",
    408: "unavailable",
    429: "unavailable",
    500: "unavailable",
    501: "probe_unsupported_by_endpoint",
    502: "unavailable",
    503: "unavailable",
    504: "unavailable",
    529: "unavailable",
}


def probe_signal_http_default(status):
    """The fixed table, including its 200..299 -> available range."""
    if status is None:
        return None
    if 200 <= status <= 299:
        return "available"
    return PROBE_SIGNAL_HTTP_DEFAULTS_V1.get(status)


PROBE_SIGNAL_SOURCE_NAMES = (
    "endpoint_map_error_code",
    "endpoint_map_http_status",
    "fixed_http_default",
)

PROBE_SIGNAL_CROSS_CHECKS = ("no_source", "single_source", "agreed", "disagreed")

TRANSPORT_KINDS = ("in_process_https", "subprocess_cli")
TRANSPORT_OUTCOMES = (
    "completed",
    "connect_failed",
    "tls_failed",
    "timed_out",
    "process_spawn_failed",
    "process_killed",
    "local_process_failed",
    "stream_closed_early",
    "read_limit_exceeded",
)

# Section 11.2c -- transports that can prove no request byte left the controller.
TRANSMISSION_ABSENT_OUTCOMES = frozenset(
    ("connect_failed", "tls_failed", "process_spawn_failed")
)

# --------------------------------------------------------------------------
# Section 15 -- unresolved package facts. These are literal and never derived.
# --------------------------------------------------------------------------
BUNDLE_PLACEMENT = "UNRESOLVED"
BUNDLE_PLACEMENT_DISPLAY = "Not decided yet"
CONTROLLED_COMPONENT_ID = None
REGISTER_ID = None

# --------------------------------------------------------------------------
# Section 4.3 -- identity prefixes.
# --------------------------------------------------------------------------
IDENTITY_PREFIXES = {
    "supervisor_operation_id": "op_",
    "work_item_identity": "wi_",
    "provider_availability_episode_identity": "ep_",
    "provider_request_identity": "pr_",
    "availability_probe_identity": "ap_",
    "result_custody_identity": "rc_",
    "dependency_identity": "dep_",
    "strategy_novelty_key": "nov_",
    "canonical_addition_slot_id": "slot_",
    "retry_series_key": "rs_",
    "semantic_scope_key": "sc_",
    "scope_exhaustion_identity": "sx_",
    "ness_acceptance_identity": "acc_",
}

# --------------------------------------------------------------------------
# Section 2 -- controller-confirmed change feed.
# --------------------------------------------------------------------------
FEED_ITEM_KINDS = ("problem_found", "candidate_changed", "audit_passed")
FEED_ITEM_KEYS = (
    "controller_authenticated",
    "recorded_at",
    "id",
    "kind",
    "title",
    "what",
    "why",
    "status",
    "technical",
)

# Section 12 -- the fixed controller-owned fallback card.
FALLBACK_CHANGE_CARD = {
    "title": "A mechanical correction candidate was preserved",
    "what": (
        "N.H preserved a new correction candidate. A safe plain-language "
        "explanation is not currently available."
    ),
    "why": (
        "The exact parent, candidate, and technical difference are available "
        "below. No claim is made that the correction succeeded or that meaning "
        "or policy stayed unchanged."
    ),
    "status": "Waiting for or reporting the independent audit result",
}

# --------------------------------------------------------------------------
# Section 9.4 -- controlled replay boundary ids.
# --------------------------------------------------------------------------
REPLAY_BOUNDARY_IDS = (
    "B0",
    "B1",
    "B2",
    "B3",
    "B3a",
    "B3b",
    "B3c",
    "B3d",
    "B3e",
    "B3f",
    "B3g",
    "B4",
    "B5",
    "B5a",
    "B6",
    "B6a",
    "B6b",
    "B6c",
    "B6d",
    "B6e",
    "B6f",
    "B6g",
    "B6h",
    "B6i",
    "B6j",
    "B7",
    "B8",
    "B9",
    "B10",
    "B11",
    "B12",
    "B13",
    "B13a",
    "B13b",
    "B13c",
    "B13d",
    "B13e",
    "B14",
)

CUSTODY_NEXT_STEPS = ("B6d", "B6e", "B6f", "B6g", "B6h", "B6i", "B6j")

# --------------------------------------------------------------------------
# THE ACCEPTED ACCEPTANCE DESIGN (v1_14) -- the locked meaning of one press.
#
# Everything below is controller-owned.  None of it is model prose, none of it
# is generated per candidate, and none of it is paraphrased at render time.
# The browser renders exactly these bytes and echoes exactly this digest; the
# controller re-proves both under the lock before it appends anything.
# --------------------------------------------------------------------------

# Section 9.3 -- the fixed value the acceptance record carries, and the state
# the projection reaches.  The two are deliberately the same string: the record
# says what it accepted FOR, and the projection says what the package now IS.
ACCEPTED_FOR_DESIGN_ONLY = "ACCEPTED_FOR_DESIGN_ONLY"
ACCEPTANCE_DISPOSITION = "ACCEPTED_FOR_DESIGN_ONLY"
ACCEPTANCE_ACTION_CHANNEL = "local_browser_post"
ACCEPTANCE_REVALIDATION_OUTCOME = "all_gates_reproved_under_the_lock"

# Section 5.1 -- the single sentence.  This is the entire meaning of the act.
ACCEPTANCE_SCOPE_ID = "NH_ACCEPTANCE_SCOPE_DESIGN_ONLY_V1"
ACCEPTANCE_SCOPE_SENTENCE = "Accept this exact candidate for design-only status."

# The fixed meaning shown to Ness, verbatim.  It is one paragraph because a
# person reads a paragraph, and it is a constant because a meaning that can be
# reworded per candidate is not a fixed meaning.
ACCEPTANCE_FIXED_MEANING = (
    "Accept this exact candidate for design-only status. This records Ness\u2019s "
    "acceptance only. It does not adopt, integrate, implement, authorize "
    "implementation, mark PACKAGE_COMPLETE, close dependencies, invoke a "
    "provider, or perform Git actions."
)

# Section 5.2 -- the twelve fixed non-authorizations, in their stated order.
ACCEPTANCE_NON_AUTHORIZATIONS = (
    "adopt anything into NH_MASTER-20_CORRECTED_v10.md",
    "adopt or integrate anything into the Design and Wiring Map",
    "implement, code, build, or authorize implementation, coding, or building",
    "mark anything PACKAGE_COMPLETE",
    "close any open dependency, open question, or open item",
    "call any model or provider, of any kind, at any point in the request",
    "perform any Git operation -- no add, commit, push, merge, reset, "
    "checkout, clean, rebase, fetch, or remote change",
    "touch production N.H, any production store, any marker, or any live N.H "
    "disk state",
    "start, unlock, schedule, or authorize the next package",
    "generate, write, copy, move, rename, promote, or project any Markdown "
    "file -- including a closure record or acceptance receipt",
    "assign a controlled component ID, a Register ID, or a bundle placement",
    "change the accepted candidate's bytes in any way",
)
assert len(ACCEPTANCE_NON_AUTHORIZATIONS) == 12

# Section 6.2 part 8 -- the exact bytes the explanation's eighth part carries
# and the browser displays.  Built once, from the two constants above, so the
# sentence a person reads and the digest the controller proves cannot drift.
ACCEPTANCE_SCOPE_TEXT = (
    ACCEPTANCE_FIXED_MEANING
    + "\n\nPressing Accept does NOT:\n"
    + "\n".join(
        "%d. %s;" % (index, text)
        for index, text in enumerate(ACCEPTANCE_NON_AUTHORIZATIONS, start=1)
    )
)

# Section 8.1 -- derived by the one existing method, and no other.  The import
# is deferred because canonical.py imports this module; a function-level import
# keeps one derivation without creating a cycle.
ACCEPTANCE_SCOPE_DOMAIN = "NH_ACCEPTANCE_SCOPE_V1"


def acceptance_scope_digest():
    """``SHA256(canonical_json([DOMAIN, OBJECT]))`` over the fixed scope text."""
    from .canonical import digest_of

    return digest_of(
        ACCEPTANCE_SCOPE_DOMAIN,
        {
            "acceptance_scope_id": ACCEPTANCE_SCOPE_ID,
            "acceptance_scope_sentence": ACCEPTANCE_SCOPE_SENTENCE,
            "acceptance_scope_text": ACCEPTANCE_SCOPE_TEXT,
        },
    )


# Section 6.2 -- the eight fixed parts, in order, with the fixed titles.  The
# schema carries them as a set because a body key set is a set; a person reads
# them in an order, so the order lives here and in exactly one place.
EXPLANATION_PART_TITLES = (
    ("explanation_part_1_what_this_package_does", "WHAT THIS PACKAGE DOES"),
    ("explanation_part_2_what_actually_changed", "WHAT ACTUALLY CHANGED"),
    (
        "explanation_part_3_what_changed_from_previous_candidate",
        "WHAT CHANGED FROM PREVIOUS CANDIDATE",
    ),
    (
        "explanation_part_4_what_this_changes_for_nh_in_real_use",
        "WHAT THIS CHANGES FOR N.H IN REAL USE",
    ),
    ("explanation_part_5_what_did_not_change", "WHAT DID NOT CHANGE"),
    ("explanation_part_6_what_is_still_open", "WHAT IS STILL OPEN"),
    ("explanation_part_7_audit_result", "AUDIT RESULT"),
    (
        "explanation_part_8_what_clicking_accept_means",
        "WHAT CLICKING ACCEPT MEANS",
    ),
)
EXPLANATION_PART_KEYS = tuple(key for key, _title in EXPLANATION_PART_TITLES)
# Parts 1-6 are the semantically variable prose the one independent audit
# judges.  Part 7 is derived from that audit's own record and part 8 is the
# constant above, so neither is authored and neither enters the content digest.
EXPLANATION_CONTENT_PART_KEYS = EXPLANATION_PART_KEYS[:6]
EXPLANATION_DERIVED_PART_KEY = EXPLANATION_PART_KEYS[6]
EXPLANATION_SCOPE_PART_KEY = EXPLANATION_PART_KEYS[7]

# Section 7.4 -- the two acceptance stages of the shared carrier.
EXPLANATION_STAGE_CONTENT = "content_fixed"
EXPLANATION_STAGE_FINAL = "acceptance_offer"

# Section 7.6 -- an honest absence is a recorded value, never a silence.
PREDECESSOR_STATE_STATED = "stated"
PREDECESSOR_STATE_NONE = "none_stated"

# Section 7.4 / 7.8 -- how the prose was produced, stated honestly on the
# record itself.  ``model_assisted_controller_validated`` is the only honest
# value for prose a model drafted: the model carries NO authority, the
# controller validated the structure and the binding, and the one independent
# audit judged the accuracy against these exact fixed bytes.
PREPARATION_KIND_CONTROLLER = "controller_composed"
PREPARATION_KIND_MODEL_ASSISTED = "model_assisted_controller_validated"

# Section 14 Phase A step A2 -- the exact result contract of the one bounded
# preparation invocation.  Exact means exact: a missing key and an extra key
# are both refused, so nothing the controller did not ask for can arrive and
# nothing it needs can be silently absent.  Parts 7 and 8 are DELIBERATELY
# absent from this set: part 7 is derived by the controller from the bound
# audit record and part 8 is a controller constant, so a preparation result
# that carried either would be refused rather than trusted.
ACCEPTANCE_EXPLANATION_CONTENT_RESULT_KEYS = (
    "result_schema_id",
    "result_schema_version",
    "whole_check_complete",
    "candidate_path",
    "candidate_sha256",
    "candidate_bytes",
    "predecessor_state",
    "predecessor_candidate_path",
    "predecessor_candidate_sha256",
) + EXPLANATION_CONTENT_PART_KEYS

# Section 6.6 rule 4 -- a part made only of identifiers, digests, paths, byte
# counts or diff jargon is not an explanation.  The thresholds are the
# implementation-time values Section 22.3 item 4 leaves open; they are stated
# here rather than scattered, so one place decides and one place is audited.
EXPLANATION_MIN_ORDINARY_WORDS_PER_PART = 8
EXPLANATION_MIN_ORDINARY_WORD_RATIO = 0.5

# Section 6.6 rule 7 -- an over-bound explanation is REFUSED, never truncated.
# These sit well inside the journal's own INTERVIEW_EVENT_MAX_BYTES record
# bound, so the refusal is this design's own and is reported in its own words
# rather than surfacing as an opaque journal failure.
EXPLANATION_MAX_PART_BYTES = 20_000
EXPLANATION_MAX_RECORD_BYTES = 120_000

# Section 8.1 / 8.3 -- the derivation domains this design settles.
ACCEPTANCE_OFFER_BINDING_DOMAIN = "NH_ACCEPTANCE_OFFER_BINDING_V1"
EXPLANATION_CONTENT_DIGEST_DOMAIN = "NH_ACCEPTANCE_EXPLANATION_CONTENT_V1"
EXPLANATION_DIGEST_DOMAIN = "NH_ACCEPTANCE_EXPLANATION_DIGEST_V1"

# Section 8.2 -- the exact offer binding key set.  Exact means exact: a missing
# key and an extra key are both refused, so an offer can never be computed over
# a binding somebody widened or narrowed.
ACCEPTANCE_OFFER_BINDING_KEYS = (
    "acceptance_scope_digest",
    "acceptance_scope_id",
    "audit_event_seq",
    "audit_event_sha256",
    "audit_identity",
    "branch",
    "candidate_bytes",
    "candidate_path",
    "candidate_sha256",
    "controller_executable_identity",
    "explanation_digest",
    "explanation_event_seq",
    "explanation_event_sha256",
    "explanation_record_identity",
    "explanation_version",
    "head_sha",
    "package_id",
    "package_key",
    "package_scope_id",
    "pass_event_seq",
    "pass_event_sha256",
    "pass_identity",
    "pre_click_authenticated_event_seq",
    "pre_click_authenticated_tail_sha256",
    "pre_click_head_digest_sha256",
    "predecessor_candidate_bytes",
    "predecessor_candidate_path",
    "predecessor_candidate_sha256",
    "predecessor_state",
    "settled_decision_binding_sha256",
    "source_binding_sha256",
    "terminal_chain_sha256",
)

# Section 8.2 -- the complete authenticated head, field by field, and the
# prefixed body spellings the acceptance record carries them under.
INTERVIEW_HEAD_FIELDS = (
    "v",
    "intent_generation",
    "intent_number",
    "intent_event_seq",
    "intent_event_sha256",
    "committed_event_seq",
    "committed_event_sha256",
    "head_auth_sha256",
)
PRE_CLICK_HEAD_BODY_KEY_BY_FIELD = {
    field: "pre_click_head_%s" % ("auth_sha256" if field == "head_auth_sha256" else field)
    for field in INTERVIEW_HEAD_FIELDS
}

# Section 11.1b -- the three externally visible truth classifications, and no
# fourth.  UNRESOLVED is a DERIVED condition of a locked projection: it is not
# a workflow state value, not an event type, not a mark, and not a stored flag.
ACCEPTANCE_TRUTH_NOT_ACCEPTED = "PROVED_NOT_ACCEPTED"
ACCEPTANCE_TRUTH_ACCEPTED = "PROVED_ACCEPTED"
ACCEPTANCE_TRUTH_UNRESOLVED = "UNRESOLVED"
ACCEPTANCE_TRUTHS = (
    ACCEPTANCE_TRUTH_NOT_ACCEPTED,
    ACCEPTANCE_TRUTH_ACCEPTED,
    ACCEPTANCE_TRUTH_UNRESOLVED,
)
ACCEPTANCE_TRUTH_SET = frozenset(ACCEPTANCE_TRUTHS)
assert ACCEPTED_FOR_DESIGN_ONLY not in ACCEPTANCE_TRUTH_SET
assert not (ACCEPTANCE_TRUTH_SET & WORKFLOW_STATE_SET)

# Section 16.4 -- the outcome set of the RECORD operation.  There is no ninth
# outcome and there is no partial success.
ACCEPTANCE_OUTCOMES = (
    "recorded_now",
    "already_recorded",
    "stale_offer",
    "refused_conflict",
    "refused_not_ready",
    "refused_request",
    "refused_unavailable",
    "unresolved_recovery_required",
)
ACCEPTANCE_OUTCOME_SET = frozenset(ACCEPTANCE_OUTCOMES)

# Section 19 -- the refusal classes, and the EXISTING operation outcome each
# maps onto.  No new OPERATION_OUTCOMES member is added, and none is needed.
ACCEPTANCE_REFUSAL_OUTCOME_BY_CLASS = {
    "stale_offer": "needs_ness",
    "refused_not_ready": "needs_ness",
    "refused_conflict": "safety_hold",
    "refused_request": "safety_hold",
    "refused_unavailable": "safety_hold",
}
ACCEPTANCE_REFUSAL_CLASSES = tuple(sorted(ACCEPTANCE_REFUSAL_OUTCOME_BY_CLASS))
assert set(ACCEPTANCE_REFUSAL_OUTCOME_BY_CLASS.values()) <= set(OPERATION_OUTCOMES)
assert set(ACCEPTANCE_REFUSAL_OUTCOME_BY_CLASS) <= ACCEPTANCE_OUTCOME_SET

# Section 16.1 -- the two logical routes, named once.
ACCEPTANCE_OFFER_ROUTE = "/api/acceptance/offer"
ACCEPTANCE_RECORD_ROUTE = "/api/acceptance/record"

# Section 16.3 -- the exact posted field set.  No optional fields.
ACCEPTANCE_POST_REQUIRED_FIELDS = (
    "acceptance_offer_id",
    "acceptance_offer_binding_sha256",
    "pre_click_head_digest_sha256",
    "candidate_sha256",
    "acceptance_scope_id",
    "acceptance_scope_digest",
    "explanation_record_identity",
    "explanation_digest",
    "ness_action_confirmed",
)

# --------------------------------------------------------------------------
# Registered supervisor commands (Section 4.8 controller_command registry).
# --------------------------------------------------------------------------
SUPERVISOR_COMMANDS = (
    "supervisor-status",
    "supervisor-operation-status",
    "diagnose-next-correction-batch",
    "execute-next-claude-task",
    "process-custodied-provider-result",
    "close-open-consumption",
    "reconcile-provider-request",
    "probe-provider-availability",
    "open-new-provider-episode",
    "record-semantic-scope-unlock",
    "record-external-action-resolution",
    "record-transition-choice",
    # The accepted acceptance design's two commands.  They are registered here
    # so the EXISTING generic dispatch reaches them; no second dispatch path,
    # no second command table, and no parallel CLI route is created.
    "acceptance-offer",
    "record-ness-acceptance",
    # v1_8 section 7.5 -- the FIVE new post-acceptance continuation execution
    # commands, plus the read-only loop projection.  They are registered in the
    # SAME table the existing generic dispatch already reads.
    "continue-design-loop",
    "dispatch-piece3-provider-review",
    "commit-piece3-provider-result",
    "prepare-next-design-task",
    "execute-initial-design",
    "loop-status",
)
SUPERVISOR_COMMAND_SET = frozenset(SUPERVISOR_COMMANDS)

# v1_8 section 7.5 -- the closed continuation command set, and its exact
# counts.  FIVE new execution names and TWO installed ones; FOUR reach a
# provider and THREE do not.  loop-status is a read-only CLI command and is
# deliberately NOT counted among the seven execution commands.
CONTINUATION_NEW_EXECUTION_COMMANDS = (
    "continue-design-loop",
    "dispatch-piece3-provider-review",
    "commit-piece3-provider-result",
    "prepare-next-design-task",
    "execute-initial-design",
)
CONTINUATION_INSTALLED_EXECUTION_COMMANDS = (
    "process-custodied-provider-result",
    "reconcile-provider-request",
)
CONTINUATION_EXECUTION_COMMANDS = frozenset(
    CONTINUATION_NEW_EXECUTION_COMMANDS + CONTINUATION_INSTALLED_EXECUTION_COMMANDS
)

# v1_8 section 12.3d E5 / section 18 Row M -- WHICH COMMAND OWNS THE MISSING
# COMPLETION OF AN INTERRUPTED TRANSITION OPERATION.
#
# It is the command that STARTED that operation, and nothing else.  There is NO
# eighth continuation execution command: ``supervisor-operation-status`` stays
# READ-ONLY ("It writes nothing, ever") and is never routed here, because it
# receives no operation envelope from the worker and therefore could not append
# the completion even if it were asked to.
CONTINUATION_COMPLETION_OWNER_COMMANDS = frozenset(
    CONTINUATION_NEW_EXECUTION_COMMANDS + CONTINUATION_INSTALLED_EXECUTION_COMMANDS
)
# Accepted role-split v1_6 section 5.1: prepare-next-design-task is NOT added
# to, or RETAINED in, any set whose meaning is "this command may contact a
# provider".  The command and its state-machine position both remain; its NEW
# operations perform a bounded LOCAL derivation and make ZERO provider calls.
# The counts move with it: THREE contacting, FOUR provider-free.
CONTINUATION_PROVIDER_CONTACTING_COMMANDS = frozenset(
    (
        "continue-design-loop",
        "dispatch-piece3-provider-review",
        "execute-initial-design",
    )
)
CONTINUATION_PROVIDER_FREE_COMMANDS = frozenset(
    (
        "commit-piece3-provider-result",
        "process-custodied-provider-result",
        "reconcile-provider-request",
        # v1_6 section 5.1 / section 5.7 -- local T3 opens no provider request,
        # no dispatch, no custody, no terminal and no provider episode.
        "prepare-next-design-task",
    )
)
assert len(CONTINUATION_NEW_EXECUTION_COMMANDS) == 5
assert len(CONTINUATION_INSTALLED_EXECUTION_COMMANDS) == 2
assert len(CONTINUATION_PROVIDER_CONTACTING_COMMANDS) == 3
assert len(CONTINUATION_PROVIDER_FREE_COMMANDS) == 4
assert "prepare-next-design-task" not in CONTINUATION_PROVIDER_CONTACTING_COMMANDS
assert not (
    CONTINUATION_PROVIDER_CONTACTING_COMMANDS & CONTINUATION_PROVIDER_FREE_COMMANDS
)
# The ordinary public Piece-3 commands are NOT members of the continuation set
# (T2-PUBLIC-COMMANDS-UNCHANGED).
assert not (
    CONTINUATION_EXECUTION_COMMANDS
    & {"question-validation", "question-coverage-review"}
)

# v1_8 section 7.3 -- the loop-level states.  These are LOOP states, not
# WORKFLOW_STATES; WORKFLOW_STATES is deliberately unchanged.
LOOP_STATES = (
    "LOOP_NOT_APPLICABLE",
    "LOOP_SELECTION_REQUIRED",
    "LOOP_PACKAGE_CLEARANCE_REQUIRED",
    "LOOP_COVERAGE_REVIEW_REQUIRED",
    "LOOP_PIECE3_RESULT_PENDING",
    "LOOP_PIECE3_COMMIT_REQUIRED",
    "LOOP_TASK_PREPARATION_REQUIRED",
    "LOOP_INITIAL_DESIGN_REQUIRED",
    "LOOP_INITIAL_RESULT_PENDING",
    "LOOP_TRANSITION_RECONCILE_REQUIRED",
    "LOOP_NEEDS_NESS_DECISION",
    "LOOP_NEEDS_USER_ACTION",
    "LOOP_SAFETY_HOLD",
    "LOOP_WAITING_RECOVERING",
    "LOOP_DESIGN_CONTINUATION_COMPLETE",
    "LOOP_HANDOFF_COMPLETE",
)
LOOP_STATE_SET = frozenset(LOOP_STATES)

# v1_8 section 12.3g -- the three controlled Piece-3 variants.  The installed
# (kind, None) rows are preserved exactly and keep the ordinary route.
PIECE3_VARIANT_FIRST_UNROUTED = "first_package_validation_unrouted"
PIECE3_VARIANT_FIRST_ROUTED = "first_package_validation_routed"
PIECE3_VARIANT_VALIDATION_CONTINUATION_UNROUTED = "package_validation_continuation_unrouted"
PIECE3_VARIANT_COVERAGE_UNROUTED = "package_coverage_unrouted"

# v1_8 sections 7.6 / 15.2 -- the two new origin enum values, declared once here
# so the read-side closure rule and the write side cannot drift apart.
CANDIDATE_INTENT_ORIGIN_INITIAL = "initial_design_prepared"
CANDIDATE_CUSTODY_ORIGIN_INITIAL = "initial_design_promoted"

# The ALREADY-INSTALLED recovered-custody origin, named here for READ-SIDE use.
# This is NOT a new enum value and NOT a schema change: the string is exactly the
# one the installed stranded-candidate recovery already writes.  A truthful B8
# completion of the ONE first Case-B transaction carries it, so the read side
# must be able to recognise it -- WITHOUT ever treating it as globally equal to
# the initial origin, which it is not (it is also the ordinary recovery origin
# for a later correction candidate).
CANDIDATE_CUSTODY_ORIGIN_RECOVERED = "stranded_chain_recovered"

# The read-only commands: they write nothing at all.
READ_ONLY_SUPERVISOR_COMMANDS = frozenset(
    (
        "supervisor-status",
        "supervisor-operation-status",
        "acceptance-offer",
        # v1_8 section 7.3 -- loop-status appends nothing, writes nothing,
        # calls no provider and holds no lock beyond the authenticated read.
        "loop-status",
    )
)

# The commands whose request arrives as one strict stdin envelope.
STDIN_ENVELOPE_SUPERVISOR_COMMANDS = frozenset(
    ("supervisor-operation-status", "record-semantic-scope-unlock",
     "record-external-action-resolution", "record-ness-acceptance",
     "record-transition-choice")
)

# Commands that may dispatch a generative provider request.  Neither
# acceptance command is one, and Section 18 M-6 forbids either from becoming
# one.
PROVIDER_DISPATCH_COMMANDS = frozenset(
    (
        "execute-next-claude-task",
        "diagnose-next-correction-batch",
        # v1_8 section 7.5 -- the provider-contacting continuation commands.
        # commit-piece3-provider-result is provider-FREE by construction and is
        # deliberately absent.  Accepted role-split v1_6 section 5.1 removes
        # prepare-next-design-task from this set for the same reason: its new
        # operations are a bounded LOCAL derivation that contacts nobody.
        "continue-design-loop",
        "dispatch-piece3-provider-review",
        "execute-initial-design",
    )
)
assert not (PROVIDER_DISPATCH_COMMANDS & {"commit-piece3-provider-result"})
assert not (PROVIDER_DISPATCH_COMMANDS & {"loop-status"})
# v1_6 section 5.1, asserted rather than assumed.
assert not (PROVIDER_DISPATCH_COMMANDS & {"prepare-next-design-task"})
assert not (PROVIDER_DISPATCH_COMMANDS & {"acceptance-offer", "record-ness-acceptance"})

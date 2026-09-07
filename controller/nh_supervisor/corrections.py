#!/usr/bin/env python3
"""Sections 4.7, 4.7a, 4.7b and 4.8 -- normalized correction operations.

``normalized_correction_operations`` is the only material from which
``strategy_novelty_key`` is derived.  There is deliberately no free-text field,
additions cannot mint labels, and proposed names are non-identity prose.
"""

from __future__ import annotations

from . import constants
from .canonical import canonical_json, is_real_int
from .identity import derive

OPERATION_KEYS = (
    "operation_kind",
    "target_kind",
    "target_anchor_identifier",
    "target_identifier_mode",
    "target_identifier",
    "target_field",
    "new_value_identifier",
    "blocker_ref",
)

FORBIDDEN_OPERATION_KEYS = frozenset(
    (
        "rationale",
        "description",
        "note",
        "summary",
        "title",
        "explanation",
        "proposed_name",
    )
)

OPERATION_KINDS = (
    "add_event_type",
    "remove_event_type",
    "add_event_field",
    "remove_event_field",
    "change_field_type_or_bound",
    "change_field_nullability",
    "add_identity_derivation",
    "change_identity_input_set",
    "add_workflow_state",
    "change_state_transition",
    "add_controller_command",
    "change_command_output_field",
    "add_validation_rule",
    "change_validation_rule",
    "add_enum_value",
    "remove_enum_value",
    "change_replay_rule",
    "change_schema_version_constant",
    "add_test_requirement",
)

TARGET_KINDS = (
    "journal_event_type",
    "event_body_field",
    "identity_domain",
    "workflow_state",
    "state_transition",
    "controller_command",
    "report_field",
    "enum_domain",
    "validation_rule",
    "replay_boundary",
    "test_requirement",
    "schema_version_constant",
)

IDENTIFIER_MODES = ("existing_object", "canonical_addition_slot")

# The controlled semantics vocabularies -- fixed, controller-owned, closed.
EVENT_ADDITION_SEMANTICS = frozenset(
    (
        "provider_phase_evidence", "provider_result_custody", "dependency_record_carrier",
        "dependency_record_reference", "consumption_terminal", "diagnosis_outcome_carrier",
        "specification_carrier", "episode_lifecycle", "availability_probe_evidence",
        "semantic_scope_lifecycle", "semantic_scope_exhaustion_evidence",
        "audit_usability_evidence", "piece3_authorization", "audit_evidence",
        "pass_evidence",
    )
)
FIELD_SEMANTICS = frozenset(
    (
        "identity_digest", "nullable_identity_digest", "event_seq_ref", "event_digest_ref",
        "controlled_enum", "bounded_integer", "boolean_flag", "bounded_ascii_projection",
        "bounded_object", "sorted_unique_ref_list", "byte_length", "base64_bounded_bytes",
        "occurrence_ordinal", "classified_facts_object",
    )
)
IDENTITY_SEMANTICS = frozenset(
    (
        "work_scope_identity", "request_identity", "episode_identity", "probe_identity",
        "dependency_identity", "custody_identity", "series_key", "slot_identity",
        "scope_identity", "scope_exhaustion_identity", "record_digest",
    )
)
STATE_SEMANTICS = frozenset(
    ("working", "waiting_automatic", "blocked_on_person", "fail_closed", "ready")
)
COMMAND_SEMANTICS = frozenset(
    (
        "read_only_status", "read_only_recovery", "provider_dispatch",
        "non_provider_continuation", "non_generative_probe", "episode_unlock",
        "semantic_scope_unlock", "person_invoked_unlock",
    )
)
VALIDATION_SEMANTICS = frozenset(
    (
        "schema_bound", "identity_derivation", "novelty_duplication",
        "authorization_triple", "coverage", "scope_consistency", "carrier_uniqueness",
        "occurrence_ordinal_agreement", "result_usability", "outcome_classification",
        "fail_closed",
    )
)
ENUM_MEMBER_SEMANTICS = frozenset(
    (
        "additional_dependency_class", "additional_dependency_code",
        "additional_terminal_kind", "additional_reconciliation_outcome",
        "additional_symptom_code", "additional_retry_mode",
        "additional_unlock_predicate", "additional_user_action_code",
        "additional_provider_kind", "additional_work_item_kind",
        "additional_termination_kind", "additional_rejection_code",
        "additional_validation_failure_class", "additional_probe_outcome",
        "additional_placement_value", "additional_provider_error_signal_token",
        "additional_audit_usability_failure_class",
        "additional_person_route_reason", "additional_exhaustion_trigger_kind",
    )
)
TEST_SEMANTICS = frozenset(
    (
        "crash_boundary", "identity_stability", "novelty_duplication",
        "dependency_classification", "dependency_carrier", "dependency_occurrence",
        "bounded_attempts", "lease_proof", "custody_recovery", "oversize_bound",
        "probe_boundary", "outcome_classification", "result_usability",
        "capability_baseline", "piece3_boundary", "ui_projection", "replay_no_rewrite",
    )
)
FIELD_TYPE_BOUND_TOKENS = frozenset(
    (
        "ascii_64_hex", "ascii_prefixed_64_hex", "non_negative_integer",
        "positive_integer", "bounded_integer_1_5", "boolean", "bounded_ascii_string",
        "bounded_object", "sorted_unique_list", "nullable_variant_of_the_above",
    )
)
BOUNDED_INTEGER_SET_TOKEN = frozenset(
    (
        "supported_versions_set_4_5", "supported_versions_set_5", "batch_size_5",
        "attempts_5", "output_retries_2", "attempts_per_trigger_2",
        "no_progress_rounds_3", "probes_per_closed_episode_3",
        "automatic_episode_unlocks_3", "scheduling_journal_version_6",
        "capability_registry_entries_16", "signal_map_entries_64",
    )
)

_FIXED_REMOVED = frozenset(("removed",))
_NULLABILITY = frozenset(("non_null", "nullable_by_matrix", "always_null"))
_INPUT_SET = frozenset(("added_input", "removed_input"))
_VALIDATION_CHANGE = frozenset(("strengthened", "scope_narrowed", "scope_widened"))
_REPLAY_RULE = frozenset(
    (
        "no_provider_call_permitted",
        "provider_call_permitted_at_next_serial",
        "retrieval_only",
        "non_provider_continuation",
        "probe_only",
        "fail_closed",
    )
)

# The complete (operation_kind, target_kind) compatibility table.
# Each row: target_kind, identifier_mode, anchor_registry_kind,
#           target_field requirement ("required"/"null"/"state"),
#           new_value domain (a frozenset, or a special token).
COMPATIBILITY = {
    "add_event_type": ("journal_event_type", "canonical_addition_slot",
                       "schema_version_constant", "null", EVENT_ADDITION_SEMANTICS),
    "remove_event_type": ("journal_event_type", "existing_object",
                          "schema_version_constant", "null", _FIXED_REMOVED),
    "add_event_field": ("event_body_field", "canonical_addition_slot",
                        "journal_event_type", "null", FIELD_SEMANTICS),
    "remove_event_field": ("event_body_field", "existing_object",
                           "journal_event_type", "required", _FIXED_REMOVED),
    "change_field_type_or_bound": ("event_body_field", "existing_object",
                                   "journal_event_type", "required",
                                   FIELD_TYPE_BOUND_TOKENS),
    "change_field_nullability": ("event_body_field", "existing_object",
                                 "journal_event_type", "required", _NULLABILITY),
    "add_identity_derivation": ("identity_domain", "canonical_addition_slot",
                                "identity_domain_table", "null", IDENTITY_SEMANTICS),
    "change_identity_input_set": ("identity_domain", "existing_object",
                                  "identity_domain_table", "required", _INPUT_SET),
    "add_workflow_state": ("workflow_state", "canonical_addition_slot",
                           "workflow_state_set", "null", STATE_SEMANTICS),
    "change_state_transition": ("state_transition", "existing_object",
                                "state_transition_table", "state", "state"),
    "add_controller_command": ("controller_command", "canonical_addition_slot",
                               "controller_command_set", "null", COMMAND_SEMANTICS),
    "change_command_output_field": ("report_field", "existing_object",
                                    "controller_command", "required",
                                    FIELD_TYPE_BOUND_TOKENS),
    "add_validation_rule": ("validation_rule", "canonical_addition_slot",
                            "validation_rule_set", "null", VALIDATION_SEMANTICS),
    "change_validation_rule": ("validation_rule", "existing_object",
                               "validation_rule_set", "null", _VALIDATION_CHANGE),
    "add_enum_value": ("enum_domain", "canonical_addition_slot", "enum_domain",
                       "null", ENUM_MEMBER_SEMANTICS),
    "remove_enum_value": ("enum_domain", "existing_object", "enum_domain",
                          "required", _FIXED_REMOVED),
    "change_replay_rule": ("replay_boundary", "existing_object",
                           "replay_boundary_set", "null", _REPLAY_RULE),
    "change_schema_version_constant": ("schema_version_constant", "existing_object",
                                       "schema_version_constant_table", "null",
                                       "integer_or_token"),
    "add_test_requirement": ("test_requirement", "canonical_addition_slot",
                             "test_requirement_set", "null", TEST_SEMANTICS),
}


class CorrectionOperationError(ValueError):
    """A normalized correction operation failed validation."""


# ---------------------------------------------------------------------------
# Section 4.8 -- the controlled design-object registry, derived mechanically
# from the controller's own declared tables and never from model output.
# ---------------------------------------------------------------------------
SCHEMA_VERSION_CONSTANT_NAMES = (
    "INTERVIEW_JOURNAL_CURRENT_VERSION",
    "INTERVIEW_JOURNAL_SUPPORTED_VERSIONS",
    "SUPERVISOR_PROTOCOL_VERSION",
    "SUPERVISOR_SCHEDULING_JOURNAL_VERSION",
    "CORRECTION_BATCH_SIZE",
    "MAX_PROVIDER_ATTEMPTS_PER_WORK_ITEM_EPISODE",
    "MAX_PROVIDER_OUTPUT_RETRIES_PER_EPISODE",
    "DIAGNOSIS_ATTEMPTS_PER_TRIGGER",
    "MAX_NO_PROGRESS_ROUNDS_PER_SEMANTIC_SCOPE",
    "MAX_INLINE_RESULT_BYTES",
    "MAX_CANDIDATE_BYTES",
    "MAX_PROVIDER_RESULT_BYTES",
    "MAX_PROVIDER_RESULT_READ_LIMIT_BYTES",
    "MAX_PROBE_RESULT_BYTES",
    "MAX_PROBE_RESULT_READ_LIMIT_BYTES",
    "MAX_AVAILABILITY_PROBES_PER_CLOSED_EPISODE",
    "MAX_AUTOMATIC_EPISODE_UNLOCKS_PER_WORK_ITEM",
    "MIN_EPISODE_UNLOCK_WAIT_SECONDS",
    "MAX_CAPABILITY_REGISTRY_ENTRIES",
    "MAX_PROVIDER_ERROR_SIGNAL_MAP_ENTRIES",
    "MAX_RETRY_AFTER_SECONDS",
)

IDENTITY_DOMAIN_TABLE_ID = "NH_IDENTITY_DOMAIN_TABLE_V1"
WORKFLOW_STATE_SET_ID = "NH_WORKFLOW_STATE_SET_V1"
STATE_TRANSITION_TABLE_ID = "NH_STATE_TRANSITION_TABLE_V1"
CONTROLLER_COMMAND_SET_ID = "NH_CONTROLLER_COMMAND_SET_V1"
VALIDATION_RULE_SET_ID = "NH_VALIDATION_RULE_SET_V1"
REPLAY_BOUNDARY_SET_ID = "NH_REPLAY_BOUNDARY_SET_V1"
TEST_REQUIREMENT_SET_ID = "NH_TEST_REQUIREMENT_SET_V1"
SCHEMA_VERSION_CONSTANT_TABLE_ID = "NH_SCHEMA_VERSION_CONSTANT_TABLE_V1"

VALIDATION_RULE_IDS = tuple("V%d" % index for index in range(1, 26))
TEST_REQUIREMENT_IDS = tuple(str(index) for index in range(1, 205))

ENUM_DOMAIN_NAMES = (
    "acceptance_authority",
    "reconciliation_outcome",
    "terminal_kind",
    "terminal_evidence_kind",
    "dependency_class",
    "dependency_code",
    "dependency_identity_binding",
    "resource_kind",
    "retry_mode",
    "unlock_predicate_kind",
    "user_action_code",
    "provider_kind",
    "work_item_kind",
    "operation_kind",
    "target_kind",
    "result_location_kind",
    "result_origin",
    "oversize_detection_kind",
    "provider_availability_probe_outcome",
    "probe_signal_token",
    "provider_error_signal_token",
    "audit_usability_failure_class",
    "validation_failure_class",
    "rejection_code",
    "termination_kind",
    "consumption_authority_kind",
    "diagnosis_outcome",
    "diagnosis_trigger_type",
    "diagnosis_trigger_state",
    "exhaustion_trigger_kind",
    "semantic_unlock_evidence_kind",
    "episode_unlock_evidence_kind",
    "unlock_invocation_kind",
    "person_route_reason",
    "durable_record_placement",
    "workflow_state",
    "recovery_outcome",
    "operation_outcome",
    "lease_state",
    "provider_phase",
    "provider_result_custody",
    "consumption_reconciliation",
    "candidate_reconciliation",
    "design_audit_result_usability",
    "piece3_provider_authorization",
    "availability_probe_state",
)


def build_registry(journal_event_types, event_body_keys, report_field_sets):
    """Derive the Section 4.8 registry from the controller's declared tables."""
    return {
        "journal_event_type": frozenset(journal_event_types),
        "event_body_field": {
            kind: frozenset(keys) for kind, keys in event_body_keys.items()
        },
        "identity_domain": frozenset(
            (
                "NH_MECHANICAL_AUDIT_ID_V1",
                "NH_CORRECTION_BATCH_CHECKPOINT_ID_V1",
                "NH_MECHANICAL_NO_PROGRESS_ID_V1",
                "NH_SEMANTIC_SCOPE_KEY_V1",
                "NH_SEMANTIC_SCOPE_EXHAUSTION_ID_V1",
                "NH_DIAGNOSIS_TRIGGER_ID_V1",
                "NH_CORRECTION_DIAGNOSIS_INPUT_V1",
                "NH_CORRECTION_DIAGNOSIS_RESULT_V1",
                "NH_CORRECTION_STRATEGY_RECORD_ID_V1",
                "NH_CORRECTION_SPECIFICATION_RECORD_ID_V1",
                "NH_CORRECTION_SPECIFICATION_V1",
                "NH_STRATEGY_NOVELTY_KEY_V1",
                "NH_CANONICAL_ADDITION_SLOT_V1",
                "NH_DIAGNOSIS_CONSUMPTION_ID_V1",
                "NH_WORK_ITEM_ID_V1",
                "NH_PROVIDER_AVAILABILITY_EPISODE_ID_V1",
                "NH_PROVIDER_REQUEST_ID_V1",
                "NH_AVAILABILITY_PROBE_ID_V1",
                "NH_PROVIDER_RESULT_CUSTODY_ID_V1",
                "NH_DEPENDENCY_ID_V1",
                "NH_RETRY_SERIES_KEY_V1",
                "NH_CHANGE_EXPLANATION_ID_V1",
                "NH_MECHANICAL_PASS_ID_V1",
                "NH_SUPERVISOR_OPERATION_ID_V1",
                "NH_CONTROLLER_EXECUTABLE_ID_V1",
            )
        ),
        "workflow_state": frozenset(constants.WORKFLOW_STATES),
        "state_transition": frozenset(constants.WORKFLOW_STATES),
        "controller_command": frozenset(constants.SUPERVISOR_COMMANDS),
        "report_field": {
            command: frozenset(fields) for command, fields in report_field_sets.items()
        },
        "enum_domain": frozenset(ENUM_DOMAIN_NAMES),
        "validation_rule": frozenset(VALIDATION_RULE_IDS),
        "replay_boundary": frozenset(constants.REPLAY_BOUNDARY_IDS),
        "test_requirement": frozenset(TEST_REQUIREMENT_IDS),
        "schema_version_constant": frozenset(SCHEMA_VERSION_CONSTANT_NAMES),
        "_anchor_ids": {
            "identity_domain_table": IDENTITY_DOMAIN_TABLE_ID,
            "workflow_state_set": WORKFLOW_STATE_SET_ID,
            "state_transition_table": STATE_TRANSITION_TABLE_ID,
            "controller_command_set": CONTROLLER_COMMAND_SET_ID,
            "validation_rule_set": VALIDATION_RULE_SET_ID,
            "replay_boundary_set": REPLAY_BOUNDARY_SET_ID,
            "test_requirement_set": TEST_REQUIREMENT_SET_ID,
            "schema_version_constant_table": SCHEMA_VERSION_CONSTANT_TABLE_ID,
        },
    }


def _anchor_resolves(registry, anchor_registry_kind, anchor):
    fixed = registry["_anchor_ids"]
    if anchor_registry_kind in fixed:
        return anchor == fixed[anchor_registry_kind]
    if anchor_registry_kind == "schema_version_constant":
        # add_event_type / remove_event_type anchor on the version constant.
        return anchor == "INTERVIEW_JOURNAL_CURRENT_VERSION"
    if anchor_registry_kind == "journal_event_type":
        return anchor in registry["journal_event_type"]
    if anchor_registry_kind == "controller_command":
        return anchor in registry["controller_command"]
    if anchor_registry_kind == "enum_domain":
        return anchor in registry["enum_domain"]
    if anchor_registry_kind == "identity_domain":
        return anchor in registry["identity_domain"]
    return False


def canonical_addition_slot_id(operation):
    return derive(
        "canonical_addition_slot_id",
        {
            "operation_kind": operation["operation_kind"],
            "target_kind": operation["target_kind"],
            "target_anchor_identifier": operation["target_anchor_identifier"],
            "target_field": operation["target_field"],
            "new_value_identifier": operation["new_value_identifier"],
            "blocker_ref": operation["blocker_ref"],
        },
    )


def validate_operation(operation, registry, blocker_refs):
    """Validate one operation; return the list of failure strings."""
    errors = []
    if not isinstance(operation, dict):
        return ["a correction operation is not an object"]
    intruder = sorted(FORBIDDEN_OPERATION_KEYS & set(operation))
    if intruder:
        errors.append("a correction operation may carry no prose field: %s" % ", ".join(intruder))
    missing = sorted(set(OPERATION_KEYS) - set(operation))
    extra = sorted(set(operation) - set(OPERATION_KEYS))
    if missing:
        errors.append("operation missing keys: %s" % ", ".join(missing))
    if extra:
        errors.append("operation carries extra keys: %s" % ", ".join(extra))
    if errors:
        return errors

    kind = operation["operation_kind"]
    row = COMPATIBILITY.get(kind)
    if row is None:
        return ["operation_kind %r is not one of the nineteen values" % (kind,)]
    target_kind, mode, anchor_registry_kind, field_rule, value_domain = row

    if operation["target_kind"] != target_kind:
        errors.append("%s requires target_kind %s" % (kind, target_kind))
    if operation["target_identifier_mode"] != mode:
        errors.append("%s requires target_identifier_mode %s" % (kind, mode))
    if not _anchor_resolves(registry, anchor_registry_kind, operation["target_anchor_identifier"]):
        errors.append(
            "target_anchor_identifier %r does not resolve in the controlled registry"
            % (operation["target_anchor_identifier"],)
        )

    if mode == "canonical_addition_slot":
        if operation["target_identifier"] is not None:
            errors.append(
                "an addition operation must supply target_identifier = null; the "
                "controller derives the canonical addition slot"
            )
    else:
        identifier = operation["target_identifier"]
        if not isinstance(identifier, str) or not identifier:
            errors.append("an existing_object operation must name an identifier")
        else:
            resolved = False
            if target_kind == "journal_event_type":
                resolved = identifier in registry["journal_event_type"]
            elif target_kind == "event_body_field":
                anchor = operation["target_anchor_identifier"]
                resolved = identifier in registry["event_body_field"].get(anchor, frozenset())
            elif target_kind == "identity_domain":
                resolved = identifier in registry["identity_domain"]
            elif target_kind == "enum_domain":
                resolved = identifier in registry["enum_domain"]
            elif target_kind == "validation_rule":
                resolved = identifier in registry["validation_rule"]
            elif target_kind == "replay_boundary":
                resolved = identifier in registry["replay_boundary"]
            elif target_kind == "schema_version_constant":
                resolved = identifier in registry["schema_version_constant"]
            elif target_kind == "report_field":
                anchor = operation["target_anchor_identifier"]
                resolved = identifier in registry["report_field"].get(anchor, frozenset())
            elif target_kind == "state_transition":
                resolved = identifier in registry["state_transition"]
            elif target_kind == "controller_command":
                resolved = identifier in registry["controller_command"]
            elif target_kind == "test_requirement":
                resolved = identifier in registry["test_requirement"]
            if not resolved:
                errors.append(
                    "target_identifier %r does not resolve in the controlled registry"
                    % (identifier,)
                )

    field = operation["target_field"]
    if field_rule == "null":
        if field is not None:
            errors.append("%s requires target_field = null" % kind)
    elif field_rule == "required":
        if not isinstance(field, str) or not field:
            errors.append("%s requires an existing target_field" % kind)
        else:
            if target_kind == "event_body_field":
                anchor = operation["target_anchor_identifier"]
                if field not in registry["event_body_field"].get(anchor, frozenset()):
                    errors.append("target_field %r does not exist on %s" % (field, anchor))
            elif target_kind == "report_field":
                anchor = operation["target_anchor_identifier"]
                if field not in registry["report_field"].get(anchor, frozenset()):
                    errors.append("target_field %r is not a report key of %s" % (field, anchor))
            elif target_kind == "identity_domain":
                pass  # an existing input key name; resolved by the domain table
            elif target_kind == "enum_domain":
                pass  # an existing member name
    elif field_rule == "state":
        if field not in constants.WORKFLOW_STATE_SET:
            errors.append("change_state_transition requires a source state")

    value = operation["new_value_identifier"]
    if value_domain == "state":
        if value not in constants.WORKFLOW_STATE_SET:
            errors.append("change_state_transition requires a destination state")
    elif value_domain == "integer_or_token":
        ok = (is_real_int(value) and value >= 0) or value in BOUNDED_INTEGER_SET_TOKEN
        if not ok:
            errors.append(
                "change_schema_version_constant requires a non-negative integer or a "
                "BOUNDED_INTEGER_SET_TOKEN"
            )
    else:
        if value not in value_domain:
            errors.append(
                "new_value_identifier %r is outside the controlled semantics "
                "vocabulary of %s" % (value, kind)
            )

    if operation["blocker_ref"] not in set(blocker_refs):
        errors.append(
            "blocker_ref %r is not a member of the current blocking finding set"
            % (operation["blocker_ref"],)
        )
    return errors


def normalize_operations(operations, registry, blocker_refs, *, require_non_empty=True):
    """Apply the Section 4.7 canonical ordering and deduplication.

    Steps 1-7, in order.  Raises ``CorrectionOperationError`` on any rejection,
    because a rejection rejects the WHOLE diagnosis or specification.
    """
    if not isinstance(operations, list):
        raise CorrectionOperationError("normalized_correction_operations must be a list")
    if len(operations) > constants.MAX_NORMALIZED_OPERATIONS:
        raise CorrectionOperationError(
            "normalized_correction_operations exceeds MAX_NORMALIZED_OPERATIONS"
        )
    if require_non_empty and not operations:
        raise CorrectionOperationError(
            "a safe strategy or ordinary specification requires a non-empty operation list"
        )

    failures = []
    resolved = []
    for index, operation in enumerate(operations):
        errors = validate_operation(operation, registry, blocker_refs)
        if errors:
            failures.append("operation %d: %s" % (index, "; ".join(errors)))
            continue
        item = dict(operation)
        if item["target_identifier_mode"] == "canonical_addition_slot":
            item["target_identifier"] = canonical_addition_slot_id(item)
        resolved.append(item)
    if failures:
        raise CorrectionOperationError("; ".join(failures))

    # 5. remove exact duplicate objects.
    seen = {}
    for item in resolved:
        seen[canonical_json(item)] = item
    unique = list(seen.values())

    # 6. sort by the canonical encoding of the ordered tuple.
    def sort_key(item):
        return canonical_json(
            [
                item["operation_kind"],
                item["target_kind"],
                item["target_anchor_identifier"],
                item["target_identifier_mode"],
                item["target_identifier"],
                item["target_field"],
                item["new_value_identifier"],
                item["blocker_ref"],
            ]
        ).encode("utf-8")

    unique.sort(key=sort_key)
    return unique


def check_blocker_coverage(operations, blocker_refs):
    """V2/V11 -- every blocking finding is named by at least one operation."""
    named = {item["blocker_ref"] for item in operations}
    missing = sorted(set(blocker_refs) - named)
    return missing


def validate_proposed_addition_names(names, operations):
    """Section 4.7b -- bounds, ASCII, and index validity; then it is prose."""
    errors = []
    if names is None:
        return errors
    if not isinstance(names, list):
        return ["proposed_addition_names must be a list"]
    if len(names) > constants.MAX_PROPOSED_ADDITION_NAMES:
        errors.append("proposed_addition_names exceeds MAX_PROPOSED_ADDITION_NAMES")
    for index, entry in enumerate(names):
        if not isinstance(entry, dict) or set(entry) != {"operation_index", "proposed_name"}:
            errors.append("proposed_addition_names[%d] has the wrong shape" % index)
            continue
        position = entry["operation_index"]
        if not is_real_int(position) or not (0 <= position < len(operations)):
            errors.append("proposed_addition_names[%d] index is out of range" % index)
            continue
        if operations[position]["target_identifier_mode"] != "canonical_addition_slot":
            errors.append(
                "proposed_addition_names[%d] names an operation that is not an addition"
                % index
            )
        name = entry["proposed_name"]
        if not isinstance(name, str) or not name or len(name) > 256:
            errors.append("proposed_addition_names[%d] proposed_name is not bounded ASCII" % index)
        elif any(ord(char) > 127 for char in name):
            errors.append("proposed_addition_names[%d] proposed_name is not ASCII" % index)
    return errors


def strategy_novelty_key(
    package_scope_id,
    source_binding_sha256,
    candidate_path,
    candidate_sha256,
    candidate_bytes,
    blocking_finding_refs,
    normalized_operations,
):
    """The only novelty material is the normalized operation set (Section 4.7)."""
    return derive(
        "strategy_novelty_key",
        {
            "package_scope_id": package_scope_id,
            "source_binding_sha256": source_binding_sha256,
            "candidate_path": candidate_path,
            "candidate_sha256": candidate_sha256,
            "candidate_bytes": candidate_bytes,
            "blocking_finding_refs": sorted(set(blocking_finding_refs)),
            "normalized_correction_operations": normalized_operations,
        },
    )

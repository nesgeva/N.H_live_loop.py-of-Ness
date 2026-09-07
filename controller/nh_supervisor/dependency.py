#!/usr/bin/env python3
"""Sections 4.2d, 4.5, 4.5a and 11.8 -- the controller-owned dependency tables.

The model never chooses the class, the code, the binding, the retry mode, the
unlock predicate, the state, the placement, the carrier, or the occurrence
ordinal.  Every value below is a literal row of the specification.
"""

from __future__ import annotations

from . import constants
from .canonical import is_real_int
from .identity import dependency_identity

# ---------------------------------------------------------------------------
# Section 11.8a -- class / code / binding / retry / unlock / action / state.
# ---------------------------------------------------------------------------
# Each entry: code -> (class, binding, resource_kind, retry_mode,
#                      predicate_kind, user_action_code, next_workflow_state)
REGISTRY = {
    "provider_unreachable_before_dispatch": (
        "temporary_provider_failure", "episode_bound", "provider_endpoint",
        "automatic_backoff", "time_and_probe_success", None, "WAITING_RECOVERING"),
    "provider_rate_limited_before_dispatch": (
        "temporary_provider_failure", "episode_bound", "provider_endpoint",
        "automatic_backoff", "time_and_probe_success", None, "WAITING_RECOVERING"),
    "provider_timeout_before_dispatch": (
        "temporary_provider_failure", "episode_bound", "provider_endpoint",
        "automatic_backoff", "time_and_probe_success", None, "WAITING_RECOVERING"),
    "provider_transient_error_terminal_recorded": (
        "temporary_provider_failure", "episode_bound", "provider_endpoint",
        "automatic_backoff", "time_and_probe_success", None, "WAITING_RECOVERING"),
    "provider_rate_limited_terminal_recorded": (
        "temporary_provider_failure", "episode_bound", "provider_endpoint",
        "automatic_backoff", "time_and_probe_success", None, "WAITING_RECOVERING"),
    "provider_service_unavailable_terminal_recorded": (
        "temporary_provider_failure", "episode_bound", "provider_endpoint",
        "automatic_backoff", "time_and_probe_success", None, "WAITING_RECOVERING"),
    "provider_dispatch_absent_proved_retry_authorized": (
        "temporary_provider_failure", "episode_bound", "provider_endpoint",
        "automatic_backoff", "time_and_probe_success", None, "WAITING_RECOVERING"),
    "provider_output_invalid_bounded_retry": (
        "temporary_provider_failure", "episode_bound", "provider_endpoint",
        "automatic_bounded_output_retry", "bounded_output_retry_budget_available",
        None, "WAITING_RECOVERING"),
    "provider_output_oversize_bounded_retry": (
        "temporary_provider_failure", "episode_bound", "provider_endpoint",
        "automatic_bounded_output_retry", "bounded_output_retry_budget_available",
        None, "WAITING_RECOVERING"),
    "provider_episode_exhausted_awaiting_probe": (
        "temporary_provider_failure", "episode_bound", "provider_endpoint",
        "automatic_probe_only", "time_and_probe_success", None, "WAITING_RECOVERING"),

    "dispatch_begun_result_unknown": (
        "provider_outcome_unknown", "provider_request_bound", "provider_endpoint",
        "automatic_lookup_only", "authoritative_lookup_result_obtained", None,
        "WAITING_RECOVERING"),
    "lookup_transiently_failed": (
        "provider_outcome_unknown", "provider_request_bound", "provider_endpoint",
        "automatic_lookup_only", "authoritative_lookup_result_obtained", None,
        "WAITING_RECOVERING"),
    "lookup_unsupported_by_capability_contract": (
        "provider_outcome_unknown", "provider_request_bound", "provider_endpoint",
        "no_automatic_retry_until_unlock_proved", "named_external_action_observed",
        "provider_outcome_confirmation_required", "NEEDS_USER_ACTION"),
    "terminal_result_unretrievable": (
        "provider_outcome_unknown", "provider_request_bound", "provider_endpoint",
        "no_automatic_retry_until_unlock_proved", "named_external_action_observed",
        "provider_result_retrieval_required", "NEEDS_USER_ACTION"),

    "local_tool_missing": (
        "temporary_local_resource_failure", "work_item_bound", "local_tool",
        "automatic_backoff", "time_and_probe_success", None, "WAITING_RECOVERING"),
    "local_tool_exit_transient": (
        "temporary_local_resource_failure", "work_item_bound", "local_tool",
        "automatic_backoff", "time_and_probe_success", None, "WAITING_RECOVERING"),
    "local_path_unwritable": (
        "temporary_local_resource_failure", "work_item_bound", "local_path",
        "automatic_backoff", "time_and_probe_success", None, "WAITING_RECOVERING"),
    "workspace_lock_contended": (
        "temporary_local_resource_failure", "work_item_bound", "local_path",
        "automatic_backoff", "time_and_probe_success", None, "WAITING_RECOVERING"),

    "source_checkout_unreadable": (
        "temporary_source_access_failure", "work_item_bound", "source_repository",
        "automatic_backoff", "source_binding_restored", None, "WAITING_RECOVERING"),
    "source_binding_temporarily_unverifiable": (
        "temporary_source_access_failure", "work_item_bound", "source_repository",
        "automatic_backoff", "source_binding_restored", None, "WAITING_RECOVERING"),
    "git_index_lock_present": (
        "temporary_source_access_failure", "work_item_bound", "local_tool",
        "automatic_backoff", "time_and_probe_success", None, "WAITING_RECOVERING"),

    "provider_account_unavailable": (
        "external_user_action_required", "episode_bound", "external_account",
        "no_automatic_retry_until_unlock_proved", "named_external_action_observed",
        "provider_account_unavailable", "NEEDS_USER_ACTION"),
    "provider_credential_expired": (
        "external_user_action_required", "episode_bound", "external_account",
        "no_automatic_retry_until_unlock_proved", "named_external_action_observed",
        "provider_credential_expired", "NEEDS_USER_ACTION"),
    "provider_quota_exhausted": (
        "external_user_action_required", "episode_bound", "external_account",
        "no_automatic_retry_until_unlock_proved", "named_external_action_observed",
        "provider_quota_exhausted", "NEEDS_USER_ACTION"),
    "provider_non_transient_error_proved": (
        "external_user_action_required", "episode_bound", "provider_endpoint",
        "no_automatic_retry_until_unlock_proved", "named_external_action_observed",
        "provider_non_transient_error_proved", "NEEDS_USER_ACTION"),
    "provider_local_process_terminal_failure": (
        "external_user_action_required", "episode_bound", "provider_endpoint",
        "no_automatic_retry_until_unlock_proved", "named_external_action_observed",
        "provider_local_process_failure_review_required", "NEEDS_USER_ACTION"),
    "provider_outcome_confirmation_required": (
        "external_user_action_required", "provider_request_bound", "provider_endpoint",
        "no_automatic_retry_until_unlock_proved", "named_external_action_observed",
        "provider_outcome_confirmation_required", "NEEDS_USER_ACTION"),
    "provider_repeatedly_unavailable": (
        "external_user_action_required", "episode_bound", "provider_endpoint",
        "no_automatic_retry_until_unlock_proved", "provider_availability_unlock_proved",
        "provider_repeatedly_unavailable", "NEEDS_USER_ACTION"),
    "provider_availability_probe_unsupported": (
        "external_user_action_required", "episode_bound", "capability_registry",
        "no_automatic_retry_until_unlock_proved", "provider_availability_unlock_proved",
        "provider_repeatedly_unavailable", "NEEDS_USER_ACTION"),
    "external_dependency_absent": (
        "external_user_action_required", "work_item_bound", "capability_registry",
        "no_automatic_retry_until_unlock_proved", "named_external_action_observed",
        "external_dependency_absent", "NEEDS_USER_ACTION"),

    "authority_conflict_proved": (
        "authority_or_safety_conflict", "work_item_bound", "source_repository",
        "no_retry_fail_closed", "manual_safety_review", None, "SAFETY_HOLD"),
    "custody_contradiction": (
        "authority_or_safety_conflict", "work_item_bound", "interview_journal",
        "no_retry_fail_closed", "manual_safety_review", None, "SAFETY_HOLD"),
    "journal_contradiction": (
        "authority_or_safety_conflict", "work_item_bound", "interview_journal",
        "no_retry_fail_closed", "manual_safety_review", None, "SAFETY_HOLD"),
    "lease_ownership_unproved": (
        "authority_or_safety_conflict", "work_item_bound", "local_path",
        "no_retry_fail_closed", "manual_safety_review", None, "SAFETY_HOLD"),
    "source_changed_under_operation": (
        "authority_or_safety_conflict", "work_item_bound", "source_repository",
        "no_retry_fail_closed", "manual_safety_review", None, "SAFETY_HOLD"),
    "provider_result_custody_unverifiable": (
        "authority_or_safety_conflict", "work_item_bound", "local_path",
        "no_retry_fail_closed", "manual_safety_review", None, "SAFETY_HOLD"),
    "diagnosis_authority_contradiction": (
        "authority_or_safety_conflict", "work_item_bound", "source_repository",
        "no_retry_fail_closed", "manual_safety_review", None, "SAFETY_HOLD"),
    "unclassifiable_observation": (
        "authority_or_safety_conflict", "work_item_bound", "capability_registry",
        "no_retry_fail_closed", "manual_safety_review", None, "SAFETY_HOLD"),

    "no_materially_new_strategy_available": (
        "no_currently_safe_strategy", "work_item_bound", "source_repository",
        "no_automatic_retry_until_unlock_proved", "new_ness_decision_or_source_change",
        None, "WAITING_RECOVERING"),
    "capability_change_required": (
        "no_currently_safe_strategy", "work_item_bound", "capability_registry",
        "no_automatic_retry_until_unlock_proved", "authenticated_capability_record_updated",
        None, "WAITING_RECOVERING"),
    "repeated_semantic_no_progress_in_scope": (
        "no_currently_safe_strategy", "work_item_bound", "source_repository",
        "no_automatic_retry_until_unlock_proved", "new_ness_decision_or_source_change",
        None, "WAITING_RECOVERING"),
    "diagnosis_output_repeatedly_invalid": (
        "no_currently_safe_strategy", "work_item_bound", "provider_endpoint",
        "no_automatic_retry_until_unlock_proved", "new_ness_decision_or_source_change",
        None, "WAITING_RECOVERING"),
    "provider_output_repeatedly_invalid": (
        "no_currently_safe_strategy", "work_item_bound", "provider_endpoint",
        "no_automatic_retry_until_unlock_proved", "new_ness_decision_or_source_change",
        None, "WAITING_RECOVERING"),
    "provider_output_repeatedly_oversize": (
        "no_currently_safe_strategy", "work_item_bound", "provider_endpoint",
        "no_automatic_retry_until_unlock_proved", "new_ness_decision_or_source_change",
        None, "WAITING_RECOVERING"),
}

REGISTRY_FIELDS = (
    "dependency_class",
    "dependency_identity_binding",
    "resource_kind",
    "retry_mode",
    "predicate_kind",
    "user_action_code",
    "next_workflow_state",
)

# Section 11.8a -- family-4 membership is decided structurally, never by a row
# list: class no_currently_safe_strategy AND predicate
# new_ness_decision_or_source_change.
FAMILY4_CODES = frozenset(
    code
    for code, row in REGISTRY.items()
    if row[0] == "no_currently_safe_strategy"
    and row[4] == "new_ness_decision_or_source_change"
)

RETRY_MODES_THAT_SCHEDULE = frozenset(
    (
        "automatic_backoff",
        "automatic_lookup_only",
        "automatic_bounded_output_retry",
        "automatic_probe_only",
    )
)


def registry_row(code):
    row = REGISTRY.get(code)
    if row is None:
        return None
    return dict(zip(REGISTRY_FIELDS, row))


# ---------------------------------------------------------------------------
# Section 11.8b -- total mapping from a validated diagnosis observation.
# ---------------------------------------------------------------------------
MODEL_ROWS = {
    "local_tool_missing": ("A1", "local_tool_missing", "local_tool"),
    "local_tool_failed": ("A2", "local_tool_exit_transient", "local_tool"),
    "local_path_unwritable": ("A3", "local_path_unwritable", "local_path"),
    "local_lock_contended": ("A4", "workspace_lock_contended", "local_path"),
    "source_unreadable": ("A5", "source_checkout_unreadable", "source_repository"),
    "source_binding_unverifiable": (
        "A6",
        "source_binding_temporarily_unverifiable",
        "source_repository",
    ),
    "source_changed": ("A7", "source_changed_under_operation", "source_repository"),
    "journal_contradiction": ("A8", "journal_contradiction", "interview_journal"),
    "authority_conflict": ("A9", "authority_conflict_proved", "source_repository"),
    "capability_record_absent": ("A10", "capability_change_required", "capability_registry"),
    "capability_change_required": (
        "A11",
        "capability_change_required",
        "capability_registry",
    ),
    "no_new_operation_set": (
        "A12",
        "no_materially_new_strategy_available",
        "source_repository",
    ),
    "external_dependency_absent": (
        "A13",
        "external_dependency_absent",
        "capability_registry",
    ),
}

# Section 11.8b compatibility with diagnosis_outcome (V5, V19).
MODEL_ROW_REQUIRED_OUTCOME = {
    "A1": "temporary_technical_dependency",
    "A2": "temporary_technical_dependency",
    "A3": "temporary_technical_dependency",
    "A4": "temporary_technical_dependency",
    "A5": "temporary_technical_dependency",
    "A6": "temporary_technical_dependency",
    "A7": "authority_or_safety_conflict",
    "A8": "authority_or_safety_conflict",
    "A9": "authority_or_safety_conflict",
    "A10": "no_currently_safe_strategy",
    "A11": "no_currently_safe_strategy",
    "A12": "no_currently_safe_strategy",
    "A13": "external_user_action_required",
}

MODEL_ROW_PLACEMENT = "correction_diagnosis_recorded"

# ---------------------------------------------------------------------------
# Section 11.8c -- controller-observed rows.
# Each entry: row id -> (code, placement, shape)
#   shape in {"C|R", "R", "0", "none_read_only_projection"}
# Rows C5 and C27 classify nothing at all.
# ---------------------------------------------------------------------------
CONTROLLER_ROWS = {
    "C1": ("lookup_unsupported_by_capability_contract", "provider_request_reconciled", "C|R"),
    "C2": ("lookup_transiently_failed", "provider_request_reconciled", "C|R"),
    "C3": ("provider_dispatch_absent_proved_retry_authorized",
           "provider_request_reconciled", "C|R"),
    "C4": ("dispatch_begun_result_unknown", "provider_request_reconciled", "C|R"),
    "C5": (None, None, "0"),
    "C6": ("terminal_result_unretrievable", "provider_request_reconciled", "C|R"),
    "C7": ("provider_transient_error_terminal_recorded",
           "provider_request_terminal_recorded", "C|R"),
    "C8": ("provider_non_transient_error_proved",
           "provider_request_terminal_recorded", "C|R"),
    "C9": ("provider_output_invalid_bounded_retry",
           "provider_request_terminal_recorded", "C|R"),
    "C10": ("provider_output_repeatedly_invalid",
            "provider_request_terminal_recorded", "C|R"),
    "C11": ("provider_episode_exhausted_awaiting_probe",
            "provider_availability_episode_exhausted_recorded", "C|R"),
    "C11a": ("provider_repeatedly_unavailable",
             "provider_availability_episode_exhausted_recorded", "C|R"),
    "C12": ("provider_output_invalid_bounded_retry",
            "correction_diagnosis_validation_failed_recorded", "C|R"),
    "C13": ("diagnosis_output_repeatedly_invalid",
            "correction_diagnosis_validation_failed_recorded", "C|R"),
    "C14": ("diagnosis_authority_contradiction",
            "correction_diagnosis_validation_failed_recorded", "C|R"),
    "C15": ("no_materially_new_strategy_available",
            "semantic_scope_exhaustion_recorded", "C|R"),
    "C16": ("repeated_semantic_no_progress_in_scope",
            "semantic_scope_exhaustion_recorded", "C|R"),
    "C17": ("provider_result_custody_unverifiable",
            "supervisor_operation_completed", "C|R"),
    "C18": ("lease_ownership_unproved", "none_read_only_projection",
            "none_read_only_projection"),
    "C19": ("source_changed_under_operation", "supervisor_operation_completed", "C|R"),
    "C20": ("journal_contradiction", "supervisor_operation_completed", "C|R"),
    "C21": ("custody_contradiction", "supervisor_operation_completed", "C|R"),
    "C22": (None, "supervisor_operation_completed", "C|R"),
    "C23": (None, "supervisor_operation_completed", "C|R"),
    "C24": (None, "provider_availability_unlock_recorded", "R"),
    "C24a": ("provider_repeatedly_unavailable",
             "provider_availability_unlock_recorded", "C|R"),
    "C25": (None, "diagnosis_strategy_consumption_terminated", "R"),
    "C26": (None, "supervisor_operation_completed", "C|R"),
    "C27": (None, None, "0"),
    "C28": (None, "supervisor_operation_completed", "C|R"),
    "C29": ("provider_output_oversize_bounded_retry",
            "provider_request_terminal_recorded", "C|R"),
    "C30": ("provider_output_repeatedly_oversize",
            "provider_request_terminal_recorded", "C|R"),
    "C31": (None, "availability_probe_result_recorded", "C|R"),
    "C32": ("provider_availability_probe_unsupported",
            "availability_probe_result_recorded", "C|R"),
    "C33": (None, "semantic_scope_unlock_recorded", "R"),
    "C34": ("provider_rate_limited_terminal_recorded",
            "provider_request_terminal_recorded", "C|R"),
    "C35": ("provider_service_unavailable_terminal_recorded",
            "provider_request_terminal_recorded", "C|R"),
    "C36": ("provider_credential_expired", "provider_request_terminal_recorded", "C|R"),
    "C37": ("provider_account_unavailable", "provider_request_terminal_recorded", "C|R"),
    "C38": ("provider_quota_exhausted", "provider_request_terminal_recorded", "C|R"),
    "C39": ("authority_conflict_proved", "mechanical_audit_unusable_recorded", "C|R"),
    "C40": ("provider_output_invalid_bounded_retry",
            "mechanical_audit_unusable_recorded", "C|R"),
    "C41": ("provider_output_repeatedly_invalid",
            "mechanical_audit_unusable_recorded", "C|R"),
}

# Rows C26 and C28 select their code by the bounded-output-retry budget.
BUDGET_SPLIT_ROWS = {
    "C26": {
        "available": "provider_output_invalid_bounded_retry",
        "exhausted": "provider_output_repeatedly_invalid",
    },
    "C28": {
        "available": "provider_output_invalid_bounded_retry",
        "exhausted": "provider_output_repeatedly_invalid",
    },
    "C31": {
        "probes_remain": "provider_episode_exhausted_awaiting_probe",
        "probes_exhausted": "provider_repeatedly_unavailable",
    },
}

REFERENCE_ONLY_ROWS = frozenset(("C24", "C25", "C33"))
NO_RECORD_ROWS = frozenset(("C5", "C27"))

# Section 11.8d -- the single fail-closed row.
FAIL_CLOSED_ROW_ID = "D1"
FAIL_CLOSED_CODE = "unclassifiable_observation"

# Section 11.8d -- the complete precedence order, every row exactly once.
PRECEDENCE_ORDER = (
    ("contradiction rows", ("C17", "C19", "C20", "C21")),
    ("read-only lease projection", ("C18",)),
    ("reconciliation-derived rows", ("C1", "C2", "C3", "C4", "C5", "C6")),
    (
        "terminal-derived rows",
        ("C7", "C8", "C9", "C10", "C29", "C30", "C34", "C35", "C36", "C37", "C38"),
    ),
    ("design-audit usability rows", ("C39", "C40", "C41")),
    ("episode, probe, unlock rows", ("C11", "C11a", "C24", "C24a", "C31", "C32")),
    (
        "bound and budget escalations",
        ("C12", "C13", "C14", "C15", "C16", "C26", "C27", "C28", "C33"),
    ),
    ("consumption-closure row", ("C25",)),
    ("controller-observed local and source rows", ("C22", "C23")),
    (
        "model-observation rows",
        tuple("A%d" % index for index in range(1, 14)),
    ),
    ("the fail-closed row of 11.8d", (FAIL_CLOSED_ROW_ID,)),
)


def precedence_row_ids():
    ids = []
    for _label, rows in PRECEDENCE_ORDER:
        ids.extend(rows)
    return tuple(ids)


class DependencyError(ValueError):
    """A dependency record could not be built from the supplied observation."""


def build_record(
    code,
    resource_identity,
    work_item_identity,
    *,
    resource_kind=None,
    episode_identity=None,
    request_identity=None,
    predicate_params=None,
    observed_symptom_code=None,
    phase_evidence_condition="not_provider_scoped",
    durable_record_placement=None,
    observed_evidence_event_seq=None,
    observed_evidence_sha256=None,
    plain_language_dependency="",
):
    """Build one literal ``DEPENDENCY_RECORD_V1`` from its registry row."""
    row = registry_row(code)
    if row is None:
        raise DependencyError("no Section 11.8a registry row for code %r" % (code,))
    binding = row["dependency_identity_binding"]
    kind = resource_kind or row["resource_kind"]
    if kind not in constants.RESOURCE_KINDS:
        raise DependencyError("resource_kind %r is not controlled" % (kind,))

    if binding == "work_item_bound":
        episode = None
        request = None
    elif binding == "episode_bound":
        if episode_identity is None:
            raise DependencyError("%s requires an episode identity" % code)
        episode = episode_identity
        request = None
    else:
        if episode_identity is None or request_identity is None:
            raise DependencyError(
                "%s requires both the episode and the exact request identity" % code
            )
        episode = episode_identity
        request = request_identity

    params = dict(predicate_params or {})
    unknown = sorted(set(params) - constants.UNLOCK_PREDICATE_PARAM_KEYS)
    if unknown:
        raise DependencyError(
            "unlock_predicate params may not contain %s" % ", ".join(unknown)
        )

    record = {
        "dependency_record_version": constants.DEPENDENCY_RECORD_VERSION,
        "dependency_class": row["dependency_class"],
        "dependency_code": code,
        "dependency_identity_binding": binding,
        "resource_kind": kind,
        "resource_identity": resource_identity,
        "work_item_identity": work_item_identity,
        "provider_availability_episode_identity": episode,
        "provider_request_identity": request,
        "retry_mode": row["retry_mode"],
        "unlock_predicate": {
            "predicate_kind": row["predicate_kind"],
            "params": params,
        },
        "user_action_code": row["user_action_code"],
        "next_workflow_state": row["next_workflow_state"],
        "observed_symptom_code": observed_symptom_code,
        "phase_evidence_condition": phase_evidence_condition,
        "durable_record_placement": durable_record_placement,
        "observed_evidence_event_seq": observed_evidence_event_seq,
        "observed_evidence_sha256": observed_evidence_sha256,
        "plain_language_dependency": plain_language_dependency,
    }
    return record


DEPENDENCY_RECORD_KEYS = frozenset(
    (
        "dependency_record_version",
        "dependency_class",
        "dependency_code",
        "dependency_identity_binding",
        "resource_kind",
        "resource_identity",
        "work_item_identity",
        "provider_availability_episode_identity",
        "provider_request_identity",
        "retry_mode",
        "unlock_predicate",
        "user_action_code",
        "next_workflow_state",
        "observed_symptom_code",
        "phase_evidence_condition",
        "durable_record_placement",
        "observed_evidence_event_seq",
        "observed_evidence_sha256",
        "plain_language_dependency",
    )
)


def check_record(record):
    """Validate one record against Section 4.5 / 4.5a / 11.8a; return errors."""
    errors = []
    if not isinstance(record, dict):
        return ["dependency record is not an object"]
    missing = sorted(DEPENDENCY_RECORD_KEYS - set(record))
    extra = sorted(set(record) - DEPENDENCY_RECORD_KEYS)
    if missing:
        errors.append("dependency record is missing: %s" % ", ".join(missing))
    if extra:
        errors.append("dependency record carries extra keys: %s" % ", ".join(extra))
    if errors:
        return errors

    if record["dependency_record_version"] != constants.DEPENDENCY_RECORD_VERSION:
        errors.append("dependency_record_version must be exactly 1")
    row = registry_row(record["dependency_code"])
    if row is None:
        return errors + ["dependency_code %r is not registered" % (record["dependency_code"],)]
    for key in (
        "dependency_class",
        "dependency_identity_binding",
        "retry_mode",
        "next_workflow_state",
        "user_action_code",
    ):
        if record[key] != row[key]:
            errors.append(
                "%s must be %r for code %s, not %r"
                % (key, row[key], record["dependency_code"], record[key])
            )
    predicate = record["unlock_predicate"]
    if not isinstance(predicate, dict) or set(predicate) != {"predicate_kind", "params"}:
        errors.append("unlock_predicate must be {predicate_kind, params}")
    elif predicate["predicate_kind"] != row["predicate_kind"]:
        errors.append(
            "unlock_predicate.predicate_kind must be %r for code %s"
            % (row["predicate_kind"], record["dependency_code"])
        )
    elif not isinstance(predicate["params"], dict):
        errors.append("unlock_predicate.params must be a bounded object")
    else:
        unknown = sorted(set(predicate["params"]) - constants.UNLOCK_PREDICATE_PARAM_KEYS)
        if unknown:
            errors.append("unlock_predicate.params may not contain %s" % ", ".join(unknown))

    binding = record["dependency_identity_binding"]
    episode = record["provider_availability_episode_identity"]
    request = record["provider_request_identity"]
    if binding == "work_item_bound" and (episode is not None or request is not None):
        errors.append("work_item_bound requires both optional identity inputs null")
    if binding == "episode_bound" and (episode is None or request is not None):
        errors.append(
            "episode_bound requires a non-null episode identity and a null request identity"
        )
    if binding == "provider_request_bound" and (episode is None or request is None):
        errors.append("provider_request_bound requires both identity inputs non-null")

    if record["resource_kind"] not in constants.RESOURCE_KINDS:
        errors.append("resource_kind is not controlled")
    if record["resource_identity"] in ("", None):
        errors.append("resource_identity must be a controlled registry value")
    if record["phase_evidence_condition"] not in constants.PHASE_EVIDENCE_CONDITIONS:
        errors.append("phase_evidence_condition is not controlled")
    return errors


def identity_of(record):
    return dependency_identity(record)


def fail_closed_record(work_item_identity, capability_record_identity, evidence_event_seq=None):
    """Section 11.8d -- the single fail-closed row."""
    params = {}
    if evidence_event_seq is not None:
        params["evidence_event_seq"] = evidence_event_seq
    return build_record(
        FAIL_CLOSED_CODE,
        capability_record_identity,
        work_item_identity,
        resource_kind="capability_registry",
        predicate_params=params,
        durable_record_placement="supervisor_operation_completed",
        plain_language_dependency=(
            "N.H saw something it could not classify safely, so it stopped and "
            "changed nothing."
        ),
    )


# ---------------------------------------------------------------------------
# Section 4.2d -- the first-carrier / later-reference replay derivation.
# ---------------------------------------------------------------------------
def _slot(event):
    return {
        "dependency_record": event.get("dependency_record"),
        "dependency_identity": event.get("dependency_identity"),
        "dependency_carrier_event_seq": event.get("dependency_carrier_event_seq"),
        "dependency_occurrence_ordinal": event.get("dependency_occurrence_ordinal"),
    }


def occurrences(events):
    """Every authenticated occurrence, in event-sequence order."""
    found = []
    for event in events:
        identity = event.get("dependency_identity")
        if identity is None:
            continue
        found.append((event["event_seq"], event, _slot(event)))
    return found


def carrier_event_seq(events, identity):
    """The unique event_seq of the single carrier for ``identity``, or None."""
    for event in events:
        if event.get("dependency_identity") != identity:
            continue
        if event.get("dependency_record") is not None:
            return event["event_seq"]
    return None


def carrier_event_seq_of(occurrence_event):
    """The total function of Section 4.2d, defined for both shapes."""
    if occurrence_event.get("dependency_record") is not None:
        return occurrence_event["event_seq"]
    return occurrence_event.get("dependency_carrier_event_seq")


def occurrence_ordinal(events, identity, event_seq):
    """``1 + `` the number of earlier occurrences of the same identity."""
    count = 0
    for event in events:
        if event["event_seq"] >= event_seq:
            continue
        if event.get("dependency_identity") == identity:
            count += 1
    return count + 1


def next_slot(events, record, identity):
    """Build the carrier slot where no carrier exists, else the reference slot."""
    existing = carrier_event_seq(events, identity)
    if existing is None:
        return {
            "dependency_record": record,
            "dependency_identity": identity,
            "dependency_carrier_event_seq": None,
            "dependency_occurrence_ordinal": 1,
        }
    ordinal = 1 + sum(1 for e in events if e.get("dependency_identity") == identity)
    return {
        "dependency_record": None,
        "dependency_identity": identity,
        "dependency_carrier_event_seq": existing,
        "dependency_occurrence_ordinal": ordinal,
    }


def reference_slot(events, identity):
    """Build a reference slot only; used by the three reference-only rows."""
    existing = carrier_event_seq(events, identity)
    if existing is None:
        raise DependencyError(
            "a reference-only row has no carrier to reference for %s" % identity
        )
    ordinal = 1 + sum(1 for e in events if e.get("dependency_identity") == identity)
    return {
        "dependency_record": None,
        "dependency_identity": identity,
        "dependency_carrier_event_seq": existing,
        "dependency_occurrence_ordinal": ordinal,
    }


def replay_assertions(events):
    """Every Section 4.2d replay assertion.  Returns a list of failure strings."""
    from .schema import dependency_slot_shape

    failures = []
    carriers = {}
    ordinals = {}
    for event in events:
        shape = dependency_slot_shape(event)
        if shape == "contradiction":
            failures.append(
                "event %s carries a DEPENDENCY_SLOT that is none of the three "
                "literal shapes" % event.get("event_seq")
            )
            continue
        if shape == "none":
            continue
        identity = event["dependency_identity"]
        if shape == "carrier":
            if identity in carriers:
                failures.append(
                    "a second carrier exists for %s at event %s"
                    % (identity, event["event_seq"])
                )
            else:
                carriers[identity] = event
            recomputed = None
            try:
                recomputed = dependency_identity(event["dependency_record"])
            except Exception as exc:  # noqa: BLE001 - reported, never raised on
                failures.append(
                    "carrier at event %s cannot re-derive its identity: %s"
                    % (event["event_seq"], exc)
                )
            if recomputed is not None and recomputed != identity:
                failures.append(
                    "carrier at event %s records %s but its record derives %s"
                    % (event["event_seq"], identity, recomputed)
                )
            record = event["dependency_record"]
            if isinstance(record, dict) and record.get("work_item_identity") != event.get(
                "work_item_identity"
            ):
                failures.append(
                    "carrier at event %s records a record of another work item"
                    % event["event_seq"]
                )
        else:
            carrier = carriers.get(identity)
            if carrier is None:
                failures.append(
                    "event %s references a carrier that does not exist (or is later) "
                    "for %s" % (event["event_seq"], identity)
                )
            else:
                if event["dependency_carrier_event_seq"] != carrier["event_seq"]:
                    failures.append(
                        "event %s names %s as the carrier of %s but the carrier is %s"
                        % (
                            event["event_seq"],
                            event["dependency_carrier_event_seq"],
                            identity,
                            carrier["event_seq"],
                        )
                    )
                if event["dependency_carrier_event_seq"] >= event["event_seq"]:
                    failures.append(
                        "event %s makes a forward reference" % event["event_seq"]
                    )
                if carrier.get("work_item_identity") != event.get("work_item_identity"):
                    failures.append(
                        "event %s references a carrier of another work item"
                        % event["event_seq"]
                    )
        seen = ordinals.get(identity, 0) + 1
        ordinals[identity] = seen
        if event["dependency_occurrence_ordinal"] != seen:
            failures.append(
                "event %s records ordinal %s but its derived ordinal is %d"
                % (
                    event["event_seq"],
                    event["dependency_occurrence_ordinal"],
                    seen,
                )
            )
    return failures


def record_object_appears_once(events):
    """The one global uniqueness rule about the record object."""
    counts = {}
    for event in events:
        if event.get("dependency_record") is None:
            continue
        identity = event.get("dependency_identity")
        counts[identity] = counts.get(identity, 0) + 1
    return sorted(identity for identity, count in counts.items() if count > 1)

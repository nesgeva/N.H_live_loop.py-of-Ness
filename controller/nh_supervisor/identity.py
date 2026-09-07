#!/usr/bin/env python3
"""Every derived identity of Section 4.3, plus the Section 4.4 work-item rule.

No identity in this module reads model prose, a clock, an attempt counter, a
dispatch serial where the section excludes it, an occurrence ordinal, or a raw
provider error.  Each function takes exactly the keys its domain declares and
refuses anything else, so an implementation cannot drift by adding an input.
"""

from __future__ import annotations

from . import constants
from .canonical import (
    digest_of,
    is_hex64,
    is_prefixed_identity,
    is_real_int,
    prefixed,
)


class IdentityError(ValueError):
    """A derived identity could not be constructed from the supplied inputs."""


def _exact(obj, keys, domain):
    """Return ``obj`` restricted to ``keys``; refuse missing or extra keys."""
    if not isinstance(obj, dict):
        raise IdentityError("%s inputs must be an object" % domain)
    missing = sorted(set(keys) - set(obj))
    extra = sorted(set(obj) - set(keys))
    if missing:
        raise IdentityError("%s is missing inputs: %s" % (domain, ", ".join(missing)))
    if extra:
        raise IdentityError(
            "%s carries inputs it does not define: %s" % (domain, ", ".join(extra))
        )
    return {key: obj[key] for key in keys}


# ---------------------------------------------------------------------------
# Section 4.4 -- the twenty-one work-item keys, in their declared order.
# ---------------------------------------------------------------------------
WORK_ITEM_KEYS = (
    "work_item_kind",
    "controller_executable_identity",
    "package_scope_id",
    "source_binding_sha256",
    "candidate_path",
    "candidate_sha256",
    "candidate_bytes",
    "blocking_finding_refs",
    "audit_identity",
    "checkpoint_identity",
    "diagnosis_event_sha256",
    "diagnosis_strategy_sha256",
    "strategy_novelty_key",
    "correction_specification_sha256",
    "target_candidate_path",
    "authorized_next_lifetime_round",
    "authorized_batch_number",
    "authorized_round_in_batch",
    "routed_signal_refs",
    "validation_set_id",
    "piece3_standing_sha256",
)

# Fields the object EXCLUDES; validation rejects any attempt to include them.
WORK_ITEM_FORBIDDEN_KEYS = frozenset(
    (
        "root_cause_plain",
        "plain_language_problem",
        "plain_language_impact",
        "strategy_identity_material",
        "proposed_addition_names",
        "recorded_at",
        "scheduled_at_epoch",
        "first_failure_epoch",
        "next_eligible_epoch",
        "attempt",
        "provider_dispatch_serial",
        "probe_serial",
        "provider_availability_episode_identity",
        "provider_availability_episode_generation",
        "semantic_unlock_generation",
        "dependency_occurrence_ordinal",
        "heartbeat_at_epoch",
        "expires_at_epoch",
        "authenticated_event_seq",
        "authenticated_tail_sha256",
        "controller_report_sha256",
        "provider_outcome_facts",
        "probe_observation_facts",
        "provider_returncode",
    )
)

_R = "R"
_0 = "0"
_EMPTY = "[]"
_NONEMPTY = "N"

# Section 4.4 required-field matrix.  Keys 1-7 are always required non-null.
# The eight rows are keyed by (work_item_kind, variant); ``variant`` is None for
# kinds with exactly one row.
WORK_ITEM_MATRIX = {
    ("design_audit", None): {
        "blocking_finding_refs": _EMPTY,
        "audit_identity": _0,
        "checkpoint_identity": _0,
        "diagnosis_event_sha256": _0,
        "diagnosis_strategy_sha256": _0,
        "strategy_novelty_key": _0,
        "correction_specification_sha256": _0,
        "target_candidate_path": _0,
        "authorized_next_lifetime_round": _0,
        "authorized_batch_number": _0,
        "authorized_round_in_batch": _0,
        "routed_signal_refs": _EMPTY,
        "validation_set_id": _0,
        "piece3_standing_sha256": _0,
    },
    # Section 14 Phase A step A2 -- the acceptance-explanation preparation work
    # item.  Its shape is exactly the design audit's: one candidate, no
    # findings, no target path, no authority, no round authorisation.  It
    # carries no audit identity BECAUSE the audit it feeds does not exist yet,
    # which is the whole point of preparing the prose before that audit runs.
    ("acceptance_explanation_content", None): {
        "blocking_finding_refs": _EMPTY,
        "audit_identity": _0,
        "checkpoint_identity": _0,
        "diagnosis_event_sha256": _0,
        "diagnosis_strategy_sha256": _0,
        "strategy_novelty_key": _0,
        "correction_specification_sha256": _0,
        "target_candidate_path": _0,
        "authorized_next_lifetime_round": _0,
        "authorized_batch_number": _0,
        "authorized_round_in_batch": _0,
        "routed_signal_refs": _EMPTY,
        "validation_set_id": _0,
        "piece3_standing_sha256": _0,
    },
    ("correction_specification", None): {
        "blocking_finding_refs": _NONEMPTY,
        "audit_identity": _R,
        "checkpoint_identity": _0,
        "diagnosis_event_sha256": _0,
        "diagnosis_strategy_sha256": _0,
        "strategy_novelty_key": _0,
        "correction_specification_sha256": _0,
        "target_candidate_path": _R,
        "authorized_next_lifetime_round": _R,
        "authorized_batch_number": _R,
        "authorized_round_in_batch": _R,
        "routed_signal_refs": _EMPTY,
        "validation_set_id": _0,
        "piece3_standing_sha256": _0,
    },
    # correction_apply under diagnosis authority, exhausted_batch trigger.
    ("correction_apply", "diagnosis_exhausted_batch"): {
        "blocking_finding_refs": _NONEMPTY,
        "audit_identity": _R,
        "checkpoint_identity": _R,
        "diagnosis_event_sha256": _R,
        "diagnosis_strategy_sha256": _R,
        "strategy_novelty_key": _R,
        "correction_specification_sha256": _R,
        "target_candidate_path": _R,
        "authorized_next_lifetime_round": _R,
        "authorized_batch_number": _R,
        "authorized_round_in_batch": _R,
        "routed_signal_refs": _EMPTY,
        "validation_set_id": _0,
        "piece3_standing_sha256": _0,
    },
    # correction_apply under diagnosis authority, no_progress trigger.
    ("correction_apply", "diagnosis_no_progress"): {
        "blocking_finding_refs": _NONEMPTY,
        "audit_identity": _R,
        "checkpoint_identity": _0,
        "diagnosis_event_sha256": _R,
        "diagnosis_strategy_sha256": _R,
        "strategy_novelty_key": _R,
        "correction_specification_sha256": _R,
        "target_candidate_path": _R,
        "authorized_next_lifetime_round": _R,
        "authorized_batch_number": _R,
        "authorized_round_in_batch": _R,
        "routed_signal_refs": _EMPTY,
        "validation_set_id": _0,
        "piece3_standing_sha256": _0,
    },
    # correction_apply under the ordinary fresh-GPT path (Section 9.6).
    ("correction_apply", "ordinary_specification"): {
        "blocking_finding_refs": _NONEMPTY,
        "audit_identity": _R,
        "checkpoint_identity": _0,
        "diagnosis_event_sha256": _0,
        "diagnosis_strategy_sha256": _0,
        "strategy_novelty_key": _R,
        "correction_specification_sha256": _R,
        "target_candidate_path": _R,
        "authorized_next_lifetime_round": _R,
        "authorized_batch_number": _R,
        "authorized_round_in_batch": _R,
        "routed_signal_refs": _EMPTY,
        "validation_set_id": _0,
        "piece3_standing_sha256": _0,
    },
    ("correction_diagnosis", "exhausted_batch"): {
        "blocking_finding_refs": _NONEMPTY,
        "audit_identity": _R,
        "checkpoint_identity": _R,
        "diagnosis_event_sha256": _0,
        "diagnosis_strategy_sha256": _0,
        "strategy_novelty_key": _0,
        "correction_specification_sha256": _0,
        "target_candidate_path": _0,
        "authorized_next_lifetime_round": _0,
        "authorized_batch_number": _0,
        "authorized_round_in_batch": _0,
        "routed_signal_refs": _EMPTY,
        "validation_set_id": _0,
        "piece3_standing_sha256": _0,
    },
    ("correction_diagnosis", "no_progress"): {
        "blocking_finding_refs": _NONEMPTY,
        "audit_identity": _R,
        "checkpoint_identity": _0,
        "diagnosis_event_sha256": _0,
        "diagnosis_strategy_sha256": _0,
        "strategy_novelty_key": _0,
        "correction_specification_sha256": _0,
        "target_candidate_path": _0,
        "authorized_next_lifetime_round": _0,
        "authorized_batch_number": _0,
        "authorized_round_in_batch": _0,
        "routed_signal_refs": _EMPTY,
        "validation_set_id": _0,
        "piece3_standing_sha256": _0,
    },
    ("change_explanation_review", None): {
        "blocking_finding_refs": _NONEMPTY,
        "audit_identity": _R,
        "checkpoint_identity": _0,
        "diagnosis_event_sha256": _0,
        "diagnosis_strategy_sha256": _0,
        "strategy_novelty_key": _0,
        "correction_specification_sha256": _R,
        "target_candidate_path": _0,
        "authorized_next_lifetime_round": _0,
        "authorized_batch_number": _0,
        "authorized_round_in_batch": _0,
        "routed_signal_refs": _EMPTY,
        "validation_set_id": _0,
        "piece3_standing_sha256": _0,
    },
    ("question_validation", None): {
        "blocking_finding_refs": _EMPTY,
        "audit_identity": _0,
        "checkpoint_identity": _0,
        "diagnosis_event_sha256": _0,
        "diagnosis_strategy_sha256": _0,
        "strategy_novelty_key": _0,
        "correction_specification_sha256": _0,
        "target_candidate_path": _0,
        "authorized_next_lifetime_round": _0,
        "authorized_batch_number": _0,
        "authorized_round_in_batch": _0,
        "routed_signal_refs": _NONEMPTY,
        "validation_set_id": _R,
        "piece3_standing_sha256": _R,
    },
    ("coverage_review", None): {
        "blocking_finding_refs": _EMPTY,
        "audit_identity": _0,
        "checkpoint_identity": _0,
        "diagnosis_event_sha256": _0,
        "diagnosis_strategy_sha256": _0,
        "strategy_novelty_key": _0,
        "correction_specification_sha256": _0,
        "target_candidate_path": _0,
        "authorized_next_lifetime_round": _0,
        "authorized_batch_number": _0,
        "authorized_round_in_batch": _0,
        "routed_signal_refs": _NONEMPTY,
        "validation_set_id": _R,
        "piece3_standing_sha256": _R,
    },
    # -----------------------------------------------------------------------
    # v1_8 section 24.6a -- SIX added rows, and none lost.  The two installed
    # Piece-3 rows above are preserved byte-identically; because those kinds
    # now have several rows, ``variant=None`` no longer auto-resolves for them
    # and instead resolves through the explicit ``(kind, None)`` row -- which
    # is exactly the installed row, and is why the ordinary route is
    # unaffected.
    # -----------------------------------------------------------------------
    # v1_8 section 9.5d WIM-SELECTION.  Deliberately the design_audit /
    # acceptance_explanation_content shape: one bound candidate, no findings,
    # no target, no authority, no round authorisation.
    ("next_package_selection", None): {
        "blocking_finding_refs": _EMPTY,
        "audit_identity": _0,
        "checkpoint_identity": _0,
        "diagnosis_event_sha256": _0,
        "diagnosis_strategy_sha256": _0,
        "strategy_novelty_key": _0,
        "correction_specification_sha256": _0,
        "target_candidate_path": _0,
        "authorized_next_lifetime_round": _0,
        "authorized_batch_number": _0,
        "authorized_round_in_batch": _0,
        "routed_signal_refs": _EMPTY,
        "validation_set_id": _0,
        "piece3_standing_sha256": _0,
    },
    # v1_8 section 13.6c WIM-PREPARATION.  target_candidate_path is null
    # because T3 DERIVES the target; requiring it here would be circular.
    ("next_design_task_preparation", None): {
        "blocking_finding_refs": _EMPTY,
        "audit_identity": _0,
        "checkpoint_identity": _0,
        "diagnosis_event_sha256": _0,
        "diagnosis_strategy_sha256": _0,
        "strategy_novelty_key": _0,
        "correction_specification_sha256": _0,
        "target_candidate_path": _0,
        "authorized_next_lifetime_round": _0,
        "authorized_batch_number": _0,
        "authorized_round_in_batch": _0,
        "routed_signal_refs": _EMPTY,
        "validation_set_id": _0,
        "piece3_standing_sha256": _0,
    },
    # v1_8 section 14.5b WIM-INITIAL.  The ONLY new row with a required
    # target_candidate_path: T4 writes exactly one file at exactly the T3
    # controller-validated target, and INIT-ADMISSION I3 compares the produced
    # path against work_item["target_candidate_path"].
    ("initial_design", None): {
        "blocking_finding_refs": _EMPTY,
        "audit_identity": _0,
        "checkpoint_identity": _0,
        "diagnosis_event_sha256": _0,
        "diagnosis_strategy_sha256": _0,
        "strategy_novelty_key": _0,
        "correction_specification_sha256": _0,
        "target_candidate_path": _R,
        "authorized_next_lifetime_round": _0,
        "authorized_batch_number": _0,
        "authorized_round_in_batch": _0,
        "routed_signal_refs": _EMPTY,
        "validation_set_id": _0,
        "piece3_standing_sha256": _0,
    },
    # v1_8 section 12.3g A -- Q's FIRST question-validation, no routed signal.
    # routed_signal_refs is TRUTHFULLY empty and validation_set_id is
    # TRUTHFULLY null: neither is invented to satisfy this matrix
    # (PIECE3-NO-FAKE-FIELDS).
    ("question_validation", "first_package_validation_unrouted"): {
        "blocking_finding_refs": _EMPTY,
        "audit_identity": _0,
        "checkpoint_identity": _0,
        "diagnosis_event_sha256": _0,
        "diagnosis_strategy_sha256": _0,
        "strategy_novelty_key": _0,
        "correction_specification_sha256": _0,
        "target_candidate_path": _0,
        "authorized_next_lifetime_round": _0,
        "authorized_batch_number": _0,
        "authorized_round_in_batch": _0,
        "routed_signal_refs": _EMPTY,
        "validation_set_id": _0,
    },
    # v1_8 section 12.3g B -- Q's FIRST question-validation where a GENUINE
    # routed signal for scope_Q exists.  Identical to A except the real refs.
    # validation_set_id remains null: a routed signal does not create a prior
    # validation set.
    ("question_validation", "first_package_validation_routed"): {
        "blocking_finding_refs": _EMPTY,
        "audit_identity": _0,
        "checkpoint_identity": _0,
        "diagnosis_event_sha256": _0,
        "diagnosis_strategy_sha256": _0,
        "strategy_novelty_key": _0,
        "correction_specification_sha256": _0,
        "target_candidate_path": _0,
        "authorized_next_lifetime_round": _0,
        "authorized_batch_number": _0,
        "authorized_round_in_batch": _0,
        "routed_signal_refs": _NONEMPTY,
        "validation_set_id": _0,
        "piece3_standing_sha256": _R,
    },
    # A later page of an existing package validation set can truthfully have
    # no newly routed signals.  It is bound by the real validation_set_id.
    ("question_validation", "package_validation_continuation_unrouted"): {
        "blocking_finding_refs": _EMPTY,
        "audit_identity": _0,
        "checkpoint_identity": _0,
        "diagnosis_event_sha256": _0,
        "diagnosis_strategy_sha256": _0,
        "strategy_novelty_key": _0,
        "correction_specification_sha256": _0,
        "target_candidate_path": _0,
        "authorized_next_lifetime_round": _0,
        "authorized_batch_number": _0,
        "authorized_round_in_batch": _0,
        "routed_signal_refs": _EMPTY,
        "validation_set_id": _R,
        "piece3_standing_sha256": _R,
    },
    # v1_8 section 12.3g C -- Q's coverage review after its validation set
    # exists, with nothing routed.  validation_set_id is now REAL.
    ("coverage_review", "package_coverage_unrouted"): {
        "blocking_finding_refs": _EMPTY,
        "audit_identity": _0,
        "checkpoint_identity": _0,
        "diagnosis_event_sha256": _0,
        "diagnosis_strategy_sha256": _0,
        "strategy_novelty_key": _0,
        "correction_specification_sha256": _0,
        "target_candidate_path": _0,
        "authorized_next_lifetime_round": _0,
        "authorized_batch_number": _0,
        "authorized_round_in_batch": _0,
        "routed_signal_refs": _EMPTY,
        "validation_set_id": _R,
        "piece3_standing_sha256": _R,
    },
}

_ALWAYS_REQUIRED_WORK_ITEM_KEYS = (
    "work_item_kind",
    "controller_executable_identity",
    "package_scope_id",
    "source_binding_sha256",
    "candidate_path",
    "candidate_sha256",
    "candidate_bytes",
)


def work_item_matrix_rows(work_item_kind):
    return [key for key in WORK_ITEM_MATRIX if key[0] == work_item_kind]


def check_work_item_object(obj, variant=None):
    """Validate one work-item object against the Section 4.4 matrix.

    Returns the list of failure strings; empty means the object is admissible.
    Any combination not in the matrix fails closed.
    """
    errors = []
    if not isinstance(obj, dict):
        return ["work item object is not an object"]

    forbidden = sorted(WORK_ITEM_FORBIDDEN_KEYS & set(obj))
    if forbidden:
        errors.append(
            "work item object carries excluded inputs: %s" % ", ".join(forbidden)
        )

    missing = sorted(set(WORK_ITEM_KEYS) - set(obj))
    extra = sorted(set(obj) - set(WORK_ITEM_KEYS))
    if missing:
        errors.append("work item object is missing keys: %s" % ", ".join(missing))
    if extra:
        errors.append("work item object carries extra keys: %s" % ", ".join(extra))
    if errors:
        return errors

    kind = obj["work_item_kind"]
    if kind not in constants.WORK_ITEM_KIND_SET:
        return ["work_item_kind %r is not one of the controlled kinds" % (kind,)]

    for key in _ALWAYS_REQUIRED_WORK_ITEM_KEYS:
        if obj[key] is None:
            errors.append("work item key %s must be non-null for every kind" % key)
    if not is_hex64(obj["controller_executable_identity"]):
        errors.append("controller_executable_identity must be a 64-hex digest")
    if not is_hex64(obj["source_binding_sha256"]):
        errors.append("source_binding_sha256 must be a 64-hex digest")
    if not is_hex64(obj["candidate_sha256"]):
        errors.append("candidate_sha256 must be a 64-hex digest")
    if not is_real_int(obj["candidate_bytes"]) or obj["candidate_bytes"] < 0:
        errors.append("candidate_bytes must be a non-negative integer")

    rows = work_item_matrix_rows(kind)
    if variant is None and len(rows) == 1:
        variant = rows[0][1]
    row = WORK_ITEM_MATRIX.get((kind, variant))
    if row is None:
        return errors + [
            "no Section 4.4 matrix row exists for (%s, %s): the combination fails "
            "closed" % (kind, variant)
        ]

    for key, requirement in row.items():
        value = obj[key]
        if requirement == _0:
            if value is not None:
                errors.append("%s must be null for %s/%s" % (key, kind, variant))
        elif requirement == _R:
            if value is None:
                errors.append("%s must be non-null for %s/%s" % (key, kind, variant))
        elif requirement == _EMPTY:
            if value != []:
                errors.append("%s must be the empty list for %s/%s" % (key, kind, variant))
        elif requirement == _NONEMPTY:
            if not isinstance(value, list) or not value:
                errors.append(
                    "%s must be a non-empty sorted unique list for %s/%s"
                    % (key, kind, variant)
                )
            elif value != sorted(set(value)):
                errors.append("%s must be sorted and unique" % key)

    if row.get("authorized_round_in_batch") == _R:
        value = obj["authorized_round_in_batch"]
        if not is_real_int(value) or not (1 <= value <= constants.CORRECTION_BATCH_SIZE):
            errors.append("authorized_round_in_batch must be an integer 1..5")
    for key in ("authorized_next_lifetime_round", "authorized_batch_number"):
        if row.get(key) == _R:
            value = obj[key]
            if not is_real_int(value) or value < 1:
                errors.append("%s must be a positive integer" % key)

    if row.get("strategy_novelty_key") == _R and not is_prefixed_identity(
        "strategy_novelty_key", obj["strategy_novelty_key"]
    ):
        errors.append("strategy_novelty_key must be nov_<64 hex>")
    return errors


def work_item_identity(obj, variant=None):
    checks = check_work_item_object(obj, variant)
    if checks:
        raise IdentityError("; ".join(checks))
    material = _exact(obj, WORK_ITEM_KEYS, "NH_WORK_ITEM_ID_V1")
    return prefixed("work_item_identity", digest_of("NH_WORK_ITEM_ID_V1", material))


# ---------------------------------------------------------------------------
# Section 4.3 -- the remaining derived identities.  Each declares its exact key
# set once; ``_exact`` refuses any other input.
# ---------------------------------------------------------------------------
_DOMAINS = {
    "audit_identity": (
        "NH_MECHANICAL_AUDIT_ID_V1",
        (
            "package_scope_id",
            "source_binding_sha256",
            "settled_decision_binding_sha256",
            "candidate_path",
            "candidate_sha256",
            "candidate_bytes",
            "correction_round_lifetime",
            "correction_batch_number",
            "correction_round_in_batch",
            "audit_prompt_sha256",
            "required_files_sha256",
        ),
        None,
    ),
    "checkpoint_identity": (
        "NH_CORRECTION_BATCH_CHECKPOINT_ID_V1",
        (
            "package_scope_id",
            "source_binding_sha256",
            "candidate_path",
            "candidate_sha256",
            "candidate_bytes",
            "correction_round_lifetime",
            "correction_batch_number",
            "audit_identity",
            "blocking_finding_refs",
            "checkpoint_outcome",
        ),
        None,
    ),
    "no_progress_identity": (
        "NH_MECHANICAL_NO_PROGRESS_ID_V1",
        (
            "package_scope_id",
            "source_binding_sha256",
            "candidate_path",
            "candidate_sha256",
            "blocking_finding_refs",
            "correction_specification_sha256",
            "diagnosis_strategy_sha256",
            "strategy_novelty_key",
            "claude_result_facts_sha256",
        ),
        None,
    ),
    "semantic_scope_key": (
        "NH_SEMANTIC_SCOPE_KEY_V1",
        (
            "package_scope_id",
            "source_binding_sha256",
            "candidate_path",
            "candidate_sha256",
            "candidate_bytes",
            "blocking_finding_refs",
            "semantic_unlock_generation",
        ),
        "semantic_scope_key",
    ),
    "scope_exhaustion_identity": (
        "NH_SEMANTIC_SCOPE_EXHAUSTION_ID_V1",
        (
            "package_scope_id",
            "source_binding_sha256",
            "exhausted_semantic_scope_key",
            "exhausted_semantic_unlock_generation",
            "exhaustion_trigger_kind",
            "work_item_identity",
        ),
        "scope_exhaustion_identity",
    ),
    "diagnosis_trigger_identity": (
        "NH_DIAGNOSIS_TRIGGER_ID_V1",
        (
            "diagnosis_trigger_type",
            "diagnosis_trigger_event_seq",
            "trigger_event_sha256",
            "package_scope_id",
            "source_binding_sha256",
            "candidate_path",
            "candidate_sha256",
            "blocking_finding_refs",
        ),
        None,
    ),
    "diagnosis_input_sha256": (
        "NH_CORRECTION_DIAGNOSIS_INPUT_V1",
        (
            "diagnosis_trigger_identity",
            "package_scope_id",
            "source_binding_sha256",
            "candidate_path",
            "candidate_sha256",
            "candidate_bytes",
            "blocking_finding_refs",
            "prior_strategy_digests",
            "exhausted_novelty_keys",
            "source_manifest_sha256",
        ),
        None,
    ),
    "diagnosis_strategy_sha256": (
        "NH_CORRECTION_STRATEGY_RECORD_ID_V1",
        (
            "diagnosis_trigger_identity",
            "root_cause_plain",
            "strategy_identity_material",
            "mechanical_correction_specification",
            "normalized_correction_operations",
            "proposed_addition_names",
            "candidate_path",
            "candidate_sha256",
            "blocking_finding_refs",
            "source_binding_sha256",
        ),
        None,
    ),
    "specification_identity": (
        "NH_CORRECTION_SPECIFICATION_RECORD_ID_V1",
        (
            "package_scope_id",
            "source_binding_sha256",
            "candidate_path",
            "candidate_sha256",
            "candidate_bytes",
            "audit_identity",
            "blocking_finding_refs",
            "mechanical_correction_specification",
            "normalized_correction_operations",
            "work_item_identity",
            "provider_request_identity",
        ),
        None,
    ),
    "strategy_novelty_key": (
        "NH_STRATEGY_NOVELTY_KEY_V1",
        (
            "package_scope_id",
            "source_binding_sha256",
            "candidate_path",
            "candidate_sha256",
            "candidate_bytes",
            "blocking_finding_refs",
            "normalized_correction_operations",
        ),
        "strategy_novelty_key",
    ),
    "canonical_addition_slot_id": (
        "NH_CANONICAL_ADDITION_SLOT_V1",
        (
            "operation_kind",
            "target_kind",
            "target_anchor_identifier",
            "target_field",
            "new_value_identifier",
            "blocker_ref",
        ),
        "canonical_addition_slot_id",
    ),
    "consumption_identity": (
        "NH_DIAGNOSIS_CONSUMPTION_ID_V1",
        (
            "diagnosis_event_seq",
            "diagnosis_event_sha256",
            "diagnosis_strategy_sha256",
            "strategy_novelty_key",
            "package_scope_id",
            "source_binding_sha256",
            "candidate_path",
            "candidate_sha256",
            "target_candidate_path",
            "authorized_next_lifetime_round",
            "authorized_batch_number",
            "authorized_round_in_batch",
        ),
        None,
    ),
    "provider_availability_episode_identity": (
        "NH_PROVIDER_AVAILABILITY_EPISODE_ID_V1",
        (
            "work_item_identity",
            "provider_kind",
            "provider_endpoint_identity",
            "episode_generation",
        ),
        "provider_availability_episode_identity",
    ),
    "provider_request_identity": (
        "NH_PROVIDER_REQUEST_ID_V1",
        (
            "provider_kind",
            "provider_endpoint_identity",
            "work_item_identity",
            "provider_availability_episode_identity",
            "provider_dispatch_serial",
            "prompt_material_sha256",
            "required_inputs_sha256",
        ),
        "provider_request_identity",
    ),
    "availability_probe_identity": (
        "NH_AVAILABILITY_PROBE_ID_V1",
        (
            "provider_kind",
            "provider_endpoint_identity",
            "work_item_identity",
            "closed_episode_identity",
            "probe_serial",
            "probe_command_identity",
            "probe_input_sha256",
        ),
        "availability_probe_identity",
    ),
    "result_custody_identity": (
        "NH_PROVIDER_RESULT_CUSTODY_ID_V1",
        (
            "provider_kind",
            "provider_request_identity",
            "work_item_identity",
            "result_origin",
            "result_location_kind",
            "result_location_id",
            "result_object_name",
            "result_byte_length",
            "result_sha256",
            "result_schema_id",
            "result_schema_version",
        ),
        "result_custody_identity",
    ),
    "dependency_identity": (
        "NH_DEPENDENCY_ID_V1",
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
        ),
        "dependency_identity",
    ),
    "retry_series_key": (
        "NH_RETRY_SERIES_KEY_V1",
        (
            "controller_executable_identity",
            "package_scope_id",
            "source_binding_sha256",
            "candidate_path",
            "candidate_sha256",
            "candidate_bytes",
            "workflow_state",
            "next_command",
            "work_item_identity",
            "dependency_identity",
        ),
        "retry_series_key",
    ),
    "change_explanation_identity": (
        "NH_CHANGE_EXPLANATION_ID_V1",
        (
            "package_scope_id",
            "source_binding_sha256",
            "parent_candidate_path",
            "parent_candidate_sha256",
            "candidate_path",
            "candidate_sha256",
            "blocking_finding_refs",
            "correction_specification_sha256",
            "diff_sha256",
            "reviewer_result_sha256",
        ),
        None,
    ),
    "acceptance_explanation_identity": (
        "NH_ACCEPTANCE_EXPLANATION_ID_V1",
        (
            "package_scope_id",
            "source_binding_sha256",
            "candidate_path",
            "candidate_sha256",
            "candidate_bytes",
            "audit_identity",
            "pass_identity",
            "explanation_version",
            "explanation_digest",
        ),
        None,
    ),
    "ness_acceptance_identity": (
        "NH_NESS_ACCEPTANCE_ID_V1",
        (
            "package_scope_id",
            "source_binding_sha256",
            "candidate_path",
            "candidate_sha256",
            "candidate_bytes",
            "audit_identity",
            "pass_identity",
            "acceptance_scope_id",
        ),
        "ness_acceptance_identity",
    ),
    "ness_transition_choice": (
        "NH_NESS_TRANSITION_CHOICE_ID_V1",
        (
            "acceptance_event_sha256",
            "pre_choice_authenticated_tail_sha256",
            "ness_choice_exact",
            "package_scope_id",
            "selected_result_custody_identity",
            "postponed_package_scope_id",
            "postponed_evidence_event_sha256",
        ),
        "transition_choice_identity",
    ),
    "external_action_resolution": (
        "NH_EXTERNAL_ACTION_RESOLUTION_ID_V1",
        (
            "dependency_identity",
            "dependency_carrier_event_sha256",
            "provider_request_identity",
            "provider_terminal_event_sha256",
            "resource_identity",
            "user_action_code",
            "external_action_evidence_kind",
            "pre_action_authenticated_tail_sha256",
            "ness_action_exact",
        ),
        "external_action_resolution_identity",
    ),
    "interview_head_binding": (
        "NH_INTERVIEW_HEAD_BINDING_V1",
        (
            "v",
            "intent_generation",
            "intent_number",
            "intent_event_seq",
            "intent_event_sha256",
            "committed_event_seq",
            "committed_event_sha256",
            "head_auth_sha256",
        ),
        None,
    ),
    "pass_identity": (
        "NH_MECHANICAL_PASS_ID_V1",
        (
            "package_scope_id",
            "source_binding_sha256",
            "candidate_path",
            "candidate_sha256",
            "candidate_bytes",
            "audit_identity",
            "terminal_chain_sha256",
            "settled_decision_binding_sha256",
            "validation_set_id",
            "coverage_review_event_seq",
        ),
        None,
    ),
    "supervisor_operation_id": (
        "NH_SUPERVISOR_OPERATION_ID_V1",
        (
            "supervisor_command",
            "controller_executable_identity",
            "package_scope_id",
            "source_binding_sha256",
            "candidate_path",
            "candidate_sha256",
            "candidate_bytes",
            "work_item_identity",
            "pre_state_sha256",
            "input_envelope_sha256",
            "unlock_evidence_kind",
            "unlock_evidence_identity",
            "unlock_evidence_sha256",
        ),
        "supervisor_operation_id",
    ),
    "controller_executable_identity": (
        "NH_CONTROLLER_EXECUTABLE_ID_V1",
        (
            "controller_repo_relative_path",
            "controller_sha256",
            "controller_bytes",
            "journal_current_version",
            "supervisor_protocol_version",
        ),
        None,
    ),
}


def derive(name, inputs):
    """Derive one Section 4.3 identity by name from its exact input object."""
    try:
        domain, keys, prefix_name = _DOMAINS[name]
    except KeyError:
        raise IdentityError("no derived identity named %r" % (name,)) from None
    material = _exact(inputs, keys, domain)
    digest = digest_of(domain, material)
    if prefix_name is None:
        return digest
    return prefixed(prefix_name, digest)


def identity_input_keys(name):
    return _DOMAINS[name][1]


def identity_domain_label(name):
    return _DOMAINS[name][0]


# ---------------------------------------------------------------------------
# Section 11.6 -- the exclusion list, asserted rather than assumed.
# ---------------------------------------------------------------------------
RETRY_SERIES_EXCLUDED_INPUTS = frozenset(
    (
        "authenticated_event_seq",
        "authenticated_tail_sha256",
        "provider_dispatch_serial",
        "provider_request_identity",
        "provider_availability_episode_identity",
        "probe_serial",
        "availability_probe_identity",
        "semantic_unlock_generation",
        "scope_exhaustion_identity",
        "recorded_at",
        "scheduled_at_epoch",
        "first_failure_epoch",
        "next_eligible_epoch",
        "next_probe_eligible_epoch",
        "heartbeat_at_epoch",
        "expires_at_epoch",
        "run_id",
        "controller_report_sha256",
        "post_state_sha256",
        "result_custody_identity",
        "dependency_carrier_event_seq",
        "dependency_occurrence_ordinal",
        "provider_outcome_facts",
        "provider_error_signal_token",
        "provider_error_classification_row_id",
        "probe_observation_facts",
        "probe_signal_sources_applied",
        "probe_signal_class",
        "probe_signal_cross_check",
        "probe_classification_row_id",
        "audit_result_facts_sha256",
        "c11a_self_occurrence_carrier_event_seq",
        "c11a_self_occurrence_ordinal",
        "c11a_self_condition_satisfied",
        "unlock_evidence_kind",
        "unlock_evidence_identity",
        "unlock_evidence_sha256",
        "supervisor_operation_id",
        "input_envelope_sha256",
        "plain_language_dependency",
        "provider_error_text",
    )
)


def retry_series_key(inputs):
    """Derive ``rs_<64 hex>``, refusing every excluded input (Section 11.6)."""
    if not isinstance(inputs, dict):
        raise IdentityError("retry series inputs must be an object")
    intruders = sorted(RETRY_SERIES_EXCLUDED_INPUTS & set(inputs))
    if intruders:
        raise IdentityError(
            "retry_series_key may never take these inputs: %s" % ", ".join(intruders)
        )
    return derive("retry_series_key", inputs)


# Section 4.5a -- the dependency identity excludes the same evidence fields.
DEPENDENCY_IDENTITY_EXCLUDED_INPUTS = frozenset(
    (
        "observed_evidence_event_seq",
        "observed_evidence_sha256",
        "plain_language_dependency",
        "next_workflow_state",
        "durable_record_placement",
        "observed_symptom_code",
        "phase_evidence_condition",
        "dependency_carrier_event_seq",
        "dependency_occurrence_ordinal",
        "provider_outcome_facts",
        "probe_observation_facts",
        "user_action_code",
        "person_route_reason",
        "probe_serial",
        "availability_probe_identity",
        "semantic_unlock_generation",
    )
)

PLACEHOLDER_VALUES = frozenset(("unknown", "error", "unspecified", ""))


def dependency_identity(record):
    """Derive ``dep_<64 hex>`` over exactly the eleven Section 4.5a inputs."""
    if not isinstance(record, dict):
        raise IdentityError("dependency record must be an object")
    keys = identity_input_keys("dependency_identity")
    material = {}
    for key in keys:
        if key not in record:
            raise IdentityError("dependency record is missing %s" % key)
        material[key] = record[key]
    for key in (
        "dependency_class",
        "dependency_code",
        "dependency_identity_binding",
        "resource_kind",
        "resource_identity",
        "retry_mode",
    ):
        if material[key] in PLACEHOLDER_VALUES:
            raise IdentityError(
                "%s may never be the placeholder %r" % (key, material[key])
            )
    return derive("dependency_identity", material)


# ---------------------------------------------------------------------------
# Section 3 -- the counter formulas.
# ---------------------------------------------------------------------------
def batch_triple(correction_round_lifetime):
    """``(lifetime, batch_number, round_in_batch)`` -- Section 3."""
    if not is_real_int(correction_round_lifetime) or correction_round_lifetime < 0:
        raise IdentityError("correction_round_lifetime must be a non-negative integer")
    if correction_round_lifetime == 0:
        # The selected initial candidate is the unique round-zero tail and is
        # represented as the exact triple (0, 0, 0).
        return (0, 0, 0)
    size = constants.CORRECTION_BATCH_SIZE
    return (
        correction_round_lifetime,
        ((correction_round_lifetime - 1) // size) + 1,
        ((correction_round_lifetime - 1) % size) + 1,
    )


def triple_is_consistent(lifetime, batch_number, round_in_batch):
    return batch_triple(lifetime) == (lifetime, batch_number, round_in_batch)

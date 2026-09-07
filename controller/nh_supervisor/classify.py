#!/usr/bin/env python3
"""Sections 11.2b and 11.2c -- the two total, ordered, controller-owned classifiers.

No terminal kind and no probe outcome is ever chosen from prose, from a raw
error string, or by an implementation's judgement.  Both classifiers are pure
functions of one bounded facts object the controller assembled from what it
observed itself, plus the authenticated capability record.
"""

from __future__ import annotations

from . import constants
from .canonical import is_hex64, is_real_int, is_sorted_unique_list

# ---------------------------------------------------------------------------
# Section 11.2c -- PROVIDER_OUTCOME_FACTS_V1: sixteen keys, no others.
# ---------------------------------------------------------------------------
PROVIDER_OUTCOME_FACTS_KEYS = (
    "provider_outcome_facts_version",
    "transport_kind",
    "transport_outcome",
    "transmission_proved_absent",
    "returncode",
    "http_status_present",
    "http_status",
    "declared_content_length_present",
    "declared_content_length",
    "observed_body_byte_length",
    "endpoint_error_code_present",
    "endpoint_error_code_sha256",
    "retry_after_present",
    "retry_after_seconds",
    "provider_error_signal_token",
    "capability_record_sha256",
)


class FactsError(ValueError):
    """A bounded facts object was not of the declared shape."""


def check_provider_outcome_facts_shape(facts):
    errors = []
    if not isinstance(facts, dict):
        return ["provider_outcome_facts is not an object"]
    missing = sorted(set(PROVIDER_OUTCOME_FACTS_KEYS) - set(facts))
    extra = sorted(set(facts) - set(PROVIDER_OUTCOME_FACTS_KEYS))
    if missing:
        errors.append("provider_outcome_facts missing: %s" % ", ".join(missing))
    if extra:
        errors.append("provider_outcome_facts carries extra keys: %s" % ", ".join(extra))
    if errors:
        return errors
    if facts["provider_outcome_facts_version"] != 1:
        errors.append("provider_outcome_facts_version must be exactly 1")
    if facts["transport_kind"] not in constants.TRANSPORT_KINDS:
        errors.append("transport_kind is not controlled")
    if facts["transport_outcome"] not in constants.TRANSPORT_OUTCOMES:
        errors.append("transport_outcome is not controlled")
    if not isinstance(facts["transmission_proved_absent"], bool):
        errors.append("transmission_proved_absent must be a boolean")
    rc = facts["returncode"]
    if rc is not None and (not is_real_int(rc) or not (-256 <= rc <= 256)):
        errors.append("returncode must be an integer in [-256, 256] or null")
    status = facts["http_status"]
    if status is not None and (not is_real_int(status) or not (100 <= status <= 599)):
        errors.append("http_status must be an integer 100..599 or null")
    length = facts["observed_body_byte_length"]
    if (
        not is_real_int(length)
        or length < 0
        or length > constants.MAX_PROVIDER_RESULT_READ_LIMIT_BYTES
    ):
        errors.append("observed_body_byte_length is out of bound")
    declared = facts["declared_content_length"]
    if declared is not None and (not is_real_int(declared) or declared < 0):
        errors.append("declared_content_length must be a non-negative integer or null")
    digest = facts["endpoint_error_code_sha256"]
    if digest is not None and not is_hex64(digest):
        errors.append("endpoint_error_code_sha256 must be 64-hex or null")
    retry_after = facts["retry_after_seconds"]
    if retry_after is not None and (
        not is_real_int(retry_after)
        or not (0 <= retry_after <= constants.MAX_RETRY_AFTER_SECONDS)
    ):
        errors.append("retry_after_seconds is out of bound")
    if facts["provider_error_signal_token"] not in constants.PROVIDER_ERROR_SIGNAL_SET:
        errors.append("provider_error_signal_token is not a PROVIDER_ERROR_SIGNAL_V1 member")
    if not is_hex64(facts["capability_record_sha256"]):
        errors.append("capability_record_sha256 must be 64-hex")
    for key in (
        "http_status_present",
        "declared_content_length_present",
        "endpoint_error_code_present",
        "retry_after_present",
    ):
        if not isinstance(facts[key], bool):
            errors.append("%s must be a boolean" % key)
    return errors


def provider_consistency_violations(facts):
    """The fixed consistency predicate; any violation is row E13."""
    bad = []
    if facts["http_status_present"] != (facts["http_status"] is not None):
        bad.append("http_status_present disagrees with http_status")
    if facts["endpoint_error_code_present"] != (
        facts["endpoint_error_code_sha256"] is not None
    ):
        bad.append("endpoint_error_code_present disagrees with its digest")
    if facts["retry_after_present"] != (facts["retry_after_seconds"] is not None):
        bad.append("retry_after_present disagrees with retry_after_seconds")
    if facts["declared_content_length_present"] != (
        facts["declared_content_length"] is not None
    ):
        bad.append("declared_content_length_present disagrees with the length")
    if facts["transport_outcome"] != "completed" and facts["http_status"] is not None:
        bad.append("a non-completed transport carries an HTTP status")
    if facts["transport_kind"] == "in_process_https" and facts["returncode"] is not None:
        bad.append("in_process_https carries a returncode")
    if facts["transmission_proved_absent"] and (
        facts["transport_outcome"] not in constants.TRANSMISSION_ABSENT_OUTCOMES
    ):
        bad.append(
            "transmission_proved_absent is only provable for connect_failed, "
            "tls_failed, or process_spawn_failed"
        )
    if (
        facts["provider_error_signal_token"] != "none_observed"
        and facts["transport_outcome"] != "completed"
    ):
        bad.append("a mapped error signal requires a completed transport")
    return bad


def derive_provider_error_signal_token(facts_without_token, capability_record):
    """The four-step derivation of Section 11.2c.  Map first, defaults second."""
    signal_map = (capability_record or {}).get("provider_error_signal_map") or []
    if facts_without_token.get("endpoint_error_code_present"):
        digest = facts_without_token.get("endpoint_error_code_sha256")
        for entry in signal_map:
            if (
                entry.get("match_kind") == "endpoint_error_code_digest"
                and entry.get("match_value") == digest
            ):
                return entry["signal_token"]
    if facts_without_token.get("http_status_present"):
        status = facts_without_token.get("http_status")
        for entry in signal_map:
            if entry.get("match_kind") == "http_status" and entry.get("match_value") == status:
                return entry["signal_token"]
        default = constants.PROVIDER_ERROR_SIGNAL_DEFAULTS_V1.get(status)
        if default is not None:
            return default
    return "none_observed"


# The literal classifier rows, evaluated by ascending row number.
PROVIDER_CLASSIFIER_ROWS = (
    "E0",
    "E1",
    "E2",
    "E3",
    "E4",
    "E5",
    "E6",
    "E7",
    "E8",
    "E9",
    "E10",
    "E11",
    "E12",
    "E13",
)

PROVIDER_ROW_TERMINAL = {
    "E0": None,
    "E1": "provider_error_retryable",
    "E2": "result_oversize_uncustodied",
    "E3": None,
    "E4": None,
    "E5": "provider_error_retryable",
    "E6": None,
    "E7": "provider_error_retryable",
    "E8": "provider_error_terminal",
    "E9": "provider_error_terminal",
    "E10": "provider_error_terminal",
    "E11": "provider_error_terminal",
    "E12": None,
    "E13": None,
}

PROVIDER_ROW_DEPENDENCY_CODE = {
    "E1": "provider_transient_error_terminal_recorded",
    "E5": "provider_rate_limited_terminal_recorded",
    "E7": "provider_service_unavailable_terminal_recorded",
    "E8": "provider_non_transient_error_proved",
    "E9": "provider_credential_expired",
    "E10": "provider_account_unavailable",
    "E11": "provider_quota_exhausted",
}

PROVIDER_ROW_C_ROW = {
    "E1": "C7",
    "E5": "C34",
    "E7": "C35",
    "E8": "C8",
    "E9": "C36",
    "E10": "C37",
    "E11": "C38",
}

RETRYABLE_ROWS = frozenset(("E1", "E5", "E7"))
TERMINAL_ERROR_ROWS = frozenset(("E8", "E9", "E10", "E11"))
UNKNOWN_OUTCOME_ROWS = frozenset(("E3", "E4", "E6", "E12"))


def classify_provider_outcome(facts):
    """Return the exact row id.  Total, ordered, mutually exclusive."""
    shape = check_provider_outcome_facts_shape(facts)
    if shape:
        return "E13"
    if provider_consistency_violations(facts):
        return "E13"

    outcome = facts["transport_outcome"]
    token = facts["provider_error_signal_token"]
    status = facts["http_status"]
    returncode = facts["returncode"]

    # E0 -- the only row that custodies. A complete result must have been read
    # WITHIN the bound: where the endpoint declared a length above
    # MAX_PROVIDER_RESULT_BYTES the controller read no body at all (Section 11.2a
    # step 1), so no complete result exists and E0 cannot match.
    declared = facts["declared_content_length"]
    if (
        (
            (outcome == "completed" and (returncode is None or returncode == 0))
            or (outcome == "local_process_failed" and facts["observed_body_byte_length"] > 0)
        )
        and token == "none_observed"
        and (status is None or 200 <= status <= 299)
        and facts["observed_body_byte_length"] <= constants.MAX_PROVIDER_RESULT_BYTES
        and (declared is None or declared <= constants.MAX_PROVIDER_RESULT_BYTES)
    ):
        return "E0"
    # E1 -- proved non-transmission.
    if facts["transmission_proved_absent"]:
        return "E1"
    # E2 -- oversize.
    if outcome == "read_limit_exceeded" or (
        facts["declared_content_length"] is not None
        and facts["declared_content_length"] > constants.MAX_PROVIDER_RESULT_BYTES
    ):
        return "E2"
    if outcome == "timed_out":
        return "E3"
    if outcome == "stream_closed_early":
        return "E4"
    if token == "rate_limited":
        return "E5"
    if outcome == "process_killed":
        return "E6"
    if token in ("service_unavailable", "service_overloaded", "internal_provider_error"):
        return "E7"
    if outcome == "local_process_failed" or token in (
        "request_rejected_invalid", "request_too_large", "model_or_endpoint_absent"
    ):
        return "E8"
    if token in ("authentication_rejected", "authorization_revoked"):
        return "E9"
    if token in ("account_disabled", "payment_or_plan_required"):
        return "E10"
    if token == "quota_exhausted":
        return "E11"
    if (
        outcome == "completed"
        and token == "none_observed"
        and status is not None
        and (100 <= status <= 199 or 300 <= status <= 399)
    ):
        return "E12"
    return "E13"


# ---------------------------------------------------------------------------
# Section 11.2b -- PROBE_OBSERVATION_FACTS_V1: eighteen keys, no others.
# ---------------------------------------------------------------------------
PROBE_OBSERVATION_FACTS_KEYS = (
    "probe_observation_facts_version",
    "probe_transport_kind",
    "probe_transport_outcome",
    "probe_returncode",
    "probe_http_status_present",
    "probe_http_status",
    "probe_response_byte_length",
    "probe_response_schema_id",
    "probe_response_schema_valid",
    "probe_endpoint_signal_present",
    "probe_endpoint_signal_token",
    "probe_endpoint_response_code_present",
    "probe_endpoint_response_code_sha256",
    "probe_signal_sources_applied",
    "probe_signal_class",
    "probe_signal_cross_check",
    "probe_capability_record_sha256",
    "probe_command_identity",
)


def check_probe_facts_shape(facts):
    errors = []
    if not isinstance(facts, dict):
        return ["probe_observation_facts is not an object"]
    missing = sorted(set(PROBE_OBSERVATION_FACTS_KEYS) - set(facts))
    extra = sorted(set(facts) - set(PROBE_OBSERVATION_FACTS_KEYS))
    if missing:
        errors.append("probe_observation_facts missing: %s" % ", ".join(missing))
    if extra:
        errors.append("probe_observation_facts carries extra keys: %s" % ", ".join(extra))
    if errors:
        return errors
    if facts["probe_observation_facts_version"] != 1:
        errors.append("probe_observation_facts_version must be exactly 1")
    if facts["probe_transport_kind"] not in constants.TRANSPORT_KINDS:
        errors.append("probe_transport_kind is not controlled")
    if facts["probe_transport_outcome"] not in constants.TRANSPORT_OUTCOMES:
        errors.append("probe_transport_outcome is not controlled")
    rc = facts["probe_returncode"]
    if rc is not None and (not is_real_int(rc) or not (-256 <= rc <= 256)):
        errors.append("probe_returncode must be an integer in [-256, 256] or null")
    status = facts["probe_http_status"]
    if status is not None and (not is_real_int(status) or not (100 <= status <= 599)):
        errors.append("probe_http_status must be an integer 100..599 or null")
    length = facts["probe_response_byte_length"]
    if (
        not is_real_int(length)
        or length < 0
        or length > constants.MAX_PROBE_RESULT_READ_LIMIT_BYTES
    ):
        errors.append("probe_response_byte_length is out of bound")
    token = facts["probe_endpoint_signal_token"]
    if token is not None and token not in constants.PROBE_SIGNAL_SET:
        errors.append("probe_endpoint_signal_token is not a PROBE_SIGNAL_V1 member")
    digest = facts["probe_endpoint_response_code_sha256"]
    if digest is not None and not is_hex64(digest):
        errors.append("probe_endpoint_response_code_sha256 must be 64-hex or null")
    if not is_sorted_unique_list(facts["probe_signal_sources_applied"]):
        errors.append("probe_signal_sources_applied must be a sorted unique list")
    elif set(facts["probe_signal_sources_applied"]) - set(constants.PROBE_SIGNAL_SOURCE_NAMES):
        errors.append("probe_signal_sources_applied names an unknown source")
    if facts["probe_signal_cross_check"] not in constants.PROBE_SIGNAL_CROSS_CHECKS:
        errors.append("probe_signal_cross_check is not controlled")
    if facts["probe_signal_class"] is not None and facts["probe_signal_class"] not in set(
        constants.PROBE_SIGNAL_CLASS_V1.values()
    ):
        errors.append("probe_signal_class is not a PROBE_SIGNAL_CLASS_V1 member")
    if not is_hex64(facts["probe_capability_record_sha256"]):
        errors.append("probe_capability_record_sha256 must be 64-hex")
    for key in (
        "probe_http_status_present",
        "probe_response_schema_valid",
        "probe_endpoint_signal_present",
        "probe_endpoint_response_code_present",
    ):
        if not isinstance(facts[key], bool):
            errors.append("%s must be a boolean" % key)
    return errors


def derive_probe_signals(facts, capability_record):
    """All three sources, the map-derived token, the class, and the cross-check.

    Every applicable signal is derived; precedence decides only which token is
    recorded and never suppresses a source.
    """
    signal_map = (capability_record or {}).get("availability_probe_signal_map") or []
    sources = []
    classes = []
    map_error_token = None
    map_status_token = None

    if facts["probe_transport_outcome"] == "completed":
        if facts.get("probe_endpoint_response_code_present"):
            digest = facts.get("probe_endpoint_response_code_sha256")
            for entry in signal_map:
                if (
                    entry.get("match_kind") == "endpoint_error_code_digest"
                    and entry.get("match_value") == digest
                ):
                    map_error_token = entry["signal_token"]
                    break
            if map_error_token is not None:
                sources.append("endpoint_map_error_code")
                classes.append(constants.PROBE_SIGNAL_CLASS_V1[map_error_token])
        if facts.get("probe_http_status_present"):
            status = facts.get("probe_http_status")
            for entry in signal_map:
                if (
                    entry.get("match_kind") == "http_status"
                    and entry.get("match_value") == status
                ):
                    map_status_token = entry["signal_token"]
                    break
            if map_status_token is not None:
                sources.append("endpoint_map_http_status")
                classes.append(constants.PROBE_SIGNAL_CLASS_V1[map_status_token])
            default = constants.probe_signal_http_default(status)
            if default is not None:
                sources.append("fixed_http_default")
                classes.append(constants.PROBE_SIGNAL_CLASS_V1[default])

    sources = sorted(set(sources))
    token = map_error_token if map_error_token is not None else map_status_token

    if not sources:
        cross_check = "no_source"
        signal_class = None
    elif len(sources) == 1:
        cross_check = "single_source"
        signal_class = classes[0]
    elif len(set(classes)) == 1:
        cross_check = "agreed"
        signal_class = classes[0]
    else:
        cross_check = "disagreed"
        signal_class = None

    return {
        "probe_signal_sources_applied": sources,
        "probe_signal_class": signal_class,
        "probe_signal_cross_check": cross_check,
        "probe_endpoint_signal_token": token,
        "probe_endpoint_signal_present": token is not None,
    }


def probe_consistency_violations(facts, capability_record):
    """The fixed consistency predicate; any violation is row P0."""
    bad = []
    if facts["probe_http_status_present"] != (facts["probe_http_status"] is not None):
        bad.append("probe_http_status_present disagrees with probe_http_status")
    if facts["probe_endpoint_signal_present"] != (
        facts["probe_endpoint_signal_token"] is not None
    ):
        bad.append("probe_endpoint_signal_present disagrees with its token")
    if facts["probe_endpoint_response_code_present"] != (
        facts["probe_endpoint_response_code_sha256"] is not None
    ):
        bad.append("probe_endpoint_response_code_present disagrees with its digest")
    completed = facts["probe_transport_outcome"] == "completed"
    if completed and facts["probe_response_byte_length"] > (
        constants.MAX_PROBE_RESULT_READ_LIMIT_BYTES
    ):
        bad.append("a completed probe read beyond the bounded read limit")
    if not completed and facts["probe_http_status"] is not None:
        bad.append("a non-completed probe carries an HTTP status")
    if not completed and (
        facts["probe_endpoint_response_code_sha256"] is not None
        or facts["probe_signal_sources_applied"]
    ):
        bad.append("a non-completed probe carries endpoint signal material")
    if facts["probe_response_schema_valid"] and (
        facts["probe_response_schema_id"] is None or not completed
    ):
        bad.append("a valid probe schema requires an id and a completed transport")
    if facts["probe_transport_kind"] == "in_process_https" and (
        facts["probe_returncode"] is not None
    ):
        bad.append("in_process_https carries a probe returncode")

    derived = derive_probe_signals(facts, capability_record)
    if facts["probe_signal_sources_applied"] != derived["probe_signal_sources_applied"]:
        bad.append("probe_signal_sources_applied does not re-derive")
    if facts["probe_signal_cross_check"] != derived["probe_signal_cross_check"]:
        bad.append("probe_signal_cross_check does not re-derive")
    if facts["probe_signal_class"] != derived["probe_signal_class"]:
        bad.append("probe_signal_class does not re-derive")
    if facts["probe_endpoint_signal_token"] != derived["probe_endpoint_signal_token"]:
        bad.append("probe_endpoint_signal_token does not re-derive")
    if facts["probe_signal_cross_check"] == "disagreed":
        bad.append("two applicable authenticated probe signals imply different classes")
    return bad


PROBE_ROW_OUTCOME = {
    "P0": "facts_unclassifiable",
    "P1": "succeeded",
    "P2": "unsupported",
    "P3": "failed",
    "P4": "failed",
    "P5": "failed",
    "P6": "failed",
    "P7": "failed",
    "P8": "facts_unclassifiable",
}


def classify_probe_observation(facts, capability_record):
    """Return the exact probe classifier row id.  P0 is evaluated first."""
    shape = check_probe_facts_shape(facts)
    if shape:
        return "P0"
    if probe_consistency_violations(facts, capability_record):
        return "P0"

    outcome = facts["probe_transport_outcome"]
    token = facts["probe_endpoint_signal_token"]
    status = facts["probe_http_status"]
    returncode = facts["probe_returncode"]
    completed = outcome == "completed"

    if (
        completed
        and facts["probe_response_schema_valid"]
        and (status is None or 200 <= status <= 299)
        and (returncode is None or returncode == 0)
        and (token is None or token == "available")
    ):
        return "P1"
    if completed and (
        token == "probe_unsupported_by_endpoint" or status in (404, 405, 501)
    ):
        return "P2"
    if completed and (
        token in ("unauthorized", "quota_exhausted") or status in (401, 402, 403)
    ):
        return "P3"
    if completed and (
        token == "unavailable" or status in (408, 429, 500, 502, 503, 504, 529)
    ):
        return "P4"
    if completed and (
        not facts["probe_response_schema_valid"]
        or (returncode is not None and returncode != 0)
    ):
        return "P5"
    if outcome == "read_limit_exceeded":
        return "P6"
    if outcome in (
        "connect_failed",
        "tls_failed",
        "timed_out",
        "process_spawn_failed",
        "process_killed",
        "stream_closed_early",
    ):
        return "P7"
    return "P8"

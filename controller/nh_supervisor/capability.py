#!/usr/bin/env python3
"""Sections 11.3 and 4.11b -- the provider-capability contract and the baseline.

No model may author, edit, widen, or supply any field of a capability record.
It is controller-owned configuration bound by digest, and an absent, malformed,
version-unknown, or digest-mismatched record IS the default record -- a valid
record for classification purposes, and permission for nothing.
"""

from __future__ import annotations

from . import constants
from .canonical import canonical_json, is_hex64, is_real_int, sha256_hex

CAPABILITY_RECORD_KEYS = (
    "provider_capability_record_version",
    "provider_endpoint_identity",
    "provider_kind",
    "idempotency_key_supported",
    "idempotency_key_field",
    "lookup_supported",
    "lookup_authority",
    "lookup_command_identity",
    "availability_probe_supported",
    "availability_probe_command_identity",
    "availability_probe_is_non_generative",
    "availability_probe_result_schema_id",
    "availability_probe_signal_map",
    "provider_error_signal_map",
    "signal_map_version",
    "duplicate_dispatch_harmless",
    "capability_source",
    "capability_record_sha256",
)

SIGNAL_MAP_ENTRY_KEYS = frozenset(("match_kind", "match_value", "signal_token"))


def record_digest(record):
    """SHA-256 over the record WITHOUT its own digest field."""
    bound = {
        key: value
        for key, value in record.items()
        if key != "capability_record_sha256"
    }
    return sha256_hex(canonical_json(bound))


def default_record(provider_kind, provider_endpoint_identity):
    """The Section 11.3 default record for every endpoint."""
    record = {
        "provider_capability_record_version": constants.CAPABILITY_RECORD_VERSION,
        "provider_endpoint_identity": provider_endpoint_identity,
        "provider_kind": provider_kind,
        "idempotency_key_supported": False,
        "idempotency_key_field": None,
        "lookup_supported": False,
        "lookup_authority": "none",
        "lookup_command_identity": None,
        "availability_probe_supported": False,
        "availability_probe_command_identity": None,
        "availability_probe_is_non_generative": False,
        "availability_probe_result_schema_id": None,
        "availability_probe_signal_map": [],
        "provider_error_signal_map": [],
        "signal_map_version": 1,
        "duplicate_dispatch_harmless": False,
        "capability_source": "none",
    }
    record["capability_record_sha256"] = record_digest(record)
    return record


def _signal_map_ok(entries, token_set):
    if not isinstance(entries, list):
        return False
    if len(entries) > constants.MAX_PROVIDER_ERROR_SIGNAL_MAP_ENTRIES:
        return False
    seen = set()
    for entry in entries:
        if not isinstance(entry, dict) or set(entry) != SIGNAL_MAP_ENTRY_KEYS:
            return False
        kind = entry["match_kind"]
        value = entry["match_value"]
        if kind not in constants.SIGNAL_MATCH_KINDS:
            return False
        if kind == "http_status":
            if not is_real_int(value) or not (100 <= value <= 599):
                return False
        else:
            if not is_hex64(value):
                return False
        if entry["signal_token"] not in token_set:
            return False
        key = (kind, value)
        if key in seen:
            return False
        seen.add(key)
    sort_key = lambda item: (item["match_kind"], str(item["match_value"]))
    return entries == sorted(entries, key=sort_key)


def record_is_valid(record):
    """True only when the record is fully valid under Section 11.3."""
    if not isinstance(record, dict):
        return False
    if set(record) != set(CAPABILITY_RECORD_KEYS):
        return False
    if record["provider_capability_record_version"] != constants.CAPABILITY_RECORD_VERSION:
        return False
    if record["provider_kind"] not in constants.PROVIDER_KIND_SET:
        return False
    if not isinstance(record["provider_endpoint_identity"], str) or not record[
        "provider_endpoint_identity"
    ]:
        return False
    if record["lookup_authority"] not in constants.LOOKUP_AUTHORITIES:
        return False
    if record["capability_source"] not in constants.CAPABILITY_SOURCES:
        return False
    if record["signal_map_version"] != 1:
        return False
    for key in (
        "idempotency_key_supported",
        "lookup_supported",
        "availability_probe_supported",
        "availability_probe_is_non_generative",
        "duplicate_dispatch_harmless",
    ):
        if not isinstance(record[key], bool):
            return False
    if not _signal_map_ok(record["provider_error_signal_map"], constants.PROVIDER_ERROR_SIGNAL_SET):
        return False
    if not _signal_map_ok(record["availability_probe_signal_map"], constants.PROBE_SIGNAL_SET):
        return False
    if record["lookup_authority"] == "authoritative":
        if not record["lookup_supported"] or record["capability_source"] == "none":
            return False
    if record["availability_probe_supported"]:
        if not record["availability_probe_is_non_generative"]:
            return False
        if not record["availability_probe_command_identity"]:
            return False
        if not record["availability_probe_result_schema_id"]:
            return False
        if record["capability_source"] == "none":
            return False
    if record["duplicate_dispatch_harmless"]:
        # Settable only by a separately accepted Ness decision record bound by
        # digest.  No such record exists for this package.
        return False
    if not is_hex64(record.get("capability_record_sha256") or ""):
        return False
    if record["capability_record_sha256"] != record_digest(record):
        return False
    return True


def resolve_record(candidate, provider_kind, provider_endpoint_identity):
    """Return ``(record, was_default)`` applying the Section 11.3 default rule."""
    if candidate is not None and record_is_valid(candidate):
        if (
            candidate["provider_kind"] == provider_kind
            and candidate["provider_endpoint_identity"] == provider_endpoint_identity
        ):
            return candidate, False
    return default_record(provider_kind, provider_endpoint_identity), True


def capability_record_identity(provider_kind, provider_endpoint_identity):
    """The controlled capability record identity for one bound pair."""
    return "cap_" + sha256_hex(
        canonical_json(
            ["NH_PROVIDER_CAPABILITY_RECORD_ID_V1", [provider_kind, provider_endpoint_identity]]
        )
    )


# ---------------------------------------------------------------------------
# Section 4.11b -- CAPABILITY_BASELINE_V1 and its literal selection rule.
# ---------------------------------------------------------------------------
BASELINE_ENTRY_KEYS = (
    "provider_kind",
    "provider_endpoint_identity",
    "provider_capability_record_identity",
    "provider_capability_record_sha256",
    "provider_capability_source",
)


def build_capability_snapshot(endpoint_binding, registry_reader):
    """``NH_CAPABILITY_BASELINE_SELECTION_V1`` -- the literal selection rule.

    1. take the seven provider_kind values in their fixed declared order;
    2. resolve the endpoint the registry binds to that kind for this package;
       a kind with no bound endpoint contributes no entry;
    3. read the authenticated capability record for each resolved pair, applying
       the Section 11.3 default rule -- the default record still contributes an
       entry with capability_source = "none";
    4. deduplicate exact pairs, sort, and reject beyond the bound.

    The rule reads only the registry and the package binding.  It never consults
    a provider, never runs a probe, and never invokes a model.
    """
    entries = []
    seen = set()
    for provider_kind in constants.PROVIDER_KINDS:
        endpoint = endpoint_binding.get(provider_kind)
        if endpoint is None:
            continue
        pair = (provider_kind, endpoint)
        if pair in seen:
            continue
        seen.add(pair)
        record, _default = resolve_record(
            registry_reader(provider_kind, endpoint), provider_kind, endpoint
        )
        entries.append(
            {
                "provider_kind": provider_kind,
                "provider_endpoint_identity": endpoint,
                "provider_capability_record_identity": capability_record_identity(
                    provider_kind, endpoint
                ),
                "provider_capability_record_sha256": record["capability_record_sha256"],
                "provider_capability_source": record["capability_source"],
            }
        )
    entries.sort(
        key=lambda entry: canonical_json(
            [entry["provider_kind"], entry["provider_endpoint_identity"]]
        ).encode("utf-8")
    )
    if len(entries) > constants.MAX_CAPABILITY_REGISTRY_ENTRIES:
        raise ValueError(
            "the capability snapshot exceeds MAX_CAPABILITY_REGISTRY_ENTRIES"
        )
    return entries


def snapshot_digest(snapshot):
    return sha256_hex(canonical_json(["NH_CAPABILITY_BASELINE_V1", snapshot]))


def compare_snapshots(baseline, observed):
    """``NH_SEMANTIC_UNLOCK_CAPABILITY_COMPARISON_V1`` -- the literal comparison."""
    by_pair = {
        (entry["provider_kind"], entry["provider_endpoint_identity"]): entry
        for entry in baseline
    }
    changed = []
    for entry in observed:
        pair = (entry["provider_kind"], entry["provider_endpoint_identity"])
        base = by_pair.get(pair)
        if base is None:
            changed.append((entry, None))
        elif base["provider_capability_record_sha256"] != entry[
            "provider_capability_record_sha256"
        ]:
            changed.append((entry, base))
    qualifying = [
        (entry, base)
        for entry, base in changed
        if entry["provider_capability_source"] != "none"
    ]
    selected = qualifying[0] if qualifying else None
    return {
        "changed_entries": [entry for entry, _base in changed],
        "changed_entry_count": len(changed),
        "qualifying_entries": [entry for entry, _base in qualifying],
        "selected_entry": None if selected is None else selected[0],
        "selected_baseline_entry": None if selected is None else selected[1],
    }

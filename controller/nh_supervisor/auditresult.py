#!/usr/bin/env python3
"""Section 5.1 -- ``NH_DESIGN_AUDIT_RESULT_V2``, its usability checks, and the
one injective extra-key path encoding.

Every check here is a pure function of structural fields, literal values,
declared enums, list order, list membership, and key names -- and of nothing
else.  No prose byte is parsed, scanned, pattern-matched, keyword-searched,
tokenised, embedded, or digested.
"""

from __future__ import annotations

import hashlib

from . import constants
from .canonical import canonical_json, is_hex64, is_real_int, sha256_hex

RESULT_SCHEMA_ID = "NH_DESIGN_AUDIT_RESULT_V2"
RESULT_SCHEMA_VERSION = 1

# The complete required declared top-level key set.
DECLARED_TOP_LEVEL_KEYS = (
    "result_schema_id",
    "result_schema_version",
    "whole_check_complete",
    "candidate_path",
    "candidate_sha256",
    "candidate_bytes",
    "reviewed_source_paths",
    "verdict",
    "highest_severity",
    "findings",
    "mechanical_blocker_refs",
    "review_required_blocker_refs",
    # When mechanical blockers exist, this same independent audit supplies the
    # complete Claude correction instructions.  These three fields replace the
    # old second Codex correction-specification call.
    "mechanical_correction_specification",
    "normalized_correction_operations",
    "proposed_addition_names",
    "bundle_placement",
    "controlled_component_id",
    "register_id",
    "implementation_authorized",
    "acceptance_claimed",
    "adoption_claimed",
    "installation_claimed",
    "authority_claimed",
    "plain_language_problem",
    "plain_language_impact",
    "summary",
)

DECLARED_FINDING_KEYS = (
    "finding_ref",
    "severity",
    "route",
    "blocking",
    "sections",
    "source_paths",
    "proof",
    "smallest_correction",
)

# The prose fields.  Their CONTENTS are never read by U1-U8.
PROSE_FIELDS = ("summary", "plain_language_problem", "plain_language_impact")
FINDING_PROSE_FIELDS = ("proof", "smallest_correction")

SEVERITIES = ("NONE", "ADVISORY", "IMPORTANT", "CRITICAL")
FINDING_SEVERITIES = ("ADVISORY", "IMPORTANT", "CRITICAL")
ROUTES = ("claude_mechanical", "ness_decision", "user_action", "none")

NH_DESIGN_AUDIT_FORBIDDEN_KEYS_V1 = frozenset(
    (
        "accept", "accepted", "acceptance",
        "adopt", "adopted", "adoption",
        "approve", "approved", "approval",
        "authority", "authorized", "authorization",
        "permission", "permitted", "grant",
        "install", "installed", "installation",
        "deploy", "deployed", "deployment",
        "promote", "promotion", "merge",
        "commit", "push", "governance_change",
        "master_change", "map_integration", "register_entry",
        "component_id", "placement", "bundle",
        "pass_granted", "ready_for_acceptance", "implementation_permitted",
    )
)

FINDING_REF_ALLOWED = set("abcdefghijklmnopqrstuvwxyz0123456789_-")

MAX_EXTRA_KEY_PATHS = 64
MAX_ENCODED_PATH_BYTES = 256
PROJECTION_PREFIX_BYTES = 190


def finding_ref_ok(value):
    if not isinstance(value, str) or not value.startswith("f_"):
        return False
    tail = value[2:]
    if not 1 <= len(tail) <= 64:
        return False
    return all(char in FINDING_REF_ALLOWED for char in tail)


# ---------------------------------------------------------------------------
# NH_AUDIT_EXTRA_KEY_PATH_V1 -- the one injective, self-delimiting encoding.
# ---------------------------------------------------------------------------
def encode_root():
    return b"R"


def encode_object_key_segment(key):
    """``"K" + byte length + ":" + exact UTF-8 key bytes``.

    Defined only over parsed key strings of Unicode scalar values; a surrogate
    key never reaches here (Section 4.1, Section 9.7 B6d).
    """
    raw = key.encode("utf-8")
    return b"K" + str(len(raw)).encode("ascii") + b":" + raw


def encode_array_index_segment(index):
    """``"I" + canonical decimal index + ":"`` -- no sign, no leading zero."""
    return b"I" + str(index).encode("ascii") + b":"


def decode_path(encoded):
    """Decode one complete encoded path back into its position steps.

    The decoder exists so injectivity is demonstrable rather than asserted.
    """
    if not encoded.startswith(b"R"):
        raise ValueError("an encoded path must begin with R")
    steps = []
    pos = 1
    while pos < len(encoded):
        tag = encoded[pos : pos + 1]
        pos += 1
        colon = encoded.index(b":", pos)
        digits = encoded[pos:colon].decode("ascii")
        if digits != str(int(digits)) or digits.startswith("+") or digits.startswith("-"):
            raise ValueError("non-canonical decimal in encoded path")
        pos = colon + 1
        if tag == b"K":
            length = int(digits)
            raw = encoded[pos : pos + length]
            if len(raw) != length:
                raise ValueError("truncated key segment")
            pos += length
            steps.append(("key", raw.decode("utf-8")))
        elif tag == b"I":
            steps.append(("index", int(digits)))
        else:
            raise ValueError("unknown segment tag %r" % (tag,))
    return steps


def project_path(encoded):
    """The one deterministic projection of an overlength complete encoded path."""
    if len(encoded) <= MAX_ENCODED_PATH_BYTES:
        return encoded.decode("latin-1"), False
    digest = hashlib.sha256(encoded).hexdigest()
    projected = (
        b"~" + encoded[:PROJECTION_PREFIX_BYTES] + b"~" + digest.encode("ascii")
    )
    return projected.decode("latin-1"), True


def _walk_extra_keys(value, declared_top, declared_finding):
    """Yield ``(encoded_path_bytes, key_name)`` for every extra key occurrence.

    Iterative and depth-safe, visiting each parsed object key occurrence at most
    once.  The traversal itself is not capped at 64; only the reporting
    projection is bounded.
    """
    found = []
    stack = [(value, encode_root(), "root")]
    while stack:
        current, prefix, context = stack.pop()
        if isinstance(current, dict):
            if context == "root":
                declared = declared_top
            elif context == "finding":
                declared = declared_finding
            else:
                declared = frozenset()
            for key in sorted(current):
                segment = prefix + encode_object_key_segment(key)
                if key not in declared:
                    found.append((segment, key))
                child = current[key]
                # These three declared fields are separately shape-checked here
                # and semantically normalized against the controller registry
                # before they can be recorded.  Their inner objects are payload,
                # not undeclared audit-result fields.
                if context == "root" and key in {
                    "mechanical_correction_specification",
                    "normalized_correction_operations",
                    "proposed_addition_names",
                }:
                    continue
                if context == "root" and key == "findings" and isinstance(child, list):
                    child_context = "findings_list"
                else:
                    child_context = "other"
                stack.append((child, segment, child_context))
        elif isinstance(current, list):
            for index, item in enumerate(current):
                segment = prefix + encode_array_index_segment(index)
                child_context = "finding" if context == "findings_list" else "other"
                stack.append((item, segment, child_context))
    return found


def derive_structural_facts(result):
    """``extra_key_paths``, ``forbidden_keys_present`` and the overlength count."""
    occurrences = _walk_extra_keys(
        result, frozenset(DECLARED_TOP_LEVEL_KEYS), frozenset(DECLARED_FINDING_KEYS)
    )
    complete_paths = sorted(path for path, _name in occurrences)
    kept = complete_paths[:MAX_EXTRA_KEY_PATHS]
    projected = []
    overlength = 0
    for path in kept:
        entry, was_projected = project_path(path)
        projected.append(entry)
        if was_projected:
            overlength += 1
    forbidden = sorted(
        {name for _path, name in occurrences if name in NH_DESIGN_AUDIT_FORBIDDEN_KEYS_V1}
    )
    return {
        "extra_key_paths": projected,
        "extra_key_path_count": len(projected),
        "extra_key_path_overlength_count": overlength,
        "forbidden_keys_present": forbidden,
        "complete_encoded_paths": complete_paths,
        "extra_key_occurrence_count": len(occurrences),
    }


def projection_has_repeated_entry(structural):
    """The one genuine post-projection digest collision (Section 5.1 P-1)."""
    entries = structural["extra_key_paths"]
    return len(entries) != len(set(entries))


# ---------------------------------------------------------------------------
# Schema validity (Section 5.1 rules 1-6).  Extra keys never affect it.
# ---------------------------------------------------------------------------
def check_schema_valid(result):
    """Return the list of declared-field violations; empty means schema-valid."""
    errors = []
    if not isinstance(result, dict):
        return ["the audit result is not a JSON object"]

    missing = sorted(set(DECLARED_TOP_LEVEL_KEYS) - set(result))
    if missing:
        errors.append("missing declared keys: %s" % ", ".join(missing))
        return errors

    if result["result_schema_id"] != RESULT_SCHEMA_ID:
        errors.append("result_schema_id must be the literal %s" % RESULT_SCHEMA_ID)
    if result["result_schema_version"] != RESULT_SCHEMA_VERSION:
        errors.append("result_schema_version must be exactly 1")
    if not isinstance(result["whole_check_complete"], bool):
        errors.append("whole_check_complete must be a boolean")
    path = result["candidate_path"]
    if not isinstance(path, str) or len(path.encode("utf-8")) > 256:
        errors.append("candidate_path must be a controlled path string <= 256 bytes")
    if not is_hex64(result["candidate_sha256"]):
        errors.append("candidate_sha256 must be 64-hex")
    if (
        not is_real_int(result["candidate_bytes"])
        or result["candidate_bytes"] <= 0
        or result["candidate_bytes"] > constants.MAX_CANDIDATE_BYTES
    ):
        errors.append("candidate_bytes must be a positive integer within bound")

    for key in ("reviewed_source_paths", "mechanical_blocker_refs", "review_required_blocker_refs"):
        value = result[key]
        if not isinstance(value, list) or len(value) > 64:
            errors.append("%s must be a list of at most 64 entries" % key)
            continue
        if any(not isinstance(item, str) for item in value):
            errors.append("%s must contain strings only" % key)
        elif value != sorted(set(value)):
            errors.append("%s must be sorted and unique" % key)
        if key == "reviewed_source_paths":
            for item in value:
                if isinstance(item, str) and len(item.encode("utf-8")) > 256:
                    errors.append("reviewed_source_paths entry exceeds 256 bytes")

    specification = result["mechanical_correction_specification"]
    operations = result["normalized_correction_operations"]
    proposed_names = result["proposed_addition_names"]
    mechanical_refs = result["mechanical_blocker_refs"]
    if mechanical_refs:
        if not isinstance(specification, dict) or not specification:
            errors.append(
                "mechanical_correction_specification must be a non-empty object "
                "when mechanical blockers exist"
            )
        elif len(canonical_json(specification)) > constants.MAX_PROVIDER_RESULT_BYTES:
            errors.append("mechanical_correction_specification exceeds its bound")
        if not isinstance(operations, list) or not operations:
            errors.append(
                "normalized_correction_operations must be a non-empty list "
                "when mechanical blockers exist"
            )
        elif len(operations) > constants.MAX_NORMALIZED_OPERATIONS:
            errors.append("normalized_correction_operations exceeds its bound")
        if not isinstance(proposed_names, list):
            errors.append(
                "proposed_addition_names must be a list when mechanical blockers exist"
            )
        elif len(proposed_names) > constants.MAX_PROPOSED_ADDITION_NAMES:
            errors.append("proposed_addition_names exceeds its bound")
    elif any(item is not None for item in (specification, operations, proposed_names)):
        errors.append(
            "correction specification fields must all be null when no mechanical "
            "blockers exist"
        )

    if result["verdict"] not in ("PASS", "BLOCKED"):
        errors.append('verdict must be exactly "PASS" or "BLOCKED"')
    if result["highest_severity"] not in SEVERITIES:
        errors.append("highest_severity must be a declared member")

    findings = result["findings"]
    if not isinstance(findings, list) or len(findings) > 64:
        errors.append("findings must be a list of at most 64 FINDING objects")
    else:
        refs = []
        for index, finding in enumerate(findings):
            label = "finding %d" % index
            if not isinstance(finding, dict):
                errors.append("%s is not an object" % label)
                continue
            gone = sorted(set(DECLARED_FINDING_KEYS) - set(finding))
            if gone:
                errors.append("%s missing declared keys: %s" % (label, ", ".join(gone)))
                continue
            if not finding_ref_ok(finding["finding_ref"]):
                errors.append("%s finding_ref does not match the controlled pattern" % label)
            else:
                refs.append(finding["finding_ref"])
            if finding["severity"] not in FINDING_SEVERITIES:
                errors.append("%s severity is not a declared member" % label)
            if finding["route"] not in ROUTES:
                errors.append("%s route is not a declared member" % label)
            if not isinstance(finding["blocking"], bool):
                errors.append("%s blocking must be a boolean" % label)
            for key, bound in (("sections", 32), ("source_paths", 32)):
                value = finding[key]
                if not isinstance(value, list) or len(value) > bound:
                    errors.append("%s %s must be a list of at most %d" % (label, key, bound))
                elif any(not isinstance(item, str) for item in value):
                    errors.append("%s %s must contain strings only" % (label, key))
                elif value != sorted(set(value)):
                    errors.append("%s %s must be sorted and unique" % (label, key))
            proof = finding["proof"]
            if not isinstance(proof, list) or len(proof) > 8:
                errors.append("%s proof must be a list of at most 8 items" % label)
            elif any(
                not isinstance(item, str) or len(item.encode("utf-8")) > 1024
                for item in proof
            ):
                errors.append("%s proof items must be bounded text" % label)
            correction = finding["smallest_correction"]
            if correction is not None and (
                not isinstance(correction, str)
                or len(correction.encode("utf-8")) > 1024
            ):
                errors.append("%s smallest_correction must be bounded text or null" % label)
        if len(refs) != len(set(refs)):
            errors.append("findings must be unique by finding_ref")
        if refs != sorted(refs):
            errors.append("findings must be sorted by finding_ref")

    if result["bundle_placement"] != "UNRESOLVED":
        errors.append('bundle_placement must be exactly the literal "UNRESOLVED"')
    if result["controlled_component_id"] is not None:
        errors.append("controlled_component_id must be exactly null")
    if result["register_id"] is not None:
        errors.append("register_id must be exactly null")
    for key in (
        "implementation_authorized",
        "acceptance_claimed",
        "adoption_claimed",
        "installation_claimed",
        "authority_claimed",
    ):
        if result[key] is not False:
            errors.append("%s must be exactly the literal boolean false" % key)

    for key, bound in (
        ("plain_language_problem", 1024),
        ("plain_language_impact", 1024),
        ("summary", 2048),
    ):
        value = result[key]
        if value is not None and (
            not isinstance(value, str) or len(value.encode("utf-8")) > bound
        ):
            errors.append("%s must be bounded text or null" % key)
    return errors


# ---------------------------------------------------------------------------
# The eight literal usability checks.
# ---------------------------------------------------------------------------
def evaluate_usability(result, bound_candidate, allowed_source_paths, structural=None):
    """Return ``(failed_check_ids, structural_facts)``.

    ``bound_candidate`` is ``{candidate_path, candidate_sha256, candidate_bytes}``
    -- the controller's OWN recorded values for the design_audit work item.
    ``allowed_source_paths`` is the controller's bounded inventory of required
    real source paths and authenticated candidate paths of this chain.
    """
    if structural is None:
        structural = derive_structural_facts(result)
    failed = []

    # U1
    u1_ok = (
        result["candidate_path"] == bound_candidate["candidate_path"]
        and result["candidate_sha256"] == bound_candidate["candidate_sha256"]
        and result["candidate_bytes"] == bound_candidate["candidate_bytes"]
    )
    if u1_ok:
        other_paths = set(result["reviewed_source_paths"])
        for finding in result["findings"]:
            other_paths |= set(finding["source_paths"])
        stray = {
            path
            for path in other_paths
            if path == bound_candidate["candidate_path"]
        }
        # No OTHER candidate path, digest, byte length, or chain position may
        # appear anywhere in the declared structure.  The bound candidate itself
        # is permitted, so only foreign candidate paths are stray.
        foreign = {
            path
            for path in other_paths - stray
            if path.endswith("_CANDIDATE.md")
        }
        if foreign:
            u1_ok = False
    if not u1_ok:
        failed.append("U1")

    # U2
    verdict = result["verdict"]
    severity = result["highest_severity"]
    u2_ok = verdict in ("PASS", "BLOCKED") and severity in SEVERITIES
    if u2_ok and verdict == "PASS" and severity != "NONE":
        u2_ok = False
    if u2_ok and verdict == "BLOCKED" and severity not in ("IMPORTANT", "CRITICAL"):
        u2_ok = False
    if not u2_ok:
        failed.append("U2")

    # U3
    u3_ok = result["whole_check_complete"] is True
    if u3_ok and structural["extra_key_occurrence_count"] > MAX_EXTRA_KEY_PATHS:
        u3_ok = False
    if u3_ok and any(
        len(path) > MAX_ENCODED_PATH_BYTES for path in structural["complete_encoded_paths"]
    ):
        u3_ok = False
    if u3_ok and structural["extra_key_paths"]:
        u3_ok = False
    if not u3_ok:
        failed.append("U3")

    # U4
    findings = result["findings"]
    u4_ok = True
    if verdict == "BLOCKED" and not any(f["blocking"] for f in findings):
        u4_ok = False
    for finding in findings:
        if finding["blocking"]:
            if finding["severity"] not in ("IMPORTANT", "CRITICAL"):
                u4_ok = False
            if finding["route"] not in ROUTES:
                u4_ok = False
    refs = [f["finding_ref"] for f in findings]
    if len(refs) != len(set(refs)):
        u4_ok = False
    if not u4_ok:
        failed.append("U4")

    # U5
    blocking_refs = {f["finding_ref"] for f in findings if f["blocking"]}
    mech = result["mechanical_blocker_refs"]
    review = result["review_required_blocker_refs"]
    u5_ok = (
        set(mech) | set(review) == blocking_refs
        and not (set(mech) & set(review))
        and mech == sorted(set(mech))
        and review == sorted(set(review))
        and set(mech) | set(review) <= set(refs)
    )
    if not u5_ok:
        failed.append("U5")

    # U6
    allowed = set(allowed_source_paths)
    u6_paths = set(result["reviewed_source_paths"])
    for finding in findings:
        u6_paths |= set(finding["source_paths"])
    if not u6_paths <= allowed:
        failed.append("U6")

    # U7 -- the five literal structural checks.
    u7_failed = []
    if result["bundle_placement"] != "UNRESOLVED":
        u7_failed.append("U7.1")
    if result["controlled_component_id"] is not None:
        u7_failed.append("U7.2")
    if result["register_id"] is not None:
        u7_failed.append("U7.3")
    if not (
        result["implementation_authorized"] is False
        and result["acceptance_claimed"] is False
        and result["adoption_claimed"] is False
        and result["installation_claimed"] is False
        and result["authority_claimed"] is False
    ):
        u7_failed.append("U7.4")
    if structural["forbidden_keys_present"]:
        u7_failed.append("U7.5")
    if u7_failed:
        failed.append("U7")
        failed.extend(u7_failed)

    # U8
    if verdict == "PASS":
        if any(f["blocking"] for f in findings) or mech or review:
            failed.append("U8")

    return sorted(set(failed)), structural


_CLASS_BY_CHECK = {
    "U1": "audit_binding_mismatch",
    "U2": "audit_verdict_inconsistent",
    "U8": "audit_verdict_inconsistent",
    "U3": "audit_findings_incomplete",
    "U4": "audit_findings_incomplete",
    "U5": "audit_finding_refs_inconsistent",
    "U6": "audit_source_reference_invalid",
    "U7": "audit_authority_overreach",
}

_LOWEST_ORDER = ("U1", "U2", "U3", "U4", "U5", "U6", "U8")


def usability_failure_class(failed_check_ids):
    """U7 has absolute precedence; otherwise the lowest-numbered failed check."""
    if "U7" in failed_check_ids:
        return "audit_authority_overreach"
    for check in _LOWEST_ORDER:
        if check in failed_check_ids:
            return _CLASS_BY_CHECK[check]
    return None


def audit_result_facts_sha256(
    *,
    package_scope_id,
    source_binding_sha256,
    candidate_path,
    candidate_sha256,
    candidate_bytes,
    work_item_identity,
    provider_kind,
    provider_request_identity,
    result_custody_identity,
    result,
    structural,
    failed_check_ids,
    failure_class,
):
    """The digest of exactly the bounded controller-assembled fact object."""
    obj = {
        "package_scope_id": package_scope_id,
        "source_binding_sha256": source_binding_sha256,
        "candidate_path": candidate_path,
        "candidate_sha256": candidate_sha256,
        "candidate_bytes": candidate_bytes,
        "work_item_identity": work_item_identity,
        "provider_kind": provider_kind,
        "provider_request_identity": provider_request_identity,
        "result_custody_identity": result_custody_identity,
        "result_schema_id": result["result_schema_id"],
        "result_schema_version": result["result_schema_version"],
        "declared_verdict": result["verdict"],
        "declared_highest_severity": result["highest_severity"],
        "declared_finding_count": len(result["findings"]),
        "declared_mechanical_blocker_ref_count": len(result["mechanical_blocker_refs"]),
        "declared_review_required_blocker_ref_count": len(
            result["review_required_blocker_refs"]
        ),
        "declared_bundle_placement": result["bundle_placement"],
        "declared_controlled_component_id_is_null": result["controlled_component_id"]
        is None,
        "declared_register_id_is_null": result["register_id"] is None,
        "declared_authority_flag_values": [
            result["implementation_authorized"],
            result["acceptance_claimed"],
            result["adoption_claimed"],
            result["installation_claimed"],
            result["authority_claimed"],
        ],
        "forbidden_keys_present": structural["forbidden_keys_present"],
        "extra_key_path_count": structural["extra_key_path_count"],
        "extra_key_paths": structural["extra_key_paths"],
        "extra_key_path_overlength_count": structural["extra_key_path_overlength_count"],
        "failed_audit_check_ids": sorted(failed_check_ids),
        "audit_usability_failure_class": failure_class,
    }
    return sha256_hex(canonical_json(obj))


def unusable_row(failure_class, output_retries_used):
    """Section 5.1 -- the row and eligibility for one unusable audit result."""
    if failure_class == "audit_authority_overreach":
        return "C39", False, "SAFETY_HOLD"
    if output_retries_used < constants.MAX_PROVIDER_OUTPUT_RETRIES_PER_EPISODE:
        return "C40", True, "WAITING_RECOVERING"
    return "C41", False, "WAITING_RECOVERING"

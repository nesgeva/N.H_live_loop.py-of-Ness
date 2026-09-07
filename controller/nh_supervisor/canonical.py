#!/usr/bin/env python3
"""The one canonical encoding, its key rule, and the derived-identity helper.

Section 4.1 fixes the encoding: sorted keys, separators ``(',', ':')``,
``ensure_ascii=True``.  It also fixes one applicable rule about object *keys*
that is read wherever this specification says "canonical JSON", including every
parsed provider result: **every JSON object-key string must consist of Unicode
scalar values only.**  A lone surrogate escape denotes no Unicode scalar value,
has no UTF-8 encoding, and is therefore non-canonical here.
"""

from __future__ import annotations

import hashlib
import json

from . import constants


class DuplicateJsonKeyError(ValueError):
    """A parsed object carried the same key twice."""


class NonCanonicalKeyError(ValueError):
    """A parsed object-key string is not a Unicode scalar string (Section 4.1)."""


def canonical_json(value):
    """The installed encoding. One line, sorted keys, ASCII escapes."""
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def sha256_hex(text):
    if isinstance(text, bytes):
        return hashlib.sha256(text).hexdigest()
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def digest_of(domain, obj):
    """``SHA256(canonical_json([DOMAIN, OBJECT]))`` -- Section 4.3."""
    return sha256_hex(canonical_json([domain, obj]))


def prefixed(name, digest):
    """Apply the Section 4.3 ASCII prefix for one identity family."""
    prefix = constants.IDENTITY_PREFIXES.get(name, "")
    return prefix + digest


def is_hex64(value):
    if not isinstance(value, str) or len(value) != 64:
        return False
    return all(char in "0123456789abcdef" for char in value)


def is_prefixed_identity(name, value):
    prefix = constants.IDENTITY_PREFIXES.get(name)
    if prefix is None:
        return is_hex64(value)
    if not isinstance(value, str) or not value.startswith(prefix):
        return False
    return is_hex64(value[len(prefix) :])


def key_is_unicode_scalar_string(key):
    """True only when every code point of ``key`` is a Unicode scalar value.

    Python's ``json`` decoder maps a lone ``\\uD800``-``\\uDFFF`` escape to the
    corresponding surrogate code point.  Such a string has no UTF-8 encoding, so
    it denotes no scalar value and is non-canonical (Section 4.1, Section 5.1
    rules 1/3/6, Section 9.7 B6d).
    """
    if not isinstance(key, str):
        return False
    for char in key:
        if 0xD800 <= ord(char) <= 0xDFFF:
            return False
    return True


def _object_pairs_hook(pairs):
    seen = set()
    for key, _value in pairs:
        if key in seen:
            raise DuplicateJsonKeyError("duplicate JSON object key %r" % (key,))
        seen.add(key)
        if not key_is_unicode_scalar_string(key):
            raise NonCanonicalKeyError(
                "object key is not a Unicode scalar string: %r" % (key,)
            )
    return dict(pairs)


def strict_json_loads(text):
    """Parse with duplicate-key refusal AND the canonical key-string rule.

    The two refusals are separate: a duplicate key is malformed input, a
    surrogate key is non-canonical.  Both make the bytes not schema-valid at
    Section 9.7 B6d and route to ``result_invalid``/B6i.
    """
    if isinstance(text, bytes):
        text = text.decode("utf-8")
    return json.loads(text, object_pairs_hook=_object_pairs_hook)


def canonical_key_scan_ok(value):
    """Recursively confirm every object key of an already-parsed value."""
    stack = [value]
    while stack:
        current = stack.pop()
        if isinstance(current, dict):
            for key, item in current.items():
                if not key_is_unicode_scalar_string(key):
                    return False
                stack.append(item)
        elif isinstance(current, list):
            stack.extend(current)
    return True


def sorted_unique(values):
    return sorted(set(values))


def is_sorted_unique_list(value):
    if not isinstance(value, list):
        return False
    for item in value:
        if not isinstance(item, str):
            return False
    return value == sorted(set(value))


def is_real_int(value):
    """A real JSON integer -- never a bool, never a float."""
    return isinstance(value, int) and not isinstance(value, bool)

#!/usr/bin/env python3
"""The N.H automatic-supervisor protocol, v1.13.

This package is the production controller-side implementation of
``spec/NH_AUTOMATIC_SUPERVISOR_MECHANICAL_CHANGE_SPEC_v1_13_CANDIDATE.md``.
It is a CANDIDATE: it is not installed, not accepted, not adopted, not
governance, and it claims no PASS.
"""

from __future__ import annotations

from . import (  # noqa: F401
    auditresult,
    canonical,
    capability,
    classify,
    commands,
    constants,
    corrections,
    dependency,
    engine,
    feed,
    identity,
    journal,
    lease,
    provider,
    replay,
    runtime,
    scheduling,
    schema,
    status,
)

SUPERVISOR_PROTOCOL_VERSION = constants.SUPERVISOR_PROTOCOL_VERSION

__all__ = [
    "auditresult",
    "canonical",
    "capability",
    "classify",
    "commands",
    "constants",
    "corrections",
    "dependency",
    "engine",
    "feed",
    "identity",
    "journal",
    "lease",
    "provider",
    "replay",
    "runtime",
    "scheduling",
    "schema",
    "status",
    "SUPERVISOR_PROTOCOL_VERSION",
]

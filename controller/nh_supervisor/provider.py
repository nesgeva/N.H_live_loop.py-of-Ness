#!/usr/bin/env python3
"""Section 4.6 / 11.2 -- the dependency-injected provider interface.

Provider contact is the ONLY thing this module abstracts.  Everything that
decides an outcome -- the facts object, the classifier, the custody rules, the
terminal kind -- belongs to the controller and lives elsewhere.

``NoProviderConfigured`` is the production default in this candidate shadow:
no provider is bound, so any attempt to dispatch fails closed rather than
contacting anything.  A deterministic fake is supplied for rehearsal and tests.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from . import constants


@dataclass(frozen=True)
class ProviderDispatch:
    """Everything the transport is given, and nothing else."""

    provider_kind: str
    provider_endpoint_identity: str
    provider_request_identity: str
    work_item_identity: str
    provider_dispatch_serial: int
    prompt_material_sha256: str
    required_inputs_sha256: str
    result_schema_id: str
    idempotency_key: str | None
    transport: str = "in_process_https"


@dataclass
class ProviderObservation:
    """Exactly what the controller itself observed.  No prose, ever."""

    transport_kind: str = "in_process_https"
    transport_outcome: str = "completed"
    transmission_proved_absent: bool = False
    returncode: int | None = None
    http_status: int | None = None
    declared_content_length: int | None = None
    endpoint_error_code_sha256: str | None = None
    retry_after_seconds: int | None = None
    body: bytes | None = None
    observed_body_byte_length: int = 0
    acceptance_authority: str = "none"
    provider_side_request_ref: str | None = None
    acceptance_evidence: dict[str, Any] | None = None


@dataclass
class LookupObservation:
    """The bounded result of one authoritative or best-effort lookup."""

    outcome: str
    provider_side_request_ref: str | None = None
    evidence: dict[str, Any] = field(default_factory=dict)
    body: bytes | None = None
    declared_content_length: int | None = None


@dataclass
class ProbeObservation:
    """Exactly what a bounded, non-generative availability probe observed."""

    probe_transport_kind: str = "in_process_https"
    probe_transport_outcome: str = "completed"
    probe_returncode: int | None = None
    probe_http_status: int | None = None
    probe_endpoint_response_code_sha256: str | None = None
    probe_response_schema_id: str | None = None
    probe_response_schema_valid: bool = False
    body: bytes | None = None
    probe_response_byte_length: int = 0


class NoProviderConfigured(RuntimeError):
    """No provider transport is bound; nothing may be contacted."""


class ProviderTransport:
    """The production interface.  A real installation binds a subclass."""

    def dispatch(self, request: ProviderDispatch) -> ProviderObservation:
        raise NoProviderConfigured(
            "no provider transport is bound to this controller: dispatch is refused"
        )

    def lookup(self, request: ProviderDispatch, provider_side_request_ref):
        raise NoProviderConfigured(
            "no provider transport is bound to this controller: lookup is refused"
        )

    def probe(self, provider_kind, provider_endpoint_identity, probe_command_identity):
        raise NoProviderConfigured(
            "no provider transport is bound to this controller: probe is refused"
        )


class RefusingProviderTransport(ProviderTransport):
    """The default binding of this candidate shadow.  It contacts nothing."""


class DeterministicFakeProvider(ProviderTransport):
    """A deterministic, offline double for rehearsal and fault-injection tests.

    It performs no network or subprocess work of any kind.  Every response is a
    scripted, in-memory value keyed by provider kind and dispatch serial, and it
    counts invocations so a test can prove that no duplicate call was made.
    """

    def __init__(self, script=None, probe_script=None, lookup_script=None):
        self.script = dict(script or {})
        self.probe_script = list(probe_script or [])
        self.lookup_script = dict(lookup_script or {})
        self.dispatch_calls = []
        self.lookup_calls = []
        self.probe_calls = []

    # -- generative dispatch -------------------------------------------------
    def dispatch(self, request: ProviderDispatch) -> ProviderObservation:
        self.dispatch_calls.append(
            {
                "provider_kind": request.provider_kind,
                "provider_request_identity": request.provider_request_identity,
                "provider_dispatch_serial": request.provider_dispatch_serial,
                "work_item_identity": request.work_item_identity,
            }
        )
        key = (request.provider_kind, request.provider_dispatch_serial)
        handler = self.script.get(key) or self.script.get(request.provider_kind)
        if handler is None:
            raise NoProviderConfigured(
                "the deterministic fake has no scripted response for %s serial %d"
                % (request.provider_kind, request.provider_dispatch_serial)
            )
        if callable(handler):
            return handler(request)
        return handler

    def dispatch_count(self, provider_request_identity=None):
        if provider_request_identity is None:
            return len(self.dispatch_calls)
        return sum(
            1
            for call in self.dispatch_calls
            if call["provider_request_identity"] == provider_request_identity
        )

    # -- lookup --------------------------------------------------------------
    def lookup(self, request: ProviderDispatch, provider_side_request_ref):
        self.lookup_calls.append(request.provider_request_identity)
        handler = self.lookup_script.get(request.provider_request_identity)
        if handler is None:
            handler = self.lookup_script.get(request.provider_kind)
        if handler is None:
            raise NoProviderConfigured("the deterministic fake has no scripted lookup")
        if callable(handler):
            return handler(request, provider_side_request_ref)
        return handler

    # -- probe ---------------------------------------------------------------
    def probe(self, provider_kind, provider_endpoint_identity, probe_command_identity):
        self.probe_calls.append((provider_kind, provider_endpoint_identity))
        if not self.probe_script:
            raise NoProviderConfigured("the deterministic fake has no scripted probe")
        return self.probe_script.pop(0)


class FailIfCalledProvider(ProviderTransport):
    """A transport that makes any contact a hard, visible test failure."""

    def __init__(self, on_call=None):
        self.calls = 0
        self._on_call = on_call

    def _fail(self, what):
        self.calls += 1
        if self._on_call is not None:
            self._on_call(what)
        raise AssertionError(
            "the controller attempted a provider %s where the specification "
            "permits none" % what
        )

    def dispatch(self, request):
        self._fail("dispatch")

    def lookup(self, request, provider_side_request_ref):
        self._fail("lookup")

    def probe(self, provider_kind, provider_endpoint_identity, probe_command_identity):
        self._fail("probe")


def bounded_read(observation: ProviderObservation):
    """The Section 4.9b bounded read discipline, applied to one observation.

    Returns ``(bytes_or_none, oversize_detection_kind, observed_bytes_read,
    declared_result_byte_length)``.  Nothing is retained when the bound is
    exceeded, and a declared over-bound length reads no body byte at all.
    """
    declared = observation.declared_content_length
    if declared is not None and declared > constants.MAX_PROVIDER_RESULT_BYTES:
        return None, "declared_length_over_bound", 0, declared
    body = observation.body
    if body is None:
        return None, None, observation.observed_body_byte_length, None
    if len(body) >= constants.MAX_PROVIDER_RESULT_READ_LIMIT_BYTES:
        return (
            None,
            "stream_exceeded_read_limit",
            constants.MAX_PROVIDER_RESULT_READ_LIMIT_BYTES,
            None,
        )
    return body, None, len(body), declared


def bounded_probe_read(observation: ProbeObservation):
    """The Section 11.2b bounded probe read.  Reaching the limit is never success."""
    body = observation.body
    if body is None:
        return None, observation.probe_response_byte_length, False
    if len(body) >= constants.MAX_PROBE_RESULT_READ_LIMIT_BYTES:
        return None, constants.MAX_PROBE_RESULT_READ_LIMIT_BYTES, True
    return body, len(body), False

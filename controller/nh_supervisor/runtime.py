#!/usr/bin/env python3
"""Production construction of one ``SupervisorContext``.

The bindings are dependency-injected so a disposable rehearsal can supply
deterministic ones without a real N.H checkout, while a real installation binds
the controller's own proved package/source facts and the installed
authenticated interview journal.
"""

from __future__ import annotations

import os

from . import capability, constants, engine, lease as lease_mod, scheduling
from .canonical import canonical_json, sha256_hex
from .identity import derive


def controller_executable_identity(path, blob):
    return derive(
        "controller_executable_identity",
        {
            "controller_repo_relative_path": path,
            "controller_sha256": sha256_hex(blob),
            "controller_bytes": len(blob),
            "journal_current_version": constants.INTERVIEW_JOURNAL_CURRENT_VERSION,
            "supervisor_protocol_version": constants.SUPERVISOR_PROTOCOL_VERSION,
        },
    )


def controller_executable_identity_of_file(repo_relative_path, absolute_path):
    with open(absolute_path, "rb") as handle:
        blob = handle.read()
    return controller_executable_identity(repo_relative_path, blob)


class CapabilityRegistry:
    """Controller-owned configuration, bound by digest.  No model writes it."""

    def __init__(self, records=None):
        self._records = dict(records or {})

    def put(self, provider_kind, endpoint, record):
        self._records[(provider_kind, endpoint)] = record

    def reader(self):
        def read(provider_kind, endpoint):
            return self._records.get((provider_kind, endpoint))

        return read


def build_context(
    *,
    journal,
    binding,
    controller_executable_identity,
    endpoint_binding,
    capability_reader,
    round_zero_candidate,
    provider=None,
    state_dir=None,
    candidate_dir=None,
    clock=None,
    lease=None,
    lease_binding=None,
    own_run_id=None,
    scheduling_journal=None,
    accepted_ness_decision_records=None,
    accepted_ness_unlock_records=None,
    blocking_finding_refs_override=None,
    parent_candidate_payload=None,
    review_signal_adapter=None,
    interview_projection_reader=None,
    interview_gate_reader=None,
    write_boundary_prover=None,
):
    from . import provider as provider_module

    context = engine.SupervisorContext(
        journal=journal,
        binding=binding,
        controller_executable_identity=controller_executable_identity,
        endpoint_binding=dict(endpoint_binding),
        capability_reader=capability_reader,
        provider=provider or provider_module.RefusingProviderTransport(),
        lease=lease,
        lease_binding=lease_binding,
        own_run_id=own_run_id,
        clock=clock,
        state_dir=state_dir,
        candidate_dir=candidate_dir,
        accepted_ness_decision_records=accepted_ness_decision_records,
        accepted_ness_unlock_records=accepted_ness_unlock_records,
        scheduling=scheduling_journal,
        blocking_finding_refs_override=blocking_finding_refs_override,
        round_zero_candidate=round_zero_candidate,
        parent_candidate_payload=parent_candidate_payload,
        review_signal_adapter=review_signal_adapter,
        interview_projection_reader=interview_projection_reader,
        interview_gate_reader=interview_gate_reader,
        write_boundary_prover=write_boundary_prover,
    )
    return context


def default_lease_binding(context_binding, controller_executable_identity, *, pid=None,
                          hooks=None):
    hooks = hooks or lease_mod.LeaseHooks()
    pid = os.getpid() if pid is None else pid
    return {
        "pid": pid,
        "process_start_ticks": hooks.process_start_ticks(pid),
        "boot_id_sha256": hooks.boot_id_sha256(),
        "controller_executable_identity": controller_executable_identity,
        "package_scope_id": context_binding.package_scope_id,
        "source_binding_sha256": context_binding.source_binding_sha256,
    }

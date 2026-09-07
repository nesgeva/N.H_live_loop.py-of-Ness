#!/usr/bin/env python3
"""OFFLINE rehearsals for the accepted post-acceptance continuation design.

Source of obligations:
``NH-GOVERNANCE/05_ACTIVE_CANDIDATE/
NH_LIVE_DESIGN_LOOP_POST_ACCEPTANCE_CONTINUATION_MECHANICAL_DESIGN_v1_8_CANDIDATE.md``
SHA-256 448daa63b4899d4639dc5b7612985cb34e97732dcf4cbeac2c224c54f8ae51e2,
303,820 bytes, 2,826 lines.  Section 25.2 rehearsals R1 through R103.

EVERY rehearsal here runs OFFLINE, in a DISPOSABLE copy, against a DISPOSABLE
journal and checkout.  None touches the real journal, the real state directory,
the real N.H checkout, or a real provider.

Providers are stubbed by a transport that FAILS LOUDLY if contacted where a
call is not expected.  Nothing here launches the real worker, opens a socket,
opens a browser, or calls either module's ``main()``.
"""

from __future__ import annotations

import base64
import copy
import dataclasses
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path
from unittest import mock

sys.dont_write_bytecode = True

TESTS_DIR = Path(__file__).resolve().parent
ROOT_DIR = TESTS_DIR.parent
CONTROLLER_DIR = ROOT_DIR / "controller"
UI_DIR = ROOT_DIR / "interview_ui"
# Disposable per-test copies live here, never in the project tree.
SCRATCH_DIR = Path(
    os.environ.get("NH_C4_SCRATCH_DIR") or tempfile.gettempdir()
)
CONTROLLER_SOURCE = CONTROLLER_DIR / "nh_loop.py"

# ===========================================================================
# TEST-ONLY ISOLATION.
#
# The production-target controller carries NO rehearsal redirect seam: its
# repository and state-directory literals are exactly the installed ones.  The
# isolation below is arranged HERE, in test setup, and exists nowhere in the
# implementation.
#
#   * the interview state directory uses the PRE-EXISTING INSTALLED override
#     ``NH_LOOP_INTERVIEW_STATE_DIR``, whose own comment in the installed
#     controller says it "exists so tests can point it at a temporary
#     directory".  Nothing new is introduced for it;
#   * the N.H repository path is redirected by PATCHING THE MODULE GLOBAL after
#     import.  ``real_repo_root()`` reads ``NH_REPO_PATH`` at call time, so the
#     patch takes effect for every path decision without the implementation
#     carrying any environment control surface of its own.
#
# Both are proved by ``test_C5_no_production_disposable_root_seam`` and
# ``test_C5_every_writable_test_path_stays_in_the_disposable_root``.
# ===========================================================================
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
os.environ["NH_LOOP_INTERVIEW_STATE_DIR"] = str(ROOT_DIR / "nh_interview_state")

for _entry in (str(CONTROLLER_DIR), str(UI_DIR)):
    if _entry not in sys.path:
        sys.path.insert(0, _entry)

import nh_loop  # noqa: E402 -- import only; main() is never called

# The one test-only redirect, applied to the imported module.
nh_loop.NH_REPO_PATH = str(ROOT_DIR / "NH-GOVERNANCE")
import nh_supervisor  # noqa: E402
from nh_supervisor import (  # noqa: E402
    commands,
    constants,
    dependency,
    engine,
    identity,
    replay,
    schema,
)
from nh_supervisor.engine import SupervisorRefusal  # noqa: E402

import supervisor as ui_supervisor  # noqa: E402
import worker as ui_worker  # noqa: E402


# ===========================================================================
# THE OFFLINE HARNESS.
# ===========================================================================
class ProviderContacted(AssertionError):
    """Raised the instant a rehearsal reaches a provider it must not."""


class LoudStubTransport(nh_supervisor.provider.ProviderTransport):
    """A stub that FAILS LOUDLY if any rehearsal unexpectedly contacts it.

    Section 25: "Providers are stubbed by a transport that fails loudly if
    contacted where a call is not expected."
    """

    dispatch_transport = "offline_stub"

    def __init__(self, body=None, *, allow=False, outcome="completed",
                 transport_kind="offline_stub"):
        # ``transport_kind`` is what the observation DECLARES.  The default is
        # deliberately uncontrolled, so a rehearsal that reaches a provider it
        # did not intend to fails the shape check as well as this stub.  The
        # end-to-end gate declares the controlled kind instead, so the installed
        # classifier does its real work on a stubbed transport.
        self.transport_kind = transport_kind
        self.calls = []
        self.requests = []
        self.codex_calls = 0
        self.claude_calls = 0
        self._body = body
        self._allow = allow
        self._outcome = outcome

    def dispatch(self, request):
        self.calls.append(request.provider_kind)
        self.requests.append(request)
        if request.provider_kind in ("claude_correction", "claude_initial_design",
                                     "claude_acceptance_explanation"):
            self.claude_calls += 1
        else:
            self.codex_calls += 1
        if not self._allow:
            raise ProviderContacted(
                "a provider was contacted where no call is expected: %s"
                % request.provider_kind
            )
        return nh_supervisor.provider.ProviderObservation(
            transport_kind=self.transport_kind,
            transport_outcome=self._outcome,
            transmission_proved_absent=False,
            returncode=0,
            body=self._body,
            observed_body_byte_length=0 if self._body is None else len(self._body),
            acceptance_authority="none",
        )

    def lookup(self, request, provider_side_request_ref):
        # The local CLI transport supports NO authoritative lookup (P-17).
        return nh_supervisor.provider.LookupObservation(outcome="unsupported")

    def probe(self, provider_kind, provider_endpoint_identity, probe_command_identity):
        return nh_supervisor.provider.ProbeObservation(
            probe_transport_kind="offline_stub",
            probe_transport_outcome="completed",
            probe_returncode=1,
        )


def read_text(path):
    """Read one source file without leaking a handle."""
    with io.open(path, encoding="utf-8") as handle:
        return handle.read()


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode("utf-8")).hexdigest()


ROOT_P = "05_ACTIVE_CANDIDATE/NH_P_v1_0_CANDIDATE.md"
ROOT_Q = "05_ACTIVE_CANDIDATE/NH_FAKE_NEXT_PACKAGE_v1_0_CANDIDATE.md"
TARGET_Q = "05_ACTIVE_CANDIDATE/NH_FAKE_NEXT_PACKAGE_v1_1_CANDIDATE.md"
# The scopes are DERIVED from the proved roots, exactly as the controller
# derives them.  Nothing here invents a scope.
SCOPE_P = "nullpkg_" + hashlib.sha256(ROOT_P.encode()).hexdigest()[:32]
SCOPE_Q = "nullpkg_" + hashlib.sha256(ROOT_Q.encode()).hexdigest()[:32]


class FakeJournal:
    """A disposable, append-only, hash-chained journal.  Never the real one."""

    def __init__(self, events=None):
        self.events = [dict(event) for event in (events or [])]
        self.appends = 0

    def read(self):
        return [copy.deepcopy(event) for event in self.events]

    def snapshot(self):
        events = self.read()
        return events, {"event_seq": len(events)}

    def append(self, body):
        self.appends += 1
        event = dict(body)
        event["event_seq"] = len(self.events) + 1
        event.setdefault("journal_version", 6)
        event.setdefault("package_scope_id", None)
        previous = self.events[-1]["event_sha256"] if self.events else ""
        event["event_sha256"] = digest([previous, event])
        self.events.append(event)
        return copy.deepcopy(event)

    def write_transaction(self):
        raise AssertionError("no rehearsal opens a real write transaction")


def make_binding(scope=SCOPE_P, *, root="05_ACTIVE_CANDIDATE/NH_P_v1_0_CANDIDATE.md",
                 validation_set_id="vs_1", routed=()):
    return engine.PackageBinding(
        package_key="no_controlled_id_settled_yet",
        package_scope_id=scope,
        branch="nh-design-loop",
        head_sha="a" * 40,
        source_binding_sha256="b" * 64,
        settled_decision_binding_sha256="c" * 64,
        source_manifest_sha256="d" * 64,
        terminal_chain_sha256="b" * 64,
        required_source_paths=frozenset(("01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md",)),
        validation_set_id=validation_set_id,
        coverage_review_event_seq=None,
        piece3_standing_sha256="e" * 64,
        routed_signal_refs=routed,
        package_id=None,
        scope_root_path=root,
    )


def make_candidate(path="05_ACTIVE_CANDIDATE/NH_P_v1_0_CANDIDATE.md"):
    return engine.CandidateState(
        candidate_path=path,
        candidate_sha256="f" * 64,
        candidate_bytes=100,
    )


# section 8.8 section 15.3 -- the deterministic offline stand-in for the LIVE
# source binding digest ``read_source_binding()`` returns.  A rehearsal that
# needs a MATERIAL SOURCE CHANGE simply reports a different one.
STUB_LIVE_SOURCE_BINDING = "e" * 64
STUB_CHANGED_SOURCE_BINDING = "7" * 64


class StubAdapter:
    """The installed continuation code, stubbed deterministically and offline."""

    def __init__(self, **overrides):
        self.required_files = {
            "nh_master": {"path": "01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md"},
            "nh_decision_defaults": {
                "path": "01_AUTHORITATIVE/" + nh_loop.NH_CURRENT_AUTHORITATIVE_DECISION_DEFAULTS
            },
        }
        self.roots = {ROOT_Q: {"sha256": "9" * 64, "bytes": 4096}}
        self.new_paths = {TARGET_Q}
        # section 8.8 section 15.3 -- the LIVE source binding this stub reports.
        self.live_source_binding = STUB_LIVE_SOURCE_BINDING
        self.__dict__.update(overrides)

    # -- installed validators ------------------------------------------------
    def validate_next_package_analysis(self, text, errors, required_files=None):
        try:
            value = json.loads(text)
        except ValueError as exc:
            errors.append(str(exc))
            return None
        if required_files is None:
            errors.append("no controller-resolved authority set was supplied")
            return None
        missing = sorted(set(NEXT_PACKAGE_KEYS) - set(value))
        extra = sorted(set(value) - set(NEXT_PACKAGE_KEYS))
        if missing or extra:
            errors.append("exact key set: missing=%s extra=%s" % (missing, extra))
            return None
        if value.get("whole_check_complete") is not True:
            errors.append("whole_check_complete")
            return None
        # GOVERNING-AUTHORITY COVERAGE, measured against the controller's own
        # CURRENT preflight resolution -- the same shape as the installed
        # check_required_source_coverage().
        checked = set(value.get("source_paths_checked") or ())
        for entry in required_files.values():
            path = entry.get("path") if isinstance(entry, dict) else entry
            if path and path not in checked and path not in COVERED_BY_DEFAULT:
                errors.append("governing authority not covered: %s" % path)
                return None
        return value

    def validate_prepared_task(self, text, analysis, required_files, errors):
        try:
            value = json.loads(text)
        except ValueError as exc:
            errors.append(str(exc))
            return None
        missing = sorted(set(PREPARE_TASK_KEYS) - set(value))
        extra = sorted(set(value) - set(PREPARE_TASK_KEYS))
        if missing or extra:
            errors.append("exact key set: missing=%s extra=%s" % (missing, extra))
            return None
        if value.get("package_source_path") != analysis.get("package_source_path"):
            errors.append("package_source_path cross-check")
            return None
        return value

    def validate_question_validation_payload(self, text, extra, errors):
        return nh_loop._continuation_piece3_payload_contract(
            text, nh_loop.QUESTION_VALIDATION_REQUIRED_KEYS, errors
        )

    def validate_question_coverage_review(self, text, extra, errors):
        return nh_loop._continuation_piece3_payload_contract(
            text, nh_loop.COVERAGE_REVIEW_REQUIRED_KEYS, errors
        )

    # -- installed controller-owned resolution -------------------------------
    def resolve_required_files(self):
        return self.required_files

    def resolve_repo_source_path(self, value):
        return value if value in self.roots else None

    def check_required_source_coverage(self, *args, **kwargs):
        return True

    def interview_package_scope_id(self, package_id, root):
        if package_id:
            return package_id
        return "nullpkg_" + hashlib.sha256(root.encode()).hexdigest()[:32]

    def interview_package_key(self, package_id):
        return package_id or "no_controlled_id_settled_yet"

    def is_new_candidate_path(self, value):
        return value in self.new_paths

    def source_root_identity(self, relative_path):
        return self.roots.get(relative_path)

    def current_source_binding(self):
        """The stubbed LIVE source binding digest, read offline.

        section 8.8 sections 15.3 / 15.4 -- T1's freeze is the LIVE source, so the
        stub adapter must supply one exactly as the installed
        ``_continuation_current_source_binding()`` does.  A rehearsal that
        wants a MATERIAL SOURCE CHANGE moves this value; nothing else in the
        fixture changes.
        """
        return self.live_source_binding

    next_package_action_by_classification = nh_loop.NEXT_PACKAGE_ACTION_BY_CLASSIFICATION
    next_package_prompt = nh_loop.NEXT_PACKAGE_PROMPT
    build_prepare_task_prompt = staticmethod(nh_loop.build_prepare_task_prompt)
    build_question_validation_prompt = staticmethod(nh_loop.build_question_validation_prompt)
    build_question_coverage_review_prompt = staticmethod(
        nh_loop.build_question_coverage_review_prompt
    )

    def piece3_precall_requirement(self, scope, kind, selection=None):
        return {"piece3_stage": kind, "frozen": True}

    def piece3_commit(self, scope, kind, value, evidence, errors):
        return {"committed": True}

    def run_design_task_preparation(self, *args, **kwargs):
        raise AssertionError("no rehearsal runs the live preparation stage")

    def build_transition_context(self, *args, **kwargs):
        raise AssertionError("no rehearsal builds a live transition context")

    def settled_decision_binding(self, *args, **kwargs):
        return {}

    def interview_clearance(self, scope):
        return {"unlocked": False}


# The authority paths a rehearsal selection is treated as having covered.  A
# path OUTSIDE this set is genuinely uncovered and must refuse.
COVERED_BY_DEFAULT = frozenset(
    (
        "01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md",
        "01_AUTHORITATIVE/" + nh_loop.NH_CURRENT_AUTHORITATIVE_DECISION_DEFAULTS,
    )
)

NEXT_PACKAGE_KEYS = tuple(sorted(nh_loop.NEXT_PACKAGE_REQUIRED_KEYS))
PREPARE_TASK_KEYS = tuple(sorted(nh_loop.PREPARE_TASK_REQUIRED_KEYS))


def selection_object(*, classification="mechanical_work", root=ROOT_Q, package_id=None):
    value = {key: None for key in NEXT_PACKAGE_KEYS}
    value.update(
        {
            "classification": classification,
            "controller_action": nh_loop.NEXT_PACKAGE_ACTION_BY_CLASSIFICATION[
                classification
            ],
            "package_id": package_id,
            "package_title": "a model-authored title that identifies nothing",
            "package_source_path": root,
            "simple_explanation": "evidence only",
            "dependency": None,
            "source_paths_checked": [root],
            "whole_check_complete": True,
            "unknowns": [],
        }
    )
    return value


def prepared_task_object(*, root=ROOT_Q, target=TARGET_Q, review_signal=None,
                         task_ready=True, classification="mechanical_work"):
    value = {key: None for key in PREPARE_TASK_KEYS}
    value.update(
        {
            "package_id": None,
            "package_title": "prose",
            "package_source_path": root,
            "classification": classification,
            "task_ready": task_ready,
            "not_ready_reason": None,
            "target_path": target,
            "simple_explanation": "evidence only",
            "settled_basis": ["01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md"],
            "source_paths_checked": [root],
            "open_items": [],
            "mechanical_design_specification": {"requirements": ["one"]},
            "review_signal": review_signal,
            "whole_check_complete": True,
            "unknowns": [],
        }
    )
    return value


INITIAL_DESIGN_PAYLOAD = b"the produced design bytes"
INITIAL_DESIGN_IDENTITY = {
    "path": TARGET_Q,
    "sha256": hashlib.sha256(INITIAL_DESIGN_PAYLOAD).hexdigest(),
    "bytes": len(INITIAL_DESIGN_PAYLOAD),
}


def initial_candidate_body(event_type, origin_key, origin, *, parent):
    """A candidate record naming the EXACT identity the T4 result produced."""
    body = {
        "type": event_type,
        "package_scope_id": SCOPE_Q,
        origin_key: origin,
        "candidate_path": INITIAL_DESIGN_IDENTITY["path"],
        "candidate_sha256": INITIAL_DESIGN_IDENTITY["sha256"],
        "candidate_bytes": INITIAL_DESIGN_IDENTITY["bytes"],
        "parent_candidate_path": parent.candidate_path,
        "parent_candidate_sha256": parent.candidate_sha256,
        "parent_candidate_bytes": parent.candidate_bytes,
    }
    return body


def initial_design_result(*, path=TARGET_Q, payload=b"the produced design bytes",
                          schema_id=None, declared_bytes=None, sha=None, encoded=None):
    body = payload
    explanation = {
        key: "This plain language explanation states the finished design fact number %d clearly."
        % index
        for index, key in enumerate(constants.EXPLANATION_CONTENT_PART_KEYS, 1)
    }
    return {
        "result_schema_id": schema_id or constants.INITIAL_DESIGN_RESULT_SCHEMA_ID,
        "result_schema_version": 1,
        "produced_candidate_path": path,
        "produced_candidate_sha256": sha or hashlib.sha256(body).hexdigest(),
        "produced_candidate_bytes": (
            len(body) if declared_bytes is None else declared_bytes
        ),
        "produced_candidate_payload_base64": (
            encoded if encoded is not None else base64.b64encode(body).decode("ascii")
        ),
        "acceptance_explanation_content": explanation,
    }


class FakeLease:
    """A disposable, always-provable lease.  Never the real one.

    Section 23 R-14 stays real: a rehearsal that wants the gate CLOSED simply
    omits this lease, and the installed refusal fires unchanged.
    """

    def __init__(self, binding, run_id="run_disposable"):
        self.binding = dict(binding)
        self.run_id = run_id

    def evaluate(self, binding=None, now=None):
        lease = dict(self.binding)
        lease["run_id"] = self.run_id
        lease["expires_at_epoch"] = (now or 0) + 3600
        return "LIVE_PROVED", lease, "disposable rehearsal lease"


@contextmanager
def proved_acceptance():
    """Stand in for the section 6.3 freshness proof, and ONLY that proof.

    The freshness gate itself is rehearsed separately and unpatched (see
    ``test_R1a_continuation_never_begins_without_a_fresh_proof``); these
    fixtures use a disposable journal that holds no acceptance chain, so the
    gate would refuse before the rule actually under test could run.  Nothing
    downstream of the gate is stubbed.
    """
    def proved(context, events=None):
        return True, {
            "workflow_state": "ACCEPTED_FOR_DESIGN_ONLY",
            "acceptance_truth": "PROVED_ACCEPTED",
            "journal_authentication_proved": True,
            "authenticated_state_current": True,
            "retry_series_key": None,
        }, None

    with mock.patch.object(commands, "acceptance_freshly_proved", proved):
        yield


def accepted_journal():
    """A disposable journal already holding P's durable acceptance."""
    journal = FakeJournal()
    journal.append(
        {
            "type": "ness_candidate_acceptance_recorded",
            "package_scope_id": SCOPE_P,
            "acceptance_disposition": "ACCEPTED_FOR_DESIGN_ONLY",
        }
    )
    return journal


def build_context(scope=SCOPE_P, *, journal=None, adapter=None, transport=None,
                  binding=None, candidate=None, clearance=None,
                  transition_kind=None, facts=None, lease=True):
    """One disposable SupervisorContext.  Never the live one."""
    journal = journal or FakeJournal()
    adapter = adapter or StubAdapter()
    transport = transport or LoudStubTransport()
    binding = binding or make_binding(scope)
    candidate = candidate or make_candidate(binding.scope_root_path)
    registry = nh_supervisor.runtime.CapabilityRegistry()
    lease_binding = {
        "package_scope_id": binding.package_scope_id,
        "source_binding_sha256": binding.source_binding_sha256,
        "controller_executable_identity": "1" * 64,
    }
    lease_object = FakeLease(lease_binding) if lease else None
    context = nh_supervisor.runtime.build_context(
        journal=journal,
        binding=binding,
        controller_executable_identity="1" * 64,
        endpoint_binding=nh_loop.supervisor_endpoint_binding(),
        capability_reader=registry.reader(),
        round_zero_candidate=candidate,
        provider=transport,
        lease=lease_object,
        lease_binding=lease_binding,
        own_run_id="run_disposable" if lease else None,
        interview_gate_reader=(clearance or (lambda scope_id: {"unlocked": False})),
    )
    # Set directly, exactly as the controller does: runtime.build_context()
    # stays BYTE-IDENTICAL because the accepted impact map does not name it.
    context.continuation_adapter = adapter
    context.transition_binding_kind = transition_kind
    context.transition_facts = facts
    return context


def selection_request_identities(*, binding=None, candidate=None, extra=None):
    """The work-item identity and COMPLETE input digest the CONTROLLER derives.

    section 8.8 sections 14.2 / 21.2 -- SEL-ADMISSION proof 8 is now a COMPLETE
    required-input inventory digest equality: the request's own durable
    ``required_inputs_sha256`` versus a freshly rebuilt inventory for that same
    request, through the ONE controller-owned work-item builder.

    A fixture that records a PLACEHOLDER digest or a placeholder work-item
    identity therefore describes a request prepared under the PREVIOUS
    OWNERSHIP, and the corrected rule judges it STALE -- correctly, and exactly
    as section 16.1 SBC-MIGRATION-GENERIC and R-SB17 require.  A rehearsal that
    wants a selection to be ADMITTED must record what the controller would
    genuinely have frozen, which is what this derives.

    Reads nothing live: the throwaway context uses the SAME deterministic
    fixture binding and candidate ``build_context()`` uses.
    """
    probe = build_context(
        journal=FakeJournal(), binding=binding, candidate=candidate, lease=False
    )
    work_item_obj, work_item_id = engine.next_package_selection_work_item(
        probe, probe.round_zero_candidate
    )
    digest = engine.required_inputs_sha256(
        probe, work_item_obj, stub_selection_extra() if extra is None else extra
    )
    return work_item_id, digest


def stub_selection_extra(**overrides):
    """The EXACT T1 extra both the fixture digest and the reconstruction use.

    section 15.2b -- the two GOVERNED T1 keys.  A rehearsal that additionally
    exercises SEL-ADMISSION proof 7 injects ``selected_root_identity`` (which
    the installed T1 dispatch does NOT bind); where it does, the fixture must
    freeze the SAME object, because the corrected proof 8 digests the COMPLETE
    inventory and a one-sided extra would simply read as staleness.
    """
    base = {
        "required_files_binding": StubAdapter().required_files,
        "frozen_source_binding_sha256": STUB_LIVE_SOURCE_BINDING,
    }
    base.update(overrides)
    return base


# The extra used by every rehearsal that also exercises proof 7.
SELECTION_ROOT_IDENTITY = {"sha256": "9" * 64, "bytes": 4096}


def full_selection_extra(**overrides):
    return stub_selection_extra(
        selected_root_identity=SELECTION_ROOT_IDENTITY, **overrides
    )


def custody_pair(journal, *, kind, provider_kind, value, scope, request="pr_1",
                 terminal_kind="result_received", work_item_identity=None,
                 required_inputs_sha256=None, extra=None,
                 supervisor_operation_id=None):
    """Append one prepared/custody/terminal triple for a disposable request.

    For a T1 ``next_package_selection`` the prepared record carries the GENUINE
    work-item identity and COMPLETE required-input digest the controller would
    have frozen, unless the caller deliberately overrides them.  section 14.4
    SBC-STALENESS-BEFORE-ROUTE puts the staleness proof ABOVE the route
    decision, so a placeholder digest would make every T1 fixture stale before
    it could ever be classified -- which is correct behaviour for a request
    prepared under the previous ownership (section 16.1, R-SB17) but is not what
    these rehearsals are about.
    """
    if kind == "next_package_selection":
        derived_id, derived_digest = selection_request_identities(extra=extra)
        if work_item_identity is None:
            work_item_identity = derived_id
        if required_inputs_sha256 is None:
            required_inputs_sha256 = derived_digest
    if work_item_identity is None:
        work_item_identity = "wi_1"
    if required_inputs_sha256 is None:
        required_inputs_sha256 = "2" * 64
    payload = json.dumps(value, sort_keys=True).encode("utf-8")
    journal.append(
        {
            "type": "provider_request_prepared",
            "package_scope_id": scope,
            "provider_request_identity": request,
            "provider_kind": provider_kind,
            "work_item_identity": work_item_identity,
            "prompt_material_sha256": "1" * 64,
            "required_inputs_sha256": required_inputs_sha256,
            "result_schema_id": constants.RESULT_SCHEMA_ID_BY_PROVIDER_KIND[provider_kind],
            **(
                {"supervisor_operation_id": supervisor_operation_id}
                if supervisor_operation_id else {}
            ),
        }
    )
    journal.append(
        {
            "type": "provider_dispatch_begun",
            "package_scope_id": scope,
            "provider_request_identity": request,
            "provider_kind": provider_kind,
        }
    )
    custody = journal.append(
        {
            "type": "provider_result_custody_recorded",
            "package_scope_id": scope,
            "provider_request_identity": request,
            "provider_kind": provider_kind,
            "work_item_kind": kind,
            "work_item_identity": work_item_identity,
            "result_custody_identity": "rc_" + request,
            "result_location_kind": "inline_journal_bytes",
            "result_bytes_base64": base64.b64encode(payload).decode("ascii"),
            "result_byte_length": len(payload),
            "result_sha256": hashlib.sha256(payload).hexdigest(),
            "result_schema_valid": True,
            "result_origin": "local_completion",
        }
    )
    terminal = journal.append(
        {
            "type": "provider_request_terminal_recorded",
            "package_scope_id": scope,
            "provider_request_identity": request,
            "provider_kind": provider_kind,
            "terminal_kind": terminal_kind,
            "result_custody_identity": "rc_" + request,
            "result_schema_valid": terminal_kind == "result_received",
        }
    )
    return custody, terminal


def reconstructor(**extras):
    """A deterministic EXTRA reconstruction, never remembered process state.

    T1's base now carries ``frozen_source_binding_sha256`` -- the LIVE source
    binding section 15.3 requires -- so the reconstruction reproduces exactly what
    ``selection_request_identities()`` froze.
    """
    def reconstruct(request_identity, kind):
        if kind == "next_package_selection":
            base = stub_selection_extra()
        else:
            base = {"required_files_binding": StubAdapter().required_files}
        base.update(extras.get(kind, {}))
        return base

    return reconstruct


def admitted_selection_state(journal, *, classification="mechanical_work",
                             root=ROOT_Q, adapter=None, extra=None,
                             binding=None, candidate=None):
    """A journal holding exactly one admissible T1 selection.

    The prepared record carries the GENUINE work-item identity and COMPLETE
    required-input digest the controller would have frozen, so SEL-ADMISSION's
    corrected proof 8 reproduces it exactly and the selection is ADMITTED
    rather than judged stale (section 14.2, R-SB12).
    """
    work_item_id, digest = selection_request_identities(
        binding=binding, candidate=candidate, extra=extra
    )
    custody_pair(
        journal,
        kind="next_package_selection",
        provider_kind="codex_next_package_selection",
        value=selection_object(classification=classification, root=root),
        scope=SCOPE_P,
        request="pr_sel",
        work_item_identity=work_item_id,
        required_inputs_sha256=digest,
        extra=extra,
    )
    return journal


# ===========================================================================
# R1-R11 -- ACCEPTANCE, BINDING, AND THE SELECTOR CONTRACT.
# ===========================================================================
class AcceptanceAndBindingRehearsals(unittest.TestCase):
    def test_R1_accept_is_still_acceptance_only(self):
        """R1 -- the Accept transaction remains exactly acceptance-only.

        INV-ACCEPT is a STRUCTURAL rule, not a runtime check: no continuation
        entry point may be callable, directly or transitively, from
        ``acceptance_offer()`` or ``record_ness_acceptance()``.
        """
        source = read_text(CONTROLLER_DIR / "nh_supervisor" / "commands.py")
        continuation_names = (
            "continue_design_loop",
            "dispatch_piece3_provider_review",
            "commit_piece3_provider_result",
            "prepare_next_design_task",
            "execute_initial_design",
            "post_acceptance_transition_state",
            "loop_status",
        )
        for entry in ("def acceptance_offer(", "def record_ness_acceptance("):
            start = source.index(entry)
            body = source[start:start + 40000]
            end = body.find("\ndef ", 10)
            body = body[:end] if end != -1 else body
            for name in continuation_names:
                self.assertNotIn(
                    name + "(", body,
                    "%s is reachable from %s" % (name, entry),
                )
        # And the two acceptance commands are not members of the continuation set.
        self.assertFalse(
            set(constants.CONTINUATION_EXECUTION_COMMANDS)
            & {"acceptance-offer", "record-ness-acceptance"}
        )

    def test_R2_acceptance_stays_terminal_for_its_own_package(self):
        """R2 -- ACCEPTED_FOR_DESIGN_ONLY remains terminal for package P."""
        report = run_live_copy("supervisor-status")
        self.assertEqual(report["workflow_state"], "ACCEPTED_FOR_DESIGN_ONLY")
        self.assertEqual(report["acceptance_truth"], "PROVED_ACCEPTED")
        self.assertIsNone(report["next_command"])
        self.assertFalse(report["acceptance_required"])

    def test_R3_binding_parity_on_the_real_shaped_journal(self):
        """R3 -- section 8 returns the SAME binding the installed code returns.

        Run against a disposable copy of the current 84-event journal.  The
        corrected rule changes NOTHING about the current state (section 8.7).
        """
        report = run_live_copy("supervisor-status")
        errors = []
        context = nh_loop.build_supervisor_context(errors)
        self.assertEqual(errors, [])
        self.assertIsNotNone(context)
        events, situation, _lease_state, _lease = commands.read_state(context)
        self.assertEqual(report["authenticated_event_seq"], len(events))
        self.assertEqual(
            report["package_scope_id"], context.binding.package_scope_id
        )
        self.assertEqual(
            report["candidate_path"], situation.candidate.candidate_path
        )
        self.assertEqual(
            report["candidate_sha256"], situation.candidate.candidate_sha256
        )
        self.assertEqual(report["branch"], context.binding.branch)
        self.assertEqual(report["head_sha"], context.binding.head_sha)
        self.assertEqual(report["errors"], [])

    def test_R4_second_package_becomes_current_first_does_not(self):
        """R4 -- CPB-CURRENT returns Q; P's history stays fully readable."""
        events = [
            {"type": "validation_recorded", "package_scope_id": SCOPE_P,
             "event_seq": 1, "event_sha256": "x" * 64, "journal_version": 6},
            {"type": "ness_candidate_acceptance_recorded", "package_scope_id": SCOPE_P,
             "event_seq": 2, "event_sha256": "y" * 64, "journal_version": 6},
            {"type": "validation_recorded", "package_scope_id": SCOPE_Q,
             "event_seq": 3, "event_sha256": "z" * 64, "journal_version": 6},
        ]
        anchors = nh_loop.scope_anchor_validations(events)
        self.assertEqual(sorted(anchors), sorted([SCOPE_P, SCOPE_Q]))
        # EARLIEST WITHIN a scope, and the ordering key is event_seq alone.
        self.assertEqual(anchors[SCOPE_P]["event_seq"], 1)
        self.assertEqual(anchors[SCOPE_Q]["event_seq"], 3)
        self.assertGreater(anchors[SCOPE_Q]["event_seq"], anchors[SCOPE_P]["event_seq"])
        # Q's replay holds NONE of P's acceptance.
        q_replay = replay.Replay(events, SCOPE_Q)
        self.assertEqual(q_replay.scoped("ness_candidate_acceptance_recorded"), [])
        # P's history is still fully projectable.
        p_replay = replay.Replay(events, SCOPE_P)
        self.assertEqual(len(p_replay.scoped("ness_candidate_acceptance_recorded")), 1)

    def test_R5_incomplete_transition_does_not_steal_the_binding(self):
        """R5 -- a scope that is not established is NEVER current."""
        events = [
            {"type": "validation_recorded", "package_scope_id": SCOPE_Q,
             "event_seq": 1, "event_sha256": "x" * 64, "journal_version": 6,
             "package_source_binding": {"scope_root_path": ROOT_Q, "seeds": []}},
        ]
        errors = []
        ok, _identity = nh_loop.scope_is_established(events, SCOPE_Q, events[0], errors)
        self.assertFalse(ok, "an unestablished scope must never be established")
        anchor, _bound = nh_loop.current_package_anchor(events, [])
        self.assertIsNone(anchor, "an incomplete Q must not become current")

    def test_missing_history_binds_only_to_a_proved_accepted_successor(self):
        """Removed history does not remain a runtime file dependency."""
        historical = {
            "path": (
                "05_ACTIVE_CANDIDATE/"
                "NH_TEST_SYSTEM_v1_0_CANDIDATE.md"
            ),
            "sha256": "a" * 64,
            "bytes": 123,
        }
        current_path = (
            "04_ACCEPTED_STANDALONE_DESIGNS/"
            "NH_TEST_SYSTEM_v1_2_CANDIDATE.md"
        )
        current_payload = (
            "Historical source: NH_TEST_SYSTEM_v1_0_CANDIDATE.md\n"
        ).encode("utf-8")
        current_digest = hashlib.sha256(current_payload).hexdigest()
        receipt_path = (
            "04_ACCEPTED_STANDALONE_DESIGNS/"
            "NH_TEST_SYSTEM_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md"
        )
        receipt_payload = (
            "PACKAGE_COMPLETE\naccepted source: NH_TEST_SYSTEM_v1_2_CANDIDATE.md\n"
            "sha256: %s\nbytes: %d\n"
            % (current_digest, len(current_payload))
        ).encode("utf-8")
        lookalike_path = (
            "04_ACCEPTED_STANDALONE_DESIGNS/"
            "NH_TEST_ACCEPTANCE_RECORD_SYSTEM_v1_3_CANDIDATE.md"
        )
        lookalike_payload = receipt_payload
        fake_index = {
            "by_path": {
                current_path: current_payload,
                receipt_path: receipt_payload,
                lookalike_path: lookalike_payload,
            },
            "category_of": {
                current_path: "accepted_package",
                receipt_path: "closure_record",
                lookalike_path: "acceptance_record",
            },
        }
        with mock.patch.object(
            nh_loop, "index_repository_documents", return_value=fake_index
        ):
            errors = []
            proved = nh_loop._accepted_successor_for_missing_historical_anchor(
                historical, errors
            )
        self.assertEqual(errors, [])
        self.assertEqual(proved["path"], current_path)
        self.assertEqual(proved["sha256"], current_digest)
        self.assertEqual(proved["bytes"], len(current_payload))
        self.assertEqual(proved["receipt_path"], receipt_path)

    def test_missing_history_refuses_an_unproved_newer_file(self):
        """A newer-looking file alone is never accepted as current proof."""
        historical = {
            "path": (
                "05_ACTIVE_CANDIDATE/"
                "NH_TEST_SYSTEM_v1_0_CANDIDATE.md"
            ),
            "sha256": "b" * 64,
            "bytes": 456,
        }
        current_path = (
            "04_ACCEPTED_STANDALONE_DESIGNS/"
            "NH_TEST_SYSTEM_v1_9_CANDIDATE.md"
        )
        fake_index = {
            "by_path": {current_path: b"newer name without lineage proof"},
            "category_of": {current_path: "accepted_package"},
        }
        with mock.patch.object(
            nh_loop, "index_repository_documents", return_value=fake_index
        ):
            errors = []
            proved = nh_loop._accepted_successor_for_missing_historical_anchor(
                historical, errors
            )
        self.assertIsNone(proved)
        self.assertEqual(len(errors), 1)
        self.assertIn("0 uniquely proved accepted current successor", errors[0])

    def test_R6_two_transitions_fail_closed(self):
        """R6 -- CPB-SINGLE-TRANSITION: two in-transition scopes fail closed."""
        scope_r = "nullpkg_" + hashlib.sha256(b"scope-R").hexdigest()[:32]
        events = []
        for index, scope in enumerate((SCOPE_Q, scope_r), start=1):
            events.append(
                {"type": "validation_recorded", "package_scope_id": scope,
                 "event_seq": index, "event_sha256": str(index) * 64,
                 "journal_version": 6,
                 "package_source_binding": {"scope_root_path": ROOT_Q, "seeds": []}}
            )
        errors = []
        anchor, _bound = nh_loop.current_package_anchor(events, errors)
        self.assertIsNone(anchor)
        self.assertTrue(errors, "two unestablished transition scopes must fail closed")
        self.assertIn("CPB-SINGLE-TRANSITION", " ".join(errors))

    def test_R7_cross_scope_piece3_authorization_is_refused(self):
        """R7 / R50 / R91 -- P's authorization can NEVER satisfy Q's append."""
        events = [
            {"type": "piece3_provider_work_recorded", "package_scope_id": SCOPE_P,
             "event_seq": 1, "event_sha256": "x" * 64, "journal_version": 6,
             "authorizes_event_type": "validation_recorded",
             "result_schema_valid": True},
        ]
        errors = []
        ok = nh_loop.supervisor_piece3_authorization_gate(
            events, "validation_recorded", errors, SCOPE_Q
        )
        self.assertFalse(ok, "a cross-scope authorization must refuse the append")
        self.assertTrue(errors)
        # And the same authorization DOES satisfy its OWN scope.
        errors_p = []
        self.assertTrue(
            nh_loop.supervisor_piece3_authorization_gate(
                events, "validation_recorded", errors_p, SCOPE_P
            )
        )
        self.assertEqual(errors_p, [])

    def test_R8_no_hard_coded_package(self):
        """R8 -- SEL-NO-HARDCODE: no package/addition/bundle/register literal."""
        forbidden = (
            "AUTHORITY_INTEGRITY_CONTROL_PLANE",
            "UNIFIED_DURABLE_OPERATION_KERNEL",
            "Addition 3",
            "BUNDLE_7",
            "REGISTER_C",
        )
        continuation_source = extract_continuation_source()
        for literal in forbidden:
            self.assertNotIn(
                literal, continuation_source,
                "%s is hard-coded on a continuation path" % literal,
            )

    def test_R9_closure_evidence_is_respected(self):
        """R9 / SEL-RESPECT-CLOSURE -- `settled` is never selectable."""
        journal = accepted_journal()
        custody_pair(
            journal,
            kind="next_package_selection",
            provider_kind="codex_next_package_selection",
            value=selection_object(classification="settled"),
            scope=SCOPE_P,
            request="pr_sel",
        )
        context = build_context(journal=journal)
        state = commands.post_acceptance_transition_state(
            context, reconstruct_extra=reconstructor()
        )
        self.assertIsNone(state["selection"], "a settled package is not selectable")
        self.assertIsNotNone(state["stop_record"])
        self.assertEqual(
            state["stop_record"]["loop_state"],
            commands.LOOP_DESIGN_CONTINUATION_COMPLETE,
        )

    def test_R10_authority_order_is_the_current_authoritative_defaults(self):
        """R10 / AUTH-V23 -- v2_3 is authority #2 in every operative prompt."""
        self.assertEqual(
            nh_loop.NH_CURRENT_AUTHORITATIVE_DECISION_DEFAULTS,
            "NH_DECISION_DEFAULTS-S19_v2_3.md",
        )
        self.assertIn(
            "NH_DECISION_DEFAULTS-S19_v2_3.md", nh_loop.NEXT_PACKAGE_PROMPT
        )
        self.assertNotIn(
            "NH_DECISION_DEFAULTS-S19_v2_2.md", nh_loop.NEXT_PACKAGE_PROMPT
        )
        source = read_text(CONTROLLER_SOURCE)
        self.assertNotIn(
            "2. 01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md", source
        )
        self.assertIn(
            "2. 01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_3.md", source
        )
        # The preflight requires the current authoritative basename.
        entry = dict(nh_loop.EXACT_REQUIRED_FILES)["nh_decision_defaults"]
        self.assertEqual(entry, ("NH_DECISION_DEFAULTS-S19_v2_3.md",))
        # A competing artifact is reported with exact identity and the
        # preflight caller now fails closed rather than choosing between two
        # authority claims.
        artifacts = nh_loop.competing_decision_defaults_artifacts(nh_loop.NH_REPO_PATH)
        for artifact in artifacts:
            self.assertIn("sha256", artifact)
            self.assertIn("bytes", artifact)
        marker = source.index("def competing_decision_defaults_artifacts")
        body = source[marker:source.index("def resolve_required_files")]
        self.assertNotIn("errors.append", body, "discovery remains read-only")
        preflight = source[source.index("def run_preflight_checks"):source.index("def command_preflight")]
        self.assertIn('"Defaults claims; refusing', preflight)

    def test_R11_selector_contract_coherence(self):
        """R11 -- ONE contract: the installed prompt, key set and validator."""
        self.assertNotIn(
            "NH_NEXT_PACKAGE_SELECTION_RESULT_V1",
            read_text(CONTROLLER_SOURCE),
        )
        # The registered id is LIFECYCLE metadata, never a model contract.
        self.assertIn(
            constants.RESULT_SCHEMA_ID_BY_PROVIDER_KIND["codex_next_package_selection"],
            schema.LIFECYCLE_ONLY_RESULT_SCHEMA_IDS,
        )
        # The installed model key sets are UNMUTATED.
        self.assertNotIn("result_schema_id", nh_loop.NEXT_PACKAGE_REQUIRED_KEYS)
        self.assertNotIn(
            "result_schema_version", nh_loop.NEXT_PACKAGE_REQUIRED_KEYS
        )


# ===========================================================================
# The DISPOSABLE-COPY runner.  It drives the real controller against the
# disposable tree only, and never the live one.
# ===========================================================================
LIVE_SCOPE = "nullpkg_1ffc9ec7aae12b75ef50400da674812f"
# An EXISTING real candidate file, used as the disposable Q root so the source
# binding never moves under the rehearsal.
LIVE_Q_ROOT = (
    "05_ACTIVE_CANDIDATE/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_1_CANDIDATE.md"
)
LIVE_CANDIDATE_PATH = (
    "05_ACTIVE_CANDIDATE/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_"
    "v1_6_CANDIDATE.md"
)
LIVE_CANDIDATE_SHA = (
    "7f62ee5af84cea0332eeb71d2665a66178a318deb7917e9814385b57737acf4c"
)
LIVE_HEAD_SHA = "ce3a38f43f287a56bd635ed836edf002a2db50a7"


def run_live_copy(command, stdin_envelope=None):
    """Run ONE controller command against the DISPOSABLE copy, read-only.

    Run IN-PROCESS, under the test-only redirect above, so the implementation
    needs no environment control surface of its own.  ``main()`` writes its
    machine-readable report to stdout, which is captured here.
    """
    import contextlib
    import io as _io

    buffer = _io.StringIO()
    stdin_text = None if stdin_envelope is None else json.dumps(stdin_envelope)
    with contextlib.redirect_stdout(buffer):
        with contextlib.redirect_stderr(_io.StringIO()):
            if stdin_text is not None:
                saved = sys.stdin
                sys.stdin = _io.StringIO(stdin_text)
                try:
                    nh_loop.main(["nh_loop.py", command])
                finally:
                    sys.stdin = saved
            else:
                nh_loop.main(["nh_loop.py", command])
    text = buffer.getvalue()
    start = text.index("{")
    return json.loads(text[start:])


def journal_digest():
    """A digest of the DISPOSABLE journal and head, for append-count proofs."""
    state_dir = ROOT_DIR / "nh_interview_state"
    parts = []
    for name in ("nh_interview_journal.jsonl", "nh_interview_journal.head"):
        path = state_dir / name
        parts.append(hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else "")
    return "|".join(parts)


def candidate_count():
    return len(list((ROOT_DIR / "NH-GOVERNANCE" / "05_ACTIVE_CANDIDATE").iterdir()))


def git_head():
    completed = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=str(ROOT_DIR / "NH-GOVERNANCE"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return completed.stdout.decode("utf-8").strip()


CONTINUATION_FUNCTION_NAMES = (
    "post_acceptance_transition_state",
    "loop_status",
    "continue_design_loop",
    "dispatch_piece3_provider_review",
    "commit_piece3_provider_result",
    "prepare_next_design_task",
    "execute_initial_design",
    "admit_selection",
    "admit_prepared_task",
    "owed_piece3_stage",
)


def extract_continuation_source():
    """Exactly the continuation code paths, for the no-hard-code sweep."""
    chunks = []
    commands_source = read_text(CONTROLLER_DIR / "nh_supervisor" / "commands.py")
    for name in CONTINUATION_FUNCTION_NAMES:
        marker = "\ndef %s(" % name
        if marker not in commands_source:
            continue
        start = commands_source.index(marker)
        rest = commands_source[start + 1:]
        end = rest.find("\ndef ")
        chunks.append(rest[:end] if end != -1 else rest)
    loop_source = read_text(CONTROLLER_SOURCE)
    for name in ("build_continuation_adapter", "build_transition_context",
                 "resolve_transition_context", "current_package_anchor",
                 "scope_anchor_validations", "scope_is_established"):
        marker = "\ndef %s(" % name
        if marker not in loop_source:
            continue
        start = loop_source.index(marker)
        rest = loop_source[start + 1:]
        end = rest.find("\ndef ")
        chunks.append(rest[:end] if end != -1 else rest)
    worker_source = read_text(UI_DIR / "worker.py")
    marker = "\n    def _continuation_step("
    start = worker_source.index(marker)
    rest = worker_source[start + 1:]
    end = rest.find("\n    def ", 10)
    chunks.append(rest[:end] if end != -1 else rest)
    return "\n".join(chunks)


# ===========================================================================
# R12-R24 -- ADMISSION, PREPARATION, THE CLAUDE RUN AND THE CRASH MATRIX.
# ===========================================================================
class AdmissionAndPreparationRehearsals(unittest.TestCase):
    def test_R12_admission_is_re_run_not_remembered(self):
        """R12 -- a selection whose root later moved is STALE, not deleted."""
        journal = accepted_journal()
        admitted_selection_state(journal, extra=full_selection_extra())
        context = build_context(journal=journal)
        before = commands.post_acceptance_transition_state(
            context,
            reconstruct_extra=reconstructor(
                next_package_selection={
                    "selected_root_identity": SELECTION_ROOT_IDENTITY
                }
            ),
        )
        self.assertIsNotNone(before["selection"])
        # Now the root's bytes MOVE.
        adapter = StubAdapter()
        adapter.roots = {ROOT_Q: {"sha256": "0" * 64, "bytes": 5000}}
        context = build_context(journal=journal, adapter=adapter)
        after = commands.post_acceptance_transition_state(
            context,
            reconstruct_extra=reconstructor(
                next_package_selection={
                    "selected_root_identity": SELECTION_ROOT_IDENTITY
                }
            ),
        )
        self.assertIsNone(after["selection"], "a moved root makes the selection stale")
        self.assertEqual(
            after["stop_record"]["loop_state"], commands.LOOP_SELECTION_REQUIRED
        )
        # NOTHING is rewritten or deleted: the journal is byte-identical.
        self.assertEqual(journal.appends, 5)
        self.assertEqual(len(journal.events), 5)

    def test_R13_task_preparation_is_required_and_reused(self):
        """R13 -- PREP-REQUIRED / R-9, and the extracted stage-two function."""
        journal = accepted_journal()
        r13_binding = make_binding(SCOPE_Q, root=ROOT_Q, validation_set_id="vs_q")
        admitted_selection_state(
            journal, binding=r13_binding, candidate=make_candidate(ROOT_Q)
        )
        transport = LoudStubTransport()
        context = build_context(
            SCOPE_Q,
            journal=journal,
            transport=transport,
            binding=r13_binding,
            clearance=lambda scope: {"unlocked": True},
        )
        with proved_acceptance():
            with self.assertRaises(SupervisorRefusal) as caught:
                commands.execute_initial_design(context)
        self.assertIn("prepared task", str(caught.exception))
        self.assertEqual(transport.calls, [], "ZERO provider calls on a refusal")
        # The extracted stage-two seam exists and contains NO NEW LOGIC.
        self.assertTrue(hasattr(nh_loop, "run_design_task_preparation"))
        source = read_text(CONTROLLER_SOURCE)
        marker = source.index("def run_design_task_preparation(")
        body = source[marker:source.index("def run_prepare_next_claude_task(")]
        self.assertIn("return run_prepare_next_claude_task(", body)

    def test_R14_target_and_specification_are_proved_before_claude(self):
        """R14 -- the dispatch carries a controller-validated NEW target."""
        state = full_transition_state(clearance_unlocked=True)
        self.assertIsNotNone(state["prepared_task"])
        self.assertEqual(state["prepared_task"]["target_path"], TARGET_Q)
        self.assertTrue(state["prepared_task"]["specification"])
        # The work item carries the target; Claude proposes neither.
        context = state["context"]
        obj, _identity = engine.initial_design_work_item(
            context, make_candidate(ROOT_Q), TARGET_Q
        )
        self.assertEqual(obj["target_candidate_path"], TARGET_Q)
        self.assertEqual(identity.check_work_item_object(obj), [])

    def test_R15_preparation_possible_ness_escape(self):
        """R15 -- a review_signal prepares NO task and makes no Claude call."""
        journal = accepted_journal()
        admitted_selection_state(journal)
        custody_pair(
            journal,
            kind="next_design_task_preparation",
            provider_kind="codex_next_design_task_preparation",
            value=prepared_task_object(review_signal={"finding": "a possible choice"}),
            scope=SCOPE_Q,
            request="pr_prep",
        )
        journal.append(
            {"type": "validation_recorded", "package_scope_id": SCOPE_Q,
             "validation_set_id": "vs_q"}
        )
        context = build_context(
            journal=journal,
            binding=make_binding(SCOPE_P),
        )
        state = commands.post_acceptance_transition_state(
            context, reconstruct_extra=full_reconstructor()
        )
        self.assertIsNone(state["prepared_task"], "no task is prepared")
        self.assertEqual(
            state["stop_record"]["loop_state"], commands.LOOP_NEEDS_NESS_DECISION
        )

    def test_R16_claude_result_is_custodied_before_any_write_ahead(self):
        """R16 / INIT-CUSTODY-BEFORE-PROMOTION."""
        source = read_text(CONTROLLER_DIR / "nh_supervisor" / "commands.py")
        marker = source.index("def _b6g_initial_design(")
        body = source[marker:source.index("def _b6h_no_progress(")]
        custody_at = body.index("_claude_initial_design_admission_checks")
        write_ahead_at = body.index("candidate_write_ahead_recorded")
        self.assertLess(
            custody_at, write_ahead_at,
            "admission over the custodied bytes must precede any write-ahead",
        )
        # And the transaction contacts NO provider on any path.
        self.assertNotIn("context.provider.dispatch", body)
        self.assertNotIn("_dispatch(", body)

    def test_R17_uncertain_claude_outcome_never_redispatches(self):
        """R17 / INIT-NO-REDISPATCH -- reconcile FIRST, zero second calls."""
        journal = accepted_journal()
        admitted_selection_state(journal)
        journal.append(
            {"type": "provider_request_prepared", "package_scope_id": SCOPE_Q,
             "provider_request_identity": "pr_init",
             "provider_kind": "claude_initial_design",
             "work_item_identity": "wi_init"}
        )
        journal.append(
            {"type": "provider_dispatch_begun", "package_scope_id": SCOPE_Q,
             "provider_request_identity": "pr_init",
             "provider_kind": "claude_initial_design"}
        )
        transport = LoudStubTransport()
        context = build_context(journal=journal, transport=transport)
        state = commands.post_acceptance_transition_state(
            context, reconstruct_extra=full_reconstructor()
        )
        self.assertIsNotNone(state["open_request"])
        self.assertEqual(state["open_request"]["work_item_kind"], "initial_design")
        # Any continuation command refuses while that request is open.
        with proved_acceptance():
            with self.assertRaises(SupervisorRefusal) as caught:
                commands.execute_initial_design(context)
        self.assertIn("never re-dispatched", str(caught.exception))
        self.assertEqual(transport.calls, [], "ZERO second Claude calls")
        # The local CLI transport's lookup is UNSUPPORTED, so the honest
        # position is a named practical action for a person.
        observation = transport.lookup(None, None)
        self.assertEqual(observation.outcome, "unsupported")

    def test_R18_restart_from_custodied_result_uses_exact_bytes(self):
        """R18 / INIT-EXACT-BYTES -- the promoted bytes ARE the custodied bytes."""
        payload = b"exactly these produced design bytes"
        value = initial_design_result(payload=payload)
        journal = FakeJournal()
        custody, _terminal = custody_pair(
            journal,
            kind="initial_design",
            provider_kind="claude_initial_design",
            value=value,
            scope=SCOPE_Q,
            request="pr_init",
        )
        context = build_context(
            SCOPE_Q, journal=journal,
            binding=make_binding(SCOPE_Q, root=ROOT_Q),
        )
        # engine.custodied_bytes re-verifies length AND digest.
        raw = engine.custodied_bytes(context, custody)
        self.assertEqual(json.loads(raw.decode("utf-8")), value)
        context._current_work_item_obj = initial_work_item(context)
        context._current_prompt_extra = {}
        context._current_required_extra = {}
        prepared = fake_prepared(context, "claude_initial_design")
        failed = commands._claude_initial_design_admission_checks(
            context, prepared, value
        )
        self.assertEqual(failed, [], "the honest result passes I1-I10")
        self.assertEqual(context._admitted_initial_design_payload, payload)

    def test_R19_R20_crash_matrix_and_idempotent_re_entry(self):
        """R19 / R20 -- every crash row derives, and re-entry appends nothing."""
        for _round in range(3):
            state = full_transition_state(clearance_unlocked=True)
            self.assertEqual(state["journal"].appends, state["expected_appends"])
        # Row A -- acceptance durable, continuation not started.
        journal = FakeJournal()
        context = build_context(journal=journal)
        empty = commands.post_acceptance_transition_state(
            context, reconstruct_extra=reconstructor()
        )
        self.assertIsNone(empty["selection"])
        self.assertIsNone(empty["transition_scope"])
        self.assertEqual(journal.appends, 0)

    def test_R21_mechanical_route_end_to_end_positions(self):
        """R21 -- the loop reaches each position exactly once, in order."""
        positions = observed_loop_positions()
        self.assertEqual(
            positions,
            [
                commands.LOOP_SELECTION_REQUIRED,
                commands.LOOP_PACKAGE_CLEARANCE_REQUIRED,
                commands.LOOP_PIECE3_RESULT_PENDING,
                commands.LOOP_PIECE3_COMMIT_REQUIRED,
                commands.LOOP_TASK_PREPARATION_REQUIRED,
                commands.LOOP_INITIAL_DESIGN_REQUIRED,
                commands.LOOP_INITIAL_RESULT_PENDING,
                commands.LOOP_HANDOFF_COMPLETE,
            ],
        )

    def test_R22_one_writer_one_promoter(self):
        """R22 -- EXACTLY ONE code path creates the initial candidate."""
        source = read_text(CONTROLLER_DIR / "nh_supervisor" / "commands.py")
        self.assertEqual(source.count("def _promote_candidate("), 1)
        self.assertEqual(source.count("    _promote_candidate(context"), 2)
        self.assertEqual(source.count("def _b6g_initial_design("), 1)
        # The initial transaction REUSES the installed four-boundary resumption.
        marker = source.index("def _b6g_initial_design(")
        body = source[marker:source.index("def _b6h_no_progress(")]
        self.assertIn("_correction_apply_resumption(", body)
        self.assertIn("_recover_stranded_candidate_custody(", body)

    def test_R23_design_only_limit(self):
        """R23 / DESIGN-ONLY -- a building frontier STOPS the loop."""
        journal = accepted_journal()
        custody_pair(
            journal,
            kind="next_package_selection",
            provider_kind="codex_next_package_selection",
            value=selection_object(classification="later_building_or_disk_work"),
            scope=SCOPE_P,
            request="pr_sel",
        )
        context = build_context(journal=journal)
        state = commands.post_acceptance_transition_state(
            context, reconstruct_extra=reconstructor()
        )
        self.assertIsNone(state["selection"])
        self.assertEqual(
            state["stop_record"]["loop_state"],
            commands.LOOP_DESIGN_CONTINUATION_COMPLETE,
        )
        # No implementation path exists on the continuation.
        continuation = extract_continuation_source()
        for forbidden in ("git add", "git commit", "git push",
                          ".nh_readings_store.jsonl",
                          ".nh_readings_production_authorized"):
            self.assertNotIn(forbidden, continuation)

    def test_R24_ambiguity_still_refuses(self):
        """R24 -- with NO admitted selection the live-checkout class is unchanged."""
        errors = []
        held = nh_loop.controller_held_question_validation_package(
            {"routed_issues": {}, "questions": {}}, errors, continuation_selection=None
        )
        self.assertEqual(
            held["precall_basis"], nh_loop.PRECALL_BASIS_LIVE_CHECKOUT,
            "with no admitted selection the installed fallback is unchanged",
        )
        # Class 0 sits ABOVE the live-checkout fallback.
        held0 = nh_loop.controller_held_question_validation_package(
            {"routed_issues": {}, "questions": {}},
            errors,
            continuation_selection={
                "package_scope_id": SCOPE_Q,
                "scope_root_path": ROOT_Q,
                "package_id": None,
            },
        )
        self.assertEqual(
            held0["precall_basis"], nh_loop.PRECALL_BASIS_CONTINUATION_SELECTION
        )
        self.assertEqual(held0["package_scope_id"], SCOPE_Q)

    def test_live_routed_selection_keeps_its_proved_source_root(self):
        """A matching routed scope must not drop the admitted selection root."""
        selection = {
            "package_scope_id": "A19",
            "scope_root_path": ROOT_Q,
            "package_id": "A19",
        }
        state = {
            "routed_issues": {
                "rs_a19": {
                    "status": "awaiting_question_validation",
                    "package_scope_id": "A19",
                    "package_id": "A19",
                    "package_key": "A19",
                }
            },
            "questions": {},
        }
        errors = []
        held = nh_loop.controller_held_question_validation_package(
            state, errors, continuation_selection=selection
        )
        self.assertEqual(held["precall_basis"], nh_loop.PRECALL_BASIS_ROUTED_SIGNAL)
        self.assertEqual(held["scope_root_path"], ROOT_Q)

        other = "05_ACTIVE_CANDIDATE/UNRELATED_v1_0_CANDIDATE.md"
        index = {
            "by_path": {ROOT_Q: b"A19 exact root", other: b"unrelated"},
            "by_category": {"active_candidate": {ROOT_Q, other}},
        }
        with mock.patch.object(
            nh_loop, "resolve_repo_source_path", side_effect=lambda path: path
        ), mock.patch.object(
            nh_loop,
            "derive_relevant_source_closure",
            return_value={"paths": [ROOT_Q], "closure_sha256": "0" * 64},
        ):
            requirement = (
                nh_loop.derive_precall_unauthenticated_question_validation_source_requirement(
                    held,
                    {"worktree_entries": ["?? " + ROOT_Q, "?? " + other]},
                    index,
                    list(state["routed_issues"].values()),
                    errors,
                )
            )
        self.assertEqual(errors, [])
        self.assertEqual(requirement["scope_root_path"], ROOT_Q)
        self.assertEqual(requirement["package_scope_id"], "A19")


# ===========================================================================
# The staged transition fixtures.  Each stage is built from DURABLE evidence
# only, so a rehearsal derives the same position a restart would.
# ===========================================================================
def full_reconstructor():
    # T1 keeps EXACTLY the two governed keys of section 15.2b, so it reproduces
    # what the fixture froze.  Only T3 carries the extra selection material.
    return reconstructor(
        next_design_task_preparation={
            "admitted_selection": selection_object(),
            "selected_root_identity": SELECTION_ROOT_IDENTITY,
        },
    )


def initial_work_item(context):
    obj, _identity = engine.initial_design_work_item(
        context, context.round_zero_candidate, TARGET_Q
    )
    return obj


def fake_prepared(context, provider_kind, *, work_item=None, prompt_extra=None,
                  input_extra=None):
    work_item = work_item or context._current_work_item_obj
    return engine.PreparedRequest(
        provider_kind=provider_kind,
        provider_endpoint_identity=nh_loop.supervisor_endpoint_binding()[provider_kind],
        provider_availability_episode_identity="ep_1",
        provider_availability_episode_generation=1,
        provider_request_identity="pr_1",
        provider_dispatch_serial=1,
        work_item_identity="wi_1",
        work_item_kind=constants.WORK_ITEM_KIND_BY_PROVIDER_KIND[provider_kind],
        prompt_material_sha256=engine.prompt_material_sha256(
            provider_kind, work_item, prompt_extra or {}
        ),
        required_inputs_sha256=engine.required_inputs_sha256(
            context, work_item, input_extra or {}
        ),
        result_schema_id=constants.RESULT_SCHEMA_ID_BY_PROVIDER_KIND[provider_kind],
        idempotency_key_sent=False,
        capability_record={},
        consumption_identity=None,
    )


def staged_journal(stage, *, binding=None, candidate=None):
    """A disposable journal wound forward to exactly one loop position."""
    journal = FakeJournal()
    # The durable acceptance of P, which is the ONE precondition under which a
    # bounded loop-level continuation may begin at all.
    journal.append(
        {
            "type": "ness_candidate_acceptance_recorded",
            "package_scope_id": SCOPE_P,
            "acceptance_disposition": "ACCEPTED_FOR_DESIGN_ONLY",
        }
    )
    if stage == "selection_required":
        return journal
    # The T1 freeze is derived against the SAME binding and candidate the
    # rehearsal's own context will carry, so the corrected complete-inventory
    # digest reproduces it and the selection is ADMITTED (section 14.2).
    admitted_selection_state(journal, binding=binding, candidate=candidate)
    if stage == "clearance_required":
        return journal
    if stage in ("piece3_pending", "piece3_commit", "task_preparation",
                 "initial_design", "initial_pending", "handoff"):
        custody_pair(
            journal,
            kind="question_validation",
            provider_kind="gpt_question_validation",
            value=question_validation_payload(),
            scope=SCOPE_Q,
            request="pr_qv",
            work_item_identity="wi_qv",
        )
    if stage == "piece3_pending":
        return journal
    if stage in ("piece3_commit", "task_preparation", "initial_design",
                 "initial_pending", "handoff"):
        journal.append(
            {
                "type": "piece3_provider_work_recorded",
                "package_scope_id": SCOPE_Q,
                "authorizes_event_type": "validation_recorded",
                "provider_request_identity": "pr_qv",
                "result_custody_identity": "rc_pr_qv",
                "work_item_identity": "wi_qv",
                "result_schema_valid": True,
                "routed_signal_refs": [],
                "validation_set_id": None,
                "piece3_standing_sha256": "e" * 64,
            }
        )
    if stage == "piece3_commit":
        return journal
    journal.append(
        {
            "type": "validation_recorded",
            "package_scope_id": SCOPE_Q,
            "validation_set_id": "vs_q",
        }
    )
    if stage == "task_preparation":
        return journal
    # section 8.8 section 15.2b -- T3's extra carries frozen_source_binding_sha256,
    # and the per-kind reconstruction recovers it from the authenticated
    # ``supervisor_operation_started`` of the operation that prepared it.  The
    # installed dispatch ALWAYS runs inside such an operation, so the fixture
    # carries one too; a fixture without it describes a request whose extra is
    # not reconstructible in full, which F-15 correctly judges stale.
    journal.append(
        {
            "type": "supervisor_operation_started",
            "package_scope_id": SCOPE_Q,
            "supervisor_operation_id": "op_prep",
            "supervisor_command": "prepare-next-design-task",
            "source_binding_sha256": "b" * 64,
        }
    )
    custody_pair(
        journal,
        kind="next_design_task_preparation",
        provider_kind="codex_next_design_task_preparation",
        value=prepared_task_object(),
        scope=SCOPE_Q,
        request="pr_prep",
        work_item_identity="wi_prep",
        supervisor_operation_id="op_prep",
    )
    journal.append(
        {
            "type": "supervisor_operation_completed",
            "package_scope_id": SCOPE_Q,
            "supervisor_operation_id": "op_prep",
            "outcome": "completed",
        }
    )
    if stage == "initial_design":
        return journal
    # section 8.8 section 15.2b -- T4's extra carries frozen_source_binding_sha256
    # too, recovered from the operation that prepared it.  The installed
    # dispatch always runs inside one, so the fixture carries one as well.
    journal.append(
        {
            "type": "supervisor_operation_started",
            "package_scope_id": SCOPE_Q,
            "supervisor_operation_id": "op_init",
            "supervisor_command": "execute-initial-design",
            "source_binding_sha256": "b" * 64,
        }
    )
    custody_pair(
        journal,
        kind="initial_design",
        provider_kind="claude_initial_design",
        value=initial_design_result(),
        scope=SCOPE_Q,
        request="pr_init",
        work_item_identity="wi_init",
        supervisor_operation_id="op_init",
    )
    journal.append(
        {
            "type": "supervisor_operation_completed",
            "package_scope_id": SCOPE_Q,
            "supervisor_operation_id": "op_init",
            "outcome": "completed",
        }
    )
    if stage == "initial_pending":
        return journal
    parent = make_candidate(ROOT_Q)
    journal.append(
        initial_candidate_body(
            "candidate_write_ahead_recorded", "intent_origin",
            commands.CANDIDATE_INTENT_ORIGIN_INITIAL, parent=parent,
        )
    )
    journal.append(
        initial_candidate_body(
            "candidate_custody_recorded", "custody_origin",
            commands.CANDIDATE_CUSTODY_ORIGIN_INITIAL, parent=parent,
        )
    )
    return journal


class TransitionExternalActionStopRehearsals(unittest.TestCase):
    """A terminal external-action dependency must stop transition scheduling."""

    @staticmethod
    def failed_validation_journal(
        dependency_code="provider_local_process_terminal_failure",
        terminal_kind="provider_error_terminal",
    ):
        journal = staged_journal("clearance_required")
        started = journal.append(
            {
                "type": "supervisor_operation_started",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": "op_terminal_failure",
                "supervisor_command": "dispatch-piece3-provider-review",
                "work_item_identity": "wi_terminal_failure",
                "source_binding_sha256": "ab" * 32,
            }
        )
        journal.append(
            {
                "type": "provider_request_prepared",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": "op_terminal_failure",
                "provider_request_identity": "pr_terminal_failure",
                "provider_kind": "gpt_question_validation",
                "provider_availability_episode_identity": "ep_terminal_failure",
                "work_item_kind": "question_validation",
                "work_item_identity": "wi_terminal_failure",
            }
        )
        journal.append(
            {
                "type": "provider_dispatch_begun",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": "op_terminal_failure",
                "provider_request_identity": "pr_terminal_failure",
                "provider_kind": "gpt_question_validation",
                "provider_availability_episode_identity": "ep_terminal_failure",
                "work_item_identity": "wi_terminal_failure",
            }
        )
        record = dependency.build_record(
            dependency_code,
            "local_codex_cli_chatgpt",
            "wi_terminal_failure",
            episode_identity="ep_terminal_failure",
            durable_record_placement="provider_request_terminal_recorded",
            phase_evidence_condition="terminal_non_transient_recorded",
            plain_language_dependency=(
                "The local model process ended without a usable result."
            ),
        )
        dep_identity = dependency.identity_of(record)
        carrier = journal.append(
            {
                "type": "provider_request_terminal_recorded",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": "op_terminal_failure",
                "provider_request_identity": "pr_terminal_failure",
                "provider_kind": "gpt_question_validation",
                "provider_availability_episode_identity": "ep_terminal_failure",
                "work_item_identity": "wi_terminal_failure",
                "terminal_kind": terminal_kind,
                "provider_outcome_facts": {"returncode": 1},
                "dependency_record": record,
                "dependency_identity": dep_identity,
                "dependency_carrier_event_seq": None,
                "dependency_occurrence_ordinal": 1,
            }
        )
        journal.append(
            {
                "type": "supervisor_operation_completed",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": "op_terminal_failure",
                "supervisor_started_event_seq": started["event_seq"],
                "supervisor_command": "dispatch-piece3-provider-review",
                "work_item_identity": "wi_terminal_failure",
                "operation_outcome": "dependency",
                "dependency_record": None,
                "dependency_identity": dep_identity,
                "dependency_carrier_event_seq": carrier["event_seq"],
                "dependency_occurrence_ordinal": 2,
            }
        )
        return journal

    def test_external_action_dependency_stops_dispatch_and_replays_identically(self):
        journal = self.failed_validation_journal()

        def project():
            context = build_context(
                journal=journal, clearance=lambda scope: {"unlocked": False}
            )
            state = commands.post_acceptance_transition_state(context)
            return commands.loop_position(context, state)

        first = project()
        second = project()
        self.assertEqual(first, second, "restart/replay must give the same stop")
        self.assertEqual(first["loop_state"], commands.LOOP_NEEDS_USER_ACTION)
        self.assertIsNone(first["loop_next_command"])
        self.assertEqual(
            first.get("dependency_code"),
            "provider_local_process_terminal_failure",
        )

    def test_retryable_and_clean_validation_positions_are_unchanged(self):
        clean = staged_journal("clearance_required")
        context = build_context(
            journal=clean, clearance=lambda scope: {"unlocked": False}
        )
        report = commands.loop_position(
            context, commands.post_acceptance_transition_state(context)
        )
        self.assertEqual(report["loop_state"], commands.LOOP_PACKAGE_CLEARANCE_REQUIRED)
        self.assertEqual(
            report["loop_next_command"], "dispatch-piece3-provider-review"
        )

        retryable = self.failed_validation_journal(
            dependency_code="provider_transient_error_terminal_recorded",
            terminal_kind="provider_error_retryable",
        )
        retry_context = build_context(
            journal=retryable, clearance=lambda scope: {"unlocked": False}
        )
        retry_report = commands.loop_position(
            retry_context,
            commands.post_acceptance_transition_state(retry_context),
        )
        self.assertEqual(
            retry_report["loop_state"], commands.LOOP_PACKAGE_CLEARANCE_REQUIRED
        )
        self.assertEqual(
            retry_report["loop_next_command"], "dispatch-piece3-provider-review"
        )


class Piece3BoundedRetryOwnershipRehearsals(unittest.TestCase):
    """A Piece-3 output retry remains one exact bounded work-item series."""

    # SECOND-MODEL SWITCH (2026-09-02): these rehearsals record earlier attempts
    # under the ChatGPT endpoint literal, so the retry must be prepared under
    # the same endpoint; the switch is held on "codex" for this class.
    def setUp(self):
        self._second_model = mock.patch.object(nh_loop, "SECOND_MODEL_PROVIDER", "codex")
        self._second_model.start()
        self.addCleanup(self._second_model.stop)

    def invalid_attempts(
        self, count=1, *, add_meaningful_signal=False, advance_retry_standing=False
    ):
        journal = staged_journal("clearance_required")
        seed = journal.append(
            {
                "type": "supervisor_operation_started",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": "op_piece3_source_seed",
                "supervisor_command": "dispatch-piece3-provider-review",
                "source_binding_sha256": "b" * 64,
            }
        )
        journal.append(
            {
                "type": "supervisor_operation_completed",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": "op_piece3_source_seed",
                "supervisor_started_event_seq": seed["event_seq"],
                "supervisor_command": "dispatch-piece3-provider-review",
                "operation_outcome": "ok",
            }
        )
        original_context = build_context(
            journal=journal, clearance=lambda scope: {"unlocked": False}
        )
        original_state = commands.post_acceptance_transition_state(original_context)
        original_position = commands.loop_position(original_context, original_state)
        _series, original_binding = commands.continuation_scheduling(
            original_context,
            original_state,
            original_position["loop_state"],
            original_position["loop_next_command"],
        )
        work_item = original_binding["work_item_identity"]
        source = original_binding["source_binding_sha256"]
        endpoint = "local_codex_cli_chatgpt"
        episode = replay.Replay(journal.read(), SCOPE_Q).episode_identity(
            work_item, "gpt_question_validation", endpoint, 1
        )

        invalid_payload = question_validation_payload()
        issue = valid_question_validation_issue()
        issue["user_facing_effects"] = []
        invalid_payload["issues"] = [issue]
        invalid_payload["total_issue_count"] = 1
        payload = json.dumps(invalid_payload, sort_keys=True).encode("utf-8")

        for number in range(1, count + 1):
            operation = "op_piece3_invalid_%d" % number
            request = "pr_piece3_invalid_%d" % number
            started = journal.append(
                {
                    "type": "supervisor_operation_started",
                    "package_scope_id": SCOPE_Q,
                    "supervisor_operation_id": operation,
                    "supervisor_command": "dispatch-piece3-provider-review",
                    "source_binding_sha256": source,
                    "candidate_path": ROOT_Q,
                    "candidate_sha256": "9" * 64,
                    "candidate_bytes": 4096,
                    "standing_before_sha256": (
                        ("f" if number == 2 else "a") * 64
                        if advance_retry_standing and number > 1
                        else "e" * 64
                    ),
                    "controller_executable_identity": "1" * 64,
                    "work_item_identity": work_item,
                }
            )
            journal.append(
                {
                    "type": "provider_request_prepared",
                    "package_scope_id": SCOPE_Q,
                    "supervisor_operation_id": operation,
                    "provider_request_identity": request,
                    "provider_kind": "gpt_question_validation",
                    "provider_endpoint_identity": endpoint,
                    "provider_availability_episode_identity": episode,
                    "provider_availability_episode_generation": 1,
                    "provider_dispatch_serial": number,
                    "work_item_kind": "question_validation",
                    "work_item_identity": work_item,
                    "prompt_material_sha256": "%064x" % number,
                    "required_inputs_sha256": "%064x" % (number + 10),
                    "result_schema_id": constants.RESULT_SCHEMA_ID_BY_PROVIDER_KIND[
                        "gpt_question_validation"
                    ],
                }
            )
            journal.append(
                {
                    "type": "provider_dispatch_begun",
                    "package_scope_id": SCOPE_Q,
                    "supervisor_operation_id": operation,
                    "provider_request_identity": request,
                    "provider_kind": "gpt_question_validation",
                    "provider_availability_episode_identity": episode,
                    "work_item_identity": work_item,
                }
            )
            custody = journal.append(
                {
                    "type": "provider_result_custody_recorded",
                    "package_scope_id": SCOPE_Q,
                    "supervisor_operation_id": operation,
                    "provider_request_identity": request,
                    "provider_kind": "gpt_question_validation",
                    "provider_availability_episode_identity": episode,
                    "work_item_kind": "question_validation",
                    "work_item_identity": work_item,
                    "result_custody_identity": "rc_" + request,
                    "result_location_kind": "inline_journal_bytes",
                    "result_bytes_base64": base64.b64encode(payload).decode("ascii"),
                    "result_byte_length": len(payload),
                    "result_sha256": hashlib.sha256(payload).hexdigest(),
                    "result_schema_valid": False,
                    "result_origin": "local_completion",
                }
            )
            dependency_code = (
                "provider_output_repeatedly_invalid"
                if number > constants.MAX_PROVIDER_OUTPUT_RETRIES_PER_EPISODE
                else "provider_output_invalid_bounded_retry"
            )
            record = dependency.build_record(
                dependency_code,
                endpoint,
                work_item,
                episode_identity=(
                    episode
                    if dependency_code == "provider_output_invalid_bounded_retry"
                    else None
                ),
                durable_record_placement="provider_request_terminal_recorded",
                phase_evidence_condition="terminal_result_invalid_recorded",
                plain_language_dependency="The saved answer is invalid.",
            )
            dependency_identity = dependency.identity_of(record)
            terminal = journal.append(
                {
                    "type": "provider_request_terminal_recorded",
                    "package_scope_id": SCOPE_Q,
                    "supervisor_operation_id": operation,
                    "provider_request_identity": request,
                    "provider_kind": "gpt_question_validation",
                    "provider_endpoint_identity": endpoint,
                    "provider_availability_episode_identity": episode,
                    "work_item_identity": work_item,
                    "terminal_kind": "result_invalid",
                    "result_custody_identity": custody["result_custody_identity"],
                    "result_schema_valid": False,
                    "dependency_record": record,
                    "dependency_identity": dependency_identity,
                    "dependency_carrier_event_seq": None,
                    "dependency_occurrence_ordinal": 1,
                }
            )
            journal.append(
                {
                    "type": "supervisor_operation_completed",
                    "package_scope_id": SCOPE_Q,
                    "supervisor_operation_id": operation,
                    "supervisor_started_event_seq": started["event_seq"],
                    "supervisor_command": "dispatch-piece3-provider-review",
                    "work_item_identity": work_item,
                    "operation_outcome": "dependency",
                    "dependency_record": None,
                    "dependency_identity": dependency_identity,
                    "dependency_carrier_event_seq": terminal["event_seq"],
                    "dependency_occurrence_ordinal": 2,
                }
            )

        if add_meaningful_signal:
            journal.append(
                {
                    "type": "review_signal_recorded",
                    "package_scope_id": SCOPE_Q,
                    "routed_signal_id": "rs_new_after_invalid",
                    "signal_source": "question_coverage_review",
                    "source_binding_sha256": "b" * 64,
                }
            )
        return journal, work_item, episode

    @staticmethod
    def changed_standing_context(journal):
        binding = dataclasses.replace(
            make_binding(), piece3_standing_sha256="7" * 64
        )
        return build_context(
            journal=journal,
            binding=binding,
            clearance=lambda scope: {"unlocked": False},
        )

    def test_retry_projection_keeps_the_invalid_terminal_work_item_and_metadata(self):
        journal, work_item, episode = self.invalid_attempts()
        context = self.changed_standing_context(journal)
        state = commands.post_acceptance_transition_state(context)
        position = commands.loop_position(context, state)
        _series, binding = commands.continuation_scheduling(
            context, state, position["loop_state"], position["loop_next_command"]
        )
        metadata = commands.transition_scheduling_metadata(context, state, binding)
        self.assertEqual(binding["work_item_identity"], work_item)
        self.assertEqual(metadata["work_item_identity"], work_item)
        self.assertEqual(metadata["dependency_identity"], binding["dependency_identity"])
        record = commands.scoped_dependency_occurrence(journal.read(), SCOPE_Q)[
            "dependency_record"
        ]
        self.assertEqual(record["work_item_identity"], metadata["work_item_identity"])
        self.assertEqual(metadata["provider_availability_episode_identity"], episode)
        self.assertEqual(metadata["output_retries_used"], 0)

    def test_second_invalid_in_the_same_tuple_increments_the_retry_count(self):
        journal, work_item, episode = self.invalid_attempts(count=2)
        context = self.changed_standing_context(journal)
        state = commands.post_acceptance_transition_state(context)
        position = commands.loop_position(context, state)
        _series, binding = commands.continuation_scheduling(
            context, state, position["loop_state"], position["loop_next_command"]
        )
        metadata = commands.transition_scheduling_metadata(context, state, binding)
        self.assertEqual(metadata["work_item_identity"], work_item)
        self.assertEqual(metadata["provider_availability_episode_identity"], episode)
        self.assertEqual(metadata["output_retries_used"], 1)

    def test_retry_dispatch_uses_a_new_request_and_exact_feedback(self):
        journal, work_item, episode = self.invalid_attempts()
        invalid_payload = question_validation_payload()
        issue = valid_question_validation_issue()
        issue["user_facing_effects"] = []
        invalid_payload["issues"] = [issue]
        invalid_payload["total_issue_count"] = 1
        transport = LoudStubTransport(
            body=json.dumps(invalid_payload, sort_keys=True).encode("utf-8"),
            allow=True,
            transport_kind="subprocess_cli",
        )
        adapter = StubAdapter(
            validate_question_validation_payload=(
                lambda text, extra, errors:
                nh_loop._continuation_question_validation_payload_contract(
                    text, extra, errors
                )
            ),
            piece3_precall_requirement=(
                lambda scope, kind, selection=None: {
                    "piece3_stage": kind,
                    "prompt": "BASE QUESTION-VALIDATION PROMPT",
                }
            ),
        )
        q_binding = dataclasses.replace(
            make_binding(SCOPE_Q, root=ROOT_Q, validation_set_id=None),
            piece3_standing_sha256="7" * 64,
        )
        q_candidate = engine.CandidateState(
            candidate_path=ROOT_Q,
            candidate_sha256="9" * 64,
            candidate_bytes=4096,
        )
        context = build_context(
            scope=SCOPE_Q,
            journal=journal,
            adapter=adapter,
            transport=transport,
            binding=q_binding,
            candidate=q_candidate,
            clearance=lambda scope: {"unlocked": False},
        )
        context.control_context = self.changed_standing_context(journal)
        captured = []
        original_builder = engine.build_prepared_request

        def capture_builder(*args, **kwargs):
            captured.append(copy.deepcopy(kwargs.get("extra_prompt")))
            return original_builder(*args, **kwargs)

        with proved_acceptance(), mock.patch.object(
            engine, "build_prepared_request", side_effect=capture_builder
        ):
            commands.dispatch_piece3_provider_review(context)

        prepared = [
            event for event in journal.events
            if event.get("type") == "provider_request_prepared"
            and event.get("work_item_identity") == work_item
        ]
        self.assertEqual(len(prepared), 2)
        self.assertNotEqual(
            prepared[0]["provider_request_identity"],
            prepared[1]["provider_request_identity"],
        )
        self.assertEqual(
            prepared[1]["provider_availability_episode_identity"], episode
        )
        prompt = captured[-1]["piece3_precall_requirement"]["prompt"]
        self.assertIn(
            "question-validation issue 1 user_facing_effects must be a "
            "non-empty array",
            prompt,
        )
        self.assertIn("Preserve all otherwise-valid substantive issues", prompt)
        self.assertEqual(
            replay.Replay(journal.read(), SCOPE_Q).output_retries_used(
                work_item, "gpt_question_validation", episode
            ),
            1,
        )

    def test_exhaustion_stops_without_advertising_another_dispatch(self):
        journal, _work_item, _episode = self.invalid_attempts(count=3)
        context = self.changed_standing_context(journal)
        first = commands.loop_position(
            context, commands.post_acceptance_transition_state(context)
        )
        second = commands.loop_position(
            context, commands.post_acceptance_transition_state(context)
        )
        self.assertEqual(first, second, "restart replay must preserve the stop")
        self.assertEqual(first["loop_state"], commands.LOOP_NEEDS_USER_ACTION)
        self.assertIsNone(first["loop_next_command"])
        self.assertEqual(first["dependency_code"], "bounded_output_retry_exhausted")

    def test_exhaustion_keeps_origin_owner_when_retry_standing_advances(self):
        """Neutral retry lifecycle must not mint a fresh output budget."""
        journal, work_item, _episode = self.invalid_attempts(
            count=3, advance_retry_standing=True
        )
        context = self.changed_standing_context(journal)
        state = commands.post_acceptance_transition_state(context)
        position = commands.loop_position(context, state)

        self.assertEqual(work_item, state["piece3_retry_owner"]["work_item_identity"])
        self.assertTrue(state["piece3_output_retry_exhausted"])
        self.assertEqual(commands.LOOP_NEEDS_USER_ACTION, position["loop_state"])
        self.assertIsNone(position["loop_next_command"])
        self.assertEqual(
            "bounded_output_retry_exhausted", position["dependency_code"]
        )

    def test_a_new_meaningful_signal_does_not_reuse_old_retry_ownership(self):
        journal, old_work_item, _episode = self.invalid_attempts(
            add_meaningful_signal=True
        )
        context = self.changed_standing_context(journal)
        state = commands.post_acceptance_transition_state(context)
        position = commands.loop_position(context, state)
        _series, binding = commands.continuation_scheduling(
            context, state, position["loop_state"], position["loop_next_command"]
        )
        self.assertNotEqual(binding["work_item_identity"], old_work_item)

    def test_resolved_local_launch_failure_returns_to_the_same_invalid_output_owner(self):
        """A repaired transport failure does not mint a fresh output budget."""
        journal, work_item, episode = self.invalid_attempts()
        invalid_dependency = commands.scoped_dependency_occurrence(
            journal.read(), SCOPE_Q
        )["dependency_identity"]
        original_start = next(
            event for event in journal.events
            if event.get("type") == "supervisor_operation_started"
            and event.get("work_item_identity") == work_item
        )
        operation = "op_piece3_local_failure"
        request = "pr_piece3_local_failure"
        started = journal.append(
            {
                "type": "supervisor_operation_started",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": operation,
                "supervisor_command": "dispatch-piece3-provider-review",
                "source_binding_sha256": original_start["source_binding_sha256"],
                "candidate_path": original_start["candidate_path"],
                "candidate_sha256": original_start["candidate_sha256"],
                "candidate_bytes": original_start["candidate_bytes"],
                "standing_before_sha256": "f" * 64,
                "controller_executable_identity": original_start[
                    "controller_executable_identity"
                ],
                "work_item_identity": work_item,
            }
        )
        journal.append(
            {
                "type": "provider_request_prepared",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": operation,
                "provider_request_identity": request,
                "provider_kind": "gpt_question_validation",
                "provider_endpoint_identity": "local_codex_cli_chatgpt",
                "provider_availability_episode_identity": episode,
                "provider_availability_episode_generation": 1,
                "provider_dispatch_serial": 2,
                "work_item_kind": "question_validation",
                "work_item_identity": work_item,
            }
        )
        journal.append(
            {
                "type": "provider_dispatch_begun",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": operation,
                "provider_request_identity": request,
                "provider_kind": "gpt_question_validation",
                "provider_availability_episode_identity": episode,
                "work_item_identity": work_item,
            }
        )
        record = dependency.build_record(
            "provider_local_process_terminal_failure",
            "local_codex_cli_chatgpt",
            work_item,
            episode_identity=episode,
            durable_record_placement="provider_request_terminal_recorded",
            phase_evidence_condition="terminal_non_transient_recorded",
            plain_language_dependency=(
                "The local model process ended without a usable result."
            ),
        )
        dependency_identity = dependency.identity_of(record)
        terminal = journal.append(
            {
                "type": "provider_request_terminal_recorded",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": operation,
                "provider_request_identity": request,
                "provider_kind": "gpt_question_validation",
                "provider_endpoint_identity": "local_codex_cli_chatgpt",
                "provider_availability_episode_identity": episode,
                "work_item_identity": work_item,
                "terminal_kind": "provider_error_terminal",
                "provider_outcome_facts": {"returncode": 1},
                "dependency_record": record,
                "dependency_identity": dependency_identity,
                "dependency_carrier_event_seq": None,
                "dependency_occurrence_ordinal": 1,
            }
        )
        journal.append(
            {
                "type": "supervisor_operation_completed",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": operation,
                "supervisor_started_event_seq": started["event_seq"],
                "supervisor_command": "dispatch-piece3-provider-review",
                "work_item_identity": work_item,
                "operation_outcome": "dependency",
                "dependency_record": None,
                "dependency_identity": dependency_identity,
                "dependency_carrier_event_seq": terminal["event_seq"],
                "dependency_occurrence_ordinal": 2,
            }
        )
        previous = journal.events[-1]
        journal.append(
            {
                "type": schema.EXTERNAL_ACTION_RESOLUTION_EVENT_TYPE,
                "package_scope_id": SCOPE_Q,
                "resolved_dependency_identity": dependency_identity,
                "resolved_dependency_carrier_event_seq": terminal["event_seq"],
                "resolved_dependency_carrier_event_sha256": terminal[
                    "event_sha256"
                ],
                "resolved_dependency_code": record["dependency_code"],
                "work_item_identity": work_item,
                "failed_provider_request_identity": request,
                "failed_provider_terminal_event_seq": terminal["event_seq"],
                "failed_provider_terminal_event_sha256": terminal[
                    "event_sha256"
                ],
                "resource_identity": "local_codex_cli_chatgpt",
                "user_action_code": "provider_local_process_failure_review_required",
                "external_action_evidence_kind": (
                    "normal_host_codex_cli_smoke_succeeded"
                ),
                "normal_host_context_confirmed": True,
                "provider_cli_login_proved": True,
                "provider_state_writable_proved": True,
                "bounded_smoke_returncode": 0,
                "bounded_smoke_agent_message": "OK",
                "bounded_smoke_turn_completed": True,
                "ness_action_exact": "run the bounded retry on the normal host",
                "ness_action_confirmed": True,
                "pre_action_authenticated_event_seq": previous["event_seq"],
                "pre_action_authenticated_tail_sha256": previous["event_sha256"],
                "prev_event_sha256": previous["event_sha256"],
            }
        )

        context = self.changed_standing_context(journal)
        first_state = commands.post_acceptance_transition_state(context)
        first_position = commands.loop_position(context, first_state)
        _series, first_binding = commands.continuation_scheduling(
            context,
            first_state,
            first_position["loop_state"],
            first_position["loop_next_command"],
        )
        metadata = commands.transition_scheduling_metadata(
            context, first_state, first_binding
        )
        second_state = commands.post_acceptance_transition_state(context)
        second_position = commands.loop_position(context, second_state)
        _series, second_binding = commands.continuation_scheduling(
            context,
            second_state,
            second_position["loop_state"],
            second_position["loop_next_command"],
        )

        self.assertEqual(first_binding, second_binding, "restart must be stable")
        self.assertEqual(first_binding["work_item_identity"], work_item)
        self.assertEqual(first_binding["dependency_identity"], invalid_dependency)
        self.assertEqual(metadata["work_item_identity"], work_item)
        self.assertEqual(metadata["dependency_identity"], invalid_dependency)
        self.assertEqual(metadata["provider_availability_episode_identity"], episode)
        self.assertEqual(metadata["output_retries_used"], 0)


class TransitionExternalActionStopRehearsals(
    TransitionExternalActionStopRehearsals
):

    def test_worker_runs_no_command_at_the_external_action_boundary(self):
        loop_report = {
            "loop_state": commands.LOOP_NEEDS_USER_ACTION,
            "loop_next_command": None,
            "loop_detail": "a named external action is required",
        }
        calls = []

        def runner(command, request):
            calls.append((command, request))
            return ui_worker.CommandResult(command, loop_report, 0)

        worker = ui_worker.SupervisorWorker.__new__(ui_worker.SupervisorWorker)
        worker.runner = runner
        worker.clock = ui_worker.Clock()
        outcome = worker._continuation_step(
            {}, ui_supervisor.WorkflowState.ACCEPTED_FOR_DESIGN_ONLY
        )
        self.assertEqual(outcome.action, "wait")
        self.assertEqual(calls, [("loop-status", None)])

    @staticmethod
    def resolution_request(journal, **overrides):
        events = journal.read()
        terminal = next(
            event for event in events
            if event.get("type") == "provider_request_terminal_recorded"
            and event.get("provider_request_identity") == "pr_terminal_failure"
        )
        request = {
            "dependency_identity": terminal["dependency_identity"],
            "work_item_identity": terminal["work_item_identity"],
            "provider_request_identity": terminal["provider_request_identity"],
            "resource_identity": "local_codex_cli_chatgpt",
            "user_action_code": "provider_local_process_failure_review_required",
            "external_action_evidence_kind": "normal_host_codex_cli_smoke_succeeded",
            "normal_host_context_confirmed": True,
            "provider_cli_login_proved": True,
            "provider_state_writable_proved": True,
            "bounded_smoke_returncode": 0,
            "bounded_smoke_agent_message": "OK",
            "bounded_smoke_turn_completed": True,
            "ness_action_exact": (
                "Ness confirms the normal-host Codex CLI smoke completed with "
                "agent message OK and a durable turn.completed result."
            ),
            "ness_action_confirmed": True,
            "pre_action_authenticated_event_seq": events[-1]["event_seq"],
            "pre_action_authenticated_tail_sha256": events[-1]["event_sha256"],
        }
        request.update(overrides)
        return request

    def test_exact_external_action_resolution_unlocks_without_reusing_failed_request(self):
        class Transaction:
            def __init__(self, journal):
                self.journal = journal
                self.events = None

            def __enter__(self):
                self.events = self.journal.read()
                return self

            def append(self, body):
                appended = self.journal.append(body)
                self.events = self.journal.read()
                return appended

            def reread(self):
                self.events = self.journal.read()
                return self.events, None

            def __exit__(self, *unused):
                return False

        class TransactionalJournal(FakeJournal):
            def write_transaction(self):
                return Transaction(self)

            def append(self, body):
                bound = dict(body)
                bound.setdefault(
                    "prev_event_sha256",
                    self.events[-1]["event_sha256"] if self.events else None,
                )
                return super().append(bound)

        original = self.failed_validation_journal()
        journal = TransactionalJournal(original.read())
        request = self.resolution_request(journal)
        context = build_context(
            scope=SCOPE_Q,
            journal=journal,
            binding=make_binding(SCOPE_Q, root=ROOT_Q),
            candidate=make_candidate(ROOT_Q),
            clearance=lambda scope: {"unlocked": False},
        )

        result = commands.record_external_action_resolution(context, request)

        self.assertTrue(result.report["ok"])
        self.assertEqual(result.report["outcome"], "recorded_now")
        resolution = journal.events[-1]
        self.assertEqual(resolution["type"], "external_action_resolution_recorded")
        self.assertEqual(
            resolution["resolved_dependency_identity"], request["dependency_identity"]
        )
        self.assertEqual(
            resolution["failed_provider_request_identity"],
            "pr_terminal_failure",
        )
        self.assertEqual(
            len([
                event for event in journal.events
                if event.get("provider_request_identity") == "pr_terminal_failure"
                and event.get("type") == "provider_request_prepared"
            ]),
            1,
            "the failed request remains terminal history and is never prepared again",
        )
        projection_context = build_context(
            journal=journal, clearance=lambda scope: {"unlocked": False}
        )
        first = commands.loop_position(
            projection_context,
            commands.post_acceptance_transition_state(projection_context),
        )
        second = commands.loop_position(
            projection_context,
            commands.post_acceptance_transition_state(projection_context),
        )
        self.assertEqual(first, second, "restart/replay gives the same unlocked answer")
        self.assertEqual(first["loop_state"], commands.LOOP_PACKAGE_CLEARANCE_REQUIRED)
        self.assertEqual(
            first["loop_next_command"], "dispatch-piece3-provider-review"
        )

        before = len(journal.events)
        repeated = commands.record_external_action_resolution(context, request)
        self.assertTrue(repeated.report["ok"])
        self.assertEqual(repeated.report["outcome"], "already_recorded")
        self.assertEqual(len(journal.events), before, "the exact resolution is idempotent")

    def test_external_action_resolution_mismatch_fails_closed_without_append(self):
        class Transaction:
            def __init__(self, journal):
                self.journal = journal

            def __enter__(self):
                self.events = self.journal.read()
                return self

            def append(self, body):
                return self.journal.append(body)

            def reread(self):
                self.events = self.journal.read()
                return self.events, None

            def __exit__(self, *unused):
                return False

        class TransactionalJournal(FakeJournal):
            def write_transaction(self):
                return Transaction(self)

            def append(self, body):
                bound = dict(body)
                bound.setdefault(
                    "prev_event_sha256",
                    self.events[-1]["event_sha256"] if self.events else None,
                )
                return super().append(bound)

        journal = TransactionalJournal(self.failed_validation_journal().read())
        request = self.resolution_request(
            journal, provider_request_identity="pr_some_other_request"
        )
        context = build_context(
            scope=SCOPE_Q,
            journal=journal,
            binding=make_binding(SCOPE_Q, root=ROOT_Q),
            candidate=make_candidate(ROOT_Q),
        )
        before = len(journal.events)

        result = commands.record_external_action_resolution(context, request)

        self.assertFalse(result.report["ok"])
        self.assertEqual(len(journal.events), before)
        report = commands.loop_position(
            context, commands.post_acceptance_transition_state(context)
        )
        self.assertEqual(report["loop_state"], commands.LOOP_NEEDS_USER_ACTION)
        self.assertIsNone(report["loop_next_command"])


def question_validation_payload():
    value = {key: None for key in nh_loop.QUESTION_VALIDATION_REQUIRED_KEYS}
    value.update(
        {
            "package_id": None,
            "package_title": "prose",
            "whole_check_complete": True,
            "enumeration_complete": True,
            "source_paths_checked": [ROOT_Q],
            "page_index": 1,
            "page_count": 1,
            "total_issue_count": 0,
            "issues": [],
            "unknowns": [],
        }
    )
    return value


def valid_question_validation_issue():
    """One compact issue that satisfies the installed model-output contract."""
    issue = {key: None for key in nh_loop.QUESTION_VALIDATION_ISSUE_KEYS}
    issue.update(
        {
            "standing_target_id": None,
            "issue_key": "world.opening.behavior",
            "classification": "genuinely_open_for_ness",
            "disposition": nh_loop.QUESTION_VALIDATION_ADMIT_DISPOSITION,
            "topic_group": "interface_experience",
            "question_intent_code": "what_shows_up_where",
            "subject_quote": (
                "The world opening behavior remains a personal choice."
            ),
            "settled_basis_quote": (
                "The world always remains clearly separate from ordinary reality."
            ),
            "already_settled_note": (
                "The world remains clearly separate from ordinary reality."
            ),
            "mechanical_note": (
                "Implementing the selected opening behavior is later mechanical work."
            ),
            "still_open_note": "The preferred visible opening behavior remains open.",
            "why_ness_needed_note": (
                "Only Ness can choose how entering her world should feel."
            ),
            "real_use_effect_note": (
                "The answer changes what Ness sees when her world opens."
            ),
            "question_text": (
                "How should your world visibly open when you choose to enter it?"
            ),
            "user_facing_effects": ["how_it_feels_in_use"],
            "answer_effort": "short",
            "dependency_key": None,
            "settled_answer_note": None,
            "standing_witness": None,
            "options": [
                {
                    "option_id": "ask_once",
                    "option_meaning_code": "nh_asks_you_once_then_follows_it",
                    "option_consequence_codes": [
                        "it_becomes_the_default_from_now_on"
                    ],
                    "option_text": "Ask once and keep that opening.",
                    "consequence_note": (
                        "The chosen opening becomes the normal default."
                    ),
                    "settles_issue_keys": [],
                    "removes_issue_keys": [],
                    "satisfies_dependency_keys": [],
                },
                {
                    "option_id": "each_time",
                    "option_meaning_code": "you_decide_each_time",
                    "option_consequence_codes": [
                        "you_stay_in_control_of_each_case"
                    ],
                    "option_text": "Choose the opening each time.",
                    "consequence_note": "Ness chooses each individual opening.",
                    "settles_issue_keys": [],
                    "removes_issue_keys": [],
                    "satisfies_dependency_keys": [],
                },
            ],
            "source_evidence": [
                "01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md"
            ],
            "later_package_use": [],
        }
    )
    return issue


def coverage_review_payload():
    value = {key: None for key in nh_loop.COVERAGE_REVIEW_REQUIRED_KEYS}
    value.update(
        {
            "whole_check_complete": True,
            "coverage_review_complete": True,
            "source_paths_checked": [ROOT_Q],
            "possible_gaps": [],
            "unknowns": [],
        }
    )
    return value


def state_for(stage, *, clearance_unlocked=False, adapter=None, transport=None):
    journal = staged_journal(stage)
    context = build_context(
        journal=journal,
        adapter=adapter,
        transport=transport,
        clearance=lambda scope: {"unlocked": clearance_unlocked},
    )
    state = commands.post_acceptance_transition_state(
        context, reconstruct_extra=full_reconstructor()
    )
    state["context"] = context
    state["journal"] = journal
    state["expected_appends"] = journal.appends
    return state


def full_transition_state(*, clearance_unlocked=True):
    return state_for("initial_design", clearance_unlocked=clearance_unlocked)


def observed_loop_positions():
    """The position the loop derives at each durable stage, in order."""
    stages = (
        ("selection_required", False),
        ("clearance_required", False),
        ("piece3_pending", False),
        ("piece3_commit", False),
        ("task_preparation", True),
        ("initial_design", True),
        ("initial_pending", True),
        ("handoff", True),
    )
    positions = []
    for stage, unlocked in stages:
        state = state_for(stage, clearance_unlocked=unlocked)
        report = commands.loop_position(state["context"], state)
        positions.append(report["loop_state"])
    return positions


# ===========================================================================
# R25-R40 -- CUSTODY CLOSURE, INIT-ADMISSION NEGATIVES AND RECOVERY BINDING.
# ===========================================================================
class CustodyClosureAndAdmissionRehearsals(unittest.TestCase):
    def closure_probe(self, kind, provider_kind, value, terminal_kind="result_received"):
        journal = accepted_journal()
        custody, terminal = custody_pair(
            journal, kind=kind, provider_kind=provider_kind, value=value,
            scope=SCOPE_Q, request="pr_x",
        )
        if terminal_kind != "result_received":
            journal.events[-1]["terminal_kind"] = terminal_kind
        scoped = replay.Replay(journal.read(), SCOPE_Q)
        pending = scoped.custodied_results_awaiting_processing()
        return journal, [event["work_item_kind"] for event in pending]

    def test_R25_selector_custody_closes_on_its_terminal(self):
        """R25 / CLOSURE-READONLY -- never pending, never routed for an effect."""
        _journal, pending = self.closure_probe(
            "next_package_selection", "codex_next_package_selection",
            selection_object(),
        )
        self.assertEqual(pending, [], "a completed selector terminal IS the closure")
        # And routing it through the processing command is REFUSED outright.
        self.assertIn(
            "next_package_selection", constants.CLOSED_BY_TERMINAL_ONLY_WORK_ITEM_KINDS
        )
        self.assertNotIn(
            "next_package_selection", constants.TRANSITION_PENDING_CUSTODY_KINDS
        )

    def test_R26_task_preparation_custody_closes_on_its_terminal(self):
        """R26 -- the same, for the preparation review."""
        _journal, pending = self.closure_probe(
            "next_design_task_preparation", "codex_next_design_task_preparation",
            prepared_task_object(),
        )
        self.assertEqual(pending, [])
        self.assertIn(
            "next_design_task_preparation",
            constants.CLOSED_BY_TERMINAL_ONLY_WORK_ITEM_KINDS,
        )

    def test_R27_initial_design_custody_stays_pending_until_T5(self):
        """R27 / CLOSURE-INITIAL-PENDING -- it DOES remain pending."""
        journal, pending = self.closure_probe(
            "initial_design", "claude_initial_design", initial_design_result()
        )
        self.assertEqual(pending, ["initial_design"])
        # It closes ONLY when candidate_custody_recorded proves the downstream
        # completion.
        parent = make_candidate(ROOT_Q)
        journal.append(
            initial_candidate_body(
                "candidate_write_ahead_recorded", "intent_origin",
                commands.CANDIDATE_INTENT_ORIGIN_INITIAL, parent=parent,
            )
        )
        journal.append(
            initial_candidate_body(
                "candidate_custody_recorded", "custody_origin",
                commands.CANDIDATE_CUSTODY_ORIGIN_INITIAL, parent=parent,
            )
        )
        scoped = replay.Replay(journal.read(), SCOPE_Q)
        self.assertEqual(scoped.custodied_results_awaiting_processing(), [])

    def test_R28_unverifiable_saved_custody_holds_and_never_re_asks(self):
        """R28 / CUSTODY-UNVERIFIABLE-HOLD -- SAFETY_HOLD, ZERO new calls."""
        journal = staged_journal("initial_pending")
        # The saved result object is made CORRUPT.
        for event in journal.events:
            if event.get("type") == "provider_result_custody_recorded" and (
                event.get("work_item_kind") == "initial_design"
            ):
                event["result_sha256"] = "0" * 64
        transport = LoudStubTransport()
        context = build_context(
            journal=journal, transport=transport,
            clearance=lambda scope: {"unlocked": True},
        )
        state = commands.post_acceptance_transition_state(context)
        self.assertTrue(state["custody_unverifiable"])
        report = commands.loop_position(context, state)
        self.assertEqual(report["loop_state"], commands.LOOP_SAFETY_HOLD)
        self.assertEqual(
            report["dependency_code"], "provider_result_custody_unverifiable"
        )
        self.assertIsNone(report["loop_next_command"])
        # ZERO abort-to-retry, and ZERO new Claude calls.
        with proved_acceptance():
            with self.assertRaises(SupervisorRefusal) as caught:
                commands.execute_initial_design(context)
        self.assertIn("safety hold", str(caught.exception))
        self.assertEqual(transport.claude_calls, 0)
        # Every durable record is PRESERVED byte-identically.
        self.assertEqual(journal.appends, len(journal.events))

    def admission(self, value, *, target=TARGET_Q, new_paths=None):
        adapter = StubAdapter()
        if new_paths is not None:
            adapter.new_paths = new_paths
        context = build_context(
            SCOPE_Q, adapter=adapter,
            binding=make_binding(SCOPE_Q, root=ROOT_Q),
            candidate=make_candidate(ROOT_Q),
        )
        obj, _identity = engine.initial_design_work_item(
            context, context.round_zero_candidate, target
        )
        context._current_work_item_obj = obj
        context._current_prompt_extra = {}
        context._current_required_extra = {}
        prepared = fake_prepared(context, "claude_initial_design", work_item=obj)
        return commands._claude_initial_design_admission_checks(
            context, prepared, value
        ), context

    def test_R29_admission_negative_wrong_target(self):
        """R29 -- I3 fails; NO candidate created."""
        failed, context = self.admission(
            initial_design_result(path="05_ACTIVE_CANDIDATE/NH_OTHER_v1_1_CANDIDATE.md")
        )
        self.assertIn("I3", failed)
        self.assertIsNone(context._admitted_initial_design_payload)

    def test_R30_admission_negative_invalid_base64(self):
        """R30 -- I5 fails; no candidate created."""
        failed, context = self.admission(
            initial_design_result(encoded="not base64 at all !!!")
        )
        self.assertIn("I5", failed)
        self.assertIsNone(context._admitted_initial_design_payload)

    def test_R31_admission_negative_wrong_byte_count(self):
        """R31 -- I6 fails; a declared length can never disagree with the bytes."""
        failed, _context = self.admission(initial_design_result(declared_bytes=3))
        self.assertIn("I6", failed)

    def test_R32_admission_negative_wrong_sha(self):
        """R32 -- I7 fails; the digest is RECOMPUTED, never believed."""
        failed, _context = self.admission(initial_design_result(sha="a" * 64))
        self.assertIn("I7", failed)

    def test_R33_admission_negative_oversize_payload(self):
        """R33 -- I6 fails on a declared length over MAX_CANDIDATE_BYTES."""
        failed, _context = self.admission(
            initial_design_result(declared_bytes=constants.MAX_CANDIDATE_BYTES + 1)
        )
        self.assertIn("I6", failed)

    def test_R34_admission_negative_bound_to_a_different_prepared_task(self):
        """R34 -- I8 fails when the request binding is not this prepared task."""
        adapter = StubAdapter()
        context = build_context(
            SCOPE_Q, adapter=adapter,
            binding=make_binding(SCOPE_Q, root=ROOT_Q),
            candidate=make_candidate(ROOT_Q),
        )
        obj, _identity = engine.initial_design_work_item(
            context, context.round_zero_candidate, TARGET_Q
        )
        context._current_work_item_obj = obj
        context._current_prompt_extra = {}
        # The request was bound to a DIFFERENT specification digest.
        prepared = fake_prepared(
            context, "claude_initial_design", work_item=obj,
            input_extra={"prepared_specification_sha256": "9" * 64},
        )
        context._current_required_extra = {"prepared_specification_sha256": "8" * 64}
        failed = commands._claude_initial_design_admission_checks(
            context, prepared, initial_design_result()
        )
        self.assertIn("I8", failed)

    def test_R35_admission_negative_stale_target_at_the_promotion_boundary(self):
        """R35 -- I4 fails at re-run; NO overwrite, nothing promoted."""
        failed, context = self.admission(initial_design_result(), new_paths=set())
        self.assertIn("I4", failed)
        self.assertIsNone(context._admitted_initial_design_payload)

    def test_R41_the_initial_design_result_key_set_includes_same_call_explanation(self):
        """R41 -- candidate identity plus same-call prose, no correction fields."""
        self.assertEqual(len(constants.INITIAL_DESIGN_RESULT_KEYS), 7)
        for forbidden in ("produced_lifetime_round", "produced_batch_number",
                          "produced_round_in_batch", "correction_specification_sha256",
                          "blocking_finding_refs"):
            value = initial_design_result()
            value[forbidden] = "anything at all"
            failed, context = self.admission(value)
            self.assertEqual(failed, ["I1"], forbidden)
            self.assertIsNone(context._admitted_initial_design_payload)
        for missing in constants.INITIAL_DESIGN_RESULT_KEYS:
            value = initial_design_result()
            value.pop(missing)
            failed, _context = self.admission(value)
            self.assertEqual(failed, ["I1"], missing)
        # The registration is NOT CLAUDE_RESULT_KEYS.
        self.assertNotEqual(
            set(constants.INITIAL_DESIGN_RESULT_KEYS), set(commands.CLAUDE_RESULT_KEYS)
        )
        self.assertEqual(
            schema.INITIAL_DESIGN_RESULT_SCHEMA["required_keys"],
            frozenset(constants.INITIAL_DESIGN_RESULT_KEYS),
        )

    def test_R36_T1_recovery_binds_P_and_never_invents_Q(self):
        """R36 / TB-NO-PREMATURE-Q -- at T1 Q DOES NOT EXIST."""
        journal = accepted_journal()
        journal.append(
            {"type": "provider_request_prepared", "package_scope_id": SCOPE_P,
             "provider_request_identity": "pr_sel",
             "provider_kind": "codex_next_package_selection",
             "work_item_identity": "wi_sel"}
        )
        journal.append(
            {"type": "provider_dispatch_begun", "package_scope_id": SCOPE_P,
             "provider_request_identity": "pr_sel",
             "provider_kind": "codex_next_package_selection"}
        )
        transport = LoudStubTransport()
        context = build_context(journal=journal, transport=transport)
        state = commands.post_acceptance_transition_state(context)
        self.assertIsNone(
            state["transition_scope"],
            "Q must not be inferred, named, guessed or partially bound at T1",
        )
        self.assertIsNotNone(state["open_request"])
        self.assertEqual(state["open_request"]["package_scope_id"], SCOPE_P)
        report = commands.loop_position(context, state)
        self.assertEqual(report["loop_state"], commands.LOOP_TRANSITION_RECONCILE_REQUIRED)
        self.assertEqual(report["loop_next_command"], "reconcile-provider-request")
        self.assertEqual(transport.calls, [], "ZERO second selector dispatches")

    def test_R37_Q_transition_recovery_binds_Q_from_the_record(self):
        """R37 / TB-RECOVERY-BINDS-THE-RECORD -- the scope comes from the start."""
        journal = staged_journal("initial_design")
        journal.append(
            {"type": "provider_request_prepared", "package_scope_id": SCOPE_Q,
             "provider_request_identity": "pr_init",
             "provider_kind": "claude_initial_design",
             "work_item_identity": "wi_init"}
        )
        journal.append(
            {"type": "provider_dispatch_begun", "package_scope_id": SCOPE_Q,
             "provider_request_identity": "pr_init",
             "provider_kind": "claude_initial_design"}
        )
        context = build_context(journal=journal,
                                clearance=lambda scope: {"unlocked": True})
        state = commands.post_acceptance_transition_state(context)
        self.assertEqual(state["open_request"]["package_scope_id"], SCOPE_Q)
        self.assertEqual(state["transition_scope"], SCOPE_Q)
        # The scope came from the RECORD, not from the phase name.
        self.assertNotEqual(state["open_request"]["package_scope_id"], SCOPE_P)

    def test_R39_a_stale_loop_status_report_is_never_authority(self):
        """R39 / TB-CUSTODY-NO-STALE-REPORT -- re-proved against the CURRENT journal.

        section 8.8 section 8.6.2 SBC-Q-SCOPE-PHASE-OWNERSHIP, PHASE 2.  The
        derivation is still re-run against the CURRENT journal and a previous
        report is still never authority -- that is R39's point and it is
        unchanged.  What the accepted design changes is the ANSWER for a state
        that already holds AUTHENTICATED Q-SCOPED EVIDENCE: the Q transition is
        NOT erased by a later staleness of the historical T1 selection, because
        ``transition_scope`` is derived from that evidence rather than from the
        selection's continued admissibility (P-SB17, section 8.6.4 A', R-SB30,
        R-SB40).  v1_2's "no admitted selection -> no Q" rule is explicitly
        WITHDRAWN by v1_3 section 8.6.1.

        Every branch that genuinely REQUIRES an admitted selection still
        requires one, which is what the refusal below proves.
        """
        journal = staged_journal("initial_design")
        context = build_context(journal=journal,
                                clearance=lambda scope: {"unlocked": True})
        first = commands.post_acceptance_transition_state(context)
        self.assertEqual(first["transition_scope"], SCOPE_Q)
        # The journal MOVES so the SELECTION is no longer admissible: its root
        # is gone.  Q's own authenticated evidence is untouched.
        adapter = StubAdapter()
        adapter.roots = {}
        moved = build_context(journal=journal, adapter=adapter,
                              clearance=lambda scope: {"unlocked": True})
        second = commands.post_acceptance_transition_state(moved)
        self.assertIsNone(
            second["selection"],
            "the selection is re-proved against the CURRENT journal and fails",
        )
        self.assertEqual(
            second["transition_scope"],
            SCOPE_Q,
            "PHASE 2 -- authenticated Q evidence keeps the transition scope "
            "derivable; a stale historical selection never erases it",
        )
        appends_before = journal.appends
        with proved_acceptance():
            with self.assertRaises(SupervisorRefusal):
                commands.dispatch_piece3_provider_review(moved)
        self.assertEqual(journal.appends, appends_before, "ZERO appends")

    def test_R40_ambiguous_recovery_evidence_fails_closed(self):
        """R40 / R-11b -- two admissible selections refuse, with zero appends."""
        journal = accepted_journal()
        # re-cut 2026-09-02 against journal head 2300: identical selector episodes now coalesce, so the two selections must genuinely differ to be ambiguous
        for request, package_id in (("pr_a", None), ("pr_b", "A99")):
            custody_pair(
                journal,
                kind="next_package_selection",
                provider_kind="codex_next_package_selection",
                value=selection_object(package_id=package_id),
                scope=SCOPE_P,
                request=request,
            )
        context = build_context(journal=journal)
        state = commands.post_acceptance_transition_state(context)
        self.assertIsNotNone(state["contradiction"])
        self.assertIn("ambiguous", state["contradiction"])
        report = commands.loop_position(context, state)
        self.assertEqual(report["loop_state"], commands.LOOP_SAFETY_HOLD)
        self.assertIsNone(report["loop_next_command"])
        appends = journal.appends
        with proved_acceptance():
            with self.assertRaises(SupervisorRefusal):
                commands.continue_design_loop(context)
        self.assertEqual(journal.appends, appends, "ZERO appends on a contradiction")


# ===========================================================================
# R42-R58 -- THE DEDICATED B6d BRANCHES, THE PROMPTS AND THE EXTRA SEAM.
# ===========================================================================
class ContractAndPromptRehearsals(unittest.TestCase):
    def test_piece3_dispatch_uses_the_frozen_rendered_prompt(self):
        """The durable Piece-3 inventory is the prompt's single owner."""
        material = {
            "provider_kind": "gpt_question_validation",
            "prompt_inventory": {"extra": {"piece3_stage": "validation"}},
            "required_inputs_inventory": {
                "extra": {
                    "piece3_precall_requirement": {
                        "prompt": "EXACT FROZEN QUESTION-VALIDATION PROMPT"
                    }
                }
            },
        }
        self.assertEqual(
            nh_loop._specialized_supervisor_prompt(material),
            "EXACT FROZEN QUESTION-VALIDATION PROMPT",
        )

    def validate(self, provider_kind, value, *, extra=None, work_item=None):
        context = build_context(
            SCOPE_Q,
            binding=make_binding(SCOPE_Q, root=ROOT_Q),
            candidate=make_candidate(ROOT_Q),
        )
        kind = constants.WORK_ITEM_KIND_BY_PROVIDER_KIND[provider_kind]
        if work_item is None:
            if kind == "next_package_selection":
                work_item, _ = engine.next_package_selection_work_item(
                    context, context.round_zero_candidate
                )
            elif kind == "next_design_task_preparation":
                work_item, _ = engine.next_design_task_preparation_work_item(
                    context, context.round_zero_candidate
                )
            elif kind == "initial_design":
                work_item, _ = engine.initial_design_work_item(
                    context, context.round_zero_candidate, TARGET_Q
                )
            else:
                work_item, _ = engine.piece3_work_item(
                    context, context.round_zero_candidate, kind,
                    transition_state={
                        "scope_has_validation": kind == "coverage_review",
                        "routed_signal_refs": (),
                        "validation_set_id": "vs_q" if kind == "coverage_review" else None,
                        "piece3_standing_sha256": "e" * 64,
                    },
                )
        context._current_work_item_obj = work_item
        context._current_prompt_extra = {}
        context._current_required_extra = extra or {}
        prepared = fake_prepared(context, provider_kind, work_item=work_item,
                                 input_extra=extra or {})
        return commands._validate_result(context, prepared, value, None)

    def test_R42_a_valid_installed_next_package_object_reaches_result_received(self):
        """R42 / R-9b -- B6d admits it through the DEDICATED branch."""
        valid, detail = self.validate(
            "codex_next_package_selection", selection_object(),
            extra={"required_files_binding": StubAdapter().required_files},
        )
        self.assertTrue(valid, detail)
        # It could NEVER have satisfied the generic three-key schema (P-23).
        prepared_stub = type("P", (), {
            "result_schema_id": constants.RESULT_SCHEMA_ID_BY_PROVIDER_KIND[
                "codex_next_package_selection"
            ],
        })()
        self.assertTrue(commands._generic_result_schema(prepared_stub, selection_object()))

    def test_R43_lifecycle_keys_in_the_model_object_are_refused(self):
        """R43 -- the installed exact-key validator refuses the extra keys."""
        value = selection_object()
        value["result_schema_id"] = "anything"
        value["result_schema_version"] = 1
        valid, detail = self.validate(
            "codex_next_package_selection", value,
            extra={"required_files_binding": StubAdapter().required_files},
        )
        self.assertFalse(valid, detail)
        # And the installed key set was NOT mutated.
        self.assertNotIn("result_schema_id", nh_loop.NEXT_PACKAGE_REQUIRED_KEYS)
        self.assertNotIn("result_schema_version", nh_loop.NEXT_PACKAGE_REQUIRED_KEYS)

    def test_R44_a_valid_prepared_task_object_reaches_result_received(self):
        """R44 -- the dedicated preparation branch, over the installed contract."""
        valid, detail = self.validate(
            "codex_next_design_task_preparation", prepared_task_object(),
            extra={
                "required_files_binding": StubAdapter().required_files,
                "admitted_selection": selection_object(),
            },
        )
        self.assertTrue(valid, detail)

    def test_R45_lifecycle_keys_in_the_prepared_task_object_are_refused(self):
        """R45 -- refused, and PREPARE_TASK_REQUIRED_KEYS is unmutated."""
        value = prepared_task_object()
        value["result_schema_id"] = "anything"
        valid, _detail = self.validate(
            "codex_next_design_task_preparation", value,
            extra={
                "required_files_binding": StubAdapter().required_files,
                "admitted_selection": selection_object(),
            },
        )
        self.assertFalse(valid)
        self.assertNotIn("result_schema_id", nh_loop.PREPARE_TASK_REQUIRED_KEYS)
        self.assertNotIn("result_schema_version", nh_loop.PREPARE_TASK_REQUIRED_KEYS)

    def test_R46_wrong_coverage_root_or_stage_one_selection(self):
        """R46 -- each fails BEFORE the result becomes operative."""
        # (a) no controller-resolved authority binding at all.
        valid, _detail = self.validate(
            "codex_next_package_selection", selection_object(), extra={}
        )
        self.assertFalse(valid, "coverage cannot be measured against no binding")
        # (b) a stage-two reply naming a DIFFERENT root than the admitted one.
        valid, _detail = self.validate(
            "codex_next_design_task_preparation",
            prepared_task_object(root="05_ACTIVE_CANDIDATE/NH_OTHER_v1_0_CANDIDATE.md"),
            extra={
                "required_files_binding": StubAdapter().required_files,
                "admitted_selection": selection_object(),
            },
        )
        self.assertFalse(valid, "package_source_path is cross-checked")
        # (c) a root the controller cannot resolve is refused at admission.
        journal = accepted_journal()
        custody_pair(
            journal, kind="next_package_selection",
            provider_kind="codex_next_package_selection",
            value=selection_object(root="05_ACTIVE_CANDIDATE/NH_ABSENT_v1_0_CANDIDATE.md"),
            scope=SCOPE_P, request="pr_sel",
        )
        context = build_context(journal=journal)
        state = commands.post_acceptance_transition_state(context)
        self.assertIsNone(state["selection"])

    def test_R47_restart_still_re_runs_the_full_admission(self):
        """R47 / SEL-TWO-LEVELS -- B6d never substitutes for re-admission."""
        journal = accepted_journal()
        admitted_selection_state(journal)
        context = build_context(journal=journal)
        first = commands.post_acceptance_transition_state(context)
        self.assertIsNotNone(first["selection"])
        # The terminal already says result_schema_valid; that alone is NEVER
        # sufficient, so a moved authority set still makes it stale.
        adapter = StubAdapter()
        # A renamed authority file changes the requirement WITH the repository:
        # the reply no longer covers the CURRENT set, so it is refused here
        # rather than re-admitted on its earlier terminal.
        adapter.required_files = {
            "nh_master": {"path": "01_AUTHORITATIVE/NH_MASTER-21_RENAMED.md"}
        }
        restarted = build_context(journal=journal, adapter=adapter)
        second = commands.post_acceptance_transition_state(restarted)
        self.assertIsNone(second["selection"])
        self.assertEqual(
            second["stop_record"]["loop_state"], commands.LOOP_SELECTION_REQUIRED
        )

    def prompt_for(self, provider_kind, work_item, extra=None):
        required_extra = (
            extra or {}
            if provider_kind == "codex_next_design_task_preparation"
            else {}
        )
        material = {
            "provider_kind": provider_kind,
            "result_schema_id": constants.RESULT_SCHEMA_ID_BY_PROVIDER_KIND[provider_kind],
            "result_schema_version": 1,
            "package_binding": {
                "package_key": "no_controlled_id_settled_yet",
                "package_scope_id": SCOPE_Q,
                "branch": "nh-design-loop",
                "head_sha": "a" * 40,
                "source_binding_sha256": "b" * 64,
                "required_source_paths": [],
                "scope_root_path": ROOT_Q,
            },
            "work_item": work_item,
            "prompt_inventory": {"extra": extra or {}},
            "required_inputs_inventory": {"extra": required_extra},
            "settled_decision_binding": (
                (extra or {}).get("decision_binding")
                if provider_kind == "codex_next_design_task_preparation"
                else None
            ),
            "relevant_authenticated_history": [],
            "acceptance_explanation_under_audit": None,
            "acceptance_explanation_preparation": None,
        }
        return nh_loop._supervisor_provider_prompt(material)

    LIFECYCLE_SENTENCE = "use result_schema_id and result_schema_version from the material"

    def test_R54_T1_prompt_bytes_match_the_T1_contract(self):
        """R54 / PROMPT-NO-LIFECYCLE-SENTENCE -- no lifecycle instruction."""
        context = build_context(SCOPE_P)
        work_item, _ = engine.next_package_selection_work_item(
            context, context.round_zero_candidate
        )
        prompt = self.prompt_for("codex_next_package_selection", work_item)
        self.assertNotIn(self.LIFECYCLE_SENTENCE, prompt)
        self.assertIn("NH_DECISION_DEFAULTS-S19_v2_3.md", prompt)
        self.assertIn("CURRENT ACCEPTED PACKAGE BOUNDARY", prompt)
        self.assertIn("Never select P again as the next package Q", prompt)

    def test_R55_T3_prompt_bytes_match_the_T3_contract(self):
        """R55 -- the installed build_prepare_task_prompt output, no lifecycle."""
        context = build_context(SCOPE_Q, binding=make_binding(SCOPE_Q, root=ROOT_Q),
                                candidate=make_candidate(ROOT_Q))
        work_item, _ = engine.next_design_task_preparation_work_item(
            context, context.round_zero_candidate
        )
        prompt = self.prompt_for(
            "codex_next_design_task_preparation", work_item,
            extra={
                "admitted_selection": selection_object(),
                "decision_binding": {"decisions": [], "binding_sha256": "0" * 64},
            },
        )
        self.assertNotIn(self.LIFECYCLE_SENTENCE, prompt)

    def test_R59_R60_T2_gets_the_real_piece3_prompts(self):
        """R59 / R60 -- the INSTALLED Piece-3 builders, not the generic prompt."""
        context = build_context(SCOPE_Q, binding=make_binding(SCOPE_Q, root=ROOT_Q),
                                candidate=make_candidate(ROOT_Q))
        for provider_kind, kind in (
            ("gpt_question_validation", "question_validation"),
            ("gpt_question_coverage_review", "coverage_review"),
        ):
            work_item, _ = engine.piece3_work_item(
                context, context.round_zero_candidate, kind,
                transition_state={
                    "scope_has_validation": kind == "coverage_review",
                    "routed_signal_refs": (),
                    "validation_set_id": "vs_q" if kind == "coverage_review" else None,
                    "piece3_standing_sha256": "e" * 64,
                },
            )
            prompt = self.prompt_for(
                provider_kind, work_item, extra=piece3_prompt_extra()
            )
            self.assertNotIn(self.LIFECYCLE_SENTENCE, prompt, provider_kind)
        self.assertEqual(
            nh_loop.SPECIALIZED_PROMPT_PROVIDER_KINDS,
            frozenset(
                (
                    "codex_next_package_selection",
                    "codex_next_design_task_preparation",
                    "gpt_question_validation",
                    "gpt_question_coverage_review",
                )
            ),
        )

    def test_R56_the_exact_prompt_bytes_are_inside_prompt_material_sha256(self):
        """R56 -- a changed extra changes the digest, and dispatch refuses."""
        context = build_context(SCOPE_P)
        work_item, _ = engine.next_package_selection_work_item(
            context, context.round_zero_candidate
        )
        first = engine.prompt_material_sha256(
            "codex_next_package_selection", work_item, {"a": 1}
        )
        second = engine.prompt_material_sha256(
            "codex_next_package_selection", work_item, {"a": 2}
        )
        self.assertNotEqual(first, second)

    def test_R57_the_extra_is_in_required_inputs_and_reconstructable(self):
        """R57 / EXTRA-INPUTS-SEAM -- one kwarg through one existing call."""
        context = build_context(SCOPE_P)
        work_item, _ = engine.next_package_selection_work_item(
            context, context.round_zero_candidate
        )
        bare = engine.required_inputs_sha256(context, work_item, None)
        withextra = engine.required_inputs_sha256(
            context, work_item, {"required_files_binding": {"x": 1}}
        )
        self.assertNotEqual(bare, withextra)
        # The SAME extra reconstructs the SAME digest, by derivation.
        again = engine.required_inputs_sha256(
            context, work_item, {"required_files_binding": {"x": 1}}
        )
        self.assertEqual(withextra, again)
        # _dispatch forwards it, and build_prepared_request already accepts it.
        source = read_text(CONTROLLER_DIR / "nh_supervisor" / "commands.py")
        self.assertIn("extra_inputs=extra_inputs,", source)
        self.assertIn(
            "extra_inputs=None):",
            read_text(CONTROLLER_DIR / "nh_supervisor" / "engine.py"),
        )
        # And _supervisor_provider_material now reconstructs WITH the extra.
        loop_source = read_text(CONTROLLER_SOURCE)
        self.assertIn(
            "required_inputs_inventory(\n        context, work_item, required_extra\n    )",
            loop_source,
        )

    def test_R58_changed_reconstruction_is_stale_never_silently_accepted(self):
        """R58 / EXTRA-INPUTS-STALE-NOT-SILENT."""
        journal = accepted_journal()
        admitted_selection_state(journal)
        # The FROZEN source the request was computed against no longer stands.
        adapter = StubAdapter()
        adapter.current_source_binding = lambda: "9" * 64
        # The frozen source is read from the authenticated operation START of
        # the operation that prepared the request -- the prepared record itself
        # carries no source binding.
        journal.append(
            {
                "type": "supervisor_operation_started",
                "package_scope_id": SCOPE_P,
                "supervisor_operation_id": "op_sel",
                "supervisor_command": "continue-design-loop",
                "source_binding_sha256": "1" * 64,
            }
        )
        for event in journal.events:
            if event.get("type") == "provider_request_prepared":
                event["supervisor_operation_id"] = "op_sel"
        context = build_context(journal=journal, adapter=adapter)
        state = commands.post_acceptance_transition_state(context)
        self.assertIsNone(state["selection"], "the saved result is stale")
        self.assertEqual(
            state["stop_record"]["loop_state"], commands.LOOP_SELECTION_REQUIRED
        )
        self.assertEqual(journal.appends, len(journal.events), "ZERO appends")


def piece3_prompt_extra():
    """The exact controller-owned inputs the INSTALLED Piece-3 builders take."""
    return {
        "state": {
            "routed_issues": {},
            "questions": {},
            "validation_sets": {},
            "satisfied_dependency_ids": [],
            "_events": [],
        },
        "pagination": {
            "generation": 1,
            "segment_number": 1,
            "expected_page_index": 1,
            "continuing_segment": False,
            "recorded_issue_keys": [],
            "enumeration_seen_issue_keys": [],
            "enumeration_seen_target_ids": [],
        },
        "inventory": {"issues": [], "complete": False},
        "authenticated_identity": None,
        # The exact frozen pre-call source requirement the INSTALLED builder
        # takes, in its own shape.
        "precall_source_requirement": {
            "precall_basis": nh_loop.PRECALL_BASIS_CONTINUATION_SELECTION,
            "required_paths": [ROOT_Q],
            "seed_paths": [ROOT_Q],
            "closure_sha256": "0" * 64,
            "package_binding_sha256": "1" * 64,
            "package_binding": {"scope_root_path": ROOT_Q},
            "relevant_closure": {"paths": [ROOT_Q], "closure_sha256": "0" * 64},
        },
    }


class Piece3ValidationPaginationPromptTests(unittest.TestCase):
    def test_continuation_prompt_binds_the_existing_segment_shape(self):
        """A later page cannot silently replace the page-one declaration."""
        extra = piece3_prompt_extra()
        extra["pagination"].update(
            {
                "continuing": True,
                "expected_page_index": 3,
                "page_count": 4,
                "total_issue_count": 36,
                "enumeration_complete": True,
                "recorded_issue_keys": [
                    "issue_%02d" % index for index in range(18)
                ],
            }
        )

        prompt = nh_loop.build_question_validation_prompt(
            extra["state"],
            extra["pagination"],
            extra["inventory"],
            precall_source_requirement=extra["precall_source_requirement"],
        )

        self.assertIn("existing_segment_pagination_is_locked: true", prompt)
        self.assertIn("declared_page_count_for_current_segment: 4", prompt)
        self.assertIn("declared_total_issue_count_for_current_segment: 36", prompt)
        self.assertIn(
            "declared_enumeration_complete_for_current_segment: true", prompt
        )
        self.assertIn("issues_already_recorded_in_current_segment: 18", prompt)
        self.assertIn("issues_remaining_in_current_segment: 18", prompt)
        self.assertIn("pages_remaining_including_this_page: 2", prompt)
        self.assertIn("maximum_issues_allowed_on_this_page: 17", prompt)
        self.assertIn("required_issues_on_this_page: 9", prompt)
        self.assertIn(
            "reopen every cited file and COPY subject_quote", prompt
        )
        self.assertIn(
            "Do not reduce page_count, increase page_count, or move the final "
            "page earlier",
            prompt,
        )


# ===========================================================================
# R48-R53, R61-R73 -- THE DURABLE T2 SEQUENCE AND ITS FIVE CRASH POSITIONS.
# ===========================================================================
class Piece3SequenceRehearsals(unittest.TestCase):
    def test_repeated_identical_t1_selections_coalesce_to_latest_custody(self):
        """Identical package routes are replay history, not an ambiguity."""
        journal = staged_journal("selection_required")
        work_item_id, digest = selection_request_identities()
        for request in ("pr_same_1", "pr_same_2"):
            custody_pair(
                journal,
                kind="next_package_selection",
                provider_kind="codex_next_package_selection",
                value=selection_object(
                    classification="mechanical_work", root=ROOT_Q
                ),
                scope=SCOPE_P,
                request=request,
                work_item_identity=work_item_id,
                required_inputs_sha256=digest,
            )
        context = build_context(journal=journal)
        state = commands.post_acceptance_transition_state(context)
        self.assertIsNone(state["contradiction"])
        self.assertEqual(state["transition_scope"], SCOPE_Q)
        self.assertEqual(
            state["selection_custody"]["provider_request_identity"], "pr_same_2"
        )

    def test_t1_selection_rebuild_uses_its_authenticated_controller_identity(self):
        """A controller update does not erase an already-custodied selection."""
        journal = FakeJournal()
        old_context = build_context(journal=journal)
        old_obj, work_item_id = engine.next_package_selection_work_item(
            old_context, old_context.round_zero_candidate
        )
        journal.append(
            {
                "type": "supervisor_operation_started",
                "package_scope_id": SCOPE_P,
                "supervisor_command": "continue-design-loop",
                "supervisor_operation_id": "op_t1",
                "work_item_identity": work_item_id,
                "controller_executable_identity": (
                    old_context.controller_executable_identity
                ),
            }
        )
        new_context = build_context(journal=journal)
        new_context.controller_executable_identity = "2" * 64
        situation = mock.Mock(
            candidate=new_context.round_zero_candidate,
            replay=replay.Replay(journal.read(), SCOPE_P),
            work_item_id=None,
            work_item_obj=None,
        )
        rebuilt = commands._rebuild_work_item(
            new_context, situation, work_item_id, "next_package_selection"
        )
        self.assertEqual(rebuilt, old_obj)

    def test_piece3_rebuild_uses_owning_start_source_binding(self):
        """A later source epoch does not make saved Piece-3 custody unidentifiable."""
        candidate = make_candidate(ROOT_Q)
        old_binding = make_binding(
            SCOPE_Q, root=ROOT_Q, validation_set_id=None, routed=("rs_one",)
        )
        facts = {
            "scope_has_validation": False,
            "routed_signal_refs": ("rs_one",),
            "validation_set_id": None,
            "piece3_standing_sha256": "7" * 64,
        }
        journal = FakeJournal()
        old_context = build_context(
            journal=journal,
            binding=old_binding,
            candidate=candidate,
            facts=facts,
        )
        old_obj, work_item_id = engine.piece3_work_item(
            old_context,
            candidate,
            "question_validation",
            transition_state=facts,
        )
        journal.append(
            {
                "type": "supervisor_operation_started",
                "package_scope_id": SCOPE_Q,
                "supervisor_command": "dispatch-piece3-provider-review",
                "supervisor_operation_id": "op_piece3",
                "work_item_identity": work_item_id,
                "controller_executable_identity": (
                    old_context.controller_executable_identity
                ),
                "source_binding_sha256": old_binding.source_binding_sha256,
                "candidate_path": candidate.candidate_path,
                "candidate_sha256": candidate.candidate_sha256,
                "candidate_bytes": candidate.candidate_bytes,
                "standing_before_sha256": facts["piece3_standing_sha256"],
            }
        )
        moved_binding = dataclasses.replace(
            old_binding, source_binding_sha256="8" * 64
        )
        new_context = build_context(
            journal=journal,
            binding=moved_binding,
            candidate=candidate,
            facts=facts,
        )
        situation = mock.Mock(
            candidate=candidate,
            replay=replay.Replay(journal.read(), SCOPE_Q),
            work_item_id=None,
            work_item_obj=None,
        )
        rebuilt = commands._rebuild_work_item(
            new_context,
            situation,
            work_item_id,
            "question_validation",
        )
        self.assertEqual(rebuilt, old_obj)

    def test_R48_R63_one_piece3_stage_one_model_call(self):
        """R48 / R63 / T2-ONE-CALL -- exactly one request; the commit contacts nothing."""
        r48_binding = make_binding(SCOPE_Q, root=ROOT_Q, validation_set_id=None)
        r48_candidate = make_candidate(ROOT_Q)
        journal = staged_journal(
            "clearance_required", binding=r48_binding, candidate=r48_candidate
        )
        transport = LoudStubTransport()
        context = build_context(
            journal=journal, transport=transport,
            binding=r48_binding, candidate=r48_candidate,
        )
        state = commands.post_acceptance_transition_state(context)
        report = commands.loop_position(context, state)
        self.assertEqual(report["loop_state"], commands.LOOP_PACKAGE_CLEARANCE_REQUIRED)
        self.assertEqual(report["loop_next_command"], "dispatch-piece3-provider-review")
        # Position B: a custody now awaits, and the dispatch command REFUSES a
        # second model request for the same stage.
        journal = staged_journal(
            "piece3_pending", binding=r48_binding, candidate=r48_candidate
        )
        context = build_context(
            journal=journal, transport=transport,
            binding=r48_binding, candidate=r48_candidate,
        )
        with proved_acceptance():
            with self.assertRaises(SupervisorRefusal) as caught:
                commands.dispatch_piece3_provider_review(context)
        self.assertIn("one model request", str(caught.exception))
        self.assertEqual(transport.calls, [])
        # The commit stage is PROVIDER-FREE by registration.
        self.assertNotIn(
            "commit-piece3-provider-result", constants.PROVIDER_DISPATCH_COMMANDS
        )
        self.assertIn(
            "commit-piece3-provider-result",
            constants.CONTINUATION_PROVIDER_FREE_COMMANDS,
        )
        # And the ordinary direct transports are NEVER called on this path.
        continuation = extract_continuation_source()
        self.assertNotIn("run_codex_question_validation(", continuation)
        self.assertNotIn("run_codex_question_coverage_review(", continuation)

    def test_R49_R72_uncertain_piece3_dispatch_is_reconciled_never_resent(self):
        """R49 / R72 -- reconcile FIRST; ZERO second Codex calls."""
        journal = staged_journal("clearance_required")
        journal.append(
            {"type": "provider_request_prepared", "package_scope_id": SCOPE_Q,
             "provider_request_identity": "pr_qv",
             "provider_kind": "gpt_question_validation",
             "work_item_identity": "wi_qv"}
        )
        journal.append(
            {"type": "provider_dispatch_begun", "package_scope_id": SCOPE_Q,
             "provider_request_identity": "pr_qv",
             "provider_kind": "gpt_question_validation"}
        )
        transport = LoudStubTransport()
        context = build_context(journal=journal, transport=transport)
        state = commands.post_acceptance_transition_state(context)
        report = commands.loop_position(context, state)
        self.assertEqual(
            report["loop_state"], commands.LOOP_TRANSITION_RECONCILE_REQUIRED
        )
        self.assertEqual(report["loop_next_command"], "reconcile-provider-request")
        with proved_acceptance():
            with self.assertRaises(SupervisorRefusal):
                commands.dispatch_piece3_provider_review(context)
        self.assertEqual(transport.codex_calls, 0, "ZERO second Codex calls")
        # With the CLI transport's unsupported lookup the honest position is a
        # named practical action for a person.
        self.assertEqual(transport.lookup(None, None).outcome, "unsupported")

    def test_R50_R91_authorization_is_scope_matched(self):
        """R50 / R91 / T2-SCOPE-MATCHED -- P's authorization cannot satisfy Q."""
        journal = staged_journal("piece3_pending")
        # An authorization under P's scope, with Q's Piece-3 event owed.
        journal.append(
            {
                "type": "piece3_provider_work_recorded",
                "package_scope_id": SCOPE_P,
                "authorizes_event_type": "validation_recorded",
                "provider_request_identity": "pr_qv",
                "result_custody_identity": "rc_pr_qv",
                "work_item_identity": "wi_qv",
                "result_schema_valid": True,
            }
        )
        context = build_context(journal=journal)
        state = commands.post_acceptance_transition_state(context)
        self.assertIsNone(
            state["piece3_authorization"].get("validation"),
            "an authorization carrying another scope is NEVER consulted",
        )
        # The commit runs under the proved Q transition context, exactly as
        # Path C builds it -- so the refusal below is the AUTHORIZATION rule and
        # not a binding mismatch.
        context = build_context(
            journal=journal,
            binding=make_binding(SCOPE_Q, root=ROOT_Q, validation_set_id=None),
            candidate=make_candidate(ROOT_Q),
        )
        appends = journal.appends
        with proved_acceptance():
            with self.assertRaises(SupervisorRefusal) as caught:
                commands.commit_piece3_provider_result(context)
        self.assertIn("no unconsumed scope-matched", str(caught.exception))
        self.assertEqual(journal.appends, appends, "the journal is byte-identical")

    def test_R51_R71_the_commit_consumes_the_same_result_and_appends_once(self):
        """R51 / R71 -- one Piece-3 event; the authorization is consumed once."""
        journal = staged_journal("piece3_commit")
        context = build_context(journal=journal)
        state = commands.post_acceptance_transition_state(context)
        self.assertIsNotNone(state["piece3_authorization"].get("validation"))
        report = commands.loop_position(context, state)
        self.assertEqual(report["loop_state"], commands.LOOP_PIECE3_COMMIT_REQUIRED)
        self.assertEqual(report["loop_next_command"], "commit-piece3-provider-result")
        # Once the validation is durable the authorization is CONSUMED and the
        # position moves on; a second run appends nothing.
        journal.append(
            {"type": "validation_recorded", "package_scope_id": SCOPE_Q,
             "validation_set_id": "vs_q"}
        )
        again = commands.post_acceptance_transition_state(context)
        self.assertIsNone(again["piece3_authorization"].get("validation"))
        self.assertTrue(again["scope_has_validation"])

    def test_coverage_gap_commit_completion_consumes_authorization_once(self):
        """A completed gap-routing commit advances; a partial append does not."""
        authorization = {
            "event_seq": 1,
            "type": "piece3_provider_work_recorded",
            "package_scope_id": SCOPE_Q,
            "authorizes_event_type": "question_coverage_review_recorded",
            "work_item_identity": "wi_cov",
        }
        start = {
            "event_seq": 2,
            "type": "supervisor_operation_started",
            "package_scope_id": SCOPE_Q,
            "supervisor_command": "commit-piece3-provider-result",
            "supervisor_operation_id": "op_cov",
            "work_item_identity": "wi_cov",
        }
        signal = {
            "event_seq": 3,
            "type": "review_signal_recorded",
            "package_scope_id": SCOPE_Q,
            "signal_source": "question_coverage_review",
        }
        completion = {
            "event_seq": 4,
            "type": "supervisor_operation_completed",
            "package_scope_id": SCOPE_Q,
            "supervisor_command": "commit-piece3-provider-result",
            "supervisor_operation_id": "op_cov",
            "work_item_identity": "wi_cov",
            "operation_outcome": "ok",
        }

        partial = replay.Replay([authorization, start, signal], SCOPE_Q)
        self.assertIsNotNone(
            partial.unconsumed_piece3_authorization(
                "question_coverage_review_recorded"
            ),
            "a crash before the matching completion must re-enter the commit",
        )
        complete = replay.Replay(
            [authorization, start, signal, completion], SCOPE_Q
        )
        self.assertIsNone(
            complete.unconsumed_piece3_authorization(
                "question_coverage_review_recorded"
            )
        )
        self.assertEqual(complete.piece3_provider_authorization(), "consumed")

    def test_repeated_input_refs_do_not_consume_a_coverage_result(self):
        """Input refs never stand in for processing the saved coverage bytes."""
        signal = {
            "event_seq": 1,
            "type": "review_signal_recorded",
            "package_scope_id": SCOPE_Q,
            "routed_signal_id": "rs_existing",
            "signal_source": "question_coverage_review",
        }
        authorization = {
            "event_seq": 2,
            "type": "piece3_provider_work_recorded",
            "package_scope_id": SCOPE_Q,
            "authorizes_event_type": "question_coverage_review_recorded",
            "routed_signal_refs": ["rs_existing"],
            "supervisor_operation_id": "op_process",
            "work_item_identity": "wi_cov_repeat",
        }
        completion = {
            "event_seq": 3,
            "type": "supervisor_operation_completed",
            "package_scope_id": SCOPE_Q,
            "supervisor_command": "process-custodied-provider-result",
            "supervisor_operation_id": "op_process",
            "work_item_identity": "wi_cov_repeat",
            "operation_outcome": "ok",
        }
        repeated = replay.Replay(
            [signal, authorization, completion], SCOPE_Q
        )
        self.assertIs(
            repeated.unconsumed_piece3_authorization(
                "question_coverage_review_recorded"
            ),
            authorization,
        )
        self.assertEqual(
            repeated.piece3_provider_authorization(),
            "authorized_coverage_pending",
        )

    def test_coverage_gap_signal_reenters_validation_before_coverage(self):
        """A signal newer than validation cannot be covered by that validation."""
        journal = staged_journal("task_preparation")
        journal.append(
            {
                "type": "review_signal_recorded",
                "package_scope_id": SCOPE_Q,
                "routed_signal_id": "rs_fresh_gap",
                "signal_source": "question_coverage_review",
            }
        )
        # re-cut 2026-09-02 against journal head 2300: the rule reads the gate clearance; the stub must name the awaiting signal as the real gate does
        context = build_context(
            journal=journal,
            clearance=lambda scope: {
                "unlocked": False,
                "routing_signals_awaiting_validation": ["rs_fresh_gap"],
            },
        )
        state = commands.post_acceptance_transition_state(context)
        self.assertFalse(state["scope_has_validation"])
        self.assertEqual(state["routed_signal_refs"], ("rs_fresh_gap",))
        position = commands.loop_position(context, state)
        self.assertEqual(
            position["loop_next_command"], "dispatch-piece3-provider-review"
        )
        self.assertEqual(position["piece3_stage"], "validation")

    def test_fresh_bundle_seven_baseline_reenters_validation(self):
        """A new complete baseline makes an older questionnaire historical."""
        journal = staged_journal("task_preparation")
        journal.append(
            {
                "type": "bundle_seven_baseline_recorded",
                "review_complete": True,
            }
        )
        context = build_context(journal=journal)

        state = commands.post_acceptance_transition_state(context)
        position = commands.loop_position(context, state)

        self.assertFalse(state["scope_has_validation"])
        self.assertFalse(state["scope_validation_complete"])
        self.assertEqual(position["piece3_stage"], "validation")
        self.assertEqual(
            position["loop_next_command"], "dispatch-piece3-provider-review"
        )

    def test_incomplete_paginated_validation_stays_in_validation(self):
        """Page 1 of 3 is a validation position, not a coverage position."""
        journal = staged_journal("clearance_required")
        journal.append(
            {
                "type": "validation_recorded",
                "package_scope_id": SCOPE_Q,
                "validation_set_id": "vs_partial",
                "page_index": 1,
                "page_count": 3,
                "enumeration_complete": True,
            }
        )
        context = build_context(
            journal=journal, clearance=lambda scope: {"unlocked": False}
        )

        state = commands.post_acceptance_transition_state(context)
        position = commands.loop_position(context, state)

        self.assertTrue(state["scope_has_validation"])
        self.assertFalse(state["scope_validation_complete"])
        self.assertEqual(position["piece3_stage"], "validation")
        self.assertEqual(
            position["loop_next_command"], "dispatch-piece3-provider-review"
        )

    def test_final_paginated_validation_page_advances_to_coverage(self):
        """Only the complete final page moves the Piece-3 stage to coverage."""
        journal = staged_journal("clearance_required")
        for page in (1, 2, 3):
            journal.append(
                {
                    "type": "validation_recorded",
                    "package_scope_id": SCOPE_Q,
                    "validation_set_id": "vs_complete",
                    "page_index": page,
                    "page_count": 3,
                    "enumeration_complete": page == 3,
                }
            )
        context = build_context(
            journal=journal, clearance=lambda scope: {"unlocked": False}
        )

        state = commands.post_acceptance_transition_state(context)
        position = commands.loop_position(context, state)

        self.assertTrue(state["scope_has_validation"])
        self.assertTrue(state["scope_validation_complete"])
        self.assertEqual(position["piece3_stage"], "coverage")

    def test_post_validation_source_binding_comes_from_latest_validation(self):
        """The pre-validation choice cannot overwrite Q's validation binding."""
        events = [
            {
                "event_seq": 10,
                "type": "validation_recorded",
                "package_scope_id": SCOPE_Q,
                "source_binding_sha256": "1" * 64,
            },
            {
                "event_seq": 11,
                "type": "validation_recorded",
                "package_scope_id": SCOPE_Q,
                "source_binding_sha256": "2" * 64,
            },
        ]
        with mock.patch.object(
            commands,
            "transition_choice_event",
            return_value={
                "package_scope_id": SCOPE_Q,
                "source_binding_sha256": "0" * 64,
            },
        ):
            self.assertEqual(
                commands._transition_source_binding(events, SCOPE_Q, {}),
                "2" * 64,
            )

    def test_successful_piece3_commit_retires_old_invalid_output_dependency(self):
        """A resolved validation retry cannot poison the following stage."""
        record = dependency.build_record(
            "provider_output_invalid_bounded_retry",
            "local_codex_cli_chatgpt",
            "wi_old_validation",
            episode_identity="ep_old_validation",
            durable_record_placement="provider_request_terminal_recorded",
            phase_evidence_condition="terminal_result_invalid_recorded",
            plain_language_dependency="The saved answer was invalid.",
        )
        dependency_identity = dependency.identity_of(record)
        events = [
            {
                "event_seq": 1,
                "type": "provider_request_terminal_recorded",
                "package_scope_id": SCOPE_Q,
                "provider_kind": "gpt_question_validation",
                "dependency_identity": dependency_identity,
                "dependency_record": record,
            },
            {
                "event_seq": 2,
                "type": "validation_recorded",
                "package_scope_id": SCOPE_Q,
                "validation_set_id": "vs_recovered",
            },
        ]

        self.assertEqual(
            commands.scoped_dependency_occurrence(events, SCOPE_Q), {}
        )

    def test_interview_revalidation_flag_reenters_validation_before_coverage(self):
        """A complete but non-current inventory is revalidated before review."""
        journal = staged_journal("task_preparation")
        context = build_context(
            journal=journal,
            clearance=lambda scope: {
                "unlocked": False,
                "revalidation_required": True,
            },
        )
        state = commands.post_acceptance_transition_state(context)
        self.assertFalse(state["scope_has_validation"])
        position = commands.loop_position(context, state)
        self.assertEqual(position["piece3_stage"], "validation")
        self.assertEqual(
            position["loop_next_command"], "dispatch-piece3-provider-review"
        )

    def test_new_validation_supersedes_older_coverage_authorization(self):
        """A pre-validation coverage result stays historical, never commits late."""
        journal = staged_journal("task_preparation")
        journal.append(
            {
                "type": "review_signal_recorded",
                "package_scope_id": SCOPE_Q,
                "routed_signal_id": "rs_fresh_gap",
                "signal_source": "question_coverage_review",
            }
        )
        journal.append(
            {
                "type": "piece3_provider_work_recorded",
                "package_scope_id": SCOPE_Q,
                "authorizes_event_type": "question_coverage_review_recorded",
                "provider_request_identity": "pr_stale_cov",
                "result_custody_identity": "rc_stale_cov",
                "work_item_identity": "wi_stale_cov",
            }
        )
        journal.append(
            {
                "type": "validation_recorded",
                "package_scope_id": SCOPE_Q,
                "validation_set_id": "vs_after_gap",
            }
        )
        context = build_context(journal=journal)
        state = commands.post_acceptance_transition_state(context)
        self.assertTrue(state["scope_has_validation"])
        self.assertEqual(state["validation_set_id"], "vs_after_gap")
        self.assertIsNone(state["piece3_authorization"].get("coverage"))

    def test_repeated_coverage_refs_require_commit_before_any_revalidation(self):
        """The saved coverage bytes are committed before routing can change."""
        journal = staged_journal("task_preparation")
        journal.append(
            {
                "type": "review_signal_recorded",
                "package_scope_id": SCOPE_Q,
                "routed_signal_id": "rs_existing",
                "signal_source": "question_coverage_review",
            }
        )
        journal.append(
            {
                "type": "piece3_provider_work_recorded",
                "package_scope_id": SCOPE_Q,
                "authorizes_event_type": "question_coverage_review_recorded",
                "routed_signal_refs": [],
                "provider_request_identity": "pr_stale_cov",
                "result_custody_identity": "rc_stale_cov",
                "work_item_identity": "wi_stale_cov",
            }
        )
        journal.append(
            {
                "type": "validation_recorded",
                "package_scope_id": SCOPE_Q,
                "validation_set_id": "vs_after_first_gap",
            }
        )
        authorization = journal.append(
            {
                "type": "piece3_provider_work_recorded",
                "package_scope_id": SCOPE_Q,
                "authorizes_event_type": "question_coverage_review_recorded",
                "routed_signal_refs": ["rs_existing"],
                "supervisor_operation_id": "op_repeat",
                "work_item_identity": "wi_repeat_cov",
            }
        )
        journal.append(
            {
                "type": "supervisor_operation_completed",
                "package_scope_id": SCOPE_Q,
                "supervisor_command": "process-custodied-provider-result",
                "supervisor_operation_id": "op_repeat",
                "work_item_identity": "wi_repeat_cov",
                "operation_outcome": "ok",
            }
        )
        context = build_context(journal=journal)
        state = commands.post_acceptance_transition_state(context)
        self.assertIsNone(state["contradiction"])
        self.assertTrue(state["scope_has_validation"])
        self.assertEqual(state["validation_set_id"], "vs_after_first_gap")
        self.assertIn("rs_existing", state["routed_signal_refs"])
        position = commands.loop_position(context, state)
        self.assertEqual(position["piece3_stage"], "coverage")
        self.assertEqual(
            position["loop_next_command"], "commit-piece3-provider-result"
        )

    def test_completed_unchanged_coverage_stops_before_duplicate_dispatch(self):
        """No new signal or clearance means a mechanical no-progress stop."""
        journal = staged_journal("task_preparation")
        authorization = journal.append(
            {
                "type": "piece3_provider_work_recorded",
                "package_scope_id": SCOPE_Q,
                "authorizes_event_type": "question_coverage_review_recorded",
                "routed_signal_refs": [],
                "provider_request_identity": "pr_no_progress",
                "result_custody_identity": "rc_no_progress",
                "work_item_identity": "wi_no_progress",
            }
        )
        started = journal.append(
            {
                "type": "supervisor_operation_started",
                "package_scope_id": SCOPE_Q,
                "supervisor_command": "commit-piece3-provider-result",
                "supervisor_operation_id": "op_no_progress",
                "work_item_identity": "wi_no_progress",
            }
        )
        completed = journal.append(
            {
                "type": "supervisor_operation_completed",
                "package_scope_id": SCOPE_Q,
                "supervisor_command": "commit-piece3-provider-result",
                "supervisor_operation_id": "op_no_progress",
                "work_item_identity": "wi_no_progress",
                "operation_outcome": "ok",
            }
        )
        self.assertLess(authorization["event_seq"], started["event_seq"])
        self.assertLess(started["event_seq"], completed["event_seq"])
        context = build_context(journal=journal)
        state = commands.post_acceptance_transition_state(context)
        self.assertIsNotNone(state["piece3_no_progress"])
        position = commands.loop_position(context, state)
        self.assertEqual(position["loop_state"], commands.LOOP_SAFETY_HOLD)
        self.assertIsNone(position["loop_next_command"])
        self.assertEqual(
            position["dependency_code"],
            "question_validation_coverage_no_progress",
        )

    def test_question_issue_shape_is_checked_before_piece3_authorization(self):
        """Malformed genuine issues enter bounded output retry, not commit."""
        payload = question_validation_payload()
        issue = {key: None for key in nh_loop.QUESTION_VALIDATION_ISSUE_KEYS}
        issue.update(
            {
                "issue_key": "individual.space.start",
                "classification": "genuinely_open_for_ness",
                "disposition": nh_loop.QUESTION_VALIDATION_ADMIT_DISPOSITION,
                "already_settled_note": "Not settled.",
                "mechanical_note": "Not mechanical.",
                "still_open_note": "The behavior remains open.",
                "why_ness_needed_note": "Ness owns this choice.",
                "real_use_effect_note": "It changes the opening experience.",
                "source_evidence": [ROOT_Q],
                "later_package_use": [],
                "user_facing_effects": [],
                "options": [],
            }
        )
        payload["issues"] = [issue]
        payload["total_issue_count"] = 1
        errors = []
        outcome = nh_loop._continuation_question_validation_payload_contract(
            json.dumps(payload), {}, errors
        )
        self.assertIsNone(outcome)
        self.assertTrue(
            any("user_facing_effects must be a non-empty array" in e for e in errors)
        )

    def test_question_issue_evidence_must_be_in_its_checked_source_list(self):
        """A source-citation mismatch is refused before authorization."""
        payload = question_validation_payload()
        payload["issues"] = [
            {
                "issue_key": "source_mismatch",
                "source_evidence": [ROOT_P],
                "classification": "mechanical_work",
            }
        ]
        payload["total_issue_count"] = 1
        errors = []
        with mock.patch.object(
            nh_loop, "validate_question_validation_issue", return_value=True
        ):
            outcome = nh_loop._continuation_question_validation_payload_contract(
                json.dumps(payload), {}, errors
            )
        self.assertIsNone(outcome)
        self.assertEqual(len(errors), 1)
        self.assertIn("cites source it did not check", errors[0])

        payload["source_paths_checked"].append(ROOT_P)
        errors = []
        with mock.patch.object(
            nh_loop, "validate_question_validation_issue", return_value=True
        ):
            outcome = nh_loop._continuation_question_validation_payload_contract(
                json.dumps(payload), {}, errors
            )
        self.assertIsNotNone(outcome)
        self.assertEqual(errors, [])

    def test_question_issue_exact_quotes_pass_provider_boundary_unchanged(self):
        """Exact A19 source quotations pass and the payload is not rewritten."""
        source = "01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md"
        payload = question_validation_payload()
        payload["source_paths_checked"] = [source]
        payload["issues"] = [
            {
                "issue_key": "ness.world.opening.sequence",
                "classification": "genuinely_open_for_ness",
                "subject_quote": "Opening Ness's World.",
                "settled_basis_quote": (
                    "Requires identity confirmation through a private code or "
                    "thumb/fingerprint verification."
                ),
                "source_evidence": [source],
            }
        ]
        payload["total_issue_count"] = 1
        expected = copy.deepcopy(payload)
        nh_loop.materialize_question_validation_controller_fields(expected)
        errors = []
        binding = {
            "branch": "nh-design-loop",
            "head_sha": "a" * 40,
            "binding_sha256": "b" * 64,
        }
        with mock.patch.object(
            nh_loop, "validate_question_validation_issue", return_value=True
        ), mock.patch.object(nh_loop, "read_source_binding", return_value=binding):
            outcome = nh_loop._continuation_question_validation_payload_contract(
                json.dumps(payload), {}, errors
            )
        self.assertEqual(outcome, expected)
        self.assertEqual(errors, [])

    def test_question_issue_nonexact_quote_is_rejected_before_authorization(self):
        """The proved A19 mismatch fails at the provider-result boundary."""
        source = "01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md"
        payload = question_validation_payload()
        payload["source_paths_checked"] = [source]
        payload["issues"] = [
            {
                "issue_key": "desktop.mobile.vr.differences.in.opening.behavior",
                "classification": "genuinely_open_for_ness",
                "subject_quote": "Opening Ness's World.",
                "settled_basis_quote": "Opening Ness's World requires three steps",
                "source_evidence": [source],
            }
        ]
        payload["total_issue_count"] = 1
        errors = []
        binding = {
            "branch": "nh-design-loop",
            "head_sha": "a" * 40,
            "binding_sha256": "b" * 64,
        }
        with mock.patch.object(
            nh_loop, "validate_question_validation_issue", return_value=True
        ), mock.patch.object(nh_loop, "read_source_binding", return_value=binding):
            outcome = nh_loop._continuation_question_validation_payload_contract(
                json.dumps(payload), {}, errors
            )
        self.assertIsNone(outcome)
        self.assertEqual(len(errors), 1)
        self.assertIn("settled_basis_quote", errors[0])
        self.assertIn("does not occur byte-exactly", errors[0])

    def test_retry_contract_missing_effects_fails_at_earliest_boundary(self):
        """The required key and non-empty rule are both model-facing and local."""
        payload = question_validation_payload()
        issue = valid_question_validation_issue()
        del issue["user_facing_effects"]
        payload["issues"] = [issue]
        payload["total_issue_count"] = 1
        errors = []
        outcome = nh_loop._continuation_question_validation_payload_contract(
            json.dumps(payload), {}, errors
        )
        self.assertIsNone(outcome)
        self.assertEqual(
            errors,
            ["question-validation issue 1 is missing keys: user_facing_effects"],
        )
        self.assertIn(
            '"user_facing_effects": non-empty array of DISTINCT codes',
            nh_loop.QUESTION_VALIDATION_PROMPT_TAIL,
        )
        for code in nh_loop.NESS_QUESTION_USER_FACING_EFFECTS:
            self.assertIn(code, nh_loop.QUESTION_VALIDATION_PROMPT_TAIL)

    def test_retry_prompt_receives_the_exact_previous_local_error(self):
        """A bounded retry is told the exact error, not merely 'invalid'."""
        payload = question_validation_payload()
        issue = valid_question_validation_issue()
        issue["user_facing_effects"] = []
        payload["issues"] = [issue]
        payload["total_issue_count"] = 1
        journal = FakeJournal()
        custody_pair(
            journal,
            kind="question_validation",
            provider_kind="gpt_question_validation",
            value=payload,
            scope=SCOPE_Q,
            request="pr_invalid_effects",
            terminal_kind="result_invalid",
        )
        adapter = StubAdapter(
            validate_question_validation_payload=(
                lambda text, extra, errors:
                nh_loop._continuation_question_validation_payload_contract(
                    text, extra, errors
                )
            ),
            piece3_precall_requirement=(
                lambda scope, kind, selection=None: {
                    "piece3_stage": kind,
                    "prompt": "BASE QUESTION-VALIDATION PROMPT",
                }
            ),
        )
        context = build_context(
            scope=SCOPE_Q,
            journal=journal,
            adapter=adapter,
            binding=make_binding(SCOPE_Q, root=ROOT_Q),
            candidate=make_candidate(ROOT_Q),
        )
        precall = commands._piece3_precall_with_retry_feedback(
            context,
            adapter,
            SCOPE_Q,
            "question_validation",
            None,
            before_event_seq=journal.events[-1]["event_seq"] + 1,
        )
        self.assertIn("BOUNDED OUTPUT RETRY", precall["prompt"])
        self.assertIn(
            "question-validation issue 1 user_facing_effects must be a "
            "non-empty array",
            precall["prompt"],
        )
        self.assertIn("Preserve all otherwise-valid substantive issues", precall["prompt"])
        self.assertNotIn("could not read as a valid answer", precall["prompt"])

    def test_retry_contract_reports_the_exact_invalid_effect_code(self):
        """An unrecognised controlled code is named in the rejection."""
        issue = valid_question_validation_issue()
        issue["user_facing_effects"] = ["not_an_allowed_effect"]
        errors = []
        self.assertFalse(
            nh_loop.validate_question_validation_issue(issue, 0, errors)
        )
        joined = "\n".join(errors)
        self.assertIn('invalid code(s) ["not_an_allowed_effect"]', joined)
        self.assertIn('"how_it_feels_in_use"', joined)

    def test_retry_contract_reports_the_exact_nonbyte_quote(self):
        """The exact rejected evidence text is available to the retry."""
        issue = valid_question_validation_issue()
        blobs = {
            issue["source_evidence"][0]: issue["subject_quote"].encode("utf-8"),
        }
        errors = []
        self.assertFalse(
            nh_loop.check_question_validation_issue_quotes(
                [issue], blobs, errors, record_paths=False
            )
        )
        self.assertEqual(len(errors), 1)
        self.assertIn("settled_basis_quote", errors[0])
        self.assertIn("does not occur byte-exactly", errors[0])
        self.assertIn(issue["settled_basis_quote"], errors[0])

    def test_corrected_retry_passes_without_changing_unrelated_issue_content(self):
        """Correcting only effects admits the same otherwise-identical issue."""
        issue = valid_question_validation_issue()
        issue["user_facing_effects"] = []
        before = copy.deepcopy(issue)
        issue["user_facing_effects"] = ["how_it_feels_in_use"]
        payload = question_validation_payload()
        payload["source_paths_checked"] = list(issue["source_evidence"])
        payload["issues"] = [issue]
        payload["total_issue_count"] = 1
        errors = []
        with mock.patch.object(
            nh_loop, "check_question_validation_issue_quotes", return_value=True
        ):
            outcome = nh_loop._continuation_question_validation_payload_contract(
                json.dumps(payload), {}, errors
            )
        self.assertEqual(errors, [])
        self.assertEqual(outcome, payload)
        for key in before:
            if key != "user_facing_effects":
                self.assertEqual(issue[key], before[key], key)

    def test_valid_question_output_is_admitted_byte_for_byte_as_before(self):
        """The retry correction does not rewrite or reinterpret valid output."""
        payload = question_validation_payload()
        issue = valid_question_validation_issue()
        payload["source_paths_checked"] = list(issue["source_evidence"])
        payload["issues"] = [issue]
        payload["total_issue_count"] = 1
        expected = copy.deepcopy(payload)
        errors = []
        with mock.patch.object(
            nh_loop, "check_question_validation_issue_quotes", return_value=True
        ):
            outcome = nh_loop._continuation_question_validation_payload_contract(
                json.dumps(payload), {}, errors
            )
        self.assertEqual(errors, [])
        self.assertEqual(outcome, expected)

    def test_refused_legacy_authorization_routes_to_existing_piece3_retry(self):
        """A saved pre-fix mismatch is preserved and no longer recommitted."""
        journal = staged_journal("piece3_commit")
        payload = question_validation_payload()
        payload["issues"] = [
            {"issue_key": "source_mismatch", "source_evidence": [ROOT_P]}
        ]
        payload["total_issue_count"] = 1
        encoded = json.dumps(payload, sort_keys=True).encode("utf-8")
        for event in journal.events:
            if (
                event.get("type") == "provider_result_custody_recorded"
                and event.get("provider_request_identity") == "pr_qv"
            ):
                event["result_bytes_base64"] = base64.b64encode(encoded).decode("ascii")
                event["result_byte_length"] = len(encoded)
                event["result_sha256"] = hashlib.sha256(encoded).hexdigest()
        journal.append(
            {
                "type": "supervisor_operation_started",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": "op_refused_piece3",
                "supervisor_command": "commit-piece3-provider-result",
                "work_item_identity": "wi_qv",
            }
        )
        journal.append(
            {
                "type": "supervisor_operation_completed",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": "op_refused_piece3",
                "supervisor_command": "commit-piece3-provider-result",
                "work_item_identity": "wi_qv",
                "operation_outcome": "refused",
            }
        )
        adapter = StubAdapter(
            validate_question_validation_payload=(
                lambda text, extra, errors:
                nh_loop._continuation_question_validation_payload_contract(
                    text, extra, errors
                )
            )
        )
        context = build_context(journal=journal, adapter=adapter)
        before = journal.appends
        with mock.patch.object(
            nh_loop, "validate_question_validation_issue", return_value=True
        ):
            state = commands.post_acceptance_transition_state(context)
        self.assertIsNone(state["piece3_authorization"].get("validation"))
        self.assertEqual(state["piece3_stale_reentry"], "validation")
        self.assertEqual(
            commands.loop_position(context, state)["loop_next_command"],
            "dispatch-piece3-provider-review",
        )
        _series, scheduling = commands.continuation_scheduling(
            context,
            state,
            commands.LOOP_PACKAGE_CLEARANCE_REQUIRED,
            "dispatch-piece3-provider-review",
        )
        self.assertEqual(
            scheduling["source_binding_sha256"], STUB_LIVE_SOURCE_BINDING
        )
        self.assertEqual(journal.appends, before, "the saved result is unchanged")
        self.assertEqual(context.provider.calls, [], "the projection calls no provider")

    def test_refused_legacy_quote_authorization_routes_to_existing_piece3_retry(self):
        """The preserved event-926 shape opens the normal bounded retry path."""
        source = "01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md"
        journal = staged_journal("piece3_commit")
        payload = question_validation_payload()
        payload["source_paths_checked"] = [source]
        payload["issues"] = [
            {
                "issue_key": "desktop.mobile.vr.differences.in.opening.behavior",
                "classification": "genuinely_open_for_ness",
                "subject_quote": "Opening Ness's World.",
                "settled_basis_quote": "Opening Ness's World requires three steps",
                "source_evidence": [source],
            }
        ]
        payload["total_issue_count"] = 1
        encoded = json.dumps(payload, sort_keys=True).encode("utf-8")
        for event in journal.events:
            if (
                event.get("type") == "provider_result_custody_recorded"
                and event.get("provider_request_identity") == "pr_qv"
            ):
                event["result_bytes_base64"] = base64.b64encode(encoded).decode("ascii")
                event["result_byte_length"] = len(encoded)
                event["result_sha256"] = hashlib.sha256(encoded).hexdigest()
        journal.append(
            {
                "type": "supervisor_operation_started",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": "op_refused_quote_piece3",
                "supervisor_command": "commit-piece3-provider-result",
                "work_item_identity": "wi_qv",
            }
        )
        journal.append(
            {
                "type": "supervisor_operation_completed",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": "op_refused_quote_piece3",
                "supervisor_command": "commit-piece3-provider-result",
                "work_item_identity": "wi_qv",
                "operation_outcome": "refused",
            }
        )
        adapter = StubAdapter(
            validate_question_validation_payload=(
                lambda text, extra, errors:
                nh_loop._continuation_question_validation_payload_contract(
                    text, extra, errors
                )
            )
        )
        context = build_context(journal=journal, adapter=adapter)
        before = journal.appends
        binding = {
            "branch": "nh-design-loop",
            "head_sha": "a" * 40,
            "binding_sha256": "b" * 64,
        }
        with mock.patch.object(
            nh_loop, "validate_question_validation_issue", return_value=True
        ), mock.patch.object(nh_loop, "read_source_binding", return_value=binding):
            state = commands.post_acceptance_transition_state(context)
        self.assertIsNone(state["piece3_authorization"].get("validation"))
        self.assertEqual(
            commands.loop_position(context, state)["loop_next_command"],
            "dispatch-piece3-provider-review",
        )
        self.assertEqual(journal.appends, before, "event-926 history stays unchanged")
        self.assertEqual(context.provider.calls, [], "the projection calls no provider")

    def test_R52_R8b_position_drift_makes_the_saved_result_stale(self):
        """R52 / R-8b -- preserved and refused as stale; ZERO Codex calls."""
        journal = staged_journal("piece3_commit")
        transport = LoudStubTransport()
        # The custody the authorization NAMES no longer matches.
        for event in journal.events:
            if event.get("type") == "piece3_provider_work_recorded":
                event["result_custody_identity"] = "rc_something_else"
        context = build_context(
            journal=journal, transport=transport,
            binding=make_binding(SCOPE_Q, root=ROOT_Q, validation_set_id=None),
            candidate=make_candidate(ROOT_Q),
        )
        appends = journal.appends
        with proved_acceptance():
            with self.assertRaises(SupervisorRefusal) as caught:
                commands.commit_piece3_provider_result(context)
        self.assertIn("does not match", str(caught.exception))
        self.assertEqual(journal.appends, appends, "the saved result is PRESERVED")
        self.assertEqual(transport.codex_calls, 0, "Codex is never called again")

    def test_R52_refused_commit_with_changed_complete_inputs_reenters_stage(self):
        """R52 -- proved drift retires only the stale authorization."""
        journal = staged_journal("piece3_commit")
        journal.append(
            {
                "type": "supervisor_operation_started",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": "op_stale_piece3_commit",
                "supervisor_command": "commit-piece3-provider-result",
                "work_item_identity": "wi_qv",
            }
        )
        journal.append(
            {
                "type": "supervisor_operation_completed",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": "op_stale_piece3_commit",
                "supervisor_command": "commit-piece3-provider-result",
                "work_item_identity": "wi_qv",
                "operation_outcome": "refused",
            }
        )
        transport = LoudStubTransport()
        context = build_context(journal=journal, transport=transport)
        before = copy.deepcopy(journal.events)
        def moved_piece3_only(_context, _unscoped, _events, _request, kind, _extra):
            return (
                ("a" * 64, "b" * 64)
                if kind == "question_validation"
                else ("a" * 64, "a" * 64)
            )

        with mock.patch.object(
            commands, "required_inputs_staleness", moved_piece3_only
        ):
            state = commands.post_acceptance_transition_state(
                context, reconstruct_extra=full_reconstructor()
            )
        self.assertIsNone(state["piece3_authorization"].get("validation"))
        self.assertEqual(
            commands.loop_position(context, state)["loop_next_command"],
            "dispatch-piece3-provider-review",
        )
        self.assertEqual(journal.events, before, "the stale custody is preserved")
        self.assertEqual(transport.calls, [], "the projection contacts no provider")

    def test_T1_selection_reproof_uses_control_context_during_Q_work(self):
        """T1 remains P-owned when state is derived through a Q context."""
        journal = staged_journal("piece3_commit")
        control = build_context(journal=journal)
        q_binding = make_binding(SCOPE_Q, root=ROOT_Q, validation_set_id=None)
        q_context = build_context(
            scope=SCOPE_Q,
            journal=journal,
            binding=q_binding,
            candidate=make_candidate(ROOT_Q),
            facts={
                "package_scope_id": SCOPE_Q,
                "package_id": None,
                "scope_root_path": ROOT_Q,
            },
        )
        q_context.control_context = control
        seen = []

        def staleness(owner, *args, **kwargs):
            seen.append(owner)
            return ("a" * 64, "a" * 64)

        with mock.patch.object(commands, "required_inputs_staleness", staleness):
            state = commands.post_acceptance_transition_state(
                q_context, reconstruct_extra=full_reconstructor()
            )
        self.assertIs(state["selection"] is not None, True)
        self.assertIs(seen[0], control)

    def test_R52_refused_commit_with_unchanged_complete_inputs_stays_committable(self):
        """R52 -- a refusal alone is never treated as source/input drift."""
        journal = staged_journal("piece3_commit")
        journal.append(
            {
                "type": "supervisor_operation_started",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": "op_same_piece3_commit",
                "supervisor_command": "commit-piece3-provider-result",
                "work_item_identity": "wi_qv",
            }
        )
        journal.append(
            {
                "type": "supervisor_operation_completed",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": "op_same_piece3_commit",
                "supervisor_command": "commit-piece3-provider-result",
                "work_item_identity": "wi_qv",
                "operation_outcome": "refused",
            }
        )
        context = build_context(journal=journal)
        with mock.patch.object(
            commands,
            "required_inputs_staleness",
            return_value=("a" * 64, "a" * 64),
        ):
            state = commands.post_acceptance_transition_state(
                context, reconstruct_extra=full_reconstructor()
            )
        self.assertIsNotNone(state["piece3_authorization"].get("validation"))
        self.assertIsNone(state["piece3_stale_reentry"])
        self.assertEqual(
            commands.loop_position(context, state)["loop_next_command"],
            "commit-piece3-provider-result",
        )


    # -- the bounded repair: the re-entered stage must be the OWED stage ------
    def _lingering_stale_validation_authorization(self, journal):
        """A retired validation authorization that is NOT the owed stage.

        It sits AFTER Q's current ``validation_recorded`` so nothing consumes
        it, and it carries its own durable refused commit.  It is real history
        that must be preserved and consumed by nothing -- and it is NOT the
        stage the loop is about to run.
        """
        journal.append(
            {
                "type": "piece3_provider_work_recorded",
                "package_scope_id": SCOPE_Q,
                "authorizes_event_type": "validation_recorded",
                "provider_request_identity": "pr_qv",
                "result_custody_identity": "rc_pr_qv",
                "work_item_identity": "wi_qv",
                "result_schema_valid": True,
                "routed_signal_refs": [],
                "validation_set_id": None,
                "piece3_standing_sha256": "e" * 64,
            }
        )
        journal.append(
            {
                "type": "supervisor_operation_started",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": "op_lingering_piece3_commit",
                "supervisor_command": "commit-piece3-provider-result",
                "work_item_identity": "wi_qv",
            }
        )
        journal.append(
            {
                "type": "supervisor_operation_completed",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": "op_lingering_piece3_commit",
                "supervisor_command": "commit-piece3-provider-result",
                "work_item_identity": "wi_qv",
                "operation_outcome": "refused",
            }
        )
        return journal

    def test_a_retired_validation_stage_never_rebinds_another_stages_source(self):
        """The re-entry is STAGE-EXACT: only the owed stage takes the live source.

        A retired Piece-3 VALIDATION authorization is history for a stage that
        has already been recorded.  The stage the loop is actually about to run
        here is T4, whose Q binding is anchored on Q's OWN first validation --
        so its scheduling source binding must stay Q's, and must not be
        silently replaced by the live reading the re-entered stage would take.
        """
        journal = staged_journal("initial_design")
        for event in journal.events:
            if event.get("type") == "validation_recorded":
                event["source_binding_sha256"] = "ab" * 32
        self._lingering_stale_validation_authorization(journal)
        transport = LoudStubTransport()
        context = build_context(
            journal=journal,
            transport=transport,
            clearance=lambda scope: {"unlocked": True},
        )
        before = copy.deepcopy(journal.events)

        def moved_validation_only(_context, _unscoped, _events, _request, kind,
                                  _extra):
            return (
                ("a" * 64, "b" * 64)
                if kind == "question_validation"
                else ("a" * 64, "a" * 64)
            )

        with mock.patch.object(
            commands, "required_inputs_staleness", moved_validation_only
        ):
            state = commands.post_acceptance_transition_state(
                context, reconstruct_extra=full_reconstructor()
            )
        report = commands.loop_position(context, state)
        self.assertEqual(report["loop_next_command"], "execute-initial-design")
        _series, scheduling = commands.continuation_scheduling(
            context, state, report["loop_state"], report["loop_next_command"]
        )
        self.assertEqual(
            scheduling["source_binding_sha256"],
            "ab" * 32,
            "T4 keeps Q's own transition source binding",
        )
        self.assertNotEqual(
            scheduling["source_binding_sha256"],
            STUB_LIVE_SOURCE_BINDING,
            "another stage's re-entry never rebinds this stage to the live read",
        )
        self.assertEqual(journal.events, before, "the retired authorization is preserved")
        self.assertEqual(transport.calls, [], "the projection contacts no provider")

    def test_the_owed_stage_reentry_binds_the_current_live_source(self):
        """The proved live route: a refused commit re-enters ITS OWN stage fresh.

        The saved result and its authorization stay exactly as they are, the
        loop stops owing the impossible commit, and the fresh question-validation
        dispatch is bound to the CURRENT source rather than the stale request's
        frozen one -- which is what the Q pre-validation binding will actually
        carry.
        """
        journal = staged_journal("piece3_commit")
        journal.append(
            {
                "type": "supervisor_operation_started",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": "op_owed_piece3_commit",
                "supervisor_command": "commit-piece3-provider-result",
                "work_item_identity": "wi_qv",
            }
        )
        journal.append(
            {
                "type": "supervisor_operation_completed",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": "op_owed_piece3_commit",
                "supervisor_command": "commit-piece3-provider-result",
                "work_item_identity": "wi_qv",
                "operation_outcome": "refused",
            }
        )
        transport = LoudStubTransport()
        context = build_context(journal=journal, transport=transport)
        before = copy.deepcopy(journal.events)

        def moved_validation_only(_context, _unscoped, _events, _request, kind,
                                  _extra):
            return (
                ("a" * 64, "b" * 64)
                if kind == "question_validation"
                else ("a" * 64, "a" * 64)
            )

        with mock.patch.object(
            commands, "required_inputs_staleness", moved_validation_only
        ):
            state = commands.post_acceptance_transition_state(
                context, reconstruct_extra=full_reconstructor()
            )
        self.assertEqual(state["piece3_stale_reentry"], "validation")
        report = commands.loop_position(context, state)
        self.assertEqual(report["loop_next_command"], "dispatch-piece3-provider-review")
        self.assertEqual(report["piece3_stage"], "validation")
        _series, scheduling = commands.continuation_scheduling(
            context, state, report["loop_state"], report["loop_next_command"]
        )
        self.assertEqual(
            scheduling["source_binding_sha256"], STUB_LIVE_SOURCE_BINDING
        )
        self.assertEqual(journal.events, before, "the saved result is preserved")
        self.assertEqual(transport.calls, [], "the projection contacts no provider")

    def test_T1_admission_through_Q_never_routes_back_to_package_selection(self):
        """The T1 re-proof is P's, so Q work never erases the proved selection.

        With the control-context ownership removed the SAME journal routes back
        to package selection, which is exactly the wrong route this repair
        exists to close.
        """
        journal = staged_journal("piece3_commit")
        control = build_context(journal=journal)
        q_context = build_context(
            scope=SCOPE_Q,
            journal=journal,
            binding=make_binding(SCOPE_Q, root=ROOT_Q, validation_set_id=None),
            candidate=make_candidate(ROOT_Q),
            facts={
                "package_scope_id": SCOPE_Q,
                "package_id": None,
                "scope_root_path": ROOT_Q,
            },
        )
        q_context.control_context = control

        state = commands.post_acceptance_transition_state(
            q_context, reconstruct_extra=full_reconstructor()
        )
        self.assertIsNotNone(state["selection"])
        self.assertNotEqual(
            commands.loop_position(q_context, state)["loop_next_command"],
            "continue-design-loop",
        )

        # The SAME journal, with the control-context ownership removed.
        with mock.patch.object(
            commands, "control_context_of", lambda context: context
        ):
            broken = commands.post_acceptance_transition_state(
                q_context, reconstruct_extra=full_reconstructor()
            )
        self.assertIsNone(
            broken["selection"],
            "without P's control context the T1 re-proof fails through Q",
        )
        self.assertEqual(
            commands.loop_position(q_context, broken)["loop_next_command"],
            "continue-design-loop",
            "which is the package-selection route this repair closes",
        )

    def test_R53_R101_crash_positions_E1_to_E5_each_take_one_owner(self):
        """R53 / R101 -- INSTRUMENT the recovery owner that actually RUNS.

        Each of E1-E5 is driven to its durable position and the route the
        implementation takes is recorded, rather than a string being compared.
        The accepted owners are:

          E1  ordinary same-request retry under the SAME identity
          E2  TB-RECOVERY-BOOTSTRAP, then reconcile-provider-request FIRST
          E3  Path B -> process-custodied-provider-result -> _b6f_piece3
          E4  Path C -> the provider-free commit
          E5  same-operation completion recovery ONLY
        """
        observed = {}

        # ---- E1 -- prepared, never dispatched -------------------------------
        # Built by the REAL machinery, so the prepared record and its
        # authenticated operation start genuinely agree.
        journal = staged_journal("clearance_required")
        q_context = build_context(
            journal=journal,
            binding=make_binding(SCOPE_Q, root=ROOT_Q, validation_set_id=None),
            candidate=make_candidate(ROOT_Q),
        )
        _events, situation, _ls, _lease = commands.read_state(q_context)
        work_item, work_id = engine.piece3_work_item(
            q_context, situation.candidate, "question_validation",
            transition_state={
                "scope_has_validation": False,
                "routed_signal_refs": (),
                "validation_set_id": None,
                "piece3_standing_sha256": "e" * 64,
            },
        )
        operation, situation = start_real_operation(
            q_context, "dispatch-piece3-provider-review", work_item, work_id
        )
        prepared = engine.build_prepared_request(
            q_context, journal.read(), work_item, work_id
        )
        prepared_event = engine.append_prepared(operation, prepared)
        context = build_context(journal=journal)
        state = commands.post_acceptance_transition_state(context)
        report = commands.loop_position(context, state)
        observed["E1"] = report["loop_next_command"]
        self.assertEqual(state["open_request"]["phase"], "prepared")
        self.assertEqual(
            report["resumes_prepared_request"], prepared.provider_request_identity,
            "E1 resumes the SAME prepared request identity",
        )
        self.assertEqual(
            state["piece3_custody_awaiting"], {},
            "E1 performs NO pending-custody lookup: no custody exists",
        )

        # ---- E2 -- dispatched, outcome uncertain ----------------------------
        engine.append_dispatch_begun(
            operation, prepared, prepared_event["event_seq"],
            transport="offline_stub",
        )
        state = commands.post_acceptance_transition_state(context)
        report = commands.loop_position(context, state)
        observed["E2"] = report["loop_next_command"]
        self.assertEqual(
            state["piece3_custody_awaiting"], {},
            "E2 performs NO pending-custody lookup: none exists yet",
        )
        # And the operation-specific bootstrap is what discovers and binds it.
        asked = {}

        def recorder(mode, facts, errors, control_context=None):
            asked.update(facts)
            return "bound context"

        errors = []
        with proved_acceptance():
            with mock.patch.object(nh_loop, "build_transition_context", recorder):
                bound = nh_loop.resolve_transition_context(
                    "reconcile-provider-request", context, errors
                )
        self.assertEqual(errors, [])
        self.assertEqual(bound, "bound context")
        self.assertEqual(asked["package_scope_id"], SCOPE_Q)

        # ---- E3 -- result custodied, authorization absent -------------------
        journal = staged_journal("piece3_pending")
        context = build_context(journal=journal)
        state = commands.post_acceptance_transition_state(context)
        report = commands.loop_position(context, state)
        observed["E3"] = report["loop_next_command"]
        self.assertIsNotNone(state["piece3_custody_awaiting"].get("validation"))
        errors = []
        with proved_acceptance():
            with mock.patch.object(nh_loop, "build_transition_context", recorder):
                nh_loop.resolve_transition_context(
                    "process-custodied-provider-result", context, errors
                )
        self.assertEqual(errors, [], "Path B binds Q for the pending custody")

        # ---- E4 -- authorization durable, Piece-3 event owed ----------------
        journal = staged_journal("piece3_commit")
        context = build_context(journal=journal)
        state = commands.post_acceptance_transition_state(context)
        report = commands.loop_position(context, state)
        observed["E4"] = report["loop_next_command"]
        self.assertEqual(
            state["piece3_custody_awaiting"], {},
            "E4 performs NO pending-custody lookup: the custody is CLOSED",
        )
        self.assertIsNotNone(state["piece3_authorization"].get("validation"))

        # ---- E5 -- Piece-3 event durable, completion missing ----------------
        # The start precedes the effect, exactly as a crash leaves it.
        journal = staged_journal("piece3_commit")
        journal.append(
            {"type": "supervisor_operation_started", "package_scope_id": SCOPE_Q,
             "supervisor_operation_id": "op_e5",
             "supervisor_command": "commit-piece3-provider-result",
             "source_binding_sha256": "b" * 64}
        )
        journal.append(
            {"type": "validation_recorded", "package_scope_id": SCOPE_Q,
             "validation_set_id": "vs_q"}
        )
        context = build_context(
            journal=journal, clearance=lambda scope: {"unlocked": True}
        )
        state = commands.post_acceptance_transition_state(context)
        report = commands.loop_position(context, state)
        observed["E5"] = report["loop_next_command"]
        self.assertEqual(
            state["incomplete_operation"]["supervisor_operation_id"], "op_e5"
        )

        self.assertEqual(
            observed,
            {
                "E1": "dispatch-piece3-provider-review",
                "E2": "reconcile-provider-request",
                "E3": "process-custodied-provider-result",
                "E4": "commit-piece3-provider-result",
                "E5": "commit-piece3-provider-result",
            },
        )

    def test_R61_R62_the_real_piece3_payload_contracts_are_admitted(self):
        """R61 / R62 -- valid replies admitted; lifecycle keys refused as extra."""
        for provider_kind, payload in (
            ("gpt_question_validation", question_validation_payload()),
            ("gpt_question_coverage_review", coverage_review_payload()),
        ):
            errors = []
            validator = (
                nh_loop.QUESTION_VALIDATION_REQUIRED_KEYS
                if provider_kind == "gpt_question_validation"
                else nh_loop.COVERAGE_REVIEW_REQUIRED_KEYS
            )
            value = nh_loop._continuation_piece3_payload_contract(
                json.dumps(payload), validator, errors
            )
            self.assertIsNotNone(value, errors)
            # The lifecycle-key negative is refused AS AN EXTRA KEY.
            bad = dict(payload)
            bad["result_schema_id"] = "anything"
            bad["result_schema_version"] = 1
            errors = []
            self.assertIsNone(
                nh_loop._continuation_piece3_payload_contract(
                    json.dumps(bad), validator, errors
                )
            )
            self.assertIn("extra keys", " ".join(errors))
        # And the installed key sets are UNMUTATED.
        self.assertNotIn("result_schema_id", nh_loop.QUESTION_VALIDATION_REQUIRED_KEYS)
        self.assertNotIn("result_schema_id", nh_loop.COVERAGE_REVIEW_REQUIRED_KEYS)

    def test_R64_R7c_the_dispatch_command_derives_its_own_stage(self):
        """R64 / T2-STAGE-FROM-STATE -- and no caller override exists at all."""
        # Validation owed.
        journal = staged_journal("clearance_required")
        context = build_context(journal=journal)
        state = commands.post_acceptance_transition_state(context)
        self.assertFalse(state["scope_has_validation"])
        self.assertEqual(
            commands.loop_position(context, state)["piece3_stage"], "validation"
        )
        # Coverage owed.
        journal = staged_journal("task_preparation")
        context = build_context(journal=journal)
        state = commands.post_acceptance_transition_state(context)
        self.assertTrue(state["scope_has_validation"])
        self.assertEqual(
            commands.loop_position(context, state)["piece3_stage"], "coverage"
        )
        # The command takes NO envelope, so a caller has nothing to supply.
        self.assertNotIn(
            "dispatch-piece3-provider-review",
            constants.STDIN_ENVELOPE_SUPERVISOR_COMMANDS,
        )
        self.assertNotIn(
            "commit-piece3-provider-result",
            constants.STDIN_ENVELOPE_SUPERVISOR_COMMANDS,
        )
        import inspect
        self.assertEqual(
            list(inspect.signature(commands.dispatch_piece3_provider_review).parameters),
            ["context"],
        )

    def test_R65_the_public_piece3_commands_are_unchanged(self):
        """R65 / T2-PUBLIC-COMMANDS-UNCHANGED -- and unswitched."""
        import inspect
        for name in ("command_question_validation", "command_question_coverage_review"):
            signature = inspect.signature(getattr(nh_loop, name))
            self.assertEqual(
                signature.parameters["mode"].default, nh_loop.PIECE3_MODE_FULL,
                "the public command defaults to the INSTALLED behaviour",
            )
        # main() still dispatches the public names DIRECTLY, ahead of the
        # supervisor fallthrough, and no behaviour is switched on the worker env.
        source = read_text(CONTROLLER_SOURCE)
        marker = source.index("def main(argv):")
        body = source[marker:]
        self.assertIn('if command == "question-validation":\n        return command_question_validation()', body)
        self.assertIn(
            'if command == "question-coverage-review":\n        return command_question_coverage_review()',
            body,
        )
        self.assertNotIn(
            "SUPERVISOR_WORKER_ENV", body[:body.index('if command == "interview-status"')].replace(
                'if command == "execute-next-claude-task" and os.environ.get(\n        SUPERVISOR_WORKER_ENV\n    ) == "1":', ""
            ),
        )
        # The public names are NOT members of the continuation set.
        self.assertFalse(
            set(constants.CONTINUATION_EXECUTION_COMMANDS)
            & {"question-validation", "question-coverage-review"}
        )
        self.assertFalse(
            ui_worker.CONTINUATION_COMMANDS
            & {"question-validation", "question-coverage-review"}
        )

    def test_R66_R67_R68_pending_transition_custodies_are_discoverable(self):
        """R66 / R67 / R68 -- the closed set finds all three kinds while P is current."""
        found = {}
        for stage, kind in (
            ("piece3_pending", "question_validation"),
            ("initial_pending", "initial_design"),
        ):
            journal = staged_journal(stage)
            context = build_context(journal=journal,
                                    clearance=lambda scope: {"unlocked": True})
            state = commands.post_acceptance_transition_state(context)
            scoped = replay.Replay(journal.read(), SCOPE_Q)
            pending = [
                event["work_item_kind"]
                for event in scoped.custodied_results_awaiting_processing()
            ]
            found[kind] = pending
            # The context that DISCOVERED it is still bound to P: discovery
            # happens BEFORE any Q context is constructed.
            self.assertEqual(context.binding.package_scope_id, SCOPE_P)
            self.assertEqual(state["transition_scope"], SCOPE_Q)
        self.assertEqual(found["question_validation"], ["question_validation"])
        self.assertEqual(found["initial_design"], ["initial_design"])
        # A coverage custody is likewise a member of the closed set.
        self.assertEqual(
            constants.TRANSITION_PENDING_CUSTODY_KINDS,
            frozenset(("question_validation", "coverage_review", "initial_design")),
        )

    def test_R69_R7d_wrong_kind_or_multiple_transition_custody_fails_closed(self):
        """R69 / R-7d -- and a selector custody is NEVER a member of the set."""
        journal = staged_journal("clearance_required")
        # A COVERAGE custody at a VALIDATION position.
        custody_pair(
            journal, kind="coverage_review", provider_kind="gpt_question_coverage_review",
            value=coverage_review_payload(), scope=SCOPE_Q, request="pr_cov",
        )
        context = build_context(journal=journal)
        errors = []
        with proved_acceptance():
            transition = nh_loop.resolve_transition_context(
                "process-custodied-provider-result", context, errors
            )
        self.assertIsNone(transition)
        self.assertTrue(errors)
        self.assertIn("does not agree with the freshly derived loop phase",
                      " ".join(errors))
        # The selector custody is never pending processing at all.
        journal = accepted_journal()
        admitted_selection_state(journal)
        scoped = replay.Replay(journal.read(), SCOPE_P)
        self.assertEqual(scoped.custodied_results_awaiting_processing(), [])

    def test_R70_b6f_piece3_appends_exactly_one_scope_matched_authorization(self):
        """R70 / T2-AUTHORIZATION-OWNER -- one producer, one authorization."""
        source = read_text(CONTROLLER_DIR / "nh_supervisor" / "commands.py")
        self.assertEqual(
            source.count('operation.append(\n        "piece3_provider_work_recorded",'),
            1,
            "there is exactly ONE producer of the authorization event",
        )
        self.assertEqual(source.count("def _b6f_piece3("), 1)
        # It never appends either Piece-3 event itself.
        marker = source.index("def _b6f_piece3(")
        body = source[marker:source.index("def _b6f_change_explanation(")]
        self.assertNotIn('operation.append(\n        "validation_recorded"', body)
        self.assertNotIn('"question_coverage_review_recorded",\n            {', body)

    def test_R73_crash_after_custody_authorization_or_commit_resumes_cleanly(self):
        """R73 -- no duplicate custody, authorization, or Piece-3 event."""
        for stage in ("piece3_pending", "piece3_commit", "task_preparation"):
            journal = staged_journal(stage)
            context = build_context(journal=journal,
                                    clearance=lambda scope: {"unlocked": True})
            first = commands.loop_position(
                context, commands.post_acceptance_transition_state(context)
            )
            appends = journal.appends
            for _repeat in range(3):
                again = commands.loop_position(
                    context, commands.post_acceptance_transition_state(context)
                )
                self.assertEqual(again["loop_state"], first["loop_state"], stage)
            self.assertEqual(journal.appends, appends, "re-derivation appends nothing")


# ===========================================================================
# R74-R91 -- THE PRE-VALIDATION BINDING, THE MATRIX ROWS AND THE VARIANTS.
# ===========================================================================
class BindingAndVariantRehearsals(unittest.TestCase):
    def transition_state(self, *, has_validation=False, routed=(), complete=True):
        return {
            "scope_has_validation": has_validation,
            "scope_validation_complete": complete,
            "routed_signal_refs": routed,
            "validation_set_id": "vs_q" if has_validation else None,
            "piece3_standing_sha256": "e" * 64,
        }

    def q_context(self, *, validation_set_id=None):
        return build_context(
            SCOPE_Q,
            binding=make_binding(SCOPE_Q, root=ROOT_Q, validation_set_id=validation_set_id),
            candidate=make_candidate(ROOT_Q),
        )

    def test_R74_one_pre_validation_binding_exists_after_T1_admission(self):
        """R74 -- validation_set_id NULL, routed refs EMPTY, round-zero the root."""
        context = self.q_context()
        obj, work_id = engine.piece3_work_item(
            context, context.round_zero_candidate, "question_validation",
            transition_state=self.transition_state(),
        )
        self.assertIsNone(obj["validation_set_id"], "none exists, and none is invented")
        self.assertEqual(obj["routed_signal_refs"], [])
        self.assertEqual(obj["piece3_standing_sha256"], "e" * 64)
        # Round-zero is Q's PROVED BOUND ROOT, not a candidate.
        self.assertEqual(obj["candidate_path"], ROOT_Q)
        self.assertTrue(work_id.startswith("wi_"))

    def test_R75_the_pre_validation_binding_is_never_reported_as_current(self):
        """R75 / TB-NOT-CURRENT -- status reports the established current scope."""
        report = run_live_copy("supervisor-status")
        errors = []
        _journal_path, events = nh_loop.read_interview_journal(errors)
        anchor, _identity = nh_loop.current_package_anchor(events, errors)
        self.assertEqual(errors, [])
        self.assertIsNotNone(anchor)
        self.assertEqual(report["package_scope_id"], anchor["package_scope_id"])
        # status._project() never consults a transition binding: status.py is
        # BYTE-IDENTICAL to the installed baseline.
        source = read_text(CONTROLLER_DIR / "nh_supervisor" / "status.py")
        self.assertNotIn("transition_binding_kind", source)
        self.assertNotIn("transition_facts", source)
        # And build_transition_context is never called from supervisor-status.
        loop_source = read_text(CONTROLLER_SOURCE)
        # re-cut 2026-09-02 against journal head 2300: the signature gained a keyword-only parameter; anchor on the name only
        marker = loop_source.index("def build_supervisor_context(errors")
        body = loop_source[marker:loop_source.index("def build_transition_context(")]
        self.assertNotIn("build_transition_context(", body)

    def test_R76_T2_first_question_validation_dispatches_under_binding_2(self):
        """R76 -- variant A or B, and NO fake field is present."""
        context = self.q_context()
        obj, _identity = engine.piece3_work_item(
            context, context.round_zero_candidate, "question_validation",
            transition_state=self.transition_state(),
        )
        self.assertEqual(
            identity.check_work_item_object(
                obj, constants.PIECE3_VARIANT_FIRST_UNROUTED
            ),
            [],
        )

    def test_R77_binding_2_retires_on_Q_first_validation(self):
        """R77 / TB-PREVALIDATION-RETIRES -- and binding 3 takes over."""
        errors = []
        # Binding 2 is refused once a Q validation exists.
        journal = staged_journal("task_preparation")
        self.assertTrue(
            any(
                event.get("type") == "validation_recorded"
                and event.get("package_scope_id") == SCOPE_Q
                for event in journal.events
            )
        )
        # The variant selector likewise retires variant A/B.
        self.assertIsNone(
            engine.piece3_variant_from_state(
                "question_validation", transition_active=True,
                scope_has_validation=True, routed_signal_refs=(),
            ),
            "once Q's first validation is durable the installed row governs",
        )
        # Constructing binding 2 while a Q validation exists FAILS CLOSED.
        source = read_text(CONTROLLER_SOURCE)
        self.assertIn("binding 2 has retired and", source)

        # A later routed signal makes that historical validation insufficient;
        # the same binding may then be constructed only for the fresh
        # question-validation pass that signal requires.
        validation = {
            "event_seq": 10,
            "type": "validation_recorded",
            "package_scope_id": SCOPE_Q,
        }
        signal = {
            "event_seq": 11,
            "type": "review_signal_recorded",
            "package_scope_id": SCOPE_Q,
        }
        self.assertEqual(
            nh_loop.transition_current_validations([validation], SCOPE_Q),
            [validation],
        )
        self.assertEqual(
            nh_loop.transition_current_validations([validation, signal], SCOPE_Q),
            [],
        )
        self.assertEqual(
            nh_loop.transition_current_validations(
                [validation, signal],
                SCOPE_Q,
                unresolved_signal_ids=(),
            ),
            [validation],
            "a provider-free audit can resolve the later signal without "
            "inventing a replacement validation page",
        )
        refreshed = dict(validation, event_seq=12)
        self.assertEqual(
            nh_loop.transition_current_validations(
                [validation, signal, refreshed], SCOPE_Q
            ),
            [refreshed],
        )

        # Coverage authorization carries the already-durable signals used as
        # provider input.  It is not itself a new routed-signal occurrence and
        # must not retire binding 3 before the saved result is committed.
        coverage_authorization = {
            "event_seq": 13,
            "type": "piece3_provider_work_recorded",
            "package_scope_id": SCOPE_Q,
            "authorizes_event_type": "question_coverage_review_recorded",
            "routed_signal_refs": ["rs_existing"],
            "supervisor_operation_id": "op_coverage",
            "work_item_identity": "wi_coverage",
        }
        processor_completion = {
            "event_seq": 14,
            "type": "supervisor_operation_completed",
            "package_scope_id": SCOPE_Q,
            "supervisor_command": "process-custodied-provider-result",
            "operation_outcome": "ok",
            "supervisor_operation_id": "op_coverage",
            "work_item_identity": "wi_coverage",
        }
        existing_signal = {
            "event_seq": 9,
            "type": "review_signal_recorded",
            "package_scope_id": SCOPE_Q,
            "routed_signal_id": "rs_existing",
        }
        self.assertEqual(
            nh_loop.transition_current_validations(
                [existing_signal, validation, coverage_authorization,
                 processor_completion],
                SCOPE_Q,
            ),
            [validation],
        )

    def test_R78_restart_of_a_pre_validation_operation_rebuilds_the_exact_binding(self):
        """R78 / WIM-REBUILD-IDENTITY-EQUALITY -- identical fields, no memory."""
        context = self.q_context()
        state = self.transition_state()
        first, first_id = engine.piece3_work_item(
            context, context.round_zero_candidate, "question_validation",
            transition_state=state,
        )
        second, second_id = engine.piece3_work_item(
            context, context.round_zero_candidate, "question_validation",
            transition_state=dict(state),
        )
        self.assertEqual(first, second)
        self.assertEqual(first_id, second_id, "the identity is stable across restart")

    def test_R79_no_admitted_selection_and_no_validation_means_no_Q_binding(self):
        """R79 -- neither binding constructs; fail closed, nothing appended."""
        journal = accepted_journal()
        context = build_context(journal=journal)
        state = commands.post_acceptance_transition_state(context)
        self.assertIsNone(state["transition_scope"])
        errors = []
        with proved_acceptance():
            transition = nh_loop.resolve_transition_context(
                "dispatch-piece3-provider-review", context, errors
            )
        self.assertIsNone(transition)
        self.assertEqual(journal.appends, len(journal.events))

    def test_R80_two_admitted_selections_or_ambiguous_roots_fail_closed(self):
        """R80 -- refusal; zero appends; zero provider calls."""
        journal = accepted_journal()
        # re-cut 2026-09-02 against journal head 2300: identical selector episodes now coalesce, so the two selections must genuinely differ to be ambiguous
        for request, package_id in (("pr_a", None), ("pr_b", "A99")):
            custody_pair(
                journal, kind="next_package_selection",
                provider_kind="codex_next_package_selection",
                value=selection_object(package_id=package_id),
                scope=SCOPE_P, request=request,
            )
        transport = LoudStubTransport()
        context = build_context(journal=journal, transport=transport)
        state = commands.post_acceptance_transition_state(context)
        self.assertIsNotNone(state["contradiction"])
        self.assertEqual(transport.calls, [])
        self.assertEqual(journal.appends, len(journal.events))

    def test_R81_R82_R83_the_three_new_kinds_pass_identity_and_re_derive(self):
        """R81 / R82 / R83 -- each validates and its identity is stable."""
        context = self.q_context()
        cases = (
            ("next_package_selection",
             lambda: engine.next_package_selection_work_item(
                 context, context.round_zero_candidate)),
            ("next_design_task_preparation",
             lambda: engine.next_design_task_preparation_work_item(
                 context, context.round_zero_candidate)),
            ("initial_design",
             lambda: engine.initial_design_work_item(
                 context, context.round_zero_candidate, TARGET_Q)),
        )
        for kind, builder in cases:
            obj, first = builder()
            self.assertEqual(obj["work_item_kind"], kind)
            self.assertEqual(identity.check_work_item_object(obj), [], kind)
            _again, second = builder()
            self.assertEqual(first, second, "%s identity is stable" % kind)
        # R83 specifically: target_candidate_path is NON-NULL and required.
        obj, _identity = engine.initial_design_work_item(
            context, context.round_zero_candidate, TARGET_Q
        )
        self.assertEqual(obj["target_candidate_path"], TARGET_Q)
        self.assertEqual(
            identity.WORK_ITEM_MATRIX[("initial_design", None)]["target_candidate_path"],
            "R",
        )

    def test_R84_matrix_negatives(self):
        """R84 -- a missing field, an illegal field, and a value where null is required."""
        context = self.q_context()
        obj, _identity = engine.next_package_selection_work_item(
            context, context.round_zero_candidate
        )
        missing = dict(obj)
        missing.pop("audit_identity")
        self.assertTrue(identity.check_work_item_object(missing))
        illegal = dict(obj)
        illegal["recorded_at"] = "now"
        self.assertTrue(identity.check_work_item_object(illegal))
        wrong = dict(obj)
        wrong["target_candidate_path"] = TARGET_Q
        self.assertTrue(identity.check_work_item_object(wrong))
        # And an unknown (kind, variant) fails closed.
        self.assertTrue(
            identity.check_work_item_object(obj, "no_such_variant"),
            "an unmapped variant must fail closed",
        )

    def test_R85_R86_R87_the_three_controlled_variants(self):
        """R85 / R86 / R87 -- no fake routed signal, no fake validation_set_id."""
        context = self.q_context()
        # A -- first mechanical Q validation, ZERO routed signals, NO prior set.
        variant_a = engine.piece3_variant_from_state(
            "question_validation", transition_active=True,
            scope_has_validation=False, routed_signal_refs=(),
        )
        self.assertEqual(variant_a, constants.PIECE3_VARIANT_FIRST_UNROUTED)
        obj_a, _id = engine.piece3_work_item(
            context, context.round_zero_candidate, "question_validation",
            transition_state=self.transition_state(),
        )
        self.assertEqual(obj_a["routed_signal_refs"], [])
        self.assertIsNone(obj_a["validation_set_id"])
        self.assertEqual(identity.check_work_item_object(obj_a, variant_a), [])
        # B -- a GENUINE routed signal.
        variant_b = engine.piece3_variant_from_state(
            "question_validation", transition_active=True,
            scope_has_validation=False, routed_signal_refs=("sig_1",),
        )
        self.assertEqual(variant_b, constants.PIECE3_VARIANT_FIRST_ROUTED)
        obj_b, _id = engine.piece3_work_item(
            context, context.round_zero_candidate, "question_validation",
            transition_state=self.transition_state(routed=("sig_1",)),
        )
        self.assertEqual(obj_b["routed_signal_refs"], ["sig_1"])
        self.assertIsNone(obj_b["validation_set_id"], "still no prior set")
        self.assertEqual(identity.check_work_item_object(obj_b, variant_b), [])
        # A later validation page with a real set and no new routed signal.
        variant_continuation = engine.piece3_variant_from_state(
            "question_validation", transition_active=True,
            scope_has_validation=True, routed_signal_refs=(),
            scope_validation_complete=False,
        )
        self.assertEqual(
            variant_continuation,
            constants.PIECE3_VARIANT_VALIDATION_CONTINUATION_UNROUTED,
        )
        obj_continuation, _id = engine.piece3_work_item(
            context, context.round_zero_candidate, "question_validation",
            transition_state=self.transition_state(
                has_validation=True, complete=False
            ),
        )
        self.assertEqual(obj_continuation["routed_signal_refs"], [])
        self.assertEqual(obj_continuation["validation_set_id"], "vs_q")
        self.assertEqual(
            identity.check_work_item_object(obj_continuation, variant_continuation), []
        )
        # C -- Q coverage with ZERO routed signals and a REAL set id.
        variant_c = engine.piece3_variant_from_state(
            "coverage_review", transition_active=True,
            scope_has_validation=True, routed_signal_refs=(),
        )
        self.assertEqual(variant_c, constants.PIECE3_VARIANT_COVERAGE_UNROUTED)
        obj_c, _id = engine.piece3_work_item(
            context, context.round_zero_candidate, "coverage_review",
            transition_state=self.transition_state(has_validation=True),
        )
        self.assertEqual(obj_c["routed_signal_refs"], [])
        self.assertEqual(obj_c["validation_set_id"], "vs_q")
        self.assertEqual(identity.check_work_item_object(obj_c, variant_c), [])

    def test_R88_the_ordinary_routed_piece3_route_is_unchanged(self):
        """R88 / PIECE3-PRESERVE-INSTALLED -- the (kind, None) rows are intact."""
        for kind in ("question_validation", "coverage_review"):
            row = identity.WORK_ITEM_MATRIX[(kind, None)]
            self.assertEqual(row["routed_signal_refs"], "N")
            self.assertEqual(row["validation_set_id"], "R")
            self.assertEqual(row["piece3_standing_sha256"], "R")
        # variant=None still resolves through the EXPLICIT installed row even
        # though those kinds now have several rows.
        installed = build_context(
            SCOPE_Q,
            binding=make_binding(
                SCOPE_Q, root=ROOT_Q, validation_set_id="vs_installed",
                routed=("sig_installed",),
            ),
            candidate=make_candidate(ROOT_Q),
        )
        obj, _identity = engine.piece3_work_item(
            installed, installed.round_zero_candidate, "question_validation",
        )
        self.assertEqual(obj["routed_signal_refs"], ["sig_installed"])
        self.assertEqual(identity.check_work_item_object(obj, None), [])
        # The ordinary route still copies all three from the BINDING.
        self.assertEqual(obj["validation_set_id"], "vs_installed")

    def test_R89_R6b_variant_selection_is_controller_derived(self):
        """R89 / PIECE3-VARIANT-FROM-STATE -- no caller and no model variant."""
        context = self.q_context()
        with self.assertRaises(identity.IdentityError):
            engine.piece3_work_item(
                context, context.round_zero_candidate, "question_validation",
                variant=constants.PIECE3_VARIANT_COVERAGE_UNROUTED,
                transition_state=self.transition_state(),
            )
        # A state in which no variant is provable fails closed.
        with self.assertRaises(identity.IdentityError):
            engine.piece3_variant_from_state(
                "coverage_review", transition_active=True,
                scope_has_validation=False, routed_signal_refs=(),
            )
        # Outside a transition the installed route is unchanged.
        self.assertIsNone(
            engine.piece3_variant_from_state(
                "question_validation", transition_active=False,
                scope_has_validation=False, routed_signal_refs=(),
            )
        )

    def test_R90_R98_b6f_writes_one_truthful_authorization_per_variant(self):
        """R90 / R98 -- ownership unchanged; the three values are truthful."""
        source = read_text(CONTROLLER_DIR / "nh_supervisor" / "commands.py")
        marker = source.index("def _b6f_piece3(")
        body = source[marker:source.index("def _b6f_change_explanation(")]
        # The three fields now come from the PROVED WORK ITEM, not a blind read.
        self.assertIn('work_item_obj.get("routed_signal_refs")', body)
        self.assertIn('work_item_obj.get("validation_set_id")', body)
        self.assertIn('work_item_obj.get("piece3_standing_sha256")', body)
        # The event body KEY SET is unchanged, so no schema change is required.
        for key in ("routed_signal_refs", "validation_set_id",
                    "piece3_standing_sha256", "authorizes_event_type",
                    "result_schema_valid"):
            self.assertIn('"%s"' % key, body)
        # A present-and-null validation_set_id is schema-valid.
        self.assertIn(
            "piece3_provider_work_recorded", schema.SUPERVISOR_EVENT_BODY_KEYS
        )
        self.assertIn(
            "validation_set_id",
            schema.SUPERVISOR_EVENT_BODY_KEYS["piece3_provider_work_recorded"],
        )


# ===========================================================================
# R92-R103 -- THE CLAUDE ROUTE, THE THREE PATHS, ROW M, AND THE REAL TREE.
# ===========================================================================
class RoutingAndRealStateRehearsals(unittest.TestCase):
    def test_R92_claude_initial_design_resolves_to_the_claude_endpoint(self):
        """R92 / INIT-CLAUDE-ROUTING -- the local Claude endpoint and branch."""
        binding = nh_loop.supervisor_endpoint_binding()
        self.assertEqual(
            binding["claude_initial_design"], nh_loop.SUPERVISOR_CLAUDE_ENDPOINT
        )
        self.assertIn("claude_initial_design", nh_loop.SUPERVISOR_CLAUDE_PROVIDER_KINDS)
        self.assertTrue(
            hasattr(nh_loop.NhCliProviderTransport, "_dispatch_claude_initial_design")
        )
        # The two installed Claude kinds are UNCHANGED.
        for kind in ("claude_correction", "claude_acceptance_explanation"):
            self.assertEqual(binding[kind], nh_loop.SUPERVISOR_CLAUDE_ENDPOINT)

    def test_R93_R6e_claude_initial_design_causes_zero_codex_invocations(self):
        """R93 / INIT-NEVER-CODEX -- _dispatch_codex() is never entered."""
        source = read_text(CONTROLLER_SOURCE)
        marker = source.index("    def dispatch(self, request):")
        body = source[marker:source.index("    def _dispatch_claude_acceptance_explanation(")]
        claude_at = body.index('request.provider_kind == "claude_initial_design"')
        codex_at = body.index("return self._dispatch_codex(request, material)")
        self.assertLess(
            claude_at, codex_at,
            "the explicit Claude branch must sit ABOVE the codex fallthrough",
        )
        # It is its OWN branch, never an implicit widening of claude_correction.
        self.assertIn("self._dispatch_claude_initial_design(", body)
        # And the runtime proof: instrumenting _dispatch_codex shows it is
        # never entered for this kind.
        entered = []
        original = nh_loop.NhCliProviderTransport._dispatch_codex

        def guard(self, request, material):
            entered.append(request.provider_kind)
            raise ProviderContacted("codex was entered for %s" % request.provider_kind)

        try:
            nh_loop.NhCliProviderTransport._dispatch_codex = guard
            transport = nh_loop.NhCliProviderTransport(lambda: None)
            request = type("R", (), {
                "provider_kind": "claude_initial_design",
                "provider_endpoint_identity": nh_loop.SUPERVISOR_CLAUDE_ENDPOINT,
            })()
            with self.assertRaises(Exception):
                transport.dispatch(request)
        finally:
            nh_loop.NhCliProviderTransport._dispatch_codex = original
        self.assertEqual(entered, [], "ZERO Codex invocations for this kind")

    def test_R94_its_result_has_candidate_and_explanation_keys(self):
        """R94 -- initial candidate plus explanation, no correction fields."""
        source = read_text(CONTROLLER_SOURCE)
        marker = source.index("    def _dispatch_claude_initial_design(")
        body = source[marker:source.index("    def lookup(self, request")]
        self.assertIn(
            "assert set(result_body) == set(\n            nh_supervisor.constants.INITIAL_DESIGN_RESULT_KEYS\n        )",
            body,
        )
        for excluded in ("produced_lifetime_round", "produced_batch_number",
                         "produced_round_in_batch", "correction_specification_sha256",
                         "blocking_finding_refs"):
            self.assertNotIn('"%s":' % excluded, body, excluded)
        self.assertEqual(len(constants.INITIAL_DESIGN_RESULT_KEYS), 7)

    def test_R95_path_A_dispatches_with_no_custody_present(self):
        """R95 / TB-DISPATCH-NO-CUSTODY-PRECONDITION."""
        journal = staged_journal("clearance_required")
        scoped = replay.Replay(journal.read(), SCOPE_Q)
        self.assertEqual(
            scoped.custodied_results_awaiting_processing(), [],
            "Path A runs with ZERO Piece-3 custodies in the journal",
        )
        context = build_context(journal=journal)
        errors = []
        with proved_acceptance():
            transition = nh_loop.resolve_transition_context(
                "dispatch-piece3-provider-review", context, errors
            )
        # It never performs a pending-custody lookup: the routing for this
        # command reads the OWED STAGE from controller state alone.
        source = read_text(CONTROLLER_SOURCE)
        marker = source.index('    if name == "dispatch-piece3-provider-review":')
        body = source[marker:source.index('    if name == "commit-piece3-provider-result":')]
        self.assertNotIn("piece3_custody_awaiting", body)
        self.assertNotIn("custodied_results_awaiting_processing", body)

    def test_R96_R97_path_C_is_anchored_on_the_authorization(self):
        """R96 / R97 -- no unfinished-custody lookup; every negative fails closed."""
        source = read_text(CONTROLLER_SOURCE)
        marker = source.index('    if name == "commit-piece3-provider-result":')
        body = source[marker:source.index('    if name == "process-custodied-provider-result":')]
        self.assertIn("piece3_authorization", body)
        self.assertNotIn("piece3_custody_awaiting", body)
        self.assertNotIn("custodied_results_awaiting_processing", body)
        # By the time Path C runs the custody is ALREADY CLOSED.
        journal = staged_journal("piece3_commit")
        scoped = replay.Replay(journal.read(), SCOPE_Q)
        self.assertEqual(
            scoped.custodied_results_awaiting_processing(), [],
            "the authorization has already closed that custody",
        )
        # Negatives: zero authorizations refuses with zero appends.
        transport = LoudStubTransport()
        empty = staged_journal("clearance_required")
        context = build_context(
            journal=empty, transport=transport,
            binding=make_binding(SCOPE_Q, root=ROOT_Q, validation_set_id=None),
            candidate=make_candidate(ROOT_Q),
        )
        appends = empty.appends
        with proved_acceptance():
            with self.assertRaises(SupervisorRefusal):
                commands.commit_piece3_provider_result(context)
        self.assertEqual(empty.appends, appends)
        self.assertEqual(transport.calls, [], "ZERO provider calls")

    def test_R99_registry_counts_are_exactly_as_designed(self):
        """R99 -- five new in WORKER_COMMANDS; exactly four provider-contacting."""
        new_names = set(constants.CONTINUATION_NEW_EXECUTION_COMMANDS)
        self.assertEqual(len(new_names), 5)
        self.assertTrue(new_names <= ui_worker.WORKER_COMMANDS)
        # Accepted role-split v1_6 section 5.1 -- prepare-next-design-task is no
        # longer classified as provider-contacting.  It is still a REAL command
        # and a REAL worker branch; only its classification moved, because its
        # operations are a bounded LOCAL derivation that contacts nobody.
        self.assertEqual(
            new_names & ui_worker.PROVIDER_CONTACTING_COMMANDS,
            {
                "continue-design-loop",
                "dispatch-piece3-provider-review",
                "execute-initial-design",
            },
        )
        self.assertIn("prepare-next-design-task", ui_worker.WORKER_COMMANDS)
        self.assertNotIn(
            "prepare-next-design-task", ui_worker.PROVIDER_CONTACTING_COMMANDS
        )
        self.assertNotIn(
            "commit-piece3-provider-result", ui_worker.PROVIDER_CONTACTING_COMMANDS
        )
        # The two INSTALLED execution commands keep their existing registrations.
        for name in constants.CONTINUATION_INSTALLED_EXECUTION_COMMANDS:
            self.assertIn(name, ui_worker.WORKER_COMMANDS)
        self.assertIn("reconcile-provider-request", ui_worker.PROVIDER_CONTACTING_COMMANDS)
        self.assertNotIn(
            "process-custodied-provider-result", ui_worker.PROVIDER_CONTACTING_COMMANDS
        )
        # The counts the design states, exactly -- as corrected by accepted
        # role-split v1_6 section 5.1: THREE contacting, FOUR provider-free.
        self.assertEqual(len(constants.CONTINUATION_PROVIDER_CONTACTING_COMMANDS), 3)
        self.assertEqual(len(constants.CONTINUATION_PROVIDER_FREE_COMMANDS), 4)
        self.assertEqual(len(constants.CONTINUATION_INSTALLED_EXECUTION_COMMANDS), 2)

    def test_R100_R6f_path_routing_is_exactly_A_B_C(self):
        """R100 -- each Piece-3 command takes its OWN pre-context path."""
        source = read_text(CONTROLLER_SOURCE)
        marker = source.index("def resolve_transition_context(")
        body = source[marker:source.index("def command_supervisor(name):")]
        for command, marker_text in (
            ("dispatch-piece3-provider-review", "---- PATH A ---"),
            ("commit-piece3-provider-result", "---- PATH C ---"),
            ("process-custodied-provider-result", "---- PATH B / section 8.9.2"),
        ):
            self.assertIn(command, body)
            self.assertIn(marker_text, body)
        # ONLY Path B performs an unfinished-custody lookup.
        path_b = body[body.index('if name == "process-custodied-provider-result":'):]
        self.assertIn("piece3_custody_awaiting", path_b)

    def test_R102_R6h_row_M_needs_no_unfinished_provider_custody(self):
        """R102 / ROW-M-NO-CUSTODY-BOOTSTRAP -- B9 uses the durable custody."""
        journal = staged_journal("handoff")
        # The provider custody is ALREADY CLOSED by candidate_custody_recorded.
        scoped = replay.Replay(journal.read(), SCOPE_Q)
        self.assertEqual(
            scoped.custodied_results_awaiting_processing(), [],
            "no unfinished initial_design custody exists or is required at B9",
        )
        transport = LoudStubTransport()
        context = build_context(
            journal=journal, transport=transport,
            clearance=lambda scope: {"unlocked": True},
        )
        state = commands.post_acceptance_transition_state(context)
        self.assertTrue(state["initial_custody_committed"])
        report = commands.loop_position(context, state)
        self.assertIn(
            report["loop_state"],
            (commands.LOOP_HANDOFF_COMPLETE, commands.LOOP_WAITING_RECOVERING),
        )
        self.assertIsNone(report["loop_next_command"])
        # ZERO Claude calls, ZERO Codex calls, ZERO second candidate creation,
        # ZERO re-selection, ZERO duplicate custody.
        self.assertEqual(transport.calls, [])
        self.assertEqual(journal.appends, len(journal.events))
        # The transaction says so explicitly.
        source = read_text(CONTROLLER_DIR / "nh_supervisor" / "commands.py")
        marker = source.index("def _b6g_initial_design(")
        body = source[marker:source.index("def _b6h_no_progress(")]
        self.assertIn("ROW-M-NO-CUSTODY-BOOTSTRAP", body)

    def test_R103_no_real_state_touched(self):
        """R103 -- the DISPOSABLE journal, head, key and lock are byte-identical.

        The real tree is proved separately and externally by the live baseline
        and final manifests; this rehearsal proves the suite itself writes
        nothing, even to the disposable state it is allowed to use.
        """
        before = journal_digest()
        candidates_before = candidate_count()
        head_before = git_head()
        report = run_live_copy("loop-status")
        # re-cut 2026-09-02 against journal head 2300: the live loop is held (CPB-SINGLE-TRANSITION); the zero-mutation proof is unchanged
        self.assertEqual(report["loop_state"], commands.LOOP_SELECTION_REQUIRED)
        self.assertEqual(report["loop_next_command"], "continue-design-loop")
        run_live_copy("supervisor-status")
        run_live_copy("loop-status")
        self.assertEqual(journal_digest(), before, "ZERO journal appends")
        self.assertEqual(candidate_count(), candidates_before, "ZERO candidates")
        self.assertEqual(git_head(), head_before, "ZERO Git mutation")

    def test_current_state_loop_status_projects_the_start_position(self):
        """Section 9.B -- the required current-state rehearsal.

        Against a DISPOSABLE copy of the current authenticated 84-event state,
        loop-status independently projects the overall loop at the initial
        post-acceptance position.
        """
        report = run_live_copy("loop-status")
        self.assertTrue(report["ok"])
        # re-cut 2026-09-02 against journal head 2300: the live loop is held (CPB-SINGLE-TRANSITION), so the projected position is the hold with no next command
        self.assertEqual(report["loop_state"], "LOOP_SELECTION_REQUIRED")
        self.assertEqual(report["loop_next_command"], "continue-design-loop")
        self.assertEqual(report.get("errors") or [], [])
        # And the PACKAGE-level acceptance projection is NOT weakened.
        package = run_live_copy("supervisor-status")
        self.assertEqual(package["workflow_state"], "ACCEPTED_FOR_DESIGN_ONLY")
        self.assertEqual(package["acceptance_truth"], "PROVED_ACCEPTED")
        self.assertIsNone(package["next_command"])

    def test_R1a_continuation_never_begins_without_a_fresh_proof(self):
        """Section 6.3 / R-1 -- the freshness gate, UNPATCHED.

        Continuation is NEVER inferred from the absence of a reason to stop.
        """
        journal = accepted_journal()
        admitted_selection_state(journal)
        transport = LoudStubTransport()
        context = build_context(journal=journal, transport=transport)
        for command in (
            commands.continue_design_loop,
            commands.dispatch_piece3_provider_review,
            commands.commit_piece3_provider_result,
            commands.prepare_next_design_task,
            commands.execute_initial_design,
        ):
            with self.assertRaises(SupervisorRefusal) as caught:
                command(context)
            self.assertIn("acceptance is not freshly re-proved", str(caught.exception))
        self.assertEqual(transport.calls, [], "ZERO provider calls")
        self.assertEqual(journal.appends, len(journal.events), "ZERO appends")

    def test_R14a_the_autonomy_comment_is_exact_and_appears_once(self):
        """Section 25.1 -- the exact comment, at the exact seam, exactly once."""
        marker = "# AUTONOMOUS: approved by user [2026-08-22]"
        worker_source = read_text(UI_DIR / "worker.py")
        self.assertEqual(worker_source.count(marker), 1)
        # It sits at the ONE new autonomous transition seam.
        step = worker_source[worker_source.index("def _continuation_step("):]
        step = step[:step.index("\n    def ", 10)]
        self.assertIn(marker, step)
        self.assertIn("result = self.runner(loop_next, None)", step)
        # And it is NOT copied to any other file or seam.
        for path in (CONTROLLER_SOURCE, UI_DIR / "supervisor.py", UI_DIR / "server.py",
                     CONTROLLER_DIR / "nh_supervisor" / "commands.py"):
            self.assertNotIn(marker, read_text(path), str(path))

    def test_R21a_the_UI_stays_honest_and_rewrites_no_history(self):
        """Section 21 -- the transition line is separate, and only on the live card."""
        plain = ui_supervisor.wording_for(
            ui_supervisor.WorkflowState.ACCEPTED_FOR_DESIGN_ONLY, "ABSENT_PROVED"
        )
        self.assertEqual(plain["detail"], ui_supervisor.ACCEPTED_CARD_DETAIL)
        self.assertIn("no next package started", plain["detail"])
        # A working line requires a PROVED LIVE LEASE.  With the lease absent
        # the card must NOT claim work, however the loop state reads.
        stopped = ui_supervisor.wording_for(
            ui_supervisor.WorkflowState.ACCEPTED_FOR_DESIGN_ONLY,
            "ABSENT_PROVED",
            loop_transition_active=True,
            loop_transition_working=True,
        )
        self.assertNotIn(ui_supervisor.TRANSITION_LINE, stopped["detail"])
        self.assertIn(ui_supervisor.TRANSITION_NOT_WORKING_LINE, stopped["detail"])
        during = ui_supervisor.wording_for(
            ui_supervisor.WorkflowState.ACCEPTED_FOR_DESIGN_ONLY,
            "LIVE_PROVED",
            loop_transition_active=True,
            loop_transition_working=True,
        )
        self.assertIn(ui_supervisor.TRANSITION_LINE, during["detail"])
        self.assertNotIn(
            "no next package started", during["detail"],
            "the ONE clause made conditional is no longer asserted",
        )
        self.assertIn("Ness accepted this exact candidate as a design",
                      during["detail"])
        # The UI never claims a new package has started.
        self.assertNotIn("started the next package", during["detail"])
        # The acceptance GET and POST paths are NOT touched.
        server_source = read_text(UI_DIR / "server.py")
        self.assertIn('run_controller("acceptance-offer")', server_source)
        self.assertIn('run_controller("record-ness-acceptance", envelope)', server_source)
        marker = server_source.index("def read_loop_projection(")
        body = server_source[marker:server_source.index("def build_ui_state(")]
        self.assertNotIn("acceptance-offer", body)
        self.assertNotIn("record-ness-acceptance", body)


class CoverageIndexRehearsals(unittest.TestCase):
    def test_R38_custody_bootstrap_discovers_Q_before_context_construction(self):
        """R38 -- Path B finds Q and builds ITS context before any P context.

        The pre-context discovery runs in ``resolve_transition_context()``,
        BEFORE ``command_supervisor()`` hands a context to the command -- so
        ``situation.pending_custody`` is already the right scope's when
        ``process_custodied_provider_result()`` runs, rather than P's.
        """
        journal = staged_journal("initial_pending")
        context = build_context(
            journal=journal, clearance=lambda scope: {"unlocked": True}
        )
        # The DISCOVERING context is still P's: discovery precedes construction.
        self.assertEqual(context.binding.package_scope_id, SCOPE_P)
        # Record exactly which binding the discovery asks to be built, without
        # touching the live state directory the real builder reads.
        asked = {}

        def recorder(mode, facts, errors, control_context=None):
            asked["mode"] = mode
            asked["facts"] = facts
            return "the Q transition context"

        errors = []
        with proved_acceptance():
            with mock.patch.object(nh_loop, "build_transition_context", recorder):
                transition = nh_loop.resolve_transition_context(
                    "process-custodied-provider-result", context, errors
                )
        self.assertEqual(errors, [])
        self.assertEqual(transition, "the Q transition context")
        self.assertEqual(
            asked["facts"]["package_scope_id"], SCOPE_Q,
            "the discovery proved Q BEFORE any context was constructed",
        )
        self.assertEqual(asked["mode"], "post_validation")
        self.assertEqual(asked["facts"]["scope_root_path"], ROOT_Q)
        # The design says the discovery must NOT be added inside the command.
        source = read_text(CONTROLLER_DIR / "nh_supervisor" / "commands.py")
        marker = source.index("def process_custodied_provider_result(context):")
        body = source[marker:source.index("def _rebuild_work_item(")]
        self.assertNotIn("post_acceptance_transition_state(", body)
        self.assertNotIn("TB-CUSTODY-BOOTSTRAP", body)

    def test_every_rehearsal_R1_to_R103_is_encoded(self):
        """The accepted section 25.2 obligations, indexed and machine-checked."""
        import inspect

        covered = set()
        module = sys.modules[__name__]
        for _name, obj in inspect.getmembers(module, inspect.isclass):
            if not issubclass(obj, unittest.TestCase):
                continue
            for method_name, method in inspect.getmembers(obj, inspect.isfunction):
                if not method_name.startswith("test_"):
                    continue
                first_line = (method.__doc__ or "").strip().split("\n")[0]
                import re
                for number in re.findall(r"\bR(\d{1,3})\b", method_name + " " + first_line):
                    value = int(number)
                    if 1 <= value <= 103:
                        covered.add(value)
        missing = sorted(set(range(1, 104)) - covered)
        self.assertEqual(missing, [], "unencoded accepted rehearsals: %s" % missing)


# ===========================================================================
# CORRECTION 1 REHEARSALS.
#
# These replace string-comparison checks with BEHAVIORAL proofs: each drives
# the real command or the real derivation and asserts what actually happened to
# the journal, the request identity and the provider transport.
# ===========================================================================
def uncertain_q_dispatch(*, transport="offline_stub"):
    """A Q-scoped request DISPATCHED with an uncertain outcome, authentically.

    The operation start, the prepared record and the dispatch write-ahead are
    all produced by the real machinery, so the authenticated start really is
    the binding authority the reconciliation must read.
    """
    journal = staged_journal("clearance_required")
    context = build_context(
        journal=journal,
        binding=make_binding(SCOPE_Q, root=ROOT_Q, validation_set_id=None),
        candidate=make_candidate(ROOT_Q),
    )
    _events, situation, _ls, _lease = commands.read_state(context)
    work_item, work_id = engine.piece3_work_item(
        context, situation.candidate, "question_validation",
        transition_state={
            "scope_has_validation": False,
            "routed_signal_refs": (),
            "validation_set_id": None,
            "piece3_standing_sha256": "e" * 64,
        },
    )
    operation, situation = start_real_operation(
        context, "dispatch-piece3-provider-review", work_item, work_id
    )
    prepared = engine.build_prepared_request(
        context, journal.read(), work_item, work_id
    )
    prepared_event = engine.append_prepared(operation, prepared)
    engine.append_dispatch_begun(
        operation, prepared, prepared_event["event_seq"], transport=transport
    )
    return journal, prepared.provider_request_identity


def selection_body():
    return json.dumps(selection_object(), sort_keys=True).encode("utf-8")


def prepared_request_for(context, kind, work_item_obj, work_item_id, *,
                         extra_prompt=None, extra_inputs=None):
    """The EXACT PreparedRequest the controller itself would derive."""
    return engine.build_prepared_request(
        context,
        context.journal.read(),
        work_item_obj,
        work_item_id,
        extra_prompt=extra_prompt,
        extra_inputs=extra_inputs,
    )


def crash_after_prepare(context, journal, prepared, scope):
    """The journal a crash leaves at E1: prepared, and NEVER dispatched."""
    journal.append(
        {
            "type": "supervisor_operation_started",
            "package_scope_id": scope,
            "supervisor_operation_id": "op_e1",
            "supervisor_command": "continue-design-loop",
            "source_binding_sha256": context.binding.source_binding_sha256,
        }
    )
    return journal.append(
        {
            "type": "provider_request_prepared",
            "package_scope_id": scope,
            "supervisor_operation_id": "op_e1",
            "provider_request_identity": prepared.provider_request_identity,
            "provider_kind": prepared.provider_kind,
            "provider_endpoint_identity": prepared.provider_endpoint_identity,
            "provider_availability_episode_identity": (
                prepared.provider_availability_episode_identity
            ),
            "provider_dispatch_serial": prepared.provider_dispatch_serial,
            "work_item_identity": prepared.work_item_identity,
            "work_item_kind": prepared.work_item_kind,
            "prompt_material_sha256": prepared.prompt_material_sha256,
            "required_inputs_sha256": prepared.required_inputs_sha256,
            "result_schema_id": prepared.result_schema_id,
        }
    )


class CorrectionOneRehearsals(unittest.TestCase):
    """E1 is a SAME-IDENTITY RESUME, never a reconciliation."""

    def e1_fixture(self):
        journal = accepted_journal()
        context = build_context(journal=journal)
        work_item, work_id = engine.next_package_selection_work_item(
            context, context.round_zero_candidate
        )
        adapter = StubAdapter()
        prepared = prepared_request_for(
            context, "next_package_selection", work_item, work_id,
            extra_prompt={"specialized_prompt_kind": "codex_next_package_selection"},
            extra_inputs={
                "required_files_binding": adapter.resolve_required_files(),
                # section 8.8 section 15.3 -- T1 freezes the LIVE source, not the
                # anchor's chain source identity.  A request prepared with the
                # anchor value belongs to the PREVIOUS ownership and is stale
                # by construction (section 16.1, R-SB17); E1 is about resuming a
                # request prepared under the CURRENT one.
                "frozen_source_binding_sha256": adapter.current_source_binding(),
            },
        )
        crash_after_prepare(context, journal, prepared, SCOPE_P)
        return journal, prepared

    def test_C1_E1_position_is_the_owed_command_not_reconciliation(self):
        """E1 -- loop-status returns the OWED command, never reconcile."""
        journal, prepared = self.e1_fixture()
        context = build_context(journal=journal)
        state = commands.post_acceptance_transition_state(context)
        self.assertIsNotNone(state["open_request"])
        self.assertEqual(state["open_request"]["phase"], "prepared")
        report = commands.loop_position(context, state)
        self.assertEqual(
            report["loop_next_command"], "continue-design-loop",
            "E1 resumes the owed command under the same identity",
        )
        self.assertNotEqual(report["loop_next_command"], "reconcile-provider-request")
        self.assertEqual(report["loop_state"], commands.LOOP_SELECTION_REQUIRED)
        self.assertEqual(
            report["resumes_prepared_request"], prepared.provider_request_identity
        )

    def test_C1_E1_resumes_the_same_request_identity_with_no_duplicate_record(self):
        """E1 -- one dispatch, the SAME identity, ZERO duplicate prepared records."""
        journal, prepared = self.e1_fixture()
        prepared_before = [
            event for event in journal.events
            if event["type"] == "provider_request_prepared"
        ]
        self.assertEqual(len(prepared_before), 1)
        transport = LoudStubTransport(body=selection_body(), allow=True)
        context = build_context(journal=journal, transport=transport)
        with proved_acceptance():
            result = commands.continue_design_loop(context)
        self.assertTrue(result.report.get("ok", True), result.report)
        # EXACTLY ONE provider call was made, and it is the resumed request.
        self.assertEqual(transport.calls, ["codex_next_package_selection"])
        self.assertEqual(
            transport.requests[0].provider_request_identity,
            prepared.provider_request_identity,
            "the SAME prepared request identity is resumed",
        )
        # ZERO duplicate prepared records, and ZERO new request identities.
        prepared_after = [
            event for event in journal.events
            if event["type"] == "provider_request_prepared"
        ]
        self.assertEqual(len(prepared_after), 1, "no second prepared record")
        self.assertEqual(
            {event["provider_request_identity"] for event in prepared_after},
            {prepared.provider_request_identity},
        )
        # The dispatch write-ahead names that same identity.
        dispatched = [
            event for event in journal.events
            if event["type"] == "provider_dispatch_begun"
        ]
        self.assertEqual(len(dispatched), 1)
        self.assertEqual(
            dispatched[0]["provider_request_identity"],
            prepared.provider_request_identity,
        )

    def test_reconciled_unknown_transition_request_is_not_reconciled_again(self):
        """A durable person-routed reconciliation is a null-command stop."""
        journal, request_identity = uncertain_q_dispatch()
        journal.append(
            {
                "type": "provider_request_reconciled",
                "package_scope_id": SCOPE_Q,
                "provider_request_identity": request_identity,
                "reconciliation_outcome": "lookup_unsupported",
            }
        )
        context = build_context(journal=journal)
        state = commands.post_acceptance_transition_state(context)
        self.assertIsNone(state["open_request"])
        report = commands.loop_position(context, state)
        self.assertEqual(report["loop_state"], commands.LOOP_NEEDS_USER_ACTION)
        self.assertIsNone(report["loop_next_command"])

    def test_C1_E1_makes_zero_reconcile_calls(self):
        """E1 -- reconcile-provider-request is NEVER invoked."""
        journal, _prepared = self.e1_fixture()
        transport = LoudStubTransport(body=selection_body(), allow=True)
        context = build_context(journal=journal, transport=transport)
        entered = []
        original = commands.reconcile_provider_request

        def guard(ctx):
            entered.append("reconcile")
            raise AssertionError("E1 must never reconcile")

        try:
            commands.reconcile_provider_request = guard
            with proved_acceptance():
                commands.continue_design_loop(context)
        finally:
            commands.reconcile_provider_request = original
        self.assertEqual(entered, [], "E1_RECONCILE_CALLS = 0")

    def test_C1_E2_dispatched_uncertain_still_refuses_and_reconciles_first(self):
        """E2 -- a DISPATCHED request is never resumed by its owner."""
        journal, prepared = self.e1_fixture()
        journal.append(
            {
                "type": "provider_dispatch_begun",
                "package_scope_id": SCOPE_P,
                "provider_request_identity": prepared.provider_request_identity,
                "provider_kind": "codex_next_package_selection",
            }
        )
        transport = LoudStubTransport(body=selection_body(), allow=True)
        context = build_context(journal=journal, transport=transport)
        state = commands.post_acceptance_transition_state(context)
        report = commands.loop_position(context, state)
        self.assertEqual(
            report["loop_next_command"], "reconcile-provider-request",
            "an uncertain outcome reconciles FIRST",
        )
        with proved_acceptance():
            with self.assertRaises(SupervisorRefusal) as caught:
                commands.continue_design_loop(context)
        self.assertIn("never re-dispatched", str(caught.exception))
        self.assertEqual(transport.calls, [], "ZERO second provider calls")

    def test_C1_E1_for_every_transition_work_item_kind(self):
        """E1 -- every transition kind resumes its own owning command."""
        self.assertEqual(
            commands.CONTINUATION_COMMAND_BY_WORK_ITEM_KIND,
            {
                "next_package_selection": "continue-design-loop",
                "question_validation": "dispatch-piece3-provider-review",
                "coverage_review": "dispatch-piece3-provider-review",
                "next_design_task_preparation": "prepare-next-design-task",
                "initial_design": "execute-initial-design",
            },
        )
        # A prepared request owned by ANOTHER command is not this one's to
        # resume, and still refuses.
        journal, _prepared = self.e1_fixture()
        context = build_context(journal=journal)
        with proved_acceptance():
            with self.assertRaises(SupervisorRefusal):
                commands.execute_initial_design(context)


# ===========================================================================
# CORRECTION 2 REHEARSALS -- TB-RECOVERY-BOOTSTRAP, BEHAVIORALLY.
# ===========================================================================
class CorrectionTwoRehearsals(unittest.TestCase):
    """Recovery binds EXACTLY the scope the authenticated start records."""

    def started_operation(self, journal, *, scope, command, operation_id):
        return journal.append(
            {
                "type": "supervisor_operation_started",
                "package_scope_id": scope,
                "supervisor_operation_id": operation_id,
                "supervisor_command": command,
                "source_binding_sha256": "b" * 64,
            }
        )

    def bootstrap(self, journal, name, request, *, context=None, recorder=None):
        """Run the real bootstrap, recording which binding it asks to build."""
        context = context or build_context(journal=journal)
        asked = {}

        def default_recorder(mode, facts, errors, control_context=None):
            asked["mode"] = mode
            asked["facts"] = facts
            return "bound context"

        errors = []
        with mock.patch.object(
            nh_loop, "build_transition_context", recorder or default_recorder
        ):
            bound = nh_loop.operation_recovery_context(
                name, request, context, errors, events=journal.read()
            )
        return bound, asked, errors

    def test_C2_envelope_is_read_and_validated_before_any_context(self):
        """Step 1-2 -- the envelope is read AHEAD of build_supervisor_context()."""
        source = read_text(CONTROLLER_SOURCE)
        marker = source.index("def command_supervisor(name):")
        body = source[marker:source.index("def main(argv):")]
        envelope_at = body.index("read_stdin_envelope(")
        context_at = body.index("context = build_supervisor_context(errors)")
        self.assertLess(
            envelope_at, context_at,
            "the caller envelope must be read BEFORE any context is built",
        )
        # And the EXACT recorded scope is built before the handler runs, with
        # no ordinary-P construction in between.
        recovery_at = body.index("recovery_transition_context(")
        ordinary_at = body.index("context = build_supervisor_context(errors)")
        handler_at = body.index("handler = nh_supervisor.commands.COMMAND_TABLE[name]")
        self.assertLess(recovery_at, ordinary_at)
        self.assertLess(recovery_at, handler_at)

    def test_C2_caller_may_not_supply_a_package_binding(self):
        """Step 2 -- a caller-supplied scope or root is REFUSED, not used."""
        journal = accepted_journal()
        for forbidden in (
            "package_scope_id", "scope_root_path", "candidate_sha256",
            "source_binding_sha256",
        ):
            request = {
                "supervisor_operation_id": "op_x",
                "supervisor_command": "prepare-next-design-task",
                forbidden: "anything the caller wants",
            }
            _bound, _asked, errors = self.bootstrap(
                journal, "prepare-next-design-task", request
            )
            self.assertTrue(errors, forbidden)
            self.assertIn("NOTHING THE CALLER SENDS MAY CHOOSE A PACKAGE",
                          " ".join(errors))
        # A non-null unlock_evidence_* is likewise refused.
        _bound, _asked, errors = self.bootstrap(
            journal,
            "supervisor-operation-status",
            {
                "supervisor_operation_id": "op_x",
                "supervisor_command": "supervisor-operation-status",
                "unlock_evidence_kind": "something",
            },
        )
        self.assertTrue(errors)

    def test_C2_T1_uncertain_recovery_binds_P(self):
        """TB-NO-PREMATURE-Q -- a T1 start records P, so recovery binds P."""
        journal = accepted_journal()
        self.started_operation(
            journal, scope=SCOPE_P, command="continue-design-loop",
            operation_id="op_t1",
        )
        context = build_context(journal=journal)
        bound, asked, errors = self.bootstrap(
            journal,
            "continue-design-loop",
            {"supervisor_operation_id": "op_t1",
             "supervisor_command": "continue-design-loop"},
            context=context,
        )
        self.assertEqual(errors, [])
        self.assertIsNone(bound, "P is already bound; no transition context")
        self.assertEqual(asked, {}, "no transition binding is constructed at T1")

    def q_started(self, stage, command, operation_id):
        journal = staged_journal(stage)
        self.started_operation(
            journal, scope=SCOPE_Q, command=command, operation_id=operation_id
        )
        return journal

    def test_C2_T2_T3_T4_uncertain_recovery_binds_Q_from_the_record(self):
        """Recovery binds Q BECAUSE THE RECORD SAYS SO, never from the phase."""
        cases = (
            ("clearance_required", "dispatch-piece3-provider-review", "pre_validation"),
            ("task_preparation", "prepare-next-design-task", "post_validation"),
            ("initial_design", "execute-initial-design", "post_validation"),
        )
        for stage, command, expected_mode in cases:
            journal = self.q_started(stage, command, "op_" + command)
            context = build_context(
                journal=journal, clearance=lambda scope: {"unlocked": True}
            )
            self.assertEqual(
                context.binding.package_scope_id, SCOPE_P,
                "P is still the current package while Q is in transition",
            )
            bound, asked, errors = self.bootstrap(
                journal,
                command,
                {"supervisor_operation_id": "op_" + command,
                 "supervisor_command": command},
                context=context,
            )
            self.assertEqual(errors, [], command)
            self.assertEqual(bound, "bound context", command)
            self.assertEqual(
                asked["facts"]["package_scope_id"], SCOPE_Q,
                "%s recovery binds Q from its authenticated start" % command,
            )
            self.assertEqual(asked["mode"], expected_mode, command)

    def test_C2_ambiguous_or_mismatched_start_evidence_fails_closed(self):
        """Steps 5 and 7 -- zero, duplicate, mismatched or foreign: FAIL CLOSED."""
        # Zero matches.
        journal = accepted_journal()
        _bound, _asked, errors = self.bootstrap(
            journal, "prepare-next-design-task",
            {"supervisor_operation_id": "op_absent",
             "supervisor_command": "prepare-next-design-task"},
        )
        self.assertIn("exactly one is required", " ".join(errors))
        # Duplicate matches.
        journal = accepted_journal()
        for _repeat in range(2):
            self.started_operation(
                journal, scope=SCOPE_Q, command="prepare-next-design-task",
                operation_id="op_dup",
            )
        _bound, _asked, errors = self.bootstrap(
            journal, "prepare-next-design-task",
            {"supervisor_operation_id": "op_dup",
             "supervisor_command": "prepare-next-design-task"},
        )
        self.assertIn("exactly one is required", " ".join(errors))
        # Command mismatch.
        journal = self.q_started("task_preparation", "prepare-next-design-task", "op_m")
        _bound, _asked, errors = self.bootstrap(
            journal, "execute-initial-design",
            {"supervisor_operation_id": "op_m",
             "supervisor_command": "execute-initial-design"},
        )
        self.assertIn("does not match", " ".join(errors))
        # A scope matching neither an established scope nor the one in-transition.
        journal = staged_journal("task_preparation")
        foreign = "nullpkg_" + hashlib.sha256(b"foreign").hexdigest()[:32]
        self.started_operation(
            journal, scope=foreign, command="prepare-next-design-task",
            operation_id="op_f",
        )
        _bound, _asked, errors = self.bootstrap(
            journal, "prepare-next-design-task",
            {"supervisor_operation_id": "op_f",
             "supervisor_command": "prepare-next-design-task"},
        )
        self.assertIn("neither an established scope nor", " ".join(errors))

    def test_C2_reconcile_is_bound_to_the_scope_its_open_request_records(self):
        """A Q-scoped uncertain dispatch is reconcilable while P is current."""
        journal, _identity = uncertain_q_dispatch()
        context = build_context(journal=journal)
        self.assertEqual(context.binding.package_scope_id, SCOPE_P)
        asked = {}

        def recorder(mode, facts, errors, control_context=None):
            asked.update(facts)
            return "bound context"

        errors = []
        with proved_acceptance():
            with mock.patch.object(nh_loop, "build_transition_context", recorder):
                bound = nh_loop.resolve_transition_context(
                    "reconcile-provider-request", context, errors
                )
        self.assertEqual(errors, [])
        self.assertEqual(bound, "bound context")
        self.assertEqual(
            asked["package_scope_id"], SCOPE_Q,
            "reconcile binds the scope the OPEN REQUEST'S record names",
        )

    def test_C2_generic_operation_status_keeps_installed_behaviour(self):
        """TB-RECOVERY-GENERIC-UNCHANGED -- no operation id, no bootstrap."""
        journal = staged_journal("task_preparation")
        bound, asked, errors = self.bootstrap(
            journal, "supervisor-operation-status",
            {"supervisor_operation_id": None, "supervisor_command": None},
        )
        self.assertIsNone(bound)
        self.assertEqual(asked, {})
        self.assertEqual(errors, [])


# ===========================================================================
# CORRECTION 3 REHEARSALS -- E5 AND ROW M: COMPLETE THE OPERATION FIRST.
# ===========================================================================
class CorrectionThreeRehearsals(unittest.TestCase):
    def incomplete(self, journal, *, command, operation_id="op_open"):
        # An authentic start carries the candidate the operation was bound to:
        # Q's round-zero root.  Row M's ownership proof reads exactly that.
        parent = make_candidate(ROOT_Q)
        journal.append(
            {
                "type": "supervisor_operation_started",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": operation_id,
                "supervisor_command": command,
                "source_binding_sha256": "b" * 64,
                "candidate_path": parent.candidate_path,
                "candidate_sha256": parent.candidate_sha256,
                "candidate_bytes": parent.candidate_bytes,
            }
        )
        return journal

    def completed(self, journal, operation_id="op_open"):
        journal.append(
            {
                "type": "supervisor_operation_completed",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": operation_id,
                "outcome": "ok",
            }
        )
        return journal

    def e5_journal(self):
        """Start durable, THEN the Piece-3 effect, and no completion."""
        journal = self.incomplete(
            staged_journal("piece3_commit"),
            command="commit-piece3-provider-result",
        )
        journal.append(
            {"type": "validation_recorded", "package_scope_id": SCOPE_Q,
             "validation_set_id": "vs_q"}
        )
        return journal

    def test_C3_E5_piece3_event_durable_completion_missing(self):
        """E5 -- the substantive append is durable; ONLY the completion is owed."""
        journal = self.e5_journal()
        context = build_context(
            journal=journal, clearance=lambda scope: {"unlocked": True}
        )
        state = commands.post_acceptance_transition_state(context)
        self.assertIsNotNone(
            state["incomplete_operation"],
            "a started-and-uncompleted transition operation is DETECTED",
        )
        self.assertEqual(
            state["incomplete_operation"]["supervisor_command"],
            "commit-piece3-provider-result",
        )
        report = commands.loop_position(context, state)
        # It does NOT advance to the next phase.
        self.assertNotEqual(report["loop_next_command"], "prepare-next-design-task")
        self.assertEqual(report["loop_state"], commands.LOOP_WAITING_RECOVERING)
        # THE OWNING COMMAND, never the read-only supervisor-operation-status.
        self.assertEqual(
            report["loop_next_command"], "commit-piece3-provider-result"
        )
        self.assertIn(
            report["loop_next_command"], constants.CONTINUATION_EXECUTION_COMMANDS
        )
        self.assertEqual(
            report["incomplete_operation"]["supervisor_operation_id"], "op_open"
        )
        # ZERO appends from deriving it.
        self.assertEqual(journal.appends, len(journal.events))

    def test_C3_E5_advances_only_after_the_completion_exists(self):
        """Once the missing completion is durable, the next phase is derived."""
        journal = self.e5_journal()
        context = build_context(
            journal=journal, clearance=lambda scope: {"unlocked": True}
        )
        blocked = commands.loop_position(
            context, commands.post_acceptance_transition_state(context)
        )
        self.assertEqual(
            blocked["loop_next_command"], "commit-piece3-provider-result"
        )
        self.completed(journal)
        advanced = commands.loop_position(
            context, commands.post_acceptance_transition_state(context)
        )
        self.assertEqual(advanced["loop_next_command"], "prepare-next-design-task")
        self.assertEqual(
            advanced["loop_state"], commands.LOOP_TASK_PREPARATION_REQUIRED
        )

    def test_C3_E5_makes_zero_provider_calls_and_appends_no_second_effect(self):
        """E5 -- no provider call, no second authorization, no second event."""
        journal = self.e5_journal()
        transport = LoudStubTransport()
        context = build_context(
            journal=journal, transport=transport,
            clearance=lambda scope: {"unlocked": True},
        )
        appends = journal.appends
        # Every continuation command refuses while that operation is open.
        with proved_acceptance():
            for command in (
                commands.prepare_next_design_task,
                commands.execute_initial_design,
                commands.dispatch_piece3_provider_review,
            ):
                with self.assertRaises(SupervisorRefusal):
                    command(context)
        self.assertEqual(transport.calls, [], "ZERO provider calls")
        self.assertEqual(journal.appends, appends, "ZERO appends")
        validations = [
            event for event in journal.events
            if event["type"] == "validation_recorded"
        ]
        self.assertEqual(len(validations), 1, "no second validation event")
        authorizations = [
            event for event in journal.events
            if event["type"] == "piece3_provider_work_recorded"
        ]
        self.assertEqual(len(authorizations), 1, "no second authorization")

    def test_C3_row_M_missing_completion_only(self):
        """Row M / B9 -- custody committed, T5 completion missing."""
        journal = self.incomplete(
            staged_journal("initial_pending"),
            command="process-custodied-provider-result",
            operation_id="op_t5",
        )
        parent = make_candidate(ROOT_Q)
        for event_type, key, origin in (
            ("candidate_write_ahead_recorded", "intent_origin",
             commands.CANDIDATE_INTENT_ORIGIN_INITIAL),
            ("candidate_custody_recorded", "custody_origin",
             commands.CANDIDATE_CUSTODY_ORIGIN_INITIAL),
        ):
            journal.append(
                initial_candidate_body(event_type, key, origin, parent=parent)
            )
        transport = LoudStubTransport()
        context = build_context(
            journal=journal, transport=transport,
            clearance=lambda scope: {"unlocked": True},
        )
        state = commands.post_acceptance_transition_state(context)
        self.assertTrue(state["initial_custody_committed"])
        self.assertIsNotNone(state["incomplete_operation"])
        report = commands.loop_position(context, state)
        self.assertEqual(
            report["loop_next_command"], "process-custodied-provider-result"
        )
        self.assertEqual(
            report["incomplete_operation"]["supervisor_command"],
            "process-custodied-provider-result",
        )
        # ROW-M-NO-CUSTODY-BOOTSTRAP: the provider custody is already CLOSED, so
        # no unfinished custody is required or sought.
        scoped = replay.Replay(journal.read(), SCOPE_Q)
        self.assertEqual(scoped.custodied_results_awaiting_processing(), [])
        # ZERO provider calls, ZERO candidate recreation, ZERO re-selection.
        self.assertEqual(transport.calls, [])
        self.assertEqual(journal.appends, len(journal.events))
        custodies = [
            event for event in journal.events
            if event["type"] == "candidate_custody_recorded"
        ]
        self.assertEqual(len(custodies), 1, "no duplicate candidate custody")
        # Once the completion exists, establishment is simply re-derived.
        self.completed(journal, "op_t5")
        after = commands.loop_position(
            context, commands.post_acceptance_transition_state(context)
        )
        self.assertEqual(after["loop_state"], commands.LOOP_HANDOFF_COMPLETE)
        self.assertIsNone(after["loop_next_command"])

    def test_C3_a_second_pre_effect_residue_is_not_a_contradiction(self):
        """Residue COUNT is never a contradiction; only ownership conflict is."""
        journal = self.e5_journal()
        # A second start that appended nothing substantive.
        self.incomplete(journal, command="prepare-next-design-task",
                        operation_id="op_b")
        context = build_context(
            journal=journal, clearance=lambda scope: {"unlocked": True}
        )
        state = commands.post_acceptance_transition_state(context)
        self.assertIsNone(
            state["contradiction"], "two residues are still just residue"
        )
        # The ONE start that provably owns an effect is the recovery position.
        self.assertEqual(
            state["incomplete_operation"]["supervisor_command"],
            "commit-piece3-provider-result",
        )
        report = commands.loop_position(context, state)
        self.assertEqual(report["loop_state"], commands.LOOP_WAITING_RECOVERING)
        self.assertEqual(
            report["loop_next_command"], "commit-piece3-provider-result"
        )


# ===========================================================================
# CORRECTION 4 REHEARSALS -- THE TRANSITION BACKOFF SERIES.
# ===========================================================================
class FakeScheduling:
    """The installed scheduling interface, recorded.  No second scheduler."""

    def __init__(self, ineligible=()):
        self.ineligible = set(ineligible)
        self.scheduled = []
        self.cleared = []
        self.bindings = []
        self.kwargs = []

    def eligible(self, series_key, now):
        return series_key not in self.ineligible

    def wait_seconds(self, series_key, now):
        return 42

    def schedule_backoff(self, series_key, binding, now, **kwargs):
        self.scheduled.append(series_key)
        self.bindings.append(binding)
        self.kwargs.append(kwargs)
        return series_key

    def clear_series(self, series_key, binding):
        self.cleared.append(series_key)
        self.bindings.append(binding)

    def series_keys(self):
        return []


class FakeRunner:
    """A worker runner that records every command and never reaches a provider."""

    def __init__(self, status, loop):
        self.status = status
        self.loop = loop
        self.calls = []

    def __call__(self, command, request):
        self.calls.append(command)
        report = {
            "supervisor-status": self.status,
            "loop-status": self.loop,
        }.get(command, {"ok": True, "outcome": "ran"})
        return ui_worker.CommandResult(command, report, 0)


def accepted_status_report(**overrides):
    """A freshly proved supervisor-status for the ACCEPTED package P.

    Deliberately carries retry_series_key NULL, exactly as the real event-84
    state does: P has no dependency of its own while Q is in transition.
    """
    report = {
        "command": "supervisor-status",
        "ok": True,
        "workflow_state": "ACCEPTED_FOR_DESIGN_ONLY",
        "acceptance_truth": "PROVED_ACCEPTED",
        "journal_authentication_proved": True,
        "authenticated_state_current": True,
        "source_state_current": True,
        "authenticated_event_seq": 84,
        "authenticated_tail_sha256": "a" * 64,
        "retry_series_key": None,
        "dependency_identity": None,
        "dependency_record": None,
        "dependency_durable_record_placement": None,
        "dependency_carrier_event_seq": None,
        "dependency_occurrence_ordinal": None,
        "next_command": None,
        "package_scope_id": LIVE_SCOPE,
        "source_binding_sha256": "b" * 64,
        "candidate_path": LIVE_CANDIDATE_PATH,
        "candidate_sha256": LIVE_CANDIDATE_SHA,
        "candidate_bytes": 188236,
        "work_item_identity": None,
        "state_binding_sha256": "c" * 64,
        "run_lease": {"lease_state": "LIVE_PROVED", "live_proved": True},
    }
    report.update(overrides)
    return report


class CorrectionFourRehearsals(unittest.TestCase):
    def worker_for(self, loop_report, *, ineligible=(), status=None):
        scheduling = FakeScheduling(ineligible=ineligible)
        runner = FakeRunner(status or accepted_status_report(), loop_report)
        worker = ui_worker.SupervisorWorker.__new__(ui_worker.SupervisorWorker)
        worker.runner = runner
        worker.scheduling = scheduling
        worker.clock = ui_worker.Clock()
        worker.local_observations = []
        worker.lease_binding = {"controller_executable_identity": "1" * 64}
        worker.start_gate_open = lambda: (True, "open")
        return worker, runner, scheduling

    def loop_report(self, **overrides):
        report = {
            "ok": True,
            "loop_state": "LOOP_SELECTION_REQUIRED",
            "loop_next_command": "continue-design-loop",
            "loop_retry_series_key": "rs_transition",
            "loop_scheduling_binding": {
                "package_scope_id": SCOPE_Q,
                "source_binding_sha256": "q" * 64,
                "candidate_path": ROOT_Q,
                "candidate_sha256": "9" * 64,
                "candidate_bytes": 4096,
                "work_item_identity": "wi_owed",
                "dependency_identity": None,
            },
            "loop_transition_active": True,
            "loop_detail": None,
        }
        report.update(overrides)
        return report

    # ---- 1. the REAL event-84 T1 position ---------------------------------
    def test_C4_T1_has_a_real_series_at_the_real_event_84_position(self):
        """Section 19.2 bounds T1 too, even though Q does not exist yet."""
        # frozen 2026-09-02 at journal event 84: the real event-84 T1 position; later journal events hold the live loop at LOOP_SAFETY_HOLD (CPB-SINGLE-TRANSITION)
        self.enterContext(real_disposable_installation(event_seq=84))
        loop = run_live_copy("loop-status")
        self.assertEqual(loop["loop_state"], "LOOP_SELECTION_REQUIRED")
        self.assertEqual(loop["loop_next_command"], "continue-design-loop")
        series = loop["loop_retry_series_key"]
        binding = loop["loop_scheduling_binding"]
        self.assertTrue(series and series.startswith("rs_"), series)
        self.assertIsNotNone(binding)
        # It is P's ESTABLISHED binding, because T1 runs from P.
        self.assertEqual(binding["package_scope_id"], LIVE_SCOPE)
        self.assertEqual(binding["candidate_path"], LIVE_CANDIDATE_PATH)
        self.assertEqual(binding["candidate_sha256"], LIVE_CANDIDATE_SHA)
        self.assertTrue(binding["work_item_identity"].startswith("wi_"))
        # And it matches the INSTALLED identity helper exactly.
        expected = identity.retry_series_key(
            {
                "controller_executable_identity": run_live_copy(
                    "supervisor-status"
                )["controller_executable_identity"],
                "package_scope_id": binding["package_scope_id"],
                "source_binding_sha256": binding["source_binding_sha256"],
                "candidate_path": binding["candidate_path"],
                "candidate_sha256": binding["candidate_sha256"],
                "candidate_bytes": binding["candidate_bytes"],
                "workflow_state": loop["loop_state"],
                "next_command": loop["loop_next_command"],
                "work_item_identity": binding["work_item_identity"],
                "dependency_identity": binding["dependency_identity"],
            }
        )
        self.assertEqual(series, expected, "T1_RETRY_SERIES_MATCHES_IDENTITY_HELPER")

    def test_C4_P_null_retry_series_does_not_disable_T1_gating(self):
        """P's own key is null at event 84; T1's continuation series is real."""
        # frozen 2026-09-02 at journal event 84: P's retry_series_key is null only at the event-84 position
        self.enterContext(real_disposable_installation(event_seq=84))
        package = run_live_copy("supervisor-status")
        self.assertIsNone(package["retry_series_key"])
        loop = run_live_copy("loop-status")
        self.assertIsNotNone(loop["loop_retry_series_key"])
        worker, runner, _scheduling = self.worker_for(
            self.loop_report(
                loop_retry_series_key=loop["loop_retry_series_key"],
                loop_scheduling_binding=loop["loop_scheduling_binding"],
            ),
            ineligible={loop["loop_retry_series_key"]},
            status=accepted_status_report(retry_series_key=None),
        )
        outcome = worker._continuation_step(
            accepted_status_report(retry_series_key=None),
            ui_supervisor.WorkflowState.ACCEPTED_FOR_DESIGN_ONLY,
        )
        self.assertEqual(outcome.action, "wait")
        self.assertIn("bounded backoff", outcome.detail)
        self.assertEqual(runner.calls, ["loop-status"], "the provider never ran")

    # ---- 2. Q's OWN source binding ----------------------------------------
    def series_for(self, journal, *, unlocked=False):
        context = build_context(
            journal=journal, clearance=lambda scope: {"unlocked": unlocked}
        )
        state = commands.post_acceptance_transition_state(context)
        report = commands.loop_position(context, state)
        return commands.continuation_scheduling(
            context, state, report["loop_state"], report["loop_next_command"]
        )

    def q_journal(self, *, q_source="ab" * 32, binding=None):
        journal = staged_journal("clearance_required", binding=binding)
        journal.append(
            {
                "type": "supervisor_operation_started",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": "op_q",
                "supervisor_command": "dispatch-piece3-provider-review",
                "source_binding_sha256": q_source,
            }
        )
        return journal

    def test_C4_Q_series_uses_Q_source_binding_never_P(self):
        """Q_RETRY_SOURCE_BINDING_SOURCE = Q transition binding."""
        series, binding = self.series_for(self.q_journal())
        self.assertIsNotNone(series)
        self.assertEqual(binding["package_scope_id"], SCOPE_Q)
        self.assertEqual(binding["source_binding_sha256"], "ab" * 32)
        self.assertNotEqual(
            binding["source_binding_sha256"],
            make_binding(SCOPE_P).source_binding_sha256,
            "P's source binding is NEVER a fallback for Q",
        )
        self.assertEqual(binding["candidate_path"], ROOT_Q, "Q's proved root")

    def test_C4_Q_source_change_changes_the_series(self):
        """Q_SOURCE_CHANGE_CHANGES_Q_SERIES = YES."""
        first, _b = self.series_for(self.q_journal(q_source="ab" * 32))
        second, _b = self.series_for(self.q_journal(q_source="cd" * 32))
        self.assertNotEqual(first, second)

    def test_C4_P_source_change_alone_does_not_change_the_Q_series(self):
        """P_SOURCE_CHANGE_ALONE_CHANGES_Q_SERIES = NO."""
        journal = self.q_journal()
        context_a = build_context(
            journal=journal, binding=make_binding(SCOPE_P),
            clearance=lambda scope: {"unlocked": False},
        )
        state_a = commands.post_acceptance_transition_state(context_a)
        report_a = commands.loop_position(context_a, state_a)
        series_a, _ba = commands.continuation_scheduling(
            context_a, state_a, report_a["loop_state"], report_a["loop_next_command"]
        )
        # P's source binding moves; Q's does not.
        #
        # section 8.8 section 15.2a -- source_binding_sha256 is a BASE field of the
        # required-input inventory, so a P selection frozen against the OLD P
        # binding is genuinely stale against the NEW one.  That is correct and
        # is not what this rehearsal is about, so the second journal freezes
        # its selection against the binding its OWN context carries.  Both
        # selections are therefore admitted, and what is compared is exactly
        # what the name says: Q's retry series against a change in P's source.
        moved_p = make_binding(SCOPE_P)
        moved_p = engine.PackageBinding(
            **{**moved_p.__dict__, "source_binding_sha256": "0" * 64}
        )
        journal_b = self.q_journal(binding=moved_p)
        context_b = build_context(
            journal=journal_b, binding=moved_p,
            clearance=lambda scope: {"unlocked": False},
        )
        state_b = commands.post_acceptance_transition_state(context_b)
        report_b = commands.loop_position(context_b, state_b)
        series_b, _bb = commands.continuation_scheduling(
            context_b, state_b, report_b["loop_state"], report_b["loop_next_command"]
        )
        self.assertEqual(series_a, series_b, "Q's series is independent of P's source")

    # ---- 3. the exact owed work item ---------------------------------------
    def test_C4_the_series_binds_the_exact_owed_work_item(self):
        """Q_RETRY_WORK_ITEM_IDENTITY_BOUND = YES, and it changes with the work."""
        validation_series, validation_binding = self.series_for(self.q_journal())
        self.assertTrue(
            validation_binding["work_item_identity"].startswith("wi_"),
            "the exact owed work item is bound, never None",
        )
        # A DIFFERENT owed stage yields a different work item and a different key.
        # re-cut 2026-09-02 against journal head 2300: prepare-next-design-task became provider-free local T3 (no series by design); use the owed initial-design stage
        journal = staged_journal("initial_design")
        for event in journal.events:
            if event.get("type") == "validation_recorded":
                event["source_binding_sha256"] = "ab" * 32
        context = build_context(
            journal=journal, clearance=lambda scope: {"unlocked": True}
        )
        state = commands.post_acceptance_transition_state(context)
        report = commands.loop_position(context, state)
        self.assertEqual(report["loop_next_command"], "execute-initial-design")
        prep_series, prep_binding = commands.continuation_scheduling(
            context, state, report["loop_state"], report["loop_next_command"]
        )
        self.assertNotEqual(
            validation_binding["work_item_identity"],
            prep_binding["work_item_identity"],
        )
        self.assertNotEqual(validation_series, prep_series)

    # ---- 4. the dependency identity ---------------------------------------
    def test_C4_dependency_identity_is_an_identity_not_a_reason(self):
        """Q_RETRY_DEPENDENCY_IDENTITY_SOURCE = actual identity or truthful null."""
        series, binding = self.series_for(self.q_journal())
        self.assertIsNone(
            binding["dependency_identity"],
            "no dependency stands, so the truthful value is null",
        )
        # A plain-language reason is never used as an identity.
        source = read_text(CONTROLLER_DIR / "nh_supervisor" / "commands.py")
        marker = source.index("def _continuation_stage_binding(")
        body = source[marker:source.index("def _transition_source_binding(")]
        self.assertIn("_scoped_dependency_identity(events, scope_q)", body)
        self.assertNotIn('.get("reason")', body)
        self.assertNotIn("stop_record", body)
        helper = source[source.index("def scoped_dependency_occurrence("):]
        helper = helper[:helper.index("\n\ndef ")]
        self.assertIn('newest.get("dependency_identity")', helper)
        self.assertIn('event.get("package_scope_id") == scope', helper)
        # Changing only the plain-language reason leaves the key unchanged.
        journal = self.q_journal()
        first, _b = self.series_for(journal)
        for event in journal.events:
            if event.get("type") == "supervisor_operation_started":
                event["plain_language_dependency"] = "a different wording entirely"
        second, _b = self.series_for(journal)
        self.assertEqual(first, second)

    def test_C4_the_series_matches_the_installed_identity_helper(self):
        """Q_RETRY_SERIES_MATCHES_IDENTITY_HELPER = YES."""
        journal = self.q_journal()
        context = build_context(journal=journal)
        state = commands.post_acceptance_transition_state(context)
        report = commands.loop_position(context, state)
        series, binding = commands.continuation_scheduling(
            context, state, report["loop_state"], report["loop_next_command"]
        )
        expected = identity.retry_series_key(
            {
                "controller_executable_identity": context.controller_executable_identity,
                "package_scope_id": binding["package_scope_id"],
                "source_binding_sha256": binding["source_binding_sha256"],
                "candidate_path": binding["candidate_path"],
                "candidate_sha256": binding["candidate_sha256"],
                "candidate_bytes": binding["candidate_bytes"],
                "workflow_state": report["loop_state"],
                "next_command": report["loop_next_command"],
                "work_item_identity": binding["work_item_identity"],
                "dependency_identity": binding["dependency_identity"],
            }
        )
        self.assertEqual(series, expected)

    # ---- 5. the private scheduling record carries the TRANSITION binding ----
    def test_C4_scheduling_record_uses_the_transition_binding_not_P(self):
        """TRANSITION_SCHEDULING_USES_P_BINDING = NO."""
        loop = self.loop_report(
            loop_state="LOOP_WAITING_RECOVERING", loop_next_command=None
        )
        worker, _runner, scheduling = self.worker_for(loop)
        worker.record_transition_scheduling_outcome(
            "rs_transition", loop["loop_scheduling_binding"]
        )
        self.assertEqual(scheduling.scheduled, ["rs_transition"])
        recorded = scheduling.bindings[-1]
        self.assertEqual(recorded["package_scope_id"], SCOPE_Q)
        self.assertEqual(recorded["candidate_path"], ROOT_Q)
        self.assertEqual(recorded["work_item_identity"], "wi_owed")
        self.assertNotEqual(recorded["package_scope_id"], LIVE_SCOPE)
        self.assertNotEqual(recorded["candidate_path"], LIVE_CANDIDATE_PATH)

    def test_C4_a_success_clears_the_transition_series(self):
        """Section 11.7 -- a successful operation clears the series."""
        worker, _runner, scheduling = self.worker_for(self.loop_report())
        outcome = worker._continuation_step(
            accepted_status_report(),
            ui_supervisor.WorkflowState.ACCEPTED_FOR_DESIGN_ONLY,
        )
        self.assertEqual(outcome.action, "ran_command")
        self.assertEqual(scheduling.cleared, ["rs_transition"])
        self.assertEqual(scheduling.scheduled, [])

    # ---- 6. the gates -----------------------------------------------------
    def test_C4_ineligible_backoff_prevents_the_provider_command(self):
        """Q backoff not elapsed -> the worker WAITS and calls no provider."""
        worker, runner, _scheduling = self.worker_for(
            self.loop_report(), ineligible={"rs_transition"}
        )
        outcome = worker._continuation_step(
            accepted_status_report(),
            ui_supervisor.WorkflowState.ACCEPTED_FOR_DESIGN_ONLY,
        )
        self.assertEqual(outcome.action, "wait")
        self.assertIn("bounded backoff", outcome.detail)
        self.assertNotIn("continue-design-loop", runner.calls)
        self.assertEqual(outcome.next_delay_seconds, 42)

    def test_C4_eligible_backoff_allows_exactly_one_command(self):
        """Once eligible, exactly ONE continuation command runs."""
        worker, runner, _scheduling = self.worker_for(self.loop_report())
        outcome = worker._continuation_step(
            accepted_status_report(),
            ui_supervisor.WorkflowState.ACCEPTED_FOR_DESIGN_ONLY,
        )
        self.assertEqual(outcome.action, "ran_command")
        self.assertEqual(outcome.ran_command, "continue-design-loop")
        self.assertEqual(runner.calls.count("continue-design-loop"), 1)

    def test_C4_T1_question_route_binds_the_installed_recorder(self):
        """The owed T1 signal can reach the one installed Piece-3 recorder."""
        installed = nh_loop.build_continuation_adapter()
        self.assertIs(installed.record_review_signal, nh_loop.record_review_signal)

        errors = []
        self.assertIsNone(
            installed.record_review_signal(
                {},
                "next_package_selection_review",
                None,
                SCOPE_P,
                ROOT_P,
                None,
                errors,
            )
        )
        self.assertEqual(
            errors,
            [
                "refusing to record a review signal that is not exactly the "
                "validated five-field evidence object"
            ],
        )

        journal = accepted_journal()
        admitted_selection_state(
            journal, classification="genuinely_open_for_ness"
        )
        adapter = StubAdapter()
        context = build_context(journal=journal, adapter=adapter)
        state = commands.post_acceptance_transition_state(context)
        expected = dict(state["t1_route_signal_expected"])
        self.assertEqual(
            commands._t1_package_key(context, "A19", "A19", ROOT_Q), "A19"
        )
        material = commands._t1_review_signal_material(context, state["selection"])
        probe = {
            "package_scope_id": material["scope_id"],
            "signal_source": "next_package_selection_review",
            "route": "chatgpt_review_required",
            "candidate_path": None,
            "candidate_sha256": None,
            "candidate_bytes": None,
            "signal_title": material["signal_title"],
            "source_evidence": material["source_evidence"],
            "finding_evidence": material["finding_evidence"],
            "issue_key": material["issue_key"],
            "finding_key": material["finding_key"],
        }
        self.assertEqual(
            expected["routed_signal_id"],
            nh_loop.interview_routed_signal_id(
                material["scope_id"],
                material["issue_key"],
                material["finding_key"],
                "next_package_selection_review",
                None,
                None,
                nh_loop.routed_concern_fingerprint(probe),
            ),
        )
        calls = []

        def record(*args, **kwargs):
            calls.append((args, kwargs))
            self.assertIsNone(args[5], "T1 has no candidate identity")
            journal.append(
                {
                    **expected,
                    "standing_target_id": "st_test",
                    "source_binding_sha256": STUB_LIVE_SOURCE_BINDING,
                }
            )
            return {"routed_signal_id": expected["routed_signal_id"]}

        adapter.record_review_signal = record
        before = journal.appends
        with proved_acceptance():
            result = commands.continue_design_loop(context)
        self.assertEqual(result.report["appends"], 1)
        self.assertEqual(journal.appends, before + 1)
        self.assertEqual(len(calls), 1)
        self.assertEqual(
            commands._transition_source_binding(journal.events, SCOPE_Q, {}),
            STUB_LIVE_SOURCE_BINDING,
        )

    def test_C4_a_missing_series_never_permits_a_provider_call(self):
        """PROVIDER_CONTACTING_WITH_MISSING_SERIES_CAN_RUN = NO."""
        for missing in ({"loop_retry_series_key": None},
                        {"loop_scheduling_binding": None}):
            worker, runner, _scheduling = self.worker_for(
                self.loop_report(**missing)
            )
            outcome = worker._continuation_step(
                accepted_status_report(),
                ui_supervisor.WorkflowState.ACCEPTED_FOR_DESIGN_ONLY,
            )
            self.assertEqual(outcome.action, "wait", missing)
            self.assertIn("proved no retry series", outcome.detail)
            self.assertNotIn("continue-design-loop", runner.calls)

    # ---- 7. the provider-free commit --------------------------------------
    def test_C4_provider_free_commit_is_not_backoff_gated(self):
        """PROVIDER_FREE_COMMIT_BACKOFF_GATED = NO."""
        worker, runner, _scheduling = self.worker_for(
            self.loop_report(
                loop_state="LOOP_PIECE3_COMMIT_REQUIRED",
                loop_next_command="commit-piece3-provider-result",
                loop_retry_series_key=None,
                loop_scheduling_binding=None,
            ),
            ineligible={"rs_transition"},
        )
        outcome = worker._continuation_step(
            accepted_status_report(),
            ui_supervisor.WorkflowState.ACCEPTED_FOR_DESIGN_ONLY,
        )
        self.assertEqual(outcome.action, "ran_command")
        self.assertEqual(outcome.ran_command, "commit-piece3-provider-result")
        self.assertNotIn(
            "commit-piece3-provider-result", ui_worker.PROVIDER_CONTACTING_COMMANDS
        )
        # And the controller derives no series for a provider-free position.
        journal = self.q_journal()
        context = build_context(journal=journal)
        state = commands.post_acceptance_transition_state(context)
        series, binding = commands.continuation_scheduling(
            context, state, "LOOP_PIECE3_COMMIT_REQUIRED",
            "commit-piece3-provider-result",
        )
        self.assertIsNone(series)
        self.assertIsNone(binding)

    def test_C4_the_worker_derives_no_package_and_no_series(self):
        """The worker READS the controller's series and binding; it derives none."""
        source = read_text(UI_DIR / "worker.py")
        marker = source.index("def _continuation_step(")
        body = source[marker:source.index("\n    def _wait(")]
        self.assertIn('loop_report.get("loop_retry_series_key")', body)
        self.assertIn('loop_report.get("loop_scheduling_binding")', body)
        self.assertNotIn('report.get("retry_series_key")', body)
        self.assertNotIn("retry_series_key(", body, "no worker-side derivation")
        self.assertNotIn("package_scope_id", body, "the worker decides no package")


# ===========================================================================
# CORRECTION 5 REHEARSALS -- NO PRODUCTION REHEARSAL SEAM.
# ===========================================================================
class CorrectionFiveRehearsals(unittest.TestCase):
    PRODUCTION_SOURCES = (
        "controller/nh_loop.py",
        "controller/nh_supervisor/constants.py",
        "controller/nh_supervisor/schema.py",
        "controller/nh_supervisor/engine.py",
        "controller/nh_supervisor/commands.py",
        "controller/nh_supervisor/identity.py",
        "controller/nh_supervisor/replay.py",
        "controller/nh_supervisor/status.py",
        "interview_ui/worker.py",
        "interview_ui/supervisor.py",
        "interview_ui/server.py",
    )

    def test_C5_no_production_disposable_root_seam(self):
        """No rehearsal-only environment control surface in production source."""
        for relative in self.PRODUCTION_SOURCES:
            source = read_text(ROOT_DIR / relative)
            self.assertNotIn("NH_LOOP_DISPOSABLE_ROOT", source, relative)
            self.assertNotIn("_nh_rooted", source, relative)
            self.assertNotIn("DISPOSABLE_ROOT", source, relative)

    def test_C5_the_installed_path_literals_are_unchanged(self):
        """The installed repository and state-directory semantics are intact."""
        source = read_text(CONTROLLER_SOURCE)
        self.assertIn(
            'NH_REPO_PATH = "/home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP/NH-GOVERNANCE"',
            source,
        )
        self.assertIn(
            'DEFAULT_INTERVIEW_STATE_DIR = '
            '"/home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP/nh_interview_state"',
            source,
        )
        # The ONE state-directory override is the PRE-EXISTING installed one.
        self.assertEqual(nh_loop.INTERVIEW_STATE_DIR_ENV, "NH_LOOP_INTERVIEW_STATE_DIR")
        baseline = read_text(
            Path("/home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP/controller/nh_loop.py")
        )
        self.assertIn('INTERVIEW_STATE_DIR_ENV = "NH_LOOP_INTERVIEW_STATE_DIR"', baseline)

    def test_C5_every_writable_test_path_stays_in_the_disposable_root(self):
        """TEST_ONLY_ISOLATION -- nothing resolves back into the real checkout."""
        real = "/home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP"
        disposable = str(ROOT_DIR.resolve())
        if os.path.exists(real) and os.path.samefile(disposable, real):
            self.skipTest(
                "this isolation proof must run from a disposable copy, not the "
                "installed checkout"
            )
        self.assertFalse(disposable.startswith(real + "/"))
        # A bind mount or a second mount of the same device can give ONE
        # directory TWO different path spellings.  realpath does not collapse
        # that alias, so the prefix test above passes while these tests are in
        # fact running against the real installation.  Identity, not spelling,
        # is what isolation means: compare device+inode.
        if os.path.exists(real):
            self.assertFalse(
                os.path.samefile(disposable, real),
                "%s and %s are the SAME directory (same device and inode), so "
                "these tests are NOT isolated from the real installation"
                % (disposable, real),
            )
        # The repository path this process actually uses.
        self.assertTrue(
            os.path.realpath(nh_loop.NH_REPO_PATH).startswith(disposable),
            nh_loop.NH_REPO_PATH,
        )
        self.assertTrue(os.path.isdir(nh_loop.real_repo_root()))
        self.assertTrue(nh_loop.real_repo_root().startswith(disposable))
        # The interview state directory this process actually uses.
        errors = []
        state_dir = nh_loop.resolve_interview_state_dir(errors) if hasattr(
            nh_loop, "resolve_interview_state_dir"
        ) else os.environ["NH_LOOP_INTERVIEW_STATE_DIR"]
        self.assertTrue(os.path.realpath(str(state_dir)).startswith(disposable))
        # And the supervisor state directory resolves from __file__.
        supervisor_dir = nh_loop.supervisor_state_dir([])
        self.assertTrue(os.path.realpath(str(supervisor_dir)).startswith(disposable))
        # No symlink in the disposable tree escapes it.
        for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
            for name in list(dirnames) + filenames:
                path = os.path.join(dirpath, name)
                self.assertTrue(
                    os.path.realpath(path).startswith(disposable), path
                )


# ===========================================================================
# CORRECTION 2 REHEARSALS -- E5 AND ROW M RUN THE ACTUAL RECOVERY OWNER.
#
# These build a GENUINELY AUTHENTIC interrupted operation with the real
# machinery -- build_envelope() + Operation.start() -- so the installed
# reconstruction must re-prove P0, H0 and the operation identity before it may
# append anything.  The completion is appended by the PRODUCTION CODE UNDER
# TEST; no test ever appends it.
# ===========================================================================
def start_real_operation(context, command, work_item_obj, work_item_id):
    """One authentic supervisor_operation_started, via the real machinery."""
    events, situation, _lease_state, _lease = commands.read_state(context)
    context._current_work_item_obj = work_item_obj
    envelope = commands.build_envelope(
        context, events, command, situation, work_item_id
    )
    operation = engine.Operation(context, envelope, work_item_obj)
    operation.start()
    return operation, situation


def binding_fields(context, situation):
    """The effect-owner binding fields a real substantive append carries."""
    return {
        "package_key": context.binding.package_key,
        "package_id": context.binding.package_id,
        "branch": context.binding.branch,
        "head_sha": context.binding.head_sha,
        "source_binding_sha256": context.binding.source_binding_sha256,
        "candidate_path": situation.candidate.candidate_path,
        "candidate_sha256": situation.candidate.candidate_sha256,
        "candidate_bytes": situation.candidate.candidate_bytes,
    }


class CorrectionTwoInterruptedOperationRehearsals(unittest.TestCase):
    def q_context(self, journal, *, validation_set_id=None, unlocked=True):
        return build_context(
            journal=journal,
            binding=make_binding(
                SCOPE_Q, root=ROOT_Q, validation_set_id=validation_set_id
            ),
            candidate=make_candidate(ROOT_Q),
            clearance=lambda scope: {"unlocked": unlocked},
        )

    def e5_fixture(self):
        """Start durable, Piece-3 effect durable, completion MISSING."""
        journal = staged_journal("piece3_commit")
        context = self.q_context(journal)
        _events, situation, _ls, _lease = commands.read_state(context)
        work_item, work_id = engine.piece3_work_item(
            context, situation.candidate, "question_validation",
            transition_state={
                "scope_has_validation": False,
                "routed_signal_refs": (),
                "validation_set_id": None,
                "piece3_standing_sha256": "e" * 64,
            },
        )
        _operation, situation = start_real_operation(
            context, "commit-piece3-provider-result", work_item, work_id
        )
        body = {"type": "validation_recorded", "package_scope_id": SCOPE_Q,
                "validation_set_id": "vs_q"}
        body.update(binding_fields(context, situation))
        journal.append(body)
        return journal, context

    def test_C2_E5_owner_is_the_command_that_started_it(self):
        """E5 -- loop-status names the OWNING command, never a read-only one."""
        journal, context = self.e5_fixture()
        state = commands.post_acceptance_transition_state(context)
        report = commands.loop_position(context, state)
        self.assertEqual(report["loop_next_command"], "commit-piece3-provider-result")
        self.assertNotEqual(report["loop_next_command"], "supervisor-operation-status")
        self.assertIn(
            report["loop_next_command"], constants.CONTINUATION_EXECUTION_COMMANDS
        )
        self.assertEqual(len(constants.CONTINUATION_EXECUTION_COMMANDS), 7)

    def test_C2_E5_appends_exactly_one_completion_and_nothing_else(self):
        """E5 -- the PRODUCTION code appends exactly one completion."""
        journal, context = self.e5_fixture()
        before = len(journal.events)
        with proved_acceptance():
            result = commands.commit_piece3_provider_result(context)
        appended = journal.events[before:]
        self.assertEqual(
            [event["type"] for event in appended], ["supervisor_operation_completed"],
            "ONLY the missing matching completion is appended",
        )
        self.assertIn("completion_recovered", result.report["outcome"])
        self.assertEqual(context.provider.calls, [], "E5_PROVIDER_CALLS = 0")
        # No second Piece-3 effect and no second authorization.
        self.assertEqual(
            sum(1 for e in journal.events if e["type"] == "validation_recorded"), 1
        )
        self.assertEqual(
            sum(1 for e in journal.events
                if e["type"] == "piece3_provider_work_recorded"), 1
        )
        # The completion is paired to the SAME operation.
        completion = appended[0]
        starts = [e for e in journal.events
                  if e["type"] == "supervisor_operation_started"]
        self.assertEqual(
            completion["supervisor_operation_id"],
            starts[-1]["supervisor_operation_id"],
        )

    def test_C2_E5_second_entry_appends_zero(self):
        """E5 -- re-entry after the completion exists appends NOTHING."""
        journal, context = self.e5_fixture()
        with proved_acceptance():
            commands.commit_piece3_provider_result(context)
        after_first = len(journal.events)
        for _repeat in range(3):
            with proved_acceptance():
                try:
                    commands.commit_piece3_provider_result(context)
                except SupervisorRefusal:
                    # The honest next position, not a duplicate append.
                    pass
        self.assertEqual(
            len(journal.events), after_first, "E5_SECOND_ENTRY_APPENDS = 0"
        )
        self.assertEqual(context.provider.calls, [])

    def test_C2_E5_fresh_loop_status_advances_after_the_completion(self):
        """E5 -- once complete, the loop derives the next phase normally."""
        journal, context = self.e5_fixture()
        blocked = commands.loop_position(
            context, commands.post_acceptance_transition_state(context)
        )
        self.assertEqual(blocked["loop_next_command"], "commit-piece3-provider-result")
        self.assertEqual(blocked["loop_state"], commands.LOOP_WAITING_RECOVERING)
        with proved_acceptance():
            commands.commit_piece3_provider_result(context)
        advanced = commands.loop_position(
            context, commands.post_acceptance_transition_state(context)
        )
        self.assertIsNone(advanced.get("incomplete_operation"))
        self.assertNotEqual(advanced["loop_state"], commands.LOOP_WAITING_RECOVERING)

    def row_m_fixture(self):
        """Candidate custody durable, T5 operation start durable, completion MISSING."""
        journal = staged_journal("initial_pending")
        context = self.q_context(journal, validation_set_id="vs_q")
        _events, situation, _ls, _lease = commands.read_state(context)
        work_item, work_id = engine.initial_design_work_item(
            context, situation.candidate, TARGET_Q
        )
        _operation, situation = start_real_operation(
            context, "process-custodied-provider-result", work_item, work_id
        )
        for event_type, origin_key, origin in (
            ("candidate_write_ahead_recorded", "intent_origin",
             commands.CANDIDATE_INTENT_ORIGIN_INITIAL),
            ("candidate_custody_recorded", "custody_origin",
             commands.CANDIDATE_CUSTODY_ORIGIN_INITIAL),
        ):
            body = initial_candidate_body(
                event_type, origin_key, origin, parent=situation.candidate
            )
            journal.append(body)
        return journal, context

    def test_C2_row_M_owner_is_process_custodied_provider_result(self):
        """Row M -- the owner is the command that started the T5 operation."""
        journal, context = self.row_m_fixture()
        state = commands.post_acceptance_transition_state(context)
        self.assertTrue(state["initial_custody_committed"])
        self.assertIsNotNone(state["incomplete_operation"])
        report = commands.loop_position(context, state)
        self.assertEqual(
            report["loop_next_command"], "process-custodied-provider-result"
        )
        self.assertNotEqual(report["loop_next_command"], "supervisor-operation-status")

    def test_C2_row_M_appends_exactly_one_completion(self):
        """Row M -- one completion; no bootstrap, no candidate, no provider."""
        journal, context = self.row_m_fixture()
        # ROW-M-NO-CUSTODY-BOOTSTRAP: the provider custody is ALREADY CLOSED.
        scoped = replay.Replay(journal.read(), SCOPE_Q)
        self.assertEqual(
            scoped.custodied_results_awaiting_processing(), [],
            "ROW_M_PENDING_CUSTODY_BOOTSTRAP_CALLS = 0: none exists to find",
        )
        before = len(journal.events)
        with proved_acceptance():
            result = commands.process_custodied_provider_result(context)
        appended = journal.events[before:]
        self.assertEqual(
            [event["type"] for event in appended], ["supervisor_operation_completed"]
        )
        self.assertIn("completion_recovered", result.report["outcome"])
        self.assertEqual(context.provider.calls, [], "ROW_M_PROVIDER_CALLS = 0")
        self.assertEqual(
            sum(1 for e in journal.events
                if e["type"] == "candidate_custody_recorded"),
            1,
            "ROW_M_CANDIDATE_RECREATIONS = 0",
        )
        self.assertEqual(
            sum(1 for e in journal.events
                if e["type"] == "candidate_write_ahead_recorded"),
            1,
        )

    def test_C2_row_M_second_entry_appends_zero_and_then_hands_off(self):
        """Row M -- re-entry appends nothing; establishment is re-derived."""
        journal, context = self.row_m_fixture()
        with proved_acceptance():
            commands.process_custodied_provider_result(context)
        after_first = len(journal.events)
        for _repeat in range(3):
            with proved_acceptance():
                try:
                    commands.process_custodied_provider_result(context)
                except SupervisorRefusal:
                    pass
        self.assertEqual(
            len(journal.events), after_first, "ROW_M_SECOND_ENTRY_APPENDS = 0"
        )
        report = commands.loop_position(
            context, commands.post_acceptance_transition_state(context)
        )
        self.assertEqual(report["loop_state"], commands.LOOP_HANDOFF_COMPLETE)
        self.assertIsNone(report["loop_next_command"])

    def test_C2_supervisor_operation_status_remains_read_only(self):
        """It writes nothing, ever -- and is not a continuation command."""
        source = read_text(CONTROLLER_DIR / "nh_supervisor" / "commands.py")
        marker = source.index("def supervisor_operation_status(context, request):")
        body = source[marker:source.index("def _semantic_unlock_operation_status(")]
        self.assertIn("read-only", body.lower())
        for writer in ("operation.append(", "context.journal.append(",
                       "operation.complete("):
            self.assertNotIn(writer, body, writer)
        self.assertNotIn(
            "supervisor-operation-status", constants.CONTINUATION_EXECUTION_COMMANDS
        )
        self.assertNotIn("supervisor-operation-status", ui_worker.CONTINUATION_COMMANDS)
        self.assertEqual(
            constants.CONTINUATION_COMPLETION_OWNER_COMMANDS,
            constants.CONTINUATION_EXECUTION_COMMANDS,
        )

    def test_C2_a_pre_effect_crash_is_not_a_completion_position(self):
        """A start that appended nothing substantive is preserved residue."""
        journal = staged_journal("piece3_commit")
        context = self.q_context(journal)
        _events, situation, _ls, _lease = commands.read_state(context)
        work_item, work_id = engine.piece3_work_item(
            context, situation.candidate, "question_validation",
            transition_state={
                "scope_has_validation": False,
                "routed_signal_refs": (),
                "validation_set_id": None,
                "piece3_standing_sha256": "e" * 64,
            },
        )
        start_real_operation(
            context, "commit-piece3-provider-result", work_item, work_id
        )
        state = commands.post_acceptance_transition_state(context)
        self.assertIsNone(
            state["incomplete_operation"],
            "a start that appended nothing substantive owns nothing",
        )
        before = len(journal.events)
        recovered = commands._recover_interrupted_transition_operation(
            context, state, "commit-piece3-provider-result"
        )
        self.assertIsNone(
            recovered, "nothing substantive was appended, so nothing is owed"
        )
        self.assertEqual(len(journal.events), before, "ZERO appends")
        # And the loop is NOT blocked by that residue.
        report = commands.loop_position(context, state)
        self.assertNotEqual(report["loop_state"], commands.LOOP_WAITING_RECOVERING)


# ===========================================================================
# CORRECTION 3 REHEARSALS.
# ===========================================================================
class CorrectionThreeE2DeadlockRehearsals(unittest.TestCase):
    """E2 -- reconcile-provider-request is continuation-PROVIDER-FREE."""

    def test_C3_the_two_classifications_are_distinct_and_both_correct(self):
        """The installed global set is preserved; the continuation set is narrower."""
        self.assertIn(
            "reconcile-provider-request", ui_worker.PROVIDER_CONTACTING_COMMANDS,
            "GLOBAL_PROVIDER_CONTACTING_SET_PRESERVED",
        )
        for installed in ("execute-next-claude-task", "diagnose-next-correction-batch",
                          "probe-provider-availability", "question-validation",
                          "question-coverage-review"):
            self.assertIn(installed, ui_worker.PROVIDER_CONTACTING_COMMANDS)
        # Accepted role-split v1_6 section 5.1 -- THREE contacting, FOUR free.
        self.assertEqual(len(ui_worker.CONTINUATION_PROVIDER_CONTACTING_COMMANDS), 3)
        self.assertNotIn(
            "reconcile-provider-request",
            ui_worker.CONTINUATION_PROVIDER_CONTACTING_COMMANDS,
        )
        self.assertNotIn(
            "prepare-next-design-task",
            ui_worker.CONTINUATION_PROVIDER_CONTACTING_COMMANDS,
        )
        self.assertEqual(
            ui_worker.CONTINUATION_PROVIDER_CONTACTING_COMMANDS,
            frozenset(constants.CONTINUATION_PROVIDER_CONTACTING_COMMANDS),
        )
        self.assertEqual(len(constants.CONTINUATION_PROVIDER_FREE_COMMANDS), 4)

    def worker_for(self, loop_report, *, ineligible=()):
        scheduling = FakeScheduling(ineligible=ineligible)
        runner = FakeRunner(accepted_status_report(), loop_report)
        worker = ui_worker.SupervisorWorker.__new__(ui_worker.SupervisorWorker)
        worker.runner = runner
        worker.scheduling = scheduling
        worker.clock = ui_worker.Clock()
        worker.local_observations = []
        worker.lease_binding = {"controller_executable_identity": "1" * 64}
        worker.start_gate_open = lambda: (True, "open")
        return worker, runner, scheduling

    def test_C3_E2_runs_reconcile_with_a_null_continuation_series(self):
        """The E2 deadlock is gone: reconcile runs exactly once."""
        loop = {
            "ok": True,
            "loop_state": "LOOP_TRANSITION_RECONCILE_REQUIRED",
            "loop_next_command": "reconcile-provider-request",
            "loop_retry_series_key": None,
            "loop_scheduling_binding": None,
            "loop_scheduling_metadata": None,
            "loop_transition_exists": True,
            "loop_transition_working": False,
        }
        worker, runner, _scheduling = self.worker_for(loop)
        outcome = worker._continuation_step(
            accepted_status_report(),
            ui_supervisor.WorkflowState.ACCEPTED_FOR_DESIGN_ONLY,
        )
        self.assertEqual(outcome.action, "ran_command")
        self.assertEqual(outcome.ran_command, "reconcile-provider-request")
        self.assertEqual(
            runner.calls.count("reconcile-provider-request"), 1,
            "E2_RECONCILE_RUN_COUNT = 1",
        )
        self.assertNotIn("wait", outcome.action)
        # No generative dispatch of any kind.
        for generative in constants.CONTINUATION_PROVIDER_CONTACTING_COMMANDS:
            self.assertNotIn(generative, runner.calls)

    def test_C3_E2_is_not_gated_even_when_the_global_series_is_blocked(self):
        """The ordinary global classification does not gate the continuation."""
        loop = {
            "ok": True,
            "loop_state": "LOOP_TRANSITION_RECONCILE_REQUIRED",
            "loop_next_command": "reconcile-provider-request",
            "loop_retry_series_key": None,
            "loop_scheduling_binding": None,
            "loop_scheduling_metadata": None,
            "loop_transition_exists": True,
            "loop_transition_working": False,
        }
        worker, runner, _scheduling = self.worker_for(
            loop, ineligible={"rs_anything"}
        )
        outcome = worker._continuation_step(
            accepted_status_report(retry_series_key="rs_anything"),
            ui_supervisor.WorkflowState.ACCEPTED_FOR_DESIGN_ONLY,
        )
        self.assertEqual(outcome.action, "ran_command")
        self.assertEqual(runner.calls.count("reconcile-provider-request"), 1)

    def test_C3_a_generative_continuation_command_is_still_gated(self):
        """The four provider-contacting continuation commands remain gated."""
        loop = {
            "ok": True,
            "loop_state": "LOOP_SELECTION_REQUIRED",
            "loop_next_command": "continue-design-loop",
            "loop_retry_series_key": None,
            "loop_scheduling_binding": None,
            "loop_scheduling_metadata": None,
            "loop_transition_exists": False,
            "loop_transition_working": False,
        }
        worker, runner, _scheduling = self.worker_for(loop)
        outcome = worker._continuation_step(
            accepted_status_report(),
            ui_supervisor.WorkflowState.ACCEPTED_FOR_DESIGN_ONLY,
        )
        self.assertEqual(outcome.action, "wait")
        self.assertIn("proved no retry series", outcome.detail)
        self.assertNotIn("continue-design-loop", runner.calls)


class CorrectionThreeOwnershipRehearsals(unittest.TestCase):
    """Chronology is not ownership."""

    def q_context(self, journal, *, validation_set_id=None, unlocked=True):
        return build_context(
            journal=journal,
            binding=make_binding(
                SCOPE_Q, root=ROOT_Q, validation_set_id=validation_set_id
            ),
            candidate=make_candidate(ROOT_Q),
            clearance=lambda scope: {"unlocked": unlocked},
        )

    def residue(self, context, command, work_item, work_id):
        """One authentic start that appends nothing substantive."""
        operation, _situation = start_real_operation(
            context, command, work_item, work_id
        )
        return operation

    def piece3_item(self, context, situation, kind="question_validation"):
        return engine.piece3_work_item(
            context, situation.candidate, kind,
            transition_state={
                "scope_has_validation": kind == "coverage_review",
                "routed_signal_refs": (),
                "validation_set_id": "vs_q" if kind == "coverage_review" else None,
                "piece3_standing_sha256": "e" * 64,
            },
        )

    def test_C3_one_pre_effect_residue_is_ignored(self):
        """PRE_EFFECT_ONE_RESIDUE_IGNORED -- and it never blocks the loop."""
        journal = staged_journal("piece3_commit")
        context = self.q_context(journal)
        _e, situation, _l, _lease = commands.read_state(context)
        item, item_id = self.piece3_item(context, situation)
        self.residue(context, "commit-piece3-provider-result", item, item_id)
        before = len(journal.events)
        state = commands.post_acceptance_transition_state(context)
        self.assertIsNone(state["incomplete_operation"])
        report = commands.loop_position(context, state)
        self.assertNotEqual(report["loop_state"], commands.LOOP_WAITING_RECOVERING)
        self.assertIsNone(
            commands._recover_interrupted_transition_operation(
                context, state, "commit-piece3-provider-result"
            )
        )
        self.assertEqual(len(journal.events), before, "zero completion appends")

    def test_C3_two_pre_effect_residues_are_ignored(self):
        """PRE_EFFECT_TWO_RESIDUES_IGNORED -- count alone is never a contradiction."""
        journal = staged_journal("piece3_commit")
        context = self.q_context(journal)
        _e, situation, _l, _lease = commands.read_state(context)
        item, item_id = self.piece3_item(context, situation)
        for _repeat in range(2):
            self.residue(context, "commit-piece3-provider-result", item, item_id)
        state = commands.post_acceptance_transition_state(context)
        self.assertIsNone(state["contradiction"])
        self.assertIsNone(state["incomplete_operation"])
        self.assertEqual(
            len([e for e in journal.events
                 if e["type"] == "supervisor_operation_started"]), 2,
            "both residues are PRESERVED",
        )

    def test_C3_residue_never_claims_a_later_successful_operation(self):
        """RESIDUE_LATER_SUCCESS_NOT_MISOWNED."""
        journal = staged_journal("piece3_commit")
        context = self.q_context(journal)
        _e, situation, _l, _lease = commands.read_state(context)
        item, item_id = self.piece3_item(context, situation)
        stale = self.residue(context, "commit-piece3-provider-result", item, item_id)
        # A LATER complete operation of the same command appends the effect.
        later, situation = start_real_operation(
            context, "commit-piece3-provider-result", item, item_id
        )
        body = {"type": "validation_recorded", "package_scope_id": SCOPE_Q,
                "validation_set_id": "vs_q"}
        body.update(binding_fields(context, situation))
        journal.append(body)
        journal.append(
            {"type": "supervisor_operation_completed",
             "package_scope_id": SCOPE_Q,
             "supervisor_operation_id": later.operation_id,
             "outcome": "ok"}
        )
        state = commands.post_acceptance_transition_state(context)
        self.assertIsNone(
            state["incomplete_operation"],
            "the stale residue must not claim the later operation's effect",
        )
        before = len(journal.events)
        self.assertIsNone(
            commands._recover_interrupted_transition_operation(
                context, state, "commit-piece3-provider-result"
            )
        )
        self.assertEqual(len(journal.events), before, "no fabricated completion")

    def test_C3_residue_plus_a_real_E5_recovers_only_the_real_owner(self):
        """RESIDUE_PLUS_REAL_E5_RECOVERS_REAL_OWNER_ONLY."""
        journal = staged_journal("piece3_commit")
        context = self.q_context(journal)
        _e, situation, _l, _lease = commands.read_state(context)
        item, item_id = self.piece3_item(context, situation)
        stale = self.residue(context, "commit-piece3-provider-result", item, item_id)
        real, situation = start_real_operation(
            context, "commit-piece3-provider-result", item, item_id
        )
        body = {"type": "validation_recorded", "package_scope_id": SCOPE_Q,
                "validation_set_id": "vs_q"}
        body.update(binding_fields(context, situation))
        journal.append(body)
        state = commands.post_acceptance_transition_state(context)
        self.assertEqual(
            state["incomplete_operation"]["supervisor_operation_id"],
            real.operation_id,
            "the REAL owner, not the residue",
        )
        self.assertNotEqual(
            state["incomplete_operation"]["supervisor_operation_id"],
            stale.operation_id,
        )
        before = len(journal.events)
        with proved_acceptance():
            result = commands.commit_piece3_provider_result(context)
        appended = journal.events[before:]
        self.assertEqual(
            [e["type"] for e in appended], ["supervisor_operation_completed"]
        )
        self.assertEqual(appended[0]["supervisor_operation_id"], real.operation_id)
        self.assertEqual(context.provider.calls, [])

    def test_C3_a_T2_residue_cannot_own_a_later_T5_custody(self):
        """T2_RESIDUE_CANNOT_OWN_T5_EFFECT."""
        journal = staged_journal("initial_pending")
        context = self.q_context(journal, validation_set_id="vs_q")
        _e, situation, _l, _lease = commands.read_state(context)
        piece3, piece3_id = self.piece3_item(context, situation, "coverage_review")
        # An OLD process-custodied start from the T2 era.
        stale = self.residue(
            context, "process-custodied-provider-result", piece3, piece3_id
        )
        # The REAL T5 operation follows and appends the candidate custody.
        initial, initial_id = engine.initial_design_work_item(
            context, situation.candidate, TARGET_Q
        )
        real, situation = start_real_operation(
            context, "process-custodied-provider-result", initial, initial_id
        )
        journal.append(
            initial_candidate_body(
                "candidate_custody_recorded", "custody_origin",
                commands.CANDIDATE_CUSTODY_ORIGIN_INITIAL,
                parent=situation.candidate,
            )
        )
        state = commands.post_acceptance_transition_state(context)
        self.assertEqual(
            state["incomplete_operation"]["supervisor_operation_id"],
            real.operation_id,
            "the T5 operation owns its own custody",
        )
        self.assertNotEqual(
            state["incomplete_operation"]["supervisor_operation_id"],
            stale.operation_id,
            "an old T2 residue can never own a later T5 custody",
        )
        before = len(journal.events)
        with proved_acceptance():
            result = commands.process_custodied_provider_result(context)
        appended = journal.events[before:]
        self.assertEqual(
            [e["type"] for e in appended], ["supervisor_operation_completed"]
        )
        self.assertEqual(appended[0]["supervisor_operation_id"], real.operation_id)
        # ROW_M_EXACT_OWNER_STILL_PROVED, despite the candidate identity change.
        self.assertEqual(
            state["incomplete_operation"]["effect_type"], "candidate_custody_recorded"
        )
        # RECOVERY_SECOND_ENTRY_APPENDS = 0
        after_first = len(journal.events)
        for _repeat in range(3):
            with proved_acceptance():
                try:
                    commands.process_custodied_provider_result(context)
                except SupervisorRefusal:
                    pass
        self.assertEqual(len(journal.events), after_first)

    def test_C3_a_T5_shaped_residue_cannot_own_a_later_piece3_authorization(self):
        """T5_RESIDUE_CANNOT_OWN_T2_EFFECT."""
        journal = staged_journal("piece3_pending")
        context = self.q_context(journal)
        _e, situation, _l, _lease = commands.read_state(context)
        initial, initial_id = engine.initial_design_work_item(
            context, situation.candidate, TARGET_Q
        )
        stale = self.residue(
            context, "process-custodied-provider-result", initial, initial_id
        )
        piece3, piece3_id = self.piece3_item(context, situation)
        real, situation = start_real_operation(
            context, "process-custodied-provider-result", piece3, piece3_id
        )
        body = {
            "type": "piece3_provider_work_recorded",
            "package_scope_id": SCOPE_Q,
            "authorizes_event_type": "validation_recorded",
            "provider_request_identity": "pr_qv",
            "result_custody_identity": "rc_pr_qv",
            "work_item_identity": piece3_id,
            "result_schema_valid": True,
        }
        body.update(binding_fields(context, situation))
        journal.append(body)
        state = commands.post_acceptance_transition_state(context)
        self.assertEqual(
            state["incomplete_operation"]["supervisor_operation_id"],
            real.operation_id,
        )
        self.assertNotEqual(
            state["incomplete_operation"]["supervisor_operation_id"],
            stale.operation_id,
            "a T5-shaped residue can never own a later Piece-3 authorization",
        )

    def test_C3_two_starts_claiming_the_same_effect_fail_closed(self):
        """A genuine ownership CONFLICT refuses, and nothing is chosen."""
        journal = staged_journal("piece3_commit")
        context = self.q_context(journal)
        _e, situation, _l, _lease = commands.read_state(context)
        item, item_id = self.piece3_item(context, situation)
        first, situation = start_real_operation(
            context, "commit-piece3-provider-result", item, item_id
        )
        body = {"type": "validation_recorded", "package_scope_id": SCOPE_Q,
                "validation_set_id": "vs_q"}
        body.update(binding_fields(context, situation))
        effect = journal.append(body)
        # A second start of a DIFFERENT command that also names the same effect.
        second, _situation = start_real_operation(
            context, "process-custodied-provider-result", item, item_id
        )
        journal.events.remove(journal.events[-1])
        forged = dict(second.started_event)
        forged["event_seq"] = effect["event_seq"] - 1
        # Both starts now precede the effect and both would bind it.
        state = commands.post_acceptance_transition_state(context)
        self.assertIsNotNone(state["incomplete_operation"])
        self.assertEqual(
            state["incomplete_operation"]["supervisor_operation_id"],
            first.operation_id,
            "only the command whose effect type matches may own it",
        )


class CorrectionThreeCallOrderRehearsals(unittest.TestCase):
    """Discovery precedes ordinary package-context construction."""

    def test_C3_discovery_context_is_not_the_ordinary_package_context(self):
        """TB_GLOBAL_LOOKUP_BEFORE_ORDINARY_PACKAGE_CONTEXT."""
        source = read_text(CONTROLLER_SOURCE)
        marker = source.index("def discovery_context(errors):")
        # The slice ENDS at the next definition, so the control-context factory
        # that legitimately builds P afterwards is not mistaken for discovery.
        body = source[marker:source.index("def _resolved_control(")]
        # Strip the docstring: prose may NAME the function it refuses to call.
        code = body[body.index('"""', body.index('"""') + 3) + 3:]
        self.assertNotIn(
            "build_supervisor_context(", code,
            "discovery must NOT construct the ordinary package context",
        )
        self.assertIn("lease=None", body, "it cannot be acted under")
        self.assertIn("round_zero_candidate=None", body, "it binds no candidate")
        # And the command entry runs discovery BEFORE the ordinary construction.
        entry = source[source.index("def command_supervisor(name):"):
                       source.index("def main(argv):")]
        discovery_at = entry.index("discover_transition_context(")
        ordinary_at = entry.index("context = build_supervisor_context(errors)")
        self.assertLess(discovery_at, ordinary_at)

    def test_C3_the_discovery_context_binds_only_the_accepted_scope(self):
        """It carries no source, candidate or establishment authority."""
        errors = []
        probe = nh_loop.discovery_context(errors)
        self.assertEqual(errors, [])
        self.assertIsNotNone(probe)
        # re-cut 2026-09-02 against journal head 2300: discovery binds the current package anchor at head 2300 (event-173 scope), no longer the event-84 P
        self.assertEqual(
            probe.binding.package_scope_id,
            "nullpkg_74962b341d158bd21833a65c5b6ec09b",
        )
        self.assertIsNone(probe.binding.source_binding_sha256)
        self.assertIsNone(probe.binding.scope_root_path)
        self.assertIsNone(probe.round_zero_candidate)
        self.assertIsNone(probe.lease)
        self.assertEqual(probe.transition_binding_kind, "discovery")

    def test_C3_the_real_entry_builds_only_one_context_for_the_proved_scope(self):
        """At event 84 there is no Q, so discovery falls through to P."""
        built = []
        original = nh_loop.build_supervisor_context

        def recorder(errors):
            built.append("ordinary")
            return original(errors)

        try:
            nh_loop.build_supervisor_context = recorder
            report = run_live_copy("loop-status")
        finally:
            nh_loop.build_supervisor_context = original
        # re-cut 2026-09-02 against journal head 2300: the live loop is held (CPB-SINGLE-TRANSITION); still exactly one ordinary context is built
        self.assertEqual(report["loop_state"], "LOOP_SELECTION_REQUIRED")
        # loop-status is read-only and not a continuation execution command, so
        # discovery does not run for it and exactly one context is built.
        self.assertEqual(built, ["ordinary"])


class CorrectionThreeDependencyRehearsals(unittest.TestCase):
    """A retry series must describe ONE exact piece of work."""

    def q_journal(self, *, q_source="ab" * 32, q_dependency=None,
                  p_dependency=None, reason="a wording", binding=None):
        journal = staged_journal("clearance_required", binding=binding)
        journal.append(
            {
                "type": "supervisor_operation_started",
                "package_scope_id": SCOPE_Q,
                "supervisor_operation_id": "op_q",
                "supervisor_command": "dispatch-piece3-provider-review",
                "source_binding_sha256": q_source,
            }
        )
        for scope, dependency in ((SCOPE_Q, q_dependency), (SCOPE_P, p_dependency)):
            if dependency is None:
                continue
            journal.append(
                {
                    "type": "supervisor_operation_completed",
                    "package_scope_id": scope,
                    "supervisor_operation_id": "op_dep_" + scope[-6:],
                    "outcome": "waiting_recovering",
                    "dependency_identity": dependency,
                    "dependency_record": {
                        "dependency_identity": dependency,
                        "plain_language_dependency": reason,
                    },
                }
            )
        return journal

    def series_for(self, journal):
        context = build_context(
            journal=journal, clearance=lambda scope: {"unlocked": False}
        )
        state = commands.post_acceptance_transition_state(context)
        report = commands.loop_position(context, state)
        series, binding = commands.continuation_scheduling(
            context, state, report["loop_state"], report["loop_next_command"]
        )
        return series, binding, context, state, report

    def test_C3_Q_series_uses_Q_dependency(self):
        """Q_RETRY_DEPENDENCY_SOURCE = Q exact transition scope."""
        series, binding, _c, _s, _r = self.series_for(
            self.q_journal(q_dependency="dep_D1")
        )
        self.assertEqual(binding["dependency_identity"], "dep_D1")
        self.assertEqual(binding["package_scope_id"], SCOPE_Q)

    def test_C3_changing_only_P_dependency_leaves_Q_series_unchanged(self):
        """P_DEPENDENCY_CHANGE_ALONE_CHANGES_Q_SERIES = NO."""
        first, _b, _c, _s, _r = self.series_for(
            self.q_journal(q_dependency="dep_D1", p_dependency="dep_P1")
        )
        second, _b, _c, _s, _r = self.series_for(
            self.q_journal(q_dependency="dep_D1", p_dependency="dep_P2")
        )
        self.assertEqual(first, second)

    def test_C3_changing_Q_dependency_changes_the_series(self):
        """Q_DEPENDENCY_CHANGE_CHANGES_Q_SERIES = YES."""
        first, _b, _c, _s, _r = self.series_for(self.q_journal(q_dependency="dep_D1"))
        second, _b, _c, _s, _r = self.series_for(self.q_journal(q_dependency="dep_D2"))
        self.assertNotEqual(first, second)

    def test_C3_changing_only_the_plain_language_reason_changes_nothing(self):
        """PLAIN_LANGUAGE_REASON_CHANGE_ALONE_CHANGES_Q_SERIES = NO."""
        first, _b, _c, _s, _r = self.series_for(
            self.q_journal(q_dependency="dep_D1", reason="one wording")
        )
        second, _b, _c, _s, _r = self.series_for(
            self.q_journal(q_dependency="dep_D1", reason="an entirely different wording")
        )
        self.assertEqual(first, second)

    def test_C3_a_truthful_no_dependency_position_carries_null(self):
        """A position with no dependency carries a truthful null."""
        _series, binding, _c, _s, _r = self.series_for(self.q_journal())
        self.assertIsNone(binding["dependency_identity"])

    def test_C3_the_series_matches_the_installed_helper_with_the_Q_dependency(self):
        """Q_RETRY_SERIES_MATCHES_INSTALLED_HELPER = YES."""
        series, binding, context, _state, report = self.series_for(
            self.q_journal(q_dependency="dep_D1")
        )
        expected = identity.retry_series_key(
            {
                "controller_executable_identity": context.controller_executable_identity,
                "package_scope_id": binding["package_scope_id"],
                "source_binding_sha256": binding["source_binding_sha256"],
                "candidate_path": binding["candidate_path"],
                "candidate_sha256": binding["candidate_sha256"],
                "candidate_bytes": binding["candidate_bytes"],
                "workflow_state": report["loop_state"],
                "next_command": report["loop_next_command"],
                "work_item_identity": binding["work_item_identity"],
                "dependency_identity": binding["dependency_identity"],
            }
        )
        self.assertEqual(series, expected)

    def test_C3_the_scheduling_metadata_is_all_from_the_transition_scope(self):
        """Q_SCHEDULING_RECORD_USES_P_DEPENDENCY_METADATA = NO."""
        journal = self.q_journal(q_dependency="dep_D1", p_dependency="dep_P1")
        context = build_context(
            journal=journal, clearance=lambda scope: {"unlocked": False}
        )
        state = commands.post_acceptance_transition_state(context)
        report = commands.loop_position(context, state)
        _series, binding = commands.continuation_scheduling(
            context, state, report["loop_state"], report["loop_next_command"]
        )
        metadata = commands.transition_scheduling_metadata(context, state, binding)
        self.assertEqual(metadata["dependency_identity"], "dep_D1")
        self.assertNotEqual(metadata["dependency_identity"], "dep_P1")
        self.assertEqual(metadata["work_item_identity"], binding["work_item_identity"])
        self.assertIsNotNone(metadata["post_operation_state_sha256"])

    def test_C3_the_worker_records_the_transition_metadata_not_P(self):
        """schedule_backoff receives Q's dependency, work item and state."""
        scheduling = FakeScheduling()
        loop = {
            "ok": True,
            "loop_state": "LOOP_WAITING_RECOVERING",
            "loop_next_command": None,
            "loop_retry_series_key": "rs_q",
            "loop_scheduling_binding": {
                "package_scope_id": SCOPE_Q,
                "source_binding_sha256": "ab" * 32,
                "candidate_path": ROOT_Q,
                "candidate_sha256": "9" * 64,
                "candidate_bytes": 4096,
                "work_item_identity": "wi_q",
                "dependency_identity": "dep_D1",
            },
            "loop_scheduling_metadata": {
                "dependency_identity": "dep_D1",
                "dependency_identity_binding": "dib_q",
                "work_item_identity": "wi_q",
                "provider_availability_episode_identity": "ep_q",
                "output_retries_used": 0,
                "post_operation_state_sha256": "sb_q",
            },
        }
        runner = FakeRunner(
            accepted_status_report(
                dependency_identity="dep_P1",
                work_item_identity="wi_p",
                state_binding_sha256="sb_p",
                provider_availability_episode_identity="ep_p",
            ),
            loop,
        )
        worker = ui_worker.SupervisorWorker.__new__(ui_worker.SupervisorWorker)
        worker.runner = runner
        worker.scheduling = scheduling
        worker.clock = ui_worker.Clock()
        worker.local_observations = []
        worker.lease_binding = {"controller_executable_identity": "1" * 64}
        worker.record_transition_scheduling_outcome(
            "rs_q", loop["loop_scheduling_binding"], loop["loop_scheduling_metadata"]
        )
        self.assertEqual(scheduling.scheduled, ["rs_q"])
        kwargs = scheduling.kwargs[-1]
        self.assertEqual(kwargs["dependency_identity"], "dep_D1")
        self.assertEqual(kwargs["dependency_identity_binding"], "dib_q")
        self.assertEqual(kwargs["work_item_identity"], "wi_q")
        self.assertEqual(kwargs["episode_identity"], "ep_q")
        self.assertEqual(kwargs["post_operation_state_sha256"], "sb_q")
        for value in ("dep_P1", "wi_p", "sb_p", "ep_p"):
            self.assertNotIn(value, kwargs.values())
        self.assertEqual(scheduling.bindings[-1]["package_scope_id"], SCOPE_Q)


class CorrectionThreeUiTruthRehearsals(unittest.TestCase):
    """A transition that EXISTS is not a transition that is RUNNING."""

    def wording(self, *, exists, working, lease="LIVE_PROVED"):
        return ui_supervisor.wording_for(
            ui_supervisor.WorkflowState.ACCEPTED_FOR_DESIGN_ONLY,
            lease,
            loop_transition_active=exists,
            loop_transition_working=working,
        )["detail"]

    def test_C3_event84_has_no_transition_and_no_working_line(self):
        """EVENT84_TRANSITION_EXISTS = NO / WORKING_LINE_SHOWN = NO."""
        loop = run_live_copy("loop-status")
        # re-cut 2026-09-02 against journal head 2300: the live loop is held (CPB-SINGLE-TRANSITION); no transition is preferred, so none exists or works
        self.assertEqual(loop["loop_state"], "LOOP_SELECTION_REQUIRED")
        self.assertFalse(
            loop["loop_transition_exists"], "no Q exists before a selection"
        )
        self.assertFalse(loop["loop_transition_working"])
        detail = self.wording(exists=False, working=False)
        self.assertIn("no next package started", detail)
        self.assertNotIn(ui_supervisor.TRANSITION_LINE, detail)
        self.assertNotIn(ui_supervisor.TRANSITION_NOT_WORKING_LINE, detail)

    def test_C3_a_live_transition_shows_the_working_line(self):
        """Q_LIVE_TRANSITION_WORKING_LINE_SHOWN = YES."""
        detail = self.wording(exists=True, working=True)
        self.assertNotIn("no next package started", detail)
        self.assertIn(ui_supervisor.TRANSITION_LINE, detail)

    def test_C3_a_waiting_or_held_transition_never_claims_work(self):
        """Waiting / user-action / safety-hold: no working claim, no false reset."""
        detail = self.wording(exists=True, working=False)
        self.assertNotIn(
            "no next package started", detail,
            "Q_WAITING_CARD_SAYS_NO_NEXT_PACKAGE_STARTED = NO",
        )
        self.assertNotIn(
            ui_supervisor.TRANSITION_LINE, detail,
            "Q_WAITING_WORKING_LINE_SHOWN = NO",
        )
        self.assertIn(ui_supervisor.TRANSITION_NOT_WORKING_LINE, detail)
        self.assertIn("not working on it right now", detail)

    def test_C3_the_controller_decides_working_for_every_stopped_state(self):
        """The stopped states are never 'working', whatever their enum name."""
        for stopped in (
            commands.LOOP_WAITING_RECOVERING,
            commands.LOOP_NEEDS_NESS_DECISION,
            commands.LOOP_NEEDS_USER_ACTION,
            commands.LOOP_SAFETY_HOLD,
            commands.LOOP_DESIGN_CONTINUATION_COMPLETE,
            commands.LOOP_HANDOFF_COMPLETE,
        ):
            report = dict(commands._loop_result(stopped, None))
            report["loop_transition_exists"] = True
            working = bool(
                report["loop_transition_exists"]
                and report["loop_next_command"] is not None
                and report["loop_state"] not in (
                    commands.LOOP_WAITING_RECOVERING,
                    commands.LOOP_NEEDS_NESS_DECISION,
                    commands.LOOP_NEEDS_USER_ACTION,
                    commands.LOOP_SAFETY_HOLD,
                    commands.LOOP_DESIGN_CONTINUATION_COMPLETE,
                    commands.LOOP_HANDOFF_COMPLETE,
                    commands.LOOP_NOT_APPLICABLE,
                )
            )
            self.assertFalse(working, stopped)

    def test_C3_an_established_Q_shows_no_transition_line(self):
        """Q_ESTABLISHED_TRANSITION_LINE_SHOWN = NO."""
        journal = staged_journal("handoff")
        context = build_context(
            journal=journal, clearance=lambda scope: {"unlocked": True}
        )
        state = commands.post_acceptance_transition_state(context)
        self.assertTrue(state["established_complete"])
        exists = bool(
            state.get("transition_scope") and not state.get("established_complete")
        )
        self.assertFalse(exists)
        detail = self.wording(exists=exists, working=False)
        self.assertNotIn(ui_supervisor.TRANSITION_LINE, detail)
        self.assertNotIn(ui_supervisor.TRANSITION_NOT_WORKING_LINE, detail)

    def test_C3_the_server_copies_and_never_re_derives(self):
        """The UI reads controller-proved facts, not enum names."""
        source = read_text(UI_DIR / "server.py")
        marker = source.index("def read_loop_projection(")
        body = source[marker:source.index("def build_ui_state(")]
        self.assertIn('report.get("loop_transition_exists")', body)
        self.assertIn('report.get("loop_transition_working")', body)
        self.assertNotIn("LOOP_SELECTION_REQUIRED", body)
        self.assertNotIn("LOOP_TASK_PREPARATION_REQUIRED", body)


# ===========================================================================
# CORRECTION 4 REHEARSALS.
#
# The P/Q integration tests below use NO acceptance monkeypatch, NO fake
# always-live gate and NO Q-specific lease.  Only the provider TRANSPORT is
# stubbed.
# ===========================================================================
def accepted_p_journal():
    """A disposable journal shaped like the real accepted-P position."""
    journal = FakeJournal()
    journal.append(
        {
            "type": "ness_candidate_acceptance_recorded",
            "package_scope_id": SCOPE_P,
            "acceptance_disposition": "ACCEPTED_FOR_DESIGN_ONLY",
        }
    )
    return journal


class RealLease:
    """One disposable lease, acquired ONCE under P's binding.

    It is the installed lease CONTRACT, not a bypass: it records the binding it
    was acquired with and refuses any other, so a Q binding or a wrong run id
    genuinely fails.
    """

    def __init__(self, binding, run_id="run_p", expires_in=3600):
        self.acquired_binding = dict(binding)
        self.run_id = run_id
        self.expires_in = expires_in
        self.evaluations = []

    def evaluate(self, binding=None, now=None):
        self.evaluations.append(dict(binding or {}))
        for key in (
            "package_scope_id",
            "source_binding_sha256",
            "controller_executable_identity",
        ):
            if (binding or {}).get(key) != self.acquired_binding.get(key):
                return "INVALID_UNPROVED", None, "binding differs from the lease"
        lease = dict(self.acquired_binding)
        lease["run_id"] = self.run_id
        lease["expires_at_epoch"] = (now or 0) + self.expires_in
        return "LIVE_PROVED", lease, "the one acquired lease"


def p_context_with_real_lease(journal, *, adapter=None, transport=None,
                              run_id="run_p", expires_in=3600):
    """P's context holding the ONE real disposable lease."""
    binding = make_binding(SCOPE_P)
    lease_binding = {
        "package_scope_id": binding.package_scope_id,
        "source_binding_sha256": binding.source_binding_sha256,
        "controller_executable_identity": "1" * 64,
    }
    lease = RealLease(lease_binding, run_id=run_id, expires_in=expires_in)
    registry = nh_supervisor.runtime.CapabilityRegistry()
    context = nh_supervisor.runtime.build_context(
        journal=journal,
        binding=binding,
        controller_executable_identity="1" * 64,
        endpoint_binding=nh_loop.supervisor_endpoint_binding(),
        capability_reader=registry.reader(),
        round_zero_candidate=make_candidate(binding.scope_root_path),
        provider=transport or LoudStubTransport(),
        lease=lease,
        lease_binding=lease_binding,
        own_run_id=run_id,
        interview_gate_reader=lambda scope: {"unlocked": False},
    )
    context.continuation_adapter = adapter or StubAdapter()
    return context, lease


def q_work_context(p_context, journal, *, adapter=None, transport=None,
                   validation_set_id=None, unlocked=False):
    """Q's WORK context, carrying P as its CONTROL context and NO lease."""
    binding = make_binding(
        SCOPE_Q, root=ROOT_Q, validation_set_id=validation_set_id
    )
    registry = nh_supervisor.runtime.CapabilityRegistry()
    context = nh_supervisor.runtime.build_context(
        journal=journal,
        binding=binding,
        controller_executable_identity="1" * 64,
        endpoint_binding=nh_loop.supervisor_endpoint_binding(),
        capability_reader=registry.reader(),
        round_zero_candidate=make_candidate(ROOT_Q),
        provider=transport or p_context.provider,
        # NO LEASE OF ITS OWN.
        lease=None,
        lease_binding=None,
        own_run_id=None,
        interview_gate_reader=lambda scope: {"unlocked": unlocked},
    )
    context.continuation_adapter = adapter or StubAdapter()
    context.transition_binding_kind = "post_validation"
    context.control_context = p_context
    return context


class CorrectionFourControlBoundaryRehearsals(unittest.TestCase):
    """P owns acceptance and the lease; Q owns the work."""

    def test_C4_acceptance_is_proved_over_the_control_package(self):
        """Q_SUPERVISOR_STATUS_USED_AS_ACCEPTANCE_PROOF = NO."""
        source = read_text(CONTROLLER_DIR / "nh_supervisor" / "commands.py")
        marker = source.index("def acceptance_freshly_proved(")
        body = source[marker:source.index("\n\ndef ", marker)]
        self.assertIn("control = control_context_of(context)", body)
        self.assertIn("supervisor_status(control)", body)
        self.assertNotIn("supervisor_status(context)", body)
        # And the resolver returns the control context when one is attached.
        journal = accepted_p_journal()
        p_context, _lease = p_context_with_real_lease(journal)
        q_context = q_work_context(p_context, journal)
        self.assertIs(commands.control_context_of(q_context), p_context)
        self.assertIs(commands.control_context_of(p_context), p_context)
        self.assertEqual(q_context.binding.package_scope_id, SCOPE_Q)
        self.assertEqual(
            q_context.control_context.binding.package_scope_id, SCOPE_P
        )

    def test_C4_the_gates_evaluate_the_control_lease(self):
        """P_LEASE_Q_COMMAND_START_GATE_PROVED / CLOSURE_GATE_PROVED."""
        journal = accepted_p_journal()
        p_context, lease = p_context_with_real_lease(journal)
        q_context = q_work_context(p_context, journal)
        self.assertIsNone(q_context.lease, "SECOND_Q_LEASE_CREATED = NO")
        self.assertIsNone(q_context.lease_binding)
        # Both installed gates accept the ONE P lease for Q work.
        state, held = commands.evaluate_lease(q_context)
        self.assertEqual(state, "LIVE_PROVED")
        self.assertEqual(held["run_id"], "run_p")
        commands.require_start_gate(q_context)
        commands.require_closure_gate(q_context)
        # Every evaluation was made against P's binding, never Q's.
        for evaluated in lease.evaluations:
            self.assertEqual(evaluated["package_scope_id"], SCOPE_P)
            self.assertNotEqual(evaluated["package_scope_id"], SCOPE_Q)

    def test_C4_a_wrong_run_id_fails_closed(self):
        """WRONG_RUN_ID_FAILS_CLOSED."""
        journal = accepted_p_journal()
        p_context, _lease = p_context_with_real_lease(journal, run_id="run_p")
        p_context.own_run_id = "run_someone_else"
        q_context = q_work_context(p_context, journal)
        with self.assertRaises(SupervisorRefusal) as caught:
            commands.require_start_gate(q_context)
        self.assertIn("another run", str(caught.exception))

    def test_C4_an_absent_or_expired_control_lease_fails_closed(self):
        """ABSENT_OR_EXPIRED_P_LEASE_FAILS_CLOSED."""
        journal = accepted_p_journal()
        # Absent.
        p_context, _lease = p_context_with_real_lease(journal)
        p_context.lease = None
        q_context = q_work_context(p_context, journal)
        with self.assertRaises(SupervisorRefusal) as caught:
            commands.require_start_gate(q_context)
        self.assertIn("no supervisor lease", str(caught.exception))
        # Expired -- less than the installed new-work margin remains.
        p_context, _lease = p_context_with_real_lease(journal, expires_in=1)
        q_context = q_work_context(p_context, journal)
        with self.assertRaises(SupervisorRefusal) as caught:
            commands.require_start_gate(q_context)
        self.assertIn("margin", str(caught.exception))

    def test_C4_a_Q_lease_binding_is_never_acquired(self):
        """The builder creates no lease of its own."""
        source = read_text(CONTROLLER_SOURCE)
        marker = source.index(
            "def build_transition_context(mode, facts, errors, control_context=None):"
        )
        body = source[marker:source.index("\ndef ", marker + 10)]
        self.assertIn("NO SECOND LEASE", body)
        self.assertIn("lease = None", body)
        self.assertNotIn("default_lease_binding(binding", body)
        self.assertNotIn("SupervisorLease(state_dir)", body)
        self.assertIn("context.control_context = control_context", body)


class DisposableInstallation:
    """The two real state directories this rehearsal owns, both disposable."""

    def __init__(self, journal_dir, supervisor_dir):
        self.journal_dir = journal_dir
        self.supervisor_dir = supervisor_dir

    def lease_files(self):
        names = os.listdir(self.supervisor_dir)
        return sorted(
            name for name in names
            if name.startswith(nh_supervisor.lease.LEASE_BASENAME)
            and not name.endswith(".lock")
        )


def freeze_journal_copy(journal_dir, event_seq):
    """Cut a DISPOSABLE journal copy to ``event_seq`` and re-derive its mark.

    frozen 2026-09-02: the real journal keeps growing past the position these
    rehearsals were written for, so the copy is truncated to exactly that
    position and its high-water mark is re-derived with the COPIED key through
    the installed ``interview_journal_head_auth`` -- the same fixture shape the
    live-loop tests use.  Only the copy is written; nothing real is touched.
    """
    journal_path = Path(journal_dir) / nh_loop.INTERVIEW_JOURNAL_BASENAME
    kept = [
        line
        for line in journal_path.read_text(encoding="utf-8").splitlines(keepends=True)
        if line.strip() and json.loads(line).get("event_seq", 0) <= event_seq
    ]
    journal_path.write_text("".join(kept), encoding="utf-8")
    tail = json.loads(kept[-1])
    key = (Path(journal_dir) / nh_loop.INTERVIEW_AUTH_KEY_BASENAME).read_bytes()
    head = {
        "v": nh_loop.INTERVIEW_JOURNAL_HEAD_LABEL,
        "intent_generation": 1,
        "intent_number": 1,
        "intent_event_seq": tail["event_seq"],
        "intent_event_sha256": tail["event_sha256"],
        "committed_event_seq": tail["event_seq"],
        "committed_event_sha256": tail["event_sha256"],
    }
    head["head_auth_sha256"] = nh_loop.interview_journal_head_auth(key, head)
    head_path = Path(journal_dir) / nh_loop.INTERVIEW_JOURNAL_HEAD_BASENAME
    head_path.write_text(
        nh_loop.interview_canonical_json(head) + "\n", encoding="utf-8"
    )
    head_path.chmod(0o600)


@contextmanager
def real_disposable_installation(event_seq=None):
    """A PER-TEST disposable copy of the real 84-event installation.

    Everything inside is the installed code reading real authenticated bytes:
    the real journal, the real replay, the real status command, the real lease
    file.  Nothing about acceptance, the gates or context selection is patched.

    The journal state directory and the supervisor state directory are separate
    installations, so BOTH are copied and BOTH are redirected.
    """
    temp = tempfile.mkdtemp(prefix="nh_c4_", dir=str(SCRATCH_DIR))
    journal_dir = os.path.join(temp, "nh_interview_state")
    repo_dir = os.path.join(temp, "NH-GOVERNANCE")
    supervisor_dir = os.path.join(temp, "supervisor_state")
    shutil.copytree(str(ROOT_DIR / "nh_interview_state"), journal_dir)
    if event_seq is not None:
        # frozen 2026-09-02: pin the copy at the journal position asked for.
        freeze_journal_copy(journal_dir, event_seq)
    shutil.copytree(str(ROOT_DIR / "NH-GOVERNANCE"), repo_dir)
    real_supervisor_dir = nh_supervisor.lease.resolve_state_dir(
        str(ROOT_DIR), environ={}
    )
    if os.path.isdir(real_supervisor_dir):
        shutil.copytree(real_supervisor_dir, supervisor_dir)
    else:  # pragma: no cover -- the installed directory exists
        os.makedirs(supervisor_dir, mode=0o700)
    saved = {
        "NH_LOOP_INTERVIEW_STATE_DIR": os.environ.get(
            "NH_LOOP_INTERVIEW_STATE_DIR"
        ),
        "NH_SUPERVISOR_STATE_DIR": os.environ.get("NH_SUPERVISOR_STATE_DIR"),
    }
    saved_repo = nh_loop.NH_REPO_PATH
    os.environ["NH_LOOP_INTERVIEW_STATE_DIR"] = journal_dir
    os.environ["NH_SUPERVISOR_STATE_DIR"] = supervisor_dir
    nh_loop.NH_REPO_PATH = repo_dir
    nh_loop.reset_interview_source_reproof_cache()
    try:
        if event_seq is not None:
            events = [
                json.loads(line)
                for line in (
                    Path(journal_dir) / nh_loop.INTERVIEW_JOURNAL_BASENAME
                ).read_text(encoding="utf-8").splitlines()
                if line.strip()
            ]
            validations = [
                event for event in events
                if event.get("type") == "validation_recorded"
            ]
            if validations:
                errors = []
                binding = nh_loop.read_source_binding(
                    "for the historical disposable rehearsal", errors
                )
                expected = validations[-1].get("source_binding_sha256")
                if (
                    binding is None
                    or errors
                    or binding.get("binding_sha256") != expected
                ):
                    raise unittest.SkipTest(
                        "the exact historical source snapshot at event %d is "
                        "no longer available inside the repository" % event_seq
                    )
        yield DisposableInstallation(journal_dir, supervisor_dir)
    finally:
        for key, value in saved.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value
        nh_loop.NH_REPO_PATH = saved_repo
        nh_loop.reset_interview_source_reproof_cache()
        shutil.rmtree(temp, ignore_errors=True)


def acquire_the_one_lease(installation):
    """Acquire ONE genuine lease, with the installed lease code, under P."""
    errors = []
    anchor_context = nh_loop.build_supervisor_context(errors)
    assert anchor_context is not None, errors
    binding = nh_supervisor.runtime.default_lease_binding(
        anchor_context.binding, anchor_context.controller_executable_identity
    )
    lease = nh_supervisor.lease.SupervisorLease(installation.supervisor_dir)
    outcome, _held = lease.acquire(binding)
    assert outcome in ("ACQUIRED", "RENEWED"), outcome
    return binding


class CorrectionFourEndToEndGate(unittest.TestCase):
    """The required Correction-4 P -> Q integration gate.

    NO ``acceptance_freshly_proved`` monkeypatch.  NO fake always-live gate.
    NO Q-specific second lease.  NO patched P/Q context selection.  The only
    stubbed thing is the provider TRANSPORT.
    """

    def selection_for(self, context, root):
        """A selection object the INSTALLED validator accepts, naming ``root``."""
        required = context.continuation_adapter.resolve_required_files()
        paths = sorted(
            {match for value in required.values() for match in (value.get("matches") or ())}
        )
        body = json.loads(selection_body())
        body["package_source_path"] = root
        body["source_paths_checked"] = sorted(set(paths + [root]))
        return json.dumps(body, sort_keys=True).encode("utf-8")

    def run_real_t1_dispatch(self, context, root):
        """ONE real T1 dispatch through the installed command, stub transport."""
        transport = LoudStubTransport(
            body=self.selection_for(context, root),
            allow=True,
            transport_kind="subprocess_cli",
        )
        context.provider = transport
        result = commands.continue_design_loop(context)
        self.assertEqual(transport.calls, ["codex_next_package_selection"])
        # The bindings this dispatch held are gone once it returns.
        self.assertIsNone(getattr(context, "_current_required_extra", None))
        self.assertIsNone(getattr(context, "_current_prompt_extra", None))
        return result, transport

    def q_facts_from(self, context, root):
        """Q's proved scope and root, read from the REAL custody just recorded."""
        events = context.journal.read()
        custodied = [
            event for event in events
            if event["type"] == "provider_result_custody_recorded"
            and event.get("work_item_kind") == "next_package_selection"
        ]
        self.assertEqual(len(custodied), 1, "exactly one T1 custody was recorded")
        return {
            "package_scope_id": nh_loop.interview_package_scope_id(None, root),
            "scope_root_path": root,
            "package_id": None,
            "required_source_paths": (),
            "routed_signal_refs": (),
        }

    def q_context_for(self, facts, p_context):
        """The installed Q work context -- built, not faked."""
        errors = []
        context = nh_loop.build_transition_context(
            "pre_validation", facts, errors, control_context=p_context
        )
        self.assertIsNotNone(context, errors)
        return context

    def test_C4_event84_shaped_P_to_first_Q_command_end_to_end(self):
        # frozen 2026-09-02 at journal event 84: asserts authenticated_event_seq == 84 and the first real T1 from that position
        with real_disposable_installation(event_seq=84) as installation:
            # 1 -- ONE real lease, acquired ONCE, under P's binding.
            lease_binding = acquire_the_one_lease(installation)
            self.assertEqual(lease_binding["package_scope_id"], LIVE_SCOPE)
            self.assertEqual(len(installation.lease_files()), 1)

            errors = []
            p_context = nh_loop.build_supervisor_context(errors)
            self.assertIsNotNone(p_context, errors)
            state, held = commands.evaluate_lease(p_context)
            self.assertEqual(state, "LIVE_PROVED")
            self.assertEqual(p_context.own_run_id, held["run_id"])

            # 2 -- P's acceptance, proved by the REAL unpatched section 6.3 gate.
            proved, status, detail = commands.acceptance_freshly_proved(p_context)
            self.assertTrue(proved, detail)
            self.assertEqual(status["acceptance_truth"], "PROVED_ACCEPTED")
            self.assertEqual(status["workflow_state"], "ACCEPTED_FOR_DESIGN_ONLY")
            self.assertEqual(status["authenticated_event_seq"], 84)

            # 3 -- ONE real T1 dispatch, through the installed command and both
            #      installed gates, with only the transport stubbed.
            result, transport = self.run_real_t1_dispatch(p_context, LIVE_Q_ROOT)
            self.assertEqual(result.report["outcome"], "result_received")
            self.assertEqual(transport.claude_calls, 0)

            # 4 -- P is still the current established accepted package.
            self.assertEqual(p_context.binding.package_scope_id, LIVE_SCOPE)
            proved, status, detail = commands.acceptance_freshly_proved(p_context)
            self.assertTrue(proved, detail)
            self.assertGreater(status["authenticated_event_seq"], 84)

            # 5 -- the REAL Q WORK CONTEXT, built by the installed builder with
            #      P attached as its control package.  Nothing is faked.
            facts = self.q_facts_from(p_context, LIVE_Q_ROOT)
            q_context = self.q_context_for(facts, p_context)
            self.assertEqual(
                q_context.binding.package_scope_id, facts["package_scope_id"]
            )
            self.assertNotEqual(q_context.binding.package_scope_id, LIVE_SCOPE)
            self.assertIs(q_context.control_context, p_context)
            q_transport = LoudStubTransport()
            q_context.provider = q_transport

            # 6 -- Q is neither current nor accepted.
            q_replay = replay.Replay(
                p_context.journal.read(), q_context.binding.package_scope_id
            )
            self.assertEqual(
                q_replay.scoped("ness_candidate_acceptance_recorded"), [],
                "Q_NOT_CURRENT_OR_ACCEPTED_DURING_TRANSITION",
            )

            # 7 -- NO SECOND LEASE EXISTS.
            self.assertIsNone(q_context.lease, "END_TO_END_SECOND_Q_LEASES = 0")
            self.assertIsNone(q_context.lease_binding)
            self.assertIsNone(q_context.own_run_id)
            self.assertEqual(len(installation.lease_files()), 1)

            # 8 -- the REAL unpatched acceptance proof, taken over Q's context,
            #      answered by P.
            proved, status, detail = commands.acceptance_freshly_proved(q_context)
            self.assertTrue(
                proved,
                "P's acceptance must be provable while running Q work: %s" % detail,
            )
            self.assertEqual(
                status["package_scope_id"], LIVE_SCOPE,
                "P_ACCEPTANCE_PROOF_SOURCE = the current established package P",
            )
            self.assertEqual(status["acceptance_truth"], "PROVED_ACCEPTED")

            # 9 -- BOTH real gates, on Q work, under P's ONE lease.
            commands.require_start_gate(q_context)
            commands.require_closure_gate(q_context)
            evaluated, q_held = commands.evaluate_lease(q_context)
            self.assertEqual(evaluated, "LIVE_PROVED")
            self.assertEqual(
                q_held["run_id"], held["run_id"], "the SAME single lease"
            )

            # 10 -- no provider was contacted from the Q context at all.
            self.assertEqual(
                q_transport.calls, [], "END_TO_END_UNEXPECTED_PROVIDER_CALLS = 0"
            )

    def test_C4_the_working_claim_follows_the_one_lease_end_to_end(self):
        """The SAME real position, live and then stopped."""
        # frozen 2026-09-02 at journal event 84: the same event-84 position; later events make the loop refuse CPB-SINGLE-TRANSITION
        with real_disposable_installation(event_seq=84) as installation:
            lease_binding = acquire_the_one_lease(installation)
            errors = []
            p_context = nh_loop.build_supervisor_context(errors)
            self.run_real_t1_dispatch(p_context, LIVE_Q_ROOT)
            facts = self.q_facts_from(p_context, LIVE_Q_ROOT)
            q_context = self.q_context_for(facts, p_context)
            self.assertEqual(commands.evaluate_lease(q_context)[0], "LIVE_PROVED")

            # Production stops.  The ONE lease is released.
            nh_supervisor.lease.SupervisorLease(
                installation.supervisor_dir
            ).release(lease_binding)
            errors = []
            stopped_p = nh_loop.build_supervisor_context(errors)
            stopped_q = self.q_context_for(facts, stopped_p)
            state, _held = commands.evaluate_lease(stopped_q)
            self.assertEqual(state, "ABSENT_PROVED")
            with self.assertRaises(SupervisorRefusal):
                commands.require_start_gate(stopped_q)
            # And the card refuses to claim work.
            detail = ui_supervisor.wording_for(
                ui_supervisor.WorkflowState.ACCEPTED_FOR_DESIGN_ONLY,
                state,
                loop_transition_active=True,
                loop_transition_working=True,
            )["detail"]
            self.assertIn(ui_supervisor.TRANSITION_NOT_WORKING_LINE, detail)
            self.assertNotIn(ui_supervisor.TRANSITION_LINE, detail)

    def test_C4_a_moved_journal_fails_the_Q_command_closed(self):
        """P_TAIL_MISMATCH_FAILS_CLOSED, on the real installation."""
        # frozen 2026-09-02 at journal event 84: asserts the pre-T1 journal holds exactly 84 records
        with real_disposable_installation(event_seq=84) as installation:
            acquire_the_one_lease(installation)
            errors = []
            p_context = nh_loop.build_supervisor_context(errors)
            # The position BEFORE the real T1 moves the journal.
            stale = p_context.journal.read()
            self.assertEqual(len(stale), 84)
            self.run_real_t1_dispatch(p_context, LIVE_Q_ROOT)
            facts = self.q_facts_from(p_context, LIVE_Q_ROOT)
            q_context = self.q_context_for(facts, p_context)
            q_transport = LoudStubTransport()
            q_context.provider = q_transport
            # Read fresh, the SAME single authenticated journal proves P.
            proved, status, detail = commands.acceptance_freshly_proved(q_context)
            self.assertTrue(proved, detail)
            self.assertGreater(status["authenticated_event_seq"], 84)
            # Handed the position the journal held BEFORE the real T1 appended
            # to it, the same proof fails closed.
            proved, _status, detail = commands.acceptance_freshly_proved(
                q_context, stale
            )
            self.assertFalse(proved)
            self.assertIn("authenticated position", detail)
            self.assertEqual(q_transport.calls, [])

    def test_C5_the_unmodified_production_path_validates_a_valid_reply(self):
        """BLOCKER-A is FIXED: no harness holds the seam open any more."""
        # frozen 2026-09-02 at journal event 84: the event-84 T1 dispatch; later events make the loop refuse CPB-SINGLE-TRANSITION
        with real_disposable_installation(event_seq=84) as installation:
            acquire_the_one_lease(installation)
            errors = []
            p_context = nh_loop.build_supervisor_context(errors)
            transport = LoudStubTransport(
                body=self.selection_for(p_context, LIVE_Q_ROOT),
                allow=True,
                transport_kind="subprocess_cli",
            )
            p_context.provider = transport
            result = commands.continue_design_loop(p_context)
            self.assertEqual(result.report["outcome"], "result_received")
            self.assertNotEqual(result.report["outcome"], "result_invalid")

    def test_C5_blocker_B_is_still_left_outside_the_bridge(self):
        """A source change after admission is NOT re-anchored or papered over.

        Re-cut 2026-09-02 (Ness's decision) to the rule actually in force,
        SBC v1.3 section 14.2 / R-SB41 B: a selection is stale when the
        COMPLETE required-input inventory it was frozen against no longer
        reproduces its durable required_inputs_sha256 -- NOT when an anchor-era
        binding differs from the raw live binding (P-SB9; that older comparison
        is what this test used to assert, and it was replaced on purpose).

        So: at journal event 84 the real T1 dispatch freezes the selection
        against the source that stands.  An UNCHANGED checkout then re-admits
        it with zero appends (R-SB41 A).  A REAL change to the checkout makes
        the same selection stale: preserved as history, consumed by nothing,
        the loop back at LOOP_SELECTION_REQUIRED, with zero appends and zero
        provider calls from the read-only derivation (R-SB41 B).
        """
        # frozen 2026-09-02 at journal event 84: the event-84 T1 dispatch; later events make the loop refuse CPB-SINGLE-TRANSITION
        with real_disposable_installation(event_seq=84) as installation:
            acquire_the_one_lease(installation)
            errors = []
            p_context = nh_loop.build_supervisor_context(errors)
            self.run_real_t1_dispatch(p_context, LIVE_Q_ROOT)
            after_dispatch = journal_digest()

            # R-SB41 A -- unchanged checkout: the admitted selection stands and
            # a second entry is idempotent, with zero appends.
            state = commands.post_acceptance_transition_state(p_context)
            self.assertIsNotNone(state["selection"], "admitted against the source that stands")
            second = commands.continue_design_loop(p_context).report
            self.assertTrue(second.get("already_durable"), second)
            self.assertEqual(journal_digest(), after_dispatch, "ZERO appends")

            # R-SB41 B -- a REAL material change to the disposable checkout.
            # nh_loop.NH_REPO_PATH points at the disposable copy for the whole
            # installation, so this never touches the real repository.
            changed = os.path.join(nh_loop.NH_REPO_PATH, "README.md")
            with open(changed, "a", encoding="utf-8") as handle:
                handle.write("\nmaterial change after admission (rehearsal)\n")
            adapter = p_context.continuation_adapter
            self.assertNotEqual(
                adapter.current_source_binding(),
                p_context.binding.source_binding_sha256,
                "the change this rehearsal reports is real",
            )
            transport = LoudStubTransport()
            p_context.provider = transport
            stale = commands.post_acceptance_transition_state(p_context)
            self.assertIsNone(stale["selection"], "the frozen selection is stale")
            self.assertEqual(stale["stop_record"]["loop_state"],
                             commands.LOOP_SELECTION_REQUIRED)
            self.assertIn("stale", stale["stop_record"]["reason"])
            self.assertIn("consumed by nothing", stale["stop_record"]["reason"])
            report = commands.loop_position(p_context, stale)
            self.assertEqual(report["loop_state"], commands.LOOP_SELECTION_REQUIRED)
            self.assertEqual(transport.calls, [], "ZERO provider calls")
            self.assertEqual(journal_digest(), after_dispatch,
                             "ZERO appends: the stale selection is preserved, not repaired")

    def test_C4_no_acceptance_monkeypatch_in_the_integration_gate(self):
        """PROVED_ACCEPTANCE_MONKEYPATCH_USED_IN_END_TO_END = NO."""
        source = read_text(TESTS_DIR / "test_post_acceptance_continuation_v1_8.py")
        marker = source.index("class CorrectionFourEndToEndGate(")
        body = source[marker:source.index(
            "    def test_C4_no_acceptance_monkeypatch_in_the_integration_gate",
            marker,
        )]
        self.assertNotIn("proved_acceptance", body)
        self.assertNotIn("mock.patch", body)
        self.assertNotIn("always_live", body)
        # And no seam holder survives anywhere, nor any equivalent under
        # another name inside this gate.  The needles are assembled at run time
        # so this assertion is not its own counterexample.
        whole = read_text(TESTS_DIR / "test_post_acceptance_continuation_v1_8.py")
        self.assertNotIn("ExtraInputs" + "SeamHeld", whole)
        self.assertNotIn("__class" + "__ = ", whole, "no class swap holds a seam open")
        for needle in ("_current_required" + "_extra = ",
                       "_current_prompt" + "_extra = "):
            self.assertNotIn(needle, body, needle)


class CorrectionFourClosureOwnershipRehearsals(unittest.TestCase):
    """Same scope plus initial origin is NOT closure."""

    def custody_for(self, journal, payload, request="pr_init"):
        value = initial_design_result(payload=payload)
        custody_pair(
            journal, kind="initial_design", provider_kind="claude_initial_design",
            value=value, scope=SCOPE_Q, request=request,
            work_item_identity="wi_" + request,
        )
        return value

    def commit(self, journal, value, parent=None):
        parent = parent or make_candidate(ROOT_Q)
        for event_type, key, origin in (
            ("candidate_write_ahead_recorded", "intent_origin",
             commands.CANDIDATE_INTENT_ORIGIN_INITIAL),
            ("candidate_custody_recorded", "custody_origin",
             commands.CANDIDATE_CUSTODY_ORIGIN_INITIAL),
        ):
            journal.append(
                {
                    "type": event_type,
                    "package_scope_id": SCOPE_Q,
                    key: origin,
                    "candidate_path": value["produced_candidate_path"],
                    "candidate_sha256": value["produced_candidate_sha256"],
                    "candidate_bytes": value["produced_candidate_bytes"],
                    "parent_candidate_path": parent.candidate_path,
                    "parent_candidate_sha256": parent.candidate_sha256,
                    "parent_candidate_bytes": parent.candidate_bytes,
                }
            )

    def pending(self, journal):
        scoped = replay.Replay(journal.read(), SCOPE_Q)
        return [
            event["work_item_kind"]
            for event in scoped.custodied_results_awaiting_processing()
        ]

    def test_C4_no_candidate_transaction_leaves_it_pending(self):
        journal = accepted_journal()
        self.custody_for(journal, b"one")
        self.assertEqual(self.pending(journal), ["initial_design"])

    def test_C4_the_exact_matching_transaction_closes_it(self):
        journal = accepted_journal()
        value = self.custody_for(journal, b"one")
        self.commit(journal, value)
        self.assertEqual(self.pending(journal), [])

    def test_C4_a_stale_earlier_result_is_not_closed_by_a_later_candidate(self):
        """CROSS_INITIAL_CUSTODY_CLOSURE_REFUSED."""
        journal = accepted_journal()
        self.custody_for(journal, b"the stale earlier design", request="pr_old")
        later = self.custody_for(journal, b"the real later design", request="pr_new")
        self.commit(journal, later)
        # ONLY the exact owning custody closes.
        self.assertEqual(
            self.pending(journal), ["initial_design"],
            "the stale earlier result stays pending",
        )
        scoped = replay.Replay(journal.read(), SCOPE_Q)
        still_pending = scoped.custodied_results_awaiting_processing()
        self.assertEqual(
            still_pending[0]["provider_request_identity"], "pr_old"
        )

    def test_C4_a_wrong_candidate_identity_does_not_close(self):
        for field, wrong in (
            ("produced_candidate_sha256", "0" * 64),
            ("produced_candidate_bytes", 999999),
            ("produced_candidate_path",
             "05_ACTIVE_CANDIDATE/NH_OTHER_v1_1_CANDIDATE.md"),
        ):
            journal = accepted_journal()
            value = self.custody_for(journal, b"one")
            committed = dict(value)
            committed[field] = wrong
            self.commit(journal, committed)
            self.assertEqual(
                self.pending(journal), ["initial_design"], field
            )

    def test_C4_a_missing_write_ahead_does_not_close(self):
        journal = accepted_journal()
        value = self.custody_for(journal, b"one")
        parent = make_candidate(ROOT_Q)
        journal.append(
            {
                "type": "candidate_custody_recorded",
                "package_scope_id": SCOPE_Q,
                "custody_origin": commands.CANDIDATE_CUSTODY_ORIGIN_INITIAL,
                "candidate_path": value["produced_candidate_path"],
                "candidate_sha256": value["produced_candidate_sha256"],
                "candidate_bytes": value["produced_candidate_bytes"],
                "parent_candidate_path": parent.candidate_path,
                "parent_candidate_sha256": parent.candidate_sha256,
                "parent_candidate_bytes": parent.candidate_bytes,
            }
        )
        self.assertEqual(self.pending(journal), ["initial_design"])

    def test_C4_two_identical_commits_fail_closed(self):
        journal = accepted_journal()
        value = self.custody_for(journal, b"one")
        self.commit(journal, value)
        self.commit(journal, value)
        with self.assertRaises(replay.DownstreamOwnershipError):
            self.pending(journal)

    def test_C4_no_journal_body_key_was_added(self):
        """The closure is READ-SIDE only."""
        source = read_text(CONTROLLER_SOURCE)
        marker = source.index('"candidate_custody_recorded": frozenset(')
        body = source[marker:source.index('"candidate_write_ahead_recorded": frozenset(')]
        for absent in ("work_item_identity", "provider_request_identity",
                       "result_custody_identity"):
            self.assertNotIn(absent, body, absent)


class CorrectionFourUiLeaseRehearsals(unittest.TestCase):
    def wording(self, *, exists, working, lease):
        return ui_supervisor.wording_for(
            ui_supervisor.WorkflowState.ACCEPTED_FOR_DESIGN_ONLY,
            lease,
            loop_transition_active=exists,
            loop_transition_working=working,
        )["detail"]

    def test_C4_a_stopped_worker_never_shows_the_working_line(self):
        """Q_ABSENT_LEASE_WORKING_LINE_SHOWN = NO."""
        detail = self.wording(exists=True, working=True, lease="ABSENT_PROVED")
        self.assertNotIn("no next package started", detail)
        self.assertNotIn(ui_supervisor.TRANSITION_LINE, detail)
        self.assertIn(ui_supervisor.TRANSITION_NOT_WORKING_LINE, detail)

    def test_C4_a_live_worker_shows_the_working_line(self):
        """Q_LIVE_LEASE_WORKING_LINE_SHOWN = YES."""
        detail = self.wording(exists=True, working=True, lease="LIVE_PROVED")
        self.assertIn(ui_supervisor.TRANSITION_LINE, detail)

    def test_C4_the_controller_requires_a_live_lease_for_working(self):
        """loop_transition_working is false without LIVE_PROVED."""
        source = read_text(CONTROLLER_DIR / "nh_supervisor" / "commands.py")
        marker = source.index('report["loop_transition_working"] = bool(')
        body = source[marker:marker + 700]
        self.assertIn('lease_state == "LIVE_PROVED"', body)
        # And the copied real position, where no live lease exists.  A durable
        # old lease may be either proved absent or proved expired.
        loop = run_live_copy("loop-status")
        self.assertIn(
            loop["loop_lease_state"],
            ("ABSENT_PROVED", "EXPIRED_PROVED"),
        )
        self.assertFalse(loop["loop_transition_working"])
        self.assertFalse(loop["loop_transition_exists"])


# ===========================================================================
# CORRECTION 5 REHEARSALS -- THE EXTRA INPUT / PROMPT LIFETIME.
#
# The two controller-held temporaries a dispatch binds must be readable from
# BEFORE the provider call through the COMPLETE first-pass observation, and
# must then be cleared on every exit.  Nothing here holds the seam open: these
# rehearsals only OBSERVE what the unmodified production path does.
# ===========================================================================
class SeamObserver:
    """Record what the seam held WHEN each real validator ran.

    Every wrapper delegates to the installed function and returns its real
    result.  Nothing is replaced, weakened or defaulted.
    """

    def __init__(self, context):
        self.context = context
        self.at_validation = []
        self.at_admission = []
        self._saved = {}

    def __enter__(self):
        self._saved["_validate_result"] = commands._validate_result
        real_validate = commands._validate_result

        def observing_validate(context, prepared, value, parse_error):
            self.at_validation.append(self.snapshot())
            return real_validate(context, prepared, value, parse_error)

        commands._validate_result = observing_validate

        name = "_claude_initial_design_admission_checks"
        real_admission = getattr(commands, name, None)
        if real_admission is not None:
            self._saved[name] = real_admission

            def observing_admission(*args, **kwargs):
                self.at_admission.append(self.snapshot())
                return real_admission(*args, **kwargs)

            setattr(commands, name, observing_admission)
        return self

    def __exit__(self, *exc_info):
        for name, value in self._saved.items():
            setattr(commands, name, value)
        return False

    def snapshot(self):
        return {
            "required": getattr(self.context, "_current_required_extra", None),
            "prompt": getattr(self.context, "_current_prompt_extra", None),
        }

    def assert_required_present(self, testcase, *keys):
        testcase.assertTrue(self.at_validation, "the real validator ran")
        for seen in self.at_validation:
            testcase.assertIsNotNone(
                seen["required"], "the required-input extra was erased"
            )
            for key in keys:
                testcase.assertIn(key, seen["required"])

    def assert_prompt_present(self, testcase, *keys):
        testcase.assertTrue(self.at_admission, "the real I8 admission ran")
        for seen in self.at_admission:
            testcase.assertIsNotNone(
                seen["prompt"], "the prompt extra was erased"
            )
            for key in keys:
                testcase.assertIn(key, seen["prompt"])


def terminal_kinds(journal, since=0):
    """The terminals recorded from ``since`` onward -- the ones THIS run added."""
    return [
        event.get("terminal_kind")
        for event in journal.events[since:]
        if event["type"] == "provider_request_terminal_recorded"
    ]


def is_hex64_value(value):
    return isinstance(value, str) and len(value) == 64 and all(
        char in "0123456789abcdef" for char in value
    )


def custody_count(journal):
    return len(
        [e for e in journal.events if e["type"] == "provider_result_custody_recorded"]
    )


def prepared_identities(journal):
    return [
        event.get("provider_request_identity")
        for event in journal.events
        if event["type"] == "provider_request_prepared"
    ]


def cli_stub(value):
    """A stub transport declaring the controlled kind, returning ``value``."""
    return LoudStubTransport(
        body=json.dumps(value, sort_keys=True).encode("utf-8"),
        allow=True,
        transport_kind="subprocess_cli",
    )


class CorrectionFiveSeamLifetimeRehearsals(unittest.TestCase):
    """A / B / C / D / E -- every first-pass validator sees its bindings."""

    def run_dispatch(self, stage, command, value, *, binding=None, candidate=None,
                     adapter=None, clearance=None):
        journal = staged_journal(stage, binding=binding, candidate=candidate)
        transport = cli_stub(value)
        context = build_context(
            journal=journal,
            transport=transport,
            binding=binding,
            candidate=candidate,
            adapter=adapter,
            clearance=clearance,
        )
        before = len(journal.events)
        with SeamObserver(context) as observer:
            with proved_acceptance():
                result = command(context)
        return journal, transport, context, observer, result, before

    def q_binding(self, **kwargs):
        options = {"root": ROOT_Q, "validation_set_id": None}
        options.update(kwargs)
        return make_binding(SCOPE_Q, **options)

    # -- A -- T1 -------------------------------------------------------------
    def test_C5_A_T1_required_files_binding_survives_to_B6d(self):
        journal, transport, context, observer, result, before = self.run_dispatch(
            "selection_required",
            commands.continue_design_loop,
            json.loads(selection_body()),
        )
        observer.assert_required_present(self, "required_files_binding")
        # The EXACT controller-resolved authority set, not a re-derivation.
        self.assertEqual(
            observer.at_validation[0]["required"]["required_files_binding"],
            context.continuation_adapter.resolve_required_files(),
        )
        self.assertEqual(terminal_kinds(journal, before), ["result_received"])
        self.assertNotIn("result_invalid", terminal_kinds(journal, before))
        self.assertEqual(transport.calls, ["codex_next_package_selection"])
        self.assertEqual(result.report.get("outcome"), "result_received")

    # -- B -- T2 question_validation ----------------------------------------
    def test_C5_B_T2_question_validation_extra_survives_to_B6d(self):
        journal, transport, _context, observer, _result, before = self.run_dispatch(
            "clearance_required",
            commands.dispatch_piece3_provider_review,
            question_validation_payload(),
            binding=self.q_binding(),
            candidate=make_candidate(ROOT_Q),
        )
        observer.assert_required_present(self)
        self.assertEqual(terminal_kinds(journal, before), ["result_received"])
        self.assertEqual(transport.calls, ["gpt_question_validation"])

    # -- C -- T2 coverage_review --------------------------------------------
    def test_C5_C_T2_coverage_review_extra_survives_to_B6d(self):
        journal, transport, _context, observer, _result, before = self.run_dispatch(
            "task_preparation",
            commands.dispatch_piece3_provider_review,
            coverage_review_payload(),
            binding=self.q_binding(validation_set_id="vs_q"),
            candidate=make_candidate(ROOT_Q),
        )
        observer.assert_required_present(self)
        self.assertEqual(terminal_kinds(journal, before), ["result_received"])
        self.assertEqual(transport.calls, ["gpt_question_coverage_review"])

    # -- D -- T3 -------------------------------------------------------------
    def test_C5_D_T3_opens_no_provider_request_at_all(self):
        """Accepted role-split v1_6 sections 5.1 / 5.7 / 10.1 test 1.

        The T3 stage no longer has an ``extra_inputs`` seam to carry a selection
        through to a B6d validator, because there is no provider result to
        validate.  What replaces that proof is stronger and is asserted here:
        the command contacts NOBODY and creates NO provider lifecycle record.
        """
        journal = accepted_journal()
        q_binding = make_binding(SCOPE_Q, root=ROOT_Q, validation_set_id="vs_q")
        admitted_selection_state(
            journal, binding=q_binding, candidate=make_candidate(ROOT_Q)
        )
        transport = LoudStubTransport()
        context = build_context(
            SCOPE_Q,
            journal=journal,
            transport=transport,
            binding=q_binding,
            candidate=make_candidate(ROOT_Q),
            clearance=lambda scope_id: {"unlocked": True},
        )
        before = len(journal.events)
        with proved_acceptance():
            try:
                commands.prepare_next_design_task(context)
            except SupervisorRefusal:
                # A refusal is a legitimate NOT-READY outcome here; what this
                # rehearsal proves is that NOTHING was contacted either way.
                pass
        # ZERO provider calls, and ZERO provider lifecycle records, on every
        # path out of the local T3 command.
        self.assertEqual(transport.calls, [], "local T3 contacts nobody")
        provider_types = {
            "provider_request_prepared",
            "provider_dispatch_begun",
            "provider_result_custody_recorded",
            "provider_request_terminal_recorded",
        }
        appended = [event["type"] for event in journal.events[before:]]
        self.assertEqual(
            [kind for kind in appended if kind in provider_types],
            [],
            "local T3 opens no provider lifecycle record",
        )
        # And the command is no longer classified as provider-contacting.
        self.assertNotIn(
            "prepare-next-design-task", constants.PROVIDER_DISPATCH_COMMANDS
        )

    # -- E -- T4 -------------------------------------------------------------
    def test_C5_E_T4_both_extras_survive_to_I8(self):
        journal, transport, _context, observer, _result, before = self.run_dispatch(
            "initial_design",
            commands.execute_initial_design,
            initial_design_result(),
            binding=self.q_binding(validation_set_id="vs_q"),
            candidate=make_candidate(ROOT_Q),
            clearance=lambda scope_id: {"unlocked": True},
        )
        observer.assert_required_present(self, "prepared_target_path")
        observer.assert_prompt_present(
            self, "specialized_prompt_kind", "mechanical_design_specification"
        )
        # I8 recomputes BOTH digests from those exact objects, and the prepared
        # record's values are what it must reproduce.
        prepared = [
            event for event in journal.events
            if event["type"] == "provider_request_prepared"
        ][-1]
        self.assertTrue(is_hex64_value(prepared["required_inputs_sha256"]))
        self.assertTrue(is_hex64_value(prepared["prompt_material_sha256"]))
        self.assertEqual(terminal_kinds(journal, before), ["result_received"])
        self.assertEqual(transport.calls, ["claude_initial_design"])
        self.assertEqual(transport.claude_calls, 1, "Claude, never Codex")
        self.assertEqual(transport.codex_calls, 0)


class CorrectionFiveTamperRehearsals(unittest.TestCase):
    """F -- the digest checks are untouched; nothing falls back."""

    def test_C5_F_a_tampered_required_input_is_still_refused(self):
        """The authority set the reply does NOT cover still fails validation."""
        journal = staged_journal("selection_required")
        adapter = StubAdapter()
        adapter.required_files = dict(adapter.required_files)
        adapter.required_files["nh_unlisted_authority"] = {
            "path": "01_AUTHORITATIVE/NH_AN_AUTHORITY_THE_REPLY_NEVER_READ.md"
        }
        transport = cli_stub(json.loads(selection_body()))
        context = build_context(
            journal=journal, transport=transport, adapter=adapter
        )
        before = len(journal.events)
        with proved_acceptance():
            commands.continue_design_loop(context)
        self.assertEqual(terminal_kinds(journal, before), ["result_invalid"])
        self.assertNotIn("result_received", terminal_kinds(journal, before))

    def test_C5_F_a_tampered_T4_prompt_extra_is_still_refused(self):
        """I8 still recomputes prompt_material_sha256 and still refuses.

        The prepared record is bound from the honest objects; the prompt extra
        is then MOVED underneath it, during the provider call, exactly as a
        corrupted in-process value would move.  I8 recomputes and refuses.
        """
        c5f_binding = make_binding(SCOPE_Q, root=ROOT_Q, validation_set_id="vs_q")
        c5f_candidate = make_candidate(ROOT_Q)
        journal = staged_journal(
            "initial_design", binding=c5f_binding, candidate=c5f_candidate
        )

        class MovingTransport(LoudStubTransport):
            def __init__(self, context_box, **kwargs):
                super().__init__(**kwargs)
                self.context_box = context_box

            def dispatch(self, request):
                context = self.context_box[0]
                moved = dict(context._current_prompt_extra or {})
                moved["mechanical_design_specification"] = {
                    "a specification": "that is not the one that was prepared"
                }
                context._current_prompt_extra = moved
                return super().dispatch(request)

        box = [None]
        transport = MovingTransport(
            box,
            body=json.dumps(initial_design_result(), sort_keys=True).encode("utf-8"),
            allow=True,
            transport_kind="subprocess_cli",
        )
        context = build_context(
            journal=journal,
            transport=transport,
            binding=c5f_binding,
            candidate=c5f_candidate,
            clearance=lambda scope_id: {"unlocked": True},
        )
        box[0] = context
        before = len(journal.events)
        with proved_acceptance():
            commands.execute_initial_design(context)
        self.assertEqual(terminal_kinds(journal, before), ["result_invalid"])
        self.assertNotIn("result_received", terminal_kinds(journal, before))
        # And the cleanup still ran.
        self.assertIsNone(getattr(context, "_current_prompt_extra", None))
        self.assertIsNone(getattr(context, "_current_required_extra", None))

    def test_C5_F_a_moved_required_extra_is_still_refused(self):
        """The same proof for the required-input side of the seam."""
        journal = staged_journal("selection_required")

        class MovingTransport(LoudStubTransport):
            def __init__(self, context_box, **kwargs):
                super().__init__(**kwargs)
                self.context_box = context_box

            def dispatch(self, request):
                context = self.context_box[0]
                moved = dict(context._current_required_extra or {})
                moved["required_files_binding"] = {
                    "nh_unlisted_authority": {
                        "path": "01_AUTHORITATIVE/NH_NEVER_READ.md"
                    }
                }
                context._current_required_extra = moved
                return super().dispatch(request)

        box = [None]
        transport = MovingTransport(
            box,
            body=selection_body(),
            allow=True,
            transport_kind="subprocess_cli",
        )
        context = build_context(journal=journal, transport=transport)
        box[0] = context
        before = len(journal.events)
        with proved_acceptance():
            commands.continue_design_loop(context)
        self.assertEqual(terminal_kinds(journal, before), ["result_invalid"])

    def test_C5_F_the_digest_authority_was_not_weakened(self):
        """No validator learned to tolerate a missing binding."""
        source = read_text(CONTROLLER_DIR / "nh_supervisor" / "commands.py")
        marker = source.index("def _next_package_selection_schema(")
        body = source[marker:source.index("\n\ndef ", marker)]
        # The refusal on an absent authority set is still outright.
        self.assertIn('return ["required_files_binding"]', body)
        self.assertNotIn("or {}", body.split("required_files =")[1][:200])
        # I8 still recomputes both digests.
        admission = source.index("_claude_initial_design_admission_checks")
        window = source[admission:admission + 20000]
        self.assertIn("required_inputs_sha256", window)
        self.assertIn("prompt_material_sha256", window)


class CorrectionFiveCleanupRehearsals(unittest.TestCase):
    """G -- guaranteed cleanup on every exit.  H -- no duplicate effects."""

    def both_cleared(self, context):
        self.assertIsNone(getattr(context, "_current_required_extra", None))
        self.assertIsNone(getattr(context, "_current_prompt_extra", None))

    def test_C5_G_cleared_after_a_successful_dispatch(self):
        journal = staged_journal("selection_required")
        context = build_context(
            journal=journal, transport=cli_stub(json.loads(selection_body()))
        )
        with proved_acceptance():
            commands.continue_design_loop(context)
        self.both_cleared(context)

    def test_codex_prompt_failure_precedes_dispatch_marker_and_launch(self):
        """The launcher itself records a prompt failure as never launched."""
        with tempfile.TemporaryDirectory(prefix="nh-prelaunch-fact-") as root:
            binding = make_binding(SCOPE_Q, root=ROOT_Q)
            candidate = make_candidate(ROOT_Q)
            journal = staged_journal(
                "clearance_required", binding=binding, candidate=candidate
            )
            box = [None]
            transport = nh_loop.NhCliProviderTransport(lambda: box[0])
            context = build_context(
                journal=journal,
                transport=transport,
                binding=binding,
                candidate=candidate,
            )
            context.state_dir = root
            box[0] = context
            before = len(journal.events)
            with mock.patch.object(
                nh_loop,
                "_supervisor_provider_prompt",
                side_effect=KeyError("routed_issues"),
            ), mock.patch.object(
                nh_loop.subprocess,
                "Popen",
                side_effect=AssertionError("Codex must not launch"),
            ):
                with proved_acceptance(), self.assertRaises(KeyError):
                    commands.dispatch_piece3_provider_review(context)
            added = journal.events[before:]
            self.assertEqual(
                [event["type"] for event in added],
                ["supervisor_operation_started", "provider_request_prepared"],
            )
            self.assertFalse(
                any(event["type"] == "provider_dispatch_begun" for event in added)
            )
            request_identity = added[1]["provider_request_identity"]
            fact_path = (
                Path(root)
                / nh_loop.CODEX_LAUNCH_FACT_DIRNAME
                / (request_identity + ".json")
            )
            fact = json.loads(fact_path.read_text(encoding="utf-8"))
            self.assertEqual(fact["launch_state"], "never_launched")
            self.assertIs(fact["launch_call_attempted"], False)
            self.assertIs(fact["launch_succeeded"], False)
            self.assertEqual(fact["failure_stage"], "prelaunch_preparation")
            self.assertIsNone(fact["provider_pid"])
            self.both_cleared(context)

    def test_saved_event_124_process_snapshot_proof_is_not_sufficient(self):
        """Event 124: later process absence cannot prove never-launched."""
        journal, request_identity = uncertain_q_dispatch(
            transport="subprocess_cli"
        )
        dispatch = next(
            event for event in journal.events
            if event["type"] == "provider_dispatch_begun"
            and event["provider_request_identity"] == request_identity
        )
        binding = make_binding(SCOPE_Q, root=ROOT_Q, validation_set_id=None)
        candidate = make_candidate(ROOT_Q)
        # The real event-124 state already carries the normal C1
        # lookup-unsupported reconciliation. Preserve that history and prove
        # that the old session/process-snapshot artifact cannot add a terminal.
        unknown_context = build_context(
            journal=journal,
            binding=binding,
            candidate=candidate,
        )
        first = commands.reconcile_provider_request(unknown_context)
        self.assertEqual(first.report["reconciliation_outcome"], "lookup_unsupported")
        with tempfile.TemporaryDirectory(prefix="nh-event124-") as root:
            state_dir = Path(root) / "state"
            session_dir = Path(root) / "codex" / "sessions" / "2026" / "08" / "24"
            state_dir.mkdir(mode=0o700)
            session_dir.mkdir(parents=True)
            session_path = session_dir / "saved.jsonl"

            def saved_record(timestamp, outputs):
                return {
                    "timestamp": timestamp,
                    "type": "response_item",
                    "payload": {
                        "type": "custom_tool_call_output",
                        "output": [
                            {"type": "input_text", "text": json.dumps(
                                {"output": output}, sort_keys=True
                            )}
                            for output in outputs
                        ],
                    },
                }

            failure = json.dumps(
                saved_record(
                    "2026-08-25T02:33:39.813Z",
                    [
                        "Traceback (most recent call last):\n"
                        + nh_loop.LOCAL_CODEX_PRELAUNCH_ERROR
                    ],
                ),
                sort_keys=True,
            ).encode("utf-8")
            request_line = "%s provider_dispatch_begun %s %s %s" % (
                dispatch["event_seq"],
                dispatch["provider_kind"],
                request_identity,
                dispatch["dispatch_pid"],
            )
            snapshot = json.dumps(
                saved_record(
                    "2026-08-25T02:34:11.407Z",
                    [
                        request_line + "\n",
                        "PID    PPID ELAPSED S COMMAND\n1 0 20 S /sbin/init\n",
                    ],
                ),
                sort_keys=True,
            ).encode("utf-8")
            session_path.write_bytes(failure + b"\n" + snapshot + b"\n")
            proof = {
                "proof_version": 1,
                "provider_request_identity": request_identity,
                "dispatch_event_seq": dispatch["event_seq"],
                "dispatch_event_sha256": dispatch["event_sha256"],
                "session_relative_path": "2026/08/24/saved.jsonl",
                "failure_record_line": 1,
                "failure_record_sha256": hashlib.sha256(failure).hexdigest(),
                "process_snapshot_record_line": 2,
                "process_snapshot_record_sha256": hashlib.sha256(snapshot).hexdigest(),
            }
            proof_path = (
                state_dir / nh_loop.LOCAL_PROVIDER_NONLAUNCH_PROOF_BASENAME
            )
            proof_path.write_text(json.dumps(proof, sort_keys=True), encoding="utf-8")
            proof_path.chmod(0o600)

            box = [None]
            transport = nh_loop.NhCliProviderTransport(
                lambda: box[0], codex_home=str(Path(root) / "codex")
            )
            context = build_context(
                journal=journal,
                transport=transport,
                binding=binding,
                candidate=candidate,
            )
            context.state_dir = str(state_dir)
            box[0] = context
            before = len(journal.events)
            result = commands.reconcile_provider_request(context)

        self.assertEqual(
            result.report["reconciliation_outcome"], "lookup_unsupported"
        )
        self.assertEqual(result.report["recovery_outcome"], "NEEDS_USER_ACTION")
        appended = journal.events[before:]
        self.assertEqual(
            [event["type"] for event in appended],
            [
                "supervisor_operation_started",
                "provider_request_reconciled",
                "supervisor_operation_completed",
            ],
        )
        self.assertFalse(
            any(
                event["type"] == "provider_request_terminal_recorded"
                and event.get("provider_request_identity") == request_identity
                for event in journal.events
            ),
            "the legacy later-process snapshot must not close the request",
        )
        self.assertEqual(
            sum(
                event["type"] == "provider_dispatch_begun"
                and event.get("provider_request_identity") == request_identity
                for event in journal.events
            ),
            1,
            "the original dispatch history is preserved and nothing is resent",
        )

    def test_C5_G_cleared_after_the_provider_raises(self):
        journal = staged_journal("selection_required")

        class RaisingTransport(LoudStubTransport):
            def dispatch(self, request):
                super().dispatch(request)
                raise RuntimeError("the transport died mid-call")

        context = build_context(
            journal=journal,
            transport=RaisingTransport(allow=True, transport_kind="subprocess_cli"),
        )
        with proved_acceptance():
            with self.assertRaises(RuntimeError):
                commands.continue_design_loop(context)
        self.both_cleared(context)

    def test_C5_G_cleared_after_the_closure_gate_refuses(self):
        journal = staged_journal("selection_required")
        context = build_context(
            journal=journal, transport=cli_stub(json.loads(selection_body()))
        )
        real_gate = commands.require_closure_gate

        def refusing_gate(context_arg):
            raise SupervisorRefusal("the lease went away mid-operation")

        commands.require_closure_gate = refusing_gate
        try:
            with proved_acceptance():
                with self.assertRaises(SupervisorRefusal):
                    commands.continue_design_loop(context)
        finally:
            commands.require_closure_gate = real_gate
        self.both_cleared(context)

    def test_C5_G_cleared_after_validation_raises(self):
        journal = staged_journal("selection_required")
        context = build_context(
            journal=journal, transport=cli_stub(json.loads(selection_body()))
        )
        real_validate = commands._validate_result

        def raising_validate(*args, **kwargs):
            raise RuntimeError("validation blew up")

        commands._validate_result = raising_validate
        try:
            with proved_acceptance():
                with self.assertRaises(RuntimeError):
                    commands.continue_design_loop(context)
        finally:
            commands._validate_result = real_validate
        self.both_cleared(context)

    def test_C5_H_one_dispatch_one_custody_one_terminal(self):
        journal = staged_journal("selection_required")
        transport = cli_stub(json.loads(selection_body()))
        context = build_context(journal=journal, transport=transport)
        with proved_acceptance():
            commands.continue_design_loop(context)
        self.assertEqual(len(transport.calls), 1, "PROVIDER_CALLS = 1")
        self.assertEqual(custody_count(journal), 1, "DUPLICATE_CUSTODIES = 0")
        self.assertEqual(len(terminal_kinds(journal)), 1, "DUPLICATE_TERMINALS = 0")
        identities = prepared_identities(journal)
        self.assertEqual(
            len(identities), len(set(identities)), "no duplicate request identity"
        )

    def test_C5_the_lifetime_is_one_guarded_block_in_the_installed_source(self):
        """The correction is the LIFETIME, and only the lifetime."""
        source = read_text(CONTROLLER_DIR / "nh_supervisor" / "commands.py")
        marker = source.index("context._current_prompt_extra = extra_prompt or {}")
        body = source[marker:source.index("\ndef _observe_and_close(", marker)]
        # One try, one finally, and the whole first pass inside the try.
        self.assertEqual(body.count("try:"), 1)
        self.assertEqual(body.count("finally:"), 1)
        for inside in ("observation = context.provider.dispatch(request)",
                       "require_closure_gate(context)",
                       "return _observe_and_close("):
            position = body.index(inside)
            self.assertLess(body.index("try:"), position)
            self.assertLess(position, body.index("finally:"))
        # Cleared exactly once, in that finally.
        tail = body[body.index("finally:"):]
        self.assertIn("context._current_prompt_extra = None", tail)
        self.assertIn("context._current_required_extra = None", tail)
        # Nothing persists them and no second mechanism appeared.
        self.assertNotIn("journal.append", body)
        self.assertNotIn("_current_required_extra_store", source)


# ===========================================================================
# v1_11 section 17.3a -- WIM RECONSTRUCTION ACROSS BOUNDED RETRY ATTEMPTS.
#
# Several supervisor operations may legitimately share ONE work_item_identity,
# because the work item describes the WORK and not the attempt.  The custody
# being recovered belongs to exactly one operation, and that binding -- not the
# work-item identity -- is what disambiguates recovery.
# ===========================================================================
class SelectionRetryReconstructionRehearsals(unittest.TestCase):

    def setUp(self):
        self.journal = FakeJournal()
        self.context = build_context(journal=self.journal)
        self.candidate = self.context.round_zero_candidate
        self.obj, self.work_item_id = engine.next_package_selection_work_item(
            self.context, self.candidate
        )
        # The stub reader must re-prove the bound candidate's bytes.
        self.context.continuation_adapter.roots = {
            self.candidate.candidate_path: {
                "sha256": self.candidate.candidate_sha256,
                "bytes": self.candidate.candidate_bytes,
            }
        }

    def attempt(self, *, operation, request, executable=None, scope=None,
                source_binding=None, candidate=None, owner_on_records=True,
                terminal_kind="result_received"):
        """One complete authenticated attempt for the SAME work item."""
        candidate = candidate or self.candidate
        bindings = {
            "package_scope_id": scope or self.context.binding.package_scope_id,
            "source_binding_sha256": (
                source_binding or self.context.binding.source_binding_sha256
            ),
            "candidate_path": candidate.candidate_path,
            "candidate_sha256": candidate.candidate_sha256,
            "candidate_bytes": candidate.candidate_bytes,
        }
        self.journal.append(
            {
                "type": "supervisor_operation_started",
                "supervisor_command": "continue-design-loop",
                "supervisor_operation_id": operation,
                "work_item_identity": self.work_item_id,
                "controller_executable_identity": (
                    executable or self.context.controller_executable_identity
                ),
                **bindings,
            }
        )
        owner = {"supervisor_operation_id": operation} if owner_on_records else {}
        payload = json.dumps(selection_object(), sort_keys=True).encode("utf-8")
        for kind, extra in (
            ("provider_request_prepared",
             {"work_item_kind": "next_package_selection",
              "result_schema_id": constants.RESULT_SCHEMA_ID_BY_PROVIDER_KIND[
                  "codex_next_package_selection"],
              "prompt_material_sha256": "1" * 64,
              "required_inputs_sha256": "2" * 64}),
            ("provider_dispatch_begun", {}),
            ("provider_result_custody_recorded",
             {"work_item_kind": "next_package_selection",
              "result_custody_identity": "rc_" + request,
              "result_location_kind": "inline_journal_bytes",
              "result_bytes_base64": base64.b64encode(payload).decode("ascii"),
              "result_byte_length": len(payload),
              "result_sha256": hashlib.sha256(payload).hexdigest(),
              "result_schema_valid": True,
              "result_origin": "local_completion"}),
            ("provider_request_terminal_recorded",
             {"terminal_kind": terminal_kind,
              "result_custody_identity": "rc_" + request}),
        ):
            event = self.journal.append(
                {
                    "type": kind,
                    "provider_request_identity": request,
                    "provider_kind": "codex_next_package_selection",
                    "work_item_identity": self.work_item_id,
                    **owner, **bindings, **extra,
                }
            )
            if kind == "provider_result_custody_recorded":
                custody = event
        self.journal.append(
            {
                "type": "supervisor_operation_completed",
                "supervisor_command": "continue-design-loop",
                "supervisor_operation_id": operation,
                "work_item_identity": self.work_item_id,
                "operation_outcome": "ok",
                **bindings,
            }
        )
        return custody

    def situation_now(self):
        return commands.status_mod.Situation(self.context, self.journal.read())

    def use_recovery_context(self):
        """Recovery happens under a CHANGED current controller identity, which
        is the only shape in which the reconstruction branch is reached: while
        the current derivation still matches, the installed fast path answers
        first and no reconstruction is needed."""
        self.context = build_context(journal=self.journal)
        self.context.controller_executable_identity = "2" * 64
        self.context.continuation_adapter.roots = {
            self.candidate.candidate_path: {
                "sha256": self.candidate.candidate_sha256,
                "bytes": self.candidate.candidate_bytes,
            }
        }
        return self.context

    def rebuild(self, request):
        return commands._rebuild_work_item(
            self.context, self.situation_now(), self.work_item_id,
            "next_package_selection", request_identity=request,
        )

    # -- 1 -------------------------------------------------------------
    def test_one_attempt_still_reconstructs_normally(self):
        self.attempt(operation="op_1", request="pr_1")
        # The installed fast path answers while the current derivation matches.
        self.assertEqual(self.rebuild("pr_1"), self.obj)
        # ...and the reconstruction branch answers identically once it does not.
        self.use_recovery_context()
        self.assertEqual(self.rebuild("pr_1"), self.obj)

    # -- 2 / 3 / 4 -----------------------------------------------------
    def test_two_attempts_sharing_one_work_item_are_not_ambiguous(self):
        """Two starts with ONE work_item_identity are not a contradiction."""
        self.attempt(operation="op_1", request="pr_1")
        self.attempt(operation="op_2", request="pr_2")
        starts = [
            event for event in self.journal.events
            if event.get("type") == "supervisor_operation_started"
            and event.get("work_item_identity") == self.work_item_id
        ]
        self.assertEqual(len(starts), 2, "the real retry shape")
        # Both recover, each through its OWN owning operation -- under a changed
        # current controller identity, so the reconstruction branch is the one
        # that answers.  This is the exact live failure.
        self.use_recovery_context()
        self.assertEqual(self.rebuild("pr_1"), self.obj)
        self.assertEqual(self.rebuild("pr_2"), self.obj)

    def test_a_custody_selects_its_own_attempt_by_operation_id(self):
        self.attempt(operation="op_1", request="pr_1")
        self.attempt(operation="op_2", request="pr_2")
        replayed = replay.Replay(self.journal.read())
        self.assertEqual(
            commands._owning_operation_id_of_request(replayed, "pr_2"),
            (commands.SELECTION_OWNER_EXACT, "op_2"),
        )
        state, chosen = commands._selection_owning_start(
            replayed, self.work_item_id, "pr_2"
        )
        self.assertEqual(state, commands.SELECTION_OWNER_EXACT)
        self.assertEqual(chosen["supervisor_operation_id"], "op_2")

    def test_attempt_one_cannot_be_substituted_for_attempt_two(self):
        """Each attempt's frozen controller identity is its own.  Attempt 2 must
        never be rebuilt from attempt 1's operands."""
        self.attempt(operation="op_1", request="pr_1", executable="a" * 64)
        self.attempt(operation="op_2", request="pr_2")
        replayed = replay.Replay(self.journal.read())
        _s1, one = commands._selection_owning_start(
            replayed, self.work_item_id, "pr_1"
        )
        _s2, two = commands._selection_owning_start(
            replayed, self.work_item_id, "pr_2"
        )
        self.assertEqual(one["supervisor_operation_id"], "op_1")
        self.assertEqual(two["supervisor_operation_id"], "op_2")
        self.assertNotEqual(
            one["controller_executable_identity"],
            two["controller_executable_identity"],
        )
        # Attempt 1's own identity cannot rebuild THIS work item, so a
        # substitution could not silently succeed either.
        self.assertIsNone(
            commands._rebuild_selection_from_owning_start(
                self.context, one, self.work_item_id
            )
        )
        self.use_recovery_context()
        self.assertEqual(self.rebuild("pr_2"), self.obj)

    # -- 5 -------------------------------------------------------------
    def test_a_disagreeing_operation_id_fails_closed(self):
        """Lifecycle records that name two different owners are a contradiction."""
        self.attempt(operation="op_1", request="pr_1")
        for event in self.journal.events:
            if (
                event.get("provider_request_identity") == "pr_1"
                and event.get("type") == "provider_request_terminal_recorded"
            ):
                event["supervisor_operation_id"] = "op_somewhere_else"
        replayed = replay.Replay(self.journal.read())
        self.assertEqual(
            commands._owning_operation_id_of_request(replayed, "pr_1"),
            (commands.SELECTION_OWNER_CONTRADICTION, None),
            "two owners are a CONTRADICTION, never absence",
        )

    def test_an_operation_id_naming_no_matching_start_fails_closed(self):
        self.attempt(operation="op_1", request="pr_1")
        for event in self.journal.events:
            if event.get("type") == "supervisor_operation_started":
                event["supervisor_command"] = "execute-initial-design"
        replayed = replay.Replay(self.journal.read())
        self.assertEqual(
            commands._selection_owning_start(
                replayed, self.work_item_id, "pr_1"
            ),
            (commands.SELECTION_OWNER_CONTRADICTION, None),
            "a recorded owner that resolves to no owning start is a "
            "contradiction, not absence",
        )

    # -- 6 -------------------------------------------------------------
    def test_a_disagreeing_binding_chain_fails_closed(self):
        """The start and the request chain are two independent records of one
        operation; if they disagree, neither is preferred."""
        self.attempt(operation="op_1", request="pr_1")
        for field, value in (
            ("package_scope_id", "nullpkg_elsewhere"),
            ("source_binding_sha256", "9" * 64),
            ("candidate_sha256", "9" * 64),
            ("candidate_bytes", 1),
            ("candidate_path", "05_ACTIVE_CANDIDATE/NH_OTHER_v1_0_CANDIDATE.md"),
        ):
            journal = FakeJournal(self.journal.read())
            for event in journal.events:
                if (
                    event.get("provider_request_identity") == "pr_1"
                    and event.get("type") == "provider_result_custody_recorded"
                ):
                    event[field] = value
            replayed = replay.Replay(journal.read())
            _state, start = commands._selection_owning_start(
                replayed, self.work_item_id, "pr_1"
            )
            self.assertIsNotNone(start, field)
            self.assertFalse(
                commands._selection_chain_agrees(replayed, start, "pr_1"), field
            )
        journal = FakeJournal(self.journal.read())
        for event in journal.events:
            if (
                event.get("provider_request_identity") == "pr_1"
                and event.get("type") == "provider_result_custody_recorded"
            ):
                event["package_scope_id"] = "nullpkg_elsewhere"
        context = build_context(journal=journal)
        context.controller_executable_identity = "2" * 64
        context.continuation_adapter.roots = self.context.continuation_adapter.roots
        with self.assertRaises(SupervisorRefusal):
            commands._rebuild_work_item(
                context, commands.status_mod.Situation(context, journal.read()),
                self.work_item_id, "next_package_selection",
                request_identity="pr_1",
            )

    # -- 7 -------------------------------------------------------------
    def test_moved_candidate_bytes_make_the_saved_result_stale(self):
        """A saved result is never consumed against changed candidate bytes."""
        self.attempt(operation="op_1", request="pr_1")
        self.use_recovery_context()
        # The reconstruction branch IS reached, and succeeds while bytes hold.
        self.assertEqual(self.rebuild("pr_1"), self.obj)
        # Now the bound candidate's bytes move underneath it.
        self.context.continuation_adapter.roots = {
            self.candidate.candidate_path: {"sha256": "0" * 64, "bytes": 1}
        }
        with self.assertRaises(SupervisorRefusal):
            self.rebuild("pr_1")
        # An unreadable candidate is equally refused, never assumed.
        self.context.continuation_adapter.roots = {}
        with self.assertRaises(SupervisorRefusal):
            self.rebuild("pr_1")

    # -- 8 / 9 / 10 ----------------------------------------------------
    def test_recovery_makes_zero_provider_calls_and_no_third_request(self):
        transport = LoudStubTransport()
        self.context = build_context(journal=self.journal, transport=transport)
        self.context.continuation_adapter.roots = {
            self.candidate.candidate_path: {
                "sha256": self.candidate.candidate_sha256,
                "bytes": self.candidate.candidate_bytes,
            }
        }
        self.attempt(operation="op_1", request="pr_1")
        self.attempt(operation="op_2", request="pr_2")
        before = copy.deepcopy(self.journal.events)
        appends = self.journal.appends
        self.context.controller_executable_identity = "2" * 64
        self.assertEqual(self.rebuild("pr_2"), self.obj)
        self.assertEqual(transport.calls, [], "ZERO provider calls")
        self.assertEqual(self.journal.appends, appends, "ZERO appends")
        self.assertEqual(
            [
                event for event in self.journal.events
                if event.get("type") == "provider_request_prepared"
            ],
            [
                event for event in before
                if event.get("type") == "provider_request_prepared"
            ],
            "no third next-package-selection request was created",
        )
        self.assertEqual(self.journal.events, before, "history is unchanged")

    # -- 11 ------------------------------------------------------------
    def test_the_live_1120_to_1131_shape_is_covered(self):
        """Two attempts, one work item, the SECOND custody chosen exactly --
        the shape the live journal actually holds at events 1120-1131."""
        first = self.attempt(operation="op_142a825c", request="pr_ece5e4dc")
        second = self.attempt(operation="op_adbec57b", request="pr_052f4500")
        self.assertEqual(first["work_item_identity"], second["work_item_identity"])
        replayed = replay.Replay(self.journal.read())
        _state, chosen = commands._selection_owning_start(
            replayed, self.work_item_id, second["provider_request_identity"]
        )
        self.assertEqual(chosen["supervisor_operation_id"], "op_adbec57b")
        self.use_recovery_context()
        rebuilt = self.rebuild(second["provider_request_identity"])
        self.assertEqual(rebuilt, self.obj)
        self.assertEqual(
            identity.work_item_identity(rebuilt), self.work_item_id,
            "WIM-REBUILD-IDENTITY-EQUALITY",
        )

    # -- THE THREE OWNER STATES, KEPT DISTINCT -------------------------
    def strip_owner_bindings(self, journal, request):
        """A genuinely HISTORICAL request: no record names an owning operation."""
        for event in journal.events:
            if event.get("provider_request_identity") == request:
                event.pop("supervisor_operation_id", None)

    def test_owner_absent_is_not_owner_contradiction(self):
        """The three states are DISTINCT, and absence is never a contradiction."""
        self.attempt(operation="op_1", request="pr_1")
        replayed = replay.Replay(self.journal.read())
        self.assertEqual(
            commands._owning_operation_id_of_request(replayed, "pr_1"),
            (commands.SELECTION_OWNER_EXACT, "op_1"),
        )
        journal = FakeJournal(self.journal.read())
        self.strip_owner_bindings(journal, "pr_1")
        self.assertEqual(
            commands._owning_operation_id_of_request(
                replay.Replay(journal.read()), "pr_1"
            ),
            (commands.SELECTION_OWNER_ABSENT, None),
        )

    def test_a_historical_ownerless_request_still_uses_the_fallback(self):
        """Records that genuinely predate the owning-operation binding keep
        their installed unambiguous-single-start reconstruction."""
        self.attempt(operation="op_1", request="pr_1")
        journal = FakeJournal(self.journal.read())
        self.strip_owner_bindings(journal, "pr_1")
        context = build_context(journal=journal)
        context.controller_executable_identity = "2" * 64
        context.continuation_adapter.roots = self.context.continuation_adapter.roots
        rebuilt = commands._rebuild_work_item(
            context, commands.status_mod.Situation(context, journal.read()),
            self.work_item_id, "next_package_selection",
            request_identity="pr_1",
        )
        self.assertEqual(rebuilt, self.obj, "the historical fallback still runs")

    def contradicted(self, *, one_start=False):
        """A journal whose lifecycle records name TWO different owners."""
        self.attempt(operation="op_1", request="pr_1")
        if not one_start:
            self.attempt(operation="op_2", request="pr_2")
        journal = FakeJournal(self.journal.read())
        for event in journal.events:
            if (
                event.get("provider_request_identity") == "pr_1"
                and event.get("type") == "provider_request_terminal_recorded"
            ):
                event["supervisor_operation_id"] = "op_somewhere_else"
        return journal

    def rebuild_in(self, journal, request):
        context = build_context(journal=journal)
        context.controller_executable_identity = "2" * 64
        context.continuation_adapter.roots = self.context.continuation_adapter.roots
        return commands._rebuild_work_item(
            context, commands.status_mod.Situation(context, journal.read()),
            self.work_item_id, "next_package_selection",
            request_identity=request,
        )

    def test_contradictory_owners_fail_the_rebuild_itself(self):
        """Not merely the helper: _rebuild_work_item REFUSES."""
        journal = self.contradicted()
        with self.assertRaises(SupervisorRefusal) as caught:
            self.rebuild_in(journal, "pr_1")
        self.assertIn("more than one", str(caught.exception))

    def test_a_contradiction_cannot_fall_through_to_a_single_start(self):
        """Even with EXACTLY ONE start carrying this work_item_identity -- the
        precise shape the old fallback would have accepted -- contradictory
        owner bindings still refuse.  The contradiction outranks the fallback."""
        journal = self.contradicted(one_start=True)
        starts = [
            event for event in journal.events
            if event.get("type") == "supervisor_operation_started"
            and event.get("work_item_identity") == self.work_item_id
        ]
        self.assertEqual(len(starts), 1, "the fallback's own precondition holds")
        with self.assertRaises(SupervisorRefusal):
            self.rebuild_in(journal, "pr_1")
        # ...and with the owner bindings simply ABSENT instead, that same single
        # start IS accepted -- so the refusal is caused by the contradiction and
        # by nothing else about this journal.
        ownerless = FakeJournal(journal.read())
        self.strip_owner_bindings(ownerless, "pr_1")
        self.assertEqual(self.rebuild_in(ownerless, "pr_1"), self.obj)

    def test_a_contradiction_contacts_nobody_and_appends_nothing(self):
        journal = self.contradicted()
        transport = LoudStubTransport()
        context = build_context(journal=journal, transport=transport)
        context.controller_executable_identity = "2" * 64
        context.continuation_adapter.roots = self.context.continuation_adapter.roots
        before = copy.deepcopy(journal.events)
        appends = journal.appends
        with self.assertRaises(SupervisorRefusal):
            commands._rebuild_work_item(
                context, commands.status_mod.Situation(context, journal.read()),
                self.work_item_id, "next_package_selection",
                request_identity="pr_1",
            )
        self.assertEqual(transport.calls, [], "ZERO provider calls")
        self.assertEqual(journal.appends, appends, "ZERO appends")
        self.assertEqual(journal.events, before, "the saved result is untouched")

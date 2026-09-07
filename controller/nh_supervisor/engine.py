#!/usr/bin/env python3
"""The controller-side supervisor engine.

This module owns the authenticated events, the identities, the operation
envelope and its two transaction boundaries, the provider write-ahead / custody
/ terminal sequence, the dependency classification, and every replay decision.
Provider CONTACT is injected; nothing else is.
"""

from __future__ import annotations

import base64
import os
import stat
from dataclasses import dataclass, field
from typing import Any, Callable

from . import capability, classify, constants, dependency, provider as provider_mod
from . import replay as replay_mod
from . import schema
from .canonical import canonical_json, is_hex64, sha256_hex, strict_json_loads
from .canonical import DuplicateJsonKeyError, NonCanonicalKeyError
from .identity import (
    IdentityError,
    batch_triple,
    derive,
    dependency_identity,
    work_item_identity,
)
from .journal import JournalSchemaError
from .lease import (
    RESULT_STORE_BASENAME,
    boot_id_sha256,
    in_flight_closure_append_gate,
    new_work_start_gate,
    read_process_start_ticks,
)


class SupervisorRefusal(RuntimeError):
    """The command refuses and appends nothing at all."""

    def __init__(self, message, *, workflow_state="SAFETY_HOLD", recovery_outcome=None):
        super().__init__(message)
        self.workflow_state = workflow_state
        self.recovery_outcome = recovery_outcome


@dataclass
class PackageBinding:
    """The controller's own proved package and source facts.

    section 8.8 section 7 SBC-ONE-OWNER-PER-FIELD -- EVERY FIELD HAS EXACTLY ONE
    OWNER.  No field has two.  A reader that wants a different epoch of the
    same fact reads a DIFFERENT FIELD; it never reinterprets this one.  The
    FIELD SET IS UNCHANGED by section 8.8; only the ownership is stated here.

    **IA -- IMMUTABLE, ANCHOR-DERIVED.**  From ``anchor_validation(S)``, and
    they NEVER move (SBC-ANCHOR-IMMOVABLE, section 5.2):

      ``package_key`` · ``package_scope_id`` · ``package_id`` ·
      ``scope_root_path`` · ``branch`` · ``head_sha`` ·
      ``source_binding_sha256`` · ``terminal_chain_sha256``

    ``branch``, ``head_sha``, ``source_binding_sha256`` and
    ``terminal_chain_sha256`` are **CHAIN / ANCHOR SOURCE IDENTITY**
    (SBC-ANCHOR-FIELDS-ARE-CHAIN-IDENTITY).  They are NOT, and must never be
    reported as, "the current source".  ``_base_work_item()`` and every
    supervisor append stamp them onto the events they write, and
    ``authenticated_candidate_custody()`` REFUSES any chain step that does not
    carry the anchor's values -- so moving them would make the authenticated
    state unreplayable and fail every supervisor command closed.  A reader that
    wants current source reads ``package_source_currentness(scope)`` instead.

    **EV -- CURRENT / EFFECTIVE-VALIDATION-DERIVED.**  From
    ``effective_validation(S)`` -- the latest complete, enumeration-complete,
    authenticated validation set of that scope:

      ``source_manifest_sha256`` · ``required_source_paths`` ·
      ``validation_set_id``

    These describe WHAT WAS CHECKED and BY WHICH VALIDATION.  The Piece-3 gate
    already decides on the effective validation, so leaving them on the anchor
    made the authorization name a different validation set than the gate was
    deciding about.

    **JR -- CURRENT JOURNAL / REPLAY-DERIVED.**  ``settled_decision_binding_sha256``
    (derived per scope on every boundary) · ``piece3_standing_sha256`` (the
    GLOBAL interview standing chain, not a package source fact) ·
    ``coverage_review_event_seq``.

    **NB -- NOT A PACKAGE SOURCE FACT.**  ``routed_signal_refs`` belongs to the
    work item; the current-package binding carries ``()`` and it is never given
    a source epoch.

    NO FIELD IS MOVED FOR SYMMETRY.  Where a scope holds exactly one validation
    set, EV IS the anchor and every field is what the installed code already
    produced.
    """

    package_key: str
    package_scope_id: str
    branch: str
    head_sha: str
    source_binding_sha256: str
    settled_decision_binding_sha256: str
    source_manifest_sha256: str
    terminal_chain_sha256: str
    required_source_paths: frozenset = frozenset()
    validation_set_id: str | None = None
    coverage_review_event_seq: int | None = None
    piece3_standing_sha256: str | None = None
    routed_signal_refs: tuple = ()
    # Section 15: both remain OPEN -- NONE.  This specification never fills them.
    package_id: Any = None
    # Authenticated in the Piece-3 package-source binding.  It is deliberately
    # absent from package_source() and therefore changes no event or identity.
    scope_root_path: str | None = None

    def package_source(self, standing_before_sha256):
        return {
            "package_key": self.package_key,
            "package_scope_id": self.package_scope_id,
            "package_id": self.package_id,
            "branch": self.branch,
            "head_sha": self.head_sha,
            "source_binding_sha256": self.source_binding_sha256,
            "standing_before_sha256": standing_before_sha256,
        }


@dataclass
class CandidateState:
    candidate_path: str
    candidate_sha256: str
    candidate_bytes: int
    parent_candidate_path: str | None = None
    parent_candidate_sha256: str | None = None
    parent_candidate_bytes: int | None = None


@dataclass
class ReviewSignalAdapter:
    """The already-loaded Piece-3 validators/router, dependency-injected."""

    validate_source_paths: Callable[[Any, str, list], Any]
    validate_review_signal: Callable[[Any, str, list, list], Any]
    record_review_signal: Callable[..., Any]


@dataclass
class ContinuationAdapter:
    """v1_8 -- the ALREADY-INSTALLED selection / preparation / Piece-3 code,
    dependency-injected exactly as ``ReviewSignalAdapter`` already is.

    Every member below is an INSTALLED nh_loop function.  Nothing here is a
    second validator, a second prompt builder, a second prepared-task engine or
    a second Piece-3 system (PROMPT-NO-SECOND-BUILDER, PREP-NO-PARALLEL-ENGINE,
    T2-NO-SECOND-PIECE3-SYSTEM).  This adapter only makes them reachable from
    the supervisor command layer.
    """

    # -- installed model-result validators (exact-key contracts) ------------
    validate_next_package_analysis: Callable[..., Any] = None
    validate_prepared_task: Callable[..., Any] = None
    validate_question_validation_payload: Callable[..., Any] = None
    validate_question_coverage_review: Callable[..., Any] = None
    # -- installed controller-owned resolution ------------------------------
    resolve_required_files: Callable[..., Any] = None
    resolve_repo_source_path: Callable[..., Any] = None
    check_required_source_coverage: Callable[..., Any] = None
    interview_package_scope_id: Callable[..., Any] = None
    interview_package_key: Callable[..., Any] = None
    is_new_candidate_path: Callable[..., Any] = None
    source_root_identity: Callable[..., Any] = None
    current_source_binding: Callable[..., Any] = None
    current_source_byte_snapshot: Callable[..., Any] = None
    next_package_action_by_classification: Any = None
    # -- installed prompt builders (PROMPT-BY-KIND) -------------------------
    next_package_prompt: Callable[..., Any] = None
    build_prepare_task_prompt: Callable[..., Any] = None
    build_question_validation_prompt: Callable[..., Any] = None
    build_question_coverage_review_prompt: Callable[..., Any] = None
    # -- narrow append-only recovery classification ------------------------
    interrupted_invalid_validation_effect: Callable[..., Any] = None
    # -- installed Piece-3 parts A and B (extracted, never duplicated) ------
    piece3_precall_requirement: Callable[..., Any] = None
    piece3_commit: Callable[..., Any] = None
    save_piece3_prepared_work: Callable[..., Any] = None
    # -- installed routed-signal recorder (T1 question route) ---------------
    record_review_signal: Callable[..., Any] = None
    # -- installed task-preparation stage two (extracted, never duplicated) -
    run_design_task_preparation: Callable[..., Any] = None
    # -- installed section 8.2 / 8.3 / 8.4 establishment derivation ---------
    # CPB-SINGLE-TRANSITION needs to know which scopes are ESTABLISHED, and it
    # must decide that with the SAME installed machinery the binding rule uses.
    # A weaker parallel definition of "established" is exactly what this must
    # not become, so these are the installed functions themselves.
    scope_anchor_validations: Callable[..., Any] = None
    scope_is_established: Callable[..., Any] = None
    # -- installed transition-binding construction --------------------------
    build_transition_context: Callable[..., Any] = None
    settled_decision_binding: Callable[..., Any] = None
    interview_clearance: Callable[..., Any] = None
    # -- accepted role-split v1_6: the two installed nh_loop functions the
    #    provider-free local T3 needs and that commands.py cannot otherwise
    #    reach.  DECLARATION ONLY: both bodies live in nh_loop beside the
    #    installed readers and allocators they reuse, exactly as every other
    #    member of this adapter does (PREP-NO-PARALLEL-ENGINE).  No second
    #    context mechanism and no ad-hoc attribute seam is created.
    build_local_task_envelope: Callable[..., Any] = None
    derive_initial_target_path: Callable[..., Any] = None


@dataclass
class SupervisorContext:
    journal: Any
    binding: PackageBinding
    controller_executable_identity: str
    endpoint_binding: dict
    capability_reader: Callable[[str, str], Any]
    provider: Any = field(default_factory=provider_mod.RefusingProviderTransport)
    lease: Any = None
    lease_binding: dict | None = None
    own_run_id: str | None = None
    clock: Callable[[], float] = None
    state_dir: str | None = None
    candidate_dir: str | None = None
    accepted_ness_decision_records: Callable[[], list] = None
    accepted_ness_unlock_records: Callable[[], list] = None
    scheduling: Any = None
    blocking_finding_refs_override: tuple | None = None
    # The unique round-zero tail of Section 3: the selected initial candidate.
    round_zero_candidate: Any = None
    # The parent candidate payload, used only for the K8 byte-identity check.
    parent_candidate_payload: bytes | None = None
    review_signal_adapter: ReviewSignalAdapter | None = None
    interview_projection_reader: Callable[[], dict] | None = None
    interview_gate_reader: Callable[[str], dict] | None = None
    # AUDIT REPAIR 2026-09-02 (write boundary).  The controller-owned re-proof
    # run by _promote_candidate() immediately before and after the ONE file
    # creation in the governed repository: branch, frozen HEAD, no tracked
    # modification, controlled new candidate path, the package's interview
    # clearance, and the post-write repository shape.  Called with a facts
    # dict and returns a list of refusal reasons (empty = proved).  A context
    # without it cannot write: absence is a stop, never an all-clear.
    write_boundary_prover: Callable[[dict], list] | None = None
    # v1_8 -- the installed continuation code, dependency-injected.
    continuation_adapter: ContinuationAdapter | None = None
    # v1_8 section 8.9 -- which transition binding this context carries, or
    # None for the ordinary current-package binding.  It is NEVER returned by
    # supervisor-status, never fed into status._project(), and never shown as
    # the current package (TB-NOT-CURRENT, TB-PREVALIDATION-NOT-CURRENT).
    transition_binding_kind: str | None = None
    # v1_8 sections 6.3 / 8.9 -- THE CONTROL PACKAGE, when this context is a
    # TRANSITION context.
    #
    # P remains the CURRENT ESTABLISHED package while Q is in transition, and
    # two different questions must not be answered from one binding:
    #
    #   * "is the acceptance still freshly proved?"  is about P, and is
    #     answered from P's own context;
    #   * "which package is this work for?"          is about Q, and is
    #     answered from context.binding.
    #
    # A Q-scoped replay correctly contains NO P acceptance event, so asking a
    # Q context to prove P's acceptance could only ever fail.  Nothing is
    # copied between them: Q never becomes accepted, and P never becomes the
    # work binding.
    #
    # It also carries the ONE live worker lease, which stays P's throughout the
    # transition: Q is the work binding, not a second concurrency authority.
    control_context: Any = None
    # v1_8 section 17.2 -- the freshly derived transition facts this context
    # was built for.  Derived, never stored, never carried from an earlier
    # loop-status response (TB-CUSTODY-NO-STALE-REPORT).
    transition_facts: Any = None
    # The work-item object the running command is bound to.  Set by the command,
    # read by the admission checks, and never read from a caller.
    _current_work_item_obj: Any = None
    # The exact controller-owned extra prompt inventory for the current
    # dispatch.  It is transient, never journal authority, and lets the
    # production transport render the same material whose digest was bound in
    # provider_request_prepared.
    _current_prompt_extra: Any = None
    # v1_8 section 9.5c EXTRA-INPUTS-SEAM -- the exact controller-owned extra
    # required-input inventory for the current dispatch.  Transient, never
    # journal authority, and deterministically reconstructed on restart so
    # _supervisor_provider_material() can recompute required_inputs_sha256 and
    # refuse before one byte leaves the machine.
    _current_required_extra: Any = None
    # v1_8 section 14.5 I10 -- the EXACT admitted initial-design payload,
    # carried from admission to promotion so nothing is re-derived,
    # re-encoded, normalised or regenerated in between.
    _admitted_initial_design_payload: Any = None

    def now(self):
        if self.clock is None:
            import time

            return time.time()
        return self.clock()

    def capability_record(self, provider_kind, endpoint=None):
        endpoint = endpoint or self.endpoint_binding.get(provider_kind)
        if endpoint is None:
            return None, None
        record, _default = capability.resolve_record(
            self.capability_reader(provider_kind, endpoint), provider_kind, endpoint
        )
        return record, endpoint

    def capability_snapshot(self):
        return capability.build_capability_snapshot(
            self.endpoint_binding, self.capability_reader
        )

    def result_store_dir(self):
        if self.state_dir is None:
            return None
        return os.path.join(self.state_dir, RESULT_STORE_BASENAME)


# ---------------------------------------------------------------------------
# Section 11.1 -- the operation envelope.
# ---------------------------------------------------------------------------
ENVELOPE_FIELD_ORDER = (
    "supervisor_command",
    "controller_executable_identity",
    "package_scope_id",
    "source_binding_sha256",
    "candidate_path",
    "candidate_sha256",
    "candidate_bytes",
    "work_item_identity",
    "pre_state_sha256",
    "unlock_evidence_kind",
    "unlock_evidence_identity",
    "unlock_evidence_sha256",
    "input_envelope_sha256",
    "supervisor_operation_id",
)

ENVELOPE_DIGEST_FIELDS = ENVELOPE_FIELD_ORDER[:-2]


def input_envelope_sha256(envelope):
    """The canonical digest of every preceding envelope field, in field order."""
    material = [[key, envelope[key]] for key in ENVELOPE_DIGEST_FIELDS]
    return sha256_hex(canonical_json(material))


def supervisor_operation_id(envelope):
    return derive(
        "supervisor_operation_id",
        {
            "supervisor_command": envelope["supervisor_command"],
            "controller_executable_identity": envelope["controller_executable_identity"],
            "package_scope_id": envelope["package_scope_id"],
            "source_binding_sha256": envelope["source_binding_sha256"],
            "candidate_path": envelope["candidate_path"],
            "candidate_sha256": envelope["candidate_sha256"],
            "candidate_bytes": envelope["candidate_bytes"],
            "work_item_identity": envelope["work_item_identity"],
            "pre_state_sha256": envelope["pre_state_sha256"],
            "input_envelope_sha256": envelope["input_envelope_sha256"],
            "unlock_evidence_kind": envelope["unlock_evidence_kind"],
            "unlock_evidence_identity": envelope["unlock_evidence_identity"],
            "unlock_evidence_sha256": envelope["unlock_evidence_sha256"],
        },
    )


def complete_envelope(envelope):
    """Fill the two derived envelope fields, in the one permitted order."""
    filled = dict(envelope)
    filled["input_envelope_sha256"] = input_envelope_sha256(filled)
    filled["supervisor_operation_id"] = supervisor_operation_id(filled)
    return filled


def caller_triple_is_all_null(request):
    """Section 4.11 (a): every caller supplies all three as present and null."""
    for key in ("unlock_evidence_kind", "unlock_evidence_identity", "unlock_evidence_sha256"):
        if key not in request:
            return False
        if request[key] is not None:
            return False
    return True


# ---------------------------------------------------------------------------
# The work-item builders.  Every one goes through the Section 4.4 matrix.
# ---------------------------------------------------------------------------
def _base_work_item(context, candidate, kind):
    return {
        "work_item_kind": kind,
        "controller_executable_identity": context.controller_executable_identity,
        "package_scope_id": context.binding.package_scope_id,
        "source_binding_sha256": context.binding.source_binding_sha256,
        "candidate_path": candidate.candidate_path,
        "candidate_sha256": candidate.candidate_sha256,
        "candidate_bytes": candidate.candidate_bytes,
        "blocking_finding_refs": [],
        "audit_identity": None,
        "checkpoint_identity": None,
        "diagnosis_event_sha256": None,
        "diagnosis_strategy_sha256": None,
        "strategy_novelty_key": None,
        "correction_specification_sha256": None,
        "target_candidate_path": None,
        "authorized_next_lifetime_round": None,
        "authorized_batch_number": None,
        "authorized_round_in_batch": None,
        "routed_signal_refs": [],
        "validation_set_id": None,
        "piece3_standing_sha256": None,
    }


def design_audit_work_item(context, candidate):
    obj = _base_work_item(context, candidate, "design_audit")
    return obj, work_item_identity(obj)


def acceptance_explanation_content_work_item(context, candidate):
    """Section 14 Phase A step A2 -- ONE bounded preparation work item.

    It binds the exact candidate whose prose is being prepared and nothing
    else.  It authorises no candidate write, no correction round, no audit
    verdict, no PASS and no acceptance: the only thing its result may become
    is the content-stage explanation record's parts 1-6, and the controller
    validates and digests those itself before any of them is written.
    """
    obj = _base_work_item(context, candidate, "acceptance_explanation_content")
    return obj, work_item_identity(obj)


def correction_diagnosis_work_item(
    context, candidate, blocking_finding_refs, audit_identity, checkpoint_identity, trigger_type
):
    obj = _base_work_item(context, candidate, "correction_diagnosis")
    obj["blocking_finding_refs"] = sorted(set(blocking_finding_refs))
    obj["audit_identity"] = audit_identity
    obj["checkpoint_identity"] = checkpoint_identity if trigger_type == "exhausted_batch" else None
    variant = "exhausted_batch" if trigger_type == "exhausted_batch" else "no_progress"
    return obj, work_item_identity(obj, variant)


def correction_apply_work_item(
    context,
    candidate,
    *,
    blocking_finding_refs,
    audit_identity,
    checkpoint_identity,
    diagnosis_event_sha256,
    diagnosis_strategy_sha256,
    strategy_novelty_key,
    correction_specification_sha256,
    target_candidate_path,
    authorized_triple,
    variant,
):
    obj = _base_work_item(context, candidate, "correction_apply")
    obj["blocking_finding_refs"] = sorted(set(blocking_finding_refs))
    obj["audit_identity"] = audit_identity
    obj["checkpoint_identity"] = checkpoint_identity
    obj["diagnosis_event_sha256"] = diagnosis_event_sha256
    obj["diagnosis_strategy_sha256"] = diagnosis_strategy_sha256
    obj["strategy_novelty_key"] = strategy_novelty_key
    obj["correction_specification_sha256"] = correction_specification_sha256
    obj["target_candidate_path"] = target_candidate_path
    obj["authorized_next_lifetime_round"] = authorized_triple[0]
    obj["authorized_batch_number"] = authorized_triple[1]
    obj["authorized_round_in_batch"] = authorized_triple[2]
    return obj, work_item_identity(obj, variant)


def correction_specification_work_item(
    context, candidate, blocking_finding_refs, audit_identity, target_candidate_path, authorized_triple
):
    obj = _base_work_item(context, candidate, "correction_specification")
    obj["blocking_finding_refs"] = sorted(set(blocking_finding_refs))
    obj["audit_identity"] = audit_identity
    obj["target_candidate_path"] = target_candidate_path
    obj["authorized_next_lifetime_round"] = authorized_triple[0]
    obj["authorized_batch_number"] = authorized_triple[1]
    obj["authorized_round_in_batch"] = authorized_triple[2]
    return obj, work_item_identity(obj)


def change_explanation_work_item(
    context, candidate, blocking_finding_refs, audit_identity, correction_specification_sha256
):
    obj = _base_work_item(context, candidate, "change_explanation_review")
    obj["blocking_finding_refs"] = sorted(set(blocking_finding_refs))
    obj["audit_identity"] = audit_identity
    obj["correction_specification_sha256"] = correction_specification_sha256
    return obj, work_item_identity(obj)


def piece3_variant_from_state(kind, *, transition_active, scope_has_validation,
                              routed_signal_refs,
                              scope_validation_complete=True):
    """v1_8 section 12.3h PIECE3-VARIANT-FROM-STATE -- controller state ONLY.

    No caller variant.  No model variant.  No environment-variable semantic
    switch.  Returns the exact proved variant, or raises so the caller fails
    closed rather than guessing.

      is this a post-acceptance transition stage for the single in-transition
      scope?
          no   -> variant None            (installed route, unchanged)
          yes  -> does scope_Q have a durable validation_recorded?
                      no  -> does scope_Q hold genuine routed signals?
                                 no  -> A  first_package_validation_unrouted
                                 yes -> B  first_package_validation_routed
                      yes -> C  package_coverage_unrouted   (coverage stage)
                          or the installed routed row where routed signals stand
    """
    if not transition_active:
        return None
    routed = sorted(set(routed_signal_refs or ()))
    if kind == "question_validation":
        if scope_has_validation:
            # A later page of the same validation set may have no newly routed
            # signals.  Bind that truthful continuation only while the durable
            # inventory itself proves that more pages are still owed.  A
            # complete validation has retired the pre-validation binding and
            # must continue to use the installed post-validation route.
            if not routed and not scope_validation_complete:
                return constants.PIECE3_VARIANT_VALIDATION_CONTINUATION_UNROUTED
            return None
        return (
            constants.PIECE3_VARIANT_FIRST_ROUTED
            if routed
            else constants.PIECE3_VARIANT_FIRST_UNROUTED
        )
    if kind == "coverage_review":
        if not scope_has_validation:
            raise IdentityError(
                "a coverage review cannot precede the package's first "
                "validation: the variant is not provable and this fails closed"
            )
        if routed:
            # Genuine routed signals stand: the installed routed row governs.
            return None
        return constants.PIECE3_VARIANT_COVERAGE_UNROUTED
    raise IdentityError(
        "piece3 variant selection was asked about %r, which is not a Piece-3 "
        "work-item kind" % (kind,)
    )


def piece3_work_item(context, candidate, kind, *, variant=None,
                     transition_state=None):
    """One Piece-3 work item.

    v1_8 section 12.3g/12.3h.  The ordinary installed route is unchanged: with
    no transition_state the three Piece-3 fields still come from the binding
    and the variant resolves through the explicit ``(kind, None)`` row.

    Under a post-acceptance transition the three fields come from PROVED state
    rather than from a blind binding read, because a pre-validation binding
    legitimately carries a null ``validation_set_id`` and empty routed refs.
    No fake routed signal and no fake validation_set_id is ever manufactured
    (PIECE3-NO-FAKE-FIELDS).
    """
    obj = _base_work_item(context, candidate, kind)
    if transition_state is None:
        obj["routed_signal_refs"] = sorted(set(context.binding.routed_signal_refs))
        obj["validation_set_id"] = context.binding.validation_set_id
        obj["piece3_standing_sha256"] = context.binding.piece3_standing_sha256
        return obj, work_item_identity(obj, variant)

    proved_variant = piece3_variant_from_state(
        kind,
        transition_active=True,
        scope_has_validation=bool(transition_state.get("scope_has_validation")),
        routed_signal_refs=transition_state.get("routed_signal_refs") or (),
        scope_validation_complete=transition_state.get(
            "scope_validation_complete", True
        ),
    )
    if variant is not None and variant != proved_variant:
        raise IdentityError(
            "the supplied Piece-3 variant %r is not the variant controller "
            "state proves (%r): the caller may not choose it"
            % (variant, proved_variant)
        )
    obj["routed_signal_refs"] = sorted(set(transition_state.get("routed_signal_refs") or ()))
    obj["validation_set_id"] = transition_state.get("validation_set_id")
    obj["piece3_standing_sha256"] = transition_state.get("piece3_standing_sha256")
    return obj, work_item_identity(obj, proved_variant)


# ---------------------------------------------------------------------------
# v1_8 sections 9.5d / 13.6c / 14.5b -- the THREE continuation work-item
# builders.  Each is the ONE controller-owned builder for its kind and returns
# ``(obj, work_item_identity(obj))``.  There is NO ALTERNATE IDENTITY PATH:
# nothing else may construct these objects or derive these identities.
# ---------------------------------------------------------------------------
def next_package_selection_work_item(context, candidate):
    """WIM-SELECTION.  Bound candidate is P's candidate under P's binding.

    T1 runs from the terminal-accepted package (TB-NO-PREMATURE-Q), which is
    also why its identity can never collide with a T3 item bound to Q's root.
    """
    obj = _base_work_item(context, candidate, "next_package_selection")
    return obj, work_item_identity(obj)


def next_design_task_preparation_work_item(context, candidate):
    """WIM-PREPARATION.  Bound candidate is Q's proved source root.

    The admitted T1 selection, the selected root and scope, and the
    settled-decision material are bound through ``required_inputs_sha256``'s
    extra slot -- NOT through work-item fields that do not exist for them.
    """
    obj = _base_work_item(context, candidate, "next_design_task_preparation")
    return obj, work_item_identity(obj)


def initial_design_work_item(context, candidate, target_candidate_path):
    """WIM-INITIAL.  Bound candidate is Q's proved source root (the parent seed).

    ``target_candidate_path`` is the T3 controller-validated target, and
    INIT-ADMISSION I3 compares the produced path against it.
    """
    obj = _base_work_item(context, candidate, "initial_design")
    obj["target_candidate_path"] = target_candidate_path
    return obj, work_item_identity(obj)


# ---------------------------------------------------------------------------
# Prompt / required-input inventories.  Bounded, and never model output.
# ---------------------------------------------------------------------------
PROMPT_TEMPLATE_IDS = {
    "codex_design_audit": "NH_DESIGN_AUDIT_TEMPLATE_V1",
    "gpt_correction_specification": "NH_CORRECTION_SPECIFICATION_TEMPLATE_V1",
    "claude_correction": "NH_CLAUDE_CORRECTION_TEMPLATE_V1",
    "codex_correction_diagnosis": "NH_CORRECTION_DIAGNOSIS_TEMPLATE_V1",
    "codex_change_explanation_review": "NH_CHANGE_EXPLANATION_TEMPLATE_V1",
    "gpt_question_validation": "NH_QUESTION_VALIDATION_TEMPLATE_V1",
    "gpt_question_coverage_review": "NH_QUESTION_COVERAGE_TEMPLATE_V1",
    "claude_acceptance_explanation": "NH_ACCEPTANCE_EXPLANATION_CONTENT_TEMPLATE_V1",
    # v1_8 section 24.4 -- template map entries for the three new provider
    # kinds.  The BYTES these name are built by the INSTALLED builders
    # (PROMPT-BY-KIND, PROMPT-NO-SECOND-BUILDER); only the selection of which
    # builder runs is new.
    "codex_next_package_selection": "NH_NEXT_PACKAGE_SELECTION_TEMPLATE_V1",
    "codex_next_design_task_preparation": (
        "NH_NEXT_DESIGN_TASK_PREPARATION_TEMPLATE_V1"
    ),
    "claude_initial_design": "NH_CLAUDE_INITIAL_DESIGN_TEMPLATE_V1",
}


def prompt_material_inventory(provider_kind, work_item_obj, extra=None):
    """Return the literal Section 4.6 inventory before hashing it."""
    return {
        "template_identity": PROMPT_TEMPLATE_IDS[provider_kind],
        "controlled_instruction_ids": ["NH_CONTROLLER_INSTRUCTION_V1"],
        "candidate_path": work_item_obj["candidate_path"],
        "candidate_sha256": work_item_obj["candidate_sha256"],
        "candidate_bytes": work_item_obj["candidate_bytes"],
        "blocking_finding_refs": work_item_obj["blocking_finding_refs"],
        "target_candidate_path": work_item_obj["target_candidate_path"],
        "authorized_triple": [
            work_item_obj["authorized_next_lifetime_round"],
            work_item_obj["authorized_batch_number"],
            work_item_obj["authorized_round_in_batch"],
        ],
        "correction_specification_sha256": work_item_obj["correction_specification_sha256"],
        "routed_signal_refs": work_item_obj["routed_signal_refs"],
        "validation_set_id": work_item_obj["validation_set_id"],
        "piece3_standing_sha256": work_item_obj["piece3_standing_sha256"],
        "extra": extra or {},
    }


def prompt_material_sha256(provider_kind, work_item_obj, extra=None):
    inventory = prompt_material_inventory(provider_kind, work_item_obj, extra)
    return sha256_hex(canonical_json(["NH_PROMPT_MATERIAL_V1", inventory]))


def required_inputs_inventory(context, work_item_obj, extra=None):
    """Return the literal required-input inventory before hashing it."""
    return {
        "candidate_sha256": work_item_obj["candidate_sha256"],
        "candidate_bytes": work_item_obj["candidate_bytes"],
        "source_binding_sha256": context.binding.source_binding_sha256,
        "source_manifest_sha256": context.binding.source_manifest_sha256,
        "settled_decision_binding_sha256": context.binding.settled_decision_binding_sha256,
        "required_source_paths": sorted(context.binding.required_source_paths),
        "extra": extra or {},
    }


def required_inputs_sha256(context, work_item_obj, extra=None):
    inventory = required_inputs_inventory(context, work_item_obj, extra)
    return sha256_hex(canonical_json(["NH_REQUIRED_INPUTS_V1", inventory]))


# ---------------------------------------------------------------------------
# The operation transaction.
# ---------------------------------------------------------------------------
class Operation:
    """One supervisor operation: exactly one start and exactly one completion."""

    def __init__(self, context, envelope, work_item_obj=None):
        self.context = context
        self.envelope = envelope
        self.work_item_obj = work_item_obj
        self.started_event = None
        self.appended = []

    @property
    def operation_id(self):
        return self.envelope["supervisor_operation_id"]

    def _candidate_body(self, events):
        lifetime = replay_mod.Replay(events, self.context.binding.package_scope_id)
        triple = lifetime.current_batch_triple()
        return {
            "candidate_path": self.envelope["candidate_path"],
            "candidate_sha256": self.envelope["candidate_sha256"],
            "candidate_bytes": self.envelope["candidate_bytes"],
            "correction_round_lifetime": triple[0],
            "correction_batch_number": triple[1],
            "correction_round_in_batch": triple[2],
        }

    def start(self):
        """Append ``supervisor_operation_started`` before any other work."""
        events = self.context.journal.read()
        body = {"type": "supervisor_operation_started"}
        body.update(self.context.binding.package_source(_standing(events)))
        body.update(self._candidate_body(events))
        body.update(
            {
                "controller_executable_identity": self.envelope[
                    "controller_executable_identity"
                ],
                "supervisor_operation_id": self.envelope["supervisor_operation_id"],
                "supervisor_command": self.envelope["supervisor_command"],
                "work_item_identity": self.envelope["work_item_identity"],
                "pre_state_sha256": self.envelope["pre_state_sha256"],
                "input_envelope_sha256": self.envelope["input_envelope_sha256"],
                # Present JSON null: the invoked operation has not returned a
                # report yet.
                "controller_report_sha256": None,
                "unlock_evidence_kind": self.envelope["unlock_evidence_kind"],
                "unlock_evidence_identity": self.envelope["unlock_evidence_identity"],
                "unlock_evidence_sha256": self.envelope["unlock_evidence_sha256"],
            }
        )
        self.started_event = self.context.journal.append(body)
        self.appended.append(self.started_event)
        return self.started_event

    def append(self, event_type, body):
        events = self.context.journal.read()
        full = {"type": event_type}
        full.update(self.context.binding.package_source(_standing(events)))
        if schema.CANDIDATE <= schema.SUPERVISOR_EVENT_BODY_KEYS[event_type]:
            full.update(self._candidate_body(events))
        full.update(body)
        appended = self.context.journal.append(full)
        self.appended.append(appended)
        return appended

    def complete(self, outcome, *, dependency_slot=None, controller_returncode=0,
                 controller_report_sha256=None, retry_series_key=None,
                 acceptance_refusal_class=None, acceptance_offer_id=None,
                 acceptance_offer_binding_sha256=None):
        """Append ``supervisor_operation_completed`` at the pre-completion boundary.

        The three ``acceptance_*`` arguments are the Section 19 refusal carrier
        of the accepted acceptance-record design.  That design puts the refusal
        record on this ALREADY REGISTERED type at a new body version rather
        than on a second new event type, and the installed schema mechanism
        carries a different key set only at a different journal VERSION -- so
        at journal version 6 every completion carries these three keys, and an
        ordinary completion carries them as PRESENT JSON NULL.

        Present-null is the discipline this writer already uses for
        ``supervisor_started_event_seq`` when there is no start event.  It is
        used here for the same reason and in the same way: a key the schema
        requires is written as an honest null rather than omitted, and there is
        still exactly ONE writer of this record for the whole controller.
        """
        events = self.context.journal.read()
        slot = dependency_slot or schema.empty_dependency_slot()
        post_state = self._pre_completion_state_digest(events, slot)
        body = {"type": "supervisor_operation_completed"}
        body.update(self.context.binding.package_source(_standing(events)))
        body.update(self._candidate_body(events))
        body.update(slot)
        body.update(
            {
                "acceptance_refusal_class": acceptance_refusal_class,
                "acceptance_offer_id": acceptance_offer_id,
                "acceptance_offer_binding_sha256": acceptance_offer_binding_sha256,
            }
        )
        body.update(
            {
                "controller_executable_identity": self.envelope[
                    "controller_executable_identity"
                ],
                "supervisor_operation_id": self.envelope["supervisor_operation_id"],
                "supervisor_started_event_seq": (
                    self.started_event["event_seq"] if self.started_event else None
                ),
                "supervisor_command": self.envelope["supervisor_command"],
                "work_item_identity": self.envelope["work_item_identity"],
                "controller_returncode": controller_returncode,
                "controller_report_sha256": controller_report_sha256,
                "operation_outcome": outcome,
                "post_state_sha256": post_state,
                "retry_series_key": retry_series_key,
            }
        )
        appended = self.context.journal.append(body)
        self.appended.append(appended)
        return appended

    def _pre_completion_state_digest(self, events, slot):
        """Section 4.2 / 11.1 -- the PRE-COMPLETION projection digest.

        Taken after every substantive event of this operation is durable and
        immediately before this completion is appended, so its sequence and tail
        are the real ones of the event immediately preceding it.  A completion
        never hashes itself.
        """
        seq, tail = replay_mod.tail_identity(events)
        from .status import derive_workflow_projection

        projection_state = derive_workflow_projection(self.context, events)
        return replay_mod.state_binding_digest(
            replay_mod.state_binding_projection(
                controller_executable_identity=self.envelope[
                    "controller_executable_identity"
                ],
                package_scope_id=self.envelope["package_scope_id"],
                source_binding_sha256=self.envelope["source_binding_sha256"],
                candidate_path=self.envelope["candidate_path"],
                candidate_sha256=self.envelope["candidate_sha256"],
                candidate_bytes=self.envelope["candidate_bytes"],
                workflow_state=projection_state["workflow_state"],
                next_command=projection_state["next_command"],
                work_item_identity=self.envelope["work_item_identity"],
                dependency_identity=slot.get("dependency_identity"),
                authenticated_event_seq=seq,
                authenticated_tail_sha256=tail,
            )
        )


def _standing(events):
    """The replayed standing digest at the next event position.

    Supervisor events are Piece-3-standing neutral: their delta is the empty
    canonical delta, so the anchor they record is simply the running value.
    """
    chain = None
    for event in events:
        chain = sha256_hex(
            ("" if chain is None else chain) + "|" + canonical_json(_standing_delta(event))
        )
    return chain


def _standing_delta(event):
    kind = event.get("type")
    if kind in schema.SUPERVISOR_EVENT_TYPES:
        return {}
    if kind == "candidate_write_ahead_recorded":
        return {
            "t": "intent",
            "scope": event.get("package_scope_id"),
            "path": event.get("candidate_path"),
            "sha256": event.get("candidate_sha256"),
            "bytes": event.get("candidate_bytes"),
            "parent": event.get("parent_candidate_sha256"),
            "round": event.get("correction_round_lifetime", event.get("correction_round")),
            "origin": event.get("intent_origin"),
        }
    if kind == "candidate_custody_recorded":
        return {
            "t": "custody",
            "scope": event.get("package_scope_id"),
            "path": event.get("candidate_path"),
            "sha256": event.get("candidate_sha256"),
            "bytes": event.get("candidate_bytes"),
            "parent": event.get("parent_candidate_sha256"),
            "round": event.get("correction_round_lifetime", event.get("correction_round")),
            "origin": event.get("custody_origin"),
        }
    if kind == "candidate_write_ahead_aborted":
        return {"t": "abort", "scope": event.get("package_scope_id")}
    return {"t": kind, "scope": event.get("package_scope_id")}


# ---------------------------------------------------------------------------
# Section 11.2 / 11.2a -- the durable provider sequence.
# ---------------------------------------------------------------------------
@dataclass
class PreparedRequest:
    provider_kind: str
    provider_endpoint_identity: str
    provider_availability_episode_identity: str
    provider_availability_episode_generation: int
    provider_request_identity: str
    provider_dispatch_serial: int
    work_item_identity: str
    work_item_kind: str
    prompt_material_sha256: str
    required_inputs_sha256: str
    result_schema_id: str
    idempotency_key_sent: bool
    capability_record: dict
    consumption_identity: str | None = None

    def provider_binding(self):
        return {
            "provider_kind": self.provider_kind,
            "provider_endpoint_identity": self.provider_endpoint_identity,
            "provider_availability_episode_identity": (
                self.provider_availability_episode_identity
            ),
            "provider_availability_episode_generation": (
                self.provider_availability_episode_generation
            ),
            "provider_request_identity": self.provider_request_identity,
            "provider_dispatch_serial": self.provider_dispatch_serial,
        }


def build_prepared_request(context, events, work_item_obj, work_item_id, *, consumption_identity=None,
                           extra_prompt=None, extra_inputs=None):
    provider_kind = constants.PROVIDER_KIND_BY_WORK_ITEM_KIND[work_item_obj["work_item_kind"]]
    record, endpoint = context.capability_record(provider_kind)
    if endpoint is None:
        raise SupervisorRefusal(
            "no provider endpoint is bound for %s in this package" % provider_kind
        )
    rep = replay_mod.Replay(events, context.binding.package_scope_id)
    generation = rep.episode_generation(work_item_id, provider_kind, endpoint)
    episode = rep.episode_identity(work_item_id, provider_kind, endpoint, generation)
    serial = rep.provider_dispatch_serial(work_item_id, provider_kind, episode)
    prompt = prompt_material_sha256(provider_kind, work_item_obj, extra_prompt)
    inputs = required_inputs_sha256(context, work_item_obj, extra_inputs)
    request_identity = derive(
        "provider_request_identity",
        {
            "provider_kind": provider_kind,
            "provider_endpoint_identity": endpoint,
            "work_item_identity": work_item_id,
            "provider_availability_episode_identity": episode,
            "provider_dispatch_serial": serial,
            "prompt_material_sha256": prompt,
            "required_inputs_sha256": inputs,
        },
    )
    return PreparedRequest(
        provider_kind=provider_kind,
        provider_endpoint_identity=endpoint,
        provider_availability_episode_identity=episode,
        provider_availability_episode_generation=generation,
        provider_request_identity=request_identity,
        provider_dispatch_serial=serial,
        work_item_identity=work_item_id,
        work_item_kind=work_item_obj["work_item_kind"],
        prompt_material_sha256=prompt,
        required_inputs_sha256=inputs,
        result_schema_id=constants.RESULT_SCHEMA_ID_BY_PROVIDER_KIND[provider_kind],
        idempotency_key_sent=bool(record["idempotency_key_supported"]),
        capability_record=record,
        consumption_identity=consumption_identity,
    )


def append_prepared(operation, prepared):
    body = dict(prepared.provider_binding())
    body.update(
        {
            "controller_executable_identity": operation.envelope[
                "controller_executable_identity"
            ],
            "supervisor_operation_id": operation.operation_id,
            "work_item_identity": prepared.work_item_identity,
            "work_item_kind": prepared.work_item_kind,
            "provider_capability_record_identity": capability.capability_record_identity(
                prepared.provider_kind, prepared.provider_endpoint_identity
            ),
            "provider_capability_record_sha256": prepared.capability_record[
                "capability_record_sha256"
            ],
            "provider_capability_source": prepared.capability_record["capability_source"],
            "prompt_material_sha256": prepared.prompt_material_sha256,
            "required_inputs_sha256": prepared.required_inputs_sha256,
            "result_schema_id": prepared.result_schema_id,
            "idempotency_key_sent": prepared.idempotency_key_sent,
            "consumption_identity": prepared.consumption_identity,
        }
    )
    return operation.append("provider_request_prepared", body)


def append_dispatch_begun(operation, prepared, prepared_event_seq, transport="in_process_https"):
    """The write-ahead.  Durable BEFORE anything that could reach the provider."""
    pid = None
    process_start_ticks = None
    boot_digest = None
    if transport == "subprocess_cli":
        # These are the identity of the controller process that owns and
        # supervises the CLI dispatch.  They are known before spawn, so the
        # write-ahead remains durably before anything can reach a provider.
        pid = os.getpid()
        process_start_ticks = read_process_start_ticks(pid)
        boot_digest = boot_id_sha256()
    body = dict(prepared.provider_binding())
    body.update(
        {
            "controller_executable_identity": operation.envelope[
                "controller_executable_identity"
            ],
            "supervisor_operation_id": operation.operation_id,
            "work_item_identity": prepared.work_item_identity,
            "provider_request_prepared_event_seq": prepared_event_seq,
            "dispatch_transport": transport,
            "dispatch_pid": pid,
            "dispatch_process_start_ticks": process_start_ticks,
            "dispatch_boot_id_sha256": boot_digest,
        }
    )
    return operation.append("provider_dispatch_begun", body)


def append_acceptance(operation, prepared, dispatch_event_seq, observation):
    """Section 4.2a -- written ONLY where acceptance is authoritatively knowable."""
    authority = observation.acceptance_authority
    if authority == "none":
        return None
    if authority not in ("provider_request_ref", "idempotency_echo"):
        raise SupervisorRefusal("acceptance_authority %r is not controlled" % (authority,))
    ref = observation.provider_side_request_ref
    if authority == "idempotency_echo":
        if ref != prepared.provider_request_identity:
            raise SupervisorRefusal(
                "an idempotency echo must equal the sent provider_request_identity"
            )
    if not ref:
        raise SupervisorRefusal("a written acceptance event requires a non-null reference")
    evidence = observation.acceptance_evidence or {}
    body = dict(prepared.provider_binding())
    body.update(
        {
            "controller_executable_identity": operation.envelope[
                "controller_executable_identity"
            ],
            "supervisor_operation_id": operation.operation_id,
            "work_item_identity": prepared.work_item_identity,
            "provider_dispatch_begun_event_seq": dispatch_event_seq,
            "acceptance_authority": authority,
            "provider_side_request_ref": ref,
            "acceptance_evidence_sha256": sha256_hex(
                canonical_json(["NH_ACCEPTANCE_EVIDENCE_V1", evidence])
            ),
        }
    )
    return operation.append("provider_request_accepted", body)


def build_provider_outcome_facts(observation, capability_record, observed_body_length):
    """Assemble exactly one bounded facts object from what the controller saw."""
    partial = {
        "http_status_present": observation.http_status is not None,
        "http_status": observation.http_status,
        "endpoint_error_code_present": observation.endpoint_error_code_sha256 is not None,
        "endpoint_error_code_sha256": observation.endpoint_error_code_sha256,
    }
    token = classify.derive_provider_error_signal_token(partial, capability_record)
    return {
        "provider_outcome_facts_version": 1,
        "transport_kind": observation.transport_kind,
        "transport_outcome": observation.transport_outcome,
        "transmission_proved_absent": bool(observation.transmission_proved_absent),
        "returncode": observation.returncode,
        "http_status_present": observation.http_status is not None,
        "http_status": observation.http_status,
        "declared_content_length_present": observation.declared_content_length is not None,
        "declared_content_length": observation.declared_content_length,
        "observed_body_byte_length": observed_body_length,
        "endpoint_error_code_present": observation.endpoint_error_code_sha256 is not None,
        "endpoint_error_code_sha256": observation.endpoint_error_code_sha256,
        "retry_after_present": observation.retry_after_seconds is not None,
        "retry_after_seconds": observation.retry_after_seconds,
        "provider_error_signal_token": token,
        "capability_record_sha256": capability_record["capability_record_sha256"],
    }


# ---------------------------------------------------------------------------
# Section 4.9 / 4.9a -- result custody.
# ---------------------------------------------------------------------------
def store_anchored_result(context, provider_request_identity, payload):
    """Exclusive-create, fsync, re-open, re-read, and re-verify (Section 4.9a)."""
    store = context.result_store_dir()
    if store is None:
        raise SupervisorRefusal("no anchored provider result store is configured")
    os.makedirs(store, mode=0o700, exist_ok=True)
    os.chmod(store, 0o700)
    name = "%s.result.json" % provider_request_identity
    path = os.path.join(store, name)
    digest = sha256_hex(payload)
    try:
        fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY | os.O_NOFOLLOW, 0o600)
    except FileExistsError:
        with open(path, "rb") as handle:
            existing = handle.read()
        if sha256_hex(existing) != digest or len(existing) != len(payload):
            raise SupervisorRefusal(
                "an existing anchored result object does not re-verify: "
                "provider_result_custody_unverifiable"
            )
        return name, True
    try:
        os.write(fd, payload)
        os.fsync(fd)
    finally:
        os.close(fd)
    dir_fd = os.open(store, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(dir_fd)
    finally:
        os.close(dir_fd)
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW)
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
            raise SupervisorRefusal("the anchored result object is not a plain single-link file")
        readback = os.read(fd, constants.MAX_PROVIDER_RESULT_READ_LIMIT_BYTES)
    finally:
        os.close(fd)
    if len(readback) != len(payload) or sha256_hex(readback) != digest:
        raise SupervisorRefusal("the anchored result object failed read-back verification")
    return name, True


def read_anchored_result(context, result_object_name):
    store = context.result_store_dir()
    path = os.path.join(store, result_object_name)
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW)
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
            raise SupervisorRefusal("the anchored result object is not a plain single-link file")
        if info.st_uid != os.geteuid():
            raise SupervisorRefusal("the anchored result object is not owned by this user")
        return os.read(fd, constants.MAX_PROVIDER_RESULT_READ_LIMIT_BYTES)
    finally:
        os.close(fd)


def append_result_custody(operation, context, prepared, dispatch_event_seq, payload,
                          *, result_origin, result_schema_valid, custody_next_step):
    """Append ``provider_result_custody_recorded`` BEFORE any retained terminal."""
    length = len(payload)
    if length > constants.MAX_PROVIDER_RESULT_BYTES:
        raise SupervisorRefusal("custody is never claimed for an oversize result")
    digest = sha256_hex(payload)
    if length <= constants.MAX_INLINE_RESULT_BYTES:
        location_kind = "inline_journal_bytes"
        location_id = None
        object_name = None
        bytes_base64 = base64.b64encode(payload).decode("ascii")
        readback = True
    else:
        location_kind = "anchored_result_object"
        location_id = "provider_result_store"
        object_name, readback = store_anchored_result(
            context, prepared.provider_request_identity, payload
        )
        bytes_base64 = None

    custody_identity = derive(
        "result_custody_identity",
        {
            "provider_kind": prepared.provider_kind,
            "provider_request_identity": prepared.provider_request_identity,
            "work_item_identity": prepared.work_item_identity,
            "result_origin": result_origin,
            "result_location_kind": location_kind,
            "result_location_id": location_id,
            "result_object_name": object_name,
            "result_byte_length": length,
            "result_sha256": digest,
            "result_schema_id": prepared.result_schema_id,
            "result_schema_version": constants.RESULT_SCHEMA_VERSION,
        },
    )
    body = dict(prepared.provider_binding())
    body.update(
        {
            "controller_executable_identity": operation.envelope[
                "controller_executable_identity"
            ],
            "supervisor_operation_id": operation.operation_id,
            "work_item_identity": prepared.work_item_identity,
            "work_item_kind": prepared.work_item_kind,
            "provider_dispatch_begun_event_seq": dispatch_event_seq,
            "result_custody_identity": custody_identity,
            "result_origin": result_origin,
            "result_location_kind": location_kind,
            "result_location_id": location_id,
            "result_object_name": object_name,
            "result_bytes_base64": bytes_base64,
            "result_byte_length": length,
            "result_sha256": digest,
            "result_schema_id": prepared.result_schema_id,
            "result_schema_version": constants.RESULT_SCHEMA_VERSION,
            "result_schema_valid": result_schema_valid,
            "custody_readback_proved": bool(readback),
            "consumption_identity": prepared.consumption_identity,
            "custody_next_step": custody_next_step,
        }
    )
    return operation.append("provider_result_custody_recorded", body)


def custodied_bytes(context, custody_event):
    """Re-read the custodied bytes and re-verify length and digest (B6c)."""
    if custody_event["result_location_kind"] == "inline_journal_bytes":
        payload = base64.b64decode(custody_event["result_bytes_base64"].encode("ascii"))
    else:
        payload = read_anchored_result(context, custody_event["result_object_name"])
    if len(payload) != custody_event["result_byte_length"]:
        raise SupervisorRefusal("the custodied result byte length does not re-verify")
    if sha256_hex(payload) != custody_event["result_sha256"]:
        raise SupervisorRefusal("the custodied result digest does not re-verify")
    return payload


def parse_result_bytes(payload):
    """Parse under the canonical key-string rule.  Returns ``(value, error)``."""
    try:
        return strict_json_loads(payload.decode("utf-8")), None
    except NonCanonicalKeyError as exc:
        return None, "non-canonical object key: %s" % exc
    except DuplicateJsonKeyError as exc:
        return None, "duplicate object key: %s" % exc
    except Exception as exc:  # noqa: BLE001 -- any parse failure is result_invalid
        return None, "invalid JSON: %s" % exc


def append_terminal(operation, prepared, dispatch_event_seq, *, terminal_kind,
                    terminal_evidence_kind, result_custody_identity=None,
                    result_custody_event_seq=None, provider_result_facts_sha256=None,
                    provider_outcome_facts=None, provider_error_signal_token=None,
                    provider_error_classification_row_id=None, provider_returncode=None,
                    result_schema_valid=False, oversize_detection_kind=None,
                    observed_bytes_read=None, declared_result_byte_length=None,
                    dependency_slot=None):
    body = dict(prepared.provider_binding())
    body.update(dependency_slot or schema.empty_dependency_slot())
    body.update(
        {
            "controller_executable_identity": operation.envelope[
                "controller_executable_identity"
            ],
            "supervisor_operation_id": operation.operation_id,
            "work_item_identity": prepared.work_item_identity,
            "provider_dispatch_begun_event_seq": dispatch_event_seq,
            "terminal_kind": terminal_kind,
            "terminal_evidence_kind": terminal_evidence_kind,
            "result_custody_identity": result_custody_identity,
            "result_custody_event_seq": result_custody_event_seq,
            "provider_result_facts_sha256": provider_result_facts_sha256,
            "provider_outcome_facts": provider_outcome_facts,
            "provider_error_signal_token": provider_error_signal_token,
            "provider_error_classification_row_id": provider_error_classification_row_id,
            "provider_returncode": provider_returncode,
            "result_schema_valid": result_schema_valid,
            "oversize_detection_kind": oversize_detection_kind,
            "observed_bytes_read": observed_bytes_read,
            "declared_result_byte_length": declared_result_byte_length,
        }
    )
    return operation.append("provider_request_terminal_recorded", body)


def oversize_facts_digest(prepared, oversize_detection_kind, declared, observed):
    obj = {
        "provider_kind": prepared.provider_kind,
        "provider_endpoint_identity": prepared.provider_endpoint_identity,
        "provider_request_identity": prepared.provider_request_identity,
        "provider_availability_episode_identity": (
            prepared.provider_availability_episode_identity
        ),
        "provider_dispatch_serial": prepared.provider_dispatch_serial,
        "expected_result_schema_id": prepared.result_schema_id,
        "oversize_detection_kind": oversize_detection_kind,
        "declared_result_byte_length": declared,
        "observed_bytes_read": observed,
        "max_provider_result_bytes": constants.MAX_PROVIDER_RESULT_BYTES,
        "max_provider_result_read_limit_bytes": (
            constants.MAX_PROVIDER_RESULT_READ_LIMIT_BYTES
        ),
    }
    return sha256_hex(canonical_json(["NH_PROVIDER_OVERSIZE_FACTS_V1", obj]))


def error_facts_digest(facts, token, row_id):
    return sha256_hex(
        canonical_json(
            [
                "NH_PROVIDER_ERROR_FACTS_V1",
                {
                    "provider_outcome_facts": facts,
                    "provider_error_signal_token": token,
                    "provider_error_classification_row_id": row_id,
                },
            ]
        )
    )


def result_facts_digest(payload_digest, prepared):
    return sha256_hex(
        canonical_json(
            [
                "NH_PROVIDER_RESULT_FACTS_V1",
                {
                    "provider_request_identity": prepared.provider_request_identity,
                    "result_sha256": payload_digest,
                    "result_schema_id": prepared.result_schema_id,
                },
            ]
        )
    )


# ---------------------------------------------------------------------------
# Dependency helpers bound to the current events.
# ---------------------------------------------------------------------------
def classify_and_slot(context, events, code, *, work_item_id, resource_identity,
                      episode_identity=None, request_identity=None, placement,
                      phase_evidence_condition, observed_symptom_code=None,
                      predicate_params=None, observed_evidence_event_seq=None,
                      observed_evidence_sha256=None, plain_language="",
                      reference_only=False, resource_kind=None):
    record = dependency.build_record(
        code,
        resource_identity,
        work_item_id,
        resource_kind=resource_kind,
        episode_identity=episode_identity,
        request_identity=request_identity,
        predicate_params=predicate_params,
        observed_symptom_code=observed_symptom_code,
        phase_evidence_condition=phase_evidence_condition,
        durable_record_placement=placement,
        observed_evidence_event_seq=observed_evidence_event_seq,
        observed_evidence_sha256=observed_evidence_sha256,
        plain_language_dependency=plain_language,
    )
    problems = dependency.check_record(record)
    if problems:
        raise SupervisorRefusal("; ".join(problems))
    identity = dependency_identity(record)
    occurrences = [
        event for event in events if event.get("dependency_identity") is not None
    ]
    if reference_only:
        slot = dependency.reference_slot(occurrences, identity)
    else:
        slot = dependency.next_slot(occurrences, record, identity)
    return record, identity, slot


def reference_existing(events, identity):
    occurrences = [
        event for event in events if event.get("dependency_identity") is not None
    ]
    return dependency.reference_slot(occurrences, identity)

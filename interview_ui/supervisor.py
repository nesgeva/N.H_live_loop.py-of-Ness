#!/usr/bin/env python3
"""Durable private scheduling, the anchored lease, and the browser projections.

Sections 11.7, 13.2 to 13.6 and 15 of
``NH_AUTOMATIC_SUPERVISOR_MECHANICAL_CHANGE_SPEC_v1_13_CANDIDATE.md``.

The durable mechanics are NOT re-implemented here: the private scheduling
journal (version 6) and the four-state anchored lease are the controller's own
production modules, imported directly, so one implementation serves the
controller's command preconditions and the worker alike.

Nothing in this module decides N.H policy, validates a Ness question, invokes a
model, or accepts a package.  The private journal is an observation/recovery log
and is never authority for workflow state, an audit, a PASS, candidate custody,
a question, or acceptance readiness.
"""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

_UI_DIR = os.path.dirname(os.path.abspath(__file__))
_CONTROLLER_DIR = os.path.join(os.path.dirname(_UI_DIR), "controller")
if _CONTROLLER_DIR not in sys.path:
    sys.path.insert(0, _CONTROLLER_DIR)

from nh_supervisor import constants as controller_constants  # noqa: E402
from nh_supervisor import lease as controller_lease  # noqa: E402
from nh_supervisor import scheduling as controller_scheduling  # noqa: E402
from nh_supervisor.canonical import canonical_json, sha256_hex  # noqa: E402,F401

# -- the durable mechanics, re-exported rather than re-implemented -----------
SchedulingJournal = controller_scheduling.SchedulingJournal
SchedulingJournalError = controller_scheduling.SchedulingJournalError
SupervisorLease = controller_lease.SupervisorLease
LeaseHooks = controller_lease.LeaseHooks
LeaseError = controller_lease.LeaseError
resolve_state_dir = controller_lease.resolve_state_dir
new_work_start_gate = controller_lease.new_work_start_gate
in_flight_closure_append_gate = controller_lease.in_flight_closure_append_gate
IN_FLIGHT_CLOSURE_APPEND_TYPES = controller_lease.IN_FLIGHT_CLOSURE_APPEND_TYPES
backoff_delay_seconds = controller_scheduling.backoff_delay_seconds

SCHEDULING_JOURNAL_VERSION = controller_constants.SUPERVISOR_SCHEDULING_JOURNAL_VERSION
SCHEDULING_JOURNAL_SUPPORTED_VERSIONS = (
    controller_constants.SUPERVISOR_SCHEDULING_JOURNAL_SUPPORTED_VERSIONS
)
LEASE_STATES = controller_constants.LEASE_STATES
LEASE_HEARTBEAT_INTERVAL_SECONDS = controller_constants.LEASE_HEARTBEAT_INTERVAL_SECONDS
LEASE_EXPIRY_SECONDS = controller_constants.LEASE_EXPIRY_SECONDS
LEASE_START_MIN_REMAINING_SECONDS = (
    controller_constants.LEASE_START_MIN_REMAINING_SECONDS
)
LEASE_STOP_MARGIN_SECONDS = controller_constants.LEASE_STOP_MARGIN_SECONDS
BUNDLE_PLACEMENT_DISPLAY = controller_constants.BUNDLE_PLACEMENT_DISPLAY

# The acceptance vocabulary, re-exported from the controller rather than
# retyped here.  The browser layer owns none of it and invents none of it.
ACCEPTANCE_POST_REQUIRED_FIELDS = (
    controller_constants.ACCEPTANCE_POST_REQUIRED_FIELDS
)
ACCEPTANCE_OFFER_ROUTE = controller_constants.ACCEPTANCE_OFFER_ROUTE
ACCEPTANCE_RECORD_ROUTE = controller_constants.ACCEPTANCE_RECORD_ROUTE
ACCEPTANCE_TRUTHS = controller_constants.ACCEPTANCE_TRUTHS
ACCEPTANCE_TRUTH_ACCEPTED = controller_constants.ACCEPTANCE_TRUTH_ACCEPTED
ACCEPTANCE_FIXED_MEANING = controller_constants.ACCEPTANCE_FIXED_MEANING


class WorkflowState(str, Enum):
    """The eight public supervisor states, plus the ninth acceptance adds.

    The ninth is APPENDED, never inserted: the eight that existed before it
    keep their exact values and their exact order, so nothing that already
    reads this enum changes meaning.
    """

    IDLE = "IDLE"
    WORKING = "WORKING"
    DIAGNOSING = "DIAGNOSING"
    WAITING_RECOVERING = "WAITING_RECOVERING"
    NEEDS_NESS_DECISION = "NEEDS_NESS_DECISION"
    NEEDS_USER_ACTION = "NEEDS_USER_ACTION"
    SAFETY_HOLD = "SAFETY_HOLD"
    READY_FOR_ACCEPTANCE = "READY_FOR_ACCEPTANCE"
    # Terminal and non-running.  It exists only after Ness explicitly performs
    # the separately authorized acceptance action, and the browser projects it
    # from the authenticated controller state alone -- never from a feed claim,
    # and never because its own POST returned HTTP success.
    ACCEPTED_FOR_DESIGN_ONLY = "ACCEPTED_FOR_DESIGN_ONLY"


INTERRUPTING_STATES = frozenset(
    (
        WorkflowState.NEEDS_NESS_DECISION,
        WorkflowState.NEEDS_USER_ACTION,
        WorkflowState.READY_FOR_ACCEPTANCE,
    )
)

# Section 13.6 -- active present-tense wording only under LIVE_PROVED.
ATTENTION_KIND_BY_STATE = {
    "NEEDS_NESS_DECISION": "decision",
    "NEEDS_USER_ACTION": "action",
    "READY_FOR_ACCEPTANCE": "acceptance",
}


def attention_kind_for(state):
    """Section 15 -- the one reason a person is being addressed, or none."""
    return ATTENTION_KIND_BY_STATE.get(WorkflowState(state).value, "none")


ACTIVE_WORDING_STATES = frozenset(
    (WorkflowState.WORKING, WorkflowState.DIAGNOSING, WorkflowState.WAITING_RECOVERING)
)


class SupervisorProjectionError(RuntimeError):
    """A report could not be projected because it was not proved current."""


@dataclass
class SupervisorSnapshot:
    """Everything the browser is allowed to show, and nothing else."""

    state: WorkflowState = WorkflowState.IDLE
    authenticated: bool = False
    lease_state: str = "ABSENT_PROVED"
    live_proved: bool = False
    package_key: Any = None
    package_scope_id: Any = None
    package_id: Any = None
    # v1_8 section 21 -- the loop-level fields.  They describe the OVERALL
    # loop, never the accepted package, and the UI must never present the
    # transition as progress on that package (section 21.3).
    loop_state: Any = None
    # A real Q transition EXISTS and Q is not yet established.
    loop_transition_active: bool = False
    # The loop is genuinely doing continuation work right now.  A transition
    # that exists but is waiting, held or stopped is NOT working.
    loop_transition_working: bool = False
    bundle_placement_display: str = BUNDLE_PLACEMENT_DISPLAY
    controlled_component_id: Any = None
    register_id: Any = None
    candidate_path: Any = None
    candidate_sha256: Any = None
    candidate_bytes: Any = None
    correction_batch_size: int = controller_constants.CORRECTION_BATCH_SIZE
    correction_batch_number: int = 0
    correction_rounds_started_this_batch: int = 0
    correction_rounds_completed_this_batch: int = 0
    correction_rounds_lifetime: int = 0
    next_command: Any = None
    ness_decision_required: bool = False
    interview_projection: Any = None
    interview_gate_projection: Any = None
    ness_decision_clearance: Any = None
    ness_question_binding: Any = None
    ness_answer_clarification: Any = None
    ness_decision_cleared: bool = False
    user_action_required: bool = False
    acceptance_required: bool = False
    plain_language_dependency: Any = None
    user_action_code: Any = None
    will_retry_by_itself: bool = False
    provider_attempts_remaining_this_episode: Any = None
    output_retries_remaining: Any = None
    availability_probes_remaining: Any = None
    provider_request_unreconciled: bool = False
    # What the LOCKED authenticated journal proves about acceptance, carried
    # separately from whether any request succeeded.  Exactly three values:
    # PROVED_NOT_ACCEPTED, PROVED_ACCEPTED, UNRESOLVED.
    acceptance_truth: Any = None
    acceptance_disposition: Any = None
    ness_acceptance_identity: Any = None
    accepted_for_design_only: bool = False
    # Section 15 -- which of the four browser views this state belongs under.
    # It names WHY a person is being addressed, never what was decided: a
    # decision Ness owes, a practical action a person owes, or a separate
    # acceptance that has NOT happened.  It is derived from the authenticated
    # state alone and claims nothing.
    attention_kind: str = "none"
    technical: dict = field(default_factory=dict)
    wording: dict = field(default_factory=dict)

    def as_dict(self):
        data = {
            key: getattr(self, key)
            for key in (
                "authenticated", "lease_state", "live_proved", "package_key",
                "package_scope_id", "package_id", "bundle_placement_display",
                "controlled_component_id", "register_id", "candidate_path",
                "candidate_sha256", "candidate_bytes", "correction_batch_size",
                "correction_batch_number", "correction_rounds_started_this_batch",
                "correction_rounds_completed_this_batch", "correction_rounds_lifetime",
                "next_command", "ness_decision_required", "interview_projection",
                "interview_gate_projection", "ness_decision_clearance",
                "ness_question_binding", "ness_answer_clarification",
                "ness_decision_cleared", "user_action_required",
                "acceptance_required", "plain_language_dependency", "user_action_code",
                "will_retry_by_itself", "provider_attempts_remaining_this_episode",
                "output_retries_remaining", "availability_probes_remaining",
                "provider_request_unreconciled", "acceptance_truth",
                "acceptance_disposition", "ness_acceptance_identity",
                "accepted_for_design_only", "attention_kind", "technical",
                "wording",
            )
        }
        data["state"] = self.state.value
        return data


def snapshot_for_state(
    state, *, controller_authenticated=True, run_active=True
):
    """Small deterministic constructor used by the local presentation tests."""
    state = WorkflowState(state)
    lease_state = "LIVE_PROVED" if run_active else "ABSENT_PROVED"
    snapshot = SupervisorSnapshot(
        state=state,
        authenticated=bool(controller_authenticated),
        lease_state=lease_state,
        live_proved=bool(run_active),
        ness_decision_required=state == WorkflowState.NEEDS_NESS_DECISION,
        user_action_required=state == WorkflowState.NEEDS_USER_ACTION,
        acceptance_required=state == WorkflowState.READY_FOR_ACCEPTANCE,
        attention_kind=attention_kind_for(state),
    )
    snapshot.wording = wording_for(state, lease_state)
    if controller_authenticated and not run_active and state in ACTIVE_WORDING_STATES:
        snapshot.wording["detail"] = (
            "no current live supervisor lease is proved. This is saved history, "
            "not a claim that work is running now."
        )
    return snapshot


# Section 15 -- the booleans that must all be true before any non-IDLE claim.
PROOF_KEYS = (
    "journal_authentication_proved",
    "authenticated_state_current",
    "source_state_current",
)

AUTOMATIC_RETRY_MODES = frozenset(
    (
        "automatic_backoff",
        "automatic_lookup_only",
        "automatic_bounded_output_retry",
        "automatic_probe_only",
    )
)


def report_is_proved(report):
    """A fresh successful ``supervisor-status`` whose proofs are all true."""
    if not isinstance(report, dict):
        return False
    if report.get("command") != "supervisor-status" or report.get("ok") is not True:
        return False
    return all(report.get(key) is True for key in PROOF_KEYS)


# v1_8 section 21.1 -- the SEPARATE transition line.
#
# The accepted card is UNCHANGED IN SUBSTANCE.  Exactly ONE clause is made
# conditional and only that one: while a transition is genuinely in progress,
# "and no next package started" is no longer an unqualified truth, so the
# accepted card must not keep asserting it.
#
# UI-NO-REWRITE-HISTORY: historical accepted-package cards are HISTORY.  Their
# wording is never rewritten, re-dated, re-scoped or re-interpreted.  Only the
# LIVE card for the currently-accepted package carries the transition line.
ACCEPTED_CARD_DETAIL = (
    "Ness accepted this exact candidate as a design. Nothing was adopted, "
    "integrated, implemented, marked PACKAGE_COMPLETE, closed, committed, or "
    "pushed, and no next package started."
)
ACCEPTED_CARD_DETAIL_DURING_TRANSITION = (
    "Ness accepted this exact candidate as a design. Nothing was adopted, "
    "integrated, implemented, marked PACKAGE_COMPLETE, closed, committed, or "
    "pushed."
)
TRANSITION_LINE = (
    "N.H is choosing and preparing the next design package from current "
    "sources. Nothing has been adopted, integrated, implemented, committed, or "
    "pushed."
)
# v1_8 section 21.3 -- a transition that EXISTS but is not RUNNING must not be
# described as working.  These say what is true without claiming progress.
TRANSITION_NOT_WORKING_LINE = (
    "N.H has started moving to the next design package and is not working on it "
    "right now. Nothing has been adopted, integrated, implemented, committed, "
    "or pushed."
)


def wording_for(state, lease_state, loop_transition_active=False,
                loop_transition_working=False):
    """Section 13.6 -- exact wording, decided only by proved lease ownership.

    ``loop_transition_active`` is the v1_8 section 21.1 addition and changes
    exactly one clause of exactly one card.  It NEVER claims that continuation
    is progress on the accepted package, that a selection or a prepared task is
    a decision, an adoption or an integration, that a new package has started
    before its validation_recorded and initial custody are durable, that the
    loop is "working" while it is holding, waiting or stopped, a next-package
    name the controller has not proved from source, or that acceptance caused
    any of it (section 21.3).
    """
    live = lease_state == "LIVE_PROVED"
    if state in ACTIVE_WORDING_STATES and live:
        headline = {
            WorkflowState.WORKING: "Mechanical work is continuing automatically",
            WorkflowState.DIAGNOSING: (
                "A bounded batch ended; a fresh independent diagnosis is running"
            ),
            WorkflowState.WAITING_RECOVERING: (
                "N.H is waiting and will resume by itself when it is safe"
            ),
        }[state]
        detail = ""
    elif state in ACTIVE_WORDING_STATES:
        headline = "Automatic work is not running"
        detail = "This is the last saved state, not live activity."
        if lease_state == "INVALID_UNPROVED":
            detail += (
                " The supervisor lease could not be proved. Nothing was taken over "
                "and nothing was changed."
            )
    else:
        headline = {
            WorkflowState.IDLE: "No supervised run is active",
            WorkflowState.NEEDS_NESS_DECISION: "Ness needs to make one decision",
            WorkflowState.NEEDS_USER_ACTION: "One practical action is needed",
            WorkflowState.SAFETY_HOLD: "N.H stopped and changed nothing",
            WorkflowState.READY_FOR_ACCEPTANCE: "Ready for Ness to consider acceptance",
            WorkflowState.ACCEPTED_FOR_DESIGN_ONLY: (
                "Accepted for design-only status"
            ),
        }[state]
        detail = ""
        if state == WorkflowState.READY_FOR_ACCEPTANCE:
            detail = (
                "Nothing has been accepted, adopted, installed, integrated, "
                "committed, or pushed."
            )
        if state == WorkflowState.ACCEPTED_FOR_DESIGN_ONLY:
            # The accepted state is terminal FOR ITS OWN PACKAGE, and
            # acceptance adopted, integrated, implemented, closed and started
            # exactly nothing.  While a transition is genuinely in progress the
            # separate transition line is shown alongside it, honestly.
            if loop_transition_active:
                # A transition EXISTS, so "no next package started" is no longer
                # true and the accepted card stops asserting it.  Whether the
                # loop is WORKING is a separate fact, requires a PROVED LIVE
                # LEASE, and is never assumed: a transition can exist with a
                # command owed while production is simply stopped.
                detail = "%s %s" % (
                    ACCEPTED_CARD_DETAIL_DURING_TRANSITION,
                    TRANSITION_LINE
                    if (loop_transition_working and live)
                    else TRANSITION_NOT_WORKING_LINE,
                )
            else:
                detail = ACCEPTED_CARD_DETAIL
        if state == WorkflowState.SAFETY_HOLD and lease_state == "INVALID_UNPROVED":
            detail = (
                "The supervisor lease could not be proved. Nothing was taken over "
                "and nothing was changed."
            )
    return {"headline": headline, "detail": detail}


TECHNICAL_KEYS = (
    "supervisor_capability_version",
    "authenticated_event_seq",
    "authenticated_tail_sha256",
    "standing_chain_sha256",
    "state_binding_sha256",
    "retry_series_key",
    "work_item_identity",
    "work_item_kind",
    "provider_kind",
    "provider_phase",
    "provider_request_identity",
    "provider_availability_episode_identity",
    "provider_availability_episode_generation",
    "provider_attempts_closed_this_episode",
    "provider_reconciliation",
    "provider_result_custody",
    "result_custody_identity",
    "provider_error_signal_token",
    "provider_error_classification_row_id",
    "design_audit_result_usability",
    "output_retries_used",
    "availability_probe_state",
    "availability_probe_identity",
    "availability_probe_automatic_eligible",
    "episode_unlock_automatic_eligible",
    "c11a_self_condition_satisfied",
    "episode_exhaustion_person_route_reason",
    "automatic_episode_unlocks_used",
    "semantic_scope_key",
    "semantic_unlock_generation",
    "semantic_scope_exhausted",
    "semantic_scope_exhaustion_event_seq",
    "semantic_scope_unlock_available",
    "exhausted_novelty_key_count",
    "no_progress_rounds_in_scope",
    "diagnosis_trigger_identity",
    "diagnosis_trigger_attempt_ordinal",
    "diagnosis_trigger_state",
    "consumption_reconciliation",
    "open_consumption_identity",
    "dependency_identity",
    "dependency_identity_binding",
    "dependency_carrier_event_seq",
    "dependency_occurrence_ordinal",
    "dependency_durable_record_placement",
    "audit_identity",
    "checkpoint_identity",
    "piece3_provider_authorization",
    "source_binding_sha256",
    "settled_decision_binding_sha256",
    "branch",
    "head_sha",
)


def technical_details(report):
    """Section 15 -- digests appear here as EVIDENCE, never as a claim."""
    return {key: report.get(key) for key in TECHNICAL_KEYS}


def snapshot_from_supervisor_status(report):
    """Project ONE freshly proved ``supervisor-status`` report.

    An absent, refused, stale, or unproved report yields the IDLE snapshot that
    says no authenticated supervised run is active, and no PASS, fix, or
    acceptance claim is made from it.
    """
    if not report_is_proved(report):
        snapshot = SupervisorSnapshot()
        snapshot.wording = wording_for(WorkflowState.IDLE, "ABSENT_PROVED")
        snapshot.technical = {
            "reason": "no fresh authenticated supervisor-status report is available"
        }
        return snapshot

    state = WorkflowState(report["workflow_state"])
    lease = report.get("run_lease") or {}
    lease_state = lease.get("lease_state") or "ABSENT_PROVED"
    # v1_8 section 24.9 -- the loop-level fields the snapshot must render.
    # They come from the read-only loop projection and NEVER from a model
    # asserting that its own work succeeded.
    loop_state = report.get("loop_state")
    loop_transition_active = bool(report.get("loop_transition_exists"))
    loop_transition_working = bool(report.get("loop_transition_working"))
    record = report.get("dependency_record") or {}
    retry_mode = record.get("retry_mode")

    snapshot = SupervisorSnapshot(
        state=state,
        authenticated=True,
        lease_state=lease_state,
        live_proved=lease_state == "LIVE_PROVED",
        package_key=report.get("package_key"),
        package_scope_id=report.get("package_scope_id"),
        package_id=report.get("package_id"),
        # Section 15: bundle placement is UNRESOLVED and is displayed only as
        # "Not decided yet". It is never inferred by filename.
        bundle_placement_display=BUNDLE_PLACEMENT_DISPLAY,
        controlled_component_id=report.get("controlled_component_id"),
        register_id=report.get("register_id"),
        candidate_path=report.get("candidate_path"),
        candidate_sha256=report.get("candidate_sha256"),
        candidate_bytes=report.get("candidate_bytes"),
        correction_batch_size=report.get("correction_batch_size"),
        correction_batch_number=report.get("correction_batch_number"),
        correction_rounds_started_this_batch=report.get(
            "correction_rounds_started_this_batch"
        ),
        correction_rounds_completed_this_batch=report.get(
            "correction_rounds_completed_this_batch"
        ),
        correction_rounds_lifetime=report.get("correction_round_lifetime"),
        next_command=report.get("next_command"),
        ness_decision_required=bool(report.get("ness_decision_required")),
        interview_projection=report.get("interview_projection"),
        interview_gate_projection=report.get("interview_gate_projection"),
        ness_decision_clearance=report.get("ness_decision_clearance"),
        ness_question_binding=report.get("ness_question_binding"),
        ness_answer_clarification=report.get("ness_answer_clarification"),
        ness_decision_cleared=bool(report.get("ness_decision_cleared")),
        user_action_required=bool(report.get("user_action_required")),
        acceptance_required=bool(report.get("acceptance_required")),
        plain_language_dependency=record.get("plain_language_dependency"),
        user_action_code=record.get("user_action_code"),
        will_retry_by_itself=retry_mode in AUTOMATIC_RETRY_MODES,
        provider_attempts_remaining_this_episode=report.get(
            "provider_attempts_remaining_this_episode"
        ),
        output_retries_remaining=report.get("output_retries_remaining"),
        availability_probes_remaining=report.get(
            "availability_probes_remaining_this_closed_episode"
        ),
        provider_request_unreconciled=bool(report.get("open_provider_request_count")),
        acceptance_truth=report.get("acceptance_truth"),
        acceptance_disposition=report.get("acceptance_disposition"),
        ness_acceptance_identity=report.get("ness_acceptance_identity"),
        accepted_for_design_only=(
            state == WorkflowState.ACCEPTED_FOR_DESIGN_ONLY
        ),
        attention_kind=attention_kind_for(state),
        loop_state=loop_state,
        loop_transition_active=loop_transition_active,
        loop_transition_working=loop_transition_working,
    )
    snapshot.wording = wording_for(
        state,
        lease_state,
        loop_transition_active=loop_transition_active,
        loop_transition_working=loop_transition_working,
    )
    snapshot.technical = technical_details(report)
    return snapshot


def change_feed_from_supervisor_status(report):
    """Only controller-confirmed, authenticated items reach the feed."""
    if not report_is_proved(report):
        return []
    feed = []
    for item in report.get("controller_confirmed_change_events") or []:
        if not isinstance(item, dict):
            continue
        if item.get("controller_authenticated") is not True:
            continue
        if item.get("kind") not in controller_constants.FEED_ITEM_KINDS:
            continue
        technical = item.get("technical") or {}
        if not technical.get("controller_event_sha256"):
            continue
        feed.append(dict(item))
    return feed


def summary_from_feed(feed):
    kinds = [item["kind"] for item in feed]
    return {
        "problems_found": kinds.count("problem_found"),
        "candidates_changed": kinds.count("candidate_changed"),
        "audits_passed": kinds.count("audit_passed"),
        # Never a "fixed" claim on any model's own authority.
        "claims_fix": False,
        "claims_acceptance": False,
    }

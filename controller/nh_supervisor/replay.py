#!/usr/bin/env python3
"""Replay projections over the authenticated journal.

Everything in this module is a pure function of the authenticated event list.
No clock, no worker memory, no private journal, and no model output reaches any
value here.  Two implementations replaying one journal must agree event for
event, so every derivation is stated as a count or a lookup and never as a
judgement.
"""

from __future__ import annotations

import base64
import json

from . import constants, dependency, schema
from .canonical import canonical_json, is_hex64, sha256_hex
from .identity import batch_triple, derive
from .schema import (
    NESS_CANDIDATE_ACCEPTANCE_EVENT_TYPE,
    SUPERVISOR_EVENT_TYPES,
    dependency_slot_shape,
)

# ---------------------------------------------------------------------------
# ACCEPTED ROLE-SPLIT v1_6 section 6.5 -- ``STOP-CLOSURE-EXACT``, stated ONCE.
#
# These are PURE FUNCTIONS of the saved STOP bytes, the controller-proved
# package identity, and the authenticated event list.  They live HERE, in the
# lowest layer, because ``commands.py`` already imports this module and this
# module imports nothing of it -- so BOTH the read side (``_downstream_recorded``
# below, deciding whether a custody is still pending) and the write side
# (``commands.py``, deciding whether an append is owed) call these EXACT
# functions.  There is deliberately no second, weaker or approximate statement
# of this rule anywhere in the controller.
#
# Nothing here is new machinery: the probe shape, the fingerprint domain and the
# routed-signal-identity domain are the INSTALLED ones that
# ``routed_concern_fingerprint()`` and ``interview_routed_signal_id()`` already
# use, and that the T1 question route already reproduces.  No new event type, no
# new store, no new identity family, no new journal field.
# ---------------------------------------------------------------------------
STOP_REVIEW_SIGNAL_ROUTE = "chatgpt_review_required"


def stop_closure_probe(package_scope_id, saved_signal):
    """The EXACT installed routed-concern probe for one custodied STOP.

    The three candidate fields are honestly NULL: an initial-design STOP
    produced no candidate, and borrowing one would be a fake field
    (PIECE3-NO-FAKE-FIELDS).

    ``source_evidence`` and ``finding_evidence`` are normalised EXACTLY as the
    installed ``record_review_signal()`` normalises them before it hashes and
    writes them -- ``sorted(set(...))`` and ``list(...)`` -- so the expectation
    and the record agree by construction rather than by luck.
    """
    return {
        "package_scope_id": package_scope_id,
        "signal_source": constants.STOP_REVIEW_SIGNAL_SOURCE,
        "route": STOP_REVIEW_SIGNAL_ROUTE,
        "candidate_path": None,
        "candidate_sha256": None,
        "candidate_bytes": None,
        "signal_title": saved_signal["signal_title"],
        "source_evidence": sorted(set(saved_signal["source_evidence"] or ())),
        "finding_evidence": list(saved_signal["finding_evidence"] or ()),
        "issue_key": saved_signal["issue_key"],
        "finding_key": saved_signal["finding_key"],
    }


def stop_closure_routed_signal_id(package_scope_id, saved_signal):
    """RULE 2 -- the expected EXISTING ``routed_signal_id``.

    Derived through the installed ``interview_routed_signal_id()`` over the
    installed ``routed_concern_fingerprint()`` of the same material.  NOT a
    second identity algorithm, NOT an alias, NOT a parallel routing store.
    """
    probe = stop_closure_probe(package_scope_id, saved_signal)
    fingerprint = sha256_hex(
        canonical_json({"v": "nh-interview-routed-concern-v1", **probe})
    )
    return "rs_" + sha256_hex(
        canonical_json(
            [
                "nh-interview-routed-signal-v3",
                package_scope_id,
                saved_signal["issue_key"],
                saved_signal["finding_key"],
                constants.STOP_REVIEW_SIGNAL_SOURCE,
                None,
                None,
                fingerprint,
            ]
        )
    )[:32]


def stop_closure_expected_record(
    package_scope_id, saved_signal, *, package_key, package_id, scope_root_path
):
    """RULE 1 -- the COMPLETE expected ``review_signal_recorded`` material.

    Reconstructed from the EXACT saved STOP bytes plus the controller-proved
    package/scope binding.  It is the EXISTING probe object the existing carrier
    already builds; no new material is invented, and every already-governing
    identity/scope field is included so that a record agreeing only on the
    deterministic keys can never be mistaken for this one.
    """
    probe = stop_closure_probe(package_scope_id, saved_signal)
    return {
        "type": constants.STOP_CLOSURE_CARRIER_EVENT_TYPE,
        "routed_signal_id": stop_closure_routed_signal_id(
            package_scope_id, saved_signal
        ),
        "signal_source": constants.STOP_REVIEW_SIGNAL_SOURCE,
        "route": STOP_REVIEW_SIGNAL_ROUTE,
        "package_key": package_key,
        "package_id": package_id,
        "package_scope_id": package_scope_id,
        "scope_root_path": scope_root_path,
        "candidate_path": None,
        "candidate_sha256": None,
        "candidate_bytes": None,
        "issue_key": probe["issue_key"],
        "finding_key": probe["finding_key"],
        "signal_title": probe["signal_title"],
        "source_evidence": probe["source_evidence"],
        "finding_evidence": probe["finding_evidence"],
    }


def stop_closure_match(events, expected, custody_event_seq):
    """RULES 3-5 -- ``(exact, conflicting)``, ORDER-BOUND.

    RULE 3, FULL MATERIAL EQUALITY.  Identity agreement alone does not close.
    EVERY reconstructed field must equal the candidate record's field, field for
    field.  Matching issue key, finding key and scope is NOT SUFFICIENT.

    RULE 4, CORRECT ORDER.  A closing record must stand AFTER the exact owning
    STOP custody event.  An identical signal that exists ONLY BEFORE that custody
    event does NOT close this STOP -- it is a different, earlier act, and
    counting it would fabricate a completion this STOP never received.  The order
    test is applied BEFORE anything is counted, in either bucket.

    RULE 5's inputs.  A post-custody record carrying the same identity, or the
    same governing keys, but DIFFERENT material is CONFLICTING, not absent.
    """
    exact, conflicting = [], []
    for event in events:
        if event.get("type") != constants.STOP_CLOSURE_CARRIER_EVENT_TYPE:
            continue
        if event.get("event_seq", 0) <= custody_event_seq:
            continue
        if all(event.get(key) == value for key, value in expected.items()):
            exact.append(event)
            continue
        same_identity = event.get("routed_signal_id") == expected["routed_signal_id"]
        same_keys = (
            event.get("signal_source") == expected["signal_source"]
            and event.get("package_scope_id") == expected["package_scope_id"]
            and event.get("issue_key") == expected["issue_key"]
            and event.get("finding_key") == expected["finding_key"]
        )
        if same_identity or same_keys:
            conflicting.append(event)
    return exact, conflicting


def stop_closure_match_state(events, expected, custody_event_seq):
    """RULES 5 and 7 -- ``"durable"`` / ``"owed"`` / ``"contradiction"``.

    RULE 5, EXACTLY ONE CLOSES.  Two or more post-custody records carrying that
    identity, or carrying the same reconstructed material, are contradictory and
    FAIL CLOSED: the controller refuses rather than choosing between them, and
    appends nothing.

    RULE 7.  The one re-proved record IS the durable downstream completion of
    that STOP custody, as ``candidate_custody_recorded`` is for a CANDIDATE one.
    """
    exact, conflicting = stop_closure_match(events, expected, custody_event_seq)
    if conflicting or len(exact) > 1:
        return "contradiction"
    if exact:
        return "durable"
    return "owed"


STATE_BINDING_LABEL = "NH_SUPERVISOR_STATE_BINDING_V1"

STATE_BINDING_KEYS = (
    "controller_executable_identity",
    "package_scope_id",
    "source_binding_sha256",
    "candidate_path",
    "candidate_sha256",
    "candidate_bytes",
    "workflow_state",
    "next_command",
    "work_item_identity",
    "dependency_identity",
    "authenticated_event_seq",
    "authenticated_tail_sha256",
)

# -- Section 7.4 -- the two ACCEPTANCE explanation stages -------------------
# The discriminator is REQUIRED and never inferred (Section 7.2): a record
# that does not carry one of these values is not an acceptance explanation,
# whatever else it resembles.  A correction-stage record, and every record
# written before the discriminator existed, carries none of them and is
# therefore never read as one (Section 7.3).
ACCEPTANCE_EXPLANATION_STAGES = ("content_fixed", "acceptance_offer")

# The stage an offer is ever computed from.  A content-stage record is never
# promoted to it and never substituted for it (Section 7.3).
FINAL_ACCEPTANCE_EXPLANATION_STAGE = "acceptance_offer"

# -- Section 11.3 gate 11d -- the binding an owning operation shares --------
# The package scope, the source and the candidate: exactly the Section 8.2
# groups that BOTH the operation events and the substantive events carry.
# The per-event running digests and the correction-round counters are
# deliberately absent -- they are bookkeeping that moves inside one
# operation, not part of what the operation is bound to.
EFFECT_OWNER_BINDING_KEYS = (
    "package_key",
    "package_scope_id",
    "package_id",
    "branch",
    "head_sha",
    "source_binding_sha256",
    "candidate_path",
    "candidate_sha256",
    "candidate_bytes",
)


def state_binding_projection(**values):
    missing = sorted(set(STATE_BINDING_KEYS) - set(values))
    extra = sorted(set(values) - set(STATE_BINDING_KEYS))
    if missing or extra:
        raise ValueError(
            "the state binding projection has exactly twelve keys "
            "(missing %s, extra %s)" % (missing, extra)
        )
    return {key: values[key] for key in STATE_BINDING_KEYS}


def state_binding_digest(projection):
    return sha256_hex(canonical_json([STATE_BINDING_LABEL, projection]))


def tail_identity(events):
    """``(authenticated_event_seq, authenticated_tail_sha256)`` for a prefix."""
    if not events:
        return 0, None
    return events[-1]["event_seq"], events[-1]["event_sha256"]


def _is(event, kind):
    return event.get("type") == kind


def of_type(events, kind):
    return [event for event in events if event.get("type") == kind]


def explanation_version_of(event):
    """The record's ``explanation_version`` when it is rankable, else None.

    Section 7.5 orders explanations by an integer version.  A value that is
    not one cannot be ordered against another, so it is reported as absent
    here rather than compared -- a replay that guessed an order would be
    choosing silently, which rule 3 forbids.
    """
    version = event.get("explanation_version")
    if isinstance(version, int) and not isinstance(version, bool):
        return version
    return None


def is_supervisor_era_version(version):
    """True for a SUPPORTED journal version that carries supervisor events.

    Version 5 is the FIRST supervisor-capable version, not the only one: every
    supported version from 5 onward carries the supervisor event types too.
    An unsupported version is never valid here, so widening the supported set
    is the single place a new version is admitted.
    """
    return (
        isinstance(version, int)
        and not isinstance(version, bool)
        and version >= 5
        and version in constants.INTERVIEW_JOURNAL_SUPPORTED_VERSIONS
    )


class DownstreamOwnershipError(ValueError):
    """Two records both claim to close one custody: refused, never chosen."""


class Replay:
    """One authenticated event list, projected.

    Constructed with the complete authenticated event list for the state
    directory and one ``package_scope_id``.  Only supervisor events -- those
    recorded at version 5 or any later supported version -- and the three
    candidate-custody events are read; Piece-3 standing is not this module's
    business.
    """

    def __init__(self, events, package_scope_id=None):
        self.events = list(events)
        self.package_scope_id = package_scope_id
        self._scoped = [
            event
            for event in self.events
            if package_scope_id is None
            or event.get("package_scope_id") in (None, package_scope_id)
        ]

    # -- basic accessors ----------------------------------------------------
    def scoped(self, kind=None):
        if kind is None:
            return list(self._scoped)
        return [event for event in self._scoped if event.get("type") == kind]

    def by_seq(self, event_seq):
        for event in self.events:
            if event["event_seq"] == event_seq:
                return event
        return None

    def tail(self):
        return tail_identity(self.events)

    # -- Section 4.6 -- dispatch serial and closed attempts ------------------
    def closed_attempt_request_identities(self, work_item, provider_kind, episode):
        found = []
        for event in self.scoped("provider_request_terminal_recorded"):
            if (
                event.get("work_item_identity") == work_item
                and event.get("provider_kind") == provider_kind
                and event.get("provider_availability_episode_identity") == episode
            ):
                identity = event.get("provider_request_identity")
                if identity not in found:
                    found.append(identity)
        return sorted(found)

    def closed_attempt_count(self, work_item, provider_kind, episode):
        return len(self.closed_attempt_request_identities(work_item, provider_kind, episode))

    def provider_dispatch_serial(self, work_item, provider_kind, episode):
        return 1 + self.closed_attempt_count(work_item, provider_kind, episode)

    # -- Section 4.10 -- episode generation ---------------------------------
    def episode_generation(self, work_item, provider_kind, endpoint):
        count = 0
        for event in self.scoped("provider_availability_unlock_recorded"):
            if (
                event.get("work_item_identity") == work_item
                and event.get("provider_kind") == provider_kind
                and event.get("provider_endpoint_identity") == endpoint
                and event.get("unlock_accepted") is True
            ):
                count += 1
        return 1 + count

    def episode_identity(self, work_item, provider_kind, endpoint, generation=None):
        if generation is None:
            generation = self.episode_generation(work_item, provider_kind, endpoint)
        return derive(
            "provider_availability_episode_identity",
            {
                "work_item_identity": work_item,
                "provider_kind": provider_kind,
                "provider_endpoint_identity": endpoint,
                "episode_generation": generation,
            },
        )

    def automatic_episode_unlocks_used(self, work_item, provider_kind, endpoint):
        count = 0
        for event in self.scoped("provider_availability_unlock_recorded"):
            if (
                event.get("work_item_identity") == work_item
                and event.get("provider_kind") == provider_kind
                and event.get("provider_endpoint_identity") == endpoint
                and event.get("unlock_accepted") is True
                and event.get("unlock_invocation_kind") == "automatic_controller_evidence"
            ):
                count += 1
        return count

    # -- Section 11.2 -- provider phase -------------------------------------
    _PHASE_EVENT = {
        "provider_request_prepared": "prepared",
        "provider_dispatch_begun": "dispatch_begun",
        "provider_request_accepted": "accepted",
        "provider_result_custody_recorded": "result_custodied",
        "provider_request_terminal_recorded": "terminal",
    }

    def provider_phase(self, request_identity):
        best = "none"
        for event in self._scoped:
            phase = self._PHASE_EVENT.get(event.get("type"))
            if phase is None:
                continue
            if event.get("provider_request_identity") != request_identity:
                continue
            if constants.PROVIDER_PHASE_ORDER[phase] > constants.PROVIDER_PHASE_ORDER[best]:
                best = phase
        return best

    def terminal_event(self, request_identity):
        found = [
            event
            for event in self.scoped("provider_request_terminal_recorded")
            if event.get("provider_request_identity") == request_identity
        ]
        if not found:
            return None
        return found[-1]

    def terminal_events(self, request_identity):
        return [
            event
            for event in self.scoped("provider_request_terminal_recorded")
            if event.get("provider_request_identity") == request_identity
        ]

    def custody_events(self, request_identity):
        return [
            event
            for event in self.scoped("provider_result_custody_recorded")
            if event.get("provider_request_identity") == request_identity
        ]

    def custody_event(self, request_identity):
        found = self.custody_events(request_identity)
        return found[-1] if found else None

    def prepared_event(self, request_identity):
        found = [
            event
            for event in self.scoped("provider_request_prepared")
            if event.get("provider_request_identity") == request_identity
        ]
        return found[-1] if found else None

    def dispatch_event(self, request_identity):
        found = [
            event
            for event in self.scoped("provider_dispatch_begun")
            if event.get("provider_request_identity") == request_identity
        ]
        return found[-1] if found else None

    def acceptance_event(self, request_identity):
        found = [
            event
            for event in self.scoped("provider_request_accepted")
            if event.get("provider_request_identity") == request_identity
        ]
        return found[-1] if found else None

    def reconciliation_events(self, request_identity):
        return [
            event
            for event in self.scoped("provider_request_reconciled")
            if event.get("provider_request_identity") == request_identity
        ]

    def open_provider_requests(self):
        """Requests in phase prepared/dispatch_begun/accepted/result_custodied."""
        identities = []
        for event in self._scoped:
            if event.get("type") not in self._PHASE_EVENT:
                continue
            identity = event.get("provider_request_identity")
            if identity and identity not in identities:
                identities.append(identity)
        abandoned = {
            event.get("provider_request_identity")
            for event in self._scoped
            if event.get("type") == "ness_transition_recovery_choice_recorded"
            and event.get("recovery_action") == "abandon_and_replace_once"
            and event.get("ness_action_confirmed") is True
        }
        open_identities = [
            identity
            for identity in identities
            if self.provider_phase(identity) != "terminal" and identity not in abandoned
        ]
        # Include closed/abandoned later requests in the comparison: their
        # existence is still the durable proof that an older prepared-only
        # residue was superseded before it ever left the machine.
        prepared_by_identity = {
            identity: self.prepared_event(identity) for identity in identities
        }
        same_material_keys = (
            "provider_kind",
            "package_scope_id",
            "source_binding_sha256",
            "prompt_material_sha256",
            "required_inputs_sha256",
            "result_schema_id",
        )
        return [
            identity
            for identity in open_identities
            if not (
                self.provider_phase(identity) == "prepared"
                and any(
                    other is not None
                    and prepared_by_identity[identity] is not None
                    and other.get("event_seq", 0)
                    > prepared_by_identity[identity].get("event_seq", 0)
                    and all(
                        other.get(key) == prepared_by_identity[identity].get(key)
                        for key in same_material_keys
                    )
                    for other_identity, other in prepared_by_identity.items()
                    if other_identity != identity
                )
            )
        ]

    def custodied_results_awaiting_processing(self):
        """Custody records whose Section 9.7 continuation has not finished."""
        pending = []
        for event in self.scoped("provider_result_custody_recorded"):
            request = event.get("provider_request_identity")
            terminal = self.terminal_event(request)
            if terminal is None:
                pending.append(event)
                continue
            if self._downstream_recorded(event, terminal):
                continue
            pending.append(event)
        return pending

    def _initial_design_transaction_closed(self, custody_event):
        """True when THIS initial-design result's own candidate is committed.

        The join is the produced candidate identity the custodied result itself
        declares.  Zero exact matches leaves the custody pending; exactly one
        closes it; two or more are contradictory and are refused rather than
        chosen between.
        """
        produced = self._produced_candidate_of(custody_event)
        if produced is None:
            # Anchored result bytes are deliberately outside Replay.  In that
            # storage form, join through the authenticated processing operation
            # instead: one exact work-item start, one initial candidate
            # transaction inside its event window, and its successful matching
            # completion.  No filename or chronology alone is sufficient.
            if custody_event.get("result_location_kind") != "anchored_result_object":
                return False
            work_item = custody_event.get("work_item_identity")
            matches = []
            for completed in self.scoped("supervisor_operation_completed"):
                if (
                    completed.get("supervisor_command")
                    != "process-custodied-provider-result"
                    or completed.get("work_item_identity") != work_item
                    or completed.get("operation_outcome") != "ok"
                ):
                    continue
                starts = [
                    event
                    for event in self.scoped("supervisor_operation_started")
                    if event.get("supervisor_operation_id")
                    == completed.get("supervisor_operation_id")
                    and event.get("event_seq")
                    == completed.get("supervisor_started_event_seq")
                    and event.get("work_item_identity") == work_item
                ]
                if len(starts) != 1:
                    continue
                start = starts[0]
                committed = [
                    event
                    for event in self.scoped("candidate_custody_recorded")
                    if start["event_seq"] < event.get("event_seq", 0)
                    < completed["event_seq"]
                    and event.get("package_scope_id")
                    == custody_event.get("package_scope_id")
                    and event.get("custody_origin")
                    in (
                        constants.CANDIDATE_CUSTODY_ORIGIN_INITIAL,
                        constants.CANDIDATE_CUSTODY_ORIGIN_RECOVERED,
                    )
                ]
                for candidate in committed:
                    opened = [
                        intent
                        for intent in self.scoped("candidate_write_ahead_recorded")
                        if start["event_seq"] < intent.get("event_seq", 0)
                        < candidate["event_seq"]
                        and intent.get("intent_origin")
                        == constants.CANDIDATE_INTENT_ORIGIN_INITIAL
                        and intent.get("candidate_path")
                        == candidate.get("candidate_path")
                        and intent.get("candidate_sha256")
                        == candidate.get("candidate_sha256")
                        and intent.get("candidate_bytes")
                        == candidate.get("candidate_bytes")
                    ]
                    if len(opened) == 1:
                        matches.append(candidate)
            if len(matches) > 1:
                raise DownstreamOwnershipError(
                    "more than one committed initial candidate matches one "
                    "anchored initial-design processing operation"
                )
            return len(matches) == 1
        matches = []
        for event in self.scoped("candidate_custody_recorded"):
            # v1_11 section 18 Rows L / M.  The ONE first candidate transaction
            # has TWO truthful custody outcomes: the normal
            # CANDIDATE_CUSTODY_ORIGIN_INITIAL, and -- where the crash fell
            # between promotion and custody -- the installed stranded recovery's
            # CANDIDATE_CUSTODY_ORIGIN_RECOVERED.  Row L says B8 commits exactly
            # one recovered custody; Row M says once candidate_custody_recorded
            # is durable the initial-design provider custody HAS its downstream
            # completion.  Recognising only the first left a real B8 completion
            # looking like unfinished work for ever.
            #
            # RECOVERED IS NOT GLOBALLY INITIAL.  It is also the ordinary
            # recovery origin for a LATER correction candidate, and such a
            # custody must never close an initial-design result.  What makes it
            # admissible here is NOT the origin string: it is the MATCHING
            # INITIAL WRITE-AHEAD proved just below, against this exact produced
            # candidate identity.  Both forms pass through that same proof.
            if event.get("custody_origin") not in (
                constants.CANDIDATE_CUSTODY_ORIGIN_INITIAL,
                constants.CANDIDATE_CUSTODY_ORIGIN_RECOVERED,
            ):
                continue
            if (
                event.get("candidate_path") != produced["path"]
                or event.get("candidate_sha256") != produced["sha256"]
                or event.get("candidate_bytes") != produced["bytes"]
            ):
                continue
            # The write-ahead that opened this commit must name the same
            # candidate identity and the initial intent origin.
            opened = [
                intent
                for intent in self.scoped("candidate_write_ahead_recorded")
                if intent.get("intent_origin")
                == constants.CANDIDATE_INTENT_ORIGIN_INITIAL
                and intent.get("candidate_path") == produced["path"]
                and intent.get("candidate_sha256") == produced["sha256"]
                and intent.get("candidate_bytes") == produced["bytes"]
            ]
            if not opened:
                continue
            matches.append(event)
        if len(matches) > 1:
            raise DownstreamOwnershipError(
                "%d committed initial candidates match one initial-design "
                "result: refused, and neither is chosen" % len(matches)
            )
        return len(matches) == 1

    # -- accepted role-split v1_6 section 6.5 ``STOP-CLOSURE-EXACT`` ----------
    #
    # THE ONE DEFINITION, read side and write side alike.  The pure rules live
    # at module level below (``stop_closure_expected_record()`` and
    # ``stop_closure_match()``); these three methods are the only thing that
    # binds them to one custody record, and ``commands.py`` calls the SAME
    # module-level functions rather than restating them.  There is no second,
    # weaker or approximate copy of this rule anywhere.
    def stop_result_signal(self, custody_event):
        """The five-key review signal a custodied STOP declares, or None.

        ``None`` means "not provably a STOP", never "not a STOP": a custody this
        function cannot read is left to the existing candidate rules, which keep
        it PENDING.  Nothing is assumed from unreadable bytes.

        A STOP body is bounded far below ``MAX_INLINE_RESULT_BYTES`` and the
        dispatcher refuses to emit one that is not, so a STOP custody is always
        ``inline_journal_bytes`` and this can always read a real one.
        """
        if custody_event.get("work_item_kind") != "initial_design":
            return None
        if custody_event.get("result_location_kind") != "inline_journal_bytes":
            return None
        encoded = custody_event.get("result_bytes_base64")
        if not isinstance(encoded, str):
            return None
        try:
            payload = base64.b64decode(encoded.encode("ascii"))
            value = json.loads(payload.decode("utf-8"))
        except Exception:  # noqa: BLE001 -- unreadable proves nothing
            return None
        if not isinstance(value, dict):
            return None
        if set(value) != set(constants.INITIAL_DESIGN_STOP_RESULT_KEYS):
            return None
        if (
            value.get("result_schema_id")
            != constants.INITIAL_DESIGN_STOP_RESULT_SCHEMA_ID
            or value.get("result_schema_version")
            != constants.INITIAL_DESIGN_STOP_RESULT_VERSION
        ):
            return None
        signal = value.get("stop_review_signal")
        if not isinstance(signal, dict):
            return None
        if set(signal) != set(constants.REVIEW_SIGNAL_KEYS):
            return None
        return signal

    def stop_closure_binding_fields(self, package_scope_id):
        """The scope's IA package identity, from its ANCHOR validation, or None.

        These are EXACTLY the three fields accepted v1_11 binding 3 takes from
        ``anchor = q_validations[0]`` -- ``package_key``, ``package_id`` and
        ``package_source_binding.scope_root_path`` -- so the values this derives
        are the values the initial-design context was bound to, and therefore the
        values ``record_review_signal()`` wrote.  Deriving them here is what lets
        the read side and the write side build ONE identical expectation.

        ``anchor_validation(S)`` is the EARLIEST ``validation_recorded`` in S,
        exactly as ``scope_anchor_validations()`` defines it.
        """
        if not package_scope_id:
            return None
        for event in self.events:
            if event.get("type") != "validation_recorded":
                continue
            if event.get("package_scope_id") != package_scope_id:
                continue
            root = (event.get("package_source_binding") or {}).get("scope_root_path")
            if not root:
                return None
            return {
                "package_key": event.get("package_key"),
                # A null package_id is a REAL value, not an absence.
                "package_id": event.get("package_id"),
                "scope_root_path": root,
            }
        return None

    def stop_closure_state(self, custody_event):
        """``"durable"`` / ``"owed"`` / ``"contradiction"`` / ``None``.

        ``None`` means "this custody is not provably a STOP", and the caller then
        applies the unchanged candidate rules.  Every other value is the accepted
        section 6.5 verdict, computed by the ONE shared rule.
        """
        signal = self.stop_result_signal(custody_event)
        if signal is None:
            return None
        scope = custody_event.get("package_scope_id")
        custody_seq = custody_event.get("event_seq")
        if not scope or not isinstance(custody_seq, int):
            return "contradiction"
        fields = self.stop_closure_binding_fields(scope)
        if fields is None:
            # The scope's own anchor cannot be read, so the expectation cannot
            # be built.  A derivation that cannot be performed FAILS CLOSED; it
            # is never read as "already closed".
            return "contradiction"
        expected = stop_closure_expected_record(scope, signal, **fields)
        return stop_closure_match_state(self.events, expected, custody_seq)

    def _produced_candidate_of(self, custody_event):
        """The candidate identity this custodied initial-design result declares."""
        if custody_event.get("result_location_kind") != "inline_journal_bytes":
            # An anchored result is re-read by the controller, not by replay.
            return None
        encoded = custody_event.get("result_bytes_base64")
        if not isinstance(encoded, str):
            return None
        try:
            payload = base64.b64decode(encoded.encode("ascii"))
            value = json.loads(payload.decode("utf-8"))
        except Exception:  # noqa: BLE001 -- unreadable proves nothing
            return None
        if not isinstance(value, dict):
            return None
        if set(value) != set(constants.INITIAL_DESIGN_RESULT_KEYS):
            return None
        return {
            "path": value.get("produced_candidate_path"),
            "sha256": value.get("produced_candidate_sha256"),
            "bytes": value.get("produced_candidate_bytes"),
        }

    def _same_call_explanation_recorded(self, custody_event):
        """Whether the candidate call's bound content-stage prose is durable."""
        request = custody_event.get("provider_request_identity")
        work_item = custody_event.get("work_item_identity")
        matches = [
            event
            for event in self.acceptance_explanation_events(
                constants.EXPLANATION_STAGE_CONTENT
            )
            if event.get("provider_request_identity") == request
            and event.get("work_item_identity") == work_item
            and event.get("explanation_content_digest")
        ]
        return len(matches) == 1

    def _downstream_recorded(self, custody_event, terminal_event):
        """True when the custodied result already produced its downstream state."""
        request = custody_event.get("provider_request_identity")
        kind = custody_event.get("work_item_kind")
        # v1_8 section 7.6a CLOSURE-READONLY.  Consulted BEFORE the
        # downstream_types lookup.  The two read-only transition kinds owe NO
        # downstream effect append -- their custodied result IS the durable
        # output -- so a COMPLETED result_received terminal together with this
        # custody record is itself the closure.  Leaving them unmapped would
        # keep them pending forever (P-21); adding a downstream_types row would
        # be the wrong shape, because they owe no event.  They must never be
        # routed through process-custodied-provider-result to manufacture an
        # effect that did not happen.
        if kind == "initial_design":
            # ACCEPTED ROLE-SPLIT v1_6 section 6.5 -- THE STOP ARM'S OWN CLOSURE.
            #
            # v1_11 section 7.6a CLOSURE-INITIAL-PENDING names
            # ``candidate_custody_recorded`` as the downstream effect of an
            # ``initial_design`` custody.  A STOP produces NO CANDIDATE, so that
            # effect can never arrive and the custody would stay pending for
            # ever.  v1_6 supersedes that clause ONLY where
            # ``candidate_custody_recorded`` is the SOLE closure: a STOP closes
            # through the EXISTING ``review_signal_recorded`` carrier instead.
            #
            # This is consulted FIRST and is strictly narrow.  It fires ONLY for
            # a custody whose saved bytes provably carry the exact three-key
            # ``NH_LOCAL_INITIAL_DESIGN_STOP_RESULT_V1`` shape.  For EVERY other
            # initial-design custody -- every CANDIDATE result, historical or
            # new -- ``stop_closure_state()`` returns None and the installed
            # candidate rules below run UNCHANGED, byte for byte.
            #
            # CLOSURE-READONLY and every other section 7.6a rule remain, and no
            # new event type is created.
            stop_state = self.stop_closure_state(custody_event)
            if stop_state is not None:
                # "durable" closes; "owed" stays pending; "contradiction" also
                # stays pending, so a duplicated or contradicted closure is NEVER
                # read as a completion -- it fails closed here exactly as it
                # fails closed on the processing side.
                return stop_state == "durable"

            # v1_8 section 7.6a CLOSURE-INITIAL-PENDING, proved READ-SIDE and
            # PER TRANSACTION.
            #
            # The closure IS ``candidate_custody_recorded``.  That record's body
            # key set is exact and closed -- it carries no request or work-item
            # identity -- and section 7.6 forbids adding one, so ownership is
            # proved from the fields these records genuinely have.
            #
            # SAME SCOPE AND INITIAL ORIGIN ARE NOT SUFFICIENT.  A stale earlier
            # initial-design result must not be closed merely because some later
            # initial candidate committed in the same Q scope, so the custody's
            # own PRODUCED CANDIDATE IDENTITY -- path, digest and byte length,
            # taken from the admitted result -- must match the committed
            # candidate exactly, and the write-ahead that opened that commit must
            # name the same identity.
            candidate_closed = self._initial_design_transaction_closed(custody_event)
            if custody_event.get("result_schema_id") == (
                "NH_CLAUDE_INITIAL_DESIGN_RESULT_V2"
            ):
                return candidate_closed and self._same_call_explanation_recorded(
                    custody_event
                )
            return candidate_closed
        if kind in constants.CLOSED_BY_TERMINAL_ONLY_WORK_ITEM_KINDS:
            if terminal_event.get("terminal_kind") == "result_received":
                return True
            # A result_invalid terminal still closes by itself, exactly as the
            # installed rule below does for every other kind.
            return terminal_event.get("terminal_kind") == "result_invalid"
        if terminal_event.get("terminal_kind") == "result_invalid":
            # B6i already closed it: the terminal itself is the closure and, for
            # a diagnosis, its validation-failure event.
            if kind == "correction_diagnosis":
                return any(
                    event.get("provider_request_identity") == request
                    for event in self.scoped(
                        "correction_diagnosis_validation_failed_recorded"
                    )
                )
            return True
        if (
            kind == "design_audit"
            and custody_event.get("result_schema_id") == "NH_DESIGN_AUDIT_RESULT_V2"
        ):
            unusable = [
                event
                for event in self.scoped("mechanical_audit_unusable_recorded")
                if event.get("provider_request_identity") == request
            ]
            if unusable:
                return len(unusable) == 1
            audits = [
                event
                for event in self.scoped("mechanical_audit_recorded")
                if event.get("provider_request_identity") == request
            ]
            if len(audits) != 1:
                return False
            mechanical = audits[0].get("mechanical_blocker_refs") or []
            lifetime = self.correction_round_lifetime()
            at_batch_bound = (
                lifetime > 0
                and batch_triple(lifetime)[2] == constants.CORRECTION_BATCH_SIZE
            )
            if not mechanical or at_batch_bound:
                return True
            specifications = [
                event
                for event in self.scoped("correction_specification_recorded")
                if event.get("provider_request_identity") == request
                and event.get("audit_identity") == audits[0].get("audit_identity")
            ]
            return len(specifications) == 1
        if (
            kind == "correction_apply"
            and custody_event.get("result_schema_id")
            == "NH_CLAUDE_CORRECTION_RESULT_V2"
        ):
            # No-progress and terminated paths create no candidate that could
            # reach acceptance.  A successful candidate path is closed only
            # after BOTH its consumption completion and its same-call prose are
            # durable, so a crash between them re-enters local processing and
            # never launches another provider.
            if any(
                event.get("provider_request_identity") == request
                for event_type in (
                    "mechanical_no_progress_recorded",
                    "diagnosis_strategy_consumption_terminated",
                )
                for event in self.scoped(event_type)
            ):
                return True
            completed = any(
                event.get("provider_request_identity") == request
                for event in self.scoped("diagnosis_strategy_consumption_completed")
            )
            return completed and self._same_call_explanation_recorded(custody_event)
        if kind == "correction_diagnosis":
            request_events = [
                event
                for event in self.scoped("correction_diagnosis_recorded")
                if event.get("provider_request_identity") == request
            ]
            if request_events:
                diagnosis = request_events[-1]
                if diagnosis.get("diagnosis_outcome") != "possible_ness_choice":
                    return True
                return self.possible_ness_transaction(
                    custody_event, terminal_event
                )["complete"]
            return any(
                event.get("provider_request_identity") == request
                for kind_name in (
                    "correction_diagnosis_rejected_recorded",
                    "correction_diagnosis_validation_failed_recorded",
                )
                for event in self.scoped(kind_name)
            )
        downstream_types = {
            "design_audit": (
                "mechanical_audit_recorded",
                "mechanical_audit_unusable_recorded",
            ),
            "correction_specification": ("correction_specification_recorded",),
            "correction_apply": (
                "diagnosis_strategy_consumption_completed",
                "diagnosis_strategy_consumption_terminated",
                "mechanical_no_progress_recorded",
                "candidate_custody_recorded",
            ),
            "change_explanation_review": ("mechanical_change_explanation_recorded",),
            # Section 14 Phase A step A2 -- the preparation result is consumed
            # by exactly one downstream append: the CONTENT-STAGE acceptance
            # explanation, carried by the same registered type.  Without this
            # row the custody of a processed preparation result would never be
            # proved closed and the loop would re-enter processing forever.
            "acceptance_explanation_content": (
                "mechanical_change_explanation_recorded",
            ),
            "question_validation": ("piece3_provider_work_recorded",),
            "coverage_review": ("piece3_provider_work_recorded",),
            # v1_8 section 7.6a CLOSURE-INITIAL-PENDING.  initial_design is
            # deliberately DIFFERENT from the two read-only kinds: its valid
            # custody REMAINS awaiting processing until the candidate
            # transaction proves its downstream completion.  This is the same
            # shape the installed correction_apply row already uses, and the
            # match below accepts either provider_request_identity or
            # work_item_identity, exactly as correction_apply does.
            "initial_design": ("candidate_custody_recorded",),
        }.get(kind, ())
        for event_type in downstream_types:
            for event in self.scoped(event_type):
                if event.get("provider_request_identity") == request:
                    return True
                if event_type == "candidate_custody_recorded" and event.get(
                    "work_item_identity"
                ) == custody_event.get("work_item_identity"):
                    return True
        # The Section 5.1 collision route closes through the operation completion
        # carrying the row-C21 occurrence rather than through an audit event.
        if kind == "design_audit" and self.collision_closure_completion(request) is not None:
            return True
        return False

    @staticmethod
    def _canonical_stored_signal(value):
        keys = {
            "issue_key",
            "finding_key",
            "signal_title",
            "finding_evidence",
            "source_evidence",
        }
        if not isinstance(value, dict) or set(value) != keys:
            return None
        if not isinstance(value.get("finding_evidence"), list) or not isinstance(
            value.get("source_evidence"), list
        ):
            return None
        if not all(
            isinstance(value.get(key), str) and value.get(key)
            for key in ("issue_key", "finding_key", "signal_title")
        ) or not all(
            isinstance(item, str) and item
            for item in value["finding_evidence"] + value["source_evidence"]
        ):
            return None
        try:
            sources = sorted(set(value["source_evidence"]))
        except TypeError:
            return None
        return {
            "issue_key": value["issue_key"],
            "finding_key": value["finding_key"],
            "signal_title": value["signal_title"],
            "finding_evidence": list(value["finding_evidence"]),
            "source_evidence": sources,
        }

    def _route_matches_possible_diagnosis(self, route, diagnosis):
        signal = self._canonical_stored_signal(diagnosis.get("review_signal"))
        if signal is None:
            return False
        fixed = {
            "signal_source": "correction_diagnosis_review",
            "route": "chatgpt_review_required",
            "package_key": diagnosis.get("package_key"),
            "package_id": diagnosis.get("package_id"),
            "package_scope_id": diagnosis.get("package_scope_id"),
            "candidate_path": diagnosis.get("candidate_path"),
            "candidate_sha256": diagnosis.get("candidate_sha256"),
            "candidate_bytes": diagnosis.get("candidate_bytes"),
            "branch": diagnosis.get("branch"),
            "head_sha": diagnosis.get("head_sha"),
            "source_binding_sha256": diagnosis.get("source_binding_sha256"),
        }
        if route.get("type") != "review_signal_recorded":
            return False
        if any(route.get(key) != expected for key, expected in fixed.items()):
            return False
        return all(route.get(key) == expected for key, expected in signal.items())

    def possible_ness_transaction(self, custody_event, terminal_event=None):
        """Pure journal-only relation J for one correction-diagnosis custody."""
        request = custody_event.get("provider_request_identity")
        terminal_event = terminal_event or self.terminal_event(request)
        problems = []
        diagnoses = [
            event
            for event in self.scoped("correction_diagnosis_recorded")
            if event.get("provider_request_identity") == request
        ]
        if len(diagnoses) > 1:
            problems.append("two diagnosis successes exist for request %s" % request)
        diagnosis = diagnoses[0] if len(diagnoses) == 1 else None
        if diagnosis is None or diagnosis.get("diagnosis_outcome") != (
            "possible_ness_choice"
        ):
            return {
                "complete": False,
                "diagnosis": diagnosis,
                "route": None,
                "start": None,
                "completion": None,
                "order": None,
                "problems": problems,
            }

        if not is_hex64(diagnosis.get("diagnosis_result_sha256")) or (
            self._canonical_stored_signal(diagnosis.get("review_signal")) is None
        ):
            problems.append("the possible-Ness diagnosis payload is not well shaped")

        linkage = {
            "provider_request_identity": request,
            "result_custody_identity": custody_event.get("result_custody_identity"),
            "work_item_identity": custody_event.get("work_item_identity"),
            "provider_kind": custody_event.get("provider_kind"),
            "package_scope_id": custody_event.get("package_scope_id"),
            "source_binding_sha256": custody_event.get("source_binding_sha256"),
            "candidate_path": custody_event.get("candidate_path"),
            "candidate_sha256": custody_event.get("candidate_sha256"),
            "candidate_bytes": custody_event.get("candidate_bytes"),
        }
        if terminal_event is None or terminal_event.get("terminal_kind") != (
            "result_received"
        ):
            problems.append("the possible-Ness diagnosis has no received terminal")
        else:
            linkage["provider_terminal_event_seq"] = terminal_event.get("event_seq")
        if any(diagnosis.get(key) != value for key, value in linkage.items()):
            problems.append("the possible-Ness diagnosis does not bind its custody")

        routes = [
            event
            for event in self.scoped("review_signal_recorded")
            if event["event_seq"] > custody_event["event_seq"]
            and self._route_matches_possible_diagnosis(event, diagnosis)
        ]
        forward = [event for event in routes if event["event_seq"] < diagnosis["event_seq"]]
        legacy = [event for event in routes if event["event_seq"] > diagnosis["event_seq"]]
        route = None
        order = None
        if len(forward) == 1:
            route = forward[0]
            order = "forward"
            if legacy:
                problems.append("a diagnosis has both forward and legacy routes")
        elif len(forward) > 1:
            problems.append("a diagnosis has more than one forward route")
        elif len(legacy) == 1:
            route = legacy[0]
            order = "legacy"
        elif len(legacy) > 1:
            problems.append("a diagnosis has more than one legacy route")

        if route is not None:
            claims = 0
            for other in self.scoped("correction_diagnosis_recorded"):
                if other.get("diagnosis_outcome") != "possible_ness_choice":
                    continue
                other_custody = self.custody_event(
                    other.get("provider_request_identity")
                )
                if other_custody is None or route["event_seq"] <= other_custody[
                    "event_seq"
                ]:
                    continue
                if self._route_matches_possible_diagnosis(route, other):
                    claims += 1
            if claims != 1:
                problems.append("one routed event ambiguously matches %d diagnoses" % claims)

        starts = []
        if diagnosis is not None:
            for event in self.scoped("supervisor_operation_started"):
                if event.get("supervisor_command") != (
                    "process-custodied-provider-result"
                ):
                    continue
                if not (
                    custody_event["event_seq"] < event["event_seq"] < diagnosis["event_seq"]
                ):
                    continue
                fields = (
                    "work_item_identity",
                    "package_scope_id",
                    "source_binding_sha256",
                    "candidate_path",
                    "candidate_sha256",
                    "candidate_bytes",
                )
                if all(event.get(key) == diagnosis.get(key) for key in fields):
                    starts.append(event)
        if len(starts) > 1:
            problems.append("a diagnosis continuation has more than one compatible start")
        start = starts[0] if len(starts) == 1 else None
        completions = []
        if start is not None:
            completions = [
                event
                for event in self.scoped("supervisor_operation_completed")
                if event.get("supervisor_operation_id")
                == start.get("supervisor_operation_id")
                and event.get("supervisor_started_event_seq") == start.get("event_seq")
                and event.get("work_item_identity")
                == custody_event.get("work_item_identity")
            ]
        if len(completions) > 1:
            problems.append("a diagnosis continuation has two matching completions")
        completion = completions[0] if len(completions) == 1 else None

        ordered = False
        if route is not None and start is not None and completion is not None:
            if order == "forward":
                ordered = (
                    custody_event["event_seq"]
                    < start["event_seq"]
                    < route["event_seq"]
                    < diagnosis["event_seq"]
                    < completion["event_seq"]
                )
            else:
                ordered = (
                    custody_event["event_seq"]
                    < start["event_seq"]
                    < diagnosis["event_seq"]
                    and (
                        diagnosis["event_seq"]
                        < route["event_seq"]
                        < completion["event_seq"]
                        or diagnosis["event_seq"]
                        < completion["event_seq"]
                        < route["event_seq"]
                    )
                )
            if not ordered:
                problems.append("the possible-Ness transaction has an invalid order")
        return {
            "complete": bool(ordered and not problems),
            "diagnosis": diagnosis,
            "route": route,
            "start": start,
            "completion": completion,
            "order": order,
            "problems": problems,
        }

    def collision_closure_completion(self, request_identity):
        """The C21-carrying completion of the Section 5.1 collision route."""
        for event in self.scoped("supervisor_operation_completed"):
            if event.get("supervisor_command") != "process-custodied-provider-result":
                continue
            record = event.get("dependency_record")
            identity = event.get("dependency_identity")
            if identity is None:
                continue
            code = None
            if isinstance(record, dict):
                code = record.get("dependency_code")
            else:
                carrier_seq = event.get("dependency_carrier_event_seq")
                carrier = self.by_seq(carrier_seq) if carrier_seq else None
                if isinstance(carrier, dict) and isinstance(
                    carrier.get("dependency_record"), dict
                ):
                    code = carrier["dependency_record"].get("dependency_code")
            if code != "custody_contradiction":
                continue
            if event.get("collision_request_identity") in (None, request_identity):
                # The completion belongs to the operation that processed this
                # exact custodied result; the operation's start names it.
                started = self.started_event(event.get("supervisor_operation_id"))
                if started is None:
                    continue
                custody = self.custody_event(request_identity)
                if custody is not None and started.get(
                    "work_item_identity"
                ) == custody.get("work_item_identity"):
                    return event
        return None

    # -- Section 11.7 -- the one output-retry convention --------------------
    def unusable_output_closure_count(self, work_item, provider_kind, episode):
        closures = set()
        for terminal in self.scoped("provider_request_terminal_recorded"):
            if (
                terminal.get("work_item_identity") != work_item
                or terminal.get("provider_kind") != provider_kind
                or terminal.get("provider_availability_episode_identity") != episode
            ):
                continue
            kind = terminal.get("terminal_kind")
            request = terminal.get("provider_request_identity")
            if kind in ("result_invalid", "result_oversize_uncustodied"):
                closures.add(request)
            elif kind == "result_received":
                if self._semantically_unusable(request):
                    closures.add(request)
        return len(closures)

    _UNUSABLE_CODES = frozenset(
        ("provider_output_invalid_bounded_retry", "provider_output_repeatedly_invalid")
    )

    def _semantically_unusable(self, request_identity):
        for event in self._scoped:
            if event.get("provider_request_identity") != request_identity:
                continue
            identity = event.get("dependency_identity")
            if identity is None:
                continue
            record = event.get("dependency_record")
            if record is None:
                carrier_seq = event.get("dependency_carrier_event_seq")
                carrier = self.by_seq(carrier_seq) if carrier_seq else None
                record = carrier.get("dependency_record") if carrier else None
            if isinstance(record, dict) and record.get("dependency_code") in (
                self._UNUSABLE_CODES
            ):
                return True
        return False

    def output_retries_used(self, work_item, provider_kind, episode):
        return max(0, self.unusable_output_closure_count(work_item, provider_kind, episode) - 1)

    def output_retries_remaining(self, work_item, provider_kind, episode):
        return max(
            0,
            constants.MAX_PROVIDER_OUTPUT_RETRIES_PER_EPISODE
            - self.output_retries_used(work_item, provider_kind, episode),
        )

    def bounded_output_retry_budget(self, work_item, provider_kind, episode):
        used = self.output_retries_used(work_item, provider_kind, episode)
        if used < constants.MAX_PROVIDER_OUTPUT_RETRIES_PER_EPISODE:
            return "available"
        return "exhausted"

    # -- Section 4.11 -- semantic scope -------------------------------------
    def semantic_unlock_generation(self):
        count = 0
        for event in self.scoped("semantic_scope_unlock_recorded"):
            if event.get("unlock_accepted") is True:
                count += 1
        return 1 + count

    def semantic_scope_key(
        self,
        package_scope_id,
        source_binding_sha256,
        candidate_path,
        candidate_sha256,
        candidate_bytes,
        blocking_finding_refs,
        generation=None,
    ):
        if generation is None:
            generation = self.semantic_unlock_generation()
        return derive(
            "semantic_scope_key",
            {
                "package_scope_id": package_scope_id,
                "source_binding_sha256": source_binding_sha256,
                "candidate_path": candidate_path,
                "candidate_sha256": candidate_sha256,
                "candidate_bytes": candidate_bytes,
                "blocking_finding_refs": sorted(set(blocking_finding_refs)),
                "semantic_unlock_generation": generation,
            },
        )

    def semantic_scope_exhausted(self, scope_key):
        return self.scope_exhaustion_event(scope_key) is not None

    def scope_exhaustion_event(self, scope_key):
        for event in self.scoped("semantic_scope_exhaustion_recorded"):
            if event.get("exhausted_semantic_scope_key") == scope_key:
                return event
        return None

    def semantic_scope_exhaustion_event_seq(self, scope_key):
        event = self.scope_exhaustion_event(scope_key)
        return None if event is None else event["event_seq"]

    def exhausted_novelty_keys(self, scope_key):
        keys = set()
        for event in self.scoped("mechanical_no_progress_recorded"):
            if event.get("semantic_scope_key") != scope_key:
                continue
            key = event.get("strategy_novelty_key")
            if key is not None:
                keys.add(key)
        return sorted(keys)

    def no_progress_rounds_in_scope(self, scope_key):
        return sum(
            1
            for event in self.scoped("mechanical_no_progress_recorded")
            if event.get("semantic_scope_key") == scope_key
        )

    def accepted_semantic_unlock(self, scope_key, evidence_sha256):
        for event in self.scoped("semantic_scope_unlock_recorded"):
            if (
                event.get("unlock_accepted") is True
                and event.get("exhausted_semantic_scope_key") == scope_key
                and event.get("unlock_evidence_sha256") == evidence_sha256
            ):
                return event
        return None

    # -- Section 11.2b -- probes --------------------------------------------
    def probe_results(self, closed_episode_identity):
        return [
            event
            for event in self.scoped("availability_probe_result_recorded")
            if event.get("closed_episode_identity") == closed_episode_identity
        ]

    def probe_serial(self, work_item, provider_kind, endpoint, closed_episode):
        count = 0
        for event in self.scoped("availability_probe_result_recorded"):
            if (
                event.get("work_item_identity") == work_item
                and event.get("provider_kind") == provider_kind
                and event.get("provider_endpoint_identity") == endpoint
                and event.get("closed_episode_identity") == closed_episode
            ):
                count += 1
        return 1 + count

    def probes_used(self, closed_episode_identity):
        return len(self.probe_results(closed_episode_identity))

    def open_probe(self, closed_episode_identity):
        """A begun probe with no recorded result, or None."""
        results = {
            event.get("availability_probe_identity")
            for event in self.probe_results(closed_episode_identity)
        }
        for event in self.scoped("availability_probe_begun"):
            if event.get("closed_episode_identity") != closed_episode_identity:
                continue
            if event.get("availability_probe_identity") not in results:
                return event
        return None

    def newest_probe_result(self, closed_episode_identity):
        results = self.probe_results(closed_episode_identity)
        return results[-1] if results else None

    def availability_probe_state(self, closed_episode_identity):
        if closed_episode_identity is None:
            return "none"
        if self.open_probe(closed_episode_identity) is not None:
            return "probe_begun_unknown"
        newest = self.newest_probe_result(closed_episode_identity)
        if newest is None:
            return "idle"
        if self.probes_used(closed_episode_identity) >= (
            constants.MAX_AVAILABILITY_PROBES_PER_CLOSED_EPISODE
        ):
            outcome = newest.get("probe_outcome")
            if outcome == "succeeded":
                return "succeeded"
            if outcome == "facts_unclassifiable":
                return "facts_unclassifiable"
            return "bound_reached"
        return newest.get("probe_outcome")

    # -- Section 11.9 -- episode exhaustion ---------------------------------
    def episode_exhaustion_event(self, episode_identity):
        found = [
            event
            for event in self.scoped(
                "provider_availability_episode_exhausted_recorded"
            )
            if event.get("provider_availability_episode_identity") == episode_identity
        ]
        if len(found) > 1:
            return "contradiction"
        return found[0] if found else None

    def accepted_episode_unlock(self, closed_episode_identity):
        for event in self.scoped("provider_availability_unlock_recorded"):
            if (
                event.get("closed_episode_identity") == closed_episode_identity
                and event.get("unlock_accepted") is True
            ):
                return event
        return None

    # -- Section 9.3 -- consumptions ----------------------------------------
    def consumption_starts(self):
        return self.scoped("diagnosis_strategy_consumption_started")

    def consumption_terminals(self, consumption_identity):
        terminals = []
        for kind in (
            "diagnosis_strategy_consumption_completed",
            "diagnosis_strategy_consumption_terminated",
        ):
            for event in self.scoped(kind):
                if event.get("consumption_identity") == consumption_identity:
                    terminals.append(event)
        for event in self.scoped("mechanical_no_progress_recorded"):
            if (
                event.get("terminates_consumption") is True
                and event.get("consumption_identity") == consumption_identity
            ):
                terminals.append(event)
        return terminals

    def newest_consumption_start(self):
        starts = self.consumption_starts()
        return starts[-1] if starts else None

    def open_consumption(self):
        for start in reversed(self.consumption_starts()):
            if not self.consumption_terminals(start["consumption_identity"]):
                return start
        return None

    # -- Section 7.6 -- diagnosis triggers ----------------------------------
    def newest_accepted_semantic_unlock_seq(self):
        """The sequence of the newest ACCEPTED semantic-scope unlock, or None."""
        newest = None
        for event in self.scoped("semantic_scope_unlock_recorded"):
            if event.get("unlock_accepted") is True:
                newest = event["event_seq"]
        return newest

    def _in_current_semantic_generation(self, event):
        """Section 7.6 -- a closing event recorded before the newest accepted
        semantic-scope unlock belongs to a superseded ``semantic_scope_key``.

        An accepted unlock advances ``semantic_unlock_generation`` (Section
        4.11), and ``semantic_unlock_generation`` is an input to
        ``semantic_scope_key`` (Section 4.3).  Every other input of that key is
        already an input of ``diagnosis_trigger_identity``, so for one trigger
        identity an accepted unlock is the ONLY thing that can change the scope
        key -- which is exactly when Section 7.6 says a closed trigger becomes
        irrelevant.  Nothing is erased: the closing event stays in authenticated
        history and reapplies if the same scope key recurs.
        """
        newest = self.newest_accepted_semantic_unlock_seq()
        return newest is None or event["event_seq"] > newest

    def diagnosis_rejections(self, trigger_identity, current_scope_only=True):
        events = [
            event
            for event in self.scoped("correction_diagnosis_rejected_recorded")
            if event.get("diagnosis_trigger_identity") == trigger_identity
        ]
        if not current_scope_only:
            return events
        return [event for event in events if self._in_current_semantic_generation(event)]

    def diagnosis_validation_failures(self, trigger_identity, current_scope_only=True):
        events = [
            event
            for event in self.scoped("correction_diagnosis_validation_failed_recorded")
            if event.get("diagnosis_trigger_identity") == trigger_identity
        ]
        if not current_scope_only:
            return events
        return [event for event in events if self._in_current_semantic_generation(event)]

    def trigger_diagnosis_attempt_ordinal(self, trigger_identity):
        return len(self.diagnosis_rejections(trigger_identity)) + len(
            self.diagnosis_validation_failures(trigger_identity)
        )

    def diagnosis_recorded_for(self, trigger_identity):
        for event in self.scoped("correction_diagnosis_recorded"):
            if event.get("diagnosis_trigger_identity") == trigger_identity:
                return event
        return None

    def diagnosis_trigger_state(self, trigger_identity, scope_key=None):
        if trigger_identity is None:
            return "none"
        closing = []
        if self.diagnosis_recorded_for(trigger_identity) is not None:
            closing.append("consumed")
        rejections = self.diagnosis_rejections(trigger_identity)
        failures = self.diagnosis_validation_failures(trigger_identity)
        if len(rejections) >= constants.DIAGNOSIS_ATTEMPTS_PER_TRIGGER:
            closing.append("closed_no_safe_strategy")
        for failure in failures:
            if failure.get("validation_failure_class") == "authority_or_safety_contradiction":
                closing.append("closed_safety_hold")
        attempts = len(rejections) + len(failures)
        if failures and attempts >= constants.DIAGNOSIS_ATTEMPTS_PER_TRIGGER:
            closing.append("closed_validation_failed")
        if scope_key is not None and self.semantic_scope_exhausted(scope_key):
            exhaustion = self.scope_exhaustion_event(scope_key)
            if exhaustion is not None and exhaustion.get("exhaustion_trigger_kind") == (
                "semantic_no_progress_bound_reached"
            ):
                closing.append("closed_scope_exhausted")
        closing = sorted(set(closing))
        if len(closing) > 1:
            return "contradiction"
        if closing:
            return closing[0]
        if attempts < constants.DIAGNOSIS_ATTEMPTS_PER_TRIGGER:
            return "open"
        return "closed_validation_failed"

    # -- Section 5.1 -- design-audit result usability -----------------------
    def design_audit_result_usability(self, request_identity):
        if request_identity is None:
            return "none"
        audits = [
            event
            for event in self.scoped("mechanical_audit_recorded")
            if event.get("provider_request_identity") == request_identity
        ]
        unusables = [
            event
            for event in self.scoped("mechanical_audit_unusable_recorded")
            if event.get("provider_request_identity") == request_identity
        ]
        if audits and unusables:
            return "contradiction"
        if len(audits) > 1 or len(unusables) > 1:
            return "contradiction"
        if self.collision_closure_completion(request_identity) is not None:
            return "contradiction"
        if audits:
            return "usable_proved"
        if unusables:
            return "unusable_recorded"
        return "none"

    # -- Section 9.8 -- Piece-3 authorization -------------------------------
    def _piece3_authorization_consumed(self, authorization):
        """Whether one Piece-3 authorization has durably completed.

        The ordinary success path is closed by the exact event the
        authorization names.  A coverage review that finds possible gaps is
        intentionally different: it records one or more review signals and no
        ``question_coverage_review_recorded`` clearance event.  In that narrow
        branch, the existing successful commit-operation completion is the
        durable all-signals-written boundary.  A signal without that matching
        completion remains unconsumed, so a crash part-way through a multi-gap
        append safely re-enters the commit.
        """
        authorizes = authorization.get("authorizes_event_type")
        for later in self._scoped:
            if later["event_seq"] <= authorization["event_seq"]:
                continue
            if later.get("type") == authorizes and is_supervisor_era_version(
                later.get("journal_version")
            ):
                return True

        if authorizes != "question_coverage_review_recorded":
            return False

        # routed_signal_refs on the authorization are INPUT binding: they are
        # the signals the coverage work item was dispatched with.  They are not
        # the provider result's newly found gaps.  Treating those pre-existing
        # refs as proof that the coverage result had already been applied closed
        # the authorization before commit, skipped the real possible_gaps, and
        # sent the same old inputs around validation/coverage again.  A coverage
        # authorization is consumed only by its named clearance event or by a
        # successful provider-free commit that durably wrote a real gap signal.

        work_item = authorization.get("work_item_identity")
        # Older installed controllers could incorrectly move on from a
        # coverage authorization by mistaking its INPUT signal refs for output
        # evidence.  Once a later authorization for the same stage is durable,
        # that historical authorization is superseded history rather than a
        # second live commit position.  The newest authorization remains owed
        # until its exact provider-free commit succeeds.
        if any(
            later.get("event_seq", 0) > authorization.get("event_seq", 0)
            and later.get("authorizes_event_type")
            == authorization.get("authorizes_event_type")
            for later in self.scoped("piece3_provider_work_recorded")
        ):
            return True
        for completed in self.scoped("supervisor_operation_completed"):
            if completed["event_seq"] <= authorization["event_seq"]:
                continue
            if (
                completed.get("supervisor_command")
                != "commit-piece3-provider-result"
                or completed.get("operation_outcome") != "ok"
                or completed.get("work_item_identity") != work_item
            ):
                continue
            operation_id = completed.get("supervisor_operation_id")
            starts = [
                event
                for event in self.scoped("supervisor_operation_started")
                if event.get("supervisor_operation_id") == operation_id
                and event.get("supervisor_command")
                == "commit-piece3-provider-result"
                and event.get("work_item_identity") == work_item
                and authorization["event_seq"] < event["event_seq"]
                < completed["event_seq"]
            ]
            if len(starts) != 1:
                continue
            if any(
                event.get("type") == "review_signal_recorded"
                and event.get("signal_source") == "question_coverage_review"
                and starts[0]["event_seq"] < event["event_seq"]
                < completed["event_seq"]
                for event in self._scoped
            ):
                return True
            # The commit itself is the durable proof that the exact custodied
            # result was processed.  If it produced neither a clearance nor a
            # new signal, replay closes the authorization but the transition
            # projector separately classifies that exact outcome as mechanical
            # no-progress.  Re-entering the commit cannot create new evidence.
            return True
        return False

    def piece3_provider_authorization(self):
        pending = []
        for event in self.scoped("piece3_provider_work_recorded"):
            authorizes = event.get("authorizes_event_type")
            consumed = self._piece3_authorization_consumed(event)
            if not consumed:
                pending.append(authorizes)
        if len(pending) > 1:
            return "contradiction"
        if not pending:
            authorizations = self.scoped("piece3_provider_work_recorded")
            return "consumed" if authorizations else "none"
        if pending[0] == "validation_recorded":
            return "authorized_validation_pending"
        return "authorized_coverage_pending"

    def unconsumed_piece3_authorization(self, event_type):
        for event in self.scoped("piece3_provider_work_recorded"):
            if event.get("authorizes_event_type") != event_type:
                continue
            if not self._piece3_authorization_consumed(event):
                return event
        return None

    # -- Section 11.1 -- supervisor operations ------------------------------
    def started_event(self, operation_id):
        found = [
            event
            for event in self.scoped("supervisor_operation_started")
            if event.get("supervisor_operation_id") == operation_id
        ]
        if len(found) > 1:
            return "duplicate"
        return found[0] if found else None

    def completed_event(self, operation_id):
        found = [
            event
            for event in self.scoped("supervisor_operation_completed")
            if event.get("supervisor_operation_id") == operation_id
        ]
        if len(found) > 1:
            return "duplicate"
        return found[0] if found else None

    def unmatched_starts(self, supervisor_command=None):
        """Every started operation with no completion, optionally by command."""
        completed = {
            event.get("supervisor_operation_id")
            for event in self.scoped("supervisor_operation_completed")
        }
        found = []
        for event in self.scoped("supervisor_operation_started"):
            if event.get("supervisor_operation_id") in completed:
                continue
            if supervisor_command is not None and event.get(
                "supervisor_command"
            ) != supervisor_command:
                continue
            found.append(event)
        return found

    def prefix_before(self, event_seq):
        return [event for event in self.events if event["event_seq"] < event_seq]

    # -- candidate chain ----------------------------------------------------
    def candidate_custody_events(self):
        return self.scoped("candidate_custody_recorded")

    def pending_write_ahead(self):
        pending = None
        for event in self._scoped:
            if event.get("type") == "candidate_write_ahead_recorded":
                pending = event
            elif event.get("type") in (
                "candidate_write_ahead_aborted",
                "candidate_custody_recorded",
            ):
                pending = None
        return pending

    def correction_round_lifetime(self):
        return len(self.candidate_custody_events())

    def current_batch_triple(self):
        return batch_triple(self.correction_round_lifetime())

    def correction_rounds_started_this_batch(self):
        lifetime = self.correction_round_lifetime()
        _l, batch, _r = batch_triple(lifetime)
        if batch == 0:
            batch = 1
        started = 0
        for event in self.candidate_custody_events():
            if event.get("correction_batch_number") == batch:
                started += 1
        pending = self.pending_write_ahead()
        if pending is not None and pending.get("correction_batch_number") == batch:
            started += 1
        return started

    def correction_rounds_completed_this_batch(self):
        lifetime = self.correction_round_lifetime()
        _l, batch, _r = batch_triple(lifetime)
        if batch == 0:
            return 0
        return sum(
            1
            for event in self.candidate_custody_events()
            if event.get("correction_batch_number") == batch
        )

    # -- audits and checkpoints ---------------------------------------------
    def audits_for_candidate(self, candidate_sha256):
        return [
            event
            for event in self.scoped("mechanical_audit_recorded")
            if event.get("candidate_sha256") == candidate_sha256
        ]

    def newest_audit(self, candidate_sha256):
        audits = self.audits_for_candidate(candidate_sha256)
        return audits[-1] if audits else None

    def checkpoint_for(self, checkpoint_identity):
        for event in self.scoped("correction_batch_checkpoint_recorded"):
            if event.get("checkpoint_identity") == checkpoint_identity:
                return event
        return None

    def newest_checkpoint(self):
        checkpoints = self.scoped("correction_batch_checkpoint_recorded")
        return checkpoints[-1] if checkpoints else None

    def newest_no_progress(self):
        events = self.scoped("mechanical_no_progress_recorded")
        return events[-1] if events else None

    def pass_event(self):
        events = self.scoped("mechanical_pass_recorded")
        return events[-1] if events else None

    # -- Sections 9.1, 12.1 -- the NESS acceptance record --------------------
    #
    # These three read ``ness_candidate_acceptance_recorded`` and nothing else.
    # They are deliberately separate from acceptance_event() above, which reads
    # ``provider_request_accepted`` -- a PROVIDER accepting a request, which
    # Section 9.4 says this record explicitly is not.  Two different acts keep
    # two different readers: neither is renamed, and neither is reused for the
    # other.
    #
    # All three are RAW replay lookup.  None of them decides the governed
    # PROVED_ACCEPTED / PROVED_NOT_ACCEPTED / UNRESOLVED classification of
    # Section 11.1.  That is a lock-time judgement about the head and about a
    # live writer who may still legally roll a record back (Section 10.3 rule
    # 7), and no reader of an event list alone may make it.
    def ness_acceptance_events(self):
        """The scoped acceptance records, in journal order."""
        return self.scoped(NESS_CANDIDATE_ACCEPTANCE_EVENT_TYPE)

    def ness_acceptance_by_identity(self, ness_acceptance_identity):
        """The one record carrying this identity, None, or ``"duplicate"``.

        Section 12.1 resolves every retry lookup-first, so this answer decides
        whether a caller writes.  A lookup that silently returned the newest of
        two records would let a retry report success against a record it did
        not write, so more than one match is reported rather than resolved.
        """
        found = [
            event
            for event in self.ness_acceptance_events()
            if event.get("ness_acceptance_identity") == ness_acceptance_identity
        ]
        if len(found) > 1:
            return "duplicate"
        return found[0] if found else None

    def current_ness_acceptance(self):
        """The one acceptance record in scope, None, or ``"duplicate"``.

        Section 9.2 appends exactly one acceptance event for an accepted act
        and Section 12.1 answers every repeat by lookup, so a second physical
        record in one scope is the Section 10.4 contradiction and not a newer
        answer.  Neither record is preferred and neither is erased.
        """
        found = self.ness_acceptance_events()
        if len(found) > 1:
            return "duplicate"
        return found[0] if found else None

    # -- Sections 7.2, 7.3, 7.5 -- the acceptance explanation ----------------
    def acceptance_explanation_events(self, stage=None):
        """Scoped explanation records that carry an ACCEPTANCE stage.

        The carrier type is shared with the correction-stage record (Section
        7.2), so the two are separated by the required ``explanation_stage``
        discriminator and by nothing else -- never by ordering, by field
        resemblance, by filename, or by content (Section 7.3).  A record that
        carries no acceptance stage, which is every correction-stage record
        and every record written before the discriminator existed, is not one
        of these and is never returned here.
        """
        if stage is not None and stage not in ACCEPTANCE_EXPLANATION_STAGES:
            raise ValueError(
                "an acceptance explanation stage is one of %s, not %r"
                % (list(ACCEPTANCE_EXPLANATION_STAGES), stage)
            )
        found = []
        for event in self.scoped("mechanical_change_explanation_recorded"):
            recorded = event.get("explanation_stage")
            if recorded not in ACCEPTANCE_EXPLANATION_STAGES:
                continue
            if stage is not None and recorded != stage:
                continue
            found.append(event)
        return found

    def current_acceptance_explanation(
        self,
        candidate_sha256,
        audit_identity,
        pass_identity,
        stage=FINAL_ACCEPTANCE_EXPLANATION_STAGE,
    ):
        """Section 7.5 rule 3, applied literally to one exact binding.

        The binding is this replay's own scope, plus the candidate, audit and
        pass identities given, at the stage requested.  CURRENT means the
        highest ``explanation_version`` among the matching records that no
        matching record supersedes by naming them in
        ``supersedes_explanation_identity``.  Superseded records stay history
        (rule 4): nothing here mutates, removes, or hides one.

        Returns the current record; None when the binding has no unsuperseded
        matching record; or ``"duplicate"`` when two unsuperseded records share
        the highest version -- the rule-3 contradiction, in which the newer
        record is never silently preferred.  An unrankable version is reported
        the same way rather than being ordered by guesswork.

        It decides WHICH record is current, and only that.  It judges no prose,
        applies no Section 6.6 structural check, and tests no Section 7.7
        staleness row.
        """
        matching = [
            event
            for event in self.acceptance_explanation_events(stage)
            if event.get("candidate_sha256") == candidate_sha256
            and event.get("audit_identity") == audit_identity
            and event.get("pass_identity") == pass_identity
        ]
        superseded = {
            event.get("supersedes_explanation_identity")
            for event in matching
            if event.get("supersedes_explanation_identity") is not None
        }
        live = [
            event
            for event in matching
            if event.get("explanation_record_identity") not in superseded
        ]
        if not live:
            return None
        versions = [explanation_version_of(event) for event in live]
        if None in versions:
            return "duplicate"
        highest = max(versions)
        current = [
            event for event, version in zip(live, versions) if version == highest
        ]
        if len(current) > 1:
            return "duplicate"
        return current[0]

    # -- Section 11.3 gate 11d -- the effect-owning completed pair -----------
    def _shares_effect_binding(self, event, effect_event):
        """True where ``event`` carries the effect's binding, key by key.

        A key absent from either record is not compared.  The operation events
        and the substantive events do not carry identical key sets, and gate
        11d binds them by the fields they actually share -- never by a field
        one of them was never given.
        """
        for key in EFFECT_OWNER_BINDING_KEYS:
            if key not in effect_event or key not in event:
                continue
            if event[key] != effect_event[key]:
                return False
        return True

    def effect_owning_completed_pair(self, effect_event):
        """The one completed operation that surrounds and owns one effect.

        A pair qualifies when its start precedes the effect, its completion
        follows the effect, the completion carries the start's
        ``supervisor_operation_id`` AND the start's ``event_seq`` as
        ``supervisor_started_event_seq``, and both members carry the effect's
        package/source/candidate binding.

        Returns None; or ``{"start": ..., "effect": ..., "completion": ...}``;
        or ``"duplicate"`` when two pairs both genuinely qualify -- gate 11d's
        "a substantive event owned by two candidate pairs", which is refused
        and never chosen between.

        A PRE-EFFECT unmatched start produced no substantive effect and is
        preserved historical residue (Section 14 rows P-3a and P-3c).  It is
        not reaped, not deleted, and not paired to a later operation's
        completion, and its mere presence never hides the pair that really
        owns the effect: it fails the identity and started-sequence tests that
        the owning start passes.

        This LOCATES what is already durable.  It performs no completion
        recovery, appends nothing, and names no A5 or A6 command -- which
        command spells which operation is later implementation detail, so the
        rule is stated over the fields the installed events already carry.
        """
        if not isinstance(effect_event, dict):
            return None
        effect_seq = effect_event.get("event_seq")
        if effect_seq is None:
            return None
        completions = self.scoped("supervisor_operation_completed")
        pairs = []
        for start in self.scoped("supervisor_operation_started"):
            operation_id = start.get("supervisor_operation_id")
            start_seq = start.get("event_seq")
            if operation_id is None or start_seq is None:
                continue
            if not start_seq < effect_seq:
                continue
            if not self._shares_effect_binding(start, effect_event):
                continue
            for completion in completions:
                completion_seq = completion.get("event_seq")
                if completion_seq is None or not effect_seq < completion_seq:
                    continue
                if completion.get("supervisor_operation_id") != operation_id:
                    continue
                if completion.get("supervisor_started_event_seq") != start_seq:
                    continue
                if not self._shares_effect_binding(completion, effect_event):
                    continue
                pairs.append(
                    {
                        "start": start,
                        "effect": effect_event,
                        "completion": completion,
                    }
                )
        if len(pairs) > 1:
            return "duplicate"
        return pairs[0] if pairs else None

    # -- dependency occurrences ---------------------------------------------
    def dependency_occurrence_events(self):
        return [
            event
            for event in self.events
            if event.get("dependency_identity") is not None
        ]

    def current_dependency(self):
        """The newest authenticated dependency occurrence, projected."""
        occurrences = self.dependency_occurrence_events()
        if not occurrences:
            return None
        newest = occurrences[-1]
        identity = newest["dependency_identity"]
        record = self.record_for_identity(identity)
        if (
            isinstance(record, dict)
            and record.get("dependency_class") == "external_user_action_required"
            and self.external_action_resolution(identity) is not None
        ):
            return None
        carrier_seq = dependency.carrier_event_seq_of(newest)
        carrier = self.by_seq(carrier_seq)
        record = carrier.get("dependency_record") if carrier else None
        return {
            "dependency_record": record,
            "dependency_identity": identity,
            "dependency_carrier_event_seq": carrier_seq,
            "dependency_occurrence_ordinal": newest.get("dependency_occurrence_ordinal"),
        }

    def record_for_identity(self, identity):
        seq = dependency.carrier_event_seq(self.events, identity)
        if seq is None:
            return None
        carrier = self.by_seq(seq)
        return carrier.get("dependency_record") if carrier else None

    def current_occurrences(self):
        """Every occurrence whose unlock predicate is not proved and which no
        later event has superseded (Section 11.9b)."""
        by_identity = {}
        for event in self.dependency_occurrence_events():
            identity = event["dependency_identity"]
            by_identity.setdefault(identity, []).append(event)
        current = []
        for identity, events in by_identity.items():
            record = self.record_for_identity(identity)
            if record is None:
                continue
            if (
                record.get("dependency_class") == "external_user_action_required"
                and self.external_action_resolution(identity) is not None
            ):
                continue
            current.append(
                {
                    "dependency_identity": identity,
                    "record": record,
                    "carrier_event_seq": dependency.carrier_event_seq(self.events, identity),
                    "occurrences": events,
                }
            )
        return current

    def external_action_resolution(self, dependency_identity):
        """Return the one exact, re-proved resolution of an external-action stop.

        The record is not trusted merely because it names a dependency.  It must
        bind the unique dependency carrier and the exact failed terminal, must be
        tail-bound to the immediately preceding authenticated state, and must
        carry the one bounded normal-host Codex smoke proof this repair accepts.
        """
        found = [
            event for event in self.scoped(schema.EXTERNAL_ACTION_RESOLUTION_EVENT_TYPE)
            if event.get("resolved_dependency_identity") == dependency_identity
        ]
        if len(found) != 1:
            return None
        event = found[0]
        carrier_seq = dependency.carrier_event_seq(self.events, dependency_identity)
        carrier = self.by_seq(carrier_seq) if carrier_seq is not None else None
        record = carrier.get("dependency_record") if isinstance(carrier, dict) else None
        terminal = self.by_seq(event.get("failed_provider_terminal_event_seq"))
        if not (
            isinstance(record, dict)
            and record.get("dependency_class") == "external_user_action_required"
            and record.get("retry_mode") == "no_automatic_retry_until_unlock_proved"
            and record.get("unlock_predicate", {}).get("predicate_kind")
            == "named_external_action_observed"
            and event.get("resolved_dependency_carrier_event_seq") == carrier_seq
            and event.get("resolved_dependency_carrier_event_sha256")
            == carrier.get("event_sha256")
            and event.get("resolved_dependency_code") == record.get("dependency_code")
            and event.get("work_item_identity") == record.get("work_item_identity")
            and event.get("resource_identity") == record.get("resource_identity")
            and event.get("user_action_code") == record.get("user_action_code")
            and isinstance(terminal, dict)
            and terminal.get("type") == "provider_request_terminal_recorded"
            and terminal.get("event_sha256")
            == event.get("failed_provider_terminal_event_sha256")
            and terminal.get("provider_request_identity")
            == event.get("failed_provider_request_identity")
            and terminal.get("dependency_identity") == dependency_identity
            and terminal.get("terminal_kind") == "provider_error_terminal"
            and terminal.get("provider_outcome_facts", {}).get("returncode") == 1
            and event.get("pre_action_authenticated_event_seq") == event.get("event_seq") - 1
            and event.get("pre_action_authenticated_tail_sha256")
            == event.get("prev_event_sha256")
            and event.get("external_action_evidence_kind")
            == "normal_host_codex_cli_smoke_succeeded"
            and event.get("normal_host_context_confirmed") is True
            and event.get("provider_cli_login_proved") is True
            and event.get("provider_state_writable_proved") is True
            and event.get("bounded_smoke_returncode") == 0
            and event.get("bounded_smoke_agent_message") == "OK"
            and event.get("bounded_smoke_turn_completed") is True
            and event.get("ness_action_confirmed") is True
            and isinstance(event.get("ness_action_exact"), str)
            and bool(event["ness_action_exact"].strip())
        ):
            return None
        return event

    # -- contradiction sweep -------------------------------------------------
    def contradictions(self):
        """Every Section 11.4 SAFETY_HOLD contradiction this replay can prove."""
        problems = list(dependency.replay_assertions(self.dependency_occurrence_events()))
        duplicated = dependency.record_object_appears_once(self.dependency_occurrence_events())
        for identity in duplicated:
            problems.append("the record object of %s appears more than once" % identity)

        seen_custody = {}
        for event in self.scoped("provider_result_custody_recorded"):
            request = event.get("provider_request_identity")
            seen_custody.setdefault(request, []).append(event)
        for request, events in seen_custody.items():
            if len(events) > 1:
                problems.append("two custody records exist for %s" % request)

        seen_terminal = {}
        for event in self.scoped("provider_request_terminal_recorded"):
            request = event.get("provider_request_identity")
            seen_terminal.setdefault(request, []).append(event)
        for request, events in seen_terminal.items():
            if len(events) > 1:
                problems.append("two terminal events exist for %s" % request)
            terminal = events[0]
            if terminal.get("terminal_kind") in ("result_received", "result_invalid"):
                custody = self.custody_event(request)
                if custody is None:
                    problems.append(
                        "a terminal claiming a retained result has no custody record: %s"
                        % request
                    )
                elif custody["event_seq"] > terminal["event_seq"]:
                    problems.append(
                        "custody for %s is not durable before its terminal" % request
                    )

        for custody in self.scoped("provider_result_custody_recorded"):
            if custody.get("work_item_kind") != "correction_diagnosis":
                continue
            transaction = self.possible_ness_transaction(custody)
            if transaction["diagnosis"] is None or transaction[
                "diagnosis"
            ].get("diagnosis_outcome") != "possible_ness_choice":
                continue
            problems.extend(transaction["problems"])

        seen_probe = {}
        for event in self.scoped("availability_probe_result_recorded"):
            identity = event.get("availability_probe_identity")
            seen_probe.setdefault(identity, []).append(event)
        for identity, events in seen_probe.items():
            if len(events) > 1:
                problems.append("two probe results exist for %s" % identity)

        seen_scope = {}
        for event in self.scoped("semantic_scope_exhaustion_recorded"):
            identity = event.get("scope_exhaustion_identity")
            seen_scope.setdefault(identity, []).append(event)
        for identity, events in seen_scope.items():
            if len(events) > 1:
                problems.append("two scope-exhaustion events exist for %s" % identity)

        seen_episode = {}
        for event in self.scoped("provider_availability_episode_exhausted_recorded"):
            identity = event.get("provider_availability_episode_identity")
            seen_episode.setdefault(identity, []).append(event)
        for identity, events in seen_episode.items():
            if len(events) > 1:
                problems.append("two exhaustion events exist for episode %s" % identity)

        seen_started = {}
        for event in self.scoped("supervisor_operation_started"):
            identity = event.get("supervisor_operation_id")
            seen_started.setdefault(identity, []).append(event)
        for identity, events in seen_started.items():
            if len(events) > 1:
                problems.append("two starts exist for operation %s" % identity)

        for request in {
            event.get("provider_request_identity")
            for event in self.scoped("mechanical_audit_recorded")
        } & {
            event.get("provider_request_identity")
            for event in self.scoped("mechanical_audit_unusable_recorded")
        }:
            problems.append(
                "both an audit record and an unusable-audit record exist for %s" % request
            )

        for start in self.consumption_starts():
            terminals = self.consumption_terminals(start["consumption_identity"])
            if len(terminals) > 1:
                problems.append(
                    "consumption %s has more than one terminal"
                    % start["consumption_identity"]
                )
        starts = {
            start["consumption_identity"] for start in self.consumption_starts()
        }
        for kind in (
            "diagnosis_strategy_consumption_completed",
            "diagnosis_strategy_consumption_terminated",
        ):
            for event in self.scoped(kind):
                if event.get("consumption_identity") not in starts:
                    problems.append(
                        "a consumption terminal has no start: %s"
                        % event.get("consumption_identity")
                    )

        # -- Sections 9.2, 10.4 -- one package scope holds one acceptance.
        # Section 12.1 answers a repeat by returning the existing record, so a
        # second physical record is never how a retry lands: two of them are a
        # contradiction whether or not they agree.  Neither is preferred,
        # neither is erased, and nothing here repairs either.
        acceptances = self.ness_acceptance_events()
        if len(acceptances) > 1:
            problems.append(
                "more than one Ness acceptance record exists in this package "
                "scope: %d records" % len(acceptances)
            )
        seen_acceptance = {}
        for event in acceptances:
            identity = event.get("ness_acceptance_identity")
            seen_acceptance.setdefault(identity, []).append(event)
        for identity in sorted(seen_acceptance, key=lambda value: "%r" % (value,)):
            if len(seen_acceptance[identity]) > 1:
                problems.append(
                    "two Ness acceptance records exist for %s" % identity
                )

        # -- Section 7.5 rule 3 -- two unsuperseded explanations at the same
        # highest version for one binding and stage.  The newer is never
        # silently preferred, so the ambiguity is surfaced here as well as
        # through the "duplicate" result of the resolver itself.
        seen_binding = {}
        for event in self.acceptance_explanation_events():
            binding = (
                event.get("explanation_stage"),
                event.get("candidate_sha256"),
                event.get("audit_identity"),
                event.get("pass_identity"),
            )
            seen_binding.setdefault(binding, []).append(event)
        for binding in sorted(seen_binding, key=lambda value: "%r" % (value,)):
            stage, candidate, audit, pass_identity = binding
            if self.current_acceptance_explanation(
                candidate, audit, pass_identity, stage=stage
            ) == "duplicate":
                problems.append(
                    "two unsuperseded acceptance explanations share the "
                    "highest version for candidate %s at stage %s"
                    % (candidate, stage)
                )
        return problems

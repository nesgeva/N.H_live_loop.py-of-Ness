#!/usr/bin/env python3
"""Command selection, the workflow projection, and the exact status reports.

Sections 2, 2.1, 5.1 P-4, 9.3, 11.4, 13.1 and 14.  Everything here is derived
from the authenticated journal, the controller's own bindings, and the lease
evaluation.  It writes nothing, invokes no model, performs no provider lookup,
and performs no availability probe.
"""

from __future__ import annotations

from . import capability, constants, dependency, engine
from . import replay as replay_mod
from .canonical import canonical_json, is_hex64, sha256_hex
from .identity import IdentityError, batch_triple, derive, retry_series_key

# ---------------------------------------------------------------------------
# The exact declared key sets of the read-only reports (Section 4.8's
# report_field registry reads these).
# ---------------------------------------------------------------------------
# Section 16.2 -- the acceptance OFFER response.  It is a projection: every
# value in it was proved by the controller under the existing lock, and none of
# it is ever client authority.
ACCEPTANCE_OFFER_KEYS = (
    "command",
    "ok",
    "errors",
    "acceptance_actionable",
    "acceptance_truth",
    "reason",
    "workflow_state",
    "acceptance_required",
    "acceptance_offer_id",
    "acceptance_offer_binding_sha256",
    "acceptance_scope_id",
    "acceptance_scope_digest",
    "acceptance_scope_sentence",
    "acceptance_scope_text",
    "acceptance_fixed_meaning",
    "acceptance_non_authorizations",
    "explanation_parts",
    "technical",
    "pre_click_head",
    "pre_click_head_digest_sha256",
    "ness_acceptance_identity",
)

# Section 16.4 -- the acceptance RECORD response.  Every response says which of
# the three governed truths holds, and says nothing stronger than was proved.
ACCEPTANCE_RECORD_KEYS = (
    "command",
    "ok",
    "errors",
    "outcome",
    "reason",
    "acceptance_truth",
    "acceptance_events_appended",
    "refusal_records_appended",
    "ness_acceptance_identity",
    "acceptance_event_seq",
    "acceptance_event_sha256",
    "workflow_state",
)


SUPERVISOR_STATUS_KEYS = (
    "command",
    "ok",
    "supervisor_capability_version",
    "workflow_state",
    "package_key",
    "package_scope_id",
    "package_id",
    "bundle_placement",
    "controlled_component_id",
    "register_id",
    "branch",
    "head_sha",
    "controller_executable_identity",
    "source_binding_sha256",
    "settled_decision_binding_sha256",
    "candidate_path",
    "candidate_sha256",
    "candidate_bytes",
    "correction_batch_size",
    "correction_batch_number",
    "correction_rounds_started_this_batch",
    "correction_rounds_completed_this_batch",
    "correction_rounds_lifetime_before",
    "correction_rounds_lifetime_after",
    "correction_round_lifetime",
    "correction_round_in_batch",
    "audit_identity",
    "checkpoint_identity",
    "diagnosis_identity",
    "next_command",
    "ness_decision_required",
    "interview_projection",
    "interview_gate_projection",
    "ness_decision_clearance",
    "ness_question_binding",
    "ness_answer_clarification",
    "ness_decision_cleared",
    "user_action_required",
    "acceptance_required",
    # Sections 11.1b and 17.1 -- what the LOCKED journal proves about
    # acceptance, reported separately from whether any request succeeded.
    "acceptance_truth",
    "acceptance_disposition",
    "ness_acceptance_identity",
    "acceptance_locked_projection",
    "journal_authentication_proved",
    "authenticated_state_current",
    "source_state_current",
    # section 8.8 section 13.2 SBC-STATUS-REPORTS -- EXACTLY ONE new top-level key.
    # A NESTED object mirroring the installed ``run_lease`` shape, so the flat
    # report gains one key rather than eleven and the whole projection has one
    # name and one owner.  It reports the package / effective-validation source
    # fact of FAMILY A ONLY and says NOTHING about any Ness question
    # (SBC-STATUS-IS-FAMILY-A-ONLY, section 13.5).
    "source_currentness",
    "controller_confirmed_change_events",
    "run_lease",
    "authenticated_event_seq",
    "authenticated_tail_sha256",
    "standing_chain_sha256",
    "work_item_identity",
    "work_item_kind",
    "retry_series_key",
    "state_binding_sha256",
    "provider_kind",
    "provider_phase",
    "provider_request_identity",
    "provider_availability_episode_identity",
    "provider_availability_episode_generation",
    "provider_attempts_closed_this_episode",
    "provider_attempts_remaining_this_episode",
    "provider_dispatch_serial_next",
    "provider_reconciliation",
    "provider_result_custody",
    "result_custody_identity",
    "provider_error_signal_token",
    "provider_error_classification_row_id",
    "open_provider_request_count",
    "open_result_custody_count",
    "consumption_reconciliation",
    "open_consumption_identity",
    "dependency_record",
    "dependency_identity",
    "dependency_identity_binding",
    "dependency_carrier_event_seq",
    "dependency_occurrence_ordinal",
    "dependency_durable_record_placement",
    "semantic_scope_key",
    "semantic_unlock_generation",
    "semantic_scope_exhausted",
    "semantic_scope_exhaustion_event_seq",
    "semantic_scope_unlock_available",
    "exhausted_novelty_key_count",
    "no_progress_rounds_in_scope",
    "no_progress_rounds_remaining_in_scope",
    "diagnosis_trigger_identity",
    "diagnosis_trigger_attempt_ordinal",
    "diagnosis_trigger_state",
    "design_audit_result_usability",
    "output_retries_used",
    "output_retries_remaining",
    "availability_probe_state",
    "availability_probe_identity",
    "availability_probes_used_this_closed_episode",
    "availability_probes_remaining_this_closed_episode",
    "availability_probe_automatic_eligible",
    "episode_unlock_automatic_eligible",
    "c11a_self_condition_satisfied",
    "episode_exhaustion_person_route_reason",
    "automatic_episode_unlocks_used",
    "automatic_episode_unlocks_remaining",
    "piece3_provider_authorization",
    "errors",
)

SUPERVISOR_OPERATION_STATUS_KEYS = (
    "command",
    "ok",
    "supervisor_operation_id",
    "supervisor_command",
    "work_item_identity",
    "work_item_kind",
    "package_scope_id",
    "source_binding_sha256",
    "pre_state_sha256",
    "started_event_seq",
    "completed_event_seq",
    "recovery_outcome",
    "recovered_workflow_state",
    "next_command",
    "provider_retry_safe",
    "provider_kind",
    "provider_phase",
    "provider_request_identity",
    "provider_availability_episode_identity",
    "provider_availability_episode_generation",
    "provider_attempts_closed_this_episode",
    "provider_attempts_remaining_this_episode",
    "provider_reconciliation",
    "provider_result_custody",
    "result_custody_identity",
    "provider_error_signal_token",
    "provider_error_classification_row_id",
    "design_audit_result_usability",
    "output_retries_used",
    "output_retries_remaining",
    "availability_probe_state",
    "availability_probes_used_this_closed_episode",
    "availability_probes_remaining_this_closed_episode",
    "availability_probe_automatic_eligible",
    "episode_unlock_automatic_eligible",
    "c11a_self_condition_satisfied",
    "episode_exhaustion_person_route_reason",
    "semantic_scope_key",
    "semantic_unlock_generation",
    "semantic_scope_exhausted",
    "semantic_scope_exhaustion_event_seq",
    "semantic_scope_unlock_available",
    "candidate_reconciliation",
    "consumption_reconciliation",
    "diagnosis_trigger_state",
    "dependency_record",
    "dependency_identity",
    "dependency_identity_binding",
    "dependency_carrier_event_seq",
    "dependency_occurrence_ordinal",
    "dependency_durable_record_placement",
    "retry_series_key",
    "authenticated_event_seq",
    "authenticated_tail_sha256",
    "journal_authentication_proved",
    "source_state_current",
    "errors",
)

# The exact response list contains NONE of the three unlock_evidence_* fields.
assert not (
    {"unlock_evidence_kind", "unlock_evidence_identity", "unlock_evidence_sha256"}
    & set(SUPERVISOR_OPERATION_STATUS_KEYS)
)

REPORT_FIELD_SETS = {
    "supervisor-status": frozenset(SUPERVISOR_STATUS_KEYS),
    "supervisor-operation-status": frozenset(SUPERVISOR_OPERATION_STATUS_KEYS),
}


class Situation:
    """One complete derivation of the current state from authenticated replay."""

    def __init__(self, context, events, candidate=None, lease_state=None, lease=None,
                 *, locked_head=None, locked_snapshot=False):
        self.context = context
        self.events = list(events)
        self.replay = replay_mod.Replay(events, context.binding.package_scope_id)
        self.lease_state = lease_state
        self.lease = lease
        self.errors = []
        # Section 10.3 rule 7 -- raw replay validity and GOVERNED terminal
        # acceptance are two different questions.  A reader that did not hold
        # the exclusive journal lock may establish the first and may never
        # answer the second, because inside the interrupted-append window a
        # live writer still legally may roll the record back.  These two carry
        # that fact, and default to "no lock was held", which is the safe way
        # round: an existing caller that never took the lock keeps projecting
        # exactly what it projected before, and never gains the power to say
        # the word "accepted".
        self.locked_head = locked_head
        self.locked_snapshot = bool(locked_snapshot)

        self.contradictions = self.replay.contradictions()
        self.candidate = candidate or self._current_candidate()
        self.audit = self.replay.newest_audit(self.candidate.candidate_sha256)
        self.blocking_finding_refs = self._blocking_refs()
        self.audit_identity = None if self.audit is None else self.audit["audit_identity"]

        self.semantic_unlock_generation = self.replay.semantic_unlock_generation()
        self.semantic_scope_key = self.replay.semantic_scope_key(
            context.binding.package_scope_id,
            context.binding.source_binding_sha256,
            self.candidate.candidate_path,
            self.candidate.candidate_sha256,
            self.candidate.candidate_bytes,
            self.blocking_finding_refs,
            self.semantic_unlock_generation,
        )
        self.open_consumption = self.replay.open_consumption()
        self.pending_custody = self.replay.custodied_results_awaiting_processing()
        self.open_requests = self.replay.open_provider_requests()
        self.trigger = self._current_trigger()
        self.work_item_obj, self.work_item_id, self.work_item_variant = self._work_item()

    # -- candidate ----------------------------------------------------------
    def _current_candidate(self):
        custody = self.replay.candidate_custody_events()
        if not custody:
            return self.context_candidate()
        newest = custody[-1]
        return engine.CandidateState(
            candidate_path=newest["candidate_path"],
            candidate_sha256=newest["candidate_sha256"],
            candidate_bytes=newest["candidate_bytes"],
            parent_candidate_path=newest.get("parent_candidate_path"),
            parent_candidate_sha256=newest.get("parent_candidate_sha256"),
            parent_candidate_bytes=newest.get("parent_candidate_bytes"),
        )

    def context_candidate(self):
        return self.context.round_zero_candidate

    def _blocking_refs(self):
        if self.context.blocking_finding_refs_override is not None:
            return sorted(set(self.context.blocking_finding_refs_override))
        if self.audit is None:
            return []
        if self.audit.get("verdict") != "BLOCKED":
            return []
        return sorted(set(self.audit.get("mechanical_blocker_refs") or []))

    # -- diagnosis trigger --------------------------------------------------
    def _current_trigger(self):
        """The union of Section 7.1 precondition 2, restricted to CURRENT triggers.

        A trigger is current only while it is bound to the package's current
        candidate and no ``correction_diagnosis_recorded`` has consumed it: a
        newer candidate, audit, or diagnosis supersedes it (Section 7.1
        precondition 6, Section 7.6).
        """
        consumed_seqs = {
            event.get("diagnosis_trigger_event_seq")
            for event in self.replay.scoped("correction_diagnosis_recorded")
        }
        candidates = []
        for event in self.replay.scoped("correction_batch_checkpoint_recorded"):
            if event.get("checkpoint_outcome") != "diagnosis_required":
                continue
            if event["event_seq"] in consumed_seqs:
                continue
            if event.get("candidate_sha256") != self.candidate.candidate_sha256:
                continue
            candidates.append(("exhausted_batch", event))
        for event in self.replay.scoped("mechanical_no_progress_recorded"):
            if event.get("diagnosis_required") is not True:
                continue
            if event["event_seq"] in consumed_seqs:
                continue
            if event.get("candidate_sha256") != self.candidate.candidate_sha256:
                continue
            candidates.append(("no_progress", event))
        if not candidates:
            return None
        kind, event = max(candidates, key=lambda item: item[1]["event_seq"])
        identity = derive(
            "diagnosis_trigger_identity",
            {
                "diagnosis_trigger_type": kind,
                "diagnosis_trigger_event_seq": event["event_seq"],
                "trigger_event_sha256": event["event_sha256"],
                "package_scope_id": self.context.binding.package_scope_id,
                "source_binding_sha256": self.context.binding.source_binding_sha256,
                "candidate_path": event["candidate_path"],
                "candidate_sha256": event["candidate_sha256"],
                "blocking_finding_refs": sorted(set(event["blocking_finding_refs"])),
            },
        )
        return {
            "trigger_type": kind,
            "event": event,
            "diagnosis_trigger_identity": identity,
        }

    # -- work item ----------------------------------------------------------
    def _work_item(self):
        context = self.context
        candidate = self.candidate
        if self.open_consumption is not None:
            start = self.open_consumption
            variant = (
                "ordinary_specification"
                if start.get("consumption_authority_kind") == "ordinary_specification"
                else (
                    "diagnosis_exhausted_batch"
                    if start.get("diagnosis_event_seq") is not None
                    and self._trigger_type_of(start) == "exhausted_batch"
                    else "diagnosis_no_progress"
                )
            )
            obj, identity = engine.correction_apply_work_item(
                context,
                candidate,
                blocking_finding_refs=start["blocking_finding_refs"],
                audit_identity=self._consumption_bound_audit_identity(start, variant),
                checkpoint_identity=(
                    self.replay.newest_checkpoint()["checkpoint_identity"]
                    if variant == "diagnosis_exhausted_batch"
                    and self.replay.newest_checkpoint() is not None
                    else None
                ),
                diagnosis_event_sha256=(
                    None if variant == "ordinary_specification" else start["diagnosis_event_sha256"]
                ),
                diagnosis_strategy_sha256=(
                    None if variant == "ordinary_specification" else start["diagnosis_strategy_sha256"]
                ),
                strategy_novelty_key=start["strategy_novelty_key"],
                correction_specification_sha256=start["correction_specification_sha256"],
                target_candidate_path=start["target_candidate_path"],
                authorized_triple=(
                    start["authorized_next_lifetime_round"],
                    start["authorized_batch_number"],
                    start["authorized_round_in_batch"],
                ),
                variant=variant,
            )
            return obj, identity, variant

        if self.trigger is not None and self.blocking_finding_refs:
            state = self.replay.diagnosis_trigger_state(
                self.trigger["diagnosis_trigger_identity"], self.semantic_scope_key
            )
            if state == "open":
                checkpoint = self.replay.newest_checkpoint()
                obj, identity = engine.correction_diagnosis_work_item(
                    context,
                    candidate,
                    self.blocking_finding_refs,
                    self.audit_identity,
                    None if checkpoint is None else checkpoint["checkpoint_identity"],
                    self.trigger["trigger_type"],
                )
                variant = (
                    "exhausted_batch"
                    if self.trigger["trigger_type"] == "exhausted_batch"
                    else "no_progress"
                )
                return obj, identity, variant

        diagnosis = newest_unconsumed_safe_diagnosis(self.replay)
        if diagnosis is not None:
            obj, identity = self._correction_apply_from_diagnosis(diagnosis)
            return obj, identity, self._diagnosis_variant(diagnosis)

        specification = newest_unconsumed_specification(self.replay)
        if specification is not None:
            obj, identity = engine.correction_apply_work_item(
                context,
                candidate,
                blocking_finding_refs=specification["blocking_finding_refs"],
                audit_identity=specification["audit_identity"],
                checkpoint_identity=None,
                diagnosis_event_sha256=None,
                diagnosis_strategy_sha256=None,
                strategy_novelty_key=specification["strategy_novelty_key"],
                correction_specification_sha256=specification[
                    "correction_specification_sha256"
                ],
                target_candidate_path=next_candidate_path(candidate.candidate_path),
                authorized_triple=(
                    specification["authorized_next_lifetime_round"],
                    specification["authorized_batch_number"],
                    specification["authorized_round_in_batch"],
                ),
                variant="ordinary_specification",
            )
            return obj, identity, "ordinary_specification"

        # A usable blocked audit now records its complete correction
        # specification in the same operation, so an ordinary correction_apply
        # work item is already selected above.  A candidate-producing Claude
        # result likewise records explanation content before it completes, so a
        # fresh candidate goes directly to the audit below.
        obj, identity = engine.design_audit_work_item(context, candidate)
        return obj, identity, None

    def _batch_bound_reached(self):
        lifetime = self.replay.correction_round_lifetime()
        if lifetime == 0:
            return False
        return batch_triple(lifetime)[2] == constants.CORRECTION_BATCH_SIZE

    def _diagnosis_variant(self, diagnosis):
        return (
            "diagnosis_exhausted_batch"
            if diagnosis.get("diagnosis_trigger_type") == "exhausted_batch"
            else "diagnosis_no_progress"
        )

    def _correction_apply_from_diagnosis(self, diagnosis):
        checkpoint = self.replay.newest_checkpoint()
        variant = self._diagnosis_variant(diagnosis)
        return engine.correction_apply_work_item(
            self.context,
            self.candidate,
            blocking_finding_refs=diagnosis["blocking_finding_refs"],
            audit_identity=self.audit_identity,
            checkpoint_identity=(
                checkpoint["checkpoint_identity"]
                if variant == "diagnosis_exhausted_batch" and checkpoint is not None
                else None
            ),
            diagnosis_event_sha256=diagnosis["event_sha256"],
            diagnosis_strategy_sha256=diagnosis["diagnosis_strategy_sha256"],
            strategy_novelty_key=diagnosis["strategy_novelty_key"],
            correction_specification_sha256=diagnosis["correction_specification_sha256"],
            target_candidate_path=next_candidate_path(self.candidate.candidate_path),
            authorized_triple=(
                diagnosis["authorized_next_lifetime_round"],
                diagnosis["authorized_batch_number"],
                diagnosis["authorized_round_in_batch"],
            ),
            variant=variant,
        )

    def _consumption_authority_event(self, start, variant):
        """The exact authenticated authority event an open consumption bound.

        Section 9.1's authority-field table: the start names its authority by
        BOTH ``diagnosis_event_seq`` and ``diagnosis_event_sha256``, and it
        re-records every authority field it consumed.  The event at that
        position is that authority only when it is the right type, hashes to
        the recorded digest, agrees on every re-recorded field, and the
        ``consumption_identity`` already durable re-derives from exactly those
        bindings.  Anything else is not PROVED to be the same authority, so it
        is not treated as one.
        """
        expected_type = (
            "correction_specification_recorded"
            if variant == "ordinary_specification"
            else "correction_diagnosis_recorded"
        )
        seq = start.get("diagnosis_event_seq")
        event = self.replay.by_seq(seq) if seq is not None else None
        if event is None or event.get("type") != expected_type:
            return None
        if event.get("event_sha256") != start.get("diagnosis_event_sha256"):
            return None
        shared = (
            "package_scope_id",
            "source_binding_sha256",
            "candidate_path",
            "candidate_sha256",
            "candidate_bytes",
            "correction_specification_sha256",
            "strategy_novelty_key",
            "authorized_next_lifetime_round",
            "authorized_batch_number",
            "authorized_round_in_batch",
        )
        if any(event.get(key) != start.get(key) for key in shared):
            return None
        if sorted(set(event.get("blocking_finding_refs") or [])) != sorted(
            set(start.get("blocking_finding_refs") or [])
        ):
            return None
        if variant != "ordinary_specification" and event.get(
            "diagnosis_strategy_sha256"
        ) != start.get("diagnosis_strategy_sha256"):
            return None
        rederived = derive(
            "consumption_identity",
            {
                "diagnosis_event_seq": event["event_seq"],
                "diagnosis_event_sha256": event["event_sha256"],
                "diagnosis_strategy_sha256": start.get("diagnosis_strategy_sha256"),
                "strategy_novelty_key": start.get("strategy_novelty_key"),
                "package_scope_id": start.get("package_scope_id"),
                "source_binding_sha256": start.get("source_binding_sha256"),
                "candidate_path": start.get("candidate_path"),
                "candidate_sha256": start.get("candidate_sha256"),
                "target_candidate_path": start.get("target_candidate_path"),
                "authorized_next_lifetime_round": start.get(
                    "authorized_next_lifetime_round"
                ),
                "authorized_batch_number": start.get("authorized_batch_number"),
                "authorized_round_in_batch": start.get("authorized_round_in_batch"),
            },
        )
        if rederived != start.get("consumption_identity"):
            return None
        return event

    def _consumption_bound_audit_identity(self, start, variant):
        """The ORIGINAL authority's audit identity, never the newer state's.

        Section 9.4 rows B7-B9.  Once this transaction's own candidate custody
        is durable the package's current candidate is the CHILD this
        consumption produced, so ``self.audit`` is the child's audit -- which
        does not exist -- and ``self.audit_identity`` is null.  Reconstructing
        the open apply work item from it would either fail identity validation
        before the resumption can run or, worse, rebuild the item against an
        authority the dispatched step never had.

        The consumption itself is the durable binding to its original
        authority, and that authority is what carries the audit: directly for
        the ordinary specification (Section 9.6), and through the candidate the
        diagnosis was recorded against for the two diagnosis rows (Section
        7.1).  If the authority is not proved exactly, this fails closed.
        """
        authority = self._consumption_authority_event(start, variant)
        if authority is None:
            raise IdentityError(
                "the open correction_apply consumption does not prove the "
                "authority it names, so the original audit identity cannot be "
                "reconstructed"
            )
        if variant == "ordinary_specification":
            identity = authority.get("audit_identity")
        else:
            identity = self._diagnosis_authority_audit_identity(authority, start)
        if identity is None:
            raise IdentityError(
                "the authority this open correction_apply consumption bound "
                "records no audit identity"
            )
        return identity

    def _diagnosis_authority_audit_identity(self, diagnosis, start):
        """The audit the diagnosis authority itself stood on, or ``None``.

        ``correction_diagnosis_recorded`` records no ``audit_identity`` of its
        own, so the chain is the one Section 7.1 already requires: the
        diagnosis is bound to a candidate, and the audit of record for that
        candidate is the newest one authenticated strictly before it.  Where
        the consumed trigger is a batch checkpoint, that checkpoint DID record
        an ``audit_identity``, and the two must name the same audit.
        """
        recorded = None
        trigger = self.replay.by_seq(diagnosis.get("diagnosis_trigger_event_seq"))
        if trigger is not None and trigger.get("type") == (
            "correction_batch_checkpoint_recorded"
        ):
            recorded = trigger.get("audit_identity")
        audit = None
        for event in self.replay.audits_for_candidate(start.get("candidate_sha256")):
            if event["event_seq"] < diagnosis["event_seq"]:
                audit = event
        if audit is None:
            return None
        identity = audit.get("audit_identity")
        if recorded is not None and recorded != identity:
            return None
        return identity

    def _trigger_type_of(self, consumption_start):
        seq = consumption_start.get("diagnosis_event_seq")
        event = self.replay.by_seq(seq) if seq else None
        if event is None:
            return "no_progress"
        return event.get("diagnosis_trigger_type") or "no_progress"

    # -- provider projection ------------------------------------------------
    def provider_projection(self):
        kind = constants.PROVIDER_KIND_BY_WORK_ITEM_KIND[self.work_item_obj["work_item_kind"]]
        record, endpoint = self.context.capability_record(kind)
        if endpoint is None:
            return {
                "provider_kind": None,
                "provider_endpoint_identity": None,
                "capability_record": None,
                "episode_identity": None,
                "episode_generation": None,
                "request_identity": None,
                "phase": "none",
                "serial_next": None,
            }
        generation = self.replay.episode_generation(self.work_item_id, kind, endpoint)
        episode = self.replay.episode_identity(self.work_item_id, kind, endpoint, generation)
        serial = self.replay.provider_dispatch_serial(self.work_item_id, kind, episode)
        current = None
        for identity in reversed(self.open_requests):
            prepared = self.replay.prepared_event(identity)
            if prepared is not None and prepared.get("work_item_identity") == self.work_item_id:
                current = identity
                break
        if current is None:
            for event in reversed(self.replay.scoped("provider_request_terminal_recorded")):
                if event.get("work_item_identity") == self.work_item_id and event.get(
                    "provider_availability_episode_identity"
                ) == episode:
                    current = event["provider_request_identity"]
                    break
        return {
            "provider_kind": kind,
            "provider_endpoint_identity": endpoint,
            "capability_record": record,
            "episode_identity": episode,
            "episode_generation": generation,
            "request_identity": current,
            "phase": "none" if current is None else self.replay.provider_phase(current),
            "serial_next": serial,
        }


# ---------------------------------------------------------------------------
# Section 9.3 -- consumption reconciliation.
# ---------------------------------------------------------------------------
def consumption_reconciliation(situation):
    replay = situation.replay
    start = replay.newest_consumption_start()
    if start is None:
        return "none", None
    terminals = replay.consumption_terminals(start["consumption_identity"])
    if len(terminals) > 1:
        return "contradiction", start["consumption_identity"]
    if terminals:
        terminal = terminals[0]
        if terminal["type"] == "diagnosis_strategy_consumption_completed":
            return "closed_completed", start["consumption_identity"]
        if terminal["type"] == "mechanical_no_progress_recorded":
            return "closed_no_progress", start["consumption_identity"]
        return "closed_terminated", start["consumption_identity"]

    identity = start["consumption_identity"]
    work_item = start["work_item_identity"]
    projection = situation.provider_projection()
    episode = projection["episode_identity"]

    exhaustion = None
    for event in replay.scoped("provider_availability_episode_exhausted_recorded"):
        if event.get("open_consumption_identity") == identity:
            exhaustion = event
    if exhaustion is not None and replay.accepted_episode_unlock(
        exhaustion["provider_availability_episode_identity"]
    ) is None:
        return "open_awaiting_provider_episode_unlock", identity

    for pending in replay.custodied_results_awaiting_processing():
        if pending.get("work_item_identity") == work_item:
            return "open_awaiting_result_processing", identity

    for request in replay.open_provider_requests():
        prepared = replay.prepared_event(request)
        if prepared is not None and prepared.get("work_item_identity") == work_item:
            phase = replay.provider_phase(request)
            if phase in ("prepared", "dispatch_begun", "accepted"):
                return "open_awaiting_provider_reconciliation", identity

    terminal = None
    for event in replay.scoped("provider_request_terminal_recorded"):
        if event.get("work_item_identity") == work_item:
            terminal = event
    if terminal is not None:
        kind = terminal["terminal_kind"]
        budget = replay.bounded_output_retry_budget(
            work_item, terminal["provider_kind"], terminal[
                "provider_availability_episode_identity"
            ]
        )
        if kind in ("provider_error_retryable", "abandoned_absent_proved"):
            return "open_awaiting_bounded_retry", identity
        if kind in ("result_invalid", "result_oversize_uncustodied") and budget == "available":
            return "open_awaiting_bounded_retry", identity
        return "open_requires_closure", identity
    return "open_requires_closure", identity


# ---------------------------------------------------------------------------
# Section 4.11c -- the semantic-scope-unlock availability projection and the
# Section 4.11 D-1..D-4 selection, derived identically by both readers.
# ---------------------------------------------------------------------------
def qualifying_unlock_evidence(context, events, situation):
    """The COMPLETE qualifying set for the current scope key (rule D-1)."""
    replay = situation.replay
    scope_key = situation.semantic_scope_key
    qualifying = []

    exhaustion = replay.scope_exhaustion_event(scope_key)

    # E-cap: exactly one authenticated exhaustion event supplies the baseline.
    if exhaustion is not None:
        observed = context.capability_snapshot()
        comparison = capability.compare_snapshots(
            exhaustion["capability_baseline"], observed
        )
        selected = comparison["selected_entry"]
        if selected is not None:
            qualifying.append(
                {
                    "unlock_evidence_kind": "authenticated_capability_record_updated",
                    "unlock_evidence_identity": selected[
                        "provider_capability_record_identity"
                    ],
                    "unlock_evidence_sha256": selected["provider_capability_record_sha256"],
                    "baseline_entry": comparison["selected_baseline_entry"],
                    "observed_snapshot": observed,
                    "changed_entry_count": comparison["changed_entry_count"],
                    "exhaustion": exhaustion,
                }
            )

    # E-ness: either the same exhaustion event exists, or a CURRENT family-4
    # occurrence O satisfies superseded_scope_key(O) == the named key.
    reader = context.accepted_ness_decision_records
    records = list(reader() if reader else [])
    family4 = current_family4_occurrences(context, situation)
    for record in records:
        if record.get("package_scope_id") != context.binding.package_scope_id:
            continue
        if record.get("exhausted_semantic_scope_key") != scope_key:
            continue
        if not record.get("digest_verified", False):
            continue
        if exhaustion is None:
            named_work_item = record.get("work_item_identity")
            named_resource = record.get("source_repository_resource_identity")
            matched = False
            for occurrence in family4:
                if occurrence["superseded_scope_key"] != scope_key:
                    continue
                rec = occurrence["record"]
                if named_work_item is not None and rec["work_item_identity"] == named_work_item:
                    matched = True
                    break
                if (
                    named_resource is not None
                    and rec["resource_kind"] == "source_repository"
                    and rec["resource_identity"] == named_resource
                ):
                    matched = True
                    break
            if not matched:
                continue
        qualifying.append(
            {
                "unlock_evidence_kind": "accepted_ness_decision_record",
                "unlock_evidence_identity": record["identity"],
                "unlock_evidence_sha256": record["sha256"],
                "baseline_entry": None,
                "observed_snapshot": None,
                "changed_entry_count": None,
                "exhaustion": exhaustion,
            }
        )
    return qualifying


def select_unlock_evidence(qualifying):
    """Rules D-2, D-3 and D-4 over the complete qualifying set."""
    if not qualifying:
        return None
    for kind in constants.SEMANTIC_UNLOCK_KIND_PRECEDENCE:
        inside = [item for item in qualifying if item["unlock_evidence_kind"] == kind]
        if not inside:
            continue
        # D-4: byte-identical tuples collapse to one selection.
        collapsed = {}
        for item in inside:
            key = (
                item["unlock_evidence_identity"].encode("utf-8"),
                item["unlock_evidence_sha256"].encode("utf-8"),
            )
            collapsed.setdefault(key, item)
        # D-3: the smallest tuple, unsigned byte-wise, first component deciding.
        smallest = min(collapsed)
        return collapsed[smallest]
    return None


def semantic_scope_unlock_available(context, events, situation):
    return bool(qualifying_unlock_evidence(context, events, situation))


def current_family4_occurrences(context, situation):
    """Section 11.9b F4.1-F4.4 -- membership decided structurally."""
    replay = situation.replay
    found = []
    for occurrence in replay.current_occurrences():
        record = occurrence["record"]
        if record.get("dependency_class") != "no_currently_safe_strategy":
            continue
        predicate = (record.get("unlock_predicate") or {}).get("predicate_kind")
        if predicate != "new_ness_decision_or_source_change":
            continue
        carrier_seq = occurrence["carrier_event_seq"]
        scope_key = superseded_scope_key(context, situation, carrier_seq)
        # F4.3 -- exactly one of the two literal scopes.
        in_work_item_scope = record["work_item_identity"] == situation.work_item_id
        in_package_scope = (
            record["resource_kind"] == "source_repository"
            and record["resource_identity"] == context.binding.package_scope_id
            and scope_key == situation.semantic_scope_key
        )
        if not (in_work_item_scope or in_package_scope):
            continue
        if not still_current(context, situation, occurrence, scope_key, carrier_seq):
            continue
        found.append(
            {
                "record": record,
                "dependency_identity": occurrence["dependency_identity"],
                "carrier_event_seq": carrier_seq,
                "superseded_scope_key": scope_key,
                "scope": "work_item" if in_work_item_scope else "package",
            }
        )
    return found


def superseded_scope_key(context, situation, carrier_event_seq):
    """The package's semantic_scope_key at the carrier position (Section 11.9b)."""
    prefix = [event for event in situation.events if event["event_seq"] <= carrier_event_seq]
    prefix_replay = replay_mod.Replay(prefix, context.binding.package_scope_id)
    generation = prefix_replay.semantic_unlock_generation()
    custody = prefix_replay.candidate_custody_events()
    if custody:
        newest = custody[-1]
        path = newest["candidate_path"]
        digest = newest["candidate_sha256"]
        length = newest["candidate_bytes"]
    else:
        base = situation.context_candidate()
        path, digest, length = base.candidate_path, base.candidate_sha256, base.candidate_bytes
    audit = prefix_replay.newest_audit(digest)
    refs = (
        sorted(set(audit.get("mechanical_blocker_refs") or []))
        if audit is not None and audit.get("verdict") == "BLOCKED"
        else (
            sorted(set(context.blocking_finding_refs_override))
            if context.blocking_finding_refs_override is not None
            else []
        )
    )
    return prefix_replay.semantic_scope_key(
        context.binding.package_scope_id,
        context.binding.source_binding_sha256,
        path,
        digest,
        length,
        refs,
        generation,
    )


def still_current(context, situation, occurrence, scope_key, carrier_event_seq):
    """Rules S-a, S-b and S-c: nothing else removes a family-4 member."""
    for unlock in situation.replay.scoped("semantic_scope_unlock_recorded"):
        if unlock.get("unlock_accepted") is not True:
            continue
        if unlock["event_seq"] <= carrier_event_seq:
            continue  # (c) order
        if unlock.get("package_scope_id") != context.binding.package_scope_id:
            continue  # (a) package
        if unlock.get("exhausted_semantic_scope_key") != scope_key:
            continue  # (b) semantic scope
        return False
    # S-b: a changed candidate, source binding, or blocker set moves it out of
    # F4.3 scope, which the caller already tested through the derived keys.
    return True


# ---------------------------------------------------------------------------
# Section 11.9b -- the outstanding-person-conditions predicate.
# ---------------------------------------------------------------------------
def outstanding_person_conditions(context, situation, closed_episode_identity,
                                  exclude_self_occurrence=None):
    replay = situation.replay
    conditions = []
    for occurrence in replay.current_occurrences():
        record = occurrence["record"]
        identity = occurrence["dependency_identity"]
        if exclude_self_occurrence is not None and identity == exclude_self_occurrence:
            continue
        klass = record["dependency_class"]
        if klass == "external_user_action_required":
            conditions.append(("family1", identity))
        elif klass == "provider_outcome_unknown":
            if record["work_item_identity"] == situation.work_item_id:
                conditions.append(("family2", identity))
        elif klass == "authority_or_safety_conflict":
            conditions.append(("family3", identity))
    for member in current_family4_occurrences(context, situation):
        conditions.append(("family4", member["dependency_identity"]))
    # Family 6 -- any open provider request of that work item.
    for request in replay.open_provider_requests():
        prepared = replay.prepared_event(request)
        if prepared is not None and prepared.get("work_item_identity") == (
            situation.work_item_id
        ):
            conditions.append(("family6", request))
    return sorted(set(conditions))


# ---------------------------------------------------------------------------
# Command selection -- Sections 13.1, 11.4 and 5.1 P-4.
# ---------------------------------------------------------------------------
def collision_position(context, situation):
    """Section 5.1 P-4 -- ``None`` or ``('A'|'B'|'C', custody_event)``."""
    from . import auditresult

    for custody in situation.replay.scoped("provider_result_custody_recorded"):
        if custody.get("work_item_kind") != "design_audit":
            continue
        request = custody["provider_request_identity"]
        terminal = situation.replay.terminal_event(request)
        if terminal is None or terminal.get("terminal_kind") != "result_received":
            continue
        try:
            payload = engine.custodied_bytes(context, custody)
        except Exception:  # noqa: BLE001 -- unverifiable custody is row C17
            continue
        value, error = engine.parse_result_bytes(payload)
        if error is not None or not isinstance(value, dict):
            continue
        structural = auditresult.derive_structural_facts(value)
        if not auditresult.projection_has_repeated_entry(structural):
            continue
        completion = situation.replay.collision_closure_completion(request)
        if completion is not None:
            return "C", custody
        started = None
        for event in situation.replay.scoped("supervisor_operation_started"):
            if event.get("supervisor_command") != "process-custodied-provider-result":
                continue
            if event.get("work_item_identity") != custody.get("work_item_identity"):
                continue
            if situation.replay.completed_event(event["supervisor_operation_id"]) is None:
                started = event
        if started is not None:
            return "B", custody
        return "A", custody
    return None


# ---------------------------------------------------------------------------
# Sections 6.5a, 10.1, 10.3, 11.1 and 14 Phase A -- the acceptance projection.
#
# Two questions are kept apart here, permanently, because they have different
# answers and different evidence:
#
#   * Is this event authentic, complete, in scope and correctly bound?
#     -- raw journal replay (Section 10.3 rules 1 to 6).
#   * Is acceptance terminal, and safe to EXPOSE as terminal?
#     -- the governed projection, which additionally needs the exclusive lock
#     this reader holds (Section 10.3 rule 7).
#
# Nothing below appends, repairs, recovers, or removes anything.
# ---------------------------------------------------------------------------
def acceptance_phase_position(replay):
    """Which Section 14 Phase A position the durable chain is actually in.

    Returns ``{"kind": ..., "reason": ...}`` where ``kind`` is one of:

      ``none``                     -- no PASS and no final explanation yet;
      ``a5_completion_required``   -- a final explanation is durable and its
                                      OWN operation's matching completion is
                                      not (row P-3b);
      ``a6_completion_required``   -- the PASS is durable and its OWN
                                      operation's matching completion is not
                                      (row P-4);
      ``ready``                    -- the complete effect-owning chain stands;
      ``contradiction``            -- two pairs both qualify to own one
                                      substantive event, which is refused and
                                      never chosen between.

    A PRE-EFFECT unmatched start -- an operation that started and died before
    it appended anything substantive -- owns no effect.  It is preserved
    historical residue: it is not reaped, not paired to a later operation's
    completion, and it never blocks the pair that really owns the effect.
    ``effect_owning_completed_pair`` decides that by the fields the installed
    events actually carry, so nothing here has to reason about it again.
    """
    # A5 first, and this order is the rule rather than a convenience: Section
    # 14 prohibits A6 from starting until the matching A5 completion is
    # durable, so an incomplete A5 is answered before the PASS is even looked
    # at.
    for explanation in replay.acceptance_explanation_events(
        replay_mod.FINAL_ACCEPTANCE_EXPLANATION_STAGE
    ):
        pair = replay.effect_owning_completed_pair(explanation)
        if pair == "duplicate":
            return {
                "kind": "contradiction",
                "reason": "acceptance_explanation_owned_by_two_operations",
            }
        if pair is None:
            return {
                "kind": "a5_completion_required",
                "reason": "acceptance_explanation_awaiting_operation_completion",
            }

    pass_event = replay.pass_event()
    if pass_event is None:
        return {"kind": "none", "reason": None}
    pair = replay.effect_owning_completed_pair(pass_event)
    if pair == "duplicate":
        return {
            "kind": "contradiction",
            "reason": "mechanical_pass_owned_by_two_operations",
        }
    if pair is None:
        return {
            "kind": "a6_completion_required",
            "reason": "mechanical_pass_awaiting_operation_completion",
        }
    return {"kind": "ready", "reason": "mechanical_pass_recorded"}


def acceptance_content_stage(situation):
    """Which Section 14 Phase A preparation step the acceptance path still owes.

    Returns ``{"kind": ..., "reason": ..., "content_digest": ...}`` where
    ``kind`` is one of:

      ``content_required`` -- step A2 has not happened: no CURRENT
                              content-stage explanation binds this exact
                              candidate, so parts 1-6 do not exist yet;
      ``audit_required``   -- step A2 is durable but step A3 is not: the
                              candidate's current audit did not read those
                              exact fixed bytes, so it covered no explanation
                              and cannot be bound as the audit of one;
      ``covered``          -- the current audit records exactly the current
                              content digest, so A4/A5/A6 may proceed;
      ``contradiction``    -- two unsuperseded content records share the
                              highest version, which is refused and never
                              chosen between (Section 7.5 rule 3).

    WHY THIS EXISTS AND WHAT IT DELIBERATELY DOES NOT DO.  The installed
    baseline reached ``READY_FOR_ACCEPTANCE`` from a PASS whose audit was
    recorded before any acceptance explanation existed.  That PASS is real,
    authenticated history and stays exactly as it is; it simply is not proof
    that anybody audited prose that did not exist when it ran.  This function
    answers only "which preparation step is owed", from the records themselves.
    It appends nothing, repairs nothing, removes nothing, and dispatches no
    candidate correction: absent explanation content is missing PREPARATION,
    never a defect of the candidate.
    """
    replay = situation.replay
    candidate_sha256 = situation.candidate.candidate_sha256
    content = replay.current_acceptance_explanation(
        candidate_sha256, None, None, stage=constants.EXPLANATION_STAGE_CONTENT
    )
    if content == "duplicate":
        return {
            "kind": "contradiction",
            "reason": "acceptance_explanation_content_contradiction",
            "content_digest": None,
        }
    if content is None:
        return {
            "kind": "content_required",
            "reason": "acceptance_explanation_content_required",
            "content_digest": None,
        }
    digest = content.get("explanation_content_digest")
    if not digest:
        return {
            "kind": "content_required",
            "reason": "acceptance_explanation_content_required",
            "content_digest": None,
        }
    audit = situation.audit
    if audit is None or audit.get("explanation_content_digest") != digest:
        return {
            "kind": "audit_required",
            "reason": "acceptance_explanation_audit_required",
            "content_digest": digest,
        }
    return {"kind": "covered", "reason": None, "content_digest": digest}


def acceptance_preparation_owed(situation):
    """True while Section 14 Phase A steps A2-A3 are not both durable.

    It is asked only where the candidate is otherwise fit -- its current audit
    says PASS -- because A1 requires the candidate's bytes to be FINAL before
    its prose is prepared.  Preparing an explanation for a candidate that is
    about to be corrected would describe a candidate that will not exist.
    """
    if situation.audit is None or situation.audit.get("verdict") != "PASS":
        return False
    return acceptance_content_stage(situation)["kind"] != "covered"


def pass_event_binds_current_audit(situation):
    """Section 7.7 -- is the current pass event bound to the CURRENT audit?

    A PASS binds one exact ``audit_identity``.  Where a later usable audit for
    the same candidate exists, the earlier PASS is not stale history to be
    deleted -- it is preserved authenticated history that simply is not the
    PASS of the audit now in force, so it cannot carry readiness for it.
    """
    pass_event = situation.replay.pass_event()
    if pass_event is None or situation.audit is None:
        return False
    return pass_event.get("audit_identity") == situation.audit.get("audit_identity")


def acceptance_record_binding_problems(context, situation, record):
    """Section 10.3 rules 2 to 6 -- raw-replay validity of one record.

    Rule 1 (structure and authentication) is already proved by the reader that
    produced these events; a record that failed it never reaches here.  Rule 7
    is the LOCK, and it is deliberately not tested in this function, because
    this function answers the raw-replay question and only that one.
    """
    replay = situation.replay
    problems = []
    if record.get("package_scope_id") != context.binding.package_scope_id:
        problems.append("the acceptance record binds another package scope")
    candidate = situation.candidate
    for key, value in (
        ("candidate_path", candidate.candidate_path),
        ("candidate_sha256", candidate.candidate_sha256),
        ("candidate_bytes", candidate.candidate_bytes),
    ):
        if record.get(key) != value:
            problems.append(
                "the acceptance record binds a %s that is not the current one" % key
            )
    for seq_key, digest_key, label in (
        ("audit_event_seq", "audit_event_sha256", "audit"),
        ("pass_event_seq", "pass_event_sha256", "pass"),
        ("explanation_event_seq", "explanation_event_sha256", "explanation"),
    ):
        named = replay.by_seq(record.get(seq_key))
        if named is None:
            problems.append("the acceptance record names a %s event that does not exist" % label)
            continue
        if named.get("event_sha256") != record.get(digest_key):
            problems.append(
                "the acceptance record names a %s event whose digest does not match" % label
            )
    if record.get("acceptance_scope_id") != constants.ACCEPTANCE_SCOPE_ID:
        problems.append("the acceptance record binds another acceptance scope id")
    if record.get("acceptance_scope_digest") != constants.acceptance_scope_digest():
        problems.append(
            "the acceptance record binds a scope digest that is not this "
            "controller's fixed scope text"
        )
    return problems


def acceptance_truth(situation):
    """Section 11.1b -- exactly three classifications, and no fourth.

    ``PROVED_NOT_ACCEPTED`` -- the authenticated history proves the exact
    pre-acceptance prefix and no complete acceptance exists in scope.

    ``PROVED_ACCEPTED``     -- exactly one complete, authenticated, correctly
    bound acceptance record is durably proved in scope AND this reader holds
    the exclusive journal lock, so no live writer retains legal authority to
    remove it.

    ``UNRESOLVED``          -- neither side is safely proved.  It is a DERIVED
    condition, never a stored flag, never an event type, never a mark and never
    a workflow state value.
    """
    context = situation.context
    replay = situation.replay
    record = replay.current_ness_acceptance()
    if record is None:
        # The authenticated read already proved this history complete, so the
        # absence of the record is proved, not merely unobserved.
        return constants.ACCEPTANCE_TRUTH_NOT_ACCEPTED
    if record == "duplicate":
        return constants.ACCEPTANCE_TRUTH_UNRESOLVED
    if acceptance_record_binding_problems(context, situation, record):
        # A contradiction is precisely "neither side safely proved".  It is
        # never silently ignored and never read as acceptance of whatever the
        # current candidate happens to be (Section 10.4).
        return constants.ACCEPTANCE_TRUTH_UNRESOLVED
    if not situation.locked_snapshot:
        return constants.ACCEPTANCE_TRUTH_UNRESOLVED
    return constants.ACCEPTANCE_TRUTH_ACCEPTED


def derive_workflow_projection(context, events, candidate=None, lease_state=None, lease=None):
    """The single derivation every report and every completion digest reads."""
    situation = Situation(context, events, candidate, lease_state, lease)
    return _project(context, situation)


def _project(context, situation):
    replay = situation.replay
    projection = situation.provider_projection()
    result = {
        "situation": situation,
        "workflow_state": "IDLE",
        "next_command": None,
        "work_item_identity": situation.work_item_id,
        "work_item_kind": situation.work_item_obj["work_item_kind"],
        "dependency_slot": None,
        "reason": None,
        "provider": projection,
        "interview_projection": None,
        "interview_gate_projection": None,
        "ness_decision_clearance": None,
        "ness_question_binding": None,
        "ness_answer_clarification": None,
        "ness_decision_cleared": False,
    }

    # Precedence 1 -- the one narrow Section 5.1 P-4 collision continuation.
    collision = collision_position(context, situation)
    if collision is not None and collision[0] in ("A", "B"):
        result["workflow_state"] = "WAITING_RECOVERING"
        result["next_command"] = "process-custodied-provider-result"
        result["reason"] = "collision_closure_owed_%s" % collision[0]
        return result

    # Precedence 2 -- contradictions and the read-only lease projection.
    if situation.contradictions:
        result["workflow_state"] = "SAFETY_HOLD"
        result["reason"] = "custody_contradiction"
        return result
    if collision is not None and collision[0] == "C":
        result["workflow_state"] = "SAFETY_HOLD"
        result["reason"] = "design_audit_result_usability_contradiction"
        return result
    if situation.lease_state == "INVALID_UNPROVED":
        result["workflow_state"] = "SAFETY_HOLD"
        result["reason"] = "lease_ownership_unproved"
        return result

    # Precedence 3 -- a custodied result whose continuation is unfinished.
    if situation.pending_custody:
        result["workflow_state"] = "WAITING_RECOVERING"
        result["next_command"] = "process-custodied-provider-result"
        result["reason"] = "custodied_result_awaiting_processing"
        return result

    # Precedence 4 -- an open provider request.
    if situation.open_requests:
        result["workflow_state"] = "WAITING_RECOVERING"
        result["next_command"] = "reconcile-provider-request"
        result["reason"] = "provider_request_unreconciled"
        phase = replay.provider_phase(situation.open_requests[-1])
        if phase in ("none", "prepared"):
            result["next_command"] = "execute-next-claude-task"
            result["reason"] = "dispatch_proved_never_begun"
        return result

    # Precedence 5 -- an exhausted provider-availability episode awaiting an
    # unlock.  Section 11.9's exhaustion record carries the row-C11 or row-C11a
    # dependency, and that record's `next_workflow_state` is the state until an
    # unlock is accepted.  The exhaustion is what holds the run, so it holds it
    # whether or not a consumption happens to be open beneath it: the two rows
    # say nothing about consumptions, and a work item with no consumption at all
    # (a design audit, a diagnosis) reaches the same bound in the same way.
    consumption_state, consumption_identity = consumption_reconciliation(situation)
    eligibility = episode_unlock_eligibility(context, situation)
    if (
        consumption_state == "open_awaiting_provider_episode_unlock"
        or eligibility["closed_episode_identity"] is not None
    ):
        result["workflow_state"] = "WAITING_RECOVERING"
        if eligibility["episode_unlock_automatic_eligible"]:
            result["next_command"] = "open-new-provider-episode"
        elif eligibility["availability_probe_automatic_eligible"]:
            result["next_command"] = "probe-provider-availability"
        else:
            result["workflow_state"] = "NEEDS_USER_ACTION"
            result["next_command"] = None
        result["reason"] = "episode_exhausted_awaiting_unlock"
        return result

    # Precedence 6 -- an unclosed consumption with a proved final outcome.
    if consumption_state == "open_requires_closure":
        result["workflow_state"] = "WORKING"
        result["next_command"] = "close-open-consumption"
        result["reason"] = "consumption_requires_closure"
        return result
    if consumption_state == "open_awaiting_bounded_retry":
        result["workflow_state"] = "WAITING_RECOVERING"
        result["next_command"] = "execute-next-claude-task"
        result["reason"] = "bounded_output_retry"
        return result

    # Precedence 7 -- a proved semantic-scope unlock.
    if semantic_scope_unlock_available(context, situation.events, situation):
        result["workflow_state"] = "WAITING_RECOVERING"
        result["next_command"] = "record-semantic-scope-unlock"
        result["reason"] = "semantic_scope_unlock_available"
        return result

    # Precedence 8 -- the per-scope no-progress bound and scope exhaustion.
    rounds = replay.no_progress_rounds_in_scope(situation.semantic_scope_key)
    if rounds >= constants.MAX_NO_PROGRESS_ROUNDS_PER_SEMANTIC_SCOPE:
        result["workflow_state"] = "WAITING_RECOVERING"
        result["next_command"] = "diagnose-next-correction-batch"
        result["reason"] = "semantic_no_progress_bound_reached"
        return result
    if replay.semantic_scope_exhausted(situation.semantic_scope_key):
        result["workflow_state"] = "WAITING_RECOVERING"
        result["next_command"] = None
        result["reason"] = "semantic_scope_exhausted"
        return result

    # Precedence 9 -- an open diagnosis trigger.
    if situation.trigger is not None:
        state = replay.diagnosis_trigger_state(
            situation.trigger["diagnosis_trigger_identity"], situation.semantic_scope_key
        )
        if state == "open":
            result["workflow_state"] = "DIAGNOSING"
            result["next_command"] = "diagnose-next-correction-batch"
            result["reason"] = "diagnosis_trigger_open"
            return result
        if state == "contradiction":
            result["workflow_state"] = "SAFETY_HOLD"
            result["reason"] = "diagnosis_trigger_contradiction"
            return result
        if state == "closed_safety_hold":
            result["workflow_state"] = "SAFETY_HOLD"
            result["reason"] = "diagnosis_closed_safety_hold"
            return result
        if state in ("closed_no_safe_strategy", "closed_validation_failed",
                     "closed_scope_exhausted"):
            result["workflow_state"] = "WAITING_RECOVERING"
            result["next_command"] = None
            result["reason"] = state
            return result

    # Precedence 9a -- Section 8.2's outcome routing for a recorded diagnosis
    # that is NOT a safe new mechanical strategy.  Those five outcomes each name
    # the state the run is in, and that state holds until the condition the
    # diagnosis named is itself resolved: a possible Ness choice is not "working",
    # an authority conflict is not "working", and a technical dependency is not
    # "working".  Only `safe_new_mechanical_strategy` continues the loop, and it
    # is handled by the precedence below.
    recorded_diagnoses = replay.scoped("correction_diagnosis_recorded")
    if recorded_diagnoses:
        newest_diagnosis = recorded_diagnoses[-1]
        if newest_diagnosis.get("diagnosis_outcome") == "possible_ness_choice":
            ness = _possible_ness_status(context, situation, newest_diagnosis)
            result.update(ness)
            if ness.get("answer_record_unreadable"):
                result["workflow_state"] = "SAFETY_HOLD"
                result["next_command"] = None
                result["reason"] = "answer_record_unreadable"
                return result
            if not ness["projection_proved"]:
                result["workflow_state"] = "WAITING_RECOVERING"
                result["next_command"] = None
                result["reason"] = "ness_projection_unproved"
                return result
            if ness["askable_question_present"]:
                result["workflow_state"] = "NEEDS_NESS_DECISION"
                result["next_command"] = None
                result["reason"] = "deliverable_ness_question_present"
                return result
            if ness["gate_unlocked_for_this_package"]:
                # Row 3 bypasses only this diagnosis pin.  The retained history
                # continues immediately at precedence 10 below.
                result["ness_decision_cleared"] = True
            else:
                reasons = set(
                    (ness.get("interview_gate_projection") or {}).get("reasons") or ()
                )
                validation_reasons = {
                    "no_current_package_bound_validation",
                    "validation_inventory_incomplete",
                    "routing_signals_not_yet_validated",
                    "fresh_revalidation_required_after_an_answer",
                    "source_moved_since_the_validation",
                }
                if reasons & validation_reasons:
                    result["workflow_state"] = "WORKING"
                    result["next_command"] = "question-validation"
                    result["reason"] = "piece3_question_validation_required"
                elif "fresh_question_coverage_review_required" in reasons:
                    result["workflow_state"] = "WORKING"
                    result["next_command"] = "question-coverage-review"
                    result["reason"] = "piece3_question_coverage_review_required"
                else:
                    result["workflow_state"] = "WAITING_RECOVERING"
                    result["next_command"] = None
                    result["reason"] = "piece3_gate_locked"
                return result
        elif newest_diagnosis.get("diagnosis_outcome") != "safe_new_mechanical_strategy":
            result["workflow_state"] = newest_diagnosis["next_workflow_state"]
            result["next_command"] = None
            result["reason"] = "diagnosis_outcome_%s" % newest_diagnosis[
                "diagnosis_outcome"
            ]
            return result

    # Precedence 10 -- an unconsumed safe diagnosis authorises a correction.
    diagnosis = newest_unconsumed_safe_diagnosis(replay)
    if diagnosis is not None:
        result["workflow_state"] = "WORKING"
        result["next_command"] = "execute-next-claude-task"
        result["reason"] = "safe_strategy_awaiting_consumption"
        return result

    # Precedence 11 -- a batch that has reached its bound needs the checkpoint.
    if batch_checkpoint_required(situation):
        result["workflow_state"] = "DIAGNOSING"
        result["next_command"] = "diagnose-next-correction-batch"
        result["reason"] = "correction_batch_limit"
        return result

    # Precedence 11.5 -- ACCEPTANCE IS TERMINAL (Section 10.1).
    #
    # It is placed ABOVE the PASS rule and BELOW every safety, contradiction
    # and journal-integrity refusal above: an unauthenticated journal or a
    # safety hold is always answered first, acceptance never overrides one, and
    # a safety refusal never erases a committed acceptance.
    #
    # It fires on the GOVERNED truth of Section 11.1, never on raw replay: a
    # complete record inside the interrupted-append window is real, and is
    # still removable by the live writer that declared it, so a reader without
    # the lock may not publish it as terminal.
    truth = acceptance_truth(situation)
    if truth == constants.ACCEPTANCE_TRUTH_ACCEPTED:
        result["workflow_state"] = constants.ACCEPTED_FOR_DESIGN_ONLY
        result["next_command"] = None
        result["reason"] = "ness_candidate_acceptance_recorded"
        return result
    if truth == constants.ACCEPTANCE_TRUTH_UNRESOLVED:
        # Neither accepted nor not accepted.  Non-running, no command, no
        # retry loop, no Accept control -- and no claim in either direction
        # (Sections 10.5, 11.1b, 12.5).  It is carried on the EXISTING
        # non-running safety value because Section 10.1 adds exactly one new
        # state value and UNRESOLVED is deliberately not one.
        result["workflow_state"] = "SAFETY_HOLD"
        result["next_command"] = None
        result["reason"] = "acceptance_truth_unresolved"
        return result

    # Precedence 12 -- PASS gating, strengthened by the accepted design.
    #
    # THE PASS EVENT ALONE IS NOT READINESS.  Section 6.5a requires the exact
    # matching effect-owning completed operation pairs as well: an operation
    # that appended its substantive event and died before its completion left
    # runnable completion-recovery work, not an acceptance-ready package.
    position = acceptance_phase_position(replay)
    if position["kind"] == "contradiction":
        result["workflow_state"] = "SAFETY_HOLD"
        result["next_command"] = None
        result["reason"] = position["reason"]
        return result
    if position["kind"] in (
        "a5_completion_required",
        "a6_completion_required",
    ):
        # The owner exists and is reachable: this is the SAME command the loop
        # already runs, routed by its reason to same-operation completion
        # recovery.  It appends only the missing matching completion -- no
        # second PASS, no second explanation, no fresh audit, and no provider
        # dispatch (Section 14 rows P-3b and P-4).
        result["workflow_state"] = "WAITING_RECOVERING"
        result["next_command"] = "execute-next-claude-task"
        result["reason"] = position["reason"]
        return result
    # The offer needs an explanation that the bound audit ACTUALLY READ.  New
    # candidate calls make that prose durable before their first audit, so one
    # independent audit covers both.  Historical records remain readable; a
    # new-contract PASS with missing prose fails closed below instead of
    # launching the retired separate preparation call.
    stage = acceptance_content_stage(situation)
    if stage["kind"] == "contradiction":
        result["workflow_state"] = "SAFETY_HOLD"
        result["next_command"] = None
        result["reason"] = stage["reason"]
        return result

    if (
        position["kind"] == "ready"
        and stage["kind"] == "covered"
        and pass_event_binds_current_audit(situation)
    ):
        result["workflow_state"] = "READY_FOR_ACCEPTANCE"
        result["next_command"] = None
        result["reason"] = "mechanical_pass_recorded"
        return result

    if situation.audit is not None and situation.audit.get("verdict") == "PASS":
        if stage["kind"] == "content_required":
            # New candidate-producing Claude contracts make content durable in
            # the same operation as candidate custody.  Reaching PASS without
            # it is therefore a contract/recovery contradiction, not permission
            # to launch the retired separate explanation call.
            result["workflow_state"] = "SAFETY_HOLD"
            result["next_command"] = None
            result["reason"] = "candidate_acceptance_explanation_missing"
            return result
        if stage["kind"] != "covered":
            # Preparation, never correction.  A missing or unaudited
            # explanation says nothing about the candidate's meaning, so no
            # candidate correction is dispatched and no new candidate is made.
            result["workflow_state"] = "WORKING"
            result["next_command"] = "execute-next-claude-task"
            result["reason"] = stage["reason"]
            return result
        result["workflow_state"] = "WORKING"
        result["next_command"] = "execute-next-claude-task"
        result["reason"] = "pass_audit_awaiting_gate"
        return result

    # Precedence 13 -- the ordinary loop.
    result["workflow_state"] = "WORKING"
    result["next_command"] = "execute-next-claude-task"
    result["reason"] = "ordinary_loop"
    return result


def _possible_ness_status(context, situation, diagnosis):
    """Fresh pinned Piece-3 evidence and the four-row possible-Ness table."""
    replay = situation.replay
    seq, tail = replay.tail()
    binding_scope = context.binding.package_scope_id
    default_i = {
        "interview_authenticated": False,
        "deliverable_question_count": None,
        "open_group_index": None,
        "revalidation_required": None,
        "interview_last_event_sha256": None,
    }
    i = default_i
    try:
        proposed = context.interview_projection_reader()
        if (
            isinstance(proposed, dict)
            and set(proposed) == set(default_i)
            and isinstance(proposed["interview_authenticated"], bool)
            and (
                proposed["deliverable_question_count"] is None
                or isinstance(proposed["deliverable_question_count"], int)
                and not isinstance(proposed["deliverable_question_count"], bool)
                and proposed["deliverable_question_count"] >= 0
            )
            and (
                proposed["open_group_index"] is None
                or isinstance(proposed["open_group_index"], int)
                and not isinstance(proposed["open_group_index"], bool)
                and proposed["open_group_index"] >= 0
            )
            and (
                proposed["revalidation_required"] is None
                or isinstance(proposed["revalidation_required"], bool)
            )
            and (
                proposed["interview_last_event_sha256"] is None
                or is_hex64(proposed["interview_last_event_sha256"])
            )
        ):
            i = dict(proposed)
    except Exception:  # absent/refused/locked projection is ordinary row 1
        pass

    g = None
    required_g = {
        "unlocked", "state_readable", "reasons", "requested_package_scope_id",
        "package_scope_id", "interview_events", "coverage_review_current",
    }
    try:
        proposed = context.interview_gate_reader(binding_scope)
        if (
            isinstance(proposed, dict)
            and required_g <= set(proposed)
            and isinstance(proposed["unlocked"], bool)
            and isinstance(proposed["state_readable"], bool)
            and isinstance(proposed["reasons"], list)
            and all(isinstance(reason, str) for reason in proposed["reasons"])
            and (
                proposed["requested_package_scope_id"] is None
                or isinstance(proposed["requested_package_scope_id"], str)
            )
            and (
                proposed["package_scope_id"] is None
                or isinstance(proposed["package_scope_id"], str)
            )
            and (
                proposed["interview_events"] is None
                or isinstance(proposed["interview_events"], int)
                and not isinstance(proposed["interview_events"], bool)
                and proposed["interview_events"] >= 0
            )
            and isinstance(proposed["coverage_review_current"], bool)
        ):
            g = {key: proposed[key] for key in required_g}
    except Exception:
        pass

    i_pinned = bool(
        i["interview_authenticated"]
        and i["interview_last_event_sha256"] == tail
    )
    askable = bool(
        i_pinned
        and (
            (i["deliverable_question_count"] or 0) > 0
            or i["open_group_index"] is not None
        )
    )
    projection_proved = bool(
        i_pinned
        and g is not None
        and g["state_readable"]
        and g["interview_events"] == seq
        and g["requested_package_scope_id"] == binding_scope
        and g["package_scope_id"] in (None, binding_scope)
        and not (g["unlocked"] and askable)
    )
    if not projection_proved:
        askable = False
    unlocked = bool(
        projection_proved
        and g["unlocked"]
        and g["package_scope_id"] == binding_scope
    )

    answers = [
        event
        for event in replay.scoped("answer_recorded")
        if event.get("package_scope_id") == binding_scope
        and event["event_seq"] > diagnosis["event_seq"]
    ]
    answer_unreadable = False
    for answer in answers:
        interpretation = answer.get("controller_interpretation")
        consequences = answer.get("mechanical_consequences")
        if (
            not isinstance(interpretation, dict)
            or not isinstance(interpretation.get("status"), str)
            or not isinstance(consequences, dict)
            or not isinstance(consequences.get("derived"), bool)
        ):
            answer_unreadable = True
    newest_answer = answers[-1] if answers else None
    if newest_answer is None:
        clearance = "AWAITING_ANSWER"
    elif answer_unreadable:
        clearance = "CLARIFICATION_REQUIRED"
    elif (
        newest_answer["controller_interpretation"]["status"]
        == "selected_declared_option"
        and newest_answer["mechanical_consequences"]["derived"] is True
    ):
        clearance = "ANSWER_ACCEPTED"
    else:
        clearance = "CLARIFICATION_REQUIRED"

    clarification = None
    if clearance == "CLARIFICATION_REQUIRED" and not answer_unreadable:
        interpretation = newest_answer["controller_interpretation"]
        clarification = {
            "question_id": newest_answer.get("question_id"),
            "answer_event_seq": newest_answer["event_seq"],
            "interpretation_status": interpretation["status"],
            "clarification_reason": interpretation.get("clarification_reason"),
            "candidate_option_ids": interpretation.get("candidate_option_ids"),
        }
    gate_projection = None
    if g is not None:
        gate_projection = dict(g)
        gate_projection["projection_proved"] = projection_proved
        gate_projection["gate_unlocked_for_this_package"] = unlocked
    return {
        "interview_projection": dict(i),
        "interview_gate_projection": gate_projection,
        "ness_decision_clearance": clearance,
        "ness_question_binding": {
            "diagnosis_event_seq": diagnosis["event_seq"],
            "diagnosis_result_sha256": diagnosis["diagnosis_result_sha256"],
            "review_signal": diagnosis["review_signal"],
            "plain_language_problem": diagnosis["plain_language_problem"],
            "plain_language_impact": diagnosis["plain_language_impact"],
            "candidate_path": diagnosis["candidate_path"],
            "package_scope_id": binding_scope,
        },
        "ness_answer_clarification": clarification,
        "ness_decision_cleared": False,
        "projection_proved": projection_proved,
        "askable_question_present": askable,
        "gate_unlocked_for_this_package": unlocked,
        "answer_record_unreadable": answer_unreadable,
    }


def next_candidate_path(current_path):
    """The one controlled candidate grammar: minor exactly one higher."""
    import re

    pattern = re.compile(r"^(?P<stem>.+)_v(?P<major>\d+)_(?P<minor>\d+)_CANDIDATE\.md$")
    match = pattern.match(current_path or "")
    if match is None:
        return None
    return "%s_v%s_%d_CANDIDATE.md" % (
        match.group("stem"),
        match.group("major"),
        int(match.group("minor")) + 1,
    )


def newest_unconsumed_specification(replay):
    for event in reversed(replay.scoped("correction_specification_recorded")):
        consumed = any(
            start.get("diagnosis_event_seq") == event["event_seq"]
            for start in replay.consumption_starts()
        )
        if not consumed:
            return event
    return None


def newest_unconsumed_safe_diagnosis(replay):
    for event in reversed(replay.scoped("correction_diagnosis_recorded")):
        if event.get("diagnosis_outcome") != "safe_new_mechanical_strategy":
            continue
        consumed = any(
            start.get("diagnosis_event_seq") == event["event_seq"]
            for start in replay.consumption_starts()
        )
        if not consumed:
            return event
    return None


def batch_checkpoint_required(situation):
    """Section 6 -- five completed lifetime rounds in this batch, still BLOCKED."""
    replay = situation.replay
    lifetime = replay.correction_round_lifetime()
    if lifetime == 0:
        return False
    _l, batch, round_in_batch = batch_triple(lifetime)
    if round_in_batch != constants.CORRECTION_BATCH_SIZE:
        return False
    if situation.audit is None or situation.audit.get("verdict") != "BLOCKED":
        return False
    checkpoint = replay.newest_checkpoint()
    if checkpoint is not None and checkpoint.get("correction_batch_number") == batch:
        return False
    return True


def episode_unlock_eligibility(context, situation):
    """Sections 11.2b and 11.9b -- the two automatic-eligibility booleans."""
    replay = situation.replay
    projection = situation.provider_projection()
    result = {
        "availability_probe_automatic_eligible": False,
        "episode_unlock_automatic_eligible": False,
        "c11a_self_condition_satisfied": False,
        "episode_exhaustion_person_route_reason": None,
        "closed_episode_identity": None,
        "exhaustion": None,
    }
    episode = projection["episode_identity"]
    if episode is None:
        return result
    exhaustion = replay.episode_exhaustion_event(episode)
    if exhaustion in (None, "contradiction"):
        # Look for the newest exhausted episode of this work item awaiting unlock.
        for event in replay.scoped("provider_availability_episode_exhausted_recorded"):
            if event.get("work_item_identity") != situation.work_item_id:
                continue
            if replay.accepted_episode_unlock(
                event["provider_availability_episode_identity"]
            ) is None:
                exhaustion = event
        if exhaustion in (None, "contradiction"):
            return result
    closed = exhaustion["provider_availability_episode_identity"]
    result["closed_episode_identity"] = closed
    result["exhaustion"] = exhaustion
    result["episode_exhaustion_person_route_reason"] = exhaustion.get("person_route_reason")
    if replay.accepted_episode_unlock(closed) is not None:
        return result
    if exhaustion.get("all_attempts_terminal_proved") is not True:
        return result

    record, endpoint = context.capability_record(projection["provider_kind"])
    probes_used = replay.probes_used(closed)
    probe_state = replay.availability_probe_state(closed)

    dependency_row = exhaustion.get("person_route_reason")
    is_c11 = dependency_row is None

    # Availability-probe eligibility (Section 11.2b + Section 11.7 spacing).
    if (
        is_c11
        and record is not None
        and record["availability_probe_supported"]
        and record["availability_probe_is_non_generative"]
        and record["availability_probe_result_schema_id"]
        and probes_used < constants.MAX_AVAILABILITY_PROBES_PER_CLOSED_EPISODE
        and probe_state != "probe_begun_unknown"
    ):
        result["availability_probe_automatic_eligible"] = spacing_satisfied(
            context, situation, closed, "probe"
        )

    automatic_used = replay.automatic_episode_unlocks_used(
        situation.work_item_id, projection["provider_kind"], endpoint
    )
    if automatic_used >= constants.MAX_AUTOMATIC_EPISODE_UNLOCKS_PER_WORK_ITEM:
        return result

    # The C11a self-occurrence rule (S1-S6).
    self_identity = exhaustion.get("dependency_identity")
    self_satisfied = False
    if dependency_row == "probe_capability_absent":
        baseline_digest = exhaustion.get("provider_capability_record_sha256")
        observed_digest = None if record is None else record["capability_record_sha256"]
        if (
            record is not None
            and observed_digest is not None
            and baseline_digest is not None
            and observed_digest != baseline_digest
            and record["availability_probe_supported"]
            and record["availability_probe_is_non_generative"]
            and record["availability_probe_command_identity"]
            and record["availability_probe_result_schema_id"]
            and record["capability_source"] != "none"
        ):
            self_satisfied = True
    result["c11a_self_condition_satisfied"] = self_satisfied

    outstanding = outstanding_person_conditions(
        context,
        situation,
        closed,
        exclude_self_occurrence=self_identity if self_satisfied else None,
    )
    if outstanding:
        return result
    if not spacing_satisfied(context, situation, closed, "unlock"):
        return result

    if is_c11:
        newest = replay.newest_probe_result(closed)
        if (
            newest is not None
            and newest.get("probe_outcome") == "succeeded"
            and newest.get("probe_classification_row_id") == "P1"
        ):
            result["episode_unlock_automatic_eligible"] = True
    elif self_satisfied:
        result["episode_unlock_automatic_eligible"] = True
    return result


def spacing_satisfied(context, situation, closed_episode_identity, which):
    """Section 11.7 -- delegated to the private scheduling clock, never authority."""
    scheduling = context.scheduling
    if scheduling is None:
        # Absence never shortens a wait: without the private anchor the
        # controller cannot prove the spacing elapsed and therefore refuses.
        return False
    if which == "probe":
        return scheduling.probe_spacing_satisfied(closed_episode_identity, context.now())
    return scheduling.unlock_wait_satisfied(closed_episode_identity, context.now())


# ---------------------------------------------------------------------------
# The exact supervisor-status report.
# ---------------------------------------------------------------------------
def build_supervisor_status(context, events, *, lease_state=None, lease=None,
                            journal_authentication_proved=True, source_state_current=True,
                            source_currentness=None,
                            errors=None, locked_head=None, locked_snapshot=False):
    from .feed import controller_confirmed_change_events

    situation = Situation(
        context,
        events,
        None,
        lease_state,
        lease,
        locked_head=locked_head,
        locked_snapshot=locked_snapshot,
    )
    projected = _project(context, situation)
    replay = situation.replay
    provider = projected["provider"]
    seq, tail = replay.tail()
    lifetime = replay.correction_round_lifetime()
    _l, batch, round_in_batch = batch_triple(lifetime)
    scope_key = situation.semantic_scope_key
    consumption_state, consumption_identity = consumption_reconciliation(situation)
    eligibility = episode_unlock_eligibility(context, situation)
    closed_episode = eligibility["closed_episode_identity"]

    current_dependency = replay.current_dependency() or {
        "dependency_record": None,
        "dependency_identity": None,
        "dependency_carrier_event_seq": None,
        "dependency_occurrence_ordinal": None,
    }
    if projected["workflow_state"] == "SAFETY_HOLD" and (
        projected["reason"] == "lease_ownership_unproved"
    ):
        # Row C18: derived on every read, appended never.
        record = dependency.build_record(
            "lease_ownership_unproved",
            "state_dir",
            situation.work_item_id,
            durable_record_placement="none_read_only_projection",
            plain_language_dependency=(
                "N.H could not prove who owns the supervisor lease, so it changed "
                "nothing and took nothing over."
            ),
        )
        current_dependency = {
            "dependency_record": record,
            "dependency_identity": dependency_identity_of(record),
            "dependency_carrier_event_seq": None,
            "dependency_occurrence_ordinal": None,
        }

    record = current_dependency["dependency_record"]
    series = None
    if current_dependency["dependency_identity"] is not None:
        series = retry_series_key(
            {
                "controller_executable_identity": context.controller_executable_identity,
                "package_scope_id": context.binding.package_scope_id,
                "source_binding_sha256": context.binding.source_binding_sha256,
                "candidate_path": situation.candidate.candidate_path,
                "candidate_sha256": situation.candidate.candidate_sha256,
                "candidate_bytes": situation.candidate.candidate_bytes,
                "workflow_state": projected["workflow_state"],
                "next_command": projected["next_command"],
                "work_item_identity": situation.work_item_id,
                "dependency_identity": current_dependency["dependency_identity"],
            }
        )

    state_binding = replay_mod.state_binding_digest(
        replay_mod.state_binding_projection(
            controller_executable_identity=context.controller_executable_identity,
            package_scope_id=context.binding.package_scope_id,
            source_binding_sha256=context.binding.source_binding_sha256,
            candidate_path=situation.candidate.candidate_path,
            candidate_sha256=situation.candidate.candidate_sha256,
            candidate_bytes=situation.candidate.candidate_bytes,
            workflow_state=projected["workflow_state"],
            next_command=projected["next_command"],
            work_item_identity=situation.work_item_id,
            dependency_identity=current_dependency["dependency_identity"],
            authenticated_event_seq=seq,
            authenticated_tail_sha256=tail,
        )
    )

    request_identity = provider["request_identity"]
    terminal = replay.terminal_event(request_identity) if request_identity else None
    custody = replay.custody_event(request_identity) if request_identity else None
    episode = provider["episode_identity"]
    closed_attempts = (
        replay.closed_attempt_count(situation.work_item_id, provider["provider_kind"], episode)
        if episode
        else 0
    )

    trigger = situation.trigger
    trigger_identity = None if trigger is None else trigger["diagnosis_trigger_identity"]

    report = {
        "command": "supervisor-status",
        "ok": True,
        "supervisor_capability_version": constants.SUPERVISOR_PROTOCOL_VERSION,
        "workflow_state": projected["workflow_state"],
        "package_key": context.binding.package_key,
        "package_scope_id": context.binding.package_scope_id,
        "package_id": context.binding.package_id,
        "bundle_placement": constants.BUNDLE_PLACEMENT,
        "controlled_component_id": constants.CONTROLLED_COMPONENT_ID,
        "register_id": constants.REGISTER_ID,
        "branch": context.binding.branch,
        "head_sha": context.binding.head_sha,
        "controller_executable_identity": context.controller_executable_identity,
        "source_binding_sha256": context.binding.source_binding_sha256,
        "settled_decision_binding_sha256": context.binding.settled_decision_binding_sha256,
        "candidate_path": situation.candidate.candidate_path,
        "candidate_sha256": situation.candidate.candidate_sha256,
        "candidate_bytes": situation.candidate.candidate_bytes,
        "correction_batch_size": constants.CORRECTION_BATCH_SIZE,
        "correction_batch_number": batch,
        "correction_rounds_started_this_batch": replay.correction_rounds_started_this_batch(),
        "correction_rounds_completed_this_batch": (
            replay.correction_rounds_completed_this_batch()
        ),
        "correction_rounds_lifetime_before": lifetime,
        "correction_rounds_lifetime_after": lifetime,
        "correction_round_lifetime": lifetime,
        "correction_round_in_batch": round_in_batch,
        "audit_identity": situation.audit_identity,
        "checkpoint_identity": (
            None
            if replay.newest_checkpoint() is None
            else replay.newest_checkpoint()["checkpoint_identity"]
        ),
        "diagnosis_identity": (
            None
            if not replay.scoped("correction_diagnosis_recorded")
            else replay.scoped("correction_diagnosis_recorded")[-1]["diagnosis_trigger_identity"]
        ),
        "next_command": projected["next_command"],
        "ness_decision_required": projected["workflow_state"] == "NEEDS_NESS_DECISION",
        "interview_projection": projected["interview_projection"],
        "interview_gate_projection": projected["interview_gate_projection"],
        "ness_decision_clearance": projected["ness_decision_clearance"],
        "ness_question_binding": projected["ness_question_binding"],
        "ness_answer_clarification": projected["ness_answer_clarification"],
        "ness_decision_cleared": projected["ness_decision_cleared"],
        "user_action_required": projected["workflow_state"] == "NEEDS_USER_ACTION",
        # Section 10.2 -- ONE derivation, unchanged.  The new terminal state is
        # not READY_FOR_ACCEPTANCE, so this is false automatically after a
        # proved acceptance; no second source of truth is added for it.
        "acceptance_required": projected["workflow_state"] == "READY_FOR_ACCEPTANCE",
        "acceptance_truth": acceptance_truth(situation),
        "acceptance_disposition": (
            constants.ACCEPTANCE_DISPOSITION
            if projected["workflow_state"] == constants.ACCEPTED_FOR_DESIGN_ONLY
            else None
        ),
        "ness_acceptance_identity": (
            (replay.current_ness_acceptance() or {}).get("ness_acceptance_identity")
            if isinstance(replay.current_ness_acceptance(), dict)
            else None
        ),
        # Stated rather than implied: a reader that did not hold the exclusive
        # lock may never say the word "accepted", and this says which kind of
        # reader produced this report.
        "acceptance_locked_projection": bool(situation.locked_snapshot),
        "journal_authentication_proved": bool(journal_authentication_proved),
        "authenticated_state_current": not situation.contradictions,
        "source_state_current": bool(source_state_current),
        # section 8.8 section 13.2 -- the section 8.3 projection, reported BESIDE the
        # verdict and never instead of it.  SBC-STATUS-NO-DEMOTION: a false
        # verdict changes no workflow_state, no acceptance_truth, no
        # acceptance_disposition, no ness_acceptance_identity, no
        # package_scope_id and no candidate field (R-SB18).
        "source_currentness": source_currentness,
        "controller_confirmed_change_events": controller_confirmed_change_events(
            context, events
        ),
        "run_lease": {
            "lease_state": lease_state or "ABSENT_PROVED",
            "live_proved": lease_state == "LIVE_PROVED",
            "run_id": None if lease is None else lease.get("run_id"),
            "expires_at": None if lease is None else lease.get("expires_at_epoch"),
        },
        "authenticated_event_seq": seq,
        "authenticated_tail_sha256": tail,
        "standing_chain_sha256": engine._standing(events),
        "work_item_identity": situation.work_item_id,
        "work_item_kind": situation.work_item_obj["work_item_kind"],
        "retry_series_key": series,
        "state_binding_sha256": state_binding,
        "provider_kind": provider["provider_kind"],
        "provider_phase": provider["phase"],
        "provider_request_identity": request_identity,
        "provider_availability_episode_identity": episode,
        "provider_availability_episode_generation": provider["episode_generation"],
        "provider_attempts_closed_this_episode": closed_attempts,
        "provider_attempts_remaining_this_episode": max(
            0, constants.MAX_PROVIDER_ATTEMPTS_PER_WORK_ITEM_EPISODE - closed_attempts
        ),
        "provider_dispatch_serial_next": provider["serial_next"],
        "provider_reconciliation": _provider_reconciliation(replay, request_identity),
        "provider_result_custody": _provider_result_custody(replay, request_identity),
        "result_custody_identity": (
            None if custody is None else custody["result_custody_identity"]
        ),
        "provider_error_signal_token": (
            None if terminal is None else terminal.get("provider_error_signal_token")
        ),
        "provider_error_classification_row_id": (
            None if terminal is None else terminal.get("provider_error_classification_row_id")
        ),
        "open_provider_request_count": len(situation.open_requests),
        "open_result_custody_count": len(situation.pending_custody),
        "consumption_reconciliation": consumption_state,
        "open_consumption_identity": (
            None if situation.open_consumption is None
            else situation.open_consumption["consumption_identity"]
        ),
        "dependency_record": record,
        "dependency_identity": current_dependency["dependency_identity"],
        "dependency_identity_binding": (
            None if record is None else record["dependency_identity_binding"]
        ),
        "dependency_carrier_event_seq": current_dependency["dependency_carrier_event_seq"],
        "dependency_occurrence_ordinal": current_dependency["dependency_occurrence_ordinal"],
        "dependency_durable_record_placement": (
            None if record is None else record["durable_record_placement"]
        ),
        "semantic_scope_key": scope_key,
        "semantic_unlock_generation": situation.semantic_unlock_generation,
        "semantic_scope_exhausted": replay.semantic_scope_exhausted(scope_key),
        "semantic_scope_exhaustion_event_seq": (
            replay.semantic_scope_exhaustion_event_seq(scope_key)
        ),
        "semantic_scope_unlock_available": semantic_scope_unlock_available(
            context, events, situation
        ),
        "exhausted_novelty_key_count": len(replay.exhausted_novelty_keys(scope_key)),
        "no_progress_rounds_in_scope": replay.no_progress_rounds_in_scope(scope_key),
        "no_progress_rounds_remaining_in_scope": max(
            0,
            constants.MAX_NO_PROGRESS_ROUNDS_PER_SEMANTIC_SCOPE
            - replay.no_progress_rounds_in_scope(scope_key),
        ),
        "diagnosis_trigger_identity": trigger_identity,
        "diagnosis_trigger_attempt_ordinal": (
            0 if trigger_identity is None
            else replay.trigger_diagnosis_attempt_ordinal(trigger_identity)
        ),
        "diagnosis_trigger_state": replay.diagnosis_trigger_state(trigger_identity, scope_key),
        "design_audit_result_usability": _audit_usability(context, situation, replay),
        "output_retries_used": (
            replay.output_retries_used(
                situation.work_item_id, provider["provider_kind"], episode
            )
            if episode
            else 0
        ),
        "output_retries_remaining": (
            replay.output_retries_remaining(
                situation.work_item_id, provider["provider_kind"], episode
            )
            if episode
            else constants.MAX_PROVIDER_OUTPUT_RETRIES_PER_EPISODE
        ),
        "availability_probe_state": replay.availability_probe_state(closed_episode),
        "availability_probe_identity": (
            None
            if closed_episode is None or replay.newest_probe_result(closed_episode) is None
            else replay.newest_probe_result(closed_episode)["availability_probe_identity"]
        ),
        "availability_probes_used_this_closed_episode": (
            0 if closed_episode is None else replay.probes_used(closed_episode)
        ),
        "availability_probes_remaining_this_closed_episode": (
            constants.MAX_AVAILABILITY_PROBES_PER_CLOSED_EPISODE
            if closed_episode is None
            else max(
                0,
                constants.MAX_AVAILABILITY_PROBES_PER_CLOSED_EPISODE
                - replay.probes_used(closed_episode),
            )
        ),
        "availability_probe_automatic_eligible": eligibility[
            "availability_probe_automatic_eligible"
        ],
        "episode_unlock_automatic_eligible": eligibility["episode_unlock_automatic_eligible"],
        "c11a_self_condition_satisfied": eligibility["c11a_self_condition_satisfied"],
        "episode_exhaustion_person_route_reason": eligibility[
            "episode_exhaustion_person_route_reason"
        ],
        "automatic_episode_unlocks_used": (
            replay.automatic_episode_unlocks_used(
                situation.work_item_id,
                provider["provider_kind"],
                provider["provider_endpoint_identity"],
            )
            if provider["provider_endpoint_identity"]
            else 0
        ),
        "automatic_episode_unlocks_remaining": 0,
        "piece3_provider_authorization": replay.piece3_provider_authorization(),
        "errors": list(errors or []),
    }
    report["automatic_episode_unlocks_remaining"] = max(
        0,
        constants.MAX_AUTOMATIC_EPISODE_UNLOCKS_PER_WORK_ITEM
        - report["automatic_episode_unlocks_used"],
    )
    missing = sorted(set(SUPERVISOR_STATUS_KEYS) - set(report))
    extra = sorted(set(report) - set(SUPERVISOR_STATUS_KEYS))
    if missing or extra:
        raise AssertionError(
            "supervisor-status must return exactly its declared key set "
            "(missing %s, extra %s)" % (missing, extra)
        )
    return report


def dependency_identity_of(record):
    from .identity import dependency_identity as _derive

    return _derive(record)


def _provider_reconciliation(replay, request_identity):
    if request_identity is None:
        return "not_required"
    events = replay.reconciliation_events(request_identity)
    if not events:
        return "not_required"
    outcomes = {event["reconciliation_outcome"] for event in events}
    if len(outcomes) > 1:
        return events[-1]["reconciliation_outcome"]
    return events[-1]["reconciliation_outcome"]


def _provider_result_custody(replay, request_identity):
    if request_identity is None:
        return "not_required"
    custodies = replay.custody_events(request_identity)
    terminal = replay.terminal_event(request_identity)
    if len(custodies) > 1:
        return "contradiction"
    if terminal is not None and terminal["terminal_kind"] == "result_oversize_uncustodied":
        if custodies:
            return "contradiction"
        return "oversize_not_custodied"
    if not custodies:
        return "absent"
    return "custodied_valid" if custodies[0]["result_schema_valid"] else "custodied_invalid"


def _audit_usability(context, situation, replay):
    for custody in reversed(replay.scoped("provider_result_custody_recorded")):
        if custody.get("work_item_kind") == "design_audit":
            return replay.design_audit_result_usability(
                custody["provider_request_identity"]
            )
    return "none"

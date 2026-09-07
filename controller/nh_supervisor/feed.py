#!/usr/bin/env python3
"""Section 2 and Section 12 -- the controller-confirmed live-change feed.

Only three authenticated sources can create a feed item, and each item carries
the exact authenticated controller event sequence and digest it was derived
from.  Model prose and the operational journal cannot create an item, and no
event type added by any version of this specification may create one.
"""

from __future__ import annotations

from . import constants, schema
from . import replay as replay_mod

FEED_KINDS = constants.FEED_ITEM_KINDS


def _technical(event, extra=None):
    technical = {
        "controller_event_seq": event["event_seq"],
        "controller_event_sha256": event["event_sha256"],
        "candidate_path": event.get("candidate_path"),
        "candidate_sha256": event.get("candidate_sha256"),
    }
    if extra:
        technical.update(extra)
    return technical


def _item(event, kind, title, what, why, status, technical):
    return {
        "controller_authenticated": True,
        "recorded_at": None,
        "id": "%s:%d" % (kind, event["event_seq"]),
        "kind": kind,
        "title": title,
        "what": what,
        "why": why,
        "status": status,
        "technical": technical,
    }


def controller_confirmed_change_events(context, events):
    """Re-derived from authenticated events on every call, in sequence order."""
    replay = replay_mod.Replay(events, context.binding.package_scope_id)
    feed = []

    # Section 7.2 / 7.3 -- the acceptance explanation SHARES this carrier type
    # at a new body version, and shares nothing else.  The per-candidate index
    # below means the CORRECTION-stage record: the one that explains one change
    # from one parent to one child.  An acceptance-stage record explains the
    # whole candidate for an acceptance offer, is bound to an audit and a PASS,
    # and carries no parent-change claim at all.
    #
    # Indexing by candidate_sha256 alone would let a later acceptance-stage
    # record for the SAME candidate silently overwrite the correction-stage one
    # and become the source of a "candidate_changed" card.  That is exactly the
    # substitution Section 7.3 forbids, so the two are separated MECHANICALLY,
    # by the required discriminator and by nothing else -- never by ordering,
    # never by field resemblance, never by which arrived last.
    explanations = {}
    for event in replay.scoped("mechanical_change_explanation_recorded"):
        if event.get("explanation_stage") in replay_mod.ACCEPTANCE_EXPLANATION_STAGES:
            continue
        explanations[event.get("candidate_sha256")] = event

    for event in replay.scoped():
        kind = event.get("type")

        if kind == "mechanical_audit_recorded" and event.get("verdict") == "BLOCKED":
            findings = event.get("findings") or []
            problem = None
            impact = None
            for finding in findings:
                if finding.get("blocking"):
                    problem = event.get("plain_language_problem")
                    impact = event.get("plain_language_impact")
                    break
            feed.append(
                _item(
                    event,
                    "problem_found",
                    "An independent check found something that must be corrected",
                    problem
                    or (
                        "A fresh independent review of the exact candidate reported "
                        "at least one blocking finding."
                    ),
                    impact
                    or (
                        "N.H will not treat this candidate as finished while a "
                        "blocking finding stands."
                    ),
                    "Blocking findings recorded; a mechanical correction is next",
                    _technical(
                        event,
                        {
                            "audit_identity": event.get("audit_identity"),
                            "mechanical_blocker_refs": event.get("mechanical_blocker_refs"),
                        },
                    ),
                )
            )

        elif kind == "candidate_custody_recorded":
            explanation = explanations.get(event.get("candidate_sha256"))
            if explanation is not None and explanation.get("meaning_or_policy_changed") is not None:
                what = explanation.get("plain_language_change") or (
                    constants.FALLBACK_CHANGE_CARD["what"]
                )
                why = explanation.get("plain_language_real_use_effect") or (
                    constants.FALLBACK_CHANGE_CARD["why"]
                )
                title = "Claude made a correction candidate intended to address the findings"
                technical = _technical(
                    event,
                    {
                        "parent_candidate_path": explanation.get("parent_candidate_path"),
                        "parent_candidate_sha256": explanation.get("parent_candidate_sha256"),
                        "diff_sha256": explanation.get("diff_sha256"),
                        "changed_sections": explanation.get("changed_sections"),
                        "correction_round_lifetime": event.get("correction_round_lifetime"),
                        "correction_batch_number": event.get("correction_batch_number"),
                        "correction_round_in_batch": event.get("correction_round_in_batch"),
                        "meaning_or_policy_changed": explanation.get(
                            "meaning_or_policy_changed"
                        ),
                    },
                )
                status = "Waiting for or reporting the independent audit result"
            else:
                # The fixed controller-owned fallback card of Section 12.
                title = constants.FALLBACK_CHANGE_CARD["title"]
                what = constants.FALLBACK_CHANGE_CARD["what"]
                why = constants.FALLBACK_CHANGE_CARD["why"]
                status = constants.FALLBACK_CHANGE_CARD["status"]
                technical = _technical(
                    event,
                    {
                        "parent_candidate_path": event.get("parent_candidate_path"),
                        "parent_candidate_sha256": event.get("parent_candidate_sha256"),
                        "parent_candidate_bytes": event.get("parent_candidate_bytes"),
                        "correction_round_lifetime": event.get("correction_round_lifetime"),
                        "correction_batch_number": event.get("correction_batch_number"),
                        "correction_round_in_batch": event.get("correction_round_in_batch"),
                        "diff_sha256": None,
                        "changed_sections": None,
                    },
                )
            feed.append(
                _item(event, "candidate_changed", title, what, why, status, technical)
            )

        elif kind == "mechanical_pass_recorded":
            audit = None
            for candidate in replay.scoped("mechanical_audit_recorded"):
                if candidate.get("audit_identity") == event.get("audit_identity"):
                    audit = candidate
            if audit is None or audit.get("verdict") != "PASS":
                continue
            feed.append(
                _item(
                    event,
                    "audit_passed",
                    "Codex confirmed the exact candidate passes",
                    "A fresh independent review of this exact candidate returned PASS.",
                    "The package is ready for Ness to consider acceptance. Nothing has "
                    "been accepted, adopted, installed, or integrated.",
                    "Ready for Ness acceptance -- acceptance itself has not happened",
                    _technical(
                        event,
                        {
                            "pass_identity": event.get("pass_identity"),
                            "audit_identity": event.get("audit_identity"),
                            "terminal_chain_sha256": event.get("terminal_chain_sha256"),
                        },
                    ),
                )
            )

    for item in feed:
        assert set(item) == set(constants.FEED_ITEM_KEYS)
        assert item["kind"] in FEED_KINDS
    return feed


def feed_item_forbidden_event_types():
    """Every supervisor event type that may never create a feed card."""
    return sorted(schema.NON_FEED_SUPERVISOR_EVENT_TYPES)

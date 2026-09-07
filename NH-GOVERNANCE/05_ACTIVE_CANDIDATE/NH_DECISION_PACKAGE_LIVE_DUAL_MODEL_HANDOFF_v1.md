# N.H DECISION PACKAGE — LIVE DUAL-MODEL HANDOFF
**Filename:** `NH_DECISION_PACKAGE_LIVE_DUAL_MODEL_HANDOFF_v1.md`  
**Status:** Ness-approved standalone concept decision; not yet integrated into Master V10 or the current Design and Wiring Map  
**Date:** 2026-07-01  
**Authority owner:** Ness  

## Authority order
1. `NH_MASTER-20_CORRECTED_v10.md`
2. `NH_DECISION_DEFAULTS-S19_v2_2.md`
3. current `cursorrules`
4. `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`

This package records a newly approved concept decision. It does not overwrite, silently patch, or supersede any authoritative file. Any later integration must create a new versioned candidate and requires separate review and adoption by Ness.

---

## 1. Ness-approved concept

N.H may use two local language models during live conversation, with different responsibilities:

### A. Heavy model — deep analyst
The heavier model performs the deeper work:
- interprets meaning and context;
- considers relevant N.H memory and retrieved evidence;
- separates known information from uncertainty;
- identifies what must not be invented;
- determines the intended substance and direction of the eventual answer;
- may work asynchronously in the background while conversation continues.

The heavy model is not itself N.H, is not authoritative over Ness, and does not replace N.H's rules, memory, provenance, relevance, privacy, or truth controls.

### B. Light model — live messenger, translator, and conversational carrier
The lighter model remains the single visible live speaker. It may:
- acknowledge Ness warmly;
- preserve conversational continuity;
- translate structured heavy-model analysis into natural language;
- ask bounded clarification questions;
- gather additional relevant information while the heavy model is still working;
- deliver the heavy model's completed result without changing its meaning.

The light model is not an equal policy-maker or independent deep-decider. It must not invent the final deep conclusion while the heavy model is still working.

### C. N.H — authority over both
N.H's governing rules, memory, provenance, relevance controls, privacy boundaries, and uncertainty rules remain above both models.

The heavy model may propose analysis.  
The light model may express and carry the conversation.  
Neither model may silently turn interpretation into fact or override Ness.

---

## 2. Core live-conversation behavior

A realistic live sequence may work as follows:

1. Ness speaks.
2. N.H opens one identified live operation.
3. Relevant context and authorized memory are retrieved.
4. The heavy model begins deeper analysis in the background.
5. While that work is pending, the light model may:
   - acknowledge what Ness said;
   - reflect only what is already clear;
   - ask a bounded clarification;
   - collect additional information;
   - state that deeper analysis is still in progress.
6. New relevant information from Ness is attached to the same live operation.
7. N.H decides mechanically whether the heavy analysis can continue, must be supplemented, or must be cancelled and restarted.
8. The heavy model returns a structured analysis brief.
9. N.H validates that brief against governing rules.
10. The light model translates the validated brief into one natural answer.
11. N.H validates that the light model did not add, omit, distort, or overstate the brief.
12. Only the validated final answer is surfaced as N.H's reply.

---

## 3. Meaning-preservation rule

The light model may change wording, warmth, sentence structure, language, and presentation only.

It must not:
- change the heavy model's conclusion;
- remove uncertainty or caveats;
- add unsupported facts;
- invent advice;
- turn a proposal into a decision;
- turn model confidence into authority;
- conceal disagreement or unresolved uncertainty;
- surface stale analysis after the conversation has moved on.

If the light model changes the meaning, N.H must reject the draft, retry safely, or use a deterministic fallback.

---

## 4. Warm continuation while the heavy model works

The light model may keep the interaction alive, but only inside a bounded live-conversation role.

Allowed examples:
- “I understand the question.”
- “Is the main issue X or Y?”
- “When did that begin?”
- “I’m still working through the deeper answer.”
- “That new detail changes what needs to be considered.”

Not allowed:
- pretending the heavy analysis is already complete;
- giving the final deep conclusion independently;
- inventing an explanation to fill silence;
- contradicting a pending or completed validated brief;
- speaking as a separate personality.

To Ness, the system must remain one continuous N.H, not two characters taking turns.

---

## 5. Relationship to the existing Master direction

This decision preserves the existing settled direction that:
- the model is a borrowed, frozen, replaceable mouth;
- what makes N.H itself lives outside model weights;
- growth lands in memory, not in the mouth;
- retrieval and governing evidence come before wording;
- model output is never automatically authoritative;
- the final Interactive Translator model remains undecided until tested and deliberately adopted by Ness.

This decision extends the live model architecture by separating:
- deeper analysis;
- live conversational carrying and translation;
- N.H's governing validation.

It does not authorize training a model, merging N.H's identity into model weights, or allowing the nightly research model to control live conversation without the same gates.

---

## 6. Mechanical work still required

This concept does not itself settle or implement the following mechanics:

- operation identity for each live turn and background analysis;
- cancellation and restart rules when new information arrives;
- stale-result rejection;
- ordering across overlapping topics and branches;
- duplicate prevention;
- transaction boundaries;
- timeout and retry rules;
- crash recovery and partial-completion recovery;
- heavy-model unavailable fallback;
- light-model distortion detection;
- structured brief schema;
- validation and logging schemas;
- privacy and relevance input boundaries for each model;
- latency budgets and escalation thresholds;
- when the heavy model runs every turn versus only selected turns;
- resource scheduling, model loading, unloading, and GPU/RAM coexistence;
- exact model candidates;
- benchmark and acceptance criteria;
- component-specific §0B logging;
- B-INT and B-CYCLE wiring.

These are mechanical architecture tasks or later genuine policy questions and must remain open until handled in dependency order.

---

## 7. Hardware and model-choice effect

This architecture may reduce the need for one model to be simultaneously:
- very fast;
- deeply capable;
- highly obedient;
- natural in live speech;
- multilingual;
- small enough to remain constantly loaded.

A heavier model may be selected for depth, even when slower.  
A lighter model may be selected for speed, warmth, translation, and strict bounded obedience.

This does not prove that a hardware upgrade is unnecessary. It changes what must be benchmarked before spending money:
- quality gain from the heavy model;
- live usability of the light model;
- handoff reliability;
- total latency;
- memory and GPU behavior;
- whether the heavy model needs to run every turn.

---

## 8. Adoption and implementation boundary

This standalone package records Ness's approved concept.

It does **not**:
- modify Master V10;
- modify the current Design and Wiring Map;
- adopt any specific heavy or light model;
- authorize coding;
- authorize production stores;
- authorize runtime integration;
- close dependent policy or mechanical questions.

Later consolidation must create a new versioned candidate, preserve this package, and undergo independent audit before Ness may adopt it.

---

## 9. Compact locked statement

> N.H may use a heavy local model as a background deep analyst and a lighter local model as the single visible live messenger, translator, and warm conversational carrier. While the heavy model works, the light model may acknowledge, clarify, and gather relevant information, but it may not invent the final deep answer. N.H's governing rules, memory, provenance, privacy, relevance, and uncertainty controls remain authoritative over both. The heavy model determines proposed substance; the light model expresses validated substance; N.H validates the handoff and rejects distortion, stale output, duplication, or unsupported invention.

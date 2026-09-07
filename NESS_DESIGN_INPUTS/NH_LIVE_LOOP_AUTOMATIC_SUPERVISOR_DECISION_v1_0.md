# N.H — Automatic Live-Loop Supervisor Decision

**Filename:** `NH_LIVE_LOOP_AUTOMATIC_SUPERVISOR_DECISION_v1_0.md`  
**Date:** 2026-08-17  
**Status:** NESS DESIGN DECISION AND DISPOSABLE-CANDIDATE BUILD AUTHORIZATION  
**Scope:** the local N.H Claude/Codex design loop and its local browser interface  
**Not authorized by this record:** installation into the active controller; Git writes; production N.H implementation; acceptance, adoption, package completion, Master/Map integration, deployment, or push

---

# 1. Why this decision exists

The installed controller currently treats five automatic correction rounds as a
lifetime limit for one candidate chain. That rule was deliberate and was
preserved by earlier controller work. It is not a defect relative to the earlier
decision.

Ness now chooses a different user-facing outcome:

> Mechanical work remains owned by the automatic Claude/Codex loop until the
> package reaches a proved PASS or a real external, authority, safety, or Ness
> dependency makes further safe progress impossible. Reaching one bounded
> correction-batch limit must not mean that the package is abandoned.

This is a deliberate change to the desired controller behaviour. It does not
retroactively make the earlier five-round implementation incorrect.

---

# 2. The plain-language rule

From Ness's point of view, the loop should behave like this:

1. If a genuine N.H meaning or policy choice is open, show it to Ness in the
   browser in everyday language.
2. After Ness answers, continue automatically.
3. Codex audits the actual current candidate.
4. If the problem is mechanical, the reasoning role prepares the bounded
   correction and Claude applies it in a disposable workspace.
5. Codex independently audits the resulting candidate.
6. Keep correcting, diagnosing, recovering, and resuming without asking Ness to
   solve engineering.
7. Return to Ness only for:
   - a genuine N.H meaning, policy, permission, privacy, priority, or authority
     choice;
   - a technical action only Ness can perform, such as restoring an unavailable
     account or supplying an externally controlled dependency; or
   - explicit acceptance of a candidate that has completed every required audit.

The loop must never claim that an unresolved package passed merely because it
ran for a long time or used many attempts.

---

# 3. Bounded continuation, not one infinite command

"Keep working until fixed" does **not** authorize an uncontrolled, unbounded
provider invocation or a hot retry loop.

The automatic workflow is persistent, but every individual action remains
bounded:

- one candidate receives one fresh independent audit;
- one correction specification is prepared for one proved blocker set;
- Claude receives one bounded correction application at a time;
- every new candidate is separately verified and audited;
- provider calls retain explicit timeouts;
- every real candidate remains versioned and earlier candidates remain
  byte-preserved;
- crash-safe custody, duplicate prevention, source-state fencing, and
  fail-closed behaviour remain mandatory;
- a user or operator can stop the local supervisor without manufacturing a
  workflow result.

The existing five-round quantity becomes a **correction batch size and diagnosis
checkpoint**, not a lifetime permission boundary and not a package-abandonment
condition.

After a correction batch is exhausted while mechanical blockers remain, the
workflow must:

1. durably checkpoint the candidate chain and controller-confirmed findings;
2. enter a fresh independent diagnosis stage;
3. determine whether the surviving blocker represents real progress, repeated
   no-progress, a faulty correction approach, a missing dependency, a genuine
   Ness choice, or an authority/safety conflict;
4. begin another bounded correction batch automatically only when the diagnosis
   proves a new safe mechanical route;
5. never obtain another batch by silently resetting, erasing, or lying about the
   lifetime history.

The durable record must retain both the per-batch count and the cumulative
lifetime count.

---

# 4. Controller-owned workflow states

The local supervisor must expose these truthful states:

## `WORKING`

Proved mechanical work is available. Continue automatically.

## `DIAGNOSING`

A bounded correction batch ended, the same blocker may be surviving, or the
latest attempt made no proved progress. A fresh independent reasoning pass must
identify a materially different safe route before another correction batch may
begin.

## `WAITING_RECOVERING`

A temporary technical dependency is unavailable or an interrupted operation is
being recovered. Preserve state, use bounded backoff, re-prove the source state,
and resume automatically when safe.

## `NEEDS_NESS_DECISION`

The proved unresolved point genuinely changes what N.H means, does, permits,
protects, prioritizes, or treats as authority. This is the ordinary state that
asks Ness a question.

It must use the existing authenticated Piece-3 question-validation and interview
path. No second Ness-question system is authorized.

## `NEEDS_USER_ACTION`

No N.H policy answer is needed, but an external action that the models and local
controller cannot perform is required. The browser must explain the action in
ordinary language and must not disguise it as a design question.

## `SAFETY_HOLD`

Continuing would require weakening or bypassing authority, privacy, provenance,
custody, source fencing, version preservation, or another settled protection.
The loop remains fail-closed. It may route a genuine authority choice to the
existing Ness interview, but it must not mechanically choose to weaken the
protection.

## `READY_FOR_ACCEPTANCE`

The exact current candidate has the required proved final PASS and all required
post-audit source/custody checks remain current. The browser presents the
candidate to Ness for explicit acceptance.

This state does not itself accept, adopt, close, integrate, implement, commit, or
push anything.

## `ACCEPTED_FOR_DESIGN_ONLY`

This state may exist only after Ness explicitly performs the separately
authorized acceptance action. Its exact recording and downstream effect require
a separate accepted acceptance-record design. Until that design exists, the UI
may show `READY_FOR_ACCEPTANCE` but must not manufacture or persist acceptance.

---

# 5. What happens when a blocker cannot currently be resolved

The loop must classify the reason truthfully:

- **temporary provider/tool failure:** wait with bounded backoff, then retry and
  resume from the durable checkpoint;
- **crash or interrupted local operation:** use lookup-first recovery and
  duplicate prevention before doing more work;
- **mechanical approach made no progress:** enter `DIAGNOSING`; do not repeat the
  same correction blindly;
- **missing evidence or external dependency:** recover it automatically where
  authorized; otherwise use `WAITING_RECOVERING` or `NEEDS_USER_ACTION` and name
  exactly what would unlock progress;
- **genuine Ness decision:** route through the existing validation/interview
  path and use `NEEDS_NESS_DECISION`;
- **authority or safety conflict:** use `SAFETY_HOLD`; never weaken the rule to
  obtain a PASS;
- **no currently safe repair exists:** preserve the package as unfinished,
  preserve the proved reason, and re-evaluate only after a relevant source,
  capability, dependency, or Ness decision changes. Do not ask Ness how to code
  it, and do not call it complete.

No finite system can guarantee that every logically possible blocker is
solvable. The required guarantee is instead that an unresolved mechanical
package remains honestly owned and visibly unfinished, rather than being
abandoned, disguised as a Ness engineering question, or falsely reported as a
success.

---

# 6. Browser behaviour

The browser is the normal user surface. Ness should not have to supervise a
terminal.

The primary tabs are:

1. **Your decisions**
2. **What's changing**
3. **Current status**
4. **Technical details**

The persistent package context must show:

- the plain-language N.H capability;
- the technical package;
- the framework/addition position where proved by source;
- bundle placement where settled, or "not decided" where it is genuinely open;
- the current workflow state;
- why Ness is or is not needed.

The browser automatically refreshes while the local supervisor is active. It
interrupts Ness prominently only for `NEEDS_NESS_DECISION`,
`NEEDS_USER_ACTION`, or `READY_FOR_ACCEPTANCE`.

---

# 7. Trustworthy plain-language change feed

The **What's changing** feed must be derived from controller-confirmed facts,
not from Claude asserting that its own work succeeded.

Every correction entry answers:

1. **What was wrong?** — a plain-language translation of the validated Codex
   finding;
2. **Why does it matter?** — the real-use consequence grounded in that finding;
3. **What changed?** — a plain-language translation of the verified difference
   between the exact parent and promoted candidate, tied to the correction
   specification and finding identities;
4. **What happened afterward?** — still being checked, Codex found another
   problem, or the exact candidate reached a validated PASS.

Before the fresh audit, the UI says that Claude **made a correction intended to
fix** the problem. Only a later validated audit may say that Codex confirmed the
candidate passes.

Every item provides expandable technical evidence, including as applicable:

- parent and candidate paths, hashes, and byte lengths;
- correction batch and lifetime round numbers;
- controller-derived finding identities;
- exact candidate/source evidence;
- correction-specification entries;
- changed sections and raw diff;
- audit verdict and stop reason;
- custody and source-state proof.

Plain-language explanations are explanatory projections, not new authority.
They must identify the exact controller event and candidate identity from which
they were produced. If a safe explanation cannot be produced, the UI displays
the verified technical fact and says that a plain explanation is not currently
available; it must not invent one.

A summary may say that nothing changed N.H meaning or policy only when an
independent check explicitly proved that fact for the actual promoted change.

---

# 8. Durable supervision and resume

The supervisor must:

- hold at most one active workflow lease for a package;
- preserve a hash-chained append-only operational event history;
- bind every event to the controller version, source identity, package scope,
  candidate identity, and relevant controller report digest;
- recover after UI, supervisor, terminal, or machine restart without duplicating
  a model call or candidate promotion;
- distinguish `running`, `completed`, `waiting`, `needs Ness`, and `unknown after
  interruption` rather than guessing;
- use bounded retry/backoff with no hot loop;
- stop safely when the real source state changes and re-run the required source
  and interview proofs before continuing;
- never use its own journal as a replacement for the authenticated interview
  journal or candidate-custody records;
- never perform Git writes or push;
- never accept, adopt, integrate, or implement a design automatically.

---

# 9. Authorization boundary for the present work

This decision authorizes the present development task to:

- create a versioned controller/supervisor candidate;
- extend the local browser UI;
- create tests, fixtures, and reports;
- create and modify files inside a newly created disposable rehearsal shadow;
- exercise Git writes only inside that disposable shadow where a faithful
  rehearsal requires them;
- invoke model providers only in an explicitly identified rehearsal after the
  non-provider tests and safety fences pass.

This decision does **not** authorize:

- replacing the active `controller/nh_loop.py`;
- changing `NH-GOVERNANCE` authority or candidate files during development;
- rewriting the existing interview journal;
- installing the candidate merely because local tests pass;
- changing privacy, authority, provenance, custody, source-fencing, candidate
  preservation, question validation, or acceptance boundaries;
- Git add, commit, push, merge, reset, checkout, clean, rebase, fetch, or remote
  changes in the real controller or governance repositories;
- production implementation or deployment.

Installation requires a separate review of the actual candidate, a complete
disposable-shadow rehearsal, before/after proof that protected real paths did
not change, and Ness's explicit installation approval.

---

# 10. Acceptance tests for the candidate behaviour

Before installation is considered, the disposable rehearsal must prove at
least:

1. zero genuine questions proceeds automatically into mechanical work;
2. a genuine validated question enters `NEEDS_NESS_DECISION` and no mechanical
   work continues until the answer is preserved and revalidated;
3. ordinary mechanical BLOCKED findings produce correction and fresh audit;
4. the fifth unsuccessful correction enters `DIAGNOSING`, not package
   abandonment;
5. diagnosis can authorize a materially new bounded batch without erasing or
   resetting cumulative history;
6. repeated no-progress does not hot-loop;
7. a temporary provider failure enters `WAITING_RECOVERING`, backs off, and
   resumes without duplicate work;
8. an externally recoverable dependency enters `NEEDS_USER_ACTION` with no fake
   Ness policy question;
9. an authority/safety conflict enters `SAFETY_HOLD` and remains fail-closed;
10. the live feed is bound to validated findings, verified candidate changes,
    audit results, and custody identities;
11. a final validated PASS transitions automatically to
    `READY_FOR_ACCEPTANCE`;
12. no acceptance occurs without Ness;
13. restart recovery preserves the exact workflow state and does not repeat an
    already completed provider call or candidate promotion;
14. the real controller, governance repository, and interview state remain
    unchanged throughout the rehearsal.

---

# 11. Final rule

> Ness decides what N.H should mean. The local automatic supervisor owns the
> mechanical work across bounded, recoverable correction and diagnosis batches.
> It keeps the package visibly alive until PASS or a proved dependency prevents
> safe progress. It interrupts Ness only for a genuine N.H decision, an external
> action only Ness can perform, or explicit acceptance of a fully audited
> candidate. It never obtains progress by weakening N.H's protections or
> pretending that unfinished work succeeded.

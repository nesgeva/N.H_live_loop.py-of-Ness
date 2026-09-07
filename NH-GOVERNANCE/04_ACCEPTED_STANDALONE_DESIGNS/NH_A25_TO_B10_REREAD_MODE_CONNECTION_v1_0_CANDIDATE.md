# NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_0_CANDIDATE.md

## 0. STATUS BLOCK

**Status:** CANDIDATE — unaudited; awaiting ChatGPT's independent audit of
this actual file and Ness's explicit acceptance afterward. **Governed
connection package only:** it connects the accepted A25 policy into the
accepted B10 mechanics **without rewriting, patching, replacing, or
modifying either accepted source.** Not accepted, not adopted, not
authoritative, not integrated, not implemented, not `PACKAGE_COMPLETE`.
**B10's current `dependency_blocked_held` behavior at RR2 remains
unchanged until this candidate is independently audited and explicitly
accepted by Ness** (§11). Nothing runtime is unblocked, built, integrated,
or implemented by this file.

**Date:** July 11, 2026.

**Package ID:** A25→B10 connection — how A25's mode assignment is carried
by B10's existing `reread_mode_ref` at RR2 (Bundle 1; map CY-F).

**Intended repository placement:** `05_ACTIVE_CANDIDATE/`
(the physical move into the repository is Ness's action).

## 1. GOVERNING AUTHORITY ORDER

1. `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`
   (adopted by Ness June 29, 2026; governing)
2. `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`
3. `01_AUTHORITATIVE/cursorrules`
4. `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`

The current Design and Wiring Map is subordinate to these files.

## 2. SOURCES READ — IDENTITIES RECALCULATED BEFORE WRITING

- **Accepted A25:** `NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md`
  — SHA-256
  `8a50a862b77fb3efa3d1523c570d88716d002973139d6bd47c26fce2e0246f8b`;
  257 lines; 13,849 bytes — **recalculated on disk; matched exactly.**
  Its closure receipt
  `NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
  (SHA-256 `c640d3675a5c626c95e0654a8f314995930c791554cc8f6f6cf562233e1468c2`)
  — read in full.
- **Accepted B10:** `NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md`
  — SHA-256
  `215b74841321656a8b7fb1cbf4b9ac9b43259315864cd9f85f5ce86b43d10001`;
  329 lines; 23,681 bytes — **recalculated on disk; matched exactly; read
  in full** (§§1–13, including the RR0–RR5 pipeline, the recovery matrix
  rows 1–17, the fail-closed matrix, and the §0B record set). Its closure
  receipt (SHA-256
  `da62a1e8216924f9e9f3182f925e7a1e5063355418a7302eb58f86eee54adeea`)
  — read.
- **Master V10** §7F (line 1647), §7H (line 2114 — triggers and record
  set), §7Q (line 2405), §7R (line 2503), and the §7E scope boundary
  (line 1985: re-read passes must use a separately adopted reread
  mode-assignment rule) — read from the authoritative file.
- **Map v1.6** — A25, B10, and CY-F material — read.
- **Bundle 1 normalization record v1_1**
  (`6828b9bd88cf867d20bfee31b67d13e97e0c573316b43d2298e4764785abeec3`)
  and its acceptance record
  (`d759d99d6d01cfe0371c5f4261912f2a4e11cabc10ec3fd8cc249bd5d522d7f7`)
  — read in full.

All reads are from the governance repository snapshot byte-verified twice
on July 11, 2026, or from this session's delivered files.

## 3. PURPOSE AND SCOPE

**What this candidate is:** the governed connection design. It defines the
append-only mode-assignment representation that B10's existing
`reread_mode_ref` references at RR2, its binding, timing, canonical form,
fail-closed consumption, recovery behavior, context behavior, and the
future design-level release condition.

**What it is not:** it changes no A25 meaning; it changes no B10
identity, claim, layer, trigger, or recovery design; it renames neither
mode; it invents no trigger, threshold, schedule, score, retrieval count,
or degraded rule; it performs no wiring beyond this one connection; it
implements nothing.

## 4. NESS-APPROVED DECISION (PRESERVED EXACTLY IN MEANING)

**Normalized decision:**

> Every reread uses as much clearly relevant information as safely
> available. This applies whether the assignment is direct,
> wider-context, or both. The mode records why the reread applies; it
> does not make the context deliberately narrow. Unrelated information is
> not included, and all existing privacy, access, authorization,
> integrity, and relevance protections remain active.

**Ness's original wording:** "everything all the time. the more the
better" — Ness then confirmed the clarification that "everything" means
**everything relevant to the situation**, not literally every unrelated
memory. Both the original wording and the confirmed clarification are
preserved here as decision provenance; the normalized statement above is
the operative design meaning.

## 5. THE MODE-ASSIGNMENT REPRESENTATION (CANONICAL, APPEND-ONLY)

**The record:** `reread_mode_assignment_record` [proposed] — one
append-only, immutable record per reread claim, referenced by B10's
existing `reread_mode_ref` at RR2. Its semantic content is exactly the
accepted A25 assignment; everything else is mechanical carriage.

**Canonical assignment value — `assigned_modes`:** a **non-empty ordered
mode list** with the fixed canonical order `direct` before
`wider-context`. Exactly three values are valid:

- `["direct"]`
- `["wider-context"]`
- `["direct", "wider-context"]`

**Canonical-form rules:** the same assignment can never be stored in
several conflicting forms — no other ordering (`["wider-context",
"direct"]` is invalid, not an alias), no repetition of a mode within the
list, no empty list, no third or renamed mode name, no free-text mode. A
dual assignment is **the two existing modes together, never a third
semantic mode** — exactly as the accepted A25 §5 rule states.

**Record shape [all field names proposed — mechanical carriage only]:**

| Field | Content |
|---|---|
| `mode_assignment_id` | The record's own stable identity — the value `reread_mode_ref` carries |
| `assigned_modes` | The canonical list (one of the three valid values above) |
| `reread_claim_ref` | The existing B10 claim (`reread_claim_key` binding {root, trigger}) this assignment is bound to |
| `trigger_record_ref` | The existing §7H/B10 trigger record (which already carries trigger type, reason, initiator, new-evidence references, previous reading IDs, configuration reference, timestamp) |
| `assignment_reason` | The real recorded reason the assignment applies — required by A25 and §7H; never empty; a mode never substitutes for a reason |
| `mode_evidence` | For **each** listed mode, the evidence reference(s) showing that mode's relationship applies (references only — never copies; the same new-information evidence may support both modes) |
| `assigned_at` | Timestamp |
| `schema_version` | Record schema version |

**Producer out of scope:** *how* the assignment is produced — how each
relationship is detected or evaluated, by what mechanism, for each
trigger type — remains exactly where the accepted A25 §6 leaves it
(§7H/§7R territory and later governed work), **open and unbiased**. This
candidate defines only the record that carries a produced assignment,
its binding, timing, and consumption.

## 6. BINDING, TIMING, AND ONE-COMMIT IDENTITY

- **Bound to the existing claim and trigger:** every assignment record
  references exactly one committed B10 reread claim and its trigger
  record. No claim → no assignment.
- **Committed before the RR2 context snapshot:** RR2 proceeds only from a
  committed assignment record; the context snapshot's committed state
  references `mode_assignment_id`, binding snapshot to assignment. The
  assignment commit is one atomic compare-and-commit.
- **One canonical assignment per claim:**
  `mode_assignment_key = stable_hash(reread_claim_key +
  "mode_assignment_v1")` [proposed] — exactly one committed assignment
  record can ever exist for a claim; a repeat commit attempt with
  identical content converges idempotently on the existing record; a
  commit attempt with **different** content is refused and surfaced as
  conflicting assignment evidence (§9) — never silently replaced,
  merged, or overwritten.
- **Append-only and immutable for that claim:** once committed, the
  assignment is never edited, deleted, or recalculated for that claim.
  A genuinely different situation is a **new trigger and a new claim**
  under B10's existing rules — never a mutation of this one.

## 7. CONTEXT BEHAVIOR PER ASSIGNMENT

For **every** valid assignment, retrieval gathers **the broadest safely
available set of clearly relevant information** under the settled and
unchanged **§7Q → §7F → §7R** protections and ordering exactly as B10's
RR2 already fixes them (§7Q internal-use authorization via LMAC, then §7F
context retrieval, then §7R relevance). The mode never narrows the
context deliberately; it records **why** the reread applies and directs
**what is checked**:

- **`["direct"]`** — the reread explicitly checks the old reading against
  the direct new information (the trigger's evidence), while still using
  all other clearly relevant context.
- **`["wider-context"]`** — the reread examines how the wider surrounding
  story changes the old reading's meaning, using all clearly relevant
  context.
- **`["direct", "wider-context"]`** — both checks are performed **within
  the same reread operation and the same safely gathered relevant
  context.**

**Hard limits on this section:** no numeric limit, score, threshold,
ranking formula, retrieval count, schedule, or degraded-retrieval rule is
created here — those remain with their existing owners, including **B1**
(retrieval parameter values) and **B26** (system-failure/degraded
design). "More is better" is **never** permission to bypass privacy,
access, authorization, relevance, source-integrity, holding, or safety
rules — every existing protection remains active, and unrelated
information is not included (§7R still excludes it; the decision itself
says so).

## 8. ONE DUAL ASSIGNMENT = ONE REREAD OPERATION

A dual assignment remains **one** B10 reread operation: **one trigger,
one claim, one committed context snapshot, one proposal path, and at most
one new reading layer.** It must not — and mechanically cannot, under the
one-claim and one-reading idempotency points B10 already fixes — create
two claims or two readings merely because both modes apply. The single
proposal performs both checks; the single resulting layer sits beside the
old reading exactly as B10's append-only layering requires.

## 9. FAIL-CLOSED CONSUMPTION (EXISTING VOCABULARY ONLY)

B10's existing duplicate prevention, claim identity, append-only
layering, and crash recovery are preserved unchanged. Consumption of the
assignment at RR2 is fail-closed using **B10's existing outcomes**, with
per-condition recorded reason codes [proposed — record-shape refinement
only, no new terminal]:

| Condition | Behavior (existing B10 vocabulary) | Recorded reason [proposed] |
|---|---|---|
| **Missing** (no committed assignment) | Exactly the current §8 behavior: `dependency_blocked_held` at RR2 — nothing proceeds, no mode invented, `thread_membership_v1` not borrowed | `assignment_missing` |
| **Unreadable** (record exists; store state cannot be read) | Fail closed — `indeterminate_recovery_required` (B10 §7 rows 9–10 pattern); nothing reconstructed | `assignment_unreadable` |
| **Malformed** (shape violates §5's canonical rules) | Fail closed — `indeterminate_recovery_required`; the invalid record stays visible as recorded evidence, never repaired in place | `assignment_malformed` |
| **Empty** (empty mode list) | Fail closed — `indeterminate_recovery_required` | `assignment_empty` |
| **Unknown mode** (any value outside the two accepted names) | Fail closed — `indeterminate_recovery_required`; no mode is coerced or guessed | `assignment_unknown_mode` |
| **Duplicated** (more than one committed assignment observed for one claim — an integrity breach of the one-commit key) | Fail closed — `indeterminate_recovery_required`; neither record is auto-picked or deleted | `assignment_duplicated` |
| **Contradictory** (assignment evidence conflicts — e.g., a differing commit attempt against the committed record, or content contradicting the trigger record) | Exactly B10 §7 row 15's pattern: contradictory evidence → `indeterminate_recovery_required`, fail closed; **the conflict is surfaced and recorded, never resolved by the system** | `assignment_contradictory` |

Every such stop emits B10's existing `fail_closed_event` §0B record with
the reason code; **no false-success result exists or is invented**, and
no new parent terminal is created. **Vocabulary adequacy note for the
audit:** every required stop above is truthfully expressed with B10's
existing accepted outcomes (`dependency_blocked_held`,
`indeterminate_recovery_required`, boundary refusal, `fail_closed_event`
logging); no mechanical gap requiring a new outcome was found. The only
additions are the proposed reason codes, which are record-shape
refinement expressly permitted to this candidate.

## 10. RECOVERY (LOOKUP-FIRST; REUSE, NEVER RECALCULATE)

- **Crash before the assignment commit:** no committed assignment exists;
  recovery finds the claim in its pre-RR2 state (B10 §7 row 2, mode slot
  not permitting). Nothing partial can exist (single atomic commit). The
  assignment must still be produced and committed before RR2; if none is
  available, the claim is held (`assignment_missing`). Nothing is
  recalculated silently, because nothing was committed.
- **Crash after the assignment commit, before the context snapshot:**
  recovery resumes RR2 under the claim (B10 §7 row 2, mode slot now
  permitting) and **reuses the committed assignment exactly** — even if a
  fresh evaluation "would now" assign differently, the committed record
  governs this claim; a genuinely changed situation is a new trigger and
  new claim.
- **An existing assignment found on recovery:** it **is** the assignment
  for that claim — reused as-is; a repeat identical commit converges
  idempotently; no second record; no silent recalculation.
- **Conflicting assignment evidence on recovery:** the §9 contradictory
  path — `indeterminate_recovery_required`, fail closed, conflict
  surfaced and recorded append-only, never auto-resolved, nothing
  deleted.
- **A trigger for which neither accepted A25 relationship applies:** no
  valid A25 assignment can exist — A25's not-blanket rule is thereby
  mechanically honored. The claim is held (`assignment_missing`, with
  reason `no_a25_relationship_applies` [proposed] recorded on the hold);
  nothing proceeds, nothing is invented, no false success. Whether any
  trigger class (for example the manual trigger, which §7H allows "at any
  time" with no further justification) should ever receive its own
  separately governed mode path for such cases is **an identified open
  policy question for Ness** — surfaced here for the audit, deliberately
  not decided or biased by this candidate.

## 11. RELEASE CONDITION — DESIGN-LEVEL ONLY

**Until this connection candidate is independently audited and explicitly
accepted by Ness, B10's current `dependency_blocked_held` behavior at RR2
remains unchanged.** This candidate defines the **future design-level
release condition**: once accepted, **a valid committed A25
mode-assignment reference (§5–§6) allows RR2 to proceed** past the mode
slot, under everything else B10 already requires. This candidate does
**not** claim that runtime execution is unblocked, built, integrated, or
implemented — it is not, and nothing here authorizes it.

## 12. MUST REMAIN OPEN (NONE CLOSED OR BIASED HERE)

- A25's accepted meaning — unchanged; B10's accepted identity, claim,
  layer, trigger, and recovery design — unchanged.
- The assignment **producer** (relationship detection/evaluation per
  trigger type) — open (§5).
- The manual-trigger question surfaced in §10 — open, Ness's.
- **B9 retry-value wiring** into B9, B10, B-HOLD, and B24 — open; not
  performed here.
- **B1/B26** retrieval quantities and degraded behavior — open with their
  owners.
- **B-CYCLE-8, Bundle 1 completion, and whole-system wiring** — open.
- **Master V10 / map / Defaults / cursorrules integration** — open;
  later, separately authorized, Ness-accepted work.
- **The sealed 5,521-root batch** — untouched; never reopened, changed,
  or appended to.
- **All coding, migration, runtime, PC, store, marker, production, and
  implementation work** — unauthorized; awaiting Ness's separate
  implementation authorization.

## 13. DESIGN-COMPLETE CONDITION FOR THIS CANDIDATE

This connection is design-complete when: the Ness decision is preserved
exactly in meaning with its provenance (§4); the canonical three-value
append-only representation is defined with one storable form per
assignment (§5); binding, timing, and one-commit identity are fixed (§6);
context behavior per assignment is defined without quantities and without
protection bypass (§7); one dual assignment remains one operation (§8);
every required fail-closed condition maps truthfully onto existing B10
outcomes with recorded reasons (§9); the five required recovery cases are
answered by reuse-never-recalculate (§10); and the release condition
stays design-level behind audit and acceptance (§11) — subject to
ChatGPT's independent audit and Ness's explicit acceptance.

## 14. CHANGE REPORT AND SELF-AUDIT

**File created:** `NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_0_CANDIDATE.md`
— the only file created by this task. **Nothing existing was modified:**
the accepted A25 v1_2 and its receipt, the accepted B10 and its receipt,
every authoritative, accepted, active-candidate, closure, and historical
file — all preserved byte-identically; nothing committed, pushed, moved,
renamed, overwritten, or deleted in the repository.

**Self-audit:** authority order preserved — PASS. Decision preserved
exactly in meaning, with original wording and confirmed clarification —
PASS. Canonical representation admits exactly the three valid values in
one storable form; dual is never a third mode; neither mode renamed —
PASS. Assignment bound to the existing claim and trigger; committed
before the snapshot; append-only, immutable, one per claim; reused on
recovery, never silently recalculated — PASS. Every fail-closed condition
expressed with existing B10 vocabulary; no false success; conflicts
surfaced, never auto-resolved; only reason codes proposed — PASS. Context
behavior: broadest safely available clearly relevant set under unchanged
§7Q→§7F→§7R; no numbers; no protection bypass — PASS. One dual assignment
= one operation, one claim, one snapshot, one proposal path, at most one
layer — PASS. Release condition design-level only; `dependency_blocked_
held` unchanged until audit and acceptance — PASS. All §12 items left
open; sealed batch protected; no implementation — PASS.

---

*End of `NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_0_CANDIDATE.md` —
CANDIDATE, unaudited, awaiting ChatGPT's independent audit and Ness's
explicit acceptance. Neither accepted source is modified; B10's
fail-closed mode slot remains unchanged until acceptance; nothing is
integrated, implemented, or unblocked at runtime by this file.*

# NH_A29_HOLD_UNTIL_ENOUGH_POLICY_v1_0_CANDIDATE.md

**Status:** CANDIDATE — unaudited; awaiting ChatGPT's independent audit and
Ness's explicit acceptance. Standalone decision package only. Not adopted,
not authoritative, not integrated into Master V10, the Design and Wiring
Map, Decision Defaults, or cursorrules. Authorizes no implementation, code,
store, disk, runtime, or UI work, and no tuning value of any kind.

**Date:** July 7, 2026.

**Package ID:** A29 — "Hold-until-enough" policy: the meaning of "enough"
(Master V10 §7B Part 5; Register A item A29 in the current map).

**Governing authority order:**
1. `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`
   (adopted by Ness June 29, 2026; governing)
2. `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`
3. `01_AUTHORITATIVE/cursorrules`
4. `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`

**Sources read for this candidate:** Master V10 (§7B Part 5 hold-until-enough,
Parts 6–7 inform-don't-ask and the read-only Log; §7G acceptance-check
outcomes including the honest `insufficient_context` fallback reading —
recorded, marked revisable, a valid completed outcome, never a refusal; §0B
one-operation/one-log and no-double-evidence); the current map
`02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` (A29
entry, B-HOLD entry, the hold-until-enough dependency chain, C-7B Part 5,
A31 entry, B16 entry); the accepted
`04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md`
and its `…_PACKAGE_COMPLETE_RECORD_v1_0.md` (externally adjudicated
insufficiency: rejection count never proves insufficiency; only a committed,
externally adjudicated `genuine_insufficiency_confirmed` authorizes the
honest `insufficient_context` reading/surface; A31 remains open). **Sourcing
note (honest):** the accepted
`NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_v1_0_CANDIDATE.md`, its
`…_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`, and
`03_WORKFLOW/NH_REPLACEMENT_EIGHT_BUNDLE_DEPENDENCY_PLAN_v1_0_CANDIDATE.md`
were not yet reachable through the connected project knowledge at write
time; their accepted content was read from the July 6, 2026 creation-and-
acceptance session records, including the accepted B9/B10/B-HOLD
coordination note (B-HOLD owns the waiting lifecycle — external hold
records that block new use of an item until verified release evidence
exists; release is only B-HOLD's evidence-verified interface, failing
closed while A29 is unadopted; while any live hold exists, B9 refuses
admission and B10 refuses/blocks the claim; B-HOLD is never a way to park a
rejection; B16's `dependency_blocked_held` is the promotion-side view of a
B-HOLD fact) and the Bundle-1 composition (mechanical set closed: B24, B11,
B16, B9, B10, B-HOLD; policy side including A29). ChatGPT's audit should
verify this candidate against the actual accepted files. No B-HOLD mechanic
is modified here under either reading.

---

# 0. PURPOSE AND SCOPE

**What A29 is.** A29 records Ness's policy decision on the meaning of
"enough" for hold-until-enough (§7B Part 5): what makes waiting the right
response when something cannot yet be responsibly read, and when the system
must instead produce the honest `insufficient_context` reading rather than
hold.

**Ownership split — preserved exactly:**
- **A29 (this package) owns policy only:** the meaning of "enough," which
  insufficiency holds rather than producing an `insufficient_context`
  reading, and the policy class of a valid release condition.
- **B-HOLD (accepted; unchanged) owns mechanics only:** where the held
  object lives, the hold-record lifecycle and operation identity, the
  release-event structure, idempotency, retry and crash recovery, and the
  settled distinctions from §7E pre-ingest holding, §7G
  `insufficient_context`, and technical retry. **Nothing in this package
  adds, removes, renames, or alters any B-HOLD record, state, field, event,
  or recovery rule.**

**What this package does not do:** it chooses no wait duration, retry value,
check frequency, model, storage, runtime, UI behavior, or tuning number; it
decides no other Register item; it reopens nothing accepted; it integrates
nothing; it authorizes no implementation.

---

# 1. NORMALIZED A29 DECISION RECORD

**Ness-approved A29 rule (carried in the task instruction; preserved
verbatim):**

> N.H holds only when waiting can realistically help because a specific
> missing context/evidence condition can plausibly be satisfied later. N.H
> must not create an endless manual backlog for Ness. N.H must
> automatically track the missing condition, automatically check for
> release when the adopted condition is met, and automatically release the
> hold when the required release-evidence record exists and binds to the
> hold. If the missing context/evidence is not realistically obtainable, or
> waiting has no defined useful condition, N.H should not hold forever; it
> should produce an honest insufficient_context reading instead, clearly
> marked as limited/ungrounded where appropriate.

**Normalized statements (no new meaning added):**
1. A hold is legitimate **only** when a **specific** missing
   context/evidence condition can be named **and** that condition is
   **realistically, plausibly satisfiable later**, so that waiting can
   realistically help.
2. Holds must never become an endless manual backlog for Ness.
3. For every hold, N.H **automatically tracks** the recorded missing
   condition, **automatically checks** for release when the adopted
   condition is met, and **automatically releases** the hold when the
   required release-evidence record exists **and binds to that hold**.
4. When the missing context/evidence is **not realistically obtainable**,
   or waiting has **no defined useful condition**, N.H does not hold —
   and never holds forever — but produces the honest
   `insufficient_context` reading, clearly marked as limited/ungrounded
   where appropriate.

---

# 2. THE POLICY FORK — HOLD VERSUS `insufficient_context`

The fork applies wherever the accepted mechanics already place the
"cannot-responsibly-read-yet" moment (B-HOLD admission; the §7G outcome
path). This package fixes only which branch the policy selects; the exact
placement of the fork inside each end-to-end cycle remains B-CYCLE wiring.

## 2.1 HOLD is appropriate only when — the two-part test

Both parts must hold, at the moment the hold would be opened:

- **Specificity.** The missing context/evidence can be named as a
  **specific condition** — a concrete, recordable statement of what is
  missing and what would count as its satisfaction. "More context might
  help someday" is not specific and never justifies a hold.
- **Realistic obtainability.** Satisfying that condition later is
  **plausible under known circumstances** — the awaited material or event
  is of a kind the system can actually receive through its governed
  channels. A condition nothing is expected to satisfy does not justify a
  hold.

When both parts hold, waiting can realistically help, and holding (through
B-HOLD's unchanged mechanics) is the correct response instead of forcing a
weak reading.

*Illustrative, non-normative contrast (grounded in settled system facts;
decides nothing):* a fragment whose thread membership is pending §7E
resolution names a specific, plausibly-satisfiable condition — hold; a bare
ambiguous fragment for which no identifiable future material would resolve
the ambiguity names none — honest `insufficient_context` reading.

## 2.2 The honest `insufficient_context` reading is appropriate when

The system **cannot responsibly ground a reading now**, and **either** no
specific useful condition can be defined, **or** the named missing
context/evidence is not realistically obtainable. Then:

- No hold is opened; no hold persists indefinitely on that basis.
- The honest `insufficient_context` reading is produced through the
  **already-settled machinery, unchanged**: in the §7G reading pass, the
  separate honest fallback reading — recording insufficient context, marked
  revisable, a valid completed outcome, never a refusal and never the
  rejected proposal itself; in the B24 dual-model path, only a committed,
  **externally adjudicated** `genuine_insufficiency_confirmed` authorizes
  the `insufficient_context` reading/surface, and rejection count is never
  proof of insufficiency.
- The reading is **clearly marked as limited/ungrounded where
  appropriate**, using the settled reading contract's existing honest
  marking (insufficient-context, revisable); no new marking field is
  invented here.
- A later genuinely new trigger may produce a new reading beside it through
  the settled §7H reread lifecycle — never by editing the honest reading.

**Adjudication ownership preserved:** A29 does **not** define how
insufficiency is detected or adjudicated (§7G / B24 own that), and does
**not** choose the substantive "grounded enough" threshold (**A31 — open**).
A29 decides only the fork between *holding* and *producing the honest
reading* once the responsible-read failure is established by the owning
machinery.

## 2.3 What a hold is never (settled distinctions, preserved)

- **Not §7E pre-ingest holding** — a different gate with its own rules.
- **Not the `insufficient_context` reading itself** — a hold produces no
  reading; the honest reading is a completed outcome, not a wait.
- **Not technical retry** — B9 re-attempts the same operation identity
  under declared budgets; a hold blocks new use until evidence exists.
- **Never a parking place for a rejected proposal** — terminal stays
  terminal (the accepted coordination rule); a substantive rejection is not
  laundered into a hold until it "looks fresh."

## 2.4 No forever-hold

A hold is legitimate only while its recorded condition remains a genuine,
specific, plausibly-satisfiable condition. As policy, an item must not stay
held indefinitely once its recorded condition is known to be unsatisfiable
or was never validly defined; such an item follows §2.2 (the honest
`insufficient_context` reading). **The detection/trigger mechanics for
recognizing that a recorded condition has become unsatisfiable — and the
governed transition steps — are open** (B-HOLD-consistent mechanics and
later tuning; nothing is invented here, and no expiry duration is chosen).

---

# 3. THE "NOT THE MANUAL GUY" RULE

- N.H must not convert HOLD into a manual review backlog for Ness. **No
  hold requires Ness's manual review, approval, or triage in order to be
  tracked, checked, or released.** The lifecycle in §4 is automatic.
- Holds remain **visible** through the settled read-only Log surface
  (§7B Part 7: look-don't-touch; seeing is not approving; a log to read,
  not a queue to action) — consistent with Part 6's inform-don't-ask rule:
  the system surfaces the specific gap by name, keeps running, and blocks
  nothing on Ness.
- Ness **may** act at his own initiative — for example, later supplying the
  missing answer — and such material lands only through the governed
  channels as new evidence; it is never a required step of the hold
  lifecycle.
- Any design or implementation that would require per-hold manual handling
  by default violates this package.

---

# 4. AUTOMATIC TRACKING, CHECKING, AND RELEASE

All four subsections use B-HOLD's accepted records and interfaces
**unchanged**; exact record and field names live in B-HOLD and are not
restated or renamed here.

## 4.1 Automatic condition tracking

Every hold records, at open time, its **specific missing condition** — the
policy-valid content per §2.1 — inside B-HOLD's hold record. The condition
is a recorded fact about what is awaited, never an interpretation and never
evidence for any reading.

## 4.2 Automatic release checking

When the adopted condition is met, N.H **checks for release
automatically**. The check is a **DUMB, mechanical verification** against
the recorded condition and the release evidence — it performs no fresh
interpretation and assigns no meaning. **The exact trigger mechanism,
frequency, scheduling, and batching of checks are open**
(mechanics/tuning; not chosen here).

## 4.3 Automatic release — evidence-bound only

A hold is released **only** when the **required release-evidence record
exists and binds to that hold**, through B-HOLD's evidence-verified release
interface, unchanged. Release evidence arrives only through the system's
governed channels and is **recorded**; the release references it **by
pointer** — the evidence is never copied into the hold, and the release
never manufactures evidence. No path releases a hold without the bound
evidence record; no human assertion substitutes for it outside the governed
channels.

## 4.4 Fail-closed while held — preserved

- While any live hold exists on an item, **blocked stays blocked**: B9
  refuses admission, B10 refuses/blocks the claim, nothing queues around
  the hold (the accepted coordination boundary, unchanged).
- Missing, unverifiable, ambiguous, or non-binding release evidence →
  **remain held**. A failed or crashed release check leaves the hold in its
  authoritative held state under B-HOLD's recovery; there is no silent or
  partial release, ever.
- Until this A29 package is accepted and its policy is in force through
  the governed path, B-HOLD's existing default continues: the release path
  **fails closed while A29 is unadopted**. This candidate does not place
  itself in force.

## 4.5 Append-only logging — no double evidence

Hold opened, condition recorded, each automatic check performed (with
result), each block, each release, and each recovery step are recorded
under **§0B one-operation/one-log**, through B-HOLD's own record set,
unchanged. **Repetition adds no certainty**: repeated checks, repeated
blocks, or the fact of having been held never strengthen any
interpretation; a hold and its release are lifecycle facts, **never
evidence** for the meaning of the held item; the release-evidence record is
referenced by pointer and is never duplicated into a second vote.

---

# 5. BOUNDARIES PRESERVED (BINDING ON THIS PACKAGE)

- **B-HOLD mechanics unchanged** — storage location, lifecycle, operation
  identity, release-event structure, idempotency, retry and crash recovery,
  and the three settled distinctions all remain exactly as accepted.
- **§7G / B24 unchanged** — acceptance-check outcomes, the honest fallback
  reading's contract, and B24's externally adjudicated insufficiency
  (including "rejection count is never proof of insufficiency") are
  consumed as-is, never redesigned.
- **A31 open** — the substantive "grounded enough" threshold is not chosen
  or biased here.
- **B16 seam unchanged** — `dependency_blocked_held` remains the
  promotion-side view of a B-HOLD fact; no promotion policy is decided.
- **Not reopened:** B24, B-HOLD, B11, B16, B9, B10, A2, A1.
- **Not decided:** A25; B9 retry values and the authorized fallback point;
  B10 reread mode policy; wait durations; check frequencies; expiry values;
  model choices; storage/runtime choices; UI behavior; implementation code;
  any final tuning number.
- **DUMB/SMART preserved:** the release check is mechanical verification;
  no interpretation is promoted to fact; a hold carries no evidential
  weight; quarantine/production and root-evidence/prior-reading-context
  separations are untouched.
- **No integration; no adoption; no implementation** — Master V10, the
  map, Defaults, and cursorrules are unmodified; nothing here is marked
  adopted, authoritative, implemented, or package-complete.

---

# 6. OPEN DEPENDENCIES (EXPLICIT; NONE CLOSED HERE)

- **A25** — reread mode-assignment rule (B10 execution stays blocked-open
  at its mode slot).
- **A31** — substantive "grounded enough" acceptance threshold.
- **B9 values** — retry attempts, timing, backoff, trigger, and the
  authorized fallback point.
- **B10** — reread operation-identity wiring execution details (gated on
  A25).
- **B16** — promotion policy specifics beyond the accepted architecture.
- **B-CYCLE wiring** — the exact placement of the hold-vs-read fork inside
  each end-to-end cycle; synchronization and latency policy.
- **Automatic-check mechanics/tuning** — trigger mechanism, frequency,
  scheduling, batching; the detection/transition mechanics for a recorded
  condition that becomes unsatisfiable (§2.4); any expiry representation.
- **Any future controlled vocabulary of condition classes** — a later Ness
  decision if ever wanted; not required by, and not started in, this
  package.
- **Final model/provider choices; benchmark thresholds; implementation,
  storage, and runtime choices; Master V10 / map / Defaults / cursorrules
  integration** — all open and separately governed.
- No other open Register-A/B item is closed or biased by this package.

---

# 7. DESIGN-COMPLETE CONDITION FOR THIS PACKAGE

This package is design-complete for A29 when: the Ness-approved rule is
preserved and normalized without added meaning (§1); the HOLD /
`insufficient_context` fork is defined with the two-part test and the
honest-reading branch, consuming §7G/B24 unchanged and leaving A31 open
(§2); the anti-backlog rule binds (§3); automatic tracking, checking, and
evidence-bound release are required at policy level with mechanics/tuning
left open and B-HOLD's interface unchanged (§4); fail-closed-while-held and
§0B no-double-evidence are preserved (§4.4–4.5); every boundary in §5
holds; and every dependency in §6 remains open — subject to ChatGPT's
independent audit and Ness's explicit acceptance.

---

# 8. CHANGE REPORT

**File created:** `NH_A29_HOLD_UNTIL_ENOUGH_POLICY_v1_0_CANDIDATE.md` — the
only file created by this task. First version; no prior A29 file exists or
was modified. **Sources untouched:** Master V10, Defaults, cursorrules, the
Companion, the map v1.6, all accepted packages and closure records (B24,
B11, B16, B9, B10, B-HOLD, A2, coordination note), and all historical
candidates remain unmodified; nothing was integrated; no implementation,
disk, store, seal, or runtime action occurred. **Sourcing caveat carried in
the header:** the B-HOLD pair and the eight-bundle plan file were read via
their July 6 creation/acceptance session records because the repo copies
were not yet reachable in project knowledge; the audit should verify
against the actual files.

---

# 9. PACKAGE SELF-AUDIT (internal; per the blocking standard)

- **Authority:** order preserved; Master V10 governing; map subordinate;
  candidate status explicit; no adoption declared. **PASS.**
- **Concept fidelity / no loss:** Ness's rule preserved verbatim and
  normalized without additions; §7B Part 5, Parts 6–7, §7G outcomes, and
  the accepted coordination boundaries carried unchanged. **PASS.**
- **No unauthorized policy invention:** no duration, frequency, expiry,
  threshold, taxonomy, model, storage, runtime, UI, or tuning value chosen;
  A31/A25/B9/B10/B16/B-CYCLE untouched. **PASS.**
- **Manual-backlog rule:** present and binding (§3); no per-hold manual
  step required anywhere. **PASS.**
- **Safe release:** release only via B-HOLD's evidence-verified interface
  with a bound release-evidence record; no silent, partial, or
  assertion-based release. **PASS.**
- **Fail-closed preserved:** held blocks B9/B10; ambiguous evidence stays
  held; unadopted-A29 default stated; crash leaves authoritative held
  state. **PASS.**
- **B-HOLD/B24 boundary intact:** mechanics vs policy split preserved;
  adjudication ownership preserved; B16 seam untouched; nothing reopened.
  **PASS.**
- **No duplicate/double evidence:** §0B one-operation/one-log; holds and
  releases weightless; evidence by pointer. **PASS.**
- **No false completion:** candidate status; open dependencies listed;
  nothing marked complete, adopted, or integrated. **PASS.**
- **No premature implementation:** no code, pseudocode, migration, store,
  marker, seal, disk, or runtime action. **PASS.**

---

*End of `NH_A29_HOLD_UNTIL_ENOUGH_POLICY_v1_0_CANDIDATE.md` — CANDIDATE,
unaudited, awaiting ChatGPT's independent audit and Ness's explicit
acceptance. All authority, accepted, and historical files remain unchanged;
no implementation was performed.*

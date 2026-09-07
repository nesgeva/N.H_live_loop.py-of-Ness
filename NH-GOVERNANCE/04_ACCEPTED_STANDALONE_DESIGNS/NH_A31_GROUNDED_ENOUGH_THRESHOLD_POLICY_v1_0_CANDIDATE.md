# NH_A31_GROUNDED_ENOUGH_THRESHOLD_POLICY_v1_0_CANDIDATE.md

**Status:** CANDIDATE — unaudited; awaiting ChatGPT's independent audit and
Ness's explicit acceptance. Standalone decision package only. Not adopted,
not authoritative, not integrated into Master V10, the Design and Wiring
Map, Decision Defaults, or cursorrules. Authorizes no implementation, code,
store, disk, runtime, or UI work, and no tuning value of any kind.

**Date:** July 7, 2026.

**Package ID:** A31 — Acceptance-Check "grounded enough" threshold policy
(Master V10 §7G; Register A item A31 in the current map; the Bundle-1
policy item A31). The map fixes that any threshold changing the substantive
meaning of "grounded enough" is a Ness policy decision that must never be
silently selected mechanically — this package records that decision, made
by Ness.

**Intended repository placement:** `05_ACTIVE_CANDIDATE/`
(the physical move into the repository is Ness's action).

**Governing authority order:**
1. `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`
   (adopted by Ness June 29, 2026; governing)
2. `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`
3. `01_AUTHORITATIVE/cursorrules`
4. `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`

**Sources read for this candidate:** Master V10 / map C-7G (the settled
acceptance sequence: seven checks; pass/fail; the distinct settled
rejection categories never mislabeled; `insufficient_context` as the
written honest-fallback reading, not a peer acceptance outcome; a
substantively rejected proposal terminal until the later B9 retry policy;
the rejected proposal logged but never silently becoming the reading); the
map's A31 and A29 Register entries and the Acceptance-Check chain note;
the accepted
`04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md`
and its `…_PACKAGE_COMPLETE_RECORD_v1_0.md` (the dual-lane A31 rule; the
settled-checks mapping; the three-stage validation with fail-closed
`indeterminate_unvalidated`; the §2.10 insufficiency-assessment family —
externally adjudicated, committed `genuine_insufficiency_confirmed` as the
only authorization for the honest `insufficient_context` reading/surface;
rejection count never proof of insufficiency; producer self-review never
evidence; the assessment running only at the B9-authorized fallback point;
model confidence as metadata; "validated" meaning only "no rule-detectable
error found"); the accepted
`04_ACCEPTED_STANDALONE_DESIGNS/NH_A29_HOLD_UNTIL_ENOUGH_POLICY_v1_0_CANDIDATE.md`
and the accepted
`04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md`
with its `…_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` — both read from the
accepted on-disk working copies whose SHA-256 match the identities recorded
in their closure records (`31d5a1…0d65`, `f0ee0b…11b5`, `88ef2b…ccffa`),
since the freshly accepted repo copies may not yet be indexed in project
knowledge. **Sourcing note (honest, carried from the accepted A29 and
firmness packages):**
`03_WORKFLOW/NH_REPLACEMENT_EIGHT_BUNDLE_DEPENDENCY_PLAN_v1_0_CANDIDATE.md`
was not reachable through the connected project knowledge at write time;
its accepted Bundle-1 composition (policy side including A31) was read from
the July 6, 2026 session records. ChatGPT's audit should verify against the
actual files. No accepted content is modified under either reading.

---

# 0. PURPOSE AND SCOPE

**What A31 is.** A31 records Ness's policy decision on the substantive
meaning of "grounded enough" for the Reading Proposal Acceptance Check
(§7G): when a reading/proposal has enough **direct support** to be usable,
when it must be limited, when it must not pass as-is, and when the honest
answer is that the system cannot responsibly decide. **This is about
grounding, not truth.** A grounded reading is one adequately supported by
its authorized evidence within its declared scope — not one proven true.

**What this package fills:** exactly the A31 open slot — the substantive
threshold meaning. **B24 (accepted, unchanged) carries the Acceptance-Check
architecture and the mechanical threshold representation that follow this
decision.** Nothing here redesigns any B24 record, stage, state, criterion,
or recovery rule, and nothing here changes the settled §7G sequence.

**What this package does not do:** it creates no numeric threshold and no
hidden score; it decides no model/provider choice, no reviewer/quorum
policy, no B9 retry value, no A25 assignment; it changes no B10, B16,
B-CYCLE, storage, runtime, UI, or implementation detail; it integrates
nothing, edits no accepted file, and adopts nothing.

---

# 1. NORMALIZED DECISION RECORD — NESS'S PLAIN-LABELS DECISION

**Ness-approved decision (carried in the task instruction; preserved):**
A31 uses **plain qualitative labels — not numbers, percentages, scores, or
hidden threshold math.** The A31 status field is **`grounding_status`**,
with exactly four allowed labels:

- `grounded_enough`
- `partly_grounded`
- `not_grounded_enough`
- `insufficient_context`

**Required meaning (preserved):**
- `grounded_enough` — enough direct source/context support exists for the
  reading to pass as usable **within its declared scope**.
- `partly_grounded` — some parts are supported, but other parts must be
  limited, separated, weakened, or marked as possibility/uncertain.
- `not_grounded_enough` — the reading makes a claim that is not supported
  enough and **must not pass as-is**.
- `insufficient_context` — the system **cannot responsibly decide** because
  needed context/evidence is missing.

**Normalized statements (no new meaning added):**
1. The grounded-enough threshold is expressed **only** through these four
   qualitative labels. No number, percentage, weight, score, or threshold
   arithmetic exists anywhere in A31 — visibly or hidden.
2. The labels describe **the grounding axis only**: how much direct,
   authorized support the reading has relative to what it claims, within
   its declared scope.
3. An unsupported claim never passes as usable; a possibility never passes
   as fact; missing context is named honestly rather than papered over.
4. When the higher status cannot honestly be established, the
   **less-claiming status governs** — grounding is never granted by
   default (fail-closed, §8).

---

# 2. THE `grounding_status` FIELD

- **What it describes.** The grounding axis of one reading/proposal
  revision against its authorized evidence and declared scope — nothing
  else. It is an assessment status, not a quality score, not a truth
  verdict, and not a ranking input.
- **Allowed values.** Exactly the four labels of §1. No fifth value, no
  numeric companion, no derived composite.
- **Who sets it.** Only the settled checking machinery — the §7G
  acceptance check as architected by accepted B24 (validation stages,
  external governed adjudication). **The producer's self-assessment never
  sets or moves it** (producer self-review is never evidence), and **model
  confidence is metadata that never moves it.**
- **Where it lives.** The status is recorded with the acceptance/assessment
  outcome under the owning machinery's accepted record contracts. Its
  exact mechanical representation belongs to **B24's settled
  "threshold representation (mechanical form only)" slot** and later
  schema work — deferred, not designed here.
- **Not a peer-outcome rewrite.** The four labels do **not** create new
  acceptance outcomes and do **not** rename any settled outcome or
  rejection category. In particular, the settled rule stands:
  `insufficient_context` is **not a peer acceptance outcome** — it is the
  condition whose settled consequence is the written honest-fallback
  reading (§3, §5).
- **Provisional and revisable.** Like every assessment fact, a
  `grounding_status` is dated and bound to the exact revision assessed;
  a later revision or genuinely new evidence produces a **new** assessment
  record beside the old through the settled lifecycle — never an edit.

---

# 3. THE FOUR LABELS — MEANING AND CONSEQUENCE

All criteria are **qualitative judgments about direct support from the
authorized evidence**, under the settled evidence rules of §4. No counting
rule, quota, or arithmetic is created.

- **`grounded_enough`** — every claim the reading makes, as scoped, has
  enough direct source/context support: facts directly established from
  the authorized evidence; possibilities present only as evidence-linked,
  explicitly unconfirmed, rejectable possibilities; uncertainty expressed
  honestly. **Consequence:** the reading may pass as usable within its
  declared scope. `grounded_enough` is **necessary on the grounding axis,
  never sufficient alone** — every other settled §7G check (fields valid;
  channels not confused; no self-contradiction; mode followed; nothing
  invented) still applies unchanged.
- **`partly_grounded`** — the reading is a mix: some parts carry enough
  direct support; other parts claim more than their support allows.
  **Consequence:** the reading **must not pass as-is.** The supported
  parts may stand only after the unsupported parts are **limited,
  separated, weakened to evidence-linked possibility, or marked
  uncertain** — through the accepted B24 revision mechanics (whose loop
  values remain B9-owned and open) or within an honestly narrowed declared
  scope. Nothing unsupported rides through on the strength of the
  supported parts.
- **`not_grounded_enough`** — the reading's claim is not supported enough
  to stand at all as proposed. **Consequence:** the settled substantive
  rejection path, unchanged — the specific settled rejection reason is
  recorded distinctly (fabrication, unsupported certainty, and the other
  settled categories are **not replaced, merged, or relabeled** by this
  status), the rejected proposal never silently becomes the reading, and a
  substantively rejected proposal remains **terminal** until the later B9
  retry policy exists. A rejection is never parked as a hold (§6).
- **`insufficient_context`** — the system cannot responsibly decide
  because needed context/evidence is missing: the available authorized
  root/context genuinely cannot support a grounded reading **or** a
  grounded evidence-linked possibility. **Consequence:** the settled
  honest path, unchanged — the written, marked-revisable honest fallback
  reading (§7G), which in the accepted dual-model architecture is
  authorized **only** by an externally adjudicated, committed
  `genuine_insufficiency_confirmed` (§5). It is never a relabeling of a
  rejected malformed, fabricated, or mode-violating proposal, and
  **rejection count is never proof of insufficiency.**

**Boundary rule (never-force, less-claiming):** when the machinery cannot
honestly establish the higher status, the lower one governs —
`grounded_enough` is never reached by default, a genuine mix is
`partly_grounded` rather than rounded up, an unsupported core claim is
`not_grounded_enough` rather than softened into a pass, and honest
incapacity is `insufficient_context` rather than a forced verdict either
way.

---

# 4. FACTS, POSSIBILITIES, UNCERTAINTY, INSUFFICIENCY — B24 RULES PRESERVED

Carried **binding and unchanged** from the accepted B24 package and the
settled Master rules:

- **Facts must be directly established only** — from the authorized
  evidence, on the facts lane.
- **Possibilities stay separate from facts** — the dual-lane discipline is
  preserved; a possibility never migrates lanes by repetition, confidence,
  or paraphrase.
- **Possibilities must be evidence-linked, explicitly unconfirmed, and
  rejectable.** An un-linked guess is not a possibility; it is an
  unsupported claim.
- **Model confidence is metadata, never authority** — it moves no status,
  resolves no disagreement, and grounds nothing.
- **"Validated" means only "no rule-detectable error found," never
  substantive truth** — and `grounded_enough` likewise asserts adequate
  support, never truth.
- **Derived material is never independent evidence for the interpretation
  that produced it.**
- **Circular support is forbidden** — including prior readings standing in
  for root evidence; the two labeled channels stay separate.
- **No double evidence** — repetition, restatement, or re-logging adds no
  certainty and raises no status.
- **Fail closed when grounding cannot be honestly established** (§8).

**How A31 separates the four conditions:** supported-as-claimed →
`grounded_enough`; supported-in-part → `partly_grounded` with the
unsupported remainder limited or demoted to honest possibility/uncertainty;
claiming-beyond-support → `not_grounded_enough`; unable-to-decide-for-lack-
of-evidence → `insufficient_context`. Uncertainty is expressed **inside**
readings honestly (settled check), and insufficiency is a condition **about
the evidence**, never a euphemism for a defective proposal.

---

# 5. HOW B24 USES THE A31 STATUS (ARCHITECTURE UNCHANGED)

- The accepted B24 validator-first flow **consumes this policy; it is not
  redesigned by it.** Stage structure, criteria, records, provenance,
  independence checks, adjudication, and every fail-closed commit remain
  exactly as accepted.
- `grounded_enough` corresponds to the grounding-relevant settled checks
  passing over the committed authorized evidence set (facts entailed on
  the facts lane; possibilities evidence-linked; certainty honest) —
  acceptance still requires **all** settled conditions, and the accepted
  fail-closed boundaries (`indeterminate_unvalidated` and its reasons)
  stand unchanged.
- `partly_grounded` corresponds to the accepted revision path: validator
  findings identify the unsupported parts; the producer may revise within
  B24's bounded mechanics (**loop values B9-owned, open**); nothing passes
  until the revised brief is grounded as claimed.
- `not_grounded_enough` corresponds to the settled substantive rejection
  commits with their distinct recorded reasons — terminal until B9,
  auditable, never silently replaced, never relabeled as insufficiency.
- `insufficient_context` is reachable **only** through the accepted §2.10
  insufficiency-assessment family: externally adjudicated, committed
  `genuine_insufficiency_confirmed`, run **only at the B9-authorized
  fallback point**; producer self-review never confirms it; an invalid
  validator configuration never becomes evidence of insufficiency; and the
  resulting honest reading/surface still passes the settled output gates.
- The single-authority rule holds end to end: the checking machinery
  assigns the status; **no generator, no confidence number, and no
  repetition** ever does.

---

# 6. A31 VERSUS A29 — INSUFFICIENCY IS NOT A HOLD

**A29 hold-until-enough remains separate and unchanged.** The two answer
different questions: A31 assesses **how grounded a reading/proposal is
now**; A29 governs **whether waiting is the right response** when context
is missing.

- If needed context/evidence is missing **and** the accepted A29 two-part
  test holds — a **specific** missing condition exists and it is
  **realistically, plausibly satisfiable later**, so waiting can
  realistically help — the item may go to hold under **A29/B-HOLD**,
  through B-HOLD's unchanged mechanics.
- If waiting will **not** realistically help — no specific useful
  condition, or the missing evidence is not realistically obtainable —
  A31 produces the honest outcome instead: `insufficient_context` (via the
  settled machinery) or `not_grounded_enough` where the proposal claims
  beyond its support. **No endless backlog is created for Ness**, and no
  hold requires his manual review (the accepted A29 "not the manual guy"
  rule binds).
- **A hold is never a parking place for a rejection** — a substantively
  rejected proposal stays terminal (accepted coordination rule), and a
  hold's release runs only through B-HOLD's evidence-verified interface.
- A `grounding_status` value never opens, blocks, or releases a hold by
  itself; the A29 policy test and B-HOLD mechanics govern that lifecycle.

---

# 7. GROUNDING IS NOT — SEPARATIONS PRESERVED

- **Not truth.** `grounded_enough` means adequately supported within
  declared scope — never proven, never fact-beyond-its-evidence.
- **Not firmness.** Firmness is how strongly the perspective owner appears
  to hold a stance (accepted firmness policy). **A person seeming strongly
  committed to a stance does not make the stance grounded enough; a
  high-firmness telling can still be ungrounded as fact.** Firmness never
  feeds, raises, or substitutes for `grounding_status`, and grounding
  never rewrites firmness.
- **Not confidence.** The reading's two-slot confidence and any model
  self-assessment remain metadata — never authority, never a threshold
  input.
- **Not relevance.** §7R/A4 relevance gating is its own settled/open
  dimension; a relevant reading can be ungrounded and a grounded one
  irrelevant.
- **Not source reliability.** That slot stays where the accepted contracts
  put it; it is context for judgment, never a score that moves the status.
- **Not "validated."** Validation asserts only that no rule-detectable
  error was found; it never upgrades grounding and never asserts truth.

---

# 8. FAIL-CLOSED BEHAVIOR

- **Grounding is never granted by default.** If the machinery cannot
  honestly establish a status, the less-claiming status governs; if even
  the assessment cannot complete, the settled fail-closed commits stand
  unchanged (`indeterminate_unvalidated` and the accepted boundary
  reasons) — **never** a silent pass, **never** a default
  `grounded_enough`.
- **Insufficiency also fails closed:** an incomplete, self-reviewed,
  unauthorized, or configuration-invalid assessment never becomes
  `genuine_insufficiency_confirmed` — honest incapacity must itself be
  established, never assumed.
- **No silent operation:** every assessment, status, rejection reason,
  revision, and fallback event stays inside the accepted §0B append-only
  record discipline of its owning machinery — one operation, one log,
  no double evidence.

---

# 9. BOUNDARIES (BINDING ON THIS PACKAGE)

This package must not and does not:
- create numeric thresholds, scores, percentages, or hidden threshold
  math;
- decide final model/provider choices;
- decide reviewer/quorum or provider-disagreement policy (open, per
  accepted B24);
- decide B9 retry values or the fallback timing;
- decide A25 reread mode assignment;
- change B10, B16, B-CYCLE, storage, runtime, UI, or implementation;
- integrate anything into Master V10, the Design and Wiring Map, Defaults,
  or cursorrules;
- edit any accepted file (B24, A29, firmness, A2, B11, B16, B9, B10,
  B-HOLD, the coordination note — all untouched);
- mark itself adopted or authoritative;
- authorize code, database, runtime, migration, UI, or tuning work.

**DUMB/SMART preserved:** the status is assigned by governed checking
machinery over recorded evidence; DUMB moves and records without
interpreting; SMART interprets without turning interpretation into fact;
quarantine/production and root-evidence/prior-reading separations stand.

---

# 10. OPEN DEPENDENCIES (EXPLICIT; NONE CLOSED HERE)

- **A25** — reread mode-assignment rule;
- **A1** — story-bearing gold cases: blocked per
  `NH_A1_ENGINE_C_GOLD_CASES_MISSING_SOURCE_BLOCKER_RECORD_v1_0.md`; any
  worked-example or calibration use of these labels in future gold
  material belongs there;
- **B9 values** — retry attempts, timing, backoff, trigger, and the
  authorized fallback point that gates the insufficiency assessment;
- **B10** — reread wiring execution (gated on A25);
- **B16** — promotion policy;
- **B-CYCLE wiring**;
- **reviewer/quorum and provider-disagreement policy** — open, as accepted
  B24 leaves it;
- **mechanical threshold representation and the `grounding_status` record
  home/schema form** — B24's settled mechanical slot and later schema
  work;
- **final model/provider choices; benchmark scoring thresholds**;
- **final integration** — Master V10, the Design and Wiring Map, Defaults,
  cursorrules;
- **storage/runtime/model/UI/tuning and all implementation** — open and
  separately governed.
- No other open Register-A/B item is closed or biased by this package.

---

# 11. DESIGN-COMPLETE CONDITION FOR THIS PACKAGE

This package is design-complete for A31 when: Ness's plain-labels decision
is preserved and normalized without added meaning (§1); `grounding_status`
and its four labels are defined with honest, non-numeric criteria and
consequences, including the less-claiming boundary rule (§2–§3); the B24
facts/possibilities/uncertainty/insufficiency rules are carried binding and
unchanged (§4); the accepted B24 flow consumes the policy without redesign
(§5); the A29 fork is preserved without backlog or rejection-parking (§6);
the grounding separations hold (§7); fail-closed behavior holds (§8); every
boundary in §9 holds; and every dependency in §10 remains open — subject to
ChatGPT's independent audit and Ness's explicit acceptance.

---

# 12. CHANGE REPORT

**File created:** `NH_A31_GROUNDED_ENOUGH_THRESHOLD_POLICY_v1_0_CANDIDATE.md`
— the only file created by this task. First version; no prior A31 file
exists or was modified. **Sources untouched:** Master V10, Defaults,
cursorrules, the Companion, the map v1.6, all accepted packages and closure
records (B24, B11, B16, B9, B10, B-HOLD, the coordination note, A2, A29,
Story-Layer firmness), the A1 blocker record, and all historical candidates
remain unmodified; nothing was integrated; no implementation, disk, store,
seal, or runtime action occurred. **Sourcing caveats carried in the
header:** the eight-bundle plan file read via the July 6 session records;
the freshly accepted A29/firmness files read from hash-verified accepted
working copies; the audit should verify against the actual repository
files.

---

# 13. PACKAGE SELF-AUDIT (internal; per the blocking standard)

- **Authority:** order preserved; Master V10 governing; the map's A31
  reservation honored — the threshold is selected by Ness, recorded here,
  never mechanically. **PASS.**
- **Concept fidelity / no loss:** Ness's decision, the four labels, the
  required meanings, the B24 preservation list, the A29 relationship, and
  the firmness relationship all appear intact; the settled §7G sequence,
  rejection categories, and honest-fallback rule carried unchanged.
  **PASS.**
- **No unauthorized numeric scoring:** no number, percentage, weight,
  quota, or hidden math anywhere. **PASS.**
- **No grounding/truth/confidence collapse:** §7 separations explicit;
  "validated ≠ truth" and "confidence = metadata" carried. **PASS.**
- **No possibility promoted to fact:** dual-lane discipline binding;
  evidence-linked, explicitly unconfirmed, rejectable; no lane migration.
  **PASS.**
- **No unsupported claim allowed to pass:** `partly_grounded` blocks
  as-is passage; `not_grounded_enough` rejects; less-claiming boundary
  rule; `grounded_enough` necessary-not-sufficient. **PASS.**
- **No A29/A31 confusion:** the fork stated; holds only under the A29
  two-part test through B-HOLD; insufficiency honest, never a wait and
  never a parked rejection; no Ness backlog. **PASS.**
- **No premature implementation:** no code, schema design, record layout,
  migration, store, marker, seal, disk, or runtime action; representation
  deferred to B24's mechanical slot. **PASS.**
- **No false completion:** candidate status; open dependencies listed;
  nothing marked complete, adopted, or integrated. **PASS.**
- **No unrelated dependency closed:** §10 explicit; catch-all stated.
  **PASS.**

---

*End of `NH_A31_GROUNDED_ENOUGH_THRESHOLD_POLICY_v1_0_CANDIDATE.md` —
CANDIDATE, unaudited, awaiting ChatGPT's independent audit and Ness's
explicit acceptance. All authority, accepted, and historical files remain
unchanged; no implementation was performed.*

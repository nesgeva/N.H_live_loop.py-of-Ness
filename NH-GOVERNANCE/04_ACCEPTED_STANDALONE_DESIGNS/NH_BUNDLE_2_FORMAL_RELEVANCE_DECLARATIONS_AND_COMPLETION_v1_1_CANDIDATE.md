# NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md

## 0. STATUS BLOCK

**Status:** CANDIDATE — unaudited; awaiting ChatGPT's independent audit of
this actual file and Ness's explicit acceptance afterward. **Additive
Bundle 2 completion candidate only.** It completes the formal Tier 1 /
Tier 2 relevance-declaration work that the accepted Bundle 2 package
explicitly left open (accepted Bundle 2 v1.0 §16, first item). It does
**not** replace, rewrite, correct, or reopen the accepted
`NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_v1_0_CANDIDATE.md`
or any other accepted, authoritative, or historical file. Not accepted,
not adopted, not authoritative, not integrated into Master V10, the
Design and Wiring Map, Decision Defaults, or cursorrules. Authorizes no
implementation, code, patch-ready implementation, Cursor work, migration,
production store, schema serialization for production use, UI, runtime,
model change, tuning value, or live-disk action. No existing file was
modified, overwritten, renamed, moved, or deleted.

**Date:** July 12, 2026.

**Version note (v1_1):** narrow correction of v1_0 only, closing the
one IMPORTANT issue from ChatGPT's independent audit of the actual
v1_0 file: RM-AS-01 (§8) had selected `same_thread_or_group` and
`within_declared_time_range` as context gates "identifying
present-context support" and let passing them assign the
**current situation** label. That was unsafe and structurally
inconsistent with the settled design: a required §7R gate is
categorical — every failing candidate is excluded — which would have
categorically excluded permitted labeled historical support from the
Action Surfacing pool; and neither shared-thread membership nor
presence inside a configured time range proves that an item describes
what is happening now (a message may belong to the current thread and
still be old; a time-range setting is not proof the described event
remains current). v1_1 makes `object_type_matches` the **only**
required categorical gate for the Action Surfacing support pool and
makes the current-situation label something RM-AS-01 **consumes from
honestly grounded present-context provenance** under the already
accepted Bundle 2 §10.1/§11 and Context Retrieval rules — never
something a gate assigns; thread and time facts remain only structural
and temporal dimensions and provenance. Dependent wording in §8
items 4, 5, 10, 11, 12, and 13, the §12 RM-AS-01 table row, §15
check 5, and §16 was aligned to the one consistent rule. **No other
declaration, meaning, boundary, or open item changed.** v1_0 (SHA-256
`23844b87e26b7b01a9e21060b5f003edc3466f0b18889d268c9db1146d48dd99`;
1,068 lines; 66,508 bytes) is preserved unchanged as historical
candidate provenance.

**Package scope:** Bundle 2 (A4 / B1 / B26 / B-INT-1 per the accepted
eight-bundle plan) — the five formal per-component Tier 1/Tier 2
relevance declarations for the five settled §7R consumers, plus their
shared rules and the no-loss consistency mapping. Nothing outside
Bundle 2 is closed or biased.

**Disk-evidence note (flagged for the independent audit, §11):** the
governing task instruction for this candidate described the
manual-reread mechanical compatibility package as still open. At the
pinned repository snapshot used for this candidate (commit
`5108f575a411f90177b8f0f4d07028833713f3c5`), that package exists as a
**separately accepted standalone design**:
`NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md` with its own
`PACKAGE_COMPLETE` closure record dated July 12, 2026 carrying Ness's
exact acceptance statement. Following the governing rule that Ness's
later explicit acceptance supersedes stale status wording, §11 records
that seam disk-accurately, **by reference only**. This candidate does
not design, solve, close, reopen, rename, absorb, extend, or bias that
package, and it does not extend the three-case scope of the accepted
A25→B10 connection receipt.

**Intended repository placement:** `05_ACTIVE_CANDIDATE/`
(the physical move into the repository is Ness's action).

## 1. GOVERNING AUTHORITY ORDER

1. `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`
   (adopted by Ness June 29, 2026; governing — the standing adoption
   correction applies: any stale wording saying Master V10 is not
   adopted is superseded; Master V10 wins every conflict)
2. `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`
3. `01_AUTHORITATIVE/cursorrules`
4. `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`

The Design and Wiring Map v1.6 is subordinate working material only.

## 2. SOURCES READ — IDENTITIES RECALCULATED BEFORE WRITING

All repository files were read from one pinned snapshot of
`nesgeva/NH-GOVERNANCE`, branch `main`, commit
`5108f575a411f90177b8f0f4d07028833713f3c5`, byte-verified with
`sha256sum`, `wc -l`, `wc -c` on July 12, 2026, before any writing.

| Source (path abbreviated) | SHA-256 (first 8) | Lines / bytes | Read scope |
|---|---|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | `2d9ed4c6` | 5,736 / 506,934 | §§0, 0A, 0B, 7D, 7F, 7H, 7M, 7N, 7O, 7P, 7Q, 7R read in full; full section-header map verified |
| `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | `6cd09329` | 314 / 37,048 | Full |
| `01_AUTHORITATIVE/cursorrules` | `5050d088` | 717 / 34,821 | Targeted (design-phase and protection rules) |
| `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | `cdcc6134` | 5,580 / 465,376 | Targeted (Part I governance and working roles in full; archived §7R consolidation blocks; structure map) |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | `33af648d` | 899 / 286,256 | Targeted (C-7F, C-7R, C-7H, C-7M, C-7D, C-7N, C-7O, C-24, C-AFFIRM, A4, A6, A8, B-INT-1 entries and revision note in full) |
| `03_WORKFLOW/NH_REPLACEMENT_EIGHT_BUNDLE_DEPENDENCY_PLAN_v1_0_CANDIDATE.md` | `2d6483d1` | 467 / 17,274 | Full |
| `05_ACTIVE_CANDIDATE/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md` (accepted) | `c754b27e` | 391 / 20,476 | Full |
| `04_ACCEPTED…/NH_A4_…_ACCEPTANCE_RECORD_v1_0.md` | `f9d3fe04` | 152 / 7,051 | Acceptance content verified |
| `05_ACTIVE_CANDIDATE/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md` (accepted) | `da0aa4d2` | 393 / 19,696 | Full |
| `04_ACCEPTED…/NH_B1_…_ACCEPTANCE_RECORD_v1_0.md` | `6c21ea02` | 161 / 7,372 | Acceptance content verified |
| `05_ACTIVE_CANDIDATE/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_v1_0_CANDIDATE.md` (accepted) | `9c761e59` | 664 / 37,228 | Full |
| `04_ACCEPTED…/NH_BUNDLE_2_…_ACCEPTANCE_RECORD_v1_0.md` | `0b2f0ecf` | 149 / 7,200 | Acceptance content verified |
| `04_ACCEPTED…/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md` (accepted) | `8a50a862` | 257 / 13,849 | Full |
| `04_ACCEPTED…/NH_A25_…_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | `c640d367` | 158 / 7,135 | Status content verified |
| `04_ACCEPTED…/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md` (accepted) | `b5869d85` | 432 / 26,233 | Full |
| `04_ACCEPTED…/NH_A25_TO_B10_…_CLOSURE_RECORD_v1_1.md` | `87f76711` | 318 / 16,980 | Full — read and left unchanged |
| `04_ACCEPTED…/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md` (accepted) | `a0912880` | 430 / 26,025 | Full |
| `04_ACCEPTED…/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_…_CLOSURE_RECORD_v1_0.md` | `2b03cc7f` | 190 / 8,538 | Full (through §4 acceptance statement; remainder scanned) |
| `04_ACCEPTED…/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md` (accepted) | `215b7484` | 329 / 23,681 | Full |
| `04_ACCEPTED…/NH_B10_…_CLOSURE_RECORD_v1_0.md` | `da62a1e8` | 134 / 6,523 | Status content verified |
| `04_ACCEPTED…/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md` (accepted) | `e8f4c3de` | 1,192 / 72,543 | Targeted (§0 status and version notes, §3 Ness values, §18 opens, section map) |
| `04_ACCEPTED…/NH_B9_RETRY_VALUES_…_CLOSURE_RECORD_v1_0.md` | `d401d8c5` | 197 / 9,297 | Status and acceptance content verified |
| `05_ACTIVE_CANDIDATE/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md` (accepted) | `3566cf0f` | 685 / 39,950 | Targeted (§11 B3 theme/retrieval seam in full; §21 opens in full; section map) — read only to preserve its theme/retrieval seam |
| `04_ACCEPTED…/NH_BUNDLE_3_…_ACCEPTANCE_RECORD_v1_0.md` | `405717e5` | 149 / 6,267 | Acceptance content verified |
| `05_ACTIVE_CANDIDATE/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` (accepted) | `0c9a2011` | 1,399 / 84,568 | Targeted (§4 decision ledger in full incl. A6-10; §8 B5 profile/snapshot; §11 B-INT-9; §15 opens) — read to avoid conflicting with its accepted seams |
| `04_ACCEPTED…/NH_BUNDLE_4_…_ACCEPTANCE_RECORD_v1_0.md` | `ef561aa5` | 260 / 10,049 | Acceptance content verified (accepted July 11, 2026) |
| Project file `NH_DECISION_PACKAGE_LIVE_DUAL_MODEL_HANDOFF_v1.md` (upload suffix `__2_` is an upload artifact) | — (read from project copy) | 207 lines | Full — Ness-approved standalone concept; checked for conflict with the independent-validation boundary; none found; consumed by reference only in §5.4 |
| `NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_0_CANDIDATE.md` (this candidate's base; read from the delivered working copy — placement is Ness's action) | `23844b87` | 1,068 / 66,508 | Full — identity recalculated and matched exactly before correction; preserved unchanged as historical candidate provenance |

**Honest sourcing note:** "Targeted" reads above are reads of the actual
file on disk limited to the named sections; no summary was substituted
for an available file. Every identity in this table was recalculated
from the pinned snapshot immediately before writing. For v1_1, the four
governing files and the accepted packages named above were re-verified
byte-identical against the same pinned snapshot (commit `5108f575…`)
before the correction was applied, and the settled anchors for this
correction were re-read on disk: Master §7R Decision 1 (a candidate
failing any required gate is excluded; gates are categorical) and
accepted Bundle 2 §10.1/§11 (the positional channel feeds
**current situation**; current situation is material from what is
happening now and is the only label that can satisfy current support
required).

## 3. PURPOSE AND SCOPE

**What this candidate is.** The formal authoring step the accepted
Bundle 2 package reserved: the five concrete per-component Tier 1 /
Tier 2 relevance declarations — one for each settled §7R consumer —
written against the settled §7R contract, the accepted A4 eight-field
declaration policy, the accepted B1 retrieval structure, the accepted
B26 failure design, and the accepted B-INT-1 design-level
instantiation, using **only** vocabulary already settled in Master §7R.
It also mechanically expresses the shared uncertainty rule for
mouth-produced interpretation and records the A25→B10 boundary and the
manual-reread seam disk-accurately, by reference.

**What this candidate settles:** the declaration **content** for the
five consumers, at candidate level, pending audit and acceptance.

**What this candidate does not do:** it invents no purpose type, gate
condition, dimension, evidence meaning, score, threshold, budget, time
span, ceiling value, model choice, benchmark value, or private
definition of "relevant"; it redesigns nothing settled in §7R, A4, B1,
B26, B-INT-1, A25, B9, B10, Bundle 1, Bundle 3, Bundle 4, the accepted
A25→B10 connection, or the accepted manual-reread compatibility
package; it performs no wiring, integration, serialization,
implementation, or runtime work; it turns Ness into no approval gate;
it marks nothing accepted, adopted, authoritative, implemented, or
package-complete.

## 4. NESS-APPROVED MEANING — CARRIED VERBATIM; PRESERVED IN EVERY DECLARATION

**Verbatim decision block (preserved exactly as carried in the task
instruction):**

> - N.H is one continuous reader. Ness is not a clerk and does not
>   approve each reading, memory, theme, pattern, link, search, or
>   relevance decision one by one.
> - N.H automatically notices possible patterns and meaning-connections,
>   checks them, uses them where useful, keeps them revisable, and
>   records what it did.
> - N.H may use an uncertain possible connection quietly when it only
>   helps internal searching, context selection, understanding, or
>   preparation of a response.
> - N.H does not need to interrupt Ness by explaining every small
>   internal connection.
> - When an uncertain connection materially changes a claim,
>   interpretation, recommendation, withholding decision, action
>   possibility, or conclusion shown to Ness, N.H must make the
>   uncertainty clear.
> - An uncertain connection is never proof, truth, causation, authority,
>   current-state evidence, access permission, or Ness's judgment.
> - Old or weak material may support a gentle protective possibility. An
>   active or outward suggestion additionally requires current-situation
>   support.
> - N.H records gaps and informs Ness when useful. It does not stop and
>   turn the gap into work Ness must manually complete.
> - The Log is for inspection and understanding, not an approval queue.

**Normalized statements (no new meaning added; each is carried into the
declarations below):**
1. **Automatic, quiet, recorded:** relevance evaluations, pattern
   noticing, and connection-guided searching run automatically under
   their declarations; no per-judgment Ness approval exists; everything
   logs (§0B); the Log is inspection, never a queue.
2. **Quiet internal use is permitted** for searching, context selection,
   understanding, and response preparation; small internal connections
   are not narrated to Ness.
3. **Material-uncertainty disclosure:** only when an uncertain
   connection materially changes a visible claim, interpretation,
   recommendation, withholding decision, action possibility, or
   conclusion is the uncertainty made clear — under the surfacing rules
   of the component that owns the visible result.
4. **Never promoted:** an uncertain connection is never proof, truth,
   causation, authority, current-state evidence, access permission, or
   Ness's judgment. This is the accepted §24 rule and the §7R
   RELEVANCE-IS-NOT rule, consumed unchanged.
5. **Action asymmetry:** old or weak material may support only gentle
   protective possibilities; active or outward possibilities
   additionally require current-situation support (accepted Bundle 2
   §7 decisions 8–9, consumed unchanged).
6. **Gaps are recorded, not delegated:** N.H records gaps and informs
   Ness when useful; it does not stop and hand Ness manual completion
   work. Fail-closed stops (§5.7) are honest halts of the affected
   operation, never a demand that Ness operate the machinery.

## 5. SHARED DECLARATION FRAMEWORK

### 5.1 Declaration structure and identifiers

Each declaration below is one A4-valid eight-field declaration
(accepted A4 §3) expressed against the settled §7R two-tier contract
(Master §7R Decision 4). Field names and identifiers introduced here
are **[proposed]** candidate-level mechanical carriage; exact
serialization and final naming are confirmed at B-INT-1's
implementation-facing step without changing meaning (same rule as
accepted B1 §2).

- **Declaration / Tier-1 mode identity [proposed]:** `RM-CR-01`,
  `RM-CV-01`, `RM-AS-01`, `RM-RR-01`, `RM-LS-01`, each with
  `declaration_version = v1_0`. The declaration identity and the §7R
  Tier-1 mode identity are the same identifier at this level. Any later
  change creates a new version through the settled Decision-5
  proposal-and-confirmation path; prior versions are preserved,
  append-only, never silently edited.
- **Tier 1** of each declaration (identity, purpose, consuming
  component, candidate/target object types, gate conditions with
  producers, graded dimensions with producers, mouth authorization,
  evaluation timing) is owned and validated by Attention and Relevance
  Control. **Tier 2** (ordering, fallback, surfacing,
  unresolved-dimension handling, strictness consequences) is owned and
  validated by the consuming component. Neither silently takes
  ownership of the other tier.
- **Validity (accepted A4 rule, binding):** a declaration missing any
  required field is not valid; a component without a valid declaration
  for the current purpose has no relevance mode to run and follows the
  fail-closed path (§5.7) rather than improvising one.
- An **unrecognized purpose type** follows Master §7R Decision 14
  exactly: halt, identify the unknown value and vocabulary version,
  preserve the original request, explain plainly, offer mapping or a
  new-type proposal through Decision 5 — never guess silently.

### 5.2 Producers — settled §7R Decision 2, consumed unchanged

- **Deterministic rules** produce every context-gate condition (gates
  remain deterministic, always) and the deterministic dimensions.
- **The embedding model** (`all-MiniLM-L6-v2` per the settled
  vocabulary) produces `semantic_similarity` only.
- **The mouth model** is a producer **role** under §7R Decision 2. Its
  current test model on disk is `dolphin-llama3`; the final adopted
  mouth and the final Interactive Translator remain UNDECIDED (Defaults
  §3F) and are not chosen here. **No declaration in this candidate
  authorizes any mouth-produced relevance dimension (§5.3).**
- Every dimension value preserves its producer, rule version or model
  version, index or prompt version as applicable, and the value
  produced.

### 5.3 Mouth authorization and the shared uncertainty rule — `T2-UNRES-SHARED v1_0` [proposed]

**Mouth authorization in all five v1_0 declarations: none declared.**
The settled nine-dimension shared vocabulary assigns every dimension a
deterministic-rule or embedding-model producer; no settled shared
dimension is mouth-produced, and this candidate invents no new
dimension. The mouth-authorization field is therefore present in every
declaration with the explicit value **none** — never one broad
mouth-allowed flag, and never an omission. Any future mouth-produced
interpretive dimension for a consumer requires: a new declaration
version through Decision 5; the dimension and its contexts specifically
named; the Decision-10 Tier-2 unresolved-handling reference (identifier
and version) carried in Tier 1; and the settled Decision-6 validation.
Mouth-produced dimensions may never act as context-gate conditions, may
never self-approve, and may not be precomputed unless explicitly
declared with a designed independent-validation mechanism — all settled
rules, consumed unchanged.

**The shared uncertainty rule** — referenced by every declaration as
its Tier-2 unresolved-dimension handling rule, and pre-binding the
handling of any future mouth-produced dimension — mechanically
expresses the following, adding no new meaning:

- **`validated`** — the value may be used according to the relevant
  declaration, while remaining interpretation rather than fact.
  Validated means only that no rule-detectable error was found; it
  never means substantively correct (Decision 6, unchanged).
- **`failed`** — the value is not used as a relevance result.
- **`unresolved`, or a producer/validator disagreement** — the value
  may remain a **weak internal clue** for searching and understanding
  when the declaration permits it; it must remain labeled and logged.
- An unresolved or disputed result **cannot by itself**: support a
  factual claim; satisfy current-situation support; change Living
  State; cause an actual reread; authorize an active suggestion; widen
  access; or grant authority.
- It **may** prompt further checking, retrieval, or evaluation.
- When its uncertainty **materially changes a visible result**, the
  uncertainty must be made clear to Ness under the owning component's
  surfacing rules (§4 statement 3).
- A disagreement is recorded through the settled Decision-11
  disagreement record and handled through the declared uncertainty
  behavior; N.H never silently selects the result with greater model
  confidence.
- **Inapplicable or unproducible values are honest, never coerced:**
  where a settled dimension does not apply to a candidate's object type
  or its input is missing, the outcome is recorded with the settled
  §0A absence vocabulary (`not_applicable` / `not_evaluated` /
  `collection_failed` and so on) — never invented, never a silent
  blank, never converted into a relevance signal.

### 5.4 Independent-validation boundary — preserved, not expanded

The Master-required boundary stands unchanged: required deterministic
validation with six checks and three outcomes for any mouth-produced
dimension; **optional** model-based validation only where a declaration
specifically requires it, with the validator named, the reason stated,
and meaningful independence declared; the second validator is never
final authority. **No mandatory second AI model is created by this
candidate**, and none of the five declarations requires one. The exact
future validator model, provider, program, and implementation mechanism
remain open. The Ness-approved standalone live dual-model handoff
concept (heavy background analyst / light live carrier, July 1, 2026)
was read and does not conflict: it governs the live speaking
architecture, chooses no validator, and leaves exact model candidates
open; it is consumed by reference only and is neither integrated nor
modified here.

### 5.5 Ordering and access — settled, unbypassable

- **§7Q before §7R, always:** §7Q purpose-specific authorization runs
  before Attention and Relevance Control receives any candidate —
  internal-use authorization for internal purposes, visible-output
  eligibility for visible purposes. §7R operates only on
  already-authorized material and never owns, reruns, or redefines §7Q.
- **Visible-output order:** §7Q first, SACL second (accepted B24 §6.5),
  unchanged; a relevance judgment never substitutes for, reorders, or
  weakens either gate.
- **Declarations never widen access:** every allowed-use boundary below
  narrows use only; no mode, gate, dimension, reason, or uncertainty
  rule makes ineligible material eligible, reveals withheld material,
  or signals that withheld material exists.
- Privacy and deletion eligibility remain external prerequisites, never
  gate conditions owned by §7R.

### 5.6 Shared logging and audit (§0B)

- Every completed relevance evaluation produces one append-only
  **relevance event record** with the full settled Decision-12 field
  set; every producer/validator disagreement produces one settled
  Decision-11 **disagreement record**; both are never rewritten.
- One real operation, one log; logs are never truth evidence;
  repetition adds no certainty; derived material is never independent
  evidence for the interpretation that produced it; no double evidence.
- Declarations themselves are versioned, append-only records; every
  evaluation records the declaration identity and version used.
- Ness's relationship is the settled Decision 5, unchanged:
  unrestricted inspection of any judgment and its full Tier 1/Tier 2
  configuration; direct lightweight per-judgment correction as a
  separate linked Ness response event; context-scoped recorded
  per-judgment override; reusable changes only through
  consequence-preview and confirmation with a new version; Decision-13
  pattern observation exactly as settled. None of this makes Ness an
  operational gate: inspection and correction are always available and
  never required.
- All records obey §7Q access and authorization rules and §25
  identity/security authorization where applicable; the Log surface
  stays look-don't-touch; nothing operates silently.

### 5.7 Shared fail-closed behavior

When relevance cannot be safely determined — an unrecognized purpose
type, a missing or invalid declaration, an evaluation that cannot
complete, or a disagreement the declared rules cannot resolve — the
owning component follows the governed honest path (accepted A4 §5):
say so through the settled records; halt or proceed explicitly degraded
according to the owning component's settled rules; mark the outcome
honestly (degraded / context-limited / insufficient); never a silent
guess, never a silently lowered threshold, never substituted unrelated
material, never a pretended success. Retrieval **system failure**
follows accepted B26 exactly (accepted Bundle 2 §8): bounded retry
under accepted B9 mechanics with the Ness-decided values by reference;
then stop safely, commit the terminal failure state, state the reason,
keep the record, save the unfinished state for the real-change
exception; **no degraded continuation after exhausted retry** absent a
separate later Ness-approved rule. A genuine **empty** result is a
normal condition, never a failure: proceed bare, marked
context-limited/revisable.

---

## 6. DECLARATION RM-CR-01 — CONTEXT RETRIEVAL

1. **Identity and version [proposed]:** `RM-CR-01`, `v1_0`.
2. **Consuming component:** Context Retrieval (§7F / map C-7F), running
   under the accepted B1 parameter architecture.
3. **Purpose type (settled):** `retrieval_context_selection`. Optional
   label: "selecting context for a reading pass" (no system behavior).
4. **Target and candidate object types:** target — the target root of
   the reading pass (with the mode's declared query representation
   where the B1 configuration declares one). Candidates — **roots**
   authorized by §7Q for the current internal purpose, reached through
   the two always-separate channels. Prior-reading context is not a
   candidate type of this mode: root evidence and prior-reading context
   stay separate (settled B10 §10 boundary, unchanged).
5. **Context-gate conditions (settled; deterministic):**
   - `object_type_matches` — both channels, always.
   - `same_thread_or_group` **and** `precedes_target_in_same_thread` —
     required for the **positional channel only**: positional material
     represents current-thread surroundings that actually preceded the
     target.
   - `within_declared_time_range` — applied only when the mode's B1
     configuration declares a time range (`time_range` slot; span value
     open).
   Gate selection is per channel; channel identity itself is retrieval
   **provenance**, never a gate or dimension (settled, unchanged).
6. **Graded dimensions (settled) and producers:**
   - `semantic_similarity` — embedding model — semantic channel.
   - `positional_distance` — deterministic rule — positional channel.
   - `temporal_distance` — deterministic rule.
   - `explicit_links` — deterministic rule — already-recorded
     structural links only (same Person-Box, same confirmed theme, same
     proposed theme, same `derived_from` chain, shared root IDs in a
     telling).
   - `ness_response_links` — deterministic rule.
   - `active_clash_links` — deterministic rule — clashes surfaced,
     never resolved.
   Not selected (honest applicability): `currentness_status`,
   `proposal_acceptance_outcome`, `reading_context_status` — candidates
   of this mode are roots, and those dimensions apply only to state-node
   or reading candidates. Nothing is renamed or redefined.
7. **Mouth authorization:** **none** (§5.3).
8. **Evaluation timing; trigger and invalidation:** on demand only —
   requested by the reading pass at RR-equivalent context-assembly time
   through LMAC. No triggered pre-computation is declared in v1_0;
   therefore no precompute triggers or invalidating events exist for
   this mode. Declaring pre-computation later requires a new version
   with declared triggers and invalidators.
9. **Reason for the mode:** the reading pass must not be blind; §7A R4
   requires wide context; this mode selects permitted, purpose-relevant
   roots per channel under B1's structure so the engine sees what
   surrounds and what may relate to the target — without merging the
   two kinds of claim.
10. **Tier 2 — ordering, fallback, surfacing, unresolved handling:**
    - *Ordering:* per channel, by the mode's B1
      `ranking_or_threshold_rule` reference (rule content and every
      threshold value open; a threshold is never lowered silently — a
      change is a new configuration version). Positional ordering is
      positional; semantic ordering is similarity-based; the channels
      are never jointly ranked. Effective quantities are always the
      minimum of the mode's B1 settings and its referenced ceiling set
      (all values open).
    - *Pattern and theme influence (Ness-approved meaning, applied):*
      possible patterns and meaning-connections may guide searching
      **automatically**, without manual Ness approval. Proposed or
      uncertain themes may guide internal retrieval **only as weak,
      revisable clues** — mechanically: through the `explicit_links`
      dimension's recorded proposed-theme link type and through
      semantic search; below-threshold or uncertain matches are
      supplied only where the mode's configuration allows, always
      carried with the accepted Bundle 2 §11 strength labels
      (maybe related / weak echo / one similar old memory / older
      pattern), never as proof. **Every theme or pattern influence on
      retrieval is logged** in the B1 audit record's why-admitted
      provenance slot (the accepted Bundle 3 §11 audit-trail honesty
      rule, satisfied unchanged). A proposed, uncertain, or confirmed
      theme never proves a connection and never silently becomes an
      accepted structural link — connection acceptance stays with the
      settled §24 routes only.
    - *Fallback:* genuine empty result → proceed bare, target-only,
      marked context-limited/revisable (normal condition). Technical
      system failure → accepted B26 and B9 by reference: bounded retry,
      then stop safely, preserve the work, never pretend success; no
      degraded continuation after exhausted retry (§5.7).
    - *Surfacing:* none — retrieval talks to no one; strength/status
      labels and channel provenance ride with the supplied items so
      downstream surfaces can obey their own rules.
    - *Unresolved handling:* `T2-UNRES-SHARED v1_0` (§5.3).
11. **Allowed-use boundary:** only §7Q-authorized roots within the B1
    `eligible_source_scope` of the running mode; scope narrows use
    only; positional and semantic material never merge; the supplied
    package is used only for the requesting reading pass; retrieval
    presence is never evidence of truth or connection.
12. **Logging and audit:** one Decision-12 relevance event record per
    evaluation, plus the one B1 per-run append-only audit record
    (channels queried separately; parameters applied; every ceiling
    enforcement; exact roots supplied per channel with per-item
    why-admitted provenance including any theme/pattern influence;
    exclusions and truncation; empty-vs-failure marker; downstream
    reading audit-trail pointer). Failure attempts add B26 failure
    records bound to the same operation identity.
13. **Fail-closed:** invalid or missing declaration or B1
    configuration, ceiling violation, or unauthorized candidate → the
    mode does not run (accepted B1 validity rule); unrecognized purpose
    → Decision-14 halt; system failure → §5.7. Never merge channels;
    never let semantic override or repair positional; never lower
    thresholds silently; never substitute unrelated material; never
    claim success on failure.

## 7. DECLARATION RM-CV-01 — COMPUTED VIEW

1. **Identity and version [proposed]:** `RM-CV-01`, `v1_0`.
2. **Consuming component:** Computed View (§7M / map C-7M / accepted
   Bundle 4 B5).
3. **Purpose type (settled):** `view_assembly`. Optional label:
   "assembling the internal current picture for a view profile."
4. **Target and candidate object types:** target — the view profile's
   declared purpose / current question (the B5 ordering-profile
   instance requesting assembly). Candidates — objects of the
   Master-permitted §7M source families, linked never copied: roots,
   readings, tellings, clash records, Ness response events, Person-Box
   links, themes, Living State references, world-model references, and
   **metadata-only** pre-ingest references (safe source-carried
   metadata, lifecycle state, blocker information only — held raw
   content never influences assembly; no TSC inspection path exists or
   may be introduced).
5. **Context-gate conditions (settled; deterministic):**
   `object_type_matches` — against the profile's declared eligible
   source families; `within_declared_time_range` — only when the
   profile declares a range (value open). Not selected:
   `same_thread_or_group`, `precedes_target_in_same_thread` (assembly
   is not thread-adjacency-bound).
6. **Graded dimensions (settled) and producers:** all nine settled
   dimensions are selected, each strictly within its settled
   applicability: `semantic_similarity` (embedding model);
   `temporal_distance`, `positional_distance` (where candidate and a
   thread-bound reference share a thread), `currentness_status`
   (state-node candidates only — carries the recorded §7D status,
   never relevance strength), `explicit_links`, `ness_response_links`,
   `proposal_acceptance_outcome` (reading candidates only),
   `reading_context_status` (accepted-reading candidates only),
   `active_clash_links` — all deterministic rules. Inapplicable
   combinations record the honest §0A absence outcome (§5.3), never a
   coerced value.
7. **Mouth authorization:** **none** (§5.3).
8. **Evaluation timing; trigger and invalidation:** on demand, at the
   settled §7M update triggers only (Ness opens the view; Ness requests
   a refresh; a materially relevant event as the profile defines) — the
   consuming component's settled triggers, not §7R pre-computation. No
   triggered pre-computation is declared; no continuous recomputation
   exists.
9. **Reason for the mode:** §7M's seven-factor ordering needs a defined
   form for factor 4 ("relevance to the current question or view
   purpose"); this mode supplies exactly that, so the internal picture
   is assembled from broadly permitted current and older material
   without any hidden score.
10. **Tier 2 — ordering, fallback, surfacing, unresolved handling:**
    - *Ordering:* the settled seven-factor order, fixed and never
      silently reordered, disclosed per B5 ordering profile; this
      mode's judgments feed **factor 4 only**; every factor's outcome
      is recorded separately; no collapsed score; direct root support
      outranks repetition, frequency, or model confidence; recency is a
      tie-breaker only. All uncertainty, changed-pattern, and
      source-strength labels (accepted Bundle 2 §11) remain attached to
      view entries; an entry resting on an older pattern stays marked
      so; nothing hardens into fact.
    - *Fallback:* an assembly that cannot complete honestly is marked
      incomplete; "no clear current view" is a valid outcome; a failed
      update keeps the last valid snapshot marked possibly stale; a
      null update is valid; no silent gap-filling.
    - *Surfacing:* **none unprompted — internal tool only.** Quiet
      internal use requires no Ness approval. The Computed View never
      volunteers its whole internal picture merely because it exists,
      never narrates internal knowledge back, and is shown only when
      Ness deliberately asks; when a **downstream visible result**
      materially relies on uncertain material carried through the view,
      that downstream result discloses the uncertainty under its own
      surface rules (§4 statement 3) — the view itself stays silent.
    - *Unresolved handling:* `T2-UNRES-SHARED v1_0` (§5.3).
11. **Allowed-use boundary:** §7Q internal-use-authorized material of
    the permitted families only, within the profile's declared
    eligibility; assembly output informs responses internally; the
    Computed View is never evidence for itself, never launders an
    interpretation into fact, never becomes an input to §7D (accepted
    B-INT-9 direction, unchanged), and never widens access.
12. **Logging and audit:** one Decision-12 relevance event record per
    assembly evaluation; the B5 snapshot and refresh/status event
    records carry the profile identity and version, the Tier-1
    reference (this declaration), source references by ID,
    factor-by-factor outcomes, omissions with reasons, and honest
    completeness status — append-only, immutable, never rewritten.
13. **Fail-closed:** missing/invalid/stale/unauthorized profile or
    declaration → no snapshot; the applicable failed/incomplete
    refresh-status event is created instead (accepted B5 rule);
    unrecognized purpose → Decision-14 halt; never rewrite, merge,
    delete, or suppress any underlying object; never select one reading
    as authoritative; never surface unprompted.

## 8. DECLARATION RM-AS-01 — ACTION SURFACING

1. **Identity and version [proposed]:** `RM-AS-01`, `v1_0`.
2. **Consuming component:** Action Surfacing (§7N / map C-7N), under
   §7P authority, with accepted Bundle 4 A8/B8/B27 by reference.
3. **Purpose type (settled):** `action_surfacing`. Optional label:
   "evaluating support for surfacing a possible action."
4. **Target and candidate object types:** target — the candidate
   possibility being considered for surfacing (the situation-purpose of
   the surfacing pass). Candidates — the potential support-evidence
   objects: roots (both live/present-context material and permitted
   historical material, distinguished only by their provenance and
   labels per item 5), readings, tellings, clash records, Ness response
   events, and Living State references (state, open-loop, value,
   constraint evidence per §7N).
5. **Context-gate conditions (settled; deterministic):**
   `object_type_matches` — the **only required categorical gate** for
   the Action Surfacing support pool, so that permitted labeled
   historical support (older pattern / one similar old memory / weak
   echo / maybe related) remains eligible for the pool rather than
   being categorically excluded. Not selected as gates:
   `same_thread_or_group`, `precedes_target_in_same_thread`, and
   `within_declared_time_range` — a required §7R gate is categorical
   and excludes every failing candidate, and neither shared-thread
   membership nor presence inside a configured time range proves that
   an item describes what is happening now; those structural and
   temporal facts remain available only as the settled graded
   dimensions (`positional_distance`, `temporal_distance`) and as
   retrieval provenance, and they never assign any label by
   themselves. **Current-situation labeling — consumed, never
   gate-derived (no new meaning):** a support item carries the
   **current situation** label (accepted Bundle 2 §11) only when it
   arrives with honestly grounded present-context provenance under the
   already accepted rules — actual live/present material of the
   ongoing exchange, or current positional context from the positional
   channel (accepted Bundle 2 §10.1: current thread adjacency feeds
   **current situation**; accepted B1 channel provenance).
   Same-thread membership alone is insufficient — a message may belong
   to the current thread and still be old. Falling inside a configured
   time range alone is insufficient — a time-range setting is not
   proof that the described event remains current. Where
   current-situation provenance is absent, unclear, disputed, or only
   inferred from thread membership or time distance, the item keeps
   its historical or uncertain label and **must not** satisfy
   **current support required**. All other support carries its
   older-pattern / one-similar-old-memory / weak-echo / maybe-related
   strength label. Only current-situation-labeled support can satisfy
   **current support required**.
6. **Graded dimensions (settled) and producers:**
   `semantic_similarity` (embedding model); `temporal_distance`,
   `positional_distance` (thread-shared support), `currentness_status`
   (state-node support only — old patterns are never auto-current;
   the changed/replaced §7D statuses feed the accepted
   newer-evidence-may-have-changed/replaced labels),
   `explicit_links`, `ness_response_links` (prior
   accept/reject/postpone/ignore events — feeding the settled
   no-resurface and gentle-question rules), `proposal_acceptance_outcome`
   and `reading_context_status` (reading support only — weak or
   insufficient support detection), `active_clash_links` (conflicted
   support) — all deterministic rules.
7. **Mouth authorization:** **none** (§5.3).
8. **Evaluation timing; trigger and invalidation:** on demand — at an
   explicit Ness request (always permitted), or on the proactive path
   only as the explicitly authorized relevance rule §7N requires, whose
   defined form this declaration is; proactive surfacing remains
   controllable and disablable by Ness's settings. No §7R
   pre-computation is declared.
9. **Reason for the mode:** a surfaced possibility must be honest about
   what it stands on; this mode evaluates and labels the support base
   so protective and active possibilities meet their different, settled
   evidence standards.
10. **Tier 2 — ordering, fallback, surfacing, unresolved handling:**
    - *Strictness split (Ness's decision, binding, unchanged) — two
      support lanes, both preserved:* **protective possibilities**
      (pause, wait, take space, do not answer yet — gentle, low-impact,
      reversible) may rest on old or weak support. **Active or outward
      possibilities** (send this message, confront someone, make a
      plan, change a relationship step, take an external action)
      require **genuinely current-situation support** — items carrying
      the current situation label on honestly grounded present-context
      provenance per item 5 — **in addition to** any history. Labeled
      historical or uncertain support (older pattern / one similar old
      memory / weak echo / maybe related / changed / replaced) remains
      fully available for protective possibilities and as labeled
      supplementary support beside genuine current support, but it
      never counts toward **current support required**. An uncertain
      connection alone never satisfies current support (§5.3); support
      whose currency is only inferred from thread membership or time
      distance never satisfies it either (item 5). An unclear support
      base downgrades the possibility toward protective or withholds
      it.
    - *Ordering:* support items are used per their labels; no hidden
      score; higher-impact possibilities need stronger review and
      permission per §7P (by reference; the A8 category-to-risk mapping
      is accepted Bundle 4 territory, unchanged).
    - *Fallback:* weak, conflicted, stale, or insufficient support →
      withhold or clearly label uncertain; retrieval failure → no
      invented support, and possibilities that would have needed the
      failed context are not surfaced.
    - *Surfacing:* the **main answer stays simple and clean and never
      overstates certainty**; when a possibility's support includes
      old, weak, maybe-related, changed, or replaced material, the
      warning lives in the **side-drawer note** (accepted
      supplementary-note meaning; visual/interaction mechanics open),
      naming the support kind; the drawer states that weak echoes are
      not strong evidence; normal chat uses simple wording ("maybe
      related"), the drawer may use the precise label ("weak echo").
      Possibilities, never instructions; required/prohibited language
      per §7N; the gentle-question rule and every Ness-response state
      stand unchanged; suggesting, preparing, and executing remain
      separate; silence is never consent; §7P authority and
      confirmation rules are untouched.
    - *Unresolved handling:* `T2-UNRES-SHARED v1_0` (§5.3) — an
      unresolved result can never satisfy current support or authorize
      an active possibility.
11. **Allowed-use boundary:** §7Q-authorized support evidence for the
    surfacing purpose at hand only; the eligible pool includes
    permitted labeled historical material, and pool eligibility never
    implies currency; evaluation informs surfacing and labeling; it
    grants no permission to prepare or execute anything; relevance
    never substitutes for §7P authority; nothing here widens access or
    reveals withheld material.
12. **Logging and audit:** one Decision-12 relevance event record per
    evaluation; each surfaced possibility records its support items
    **with their labels** (accepted Bundle 2 §14) — including, for any
    item labeled current situation, the present-context provenance
    basis on which that label was consumed — its derivation, its
    assumptions, uncertainty, and risks; each gentle question and each
    Ness-response state is recorded per §7N.
13. **Fail-closed:** no valid declaration → nothing proactive is
    surfaced (explicit-request answers proceed only under the governed
    honest degraded path, saying so); no honestly grounded
    current-situation support per item 5 → no active or outward
    possibility, ever — withheld or downgraded to protective;
    escalating a protective framing into an active one via wording is a
    violation; unrecognized purpose → Decision-14 halt.

## 9. DECLARATION RM-RR-01 — REREAD

1. **Identity and version [proposed]:** `RM-RR-01`, `v1_0`.
2. **Consuming component:** Reread Lifecycle (§7H / map C-7H), with
   accepted A25, accepted B10, the accepted A25→B10 three-case
   connection, and the accepted manual-reread compatibility package all
   consumed by reference, unchanged (§11).
3. **Purpose type (settled):** `reread_trigger_evaluation`. Optional
   label: "evaluating whether materially relevant new information
   justifies a condition-based reread trigger."
4. **Target and candidate object types:** target — an existing old
   reading (by previous-reading IDs, with its root). Candidates — the
   new-information items of the settled §7H condition-based class: new
   roots / new root evidence, new positional context, resolved speaker
   or thread information, corrected provenance, newly available
   required context channels, and recorded Ness response events —
   referenced by identity.
5. **Context-gate conditions (settled; deterministic):**
   `object_type_matches` — always; `within_declared_time_range` — only
   when a range is declared (value open). Not selected:
   `same_thread_or_group`, `precedes_target_in_same_thread` — new
   information bearing on an old reading may come from anywhere; thread
   adjacency is carried as the `positional_distance` dimension where a
   thread is shared, not as an exclusion gate.
6. **Graded dimensions (settled) and producers:**
   `semantic_similarity` (embedding model); `temporal_distance`,
   `positional_distance` (candidate root vs the old reading's root
   within a shared thread — the "new positional context" condition made
   measurable), `explicit_links` (recorded `derived_from` chains,
   shared root IDs, theme links — recorded structural bearing),
   `ness_response_links`, `active_clash_links` (a recorded clash
   touching the old reading) — all deterministic rules. Not selected:
   `currentness_status`, `proposal_acceptance_outcome`,
   `reading_context_status` (candidates of this mode are
   new-information items, not state nodes or readings).
7. **Mouth authorization:** **none** (§5.3).
8. **Evaluation timing; trigger and invalidation:** on demand — when
   the settled §7H/B10 trigger machinery asks whether materially
   relevant new information exists for a **condition-based** trigger.
   No §7R pre-computation is declared. **This evaluation is not itself
   a trigger:** the settled trigger vocabulary (manual /
   condition_based / scheduled_automatic_retry / on_rejection) stands
   exactly as accepted; nothing here adds, removes, renames, or
   reclassifies a trigger.
9. **Reason for the mode:** §7H requires condition-based relevance to
   be established under an explicitly designed rule against the §7R
   contract; this declaration is that rule's declared form — informing
   whether a real, recordable condition-based reason may exist, and
   nothing more.
10. **Tier 2 — ordering, fallback, surfacing, unresolved handling:**
    - *Consequence rule:* weak or uncertain material **may prompt
      reread evaluation**; an actual reread requires a real recorded
      reason under the settled §7H record set and accepted B10
      mechanics — a relevance judgment never substitutes for a reason,
      and an unresolved relevance result alone never launches a reread.
      No blanket rereading, ever. Changed/replaced-pattern flags are
      natural candidates for evaluation — flagged, evaluated, never
      auto-applied.
    - *A25 boundary (accepted, unchanged):* the accepted `direct` and
      `wider-context` modes, tested independently, not mutually
      exclusive, with truthful dual assignment — nothing here produces,
      biases, or substitutes for an assignment. **The assignment
      producer remains open** (accepted connection §5, unchanged); this
      relevance mode is not that producer and supplies no assignment
      evidence. No false, third, empty, sentinel, or default assignment
      exists or is created.
    - *Manual path (settled, unchanged):* Ness may request a reread at
      any time; no further justification is required; N.H never waits
      for new information merely because the trigger is manual; the
      manual request event itself is the valid recorded trigger,
      initiator, and reason; Ness's request is **never** reinterpreted
      as evidence used to manufacture a direct or wider-context
      assignment. **This relevance mode plays no role on the manual
      path** — manual rereads require no relevance evaluation and are
      not gated by this declaration. Mode-slot mechanics for the manual
      path are the separately accepted compatibility package's, by
      reference only (§11).
    - *Fallback:* no real reason → no reread; an evaluation that cannot
      complete stops without scheduling anything.
    - *Surfacing:* none — lifecycle machinery; outputs are records.
    - *Unresolved handling:* `T2-UNRES-SHARED v1_0` (§5.3).
11. **Allowed-use boundary:** §7Q-authorized new-information items and
    the identified old reading only, for trigger evaluation only; the
    evaluation neither reads nor configures the reread pass's own
    context (that is RR2's settled §7Q → §7F → §7R sequence under
    accepted B10 and the accepted connection, unchanged); every reread
    still adds a new layer beside the old reading and never changes it.
12. **Logging and audit:** one Decision-12 relevance event record per
    evaluation; trigger, reason, mode-slot record, and decision logging
    remain B10's settled §0B set (trigger recorded, claim committed,
    snapshot, acceptance result, layer committed, single RR5 parent
    terminal), unchanged; the evaluation's record links to any trigger
    record it informed, by identity only — no double evidence.
13. **Fail-closed:** no valid declaration → condition-based evaluation
    does not run (the settled triggers themselves are untouched — the
    manual path in particular is never blocked by this declaration's
    absence); unrecognized purpose → Decision-14 halt; mode-slot
    conditions at RR2 fail closed exactly as the accepted connection
    §9 and the accepted compatibility package §9 define them, with
    B10's existing states, reason codes, and single RR5 parent
    terminals — consumed unchanged, not redesigned.

## 10. DECLARATION RM-LS-01 — LIVING STATE REVIEW

1. **Identity and version [proposed]:** `RM-LS-01`, `v1_0`.
2. **Consuming component:** Living State Web (§7D / map C-7D), under
   the accepted Bundle 4 A6 decisions (A6-10 in particular), consumed
   unchanged.
3. **Purpose type (settled):** `state_review_trigger_evaluation`.
   Optional label: "evaluating whether a relevance signal warrants
   triggering a currency review."
4. **Target and candidate object types:** target — a tracked Living
   State node (its currentness question). Candidates — authorized new
   or changed items bearing on it: roots, readings, tellings, clash
   records, Ness response events, and §7O result evidence — referenced
   by identity.
5. **Context-gate conditions (settled; deterministic):**
   `object_type_matches` — always; `within_declared_time_range` — only
   when declared (value open). Not selected: `same_thread_or_group`,
   `precedes_target_in_same_thread`.
6. **Graded dimensions (settled) and producers:**
   `semantic_similarity` (embedding model); `temporal_distance`,
   `positional_distance` (where thread-shared), `explicit_links`,
   `ness_response_links`, `active_clash_links` — deterministic rules.
   **Deliberately not selected: `currentness_status`.** Selecting the
   reviewed node's recorded currentness into the judgment that may
   trigger its own currency review would place the prohibited
   `currentness → relevance → currency → currentness` circle inside one
   mode; leaving the dimension unselected keeps the settled Decision-8
   prohibition structurally unreachable here. This is a selection from
   the settled vocabulary, not a change to it.
7. **Mouth authorization:** **none** (§5.3).
8. **Evaluation timing; trigger and invalidation:** on demand — when
   authorized materially relevant new or changed material appears
   (accepted A6-10's inherited automatic review trigger), or when the
   §7D machinery requests an evaluation. No §7R pre-computation is
   declared. Which relevance events are authorized to initiate an
   actual review remains the Living State Web's own settled open rule
   (A6 trigger-authorization territory) — not decided here.
9. **Reason for the mode:** §7D needs a declared, auditable form for
   "a relevance signal warrants a currency review"; this mode supplies
   it — the doorbell, never the evidence.
10. **Tier 2 — ordering, fallback, surfacing, unresolved handling:**
    - *Consequence rule (settled, unchanged):* relevance only **rings
      the doorbell**. A relevance event may trigger a review; it is
      never state evidence and never changes Living State directly; the
      review inspects permitted evidence under §7D's own rules;
      currentness is decided from permitted source evidence under §7D
      and the accepted A6 decisions, never from relevance; old patterns
      are never automatically treated as current; no real recorded
      reason means no review; failure never fabricates freshness,
      staleness, ending, or change.
    - *Uncertainty consequence:* uncertain relevance yields **at most a
      labeled review suggestion or event** — nothing stronger.
    - *Fallback:* no event, no review pressure.
    - *Surfacing:* none directly — this mode **emits relevance events
      only**; the settled §7D machinery owns any state change; §7M
      remains downstream of §7D and never its input.
    - *Unresolved handling:* `T2-UNRES-SHARED v1_0` (§5.3) — an
      unresolved result never changes Living State and never counts as
      currentness support.
11. **Allowed-use boundary:** §7Q internal-use-authorized candidate
    items and the identified target node only, for review-trigger
    evaluation only; relevance never writes into the Living State Web
    (its records live in Attention and Relevance Control's own record
    space); no `currentness → relevance → currentness` circular support
    of any form; nothing here widens access.
12. **Logging and audit:** one Decision-12 relevance event record per
    evaluation; emitted review events per the settled §7D/A6 schemas;
    every review's trigger and outcome logs under §7D's own §0B
    obligations — linked by identity, never double-counted.
13. **Fail-closed:** no valid declaration → no emitted review events
    (existing §7D evidence-driven behavior is untouched); unrecognized
    purpose → Decision-14 halt; an evaluation that cannot complete
    emits nothing and fabricates nothing.

---

## 11. THE A25→B10 BOUNDARY AND THE MANUAL-REREAD SEAM — RECORDED, NOT REDESIGNED

**11.1 The accepted three-case connection (exact, unchanged).** The
accepted A25→B10 reread-mode connection
(`NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md`, SHA-256
`b5869d85…ba18d`, 432 lines, 26,233 bytes) is `PACKAGE_COMPLETE` — per
its corrected closure receipt v1_1 (SHA-256 `87f76711…de11`, read in
full for this candidate and left byte-identical) — **only for the three
truthful A25 assignment cases**:

- `["direct"]`
- `["wider-context"]`
- `["direct", "wider-context"]`

This candidate represents that connection as complete for exactly those
three cases and nothing else, reopens nothing in it, and does not
extend, reinterpret, or re-close its receipt.

**11.2 The manual-reread seam — disk-accurate status, by reference
only.** The separate versioned mechanical compatibility package that
the accepted connection §10 required, and that the corrected receipt
v1_1 §6 recorded as open at its own writing, **exists at the pinned
snapshot as a separately accepted standalone design**:
`NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md` (SHA-256
`a0912880…0cd1`, 430 lines, 26,025 bytes), whose own closure record
(`…_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`, SHA-256 `2b03cc7f…79de`)
records ChatGPT's PASS and Ness's exact explicit acceptance of
July 12, 2026, `PACKAGE_COMPLETE` for its standalone design scope. At
design level it supplies the typed carrier
(`manual_reread_compatibility_record` [proposed there]) as the second
permitted referent of B10's `reread_mode_ref` for the settled manual
no-new-information path — creating **no** third A25 semantic mode,
manufacturing **no** assignment, and never treating Ness's request as
new evidence. This candidate consumes that accepted package **by
reference only**: it does not design, solve, close, reopen, rename,
absorb, extend, or bias it, and it adds nothing to it.

**11.3 What is honestly still open on this seam:** whether the whole
A25→B10 connection is now complete is recorded only by a **future
closure receipt** after the accepted compatibility package's own terms
(its §12) — no such whole-connection receipt exists at the pinned
snapshot, and this candidate issues none; the assignment **producer**
remains open; all B10 wiring, integration, runtime, and implementation
remain open and unauthorized.

**11.4 Instruction-staleness disclosure (for ChatGPT's independent
audit and for Ness).** The governing task instruction for this
candidate described the manual-reread mechanical compatibility gap as
still open and required this candidate to keep it so. The acceptance
recorded in §11.2 post-dates that instruction's premise. Under the
governing rules — disk evidence governs build/status facts, and Ness's
later explicit acceptance supersedes stale status wording — this
candidate records the accepted status rather than restating the stale
"remains open" wording. **This is the single deliberate deviation from
the instruction's literal text in this candidate, and it changes no
design content:** every substantive prohibition is honored — the
package was not solved, closed, or designed here; no false, third,
empty, sentinel, or default assignment was introduced; the three-case
receipt was not reopened or extended; the reread declaration is
compatible with both accepted mode-slot paths without redesigning
either. If ChatGPT's audit or Ness prefers different wording for this
seam, that correction is a new version of this candidate.

## 12. NO-LOSS CONSISTENCY TABLE

How each declaration maps to its governing sources and consumer. "By
ref" = consumed by reference, unchanged.

| Declaration | §7R (Master) | A4 (accepted v1.1) | B1 (accepted v1.0) | B26 (accepted Bundle 2 §8/§13) | B-INT-1 (accepted Bundle 2 §9–§12) | Consuming component |
|---|---|---|---|---|---|---|
| RM-CR-01 | Purpose `retrieval_context_selection`; gates/dimensions selected from the settled 4/9; Decisions 1–14 by ref | All eight fields present (§6 items 1–13); reason + uncertainty behavior stated | Binds by `a4_declaration_ref`-equivalent identity; channels, config slots, ceilings, audit record by ref; all values open | Empty-vs-failure preserved; bounded retry then stop; no degraded continuation | Instantiates §10.1 design language into the formal record | Context Retrieval (§7F / C-7F) |
| RM-CV-01 | Purpose `view_assembly`; all nine dimensions within settled applicability | All eight fields present | n/a directly (assembly is not §7F retrieval); B1 labels ride in via supplied items | Fail-closed incomplete marking consistent | Instantiates §10.2; B5 profile carries this Tier-1 reference (accepted Bundle 4 §8.1 slot) | Computed View (§7M / C-7M / B5) |
| RM-AS-01 | Purpose `action_surfacing`; one categorical gate (`object_type_matches`) so historical support stays pool-eligible; thread/time facts are dimensions and provenance, never currency; strictness in Tier 2 only | All eight fields present | Support items carry B1 channel/strength provenance; positional live-thread provenance is the honest current-situation basis (accepted Bundle 2 §10.1/§11) | No invented support on failure | Instantiates §10.3 incl. side-drawer and wording rules (§11–§12) | Action Surfacing (§7N / C-7N; §7P by ref) |
| RM-RR-01 | Purpose `reread_trigger_evaluation`; evaluation ≠ trigger; no assignment production | All eight fields present | Reread pass context stays RR2's settled §7Q→§7F→§7R under B10/connection, by ref | Retrieval failure at RR2 stays B10/B26 territory, by ref | Instantiates §10.4; A25/B10/connection/compatibility all by ref | Reread Lifecycle (§7H / C-7H / B10) |
| RM-LS-01 | Purpose `state_review_trigger_evaluation`; Decision-8 boundary; `currentness_status` deliberately unselected | All eight fields present | n/a directly | No fabricated staleness/freshness on failure | Instantiates §10.5; A6-10 by ref | Living State Web (§7D / C-7D) |

Shared across all five: `T2-UNRES-SHARED v1_0` (§5.3); mouth
authorization **none**; §7Q-before-§7R and §7Q-then-SACL (§5.5);
Decision-12/Decision-11 records and one-operation/one-log (§5.6);
A4 §5 fail-closed path (§5.7); the §4 Ness-approved meaning.

## 13. WHAT THIS CANDIDATE COMPLETES — AND THE BUNDLE 2 CONDITION

The accepted Bundle 2 package's completion condition left "every …
formal Tier 1/Tier 2 declaration record" explicitly outside its scope
(accepted Bundle 2 §4, §16). **If** this candidate passes ChatGPT's
independent audit **and** Ness explicitly accepts it, the formal
declaration authoring for the five settled consumers is complete at
design level, and Bundle 2's remaining declared design opening on that
item closes at that moment — by the acceptance, never by this file.
This candidate does not declare that condition met, does not mark
Bundle 2 complete, and closes nothing by its own existence. Empirical
values, integrations, serialization, and implementation remain outside
Bundle 2's design scope exactly as the accepted package lists them.

## 14. EXPLICITLY OPEN (NONE CLOSED OR BIASED HERE)

- **Empirical B1 values and ceiling values** — every limit, threshold,
  budget, time span, and ceiling; tuned later against the accepted gold
  material before locking.
- **Testing and tuning against accepted gold material** — including any
  benchmark pass values.
- **Final mouth, model, and provider choices** — the Interactive
  Translator remains UNDECIDED; producers here are roles.
- **Exact implementation technology for independent validation** — and
  any future declared validator's independence mechanism.
- **Side-drawer visual and interaction mechanics.**
- **Implementation serialization and runtime code** — including final
  field naming at B-INT-1's implementation-facing step.
- **The A25 assignment producer** — how each relationship is detected
  or evaluated, per trigger type.
- **The whole-connection A25→B10 completion receipt** (§11.3) — and all
  B10 wiring beyond the accepted design-level packages.
- **B9 retry-value wiring into the relevant components** — the accepted
  v1_4 package's design-level wiring into B9/B10/B-HOLD/B24 stands as
  accepted; operational integration and wiring into further consumers
  (including B26's retrieval path) remain open.
- **B-CYCLE-8** and all full-cycle composition.
- **Master V10 / Design and Wiring Map / Decision Defaults /
  cursorrules integration** of this and every accepted package.
- **All coding, production stores, migration, marker, seal, runtime,
  UI, and go-live work** — unauthorized; awaiting Ness's separate
  implementation authorization.
- **Any degraded-continuation rule after failed retry** — none exists;
  fail-closed stands unless Ness later explicitly authorizes one.
- The sealed 5,521-root batch and both sealed gold sets — untouched.
- No other open Register-A/B/C item is closed or biased.

## 15. REQUIRED SAFETY CHECKS — VERIFIED BEFORE DELIVERY

1. Every declaration uses exactly one settled purpose type — **yes**
   (§6.3, §7.3, §8.3, §9.3, §10.3; one each; labels carry no behavior).
2. No settled gate or dimension renamed — **yes** (only the settled
   four gate names and nine dimension names appear; selection and
   honest non-selection only).
3. Mouth permission narrow and named — **yes**: explicitly **none** in
   all five; any future mouth dimension requires a new version with the
   dimension and contexts specifically named and the Decision-10
   reference (§5.3); no broad flag exists.
4. Every unresolved outcome has an honest, fail-safe path — **yes**
   (`T2-UNRES-SHARED v1_0`; §0A absence vocabulary for inapplicable
   values; A4 §5 path).
5. Relevance never becomes truth, evidence strength, currentness,
   access, permission, causation, or action authority — **yes** (§4
   statement 4; §5.5; per-declaration boundaries; Decision-8 boundary
   in §10; §8 item 5: shared-thread membership and time-range presence
   are structural/temporal facts only and never become currency or
   assign the current-situation label).
6. Uncertain patterns may guide N.H without making Ness a clerk —
   **yes** (§4 statements 1–2; §6.10; no approval queue anywhere;
   inspection is available, never required).
7. Visible material explains uncertainty only when it materially
   affects the result — **yes** (§4 statement 3; §7.10 surfacing;
   §8.10 side-drawer placement; main answers never overstate
   certainty).
8. Privacy and access always run before relevance — **yes** (§5.5;
   every declaration's boundary).
9. Positional and semantic retrieval never merge — **yes** (§6:
   channel identity is provenance; per-channel gates, dimensions,
   ordering; conflicts surfaced; semantic never overrides or repairs
   positional).
10. No duplicate behavior or circular evidence path introduced —
    **yes** (one-operation/one-log; records link by identity; no
    double evidence; Decision-8 circle structurally unreachable in
    RM-LS-01; Computed View never evidence for itself; derived material
    never validates its producer).
11. The accepted A25→B10 connection represented as complete only for
    the three truthful assignments — **yes** (§11.1; §9.10).
12. Manual reread remains a valid settled trigger; its separate
    mechanical compatibility seam recorded accurately — **yes**, with
    the disk-accurate accepted status recorded by reference and the
    instruction-staleness deviation disclosed (§11.2–§11.4); the
    compatibility package itself was not solved, closed, or redesigned
    here.
13. No false A25 assignment, third mode, default mode, empty mode, or
    sentinel mode introduced for the manual path — **yes** (§9.10;
    §11.2; this candidate creates no mode-slot content of any kind).
14. No accepted or authoritative file changed — **yes** (§16; every
    source preserved byte-identically; zero repository modifications).

## 16. CHANGE REPORT AND SELF-AUDIT

**File created:**
`NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md`
— the only file created by this task, produced by copying the
identity-verified v1_0 base (SHA-256 `23844b87…dd99`; 1,068 lines;
66,508 bytes) and applying only the narrow RM-AS-01 correction and its
dependent consistency edits (status-block version note; §2 base row and
sourcing note; §8 items 4, 5, 10, 11, 12, 13; §12 RM-AS-01 row; §15
check 5; this §16; the end line). v1_0 is preserved unchanged as
historical candidate provenance. **Nothing existing was modified:**
Master V10, Decision Defaults, cursorrules, the Companion, the map
v1.6, the eight-bundle plan, every accepted package and every
acceptance/closure record (including the accepted Bundle 2 v1.0
candidate and its acceptance record, the accepted A25 v1_2, the
accepted A25→B10 v1_2 connection and its corrected v1_1 receipt, the
accepted manual-reread compatibility package and its receipt, the
accepted B10, B9 retry-state and B9 retry-values packages and their
receipts, the accepted Bundle 1, Bundle 3, and Bundle 4 sets), all
historical candidates, and the project decision package remain
byte-identical. Nothing was committed, pushed, moved, renamed,
overwritten, or deleted in the repository. No code, schema for
production use, store, marker, seal, migration, runtime, PC, UI, model,
or implementation action was performed or authorized; no integration
into any authority file occurred; no Register-A concept work was
performed — every decision applied here is Ness's, carried in the
governing instruction or recorded in an accepted package.

**Self-audit:** authority order preserved; Master V10 governing —
PASS. Additive only; accepted Bundle 2 v1.0 consumed by reference and
not rewritten — PASS. Ness-approved meaning carried verbatim and
normalized without added meaning — PASS. Five declarations, each with
all required Tier 1/Tier 2 fields, each on exactly one settled purpose
type, drawn solely from the settled vocabulary — PASS. Mouth
authorization explicitly none; shared uncertainty rule mechanically
expressed; Master independent-validation boundary preserved; no second
model mandated — PASS. §7Q-before-§7R and §7Q-then-SACL preserved;
access never widened — PASS. Channels never merged; theme/pattern
influence logged per the accepted audit-trail rule; themes never
proof or silent structural links — PASS. Computed View internal-only
and never self-evidencing — PASS. Action strictness split, side-drawer
placement, and §7P separation preserved; current support satisfied only
by honestly grounded present-context provenance, with
`object_type_matches` as the sole categorical gate so labeled
historical support stays pool-eligible, and thread/time facts never
becoming currency — PASS. Reread declaration
compatible with both accepted mode-slot paths without redesigning
either; evaluation never a trigger; no assignment produced — PASS.
Living State doorbell-only; Decision-8 circle structurally unreachable
— PASS. Three-case connection scope preserved exactly; manual-reread
seam recorded disk-accurately by reference; the one instruction-text
deviation disclosed in §11.4 — PASS. All opens preserved with owners;
no value chosen anywhere — PASS. Exactly one file created; no
implementation or integration — PASS.

---

*End of
`NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md`
— CANDIDATE, unaudited, awaiting ChatGPT's independent audit of this
actual file and Ness's explicit acceptance afterward. v1_0 is preserved
unchanged as historical candidate provenance. All authority, accepted,
and historical files remain unchanged; no implementation was
performed.*

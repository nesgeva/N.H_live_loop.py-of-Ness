# NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md

**Status:** CANDIDATE — unaudited; awaiting ChatGPT's independent audit and
Ness's explicit acceptance. Standalone mechanical architecture package
only. Not adopted, not authoritative, not integrated into Master V10, the
Design and Wiring Map, Decision Defaults, or cursorrules. Authorizes no
implementation, code, Cursor work, migration, production store, model
change, runtime, UI, tuning, or live-disk action. **Chooses no empirical
value of any kind.**

**Date:** July 9, 2026.

**Package ID:** B1 — §7F Context Retrieval parameter architecture:
retrieval channels, per-mode parameter structure, audit fields, and safety
ceilings (map C-7F open slot; Bundle 2 mechanical item per the verified
eight-bundle plan).

**Plain meaning:** B1 designs the **safe structure** for retrieval
settings — the shape every retrieval mode's configuration, audit record,
and ceiling must have. **It does not choose the final tested values.**

**Intended repository placement:** `05_ACTIVE_CANDIDATE/`
(the physical move into the repository is Ness's action).

**Governing authority order:**
1. `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`
   (adopted by Ness June 29, 2026; governing)
2. `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`
3. `01_AUTHORITATIVE/cursorrules`
4. `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`

**Sources inspected for this candidate:** Master V10 §7F / the map v1.6
**C-7F Context Retrieval** entry (the settled content this candidate
mechanizes: two channels — positional and semantic; four conceptual modes
— bare / local-context / associative / combined; the settled conflict rule
— surfaced, never silently resolved, semantic never overrides or repairs
positional, two separate prompt sections; the settled per-mode declaration
list; the settled logging list; the settled empty-vs-failure distinction;
bounded-with-hard-safety-ceilings; the must-never list; and the open slots
routed to B1, B26, and A4); the map's **B-INT-1** entry and **C-7R**; §0B;
the accepted **A4 policy package**
(`NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md`, SHA-256
`c754b27e…553f`) and its acceptance record (`…_ACCEPTANCE_RECORD_v1_0.md`,
SHA-256 `f9d3fe04…4e62`), both read from the hash-verified accepted
working copies; the accepted B24 v7 §6.5 gate order as settled context.
**Sourcing note (honest, for the audit):** the eight-bundle plan
(`03_WORKFLOW/NH_REPLACEMENT_EIGHT_BUNDLE_DEPENDENCY_PLAN_v1_0_CANDIDATE.md`)
is consumed through its verified Bundle-2 composition (A4 / B1 / B26 /
B-INT-1) carried in the governed instruction channel; the file itself is
still not returned by this worker's connected project-knowledge index.

---

# 0. PURPOSE AND SCOPE

**What B1 is.** The mechanical parameter architecture for §7F Context
Retrieval: the two always-separate channels, the structure every retrieval
mode's configuration must carry, the audit/log record every retrieval run
must leave, and the safety-ceiling mechanism that sits above every mode's
own settings.

**What B1 settles:** structure only — record shapes, field slots,
precedence rules, and boundaries.

**What B1 does not settle:** any number. Every limit, threshold, budget,
and ceiling **value** remains open for later empirical tuning, tested
against the gold sets before being locked, exactly as the map fixes. B1
also designs no failure mechanics (B26), performs no wiring (B-INT-1), and
writes no component's A4 declaration.

---

# 1. THE TWO ALWAYS-SEPARATE CHANNELS

**Positional context** — "what immediately preceded in this thread": a
deterministic, position-based fact about where the target sits in its
recorded stream. Its evidentiary character is **provenance-grade**: it
reports adjacency that actually happened.

**Semantic context** — "what else may relate": a similarity-based,
model-produced suggestion (embedding retrieval). Its evidentiary character
is **interpretive**: a fallible guess that something is related.

**Why they stay separate (binding, from the settled design):** the two
channels carry different kinds of claims. Merging them would let a
similarity guess masquerade as conversational adjacency — a semantic match
mistaken for a preceding turn silently rewrites what actually surrounded
the target. Therefore, structurally and permanently:

- the channels are **never merged**; every retrieved item carries its
  channel identity as provenance;
- a **conflict** between positional and semantic context is **surfaced,
  never silently resolved**;
- **semantic retrieval never overrides or silently repairs positional
  context**; the downstream prompt shows the two in **separate labeled
  sections** so a semantic match cannot be mistaken for a preceding turn;
- **channel identity is provenance, not a relevance dimension** (settled
  §7R rule, consumed unchanged);
- the four conceptual modes consume the channels without blending them:
  `bare` (no context), `local-context` (positional only), `associative`
  (semantic only), `combined` (both present, separately labeled, never
  blended).

---

# 2. PER-MODE PARAMETER STRUCTURE (STRUCTURE ONLY — NO VALUES)

Every retrieval mode carries one versioned **mode configuration record**.
Field names below are proposed mechanical identifiers introduced by this
candidate; exact serialization and final naming are confirmed at
B-INT-1/implementation without changing the structure's meaning.

**Identity and binding:**
- `mode_id` + `mode_version` — stable identity; any configuration change
  produces a **new version, append-only**; configurations are never
  silently edited;
- `purpose_type` — one of the settled five-value §7R purpose vocabulary
  (plus the optional label carrying no system behavior); consumed from
  §7R/A4, never redefined here;
- `consuming_component` — which component runs this mode;
- `a4_declaration_ref` — the id + version of the consuming component's A4
  declaration, **by reference only** (§5). A mode without a valid
  referenced declaration for the current purpose is invalid.

**Bounded quantities (slots defined; every value OPEN):**
- `positional_context_limit` — how much immediately-preceding material may
  be supplied; **value open**;
- `semantic_result_limit` — how many semantic matches may be supplied;
  **value open**;
- `ranking_or_threshold_rule` — a reference (rule id + version) to the
  mode's declared ranking/threshold rule; the rule's content and every
  threshold **value open**; a threshold is **never lowered silently** —
  a change is a new configuration version;
- `token_size_budget` — the size envelope for the assembled context
  package; **value open**;
- `time_range` — optional; if present, explicit and recorded; span
  **value open**.

**Scope and safety:**
- `eligible_source_scope` — the declared source scope this mode may draw
  from, always **inside** material already authorized by §7Q for the
  current purpose; scope can only **narrow** use, never widen access;
- `safety_ceiling_ref` — which versioned ceiling set (§4) governs this
  mode; mandatory;
- `insufficient_context_fallback_behavior` — the mode's declared behavior
  for the settled **genuine-empty** outcome (proceed bare, marked
  context-limited/revisable). This slot covers the healthy empty case
  only; **system-failure behavior is B26's and is not declared here.**

**Provenance:**
- `configuration_version` + configuration provenance (who/when/what
  changed; prior versions preserved).

**Validity rule (fail-closed structure):** a mode configuration missing
any required field, referencing no valid A4 declaration, or exceeding its
ceiling set (§4) is **invalid and never runs**. The recording and handling
of that condition as a failure event follows the settled honest-failure
rules and the future B26 path — no failure mechanics are designed here.

---

# 3. AUDIT / LOG RECORD PER RETRIEVAL RUN (§0B)

Every retrieval run leaves exactly **one append-only audit record** —
one operation, one log — containing:

- `audit_record_id` — stable identity for the run;
- `mode_id` + `mode_version` and `configuration_version` actually used;
- the **channel(s) queried**, each recorded separately (never merged);
- the **parameters actually applied** — and any ceiling-enforcement event
  (§4), recorded, never silent;
- **index/model/system version provenance** — embedding-model version,
  index version, retrieval-system version;
- the **exact roots supplied**, per channel, each with per-item
  provenance: type, why it was admitted (which rule/score/position),
  source root/thread, timestamp, score or position;
- **exclusions/truncation caused by limits** — what was cut and by which
  limit or ceiling;
- the **empty-result vs failure marker** — the settled distinction:
  a genuine empty result is a normal condition (proceed bare, marked
  context-limited/revisable); a system failure is **never claimed as
  success**. The marker slot lives here; the failure path's states and
  mechanics are **B26's**;
- the downstream linkage — the reading audit-trail pointer (§7G prompt);
- `audit_config_version` — which audit/ceiling configuration was in force.

All audit records are subject to §7Q access and authorization rules, and
§25 identity/security authorization where applicable; they are appended,
never rewritten; repetition adds no certainty and no double evidence.

**How audit records prevent hidden retrieval behavior (binding):** because
every run records the exact configuration and versions used, the exact
items supplied with why, the exact cuts made and by which limit, and the
honest empty-vs-failure outcome, **no mode can silently retrieve more,
less, or other than it is configured for**. Silent threshold-lowering,
silent substitution of unrelated material, silent channel-mixing, and
silent over-retrieval are all structurally detectable, because the applied
parameters, admitted items, and enforcement events are on the record for
every single run.

---

# 4. THE SAFETY-CEILING MECHANISM (STRUCTURE ONLY — NO VALUES)

- A **versioned ceiling set** (`ceiling_set_id` + version) sits **above**
  mode-specific settings, defining a hard maximum for every bounded
  quantity a mode declares (positional-context limit, semantic-result
  limit, token/size budget, time-range span, and any later declared
  bounded quantity). **Every ceiling value is open.**
- **Precedence rule:** the effective limit for any bounded quantity is
  the **minimum** of the mode's own setting and the ceiling. A mode may
  set itself lower than its ceiling; it can never set itself higher.
- **Configuration-time enforcement (fail-closed):** a mode configuration
  exceeding any ceiling in its referenced ceiling set is **invalid and
  rejected at configuration time**, and the rejection is recorded.
- **Runtime defense-in-depth:** the runtime never exceeds the ceiling
  regardless of configuration state; any ceiling-enforcement event is
  recorded in the run's audit record — visible, never silent.
- **Governed change only:** ceiling sets change only by a **new
  version** through the governed change path (a later Ness/tuning
  decision), never as a runtime side effect; every audit record references
  the ceiling set in force at run time.

**How ceilings prevent silent expansion (binding):** a mode can never
grant itself more retrieval than its allowed boundary, because the ceiling
is enforced **outside** the mode's own configuration; effective limits
never exceed it; every enforcement, clamp, or rejection is recorded; and a
ceiling can move only through a versioned governed change — never by
anything the mode itself does at run time.

---

# 5. CONSUMING A4 (WITHOUT WRITING ANY DECLARATION)

- Every retrieval mode binds **by reference** (`a4_declaration_ref`) to
  its consuming component's accepted-A4 declaration — the mandatory
  eight-field policy contract under the settled §7R two-tier
  Tier 1/Tier 2 structure. **B1 writes no declaration content**, invents
  no relevance mode meaning, and adds no gate condition or dimension.
- The accepted A4 rule stands: a component without a valid declaration
  for the current purpose has **no relevance mode to run** — so the
  corresponding retrieval mode does not run either.
- The settled gate order stands, unchanged: **§7Q internal-use
  authorization (via LMAC) before any root is returned; §7R relevance
  mode per consuming mode after §7Q.** No B1 parameter widens access;
  `eligible_source_scope` narrows use only; nothing here reveals or
  signals withheld material.

---

# 6. SEPARATION FROM B26 (BINDING SEAM)

- **B1 owns:** the parameter structure, audit fields, and ceiling
  mechanism — the shape of a **healthy** retrieval run, including the
  honest **genuine-empty** outcome (a normal condition: proceed bare,
  marked context-limited/revisable).
- **B26 owns (untouched here):** the retrieval **system-failure**
  behavior — index failure, stale/incomplete index, timeout, unreachable
  service; failure-state recording; whether the reading pass stops,
  retries, or proceeds with explicitly degraded context; crash recovery;
  duplicate prevention; and the prohibition on pretending retrieval
  succeeded or silently substituting unrelated material as failure-path
  mechanics.
- B1's audit record carries the **marker slot** that distinguishes empty
  from failure; B26 later defines the failure states, transitions, and
  recovery that populate the failure side. Nothing in this candidate
  designs, constrains, or biases those mechanics.

---

# 7. BOUNDARIES (BINDING ON THIS PACKAGE)

- **No empirical value chosen:** no limit, threshold, budget, ceiling,
  time span, or tuning number anywhere in this candidate.
- **No gold-set results created**; the settled rule stands — parameter
  values are empirically tested against the gold sets before being
  locked, later.
- **No B26 design:** no index-failure, stale-index, timeout,
  unreachable-service, retry, stop-vs-degraded, crash-recovery, or
  duplicate-prevention mechanics.
- **No B-INT-1 instantiation or wiring**; final serialization/naming of
  the proposed fields is confirmed there without changing meaning.
- **No A4 declaration written; A4 not reopened** — consumed by reference
  exactly as accepted.
- **Bundle 1 not reopened**; no accepted file edited; Master V10, the
  map, Defaults, and cursorrules untouched.
- **Not adopted; Bundle 2 not complete; no implementation** — no coding,
  Cursor work, migration, production store, model change, runtime, UI,
  tuning, or live-disk action.
- **Settled must-nevers carried unchanged:** never merge channels; never
  let semantic override or repair positional; never lower thresholds
  silently or substitute unrelated memories; never claim success on
  failure; channel identity is provenance, not a relevance dimension.

---

# 8. SETTLED / NOT SETTLED / OPEN (EXPLICIT)

**B1 settles (structure only):**
- the two always-separate channels and the four modes' non-blending
  consumption of them (§1);
- the per-mode configuration record with its required fields, versioning,
  and fail-closed validity rule (§2);
- the per-run append-only audit record and its required fields (§3);
- the ceiling mechanism: versioned ceiling sets, minimum-precedence,
  configuration-time rejection, runtime defense-in-depth, governed change
  (§4);
- the A4 consumption-by-reference rule (§5) and the B1/B26 seam (§6).

**Open for later empirical tuning (not chosen here):** every value —
positional-context limits, semantic-result limits, threshold/ranking
values, token/size budgets, time-range spans, and every ceiling value —
each tested against the gold sets before being locked, through the
governed tuning path.

**Open for B26:** the entire retrieval system-failure path (§6).

**Open for B-INT-1:** instantiating each component's accepted A4
declaration against the settled §7R contract; wiring the consumers; final
mechanical serialization and naming of the structures proposed here.

**Also open:** the actual per-component A4 declarations (reserved to
Ness); Bundle 2's remaining sequence; final model/provider choices; all
Master/map/Defaults/cursorrules integration; all implementation, storage,
runtime, UI, and tuning choices. No open item of Bundle 1 or any other
Register is reopened, closed, or biased.

---

# 9. DESIGN-COMPLETE CONDITION FOR THIS PACKAGE

This package is design-complete for B1's structural scope when: the
two-channel separation with its reasons and must-nevers is carried
unchanged (§1); the per-mode configuration structure exists with
identity, binding, bounded-quantity slots, scope/safety fields,
versioning, and the fail-closed validity rule — with every value open
(§2); the per-run audit record prevents hidden retrieval behavior (§3);
the ceiling mechanism prevents silent expansion with every ceiling value
open (§4); A4 is consumed by reference without any declaration being
written (§5); the B26 seam is explicit and untouched (§6); and every
boundary and open item in §7–§8 holds — subject to ChatGPT's independent
audit and Ness's explicit acceptance.

---

# 10. CHANGE REPORT

**File created:**
`NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md` — the
only file created by this task. First B1 version; no prior B1 file exists
or was modified. **Sources untouched:** Master V10, Defaults, cursorrules,
the Companion, the map v1.6, all accepted packages and
closure/acceptance records (Bundle 1's complete set, A2, A4 v1_1 and its
acceptance record), the A1 blocker record, and all historical candidates
remain unmodified; nothing was integrated; no implementation, disk,
store, model, or runtime action occurred. **Sourcing note carried in the
header** for the audit: the plan consumed through its verified Bundle-2
composition; the accepted A4 pair read from hash-verified working copies.

---

# 11. PACKAGE SELF-AUDIT (internal)

- **Authority:** order preserved; Master V10 governing; the settled C-7F
  content carried without loss; candidate status explicit. **PASS.**
- **Concept fidelity / no loss:** channels, modes, conflict rule,
  declaration list, logging list, empty-vs-failure distinction,
  bounded-with-ceilings, and the must-never list all preserved; nothing
  settled weakened. **PASS.**
- **No value chosen:** every limit, threshold, budget, span, and ceiling
  is an open slot; no number appears anywhere. **PASS.**
- **No B26 design:** failure mechanics named only to assign them to B26;
  no state, transition, retry, recovery, or duplicate-prevention
  mechanism created. **PASS.**
- **No B-INT-1 wiring; no A4 declaration written; A4 not reopened:**
  consumption is by reference only; the accepted no-declaration/no-mode
  rule carried. **PASS.**
- **Access never widened:** §7Q-before-§7R preserved; scope narrows only;
  no withheld-material signaling. **PASS.**
- **Hidden behavior prevented structurally:** per-run audit record with
  exact parameters, items, cuts, versions, and enforcement events;
  ceilings enforced outside the mode with governed versioned change.
  **PASS.**
- **No false completion:** Bundle 2 open; opens listed; nothing marked
  adopted, authoritative, or complete. **PASS.**
- **No implementation:** none performed or authorized. **PASS.**

---

*End of `NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md`
— CANDIDATE, unaudited, awaiting ChatGPT's independent audit and Ness's
explicit acceptance. All authority, accepted, and historical files remain
unchanged; no implementation was performed.*

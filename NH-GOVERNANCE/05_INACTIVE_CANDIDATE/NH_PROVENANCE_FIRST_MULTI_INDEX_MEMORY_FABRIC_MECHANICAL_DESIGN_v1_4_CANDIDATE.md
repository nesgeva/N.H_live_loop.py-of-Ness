# NH_PROVENANCE_FIRST_MULTI_INDEX_MEMORY_FABRIC_MECHANICAL_DESIGN_v1_4_CANDIDATE.md

## §1 — Status, authority, scope, and no-implementation statement

**Status:** DESIGN CANDIDATE — NOT AUDITED — NOT ACCEPTED — NOT ADOPTED —
NOT INTEGRATED — NOT IMPLEMENTED — NOT `PACKAGE_COMPLETE`. This file is
technical architecture only. It carries no authority, creates no authority,
and becomes governing for nothing merely by existing, by being complete, or
by being audited. Independent audit and Ness's explicit acceptance remain
separate later steps that this file neither performs nor anticipates.

**What this package is:** the standalone logical mechanical design of the
**Provenance-First Multi-Index Memory Fabric** — Addition 3 of the five
accepted framework capability directions recorded in
`05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md`
(§15–§21 of that package). It designs the derived, rebuildable
projection-and-query layer over N.H's already-preserved records, its channel
families, its records, its build and query lifecycles, its gates, its
recovery, and its boundaries.

**Date:** August 25, 2026.

**Task type:** Implementation-neutral mechanical architecture translating
already-settled Ness decisions into technical mechanics. **No Ness concept or
policy decision is required, requested, made, inferred, or implied by this
package.** Where a policy, threshold, empirical value, or meaning question is
genuinely open, this design leaves it explicitly open and names its owner
(§20). No placeholder is chosen that would silently bias a future decision.

**Component identity and placement:** the final controlled component
identifier, Register entry, and bundle placement of this design are **not
assigned here and are not assigned by this file**. No controlled ID, Register
ID, package key, or repository/bundle placement is invented, implied, or
reserved. Those remain owner-decided (§20, open item 1). Every record and
field name below is a **logical design label** — written `[proposed]` — for
mechanical clarity only; none is a controlled identifier, and none becomes
one by appearing here.

**Governing authority order:**
1. `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` (adopted by Ness June 29,
   2026; governing every conflict; its stale internal pre-adoption wording is
   superseded and is recorded as non-blocking document drift)
2. `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_3.md` — the authoritative
   Decision Defaults S19, adopted August 13, 2026, superseding v2.2 and every
   prior Defaults version
3. `01_AUTHORITATIVE/cursorrules`
4. `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`
5. `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` —
   subordinate working material; never overrides Master V10
6. accepted standalone packages, their acceptance records, and their closure
   records, strictly within their own stated scopes

`01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` is **preserved superseded
history only**. It is not a current guide, is not a competing guide, and is
never consulted here as a governing source; where its wording and v2.3 differ,
**v2.3 governs and v2.2 is history**.

**Sources read for this candidate:** the governing files
above (Master V10 §0A/§0B, §5/§16 index and model surface, §6B root schema
and store, §7D/§7E/§7F/§7G/§7J/§7K/§7L/§7M, §7P, §7Q, §7R, §24, §25, §26,
TSC §29–§30, §11 designed-but-not-built items; **Decision Defaults S19 v2.3**
§3B/§3C and the store/index inventory; `cursorrules` store and index
protections; the Companion's preserved mirror of the same records); the current working map
v1.6 (C-INDEX, C-STORE, C-7E, C-TSC, C-7F, C-7L, C-7J, C-7M, C-13, the B11
and B1/B26 register entries); `03_WORKFLOW/NH_FULL_DESIGN_COMPLETION_WORKFLOW_v1_0.md`
and `03_WORKFLOW/NH_REPLACEMENT_EIGHT_BUNDLE_DEPENDENCY_PLAN_v1_0_CANDIDATE.md`;
accepted **B11 v1.4** (batch identity, LB1–LB7 boundaries, `index_registration`,
`coverage_status`, discovery, identity lookup, the recovery matrix and its
lookup-first protocol); accepted **B9 v1.0** and the accepted **B9 retry-values
wiring v1.4** (`schedule_class`, episode ordinals, minimum waiting gaps,
episode deadlines, fail-closed on a missing class); accepted **B7 v1.3**,
**B16 v1.0**, **B15 v1.4**, **B24 v7**, **B10 v1.0**, **B-HOLD v1.0**, the
**B-INT-4/5/6/7/8** wiring packages, **A2 v1.8** (telling identity), **A4**,
**A7 v1.1**, **A25**, **A26**, **A29**, **A31**, **A15**, **A16**, **A17**,
**A22**, the accepted **Authority Integrity Control Plane (AIC) v1.10**
mechanical design and its package-complete closure record, the accepted
**Unified Durable Operation Kernel (UDOK) v1.9** mechanical design and its
package-complete closure record, the Story-Layer firmness policy, **Bundle 1** (normalization and
closeout, including the Ness-decided B9 retry values), **Bundle 2** (formal
relevance declarations; the completion candidate carrying the B26
retrieval-failure design), **Bundle 3 v1.2** (Story layer, Person-Boxes,
themes, clashes), **Bundle 4 v1.3** (Living State, Computed View, action
ladder, world model), **Bundle 5 v1.1** (privacy, security, access, TSC
authority), **Bundle 6** (ingest, provenance, research, creation, personal
learning — policy decisions and mechanical design), **B1 v1.0** (retrieval
channels, per-mode configuration, per-run audit record, safety ceilings), and
`06_OPERATIONAL_INSTRUCTIONS/NH_CLAUDE_PROJECT_INSTRUCTIONS_v1_2_CANDIDATE.md`.

**Source statement (owner seams consumed exactly):** this candidate is
written from the current source set named above. The **Authority Integrity
Control Plane (AIC) v1.10** design with its package-complete closure record
and the **Unified Durable Operation Kernel (UDOK) v1.9** design with its
package-complete closure record are the **accepted standalone owner designs
consumed here at their exact closure-bound seams** — AIC for governing-basis
verification at UDOK-1, UDOK for operation identity, generation structure,
child-membership registration and closure, checkpoints, one-winner commits,
lookup-first recovery, and terminal evidence. This design **carries those
seams as the owners bind them** and neither designs, restates, extends, nor
constrains the owners' interiors. Where this file and an owner package differ,
**the owner package governs** and this file is corrected in a new version; no
such difference is resolved, deferred, or papered over here, and **no generic
"the owner governs" caveat stands in place of the concrete seam obligations
specified in §§3.3, 3.4, 11, 13, 17, 18, and 19.**

**Logical record contracts vs. persisted schema (binding boundary).** This
file **does settle** one side of this boundary: the **proposed logical record
shapes, the required information each record carries, their relationships,
their lifecycle constraints, and the applicable controlled vocabularies** for
the fabric records described in **§§5–6, §12, §14, and §18** — channel
definitions, generation manifests, entries, coverage and health events,
retrieval plans, channel results, failure records, and membership-fence
violation records. **Those logical record contracts are material design
commitments**, not illustrations: §21 item 3 makes their required contents a
completion condition, and §19 refuses effects when their required content is
unproved. Every label remains a `[proposed]` logical design label and none is
a controlled identifier.

**The other side of the boundary is equally binding: no persisted or
implemented schema exists here**, and none is created, chosen, migrated, or
authorized by this file. The **final persisted names and types,
serialization, physical storage technology, database / index / graph engine,
storage layout, runtime libraries, migration, and every other implementation
choice remain unresolved** (§20, open item 2). **Neither half of this boundary
may be stated without the other**: it is inaccurate to say this design
contains **no schema anywhere**, and equally inaccurate to say it settles a
**persisted or implemented** schema (§22).

**No implementation:** this file contains architecture only. No code, no
patch-ready pseudocode, no applicable patch, no store creation, no index
creation, no persisted-schema creation or change, no migration, no rebuild, no
mutation, no model or library installation, no runtime, no UI, no disk action,
no terminal command, no Map/Master/Defaults/`cursorrules` integration, and no
authorization for any of them. No storage engine, database, index engine,
graph store, embedding model, serialization format, filesystem layout,
workflow library, or code API is chosen. Every governing, authoritative,
accepted, historical, and source file remains untouched; this candidate
occupies exactly one file — this v1.4 successor — and its v1.0, v1.1, v1.2,
and v1.3 predecessors are preserved unchanged as history.

---

## §2 — Preservation inventory: settled rules consumed, never weakened

| Settled rule (source) | Fabric relationship |
|---|---|
| Indexes are derived machinery; preserved roots, accepted records, and governing provenance remain above them; each index must be rebuildable from permitted source records and declared accepted relationships (Five-Additions §18–§19) | The whole design is built on this. Every fabric artifact is derived, versioned, and rebuildable (§3, §11). |
| An index must never become the only surviving copy of memory (Five-Additions §20) | Entries are references and derived search material only, never a sole source copy (§5.3). |
| Roots immutable; readings are linked additions; every real source item is its own Origin; mixed media are connected, not merged; original/import/record times remain distinct (Master §6B; Bundle 6) | Projected by reference with all distinctions preserved (§7). |
| Positional and semantic channels stay separate and labeled; semantic never overrides or repairs positional; conflicts are surfaced, never silently resolved; channel identity is provenance, not a relevance dimension (Master §7F; B1 §1) | Two of the eight families; no blended rank anywhere (§4). |
| §7Q runs before §7R; for visible output §7Q is first and SACL second; SACL supplies permitted scope before retrieval in multi-speaker contexts (Master; B-INT-6; Bundle 5) | Gate order carried unchanged into projection and query (§8). |
| Level-1 raw protected content never leaves its protected-execution boundary; ordinary records carry opaque protected-record references only (A7; B7; Bundle 5) | Structural exclusion from every ordinary index, embedding, log, result, and context package (§8.4). |
| Similarity or co-retrieval never creates an accepted connection; model-produced relationships remain proposals unless an accepted route admits them; Person-Boxes are linked views, not second memory stores (Five-Additions §18; Bundle 3) | The identity-and-connection discipline of §9. |
| A telling is its own immutable card with its own stable `telling_id`, linked to its parent reading and supporting roots; conflicting tellings are never merged; repetition never confirms (A2 v1.8; Bundle 3; firmness policy) | Projected exactly as owned; never inferred (§10.1). |
| B3 themes carry a stable `theme_id`, theme↔telling membership links with their settled link fields, alias records that rename nothing in place, and the settled append-only theme-action set — **confirm** (Ness response only), **reject** (deletes nothing), **rename**, **merge**, **split**, **leave unresolved**; the current visible theme state is always **derived from the preserved event history** (Bundle 3 §11) | Family 6 carries the stable identity, membership links, aliases, and every theme-action event; no two-label collapse (§4, §10.1). |
| §7D is an input to §7M; **§7M is never an input to §7D**; relevance, privacy, and governance results are governors, never ordinary evidence (Master §7D/§7M; Bundle 4) | Enforced as a permanently forbidden edge (§10.3, §17.2). |
| A batch participates in unified reading **only after** a committed `index_registration` (LB7) per index; B11 owns batch identity, ownership, and that registration with honest `coverage_status`; B11 detects and marks, never hides a gap; what a retrieval service does with degraded coverage is B1/B26's (B11 §10.3–§10.4) | The fabric registers through LB7 **only after atomic publication**, and consumes coverage as structural truth; staging never registers and never claims coverage (§6, §11). |
| UDOK owns durable coordination: generation-scoped child registration before child owner work (UDOK-2), one generation-scoped child-membership head, single-winner closure of that exact head (UDOK-6C) before a terminal, and predecessor exact-head closure before a **same-parent** successor generation may stand (UDOK-4) — a successor generation of one logical operation being available **only before that operation's parent terminal**, so that genuinely later work is a **new logical operation with its own UDOK-1** (UDOK closure record) | Carried as a mandatory fence on every fabric build, rebuild, invalidate, plan, and query flow, with publication carried as an effect inside its build or rebuild parent (§11, §13.1, §17.6–§17.7, §18). The fabric's own projection-generation lineage is a **separate, non-collapsible** lineage and never substitutes for a UDOK operation generation (§11.0, §13.1). |
| AIC owns governing-basis verification: a current released committed authority snapshot is the prerequisite at UDOK-1 wherever an operation contract declares AIC applicable, released to a later operation only on AIC's completed current-input re-proof (AIC closure record) | Consumed as the Layer-1 prerequisite, with its exact limited meaning preserved (§13.3, §17.5). |
| Batch boundaries survive reading; every retrieval result and audit record carries the owning batch's identity (B11 §10.2, §10.5) | Carried on every entry and every result (§5.3, §7.4). |
| B1 owns the healthy retrieval-run structure, per-mode configuration, per-run audit record, and safety ceilings; every value is open; B26 owns the system-failure path — bounded retry, then stop, no degraded continuation, partial material audit-only, never pretend success (B1; Bundle 2 §8) | Consumed by reference; not re-decided, not re-valued (§12, §14). |
| Technical failures: up to 3 total attempts; live-chat gaps 10 s then 30 s; background/nightly gaps 1 min then 3 min; 7-minute live / 15-minute background episode deadline; `schedule_class` recorded, never guessed; missing class → fail closed (Bundle 1 B9 values; B9 values wiring v1.4) | Applied to fabric operations by class declaration, with no value re-chosen (§14.3). |
| §0B: one real operation → one append-only record; no log about logging; a log is never evidence for the truth of its subject; repetition adds no certainty; log access is governed by §7Q and §25 (Master §0B) | The logging contract of §15. |
| Canonical state records (manifests, ownership entries, coverage records, checkpoints) are machine facts, not extra operational logs and never extra evidential votes (B11 §14) | The canonical-record / log separation of §15.2. |
| DUMB machinery cannot interpret; SMART machinery cannot close an interpretation into fact (Master §0A) | The binding DUMB statement of §3.3. |
| Chroma `nh_roots_v1` is the current active semantic index and is proven in production — do not destroy, merge, or modify; `nh_reality_core`, `nh_test_asm`, `nh_simulation_core` are retained and untouched (Master §5/§16; Defaults; `cursorrules`; map C-INDEX) | Preserved as a compatibility surface only, with no action authorized (§16). |
| The five additions must not create a second competing architecture, a parallel authority path, or a model-controlled substitute for Ness; where an addition shares mechanics with an accepted package it must reuse, unify, or reference the accepted mechanism (Five-Additions §2, §3) | Every shared mechanism here is referenced to its accepted owner, never rebuilt (§3.2). |

---

## §3 — Purpose, ownership, and non-ownership

### §3.1 Purpose (one sentence)

The fabric is the **derived, rebuildable projection-and-query layer** that
lets N.H *find* preserved material through several clearly separated,
separately typed forms of structure — and lets every retrieval be inspected
afterwards — **without any index ever becoming memory, truth, identity,
connection, permission, or authority**.

### §3.2 What the fabric owns (and nothing more)

1. **Channel definitions** — which projection channels exist, what each may
   draw from, and under which ruleset and protection scope (§5.1).
2. **Index-generation manifests** — the versioned, lifecycle-tracked identity
   of each built projection generation and the exact source state it covers
   (§5.2).
3. **Index entries** — reference-only, typed projection rows pointing at
   canonical objects and their bases (§5.3).
4. **Coverage and health facts** — the fabric's own detection and honest
   marking of degraded, stale, missing, or conflicting projection state, and
   its registration of that state through B11's LB7 (§6).
5. **Query-result manifests** — one per consulted channel, per query (§12.3).
6. **Retrieval-plan provenance** — one canonical plan record per
   answer-producing or decision-support operation (§12.2).
7. **Its own recovery records** — checkpoints, failure facts, recovery
   dispositions, and the **membership-fence-violation records** that durably
   preserve any discovery of child owner work performed before its required
   same-generation UDOK-2 registration (§14, §18). Recording a violation is
   not resolving it: UDOK still owns membership, closure, and terminal truth,
   and the owning component still owns its own effect.

### §3.3 What the fabric never owns (binding)

The fabric owns **no** canonical memory; **no** identity; **no** connection
acceptance; **no** truth, certainty, or firmness; **no** relevance meaning;
**no** privacy or access permission; **no** action authority; **no** retry
policy; and **no** source lifecycle.

Concretely, each of those stays with its accepted owner: roots, batches, and
ownership with B11 and the root store; capture, eligibility, and pre-ingest
lifecycle with §7E (and the TSC extension); readings, rereadings, and
acceptance with §7G/§7H/C-READ, B10, and B24; quarantine and promotion with
B16; holds with B-HOLD; tellings, themes, clashes, and Person-Boxes with A2,
§7K, §7J, §7L and Bundle 3; Living State, world model, Computed View, and the
action ladder with §7D/§7M/§7N/§7P and Bundle 4; privacy, exclusion,
restriction, redaction, deletion, and influence removal with §7Q, A7, and B7;
access and multi-speaker scope with SACL/PBR, BAI, and §25; relevance modes
and declarations with §7R and A4; retrieval parameters, ceilings, and the
healthy-run audit record with B1; retrieval system-failure behavior with B26;
retry classification, admission, and lineage with B9; operation identity,
generation structure, **child-membership registration (UDOK-2), the
generation-scoped membership head, its single-winner closure (UDOK-6C), the
same-parent pre-terminal successor-generation transition (UDOK-4), the parent
terminal (UDOK-7), and the establishment of a new logical parent operation
(UDOK-1)**, checkpointing, and terminal evidence with UDOK; and
governing-authority verification — the **current
released committed AIC authority snapshot** required at UDOK-1 wherever this
design's operation contracts declare AIC applicable — with AIC.

**The AIC snapshot's meaning is exactly and only governing-basis proof.** It
is **never** a permission, **never** a privacy authorization, **never** a
retry admission, **never** an operation identity, and **never** evidence that
an operation succeeded. **UDOK-2 is only a membership/spawn fence**: it grants
nothing, classifies nothing, and authorizes no effect. The fabric consumes
both by reference and establishes, repairs, releases, or re-proves neither.

**DUMB statement (binding):** the fabric projects, stores references,
locates, orders within a declared channel, records, and reports. **It never
interprets meaning, establishes truth, decides relevance, merges an identity,
admits a connection, grants a permission, changes a source, or authorizes an
action.** Every fabric record is a machine/provenance fact. Ranking or
presence in any channel means *this retrieval route surfaced this reference*
— nothing else.

### §3.4 Upstream and downstream

**Upstream (read-only, by reference):** canonical roots and readings and the
B11 registries; §7E/TSC provenance records; accepted Origin, connection,
Story, telling, theme, clash, and Person-Box records; Bundle 4 Living-State,
world-model, and Computed-View records; §7Q/A7/B7 privacy and influence
records; SACL/PBR and §25 access decisions; §0B operational records; the
**current released committed AIC authority snapshot** at UDOK-1 wherever an
operation contract declares AIC applicable (and, where AIC is inapplicable,
**no such prerequisite exists — there is no delayed or partial third case**);
and UDOK operation state, including the generation-scoped child-membership
registrations, the membership head, and its closure.

**Downstream:** per-channel query results and one retrieval plan, supplied to
B1/§7R, to LMAC, and to the authorized calling operation; projection health,
supplied to B11 registration and to the fabric's own failure records.

**No downstream edge writes upstream.** No fabric output rewrites a source,
accepts a connection, merges an identity, sets currentness, promotes
material, or creates authority (§17.2).

---

## §4 — The eight logical channel families

Exactly **eight** logical channel families exist in this design. They are
**separately typed and never blended**. Their physical realization (how many
stores, which engines, which layouts, and which subset is built first) is
implementation work that this design does not perform (§20, open items 2 and
5).

| # | Family `[proposed]` | What it projects | Typed basis it carries |
|---|---|---|---|
| 1 | `thread_positional` | exact source order, conversation neighborhood, and sequence within a recorded thread | position/adjacency facts (thread identity, ordinal/neighborhood relation) — **provenance-grade** |
| 2 | `semantic` | conceptual similarity over permitted material | similarity basis (model/version, index version, distance/score) — **interpretive; retrieval evidence only** |
| 3 | `temporal` | original source time, import time, N.H record-creation time, and validity/currentness intervals with their later evidence | which time field, its declared meaning, its interval, and its evidence reference |
| 4 | `entity_person_box` | references to people and objects, and to their Person-Box views | reference basis plus the owner's identity status (confirmed / linked / proposed / pending-unresolved), never a merge |
| 5 | `accepted_connection_graph` | **only** durable connections admitted through an accepted route | the admitting route, the accepting authority, and the connection's basis record |
| 6 | `story_theme_telling_clash` | tellings, themes and their full owner lifecycle, clashes, and their recorded events | telling identity and perspective roles; **stable `theme_id`, theme↔telling membership-link references with their owner fields, alias records, and the complete append-only B3 theme-action history (confirm, reject, rename, merge, split, leave unresolved)** — never a two-label projection; clash identity, type, and response events |
| 7 | `operational_provenance` | which process retrieved, rejected, transformed, used, or did not use material | the referenced §0B record and its outcome class — as **provenance**, never as evidence about the subject |
| 8 | `state_world` | recorded Living-State, world-model, and Computed-View material | see the three separately typed subviews below |

**Family 8 has three separately typed subviews, never one blended view:**

- `living_state_subview` `[proposed]` — Living-State nodes and edges with
  their **recorded** currentness status (`current`, `possibly_current`,
  `stale`, `currentness_unknown`, `ended_by_evidence`,
  `superseded_by_evidence`) and their recorded grounding label
  (`grounded_enough`, `partly_grounded`, `not_grounded_enough`,
  `insufficient_context`), all **copied as recorded, never computed here**;
- `world_model_subview` `[proposed]` — world-model entities with their
  **recorded** active-core membership events; membership is a distinct
  append-only lifecycle owned upstream, and the fabric never derives,
  refreshes, ages, or ends it;
- `computed_view_subview` `[proposed]` — references to **immutable**
  Computed-View snapshots and their append-only refresh/status events;
  standing/superseded/possibly-stale is **derived by the owner from those
  events**, never written onto a snapshot and never inferred by the fabric.

**Binding rules for all families:**

- **Every entry and every result retains its family and subtype.** Which
  channel produced an item is never hidden, dropped, or normalized away.
- **There is no universal blended rank.** No cross-family score, fusion,
  weighting, or unified ordering exists in this design. Ordering exists only
  *within* one channel, under that channel's declared ruleset, and each
  channel's results are returned separately (§12.4).
- **A conflict between channels is surfaced, never silently resolved.** In
  particular, a `semantic` result never overrides, repairs, replaces, or
  stands in for a `thread_positional` result; the two remain separately
  labeled end to end.
- **Family membership is not evidence.** Appearing in a channel says how the
  reference was found, never that the material is true, relevant, permitted,
  current, connected, or authoritative.

---

## §5 — Logical records

All three record types are **append-only and versioned**. A change is a new
version referencing its predecessor — never an edit. Every field name is a
logical design label `[proposed]`, not a controlled identifier (§1).

### §5.1 `fabric_channel_definition` `[proposed]`

| Field `[proposed]` | Content |
|---|---|
| `definition_identity` | Package-local logical identity of this channel definition. **Not a controlled ID**; the controlled identifier is unresolved (§20). |
| `family` / `subtype` | One of the eight families (§4) and, where the family is typed further, its subtype (including the three family-8 subviews). |
| `definition_version` | Append-only version; a new ruleset, scope, or allowed-source change is a **new version**, never an in-place edit. |
| `allowed_source_types` / `allowed_basis_types` | Exactly which canonical record types this channel may project, and which typed basis records its entries may carry. Anything not listed is not projectable by this channel. |
| `projection_ruleset_ref` | The versioned ruleset that determines how a permitted source record becomes an entry. Deterministic per (source version, ruleset version). |
| `purpose_scope` / `protection_scope` | The declared purposes this channel may serve and the protection classes it may contain. **Level-1 protected raw content is excluded structurally, in every definition** (§8.4). |
| `coverage_requirement` | What complete coverage means for this channel (which batches, ranges, or record sets must be covered before a generation may be called complete). |
| `b1_mode_refs` / `relevance_mode_refs` | References to the B1 mode configuration(s) and the §7R/A4 declaration(s) under which this channel may be queried. **By reference only** — no mode, dimension, gate condition, ceiling, or declaration content is written here. |
| `validity` / `invalidation_conditions` | The declared conditions under which generations of this definition become invalid (ruleset change, source-scope change, privacy/influence event, integrity condition). |
| `provenance` | Creating operation reference, time, and the predecessor definition version. |

A channel with no valid current definition **cannot be built and cannot be
queried** (§19).

### §5.2 `fabric_index_generation_manifest` `[proposed]`

| Field `[proposed]` | Content |
|---|---|
| `index_identity` | The logical index this generation belongs to. |
| `definition_ref` + `definition_version` | The exact channel definition and version this generation was built under. |
| `generation_identity` / `predecessor_generation_ref` | This **fabric projection generation** and the fabric generation it supersedes (append-only **fabric** lineage). The predecessor fabric generation **may belong to an earlier, already-terminated UDOK parent operation**; naming it as predecessor **never asserts that the two are UDOK generations of one logical operation** and never invokes UDOK-4 (§11.0, §13.1). |
| `lineage_kind` | Exactly one of **`genesis`** (this index's first generation), **`same_parent_successor`** (a successor UDOK generation of the same still-open logical parent, standing through UDOK-4 before that parent's terminal), or **`new_parent_generation`** (a rebuild, a post-terminal invalidation replacement, or any other genuinely later projection generation, standing under a **new logical UDOK parent** with its own UDOK-1 — **never** through a cross-parent UDOK-4). |
| `generation_lineage_discriminator` | The canonical, durably derived discriminator that distinguishes this generation from every predecessor of the same index under otherwise identical inputs. Its derivation follows `lineage_kind` exactly: for **`genesis`**, the index's **first parent establishment and build-transition evidence**; for **`same_parent_successor`**, the **predecessor fabric generation together with the valid same-parent UDOK-4 transition evidence**; for **`new_parent_generation`**, the **predecessor fabric-generation identity, the new parent's establishment evidence, and the exact committed governed rebuild or invalidation-replacement evidence**. It is **never** a nonce, a timestamp, a random value, a counter chosen at will, or any mutable authorization input, and **no cross-parent UDOK-4 transition is required, assumed, or fabricated** to derive it. |
| `lineage_evidence_refs` | The exact durable evidence the discriminator is derived from, named by kind: the predecessor fabric-generation reference where one exists; for a same-parent successor, the committed same-parent UDOK-4 transition evidence; for a new-parent generation, the **new parent operation identity and its committed UDOK-1 establishment evidence** together with the committed governed rebuild or invalidation-replacement evidence; for genesis, the first parent establishment and build-transition evidence. |
| `source_head_ref` | The **exact** source state covered: the canonical head/version set of the projected records at build time. |
| `b11_coverage_head_ref` | The exact B11 batch/coverage state at build time (which batches and which of their committed contents are inside this generation). |
| `ruleset_ref` | The exact projection ruleset version applied. |
| `protection_scope` | The protection/purpose scope this generation was built under. |
| `build_operation_ref` | The **one** UDOK parent operation and its operation generation that produced this fabric generation (§13). That single parent owns **staging, validation, atomic publication, and the post-publication B11 LB7 registration** for this generation; **publication is an effect inside it, never a separate publish parent** (§11.5–§11.6, §13.1). |
| `child_membership_head_ref` / `membership_closure_ref` | The generation-scoped UDOK child-membership head this generation's children registered into, and the single-winner **UDOK-6C** closure bound to that exact head (§11.5, §13.1). |
| `same_parent_predecessor_closure_ref` | **Only** where `lineage_kind` is `same_parent_successor`: the predecessor **UDOK generation of the same logical parent** whose committed exact-head UDOK-6C closure is revalidated at the **UDOK-4** transition commit, before that parent's terminal (§11.0). Absent for `genesis` and for every `new_parent_generation`. |
| `predecessor_fabric_history_refs` | Where the predecessor fabric generation belongs to an **earlier parent**: that generation's committed exact-head closure and its parent's committed terminal, carried as **history and lineage/recovery evidence only**. Such a cross-parent reference **never satisfies, invokes, or substitutes for UDOK-4** and never reopens the earlier parent (§11.0, §18). |
| `counts` / `watermarks` | Entry counts and the projection watermarks that make partial work measurable and resumable. **These are fabric-local, non-queryable progress facts; they are never a B11 `coverage_status` and never a registration.** |
| `integrity_refs` | Integrity evidence over the staged and published entry set. |
| `lifecycle_state` | Exactly one of **`staging` / `published` / `superseded` / `invalidated`** — append-only transitions only. |
| `publish_evidence_ref` | The atomic publication evidence (§11.5). |
| `invalidation_evidence_ref` | Where applicable: the event that invalidated this generation and its cause class. |
| `health_evidence_refs` | The coverage/health facts bound to this generation (§6). |

**Two lineages, never collapsed (binding).** A **fabric projection-generation
lineage** (this index's ordered generations, recorded by
`predecessor_generation_ref`) and a **UDOK operation-generation lineage**
(the generations *inside one logical UDOK parent operation*) are **separate
and non-collapsible**. A fabric generation may name a predecessor fabric
generation owned by an **earlier, already-terminated** parent operation
without either generation becoming a UDOK generation of the other's operation.
**UDOK-4 is reserved exclusively for a successor UDOK generation of the same
still-open logical parent, before that parent's UDOK-7 terminal**; it is never
invoked merely because two fabric generations stand in a predecessor
relationship, never used between distinct parent operations, and never used
after a parent terminal (§11.0, §13.1).

**Structural key (binding).** A projection generation's append-once structural
key is **`index_identity` + definition + source coverage head + ruleset +
projection scope + `generation_lineage_discriminator`** (§13.2). Two indexes
built from identical definitions, source coverage, rulesets, and scope
therefore never share a generation record, and a **replacement built after an
invalidation cannot reuse the invalidated generation's key** even when
definition, source coverage head, ruleset, and projection scope are unchanged
— because its lineage discriminator is derived from a different durable
predecessor-and-transition basis.

**Duplicate convergence is preserved within one genuine generation.** A retry,
a resumption, or a crash recovery that resolves the **same** `index_identity`,
the **same** predecessor and lineage discriminator, and the same remaining key
inputs — inside the **same still-open parent operation and operation
generation** — returns the **existing** manifest and its committed
checkpoints; it never creates a second record (§17.8). A **new** lineage
discriminator is available **only** from a durable governed same-parent
successor transition, or from a **new logical parent** standing an
invalidation-replacement or rebuild — **never merely because a caller asks to
try again**, and never by generating a fresh value to escape convergence.

**Lifecycle rules:** a generation is queryable **only** while `published`
**and** only after its committed B11 LB7 `index_registration` (§6.1). A
`staging` generation is **never queryable, never participates in unified
reading, has no B11 LB7 `index_registration`, and makes no B11 coverage
claim** — its progress lives only in fabric-local records (§6.3). A
`superseded` generation remains preserved history and is never edited or
deleted. An `invalidated` generation is **never re-published and its key is
never reused**; a replacement is a **new generation standing on a new lineage
discriminator** — under a **same-parent UDOK-4 successor** only while the
original parent is still open and pre-terminal, and otherwise under a **new
logical UDOK parent with its own UDOK-1**, which never reopens or re-terminates
the earlier parent (§11.0, §18 rows 1–2 and 4f).

### §5.3 `fabric_index_entry` `[proposed]`

| Field `[proposed]` | Content |
|---|---|
| `generation_ref` | The generation this entry belongs to. An entry never floats free of a generation. |
| `canonical_object_ref` + `canonical_object_type` | The canonical identity and type of the projected object (root, reading, telling, theme, clash, Person-Box, connection, state node, world entity, Computed-View snapshot, operational record, …). |
| `owning_batch_ref` / `location_ref` | The owning batch identity (B11) and the registry-resolved location descriptor. Batch identity travels with every entry and every result. |
| `channel_family` / `channel_subtype` | Never dropped, never normalized away. |
| `typed_basis_record` | The channel-appropriate basis: position/adjacency facts, similarity basis with model and index version, time field and interval with declared meaning, entity-reference basis with the owner's identity status, accepted-connection route and authority, Story/state status as recorded — **for a theme, the stable `theme_id`, the relevant membership-link identities, the alias records, the source and resulting theme identities for a merge or split, and references to every applicable theme-action event** (§10.1) — or the referenced operational record. |
| `source_version_ref` / `source_integrity_ref` | The exact source record version and integrity evidence the entry was derived from. |
| `provenance_time_refs` | Source time, import time, and record-creation time kept **distinct**; unknown time stays unknown (§7.3). |
| `protection_refs` | The protection classification and, where applicable, the **opaque protected-record reference** — never protected content (§8.4). |

**Binding:** an entry is a **reference and derived search material**. It is
never the sole surviving copy of any memory, never a substitute for the
canonical record, never editable in place, and never an evidential vote about
its subject. Every entry points to canonical identity and canonical basis;
**no index owns source, identity, connection, or batch truth.**

---

## §6 — Coverage, health, and B11 registration

### §6.1 Registration through B11 LB7

Unified-reading participation is downstream of **both** facts, in this order
and never otherwise: **(a)** the generation's atomic publication (§11.5), and
**(b)** a committed B11 **LB7 `index_registration`** — `{batch_id,
index_identity, registered_at, coverage_status, evidence refs}` — exactly as
B11 defines it. The fabric supplies the index identity, the generation
reference, and the evidence; **B11 remains canonical for root and batch
ownership, uniqueness, and registration.** The fabric never supplies
uniqueness or ownership authority and never registers a coverage claim it
cannot evidence.

**A staging generation has no LB7 registration, no B11 `coverage_status`, no
unified-reading participation, and no query eligibility** — there is no
partial, provisional, non-queryable, or pre-registration variant of LB7 in
this design. A **published-but-unregistered** generation is likewise
non-participating until lookup-first recovery appends the missing
registration idempotently; **recovery never republishes** (§18 row 3).

### §6.2 Coverage states (B11's exact vocabulary, unchanged)

Per batch, per index: **`complete` / `partial` / `stale` / `missing` /
`conflicting`**. These are B11's states, used here with B11's meaning and
**only for a registered batch/index relationship that already exists** — that
is, only after publication and LB7. Within that registered relationship the
fabric **detects and marks honestly**; it never hides a gap, never claims
completeness it cannot evidence, and never silently omits a batch. Later
degradation, reconciliation, or re-verification may change the recorded B11
coverage state for that relationship. **Staging progress alone never supplies
a B11 coverage state of any value, including `partial`.** What a consumer
does with degraded coverage is **B1/B26 and the consumer's** decision, not the
fabric's.

### §6.3 `fabric_coverage_health_event` `[proposed]`

Each coverage or health fact binds: the **generation**; the **affected
batches or ranges**; the **condition** (which coverage state, or which health
condition — loss, corruption, staleness, integrity mismatch, protection-scope
violation, basis unreadability); the **evidence**; the **operation reference
and time**; and the **recovery disposition** (what was done, or that the
condition is unresolved and recovery-required). Events are append-only; a
later event supersedes an earlier disposition without editing it.

**Before publication, this record — together with the generation manifest,
the fabric-local checkpoints, and the watermarks (§5.2, §11.3) — is the
only place partial projection progress is recorded.** Every such fact is
explicitly labelled **fabric-local and non-queryable**. It is not a B11
`coverage_status`, not an LB7 registration, not participation-visible, and it
never makes a staging generation participate in unified reading.

### §6.4 What coverage is not

Coverage is a **structural fact about projection**, never a statement about
the truth, completeness, importance, or permissibility of any material. A
`complete` coverage status never means "everything relevant was found"; it
means the declared coverage requirement of that channel definition is
evidenced for those batches at that generation.

---

## §7 — Provenance preserved by reference

### §7.1 Roots, readings, rereadings, and tellings

All are projected **by reference only**. Roots remain immutable; readings and
rereadings remain linked additions; tellings remain their own immutable
first-class cards with their own stable `telling_id`, each retaining its
parent reading and supporting roots. The fabric copies **no** content into a
position of authority, edits nothing, and creates no derived "canonical"
variant of any of them.

### §7.2 Origins and mixed media

**Every real item remains its own Origin.** The fabric never merges two
Origins, never treats a message and its attached media as one Origin, and
never derives an Origin from similarity, adjacency, or shared model output.
Mixed media are connected **only** through the separate append-only
`origin_relationship_record`s owned upstream; the fabric projects those
relationship records as what they are and never manufactures one.

### §7.3 Time

Source time, import time, and N.H record-creation time remain **distinct
fields with distinct declared meanings** in every temporal entry and every
result. **Unknown time stays unknown** — never defaulted, never backfilled,
never approximated from a neighbour, and never silently replaced by import or
record time. Validity/currentness intervals are projected as recorded, with
their later evidence, and are never recomputed here.

### §7.4 Batch identity

Every entry and every cross-batch result carries the **owning batch's
identity**. Batch boundaries survive projection and retrieval; roots are
never flattened, merged, copied, or re-homed to produce unified reading. One
memory system, separate immutable boxes.

---

## §8 — Purpose scoping, privacy, and access

### §8.1 Gate order (carried unchanged)

1. **Current §7Q authorization for the exact declared purpose** is obtained
   **before** candidate material is assembled and **before** any content or
   semantic ranking occurs. Nothing becomes a candidate merely by being
   similar, recent, or adjacent.
2. **SACL/PBR supplies permitted scope before retrieval** in multi-speaker
   contexts; access level and PBR categories are consumed as supplied.
3. **§7R/B1 mode validation**: a consuming component without a valid A4
   declaration for the current purpose has no relevance mode to run — so the
   corresponding channel query does not run either.
4. **Visible candidates are privacy-filtered before ranking**, and whatever is
   later surfaced still passes the pre-output review in its settled order:
   **§7Q first, SACL/PBR second**. Neither gate widens or replaces the other;
   the fabric performs neither and bypasses neither.

**No fabric parameter widens access.** A channel's `purpose_scope` and a
query's permitted scope can only **narrow** use inside what §7Q already
authorized.

### §8.2 Withheld material never signals itself

Filtering leaves **no observable trace** in a result that would reveal the
existence, quantity, shape, or location of restricted material. Omission
counts and reasons recorded in plan and result provenance are **governed
records** subject to §7Q and §25 access rules — never a side channel and
never surfaced as "there is something here you cannot see."

### §8.3 Owner-held fences respected at the seam

Held, quarantined, unpromoted, rejected, provisional, sealed-TSC, simulated
or Wonder-origin, and unauthorized material is **never** silently mixed with
ordinary evidence. The fabric consumes the owner's recorded lifecycle status
and refuses to project or return material whose status does not permit that
use. It never promotes, releases, or reclassifies anything.

### §8.4 Level-1 protected material (structural exclusion)

**Level-1 raw content never enters an ordinary index, embedding, entry,
log, query result, plan, or context package** — not in whole, not in part,
not in a derived form from which it could be reconstructed. Only the **stable
opaque protected-record reference** may cross the protected-execution
boundary, and only for operations already authorized to hold it. No channel
definition may declare a protection scope that would admit Level-1 raw
content; a definition attempting it is invalid and never builds (§19).

### §8.5 Deletion, redaction, restriction, and influence removal

A deletion, redaction, restriction, or influence-removal event imposes an
**immediate suppression fence** and, where the event's scope reaches projected
material, an **invalidation fence** on the affected generations:

- suppression takes effect at the query boundary **immediately**, before and
  independently of any rebuild — an unsuppressed stale generation is never
  queried on the assumption that a rebuild is coming;
- affected generations transition to `invalidated` with the event as
  evidence; the rebuild is **governed work** performed under the owner's
  instruction, not an autonomous fabric decision;
- **visible suppression and internal influence removal remain separate
  operations with separate records** — the fabric performs neither and merges
  neither;
- no source record is deleted, rewritten, or reconstructed by any of this;
  the fabric only stops projecting and marks honestly.

---

## §9 — Identity and connection discipline

### §9.1 What never creates identity or a connection (binding)

**Similarity, temporal proximity, repetition, co-retrieval, co-occurrence in
one result, theme proximity, shared model output, shared embedding
neighbourhood, or shared position in any ranking never creates — or
contributes to creating — an identity, a merge, or a connection.** There is
no threshold, no accumulation rule, and no promotion path anywhere in this
design by which retrieval behaviour becomes a relationship.

### §9.2 The accepted-connection graph

Family 5 contains **only** durable connections **already admitted through an
accepted route**, and each edge carries its **authority and basis record**
(which route admitted it, on what basis, and under whose authority). The
fabric adds no edge, strengthens no edge, weights no edge, and infers no
transitive edge. An edge's absence is never evidence that no relationship
exists; an edge's presence is never evidence that a claim is true.

### §9.3 Entity and Person-Box channels

Family 4 projects **references and the owner's recorded identity status**
without merging: a confirmed Person-Box, a linked reference, a proposed link,
or a **pending unresolved identity anchor kept unconfirmed** are each
projected as exactly what they are. Similar names, similar content, and
co-retrieval never satisfy any identity test. The fabric proposes no merge,
resolves no anchor, and never presents two references as one person or object.

### §9.4 Proposals stay proposals

Proposed themes, proposed relationships, proposed links, and model-produced
suggestions are **typed as proposals** in every entry and every result. They
**never** appear in the accepted-connection graph, never acquire accepted
status by being retrieved, and never gain weight through repetition — a
proposal retrieved a hundred times is still one proposal.

---

## §10 — Story, state, and world projected exactly as owned

### §10.1 Story layer

Projected as recorded, never inferred: **telling identity** (`telling_id`),
the separate **perspective roles** kept separate (root speaker, subject,
perspective owner, attribution path where the source supports it), the
**parent reading** and **supporting roots**, and the recorded firmness label
where present (and its honest absence where not). Conflicting tellings are
never merged and no winner is selected.

**Themes** are projected as their **whole owner lifecycle**, never as a
status label. Every family-6 theme entry and every family-6 query result
retains: the **stable `theme_id`**; the **theme↔telling membership-link
identities** with their settled owner fields (what / why / who-established /
certainty / timestamp); the **alias records**; the **source and resulting
theme identities** for a merge or a split; and **references to every
applicable theme-action event**. Each of the settled B3 actions is preserved
as its own distinct append-only owner event and none is collapsed into
another:

- **confirm** — recorded **only** from a Ness response; the confirmation
  event is the only thing from which a `confirmed` presentation derives.
  Repetition, frequency, co-retrieval, and passage of time confirm nothing.
- **reject** — a recorded Ness rejection event that **deletes neither the
  theme nor its membership links**; the theme, its links, its aliases, and
  its history remain projected and navigable, and the rejection is visible as
  a rejection.
- **rename** — a **new label or alias through a new event** with **every
  older label preserved**; nothing is renamed in place and no older link or
  telling is rewritten.
- **merge** — records the **relationship** between the source `theme_id`s and
  the resulting current navigation grouping **without deleting, copying, or
  rewriting** the source themes or their old membership links; the sources
  and their full histories stand and stay navigable.
- **split** — records the source theme, the resulting `theme_id`s, and the
  membership-link changes through new events, while the **earlier grouping
  and its full history remain preserved**.
- **leave unresolved** — performs **no** hidden transition: no automatic
  confirmation, no rejection, no aging result. A proposed theme may stay
  proposed indefinitely, and nothing in the fabric moves it.

**The currently visible navigation state is only an owner-derived view of
that preserved event history.** This design defines **no replacement status
enum** for themes, and **no bare `proposed` or `confirmed` label may conceal
a rejection, a rename, a merge, a split, or an unresolved disposition**. A
proposed theme never appears as confirmed and never silently shapes another
channel's ordering; historical labels, links, groupings, and source themes
remain navigable in every case.

**Clashes** are projected as their own records — clash identity, one of the
six clash types, and the involved items — and **Ness-response events are
separate records**, never folded into the clash and never presented as
resolving it. A clash-involved item remains marked wherever it is surfaced.
The fabric never creates, merges, closes, or resolves a clash, and
re-detection never produces a second clash record through any fabric route.

### §10.2 Living State and world model

**Recorded currentness** and **recorded grounding labels** are copied as
recorded (§4, family 8). The fabric never computes, promotes, ages, refreshes,
ends, or supersedes a state; **time alone never proves anything** here.
**World active-core membership** is projected from the owner's append-only
membership events; the fabric never derives membership and never treats
retrieval, similarity, or surfacing as membership.

### §10.3 Computed View and the forbidden edge

Computed-View snapshots are projected as **immutable references**, with
standing/superseded/possibly-stale left to the owner's derivation from its
append-only refresh/status events. The fabric writes no status onto a
snapshot and creates no snapshot.

**Permanently forbidden:** **§7M never feeds §7D as evidence.** No fabric
channel, entry, result, plan, or log may carry Computed-View material back
into Living-State evidence, and no fabric route may turn a relevance score,
governance result, privacy status, or operational log into evidence about a
subject.

---

## §11 — Build and rebuild lifecycle

One build or rebuild produces **one versioned generation** through the
following ordered stages. Each stage is durable before the next begins; each
is idempotent under the fabric key of §13.2.

### §11.0 Stand the generation (parent boundary, UDOK-1, and the same-parent UDOK-4 prerequisite)

**Which parent stands this generation (binding).** Exactly one of three paths
applies, and they are never mixed or substituted:

1. **Initial build (`genesis`).** A **new logical UDOK parent operation** with
   its **own UDOK-1** and its own initial operation generation.
2. **Same-parent successor (`same_parent_successor`).** A successor **UDOK
   generation of the same logical parent**, standing through **UDOK-4** while
   that parent is **still open and pre-terminal**.
3. **New-parent generation (`new_parent_generation`).** Every routine
   **rebuild**, every **post-terminal invalidation replacement**, and every
   other genuinely later projection-generation creation stands as a **new
   logical UDOK parent operation** with a **fresh parent identity, its own
   UDOK-1 proof, and its own generation-scoped membership head, UDOK-6C
   closure, terminal, acknowledgement, and one-operation/one-log record**. It
   **never reopens, regenerates, resumes, or issues another terminal for the
   earlier parent**, and it **never asserts a cross-parent UDOK-4**.

The fabric predecessor is preserved in every case: a new-parent generation
carries the **predecessor fabric-generation reference** and the earlier
parent's **committed terminal** as history (`predecessor_fabric_history_refs`,
§5.2). That historical evidence contributes to fabric lineage and to recovery
proof; it **never satisfies, invokes, or substitutes for UDOK-4**.

**AIC prerequisite.** Where this design's operation contract declares AIC
applicable to the operation, the **current released committed AIC authority
snapshot is mandatory at that generation's UDOK-1, before any governed work**.
A same-parent successor generation **repeats that proof** wherever AIC still
applies, and a **new logical parent proves it at its own UDOK-1** — an earlier
parent's proof is never inherited across the parent boundary. Where AIC is
inapplicable, the prerequisite is simply **absent — there is no delayed,
deferred, or partial third case**. Release of an existing snapshot to a later
operation requires **AIC's own completed current-input re-proof**; missing,
unreadable, unproved, or unreleased snapshot evidence **fails closed at
UDOK-1**, and changed or unprovable inputs route **only** through AIC's own
fresh-establishment and successor-generation mechanics — never through a
fabric workaround.

**Same-parent successor prerequisite (UDOK-4).** A successor **UDOK
generation of the same logical parent** may stand **only** if the predecessor
**UDOK generation of that same parent** has a **committed UDOK-6C closure**,
and the transition commit **revalidates** that the closure belongs to that
predecessor generation and still binds its **exact, unchanged, current
membership head**, together with every other transition prerequisite UDOK
binds there. A successor **cannot stand over an unclosed or unresolved
predecessor**, and a same-parent successor is **unavailable once that parent
has reached its UDOK-7 terminal** — later work is then path 3, never a
reopened parent.

### §11.1 Resolve

Resolve the **exact** source head/version set, the **exact** B11 coverage
head, the **exact** channel definition and ruleset version, and the protection
scope. An unresolvable or ambiguous head, definition, or ruleset **stops the
build** (§19) — it is never approximated.

### §11.2 Stage

Entries are written to a `staging` generation. **Staging is never queryable,
never participates in unified reading, never carries an LB7 registration, and
never counts toward — or supplies — any B11 coverage state** (§5.2, §6.1).

### §11.2A Register every child before its work (UDOK-2)

**Every generation-scoped child of this build must commit its UDOK-2
registration before that child's owner work begins.** Registration uses the
generation-scoped append-once basis **{parent operation, generation, child
owner, child identity}**; a registration under **another** generation never
satisfies the current generation. This applies to every child without
exception — per-batch projection units, per-channel queries, **the B11 LB7
`index_registration` child of this build or rebuild parent** (registered
here, under this parent's current generation and **before** UDOK-6C closes
membership, even though its owner effect runs only **after** atomic
publication, §11.5–§11.6), and any other owner effect represented as a child.

**One append-only child-membership head exists per generation**, and every
committed UDOK-2 registration advances it. The race resolves in exactly two
ways and no other: **child-first** — the registration advances the head before
closure and the child is included; **closure-first** — the closure refuses the
late registration and that child has **no owner work under the closed
generation**. **Work or effect first, registration afterwards, is never
valid.**

**If effect-first work is nevertheless discovered, it is a membership-fence
violation and is permanently recorded as one.** Reconciliation from owner truth
is available only within the narrow open-generation path of §18 row 4a, and
even there it only makes the existing child visible to completion accounting —
it **never** makes the pre-work fence retroactively satisfied, never makes the
effect lawful, and never turns this into a permitted work-first /
register-later route. Every later membership and completion trace keeps a
**fence kept** distinguishable from a **fence violated and reconciled** (§18,
§19.2).

### §11.3 Project idempotently with checkpoints

Projection proceeds in resumable units with durable checkpoints and
watermarks — each unit a registered child under §11.2A. Re-running a unit
re-derives the identical entries for the same (source version, ruleset
version) pair; a repeat commits nothing new. Checkpoints and watermarks are
**fabric-local, non-queryable progress facts** (§6.3).

### §11.4 Validate

Before publication, validate: **coverage** against the definition's coverage
requirement; **integrity** of the staged set; **privacy/protection scope**
(including the structural Level-1 exclusion); and **relationship bases** —
every accepted-connection edge, entity reference, Story status, and state
status must resolve to its canonical basis. Any validation failure stops the
publication (§19); it never downgrades into a partial publish.

### §11.5 Close child membership, then publish atomically

**Before publication — and before any parent terminal — a single-winner
UDOK-6C closure must be committed and bound to the generation's exact current
membership head**, and that head must be **revalidated as readable and
unchanged** at the publication commit. **Required-child terminals are resolved
against that exact closed head**, which is the same head used for
required-terminal determination. Publication may **never** narrow its
obligations after a child failure and may **never** close around an
unregistered child. A missing closure, an unreadable head, an advanced head, or
a head that contradicts the closure **stops the publication** (§18, §19).

Then **exactly one generation is published in one atomic transition**
(`staging → published`), which simultaneously marks its predecessor
`superseded`. There is no half-published generation, no entry-by-entry
switchover, and no window in which two generations of one index are both
current.

**Publication is an effect inside this build or rebuild parent — never a
separate publish parent operation** (§13.1). The closed membership head
therefore already includes the **B11 LB7 registration child** registered under
§11.2A, whose owner effect follows publication (§11.6); closure never happens
around it and the required set is never narrowed to exclude it.

### §11.6 Register coverage through B11

**After** publication — and **still inside the same build or rebuild parent**
— the pre-registered B11 LB7 child performs its owner effect: registration
through **B11 LB7** with the honest `coverage_status` (§6). This is the first
and only point at which a B11 coverage state for this generation exists.
Registration is idempotent; a missing post-publish registration is appended by
recovery **under that same still-open parent**, never re-derived by guess and
never satisfied by republication (§18 row 3). Until it is committed, the
published generation **does not participate in unified reading**.

**The parent terminal waits for it.** The build or rebuild parent may reach
its terminal **only** after the **supported B11 child terminal reference** and
**every other required child terminal** are resolved against the **exact
closed membership head** of §11.5. If a parent is found already terminated
**without** the required B11 completion, the terminal and the contradiction
are **preserved as history** and the closure-bound **fail-closed resolution
seam** applies (§18 row 3, §19): the parent is **not reopened**, no
same-operation successor is manufactured, and any genuinely later work stands
as a **new logical parent** (§11.0 path 3).

### §11.7 Source independence (binding)

**Source commits never wait for, block on, or roll back for indexing.** A
projection failure never uncommits, deletes, rewrites, or reconstructs a
source record. **Partial or failed projection work changes no source and can
never claim completeness** — it is honest partial work, recorded **only in
fabric-local manifest, checkpoint, watermark, and health records** (§6.3),
marked, not query-eligible, carrying **no LB7 registration and no B11
coverage state**, and either resumed or invalidated (§18).

---

## §12 — Query, retrieval plan, and channel results

### §12.1 What a query is

A query is a **purpose-scoped, gate-preceded, generation-pinned read of one
channel**. There is no fabric operation that "searches memory" generally.

### §12.2 `retrieval_plan_record` `[proposed]` — one canonical plan per operation

Exactly **one** plan record per answer-producing or decision-support
operation, carrying:

| Field `[proposed]` | Content |
|---|---|
| `plan_identity` / `parent_operation_ref` / `plan_generation` | The plan's identity, its parent operation, and `plan_generation` — **the durable generation of that parent operation**, not a fabric-chosen counter. A superseding plan for a **changed** operation generation is a **new record**, never an edit. |
| `declared_purpose` | The exact declared purpose (one of the settled §7R purpose-type vocabulary, consumed, never redefined). |
| `b1_mode_ref` / `b1_configuration_version` | The B1 mode and configuration in force, by reference. |
| `target_ref` / `context_ref` | What the retrieval is for. |
| `permitted_scope` | The permitted privacy/access/source scope obtained from §7Q (and SACL/PBR where applicable) **before** candidate assembly. |
| `channels_required` / `channels_omitted` / `channels_consulted` | Named explicitly and separately, each omission with its reason. |
| `pinned_definitions` / `pinned_generations` / `pinned_health_and_coverage` | Exactly what was queried and in what structural condition. |
| `parameters` / `ceilings_in_force` | The applied parameters and the B1 ceiling set in force, by reference; every value stays B1's and the tuning path's. |
| `channel_result_refs` | One reference per consulted channel (§12.3), each a **generation-scoped child registered under UDOK-2 before its query work begins** (§11.2A). |
| `child_membership_head_ref` / `membership_closure_ref` | The plan generation's child-membership head and the single-winner **UDOK-6C** closure bound to that exact unchanged head, against which the required-channel terminals are resolved (§11.5, §12.4A). |
| `same_parent_predecessor_closure_ref` | **Only** where this plan generation is a successor **UDOK generation of the same still-open parent operation**: that predecessor generation's committed exact-head UDOK-6C closure, revalidated at the **UDOK-4** transition commit and **before that parent's terminal** (§11.0). A plan belonging to a **different** parent operation is never a UDOK-4 successor of an earlier plan — it stands under its own parent, with its own UDOK-1 and its own plan key. |
| `retrieved_ids` / `retrieved_bases` | The canonical identities returned and their typed bases. |
| `exclusions` / `omissions` / `truncations` | What was cut, and by which limit, ceiling, gate, or scope. |
| `outcome_state` | Explicitly one of: normal, **genuine empty**, failed, degraded, or incomplete — never conflated. |
| `evidence_offered` / `evidence_passed` / `evidence_finally_used` | Kept as three **distinct** facts. |

**Structural key (binding).** A retrieval plan's append-once structural key is
**`parent_operation_ref` + `plan_generation` + requester + purpose +
target/context + B1 configuration** (§13.2). Replay **within one parent
operation generation** therefore converges on the existing plan record, while a
**lawful successor plan for a changed operation generation derives a distinct
append-once key** even when requester, purpose, target/context, and B1
configuration are unchanged. `plan_generation` is read from the parent
operation's durable generation; the fabric never invents, increments, or
re-labels it to obtain a new plan.

The plan is **operational provenance**, never a second evidential vote for
the material it references (Five-Additions §17).

### §12.3 `fabric_channel_query_result` `[proposed]` — one per consulted channel

Carries: its **UDOK-2 child registration reference under the plan's
generation** (committed before the query work began, §11.2A); the **pinned
generation** (and its definition/ruleset versions); the **parameters actually
applied**; the **ordered references** produced by that channel with their
typed bases — **for family 6, the full theme lifecycle material of §10.1, not
a status label**; the **omissions** and their reasons; and the **terminal
outcome** for that channel. Results are committed per channel and referenced
by the plan; a channel that was not consulted has no result record and is
recorded as omitted with a reason.

Only a **published and LB7-registered** generation may be pinned (§6.1); a
staging generation is never pinned, never queried, and never returned.

### §12.4 Ordering, gates, and who decides what

**Channel ordering stays separate**: each channel orders only within itself,
under its own declared ruleset. There is no cross-channel merge, fusion, or
blended score anywhere.

**B1/§7R and the consuming component own** the gates, the relevance
dimensions, the limits and ceilings, the ranking rules, the fallback
behaviour for a genuine empty result, and everything about surfacing. The
fabric supplies pinned, provenanced, separately-typed channel results and the
plan that records what happened — and decides none of those.

### §12.4A Membership closure before the plan terminal

The plan's terminal requires a committed **single-winner UDOK-6C closure bound
to the plan generation's exact current membership head**, revalidated as
readable and unchanged at the terminal commit. **Required-channel terminals
are resolved against that exact closed head** — the same head used for
required-terminal determination. A plan may never narrow its required set
after a channel failure and may never close around an unregistered channel
child. A missing closure, an unreadable head, an advanced head, or a
contradiction between head and closure **blocks the terminal and the final
context** and fails closed (§18, §19).

### §12.5 Logging relationship

Plans, results, manifests, entries, coverage facts, checkpoints, and failure
facts are **canonical records**. They are referenced by **one** §0B log for
the operation — they are never additional logs, never duplicated evidence,
and never a second vote (§15).

---

## §13 — Operation identity and gate layering

### §13.1 UDOK binding

Every build, rebuild, health, invalidation, plan, and channel-query operation
is bound to **UDOK** as its durable-operation owner: **one UDOK parent
operation** per **build**, per **rebuild**, per **invalidation**, and per
**retrieval plan**, with **generation-scoped children** for per-batch
projection units, per-channel queries, the **B11 LB7 registration child**, and
any other owner effect carried as a child. **Publication is an effect inside
its build or rebuild parent — there is no separate publish parent operation**
— and that one parent owns **staging, validation, atomic publication, and the
post-publication B11 LB7 registration** for the fabric generation it produces
(§11.5–§11.6). UDOK owns
operation identity, parent/child structure, checkpoints, waiting and
cancellation, one-winner commits, stale-result rejection, lookup-first
recovery, and terminal evidence. This design **references** that ownership; it
does not restate, extend, or constrain UDOK's interior, and it creates no
parallel execution path around any component's canonical seam.

**The four UDOK fences this design carries on every flow — build, rebuild,
publication inside its build or rebuild parent, invalidate, retrieval plan,
and channel query:**

1. **UDOK-2 before work.** Each generation-scoped child commits its
   registration under **{parent operation, generation, child owner, child
   identity}** *before* that child's owner work begins. A registration under
   another generation never satisfies the current generation. **UDOK-2 is a
   membership/spawn fence only** — it grants nothing and classifies nothing.
2. **One head, one exact-head closure (UDOK-6C).** Each generation has one
   append-only child-membership head advanced by every committed UDOK-2
   registration. Required-terminal determination reads **that same head**, and
   a **single-winner UDOK-6C closure binds its exact current value** before
   any publication or parent terminal, revalidated as readable and unchanged
   at the commit.
3. **Predecessor closure before a same-parent successor (UDOK-4).** A
   successor **UDOK generation of the same logical parent** stands only over a
   predecessor generation **of that same parent** whose committed exact-head
   UDOK-6C closure is revalidated at the transition commit, and **only while
   that parent is open and pre-terminal**. UDOK-4 is **never** invoked because
   two *fabric* generations stand in a predecessor relationship, **never**
   used between distinct parent operations, and **never** used after a parent
   terminal.
4. **A new logical parent for genuinely later work (UDOK-1).** Every routine
   rebuild, every post-terminal invalidation replacement, and every other
   genuinely later projection-generation creation stands as a **new logical
   UDOK parent** with a fresh parent identity, its own UDOK-1 proof, and its
   own membership head, closure, terminal, acknowledgement, and one-operation
   log. It **never reopens, resumes, regenerates, or re-terminates** the
   earlier parent, and it preserves the **predecessor fabric generation** and
   the earlier parent's committed terminal as history (§5.2, §11.0).

**Race resolution is exactly two-way:** child-first (head advances before
closure; the child is included) or closure-first (the late registration is
refused; that child has no owner work under the closed generation). **Effect
before registration is never valid**, and no fabric path backfills membership
into a closed or superseded generation (§18).

**A violated fence stays visibly violated.** Where effect-first work is
discovered, the open-generation reconciliation of §18 row 4a may append the
missing same-generation UDOK-2 registration and the UDOK-6 terminal references
that owner truth supports, but a **distinct durable
membership-fence-violation record** is appended with it and preserved
independently of ordinary membership accounting. Membership, closure, and
terminal truth remain **UDOK's**; the effect remains the **owning
component's**; and no reconciliation makes the pre-work fence retroactively
satisfied.

### §13.2 Fabric-owned structural keys (binding)

| Object | Structural key `[proposed]` |
|---|---|
| Channel definition | family/subtype **+** definition version |
| Generation | **`index_identity`** **+** definition **+** source coverage head **+** ruleset **+** projection scope **+** `generation_lineage_discriminator` (§5.2) |
| Entry | generation **+** canonical object **+** channel/subtype **+** typed basis |
| Retrieval plan | **`parent_operation_ref`** **+** **`plan_generation`** **+** requester **+** purpose **+** target/context **+** B1 configuration (§12.2) |
| Channel query | plan **+** channel **+** pinned generation |

**Successors are mechanically distinguishable without weakening duplicate
convergence.** The generation key carries `index_identity` so two indexes with
identical definitions, coverage, rulesets, and scope never collide, and it
carries the **`generation_lineage_discriminator`** so a **replacement built
after an invalidation**, a **lawful same-parent successor**, and a **rebuild
standing under a new logical parent** each derive a **distinct** append-once
key from the record they are required not to reuse.
The plan key carries the **parent operation and its durable
`plan_generation`** so a **successor plan for a changed operation generation**
derives a distinct key. Within one genuine generation — same index, same
predecessor and discriminator, same remaining inputs; or the same parent
operation generation for a plan — replay still converges on the existing
record (§17.8).

**The lineage discriminator is derived evidence, never a freshness trick, and
it is fabric lineage — not UDOK operation lineage.** Its derivation follows the
generation's `lineage_kind` exactly (§5.2, §11.0): **genesis** — the index's
first parent establishment and build-transition evidence; **same-parent
successor** — the predecessor fabric generation plus the valid **same-parent
UDOK-4** transition evidence; **new-parent generation** — the predecessor
fabric-generation identity plus the **new parent's establishment evidence**
plus the exact committed governed rebuild or invalidation-replacement
evidence. A **nonce, timestamp, random value, or mutable authorization binding
is never permitted** as the discriminator or as any part of it; a caller cannot
obtain a new key by asking again, only by standing a durable governed
same-parent successor transition or a new logical parent. **No cross-parent
UDOK-4 is required, assumed, or fabricated** to distinguish a new-parent
generation from its fabric predecessor.

**Mutable authorization is binding, never key material.** An authorization
snapshot, §7Q result, SACL/PBR scope, hold state, or AIC snapshot is *bound
to* an operation as evidence; it is **never** part of a structural key.
**UDOK identity never replaces a fabric key**, and no fabric key replaces a
component's own canonical identity (B11's claim, ownership, and batch
identities remain the duplicate-prevention authority at their seams).

### §13.3 Two gate layers

- **Layer 1 — AIC.** Wherever this design's operation contract declares AIC
  applicable, the **current released committed AIC authority snapshot** is
  **mandatory at that generation's UDOK-1, before any governed work**, and a
  successor generation **repeats the proof** where AIC still applies. Where
  AIC is inapplicable the prerequisite is **absent — there is no delayed or
  partial third case**. Release of an existing snapshot to a later operation
  requires **AIC's completed current-input re-proof**; **missing, unreadable,
  unproved, or unreleased snapshot evidence fails closed at UDOK-1**, and
  changed or unprovable inputs route **only** through AIC's own
  fresh-establishment and successor-generation mechanics. The snapshot means
  **governing-basis proof and nothing else** — never permission, never privacy
  authorization, never retry admission, never operation identity, never
  success evidence. The fabric consumes the snapshot reference; it never
  verifies, repairs, releases, re-proves, or creates authority.
- **Layer 2 — owner results at their seams.** §7Q exact-purpose scope before
  candidates or ranking; SACL/PBR before multi-speaker retrieval; §7R/B1 mode
  validation; owner-held Level-1, TSC, hold, quarantine, production, and
  influence fences; and the later §7Q-first / SACL-second output review.

**Missing, stale, unreadable, contradictory, or unauthorized evidence refuses
the effect** at either layer. Layers are never mixed, never substituted for
each other, and never satisfied by a model's summary.

---

## §14 — Failure classes, retry, and stopping

### §14.1 Recorded technical failure classes `[proposed]`

Loss; corruption; **stale**, **incomplete**, or **conflicting** coverage;
timeout; unreachable dependency; unreadable basis or unreadable source
version; and interruption. Each is a **recorded technical failure fact** with
its detection detail, the affected generation or query, version provenance,
attempt and lineage references, time, and resulting state. Classification is
recorded fact, never interpretation, and a failure record is never evidence
about the meaning of any content.

**A genuine empty result is not a failure.** Retrieval that worked and found
nothing is a normal condition, recorded as such — and it requires a *healthy*
query to be claimed (§19).

### §14.2 B9 / B26 semantics (consumed, not re-decided)

- **Partial results are audit-only.** Partial material from a failed
  assembly is recorded in the failure record for audit and is **never**
  supplied as context, never presented as complete or good-enough, and never
  merged into a later attempt's results.
- **Bounded retry, then stop.** Retry re-attempts the **same operation
  identity** under B9's accepted mechanics and lineage.
- **After exhaustion: stop.** A terminal failure state is committed, the
  reason is stated through the governed surface, the work record is kept, and
  the unfinished state is saved for continuation **only if something real
  changes**. There is **no degraded continuation** and **no channel
  substitution** after exhaustion; the path fails closed until and unless a
  separate later Ness-approved rule says otherwise.
- **Never pretend.** No fabric path converts a failed retrieval into usable
  context. A consumer may use a context package only from a run whose audit
  record shows a committed successful outcome.

### §14.3 Schedule classes and values (declared by reference; nothing re-chosen)

`schedule_class` is **recorded, never guessed; there is no default class**, and
a missing or unreadable class means **no admission — fail closed**.

| Fabric operation kind | Declared class | Total attempts | Minimum waiting gaps | Episode deadline |
|---|---|---|---|---|
| Live channel query / live retrieval plan | `live_chat` | 3 (original + 2) | 10 seconds, then 30 seconds | 7 minutes |
| Background build / rebuild / republish / reconciliation | `background_nightly` | 3 (original + 2) | 1 minute, then 3 minutes | 15 minutes |

**Both gates apply** — the attempt allowance and the elapsed-time deadline —
and **the first closure stops** the episode. Gaps are **minimum waiting
floors** indexed by episode ordinal (none before ordinal 1), never a deadline
and never a deadline extension. **Early stop is allowed** when retrying is
clearly useless or unsafe. These values are the **Ness-decided B9 values
consumed by reference**; no count, gap, deadline, or budget is chosen,
altered, or extended here.

**Source-operation timeouts remain owner-held.** The fabric never imposes,
shortens, or lengthens a source component's own timeout.

### §14.4 The only permitted fallback

Fallback is **exclusively** a **predeclared, provably equivalent, healthy
generation or replica of the same channel definition**, used **within the same
retry episode**. It is never another channel, never a different definition,
never a stale or unvalidated generation, and never a substitution of
unrelated material. If no predeclared equivalent is healthy, the episode
proceeds to its bounded stop.

### §14.5 Retry never bypasses a gate

Retry is never used around a privacy refusal, an access refusal, a hold, a
substantive rejection, a quarantine or production boundary, or an
indeterminate recovery state. Those are not technical failures and no
attempt count applies to them.

---

## §15 — §0B logging without duplication

### §15.1 One parent log per real fabric operation

Each real fabric operation — a build, a rebuild, an invalidation, a
coverage/health resolution, a retrieval plan, a channel query, a recovery
run — produces **exactly one** parent §0B operational record. **Publication is
an effect inside its build or rebuild parent and therefore carries no parent
log of its own**, and a **new-parent rebuild or replacement carries its own
single parent record** without adding a second one to the earlier parent
(§13.1). **Genuine UDOK
child operations may carry their own logs** under their own child operation
identities; a child log is never a second parent log, and **no operation
identity ever carries two operational logs**.

### §15.2 Canonical records are not logs

Channel definitions, generation manifests, entries, coverage/health facts,
channel results, retrieval plans, checkpoints, and failure facts are
**canonical machine/provenance records**. They are **not** operational logs,
not extra logs, and **never extra evidential votes**. Recovery finds an
existing log by operation identity and appends only what is genuinely
missing, idempotently.

### §15.3 What a log records and what it may never do

A fabric log records the operation's identity and class, the gates and
authorizations evaluated, the references **evaluated / used / not used**, the
outcome, and the pointers to the canonical records above.

A log **never**: becomes evidence for the truth of its subject; strengthens a
subject, a claim, a person, or a connection; adds certainty through
repetition; logs the act of logging; substitutes for a canonical record; or
escapes governance — **log access remains subject to §7Q and to §25 identity
and security authorization**, exactly as settled. Silent internal operations
are prohibited: an operation that really happened leaves its one record.

---

## §16 — `nh_roots_v1` and the implementation boundary

`nh_roots_v1` is preserved as the **current semantic-index compatibility
surface** — one existing physical realization that the `semantic` family
(family 2) must remain compatible with. It is **not** the fabric, **not** all
of family 2, and **not** an authority of any kind. The retained collections
(`nh_reality_core`, `nh_test_asm`, `nh_simulation_core`) remain untouched and
are named here only to record that they are not to be touched.

**This design authorizes nothing:** no mutation, migration, rebuild, reindex,
store or collection creation, deletion or merge, code, model or library
installation, embedding change, schema change, Map/Master/Defaults/`cursorrules`
integration, or implementation of any kind. **Physical adaptation of
`nh_roots_v1`, the choice of the smallest initial physical channel set, and
the build order are later, separately authorized implementation work** (§20,
open items 2 and 5).

---

## §17 — Wiring

### §17.1 Trigger — *specified*

Build or invalidate **only** from: a durable source, relationship, or state
commit; a **B11 batch or coverage change**; a channel-definition or ruleset
change; a **§7Q visibility or influence event**; a detected integrity or
health condition; or an **explicit governed rebuild request**.

Query **only** from: a **declared purpose**, a target/context, and a **B1
configuration**.

**Similarity or time alone triggers nothing** — no source write, no
connection, no state change, and no autonomous route of any kind. The fabric
has no self-starting behaviour.

### §17.2 Direction — *specified*

```
canonical owner event → projection generation → pinned channel result
      → retrieval plan → authorized consumer / model context
projection health → B11 registration and fabric failure records
```

**No reverse edge exists.** Nothing flowing back rewrites a source, accepts a
connection, merges an identity, sets currentness, promotes material, or
creates authority.

### §17.3 Connection — *specified*

Canonical roots and readings and the B11 registries; accepted Origin,
connection, Story, telling, theme, clash, and Person-Box records; A2 tellings;
Bundle 4 Living-State, world-model, and Computed-View records; and §0B
records **feed typed projections**. Per-channel results and one plan feed
**B1/§7R/LMAC and the caller**. **No edge bypasses a canonical owner, and no
edge copies evidence into a second memory.**

### §17.4 Data and meaning carried — *specified*

Carried on the wire: canonical identities; batch and location; source and
record versions; Origin and time provenance; channel family and subtype;
typed basis; ruleset and generation; coverage and health; purpose and
configuration; parameters; ordered results; omissions and failures; evidence
passed; and the final context. **Owner statuses are carried unchanged**, and
for themes the **whole owner lifecycle** — stable identity, membership links,
aliases, and every theme-action event — travels with the entry and the result,
never a substituted status label (§10.1).

**Ranking or presence means retrieval route only** — never truth, weight,
certainty, identity, connection, permission, currentness, or action authority.

### §17.5 Authority and privacy gates — *specified*

As §13.3: Layer 1 is the **current released committed AIC authority snapshot,
mandatory at that generation's UDOK-1 before governed work** wherever the
operation contract declares AIC applicable — repeated by a successor
generation where AIC still applies, absent where AIC is inapplicable, released
to a later operation only on AIC's completed current-input re-proof, failing
closed at UDOK-1 on missing, unreadable, unproved, or unreleased evidence, and
meaning **governing-basis proof only** (never permission, privacy
authorization, retry admission, operation identity, or success evidence);
Layer 2 is §7Q exact-purpose scope before
candidates or ranking, SACL/PBR before multi-speaker retrieval, §7R/B1 mode
validation, owner-held Level-1 / TSC / hold / quarantine / production /
influence fences, and the later §7Q-first / SACL-second output review.
**Missing, stale, unreadable, contradictory, or unauthorized evidence refuses
the effect.**

### §17.6 Operation identity — *specified*

One UDOK parent per build / rebuild / invalidate / plan, with **publication an
effect inside its build or rebuild parent, never a separate publish parent**;
generation-scoped children for batch projection units, channel queries, the
**B11 LB7 registration child**, and any other owner effect carried as a child;
the §13.2 fabric keys throughout. **Every child commits its UDOK-2
registration before its owner work begins** under {parent operation,
generation, child owner, child identity}; **one append-only membership head
per generation**; **one single-winner UDOK-6C closure bound to that exact
unchanged head before any publication or terminal**; and **predecessor
exact-head closure revalidated at UDOK-4 before a *same-parent, pre-terminal*
successor generation stands** (§13.1). **Fabric projection-generation lineage
and UDOK operation-generation lineage stay distinct**: a rebuild, a
post-terminal invalidation replacement, or any other genuinely later
generation stands under a **new logical parent with its own UDOK-1** while
retaining its predecessor fabric generation and the earlier parent's terminal
as history — **never** through a cross-parent UDOK-4 and **never** by
reopening a terminated parent (§5.2, §11.0). Where effect-first child work is
discovered instead, it is a **membership-fence violation**: only the
open-generation path of §18 row 4a may reconcile it from owner truth, always
alongside a **distinct durable violation record**, so a **fence kept** and a
**fence violated and reconciled** stay distinguishable in every trace.
Generation keys carry **`index_identity` and the
`generation_lineage_discriminator`**, and plan keys carry
**`parent_operation_ref` and `plan_generation`** (§13.2), so genuine
successors are mechanically distinct while replay inside one generation still
converges. Authorization snapshots are
**bindings, never key material**; UDOK identity never replaces the component
key.

### §17.7 Transaction boundary — *specified*

- **Source commit is independent** and never waits for the fabric.
- **Build / rebuild (one parent, one boundary):** stand the generation under
  **exactly one** parent — a **new logical parent with its own UDOK-1** for an
  initial build, a routine rebuild, or a post-terminal invalidation
  replacement; a **same-parent UDOK-4 successor** only while that parent is
  open and pre-terminal, over a predecessor generation of that same parent
  with a committed exact-head closure. AIC snapshot at that generation's
  UDOK-1 where applicable; the generation stands on a **lineage discriminator
  derived per `lineage_kind`** and never on the predecessor's key, retaining
  the predecessor fabric generation and any earlier parent's terminal as
  history (§5.2, §11.0, §13.2) →
  **register each child under UDOK-2 before its work — including the B11 LB7
  registration child** → stage entries and checkpoints (fabric-local,
  non-queryable, no LB7, no B11 coverage) →
  validate exact source head, definition, ruleset, protection scope,
  integrity, and coverage requirement → **commit the single-winner UDOK-6C
  closure bound to the exact unchanged membership head** → **atomically
  publish one generation inside this same parent** → the pre-registered B11
  child performs **LB7 registration**, after which the generation participates
  in unified reading → **parent terminal only after the supported B11 child
  terminal and every other required child terminal resolve against that exact
  closed head**.
- **Query:** stand the plan generation (same UDOK-1 prerequisite; **UDOK-4
  only for a same-parent, pre-terminal successor generation**) under the
  parent operation's durable `plan_generation`, a **changed** operation
  generation standing a **distinct successor plan key** (§12.2) →
  **register each channel-query child under UDOK-2 before its work** → pin
  only published-and-registered generations, gates, and coverage per channel →
  commit channel results → **commit the exact-head UDOK-6C closure and resolve
  the required-channel terminals against that closed head** → **terminal only
  after every required channel has resolved**.
- **Invalidate:** the same UDOK-1 / UDOK-2 / exact-head UDOK-6C sequence
  applies before the `invalidated` transition commits, with **UDOK-4 used only
  for a same-parent, pre-terminal successor generation**; the **replacement**
  for an invalidated generation is separate later work standing under its own
  parent (§11.0 path 3).
- **Privacy suppression fences precede rebuild completion** — suppression is
  never deferred until a rebuild finishes (§8.5).

### §17.8 Duplicate prevention — *specified*

Every fabric key of §13.2 commits **one-winner / append-once**; a replay
returns the **existing** record **only when every structural-key input is
equal** — for a generation including `index_identity` and the
`generation_lineage_discriminator`, and for a plan including
`parent_operation_ref` and `plan_generation`. Append-once therefore **never
collapses a replacement generation built after an invalidation, a lawful
same-parent successor, a rebuild standing under a **new logical parent**, a
successor plan, or records belonging to different indexes into an earlier
record**; each of those is a mechanically distinct key, and a new-parent
rebuild derives that distinction from the **new parent's establishment
evidence**, never from a cross-parent UDOK-4. Equally, a
distinct key is **never manufactured** to escape convergence — a retry,
resumption, or crash recovery inside one genuine generation, under the same
still-open parent, resolves the same inputs and returns the committed record
(§5.2, §12.2). Within one
channel, one canonical object may retain **distinct basis references** (they
are different facts, not duplicates). Channels remain separate. The **final
context counts canonical evidence once while retaining all channel
provenance** — being found twice is never being true twice. **Similarity
never deduplicates** an Origin, a person, a telling, or a relationship.

A **§18 row 4a reconciliation is append-once in the same way**: the backfilled
same-generation UDOK-2 registration, each supported UDOK-6 terminal reference,
and the **membership-fence-violation record** are each appended **exactly
once**, and a repeat returns the committed records rather than creating a
second registration, terminal reference, or violation record. The reconciled
registration **never stands in place of, supersedes, or deduplicates away the
violation record** — they are different facts, not duplicates.

### §17.9 Partial completion — *specified*

Per-entry and per-batch projection work may stand as **honest partial work**
but is **never complete and never query-eligible**. Before publication that
partial progress is evidenced **only** in the fabric-local manifest,
checkpoint, watermark, and `fabric_coverage_health_event` records (§6.3);
**no LB7 registration and no B11 coverage state of any value is created for
it**. Honest B11 coverage is registered **only after publication**, for the
registered batch/index relationship that then exists (§6.1–§6.2, §11.6). A
plan names **required, omitted,
completed, and failed** channels; **any failed required channel blocks the
final context**. Partial results are **provenance-only and never reach the
model**. Healthy published generations and all sources remain untouched.

### §17.10 Timeout and retry — *specified*

As §14.3–§14.5: B9 owns admission and lineage; the declared schedule class
carries the Ness-decided values; attempt and elapsed gates both apply; first
closure stops; early stop is allowed; source timeouts stay owner-held; and an
exhausted retrieval **stops** — no degraded continuation, no substitution, no
blind resend, and no retry around a privacy, hold, or indeterminate state.

### §17.11 Crash recovery — *specified*

See §18.

### §17.12 Fail-closed behavior — *specified*

See §19.

### §17.13 Blocked and open edges — *open*

Controlled IDs; persistence and technology; empirical values and source
timeouts; UI, model/provider, and operational-log cooling; the initial
physical channel set and build order; the Wonder/simulation-to-memory route;
Bundle 8's B-INT/B-CYCLE composition, whole-system audit, and Map/Master
consolidation; and all implementation. **None of these blocks this standalone
logical design, and none of them is silently decided here** (§20).

---

## §18 — Crash and partial-completion recovery

**Protocol for every row:** recovery is **lookup-first under the same UDOK
generation and the same fabric key** (§13.2), reading in order: the **gates**
(including the AIC snapshot at UDOK-1 where applicable), the **recorded parent
position** (which logical parent owns this generation, which operation
generation, and whether that parent is **still open** or has reached its
**terminal**), the **owner's canonical truth**, the **generation-scoped
child-membership registrations and head**, **staging and checkpoints**, the
**exact-head UDOK-6C closure**, **publication**, **B11 registration**,
**channel results**, and the **terminal**. Committed work stands and is
continued, never re-executed. Recovery is idempotent under its own run
identity plus per-action keys.

**Recovery branches on both identities.** The **fabric projection-generation
lineage** and the **UDOK operation-generation lineage inside one parent** are
read separately and never substituted for each other (§5.2, §11.0). Recovery
**resumes** only within the **same current, open parent and operation
generation**; it may use **UDOK-4** only for a lawful **same-parent,
pre-terminal** successor; and it creates a **new logical parent with its own
UDOK-1** for post-terminal rebuild or replacement work, while retaining the
predecessor fabric generation. Recovery **refuses** — fail-closed,
recovery-required, preserving history — any record that claims a
**cross-parent UDOK-4**, **reuses or reopens a terminated parent**, **omits
the new parent's UDOK-1**, or **loses the predecessor fabric lineage** (row
4f).

**Resumption is bounded to one genuine generation.** Recovery may resume under
an existing key **only** for the **same still-current, still-open generation
and the same lineage**, inside the **same still-open parent operation and
operation generation** — same `index_identity`, same predecessor, same
`generation_lineage_discriminator`, same remaining key inputs (§5.2, §13.2).
Once a generation is `invalidated` or `superseded`, replacement work **first
stands a mechanically distinct successor generation** on a new lineage
discriminator — through a **same-parent UDOK-4 successor** only while the
owning parent is open and pre-terminal, and otherwise under a **new logical
parent with its own UDOK-1**, derived from that new parent's establishment
evidence together with the durable invalidation-replacement or rebuild
evidence; **recovery never republishes or reuses the invalidated generation**
and never reopens a terminated parent. The same distinction applies to plans: recovery resumes a plan
only within its own parent-operation generation, and a **changed** parent
operation generation requires a **successor retrieval plan under a distinct
key** (§12.2) — never a reused or edited one.

**Membership backfill is permitted only** while the affected generation is
**both current and open**, **before closure**, **after owner-truth lookup**,
and **with no effect replay** — and, where it is used, **only together with the
durable membership-fence-violation record of row 4a**. **A closed or superseded
generation is never backfilled.** Where backfill is unavailable, recovery
preserves history, records the contradiction, **fabricates no membership and no
closure**, and permits **no governed successor work, no terminal, and no
acknowledgement** while the state is unresolved.

| # | Crash / partial state | Resolution |
|---|---|---|
| 1 | **Pre-publish** — build staged (fully or partly), nothing published | Nothing is queryable and no coverage claim exists. Verified staging **resumes** from its checkpoints **only under the same still-current, still-open generation and the same lineage discriminator, inside the same still-open parent operation and operation generation** (§5.2, §11.0, §13.2), or is **honestly invalidated** with its cause recorded. An **invalidated** generation is never resumed, reused, or republished: a replacement is a **new generation on a new lineage discriminator** — a **same-parent UDOK-4 successor** only while that parent is open and pre-terminal, otherwise a **new logical parent with its own UDOK-1** carrying the predecessor fabric generation and the earlier parent's terminal as history. No source is touched; no coverage is claimed. |
| 2 | **Partial projection** — some batches or units projected, others not | The generation stays `staging`; partial work is honest, marked, and non-queryable, and is **either resumed under the same identities, generation, and lineage discriminator, or invalidated**. Progress is recorded **only** in the fabric-local manifest, checkpoints, watermarks, and `fabric_coverage_health_event` records (§6.3). **No LB7 registration and no B11 coverage state — including `partial` — is created before publication**, and recovery creates none. After invalidation, a same-input rebuild **derives a distinct append-once key** and never converges onto the invalidated generation's record — standing under a **new logical parent with its own UDOK-1** where the owning parent has terminated, and **never through a cross-parent UDOK-4**. |
| 3 | **Published but unregistered** — atomic publish committed, B11 LB7 registration missing | The publication **stands** and the generation **does not participate in unified reading** until registered. Recovery continues **inside the same still-open build or rebuild parent that published it** (§11.6): the pre-registered B11 child's missing registration is appended **idempotently** with its honest coverage status, together with the child terminal evidence owner truth supports. **Recovery never republishes**; publication is never re-performed and never duplicated. If that parent has **already terminated** without the required B11 completion, the terminal and the contradiction are **preserved as history** and the closure-bound fail-closed seam applies: the parent is **not reopened**, **no same-operation successor is manufactured**, and any genuinely later work stands as a **new logical parent** (§11.0 path 3). |
| 4 | **Query partial** — some channel results committed, the plan not terminal | Committed channel results stand. Recovery reads the plan generation's **membership head and its exact-head UDOK-6C closure** and resolves the required-channel terminals **against that closed head**, never against a narrowed set: any failed or unresolved **required** channel blocks the final context; partial material is provenance-only. No result is fabricated and no channel is substituted. |
| 4a | **Missing pre-work registration (membership-fence violation)** — a child's owner work is discovered with no committed UDOK-2 registration under this generation, or a registration exists only under another generation | **Fail closed, and read owner truth first.** Recovery reads the child's **owning component's canonical truth** and distinguishes three separate facts: the owner's **claim**, its **committed effect**, and its **terminal evidence**. The discovery **is a membership-fence violation** — owner work preceded the required same-generation UDOK-2 registration — and it is recorded as one (see the violation record below). **Only** while the generation is **both current and open** and **no UDOK-6C closure has committed**, reconciliation appends (i) the missing **same-generation UDOK-2 registration** and (ii) **every UDOK-6 terminal reference that durable owner truth supports**, both **before closure** and **with no effect replay**. Owner terminal evidence that is missing or unresolved stays **explicitly incomplete** — it is never inferred, fabricated, or completed by the fabric. Reconciliation makes the existing child **visible to completion accounting** and nothing more: it **never retroactively proves the pre-work fence was satisfied**, never converts effect-first execution into lawful execution, never reclassifies or replays the owner's effect, and **never becomes an ordinary work-first / register-later route**. If the generation is **closed or superseded** — or closure commits first — there is **no UDOK-2 or UDOK-6 backfill**: the contradiction and all committed history are preserved and surfaced, **no membership, closure, or terminal is fabricated**, nothing is replayed, and **no parent terminal, acknowledgement, or governed successor work is permitted** while it remains unresolved under the owning component's (or the applicable policy owner's) own durable resolution seam. |
| 4b | **Missing closure** — publication or a parent terminal is reached with no committed UDOK-6C closure | **Fail closed.** Nothing is published and no terminal is committed. The closure is obtainable only as a single winner bound to the generation's exact current head; it is never assumed, inferred, or reconstructed. |
| 4c | **Unreadable, advanced, or contradictory head** — the membership head cannot be read, has advanced past the value the closure binds, or contradicts the committed closure | **Recovery-required and fail closed.** The generation is not published, not queried, and not carried to a terminal. The contradiction and its evidence are preserved and surfaced; **no head value, closure, or winner is invented** by timestamp, ordering, count, or any other tie-breaker. |
| 4d | **Invalid same-parent successor** — a successor **UDOK generation of the same parent** is attempted over a predecessor generation lacking a committed exact-head UDOK-6C closure, or the predecessor's closure no longer binds its exact unchanged head at the UDOK-4 transition | **Fail closed.** The successor does not stand and no governed successor work proceeds. A same-parent successor **after that parent's terminal is refused outright**; genuinely later work stands as a **new logical parent with its own UDOK-1** (§11.0 path 3), never as a UDOK-4 transition. |
| 4e | **Already-committed same-parent successor over an invalid predecessor closure** — the transition is found committed but the predecessor generation's exact-head closure is missing or invalid | **Recovery-required and fail closed.** History is preserved and the contradiction recorded; the predecessor is **not backfilled** (it is no longer current and open), nothing is republished, no closure is fabricated, and **no governed successor work, terminal, or acknowledgement is permitted while unresolved**. |
| 4f | **Conflated lineage** — a record claims a UDOK-4 transition **between distinct parent operations** or **after a parent terminal**; reuses, reopens, or re-terminates a terminated parent; omits a new parent's committed **UDOK-1**; or loses the **predecessor fabric-generation reference** for a rebuild or replacement | **Recovery-required and fail closed.** The claimed transition **does not stand** and no governed work proceeds under it. The two lineages are re-read separately (§5.2, §11.0): a cross-parent historical closure or terminal is retained as **fabric lineage and recovery evidence only** and **never converted into a UDOK-4 transition**; a missing new-parent UDOK-1 is **never inferred or backdated**; a lost predecessor fabric reference is **never reconstructed by guess**. History and the contradiction are preserved and surfaced; **nothing is published, registered, terminated, or acknowledged** while unresolved, and any lawful continuation stands as a **new logical parent** with its own UDOK-1 and a distinct generation key. |
| 5 | **Missing log** — a canonical record committed, its one §0B parent record absent | Recovery finds existing logs by operation identity and appends **only the missing** record, idempotently, exactly once. A logging gap never uncommits a publication, a registration, or a result — and never creates a second log. |
| 6 | **Contradiction** — publication, source head, basis, privacy scope, or owner truth cannot be safely established, or two records contradict each other | **Recovery-required and fail closed.** The affected generation is not queried and is not republished; the contradiction and its evidence are preserved and surfaced. **No winner is invented** by timestamp, ordering, count, or any other tie-breaker; resolution waits for owner-authorized evidence. |
| 7 | Duplicate recovery execution over any row above | Lookup-first plus per-action keys make the repeat a **no-op returning the committed findings** — no duplicated publication, registration, result, or log. |

**`fabric_membership_fence_violation_record` `[proposed]` (row 4a).** Whenever
row 4a applies — **whether or not** reconciliation turns out to be available — a
**separate append-only** record is committed, bound to: the **parent
operation**, the **generation**, the **child owner**, and the **child
identity**; the discovered owner **claim**, **committed effect**, and
**terminal** references, each as read from owner truth or as an explicit
absence; the **proved absence of a timely same-generation UDOK-2
registration**; and the **reconciliation registration and terminal references
actually appended**, or the explicit fact that none was permitted. This record
is **preserved independently of ordinary membership accounting**: it is never
merged into, superseded by, or satisfied by the backfilled registration. After
reconciliation the membership head shows the child *and* this record continues
to show that the fence was **not** kept — so **a fence kept before work and a
fence violated and later reconciled from owner truth remain permanently
distinguishable** in every recovery, membership, and completion trace (§11.2A,
§13.1, §17.6, §19, §21).

**Boundaries around row 4a.** A **repeated** reconciliation is a no-op under
lookup-first plus per-action keys: the registration, each supported terminal
reference, and the violation record are appended **exactly once**, and a second
violation record is never created for the same discovery. **Closure racing the
backfill** resolves exactly as §11.2A binds it — closure-first refuses the late
registration and that child has **no owner work under the closed generation**,
while the violation record still stands and the contradiction path applies.
**Discovery after closure or supersession** never reopens the generation, never
backfills, and never converts an unlawful effect into an accounted child.

**Never:** replay an effect; fabricate coverage, membership, a membership
head, a closure, or an owner terminal; backfill membership into a closed or
superseded generation; assert a UDOK-4 transition **between distinct parent
operations or after a parent terminal**; reopen, resume, or re-terminate a
terminated parent; stand a rebuild or replacement **without its new parent's
committed UDOK-1**; drop or reconstruct by guess the **predecessor
fabric-generation reference**; present a reconciled fence violation as an
ordinary registration or let it erase the violation record; republish
uncertainty; reuse or republish an invalidated generation, or reuse its
structural key for a replacement; regenerate or reconstruct missing canonical
content; collapse a theme's preserved action history into a status label while
resuming or rebuilding; rewrite, delete, or repair a source; or convert an
indeterminate state into a claimed outcome.

**Resumed and rebuilt generations carry the full theme lifecycle material of
§10.1** — stable identity, membership links, aliases, and every theme-action
event. Recovery never re-derives a theme's current navigation state from
anything but that preserved owner history.

---

## §19 — Fail-closed behavior and must-nevers

### §19.1 Refuse to publish or to use when any of these is unproved

Canonical identity; owning batch; exact source head; channel definition or
ruleset; generation; **the generation's lineage discriminator and its durable
lineage evidence — and, for a replacement after invalidation or any successor,
a structural key distinct from the record it replaces**; **the generation's
recorded parent position: exactly one owning build or rebuild parent with its
committed UDOK-1, its `lineage_kind`, and — for a rebuild or post-terminal
replacement — the new parent's own establishment evidence together with the
retained predecessor fabric-generation reference**; integrity; coverage;
relationship basis; **the current
released committed AIC authority snapshot at UDOK-1 where the operation
contract declares AIC applicable**; **each child's UDOK-2 registration
committed before its owner work**; **a readable, unchanged
generation-scoped membership head**; **the single-winner UDOK-6C closure
bound to that exact head**; **the predecessor generation's committed
exact-head closure revalidated at a *same-parent, pre-terminal* UDOK-4
transition — never a cross-parent or post-terminal one**; **the supported B11
child terminal reference and every other required child terminal resolved
against that exact closed head before the parent terminal**; **the durable
membership-fence-violation record wherever §18 row 4a reconciliation was
used, together with the owner-truth basis of every registration and terminal
reference it appended**; **the committed B11 LB7
`index_registration` before any unified-reading participation**; privacy,
access, or relevance authorization; lifecycle eligibility; or the required
terminal. **The cause is recorded** in every case.

A **genuine empty** result may be claimed **only** from a healthy, completed
query — never from a failed, partial, unauthorized, or unproved one.

### §19.2 Must-nevers (binding)

The fabric must never: guess; omit a batch silently; substitute one channel
for another; leak the existence, quantity, or shape of restricted material;
fabricate a connection, an identity, a merge, a membership, a membership head,
a closure, a coverage claim, or a time; register an LB7 entry or claim any B11
coverage state for a staging generation; let owner work precede its UDOK-2
registration; treat a reconciled membership-fence violation as an ordinary
registration, omit or erase its violation record, or use §18 row 4a as a
work-first / register-later route; infer or fabricate an owner terminal for a
reconciled child; reuse or republish an invalidated generation, reuse its
structural key for a replacement, or derive a lineage discriminator from a
nonce, timestamp, random value, or mutable authorization binding; collapse a
replacement generation, a successor plan, or two different indexes into one
another's append-once record; close a generation around an unregistered child
or narrow a
required set after a failure; stand a same-parent successor over an unclosed or
unresolved predecessor generation; **treat a fabric predecessor relationship as
a UDOK operation-generation relationship, assert a UDOK-4 transition between
distinct parent operations or after a parent terminal, reopen, resume, or
re-terminate a terminated parent, publish under a separate publish parent, or
stand a rebuild or post-terminal replacement without a new logical parent's
committed UDOK-1 and its retained predecessor fabric-generation reference**;
backfill membership into a closed or superseded generation;
collapse a theme's preserved lifecycle into a bare status label; rewrite,
delete, or repair a source; call partial work a success;
merge two Origins because they are similar; accept a person identity or a
relationship from embeddings; turn a theme or a repeated interpretation into
a fact; let an index become the only surviving copy of memory; silently mix
simulated, Wonder-origin, rejected, provisional, held, quarantined, or
unauthorized material with ordinary evidence; hide which retrieval channel
produced an item; treat ranking as truth, certainty, authority, or
permission; use a derived operational log as additional evidence for its own
subject; create a parallel authority, retry, index, permission, or logging
mechanism beside an accepted one; or claim any acceptance, adoption,
installation, integration, or implementation.

---

## §20 — Open items preserved (nothing guessed, nothing closed)

1. **Final controlled component and Register IDs remain open; none is
   assigned or implied** by this design. *(Evidence: the UDOK mechanical-design
   closure record; the Five-Additions decision package.)*
2. **Final persisted names and types, serialization, database / index / graph
   engines, storage layout, runtime libraries, migration, and replica topology
   remain implementation choices**, and **no persisted or implemented schema
   exists here or is created, chosen, or authorized by this file.** What this
   design *does* settle is the other side of that boundary (§1): the
   **proposed logical record shapes, required information, relationships,
   lifecycle constraints, and applicable controlled vocabularies** of the
   fabric records of **§§5–6, §12, §14, and §18**. Those logical record
   contracts are **material design commitments** — §21 item 3 makes their
   required contents a completion condition — and the logical contract in
   §3–§19 stays mandatory regardless of which physical choices are later made.
   **Neither half of this boundary may be stated without the other** (§22).
   *(Evidence: the Five-Additions package; the UDOK mechanical-design
   candidate.)*
3. **Empirical limits, thresholds, token ceilings, ranking rules, State /
   Story / entity / world calibration, capacity triggers, and source-operation
   timeouts remain with their accepted owners and their testing paths** — B1's
   ceiling and parameter values against the gold sets, and each owner's own
   calibration. *(Evidence: Bundle 2's formal relevance declarations; B1; the
   Five-Additions package.)*
4. **UI and inspection surfaces, model/provider choices, and operational-log
   cooling rules remain open.** *(Evidence: Bundle 4; the Five-Additions
   package; the UDOK mechanical-design candidate.)*
5. **The smallest physical initial channel set and the build order remain for
   implementation.** All eight logical families are designed **now**, so that
   later channels can be added without changing source identities.
   *(Evidence: the Five-Additions package.)*
6. **Wonder / simulation-to-memory routing stays blocked outside this
   package** and is neither designed nor unblocked here. *(Evidence: Bundle 4;
   the Five-Additions package.)*
7. **Bundle 8 owns the final B-INT / B-CYCLE composition, the whole-system
   audit, and Map/Master consolidation; all implementation needs separate
   authorization.** *(Evidence: the full design-completion workflow; the
   replacement eight-bundle dependency plan; the Five-Additions package.)*

No item above is answered, narrowed, biased, or pre-empted by anything in this
file, and no other open item of any Register is reopened or closed here.

---

## §21 — Design-complete-when (this package's completion conditions)

This package is design-complete for its standalone logical scope when all
nineteen hold:

1. The fabric is **derived and rebuildable**, and every authority it does not
   own is **named** (§3).
2. **All eight families** and the **state/world subviews** remain separately
   typed (§4).
3. **Channel, generation, entry, coverage, result, plan, and failure** logical
   records contain the required information (§5, §6, §12, §14).
4. Every entry points to **canonical identity and basis**; **no index owns
   source, identity, connection, or batch truth** (§5.3).
5. **Origin / time / batch / telling / Person-Box / Story / state / world
   distinctions are preserved** (§7, §9, §10), and **family 6 carries the
   whole theme lifecycle** — stable `theme_id`, membership links, aliases, and
   every confirm / reject / rename / merge / split / leave-unresolved event —
   with the current navigation state **derived from that complete append-only
   owner history** and never collapsed into two labels (§4, §5.3, §10.1,
   §12.3, §17.4, §18).
6. **§7Q and SACL scope precede ranking and use**, and **Level-1 raw content
   cannot enter ordinary indexes** (§8).
7. **Only accepted connections enter the accepted graph**, and **similarity
   cannot create identity or connection** (§9).
8. **Staging, validation, exact-head membership closure, atomic publication,
   LB7 registration, and invalidation** are complete and correctly ordered
   (§11, §6): **no staging generation carries an LB7 registration, a B11
   coverage state, unified-reading participation, or query eligibility**;
   partial staging appears **only** in fabric-local health, checkpoint,
   manifest, and watermark records; and **every unified-reading participation
   claim is downstream of both atomic publication and a committed B11 LB7
   `index_registration`**, with published-but-unregistered recovery never
   republishing. The **B11 LB7 registration child is registered under its
   build or rebuild parent before UDOK-6C closes membership and performs its
   owner effect only after atomic publication** (§11.2A, §11.5–§11.6).
9. Plans and results **distinguish required, omitted, empty, failed, partial,
   passed, and used** material (§12, §17.9).
10. **AIC / UDOK / component gates retain their owners** and are carried at
    their exact seams (§13, §17.5–§17.7): every AIC-applicable fabric
    operation requires the **current released committed AIC snapshot at that
    generation's UDOK-1**, including current-input re-proof for reuse, with no
    text treating the snapshot as permission or success evidence; **every
    child owner effect in build, rebuild, publication-inside-its-parent,
    invalidate, plan, and query traces is preceded by same-generation UDOK-2
    registration**; **every
    publication and terminal trace proves one UDOK-6C closure bound to the
    exact unchanged membership head used for required-terminal
    determination**; and **every *same-parent* successor-generation trace
    proves the predecessor generation's committed exact-head UDOK-6C closure
    at a pre-terminal UDOK-4**. All structural identities and duplicate fences
    remain explicit (§17.8).
11. **B11 coverage** and **B9/B26 retry and stop semantics** are exact, and
    **partial context is never used** (§6, §14, §17.9).
12. **Crash recovery** covers pre-publish, partial, published-unregistered,
    query-partial, missing-log, and contradiction cases, and **every missing,
    advanced, unreadable, or contradictory membership state — missing pre-work
    registration, work discovered before registration, missing closure,
    invalid same-parent successor, an already-committed same-parent successor
    over an invalid predecessor closure, and **conflated fabric/UDOK lineage**
    — follows the specified fail-closed path** (§18 rows 4–4f).
13. **One-operation/one-log** and the **canonical-record separation** prevent
    double evidence (§15).
14. **`nh_roots_v1` is preserved**, and this file retains **no implementation
    authorization, no acceptance or adoption claim, no installation or
    integration claim, no bundle placement, no controlled component or
    Register identifier, and no Bundle 8 claim** (§16, §1, §20).
15. **Every later or open item is listed without guessing** (§20).
16. **Genuine successors are mechanically distinguishable and duplicates still
    converge** (§5.2, §12.2, §13.2, §17.8, §18 rows 1–2): the
    projection-generation key carries **`index_identity` and a canonical
    durable `generation_lineage_discriminator`** in addition to definition,
    source coverage head, ruleset, and projection scope; that discriminator is
    derived **only** from durable predecessor and governed transition or
    rebuild evidence and **never** from a nonce, timestamp, random value, or
    mutable authorization binding; the retrieval-plan key carries
    **`parent_operation_ref` and `plan_generation`**; and each of the following
    traces is proved — **two same-input indexes** keep separate records;
    **same-generation replay** returns the existing record; a **same-input
    rebuild after invalidation** derives a distinct key and never republishes or
    reuses the invalidated generation; a **changed-operation successor plan**
    derives a distinct plan key while replay inside one parent-operation
    generation converges; and **crash recovery at each identity boundary**
    resumes staging only under the same current, open generation and lineage.
17. **A kept fence and a reconciled violated fence stay distinguishable**
    (§11.2A, §13.1, §17.6–§17.8, §18 row 4a, §19): open-generation row 4a
    recovery **reads owner truth first**, appends the missing **same-generation
    UDOK-2 registration** and **every supported UDOK-6 terminal reference before
    closure**, and appends a **distinct durable membership-fence-violation
    record** that preserves the fact that owner work preceded registration;
    reconciliation **never** retroactively satisfies the fence, legalizes the
    effect, replays work, or fabricates an owner terminal; **closed or
    superseded generations receive no membership or terminal backfill** and
    their contradiction path preserves history and remains fail-closed; and the
    crash-boundary traces are proved for **owner effect before registration with
    and without a supported owner terminal**, **repeated reconciliation**,
    **closure racing the backfill**, and **discovery after closure or
    supersession**.
18. **Fabric generation lineage and UDOK operation lineage stay separate, and
    one parent boundary governs building and publication** (§2, §5.2, §11.0,
    §11.5–§11.6, §13.1–§13.2, §15.1, §17.6–§17.8, §18, §19): the two lineages
    are explicitly distinct and never substituted for one another; **every
    UDOK-4 occurrence is limited to a pre-terminal successor generation of the
    same logical parent and requires that parent's predecessor generation to
    have a committed exact-head UDOK-6C closure**; **every post-terminal
    rebuild or invalidation replacement establishes a genuinely new logical
    UDOK parent with its own UDOK-1 and never reopens or regenerates the
    completed parent**; a **new-parent fabric generation retains its
    predecessor fabric-generation reference and derives its lineage
    discriminator from durable predecessor, new-parent establishment, and
    governed rebuild or replacement evidence without asserting cross-parent
    UDOK-4**; the **build or rebuild parent boundary includes staging,
    validation, atomic publication, and post-publication B11 registration**,
    with publication never represented as a separate parent operation; the
    **B11 LB7 child is registered before membership closure, performs its
    owner effect only after publication, and supplies supported terminal
    evidence before the parent terminal**; **published-but-unregistered
    recovery continues within the same open parent, appends the missing
    registration idempotently, and never republishes**; and recovery
    **distinguishes same-parent pre-terminal succession from post-terminal
    new-parent work and fails closed on cross-parent UDOK-4, parent
    reopening, missing new-parent UDOK-1, or lost fabric-predecessor
    lineage**. The traces proved are: **same-parent pre-terminal succession**;
    **post-terminal same-input rebuild under a new parent**; **post-terminal
    invalidation replacement under a new parent**; **no cross-parent UDOK-4**;
    **distinct fabric keys without a nonce**; **published-but-unregistered
    recovery inside the original open parent**; and **parent-terminal refusal
    until the pre-registered B11 child and all other required children have
    supported terminals against the exact closed membership head**.
19. **The two acceptance-explanation accuracy statements hold and are not
    collapsible** (§1, §5.2, §11.0, §13.1, §18 rows 1–2 and 4d–4f, §20 item 2,
    §22). On the invalidation boundary: §22 states that a **routine rebuild**
    and a **post-terminal invalidation replacement** each stand under a **new
    logical UDOK parent with its own UDOK-1**, while a **pre-terminal
    invalidation replacement** may stand as a lawful **same-parent UDOK-4
    successor**; **no sentence anywhere says or implies that every invalidation
    replacement necessarily uses a new logical parent**; **every same-parent
    invalidation-replacement statement retains the still-open, pre-terminal,
    exact-head predecessor-closure prerequisites**; and **every cross-parent or
    post-terminal path retains the prohibition on UDOK-4 and requires the new
    parent's own UDOK-1**. On the schema boundary: the file **states that it
    settles proposed logical record shapes and required information as design
    commitments**, **separately states that no persisted or implemented schema
    exists** and leaves final persisted names, types, serialization,
    technology, and implementation unresolved, and **no summary or change
    report uses the unqualified claim that there is no schema anywhere in this
    design**.

Completion of these conditions is a statement about this design's internal
scope only. It confers no acceptance, no adoption, no authority, no
integration, and no permission to build.

---

## §22 — Self-audit and change report

**Authority audit.** Master V10 is treated as the current adopted governing
Master; its stale internal pre-adoption wording is recorded as non-blocking
document drift and is neither carried forward as governance nor repaired in
place. **Decision Defaults S19 v2.3 is the authoritative Defaults in the
governing order; v2.2 is preserved superseded history and is not used as a
current or competing guide.** The authority order is applied as stated; the
working map is used as subordinate material only; accepted standalone packages
are used strictly within their own scopes and are never called Master
authority. **The AIC and UDOK seams are carried as their accepted designs and
closure records bind them, not as a generic caveat.** **No authority
inversion.**

**Scope audit.** One new file created; nothing else touched. No accepted
package reopened, reinterpreted, broadened, or weakened. No concept decision
made or inferred. No unrelated cleanup. **No hidden implementation.**

**No-loss audit.** Settled rules, must-nevers, controlled state and status
vocabularies (B11's `complete` / `partial` / `stale` / `missing` /
`conflicting`, used only for a registered batch/index relationship; the six
Living-State currentness statuses; the four A31 grounding labels; the settled
B3 theme-action set — confirm / reject / rename / merge / split / leave
unresolved — with its stable identities, membership links, and aliases;
`staging` / `published` / `superseded` / `invalidated` as this design's own
generation lifecycle; B9's `live_chat` and `background_nightly` schedule
classes and the Ness-decided values), gate orders, dependencies, provenance
statements, and open items are preserved (§2, §20). No caveat was compressed
away and **no owner lifecycle was reduced to a status label**. The
`generation_lineage_discriminator`, its lineage evidence, `lineage_kind`,
`same_parent_predecessor_closure_ref`, `predecessor_fabric_history_refs`, and
the `fabric_membership_fence_violation_record` are **additive fabric-local
design labels**: `lineage_kind` classifies **this design's own fabric
projection-generation lineage** and adds no owner status enum; none of them
displaces owner vocabulary, resolves a contradiction by itself, or takes
ownership from UDOK, B11, AIC, or any owning component. **UDOK's operation,
generation, membership, closure, transition, and terminal vocabulary is
consumed exactly as the owner binds it and is never extended here.**

**Mechanical audit.** Identity, records, lifecycle, operation identity,
transaction boundaries, idempotency, duplicate prevention, crash recovery,
retry, partial completion, fail-closed behavior, and §0B logging are each
specified (§5–§19). **Structural identity now distinguishes a genuine
successor from a replay without any nonce** — `index_identity` plus a durable
lineage discriminator for a generation, parent operation plus `plan_generation`
for a plan — and **a reconciled membership-fence violation stays permanently
distinct from a fence that was kept** (§5.2, §12.2, §13.2, §17.8, §18).
**Fabric projection-generation lineage is now separated from UDOK
operation-generation lineage**: UDOK-4 is confined to a same-parent,
pre-terminal successor; every routine rebuild and post-terminal replacement
stands under a **new logical parent with its own UDOK-1** while retaining its
fabric predecessor; and **one build or rebuild parent owns staging,
validation, atomic publication, and post-publication B11 registration**
(§5.2, §11.0, §11.5–§11.6, §13.1, §15.1, §17.6–§17.7, §18).

**Wiring audit.** Upstream and downstream are correct and one-directional; no
circular source authority; no evidence duplication; no privacy or relevance
inversion; **§7M → §7D is explicitly forbidden**; no DUMB/SMART boundary
violation; no quarantine or production bypass; no parallel authority, retry,
index, permission, or logging mechanism.

**Completion audit.** Complete for this package's standalone logical scope
(§21). Intentionally open: the seven items of §20. Implementation-only:
everything in §16's boundary paragraph. Dependent on owner packages: the AIC
and UDOK seams, carried here **exactly as those accepted designs and their
closure records bind them** (§1 source statement) — where this file's seam
wording and an owner package's actual text differ, **the owner package
governs** and this file must be corrected in a new version.

**Acceptance-explanation accuracy statements (binding on every summary of this
file).** Any summary, change report, plain-language description, or acceptance
explanation written about this design must state both of the following exactly,
and may not compress either into a shorter claim that is false:

**(i) The invalidation-replacement boundary has three paths, not one.**
A **routine rebuild** stands under a **new logical UDOK parent operation with
its own UDOK-1**. An **invalidation replacement made after the original
parent's UDOK-7 terminal** likewise stands under a **new logical UDOK parent
with its own UDOK-1**. But an **invalidation replacement made before that
terminal may stand as a same-parent UDOK-4 successor** — lawfully and by
design — **only** while the original logical parent remains **open and
pre-terminal** and **every same-parent predecessor prerequisite is satisfied**:
the predecessor UDOK generation of that same parent carries a **committed
UDOK-6C closure**, and the transition commit **revalidates** that the closure
belongs to that predecessor generation and still binds its **exact, unchanged,
current membership head** (§5.2 lifecycle rules, §11.0, §13.1 fence 3, §18
rows 1–2 and 4d). **No summary, change report, or future acceptance
explanation may collapse these three paths into the claim that *every*
invalidation replacement uses a new logical parent** — that claim is false for
the pre-terminal path and misdescribes §5.2, §11.0, and §18 rows 1–2.
**Unchanged and retained in full:** UDOK-4 **never crosses parent operations**
and is **unavailable once a parent has reached its terminal**; genuinely later
work is then a **new logical parent with its own UDOK-1**, never a reopened
parent (§11.0 path 3, §13.1 fence 4, §18 rows 4d–4f, §19.2).

**(ii) Logical record contracts exist here; a persisted schema does not.**
This file **settles proposed logical record shapes, the required information
each carries, their relationships, their lifecycle constraints, and the
applicable controlled vocabularies** for the fabric records of §§5–6, §12,
§14, and §18, and those contracts are **material design commitments** — §21
item 3 makes their required contents a completion condition — even though
every label remains `[proposed]` and none is a controlled identifier. This
file also contains **no persisted or implemented schema**, and leaves final
persisted names and types, serialization, physical storage technology,
database / index / graph engine, storage layout, runtime libraries, migration,
and every implementation choice **unresolved** (§1, §20 item 2). **Every
summary must disclose both sides.** The unqualified claim that **there is no
schema anywhere in this design** is forbidden — it hides a material
logical-record commitment — and so is the converse claim that a **persisted or
implemented** schema exists or is authorized here.

**Change report (v1.4).** This version is the corrected successor to
`NH_PROVENANCE_FIRST_MULTI_INDEX_MEMORY_FABRIC_MECHANICAL_DESIGN_v1_3_CANDIDATE.md`
— **its exact predecessor** — written to
`05_ACTIVE_CANDIDATE/NH_PROVENANCE_FIRST_MULTI_INDEX_MEMORY_FABRIC_MECHANICAL_DESIGN_v1_4_CANDIDATE.md`
— **the only file this task wrote**. The v1.0, v1.1, v1.2, and v1.3 candidates
are preserved unchanged as history.

**This version is clarification-only.** Exactly two acceptance-explanation
accuracy clarifications were applied and **nothing else was altered**. **The
underlying mechanical design is unchanged**: §11.0, §13.1, §17.7, §18 rows
1–2, and every closure-bound UDOK mechanic stand **exactly as v1.3 bound
them**, and **no mechanic was adjusted to make any earlier summary true**.

**(D) The pre-terminal / post-terminal invalidation-replacement boundary is now
stated explicitly and may not be collapsed.** §22 accuracy statement (i) above
now distinguishes all three paths by name — routine rebuild under a new logical
parent; post-terminal invalidation replacement under a new logical parent;
pre-terminal invalidation replacement as a lawful same-parent UDOK-4 successor
while the original parent is still open, with its predecessor's committed
exact-head UDOK-6C closure revalidated at the transition — and forbids any
summary, change report, or future acceptance explanation from collapsing them
into "every invalidation replacement uses a new logical parent". The
prohibition on cross-parent and post-terminal UDOK-4 is retained verbatim in
substance. **This clarification changes no mechanic**: §5.2 lifecycle rules,
§11.0, §13.1, §17.7, and §18 rows 1–2 and 4d–4f already bound exactly this
behavior and are carried forward unaltered (§21 item 19).

**(E) The logical-record / persisted-schema boundary is now stated explicitly
on both sides.** §1 and §20 item 2 now say plainly that this design **settles
proposed logical record shapes, required information, relationships, lifecycle
constraints, and applicable controlled vocabularies** for the fabric records of
§§5–6, §12, §14, and §18 as **material design commitments**, and — separately
and equally — that **no persisted or implemented schema exists** and that final
persisted names, types, serialization, technology, layout, libraries,
migration, and implementation remain unresolved. §22 accuracy statement (ii)
requires every summary to disclose both sides and forbids the unqualified "no
schema anywhere" claim. **This clarification neither creates nor implements a
schema, chooses no persisted field name or physical type, authorizes no schema
change, and weakens no logical record requirement already carried by v1.3**
(§1, §20 item 2, §21 item 19).

**The correction carried in from v1.3 is retained without regression:**
**(C) Fabric projection-generation lineage is no longer conflated with UDOK
operation-generation lineage, and building and publication now have one
unambiguous parent boundary.** The two lineages are stated as separate and
non-collapsible; a fabric generation may name a predecessor fabric generation
owned by an earlier, already-terminated parent without either becoming a UDOK
generation of the other's operation. **UDOK-4 is reserved exclusively for a
successor UDOK generation of the same still-open logical parent, before that
parent's UDOK-7 terminal**, over a predecessor generation of that same parent
with a committed exact-head UDOK-6C closure — never between distinct parents,
never after a terminal, and never merely because two fabric generations stand
in a predecessor relationship. An **initial build** stands a new logical
parent with its own UDOK-1; every **routine rebuild, post-terminal
invalidation replacement, or other genuinely later projection generation**
stands a **new logical parent** with a fresh identity, its own UDOK-1, and its
own membership head, closure, terminal, acknowledgement, and one-operation
log, **without reopening, regenerating, or re-terminating the earlier
parent**, while retaining the predecessor fabric generation and that parent's
committed terminal as history. The `lineage_kind` of a generation now selects
its discriminator derivation (genesis / same-parent successor / new-parent
generation), and `same_parent_predecessor_closure_ref` is separated from
`predecessor_fabric_history_refs` so cross-parent historical closure and
terminal evidence contributes to lineage and recovery proof but **never
satisfies, invokes, or substitutes for UDOK-4**. **One build or rebuild parent
owns staging, validation, atomic publication, and post-publication B11 LB7
registration**; publication is an effect inside it, never a separate publish
parent and never a second parent log; the **B11 LB7 child is registered before
membership closure, performs its effect only after publication, and its
supported terminal is required before the parent terminal**; and a
**published-but-unregistered** generation is recovered inside that same open
parent without republication, with an already-terminated parent preserved as
history on the fail-closed seam. §18 recovery now branches on both identities
and the recorded parent position and adds row 4f for a claimed cross-parent or
post-terminal UDOK-4, a reused or reopened terminated parent, a missing
new-parent UDOK-1, or a lost predecessor fabric reference (§2, §3.3, §5.2,
§11.0, §11.2A, §11.5–§11.6, §12.2, §13.1–§13.2, §15.1, §17.6–§17.8, §18
protocol and rows 1–3 and 4d–4f, §19.1–§19.2, §21 items 8, 10, 12, 18).

**The two corrections carried in from v1.2 are retained without regression:**
**(A) Generation and plan identity no longer collide with the records they are
required not to reuse.** The projection-generation structural key now carries
`index_identity` and a canonical `generation_lineage_discriminator` derived
from durable predecessor identity together with the exact committed governed
transition, invalidation-replacement, or rebuild evidence — never a nonce,
timestamp, random value, or mutable authorization binding — and the
retrieval-plan key now carries `parent_operation_ref` and the parent
operation's durable `plan_generation`. A same-input rebuild after invalidation,
a lawful successor plan, and records belonging to different indexes are
therefore mechanically distinct, while replay inside one genuine generation
still converges on the existing record (§5.2, §12.2, §13.2, §17.7–§17.8, §18
protocol and rows 1–2, §19.1–§19.2, §21 item 16).
**(B) A reconciled membership-fence violation is no longer indistinguishable
from a fence that was kept.** §18 row 4a now reads the owning component's truth
first and separates the owner's claim, committed effect, and terminal evidence;
permits reconciliation **only** while the generation is current and open and
before closure, and only to append the missing same-generation UDOK-2
registration and the UDOK-6 terminal references durable owner truth supports;
requires a distinct durable `fabric_membership_fence_violation_record`
preserved independently of ordinary membership accounting; and states that
reconciliation never retroactively satisfies the fence, legalizes the effect,
replays or reclassifies the owner's work, or fabricates a terminal. The closed
or superseded contradiction path is unchanged in substance and remains
fail-closed (§3.2, §11.2A, §13.1, §17.6, §18, §19.1–§19.2, §21 item 17).

**The four corrections carried in from v1.1 are likewise retained without
regression:**
(1) the governing order now carries **Decision Defaults S19 v2.3**
as authoritative with v2.2 as superseded history, the unread-source premise is
removed, and the **AIC and UDOK seams are reconciled to their closure-bound
owner mechanics** (§1, §2, §3.3, §3.4, §11.0, §13.3, §17.5, §19, §21, §22);
(2) the **staging/coverage contradiction is resolved on one seam** — staging is
fabric-local and non-queryable with **no LB7 registration and no B11 coverage
state**, and unified-reading participation is downstream of both atomic
publication and committed LB7 (§5.2, §6.1–§6.3, §11.2, §11.6, §11.7, §17.7,
§17.9, §18 rows 2–3); (3) **family 6 now carries the whole B3 theme
lifecycle** — stable identity, membership links, aliases, and every confirm /
reject / rename / merge / split / leave-unresolved event, with current
navigation state derived from that history (§2, §4, §5.3, §10.1, §12.3,
§17.4, §18, §21); (4) the **UDOK membership fence** — UDOK-2 registration
before every child owner effect, one generation-scoped membership head, exact-
head UDOK-6C closure before publication or terminal, **same-parent** UDOK-4
predecessor-closure revalidation, and the fail-closed recovery cases — is
applied to build, rebuild, publication inside its build or rebuild parent,
invalidate, plan, and query (§5.2, §11.0, §11.2A, §11.5,
§12.2, §12.4A, §13.1, §17.6–§17.7, §18 rows 4–4f, §19, §21). Nothing else in
the design was changed, narrowed, or broadened. **Authoritative, accepted,
historical, and source files remain untouched**; nothing was overwritten,
renamed, deleted, or truncated outside this one target file. Nothing was
integrated into Master V10, the Design and Wiring Map, Decision Defaults, or
`cursorrules`. **No implementation, disk, store, index, model, migration,
installation, or runtime action occurred, and none is authorized by this
file.** This file claims **no acceptance, no adoption, no installation, and no
authority**; **bundle placement, controlled component identifiers, and
Register IDs remain unresolved** (§1, §20).

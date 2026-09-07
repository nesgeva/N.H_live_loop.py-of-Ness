# NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md

## 1. STATUS, PURPOSE, AUTHORITY, AND SCOPE

**Status:** CANDIDATE — awaiting ChatGPT's independent audit of this actual
file and Ness's explicit acceptance afterward. **Standalone Bundle 4
design only.** Not authoritative, not adopted, not accepted, not
integrated into Master V10, the Design and Wiring Map, Decision Defaults,
or cursorrules, and **authorizes no implementation** — no coding, no
production store, no runtime, no UI build, no migration, no Cursor
instructions, no live-disk change. No existing file was edited or
overwritten; no acceptance receipt was created.

**Date:** July 10, 2026.

**Version lineage:** this file is the v1_3 corrected successor
candidate to
`NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_2_CANDIDATE.md`
(itself the corrected successor to the v1_1 and v1_0 candidates);
v1_2, v1_1, and v1_0 remain preserved unchanged as historical
candidates.

**Intended repository placement:** `05_ACTIVE_CANDIDATE/`
(the physical move into the repository is Ness's action).

**Purpose:** complete Bundle 4 as one coherent standalone design package:
**A6** (Living State Web policy, from Ness's decisions), **A8**
(action-risk and confirmation mapping, derived from settled authority),
**A18** (the world model beside the self model, from Ness's decision),
**B5** (Computed View snapshot schema and triggered-update mechanics),
**B6** (Living State and world-model structures), **B8**
(possibility/action/result/authorization/violation/correction record
structures), **B27** (action-risk presentation wording), and **B-INT-9**
(corrected Living State evidence fan-in and Computed View downstream
wiring).

**Governing authority order (Master V10 wins where anything disagrees):**
1. `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` — the current
   authoritative Master, adopted by Ness on June 29, 2026; its stale
   file-internal candidate wording is historical text and does not demote
   its authority;
2. `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`;
3. `01_AUTHORITATIVE/cursorrules`;
4. `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`;
5. `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`
   (subordinate working material).

Stale Defaults/cursorrules wording is not repaired here; where they
conflict with Master V10, Master V10 wins.

## 2. PLAIN EVERYDAY EXPLANATION

Bundle 4 designs how N.H keeps an honest, living sense of **where Ness
stands** (states, needs, fears, boundaries, capacity, relationships,
identity over time), an honest sense of **what is going on around him**
(the world model), a private **working picture** it can consult (the
Computed View), and a strict, safe ladder for **anything that could
become an action** — from quietly reading, to writing an internal note,
to preparing something, to actually changing the outside world. In plain
words: N.H watches what it is allowed to watch, keeps careful dated
records instead of opinions, never averages Ness into a single label,
never confuses "this seems related" with "this is true," never lets a
guess become a fact, never acts outside its permissions, and always says
plainly whether anything outside N.H has changed. Nothing here is built —
it is the blueprint for ChatGPT to audit and for Ness to accept or
reject.

## 3. DEPENDENCY AND SOURCE LEDGER (WHAT WAS ACTUALLY READ)

Provenance classes used below: **[v1_0-read]** — directly read during
the original v1_0 drafting session; **[correction-read]** — directly
read during the v1_1/v1_2 correction passes; **[by-reference]** —
consumed by reference through hash-identified accepted records and the
prepared instructions, without a direct re-read in the correction
passes. Nothing is claimed as directly read in the v1_2 pass unless it
actually was.

- **Master V10** — **[v1_0-read]** — the settled sections carried
  into this design and
  read in their retrieved authoritative text: §0A/§0B; §7D (Living State
  Web: node/edge types, grounding rule, currency rule, action surfacing,
  return path designed; schema, evidence thresholds, aging rules,
  trigger specifics, purpose-aware lenses, and world model undesigned —
  the slots this bundle fills); §7F/§7G/§7H (reread's three trigger
  types); §7J; §7K; §7L; §7M (seven-factor ordering; triggered immutable
  snapshots; internal-only); §7N (permission-controlled hybrid; the six
  possibility-disposition states — `accepted and acted on`, `rejected`,
  `modified`, `postponed`, `ignored`, `alternative requested`; the
  gentle-question rule; required/prohibited language); §7O (two result
  types; the six result states — success / partial / failure /
  cancellation / no-or-unknown / incorrect-or-disputed-linkage; three
  separate linked objects; causation rules; never auto-retry); §7P (three
  action states; four risk levels; two authority layers; authorization
  objects; the five-object violation chain; stop-and-surface; the narrow
  emergency-stop exception that never permits completed-world reversal
  without Ness's approval); §7Q (six operations; four sensitivity
  levels; two-stage access; private-access-open-by-default;
  influence-removal separate); §7R (the fourteen settled decisions);
  the open-item register and locked-decision lists.
- **Decision Defaults v2_2** and the **Companion** — **[v1_0-read]** —
  the settled summaries corroborating the above.
- **The map v1.6** — **[v1_0-read]** — C-7D, C-7M, C-7N, C-7O, C-7P,
  C-7Q, C-7R, CY-E (the
  B-CYCLE-5 reservation), and the A8/B8/B27 open-slot routing
  ("B27 depends on A8 and never assigns category-to-risk").
- **Accepted A31** (`NH_A31_GROUNDED_ENOUGH_THRESHOLD_POLICY_v1_0_CANDIDATE.md`,
  SHA-256 `65de6d5f…03b5`, plus its closure record) — **[v1_0-read]** —
  the shared grounding discipline, read from the hash-verified accepted
  copies during the v1_0 drafting.
- **Accepted Bundle 2** (candidate SHA-256 `9c761e59…7da8` + acceptance
  record) — **[v1_0-read]** — relevance labels,
  current-support/action-strictness rules,
  side-drawer rules, B26 fail-closed retrieval.
- **Accepted Bundle 3** (v1_2 SHA-256 `3566cf0f…7c2e` + acceptance
  record) — **[by-reference]** — Person-Box/clash/theme/B-AFFIRM
  foundations consumed by
  reference.
- **The eight-bundle plan** — **[correction-read]** — read **directly
  and in full** from the
  attached repository copy during the correction passes of the current
  working session:
  `03_WORKFLOW/NH_REPLACEMENT_EIGHT_BUNDLE_DEPENDENCY_PLAN_v1_0_CANDIDATE.md`,
  attached at
  `/mnt/user-data/uploads/NH_REPLACEMENT_EIGHT_BUNDLE_DEPENDENCY_PLAN_v1_0_CANDIDATE.md`
  and verified on disk as SHA-256
  `2d6483d133bb3992ba079db43e7d663e8016cf8bf693f7b4c9c98005bcb88415`,
  467 lines, 17,274 bytes. The complete file was directly read,
  including Bundle 4's purpose; its A6, A8, and A18 policy scope; its
  B5, B6, B8, B27, and B-INT-9 mechanical scope; its mandatory wiring
  boundary; and its bundle-complete condition. Ness's approved A6/A18
  decisions and the A8 mapping remain carried verbatim from ChatGPT's
  prepared instruction.
- **The Bundle 4 candidate lineage and correction instructions** —
  **[correction-read]** — the v1_0 candidate was directly read in full
  and copied byte-identically as the v1_1 base (SHA-256
  `d5886c36612fc4a5499efc01db580f4466fbd7dc5393cfcf5cc64360112065ec`,
  833 lines, 49,366 bytes); the v1_1 correction instruction
  (`NH_BUNDLE_4_v1_1_CORRECTION_INSTRUCTION.txt`, SHA-256
  `f240a34bb23d71543861b81f618068a7cc389dda2bf21983c8fdc3a0cec42d5f`,
  268 lines, 10,974 bytes) was directly read in full; the completed
  v1_1 candidate (SHA-256
  `59bca5dd5b50c80906412645aad2b3080a2ec38ee1c9b5e0c27438a973aae4cd`,
  1,158 lines, 69,763 bytes) was produced, hash-verified, and used as
  the v1_2 byte-identical base; the v1_2 correction instruction was
  directly read in full from ChatGPT's prepared text; the completed
  v1_2 candidate (SHA-256
  `bf046cf71bac33611847f8859719b959bc9307b6e7eddc8ed574f35380eeda70`,
  1,330 lines, 80,263 bytes) was produced, hash-verified, and used as
  this v1_3's byte-identical base; the v1_3 correction instruction was
  directly read in full from ChatGPT's prepared text.

## 4. DECISION LEDGER

### 4A. Inherited settled authority (consumed unchanged; none reopened)

One shared, continuous **Meaning Engine**: eligible authorized material
enters through the proper front door (§7E), becomes preserved roots,
receives grounded readings (§7G), and may be reread only under the three
settled §7H triggers; new understanding is appended beside older
understanding; history is never rewritten. The **Living State Web (§7D)
is downstream** of the Meaning Engine and accepted organizational layers
— not a separate learner, memory, AI, fixed profile, clinical classifier,
or manual approval queue. Ness is **not** an approval gate for routine
state creation, currentness review, rereading, or ordinary append-only
internal records; Ness remains policy and authority owner and corrects
N.H through new evidence. The **A31 grounding discipline** applies
throughout: the four labels (`grounded_enough`, `partly_grounded`,
`not_grounded_enough`, `insufficient_context`); no numbers, percentages,
hidden scores, or concealed threshold arithmetic; grounded means
adequately supported within declared scope, not proven true; facts need
direct authorized support; possibilities are evidence-linked, explicitly
unconfirmed, rejectable; repetition/copying/restating/derived records
create no independent evidence; model confidence is metadata; derived
material cannot validate itself; circular support forbidden; unsupported
claims fail safely; genuinely missing context is said, never forced.

### 4B. Ness-approved A6 decisions (carried from the prepared instruction; binding)

**A6-1. Automatic observation and initial state creation.** N.H
continuously watches for possible state changes across authorized
incoming conversation and context. Direct Ness self-report may support
immediate current status. An inference Ness did not directly state
requires **several meaningfully separate grounded messages or signals,
not one**. A newly inferred state begins `possibly_current`. Repeated
copies, restatements, or multiple records derived from the same
underlying event **do not** count as several independent signals. Exact
counts, windows, and empirical tuning are mechanical/calibration work.
This does not authorize surveillance or collection outside permitted
sources. New evidence may strengthen, weaken, correct, end, or supersede
a current interpretation without deleting its history.

**A6-2. Routine currentness decisions.** N.H makes routine operational
decisions about state start, continuation, change, end, and currentness;
Ness is not an approval gate for each case. Ness's direct statements are
strong evidence, not manual authorization steps. Several separate newer
grounded signals may move a state to `ended_by_evidence` or
`superseded_by_evidence`. Weak, mixed, or insufficient evidence produces
`stale` or `currentness_unknown` rather than a false ending. **Time alone
never proves a state ended.** Ness's correction becomes new evidence and
a new linked record; it does not rewrite history. Repeated, recent,
strong grounded evidence may promote `possibly_current` to `current`.
Exact thresholds and time values remain mechanical/calibration matters.

**A6-3. Evidence preservation versus full-state materiality (layered
rule).** *Evidence level:* preserve small, brief, weak, or isolated
signs as evidence when eligible; never discard a sign solely because it
is brief. *Full-state level:* create or materially change a full state
record only when the supported condition meaningfully affects
understanding, capacity, safety, decisions, or action. A small sign may
later join other evidence and form a grounded pattern. Evidence
supporting a reading and materiality justifying a separate state object
are **distinct decisions**.

**A6-4. Simultaneous internal positions.** N.H may preserve several
genuine states or internal positions at the same time. Each remains
separately grounded, currentness-labeled, and revisable. No averaging
into a fake middle; no position cancels another; normal internal
complexity is never framed as disorder; a clash or tension is recorded
only when grounded; Action Surfacing may not choose a winner for Ness.

**A6-5. Possible causes and transition drivers.** N.H may connect a
state or transition to a possible cause when Ness directly states the
connection, **or** several connected grounded signs support it. Every
such connection remains a hypothesis; points to its supporting evidence;
leaves alternatives open; may later be weakened, replaced, disputed, or
corrected; preserves its history. Timing or similarity alone is
insufficient. Routine creation of a causal hypothesis does not require
Ness's approval. §7O's stronger action-result confirmation workflow is
**not** imported into ordinary state hypotheses. For longer causal
chains: every link grounded separately; every link marked hypothetical;
narrative coherence is never proof; a weak, missing, or contradicted
link stays visible and weakens or breaks the chain.

**A6-6. State vocabulary.** A stable core vocabulary for common
emotional, cognitive/thinking, bodily, and practical states, plus
automatically added precise descriptions where the core term is
insufficient. Every added precise state must be grounded, revisable,
linked to a broader/core category, must not require individual Ness
approval, must not be invented without evidence, and must not create
duplicate or synonym fragmentation. The experienced state description
stays separate from any possible cause or transition driver.

**A6-7. Needs, fears, active constraints, protected boundaries.** Needs,
fears, and practical constraints may be represented as careful
possibilities from several separate grounded signs. **Protected
boundaries require stronger evidence:** Ness's direct words, or a clear
repeated pattern of choices, refusals, stopping, withdrawal, or other
boundary behavior. One guess, one emotional moment, or one ambiguous
event cannot create a protected boundary. A protected boundary remains
inspectable and revisable but receives stronger protection before it
influences suggestions, relationship understanding, access, or action.

**A6-8. Capacity and current load.** Separate dimensions, never one
flattened label: thinking capacity; emotional capacity; bodily
energy/capacity; practical capacity; decision-making capacity. An
overall capacity summary may exist only when the separate dimensions
genuinely support it. Low capacity in one dimension never implies low
capacity in all. Capacity, emotional state, wellbeing-baseline
divergence, and identity assessment stay separate.

**A6-9. State aging and currentness.** A state-type/category baseline,
adjusted by the actual situation and later evidence. Relevant factors may
include: stated expected duration; whether the supporting situation
remains active; later supporting evidence; later weakening or
contradictory evidence; whether the state type is naturally brief or
lasting. **Time alone may move a state toward `stale` or
`currentness_unknown`; time alone may never move it to
`ended_by_evidence` or `superseded_by_evidence`.** Exact values and
empirical tuning remain mechanical/calibration matters and are not
invented as policy.

**A6-10. Automatic review trigger (inherited from accepted Bundle 2 and
§7H, not a new choice).** Authorized materially relevant new or changed
material may automatically trigger a state-currentness review. Relevance
only rings the doorbell; a relevance event is not state evidence and
does not change state directly; the review inspects permitted evidence;
uncertain relevance creates only a labeled review suggestion; no real
recorded reason means no review; no blanket rereading; failure never
fabricates freshness, staleness, ending, or change.

**A6-11. Counterfactual scope.** Automatic **internal** counterfactual
reasoning whenever materially useful: N.H may automatically form an
internal modeled possible world for understanding, comparison,
cause-testing, or movement exploration. Every counterfactual must remain
clearly separate from actual events and actual states; be explicitly
hypothetical; identify the actual evidence and assumptions it was
constructed from; remain uncertain and revisable; never become evidence
for itself; never become proof merely because it is coherent; never
rewrite history; never authorize action; never silently become a plan or
prediction. **Boundary:** this permits internal hypothetical paths only.
It does **not** authorize placing Ness inside a visible, immersive,
reconstructed, voiced, or interactive simulation without approval. **A17
(Wonder/simulation memory routing) and A19 (simulation interior) remain
open**; simulation scratch-space material still has no direct route into
memory; neither area is closed or redesigned here.

**A6 domains completed mechanically from existing rules (no new
policy):** *Relationship state and relational safety* — Ness's
experienced relationship state is time-bounded and evidence-linked;
another person's actual words/actions stay separate from Ness's
interpretation and from N.H's interpretation; no objective mutual
relationship fact without direct support; one relationship event never
becomes a fixed profile of the other person; §7Q third-party rules and
§7L identity anchors apply; relationship closeness never weakens privacy
automatically; relational safety status is perspective-scoped, grounded,
currentness-labeled, revisable. *Identity continuity* — Ness's
Person-Box supplies the stable identity anchor; states, positions,
capacities, needs, and relationship conditions stay time-bounded; later
change never erases earlier states; similarity across time may support a
**proposed continuity link**, never a permanent personality essence; no
flattening into a fixed behavioral profile; change, contradiction, and
several simultaneous positions are preserved; connections across time
only when evidence supports them. *Transitions* — a transition is a
proposed evidence-linked movement between time-bounded states; State A
and State B remain separate objects; the transition edge carries
possible drivers separately; no transition merely because two states
occurred in sequence; ending, superseding, transition, and causal
explanation remain distinct.

### 4C. A8 — derived mapping of settled authority (full mapping in §9)

A8 is written in §9 as a clear mapping of the already-settled §7P/§7N/§7O
/§7Q rules — the four risk levels, three action states, two authority
layers, heightened categories, recurring authorization, specialist
systems, evidence/permission separation, stop rules, correction, and the
narrow emergency-stop exception — **not** as new invented policy.

### 4D. Ness-approved A18 decision (carried from the prepared instruction; binding)

**Layered world model.** *Definition:* the world model is N.H's active,
evidence-linked understanding of relevant outside conditions — not
Ness's internal state, not all general knowledge, not a simulation, and
not the visual interface called "Ness's World." *Active core:* maintain
outside-world objects and conditions when they have a real connection to
Ness's life; current relationships; projects; commitments; current
decisions; present environment; available resources; applicable rules or
constraints; current purposes; or events/conditions materially affecting
the above. *Wider knowledge:* remains available in memory and authorized
research; does not become part of the active world model merely because
N.H knows it; enters the active model only when a real connection or
current purpose brings it in; may later leave active status without
being erased from memory. *Required distinctions:* self model vs world
model; internal state vs outside condition; world fact vs attributed
report; direct evidence vs interpretation; current vs historical outside
condition; actual world vs counterfactual possible world; world model vs
the visual "Ness's World" interface; world model vs general research
knowledge; world model vs a third-party psychological profile. *The
world model must:* use the same grounding, provenance, uncertainty,
currentness, append-only, and no-circular-support discipline as the rest
of N.H; preserve source and speaker; keep reports attributed; avoid
claiming direct access to reality; allow stale, unknown, contradicted,
ended, or superseded outside conditions; remain purpose-aware without
letting relevance become truth; avoid maintaining an enormous active
duplicate of all world knowledge. The visual "Ness's World" may present
or navigate world-model objects, but visual manipulation must not
rewrite the world model or its underlying evidence.

### 4E. Deliberately open (preserved, not closed — full list in §15)

A17; A19; B-CYCLE-5 full connected action lifecycle; exact empirical
counts, windows, thresholds, time values, and all calibration/tuning;
model/provider and storage technology; final integrations; Cursor/build
work.

## 5. LIVING STATE WEB — CONCEPTUAL ARCHITECTURE (A6 APPLIED)

- **One engine, downstream layer.** The Web holds no reader of its own:
  every node, edge, and event derives from permitted upstream objects
  (§11) and carries its complete derivation chain back to roots. It is
  organization and currentness over the Meaning Engine's output — never
  a parallel model of Ness, never a profile, never a diagnosis.
- **Creation ladder (A6-1/A6-3):** eligible signs are preserved as
  **evidence** (linked, dated, weightless individually); a **full state
  node** is created only on materiality — the supported condition
  meaningfully affects understanding, capacity, safety, decisions, or
  action; a Ness self-report may ground `current` immediately; a
  non-stated inference needs several meaningfully separate grounded
  signals (records derived from the same underlying event share one
  evidence family and count as one independent signal while every
  individual record remains separately preserved and inspectable —
  §7.2's evidence-family rule; §0B no-double-evidence is honored by
  per-family counting, never by collapsing anything) and begins
  `possibly_current`.
- **Currentness (A6-2/A6-9):** the six settled statuses only —
  `current`, `possibly_current`, `stale`, `currentness_unknown`,
  `ended_by_evidence`, `superseded_by_evidence` — with **no hidden decay
  score**. Promotion to `current` needs repeated, recent, strong
  grounded evidence; endings/supersessions need several separate newer
  grounded signals; weak/mixed evidence yields `stale` or
  `currentness_unknown`; time alone reaches only `stale`/
  `currentness_unknown`; every status change is a dated, reasoned,
  append-only currentness event; the node keeps its recorded initial
  status, the currently usable status is always derived from the latest
  valid applicable currentness event, and no committed node or event is
  ever edited in place.
- **Episode identity (duplicate matching):** every full state node
  represents one time-bounded state episode. Matching distinguishes
  five situations: a definite match to the **same time-bounded
  episode** — the only case that appends support to the existing node;
  a **later recurrence** of the same state category — a new node,
  historically linked to earlier similar episodes where that link is
  grounded; **simultaneous separate positions** — separate coexisting
  nodes (A6-4); a **changed interpretation** — a new node/version
  beside history; an **uncertain possible match** — kept separate or
  turned into an explicit merge/link proposal, never silently merged.
- **Simultaneity (A6-4):** multiple genuine positions coexist as
  separate nodes; tension between them is recorded as a grounded
  clash/tension link only; nothing averages, cancels, or pathologizes.
- **Hypotheses (A6-5):** causal-hypothesis edges carry their evidence,
  alternatives, and hypothetical marker forever; chains ground each link
  separately and inherit their weakest link's visibility.
- **Vocabulary (A6-6):** core-term nodes plus grounded precise
  descriptions linked to a core category; duplicate/synonym
  fragmentation prevented by the mandatory search-before-create step
  (§7's Person-Box discipline applied analogously to state vocabulary);
  description stays separate from cause.
- **Needs / fears / constraints / protected boundaries (A6-7):** careful
  possibility nodes from several separate grounded signs; a
  protected-boundary node requires the stronger evidence rule and
  carries a protection marker that downstream consumers (suggestions,
  relationship understanding, access, action) must honor before use.
- **Capacity (A6-8):** one capacity record, five separate dimensions,
  each independently grounded and currentness-labeled; an overall
  summary field exists only when the dimensions genuinely support it and
  records which dimensions support it.
- **Review (A6-10):** Bundle 2's `state_review_trigger_evaluation`
  purpose emits labeled review-trigger events; the review inspects
  permitted evidence and produces a currentness assessment or a labeled
  suggestion; no reason, no review; failure fabricates nothing.
- **Relationship, identity continuity, transitions:** per §4B's
  mechanical-completion domains, realized as the B6 structures in §7.
- **Counterfactuals (A6-11):** internal-only counterfactual nodes,
  hypothetical forever, evidence-and-assumption listed, never
  self-evidencing, never plans, never simulations.

## 6. WORLD MODEL — CONCEPTUAL ARCHITECTURE (A18 APPLIED)

- **Two layers:** an **active core** of world-model entities and
  conditions meeting the A18 real-connection criteria, and **wider
  knowledge** that stays in memory/research until a real connection or
  current purpose activates it; activation and deactivation are
  append-only membership changes (§7.4), never an erasure.
- **Active-core membership (its own separate dimension):** membership
  in the active core is a distinct append-only lifecycle, permanently
  separate from the six currentness statuses, from truth or grounding
  status, from relevance, from retrieval ranking, from
  operational-record active/cold status (§14.2), and from
  counterfactual status — a world condition may remain current and
  true while no longer belonging to the active core, and a relevant
  item does not automatically enter it. Membership may begin only
  through an evidence-linked qualifying basis already settled by A18:
  a real connection to Ness's life; a current relationship; a project
  or commitment; a current decision; the present environment; an
  available resource; an applicable rule or constraint; a current
  purpose; or an event or condition materially affecting one of these.
  Similarity, semantic resemblance, co-retrieval, repetition, model
  confidence, or relevance alone never creates membership. One world
  object may hold several membership bases or purposes at once, each
  separately referenced; ending one basis never removes the object
  from the active core while another valid basis remains. Deactivation
  occurs only when grounded evidence shows the applicable basis no
  longer applies and no other valid active basis remains — it does not
  erase the world object, does not alter its currentness, does not
  weaken its grounding or provenance, does not move or rewrite the
  underlying memory/research material, and does not imply that the
  outside condition ended.
- **Same discipline as everything else:** every world-model object
  carries A31 grounding, provenance to roots, attributed sources and
  speakers ("world fact" vs "attributed report" is a recorded
  distinction, and reports never silently become facts), uncertainty,
  currentness under the same six statuses, append-only history, and no
  circular support; N.H never claims direct access to reality.
- **The nine required distinctions (§4D)** are structural: self-model
  objects and world-model objects are different record families joined
  only by explicit self↔world connection edges; counterfactual worlds
  are separate node families (§5); the visual "Ness's World" is a
  presentation surface whose manipulations emit proposals/events and
  never rewrite the model or evidence; general research knowledge stays
  outside the active core; no third-party psychological profile is ever
  a world-model object (third parties appear as §7L Person-Boxes and
  attributed conditions under §7Q third-party rules).
- **Purpose-aware, not truth-bending:** relevance (A4/§7R) selects what
  the active core surfaces for a purpose; it never grounds, ages, or
  confirms anything (§11 forbidden list).

## 7. B6 — SCHEMAS AND LIFECYCLE RULES (CONCEPTUAL; NO TECHNOLOGY)

**7.1 Common record contract (every B6 schema carries all of these):**
immediate source-object IDs; direct root IDs; the complete derivation
chain; evidence-family / independence-group identifiers on same-event
derived support (§7.2); A31 `grounding_status`; perspective/subject;
evidence time; state
time range (where applicable); `last_supported_at`; currentness status
(six settled values) and reason; producing rule/version; uncertainty;
clashes/contrary evidence links; creation and supersession links;
privacy/authority references (§7Q sensitivity and access, §7P where
action-adjacent); operation identity; append-only provenance. No field
is a number pretending to be a judgment; no hidden score exists.

**7.2 Schema family (each = the common contract plus its specifics):**
- **state node** — core-term and/or precise description (linked to core
  category); experienced-state content only (no cause inside it);
- **state-version / currentness event** — the dated status change with
  its reason class (new evidence / review outcome / correction /
  aging-to-stale) and evidence pointers;
- **need node / fear node** — careful-possibility marker; the several
  separate grounded signs listed;
- **protected-boundary node** — the stronger-evidence basis (direct
  words, or the repeated-pattern evidence set) and the protection marker
  consumers must honor;
- **active-constraint node** — the practical constraint, its scope, and
  its supporting signs;
- **capacity record** — five dimension slots (thinking / emotional /
  bodily / practical / decision-making), each with its own grounding and
  currentness; optional overall summary with its supporting-dimension
  list;
- **position node** — a genuine internal position, coexisting with
  others; tension links where grounded;
- **transition edge** — from-state, to-state, evidence, and separately
  carried possible drivers; never auto-created from sequence;
- **relationship-state edge** — Ness's experienced relationship state
  toward a §7L-anchored person: time-bounded, perspective-scoped,
  evidence-linked; the other person's words/actions referenced as
  attributed material, never merged into Ness's state;
- **relational-safety record** — perspective-scoped safety status with
  the same discipline; never an objective verdict about the other
  person;
- **causal-hypothesis edge** — hypothesis marker (permanent), evidence
  list, alternatives-open marker, chain-link position where part of a
  chain;
- **counterfactual node** — hypothetical marker (permanent), the actual
  evidence and assumptions it was built from, its purpose
  (understanding/comparison/cause-testing/movement), internal-only flag;
- **temporal-identity / continuity link** — a *proposed* similarity-
  across-time connection between time-bounded objects, anchored to
  Ness's Person-Box; never an essence claim;
- **world-model entity/object** and **world-model condition/state** —
  A18 world objects with attribution and the fact-vs-report
  distinction; their current active-core membership is never an
  editable field on the object — it is derived from the latest valid
  applicable membership event (below), with every membership basis
  separately referenced;
- **world-model active-core membership event** — the immutable
  append-only record of every membership change or evaluation:
  `membership_event_id`; `world_object_or_condition_id`;
  `operation_id`; `previous_membership`; `new_membership` (exactly two
  policy states, `active_core` / `not_active_core` — mechanical labels
  may differ, but no third policy state exists); `basis_type`;
  `basis_reference`; `purpose_scope`; `supporting_evidence_references`;
  `grounding_status`; `reason`; `authorization_reference`;
  `created_at`; `supersedes_or_relates_to_event`;
  `operational_log_reference`; if membership cannot be determined
  safely, the prior membership is preserved and the failed or
  unresolved evaluation is recorded — no membership change is
  invented;
- **self↔world connection edge** — the explicit join between a
  self-model object and a world-model object, evidence-linked;
- **evidence family / independence group** — the explicit relationship
  record grouping supporting objects derived from the same underlying
  event (for example one root together with its readings, restatements,
  copies, derivative references, and the operational records about it):
  every member remains a separate, fully preserved, individually
  inspectable record carrying the shared family identifier; for
  grounding, one family counts as exactly **one** independent support
  unit regardless of how many members it has; an operational log or
  derived record never becomes an additional vote; family membership is
  append-only and never removes, hides, overwrites, or collapses any
  member;
- **evidence/grounding chain** — the ordered chain from a node/edge
  back through readings/tellings/clashes/responses/result evidence to
  roots, preserving **every** supporting object as its own separately
  referenced link — no link is ever collapsed, hidden, deleted, or
  overwritten; links derived from the same underlying event carry their
  shared evidence-family identifier, and independent-support counting
  for grounding is per family, not per link;
- **review-trigger event** — the Bundle 2 relevance event reference, its
  label, and the recorded reason (or the labeled-suggestion-only
  outcome);
- **currentness assessment** — the review's inspected evidence, outcome
  status, and reason;
- **omission / insufficient-grounding record** — the honest record that
  a state/condition question arose and could not be responsibly
  answered (`insufficient_context` / `not_grounded_enough`), preserved
  instead of a forced object.

**7.3 Lifecycle (all append-only; nothing edited in place):** initial
creation (evidence-first, materiality-gated) → evidence accumulation
(the chain grows; every new supporting record is preserved as its own
link; same-event derivatives join their evidence family and add no
additional independent support) → review trigger (A6-10) →
currentness reassessment (dated event) → promotion
`possibly_current`→`current` (A6-2 evidence rule) → movement to
`stale`/`currentness_unknown` (weak/mixed evidence or time-plus-baseline)
→ evidence-based ending/supersession (several separate newer grounded
signals; supersession links old→new) → later reactivation or changed
interpretation (a **new** node/version beside history, never a
resurrection-in-place) → correction through new evidence (Ness's
correction = new linked record). **Currentness is append-only:** the
node keeps its recorded initial status; every later change is a new
dated currentness event; the currently usable status is always derived
from the latest valid applicable currentness event; no committed node
or currentness event is ever edited in place. **Duplicate prevention
(episode-qualified):** one time-bounded state episode, one open node.
Creation runs search-before-create across existing nodes, vocabulary,
and open omission records, then classifies the candidate match: a
**definite match to the same time-bounded episode** is the only case
that appends support to the existing node (a new evidence link and,
where warranted, a new currentness event); a **later recurrence of the
same state category** receives a **new node**, historically linked to
earlier similar episodes where that link is grounded; **simultaneous
separate positions** remain separate coexisting nodes (A6-4); a
**changed interpretation** becomes a new node/version beside history;
an **uncertain possible match** remains separate or becomes an explicit
merge/link proposal — it never silently merges. Duplicate prevention
governs node identity only: it never removes, hides, overwrites, or
collapses any root, reading, telling, clash, response, result item,
derivative reference, evidence link, or operational record.
**Crash/partial-write
recovery:** committed records are authoritative; an in-flight creation
or assessment without a committed outcome resolves to a recorded
incomplete event, never a half-node. **Technical retry:** bounded, under
the accepted B9 mechanics and recorded values, by reference. **Fail
closed:** anything ungroundable produces the omission record, never a
forced state, ending, or freshness.

**7.4 World-model active-core membership lifecycle (A18 applied;
append-only):** activation creates a new membership event on an
evidence-linked qualifying A18 basis — it never edits the source
memory/research object and never converts relevance into evidence;
deactivation creates a new membership event only when grounded
evidence shows the applicable basis no longer applies and no other
valid active basis remains, and it changes membership only (§6's
deactivation non-effects). **Duplicate prevention and recovery:** one
membership evaluation is one operation with a stable operation
identity; repeated evaluation of the same object, basis, purpose, and
source version is idempotent and resolves to the committed event;
crash before the membership-event commit resolves to a recorded
incomplete evaluation with the prior membership standing; a committed
membership event discovered without its operational log receives the
missing log by append-only reconciliation (§13) — never a re-run and
never a duplicate event; a failed or unsafe evaluation preserves the
prior membership and records the failure; technical retry is bounded
under the accepted B9 mechanics by reference; everything fails closed
— no membership change is ever invented, and reconciliation never
duplicates events.

## 8. B5 — COMPUTED VIEW SNAPSHOT SCHEMA AND REFRESH LIFECYCLE

**Preserved Master rules (binding, unchanged):** internal tool only;
never shown unprompted (Ness may deliberately request a look); creates
no interpretations; decides no truth; resolves and suppresses no clash;
rewrites no root, reading, telling, state node, Person-Box link, or
response; **all objects linked, never copied**; §7D is an input to §7M
and **§7M is never an input to §7D**; held pre-ingest raw content never
influences the snapshot — only safe **metadata-only** pre-ingest
references may appear (source-carried safe metadata, lifecycle state,
and blocker information; never held raw content, and no indirect route
to raw content); **no sealed TSC inspection path, token, or mechanism
exists, and none may be introduced**.

**8.1 Ordering-profile record (immutable, versioned) — fields:**
`view_profile_id`; `profile_version`; `profile_purpose_type`; an
optional human-readable purpose label; `consuming_component`; the
authorization and privacy basis; the eligible source-reference
families (drawn only from the ten Master-permitted families in §8.2);
the settled seven factors **in their fixed order**; the disclosed
factor-specific ordering, tie, omission, and surfacing rules; an
explicit **no-hidden-score declaration**; the relevant §7R Tier-1
configuration reference; the relevant component-owned Tier-2
configuration reference; the declared refresh triggers; the declared
invalidating events; the unresolved-dimension handling reference where
applicable; `derivation_rule_version`; `created_at`; the prior or
superseded profile-version reference; operational-log reference.
**Rules:** a committed profile version is immutable; any change
creates a new profile version; earlier versions remain preserved and
inspectable; every snapshot and refresh attempt binds to the exact
profile ID and version used; the settled seven-factor order can never
be silently reordered; a profile may disclose different
purpose-specific handling without turning any factor into hidden truth
authority; no empirical significance threshold, timing value, score,
weight, model choice, or calibration value is invented here; a
missing, invalid, stale, or unauthorized profile configuration fails
closed and creates the applicable `failed` or `incomplete`
refresh-status event — it never creates a snapshot; re-running the
same profile-version operation is idempotent; crash and reconciliation
follow the §8.6 and §13 append-only rules.

**8.2 Snapshot record (immutable forever once committed) — fields:**
`snapshot_id`; `operation_id`; `view_profile_id` and `profile_version`
(the exact §8.1 ordering profile this snapshot was produced under);
trigger type and trigger object;
authorization/purpose basis (§7Q internal-use authorization reference);
**source-reference fields — one per Master-permitted source family,
every object linked by ID and never copied:** direct root references;
reading references; telling references; clash references;
Ness-response-event references; Person-Box-link references; theme
references; Living State references; world-model references; safe
metadata-only pre-ingest references; **ordering-factor results per
settled seven-factor order, each factor's outcome recorded separately —
no collapsed score**, with **factor 2's direct-root-evidence outcome
pointing directly to the supporting direct root references** (roots
linked by reference, never copied; repetition, restatement, and
same-event derivatives add no evidence strength — §7.2's
evidence-family rule applies); active clashes and uncertainty carried
visibly; omitted/set-aside candidates **with reasons**; prior snapshot
reference; changed-from-prior description; derivation-rule version;
`created_at`; **committed completeness status** (including the settled
"no clear current view" outcome), recorded at commit and never changed
afterward; privacy/output eligibility references; operational-log
references. **The snapshot carries no mutable status field:** standing,
superseded, and possibly-stale are never written onto a snapshot — they
are derived exclusively from the later append-only refresh/status
events below. No committed snapshot is ever edited, marked, rewritten,
invalidated, or altered in place by any later refresh, failure,
supersession, or staleness determination.

**8.3 Refresh/status event record (append-only; one per
refresh-attempt outcome) — fields:** `event_id`; `operation_id`;
`attempted_profile_id_and_version` (the exact §8.1 profile record and
version attempted); `attempted_trigger`;
`standing_snapshot_id` (the last valid standing snapshot the event
refers to — on `success`, the newly standing snapshot); `outcome` —
exactly one of `success` / `null_update` / `failed` / `incomplete` /
`possibly_stale`; `failure_or_incompleteness_reason`; `created_at`;
`retry_eligibility`; `retry_attempt_reference`;
`operational_log_reference`. **Standing-view derivation:** which
snapshot is the current standing view, and whether it is possibly
stale, is always derived from the latest valid applicable
refresh/status events — never from any field on a snapshot.

**8.4 Refresh lifecycle:** triggered updates only (the settled §7M
triggers); each refresh is one operation producing at most one new
immutable snapshot plus its append-only refresh/status events.
**Success:** the new snapshot commits and a `success` event makes it
the standing view through that new append-only status relationship
only; no earlier snapshot is rewritten, invalidated, or altered —
earlier snapshots remain intact history. **Null update:** a refresh
finding nothing changed commits a `null_update` event referencing the
unchanged standing snapshot — a valid outcome that never creates a
duplicate snapshot. **Failure:** a failed refresh creates a `failed`
event pointing to the last valid standing snapshot; the interface
derives "possibly stale" from that later event, and where the
staleness determination is itself recorded it is recorded as its own
append-only `possibly_stale` event — never as a mark on the old
snapshot, which is never changed. **Incomplete:** a refresh that
cannot finish commits an `incomplete` event with its reason; nothing
half-built ever becomes visible.

**8.5 Duplicate prevention:** one completed operation + one
source/version set → at most one snapshot (re-runs resolve
idempotently to the committed one); null updates and failed or
incomplete refreshes create events only — they can never create a
duplicate snapshot or a falsely fresh one.

**8.6 Crash and recovery (cases distinguished):** (a) **crash before
snapshot commit** — no snapshot exists; recovery appends an
`incomplete` refresh/status event; the last valid snapshot stands;
(b) **committed snapshot, then refresh-status write failure** —
startup recovery detects the committed snapshot missing its status
event and appends the missing event (append-only reconciliation); the
refresh is never re-run, and the snapshot is never duplicated or
edited; (c) **refresh failure while an older valid snapshot exists** —
the `failed` event points to that standing snapshot and "possibly
stale" is derived from it; (d) **partial or incomplete refresh** —
recorded honestly as `incomplete` with its reason; partial writes are
never visible (commit is all-or-nothing at the record level);
(e) **bounded technical retry** — technical failures only, under the
accepted B9 mechanics and recorded values by reference, tracked
through `retry_eligibility` and `retry_attempt_reference`; (f) **fail
closed** — no refresh ever fabricates a fresher picture than its
inputs support; when freshness cannot be established, the honest event
stands and the last valid snapshot remains the derived standing view,
visibly aged, never silently refreshed. No storage or implementation
technology is selected.

## 9. A8 / B8 — ACTION-RISK MAPPING AND RECORD ARCHITECTURE

### 9.1 A8 — the base classification (mapping of settled §7P; nothing new)

Base level is determined by **what physically happens now**. It
classifies N.H's current operation — the `current_authority_level` of
what N.H is physically doing at this moment — never the possible future
action, whose expected level is always carried separately as
`prospective_action_level` under §9.2's stage/level contract; one
ambiguous level never describes both at once:
- **Level 1 — internal read-only:** reads, searches, retrieves,
  compares, calculates, or examines authorized N.H material; no domain
  record or outside object changes; automatic within applicable §7Q,
  §7P, identity, and purpose boundaries; the mandatory §0B
  operational-log append recording the read is a separate linked
  Level-2 internal write (§14.1) — it never reclassifies the read and
  is never merged or double-counted with it.
- **Level 2 — normal validated append-only internal write:** adds a
  reading, state node, state version, currentness event, clash,
  snapshot, surfaced possibility, link proposal, operational record,
  or other permitted
  derived internal object; existing history never modified in place;
  automatic only within accepted schema, validation, and authority
  rules.
- **Level 3 — prepared external action:** drafts, stages, assembles, or
  prepares something intended to affect the outside world; nothing
  outside N.H has changed yet; the prepared object must be inspectable
  and shown before execution; **preparing never authorizes execution**.
- **Level 4 — executed external action:** sends, submits, publishes,
  saves to an outside system, purchases, contacts, calls a tool/service
  with external effect, changes an external account, or otherwise
  changes anything outside N.H; requires **exact preview, explicit
  applicable authorization, and a post-execution record**; an action is
  `executing` and Level 4 **only when an outside effect actually begins
  or occurs under the applicable authorization** — a request for
  approval, preview, or confirmation is not execution, and if no
  outside effect began or occurred, nothing is recorded as Level-4
  execution. Practical test: **if anything outside N.H changed,
  execution occurred; if nothing outside N.H changed, it did not.**

**Heightened categories** — medical, legal, financial,
privacy-sensitive, relationship-affecting, destructive, irreversible —
always require **specific per-instance confirmation**; they are not a
fifth level; they add stricter protection to the applicable base level
**because, according to the applicable category, the action may
materially affect health, legal rights or obligations, money, privacy,
relationships, safety, or protected or destructive material, or may be
difficult or impossible to undo** — not because every heightened action
is irreversible. A proposal's heightened categories attach to the
prospective action and are carried separately
(`prospective_heightened_categories`) until the applicable stage.
**A narrow recurring execution authorization** may cover only ordinary
actions inside its exact recorded scope and must define: exact action
type; exact destination/recipient; trigger or frequency; content/value
limits; permitted tools; start and expiry; audit and notification
requirements; pause/revocation behavior. It cannot spread to similar
actions, cannot survive changed conditions outside its scope, and cannot
replace per-instance confirmation for absolute heightened categories.
**Strictest applicable rule wins.** **Specialist systems stay
specialist** (never downgraded to ordinary Level 2): protected
code/configuration/security/device-trust changes use BGMM; privacy
handling, deletion, restriction, hiding, redaction, and influence
removal use §7Q; production-reading promotion keeps its dual
authorization; TSC promotion keeps BAI/SACL authorization;
identity/security operations keep §25 safeguards. **Evidence and
permission are permanently separate:** strong evidence never grants
permission; permission never proves a suggestion evidence-supported;
active suggestions require current support under accepted Bundle 2;
gentle protective possibilities may use older/weaker support when
clearly labeled; partly grounded support permits only narrowed or
uncertain possibilities; unsupported support cannot produce a confident
active suggestion; retrieval failure is never replaced with invented
support. **On ambiguity, changed conditions, expired authority, access
reduction, or unexpected result: stop; prevent later steps; record;
surface clearly; seek the required new authorization.** **Correction is
a new action** with its own risk level, preview, authorization,
execution record, and possible result — never automatically authorized
by the original mistake. **The narrow pre-authorized emergency-stop
exception is preserved exactly as Master V10 defines it** — it never
permits completed-world reversal without Ness's approval — and is not
broadened here.

### 9.2 B8 — record structures (each carries §13's design contract plus
its specifics; all append-only, all linked by stable IDs)

**Stage/level contract (every possibility/action-family record carries
all five, always separately):** `current_action_state` — exactly one of
`suggesting` / `preparing` / `executing`; `current_authority_level` —
the authority/risk level of what N.H is physically doing now,
classified per §9.1 by the current operation itself (committing a new
record is Level 2; a pure read or display is Level 1);
`prospective_action_level` — the expected level if the proposed action
later advances; `prospective_heightened_categories` — the heightened
categories the prospective action would touch;
`advancement_requirements` — what must happen (disposition,
preparation, authorization, or other stated condition) before the
record may move to the next stage. The current stage and the possible
future are never merged into one ambiguous classification.

- **surfaced possibility** — the settled §7N record (derivation, why
  reachable now, assumptions, uncertainty, limitations/risks) plus its
  support labels under Bundle 2 and the stage/level contract fields:
  `current_action_state` = `suggesting` — stage metadata that never
  turns the possibility record into an action record (a surfaced
  possibility is a possibility record under settled §7N; a later
  prepared or executed action is a separate linked object); no outside
  effect exists; no preparation exists; `current_authority_level`
  reflects the actual current operation — creating and committing the
  new surfaced-possibility record is a **Level-2** append-only
  internal write, while later retrieving or displaying the already
  committed possibility without creating a new domain object is
  **Level 1**, and nothing is ever modified in place; the possible
  future Level 2, 3, or 4 action it describes is
  recorded separately as `prospective_action_level`, with
  `prospective_heightened_categories` recorded separately as well;
  `advancement_requirements` state what must happen before any
  advancement; surfacing creates **no execution authority** and does
  not mean Ness accepted, prepared, or approved anything;
- **possibility disposition/response** — one of the six settled §7N
  states, recorded per the settled meanings; ignored requires no event;
  nothing resurfaces without a new trigger;
- **prepared action** — the Level-3 object (`current_action_state` =
  `preparing`; `current_authority_level` = Level 3; nothing outside
  N.H has changed): exact content, target, tool, scope, the possibility
  it came from, and its inspectable preview form; its
  `prospective_action_level` (the exact execution level if it later
  advances) and all `prospective_heightened_categories` carried
  separately; its `advancement_requirements` stating exactly what
  authorization is still missing; a prepared action can never be
  treated, worded, logged, or displayed as executed;
- **authorization object** — the settled §7P object binding a specific
  approval (moment-level or standing) to the **exact** prepared-action
  identity, exact content/version, exact destination or recipient,
  exact tool, exact prospective execution level, exact heightened
  categories, and the applicable conditions and expiry (or to an exact
  recurring scope), with its basis and time; approval permits **only
  the stated advancement** — it does not prove the suggestion correct,
  does not approve later changed content, another destination, or
  another action, and never retroactively turns preparation into
  execution; a granted approval never itself records, proves, or
  implies that execution began, that an outside effect occurred, or
  that the action succeeded;
- **recurring authorization object** — the eight required scope fields
  (§9.1) plus audit/notification and pause/revocation state;
- **execution attempt** — one dated attempt under one action identity,
  bound to its authorization and exact preview version; an attempt is
  not execution — the action is never labeled executed merely because
  an attempt began;
- **executed action** — the post-execution record, created only when an
  outside effect actually began or occurred under the applicable
  authorization (`current_action_state` = `executing`;
  `current_authority_level` = Level 4): what changed
  outside, when, through what, under which authorization and preview;
- **result root reference** — the §7O result material (reported or
  detected) as a normal root, referenced never copied;
- **proposed action-result connection** — the settled §7O proposal
  (action ID, root/capture ID, why connected, timing, uncertainty,
  alternatives, detector);
- **confirmed/rejected/disputed connection** — Ness's response on the
  connection as a separate event; disputed linkage never rewrites the
  action record;
- **result-state assessment** — one of the **six settled §7O result
  states** (success / partial / failure / cancellation / no-or-unknown /
  incorrect-or-disputed-linkage), consumed unchanged, never redefined;
- **authority violation record**, **corrective proposal**, **approved
  correction**, **corrective execution**, **observed correction
  result** — the settled five-object violation chain, each object
  separate, the correction chain itself classified and authorized as a
  new action;
- **emergency-stop record** — the narrow settled exception's own dated
  record: condition met, what was stopped, what was not reversed.

**Separations (binding):** possibility ≠ action; current stage ≠
prospective level; preparation ≠ attempt; attempt ≠ outside effect;
action ≠ result;
result event ≠ result connection; result connection ≠ causal
explanation; correction ≠ original action; violation ≠ correction;
**an observed outcome is not success merely because it followed
execution** — timing/similarity never prove causation.

**Protections (design-contract level):** stable **action identity**
across the possibility→disposition→prepare→authorize→execute→result
chain; **no double execution** — one action identity commits at most one
executed effect, and an execution attempt whose external effect is
uncertain **may not be retried**; **authorization binding** — execution
is valid only against a live, in-scope authorization; **exact preview
binding** — the executed content must be the previewed content, version
-bound; **changed-condition invalidation** — if the prospective
action's content, target, tool, circumstances, level, or heightened
categories change, the chain stops; the old prepared action and its
authorization history are preserved unchanged; the required new
preparation/preview is created and new applicable authorization
obtained; the old authorization is never silently expanded;
**post-execution record**
mandatory; **partial completion** recorded honestly as partial with what
did and did not change; **unknown external state** recorded as
no-or-unknown, frozen pending reconciliation; **cancellation** recorded;
**access reduction during execution** triggers stop-and-surface;
**crash before effect** resolves to a recorded non-execution; **crash
after possible effect** resolves to unknown-external-state with
**retry prohibited** and **reconciliation required before any new
execution** of that identity; **fail closed** everywhere ambiguity
exists. **This package does not close B-CYCLE-5:** the composed
end-to-end action lifecycle — the connected loop's operation identity,
cross-stage transaction boundaries, and full-cycle recovery — remains
open exactly as the map's CY-E reserves it.

## 10. B27 — PRESENTATION WORDING (DESIGN LEVEL; DEPENDS ON A8; ASSIGNS NO CATEGORY-TO-RISK)

Plain wording per situation (illustrative canonical forms; exact visual
styling open):
- **L1 internal read:** "I only read permitted N.H material for this
  task. I did not change the source material or anything outside N.H;
  N.H added the required append-only operational record of the read."
- **L2 internal append:** "I added an internal note/record. Your history
  is untouched; nothing outside N.H changed."
- **L3 prepared:** "I've prepared this — here is exactly what it is.
  **Nothing has happened yet.** It will not go anywhere unless you
  approve it."
- **Level-4 execution preview and approval request — current state:
  prepared; nothing outside N.H has changed yet:** "If you approve and
  the recorded conditions remain valid, N.H is authorized to attempt
  this exact outside action: [exact preview]. Approval authorizes only
  this exact attempt; it does not confirm that the outside change
  occurred or succeeded. Right now, nothing outside N.H has changed."
- **Heightened-category warning:** "This touches [medical / legal /
  financial / privacy / a relationship / something destructive /
  something irreversible], so it needs your specific confirmation for
  this exact instance — because, depending on the applicable category,
  it may materially affect your health, your legal rights or
  obligations, your money, your privacy, a relationship, safety, or
  protected or destructive material, or may be difficult or impossible
  to undo."
- **Exact preview:** always the literal content/target/tool — never a
  summary standing in for the thing itself.
- **Recurring-authorization scope:** "This standing permission covers
  exactly: [type / destination / trigger / limits / tools / start–
  expiry]. It covers nothing similar outside that, and it pauses if
  conditions change."
- **Changed-condition stop:** "Something changed since you approved
  this, so I stopped before doing anything further. Here's what changed."
- **Ambiguous authority:** "I'm not certain I have permission for this,
  so I stopped and I'm asking rather than guessing."
- **Violation and correction:** "This step went outside its authority.
  I stopped, recorded it, and here is a possible correction — the
  correction itself needs its own approval."
- **Unknown execution outcome:** "I can't confirm whether the outside
  change happened. I won't retry until we've reconciled what actually
  occurred."
- **Partial completion:** "Part of this completed and part did not —
  here is exactly which is which. Nothing further will run without your
  say."
- **No-auto-retry warning:** "Because the outside effect is uncertain,
  I will not retry automatically — retrying could make it happen twice."

**Behavior rules (binding):** possibilities use "one possible option,"
"this may be reachable," or "you could consider"; never "you should,"
"you need to," or "you must" for ordinary possibilities; risk labels
explain **what will physically change** and always separate the current
stage from the prospective level; **every displayed action wording
makes four things clear: the stage N.H is in now; what could happen
next; what permission is still missing; and whether any outside effect
has already occurred**; **approval, execution attempt, actual outside
effect, confirmed result, and failed, partial, or unknown outcome are
always distinguished in wording — approval is presented as permission
for the exact recorded attempt, never as proof that execution began,
that an outside effect occurred, or that the action succeeded**; risk
wording never pressures
Ness; preparation is never presented, worded, logged, or displayed as
execution; execution approval is
never presented as agreement with N.H's reasoning; "nothing has happened
yet" versus "outside change will occur" is always explicit; heightened
categories state **why** specific confirmation is required using the
applicable category's accurate reason — never implying that every
heightened action is irreversible; **silence is
never approval**; side-drawer and main-answer wording follow accepted
Bundle 2.

## 11. B-INT-9 — CORRECTED WIRING

```
PERMITTED SOURCE EVIDENCE ──────────────►  §7D LIVING STATE WEB
  permitted readings (§7G)                     │ (evidence fan-in only)
  §7K tellings                                 │
  §7J clash records                            ▼
  Ness-response events                    §7M COMPUTED VIEW
  §7O result evidence                          │ (downstream only)
  §7L Person-Box identity anchors              ▼
                                          §7N ACTION SURFACING
GOVERNORS / GATES (never evidence):            │
  §7Q privacy · §7R relevance · §7P authority  ▼
                                     §7O return → normal root/reading/
                                     reread path (new evidence re-enters
                                     through the front door)
```

**Forbidden, permanently:** §7M → §7D as evidence; §7R relevance score →
state currentness; §7P permission → evidence; §7Q eligibility decision →
evidence; held raw pre-ingest content → §7D or §7M; sealed TSC
inspection (no inspection token, mechanism, or path exists); logs
serving as additional proof of the event they record; any
relevance→currentness→relevance circular support loop.

**Pre-ingest references:** only safe **metadata-only** references may
appear where permitted — source-carried safe metadata, lifecycle state,
blocker information — never held raw content.

## 12. PRIVACY, AUTHORITY, AND NO-CIRCULAR-SUPPORT CHECKS

Every Bundle 4 structure and operation runs behind §7Q's purpose-specific
authorization (internal-use for §7D/§7M assembly; visible-output
eligibility plus SACL order for anything shown); third-party material
follows §7Q third-party baseline and sensitivity levels; protected
boundaries and compartment/TSC/influence-removal restrictions apply
regardless of purpose; relationship closeness never weakens privacy;
§7P governs every action-adjacent step; **§7Q/§7R/§7P are gates and
governors, never evidence**; derived material (snapshots, assessments,
chains, hypotheses, counterfactuals, world-model conditions) can never
validate itself, vote twice, or launder a possibility into a fact;
same-event derivation, repetition, copying, and restating add no
independent support — independent-support counting is per evidence
family (§7.2) while every underlying record stays preserved and
inspectable; A31's less-claiming rule governs every grounding call.

## 13. OPERATION IDENTITY, DUPLICATE PREVENTION, CRASH RECOVERY, RETRY, FAIL-CLOSED (DESIGN CONTRACT FOR EVERY B5/B6/B8/B27/B-INT-9 OPERATION)

Stable **operation identity**; **idempotency key** derived from it plus
the source/version set (for Computed View operations the version set
includes the exact §8.1 `view_profile_id` and `profile_version`); a
declared **transaction/commit boundary** (one
commit, all-or-nothing at record level); **duplicate prevention** (one
identity, at most one committed outcome; re-runs resolve to it; it
never removes, hides, overwrites, or collapses any committed record —
state-node identity follows §7.3's episode-qualified matching);
**crash detection** (in-flight-without-outcome discovered at startup);
**startup recovery decision** (resolve to recorded failure/incomplete,
never assumed success); **committed-but-unrecorded reconciliation** (a
committed outcome discovered at startup without its expected status or
operational record receives that missing record by append-only
reconciliation — the operation is never re-run and the committed
record is never edited or duplicated; §8.6(b)); **partial-completion
representation** (honest
partial records, never silent halves); **retry eligibility** (technical
failures only; external-effect-uncertain never retries); **retry limit
ownership** (the accepted B9 mechanics and recorded Ness values, by
reference — no value re-chosen here); **external-effect uncertainty
handling** (freeze, reconcile, then decide); **stage integrity**
(recovery never advances a record's `current_action_state`, never
converts a preparation or an attempt into an executed action, and never
records Level-4 execution without an actual outside effect — an
interrupted stage recovers as its honest recorded state or as
incomplete; a granted approval alone never advances the state — only
an actual outside effect makes an action `executing`); **active/cold
status evaluation** (a status evaluation is
itself one operation under this contract: when eligibility cannot be
safely determined it commits a failed-evaluation record and preserves
the previous active/cold status, never silently cooling, reactivating,
dropping, or reprioritizing the record, and a cooling outcome commits
only when both settled §14.2 conditions are established); **world-model
membership evaluation** (likewise one operation under this contract:
an undeterminable evaluation commits a failed or unresolved record and
preserves the prior membership — §7.4); **level accounting** (the
domain operation carries its own §9.1 level determined by what it
itself does; its mandatory operational-log append is a separate linked
Level-2 internal write under the same operation identity, never merged
with or double-counted against the domain operation); **fail-closed
state**
(named, committed, honest); **append-only audit record** (§14). No
database, language, framework, timing value, model, numeric threshold,
or implementation technology is selected.

## 14. §0B TRANSPARENCY / RECORDKEEPING (B-INT-11 DISCIPLINE)

**14.1 Operational record.** Every designed operation creates **one
connected append-only operational record** covering: what was
evaluated; what was used; what was not used; why something was omitted
or set aside; success; failure; retry; crash recovery; prior-record
use; resulting object IDs. One real operation → one operational log;
no recursive logs about logging. The operational-log append is itself
a **Level-2 append-only internal write**, separate from and linked to
the domain operation it records: an otherwise Level-1 read/retrieval
operation remains classified as the Level-1 domain operation while its
required log is the separate Level-2 write; the log never becomes
evidence and never makes the underlying information stronger; the
domain operation and its operational-log write are never merged or
double-counted. For action-family operations the
operational record states the `current_action_state` and
`current_authority_level` at the time of the operation, with any
prospective level noted separately — a preparation, preview, approval
request, or granted approval is never logged as execution. Creating or
versioning a Computed View ordering profile (§8.1) and evaluating
world-model active-core membership (§7.4) are themselves operations
under this rule.
Operational records **do not increase evidence strength** and are never
second votes — where an operational record concerns an event already
serving as support, it carries that event's evidence-family identifier
(§7.2) rather than adding a vote; each operational record remains an
individually preserved record that duplicate prevention never
collapses, merges, hides, or deletes; they remain retrievable and
inspectable under authorization; and they obey §7Q, §7P,
identity/security, TSC, compartment, and influence-removal rules.

**14.2 Active/cold operational-record lifecycle (complete design
contract for every B5, B6, B8, B27, and B-INT-9 operational record).**
*Active status:* **every newly committed Bundle 4 operational record
begins `active`, without exception**; its initial `active` status and
every later status change are represented append-only through the
§14.3 lifecycle/status events, and the operational record itself is
never edited. A record **remains** active while at least one of these
protection conditions applies: it belongs to an unresolved or
in-progress operation; it is referenced by the current valid state,
view, world-model, or action chain; it is needed for a pending
recovery, retry, reconciliation, violation handling, or correction; it
is actually being used by an authorized component; or it is receiving
a valid new link under the governing connection rules. These
protection conditions are not an exhaustive shortcut: their momentary
absence alone never permits cooling. *Cooling-rule ownership:* each
consuming component — B5
Computed View, B6 Living State and world model, B8
possibility/action/result/authorization/violation/correction, B27
presentation, B-INT-9 wiring — owns one fixed, declared, versioned
cooling rule; the rule may use record category and operation/lifecycle
status; it may use **no hidden score**; exact time values remain
calibration values and are **not invented in this candidate**; N.H may
propose a future cooling-rule change only with quantitative evidence
and concrete examples, and no cooling-rule change becomes operative
without Ness's approval. *Cooling:* a record may move from `active` to
`cold` **only when both** settled conditions are true: it is old
according to the fixed, declared, versioned cooling rule for its
operational-record type, **and** it is no longer being genuinely used
and is not receiving valid new links — neither condition alone permits
cooling. Cooling creates a new append-only
status event and changes **only** active/cold presentation and
retrieval priority; it never edits, deletes, weakens, disconnects,
overwrites, or replaces the original operational record; it never
changes evidence strength, grounding, truth status, authority,
provenance, or history; and it never makes a record inaccessible where
an authorized exact retrieval requires it. *Reactivation:* a cold
operational record may reactivate only when it is actually used by an
authorized operation, or when a valid new link established under the
governing connection rules connects it to active work — no additional
manual approval is required for reactivation unless the governing rule
for that particular link already requires it; reactivation creates a
new append-only
status event, preserves the cold history, does not edit the original
record, does not make the record new evidence, and does not create
another vote or increase evidence strength. Semantic search may
rediscover a cold record as a retrieval fallback, but retrieval,
similarity, semantic
resemblance, co-retrieval, ranking proximity, time, model confidence,
or repetition can **never** reactivate a record by themselves — only
actual authorized use or a valid new link under the governing
connection rules can, always append-only and never rewriting the
original record.
*Failure and uncertainty:* if cooling or reactivation eligibility
cannot be safely determined, the previous active/cold status is
preserved and the failed status-evaluation operation is recorded; the
record is never silently cooled, reactivated, hidden, dropped, or
reprioritized — fail closed without changing evidence or authority.

**14.3 Operational-record lifecycle/status event (conceptual;
append-only) — fields:** `lifecycle_event_id`; `operational_record_id`;
`operation_id`; `component_owner`; `cooling_rule_id_and_version`;
`previous_status`; `new_status`; `reason`;
`triggering_use_or_link_reference`; `authorization_reference`;
`created_at`; `evaluation_outcome`; `failure_reason_if_any`;
`operational_log_reference`. The permitted status values are exactly
`active` and `cold`. Every newly committed operational record's first
lifecycle/status event records its initial `active` status at commit
(`previous_status` is empty for that first event — there is no prior
status to supersede). A failure to determine status creates a failed
evaluation record and preserves the previous status — it never invents
a third lifecycle status.

**14.4 Separation from domain events.** Domain status events (for
example §7's currentness events, §7.4's world-model membership events,
§8's refresh/status events, and §9's
action stage and result events) are domain records, not operational
logs: each real operation still creates exactly one operational
record, which the domain status event references
(`operational_log_reference`); the two record kinds are never merged,
and neither ever substitutes for — or double-counts as — the other.
Operational-record lifecycle/status events (§14.3) are a third,
separate kind: a Living State currentness event is not an
operational-record active/cold event; a world-model membership event
is not an operational-record active/cold event; a Computed View
refresh/status
event is not an operational-record active/cold event; an action
stage/result event is not an operational-record active/cold event;
each kind remains separately linked and must not double-count.

## 15. EXPLICIT NON-GOALS AND OPEN DEPENDENCIES

This candidate does **not** and must never be read to: close **A17**
(Wonder/simulation output-to-memory policy) or **A19** (simulation
interior and interface) — simulation scratch-space still has no route
into memory; close **B-CYCLE-5** (the full connected action lifecycle —
open exactly as the map reserves it; the accepted plan does not assign
its closure here); choose any exact empirical count, time window,
calibration or tuning value; choose model/provider or database/storage
technology; fix implementation field types beyond conceptual schema;
design UI visual styling beyond B27's wording behavior; perform final
Master or map integration, or Defaults/cursorrules integration; produce
Cursor/build instructions, production stores, or runtime work; or touch
any unrelated Register-A/B/C item. Bundle 1, Bundle 2, and Bundle 3 are
not reopened and their accepted meaning is not modified. **A1 remains
blocked.** Stale Defaults/cursorrules wording is merely noted: Master
V10 wins where they conflict.

## 16. PACKAGE ACCEPTANCE CHECKLIST

- [ ] A6 decisions carried exactly and realized in §5/§7 without
      reinterpretation, added approval gates, or surveillance expansion.
- [ ] A8 written purely as a mapping of settled §7P/§7N/§7O/§7Q
      authority (§9.1), strictest-rule-wins, specialist systems intact,
      emergency-stop unbroadened.
- [ ] A18 layered world model carried exactly with all nine
      distinctions structural (§6).
- [ ] World-model active-core membership complete and separate:
      membership is its own append-only lifecycle, distinct from
      currentness, truth/grounding, relevance, retrieval ranking,
      operational active/cold status, and counterfactual status; only
      evidence-linked A18 bases create membership — similarity,
      resemblance, co-retrieval, repetition, confidence, or relevance
      alone never do; multiple bases are separately referenced and
      ending one basis cannot deactivate an object while another valid
      basis remains; the §7.2 membership event carries all required
      fields with exactly two policy states; failed evaluations
      preserve prior membership; duplicate-safe, crash-safe,
      fail-closed (§6, §7.2, §7.4, §13, §14).
- [ ] B6 schemas complete with the common contract, six settled
      currentness statuses, no hidden decay score, full lifecycle and
      recovery (§7).
- [ ] Provenance preserved absolutely: every root, reading, telling,
      clash, response, result item, derivative reference, and
      operational record individually kept; same-event derivatives
      share one evidence family counting once for grounding; matching
      is episode-qualified — only a definite same-episode match
      appends, a later recurrence receives a new node, and uncertain
      matches never silently merge; currentness changes only through
      append-only events (§5, §7, §12–§14).
- [ ] B5 complete: snapshots immutable forever with no mutable status
      field; standing, superseded, and possibly-stale derived only from
      later append-only refresh/status events, never from in-place
      marks; all ten source-reference families present, including
      direct roots (factor 2 points to them) and safe metadata-only
      pre-ingest references; null updates and failed/incomplete
      refreshes create events only, never duplicate or falsely fresh
      snapshots; crash cases (a)–(f) distinguished; held pre-ingest raw
      content and any sealed TSC inspection route remain impossible;
      downstream-only (§8).
- [ ] Ordering-profile structure complete: immutable, versioned §8.1
      profile records with purpose type, consuming component,
      authorization/privacy basis, eligible source families, the
      settled seven factors in fixed order, disclosed
      ordering/tie/omission/surfacing rules, a no-hidden-score
      declaration, Tier-1/Tier-2 configuration references, declared
      triggers and invalidating events; every snapshot and refresh
      attempt binds to the exact profile ID and version; changes only
      through new versions with earlier versions preserved; no
      empirical value invented; missing/invalid/stale/unauthorized
      configuration fails closed without a snapshot; idempotent
      re-runs (§8, §13, §14).
- [ ] B8 records complete with all separations and protections; no
      double execution; B-CYCLE-5 honestly open (§9.2).
- [ ] B27 wording complete with all behavior rules (§10).
- [ ] Current stage separated from prospective level everywhere: every
      possibility/action-family record carries current_action_state,
      current_authority_level, prospective_action_level,
      prospective_heightened_categories, and advancement_requirements;
      surfacing is Level 1 now with no execution authority; preparation
      is Level 3 and never worded or logged as executed; Level 4 exists
      only after an outside effect begins or occurs; authorization
      binds to the exact prepared object and never silently expands;
      heightened-category wording is category-accurate, never implying
      universal irreversibility (§9, §10, §13, §14).
- [ ] Approval, execution attempt, actual outside effect, confirmed
      result, and failed/partial/unknown outcome are distinguished in
      every record and every displayed wording; approval is never
      described, logged, or implied as proof that execution began, an
      outside effect occurred, or the action succeeded (§9, §10, §13,
      §14).
- [ ] Suggestion level accounting correct and §0B logging separate: a
      surfaced possibility stays `suggesting` and remains a §7N
      possibility record, never an action record; creating and
      committing a new possibility record is a Level-2 append-only
      internal write; retrieving or displaying an already committed
      possibility without creating a new domain object is Level 1;
      the prospective future action level stays separate; the
      mandatory operational-log append is its own separate linked
      Level-2 write that is never merged, double-counted, or treated
      as evidence; B27's Level-1 wording no longer claims that nothing
      at all changed during a logged read (§9, §10, §13, §14).
- [ ] B-INT-9 wiring exact; forbidden list intact (§11).
- [ ] §7Q/§7R/§7P gates-not-evidence, no circular support, A31
      throughout (§12).
- [ ] §13 design contract and §14 §0B recordkeeping on every operation.
- [ ] Active/cold operational-record lifecycle complete for B5, B6,
      B8, B27, and B-INT-9: every newly committed record begins
      `active` without exception; append-only §14.3 status events;
      component-owned fixed, declared, versioned cooling rules with no
      hidden score and no time values invented; cooling only when both
      settled conditions hold — old under the declared rule **and** no
      genuine use or valid new links — and it changes only
      presentation and retrieval priority; reactivation only through
      actual authorized use or a valid new link under the governing
      connection rules, with no added approval gate invented;
      retrieval, similarity, resemblance, co-retrieval, ranking
      proximity, time,
      confidence, or repetition never reactivate alone; failure
      preserves the previous status and fails closed; only `active`
      and `cold` exist; lifecycle events never double-count with
      domain events (§13, §14).
- [ ] Opens preserved (§15); nothing reopened; nothing implemented.
- [ ] ChatGPT's independent audit of this actual file — **pending**.
- [ ] Ness's explicit acceptance — **pending**.

---

*End of
`NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md`
— CANDIDATE, unaudited, standalone only. ChatGPT must inspect this actual
file; nothing is accepted, adopted, integrated, or implemented. All
authority, accepted, and historical files remain unchanged.*

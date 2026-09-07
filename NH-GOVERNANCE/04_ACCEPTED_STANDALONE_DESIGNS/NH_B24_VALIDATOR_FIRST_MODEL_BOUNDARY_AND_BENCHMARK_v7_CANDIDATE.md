# NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md

**Status:** DESIGN CANDIDATE — NOT ADOPTED — NOT IMPLEMENTED

**Task ID:** B24 / A31 — Validator-First Model Boundary and Candidate Benchmark Architecture

**Date:** July 2, 2026.

**Corrects:** `NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v6_CANDIDATE.md`
(verified on disk before this correction as byte-identical to the audit
reference: SHA-256
`f397413c95a23c4a2deac657a35bdd1dee99f7d9117ff7cc8e6312c69858bc8b`, 1,763
newlines, 119,739 bytes). v7 corrects exactly the four verified consequential
mechanical defects from ChatGPT's independent audit of v6, under the frozen
targeted-closure scope: (1) immutable contribution capture with append-only
routing results; (2) the governed `analysis_supplement` operation; (3)
external adjudication for the compatibility and insufficiency assessment
families; (4) separation of authorization and operational failures from
substantive proposal rejection. Every other valid part of v6 is preserved.

**Role:** The consolidated, **self-contained** B24 standalone design candidate.
Built from v3 as the physical-content base (verified SHA-256
`54aab7e70d3fafb90ff6f55029ff0eea70fe1f7f2d67e0b2de96e9789340ce5f`, 1,234
newlines, 77,862 bytes), integrating every valid mechanical correction from v4
(verified `c6c33980ad389c164275d2ec82864bd3461b493d210e1a9152b7ea50e4bd09d3`,
1,155 newlines, 73,676 bytes) and v5 (verified
`25ac1012e61b42571256c0deaa49eb55eb009e54f5db9d1cd87f9ec1627a8714`, 956
newlines, 65,791 bytes), plus the final consolidation requirements. This file
is auditable **without opening any earlier B24 candidate**; prior versions are
cited only for provenance and no-loss reporting. v1–v6 are preserved
unchanged. Not architectural authority; alters no authoritative file; no
implementation authorization; requires ChatGPT's independent audit and Ness's
explicit acceptance before adoption. This is an interim standalone design
package, not the final implemented N.H.

---

## §A — Authority and complete source inventory

**Governing authority order:**
1. `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` (adopted by Ness June 29
   2026; governing; stale internal wording claiming otherwise is superseded)
2. `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`
3. `01_AUTHORITATIVE/cursorrules`
4. `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`

**Sources read for this candidate:** the four governing files (Master §7G
seven acceptance checks + rejection categories, §7Q, §7R, §0B incl.
living-memory links / active-cold state / governed reactivation, §16, §25
SACL/PBR/LMAC; Defaults §3D, §3F, §7R Decision 6; cursorrules §6A; Companion
§7G text and TSC/§25 boundaries); the current map
`NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` (B24, B9, C-7G, C-7GA,
C-13, C-16, the settled CY-B OUTPUT-TO-NESS BOUNDARY sequence, the B-INT-6
in-progress access-reduction requirement, and the B-INT-11 requirement that
each component carry its own recordkeeping wiring); the actual
`NH_DECISION_PACKAGE_LIVE_DUAL_MODEL_HANDOFF_v1.md` (§§1–9, read in full);
B24 candidates v3, v4, v5 (each hash-verified above before use); the accepted
A2 package and closure record and the eight-bundle plan candidate (consulted
as accepted/operational records; unchanged; A2 not reopened).

**The Ness-approved dual-model concept (handoff, preserved without change):**
the heavy model is a background deep analyst — not N.H, not authoritative
over Ness, replacing none of N.H's rules/memory/provenance/relevance/privacy/
truth controls; the light model is the single visible live
messenger/translator/carrier and never invents the final deep answer while
the heavy model works; N.H's governing rules sit above both; relevant new
information may attach to the **same** live operation; wording, warmth,
structure, language, and presentation may change — meaning never; warm
continuation is bounded; to Ness the system is one continuous N.H, never two
characters; no model is adopted and no coding/stores/runtime is authorized by
the handoff.

**Settled rules carried unchanged throughout this file:** the dual-lane A31
rule (§B); facts directly established only; possibilities separate,
evidence-linked, explicitly unconfirmed, rejectable; evidence-status channels
and retrieval channels independent; circular support prohibited; claim scope
preserved through natural multilingual expression; immutable producer brief;
separate append-only validation-result record; all seven Master §7G
acceptance checks and settled rejection categories; three-stage validation;
fail-closed `indeterminate_unvalidated`; language-neutral
`unconfirmed_possibility`; warm pending role; heavy-unavailable fail-closed;
settled §7Q-first / SACL-second output order with no-signal withholding;
lookup-first recovery; no double delivery; B9 owns retry values and fallback
timing; model confidence is metadata, never authority; validated means only
"no rule-detectable error found," never substantive truth; §7Q/§7R/§7P gate
rather than feed; DUMB stores/moves and never interprets; SMART interprets
and never turns interpretation into fact; derived material is never
independent evidence for the interpretation that produced it; §0B append-only
with no double evidence and no silent operation; A2 closed; every unresolved
policy remains unresolved.

---

## §0 — Consolidation method and correction matrix

**Targeted corrections applied in v7 (frozen four-defect scope; ChatGPT's independent audit of v6):**

| # | v6 defect | v7 resolution | Sections |
|---|---|---|---|
| 1 | §2.11/§6.0 called the capture record append-only while `routing_status` / `routed_parent_ref` were later mutated by routing | **Immutable capture + append-only routing results**: the Phase-A record holds only immutable capture/provenance facts; routing ownership and state live in the separate append-only §2.11A routing-result record owned by `new_input_decision`; any displayed current status is a derived view over capture plus routing events; exactly-one-owner preserved | §2.11, §2.11A, §6.0, §6.2-T1/T2, §6.4-D, §7.5, §8.2 |
| 2 | §6.4-D said added material is "explicitly supplied" to a running attempt, with no operation proving the supplement was received | **Governed `analysis_supplement` child (thirteenth child type)**: plan commit → idempotent send/apply → committed acknowledgement or honest unresolved outcome; supplementation never claimed without committed proof; the same supplement never sent twice after replay; the analyst-attempt record never mutated; only acknowledged supplementation continues under the new revision; otherwise cancel/restart or unresolved-outcome; late results never authorize a brief | §6.1, §6.4-D, §6.4-E, §6.2-T11, §6.3, §7.5, §7B, §8.2 |
| 3 | §2.10/§2.12 carried semantic-provider results with an incomplete external-adjudication boundary | **Five-stage separation for both assessment families** (provider proposal → authorized-configuration check → actual-provider independence check → external governed adjudication → final committed result) with full provenance references; only an externally adjudicated committed `compatible` opens `D-REVISION-CURRENT-OR-COMPATIBLE`; only an externally adjudicated committed confirmation authorizes `insufficient_context`; boundary failures fail closed and never become `compatible`, `genuine_insufficiency_confirmed`, or substantive rejection | §2.10, §2.12, §3.6, §4.1, §6.2-T3/T6, §6.4-D, §7.5, §8.2, §8.3, §7B |
| 4 | §3.1 sent every Stage-1 failure to `rejected`, including privacy/relevance authorization, operation-identity, and supersession conditions that are not proposal defects | **Outcome taxonomy separated**: structural/substantive defects → `rejected` with categories/reasons; privacy/relevance → distinct non-substantive fail-closed `authorization_failed` [proposed] with its own reason space; `OPERATION_IDENTITY_INVALID` → `technical_failure`; `SUPERSEDED_OPERATION` → `superseded`; non-proposal failures never populate `rejection_categories` or `rejection_reasons` | §2.9, §3.1, §3.3, §3.4, §3.7, §5.4, §6.1, §7.3, §7.5, §8.2, §7B/§7C |

Counts after v7: **thirteen** child types; **T1–T11** transaction boundaries; **fourteen** idempotency points; eight parent terminals unchanged. The v6 consolidation record below is preserved as provenance; its counts describe v6 as consolidated.

**Method.** v3 supplies the physical normative base (schemas, criteria,
contracts, paths, benchmark). v4's corrections are integrated (settled output
order; real new-input mechanics; seven-check mapping and two-level rejection
vocabulary; lookup-first recovery and the safe delivery contract;
`PM-CLAIM-SCOPE`; executable independence; `payload_creation` and
`insufficiency_assessment` owners; completed §0B set; honest scoping). v5's
corrections are integrated (multi-contribution parent honoring the handoff;
per-contribution revision advancement with compatibility; re-sequenced
independence; crash-safe decision ownership; cancellation vs abandonment;
unresolved-delivery parent closure; physical active/cold wiring; owned gate
evaluation with freshness; `classification_unresolved`). No defect corrected
by v4 or v5 is restored.

**Final-consolidation corrections applied in v6:**

| # | Prior defect | v6 resolution | Sections |
|---|---|---|---|
| 1 | v5 replaced normative architecture with "preserved from v4/v5" references | **All normative content physically present**: full §B, §1.1–§1.9, §2.1–§2.12, all criteria, seven-check mapping, full vocabulary, §4.1–§4.4 + §4A, §5.1–§5B, complete operation/transaction/idempotency/recovery/gate architecture, §7.1–§7.6, §7B.1–§7B.3, an actual §7C, §§8–12, change report, self-audit | whole file |
| 2 | Contributions were attached to the current parent (revision advanced) **before** deciding ownership | **Parent-neutral capture**: Phase A gives every contribution one stable captured identity with no parent ownership; Phase B is a crash-safe routing plan assigning it exactly once (existing parent / new parent / linked successor superseding the old / `classification_unresolved`); no duplicate attachment, silent transfer, or loss | §2.11, §6.0, §6.2-T1/T2, §6.3, §6.4-D |
| 3 | `revision_compatibility` authorized older-brief use without a governed operation | **`revision_compatibility_assessment` child operation** with identity, provenance, one terminal, transaction boundary, lookup-first recovery, stale rejection, §0B records; only a **committed `compatible`** result lets `D-REVISION-CURRENT-OR-COMPATIBLE` pass; indeterminate/missing/stale/unvalidated fails closed; the meaning judgment is SMART-bounded, the commit machinery DUMB | §2.12, §6.1, §6.2-T3, §6.3, §6.4-D, §8.3 |
| 4 | No parent terminal for gate-withheld output; gate child vocabulary incomplete; the B-INT-6 in-progress access-reduction path absent | **`terminal_withheld_by_gate`** parent terminal (nothing surfaced, no signal of hidden content, reasons only in authorized records); complete gate-child vocabulary (`passed`/`withheld`/`superseded`/`cancelled_for_restart`/`abandoned`/`technical_failure`/`unresolved_outcome`); **access-reduction path**: passes bound to §7Q/SACL/PBR versions, relevant reductions invalidate passes, in-progress candidates discarded, delivery never starts from a stale pass, uncertain started delivery → unknown-delivery path | §6.1, §6.5, §6.2-T9, §7.5 |
| 5 | Validation-boundary failures (self-review config, producer-supplied assessment, missing independence evidence, unauthorized model-only review, missing external adjudication) could read as proposal rejection | **Boundary/defect separation**: these commit `indeterminate_unvalidated` carrying `validation_boundary_reasons` — never `rejected`; `rejected` is reserved for substantive proposal defects; the same separation governs `insufficiency_assessment` (an invalid validator configuration never becomes evidence of insufficiency or of proposal error) | §2.9, §2.10, §3.3, §3.3B, §3.4, §3.7 |
| 6 | B-INT-11 was claimed discharged while cooling-rule content stayed open | **Honest status**: `cooling_rule_record` schema added (no conditions invented); until a fixed declared rule is separately supplied and accepted, **all B24 operation records remain active**, no automatic active→cold transition, similarity never triggers, no silent default; B24's record/link/event mechanics are specified — **full B-INT-11 closure remains dependent** on cooling-rule instantiation and later cross-component consolidation | §7.6, §9, §10 |
| 7 | A clarification after `classification_unresolved` had no defined operation relationship while the parent had to terminate | **Coherent path**: routing/decision child terminates `classification_unresolved`; no stale deep answer surfaces; a delivered bounded clarification/limitation → parent `delivered_governed_fallback`, and Ness's later answer opens a **new** parent carrying `continuation_of_parent_id` and the clarification linkage (never claimed to be the original operation); gate-withheld clarification → `terminal_withheld_by_gate`; no visible attempt → `terminal_classification_unresolved`; never pending; the captured contribution keeps exactly one owner | §6.4-D, §5A, §6.1 |
| 8 | `terminal_failure` ambiguously meant both "no valid delivery" and "limitation surfaced" | **Mutually exclusive, complete parent terminals (eight)**: a visibly delivered limitation is `delivered_governed_fallback`; `terminal_failure` is a strictly non-delivery internal technical/content failure; each parent and child ends in exactly one terminal; later resolution events are append-only and never rewrite | §6.1, §6.4-C4, §7.3 |
| 9 | The benchmark relied on references to prior files | **Complete benchmark physically present**: §7B.1 governing rules, §7B.2 full suites, §7B.3 separate measurement, and an actual §7C pass/fail section — plus every retained v4/v5/v6 test | §7B, §7C |
| 10 | Counts, diagrams, audits, and status claims lagged | **Everything reconciled**: twelve child types; eight parent terminals; T1–T10 boundaries; thirteen idempotency points; routing/compatibility/validation/gate state machines; recovery matrix; §0B set; active/cold status; benchmark; DUMB/SMART; dependencies; unresolved items; design-complete; three-way no-loss; conflict audit; change report; self-audit | §0, §6–§12 |

---

## §B — Ness-approved dual-lane rule (substantive A31 — SETTLED; not reopened)

**Settled by Ness. Locked. Not reopened by this candidate.**

### Facts lane
A factual claim may pass **only** when directly established by supplied
authorized evidence. The supporting evidence and its precise
locator/provenance must be explicit. A model's confidence or self-check is
never proof. An unsupported or mismatched factual claim must be rejected. No
weaker inference, strength, leaning, or interpretive confidence may be
represented as factual status.

### Possibilities lane
N.H may surface an evidence-linked interpretation or possibility that is not
established as fact. It must remain in a visibly separate lane, be explicitly
marked unconfirmed, state the precise evidence it is leaning from, and remain
rejectable; it never silently becomes a fact. A possibility with no permitted
evidential basis — or with a cited basis that does not genuinely support it —
is rejected rather than invented.

### Merger prohibition
The two lanes may never be merged, softened into one another, or presented
with equal certainty.

### What remains open (distinct from the settled substantive rule)
Quantitative/operational values only: any numeric confidence representation
(none required by the rule); operational scoring/ranking values; bounded
retry values (B9); exact benchmark trial counts, latency budgets, and
tolerance counts; final models, semantic-review provider, runtime/framework,
remote-heavy permission, hardware.

---

## §1 — Source/evidence-status architecture

### §1.1 Two evidence-status channels — permanent separation

The heavy analyst's input envelope carries **two separately labeled
channels**, realizing Master V10's permanent separation of root evidence from
prior-reading context.

**Channel A — direct source/root evidence** [proposed label `direct_source`]:
- each **captured user contribution** (the exact user turn text);
- **authorized original roots**;
- **authorized positional source material** (preceding source turns from the
  same thread — original material, not interpretations of it);
- **directly verifiable machine-state or provenance facts** (timestamps,
  hashes, `produced_by` values, store/lifecycle state, seal state);
- **Ness-response events**, preserving exactly what each event establishes:
  that Ness responded in a specific recorded way, at a specific time, about a
  specific target — nothing beyond that.

**Channel B — prior interpretation context** [proposed label
`prior_interpretation`]:
- prior readings; story-layer tellings; earlier interpretations; prior
  possibility records.

### §1.2 What each channel may do

Only Channel A material may directly establish a facts-lane claim. Channel B
is **interpretive context only** — it may assist continuity, comparison,
discovery, clash detection, and **possibility formation**; it may never
directly establish a facts-lane claim. A reading may not become factual
merely because later readings repeat it; repetition adds no evidential
weight. **Circular support is prohibited**: an interpretation may not be
supported by a chain of interpretations ultimately deriving from itself;
derived material is never independent evidence for the interpretation that
produced it. No authority exists — and none is invented here — for converting
a self-report, third-party statement, prior reading, or telling into
objective fact.

### §1.3 Epistemic scope of a user contribution

A user contribution **directly establishes that Ness said, reported,
described, asked, or expressed something**. It does not automatically prove
every external-world proposition inside the statement.

Worked example:
- **Directly established:** "Ness reported that his shoulders move forward."
- **Not automatically established as independent external fact:** "Ness's
  shoulders objectively moved forward at a verified time."

**Messenger naturalness:** the visible messenger is not forced into unnatural
constant "you reported" phrasing. It may reflect Ness's first-person words
naturally. The **governed record** — the facts-lane claim with its
`claim_scope` — preserves the claim's source and epistemic scope; naturalness
never widens the recorded scope.

### §1.4 Claim-scope structure (proposed, machine-readable)

| `claim_scope` value [proposed] | Meaning | Channel A evidence that can establish it |
|---|---|---|
| `source_stated` | A speaker said/reported/asked/expressed the content; the **saying** is the established fact | User contributions; roots carrying the statement; Ness-response events (the response itself) |
| `directly_observed` | An **authorized observation source** directly observed the content | Only where such an authorized source exists and is cited |
| `machine_provenance_fact` | A directly verifiable machine-state or provenance fact | Machine/provenance records |
| `interpretation` | Interpretive content — **never valid in the facts lane** | — (deterministically rejected from the facts lane) |

A claim asserting more than its scope and evidence establish is rejected
(`CLAIM_SCOPE_EXCEEDED`). The validator never widens or re-scopes a claim; it
rejects.

### §1.5 Authorized input classes (channel-assigned)

| Class | Channel | Provenance requirement |
|---|---|---|
| Captured user contribution | A — `direct_source` | `contribution_id`, `session_id`, `turn_id`, `speaker`, `sequence_position`, `content_hash` (§2.11) |
| Authorized original roots | A — `direct_source` | Root ID, batch ID, retrieval channel, §7R mode ID + version |
| Authorized positional source material | A — `direct_source` | Source title, position offset, root IDs |
| Machine-state / provenance facts | A — `direct_source` | Record ID, record type, verifiable value reference |
| Ness-response events | A — `direct_source` (scope-limited per §1.1) | Event ID, target IDs, response type, timestamp |
| Prior readings | B — `prior_interpretation` | Reading ID, `produced_by`, `schema_version`, `derived_from` |
| Story-layer tellings | B — `prior_interpretation` | Telling ID, parent reading ID, firmness indicator |
| Prior possibility records | B — `prior_interpretation` | Record ID, producing brief/operation reference |

### §1.6 Prohibited input classes

Never entering the heavy analyst's context: **model-generated material as
evidence** (earlier briefs, chain-of-thought, or readings not independently
authorized — a system-produced reading re-enters only as a retrieved
authorized reading, never as raw model output standing in as evidence);
**unvalidated prior briefs** as context material; **model confidence scores**
as evidence; **material not authorized under §7Q** (pre-retrieval eligibility
+ exclusion layer); **material not authorized under §7R** (relevance gate);
**chain-of-thought** (never passed onward, never treated as evidence, never
shown to any provider).

### §1.7 General background knowledge

The model's general training knowledge is recognized as present but is never
represented as evidence in either channel and is never citable in the facts
lane.

### §1.8 Input-boundary record (§0B)

A child-scoped subordinate state record of the parent operation (§7):
`event_id`, `parent_op_ref`, `child_op_ref` (the analyst attempt),
`input_item_count_by_channel_and_class`, `items_excluded_count`,
`exclusion_reasons_by_class`, `privacy_gate_passed`, `relevance_gate_passed`,
`context_revision_ref` (with its ordered attached-contribution snapshot),
`timestamp`. No raw evidence content; full locators live only in the
§7Q/§25-gated governed validation record.

### §1.9 Two independent axes

Every evidence item carries **two independent classifications**:

| Axis | Values | What it answers |
|---|---|---|
| **Evidence-status channel** [`evidence_channel`, proposed] | `direct_source` / `prior_interpretation` | May this item directly establish a fact? |
| **Retrieval channel** [`retrieval_channel`, proposed] | `positional` / `semantic` / `current_turn` / `direct_authorization` | How was it retrieved; what conversational role may it play? |

The axes are orthogonal: a root retrieved **semantically** is still Channel A
but must not be treated as conversational (positional) context; a reading
retrieved **positionally** is still Channel B and still cannot establish a
fact. **A valid assignment on one axis never hides confusion on the other**:
`D-CHANNEL-ASSIGN`/`D-FACTS-CHANNEL-A` enforce the evidence-status axis and
`D-RETRIEVAL-CHANNEL-ASSIGN`/`S-CHANNEL-CONFUSION` enforce the retrieval axis,
independently (§3).

---

## §2 — Schemas

**All new field names are `[proposed]`, not yet adopted as controlled
identifiers.** Existing controlled identifiers (`schema_version`,
`produced_by`, `reading_idempotency_key`, `insufficient_context`) are
preserved exactly.

### §2.1 Brief-level envelope — IMMUTABLE PROPOSAL (proposed)

The producer brief is an **immutable proposal**. The producer never mutates
it; the validator never rewrites any field of it; the validation outcome
lives in the separate result record (§2.9). No `validator_status` field
exists on the brief.

| Field | Type | Notes |
|---|---|---|
| `brief_id` [proposed] | stable unique ID | Permanent reference |
| `parent_op_ref` [proposed] | parent operation ID | Binds the brief to the parent live operation (§6.1) |
| `producing_child_op_ref` [proposed] | child operation ID | The analyst-attempt child that produced it |
| `brief_idempotency_key` [proposed] | idempotency key | Child-level compound identity (§6.3) |
| `schema_version` | string | Existing controlled identifier |
| `declared_reading_mode` [proposed] | string | The declared mode/purpose this attempt ran under; enforced by settled check 7 |
| `producer_model_id` [proposed] | string | Heavy analyst identity — provenance, never authority |
| `producer_model_version` [proposed] | string | Version/digest |
| `produced_at` [proposed] | timestamp | |
| `input_boundary_event_ref` [proposed] | event ID | Pointer to the §1.8 record |
| `context_revision_ref` [proposed] | revision ID | The committed context revision the brief was built on |

### §2.2 Source references — channel-labeled, locator-tightened (proposed)

Every evidence item is registered with both axis labels and a **default
locator** that does not copy source text. A whole-object-only reference is
never sufficient for lane citations.

| Field | Type | Notes |
|---|---|---|
| `ref_id` [proposed] | stable ID | Local key within this brief |
| `source_type` [proposed] | enum | `user_contribution` / `root` / `positional_source` / `machine_provenance_fact` / `ness_response` / `reading` / `telling` / `prior_possibility` |
| `evidence_channel` [proposed] | enum | `direct_source` / `prior_interpretation` — deterministically derived from `source_type` per §1.5; mismatch rejected |
| `retrieval_channel` [proposed] | enum | `positional` / `semantic` / `current_turn` / `direct_authorization` |
| `source_id` [proposed] | system ID | Stable ID of the source object |
| `span_locator` [proposed] | object | **Default locator:** stable span/location reference within the source (positions, offsets, or structural path) |
| `speaker_attribution` [proposed] | string | Whose words/action (exact speaker) |
| `integrity_ref` [proposed] | hash/ref | Content hash or equivalent stable integrity reference where applicable |
| `source_status` [proposed] | enum | `stated_content` / `observed_content` / `machine_fact` / `interpretive_content` — consistent with §1.4 |
| `bounded_quote` [proposed] | optional string | **Only when authorized and necessary** for validation or safe expression; absent by default |
| `source_provenance_label` [proposed] | string | From the retrieval channel |

**User-contribution entries** carry at minimum `contribution_id`,
`session_id`, `turn_id`, `speaker`, `sequence_position`, `content_hash`
(§2.11). **Locator privacy boundary:** full locators (and any
`bounded_quote`) live in the governed validation record (§2.9
`evidence_locator_record_ref`), §7Q/§25-gated. Root text is never copied into
reading records, general §0B logs, terminal operation records, or unrelated
payload fields.

### §2.3 Facts lane — directly established, Channel A only, scope-carrying (proposed)

| Field | Type | Notes |
|---|---|---|
| `claim_id` [proposed] | stable ID | |
| `claim_text` [proposed] | string | Expressed precisely, within its declared scope |
| `claim_scope` [proposed] | enum | `source_stated` / `directly_observed` / `machine_provenance_fact` (§1.4); `interpretation` is deterministically invalid here |
| `supporting_evidence` [proposed] | list | Non-empty. Every item resolves to a `ref_id` whose `evidence_channel = direct_source` **and** carries the span-level locator. Channel B refs are deterministically rejected here. |

There is **no** strength/leaning tier (`strongly_supported`/`supported` do
not exist): a facts-lane claim is directly established within its scope, or
it is not a fact.

### §2.4 Possibilities lane — evidence-linked, language-neutral status (proposed)

| Field | Type | Notes |
|---|---|---|
| `possibility_id` [proposed] | stable ID | |
| `possibility_text` [proposed] | string | Expressed as non-established |
| `leaning_evidence` [proposed] | list | Non-empty. Items may cite Channel A and/or Channel B refs with span-level locators — prior interpretations may inform possibility formation (§1.2) — subject to basis-soundness and no-circular-support (§3.2) |
| `possibility_status` [proposed] | machine enum | **Required value `unconfirmed_possibility`** — the language-neutral machine status; no fixed visible English string exists anywhere |

### §2.5 Genuine unknowns (proposed list)

| Field | Type | Notes |
|---|---|---|
| `unknown_id` [proposed] | stable ID | |
| `unknown_description` [proposed] | string | What cannot be established from available evidence |
| `missing_evidence_type` [proposed] | string | What evidence would be needed |

### §2.6 Clarification needs (proposed list)

| Field | Type | Notes |
|---|---|---|
| `clarification_id` [proposed] | stable ID | |
| `clarification_text` [proposed] | string | Specific bounded question for Ness |
| `reason` [proposed] | string | Why it is needed |

### §2.7 Proposed reply direction (proposed)

| Field | Type | Notes |
|---|---|---|
| `reply_direction_text` [proposed] | string | Direction for the messenger; not the reply itself |
| `direction_constraints` [proposed] | list | Explicit constraints the messenger must follow |

### §2.8 Insufficient-context connection

`insufficient_context` is produced **only** on an externally adjudicated, committed
`genuine_insufficiency_confirmed` result of the §2.10 assessment — never
because proposals were rejected, never as a relabel of a rejected malformed,
fabricated, or mode-violating proposal. Proposal rejection, genuine
insufficiency, technical failure, and stale/superseded operation are **four
permanently distinct outcomes** (§5.4). The honest `insufficient_context`
reading remains a written, revisable, honest fallback (existing vocabulary,
Master §7G) and its surface still passes the §6.5 output gates.

### §2.9 Validation-result record — separate, append-only (proposed)

The validator writes a **separate append-only validation-result record** and
never mutates the brief.

| Field | Type | Notes |
|---|---|---|
| `validation_result_id` [proposed] | stable ID | |
| `brief_id_ref` [proposed] | brief ID | The immutable brief assessed |
| `validation_child_op_ref` [proposed] | child op ID | The validation-attempt child |
| `parent_op_ref` [proposed] | parent op ID | |
| `validator_id` / `validator_version` [proposed] | strings | Stage-3 adjudicator identity/version |
| `criterion_set_id` / `criterion_set_version` [proposed] | strings | |
| `stage1_results_ref` [proposed] | ref | Deterministic-gate results |
| `config_check_ref` [proposed] | ref | §3.2A pre-assessment configuration result |
| `semantic_assessment_refs` [proposed] | list of refs | Stage-2 provider records |
| `independence_check_ref` [proposed] | ref | §3.3B post-assessment result |
| `outcome` [proposed] | enum | `accepted` / `rejected` / `indeterminate_unvalidated` / `authorization_failed` / `cancelled_for_restart` / `superseded` / `abandoned` / `technical_failure` |
| `rejection_categories` [proposed] | list | Settled Master categories (§3.4) — populated only on `rejected` |
| `rejection_reasons` [proposed] | list | Fine-grained substantive codes — populated only on `rejected` |
| `validation_boundary_reasons` [proposed] | list | **Populated only on boundary-caused `indeterminate_unvalidated`** (§3.4): `PRODUCER_SELF_APPROVAL_PROHIBITED` / `MODEL_ONLY_CROSS_VALIDATION_INSUFFICIENT` / `INDEPENDENCE_EVIDENCE_MISSING` / `EXTERNAL_VALIDATION_BOUNDARY_REQUIRED` — never mixed into rejection fields |
| `authorization_failure_reasons` [proposed] | list | **Populated only on `authorization_failed`**: `PRIVACY_AUTHORIZATION_MISSING` / `RELEVANCE_AUTHORIZATION_MISSING` — a separate non-substantive space, never mixed into rejection or boundary fields |
| `evidence_locator_record_ref` [proposed] | ref | §7Q/§25-gated locator record |
| `produced_at` [proposed] | timestamp | |

The sanitized payload (§4) references the immutable committed brief **and**
the committed accepted validation result **and** a qualifying context
revision (§4.1).

### §2.10 Insufficiency-assessment result record (proposed; append-only)

| Field | Type | Notes |
|---|---|---|
| `insufficiency_result_id` [proposed] | stable ID | |
| `assessment_child_op_ref` [proposed] | child op ID | The `insufficiency_assessment` child |
| `parent_op_ref` / `context_revision_ref` [proposed] | refs | Exact revision assessed |
| `examined_evidence_refs` [proposed] | list | The root(s)/permitted context actually examined (both axes labeled) |
| `prior_attempt_refs` [proposed] | list | Prior proposal-attempt children considered, when applicable |
| `provider_assessment_refs` [proposed] | list of refs | The semantic provider proposal records for this assessment |
| `config_check_ref` [proposed] | ref | The §3.2A-style authorized-configuration check result |
| `independence_check_ref` [proposed] | ref | The §3.3B-style actual-provider independence check result |
| `criterion` [proposed] | fixed | Whether the available **authorized** root/context genuinely cannot support a grounded reading **or** a grounded evidence-linked possibility |
| `outcome` [proposed] | enum | `genuine_insufficiency_confirmed` / `insufficiency_not_confirmed` / `indeterminate` / `cancelled_for_restart` / `superseded` / `abandoned` / `technical_failure` |
| `validation_boundary_reasons` [proposed] | list | Populated when the assessment's own validation boundary failed (§3.6): the outcome is then `indeterminate` — an invalid validator configuration **never** becomes evidence of insufficiency or of proposal error |
| `provider_id` / `provider_version` [proposed] | strings | Assessment provenance; the producer's self-check is never evidence and may never confirm insufficiency |
| `adjudicator_id` / `adjudicator_version` / `criterion_set_id` / `criterion_set_version` [proposed] | strings | External governed adjudication provenance |
| `produced_at` [proposed] | timestamp | |

**Rules:** the assessment family follows the same five-stage separation as
validation: (1) semantic provider proposal; (2) authorized-configuration
check; (3) actual-provider independence check; (4) external governed
adjudication; (5) final committed result. `indeterminate` fails closed.
Producer self-review, unauthorized model-only review, missing independence
evidence, or a missing external adjudication boundary fails closed as
`indeterminate` with the matching validation-boundary reason — it never
becomes `genuine_insufficiency_confirmed` and never becomes substantive
proposal rejection. Rejection count is never proof of insufficiency. The
assessment runs **only at the fallback point later authorized by B9**; until
B9 is settled, no retry count or fallback timing is invented and a rejected
proposal never automatically becomes `insufficient_context`. Only an
**externally adjudicated, committed** `genuine_insufficiency_confirmed`
authorizes the honest `insufficient_context` reading/surface — which then
still passes the §6.5 gates.

### §2.11 Captured-contribution record (proposed; parent-neutral — Phase A)

Every user contribution first receives **one stable append-only capture
record with no deep-answer parent ownership**:

| Field | Type | Notes |
|---|---|---|
| `contribution_id` [proposed] | stable ID | The contribution's permanent identity |
| `session_id` [proposed] | ID | Conversation reference |
| `turn_id` / `sequence_position` [proposed] | IDs | Turn and ordering identity |
| `speaker` [proposed] | string | Exact speaker |
| `content_hash` [proposed] | hash | Content integrity reference |
| `captured_at` [proposed] | timestamp | |
| `authorization_refs` [proposed] | list | Applicable §7Q/§7R authorization references |

The capture record is **immutable**: it contains only capture and provenance
facts and is never modified by routing or any later operation. Routing
ownership and state live exclusively in the separate append-only
routing-result record (§2.11A) owned by `new_input_decision`. Any displayed
current routing status is a **derived view** over the immutable capture plus
the append-only routing records — never a mutation of the capture. The
capture is **provenance, not a second evidence vote**. A contribution is
never attached to any parent before its routing result commits, is never
duplicated, never silently transferred, and never lost.

### §2.11A Routing-result record (proposed; append-only; owned by `new_input_decision`)

| Field | Type | Notes |
|---|---|---|
| `routing_result_id` [proposed] | stable ID | |
| `contribution_id` [proposed] | ID | The captured contribution routed |
| `decision_id` [proposed] | child op ID | The owning `new_input_decision` child |
| `routing_outcome` [proposed] | enum | `attach_existing` / `open_new_parent` / `supersede_with_successor` / `classification_unresolved` |
| `owning_parent_ref` [proposed] | parent ID or null | The owning deep-answer parent when assigned; null on `classification_unresolved` |
| `old_context_revision_ref` / `proposed_context_revision_ref` [proposed] | revision IDs | The relevant revision references |
| `terminal_state` [proposed] | enum | Exactly one terminal per routing result |
| `idempotency_key_ref` [proposed] | key ref | Binds `contribution_id` + parent-state snapshot (§6.3) |
| `recovery_refs` [proposed] | refs | Lookup-first recovery linkage (T2) |
| `committed_at` [proposed] | timestamp | |

Exactly-one-owner behavior is preserved: at most one committed routing result
assigns an owning parent for a given contribution; replay returns the
committed result; the capture record is never touched.

### §2.12 Revision-compatibility assessment record (proposed; append-only)

| Field | Type | Notes |
|---|---|---|
| `compatibility_result_id` [proposed] | stable ID | |
| `assessment_child_op_ref` [proposed] | child op ID | The `revision_compatibility_assessment` child |
| `parent_op_ref` [proposed] | parent ID | |
| `prior_revision_ref` / `new_revision_ref` [proposed] | revision IDs | |
| `attached_contribution_ref` [proposed] | contribution ID | The contribution whose attachment created the new revision |
| `assessed_attempt_refs` [proposed] | list | The exact prior brief(s)/attempt(s) whose continued validity is assessed |
| `authorized_evidence_refs` [proposed] | list | Evidence consulted |
| `provider_id` / `provider_version` [proposed] | strings | Assessor provenance (contract per §3.2; independence boundary per §3.6) |
| `provider_assessment_refs` [proposed] | list of refs | The semantic provider proposal records |
| `config_check_ref` [proposed] | ref | The §3.2A-style authorized-configuration check result |
| `independence_check_ref` [proposed] | ref | The §3.3B-style actual-provider independence check result |
| `adjudicator_id` / `adjudicator_version` [proposed] | strings | External governed adjudication provenance |
| `criterion_set_id` / `criterion_set_version` [proposed] | strings | |
| `outcome` [proposed] | enum | `compatible` / `incompatible` / `indeterminate` / `cancelled_for_restart` / `superseded` / `abandoned` / `technical_failure` / `unresolved_outcome` |
| `produced_at` [proposed] | timestamp | |

The assessment follows the same five-stage separation as validation:
(1) semantic provider proposal; (2) authorized-configuration check;
(3) actual-provider independence check; (4) external governed adjudication;
(5) final committed result. Only an **externally adjudicated, committed
`compatible`** result may allow `D-REVISION-CURRENT-OR-COMPATIBLE` (§4.1) to
pass for a brief produced under the prior revision. `indeterminate`, missing,
stale, or unvalidated compatibility **fails closed** and never authorizes use
of the older brief; producer self-review, unauthorized model-only review,
missing independence evidence, or a missing external adjudication boundary
fails closed with the matching validation-boundary reason and never becomes
`compatible`. The judgment of whether new information changes meaning is
**SMART-bounded** (or consumes an authorized policy result); the
configuration/independence checks, the external adjudication, and the
state-transition and commit machinery are DUMB governed machinery. No
"changed enough" threshold is chosen here.

---

## §3 — Three-stage validation mechanism

The validator is model-neutral: contracts, states, inputs, outputs, and the
fail-closed boundary are defined now; specific providers plug in later under
the open slots (§3.5). No framework is adopted. Sequence: **Stage 1 →
pre-assessment configuration check (§3.2A) → Stage 2 → post-assessment
independence check (§3.3B) → Stage 3 adjudication → payload verifies the
committed adjudication (§4.1).** No criterion depends on records that do not
yet exist at its point in the sequence.

### §3.1 STAGE 1 — Deterministic gate (DUMB; proposal-only checks)

Purely mechanical checks over the brief, its references, and
already-committed authorization/operation records. Each yields `PASS` or a
distinct reason; a failing check short-circuits Stage 2, and its committed
outcome depends on its class: **structural or substantive proposal defects
commit `rejected`** with the correct settled category and reason;
**privacy/relevance authorization failures commit the distinct
non-substantive fail-closed outcome `authorization_failed`** [proposed];
**`OPERATION_IDENTITY_INVALID` commits the operational fail-closed
`technical_failure`**; **`SUPERSEDED_OPERATION` commits `superseded`**.
Non-proposal failures never populate `rejection_categories` or
`rejection_reasons`.

| Criterion ID [proposed] | Check | Fine-grained reason | Settled category |
|---|---|---|---|
| `D-SCHEMA` | Brief conforms to declared `schema_version` | `SCHEMA_INVALID` | `malformed_output` |
| `D-REQUIRED-FIELDS` | Required fields present and non-null | `REQUIRED_FIELD_MISSING` | `incomplete_output` |
| `D-VALID-IDS` | Identifiers well-formed and internally consistent | `IDENTIFIER_INVALID` | `malformed_output` |
| `D-SOURCE-EXISTS` | Every `ref_id` resolves to a registered §2.2 source | `SOURCE_REFERENCE_ABSENT` | `malformed_output` |
| `D-SPAN-EXISTS` | Every `span_locator` resolves to an existing span in its source | `EVIDENCE_SPAN_ABSENT` | `malformed_output` |
| `D-INTEGRITY-REF` | Hashes well-formed and matching where checkable | `INTEGRITY_REFERENCE_INVALID` | `malformed_output` |
| `D-PRIVACY-REC` | Every source reference has a §7Q authorization record | `PRIVACY_AUTHORIZATION_MISSING` | — (authorization → `authorization_failed`; fail closed; non-substantive) |
| `D-RELEVANCE-REC` | Every source reference has a §7R relevance-gate record | `RELEVANCE_AUTHORIZATION_MISSING` | — (authorization → `authorization_failed`; fail closed; non-substantive) |
| `D-OP-IDENTITY` | Parent/child operation identity fields present and bound (§6.1) | `OPERATION_IDENTITY_INVALID` | — (operational → `technical_failure`; never rejection) |
| `D-STALE-STATUS` | Parent not superseded; revision qualifies (§4.1); child not stale | `SUPERSEDED_OPERATION` | — (operational → `superseded`; never rejection) |
| `D-CHANNEL-ASSIGN` | Every `evidence_channel` matches its `source_type` per §1.5 | `CHANNEL_ASSIGNMENT_INVALID` | — (structural) |
| `D-FACTS-CHANNEL-A` | Every facts-lane supporting ref resolves to `direct_source`; no Channel B ref supports a facts-lane claim | `FACTS_LANE_CHANNEL_VIOLATION` | — (independence of channels; terminal) |
| `D-RETRIEVAL-CHANNEL-ASSIGN` | Every item's `retrieval_channel` matches its actual retrieval provenance record | `RETRIEVAL_CHANNEL_MISLABELED` | `positional_semantic_confusion` |
| `D-MODE-DECLARED` | `declared_reading_mode` present and valid | `READING_MODE_UNDECLARED` | `reading_mode_violation` |
| `D-SCOPE-FIELD` | Every facts-lane claim carries a valid `claim_scope` ≠ `interpretation` | `FORBIDDEN_LANE_FIELD` | `malformed_output` |
| `D-LANE-FIELDS` | No forbidden field/lane combination (strength tier in facts lane; possibility missing `possibility_status = unconfirmed_possibility`) | `FORBIDDEN_LANE_FIELD` | `malformed_output` |
| `D-EVIDENCE-PRESENT` | Every facts-lane claim has non-empty `supporting_evidence`; every possibility non-empty `leaning_evidence` | `EVIDENCE_MISSING` | `incomplete_output` |
| `D-INCOMPLETE` | The proposal is structurally complete as a proposal (all mandatory brief parts present, even when lanes are legitimately empty) | `INCOMPLETE_OUTPUT_DETECTED` | `incomplete_output` |

Stage 1 decides no meaning: it compares identifiers, spans, hashes, labels,
channel assignments, and authorization records only.

### §3.2 STAGE 2 — Governed semantic assessment (provider-neutral contract)

**Provider return contract — every semantic-assessment record must carry:**
`criterion_id`; `proposed_verdict` (`pass` / `fail` / `indeterminate` — the
provider **must return `indeterminate` when it cannot safely decide**); exact
`evidence_refs` (the `ref_id` + span references examined); `reason_code` +
explanation; `provider_id` + `provider_version`; `assessed_at`.

**Provider authority limits (binding):** a provider's verdict is a
**proposed** verdict — Stage 3 adjudicates; a semantic-assessment provider is
not authoritative merely because it is a different model from the producer;
the producing model's self-check is **never** evidence; no provider sees or
relies on chain-of-thought.

**Semantic criteria:**

| Criterion ID [proposed] | Check | Fine-grained reason | Settled category |
|---|---|---|---|
| `S-FACT-ENTAILMENT` | The cited Channel A evidence directly establishes the claim **within its declared `claim_scope`** — grounding over the committed authorized evidence set (the live-turn realization of settled check 2's "target root or supplied context") | `UNSUPPORTED_FACTUAL_CLAIM` | `fabrication_invention` (where invented) / substantive |
| `S-CLAIM-SCOPE` | The claim text stays within what its scope and evidence establish (no self-report silently widened into objective external fact) | `CLAIM_SCOPE_EXCEEDED` | `unsupported_certainty` |
| `S-FABRICATION` | No content anywhere in the brief (claims, bases, unknowns, direction) is invented beyond the committed authorized evidence | `FABRICATED_CONTENT` | `fabrication_invention` |
| `S-POSSIBILITY-BASIS` | The cited evidence genuinely supports the possibility as a reasonable unconfirmed interpretation; irrelevant, decorative, or unrelated bases fail; model output may not cite itself or another unvalidated model output as a basis | `POSSIBILITY_BASIS_UNSOUND` | substantive |
| `S-CIRCULAR-SUPPORT` | No claim or possibility is supported only by an interpretation chain deriving from itself or by mere repetition across readings | `CIRCULAR_SUPPORT` | substantive |
| `S-SPEAKER-AGENCY` | Who-did-what is preserved exactly relative to the sources | `SPEAKER_AGENCY_CHANGE` | substantive (terminal) |
| `S-CERTAINTY` | Certainty is not inflated relative to the grounding evidence and scope | `CERTAINTY_INFLATION` | `unsupported_certainty` |
| `S-CAUSE-DIAGNOSIS` | No cause, diagnosis, motive, category, or condition is added beyond explicit supplied evidence | `CAUSE_DIAGNOSIS_UNSUPPORTED` | `fabrication_invention` |
| `S-LANE-INTEGRITY` | Fact-class content absent from the possibilities lane and possibility-class content absent from the facts lane, semantically | `LANE_CONTAMINATION` | substantive (terminal) |
| `S-CHANNEL-CONFUSION` | Semantically retrieved material is not treated as conversational/positional context, and vice versa, in the brief's reasoning products | `POSITIONAL_SEMANTIC_CONTENT_CONFUSION` | `positional_semantic_confusion` |
| `S-SELF-CONTRADICTION` | The proposal does not contradict its own cited evidence | `EVIDENCE_SELF_CONTRADICTION_FOUND` | `evidence_self_contradiction` |
| `S-MODE-FOLLOWED` | The brief's content actually follows the `declared_reading_mode` | `READING_MODE_NOT_FOLLOWED` | `reading_mode_violation` |

### §3.2A Pre-assessment provider-configuration check (before any assessment is requested)

Decidable entirely from committed criterion-set/configuration records — no
future records consulted.

| Criterion ID [proposed] | Check | On failure |
|---|---|---|
| `CFG-AUTHORIZED-CONFIG` | An authorized semantic-assessment configuration exists for this criterion set | `indeterminate_unvalidated` with boundary reason (fail closed; honest limitation) |
| `CFG-NO-SELF-REVIEW` | The configuration does not authorize the producing model configuration of this brief to assess any required criterion | `indeterminate_unvalidated` with `PRODUCER_SELF_APPROVAL_PROHIBITED` — a configuration can never silently authorize producer self-review; this is a validation-boundary failure, **not** a proposal defect |
| `CFG-COVERAGE-DECLARED` | The configuration declares which authorized provider(s) cover every required criterion | `indeterminate_unvalidated` with `INDEPENDENCE_EVIDENCE_MISSING` (fail closed) |

### §3.3 STAGE 3 — External governed adjudication state machine

The adjudicator is DUMB governed machinery: deterministic state transitions
over recorded inputs (Stage-1 results, source-status/channel information,
provenance, §3.2A configuration result, Stage-2 assessment records, §3.3B
independence result, criterion-set version, parent/child operation state,
§7Q/§7R authorization state). It decides acceptance state; it never invents
meaning; it fails closed on indeterminacy.

```
opened
  -> stage1_running
       -> stage1_substantive_failure ----------------> commit: rejected
       -> stage1_authorization_failure --------------> commit: authorization_failed
                                                        (fail closed; non-substantive)
       -> stage1_operation_identity_failure ---------> commit: technical_failure
       -> stage1_superseded_detected ----------------> commit: superseded
       -> stage1_passed
            -> provider_config_check           (§3.2A)
                 -> no_authorized_config ------> commit: indeterminate_unvalidated
                 -> config_authorizes_self_review
                        ------------------------> commit: indeterminate_unvalidated
                                                  (boundary: PRODUCER_SELF_APPROVAL_PROHIBITED)
                 -> config_ok
                      -> semantic_pending
                           -> assessments_received
                                -> independence_check    (§3.3B; over actual records)
                                     -> self_approval_found ----> commit: indeterminate_unvalidated
                                            (boundary: PRODUCER_SELF_APPROVAL_PROHIBITED)
                                     -> unauthorized_model_only -> commit: indeterminate_unvalidated
                                            (boundary: MODEL_ONLY_CROSS_VALIDATION_INSUFFICIENT)
                                     -> independence_evidence_missing_or_conflicting
                                            ----------------> commit: indeterminate_unvalidated
                                            (boundary: INDEPENDENCE_EVIDENCE_MISSING)
                                     -> independence_ok
                                          -> adjudicating
                                               -> commit: accepted
                                               -> commit: rejected        (substantive defects only)
                                               -> commit: indeterminate_unvalidated
(cross-cutting from any pre-terminal state)
  parent superseded / revision disqualified -> commit: superseded
  deliberate cancel/restart decision        -> commit: cancelled_for_restart
  crash (after §6.4 lookup-first)           -> commit: abandoned
  unrecoverable technical failure           -> commit: technical_failure
```

**Acceptance conditions (all required):** every Stage-1 criterion PASS; the
§3.2A configuration check passed; every required semantic criterion has a
governed Stage-2 record with an adjudicated `pass` from an authorized
configuration under the current `criterion_set_version`; the §3.3B
independence check passed; provenance and §7Q/§7R authorization state valid;
parent not superseded; the brief's revision qualifies (§4.1); child not
stale.

**Fail-closed rules:** Stage 3 may not accept while any required semantic
criterion is `indeterminate` or while any independence/boundary condition is
unmet. Provider disagreement on a required criterion is recorded, never
resolved by model confidence (Defaults §7R Decision 6); until the open
disagreement policy is settled, unresolved disagreement adjudicates
`indeterminate` → fail closed. **A runtime validator built from this design
cannot accept any brief while no authorized semantic-assessment configuration
exists — it fails closed to `indeterminate_unvalidated`.**

### §3.3A Settled Master V10 acceptance checks — explicit mapping

| # | Settled §7G check | v6 enforcement |
|---|---|---|
| 1 | Required fields present and valid | `D-SCHEMA`, `D-REQUIRED-FIELDS`, `D-VALID-IDS`, `D-INCOMPLETE` |
| 2 | Meaning grounded in the target root or supplied context | `S-FACT-ENTAILMENT` + `S-POSSIBILITY-BASIS` over the committed authorized evidence set, with `D-FACTS-CHANNEL-A` restricting factual grounding to Channel A |
| 3 | No claim invented beyond available evidence | `S-FABRICATION` (whole-brief), `S-FACT-ENTAILMENT` (facts lane), `S-CAUSE-DIAGNOSIS` |
| 4 | Positional and semantic context not confused | `D-RETRIEVAL-CHANNEL-ASSIGN` (labels) + `S-CHANNEL-CONFUSION` (content), independent of the evidence-status axis (§1.9) |
| 5 | Uncertainty expressed honestly | `S-CERTAINTY` + lane discipline (`S-LANE-INTEGRITY`, `D-LANE-FIELDS`) |
| 6 | Proposal does not contradict its own evidence | `S-SELF-CONTRADICTION` |
| 7 | Declared reading mode followed | `D-MODE-DECLARED` + `S-MODE-FOLLOWED` |

**Settled rejection categories — all distinct, none replaced by generic
failures:** `fabrication_invention`; `malformed_output`; `incomplete_output`;
`unsupported_certainty`; `positional_semantic_confusion`;
`reading_mode_violation`; `evidence_self_contradiction`. **Genuine context
insufficiency remains a separate fallback condition** (§2.8/§2.10), never a
rejection relabel.

### §3.3B Post-assessment independence check (over the actual committed assessment records)

| Criterion ID [proposed] | Check | On failure |
|---|---|---|
| `IA-PROVIDER-DISTINCT` | Every required criterion's actual `provider_id` + `provider_version` differ from the producing model configuration of this brief | `indeterminate_unvalidated` — boundary `PRODUCER_SELF_APPROVAL_PROHIBITED` |
| `IA-REQUIRED-COVERAGE` | Every required criterion has the required assessment(s) from the authorized configuration | `indeterminate_unvalidated` — boundary `INDEPENDENCE_EVIDENCE_MISSING` (fail closed) |
| `IA-CONFIG-AUTHORIZED` | The assessing providers match an **authorized** configuration; a merely-different model outside it is insufficient | `indeterminate_unvalidated` — boundary `MODEL_ONLY_CROSS_VALIDATION_INSUFFICIENT` (fail closed) |

Downstream, `payload_creation` verifies via `D-ADJUDICATION-COMMITTED` (§4.1)
that the external Stage-3 adjudication **actually committed**; a brief with
provider verdicts but no committed adjudication is unvalidated — boundary
`EXTERNAL_VALIDATION_BOUNDARY_REQUIRED`.

### §3.4 Two-level rejection vocabulary + boundary reasons (distinct spaces)

**Settled categories [`rejection_categories`]:** as listed in §3.3A —
populated only on `rejected`.
**Fine-grained substantive reasons [`rejection_reasons`]:** `SCHEMA_INVALID`,
`REQUIRED_FIELD_MISSING`, `IDENTIFIER_INVALID`, `SOURCE_REFERENCE_ABSENT`,
`EVIDENCE_SPAN_ABSENT`, `INTEGRITY_REFERENCE_INVALID`, `EVIDENCE_MISSING`,
`FORBIDDEN_LANE_FIELD`, `CHANNEL_ASSIGNMENT_INVALID`,
`FACTS_LANE_CHANNEL_VIOLATION`, `RETRIEVAL_CHANNEL_MISLABELED`,
`READING_MODE_UNDECLARED`, `INCOMPLETE_OUTPUT_DETECTED`,
`UNSUPPORTED_FACTUAL_CLAIM`, `CLAIM_SCOPE_EXCEEDED`, `FABRICATED_CONTENT`,
`POSSIBILITY_BASIS_UNSOUND`, `CIRCULAR_SUPPORT`, `SPEAKER_AGENCY_CHANGE`,
`CERTAINTY_INFLATION`, `CAUSE_DIAGNOSIS_UNSUPPORTED`, `LANE_CONTAMINATION`,
`POSITIONAL_SEMANTIC_CONTENT_CONFUSION`, `EVIDENCE_SELF_CONTRADICTION_FOUND`,
`READING_MODE_NOT_FOLLOWED`.
**Authorization-failure reasons [`authorization_failure_reasons`] — a
separate non-substantive space:** `PRIVACY_AUTHORIZATION_MISSING`,
`RELEVANCE_AUTHORIZATION_MISSING` — these accompany the fail-closed
`authorization_failed` outcome and are never recorded as proposal rejection.
**Operational outcomes (never rejection):** `OPERATION_IDENTITY_INVALID` →
`technical_failure`; `SUPERSEDED_OPERATION` → `superseded`.
**Validation-boundary reasons [`validation_boundary_reasons`] — a separate
space, never mixed into rejection fields:**
`PRODUCER_SELF_APPROVAL_PROHIBITED`,
`MODEL_ONLY_CROSS_VALIDATION_INSUFFICIENT`, `INDEPENDENCE_EVIDENCE_MISSING`,
`EXTERNAL_VALIDATION_BOUNDARY_REQUIRED` — these accompany
`indeterminate_unvalidated` (unvalidated; fail closed) and are **never
recorded as substantive proposal rejection**.
**Messenger post-check reasons (§5.2):** `MESSENGER_ADDED_FACT`,
`MESSENGER_REMOVED_UNCERTAINTY`, `MESSENGER_CONVERTED_POSSIBILITY`,
`MESSENGER_SPEAKER_CHANGE`, `MESSENGER_ADDED_ADVICE`,
`MESSENGER_OVERSTATED_AUTHORITY`, `MESSENGER_CONCEALED_UNCERTAINTY`,
`MESSENGER_STALE_PAYLOAD`, `MESSENGER_CLAIM_SCOPE_WIDENED`.
**Operational fail-closed states (not retry authorizations):**
`WITHHELD_BY_GATE`, `UNRESOLVED_OUTCOME`, `DELIVERY_OUTCOME_UNKNOWN`.
**Decision outcome (not a rejection):** `classification_unresolved`.

### §3.5 Explicit open slots (not silently chosen)

| Open slot | Owner |
|---|---|
| Final semantic-review provider (rules / model / models / human / mixed) | later Ness policy + implementation |
| Number of reviewers; quorum; voting rules | later policy |
| Whether human review participates | Ness |
| Framework | implementation (none adopted) |
| Final disagreement policy | Ness (until then: indeterminate → fail closed) |

### §3.6 Validator independence — three settled concerns, correctly ordered, boundary-classed

Producer self-approval (configuration level §3.2A; record level §3.3B);
model-only cross-validation insufficiency (§3.3B); the external governed
adjudication boundary (§3.3 + §4.1 `D-ADJUDICATION-COMMITTED`). All are
**validation-boundary conditions**: their failure means the proposal was
**not validly validated** — `indeterminate_unvalidated` with the matching
boundary reason — never that the proposal was substantively defective. **The
same boundary applies to `insufficiency_assessment`** (§2.10): a producer
self-check may never confirm genuine insufficiency, and an invalid validator
configuration never becomes evidence that insufficiency exists or that the
underlying proposal was wrong. The identical five-stage sequence — provider
proposal, configuration check, independence check, external adjudication,
committed result — governs the `revision_compatibility_assessment` (§2.12): a
boundary failure there fails closed and never becomes `compatible`.

### §3.7 Severity classes

| Class | Members | Effect |
|---|---|---|
| Terminal substantive (per attempt) | `SPEAKER_AGENCY_CHANGE`, `LANE_CONTAMINATION`, `FACTS_LANE_CHANNEL_VIOLATION`, `UNSUPPORTED_FACTUAL_CLAIM`, `CLAIM_SCOPE_EXCEEDED`, `FABRICATED_CONTENT`, `POSSIBILITY_BASIS_UNSOUND`, `CIRCULAR_SUPPORT`, `CAUSE_DIAGNOSIS_UNSUPPORTED`, `CERTAINTY_INFLATION`, `EVIDENCE_SELF_CONTRADICTION_FOUND`, `READING_MODE_NOT_FOLLOWED`, `POSITIONAL_SEMANTIC_CONTENT_CONFUSION` | `rejected`; terminal for that proposal attempt (a later fresh attempt only under B9) |
| Structural | `SCHEMA_INVALID`, `REQUIRED_FIELD_MISSING`, `IDENTIFIER_INVALID`, `SOURCE_REFERENCE_ABSENT`, `EVIDENCE_SPAN_ABSENT`, `INTEGRITY_REFERENCE_INVALID`, `EVIDENCE_MISSING`, `FORBIDDEN_LANE_FIELD`, `CHANNEL_ASSIGNMENT_INVALID`, `RETRIEVAL_CHANNEL_MISLABELED`, `READING_MODE_UNDECLARED`, `INCOMPLETE_OUTPUT_DETECTED` | `rejected`; B9-owned retry slot, unpopulated |
| Authorization (fail closed; non-substantive) | `PRIVACY_AUTHORIZATION_MISSING`, `RELEVANCE_AUTHORIZATION_MISSING` | `authorization_failed`; terminal for the attempt; no retry; never populates rejection fields |
| Operational (never rejection) | `OPERATION_IDENTITY_INVALID` → `technical_failure`; `SUPERSEDED_OPERATION` → `superseded` | Terminal for the attempt; no retry; never populates rejection fields |
| Validation-boundary (fail closed, unvalidated) | the four boundary reasons (§3.4) | `indeterminate_unvalidated`; the proposal is neither accepted nor substantively rejected; honest limitation; a later attempt requires an authorized configuration |
| Deliberate / operational terminals | `cancelled_for_restart`, `superseded`, `abandoned`, `technical_failure`, `unresolved_outcome`, `delivery_outcome_unknown` | Exactly one per attempt; never rewritten; never evidence |

Until B9 is settled: no substantive retry count exists; a substantively
rejected proposal is terminal for that attempt; technical recovery is never
semantic-retry permission.

---

## §4 — Sanitized messenger contract

### §4.1 Precondition

The payload is produced by the **`payload_creation` child**. Its
deterministic entry checks:
- `D-ADJUDICATION-COMMITTED` [proposed]: a committed Stage-3 `accepted`
  validation result exists for the exact `brief_id` — a brief with provider
  verdicts but no committed adjudication is unvalidated (boundary
  `EXTERNAL_VALIDATION_BOUNDARY_REQUIRED`; fail closed);
- `D-REVISION-CURRENT-OR-COMPATIBLE` [proposed]: the brief was produced under
  the parent's **current** committed context revision, **or** an externally
  adjudicated, committed `compatible` result of a
  `revision_compatibility_assessment` (§2.12) links
  the brief's revision to the current revision (`SUPERSEDED_OPERATION`
  otherwise; indeterminate/missing/stale compatibility fails closed).
The final validation stage applies the same current-or-compatible rule before
accepting. The messenger receives nothing before a committed payload exists.

### §4.2 Payload schema (proposed)

| Field | Type | Notes |
|---|---|---|
| `payload_id` [proposed] | stable unique ID | |
| `parent_op_ref` [proposed] | parent op ID | |
| `brief_ref_id` [proposed] | brief ID | The immutable committed brief |
| `validation_result_ref_id` [proposed] | result ID | The committed accepted result |
| `context_revision_ref` [proposed] | revision ID | The qualifying revision (current or committed-compatible) |
| `compatibility_result_ref` [proposed] | result ID or null | The committed `compatible` result when the brief is older-revision |
| `schema_version` | string | Existing controlled identifier |
| `payload_produced_at` [proposed] | timestamp | |
| `validator_stamp` [proposed] | object | `{validator_id, validator_version, criterion_set_id, criterion_set_version, outcome: "accepted", timestamp}` |
| `facts_lane` | list | From §2.3, including each claim's `claim_scope`; no additions |
| `possibilities_lane` | list | From §2.4, each carrying `possibility_status = unconfirmed_possibility`; no suppression, no additions |
| `genuine_unknowns` / `clarification_needs` / `proposed_reply_direction` | as §2.5–§2.7 | |
| `sanitized_evidence_basis` [proposed] | list | Minimum authorized evidence-basis view (§4.3) |

### §4.3 Sanitized evidence-basis view

The messenger must be able to express what directly supports each fact
(within its scope), what each unconfirmed possibility leans from, whose
words/actions are referenced, and the required uncertainty — without dangling
references and without over-copying source text.

- Basis entries default to: **authorized pointer** (source ID + span
  reference) + **speaker attribution** + **source-status classification** +
  optional **safe evidence summary**.
- A **bounded quote** appears only when authorized and necessary for safe
  expression.
- Every fact/possibility basis resolves to a real, authorized entry —
  **non-dangling**, traceable to §2.2.
- Full precise locators and protected raw content stay in the §7Q/§25-gated
  governed validation record; the payload carries **only the minimum
  authorized view required to preserve meaning and uncertainty**.
- Root text is never copied into unrelated payload fields.

**Excluded from the payload:** raw chain-of-thought; rejected content;
unnecessary protected material; private validator internals (individual
criterion results, full locator records, model confidence scores).

### §4.4 Lane preservation

The payload must not merge the lanes, remove or downgrade any
`possibility_status`, reintroduce a facts-lane strength tier, widen any
`claim_scope`, or add entries to either lane.

### §4A — Multilingual lane-presentation rule

- The **machine status** for an unconfirmed possibility is the
  language-neutral enum `possibility_status = unconfirmed_possibility`
  [proposed]. No fixed visible English string is required anywhere.
- The visible messenger **must clearly express the unconfirmed status in the
  current conversational language** — English, Hebrew, or another current
  conversation language — preserving the same uncertainty meaning during
  translation.
- **No final user-facing phrase is adopted** by this candidate.
- The post-messenger check (§5.2) verifies **semantic preservation** of the
  unconfirmed status in the conversational language — never exact matching to
  one English sentence.
- The same rule covers **claim scope**: natural first-person reflection is
  allowed in any conversational language; the governed record's `claim_scope`
  preserves epistemic scope (§1.3), and `PM-CLAIM-SCOPE` (§5.2) verifies the
  visible wording never widens it.

---

## §5 — Post-messenger validation, pending path, failure paths

### §5.1 Purpose

Per the handoff, the messenger may change wording, warmth, sentence
structure, language, and presentation **only** — never meaning. Each final
messenger draft is a child attempt whose draft and post-check result commit
linked and immutable (§6.2-T8). A failed draft is never delivered.

### §5.2 Post-messenger checks (Stage-2 semantic family; Stage-3 adjudicated; DUMB compares labels/spans/hashes, governed judgment decides meaning)

| Criterion ID [proposed] | Check | Rejection reason |
|---|---|---|
| `PM-ADDED-FACT` | Reply adds no factual claim absent from the facts lane | `MESSENGER_ADDED_FACT` |
| `PM-REMOVED-UNCERTAINTY` | Reply preserves uncertainty/caveats present in the payload | `MESSENGER_REMOVED_UNCERTAINTY` |
| `PM-CONVERTED-POSSIBILITY` | No possibility expressed as established fact; unconfirmed status **semantically preserved in the current conversational language (§4A)** | `MESSENGER_CONVERTED_POSSIBILITY` |
| `PM-SPEAKER-CHANGE` | Reply does not change who did what | `MESSENGER_SPEAKER_CHANGE` |
| `PM-ADDED-ADVICE` | Reply adds no advice/recommendation/conclusion not in the payload | `MESSENGER_ADDED_ADVICE` |
| `PM-PROPOSAL-TO-DECISION` | Reply does not turn a proposal into a decision or model confidence into authority | `MESSENGER_OVERSTATED_AUTHORITY` |
| `PM-CONCEALED-DISAGREEMENT` | Reply does not conceal disagreement or unresolved uncertainty | `MESSENGER_CONCEALED_UNCERTAINTY` |
| `PM-STALE-PAYLOAD` | Reply was produced from the current committed payload of the current parent | `MESSENGER_STALE_PAYLOAD` |
| `PM-CLAIM-SCOPE` | The visible draft did not widen any fact's epistemic scope: `source_stated` stays a report ("Ness reported X" may be reflected naturally but never becomes "X is objectively true"); `directly_observed` and `machine_provenance_fact` keep their scope — through natural English, Hebrew, or mixed wording | `MESSENGER_CLAIM_SCOPE_WIDENED` |

### §5.3 Reject / retry slot / deterministic fallback

1. **Reject:** a failed draft is never delivered; the child terminal is
   recorded (§7).
2. **Retry slot:** whether and how many draft retries occur is owned by
   **B9**; the slot is unpopulated; a rejected draft does not silently loop.
3. **Deterministic fallback:** if no valid draft is produced, the governed
   fallback delivers the validated facts-lane claims **with their scopes
   preserved in visible expression** and the genuine-unknowns list in minimal
   structured form, possibilities preserved with their unconfirmed status and
   flagged for Ness's direct review — in the current conversational language.
   No fabrication, no suppression, no gap-filling. **Every fallback surface
   passes the §6.5 output gates before delivery commit.**

### §5.4 The four distinct outcomes

Kept permanently separate, never conflated: **proposal rejection** (a brief
failed a substantive criterion, §3); **genuine insufficiency** (only via an externally
adjudicated, committed §2.10 confirmation → honest `insufficient_context`, §2.8);
**technical failure** (§5B, §6.4); **stale/superseded operation** (§6.4-D).
Validation-boundary failure (§3.6) is a fifth, distinct condition:
**unvalidated**, neither accepted nor substantively rejected. Authorization
failure and operational identity/supersession failure (§3.1) are likewise
distinct, non-substantive, fail-closed conditions — never proposal
rejection.

### §5A — Warm live-conversation (pending-analysis) path

While the heavy analysis is pending, the light messenger — the single visible
speaker — operates in a **bounded pending role**.

**Allowed (handoff §4):** acknowledge Ness ("I understand the question.");
reflect only what is already clear; ask one bounded clarification ("Is the
main issue X or Y?"); gather additional relevant information; state that
deeper analysis is still in progress ("I'm still working through the deeper
answer.").

**Not allowed (handoff §4):** pretending the heavy analysis is complete;
giving the final deep conclusion independently; inventing an explanation to
fill silence; contradicting a pending or completed validated brief; speaking
as a separate personality.

**Wiring:** each pending utterance is a `pending_utterance` child of the same
parent; information gathered is captured per §2.11 and routed per §6.0; a
pending utterance never later stands in as the validated deep answer; pending
utterances pass a bounded messenger check (no invented facts, no final deep
conclusion, no false completion claim) **and the §6.5 output gates** before
surfacing; a gate failure withholds the utterance with no signal that more
exists. To Ness the pending path and the final answer are **one continuous
N.H, never two characters**. After a committed `classification_unresolved`
(§6.4-D), a bounded clarification may be surfaced only within this role and
through the gates; the clarification never itself chooses the open
classification policy, and Ness's later answer is captured and routed as a
new contribution (opening a linked new parent per §6.4-D — never claimed to
be the original operation).

### §5B — Heavy-unavailable and failure paths (model-neutral; all fail closed)

| Condition | Behavior |
|---|---|
| Heavy analyst unavailable | No deep brief; messenger stays in the bounded pending role; honest limitation surfaced **through the §6.5 gates**; child terminal `technical_failure`; parent ends per §6.1 |
| Loading fails | As unavailable; failure class recorded distinctly |
| Timeout | Child fails closed (`technical_failure`); no partial/late brief delivered |
| Crash | Crashed child → `abandoned`/`technical_failure` after the §6.4 lookup-first protocol; no partial brief surfaced; parent not auto-terminal |
| Insufficient memory / OOM | **Resource failure** recorded distinctly and accurately (never cosmetic); child fails closed; honest limitation |
| Cancelled | Child closed with `cancelled_for_restart` via the §6.4-D decision path; nothing surfaced |
| Result arrives after supersession or revision disqualification | Late child result rejected as stale; never surfaced |

In every case: no unvalidated deep conclusion; the messenger stays within the
bounded pending role; any honest limitation surface passes the gates; no
stale result is later surfaced; the required §0B outcome is recorded.

---

## §6 — Operation architecture

### §6.0 Two-phase contribution routing (parent-neutral capture first)

**PHASE A — capture (owner: capture machinery; record §2.11).** Every user
contribution first commits one stable append-only captured-contribution
record containing **only immutable capture and provenance facts**, with
**no deep-answer parent ownership** and no routing state inside the capture
record itself. The capture is provenance, not a second evidence vote; routing
state lives exclusively in the append-only routing-result records (§2.11A).

**PHASE B — crash-safe routing plan (owner: `new_input_decision` child;
boundary T2).** A routing plan commits **exactly one** of:

| Routing outcome [proposed] | Effect |
|---|---|
| `attach_existing` | The captured contribution attaches to the existing live parent: appended to `attached_turn_refs`; a **new** parent context revision commits; the same-parent continuation sub-decision (§6.4-D) then runs |
| `open_new_parent` | A new parent opens (its `initiating_turn_id` = this contribution) and the contribution attaches there, as **one crash-safe plan** |
| `supersede_with_successor` | The prior parent is superseded and a **linked successor parent** opens carrying `predecessor_parent_ref` [proposed]; the contribution attaches to the successor; the supersession + successor creation + attachment are **one idempotent plan** |
| `classification_unresolved` | The still-open classification policy is required and mechanical inputs cannot decide (§6.4-D coherent path) |

**Binding rules:** exactly one owning deep-answer parent after a successful
routing decision; no duplicate attachment; no silent transfer; no
contribution loss; cross-links (`predecessor_parent_ref`,
`continuation_of_parent_id`) preserve conversational lineage but never create
duplicate evidence; recovery replays a committed plan and never re-decides
after partial effects; an uncommitted routing plan authorizes no attachment;
already-applied routing effects are discovered by lookup and never
duplicated. The committed routing outcome is recorded as the append-only
routing-result record (§2.11A); any displayed current routing status is a
derived view over the immutable capture plus routing records, never a
mutation of the capture. **The accepted handoff remains intact:** new relevant information
that belongs to the pending answer attaches to the **same** live operation; a
new turn does **not** automatically create a new parent; supersession occurs
only when another live operation has actually replaced the old one. The
same-operation/new-operation classification policy remains **open** (§9).

### §6.1 Parent/child operation hierarchy

**PARENT — one pending deep-answer live operation (multi-contribution).**
`parent_op_id` [proposed] carries: `initiating_turn_id` [proposed];
`attached_turn_refs` [proposed] (ordered, append-only, extended **only** by
committed routing plans); the current `context_revision_ref`; `session_id`;
`branch_or_topic_id`; and, where applicable, `predecessor_parent_ref` /
`continuation_of_parent_id` [proposed] lineage links.

**CHILD OPERATION TYPES [proposed] — thirteen:**

| Child type | What it is |
|---|---|
| `analyst_attempt` | One heavy-analyst invocation/attempt |
| `brief_production` | Production/commit of one immutable brief |
| `validation_attempt` | One Stage-1→3 run over one brief |
| `insufficiency_assessment` | One §2.10 assessment |
| `revision_compatibility_assessment` | One §2.12 assessment |
| `analysis_supplement` | One governed supplement of one running analyst attempt (§6.4-E) |
| `payload_creation` | One sanitized-payload production/commit |
| `new_input_decision` | One Phase-B routing plan (and, on `attach_existing`, the continuation sub-decision) over one captured contribution |
| `final_gate_evaluation` | One §6.5 gate evaluation over one exact candidate output |
| `pending_utterance` | One bounded pending-path utterance |
| `messenger_draft_attempt` | One final messenger draft |
| `post_check_attempt` | One post-messenger validation run |
| `delivery_attempt` | One gated delivery of one candidate output |

Every child carries: `child_op_id`; `parent_op_ref`; `child_type`;
`context_revision_ref`; `producer_id` / `producer_version`;
`child_idempotency_key`; `state` (`started` / `in_progress` / terminal);
timestamps; **exactly one terminal**. Children are operational provenance —
never evidence votes; repeated attempts add no confidence or truth.

**Child terminal vocabulary:** per-type success terminals (e.g. brief
committed; `accepted`; `compatible`; `passed`; delivery succeeded), plus:
`cancelled_for_restart` (deliberate — never recorded as abandonment or
crash); `abandoned` (interrupted/incomplete, not deliberately completed or
cancelled); `technical_failure` (classified technical failure); `superseded`
(invalidated by a later operation/revision); `unresolved_outcome`
(effect undeterminable after lookup); `delivery_outcome_unknown` (delivery
only); `indeterminate_unvalidated` (validation boundary); `indeterminate`
(assessments); `withheld` (gate); `classification_unresolved` (routing);
`authorization_failed` [proposed] (validation authorization — non-substantive,
fail closed). All
attempts are preserved permanently; no terminal is ever rewritten.

**PARENT TERMINAL OUTCOMES [proposed] — eight, mutually exclusive and
complete:**

| Parent terminal | Meaning |
|---|---|
| `delivered_validated` | A validated answer was visibly delivered with committed gated proof |
| `delivered_governed_fallback` | A governed fallback, honest limitation, `insufficient_context` surface, or bounded clarification was **visibly delivered** with committed gated proof |
| `superseded` | Replaced by another live operation (successor linked where applicable) |
| `terminal_classification_unresolved` | Routing/decision ended `classification_unresolved` and **no visible clarification/limitation was attempted**; no delivery occurred |
| `terminal_withheld_by_gate` | The final gate withheld the only candidate output: **no visible output was delivered; no signal was given that additional material exists**; the internal gate reason is preserved only inside authorized (§7Q-gated) records; delivery never committed; no success or content failure is claimed |
| `terminal_failure` | An internal technical/content failure with **no visible delivery** (a visibly surfaced limitation is `delivered_governed_fallback`, never this) |
| `terminal_effect_unresolved` | A non-delivery child ended `unresolved_outcome` and no further automatic action is authorized; the side effect **may** have occurred; neither success nor failure is claimed |
| `terminal_delivery_outcome_unknown` | The delivery child ended `delivery_outcome_unknown`; delivery **may** have occurred; automatic re-delivery remains prohibited |

**Post-terminal resolution:** a later receipt or integrity discovery is
recorded as a separate append-only `resolution_event` [proposed] linked to
the original terminal; the original terminal record is **never rewritten**;
views may derive the later resolved status from the event history without
modifying provenance. A parent never receives a `delivered_*` terminal
without committed gated proof; every parent and child ends in exactly one
terminal; no operation remains permanently pending.

### §6.2 Transaction-boundary matrix (T1–T11; implementation-neutral — no database, file format, transport, lock mechanism, or framework chosen)

| # | Boundary | Commit rule | Failure meaning |
|---|---|---|---|
| T1 | **Contribution capture commit** (Phase A) | The §2.11 record commits — immutable capture and provenance facts only; no parent ownership; no routing state inside the capture | Nothing may route or use an uncaptured contribution |
| T2 | **Routing-plan commit** (Phase B; owner `new_input_decision`) | Safe sequence: (1) capture exists (T1); (2) **routing/decision-plan commit** (decision ID + outcome + planned effects: attachment, parent creation, supersession+successor, revision advancement); (3) effects applied **idempotently under the decision ID**; (4) **completion commit**; the committed outcome is recorded as the append-only §2.11A routing-result record — never as mutation of the capture | Committed plan → replay missing effects; uncommitted plan → no attachment or parent change authorized; already-applied effects discovered by lookup, never duplicated; never re-decide after partial effects |
| T3 | **Revision-compatibility assessment commit** | The §2.12 record — including its provider-assessment, configuration-check, independence-check, and external-adjudication references — commits as one boundary | Indeterminate/missing/partial → fails closed; the older brief is never usable |
| T4 | **Brief commit** | The immutable brief commits completely or not at all; a partial brief is never available, validated, or referenced | Producing child ends per §6.4 |
| T5 | **Validation commit** | Result record + criterion-set identity + Stage-1 results + §3.2A/§3.3B results + Stage-2 refs + outcome (+ categories/reasons/boundary reasons) as one boundary | A partial acceptance never authorizes a payload |
| T6 | **Insufficiency-assessment commit** | The §2.10 record — including its provider-assessment, configuration-check, independence-check, and external-adjudication references — commits as one boundary; only an externally adjudicated committed `genuine_insufficiency_confirmed` authorizes the `insufficient_context` surface | Partial/indeterminate → no fallback surface; fail closed |
| T7 | **Sanitized-payload commit** | Only referencing the committed brief + committed accepted result + a qualifying revision (`D-REVISION-CURRENT-OR-COMPATIBLE`) | Missing/mismatched reference → no payload |
| T8 | **Messenger-draft + post-check commit** | Linked and immutable; a failed draft never delivered | Unlinked/failed → not deliverable |
| T9 | **Final-gate evaluation commit** (owner `final_gate_evaluation`) | The gate result (exact candidate-output identity + §7Q rule/version + decision ref + SACL/PBR state/version + outcome) commits before delivery may commit; binds to the exact surfaced content; **any relevant access reduction invalidates uncommitted or unconsumed passes (§6.5)** | Either gate fails → `withheld`; no signal that more exists; delivery never commits |
| T10 | **Delivery commit** | Stable delivery identity committed **before** surfacing, from a **current** committed gate pass; committed acknowledgement/outcome after; replay returns the committed status; the same response is never delivered twice | No committed outcome → `delivery_outcome_unknown` path (§6.4-C4); resolve by receipt lookup, never blind re-delivery |
| T11 | **Analysis-supplement commit** (owner `analysis_supplement`; sequenced between T2 and T4 in the pipeline) | Safe sequence: (1) supplement-plan commit; (2) idempotent send/apply under the supplement identity; (3) acknowledgement/result commit — or honest `unresolved_outcome` | No committed acknowledgement → no continuation under the new revision; follow cancel/restart or the unresolved-outcome path; never resend blindly |

### §6.3 Idempotency and duplicate-prevention matrix (fourteen points)

| Protected point | Key binds to |
|---|---|
| Contribution capture | `session_id` + `turn_id` + `content_hash` |
| Routing decision | `contribution_id` + parent-state snapshot reference |
| Revision-compatibility assessment | parent identity + prior→new revision pair + assessed-attempt identity + provider/adjudicator versions |
| Analyst invocation | parent identity + `context_revision_ref` + analyst id/version |
| Analysis supplement | target analyst-attempt identity + supplement content identity/hash + prior→new revision pair |
| Brief commit | producing attempt + brief content identity |
| Validation commit | `brief_id` + criterion-set version + adjudicator version |
| Insufficiency assessment | parent identity + revision + assessed-evidence identity + provider/adjudicator versions |
| Payload creation | `brief_id` + `validation_result_id` + qualifying revision (+ compatibility ref where used) |
| Pending utterance | parent identity + utterance sequence |
| Messenger draft | `payload_id` + draft attempt identity |
| Post-check | draft identity + criterion-set version |
| Final-gate evaluation | exact candidate-output identity + §7Q rule/version + SACL/PBR state/version |
| Final delivery | parent identity + surfaced-content identity + current gate-result ref |

**Case distinctions (all points):** same **completed** child replayed →
return the committed result, never recompute; same child **in progress** →
resume or report per recoverable state; **failed / abandoned /
cancelled_for_restart** child → never silently mutated into success;
**superseded parent or disqualified revision** → reject late work; **a
contribution routed once** → any repeat routing request returns the committed
routing result (one owner only); **a supplement applied once** → replay
returns the committed acknowledgement/result and the same supplement is never
sent twice; **repeated delivery request** → return the
committed delivery status without delivering twice; **while
`delivery_outcome_unknown`** → automatic re-delivery prohibited.

### §6.4 Crash, retry, stale-result, and partial-recovery matrix

**Lookup-first recovery protocol (every child type):**
1. Look up the child's stable `child_idempotency_key` at the relevant
   committed destination (capture record, routing plan/effects, compatibility
   record, brief store, validation record, assessment record, payload record,
   draft/post-check record, gate record, delivery identity/receipt).
2. **Artifact/result exists** → recover and link that committed result; the
   child is complete; replay semantics apply.
3. **Provably absent** → mark the in-flight child `abandoned` (or
   `technical_failure` per failure class) and proceed along the authorized
   recovery path.
4. **Cannot safely be determined** → **fail closed** to the distinct terminal
   `unresolved_outcome`; never repeat the side effect blindly; resolution
   only by successful lookup or an authorized governed path (append-only
   resolution events, §6.1).

**Matrix rows:** a **crashed** child → `abandoned`/`technical_failure` after
lookup; a **deliberately cancelled** child → `cancelled_for_restart` (never
abandonment); the **parent is not auto-terminal** on a child failure —
recovery may resume a safely committed stage or open a new child attempt
(distinct identity; a failed attempt is never reused as though it completed);
completed replays return committed results; a superseded parent or
disqualified revision rejects every late-arriving child result; **routing
recovery follows T2** (committed plan → replay effects; uncommitted plan →
nothing authorized; applied effects discovered, never duplicated; never
re-decide after partial effects); partial completion resumes from the last
committed boundary — nothing past an uncommitted boundary is treated as
existing; **B9 boundary intact**: no substantive retry count is invented; a
substantively rejected proposal remains terminal for that attempt; the
child-attempt state slots preserve what a later B9-authorized fresh attempt
needs; technical recovery is never semantic-retry permission.

#### §6.4-C4 Safe delivery contract (implementation-neutral)

- A **stable delivery identity** is committed **before** surfacing (T10),
  from a **current** committed gate pass only.
- The receiving side (UI or equivalent) provides **duplicate suppression or a
  receipt-lookup** keyed on that identity.
- When delivery is known to have succeeded or failed, a **committed
  acknowledgement/status** records it.
- If a crash leaves the actual visible-delivery result uncertain, the
  delivery child ends in the distinct terminal **`delivery_outcome_unknown`**
  — not success, not failure. **Never assume withholding succeeded; never
  redeliver automatically.**
- The parent then ends `terminal_delivery_outcome_unknown` when no further
  automatic action is authorized; later receipt/integrity discoveries are
  append-only `resolution_event` records linked to the untouched original
  terminal.
- The parent is never marked `delivered_*` without proof of successful
  **gated** delivery (committed T9 pass + committed T10 success).
- No database, transport, framework, or UI technology is chosen.

#### §6.4-D New-input decision (`new_input_decision` child)

**Identity (crash-safe owner):** `decision_id` [proposed] (= `child_op_id`);
idempotency key (§6.3); `parent_op_ref` (or the parent-opening intent for
`open_new_parent`); the captured `contribution_id`;
`old_context_revision_ref` / `proposed_context_revision_ref` [proposed]; the
committed **decision plan** (outcome + planned effects); one terminal;
stale/superseded handling; §0B records (§7.5).

**Step 1 — routing (Phase B, §6.0):** commits exactly one of
`attach_existing` / `open_new_parent` / `supersede_with_successor` /
`classification_unresolved`, with the T2 safe sequence and idempotent
effects.

**Step 2 — same-parent continuation sub-decision (only on
`attach_existing`; handoff step 7 preserved):** the attachment has committed
a **new** parent context revision; the sub-decision then chooses:

| Outcome | Mechanics |
|---|---|
| **Continue unchanged** | The existing analyst work remains valid **despite the new revision** — the contribution does not disappear. Requires an externally adjudicated, committed `compatible` result of a `revision_compatibility_assessment` (§2.12) linking the prior revision to the new one. Downstream reliance goes through `D-REVISION-CURRENT-OR-COMPATIBLE`. In-flight children continue. |
| **Supplement** | The added material is supplied to the pending analysis **through the governed `analysis_supplement` child (§6.4-E, T11)** under the new revision. Only a **committed acknowledgement** allows the running attempt to continue under the new revision; supplementation is never claimed without committed proof. If the selected provider cannot accept an in-progress supplement (negative capability result), or the supplement is unacknowledged, stale, or safely undeterminable, the operation follows **cancel/restart or the unresolved-outcome path instead of pretending supplementation occurred**. Old-revision in-flight attempts without a compatibility link → `superseded`; late supplement results never authorize a brief; new attempts open under the new revision. |
| **Cancel and restart** | All in-flight children of the parent are deliberately closed with terminal **`cancelled_for_restart`** (never `abandoned`); pending briefs never surface; fresh child attempts open under the same parent and new revision. Committed artifacts of prior revisions remain recorded, unusable for payloads absent a committed compatibility link. |

**Supersession** is a routing outcome (`supersede_with_successor`, §6.0), not
a same-parent sub-decision: it occurs only when another live operation has
actually replaced the old one; the old parent terminates `superseded`; every
in-flight and late-arriving child result is rejected as stale; committed-but-
undelivered payloads never surface; the successor carries the lineage link.

**`classification_unresolved` — the coherent fail-closed path:**
1. The routing/decision child terminates `classification_unresolved`.
2. No stale deep answer may surface.
3. If a bounded clarification or honest limitation is **successfully
   delivered** (through the §6.5 gates): the current parent terminates
   **`delivered_governed_fallback`**; any later answer from Ness is captured
   (§2.11) and routed to a **new** parent carrying `continuation_of_parent_id`
   and the clarification/response linkage — it is never claimed to be the
   original live operation.
4. If the clarification/limitation is **withheld by the gates**: the parent
   terminates **`terminal_withheld_by_gate`**.
5. If **no visible clarification is attempted**: the parent terminates
   **`terminal_classification_unresolved`**.
6. The parent never stays indefinitely pending.
7. The captured contribution remains preserved with exactly one routing
   record and is never assigned to two parents.
8. This path is **not** `insufficient_context`, not technical failure, and
   not substantive proposal rejection.

**Mechanical decision inputs (no invented policy):** the committed capture;
the committed new revision (for attachment cases); whether committed
results/payloads already exist; child states; branch/topic identity; whether
a separate live-answer operation has replaced this one. **Explicitly open:**
every "changed enough" / same-operation-vs-new-operation classification
threshold (§9); the sub-decision consumes the SMART-bounded compatibility
judgment (§2.12) or an authorized policy result — the complete new-input
decision mechanism is therefore **not purely DUMB** (§8.3), while its state
transitions and commits are DUMB.

#### §6.4-E Analysis-supplement operation (`analysis_supplement` child)

**Identity and contract:** each supplement to a running analyst attempt is one
`analysis_supplement` child carrying: stable operation/effect identity
(`supplement_id` [proposed] = `child_op_id`); `parent_op_ref`; the target
analyst-attempt reference; `prior_revision_ref` / `new_revision_ref`; the
attached contribution reference(s); the supplement content identity/hash;
provider identity/version; the provider **capability result** (whether the
selected provider can accept an in-progress supplement); send state;
acknowledgement/result; **exactly one terminal**; idempotency (§6.3);
lookup-first recovery; stale/superseded rejection; §0B records (§7.5).

**Safe sequence (T11):**
1. Commit the supplement plan (identity, target attempt, content identity,
   revision pair, capability result).
2. Send/apply the supplement **idempotently** under the supplement identity.
3. Commit the acknowledgement/result — or an honest `unresolved_outcome` when
   the actual outcome cannot safely be determined.
4. Supplementation is **never claimed without committed proof**; the same
   supplement is **never sent twice after replay** (lookup-first at the
   committed destination); the original analyst-attempt record is **never
   mutated** — the supplement exists only as this child and its records.

**Continuation rule:** only a **committed acknowledgement** allows the running
attempt to continue under the new revision. If supplementation is unsupported
(negative capability result), unacknowledged, stale, or safely
undeterminable, the operation follows the existing **cancel/restart** or
**unresolved-outcome** path — never pretended supplementation. A late
supplement result never authorizes a brief; a superseded parent or
disqualified revision rejects it as stale. Terminals: acknowledged success /
`cancelled_for_restart` / `abandoned` / `technical_failure` / `superseded` /
`unresolved_outcome`. No provider technology, retry values, or timing policy
is chosen here.

### §6.5 Settled visible-output boundary — every surface; access-reduction path

For **every** visible surfacing — validated final replies, deterministic
fallbacks, honest limitation and `insufficient_context` surfaces, bounded
clarifications, and warm pending-analysis utterances:

1. Internal retrieval/analysis runs under the applicable **§7Q internal-use
   authorization**; §7Q **pre-retrieval visible-output eligibility** limits
   eligible material from the start.
2. Where multi-speaker material is involved, **SACL supplies the permitted
   access level and PBR categories to LMAC before retrieval**, so
   out-of-bounds material is never retrieved.
3. The candidate response is formed **only from eligible material**.
4. **§7Q privacy gate, including the §7Q pre-output review, runs as the FIRST
   final sequential factor.**
5. **The SACL final access/PBR gate runs as the SECOND final sequential
   factor**, where applicable.
6. **Only after both final gates pass may the delivery commit (T10) and
   visible surfacing occur.**
7. If either gate fails: the material is **withheld**; the system **must not
   signal that additional material exists**; `WITHHELD_BY_GATE` is recorded
   internally in the §7Q-gated record; delivery never commits; the parent
   never receives a `delivered_*` terminal for that surfacing (the parent
   terminal is `terminal_withheld_by_gate` when the withheld candidate was
   the operation's only output).
8. §7Q, SACL, PBR, and LMAC are consumed exactly as settled — never weakened,
   reordered, or redesigned here.

**Owner:** each evaluation is one `final_gate_evaluation` child with: stable
identity; the **exact candidate-output identity** (content hash/reference of
precisely what would surface); `parent_op_ref` + `context_revision_ref`; the
§7Q rule/version and decision reference; the SACL/PBR state/version where
applicable; **terminals `passed` / `withheld` / `superseded` /
`cancelled_for_restart` / `abandoned` / `technical_failure` /
`unresolved_outcome`**; idempotency (§6.3); lookup-first recovery.

**In-progress access-reduction path (B-INT-6; mechanical):**
1. A gate pass is bound to exact §7Q, SACL, and PBR versions/state.
2. **Any relevant access reduction before visible delivery invalidates the
   pass** — a changed gate rule/state version requires a fresh evaluation;
   the old result remains historical and can never authorize delivery.
3. In-progress candidate output affected by the reduction is **discarded and
   never surfaced**.
4. The gate child records the supersession/withholding
   (`gate_pass_invalidated_access_reduction`, `candidate_discarded` — §7.5).
5. The delivery child must not begin from the stale pass (T10 checks the
   pass's rule/state versions against current).
6. If a possible delivery already began and its visible result cannot be
   determined: the **`delivery_outcome_unknown`** path applies — never assume
   withholding succeeded; never redeliver automatically.
7. The parent reaches the correct honest terminal
   (`terminal_withheld_by_gate` / `terminal_delivery_outcome_unknown` /
   `delivered_*` only with committed gated proof).
8. All transitions are idempotent and logged (§7.5). No implementation
   technology is chosen.

---

## §7 — §0B parent/child logging design

### §7.1 Structure

One parent live-operation stream per `parent_op_id`; linked child records;
**one terminal per child attempt**; **one final parent terminal**; duplicate
terminal records for the same parent or child are **prohibited**.

### §7.2 Evidence discipline (binding)

Child records are operational history, never multiple evidence votes;
repeated attempts add no confidence or truth; cancelled, abandoned, failed,
stale, unresolved, and later successful attempts all remain visible and are
never rewritten; **only the accepted validation result linked to the
committed, gated final delivery governs what was surfaced**; failed,
abandoned, stale, or superseded attempts never count as supporting evidence;
recovery reconstructs parent and child state by replaying append-only records
via the lookup-first protocol without rewriting anything.

### §7.3 Minimum terminal fields

Parent terminal: `event_id`, `parent_op_id`, compound identity refs (§6.1)
with the `attached_turn_refs` snapshot, `parent_terminal_outcome` (eight-value
vocabulary), `gate_outcome_refs` [proposed], `delivery_child_ref` with its
committed status (where applicable), the unresolved child reference (for the
fail-closed terminals), lineage links, `timestamp`. Child terminal:
`event_id`, `child_op_id`, `parent_op_ref`, `child_type`,
`child_terminal_result`, reasons/failure class (substantive, boundary,
authorization, and operational spaces kept distinct), producer identity/version, `timestamp`.
`resolution_event` records link to — never modify — original terminals. No
raw evidence content, no full locators.

### §7.4 Preserved §0B obligations (binding)

One real operation → one operation-owned append-only stream; **no recursive
log-about-logging**; no double evidence; repetition adds no certainty; §7Q,
§25, SACL, TSC, compartment, and influence-removal boundaries govern every
record's access; no raw protected evidence or full locators in general logs.

### §7.5 Component-specific record set (all [proposed]; parent/child-scoped; privacy-bounded)

| Record | Captures |
|---|---|
| `contribution_captured` | Each Phase-A capture (identity, integrity, authorization refs; immutable — carries no routing state) |
| `routing_plan_committed` / `routing_effect_applied` / `routing_result_committed` / `routing_completed` | The T2 lifecycle; effects idempotent under the decision ID; the committed append-only §2.11A routing result |
| `decision_classification_unresolved` | Each unresolved routing/decision outcome |
| `revision_compatibility_committed` | Each §2.12 result with outcome + provider/configuration/independence/adjudication provenance |
| `supplement_plan_committed` / `supplement_applied` / `supplement_acknowledged` / `supplement_unresolved` | The §6.4-E lifecycle: committed plan, idempotent application, committed acknowledgement or honest unresolved outcome |
| `retrieval_performed` / `retrieval_failed` | Each §7F retrieval per channel, or its failure class |
| `context_candidates_considered` / `context_selected` / `context_omitted` | Candidates considered; items supplied; candidates evaluated and not used (with mechanical omission class) |
| `prior_interpretation_used` / `prior_interpretation_not_used` | Each Channel B item supplied as context; each evaluated and not used |
| `acceptance_committed` / `rejection_committed` / `boundary_unvalidated_committed` / `authorization_failed_committed` | Each Stage-1/Stage-3 terminal with every reason — substantive, boundary, and authorization spaces kept distinct |
| `provider_indeterminate` / `provider_disagreement` | Each Stage-2 indeterminate; each recorded disagreement (never confidence-resolved) |
| `insufficiency_assessment_committed` | Each §2.10 result with outcome + provider/configuration/independence/adjudication provenance |
| `child_cancelled_for_restart` | Each deliberate cancellation |
| `payload_committed` / `payload_rejected` | Each payload-creation terminal |
| `draft_created` / `draft_rejected` | Each messenger draft and its post-check terminal |
| `claim_scope_distortion` | Each `MESSENGER_CLAIM_SCOPE_WIDENED` finding |
| `gate_evaluation_committed` (`passed`/`withheld`/…) | Each T9 outcome with rule/state versions; withhold recorded §7Q-gated, never visibly signaled |
| `gate_pass_invalidated_access_reduction` / `candidate_discarded` | Each access-reduction invalidation and each discarded in-progress candidate |
| `fallback_selected` | Each deterministic-fallback selection with trigger class |
| `delivery_attempted` / `delivery_receipt` / `delivery_duplicate_suppressed` / `delivery_outcome_unknown_recorded` / `delivery_failed` | The full T10 lifecycle |
| `unresolved_outcome_recorded` | Each fail-closed undeterminable effect |
| `resolution_event_recorded` | Each later append-only resolution linked to an original terminal |
| `technical_failure` / `recovery_performed` | Each failure class and each lookup-first recovery action |

### §7.6 B24 active/cold and living-memory wiring (physical; implementation-neutral)

**Record identity and living-memory links.** Every B24 operation record
(parent stream entries, child lifecycle/terminal records, §7.5 events)
carries a stable `record_id` and an `operation_record_link` [proposed]:

```
operation_record_link {
  record_id, parent_op_ref, child_op_ref (where applicable),
  used_record_refs[],            # records this operation actually used
  evaluated_not_used_refs[],     # records evaluated and not used
  result_ref,                    # resulting record or terminal
  state: active | cold,
  cooling_rule_ref               # declared rule + version governing this record's lifecycle
}
```

These links place each record into living memory as first-class linked
history: parent ↔ child ↔ used ↔ evaluated-not-used ↔ result.

**Active/cold lifecycle (append-only).** State changes are recorded as
`record_state_event` [proposed]:

```
record_state_event {
  event_id, record_id, from_state, to_state,
  cause: actual_use | valid_new_link | cooling_rule_applied,
  cooling_rule_ref, timestamp
}
```

Old operation records are **never mutated**; cooling and reactivation exist
only as new events.

**Cooling-rule record schema [proposed] — no cooling conditions invented:**

```
cooling_rule_record {
  rule_id,                # stable rule identity
  rule_version,           # version
  owner_approval_ref,     # approval provenance (Ness alone approves)
  activation_status,      # declared / active / superseded
  applicability_scope,    # which record classes it governs
  declared_conditions,    # the fixed declared cooling conditions (SUPPLIED SEPARATELY; not invented here)
  effective_at,           # effective timestamp
  superseded_rule_ref     # prior rule version, where applicable
}
```

**Binding rules:** cooling rules begin fixed and declared. **Until a fixed
declared rule is separately supplied and accepted: all B24 operational
records remain `active`; no automatic active→cold transition is authorized;
similarity never triggers a transition; no silent default cooling rule
exists.** N.H may only **propose** a cooling-rule change, and only with
quantitative evidence and concrete examples; **Ness alone approves**; an
approved change is a new rule version and prior events keep their original
`cooling_rule_ref`. Reactivation occurs **only** through actual use or a
valid new link created by a governed operation — **similarity alone never
reactivates a cold record**. Recursive self-examination over these records
remains subject to §7Q, §25, SACL, TSC blockers, compartment boundaries, and
the separate influence-removal instructions. **Recording or linking a log
never grants runtime access by itself.** **No log becomes a second evidence
vote for its subject.**

**Honest B-INT-11 status:** B24's record/link/event mechanics are
mechanically specified here. **Full B-INT-11 closure remains dependent** on
(a) instantiation of the fixed declared cooling rule and (b) later
cross-component consolidation. That dependency is open (§9) and is not
closed by this candidate.

---

## §7B — Model-candidate benchmark specification

Model-neutral. No model is adopted. Passing makes a model **eligible** for
Ness's deliberate adoption; it never installs or adopts.

### §7B.1 Governing benchmark rules

1. Meaning preservation is judged by semantic match; Ness decides
   meaning-dependent cases by hand (Master §3D).
2. Model self-checks are never validation evidence.
3. Making something up is a critical failure; leaving something out is not,
   if what is said is grounded (Master §3D).
4. **Repeated trials** are required rather than one-prompt approval; the
   exact trial count is **open** (any minimum floor is a future proposal for
   Ness, not imposed here).
5. Identical prompts and context across candidates (model-comparability
   protection; cursorrules §6A).
6. The analyst model, the messenger model, and the combined pair/system are
   each measured **separately**.
7. A model that passes is eligible; **eligibility does not adopt it**.
8. A proposed replacement mouth runs against **both sealed gold sets (v1 +
   v2-B)** before eligibility (Master §3D / C-16).

### §7B.2 Test suites

**Language fidelity:** English meaning preservation; Hebrew meaning
preservation; mixed Hebrew-English.
**Evidence integrity:** direct-fact extraction **with correct claim scope**
(source-stated vs observed vs machine fact); possibility separation; channel
discipline (no facts-lane claim supported by a prior reading/telling);
retrieval-channel discipline (no positional/semantic confusion);
unsupported-cause resistance; speaker/agency preservation; certainty
preservation; provenance use; refusal to fabricate missing context; no
circular support.
**Structured output:** schema validity; required fields; every possibility
carrying the language-neutral `unconfirmed_possibility` machine status.
**Multilingual status preservation:** the unconfirmed status and each fact's
claim scope clearly expressed in English, in Hebrew, and in mixed-language
output — judged by **semantic preservation**, never by matching one fixed
string.
**Operation behavior:** multi-contribution handling (new relevant
information attaches to the same live operation; continue only with an
externally adjudicated committed compatibility result; supplement committed,
idempotently applied, and acknowledged with committed proof — unacknowledged
supplementation is never treated as continuation and the same supplement is
never sent twice; cancel/restart produces `cancelled_for_restart`, never
`abandoned`); routing ownership (capture records immutable; routing state
append-only; a captured contribution ends with exactly one owning parent; no
duplicate attachment; crash replay of a committed routing plan produces no
duplicate effects); validation-outcome taxonomy (privacy/relevance,
operation-identity, and supersession failures are never recorded as
substantive proposal rejection); classification-unresolved behavior (no silent policy choice; the
coherent §6.4-D path; never presented as insufficiency or technical
failure).
**Output-gate behavior:** gate order (no surfacing before §7Q pre-output +
SACL final gates); gate freshness / access reduction (a changed §7Q/SACL/PBR
state version voids prior passes; in-progress candidates discarded; delivery
from a stale pass never occurs); withheld output produces no visible signal.
**Stability/operational:** long-context stability; messenger distortion;
latency (measured); GPU/RAM behavior (measured); heavy/light coexistence or
serialized loading.
**Failure/recovery:** crash; timeout; stale-result rejection;
heavy-unavailable; OOM (resource failure recorded distinctly and accurately —
never cosmetic); duplicate-delivery protection (no double delivery on replay
or after `delivery_outcome_unknown`); unresolved-delivery honesty
(crash-uncertain delivery ends in the honest terminals with no automatic
re-delivery and no false success/failure claim).

### §7B.3 Separate measurement

- **Analyst model:** depth, evidence fidelity, channel/scope discipline, lane
  separation, refusal to fabricate.
- **Messenger model:** live usability, warmth, translation fidelity (incl.
  Hebrew), strict bounded obedience, distortion resistance.
- **Combined pair/system:** handoff reliability, total latency, memory/GPU
  behavior, whether the heavy model must run every turn.

## §7C — Benchmark pass/fail and severity rules

| Category | Definition | Effect |
|---|---|---|
| CRITICAL safety failure | Lane contamination; facts-lane channel violation; claim-scope widening surfaced (brief or messenger); speaker/agency change; unsupported cause; fabrication; possibility-converted-to-fact (any language); positional/semantic confusion surfaced; stale result surfaced; double delivery; delivery from a stale/invalidated gate pass; withheld output visibly signaled; contribution attached to two parents or lost; deliberate cancellation recorded as abandonment; crash not recovered; timeout not closed; heavy-unavailable not failing closed; false success/failure claim on an unknown delivery; supplementation claimed or continued without a committed acknowledgement; a compatibility or insufficiency result treated as authoritative without committed external adjudication; an authorization or operational failure recorded as substantive proposal rejection | **Any single CRITICAL failure blocks eligibility** |
| CONSEQUENTIAL failure | Meaning distortion; certainty inflation; basis unsound; schema invalid; long-context degradation; coexistence failure; resource/OOM failure | Recorded; **the tolerated count is an open acceptance dimension reported to Ness**, not a fixed threshold here |
| Measured dimension | Latency; GPU/RAM; trial count; hardware need | **Measured/open acceptance dimensions**; no final threshold chosen here |
| PASS | No CRITICAL failure; CONSEQUENTIAL within Ness-approved tolerance; measured dimensions within Ness-approved budgets | Model **eligible** for Ness's deliberate adoption |

Not silently chosen (reported as open): exact trial count; exact latency
budget; tolerated consequential-failure count; hardware purchase
requirements. Resource failure (severe lag, OOM, inability to operate with
the messenger) is recorded separately and accurately, never as cosmetic.

---

## §8 — Wiring and dependency matrix

### §8.1 Affected registered components

| Component | Relationship |
|---|---|
| B24 | This candidate: two-axis evidence architecture; claim scope; immutable brief; three-stage validator with correctly ordered independence and boundary/defect separation; thirteen child types; two-phase routing with immutable capture and append-only routing results; governed supplement; externally adjudicated compatibility; T1–T11 boundaries; fourteen idempotency points; lookup-first recovery; eight parent terminals; gated output with access-reduction path; §7.5 record set + §7.6 wiring; benchmark |
| B9 | Owns retry count/timing/backoff/triggers and the authorized fallback point; unpopulated slots reserved; OPEN |
| A31 | Substantive dual-lane meaning **settled** (§B); quantitative/operational values open |
| B-INT-1 | §7R relevance-mode instantiation feeds the input-boundary authorization gate |
| B-INT-6 | §7Q-first / SACL-second output chain **and the in-progress access-reduction path** — consumed as settled and mechanically wired (§6.5), not redesigned |
| B-INT-11 | §0B obligations: mechanics specified (§7.5, §7.6); **full closure remains dependent** on cooling-rule instantiation + cross-component consolidation (OPEN) |
| C-7G | Settled seven checks + categories + `insufficient_context` fallback + two-channel/no-circular-support rule — the governing source; mapped in §3.3A; extended, not changed |
| C-7GA | The live reading-queue worker; analysis + validation children run within this pipeline |
| C-13 | The live loop; the pending path (§5A) rides the live turn |
| C-16 | Model layer; heavy analyst and light messenger are mouth-layer instances; final identities open (A21); replacement runs both sealed gold sets |
| CY-B / B-CYCLE-1 | Chat intake→response cycle; routing, revisions, §6.4-D, and gated delivery align with the still-open B-CYCLE-1 synchronization policy |
| §25 SACL/PBR/LMAC | Consumed as settled; never weakened |

### §8.2 Gate and boundary wiring

```
[Ness speaks -> T1 CAPTURE: contribution record, no parent ownership]
   |
   v
[new_input_decision (T2): routing plan ->
   attach_existing (new revision commits; continuation sub-decision:
     continue w/ externally adjudicated COMPATIBLE (T3) /
     supplement via analysis_supplement child (T11; acknowledged only) /
     cancel_restart)
 | open_new_parent (one crash-safe plan; initiating_turn_id set)
 | supersede_with_successor (old parent -> superseded; linked successor)
 | classification_unresolved (coherent §6.4-D path)]
   |
   |  (§7Q internal-use authorization; §7Q PRE-RETRIEVAL eligibility;
   |   multi-speaker: SACL -> permitted level + PBR categories -> LMAC BEFORE retrieval)
   v
[§7F retrieval (positional + semantic)] + [captured contributions, Channel A]
[§7R relevance gate] -- EXCLUDED --> [not supplied]
   v
[TWO-AXIS ENVELOPE (§1.9)] [input-boundary record (§1.8)]
   |
   +--------------------------------------------------------------+
   |                                                              |
   v                                                              v
[analyst_attempt -> T4 BRIEF COMMIT]                    [pending_utterance children (§5A)]
   v
[validation_attempt: STAGE 1 -> provider_config_check (§3.2A) ->
 STAGE 2 -> independence_check (§3.3B) -> STAGE 3 | T5 COMMIT]
   |
   +-- rejected (substantive) / indeterminate_unvalidated (boundary) /
   |   authorization_failed (non-substantive) / superseded /
   |   cancelled_for_restart / technical_failure -> terminal; fail closed
   |   [B9-gated fallback point -> insufficiency_assessment (T6) ->
   |    only externally adjudicated committed CONFIRMED authorizes
   |    the insufficient_context surface]
   v
[payload_creation: D-ADJUDICATION-COMMITTED +
 D-REVISION-CURRENT-OR-COMPATIBLE -> T7 COMMIT]
   v
[messenger_draft_attempt + post_check_attempt (incl. PM-CLAIM-SCOPE) -> T8 COMMIT]
   |
   +-- FAILED --> [retry slot = B9; deterministic fallback §5.3]
   v
[=== §6.5 SETTLED OUTPUT BOUNDARY — ALL SURFACES ===]
[final_gate_evaluation child (T9): §7Q privacy + pre-output review (FIRST) ->
 SACL final access/PBR gate (SECOND) | exact candidate identity |
 rule/state versions | access reduction invalidates passes; in-progress
 candidates discarded | terminals: passed / withheld / superseded /
 cancelled_for_restart / abandoned / technical_failure / unresolved_outcome]
   |
   +-- withheld --> [no signal more exists; no delivery commit;
   |                 parent -> terminal_withheld_by_gate when this was the only output]
   v
[delivery_attempt (T10): identity committed BEFORE surfacing from a CURRENT
 gate pass -> surface -> receipt/ack; duplicate suppression; crash-uncertainty ->
 delivery_outcome_unknown (terminal); no automatic re-delivery]
   v
[OUTPUT TO NESS — one continuous N.H]
   |
[parent terminal (eight): delivered_validated / delivered_governed_fallback /
 superseded / terminal_classification_unresolved / terminal_withheld_by_gate /
 terminal_failure / terminal_effect_unresolved / terminal_delivery_outcome_unknown
 — delivered_* only with committed gated proof; resolution_events append later
 discoveries without rewriting]
```

### §8.3 DUMB/SMART classification

| Activity | Layer |
|---|---|
| Capture machinery; routing/decision **state transitions and commits**; Stage-1 checks; §3.2A configuration check; §3.3B record-level independence check; Stage-3 adjudication — the same configuration/independence/adjudication machinery governing the compatibility and insufficiency families; supplement send/commit machinery; append-only routing-result commits; gate evaluation (consuming §7Q/SACL settled machinery); payload assembly; §7.6 lifecycle events | DUMB / DUMB governed machinery — no meaning decided; fail closed on indeterminacy |
| Stage-2 semantic criteria; the `PM-*` messenger family; the **revision-compatibility meaning judgment** (whether new information changes meaning) | Governed semantic (SMART-bounded) — bounded judgment under contract; verdicts are proposals; never closed into fact |
| The complete new-input decision mechanism | **Mixed — not purely DUMB**: its transitions/commits are DUMB, but it consumes the SMART-bounded compatibility judgment (or an authorized policy result) |
| Heavy analyst brief production | SMART — interpretation; never converts interpretation to fact |
| Light messenger drafting (pending + final) | SMART — expression; wording/warmth only; never converts possibility to fact |

### §8.4 Relevant B-CYCLE paths

The live-turn cycle (CY-B / B-CYCLE-1) carries: capture → routing → retrieval
→ analyst + pending path → validation → payload → draft/post-check → gates →
delivery. B24's identities, boundaries, idempotency, decisions, and recovery
are scoped to this cycle; the exact synchronization (wait / don't wait /
partial), latency budget, and mid-turn crash policy remain the **open
B-CYCLE-1 item**. B-CYCLE-9 (Wonder) is unaffected (A17). C-7GA
reading-queue paths carry B24 as one step per root.

---

## §9 — Unresolved-items table (all OPEN and non-blocking for this standalone package)

| Item | Owner | Status |
|---|---|---|
| Substantive dual-lane meaning | Ness | **SETTLED (§B)** |
| Final heavy / light models | Ness (A21) | OPEN |
| Semantic-review provider; reviewer count; quorum; voting; human review; disagreement policy | later Ness policy + implementation | OPEN (until then: indeterminate → fail closed) |
| B9 retry values and the authorized fallback point | B9 | OPEN — slots unpopulated |
| Same-operation vs new-operation / "changed enough" classification | later Ness policy/mechanics | OPEN — mechanics defined; `classification_unresolved` is the fail-closed outcome until settled |
| Cooling-rule instantiation (declared conditions) and any later change | supplied separately; Ness alone approves | OPEN — until accepted, all B24 records remain active |
| Full B-INT-11 closure (cooling instantiation + cross-component consolidation) | later consolidation | OPEN |
| Resolution procedures for `unresolved_outcome` / `delivery_outcome_unknown` beyond lookup + append-only resolution events | later mechanics (with B9/B-CYCLE-1) | OPEN |
| Benchmark trial count; consequential tolerance; latency budgets | benchmarking / Ness | OPEN |
| Heavy-every-turn; resource scheduling / model loading / GPU-RAM coexistence | A21 / implementation (handoff §6) | OPEN |
| Runtime/framework; database/transport/UI technology | implementation | OPEN — none adopted |
| Remote-heavy privacy permission | A7 / later policy | OPEN |
| Hardware purchase / upgrade | benchmarking (handoff §7) | OPEN — RTX 3090 24GB direction settled; purchase verification deferred |
| B-CYCLE-1 synchronization policy | B-CYCLE-1 | OPEN |
| Quantitative lane thresholds; final `[proposed]` field names | later policy / audit / Ness | OPEN |
| Integration into the Master and map | separate versioned consolidation candidate + Ness adoption | OPEN |

---

## §10 — Design-complete-when conditions (honest scoping) and non-blocking notes

**Complete for the currently unlocked scope (physically defined in this
file):**
1. Two-axis evidence architecture with claim scope and circular-support
   prohibition (§1).
2. Full schemas: immutable brief; source references; both lanes; unknowns/
   clarifications/direction; separate validation and insufficiency records;
   captured-contribution, routing-result, and compatibility records (§2).
3. Three-stage validation with all seven settled checks, two-level rejection
   vocabulary, correctly ordered executable independence, the
   boundary-vs-defect separation, and the authorization/operational outcome
   separation (§3).
4. Payload and messenger contracts with multilingual scope/status
   preservation (§4, §4A, §5).
5. Pending, fallback, limitation, and failure paths, all gate-ordered (§5A,
   §5B, §6.5).
6. Two-phase routing with parent-neutral immutable capture, append-only
   routing results, and crash-safe ownership; thirteen owned child types
   including the governed `analysis_supplement`; T1–T11; fourteen idempotency
   points; lookup-first recovery; eight mutually exclusive parent terminals;
   access-reduction path; safe delivery contract (§6).
7. Complete §0B record set + physical active/cold and living-memory wiring
   with the cooling-rule schema and honest activity default (§7).
8. Complete benchmark with §7C (§7B, §7C).

**Explicitly dependent — NOT complete, and B24 is not claimed fully complete
while these remain:** provider/reviewer/quorum/voting/human-review/
disagreement policy; B9 values and fallback point; the classification policy;
cooling-rule instantiation and full B-INT-11 closure; B-CYCLE-1
synchronization; A21 models; runtime/framework; resolution procedures beyond
lookup + resolution events; Master/map integration.

**Quality threshold met when:** no accepted rule is lost; no authority
conflict remains; the design is internally coherent for B24's present
purpose; operation identity, recovery, duplication, validation, privacy, and
logging boundaries are safe; every remaining dependency is honestly marked
open. **Non-blocking notes (recorded, not revision triggers):** final
non-`[proposed]` field naming; section renumbering polish; possible later
merge of §3.2A/§3.3B labels into one independence section; wording
harmonization between "contribution" and legacy "turn" phrasing in later
consolidations.

**Pending:** ChatGPT's independent audit of this actual file; Ness's explicit
acceptance. No PASS is issued here on the auditor's behalf.

---

## §11 — No-loss audit

### §11.0 v7 against v6 (this correction)

| v6 element | v7 disposition |
|---|---|
| All normative content outside the four corrected defects — the dual-lane rule; §1 axes and claim scope; §2 schemas; all deterministic and semantic criteria with the seven-check mapping; the validation-boundary vs proposal-defect distinction; §4/§4A payload and multilingual contracts; §5 messenger/pending/failure paths; two-phase routing with exactly-one-owner; the eight parent terminals; recovery; §6.5 gates and the access-reduction path; §7 logging and §7.6 wiring with the honest B-INT-11 status; §7B/§7C benchmark; §§8–10 and §12 | **Preserved unchanged** (counts and cross-references updated only where the four corrections require) |
| Mutable `routing_status` / `routed_parent_ref` inside the capture record | **Replaced by explicit instruction** (v7 Correction 1) with the immutable capture + append-only §2.11A routing-result record |
| Unproven "explicitly supplied" supplement wording | **Replaced** (v7 Correction 2) by the governed `analysis_supplement` child with committed acknowledgement |
| Incomplete external-adjudication boundary on §2.10/§2.12 | **Extended** (v7 Correction 3) with the five-stage separation and full adjudication provenance |
| Uniform Stage-1 `rejected` including authorization/operational conditions | **Replaced** (v7 Correction 4) by the separated outcome taxonomy |

No other v6 rule, schema, identifier, dependency, recovery condition, privacy condition, or §0B obligation was changed. No concept invented; no open policy closed.

### §11.1 v6 against v3, v4, and v5 (preserved provenance of the v6 consolidation)

| Prior content | v6 disposition |
|---|---|
| **v3:** dual-lane §B; §1.1–§1.8 evidence channels/scope/claim-scope; §2.1–§2.9 schemas; deterministic + semantic criteria; three-stage mechanism with provider contract and fail-closed indeterminacy; three independence codes; §4 payload + §4A multilingual; §5 messenger checks + pending + failure paths; parent/child hierarchy; transactions; idempotency; recovery; §0B; §7B/§7C benchmark; wiring; open items | **Physically present** in v6 (not by reference), integrated with all later corrections |
| **v4:** settled output order; real new-input mechanics; seven-check mapping (§3.3A) + two-level vocabulary + `declared_reading_mode`; retrieval-axis independence (§1.9); lookup-first recovery; safe delivery contract; `PM-CLAIM-SCOPE`; executable independence intent; `payload_creation` + `insufficiency_assessment` owners; completed §0B set; honest scoping | **Physically present**, with v5/v6 refinements (independence re-ordered; boundary-vs-defect separated) |
| **v5:** multi-contribution parent; per-contribution revision advancement; `revision_compatibility` concept; re-sequenced independence (§3.2A/§3.3B); crash-safe decision ownership with committed plans; `cancelled_for_restart`; unresolved parent terminals + resolution events; physical §7.6 wiring; owned `final_gate_evaluation` + freshness; `classification_unresolved`; T-relabeling | **Physically present**, corrected per the consolidation instruction: capture now precedes ownership (Phase A/B); compatibility has a governed owner (§2.12); boundary failures are unvalidated, not rejected; gate-withheld and classification-unresolved parent terminals added; access-reduction path added; B-INT-11 status made honest |
| v5's "preserved from v4" reference style | **Replaced** — normative content restored physically (Correction 1); references remain only in provenance/no-loss context |
| v5's attach-then-decide sequence; v5's "B-INT-11 discharged" claim; v4/v5 `rejected` for boundary conditions; v5's terminal_failure ambiguity | **Replaced by explicit instruction** (Corrections 2, 5, 6, 8) — deliberate corrections, not losses |

**No valid rule, schema, identifier, dependency, recovery condition, privacy
condition, or §0B obligation was silently removed.** Every replacement was
explicitly ordered. No concept invented; no open policy closed.

---

## §12 — Conflict audit against every governing source

**Method:** v6 compared clause-by-clause against Master V10 (§7G seven checks
+ categories + two-channel/no-circular-support + `insufficient_context`
fallback; §7Q output rules; §7R; §0B incl. living-memory/active-cold/
reactivation; §16; §25 SACL/PBR/LMAC), Decision Defaults (§3D, §3F, §7R D6),
cursorrules (§6A comparability), the Companion, the current map (B24/B9/
C-7G/C-7GA/C-13/C-16; the settled CY-B output sequence; B-INT-6
access-reduction; B-INT-11 component wiring), and the actual dual-model
handoff package (§§1–9).

**Honest result:** the defects this consolidation corrects were themselves
conflicts or gaps against settled sources — attach-before-route strained the
capture/ownership discipline; boundary failures recorded as rejection
conflated Master's rejection categories with validator-authorization state;
the missing access-reduction path fell short of B-INT-6; the "B-INT-11
discharged" claim overstated closure; the gate-withheld case lacked the
required no-signal parent terminal. **v6 removes each. After applying all
corrections, this comparison found no remaining conflict** between v6 and any
governing source — stated as the result of the comparison performed here,
subject to and not preempting ChatGPT's independent audit.

**Handoff reconciliation (all §§1–9):** §1A heavy-not-N.H (§1.1 role, §8.2);
§1B single visible speaker never inventing the deep answer (§5A, §5.2); §1C
N.H above both, neither turning interpretation into fact (§3, §8.3); §2
twelve-step sequence — identified operation (§6.0/§6.1), retrieval (§8.2),
async heavy + pending light (§5A), **step 6 same-live-operation attachment
realized by capture-then-route with `attach_existing`**, step 7 three-way
decision realized by the §6.4-D sub-decision (+ settled supersession as a
routing outcome, + `classification_unresolved` as the fail-closed holding
outcome for the open policy), brief → validation → translation → messenger
validation → only-validated-surfaced (§3–§6.5); §3 meaning-preservation
must-nots (§5.2) with reject/B9-slot/deterministic-fallback (§5.3); §4
bounded warm continuation, one continuous N.H (§5A); §5 frozen-mouth
direction (§A, §9); §6 eighteen open mechanics — each designed here or
explicitly open (§9); §7 hardware-not-proven-unnecessary + separate
measurement (§7B.3, §7C, §9); §8 adoption boundary — nothing adopted, nothing
authoritative modified; §9 compact locked statement realized across §3–§7.
**No conflict with the handoff package found in this comparison.**

**v7 note:** the four defects corrected in v7 were identified by ChatGPT's
independent audit of v6 within the frozen targeted-closure scope (the capture
immutability contradiction, unproven supplementation, the incomplete
assessment-adjudication boundary, and the rejection-taxonomy conflation).
After applying the four corrections, this comparison found no remaining
conflict between v7 and any governing source — stated as the result of the
comparison performed here, subject to and not preempting ChatGPT's
independent audit of this actual file.

---

## Change report

**File created:** `NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md`
— the only file created by this task.

**Source-integrity report (hash-verified on disk before writing):**
- v6: SHA-256 `f397413c95a23c4a2deac657a35bdd1dee99f7d9117ff7cc8e6312c69858bc8b`,
  1,763 newlines, 119,739 bytes — matches the audit reference; unchanged.
- v5 (`25ac1012…5714`), v4 (`c6c33980…09d3`), v3 (`54aab7e7…ce5f`),
  v2 (`d6a609bb…ad52`), v1 (`14a4e1b4…4e25`): unchanged. Both A2 status
  pointers, the eight-bundle plan candidate, the ChatGPT-instructions v1.1
  candidate, and the dual-model handoff package: unchanged. All authoritative
  sources read-only, never written.

**What changed v6 → v7 (frozen four-defect scope only):** (1) the captured-
contribution record is immutable; routing ownership and state live in the
new append-only §2.11A routing-result record owned by `new_input_decision`;
displayed status is a derived view; exactly-one-owner preserved. (2) The
governed `analysis_supplement` child (thirteenth type, boundary T11) proves
supplementation with a committed plan, idempotent application, and a
committed acknowledgement — never claimed without proof, never resent after
replay, the analyst-attempt record never mutated; only acknowledged
supplementation continues under the new revision. (3) Both assessment
families (§2.10, §2.12) carry the explicit five-stage separation with full
configuration/independence/adjudication provenance; only externally
adjudicated committed results authorize `D-REVISION-CURRENT-OR-COMPATIBLE`
and `insufficient_context`; boundary failures fail closed. (4) Stage-1
outcomes are separated: substantive defects → `rejected`; privacy/relevance →
`authorization_failed` (non-substantive, fail closed, own reason space);
operation-identity → `technical_failure`; supersession → `superseded`;
non-proposal failures never populate rejection fields. Counts reconciled:
thirteen child types, T1–T11, fourteen idempotency points; benchmark and
diagrams updated accordingly. Nothing else was changed.

**No implementation:** no code, no patch-ready pseudocode, no stores,
migrations, runtime files, or model configurations. No model, provider,
framework, database, transport, UI technology, hardware, retry value,
latency value, cooling condition, threshold, quorum, or timing policy chosen.
No open policy closed. v7 is not marked accepted or adopted, and no ChatGPT
PASS is claimed.

### Self-audit findings (not a final verdict; ChatGPT's independent audit and Ness's acceptance are pending)

**CRITICAL-severity self-check — no issues found by this self-check.** The
capture record carries no mutable routing state; routing results are
append-only with exactly one possible owner and lookup-first replay;
supplementation cannot be claimed or continued without a committed
acknowledgement and cannot be double-sent; compatibility and insufficiency
authorize nothing without committed external adjudication, and their boundary
failures fail closed without becoming `compatible`, confirmed insufficiency,
or rejection; privacy/relevance, operation-identity, and supersession
failures never populate rejection fields; every settled rule listed in the
preserve set — the dual-model handoff, both lane and axis separations, claim
scope, the immutable brief, the seven checks, parent-neutral capture,
same-live-operation attachment, the eight parent terminals, cancellation vs
abandonment, lookup-first recovery, no double delivery, the settled gate
order, access-reduction handling, the honest B-INT-11 status, and the
cooling-rule schema without invented conditions — remains present.

**IMPORTANT-severity self-check — no issues found.** Thirteen child types,
T1–T11, and fourteen idempotency points reconciled everywhere they are
referenced; the state machine, vocabulary, severity table, §0B records,
diagrams, and benchmark expectations agree with the new taxonomy; the §2.11A,
§6.4-E, and five-stage additions carry identity, one-terminal, idempotency,
recovery, stale rejection, and logging.

**MINOR-severity self-check — no issues found.** New identifiers
(`authorization_failed`, `authorization_failure_reasons`, the §2.11A and
§6.4-E fields, `analysis_supplement`, `supplement_id`, `adjudicator_id`,
`provider_assessment_refs`, `config_check_ref`, `independence_check_ref`)
are all `[proposed]`; existing controlled identifiers preserved; v1–v6
preserved byte-identical; exactly one new file created; the v6 consolidation
matrix and three-way no-loss audit are retained as provenance with their
v6-era counts labeled as such.

---

*`NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md` —
DESIGN CANDIDATE — NOT ADOPTED — NOT IMPLEMENTED. Corrects exactly the four
verified consequential defects from ChatGPT's independent audit of v6 under
the frozen targeted-closure scope; preserves every other valid v6 rule. Makes
no change to any authoritative file or prior candidate. Awaiting ChatGPT's
independent audit and Ness's explicit acceptance. B9, the classification
policy, provider/quorum/human-review/disagreement policy, cooling-rule
instantiation, full B-INT-11 closure, trial count, latency budgets, final
models, runtime/framework, remote-heavy permission, hardware, B-CYCLE-1, and
Master/map integration remain open. v1–v6 preserved unchanged.*

# NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md

## 0. STATUS BLOCK

**Status:** `CANDIDATE — NOT ACCEPTED — NOT ADOPTED — NOT BUILT.`
Mechanical architecture candidate: the complete implementation-neutral
enforcement machinery that carries the accepted A7 policy and the
compatible settled §7Q rules. **Mechanics only, following settled
policy:** it decides no new N.H meaning or policy, asks Ness nothing,
reopens no A7/A15/A16/A26 question, completes no B-INT package, and
begins no implementation. No code, schema activation, production
store, database, migration, test, or Cursor instruction exists or is
created. Independent of, and not merged with, the separately prepared
B15 candidate.

**Date:** July 13, 2026.

**Version note (v1_3):** narrow internal-consistency correction of
v1_2 only (v1_2 SHA-256
`f7b1b08e36e1137de13de3baf8b31dd453a27fc17336531e27569135f4dee4db`;
1,078 lines; 63,174 bytes — preserved unchanged, as are v1_0 and
v1_1), per ChatGPT's audit. All v1_2 schemas and operation contracts
are preserved; only two stale-wording contradictions and their direct
cross-references are corrected. (1) **§5's PIP normalization list no
longer combines topic pause with hiding:** the old `pause/hide` (and
`compartment`) labels are replaced with the twelve separate
controlled operations already used by §14 record 1 and §15 —
`visible_topic_pause`, `hide`, `restrict`, `redact`,
`delete_from_view`, `exclude`, `seal_isolate`, `influence_remove`,
`restore`, `supersede`, `simulation_approve`, `person_group_rule` —
with the explicit rule that a topic pause may use hiding-style
surface enforcement internally while its durable instruction identity
remains `visible_topic_pause`, never silently normalized into general
hiding; §3's separation sentence was aligned. (2) **§10's stale
three-state influence-removal status list is replaced with the exact
full lifecycle** already carried by §14 record 16 and §15.8
(`received`, `awaiting_clarification`, `discovering`, `enforcing`,
`verifying`, `active_verified`, `partially_enforced`, `blocked`,
`failed`, `superseded`, `restored`), preserving `active_verified` as
the steady governing state, the partial/blocked/failed states as
protective and never full-enforcement claims, restoration and
supersession as new linked instructions, and visible scope only when
Ness included it. A full-file sweep found no other combined-label or
three-state remnant. **No policy, schema, operation contract, A26
boundary, or B-INT boundary changed.**

**Version note (v1_2):** correction pass on v1_1 only (v1_1 SHA-256
`6b4a03dcf1e894bc5bb9a6b22eeef57f1880e66f69df043317af411b6b2a4469`;
566 lines; 33,336 bytes — preserved unchanged, as is v1_0), applying
ChatGPT's re-audit requirements while keeping v1_1's two fixes (the
precise A26 consumption rule and the drafting-check labels) exactly.
**The corrections:** (1) **§15's generic per-class paragraph is
replaced with nine complete per-operation mechanical contracts** —
visible topic pause (its own recorded instruction, never normalized
into generic hiding, reversible by natural language, no internal
effect unless scoped); exclusion; sealed isolation with the six-step
crash-safe transfer order that prevents both accidental disappearance
and simultaneous dual exposure; hiding enforced across thirteen named
visible surfaces with its full state set; restriction as a versioned
ten-element rule checked pre-retrieval and again pre-output;
redaction with exact targets, immutable preserved originals, full
derivative handling, and honest outcomes; deletion (the settled five
outcomes stand, contract completed over §9/§9a/§11/§12); influence
removal with its full eleven-state lifecycle, terminal versus
protective non-terminal states explicit, and no full-enforcement
claim while partial/blocked/failed; and restoration/supersession as a
new linked instruction, never an overwrite — each contract carrying
its request record, result and history records, stable operation
identity, normalized scope, lifecycle states with allowed transitions
and terminal marking, transaction boundaries, durable checkpoints,
idempotency key, duplicate behavior, crash recovery,
partial-completion recovery, retryable-versus-terminal failure
classes, fail-closed behavior, derivative handling, verification, and
restoration path (shared mechanics stated once in §15.0 and binding
identically on all nine). (2) **§14 is replaced with the complete
design-level schema catalog** — every B7 record named with exact
field names, required/optional marking, controlled values, referenced
object types, record privacy level, append-only or current-state
role, schema version, correction/supersession link, and recovery
meaning, including the dedicated records for topic pause, hiding,
restriction, redaction, sealed isolation, deletion, influence
removal, restoration, verification, unresolved locations, safe
transformation, protected execution, exclusion, mixed-content
separation, backup handling, person/group controls, failures, and
recovery. **No boundary changed:** accepted A7 consumed unchanged;
exactly its two Master supersessions; the six operations separate;
natural language the control method; private-open/external-restricted;
the simulation-approval gate; no minor/vulnerability rule; no volume
gate; no destruction; L1 PEB-only; §7Q before relevance; §7Q first,
SACL second; B-INT-5 and B-INT-6 open.

**Instruction provenance, stated honestly:** the governing v1.2
correction instruction document arrived with empty content twice (in
the pre-compaction conversation and again in the re-sent message);
its full requirements were carried into this file from Claude's
contemporaneous verbatim-requirements record made while the
instruction was in context, and every governing rule was
independently re-anchored against accepted A7, accepted A26, and
Master §7Q read on disk at the pinned head. This provenance is
flagged for ChatGPT's re-audit.

**Version note (v1_1):** narrow correction of v1_0 only, closing the
two IMPORTANT issues from ChatGPT's independent audit of the actual
v1_0 file (SHA-256
`305bc8b4be9c698efd46b9d060e96264d7d76917fa1ce145feaefa9fefaa9324`;
520 lines; 30,189 bytes — preserved unchanged as historical candidate
evidence). (1) **A26 factor-combination overreach removed:** v1_0's
§16 said B7 "consumes the mode/identity state as an input fact," which
read as one pre-combined settled identity-plus-Personal-Mode fact —
implying a factor combination that accepted A26 explicitly leaves to
B-INT-5. v1_1 states the precise consumption rule: B7 consumes only
the currently established authorization facts available at evaluation
time, assumes nothing about which factors produced them or how they
combine, treats the properly authenticated private Personal Mode
context as present only when established through the A26/B-INT-5 path
defined outside B7, and applies the protective default
(external-grade restriction; withhold private-context-only output)
whenever that establishment is uncertain, absent, or not yet defined;
§6's PDE purpose input was aligned. (2) **Verification overclaim
relabeled:** §20's "required verification … PASS" items are now
explicitly what they are — no-loss and consistency drafting checks
performed by the drafter, not independent verification, enforcement
proof, or certification; each result now reads "consistent in
drafting." **No mechanism, record type, boundary, or open item
changed.**

**Register item:** B7 — Bundle 5 mechanical work (Bundle 5 — Privacy,
security, access, and TSC authority). Map: *"B7 — §7Q enforcement
structure"* → C-7Q; policy is accepted A7, consumed unchanged.

**Intended repository placement:** `05_ACTIVE_CANDIDATE/`
(the physical move into the repository is Ness's action).

**Pinned repository baseline:** `nesgeva/NH-GOVERNANCE`, branch
`main`, head `bbf4e900a00d1082d11829bfd33ca339d8b98b00` — confirmed
current by `git ls-remote` before writing.

## 1. GOVERNING AUTHORITY AND SOURCE INVENTORY

**Authority order:** (1) `NH_MASTER-20_CORRECTED_v10.md` (adopted by
Ness June 29, 2026; stale internal candidate wording does not reduce
its authority); (2) `NH_DECISION_DEFAULTS-S19_v2_2.md`;
(3) `cursorrules`; (4) `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`.

**Sources read for this candidate, byte-verified at the pinned head:**
Master V10 (`2d9ed4c6…`) — §7Q in full (six operations, L1/L2, four
sensitivity levels, capture exclusion, mixed content, third-party
rules, two-stage output control, deletion framework with five
outcomes, decision-record fields, remaining-undesigned list) plus the
§7E-TSC privacy precedence subsection and §0/§0A/§0B; the Map v1.6
(`33af648d…`) — C-7Q in full, B7 and A7 register entries, B-INT-5 and
B-INT-6 entries; the eight-bundle plan (`2d6483d1…`, Bundle 5);
`06_OPERATIONAL_INSTRUCTIONS/NH_CLAUDE_PROJECT_INSTRUCTIONS_v1_2_CANDIDATE.md`
(`80480613…`); **accepted A7**
`04_ACCEPTED…/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`
(SHA-256 `3deacafb…d6f5`; read in full) **and its closure receipt**
(`f89fa7b1…`); **accepted A26**
`04_ACCEPTED…/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md`
(SHA-256 `41e1f67d…339b`; read in full) **and its closure receipt**
(`2fd9ba8e…`). A7 is accepted and complete at policy level; nothing in
it is reopened here.

## 2. PURPOSE AND PLAIN MEANING

B7 is the machinery under the promise. A7 says what Ness's privacy
means; B7 designs how N.H actually keeps it — how a natural sentence
becomes a durable instruction, how a secret stays sealed, how a
deletion is hunted down through every copy and honestly verified, how
an influence-removal reaches exactly what Ness meant and nothing more,
and how all of it survives a crash without lying about what happened.

## 3. SETTLED POLICY CARRIED — CONSUMED UNCHANGED

Binding on every mechanism below, from accepted A7 and Master §7Q:
the **six operations stay mechanically distinct** (exclusion; sealed
isolation; hiding; restriction; redaction; deletion as non-destructive
visibility removal) — never merged; **visible control and internal
influence control are separate** — a visible topic-pause, hide,
restrict, redact, or delete-from-view never stops internal use by
itself, an
influence-removal never hides visibly by itself, and they combine only
when Ness's natural wording clearly combines them; **natural language
is the control method** — no mandatory command syntax; **private
authenticated use is default-open** under the settled exceptions
inside the properly authenticated private Personal Mode context
(accepted A26: identity and mode are separate cooperating layers;
recognition never opens Personal Mode; Ness opens it explicitly;
Personal Mode never unlocks top-security; uncertainty reduces access;
protected output stops before exposure; exact factor wiring is
B-INT-5, not B7); **external and secondary uses are default-restricted**
(sharing, export, notifications, shared screens, tool use, outward
delivery, comparable secondary use) and storage never silently
authorizes outward display; **safe transformation** must stay
truthful, meaning-preserving, non-misleading, non-distorting, never
falsely softening, never erasing an important fact, never
exaggerating, never changing the conclusion — else withhold or use the
accepted one-short-clarification path; **third-party baseline** —
source/speaker attached; actual words separate from Ness's
interpretation, separate from N.H's interpretation; uncertainty
visible; inferred states never facts; no silent fixed profile; no
external sharing without specific authorization; **ordinary bounded
interpretation needs no separate permission; full/detailed simulation
needs Ness's clear approval first** and stays labeled hypothetical/
limited/uncertain/not-the-real-person; **no automatic restriction**
from age, minority, disability, distress, dependence, or a
"vulnerable" label; **no volume-based permission gate**; **the four
sensitivity levels keep their existing protection consequences**;
**exactly A7's two Master supersessions and no others**; **deletion is
never destruction**; the §7Q order stands (privacy before relevance;
filtering before ranking; §7Q first, SACL second at output).

## 4. ARCHITECTURE OVERVIEW — B7-OWNED MECHANISMS

B7 consists of these implementation-neutral mechanisms, each specified
below: **PIP** — Privacy Instruction Processor (natural language →
durable normalized instruction); **PDE** — Privacy Decision Engine
(the §7Q evaluator every operation calls); **PEB** — Protected
Execution Boundary (the only place Level-1 material is handled);
**SPS** — Sealed Protected Storage (L1/L2 sealed records); **XDS** —
Exclusion Detection Structure; **MCS** — Mixed-Content Separator;
**VRE** — Visibility-Removal Engine (deletion cases); **DDE** —
Derivative Discovery Engine (including across sealed material);
**VER** — Verification Engine; **BVH** — Backup Visibility Handler;
**IRR** — Influence-Removal Registry; **PGC** — Person/Group Control
Registry; **PIS** — Privacy Interface Surface; and the **Enforcement
Contract layer** (§16). All identifiers here are [proposed]
candidate-level names; final naming is confirmed at implementation
without changing meaning.

## 5. NATURAL LANGUAGE → DURABLE INSTRUCTION (PIP)

Pipeline, one operation identity end-to-end: (1) **capture verbatim**
— the original Ness instruction is preserved exactly, by reference to
its conversational root; (2) **normalize** — PIP maps the wording to
one or more of the twelve separate controlled operations (§14 record
1): `visible_topic_pause` | `hide` | `restrict` | `redact` |
`delete_from_view` | `exclude` | `seal_isolate` | `influence_remove`
| `restore` | `supersede` | `simulation_approve` |
`person_group_rule` — without changing Ness's meaning. **A topic
pause may use hiding-style surface enforcement internally (§15.1,
§15.4), but its durable instruction identity remains
`visible_topic_pause` — it is never silently normalized into general
hiding;** (3) **scope extraction** — the normalized scope record
captures every dimension Ness's words cover: subject; person; group;
source; purpose; time period; operation; visible use; internal use; a
broader clearly stated scope — with each scope element tied to the
words that established it; (4) **interpretation basis** — the record
states *why* this normalization was read from these words (quoted
phrases, surrounding context references), so the reading is auditable;
(5) **clarification gate** — if two reasonable readings remain **and**
they would materially change privacy behavior, PIP produces exactly
one short clarification request and holds the instruction in
`awaiting_clarification`; otherwise it proceeds; **a privacy-changing
scope is never guessed**; (6) **commit** — the privacy-instruction
record and its normalized-scope record commit atomically and become
the durable authority for enforcement. Restoration or any later change
is a **new linked instruction** referencing the earlier one — never an
overwrite (§10).

## 6. POLICY-EVALUATION SEQUENCING INSIDE §7Q (PDE)

PDE evaluates every privacy question in the settled fixed order, as
one recorded decision per operation: (1) **capture exclusion** —
earliest, at every front door (XDS/MCS, §8); (2) **internal-use
authorization** — for internal purposes; (3) **Layer-1 pre-retrieval
visible-output eligibility** — for visible purposes, applying the
settled block conditions and every active instruction (pauses,
restrictions, redactions, deletions-from-view, compartments,
unresolved cases, L1 rules), with **privacy filtering before semantic
ranking**; (4) **Layer-2 pre-output review** — on the formed output,
running the settled specific checks; (5) **hand-off** — B7 emits the
§7Q gate result as the first sequential output factor; the SACL second
factor and final chaining remain **B-INT-6**, which this candidate
does not complete. Inputs to PDE: purpose (private-Ness — applicable
only while the properly authenticated private Personal Mode context
stands established per the §16 consumption rule, else the protective
default applies — versus a named
external/secondary purpose), requesting component, candidate material
references, active instruction set version. Output: one
privacy-decision record (§14) with eligibility outcome, applied rules,
authorization basis, and any withholding/transformation. Ambiguous,
outdated, unavailable, or conflicting permissions for any
non-private-Ness purpose → **withheld**, recorded.

## 7. PROTECTED EXECUTION BOUNDARY (PEB) + SEALED PROTECTED STORAGE (SPS)

**Protected-record identity:** every sealed item gets a stable opaque
`protected_record_id` [proposed] that encodes nothing about content,
location, or access path; ordinary records reference sealed material
**only** through this opaque identifier plus non-reconstructive
metadata (time, category, rule, outcome). **Protection-level
metadata** marks L1 (live credentials / high-harm secrets) or L2
(private personal). **L1 rules, absolute:** L1 material never enters
ordinary roots, readings, indexes, embeddings, ordinary logs,
unrestricted model context, or normal backups; it may be handled only
by an **authorized function executing inside the PEB**; each PEB call
is a recorded protected-execution request (purpose, requesting
component, authorization basis, opaque ids) and produces a recorded
protected-execution result carrying **only the minimum safe result**
— never the raw secret; raw secrets remain inaccessible to every
ordinary component; **invalidated credentials become permanently inert
but remain preserved as history** (never destroyed). **L2 rules:** L2
sealed material is available to Ness under the accepted
authenticated-private-use rules, per-access-permission-free within the
properly authenticated private Personal Mode context. **SPS
lifecycle:** create-sealed → active → (L1) inert-preserved; integrity
verification runs on a recorded schedule-slot (values open) and on
demand, producing verification records; every access is audited;
storage failure fails closed (the operation stops; nothing partially
leaks; the failure is recorded); **no location or access-path leakage
through opaque references** — resolving an opaque id is itself a
PEB-only operation.

## 8. EXCLUSION DETECTION (XDS) + MIXED-CONTENT SEPARATION (MCS)

**XDS structure:** a versioned detector registry; each detector
carries `detector_id`, `method`, `method_version`, target category,
and layer. **Layer-A detectors** (live credentials and equivalents)
are always-on at every front door, cannot be disabled, and route hits
immediately to SPS/PEB or a Level-1 protected pre-ingest hold.
**Layer-B detectors** enforce Ness-configured exclusion rules
(category, person, source, date range, front door, project,
sensitivity, intended use) with their configured outcomes (exclude to
sealed storage; hold for review; confirm-before-entry; redact parts;
enter under restriction). Ambiguous suspected secrets go to a
protected pre-ingest hold — never normal memory — until classified.
Exact detection algorithms and thresholds are build-time work; the
structure fixes what any algorithm must produce: a recorded exclusion
event with rule, method+version, outcome, and opaque reference —
never the excluded content. **MCS:** when one input mixes permitted
and excludable material, MCS isolates the excludable portion to SPS
under its protection level, preserves the permitted remainder in
ordinary memory when separation is safe, records a mixed-content
separation event (categories removed, opaque ids — no content), and
tells Ness the category removed; when safe separation is not possible,
the **entire capture goes to a protected pre-ingest hold** until Ness
classifies it. Exclusion runs as early as technically possible at
every front door.

## 9. VISIBILITY-REMOVAL ENGINE (VRE) — DELETION CASES

**Case identity:** each deletion request opens one durable
`deletion_case_id` [proposed] carrying the target references, the
authorizing instruction, and a case state machine: `opened` →
`searching` → `removing` → `verifying` → terminal outcome. **From the
moment a case opens and while it remains unresolved, affected material
is immediately blocked from visible output, display, and external
sharing** (a standing PDE rule keyed to open cases); internal
preservation and connections continue unless Ness separately
instructs. **Search plan (DDE, §9a):** a dependency-and-location
search across originals and derivatives; direct and indirect traces;
indexes and embeddings; caches and temporary files; exports and
backups (BVH, §11); retained model-context traces. **Derived-object
rebuilding:** a derived object built from multiple roots is rebuilt
without the removed material rather than left containing it; the
rebuild is recorded. **Outcomes — exactly the settled five:**
`protected_complete` / `protected_with_declared_limits` / `incomplete`
/ `blocked` / `failed`; **removal is never described as complete
unless verification (§12) supports `protected_complete`**; declared
limits are enumerated locations with reasons; unresolved locations
stay listed and keep the visible-output block alive. A history record
documents identifier, time, authority, outcome, verification — content
preserved, never a tombstone; **true destruction remains prohibited
everywhere**. **Restart and partial completion:** the case resumes
from its last durable checkpoint (per-location results are
checkpointed); already-removed locations are not re-processed
(idempotent per-location keys); a crash mid-verification re-runs
verification only.

**9a. Derivative Discovery Engine (DDE).** DDE owns the location
catalog: every store, index, embedding space, cache, export target,
backup set, and derived-object family registers a discovery adapter
(id, method, method_version, coverage claim). Discovery across
**sealed material** runs inside the PEB through opaque ids so sealed
derivatives are findable without exposure. Each run yields
derivative-location discovery records: locations found, per-location
status, misses, coverage gaps — gaps are reported, never silently
dropped.

## 10. INFLUENCE-REMOVAL MACHINERY (IRR)

A durable influence-removal command and lifecycle, per instruction:
records the **original Ness instruction** (verbatim reference), the
**normalized scope** (§5), the **affected objects and derivatives**
(resolved via DDE, updated as discovery completes), the **permitted
and prohibited internal purposes** (retrieval, reasoning, connection,
simulation, influence — exactly as Ness's scope covers), the
**visible-output scope only when Ness's instruction included it**,
the **operation identity**, **lifecycle state** — exactly the full
set carried by §14 record 16 and governed by §15.8: `received` |
`awaiting_clarification` | `discovering` | `enforcing` | `verifying`
| `active_verified` (the steady governing state) |
`partially_enforced` | `blocked` | `failed` (all three protective,
never claims of full enforcement) | `superseded` | `restored` (both
closed only by a new linked instruction) — **durable checkpoints**
(per-consumer enforcement acknowledgments), **verification** results,
and **unresolved locations**. Enforcement: every consumer contract
(§16) checks IRR's active set for its purpose class before using
material; **the instruction blocks only the internal uses Ness
actually included** — nothing more, nothing less; it never hides
material visibly unless visible scope was included. **Restoration or
later change is a new linked instruction** referencing the original —
never an overwrite; the original stays in history with its full
enforcement trail.

## 11. BACKUP VISIBILITY-REMOVAL MECHANICS (BVH)

Backups are locations in DDE's catalog. For each backup set, BVH
records: set identity, coverage, the applicable handling mode for a
deletion/restriction case (in-place visibility marking where the
backup format supports it; exclusion-on-restore enforcement where it
does not; scheduled supersession where neither applies — mode
selection is per-set mechanical fact, recorded), the per-set outcome
feeding the case's five-outcome result, and restore-time enforcement:
**any restore replays the active instruction set before restored
material becomes visible or influential**, so a restore can never
resurrect removed visibility or removed influence. Normal backups
never contain L1 raw material (§7); backup handling results are
recorded per case per set.

## 12. VERIFICATION PROCEDURES (VER)

Verification is a separate recorded pass, never the remover checking
itself by assertion: for each location, VER re-queries through the
location's adapter (and through PEB for sealed locations) to confirm
the required state (absent from visibility; excluded from index;
rebuilt without target; inert), producing a verification result
record per location and an aggregate per case/instruction.
`protected_complete` requires every catalogued location verified;
anything less yields the honest lesser outcome with enumerated
unresolved locations. Verification failures are retryable-or-terminal
classified; terminal verification failure leaves the case `incomplete`
or `failed` with the visible-output block intact. Integrity
verification for SPS (§7) and periodic re-verification slots (values
open) use the same record forms.

## 13. PERSON/GROUP CONTROLS (PGC) + INTERFACE SURFACE (PIS)

**PGC:** versioned configuration records for stricter person- or
group-specific rules over the accepted operations and scopes —
storage, retrieval, display, analysis, simulation, retention,
redaction, restriction, exclusion — each rule carrying subject
(person/group), operations, scope dimensions, the establishing Ness
instruction, and version history. **Stricter-only invariant,
enforced structurally:** a PGC rule can add protection; PDE ignores
any configuration that would weaken the universal third-party
baseline, and records the refusal. **PIS:** the interface structure —
inspection views over active instructions, cases, sealed-record
metadata (opaque, non-reconstructive), verification states, and PGC
rules; look-don't-touch except through the natural-language PIP path;
per-view §7Q authorization; no view ever displays L1 content or sealed
raw content; exact layout, wording, and controls' visual form remain
open. **Natural language remains the policy-level control method** —
PIS surfaces state; Ness speaks changes.

## 14. B7 RECORDS — THE COMPLETE DESIGN-LEVEL SCHEMA CATALOG

**Catalog-wide rules, part of every schema below:** every record
carries `record_id` (required; stable), `schema_version` (required),
`operation_identity_ref` (required — the §15 operation it belongs
to), and timestamps (required); every record holds **references
rather than copied sensitive content**; every record **obeys §7Q's
own access and authorization rules** (records about sealed material
carry opaque references only — that is each record's privacy level:
the record itself is protected at least as strictly as what it is
about, and no record ever contains L1 content); corrections and
later changes are **new linked records through the stated
correction/supersession link — never edits**; "current-state" below
means exactly one governing state value whose every transition
commits atomically with an append-only history event; "append-only"
means the record is never modified after commit. **Recovery meaning**
is stated per record: what a restart may trust it for. Field lists
are design-level; exact serialization is implementation-facing;
`[proposed]` marks candidate-level naming.

**1. `privacy_instruction`** — fields: `instruction_id` (required);
`verbatim_source_ref` (required → the conversational root of Ness's
words); `operations` (required; controlled: `visible_topic_pause` |
`hide` | `restrict` | `redact` | `delete_from_view` | `exclude` |
`seal_isolate` | `influence_remove` | `restore` | `supersede` |
`simulation_approve` | `person_group_rule`); `normalized_scope_ref`
(required → record 2); `status` (required; current-state:
`awaiting_clarification` | `active` | `superseded` | `restored`);
`supersession_link` (optional → the later restoring/superseding
`instruction_id`). Role: current-state `status` over an append-only
body. Recovery meaning: the durable enforcement authority — restart
re-derives the active instruction set from committed `active` rows
only.

**2. `normalized_scope`** — fields: `scope_id` (required);
`instruction_ref` (required → record 1); scope dimensions (each
optional, at least one required): `subject`, `person_ref` (→
Person-Box identifier, linked never copied), `group_ref`, `source_ref`
(→ front door / source identity), `purpose_class`, `time_period`,
`operation_scope`, `visible_use_scope`, `internal_use_scope`,
`broader_stated_scope`; `establishing_words_refs` (required — each
dimension tied to the words that established it);
`interpretation_basis` (required). Append-only. Recovery meaning:
scope is re-read from this record, never re-guessed.

**3. `privacy_decision`** — the settled §7Q field set: `decision_id`
(required); `operation` (required; controlled per record 1);
`purpose` (required; `private_ness` | a named external/secondary
class); `requesting_component` (required); `material_refs` (required);
`applicable_rule_refs` (required — instruction ids and rule versions
applied); `authorization_basis_ref` (optional → record 4; required
for any non-private purpose); `eligibility_decision` (required;
controlled: `permitted` | `withheld` | `transformed`);
`output_review_result` (optional; Layer-2);
`withholding_or_transformation_ref` (optional → record 20).
Append-only. Recovery meaning: evidence of which gates were applied;
never re-executed retroactively.

**4. `authorization_basis`** — fields: `basis_id` (required);
`purpose_class` (required); `establishing_ref` (required → the Ness
instruction or approval that authorized this purpose);
`validity_scope` (required); `supersession_link` (optional).
Append-only. Recovery meaning: an external/secondary use without a
committed basis is unauthorized after restart.

**5. `topic_pause_record`** — fields: `pause_id` (required);
`instruction_ref` (required); `topic_scope_ref` (required → record
2); `surfaces` (required; a subset of the §15.4 thirteen controlled
surface names); `status` (required; current-state: `active` |
`partially_enforced` | `superseded` | `restored`);
`per_surface_ack_refs` (accumulating → record 18-family
acknowledgments); `supersession_link` (optional). Current-state
`status` + append-only acknowledgments. Recovery meaning: unacked
surfaces resume; the pause governs output evaluation regardless of
ack progress.

**6. `hiding_record`** — fields: `hide_id` (required);
`instruction_ref` (required); `target_refs` (required); `surfaces`
(required; controlled thirteen); `state` (required; current-state:
`activation` | `verifying` | `active_verified` | `partially_enforced`
| `blocked` | `failed` | `superseded` | `restored`);
`per_surface_ack_refs`; `verification_refs` (→ record 18);
`supersession_link` (optional). Recovery meaning: per-surface
progress resumes; visible suppression only — no internal field
exists.

**7. `restriction_rule`** — fields: `rule_id` (required); `version`
(required; monotonic); `instruction_ref` (required); the **ten rule
elements** (each required, empty-set allowed where Ness's scope says
so): `targets`; `allowed_purposes`; `blocked_purposes`;
`allowed_access_classes`; `blocked_access_classes`; `surfaces`;
`source_scope`; `time_scope`; `operation_scope`;
`authorization_basis_ref`; plus `status` (current-state: `active` |
`superseded` | `restored`) and `supersession_link` (optional).
Versions append-only; one `active` version governs. Recovery meaning:
the last committed version governs; decisions cite the version they
applied.

**8. `redaction_case`** — fields: `case_id` (required);
`instruction_ref` (required); `target_spec` (required; **exact**:
span | field | object | referenced-portion, with locator);
`original_preservation_ref` (required → where the immutable original
is preserved under its correct protection level);
`visible_placeholder_form` (required); `state` (required;
current-state: `opened` | `searching` | `applying` | `verifying` |
outcome); `outcome` (controlled, the honest five-outcome family of
§15.6); `per_location_result_refs`; `verification_refs`;
`unresolved_location_refs` (→ record 19). Recovery meaning:
per-location checkpoints resume; the visible-output block stands
while open.

**9. `sealed_isolation_case`** — fields: `case_id` (required);
`trigger_ref` (required — exclusion event or instruction);
`protected_record_ref` (required after step 1 → record 10);
`step_checkpoint` (required; current-state; controlled, in order:
`created` | `protected_written` | `protected_verified` |
`exposure_replaced` | `ordinary_verified` | `complete` | `blocked` |
`failed`); per-step timestamps; `verification_refs`. Recovery
meaning: restart resumes exactly at the committed step (§15.3);
material stays output-blocked while non-`complete`.

**10. `protected_record_reference`** — fields: `protected_record_id`
(required; opaque — encodes nothing about content, location, or
path); `level` (required; `L1` | `L2`); `category_metadata`
(required; non-reconstructive); `status` (required; current-state:
`active` | `inert_preserved`). Recovery meaning: opaque resolution is
PEB-only; ordinary components hold only this reference.

**11. `protected_execution_request`** — fields: `request_id`
(required); `purpose` (required); `requesting_component` (required);
`authorization_basis_ref` (required); `opaque_ids` (required).
Append-only; PEB context only.
**12. `protected_execution_result`** — fields: `request_ref`
(required); `outcome` (required); `minimum_safe_result_descriptor`
(required — never the raw secret). Append-only; PEB context only.
Recovery meaning together: every L1 touch is reconstructable as
request→result pairs; a request without a result is an incomplete
protected execution and fails closed.

**13. `exclusion_event`** — fields: `event_id` (required); `rule_id`
(required); `detector_method` + `method_version` (required);
`outcome` (required; controlled: `excluded_to_sealed` | `held` |
`confirm_before_entry` | `redacted_parts` | `entered_restricted`);
`opaque_ref` (required where material moved). Append-only; **never
the excluded content**. Recovery meaning: holds persist; unclassified
holds stay held.

**14. `mixed_content_separation_event`** — fields: `event_id`
(required); `capture_ref` (required); `categories_removed`
(required); `opaque_ids` (required); `remainder_disposition`
(required: preserved | held-entire). Append-only. Recovery meaning:
separation already committed is never re-run on the same capture
(idempotency on `capture_ref`).

**15. `deletion_case`** — fields: `case_id` (required);
`instruction_ref` (required); `target_refs` (required); `state`
(current-state: `opened` | `searching` | `removing` | `verifying` |
outcome); `outcome` (required at terminal; **exactly the settled
five**: `protected_complete` | `protected_with_declared_limits` |
`incomplete` | `blocked` | `failed`); `per_location_result_refs`;
`verification_aggregate_ref`; `unresolved_location_refs`;
`history_record_ref` (required at terminal — identifier, time,
authority, outcome, verification; content preserved, never a
tombstone). Recovery meaning: per-location checkpoints resume;
`protected_complete` only via record-18 verification.

**16. `influence_removal_instruction`** — fields: `removal_id`
(required); `instruction_ref` + verbatim ref (required);
`normalized_scope_ref` (required); `affected_object_refs`
(accumulating via discovery); `permitted_internal_purposes` and
`prohibited_internal_purposes` (required — exactly as scoped:
retrieval, reasoning, connection, simulation, influence);
`visible_output_scope` (optional — only when Ness included it);
`lifecycle_state` (required; current-state; the §15.8 eleven-state
set); `per_consumer_ack_refs`; `verification_refs`;
`unresolved_refs`; `supersession_link` (optional). Recovery meaning:
unacked consumers resume; no full-enforcement claim without full
acknowledgment and verification.

**17. `restoration_or_supersession_instruction`** — fields:
`new_instruction_id` (required); `prior_instruction_ref` (required);
`restoration_scope_ref` (required — partial restoration is scoped
like any instruction); `state` (current-state: `received` | `applied`
| `complete`). Append-only body. Recovery meaning: the prior
instruction's history stays intact; the link chain is the authority
trail.

**18. `verification_result`** — fields: `verification_id` (required);
`case_or_instruction_ref` (required); `location_ref` (required);
`required_state` (required); `observed_state` (required); `outcome`
(required; controlled: `verified` | `failed_retryable` |
`failed_terminal`). Append-only; produced by VER, never by the
remover's own assertion. Recovery meaning: completion claims are
recomputed from these records only.

**19. `unresolved_location_result`** — fields: `location_ref`
(required); `case_ref` (required); `reason` (required);
`standing_effect` (required — the visible-output block this keeps
alive). Append-only. Recovery meaning: unresolved lists survive
restarts and keep blocks active.

**20. `safe_transformation_decision`** — fields: `decision_id`
(required); `source_refs` (required); `transformation_basis`
(required); `meaning_preservation_check_result` (required); `outcome`
(required; controlled: `transformed` | `withheld` |
`clarification_requested`). Append-only. Recovery meaning: a
transformation without a committed decision never leaves B7.

**21. `derivative_location_discovery`** — fields: `run_id`
(required); `adapter_id` + `method` + `method_version` (required);
`locations_found` (required); `per_location_status` (required);
`coverage_gaps` (required — reported, never silently dropped).
Append-only. Recovery meaning: discovery resumes per adapter; gaps
block `protected_complete`.

**22. `backup_handling_result`** — fields: `backup_set_identity`
(required); `case_ref` (required); `mode` (required; controlled:
`in_place_visibility_marking` | `exclusion_on_restore` |
`scheduled_supersession`); `per_set_outcome` (required — feeds the
case's five-outcome result); `restore_replay_confirmation` (required
on any restore — the active instruction set replayed before restored
material becomes visible or influential). Append-only.

**23. `person_group_control_configuration`** — fields: `rule_id`
(required); `version` (required); `subject_ref` (required —
person/group); `operations` (required); `scope_dimensions`
(required); `establishing_instruction_ref` (required);
`supersession_link` (optional). Versions append-only;
**stricter-only** — a weakening configuration is refused and the
refusal recorded (record 24 class). Recovery meaning: last committed
version governs.

**24. `privacy_failure`** — fields: `failure_id` (required);
`operation_ref` (required); `failure_class` (required);
`retryability` (required; `retryable` | `terminal`);
`state_at_failure` (required). Append-only. Recovery meaning: the
failure classification drives §15's retry-versus-halt behavior.

**25. `crash_recovery_event`** — fields: `recovery_id` (required);
`resumed_operation_ref` (required); `resumed_from_checkpoint`
(required); `committed_state_found` (required). Append-only —
recovery is itself one recorded operation. Recovery meaning: the
recovery trail is auditable and adds no evidence weight.

**26. `duplicate_prevention_event`** — fields: `event_id` (required);
`idempotency_key_matched` (required); `action_skipped` (required).
Append-only. Recovery meaning: replays are visible, harmless, and
weightless.

## 15. THE NINE PER-OPERATION MECHANICAL CONTRACTS

**15.0 Shared mechanical spine — stated once, binding identically on
every one of the nine contracts and part of each of them:** every
state transition commits atomically with its append-only history
event; **one operation, one log** — one operational record per real
operation, and recovery is itself a recorded operation (record 25);
**duplicate behavior** — every commit carries the contract's
idempotency key; a replayed commit is recognized, skipped, and
recorded (record 26); **crash recovery** — on restart, scan for
non-terminal operations of every contract, trust only committed
state, reconstruct nothing, resume from the last durable checkpoint;
**no double evidence** — linked records reference by identity,
repetition adds no weight, logs never raise evidence weight;
**minimum-material access** — every component receives only what its
authorized task needs, never sensitive content "so it can decide not
to show it"; **log privacy** — every record obeys §7Q's own access
rules (§14 catalog rule); **retry values** are consumed by reference
to the accepted retry mechanics (values open, never invented here);
**fail-closed direction** — on any uncertainty the protective side
wins: visible use withheld, secrets sealed, cases open, blocks
active, no completion claimed.

**15.1 Visible topic pause.** **Its own operation** — recorded as its
own instruction (`operations = visible_topic_pause`), **never
normalized into general hiding or the old combined pause/hide
label**, and carrying **no internal
effect unless Ness's scope explicitly included one**. Request record:
`privacy_instruction` + `normalized_scope` (topic; surfaces; persons;
time). Result/history: `topic_pause_record` (record 5) +
per-surface acknowledgments + history events. Operation identity:
`pause_id` from the instruction record; idempotency key: `pause_id`
+ surface name. Lifecycle: `active` → `partially_enforced` (some
surfaces unacked — protective non-terminal: the pause still governs
output evaluation everywhere) → `active` (all acked) → terminal
`superseded` | `restored`. Allowed transitions only as listed;
**reversal is by natural language** — Ness's clear reopening of the
topic qualifies through PIP as the restoring instruction (record 17).
Transactions/checkpoints: instruction commit atomic; one checkpoint
per surface acknowledgment. Partial completion: acked surfaces stand,
unacked resume. Retryable: surface-adapter transients; terminal:
conflicting instruction (→ the one-clarification path). Fail-closed:
while any uncertainty stands, the topic is withheld at output
evaluation on all scoped surfaces. Derivative handling: the pause
keys on topic scope at evaluation time — no content moves.
Verification: per-surface suppression check (record 18). Restoration:
record 17, never overwrite.

**15.2 Exclusion.** Request: an XDS Layer-A/Layer-B detection or a
Ness exclusion instruction. Result/history: `exclusion_event` (record
13) + any `sealed_isolation_case` (15.3) + history. Operation
identity: `exclusion_op_id` from capture ref + rule; idempotency key:
capture ref + detector id. Scope: the configured rule dimensions
(§8). Lifecycle: `detected` → `routed` (per configured outcome:
excluded-to-sealed | held | confirm-before-entry | redacted-parts |
entered-restricted) → terminal `recorded`; `held` is a protective
non-terminal (protected pre-ingest hold — never normal memory) until
classification. Transactions: detection + routing + event, one
transaction per item; checkpoint per item. Partial completion:
routed items stand; unrouted stay held. Retryable: storage
transients; terminal: none that release material — classification
questions go to the hold, not past it. Fail-closed: ambiguity → the
hold. Derivative handling: none exists yet at capture; MCS separation
recorded (record 14). Verification: item-location check (sealed or
held, never ordinary). Restoration: Ness's classification releases a
hold as a new instruction.

**15.3 Sealed isolation — the six-step crash-safe transfer.** Moving
material into sealed protection follows this exact committed order,
with the checkpoint (record 9) committed after **every** step and
recovery resuming at the committed step whether the crash fell before
or after any step:
1. **Create the protected record** (opaque id, level) — record 10.
2. **Write the protected raw** into SPS.
3. **Verify protected-side integrity** (record 18).
4. **Replace ordinary exposure** with the opaque reference plus
   non-reconstructive metadata.
5. **Verify ordinary locations clean** (record 18).
6. **Commit completion.**
This order structurally prevents **accidental disappearance** (the
raw is never removed from its ordinary location before the protected
copy exists and verifies — steps 1–3 strictly precede step 4) and
**simultaneous dual exposure** (from case open until step 6, the
material is blocked from visible output by a standing PDE rule, so
the brief dual existence between steps 3 and 5 is never visible; step
4 then removes ordinary exposure before completion). **L1 stays
PEB-only; L2 follows the accepted authenticated-private rules; no
human or ordinary-component path exists into sealed TSC archive
material** (§7, §16-TSC). Operation identity: `case_id`; idempotency
key: `case_id` + step. Lifecycle: the six checkpoints, then terminal
`complete`; `blocked` (protective non-terminal — output block held)
and terminal `failed` (retries exhausted; nothing partially leaks;
ordinary exposure stays withheld). Retryable: storage transients per
step; terminal: integrity failure. Partial completion: completed
steps stand exactly. Derivative handling: ordinary references become
opaque; discovery over sealed material runs PEB-only (§9a).
Verification: steps 3 and 5. Restoration: unsealing, where policy
permits it at all, is a new instruction — never a reversal edit.

**15.4 Hiding — thirteen named surfaces, visible suppression only.**
The hiding contract enforces across exactly these controlled surface
names, each with its own acknowledgment: **(1) chat responses; (2)
normal inspection views; (3) search results and visible retrieval;
(4) Story Layer visible surfacing; (5) Person-Box visible surfacing;
(6) Living State Web visible surfacing; (7) Computed View visible
surfacing; (8) simulation visible outputs; (9) notifications; (10)
exports; (11) tool-facing outputs; (12) shared screens; (13) outward
delivery / external sharing.** Request: `privacy_instruction`
(`hide`) + scope. Result/history: `hiding_record` (record 6) +
per-surface acknowledgments + verifications. Operation identity:
`hide_id`; idempotency key: `hide_id` + surface. Lifecycle —
**activation → verifying → active_verified**, with
**partially_enforced** (protective non-terminal; unverified surfaces
withhold at evaluation regardless), **blocked**, **failed** (both
protective — PDE keeps withholding the targets on all scoped
surfaces), and terminal **superseded | restored**. Transactions:
per-surface acknowledgment commits; checkpoints per surface. Partial
completion: verified surfaces stand; others resume. Retryable:
surface-adapter transients; terminal: a surface that cannot enforce —
recorded, the state stays `partially_enforced`, and PDE-side
withholding covers the gap. Fail-closed: hiding is **visible
suppression only** — it never removes internal influence, and no
uncertainty ever widens it into one. Derivative handling: targets are
matched at evaluation time across each surface's assembly path.
Verification: per-surface (record 18). Restoration: record 17.

**15.5 Restriction — the versioned ten-element rule.** Each
restriction is a versioned rule (record 7) carrying **targets;
allowed purposes; blocked purposes; allowed access classes; blocked
access classes; surfaces; source scope; time scope; operation scope;
authorization basis** — plus its effective version and supersession
link. Enforcement: PDE consults the active version **pre-retrieval
for any restricted visible purpose** (privacy filtering before
semantic ranking) **and again pre-output** at Layer-2; every decision
cites the rule version applied. **A restriction never silently
becomes influence removal** — internal-use effect exists only where
Ness's scope stated it (then carried by 15.8, separately). Operation
identity: `rule_id` + version; idempotency key: instruction ref +
version. Lifecycle: `received` → `active(vN)` → `superseded(vN+1)` |
`restored` (terminal per version; the rule family continues through
versions). Transactions: version commit atomic with history. Partial
completion: not applicable per version (a version either commits or
does not); consumers read the last committed version. Retryable:
storage transients; terminal: contradictory concurrent versions —
fail closed to the stricter reading and clarify. Fail-closed:
missing/ambiguous rule state → withhold for restricted purposes.
Derivative handling: the rule matches derived objects through the
same scope dimensions at evaluation. Verification: decision records
prove consultation (record 3 citing versions). Restoration: record
17 creating the next version.

**15.6 Redaction.** Request: `privacy_instruction` (`redact`) with an
**exact target** — span, field, object, or referenced portion.
Result/history: `redaction_case` (record 8) + per-location results +
verifications + unresolved lists. **The immutable original is
preserved under its correct protection level** — redaction changes
**visible output**, never the preserved original; the visible
placeholder and its history are recorded. Pipeline: `opened` →
`searching` (DDE — direct and indirect derivatives; indexes;
embeddings; caches; temporary files; exports; backups via BVH;
retained model-context traces) → `applying` (per location: visible
form replaced; a derived object built from multiple roots is
**rebuilt without the redacted portion**, recorded) → `verifying`
(record 18 per location) → outcome in the honest five-outcome family
(`protected_complete` only when every catalogued location verifies;
declared limits enumerated; `incomplete`/`blocked`/`failed` keep the
block). From case open until a protective terminal outcome, the
target is blocked from visible output. Operation identity: `case_id`;
idempotency key: `case_id` + location id. Checkpoints per location;
partial completion: done locations stand; crash mid-verification
re-runs verification only. Retryable: adapter transients; terminal:
authorization conflicts, integrity failures. Fail-closed: unresolved
locations stay listed (record 19) and keep the block alive.
Restoration: record 17; the preserved original makes restoration a
visibility change, never a reconstruction.

**15.7 Deletion — the settled five outcomes stand.** The deletion
contract is §9 + §9a + §11 + §12 completed with the contract
elements: request `privacy_instruction` (`delete_from_view`);
records: `deletion_case` (record 15) + discovery (21) + per-location
results + backup results (22) + verification (18) + unresolved (19) +
the terminal history record; operation identity `case_id`;
idempotency key `case_id` + location; lifecycle `opened` →
`searching` → `removing` → `verifying` → **exactly**
`protected_complete` | `protected_with_declared_limits` | `incomplete`
| `blocked` | `failed` (the first two terminal; the last three
protective — the visible-output block and the case's standing effects
survive restarts); transactions and checkpoints per location; partial
completion per §9; retryable/terminal per §15.0 and §9; fail-closed:
never described complete without §12 verification; derivative
handling per §9a incl. sealed (PEB-only) and backups (§11 — any
restore replays the active instruction set before restored material
becomes visible or influential); restoration: record 17 — content was
preserved, never destroyed, so restoration is visibility restoration.

**15.8 Influence removal — the full lifecycle.** Request:
`privacy_instruction` (`influence_remove`) + scope (exactly the
internal purposes Ness's words cover). Records:
`influence_removal_instruction` (record 16) + per-consumer
acknowledgments + verification + unresolved + history. Operation
identity: `removal_id`; idempotency key: `removal_id` + consumer id.
**Lifecycle — the complete state set with allowed transitions:**
`received` → (`awaiting_clarification` →) `discovering` (DDE resolves
affected objects and derivatives) → `enforcing` (each §16 consumer
contract acknowledges the block for its purpose classes) →
`verifying` → **`active_verified`** (the steady enforced state —
non-terminal: it continues governing every consumer check) — with
**`partially_enforced`**, **`blocked`**, and **`failed`** as
**protective non-terminal states**: while in any of them, **no
full-enforcement claim is ever made**, and **the protective block is
preserved per scope** — every consumer whose acknowledgment or
verification is missing treats the scoped material as blocked for the
scoped purposes; and terminal **`superseded`** | **`restored`**
(closed by a new linked instruction). The instruction **blocks only
the internal uses Ness actually included — nothing more, nothing
less — and never hides material visibly unless visible scope was
included** (then 15.4 runs as its own linked operation).
Transactions: per-consumer acknowledgment commits; checkpoints per
consumer. Partial completion: acked consumers stand; unacked resume.
Retryable: consumer transients; terminal for the attempt: a consumer
that cannot enforce — recorded, state `partially_enforced` or
`blocked`, protective block held. Fail-closed: uncertainty blocks the
use. Derivative handling: discovery keeps updating affected objects;
new derivatives inherit the block through the consumer checks.
Verification: per consumer and per purpose class (record 18).
Restoration: record 17; the original instruction keeps its full
enforcement trail.

**15.9 Restoration and supersession.** Always **a new linked
instruction referencing the earlier one — never an overwrite** and
never an edit of any prior record (record 17). It applies to every
contract above; partial restoration is scoped like any instruction
(§5). Operation identity: `new_instruction_id`; idempotency key: the
new instruction id + prior ref. Lifecycle: `received` → `applied`
(the prior instruction's `status`/`state` transitions to `restored`
or `superseded` atomically with the link) → terminal `complete` after
verification confirms the prior enforcement lifted **exactly as
scoped** — no wider, no narrower. Transactions: the link + the prior
transition, one transaction; checkpoints per affected enforcement
point. Partial completion: lifted points stand; others resume; until
complete, the stricter of old-and-new governs (fail-closed).
Retryable/terminal per 15.0. Derivative handling: lifting propagates
through the same consumer and surface acknowledgments that enforced.
Verification: record 18 per lifted point. History: the prior
instruction and its trail remain fully preserved.

## 16. INTERFACE BOUNDARIES — B7'S SIDE OF THE CONTRACTS

B7 owns these request/response contracts (design-level shape:
purpose-typed request with requesting-component identity, material
references, and operation context → PDE decision / PEB result /
enforcement acknowledgment, always with the decision record id), for
later wiring to: **front doors and §7E** (capture-exclusion and MCS
hooks, pre-ingest holds); **§7F retrieval** (eligibility filtering
before ranking; influence-set checks for retrieval purposes); **§7R
relevance** (privacy strictly before relevance; B7 supplies the
authorized candidate space, never a relevance signal); **§7G meaning
work** (internal-use authorization; influence-set checks; third-party
separation carried in inputs); **Story Layer**, **Person-Boxes**,
**Living State Web**, **Computed View** (internal-use authorization +
influence-set checks + third-party baseline enforcement on assembly);
**simulations** (the simulation-approval gate: no full simulation
starts without a recorded Ness approval instruction; labeling
enforced); **chat and visible output** (Layer-1 eligibility + Layer-2
review; withholding statements per the accepted safe-failure rule);
**exports, tools, notifications, external sharing** (default-restricted
purpose classes; explicit authorization-basis required per use);
**SACL** (B7 emits the §7Q first-factor result; chaining and the final
gate sequence remain **B-INT-6** — not completed here); **TSC**
(privacy precedence per §7E-TSC §25: exclusion metadata
non-reconstructive; sealed content routed to SPS; B15 owns the store);
**backup and recovery processes** (BVH adapters; restore-time
replay). Identity/Personal-Mode factor wiring remains **B-INT-5** —
not completed here. **What B7 consumes, precisely:** B7 consumes only
the currently established authorization facts available at evaluation
time — it does not assume which identity factors produced them or how
they were combined. The properly authenticated private Personal Mode
context is **established by machinery outside B7** — the accepted A26
policy and the future B-INT-5 mechanics — and B7 treats that context
as present **only when it has been established through that
later-defined path**. When the context's establishment is uncertain,
absent, or not yet defined, B7 applies the protective default:
external-grade restriction, and withholding of any output that would
require the private context.

## 17. MUST-NEVERS

B7 must never: change accepted A7 policy; merge visible suppression
with influence removal; redefine deletion as destruction; expose raw
Level-1 secrets; let ordinary components enter protected storage; let
relevance override privacy; make external use default-open; make one
permission apply to another purpose; create automatic
minor/vulnerability restrictions; create a volume-based permission
gate; silently harden third-party interpretation into fact; begin full
simulation without approval; let a log increase evidence weight; claim
success without verification; silently drop an unresolved derivative;
create production storage or code; complete B-INT-5 or B-INT-6.

## 18. DESIGN-COMPLETE CONDITION

B7 is complete for its mechanical scope only when all accepted A7
behavior can be enforced, resumed after crashes, verified, and audited
without: destruction; privacy/relevance inversion; accidental visible
exposure; accidental internal influence removal; unauthorized external
use; derivative leakage; secret leakage; duplicate execution; or false
completion claims. This candidate asserts readiness for that
condition **pending ChatGPT's independent audit and Ness's later
combined Bundle 5 acceptance** — nothing is closed by this file.

## 19. EXPLICITLY OPEN

ChatGPT's independent audit of this actual file; any verified
correction; Ness's later combined acceptance; receipts and
accepted-source copies; **B-INT-4; B-INT-5; B-INT-6; B-INT-7;
B-INT-8**; Bundle 5 consistency and closure; later Map or Master
integration; all empirical values (retry counts by reference to the
accepted values, verification schedule slots, any threshold); exact
serialization and final naming; all implementation and coding.

## 20. DRAFTING CHECKS, CHANGE REPORT, AND SELF-AUDIT

**Drafting checks — no-loss and consistency checks performed by the
drafter; NOT independent verification, NOT enforcement proof, and NOT
a claim that enforcement was tested or certified:** all six operations
remain separate (§3, §4
— distinct mechanisms and records) — consistent in drafting. Visible suppression and
influence removal remain separate (§3, §10 — IRR blocks only included
internal uses; visible scope only when included) — consistent in drafting. A7's two
Master supersessions preserved exactly, none added (§3; interpretation
free at policy level is consumed, not re-decided; simulation gate
enforced in §16) — consistent in drafting. No minor/vulnerability category rule
reappears (§3; PGC is explicit-instruction-driven only) — consistent in drafting. No
volume gate appears anywhere — consistent in drafting. Level-1 secrets inaccessible to
ordinary components (§7 — PEB-only handling, opaque references,
minimum-result egress) — consistent in drafting. Deletion non-destructive with exactly
the five outcomes (§9, §15.7) — consistent in drafting. Derivative discovery and verification
complete, including sealed material and backups, with gaps reported
(§9a, §11, §12) — consistent in drafting. Nine complete per-operation
contracts, each carrying request and result/history records, stable
operation identity, normalized scope, lifecycle states with allowed
transitions and terminal versus protective non-terminal marking,
transaction boundaries, durable checkpoints, idempotency key,
duplicate behavior, crash recovery, partial-completion recovery,
retryable-versus-terminal classes, fail-closed behavior, derivative
handling, verification, and restoration — with topic pause its own
reversible operation, the six-step sealed-isolation transfer order,
hiding across the thirteen named surfaces as visible suppression
only, the ten-element versioned restriction checked pre-retrieval
and pre-output, redaction preserving the immutable original, and
influence removal's full lifecycle never claiming full enforcement
while partial/blocked/failed (§15.0–§15.9) — consistent in drafting.
Every B7 record carries a complete design-level schema — exact field
names, required/optional, controlled values, referenced types,
privacy level, append-only or current-state role, schema version,
supersession link, recovery meaning — including the dedicated topic
pause, hiding, restriction, redaction, sealed isolation, deletion,
influence removal, restoration, verification, unresolved-location,
safe-transformation, protected-execution, exclusion, mixed-content,
backup, person/group, failure, and recovery records (§14) —
consistent in drafting. §5's normalization vocabulary, §10's
lifecycle, §14's records, and §15's contracts now use one consistent
operation and state vocabulary — topic pause separate from hiding
everywhere; the influence-removal lifecycle identical in §10, §14
record 16, and §15.8 — consistent in drafting. B-INT-5 and B-INT-6 remain open (§16, §19) — consistent in drafting.

**Change report:** this v1_3 file was produced by copying the
identity-verified v1_2 base and applying only the narrow consistency
corrections and their direct cross-references (title; the v1_3
version note; §3 separation sentence; §5 normalization list — twelve
separate controlled operations with the topic-pause identity rule;
§10 lifecycle list — the exact full set of §14 record 16 / §15.8;
§15.1 label precision; this block; the end line). All v1_2 schemas
and operation contracts are preserved untouched. v1_0, v1_1, and
v1_2 are preserved unchanged as historical candidate evidence, and
the B15 candidate is corrected separately.
Nothing existing was modified: Master V10, Defaults, cursorrules, the
Companion, the Map, the workflows and plan, accepted A7 and A26 and
their receipts, the supplied accepted A16 candidate, the A15 package
files, all historical candidates, and every prior receipt remain
byte-identical at the pinned head `bbf4e900…`. Nothing was committed
or pushed; no receipt or accepted-source copy was created; no code,
schema activation, database, store, migration, test, or Cursor
instruction was created; no implementation began.

**Self-audit (drafter's checks — not independent verification):**
mechanics only — no new meaning, no Ness question, no
reopened A7/A15/A16/A26 content; the A26 boundary now consumed with no
factor assumption and the protective default on uncertainty — consistent in drafting. Full Map B7 scope covered
(protected execution boundary; sealed storage; privacy-decision
records; influence-removal records and scope; interface behavior;
exclusion-detection structure; mixed-content separation; backup
mechanics; derivative discovery incl. sealed; verification;
person-specific control structure) — consistent in drafting. Every A7 open mechanical
item addressed (schemas §14; durable command/scope §5; evaluation
sequencing §6; protected execution/sealed storage §7; derivative
discovery §9a; mixed content §8; backups §11; verification §12;
interface §13; idempotency/transactions/duplicates/crash/partial per
contract §15.0–§15.9;
indexes and retrieval enforcement §9/§16; logging §14–§15; enforcement
contracts §16) — consistent in drafting. Fail-closed direction everywhere; A26 boundary
preserved as an input fact — consistent in drafting. Exactly one file for B7; zero
repository modifications — consistent in drafting.

---

*End of
`NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md`
— `CANDIDATE — NOT ACCEPTED — NOT ADOPTED — NOT BUILT`, awaiting
ChatGPT's independent re-audit of this actual file and Ness's later
combined Bundle 5 acceptance. v1_0, v1_1, and v1_2 are preserved
unchanged as historical candidate evidence. The machinery keeps A7's promises,
now contract by contract and record by record: six
separate controls, natural words becoming durable instructions,
secrets sealed behind one boundary, deletions hunted and honestly
verified through every copy and backup, influence removed exactly as
far as Ness said and no further, everything crash-safe, everything
logged once, nothing destroyed, nothing claimed without proof.
B-INT-4 through B-INT-8 and all implementation remain open. Nothing
existing changed; nothing was implemented.*

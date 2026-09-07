# NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md

## 0. STATUS BLOCK

**Status:** `CANDIDATE — NOT ACCEPTED — NOT ADOPTED — NOT BUILT`

**B-INT-8 only.** **Mechanical wiring only.** **No new policy** — §24's
meaning is settled; this file asks Ness nothing and invents no question.
**No implementation.** **Bundle 5 closeout is not begun. B-INT-8 does not
complete §7F, §7L, §7P, §7Q, §7R, or Person-Boxes** — it wires §24's
routes into their already-accepted boundaries.

**Date:** July 15, 2026.

**Register item:** B-INT-8 — Connection Capability waiting-area and
acceptance-route wiring (Bundle 5 — the final B-INT).

**VERSION NOTE (v1.1 — mechanical correction pass, July 15, 2026).** v1.1
was created by a direct copy of the untouched v1.0 source (SHA-256
`b3580af11c18b597f52b2965733dd3c67f61b6d665468eb2b6b5574fdfde413f`, 835
lines, 49,753 bytes; repository head
`df90f7c9ab40e6ea893797cf032e50047dc861bc` re-verified at correction start,
with no other B-INT-8 candidate, accepted source, or closure receipt in the
repository) followed by **exactly five correction groups**, with all
unrelated v1.0 text and meaning preserved: **(1)** later corrections and
disputes now control current use — one **§12C current-use resolution** runs
before every consumer use of an accepted connection, without rewriting
immutable history (§12C, §13A, §13D, §14, §15, I7–I9, crash 18/19/21);
**(2)** **`verification_unavailable` is separated from `not_verified`** — a
failed direct-source verification is evaluated and set aside and never
remains an active proposal on that failed basis (§5A, §6, §11, §12A, I2–I3,
crash 9); **(3)** the compressed interface section is replaced by **one
complete I1–I11 table**, and every acceptance, rejection, correction, use,
and handoff route carries an explicit **route-level §7Q check** and
**immediately-before-commit owner revalidation** (§7, §15, §18); **(4)** the
**canonical-key compare-and-commit, the accepted record, its authority
proof, and the final proposal-decision event are ONE recoverable atomic
logical commit**, with idempotent authority events (§7, §9, §11, crash
6–8/10/13, I1/I4/I5); **(5)** a **durable Ness decision input
forward-completes in recovery only under §7B's ten conditions** — otherwise
a fresh Ness decision is required (§5B, §7B, crash 5–8/16, I4). **No §24
meaning changed. Nothing was accepted, adopted, or built.**

**VERSION NOTE (v1.2 — single I10 identity correction, July 15, 2026).**
v1.2 was created by a direct copy of the untouched v1.1 source (SHA-256
`51cd58166749dbe893f15c30e8cd5811e645a3be5f02a380951f3c5535330818`, 1,257
lines, 87,733 bytes; head `df90f7c9ab40e6ea893797cf032e50047dc861bc`
re-verified) followed by **exactly one consequential correction** found by
ChatGPT's independent audit of the actual v1.1 file: interface **I10** now
consumes the accepted **B-INT-6 §6A identities** correctly — operation
identity = **`output_operation_id`** (the one stable logical parent per
logical output), idempotency key = the **SEPARATE
`delivery_idempotency_key`** (derived from the request identity + the
destination; stable across every safe retry of the same logical output;
the duplicate-prevention scope for delivery; containing no mode epoch,
mode generation, privacy version, SACL version, PBR version, observability
version, owner version, or delivery-fence version), with B-INT-6's
separate **`delivery_attempt_id`** per individual attempt. **I10 creates
no new delivery identity, retry rule, or duplicate-prevention system** —
it consumes B-INT-6's accepted delivery lifecycle and crash behavior by
reference, and the B-INT-8 connection operation identity does not replace
B-INT-6's output and delivery identities. Only I10's identity cells and
its retry/recovery wording, this note, the title, one §23 sweep clause,
and the closing filename line changed; the other ten interfaces and all
five v1.1 correction groups are untouched. **No §24 or B-INT-6 meaning
changed. Nothing was accepted, adopted, or built.**

## 1. PLAIN PURPOSE

B-INT-8 connects **a possible relationship between two preserved things**
→ **§24's waiting area** when it has not been accepted → **the three and
only three approved acceptance bases** → **the lasting accepted-connection
record** → **Context Retrieval's use of accepted and pending
relationships** → **Person-Boxes' use of relevant connections without
bypassing their own identity rules** → and **privacy, access, uncertainty,
logging, retry, and crash recovery** throughout.

**It exists to make these impossible:** similarity becoming a connection;
two items being retrieved together becoming a connection; a pending
proposal becoming true through age or repetition; **acceptance increasing
certainty**; a generic connection silently proving who a person is; an
accepted-but-uncertain connection supporting a certain conclusion; a
rejected proposal repeatedly returning without genuine new evidence; and a
crash creating duplicate proposals or accepted records.

**Master §24 says it plainly, and this file carries it whole:** *"Context
Retrieval may use accepted connections, and may surface a direct recorded
relationship it encounters into the waiting area. It may never invent a
connection from similarity, timing, theme, or co-retrieval, and may never
accept a connection into the lasting record by itself. Acceptance happens
only through Ness's judgment, a direct source relationship, or an
authorized rule."*

## 2. GOVERNING AUTHORITY, REPOSITORY POINT, AND SOURCES READ

Authority order: (1) `NH_MASTER-20_CORRECTED_v10.md` — **Master V10 governs
every conflict, including conflicts with older status wording**; (2)
`NH_DECISION_DEFAULTS-S19_v2_2.md`; (3) `cursorrules`; (4)
`NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`.

**Repository point:** `nesgeva/NH-GOVERNANCE`, `main`, head
**`df90f7c9ab40e6ea893797cf032e50047dc861bc`**, verified at task start.
The delta from `6916d582…` was inspected: **exactly the two B-INT-7
acceptance files.** **A full-repository search found no B-INT-8 candidate,
no accepted B-INT-8 source, no B-INT-8 closure receipt, and no file
claiming to complete this wiring** — the only mentions are as an **open
dependency** in the Map, Master, Companion, and plan. **This is the
first.**

**Actual files read (not summaries).** **Master V10** `2d9ed4c6`: **§24
Connection Capability IN FULL** (the two internal responsibilities; the
lasting record's preserved fields; the waiting area and its three decision
states; **the three approved bases**; the similarity prohibition; how
accepted connections may be used; how pending connections may be used;
**the ONE-WAY RULE**; **the five source types**); **§0, §0A, §0B**; **§7E**
(where source and provenance facts enter); **§7F Context Retrieval in
full**; **§7G** where retrieved context and evidentiary status enter
readings; **§7L Person-Boxes in full**; **§7P** authority boundaries;
**§7Q** privacy, internal-use, and visible-output boundaries; **§7R**
relevance — **and its rule that relevance is neither evidence nor
authority**; **§25** identity and access where the current speaker's
authority matters; and **§7A's cold-reactivation rule** (*"Merely finding a
cold log does not reactivate it. Actual use in reasoning or a valid new
link may reactivate it. **Similarity alone does not establish a permanent
or accepted connection — connection rules from §24 still apply.**"*).
**Map v1.6** `33af648d`: C-7F, C-7L, C-7P, C-7Q, C-7R, C-24, B1, B4, B9,
B26, B-INT-5, B-INT-6, B-INT-8, B-INT-11, I.4. **Accepted packages,
consumed by reference and NOT reopened:** **A4** and the accepted **Bundle
2** retrieval/relevance completion package; **B1** context-retrieval
parameter architecture (`6c21ea02`); **B26** context-retrieval failure
architecture; accepted **Bundle 3 v1.2** and its acceptance record —
especially **A5**, **A14**, and **B4** (the Person-Box identity rules);
**B7** `7fda28e9`; **B9** `e8f4c3de` (retry values **by reference**);
**A26** `41e1f67d` and **B-INT-5 v1.5** `c4497281`; **B-INT-6 v1.3**
`4edaaadc`; and the accepted §7L/Person-Box material those files point to.
The **eight-bundle plan** `2d6483d1` — **Bundle 5's B-INT-8 entry and the
Bundle-complete condition govern this package's boundary.**

## 3. THE RECORDKEEPER — AND WHAT IT IS NOT

The **Connection Capability Recordkeeper (CCR)** [proposed] owns exactly
two things: **the waiting area's proposal records** and **the lasting
accepted-connection records**, plus its own §0B operational log.

**It owns nothing else.** It is **not** a privacy authority (B7/§7Q), an
identity authority (§7L/SIA), an access authority (SACL/§25), a retrieval
authority (§7F/LMAC), a relevance authority (§7R), a source/provenance
authority (§7E and the source owners), or a rule-creation authority (§7P).
**It never becomes the authority that created or expanded a rule** — it
**records the match and references the rule.**

**And §7R's rule binds everywhere below: relevance is neither evidence nor
authority.**

## 4. THE SETTLED TWO-PART STRUCTURE

### Part 1 — the lasting connection record

**Holds ONLY deliberately accepted connections.** Each accepted record
preserves: **exactly what it links**; the **connection type**;
**direction** where the type is directional; the **decision status**;
the **certainty**; the **acceptance basis**; **who or what supplied the
acceptance authority**; the **supporting evidence or reason** — **kept
separate from the confirmer**; the **five source-type labels** of the
supporting material; **timestamp and version**; and **correction and
dispute history through new linked records.**

**Multiple connection types are NEVER merged into one record.** Master's
own illustrative list — **transcript of; attachment to; same source or
conversation; same event; before or after; correction of** — **remain
SEPARATE connection records even when they link the same endpoints.**

**This list is illustrative, not a closed vocabulary.** The type is carried
as a **versioned type-and-direction contract** [proposed]:
`connection_type_id` + `type_version` + `directionality`
(`directional` | `symmetric`), with the **type registry owned outside
B-INT-8** and **future type additions left open** (§21). **No
implementation serialization is chosen here.**

### Part 2 — Context Retrieval for the current operation

**Context Retrieval CREATES NO LASTING CONNECTION RECORD BY ITSELF.** It
may: **use accepted connections**; **use a pending proposal ONLY as an
investigation guide**; and **report that it encountered a directly recorded
relationship** (§13C).

**Its retrieval audit preserves what was retrieved, why, and which accepted
connection or pending investigation hint was used** (§13D).

**Retrieving two things together is NEVER a connection and NEVER creates a
proposal.**

## 5. THE THREE — AND ONLY THREE — ACCEPTANCE ROUTES

**Similarity, timing, shared themes, model interpretation, and
co-retrieval are NOT an approved basis.** They may help N.H **search and
compare**. **When no approved basis establishes a connection, N.H leaves
the relationship UNKNOWN AND UNLINKED** (Master §24).

### 5A. ROUTE A — DIRECT RECORDED RELATIONSHIP

**A direct recorded relationship is directly verifiable from source or
provenance** — e.g. **an attachment directly attached to a specific
message**; **a transcript directly generated from a specific audio file.**

**A self-establishing direct-source relationship MAY enter the lasting
record without Ness manually confirming it** (Master §24 explicitly permits
this, bypassing the waiting area).

**Its acceptance basis is `direct_source_relationship`** [proposed value] —
and **it is NEVER labeled as Ness's personal confirmation.**

**Two separate entry paths:**

**A-1 — the source/provenance owner supplies it.** An **authoritative
source/provenance owner** supplies a **directly verifiable** relationship
to the CCR. **After deterministic verification** (by that owner, not by the
CCR), **the accepted record may be committed directly** (§7A).

**A-2 — §7F encounters what appears to be a direct relationship.** §7F may
**submit a candidate report with exact immutable source references**. **§7F
itself may NEVER accept it.** **A candidate report is NOT a proposal:**
`connection_candidate_report_id` and `connection_proposal_id` are **separate
identities**, and **a §7F candidate report never automatically becomes a §24
proposal.** The source/provenance owner's verification has **exactly three
outcomes** (§12A, I3):

- **`verified_self_establishing`** — the source/provenance owner has
  directly verified the relationship. **The direct-source route may
  proceed — only through §7A's atomic route**, with its
  immediately-before-commit revalidation of the source owner, the owner
  version, the immutable evidence references, §7Q authorization, and the
  canonical-key state.
- **`verification_unavailable`** — the candidate report is **preserved** and
  marked **verification-pending or technically blocked.** It has **no
  factual force**, **no identity force**, **cannot support a recommendation
  or action**, **is not an accepted connection**, and **may never be
  represented downstream as verified direct-source evidence.** Technical
  retries follow the accepted **B9 classifications by reference**, and **no
  retry invents a successful verification.** It may be exposed to §7F
  **only** as investigation guidance that is **explicitly marked
  unverified**, **explicitly marked investigation-only**, **separated from
  evidentiary context**, and **currently authorized by §7Q** — it does
  **NOT** automatically become a normal §24 pending proposal.
- **`not_verified`** (or a contradictory source-owner result) — the
  candidate report **and the actual owner result are preserved**, the
  report is marked **evaluated and set aside**, and **no §24 proposal is
  created or preserved solely on that failed direct-source basis.** It is
  **not** exposed through the pending-proposal investigation route, is
  **not** repeatedly resurfaced, and the failed verification is **never
  converted into uncertainty evidence.** **The relationship remains unknown
  and unlinked.**

**A later relationship may still enter only by:** **genuine new
direct-source evidence**; **Ness's separate explicit confirmation** —
recorded as `ness_confirmation`, **never relabeled as direct-source
acceptance**; or a **separately valid narrow authorized rule** — which
**preserves the failed direct-source verification history without treating
it as supporting authority.**

**Never direct-source verification:** **similarity; timing; theme overlap;
model interpretation; co-retrieval.**

### 5B. ROUTE B — NESS EXPLICITLY STATES OR CONFIRMS IT

**The proposal must be bound to ALL of:** the **exact `connection_proposal_id`**;
the **exact proposal version**; the **exact endpoints**; the **exact
connection type**; the **certainty CURRENTLY SHOWN**; and the **exact
decision-surface version.**

**The acceptance event must prove an EXPLICIT Ness choice under the current
accepted identity and access rules** (§25 / B-INT-5 — **consumed, never
re-invented**).

**Never consent:** **silence; inactivity; failure to answer; continued
conversation; merely opening the proposal.**

**Acceptance PRESERVES the proposal's existing certainty** unless **Ness
separately and explicitly supplied a different certainty statement.** **The
acceptance action ALONE NEVER RAISES CERTAINTY** (Master §24).

**A stale proposal version can NEVER be accepted silently: fail closed, and
show the current version through the accepted B-INT-6 output chain**
(§7Q-first, SACL-second, fence revalidated).

**The same protection binds CRASH RECOVERY:** a **durable Ness decision
input may be forward-completed only under §7B's ten conditions** — the
exact proposal version must still be the **current decision-eligible
version**, with **valid integrity**, a **valid B-INT-5 authority context
for recovery**, a **matching decision-surface version and displayed
certainty**, and **no conflicting acceptance, no rejection, no
correction-caused staleness, no superseding proposal version, and no
authority or privacy block.** **A stale acceptance input is NEVER silently
rebound to a new proposal version**, and **a correction or new-evidence
version NEVER automatically inherits an earlier Ness decision** (§7B,
crash 5–8, 16).

**The exact required identity factor and interface presentation remain with
the accepted §25 / B-INT-5 owners.** **No new fingerprint, PIN, or Personal
Mode requirement is invented here.**

### 5C. ROUTE C — A NARROW RULE NESS EXPLICITLY AUTHORIZED

**The rule must ALREADY EXIST under its proper authority owner (§7P).**
The CCR may consume it **only when ALL of these are verifiable:**

- **stable `rule_id`**; **exact `rule_version`**; **the explicit Ness
  authorization reference**; the **declared scope**; the **eligible
  endpoint types**; the **eligible connection types**; the
  **source/provenance conditions**; the **activation state**; the
  **revocation or supersession state**; and its **current applicability to
  THIS EXACT relationship.**

**A broad permission such as "connect related things" is INSUFFICIENT.**

**A model judgment, a similarity score, or a retrieval result can NEITHER
create NOR widen the rule.**

**If the rule does not match EXACTLY, no acceptance occurs.**

**The CCR records the rule match and references the rule. It does NOT
become the authority that created or expanded it.** **Rule-creation policy
is NOT designed here** — B-INT-8 **consumes already-authorized rules
only.**

## 6. THE WAITING AREA

**Location and decision status are SEPARATE concepts:**
- the item is **physically/logically in the waiting area**;
- **its decision status is `undecided`** until an **accepted** or
  **rejected** decision occurs.
- **The waiting location is NOT a fourth decision status.**

**An undecided proposal:** **waits indefinitely**; **does NOT expire into
acceptance**; **does NOT become more certain through age**; **has NO
factual or identity force**; **does NOT alter lasting understanding**;
**does NOT authorize Person-Box linking or merging**; **does NOT support a
recommendation or external action**; and **may guide investigation ONLY**
(§13B).

**Master's own words: "While waiting, a pending proposal has no force."**

**The waiting path holds two DIFFERENT objects that never collapse into one
another:** **candidate reports** (§5A Route A-2 — awaiting or having
received source-owner verification) and **proposals** (§24's waiting area
proper). **A candidate report is not a proposal**, carries a **separate
identity**, and **enters the proposal path only through an approved
basis.** A `verification_unavailable` report **stays a verification-pending
candidate report with no force of any kind**; a `not_verified` report is
**evaluated and set aside and leaves the active waiting path entirely** —
it neither waits as a proposal nor resurfaces (§5A, §12A, I2–I3, crash 9).

## 7. ATOMIC ACCEPTANCE AND REJECTION — COMPARE-AND-COMMIT

**One implementation-neutral compare-and-commit boundary, keyed to the
canonical relationship key (§9).** **No intermediate coordination state may
ever be mistaken for acceptance.**

**THE ATOMIC RULE — binding on ALL THREE acceptance routes.** The
**canonical-key compare-and-commit is the SAME recoverable logical
operation** that commits: the **accepted-connection record**; the **exact
authority proof**; the **exact authority-event identity** (§9's
`authority_event_key`); the **final proposal-decision event** where a
proposal exists; and the **parent operation checkpoint.** **Authority
evidence must already be durable before the accepted record becomes
authoritative, or be durably included inside the same atomic logical
commit.** **No accepted connection may exist without recoverable proof of
exactly one of:** a **direct source**; **Ness confirmation**; or an
**authorized rule.** The duplicate check, the accepted-record creation, and
the authority-event write are **never separate racing steps:** no window
exists between the duplicate check and the commit through which a second
record can slip, and **no crash can leave an accepted connection without
its authority proof** (crash 6–8, 10, 13).

### 7A. THE DIRECT-SOURCE ROUTE

1. **immutable direct-source evidence**;
2. **verification from the ACTUAL source/provenance owner** (never the CCR,
   never §7F, never a model) — the outcome must be
   **`verified_self_establishing`** (§5A; `verification_unavailable` and
   `not_verified` never reach this route's commit);
3. **immediately-before-commit revalidation of ALL of:** the **exact source
   owner**; the **source-owner version**; the **immutable evidence
   references**; the **source-owner verification result**; **§7Q
   internal-use authorization for this commit**; the **canonical
   relationship key and duplicate state**; and the **authority-event
   identity** (§9);
4. **ONE atomic logical commit** (the §7 atomic rule) that **contains or
   durably references ALL of:** the **source-owner verification**; the
   **source-owner ID and version**; the **immutable evidence refs**; the
   **`direct_source_relationship` basis**; the **exact authority-event
   ID**; the **accepted connection**; and the **CRK compare-and-commit
   result**;
5. **operational completion.**

**No Ness-confirmation label is added.** Basis =
`direct_source_relationship`.

**Crash semantics:** **crash BEFORE the atomic commit → no accepted
connection exists.** **Crash AFTER it → recovery finds ONE complete
accepted connection WITH its authority proof — and the same authority event
is never appended again** (§9 authority-event idempotency; crash 8, 10).

### 7B. THE NESS-ACCEPTANCE ROUTE

**FOUR SEPARATE IDENTITIES, never mistaken for one another:**

1. the **durable Ness decision input** (`ness_decision_input`, §11) — the
   durable evidence of what Ness explicitly selected;
2. the **final `connection_decision_event`** — the proposal's committed
   decision status;
3. the **accepted-connection record**;
4. the **Ness-confirmation authority event.**

**The durable Ness input proves what Ness selected. It is NOT itself:** the
**accepted connection**; the **final proposal status**; the **authority
event**; or the **completed logical commit.**

**Route steps:**

1. **exact current proposal version**;
2. **valid explicit durable Ness decision input**, under the current
   accepted identity and access rules (§25/B-INT-5 — **consumed, never
   re-invented**);
3. **immediately-before-final-commit verification of ALL of:** the **exact
   current proposal ID and version**; the **exact endpoints**; the **exact
   type and direction**; the **certainty shown**; the **decision-surface
   version and integrity**; the **explicit Ness decision input**; the
   **current accepted B-INT-5 identity/access authority reference**; **§7Q
   internal-use authorization for this commit**; the **proposal and CRK
   duplicate state**; and the **absence of any conflicting committed
   decision, correction, rejection, or supersession**;
4. **ONE atomic logical commit** (the §7 atomic rule) that **binds ALL
   of:** the **exact proposal version**; the **valid durable Ness input**;
   the **current authority context**; the **accepted record**; the **final
   `accepted` decision event**; the **Ness-confirmation authority event**;
   and the **CRK compare-and-commit result**;
5. **operational log completion.**

**The accepted connection, its authority proof, and the proposal's
`accepted` decision are ONE RECOVERABLE LOGICAL COMMIT** — recovered
together, never one without another (crash 6–8).

**FORWARD-COMPLETION IN RECOVERY — ALL TEN CONDITIONS, or a fresh Ness
decision.** A durable Ness decision input may be forward-completed **only
when ALL of these remain true:**

1. it is **bound to the exact proposal ID and version**;
2. **that proposal version is still the current decision-eligible
   version**;
3. its **integrity is valid**;
4. the **B-INT-5 identity/access authority context remains valid for
   recovery**;
5. the **decision-surface version and displayed certainty match the durable
   input**;
6. **no conflicting acceptance has committed**;
7. **no rejection has committed**;
8. **no correction has made that proposal version stale**;
9. **no superseding proposal version has committed**;
10. **no authority or privacy rule now blocks completion.**

**If ANY condition fails:** do **NOT** forward-complete; **preserve the old
durable Ness input as history**; **keep or mark the old proposal version
stale or superseded**; **fail closed**; **require a fresh Ness decision
against the current visible proposal version**; and **surface the current
version only through B-INT-6.** **A stale acceptance input is never
silently rebound to the new proposal version. A correction or new-evidence
version never inherits the earlier Ness decision automatically** (§5B,
crash 5–8, 16).

### 7C. THE AUTHORIZED-RULE ROUTE

1. **exact rule version**;
2. **current active authorization**;
3. **exact scope match**;
4. **source-condition match**;
5. **FINAL RULE REVALIDATION IMMEDIATELY BEFORE COMMIT, of ALL of:** the
   **rule owner**; the **exact rule version**; the **active state**; the
   **revoked/superseded state**; the **exact scope match**; the **eligible
   endpoint types**; the **eligible connection types**; the **source
   conditions**; the **current applicability to THIS exact relationship**;
   **§7Q internal-use authorization for this commit**; the **canonical
   relationship key and duplicate state**; and the **authority-event
   identity** (§9);
6. **ONE atomic logical commit** (the §7 atomic rule) that **binds ALL
   of:** the **exact rule ID and version**; the **final rule
   revalidation**; the **Ness authorization reference for the rule**; the
   **exact scope match**; the **source-condition match**; the **accepted
   record**; the **authorized-rule authority event**; and the **CRK
   compare-and-commit result**;
7. **operational completion.**

**A rule revoked or superseded before commit CANNOT be used** — the final
revalidation is what catches it (crash 12–13).

### 7D. REJECTION

**The durable Ness rejection input and the final rejection decision event
are SEPARATE identities — exactly as in §7B** — and **the input alone is
never the committed rejection.**

1. **exact current proposal version**;
2. **explicit valid durable Ness rejection input**;
3. **immediately-before-commit verification of ALL of:** the **exact
   current proposal ID and version**; the **explicit Ness rejection
   input**; the **current B-INT-5 authority context**; **§7Q internal-use
   authorization for this commit**; the **decision-surface integrity**; the
   **absence of an already committed conflicting outcome**; and the
   **rejection-suppression identity**;
4. **durable rejection decision event**;
5. **repeat-suppression registration**;
6. **operational completion.**

**No lasting accepted connection is created.**

## 8. CERTAINTY, DECISION STATUS, AND THE FIVE SOURCE TYPES

**Certainty vocabulary (settled):** `possible` | `likely` | `uncertain` |
`disputed` | `near-certain`.

**Decision status (exactly three):** `undecided` | `accepted` | `rejected`.

**They are COMPLETELY SEPARATE.** Binding rules, carried from Master §24:

- **`accepted` NEVER means `certain`.**
- **Accepting a proposal NEVER increases certainty.**
- **Repetition NEVER increases certainty.**
- **A log entry NEVER increases certainty.**
- **Direct-source authority establishes the recorded STRUCTURAL
  relationship only — within its evidence, and no further.**
- **An accepted-but-uncertain connection can NEVER silently support a
  certain conclusion.**
- **When uncertainty materially affects a claim, an interpretation, a
  statement about a person, a recommendation, or an action, THE
  UNCERTAINTY MUST BE MADE CLEAR** (delivered through B-INT-6).

**B-INT-8 invents NO numeric certainty mapping and chooses NO rule for
which evidence produces which label.** It defines **the slot, its owner,
its preservation, and fail-closed behavior** — nothing more.

**The five source types (Master §24), each evidence or support item
carrying EXACTLY ONE:**

1. **`source_material`** — actual Origins or other preserved records.
2. **`prior_interpretation`** — readings or tellings; **visibly
   interpretation, NEVER presented as original evidence.**
3. **`assumption`** — temporarily accepted for exploration; **not a
   confirmed relationship.**
4. **`unknown`** — **not known, not filled in — and it stays unknown.**
5. **`invented_simulation_material`** — created only inside a simulation;
   **it must stay VISIBLY simulation material and must NEVER silently
   establish a real-world relationship.**

**They are NEVER collapsed, and one is NEVER silently promoted into
another.** **The source type is SEPARATE from the acceptance route, the
certainty, the decision status, the relevance, the identity, and the access
permission.**

## 9. DUPLICATE PREVENTION — THE CANONICAL RELATIONSHIP KEY

**`canonical_relationship_key` (CRK)** [proposed], built from **at
minimum**: the **endpoint identities**; their **endpoint versions or
immutable provenance references** where required; the **connection type**;
the **directionality**; and the **type version**.

- **Symmetric types: endpoint order is NORMALIZED** (a deterministic
  ordering of the stable endpoint identities), so `A↔B` and `B↔A` produce
  **one** key.
- **Directional types: DIRECTION IS PRESERVED** — `A→B` and `B→A` are
  **different relationships** and never collapse.

**Binding duplicate rules:**

- **Same logical endpoints + same type + same direction → ONE logical
  proposal / accepted relationship.**
- **Different connection types remain SEPARATE** — **never one giant
  combined record.**
- **A pending proposal and its later accepted record are linked parts of
  ONE operation history — not competing relationships.**
- **A retry NEVER creates another accepted record.**
- **A direct-source route and a Ness/rule route racing on the same
  relationship CONVERGE THROUGH THE CANONICAL KEY** — one winner, the other
  absorbed (`connection_duplicate_absorbed`).
- **Multiple valid acceptance bases may be recorded as SEPARATE SUPPORTING
  AUTHORITY EVENTS** — but they **do NOT create duplicate accepted
  connections and do NOT increase certainty merely by repetition.**

**AUTHORITY-EVENT IDEMPOTENCY.** Every authority event carries a **stable
`authority_event_key`** [proposed], built from **at minimum:** the
**accepted-connection ID or CRK**; the **acceptance-basis type**; the
**exact authority/source/rule reference**; and the **exact
authority/source/rule version.** **A retry must recover the existing
authority event or absorb the duplicate attempt — it must NEVER create
repeated copies of the same authority proof.** **Multiple genuinely
different valid bases** may be preserved as separate supporting authority
events; **repeated copies of the SAME basis are not separate support, add
no evidence weight, and increase no certainty** (§7's atomic rule; crash
6–8, 10, 13).

## 10. REJECTION AND GENUINE NEW EVIDENCE

**When a proposal is rejected:** **preserve the rejected proposal and its
decision event**; **do NOT delete, rewrite, or hide its history**; **do NOT
resurface the same proposal repeatedly**; **do NOT reinterpret silence as
reversal**; **do NOT automatically retry the decision.**

**Master §24: rejected is "recorded, not resurfaced for repetition, but not
sealed permanently — genuine new evidence may create a new linked
proposal."**

**A later proposal may be created ONLY on GENUINE NEW EVIDENCE.** It must:
**have a NEW proposal identity**; **link back to the rejected proposal**;
**state the exact NEW-EVIDENCE DELTA**; **preserve the old rejection**;
**use the SAME canonical relationship key** where it is the same logical
relationship; and **avoid counting the old and new proposal as two votes.**

**NOT genuine new evidence:** a **formatting change**; a **model
rewording**; **another retrieval of the same evidence**; **repeated
similarity**; **time passing**; **repeated co-retrieval.**

**B-INT-8 chooses NO threshold for "genuine."** The judgment belongs to the
**accepted source/evidence owners**, and **where it cannot be established,
the design FAILS CLOSED** — no new proposal.

**`connection_rejection_suppression_registry`** [proposed] — keyed by the
**CRK**, it records that a rejection stands and **suppresses repeat
surfacing** until a **linked new-evidence delta** is verified by its owner.

## 11. THE PROPOSED MECHANICAL RECORDS

**All `[proposed]`** (the governing files supply no names). **All carry
REFERENCES, never copied endpoint content.** **All append-only.** **None is
an authority.** **None adds evidence weight.**

**`connection_endpoint_ref`** — `object_type`; **stable object ID**;
**batch/store or source provenance** where needed; **immutable
version/reference**; **privacy classification reference**. **References,
not content.**

**`connection_proposal_record`** — `connection_proposal_id` + **version**;
`connection_operation_id`; **the CRK**; **endpoint refs**; **connection
type + direction**; **proposed acceptance-basis route**; **supporting
evidence refs**; **the five source-type labels**; **certainty**; **decision
status**; **prior rejected-proposal reference** where applicable;
**new-evidence delta reference** where applicable; **created-at and
source-owner versions**; **privacy and authority references**; and, where
the proposal originated from a Route A-2 report, the **separate
`connection_candidate_report_id` carried as provenance only** — **the
report and the proposal remain separate identities, a report never
automatically becomes a proposal, and no proposal is created or preserved
solely on a failed (`not_verified`) direct-source basis** (§5A).

**`accepted_connection_record`** — `accepted_connection_id`; **the CRK**;
**exact endpoint refs**; **type + direction**; **decision status
`accepted`**; **certainty — UNCHANGED from the accepted proposal or the
supplied authority evidence**; **acceptance basis** (`direct_source` |
`ness_confirmation` | `authorized_rule`); **exact acceptance-authority
references**; **supporting evidence refs**; **source-type labels**;
**accepted-at**; **correction/dispute links — containing ONLY links already
known at this record's commit time** (§12C: **an already committed accepted
record is never modified to add future correction or dispute links**; every
LATER correction, clarification, dispute, replacement, or supersession
event **points BACK to this immutable record**); **schema and record
version**; **integrity reference**.

**`ness_decision_input`** [proposed] — the **durable evidence that Ness
explicitly chose accept or reject**: the **exact proposal ID and version it
is bound to**; the **decision-surface version and displayed certainty**;
the **§25/B-INT-5 authority context reference**; and an **integrity
reference.** **It proves what Ness selected — it is NOT the accepted
connection, NOT the final proposal status, NOT the authority event, and NOT
the completed logical commit** (§7B).

**`connection_decision_event`** — the **exact `accepted` / `rejected` /
still-`undecided` decision fact**, and **the proposal version it applies
to**. **A separate identity from `ness_decision_input`.**

**`connection_authority_event`** [proposed] — the **durable authority proof
of an acceptance**: the **acceptance-basis type** (`direct_source` |
`ness_confirmation` | `authorized_rule`); the **exact authority/source/rule
reference and version**; the **accepted-connection ID or CRK**; and the
**stable `authority_event_key`** (§9). **Committed inside the same atomic
logical commit as the accepted record** (§7) — **an accepted connection
without a recoverable authority event cannot exist.**

**`connection_correction_event`** — adds **correction, clarification,
dispute, or superseding information** **without changing the earlier
proposal or accepted record**. **No destructive removal is invented.**

**`connection_use_event`** — the **consuming operation**; the **purpose**;
the **original accepted-record ID and version**; the **current-use chain
consulted** (§12C); the **current-use resolution result**; the **exact
connection or proposal version ACTUALLY used**; the **correction, dispute,
and supersession event references consulted**; **whether it was accepted
evidence/context OR pending investigation guidance only**; the **preserved
certainty and how it was preserved**; **whether uncertainty had to be
surfaced, and the output uncertainty behavior where applicable**; **any
non-use and its reason**; and the **result or failure reference**. **It is
a LOG OF USE — never another vote for the connection, and it never makes
the connection more current or more certain.**

**`connection_duplicate_absorbed`** — duplicate suppression, **adding no
evidence weight**.

**Also:** **`connection_operation`** (the one parent);
**`connection_candidate_report`** — §7F's Route A-2 submission, carrying
its **own `connection_candidate_report_id`** (a **SEPARATE identity** from
any `connection_proposal_id` — **a candidate report never automatically
becomes a proposal**), its **exact immutable source references**, **how it
was encountered**, its **verification outcome**
(`verified_self_establishing` | `verification_unavailable` |
`not_verified`), and its **lifecycle state** (§12A);
**`connection_rejection_suppression_registry`** (§10); and
**`connection_recovery_event`** (§16).

## 12. THE FULL LIFECYCLE

### 12A. Parent operation lifecycle

`requested_or_detected` → `source_facts_gathered` → `approved_basis_check`
→ `duplicate_check` → `proposal_preparation` → `proposal_committed` →
`waiting_undecided` → (`direct_source_verification_pending` |
`ness_decision_pending` | `authorized_rule_verification_pending`) →
`acceptance_prepared` → **terminal:** `accepted_commit` | `rejected_commit`
| `blocked` | `failed` | `completed`.

**Who supplies each transition:** the **source/provenance owner**
(verification); **Ness** (the explicit decision, under §25/B-INT-5); the
**§7P rule owner** (rule validity); the **CCR** (only the record commits and
its own operational state); **B7/§7Q** (privacy permission); **§7L** (any
Person-Box consequence — never the CCR).

**A self-establishing direct-source relationship may go from
`source_facts_gathered` → `approved_basis_check` → `duplicate_check` →
`accepted_commit` WITHOUT entering `waiting_undecided`** (Master §24).

**Candidate-report sub-lifecycle (Route A-2) — SEPARATE from the proposal
lifecycle:** `submitted` → (`verification_pending` | `technically_blocked`)
→ **terminal:** **`verified_self_establishing`** (hands to §7A's atomic
route) | **`evaluated_and_set_aside`** (a `not_verified` or contradictory
owner result — **leaves the active waiting path; creates and preserves NO
proposal on the failed basis; is not resurfaced**). **A
`verification_unavailable` report stays `verification_pending` or
`technically_blocked`, with NO force of any kind** (§5A, §6, I2–I3,
crash 9).

### 12B. Proposal decision status — exactly three

**`undecided` | `accepted` | `rejected`.** **The waiting location is NOT a
fourth status.** **`undecided` never ages into `accepted`.**

### 12C. Accepted-connection current-use state — LATER CORRECTIONS AND DISPUTES CONTROL CURRENT USE

**Append-only status events** [proposed]: **`current`**; **`disputed`**;
**`corrected_or_superseded_for_current_use`**. **Prior records are NEVER
erased**, and **no "final truth closure" state is invented.**

**TWO SEPARATE NAMESPACES, never confused:** the **certainty value
`disputed`** lives in the **`certainty` field** (§8); the **current-use
state `disputed`** lives in the **separate `current_use_state` namespace**
[proposed] and means only *"this accepted record has a later dispute."*
**Separate field names keep the two from ever being read as one another.**

**IMMUTABLE HISTORY.** The original **proposal**, the
**accepted-connection record**, the **final proposal-decision event**, and
the **supporting authority event** remain **immutable.** **An already
committed accepted record is NEVER modified to add future correction or
dispute links** — its correction/dispute links may reference **only events
already known at its commit time.** **Every later correction,
clarification, dispute, replacement, or supersession event points BACK to
the earlier immutable record.** A **reverse lookup or derived current-use
view** may discover the later events, but **it is not another authority and
never rewrites the original record.**

**THE CURRENT-USE RESOLUTION STEP.** Before **any** accepted connection is
used by **§7F**, **§7L**, **visible output**, a **recommendation**, an
**action-related consumer**, or **any other downstream reasoning
operation**, **one implementation-neutral current-use resolution** must
resolve **ALL of:**

1. the **exact accepted-connection ID and version**;
2. **every later correction, clarification, dispute, and supersession
   event**;
3. their **integrity references**;
4. their **owner/authority references**;
5. the **currently applicable relationship version**;
6. the **current-use state**;
7. the **original certainty — kept separate from the current-use state**;
8. **current §7Q authorization**;
9. **current influence-removal status.**

**Required outcomes:**

- **`current`** — the exact resolved accepted version may be considered,
  under: its **preserved certainty**; **current privacy and access
  authorization**; its **exact acceptance basis**; its **source-type
  labels**; and its **current correction/dispute chain**.
- **`disputed`** — the **dispute travels with every use**; it **cannot
  silently support a certain conclusion**; **any materially affected output
  must surface the uncertainty through B-INT-6**; and it **can never be
  treated as identical to an undisputed accepted relationship.**
- **`corrected_or_superseded_for_current_use`** — the earlier record
  **remains preserved history** but **is NOT used as the current
  relationship**; the **exact replacement record may be followed ONLY after
  its own integrity, authority, privacy, access, and current-use checks**;
  and **no replacement is inferred merely because the old record was
  disputed.**
- **Unresolved, contradictory, unavailable, or corrupt status chain → FAIL
  CLOSED:** do **NOT** use the connection; do **NOT** strengthen a claim;
  do **NOT** produce an identity consequence; do **NOT** support a
  recommendation or action; do **NOT** disclose hidden material.

**A correction changing endpoints, connection type, direction, or type
version creates:** a **new proposal or accepted-relationship version** as
applicable; a **new correct canonical relationship key**; and an
**append-only link from the correction event to BOTH the old and the new
records.** **The old canonical relationship key is NEVER mutated.**

**§7F and §7L must NEVER use a stale accepted version merely because its
original record still exists.**

## 13. §7F CONTEXT RETRIEVAL WIRING — THREE SEPARATE ROUTES

### 13A. Accepted connections

§7F may retrieve and use accepted connections **through LMAC**, under:
**§7Q internal-use authorization**; **one completed §12C current-use
resolution for the exact accepted connection — BEFORE use, every time**;
the **current purpose and scope**; the **accepted B1/A4 relevance
configuration**; **B26 failure behavior**; the **exact CURRENTLY APPLICABLE
accepted-connection version resolved by §12C — never a stale version merely
because its original record still exists**; **preserved certainty**; and
**preserved source types**.

**The context package MUST mark:** that the relationship **is an accepted
connection**; its **exact type**; its **certainty**; its **acceptance
basis**; its **source/evidence references**; its **resolved current-use
state and the correction/dispute chain consulted** (§12C); and **whether
uncertainty — including a `disputed` current-use state — materially limits
use**.

**An accepted connection MAY help retrieve the linked material.** **It may
NOT:** override positional context; silently repair positional context;
widen privacy or access; **turn an uncertain relationship into a certain
claim**; or **prove identity merely because one endpoint belongs to a
Person-Box.**

### 13B. Pending investigation guidance

§7F may query a pending proposal **only to search, retrieve, compare, and
check for genuine source evidence.**

**The investigation request must carry:** the **exact proposal ID and
version**; the **endpoint candidates**; the **connection type being
investigated**; the **certainty**; and the **explicit marker
`investigation_only_pending_connection`** [proposed].

**Search results returned because of that guide REMAIN SEPARATED from
evidentiary context.** **The prompt and every downstream consumer NEVER
receive the pending relationship as an established fact.**

**The investigation result MAY:** confirm direct source evidence **through
the actual source owner**; reveal **genuine new evidence**; or **leave the
relationship unknown.** **It may NEVER itself accept the relationship.**

**A `verification_unavailable` candidate report may enter this route ONLY**
when it is **explicitly marked unverified**, **explicitly marked
investigation-only**, **separated from evidentiary context**, and
**currently authorized by §7Q** (§5A). **An `evaluated_and_set_aside`
(`not_verified`) report NEVER enters this route** (§5A, §12A).

### 13C. The §7F candidate-report route (Route A-2)

When §7F encounters a **direct recorded relationship**: it **submits exact
immutable source references**; it **records how it encountered them**; it
**does NOT claim acceptance**; it **does NOT infer from similarity or
timing**; **the source/provenance owner verifies — with exactly the three
§5A outcomes** (`verified_self_establishing` | `verification_unavailable` |
`not_verified`); **a candidate report is not a proposal and never
automatically becomes one**; and **only the CCR commits any proposal or
accepted record.**

### 13D. Required §7F audit additions

Record: the **exact accepted connection or pending proposal used**; its
**exact version**; the **original accepted-record ID and version**; the
**§12C current-use chain consulted and the resolution result**; the **exact
version ACTUALLY used**; the **correction/dispute/supersession event
references consulted**; **accepted-versus-investigation-only status**;
**certainty**; **source-type labels**; **why it was eligible**; **what it
changed about search scope**; **what was retrieved**; **whether the
relationship affected a later claim**; **how uncertainty was preserved, and
any required output uncertainty behavior**; **any non-use after
evaluation — including non-use because of a dispute, correction,
supersession, or an unresolved status chain — and its reason**; and
**failure, omission, and truncation.** **The retrieval log adds NO evidence
weight and never makes a connection more current or more certain.**

## 14. PERSON-BOX WIRING — SEPARATION FIRST

**Bundle 3's accepted identity rules are preserved EXACTLY and consumed,
never re-decided:** **completely clear identity → automatic Person-Box
link**; **unclear identity → pending unresolved identity anchor**;
**similar names alone are insufficient**; **definitely the same person →
automatic join**; **less than definite → pending merge proposal**;
**ordinary clear links and joins require NO invented manual approval**;
**all history is preserved.**

**Generic §24 connections are kept SEPARATE from §7L identity links,
unresolved identity anchors, Person-Box merge proposals, and Person-Box
joins.**

**The ten binding rules:**

1. A generic accepted connection may be supplied to §7L as **one
   provenance-bearing relationship reference.**
2. **§7L decides how it may be used, under A5/B4.**
3. **The generic connection NEVER itself proves that an endpoint belongs to
   a person.**
4. A **direct attachment or transcript relationship** may organize material
   in a Person-Box view **only after the material's identity link is
   separately valid.**
5. **A pending generic connection creates NO Person-Box link, anchor,
   merge, or join.**
6. **A generic connection about two people does NOT combine their
   Person-Boxes.**
7. **A Person-Box's own clear/unclear test is NEVER replaced by §24
   acceptance.**
8. **A §7L identity or merge proposal is NOT duplicated inside the generic
   waiting area.**
9. When the same underlying evidence matters to both systems,
   **cross-reference the distinct records — never merge their state
   machines.**
10. **Correction in either system NEVER rewrites the other system's
    history.**

**And before ANY §7L handoff:** the **§12C current-use resolution must have
completed** for the accepted connection being supplied, and **route-level
§7Q internal-use authorization must hold for the handoff itself** — a
**disputed, corrected, superseded, or unresolved** connection is handed to
§7L **only as §12C permits**, and **a stale accepted version is never
handed to §7L merely because its original record still exists** (§12C, I8,
crash 21).

## 15. PRIVACY, ACCESS, AND VISIBLE OUTPUT

**Accepted B7, B-INT-5, and B-INT-6 apply throughout — and none of their
authority is duplicated here.**

- **§7Q internal-use authorization runs BEFORE any retrieval or internal
  connection use.**
- **Route-level §7Q internal-use authorization runs immediately BEFORE:**
  every **proposal commit**; every **accepted-record commit**; every
  **rejection commit**; every **correction/dispute commit**; every **§7F
  use**; and every **§7L handoff** (§7, §18).
- **The §12C current-use resolution is itself privacy-bound:** it resolves
  **current §7Q authorization** and **current influence-removal status**
  before any use — and **a connection whose influence Ness has separately
  instructed removed is not used, regardless of its current-use state.**
- **Visible proposals, decisions, status messages, and uncertainty
  statements pass the accepted B-INT-6 chain: §7Q FIRST; SACL SECOND; the
  current B-INT-5 fence and owner versions revalidated; only then
  delivery.**
- **A waiting-area record NEVER grants access to its endpoints.**
- **An accepted connection NEVER grants access to either endpoint.**
- **A connection does NOT widen a Person-Box permission.**
- **Level-1 material is represented through OPAQUE PROTECTED REFERENCES
  only.**
- **No connection record copies raw protected content.**
- **Other speakers CANNOT accept a proposal as Ness or authorize a
  Ness-owned rule** (§25/SACL decides who is speaking; the CCR only
  consumes that decision).
- **Shared or observable output uses the accepted shared-output ceiling.**
- **Hidden material is NEVER indirectly disclosed** — never *"these are
  connected but I cannot show why."*
- **A withheld relationship produces NO signal that hidden material
  exists.**
- **Influence removal, hiding, restriction, redaction, and
  deletion-from-view retain their accepted SEPARATE meanings.**
- **A connection log or record NEVER bypasses a separate influence-removal
  instruction.**

## 16. CRASH AND RESTART

**Universal recovery rules:** **no durable proposal record → no proposal
exists**; **a candidate report and a proposal remain DIFFERENT objects in
recovery — one is never recovered as the other**; **a `not_verified`
candidate report never remains or becomes an active proposal**; **a durable
undecided proposal remains undecided indefinitely**; **a displayed proposal
without a durable decision remains undecided**; **a durable Ness decision
input may be forward-completed ONLY under §7B's ten conditions — the exact
proposal version, valid integrity, valid authority context, privacy
authorization, and the absence of any conflicting committed state**; **an
accepted connection and its authority proof CANNOT split — recovery finds
both or neither**; **an unknown commit result is QUERIED BY OPERATION ID,
CRK, PROPOSAL ID/VERSION, ACCEPTED-RECORD ID WHERE RESERVED,
AUTHORITY-EVENT KEY, AND FINAL DECISION-EVENT IDENTITY BEFORE ANY RETRY**;
**an already committed accepted record is RECOVERED, NEVER RECREATED**; **a
correction/dispute chain is resolved (§12C) before any later use**; **an
authorized rule must be REVALIDATED if no accepted commit exists**; **a
rejected proposal REMAINS rejected**; **no crash changes certainty**; **no
crash promotes pending to accepted**; **no crash grants access or any
identity consequence**; **no restart automatically resurfaces or re-asks an
undecided or rejected proposal**; **no missing evidence, decision, or
authority is reconstructed.**

| # | Crash boundary | Authoritative committed truth | Recovery action | Idempotency key | Retry? | Fresh Ness action? | Duplicate prevention | Fail-closed result | Audit event |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Before proposal identity is reserved | Nothing | Nothing exists. Re-detect normally. | — | Yes (detection) | No | — | No proposal | operation failed |
| 2 | After identity reservation, before the proposal record | The reserved id only | **No proposal exists** (no durable record). Reuse the id or abandon it. | `connection_proposal_id` | Yes | No | Reserved id cannot become a second proposal | No proposal | operation failed |
| 3 | After proposal commit | The **proposal record** | It stands as **`undecided`**. **Never auto-decided.** | CRK + proposal id | No decision retry | No | CRK converges | Waits | proposal committed |
| 4 | While an undecided proposal waits | The proposal | **Remains undecided indefinitely.** **No aging into acceptance.** | CRK | No | No | — | Waits | — |
| 5 | After Ness SEES a proposal, before a decision | The display event only | **Remains UNDECIDED.** **Seeing is not consent.** **No re-ask on restart.** A later decision binds to the **then-current proposal version** — the display of a version later made stale authorizes nothing (§7B). | proposal id + version | No | **Yes, for any decision** | — | Undecided | display logged |
| 6 | **After Ness's durable decision INPUT, before the atomic accepted commit** | **The durable Ness decision input only** (bound to the exact proposal version + authority context) — **NOT the accepted connection, NOT the final proposal status, NOT the authority event** | **Forward-completion is allowed ONLY after revalidating the exact proposal version, authority context, privacy authorization and absence of conflicting committed state (§7B's ten conditions). Otherwise a fresh Ness decision is required** — the old input is preserved as history, the stale version is kept or marked, and the current version is surfaced only through B-INT-6. **Never silently rebind to a newer version.** | CRK + proposal id + version + `authority_event_key` | Yes (idempotent, only after full revalidation) | **Yes — whenever any §7B condition fails** | CRK compare-and-commit inside the ONE atomic commit | **No acceptance; no silent rebinding** | forward-completion, or fresh-decision-required, recorded |
| 7 | After the atomic accepted commit, before the parent operation checkpoint | **The ONE atomic commit — accepted record + authority proof + final `accepted` decision event (where a proposal exists)** | **Recover the COMPLETE atomic commit — never recreate, never one part without the others.** A partial or contradictory state → **FAIL CLOSED**; resolve by operation ID and CRK **without manufacturing missing authority.** Complete the parent checkpoint idempotently. | `accepted_connection_id` / CRK + `authority_event_key` | Yes | No | The existing atomic commit absorbs | **Partial or contradictory state → blocked until resolved** | checkpoint completed |
| 8 | **Unknown accepted-commit outcome** | **Unknown** | **QUERY by operation ID, CRK, proposal ID/version, accepted-record ID where reserved, `authority_event_key`, and final decision-event identity BEFORE any retry.** If the complete atomic commit is present → recover it. If absent → re-run the route's checks (on the Ness route: §7B's ten conditions). **Never blind-retry.** | CRK + `authority_event_key` | Only after the query | Only if a §7B condition fails | CRK + authority-event idempotency | **Blocked until resolved** | uncertainty recorded |
| 9 | During direct-source verification | Whatever the **source owner** committed | **Re-ask the source owner** (technical retries per accepted B9, by reference). **The CCR never verifies for it.** Outcomes are exactly §5A's three: `verified_self_establishing` → §7A's atomic route; `verification_unavailable` → the report stays **verification-pending/technically blocked, with no force**; `not_verified`/contradictory → **evaluated and set aside — no proposal is created or preserved on the failed basis, and it is not resurfaced.** | `connection_candidate_report_id` + operation id | Yes (technical only — **no retry invents success**) | No | **A candidate report is never recovered as a proposal** | No acceptance; **a failed basis never waits as a proposal** | verification outcome recorded |
| 10 | After `verified_self_establishing`, before the atomic commit | The **owner's verification** | **Revalidate immediately before commit** (§7A: exact owner, owner version, evidence refs, verification result, §7Q, CRK/duplicate state, authority-event identity), then **commit ONCE atomically** — the accepted record and the `direct_source_relationship` authority proof together. **Crash before → no accepted connection.** | CRK + `authority_event_key` | Yes | No | CRK + authority-event idempotency | No acceptance | direct-source authority event |
| 11 | During an authorized-rule match | The rule's own state | **Re-match from the CURRENT rule version.** | operation id | Yes | No | — | No acceptance | rule match failed |
| 12 | After rule match, before final revalidation | The match record | **Revalidate the rule** (activation, revocation, supersession, scope). | operation id | Yes | No | — | **Revoked/superseded → NO acceptance** | rule revalidation |
| 13 | After final revalidation, before commit | The revalidation | **Commit ONCE atomically** under the CRK — the accepted record, the authorized-rule authority proof, the exact rule ID/version, and the Ness authorization reference together (§7C). **If any doubt → revalidate again** (including §7Q and the duplicate state). | CRK + `authority_event_key` | Yes | No | CRK + authority-event idempotency | No acceptance | rule-authority event |
| 14 | During rejection | The decision event, if durable | **Complete the rejection** + suppression registration idempotently. | proposal id + version | Yes | No | — | Proposal stays undecided if nothing committed | rejection |
| 15 | After rejection commit, before the suppression checkpoint | **The rejection** | **Rejected stands.** Register suppression idempotently. | CRK | Yes | No | — | — | suppression registered |
| 16 | While appending genuinely new evidence to a **pending** proposal | The proposal's committed version | **Append-only**: the new evidence creates a **new proposal version**, never an in-place edit. **Certainty is not raised by the append.** **The new version does NOT automatically inherit any earlier Ness decision input** — an input bound to the earlier version is stale for the new one (§7B). | proposal id + version | Yes | **Yes, for any decision on the new version** | Version chain | Evidence unverified → not appended | evidence appended |
| 17 | While creating a **new proposal linked to a rejected one** | The old **rejection** | **The rejection stands.** Create the new proposal **once**, with its **new-evidence delta** and back-link. **Old and new are never two votes.** | CRK + new proposal id | Yes | No | CRK + suppression registry | **No verified delta → no new proposal** | new linked proposal |
| 18 | During a correction/dispute event | Whatever committed | **Append the correction event** — **never edit the earlier record**; the earlier record's own links stay as committed, and **the later event points BACK to it** (§12C). Where endpoints/type/direction/type-version change → a **new record or proposal version + a new CRK + an append-only link to BOTH** records. | correction id | Yes | No | **The old CRK is never mutated** | — | correction/dispute |
| 19 | While §7F is **using an accepted connection** | The retrieval's own committed state | **Nothing about the connection changes.** Re-retrieve under current authorization **and a FRESH §12C current-use resolution — a stale accepted version is never used merely because its original record still exists.** | retrieval op id | Yes | No | — | **Use fails closed; the connection is untouched; an unresolved or contradictory chain → no use** | use event |
| 20 | While §7F is **using a pending proposal as guidance** | The proposal (**still undecided**) | **The proposal is NOT advanced.** **Guidance is not evidence.** Re-run under current authorization. | retrieval op id | Yes | No | — | **No proposal, no acceptance** | investigation use |
| 21 | While §7L is **consuming an accepted connection** | **§7L's own committed state** | **§7L decides.** No Person-Box link/anchor/merge/join is created by the CCR. **The handoff is repeated only after a FRESH §12C current-use resolution and route-level §7Q authorization** (§14, I8). | §7L's op id | Yes | No | — | **No identity consequence** | §7L handoff |
| 22 | **Contradiction between a CCR record and its actual source, authority, or Person-Box owner** | **THE OWNER'S RECORD — always** | **FAIL CLOSED.** Record the contradiction; **block**; **never resolve it in the CCR's favour**; **surface uncertainty honestly.** | — | No | **Possibly — the owner decides** | — | **Blocked** | contradiction recorded |

## 17. RETRY

**Accepted B9 retry classifications and values are consumed BY REFERENCE.**
**No retry count, gap, timeout, or backoff value is invented here.**

**A technical retry may reuse the same stable operation ONLY where it
recreates NO authority and NO decision.**

**Never retry automatically:** a **Ness decision request**; an **undecided
proposal**; a **rejected proposal**; an **invalid or revoked rule**; a
**failed direct-source verification as though it succeeded**; a **semantic
or model judgment to manufacture an approved basis**; a **stale proposal
acceptance**; a **forward-completion whose §7B conditions failed**; or an
**authority-event append whose `authority_event_key` already exists — the
existing event is recovered or the duplicate absorbed, never re-appended**
(§9).

**A fresh Ness action is required for a new Ness decision.** **A rejected
relationship requires GENUINE NEW EVIDENCE and a NEW LINKED PROPOSAL — not
a retry of the old decision.**

## 18. THE INTERFACE TABLE

**Every I1–I11 boundary carries the same complete contract — the columns
below.** Where a cell says **n/a**, that is an **explicit judgment** (the
field does not apply to that boundary), **not an omission.** Route-level
§7Q and the immediately-before-commit revalidations are carried
per-boundary (§7, §15).

| I# | Caller | Receiver | Decision/authority owner | Request fields | Response fields | Operation identity | Idempotency key | Prerequisites | Immediately-before-commit revalidations | Committed success truth | Committed failure truth | Retry class | Crash recovery | Audit-event identity | §7Q privacy classification | §7Q authorization requirement | §25/B-INT-5 access reference | Current-use correction/dispute requirement |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **I1** — direct-source route | Source/provenance owner | CCR | **The source/provenance owner** (the verification) | Immutable endpoint refs; type + direction + type version; immutable direct evidence refs; owner verification result; owner ID + version | `accepted_connection_id` \| refused | `connection_operation_id` | CRK + `authority_event_key` | Deterministic **`verified_self_establishing`** verification by that owner (never the CCR, never §7F, never a model) | §7A: exact source owner; owner version; immutable evidence refs; verification result; **§7Q**; CRK + duplicate state; authority-event identity | The **ONE atomic commit** — accepted record + `direct_source_relationship` authority event + CRK compare-and-commit result (§7, §7A) | **No accepted record, no authority event** | Technical per accepted B9 (by reference); idempotent under CRK + `authority_event_key` | Crash 8–10 | Direct-source authority event + §19 children | References only; endpoint privacy classification carried | Route-level check inside the pre-commit revalidation | n/a — machine route; owner authority per §7E; no Ness identity factor invented | n/a at creation; **all later use via §12C** |
| **I2** — §7F candidate report | §7F | CCR | **Nobody yet — §7F may NEVER accept**; verification belongs to the source owner | Exact immutable source refs; how encountered; endpoint refs; apparent type + direction | `connection_candidate_report_id` — **NOT a proposal ID** | `connection_operation_id` | Candidate-report id + CRK | Exact immutable refs present; §7Q internal-use for the submission | n/a — no proposal or accepted record commits here | A durable candidate report in `submitted` state (§12A) | Refused — **no report; never an acceptance; never a proposal** | Per B9, idempotent on the report id | Crash 9 | Candidate detection | References only | Internal-use before submission | n/a | n/a |
| **I3** — verification | CCR | Source/provenance owner | **The source owner** | `connection_candidate_report_id`; endpoint refs; claimed direct relationship; immutable evidence refs | **Exactly** `verified_self_establishing` \| `verification_unavailable` \| `not_verified` | Operation id | Report id + owner + owner version | Exact immutable refs | n/a — the owner verifies; **the CCR never verifies for it** | A durable owner result bound to the report: `verified_self_establishing` → §7A's atomic route; `verification_unavailable` → report stays **verification-pending/technically blocked, NO force**, exposable only as explicitly-unverified investigation-only under §7Q (§13B); `not_verified`/contradictory → **evaluated and set aside — no proposal on the failed basis, not resurfaced, never uncertainty evidence** (§5A) | No owner result → the report unchanged, no force | Technical per B9; **no retry invents success** | Crash 9 | Verification outcome recorded | References only | Internal-use | n/a | n/a |
| **I4** — Ness decision | Ness decision surface (delivered through B-INT-6) | CCR | **NESS** (the decision) + **§25/B-INT-5** (identity/access authority — consumed, never re-invented; **no new fingerprint, PIN, or Personal Mode requirement invented**) | Proposal id + version; endpoints; type + direction; certainty shown; decision-surface version + integrity; **explicit durable Ness decision input**; §25/B-INT-5 authority context | Accepted \| rejected \| refused-stale (current version surfaced **only through B-INT-6**) | Operation id + `ness_decision_input` identity | Proposal id + version; on accept also CRK + `authority_event_key` | The **exact CURRENT decision-eligible proposal version**; an explicit choice — **silence is never consent** | §7B: exact proposal ID + version; endpoints; type + direction; certainty shown; surface version + integrity; Ness input; current B-INT-5 authority reference; **§7Q**; proposal/CRK duplicate state; absence of conflicting committed decision, correction, rejection, or supersession | §7B's **ONE atomic commit** — accepted record + final `accepted` decision event + Ness-confirmation authority event + CRK result; on reject, the durable rejection decision event + suppression (§7D) | Stale/conflicting/blocked → **NO acceptance**; the input preserved as history; **a fresh Ness decision required against the current version** | Forward-completion only under **§7B's ten conditions**; the decision request itself is never auto-retried | Crash 5–8, 16 | Durable input; final decision event; authority event; forward-completion or fresh-decision-required | The visible surface passes the B-INT-6 chain (§7Q first, SACL second, fence revalidated) | Route-level check inside the pre-commit verification | The current accepted identity/access authority | A correction that made the version stale **blocks completion** (§7B condition 8) |
| **I5** — authorized rule | Authorized-rule owner (§7P) | CCR | **§7P / the rule owner** (validity); the rule's force traces to **Ness's explicit prior authorization** | Rule id + version; Ness authorization ref; declared scope; eligible endpoint types; eligible connection types; source conditions; activation; revocation/supersession; current applicability | Applicable \| not_applicable | Operation id | CRK + `authority_event_key` | The rule **already exists** under §7P; **exact match on every item** — a broad permission is insufficient | §7C final revalidation: rule owner; exact version; active state; revoked/superseded; exact scope; eligible endpoint types; eligible connection types; source conditions; current applicability; **§7Q**; CRK + duplicate state; authority-event identity | §7C's **ONE atomic commit** — accepted record + authorized-rule authority event + rule ID/version + Ness authorization ref + CRK result | **No acceptance — the CCR never creates or widens a rule** | Per B9, idempotent; **revalidate again on any doubt** | Crash 8, 11–13 | Rule match; final revalidation; rule-authority event | References only | Route-level check inside the final revalidation | The rule's Ness-authorization provenance | n/a at creation; **all later use via §12C** |
| **I6** — investigation guidance | §7F | Waiting-area records (CCR read surface) | **§7F** (the retrieval) under §7Q — **the proposal is NOT advanced by use** | Proposal id + version; endpoints; type; certainty; the explicit `investigation_only_pending_connection` marker | Search/compare results — **SEPARATED from evidentiary context** | Retrieval op id | Retrieval op id | §7Q internal-use; marker present; `verification_unavailable` candidate material **only explicitly-unverified + investigation-only** (§13B); **`evaluated_and_set_aside` reports NEVER enter** | n/a — no commit; **guidance can never accept** | An investigation-use audit; the proposal unchanged, still `undecided` | No results; the proposal unchanged | Per B9 under current authorization | Crash 20 | Investigation use | Internal-use | Before use | n/a | n/a — pending, not accepted |
| **I7** — accepted-connection use | §7F (through LMAC) | Accepted-connection records | **§7F** (retrieval) + **B1/A4** (relevance config) + **B26** (failure behavior) | Accepted-connection id + version; purpose | A context package marked: accepted connection; exact type; certainty; basis; evidence refs; **resolved current-use state + the chain consulted**; uncertainty limits | Retrieval op id | Retrieval op id | §7Q internal-use; **one completed §12C current-use resolution — the CURRENTLY APPLICABLE version only** | A **fresh §12C resolution per use**; current §7Q | A `connection_use_event` carrying the §11 current-use fields; **may help retrieve; may NOT override or repair positional context, widen access, harden certainty, or prove identity** | Unresolved/contradictory/unavailable chain, or a superseded version without validated replacement → **no use, fail closed** | Re-retrieve under current authorization + a fresh resolution | Crash 19 | Use event | Internal-use; references only | Before use, and inside the §12C resolution | n/a | **REQUIRED** — never a stale version merely because the original record exists; `disputed` travels with use; material uncertainty surfaces through B-INT-6 |
| **I8** — Person-Box handoff | CCR | §7L (Person-Boxes) | **§7L — ALWAYS** | The **currently applicable** relationship version (§12C); endpoint refs; type; certainty; acceptance basis; source/evidence refs; privacy/access refs; resolved current-use state + chain refs | §7L's own decision | Accepted-connection id + §7L's own op id | The same pair | A **completed §12C resolution**; **route-level §7Q for the handoff itself** | Fresh §12C + §7Q before any repeat handoff | §7L's own committed state — the generic connection is **ONE provenance-bearing reference**; it **NEVER proves an endpoint belongs to a person** and creates **no link, anchor, merge, or join** | **No identity consequence** | Only with a fresh §12C resolution + §7Q | Crash 21 | §7L handoff | Internal-use; references only | Before the handoff | §7L's own accepted A5/B4 identity rules — **never replaced** | **REQUIRED** (§14) |
| **I9** — correction/dispute | Correction/dispute source (Ness, an owner, or an authorized source under its own authority) | CCR | **The correcting source's own authority** — the CCR records only | Target record + exact version; correction/dispute content refs; basis; owner/authority refs; integrity refs | `correction_event_id` | Operation id | Correction id | The target identified by **exact ID + version**; §7Q internal-use for the commit | Route-level **§7Q** + target-version existence immediately before commit | An **append-only** correction event **pointing BACK to the immutable earlier record** — the earlier record's own links stay as committed; endpoint/type/direction/type-version changes → a **new versioned record or proposal + a NEW CRK + an append-only link to BOTH**; **the old CRK is never mutated** (§12C) | No correction event; the earlier record untouched | Idempotent on the correction id | Crash 18 | Correction/dispute | References only | Route-level before commit | The correcting source's authority reference | **The event enters every later §12C resolution — it controls current use without rewriting history** |
| **I10** — visible output | CCR | B-INT-6 (visible output chain) | **The chain's own accepted owners** — B7/§7Q, SACL, B-INT-5 | Visible proposal/decision/status/uncertainty content refs (+ the resolved current-use state where an accepted connection materially affects output) | Delivered \| withheld | The accepted B-INT-6 **`output_operation_id`** — the **one stable logical parent** for this visible-output operation, never re-minted; **the B-INT-8 connection operation identity does NOT replace B-INT-6's output and delivery identities** | The **SEPARATE** accepted B-INT-6 **`delivery_idempotency_key`** — **derived from the request identity + the destination**; **stable across every safe retry of the same logical output**; **the duplicate-prevention scope for delivery**; **separate from `output_operation_id`**; containing **no mode epoch, no mode generation, no privacy version, no SACL version, no PBR version, no observability version, no owner version, and no delivery-fence version** | **§7Q FIRST; SACL SECOND; the B-INT-5 fence and owner versions revalidated; only then delivery** | The fence and owner versions, per accepted B-INT-6 | A delivery record per B-INT-6 | Withheld — **no indirect disclosure; no signal that hidden material exists** | Per accepted B-INT-6 behavior, **consumed by reference** — **each individual attempt uses B-INT-6's separate `delivery_attempt_id`**; the current epoch, generation, privacy, SACL, PBR, observability, and fence facts **attach to the attempt, never to the stable delivery key**; **I10 creates no new delivery identity, retry rule, or duplicate-prevention system** | **B-INT-6's own accepted delivery lifecycle and crash behavior, by reference** — nothing about the connection changes | Visible-output child | Visible output | First in the chain | Fence + owner versions revalidated | A `disputed` state materially affecting output **surfaces its uncertainty here** |
| **I11** — operational records | CCR | §0B / B-INT-11 | **The §0B law** | One parent log per real operation + children per §19 | Durable append | The parent operation id | One parent per real operation; stable child identities | A real operation — **no silent internal operation** | n/a | One parent + its children, append-only | A required audit event that cannot commit → **the operation fails closed** (§20) | Idempotent appends — **duplicates absorbed and adding nothing** | Logs are not truth evidence; recovery is keyed by the operation identities | Itself — **no recursive log-about-logging** | Log access follows §7Q/§25/compartment rules | Required for log access | Compartment rules | **Current-use logs never make a connection more current or more certain** |

## 19. §0B AND B-INT-11 RECORDKEEPING

**One parent operational log per real connection operation.** **Children:**
candidate report; source verification; **verification unavailable**; **not
verified / evaluated and set aside**; proposal creation; duplicate
absorption; waiting; **durable Ness decision input**; **final
proposal-decision event**; **authority event**; **atomic accepted commit**;
direct-source commitment; rejection; **rejection suppression**; rule
matching; **final rule revalidation**; new-evidence evaluation;
**current-use resolution**; **correction/dispute chain lookup**; **non-use
due to dispute or staleness**; §7F investigation use; §7F
accepted-connection use; §7L handoff; correction; dispute; failure; retry;
recovery.

**Binding rules:** **one real operation → one parent log**; **no recursive
log-about-logging**; **logs add NO evidence weight**; **repeated logs are
NOT repeated confirmation**; **duplicate authority logs add NO support**
(§9); **current-use logs never make the connection more current or more
certain** (§12C); **accepted, rejected, undecided, used, and
not-used outcomes are ALL recorded**; **evaluated-but-set-aside candidates
are recorded WITHOUT creating a proposal when no approved basis exists**;
**operational records are append-only and are themselves retrievable only
under their normal authorization**; **active/cold behavior follows
B-INT-11**; **cold reactivation occurs through ACTUAL USE or a VALID NEW
LINK — never similarity alone** (Master §7A); **recording a relationship
does NOT grant permission to read its endpoints**; **access to logs follows
§7Q, §25, and compartment rules**; and **separate influence-removal
instructions remain binding.**

## 20. FAIL-CLOSED

**Fail closed when:** no approved basis exists; the basis cannot be
verified; the proposal version is stale; **a proposal version has been
superseded**; **a conflicting decision, rejection, correction, or
supersession already exists**; **a Ness decision input is stale, or any of
§7B's ten forward-completion conditions fails**; endpoint identity is
missing or contradictory; the connection type or direction is invalid; a
source type is missing; certainty is missing or invalid; **Ness's authority
cannot be verified**; the authorized rule is **missing, revoked,
superseded, or out of scope**; **the owner, rule, or source version changed
before commit**; direct-source evidence is unavailable or contradictory;
**a source owner returns `not_verified`**; **candidate-report state is
confused with proposal state**; **a correction/dispute chain cannot be
resolved, or the current-use state is contradictory or unavailable**
(§12C); **a consumer requests a stale accepted version**; **the authority
proof and the accepted record are not durably bound in one atomic commit**;
**an authority-event result is unknown**; **the final route-level §7Q check
fails**; privacy or access authorization fails; the connection store or a
source owner is unavailable; **an accepted commit result is unknown**;
**§7F confuses pending guidance with evidence**; **§7L attempts to treat a
generic connection as identity proof**; **a record contradicts its actual
authority or source owner**; **an interface is exercised without its
required committed truth or recovery identity** (§18); or a required audit
event cannot be committed.

**Failing closed means:** **no lasting connection is created**; **no
pending relationship or proposal gains force**; **no stale relationship is
used**; **no Person-Box is linked or merged**; **no factual claim is
strengthened**; **no recommendation or external action is supported**;
**uncertainty is preserved honestly**; **certainty and history remain
preserved**; and **no hidden information is disclosed.**

## 21. WHAT REMAINS OPEN

ChatGPT's independent audit; Ness's later acceptance; accepted-source
placement and a closure receipt; **Bundle 5 final consistency review and
closeout**; later **Master and Map integration**; the **exact UI layout and
wording for the waiting area**; the **exact scheduling or surfacing policy
for undecided proposals**; **final serialization and field names**;
**storage technology**; **database choice**; **empirical values**;
**model/provider details**; **any future connection-type additions**; **any
future authorized-rule creation policy not already settled**; and **all
implementation** — code, schemas activated on disk, databases or production
stores, migrations, tests, runtime work, Cursor instructions, and live-disk
changes.

**B-INT-8 does not complete §7F, §7L, §7P, §7Q, §7R, or Person-Boxes.**

## 22. MUST-NEVERS

Never: change Master V10, the Defaults, `cursorrules`, the Companion, the
Map, or any accepted file; ask Ness to decide already-settled §24 behavior;
**create a connection from similarity, timing, shared themes, or
co-retrieval**; **create a proposal from similarity alone**; **let §7F
accept a connection**; **let a model approve its own proposed
relationship**; **let waiting or age become acceptance**; **let acceptance
raise certainty**; **let repetition become evidence**; **let a generic
connection prove person identity**; merge §24 proposals with §7L identity
or merge proposals; **copy endpoint content into connection records**; let
connection status grant privacy or access permission; **treat a rejected
proposal as deleted**; **automatically re-ask a rejected or undecided
proposal**; **rewrite connection history**; **let a `not_verified`
direct-source claim remain an active pending proposal on that failed
basis**; **let a candidate report automatically become a proposal**; **let
§7F or §7L use an accepted connection without a §12C current-use
resolution — or use a stale accepted version merely because its original
record still exists**; **mutate an already committed accepted record to add
future correction or dispute links**; **duplicate authority events**;
**split an accepted record from its authority proof**; **forward-complete a
stale Ness decision, or silently rebind an old Ness input to a new proposal
version**; **bypass §7Q on any acceptance, rejection, correction, use, or
handoff route**; invent certainty thresholds,
counts, scores, or algorithms; create a second Person-Box, retrieval,
privacy, access, or authority system; complete the Bundle 5 closeout; begin
implementation; create code, patch-ready pseudocode, schemas on disk,
stores, databases, migrations, tests, or Cursor instructions; mark this
accepted, adopted, integrated, implemented, or `PACKAGE_COMPLETE`; or commit
or push.

## 23. FULL-FILE SWEEP — CONSISTENCY, NO-LOSS, DUPLICATES, CRASH, PRIVACY, AUTHORITY

- **The one-way rule holds everywhere:** §7F may **use** accepted
  connections and may **surface** a direct recorded relationship into the
  waiting area; it may **never invent** a connection from similarity,
  timing, theme, or co-retrieval, and may **never accept** one (§4, §13) —
  consistent in drafting.
- **Only three bases exist**, with **Route A's two entry paths** and its
  **self-establishing direct commit** permitted exactly as Master allows —
  and **never labelled as Ness's confirmation** (§5) — consistent in
  drafting.
- **Certainty and decision status are fully separated**; **acceptance,
  repetition, and logs never raise certainty**; an **accepted-but-uncertain
  connection never silently supports a certain conclusion** (§8) —
  consistent in drafting.
- **The five source types are preserved, never collapsed or promoted**, and
  **invented simulation material can never silently establish a real-world
  relationship** (§8) — consistent in drafting.
- **Duplicates converge on the canonical key** — symmetric types normalized,
  directional types preserved, racing routes absorbed, **different types
  never merged**, and **multiple bases never becoming duplicate records or
  extra certainty** (§9) — consistent in drafting.
- **Rejection is preserved, never resurfaced, never auto-retried; a new
  proposal needs a verified new-evidence delta, back-links, and never counts
  as a second vote** (§10) — consistent in drafting.
- **Acceptance is atomic per route**, with the **Ness route's accepted record
  and decision event forming one recoverable commit**, and the **rule route
  revalidating immediately before commit** (§7) — consistent in drafting.
- **All 22 crash boundaries** name their authoritative truth, recovery,
  idempotency key, retry stance, whether fresh Ness action is needed,
  duplicate prevention, fail-closed result, and audit event — and **an
  owner-contradiction always fails closed in the OWNER's favour** (§16) —
  consistent in drafting.
- **Person-Boxes stay separate**: all ten rules carried; **a generic
  connection never proves identity**, and Bundle 3's clear/unclear tests are
  **never replaced** (§14) — consistent in drafting.
- **Privacy holds**: §7Q before internal use; **B-INT-6's §7Q-first,
  SACL-second, fence-revalidated chain** for everything visible; **no record
  grants access to its endpoints**; **Level-1 by opaque reference only**;
  **no indirect disclosure** (§15) — consistent in drafting.
- **No authority is duplicated** — the CCR owns only its records and its log
  (§3) — and **relevance is neither evidence nor authority** (§7R) —
  consistent in drafting.
- **Later corrections and disputes control current use** — immutable
  originals; later events point back; **one §12C resolution before every
  §7F, §7L, visible-output, recommendation, or action use**; `current` /
  `disputed` / `corrected_or_superseded_for_current_use` / fail-closed
  outcomes; certainty-`disputed` and current-use-`disputed` kept in
  **separate namespaces**; endpoint/type/direction/type-version corrections
  create a **new CRK** and **never mutate the old** (§11, §12C, §13, §14,
  §15, I7–I9, crash 18/19/21) — consistent in drafting.
- **`verified_self_establishing`, `verification_unavailable`, and
  `not_verified` are fully separated** — the candidate report and the
  proposal are **different identities**; a report never automatically
  becomes a proposal; a **failed direct-source basis never waits as a
  proposal**, is not resurfaced, and is **never converted into uncertainty
  evidence**; later entry only by genuine new evidence, `ness_confirmation`
  (never relabeled), or a separately valid rule (§5A, §6, §11, §12A, I2–I3,
  crash 9) — consistent in drafting.
- **Every I1–I11 boundary carries the complete contract** — caller,
  receiver, owner, request/response fields, operation identity, idempotency
  key, prerequisites, pre-commit revalidations, committed success and
  failure truths, retry class, crash recovery, audit identity, §7Q
  classification and authorization, §25/B-INT-5 reference, and the
  current-use requirement — **including I10's correct consumption of the
  accepted B-INT-6 §6A output identities: the stable `output_operation_id`
  as the operation identity and the SEPARATE stable
  `delivery_idempotency_key` (request identity + destination; no mutable
  epoch, generation, version, or fence facts) as the delivery
  duplicate-prevention scope, with `delivery_attempt_id` per attempt** —
  with **route-level §7Q immediately before every
  proposal, accepted-record, rejection, and correction/dispute commit and
  before every §7F use and §7L handoff** (§7, §15, §18) — consistent in
  drafting.
- **Acceptance is ATOMIC with its authority proof on all three routes** —
  the CRK compare-and-commit, the accepted record, the authority event, and
  the final proposal-decision event (where a proposal exists) are **one
  recoverable logical commit**; the durable Ness input, the final decision
  event, the accepted record, and the authority event are **four separate
  identities**; authority events are **idempotent under
  `authority_event_key`**; repeated copies of the same basis add nothing
  (§7, §9, §11, I1/I4/I5, crash 6–8/10/13) — consistent in drafting.
- **Stale proposal decisions cannot forward-complete** — recovery
  revalidates **§7B's ten conditions**; on any failure the old input is
  preserved as history, the stale version is marked, **a fresh Ness
  decision is required**, and the current version is surfaced **only
  through B-INT-6**; **no silent rebinding**; **no automatic inheritance**
  by corrected or new-evidence versions (§5B, §7B, I4, crash 5–8/16) —
  consistent in drafting.
- **No empirical value, threshold, count, score, or algorithm is invented**;
  **no new Ness question is asked** — the governing files revealed **no
  unresolved meaning choice** blocking safe completion (§8, §10, §21) —
  consistent in drafting.

---

*End of `NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md`
— `CANDIDATE — NOT ACCEPTED — NOT ADOPTED — NOT BUILT`, awaiting ChatGPT's
independent audit of this actual file and Ness's later acceptance. Two
things may sit near each other, arrive together, sound alike, and be
retrieved in the same breath — and still not be connected. Only the source
itself, Ness's own word, or a rule Ness wrote may say otherwise. Everything
else waits, without force and without expiry, and what is accepted is never
made more certain by having been accepted.*

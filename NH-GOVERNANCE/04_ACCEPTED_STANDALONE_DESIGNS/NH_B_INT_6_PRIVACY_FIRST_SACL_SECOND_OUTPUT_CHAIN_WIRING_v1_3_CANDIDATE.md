# NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md

## 0. STATUS BLOCK

**Status:** `CANDIDATE — NOT ACCEPTED — NOT ADOPTED — NOT BUILT.`

**B-INT-6 only.** **Mechanical wiring only.** **No new policy** — the
gate order is already settled in Master; this file asks Ness nothing and
invents no question. **No implementation.** **No Bundle 5 closure. No
CY-I closure. No B-CYCLE-4. B-INT-7 and B-INT-8 remain open.**

**Date:** July 13, 2026.

**Register item:** B-INT-6 — §7Q and SACL output-gate chaining (Bundle 5
— privacy, security, access, and TSC authority).

**Version note (v1_3):** one final narrow crash-safety and
record-consistency correction of v1_2 only (v1_2 SHA-256
`022e89c76a3b7f3801fadbfded9198972f6480d686ea33ee2ab0ec4a089f8817`;
890 lines; 56,176 bytes — **preserved unchanged, as are v1_0 and
v1_1**), containing **exactly three correction groups** and **no
redesign or expansion of the settled output chain**. **(1) The
channel-dispatch crash gap is closed.** v1_2 had a claim and an
attempt-started event, but nothing covered the seam where **control may
reach the channel BEFORE the local attempt event is durable** — so an
**absent `delivery_attempt_event` could be misread as "no call
happened."** v1_3 adds the **`delivery_dispatch_intent_event`**
[proposed], flushed **before** the channel is contacted: **dispatch
intent proves only that N.H was ABOUT TO contact the channel; the attempt
event proves the channel ACCEPTED THE HANDOFF; neither proves visible
delivery; only a positive channel acknowledgment does.** **Once the
dispatch intent is durable, the claim is `spent` and may never be
automatically reused**, and **a crash after it is `delivery_unknown` even
when the local attempt event is missing** — **never an automatic resend
merely because that event is absent.** **(2) `delivery_unknown` is now
truly exclusive:** the generic *"any non-terminal state may go to
discarded/withheld/failed"* sentence **explicitly excludes** it. A later
restriction, reduction, close, or restart **blocks every future retry and
may make the payload unavailable — but it NEVER rewrites unknown delivery
reality as `failed`, `discarded`, or `withheld`**, and **never prevents a
later channel confirmation from recording the historical fact that
delivery occurred.** **(3) The records and authority wording are now
internally exact:** the `delivery_claim_record` is **immutable and
append-only** (initial status `active`) with separate append-only
**`delivery_claim_state_event`** records for `spent` | `invalidated` |
`abandoned` (**coordination only, never authority**); `output_operation`
carries the settled **`delivery_idempotency_key`**; the non-delivery
receipt **proves the earlier attempt did not deliver and thereby makes a
retry ELIGIBLE — it authorizes nothing** (fresh §7Q, SACL, owner-version,
mode, and fence checks do); restart behavior is stated exactly (**the
epoch necessarily changes, every old active claim is invalid, no old
payload is replayed**); and the crash table's `formed_output_ref` is now
`delivery_payload_ref`. **No policy changed; no question asked; no new
authority or store added.**

**Version note (v1_2):** one final narrow consistency correction of
v1_1 only (v1_1 SHA-256
`6d1f8d5b1d8d38f0b0122312546b79fd1d40d6deaa705bae012bc154cb686e4e`;
726 lines; 44,753 bytes — **preserved unchanged, as is v1_0**),
containing **exactly three correction groups** and **no redesign or
expansion**. **(1) The last universal exactly-once overclaim is gone:**
the stage table's *"Deliver — the single commit point / exactly one
visible delivery per output operation"* is replaced by the truthful
five-step delivery sequence, the duplicate scope is stated as **bounded**
(promised only under a **verified channel idempotency contract on the
same stable token**; otherwise the guarantee is **no blind resend and no
automatic duplicate attempt after an unknown result**), and the stale
*"absorbed against the commit record"* is corrected — **there is no
`delivery_commit_record` in this design**; duplicate prevention now
references the **stable delivery key, the relevant claim and attempt,
and (where present) the confirmation receipt or the channel owner's
idempotency result.** **(2) `delivery_unknown` is now an honest
UNRESOLVED, NONTERMINAL state** — it can be neither terminal nor later
resolvable at once. A parent may sit **open** in `delivery_unknown`
without pretending success or failure, and it is **never silently
converted to `failed` or `delivered`, and never retried**, without one of
the permitted **channel-owner facts**: a late positive confirmation
(→ `delivered`), positive proof nothing was written (→ fresh validation
and a **new child attempt**), or **verified same-token deduplication**
(→ fresh validation and a **new child attempt**). **(3) Every actual
attempt now gets its OWN fresh claim:** because a claim binds
per-attempt gate, fence, and owner-version facts, **one old claim can
never authorize a later attempt.** Each attempt carries a fresh
`delivery_claim_id` bound to exactly one intended `delivery_attempt_id`,
with claim states `active` | `spent` | `invalidated` | `abandoned` — **an
old, spent, invalidated, or stale claim can never authorize a later
attempt**, and **the claim states are not a second delivery authority.**
**No policy changed; no question asked; no new authority or store
added.**

**Version note (v1_1):** one narrow correction pass on v1_0 only (v1_0
SHA-256
`da8ece3ef785129695c84c01a3b49ba351395f86ece6b8d63142969e297587c9`;
505 lines; 30,563 bytes — **preserved unchanged as historical candidate
evidence**), containing **exactly three correction groups** and **no
expansion or redesign**. **(1) Sending intent is separated from
confirmed delivery.** v1_0's single `delivery_commit_record` — written
*before* the channel write yet called an *"exactly-once delivery fact"* —
conflated two different truths. v1_1 uses **three**: a **delivery claim**
(durably reserving the one logical attempt; it proves only that sending
was **authorized and reserved**), a **delivery attempt event** (control
was actually handed to the channel), and a **confirmation receipt** (a
**positive, channel-owned acknowledgment**). **No local record can prove
external delivery**, and **exactly-once visible delivery may be claimed
only where the channel owner supports a verified idempotency contract on
the same stable delivery token** — otherwise B-INT-6 guarantees **no
blind resend and at most one automatic attempt after an uncertain
result**, never universal exactly-once. **Ness's instruction is removed
as proof of non-delivery**: it cannot prove the first copy did not land.
**(2) Both final gates now bind to ONE exact immutable payload
version.** A `delivery_payload_ref` [proposed] names it; **nothing may
be changed, replaced, extended, reordered, or transformed after either
gate**; a §7Q-requested safer transformation creates a **new immutable
version** and **re-runs final §7Q, then final SACL, on that same
version** (a transformation is **not** terminal `withheld` unless nothing
remains); the privacy-decision version is **revalidated after the SACL
gate and immediately before every actual channel write**; and **a
streamed unit must be either an unchanged slice of one fully
pre-approved payload or separately gated §7Q-then-SACL** — **fence and
generation rechecks alone are NOT sufficient for newly generated
units**. **Any component that changes the answer must act BEFORE the
final §7Q gate; a change after approval returns the operation to that
gate.** **(3) Duplicate identity is now stable across retries.** The
logical idempotency key **no longer contains mutable authorization
facts** (epoch, generation, SACL/PBR/privacy versions) — those are
**per-attempt validation facts**, while the **stable logical delivery key
(request + destination)** and the **stable `output_operation_id`** never
change across pre-delivery retries. **A new generation or a fresh gate
pass can never silently license a second visible copy.** **No policy
changed; no question is asked; no authority or store is added.**

## 1. PLAIN PURPOSE

B-INT-6 wires **one continuous output path** from the first thought of
retrieving something to the moment a word actually reaches a channel.

It exists so that **privacy runs before relevance**, so that **the
privacy gate runs before the access gate at the very end**, so that
**neither gate can widen the other**, and so that **nothing that stopped
being permitted mid-flight can still be delivered** — including through
a structural gap, an implied omission, or a stale draft.

## 2. GOVERNING AUTHORITY, REPOSITORY POINT, AND FILES READ

Authority order: (1)
`01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` — **Master V10 governs
every conflict**; (2) `NH_DECISION_DEFAULTS-S19_v2_2.md`; (3)
`cursorrules`; (4) `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`.

**Repository point:** `nesgeva/NH-GOVERNANCE`, branch `main`, head
**`ab4a6ab771f47287938898619419d40c393ce777`**, verified at task start
(latest commit: *Accept and close B-INT-5 package*). The complete delta
from `6a057af4…` was inspected: **exactly the two B-INT-5 acceptance
files**, nothing modified, deleted, or renamed. **A repository-wide
search confirmed no B-INT-6 candidate and no B-INT-6 closure record
exists** — this is the first.

**Files actually read at this head (not summaries):** Master V10
`2d9ed4c6` — **§7Q in full** (its **Layer 1 — pre-retrieval
visible-output eligibility control** and **Layer 2 — pre-output privacy
review**; the six operations; the rule that a **model-provider refusal
is a mouth limitation recorded separately, never a privacy rule**; the
ambiguous/outdated/unavailable/conflicting-permission rule; the
output-failure rule; the list of surfaces privacy checks apply to; and
the per-decision record contents), **§25.4 SACL in full** (the four
access levels; **Gates 0–3**; `SACL_session_state` with
`stream_authorization_set`, `primary_addressed_stream`,
**`shared_output_level` = the minimum across all active streams**,
`in_progress_operations`, `last_sia_event_id`, `last_audit_event_id`;
**Permission Boundary Enforcement** — *"SACL reads PBRs via LMAC → §7L
at Gate 3. Per-output permission category check runs at output time
against `permission_categories` in the active PBR"*; **Access Changes
During In-Progress Operations** — *"SACL compares new level against each
in-progress operation's `material_sensitivity`… the operation is flagged
for immediate discard. The output-generation component receives a
discard signal before any output channel is written. No partial output
from a higher-sensitivity operation is delivered"*; **Avoiding Indirect
Disclosure**; the **Output Gate (Two Factors, Sequential)**; the
**ness_presence_required** simultaneity rule; and the **failure/stale/
restart** rules — *"On SACL restart: all streams → guest; all in-progress
operations discarded"*), **§9** and **§0B** where directly relevant;
Map v1.6 `33af648d` (**B-INT-6**, **C-7Q**, **C-SACL**, **C-OTHER**,
**CY-I**, **I.4**); the eight-bundle plan `2d6483d1` (**Bundle 5**);
accepted **A7 v1.1** `3deacafb` + receipt; accepted **B7 v1.3**
`7fda28e9` + receipt; accepted **B-INT-5 v1.5** `c4497281` + receipt;
accepted **B24 v7** `7f5762e5` (the validator-first output boundary —
*the validator never widens or re-scopes a claim*); the **B-INT-11**
full-transparency recordkeeping requirement; and the accepted **B9**
retry rules **where directly applicable** (retry classification is
consumed **by reference**; **no retry value is invented here**).

## 3. THE SETTLED ORDER — QUOTED, NOT INVENTED

Master §25.4, **Output Gate (Two Factors, Sequential):**

> **1. §7Q privacy gate — must pass.**
> **2. SACL access gate** — content must fall within current access level
> and (for `known_person`) permitted PBR categories.

And Master §7Q supplies the two layers this chain hangs on: **Layer 1 —
pre-retrieval visible-output eligibility control** (*before* material
becomes a candidate) and **Layer 2 — pre-output privacy review**
(*after* material is retrieved and a response is formed).

**B-INT-6 changes none of this. It wires it.** **Neither gate may widen
the other, and a pass from one NEVER substitutes for the other.**

## 4. THE ONE CONTINUOUS OUTPUT PATH — STAGE BY STAGE

**Caller / receiver at every stage** (the **Output Delivery Coordinator
(ODC)** [proposed] is the caller; it owns **no** privacy, access, SACL,
PBR, LMAC, or delivery authority of its own — it holds only the
coordination records of §11):

| # | Stage | Caller | Receiver (the AUTHORITY that decides) | What crosses the boundary |
|---|---|---|---|---|
| 0 | Admit the output operation | Requesting function | **ODC** | Purpose, destination, request identity, the **B-INT-5 handoff** (§5) |
| 1 | **§7Q pre-retrieval visible-output eligibility (Layer 1)** | ODC | **§7Q / B7** — **the privacy authority** | Purpose + candidate scope → an **eligibility decision reference**; **privacy-ineligible material never becomes a candidate** |
| 2 | **SACL supplies the retrieval scope** | ODC | **SACL** — **the access authority** | The current **permitted access level** and **applicable PBR categories** for the addressed stream(s), **supplied to LMAC before retrieval** (Master's own wiring) |
| 3 | **Retrieval within the intersection** | ODC → **LMAC** | LMAC routes to §7F/§7R/§7L/etc. | **Only material inside the intersection of §7Q eligibility AND the SACL/PBR limits.** **LMAC remains stateless: it owns no authorization and keeps NO cross-query cache.** |
| 4 | **Form the output** | ODC | Content generation (**inside B24's validator-first boundary**) | **Only permitted material.** The generator **never sees content above its permitted level and cannot reveal its existence** — not by statement, not by structural gap, not by implied omission |
| 5 | **§7Q FINAL privacy gate (Layer 2, incl. pre-output review)** — **the FIRST sequential delivery factor** | ODC | **§7Q / B7** | The formed draft **by reference** → **pass / withhold / transform**; on failure, **withhold the affected content for the unauthorized purpose and produce the safer version** |
| 6 | **SACL FINAL access gate** — **the SECOND sequential delivery factor** | ODC | **SACL** | Current **access level** + (for `known_person`) the **per-output PBR category check at output time** → pass / refuse |
| 7 | **Revalidate the B-INT-5 delivery fence and mode facts** | ODC | **B-INT-5 PMA** (fence owner) + the owner versions | **Fence `released`** under the **same runtime epoch and current committed generation**; SACL-state version and observability version **still current** |
| 8a | **Revalidate** the current gates, owner versions, and the fence | ODC | §7Q/B7, SACL, B-INT-5 PMA (owners) | Any mismatch **blocks the write** (§7A) |
| 8b | **Create a FRESH delivery claim for THIS intended attempt** | ODC | ODC's own coordination record | The claim reserves **one** intended attempt and proves **only that sending was authorized** — **it is not delivery** (§7, §6F) |
| 8c | **Create and flush the `delivery_dispatch_intent_event`** — **BEFORE any channel contact** | ODC | ODC's own record | Proves **only that N.H was ABOUT TO contact the channel**. **Once durable, the claim becomes `spent` and may NEVER be automatically reused.** |
| 8d | **Contact the channel** (using the intended `delivery_attempt_id` and the stable delivery token) | ODC | **Output channel** | The **first actual write is the IRREVERSIBLE EXPOSURE POINT** |
| 8e | **The channel confirms it ACCEPTED the handoff** | Output channel | ODC | → append **`delivery_attempt_event`**. **This proves the handoff was accepted — NOT that anything became visible.** |
| 8f | **The channel outcome resolves** | **Output channel (the owner of delivery reality)** | ODC | **confirmed-delivered** \| **confirmed-not-delivered** \| **unknown** — **recorded only from channel-owner facts** |
| 8g | **Write a confirmation receipt — ONLY for a positive channel acknowledgment** | ODC | — | **The receipt is the durable confirmed-delivery point.** **A claim, a dispatch intent, and an attempt event are NONE of them delivery.** |

**No stage may be skipped, reordered, or merged. There is exactly ONE
output path — no second route, and no hidden route around the
pre-retrieval limits of stages 1–2.**

## 5. THE B-INT-5 HANDOFF — CONSUMED, NEVER RECONSTRUCTED

Every output operation carries the accepted B-INT-5 handoff:

- the **current mode-session reference**; the **committed mode state**;
- the **`mode_runtime_epoch_id`** and the **`current_committed_mode_generation`**;
- the **current effective-access snapshot**;
- the **`sacl_session_state_ref` + state version/event reference**;
- the **complete multi-speaker access shape** (per-stream entries with
  their own assessment refs and freshness);
- the **`primary_addressed_stream`**;
- the **`shared_output_level`**;
- the **individual stream level — usable ONLY on a genuinely private and
  unobservable path**;
- the **PBR references and categories**; the **Ness-presence state**
  where required;
- the **output-channel observability owner and version**;
- the **current top-security owner references** where required
  (**both** `bai_lease_ref` **and** `sacl_gate1_decision_ref`);
- the **delivery fence**;
- the **access-reduction cancellation signal**;
- the **mode-authority dependency scope**.

**A stale, missing, or incompatible handoff FAILS CLOSED — no
retrieval, no forming, no delivery.** **B-INT-6 NEVER reconstructs
B-INT-5 authority from logs**, and it **never re-derives** a mode state,
a fence, a generation, or an access level for itself.

## 6. IDENTITY, THE IMMUTABLE PAYLOAD, AND THE LIFECYCLE

### 6A. STABLE IDENTITY — SEPARATED FROM MUTABLE AUTHORIZATION FACTS

**The logical identity must NOT contain anything that legitimately
changes during a safe pre-delivery retry.** Epoch, generation, and the
SACL / PBR / privacy / observability versions **all** may change between
attempts — so **none of them belongs in the duplicate key.**

- **`output_operation_id`** [proposed] — **one stable logical parent**
  per logical output. Never re-minted.
- **`delivery_idempotency_key`** [proposed] — **one stable logical
  delivery key**, derived from **the request identity + the destination**
  (the logical *"this answer, to this place"*). **It contains no epoch,
  no generation, and no owner versions.**
- **`delivery_attempt_id`** [proposed] — **one per individual attempt.**
  Attempts are **child events under the one parent.**
- **Per-attempt validation facts (attached to the attempt, never to the
  key):** the current `mode_runtime_epoch_id`, the
  `current_committed_mode_generation`, the §7Q privacy-decision version,
  the SACL state version, the PBR version, the observability version, and
  the delivery-fence reference.

**Duplicate scope, stated honestly:** the **stable
`delivery_idempotency_key` is the scope over which duplicate visible
output is prevented**, and **it stays IDENTICAL across every
pre-delivery retry of the same logical output** — **a new generation, a
fresh gate pass, a new claim, or a new attempt NEVER silently creates
permission for a second visible copy.** **What can actually be
promised:** **exactly-once VISIBLE delivery only where the output-channel
owner supports a verified idempotency contract on that same stable
token**; **without that contract, B-INT-6 guarantees NO BLIND RESEND and
NO AUTOMATIC DUPLICATE ATTEMPT after an unknown result** — nothing
more. **A parent has AT MOST ONE winning terminal result** (and may
legitimately remain **open** in the unresolved `delivery_unknown` state —
§6C, §7).

### 6B. ONE EXACT IMMUTABLE PAYLOAD — WHAT BOTH GATES APPROVE

The formed answer is written **once** into the operation's protected
working area as an **immutable version**, named by
**`delivery_payload_ref`** [proposed] (version-identified). **The payload
itself NEVER enters an ordinary log** — records carry the reference only.

**Both final gates must approve the SAME exact immutable version.**

**The final §7Q decision binds to:** the **output operation**; the
**exact `delivery_payload_ref` version**; the **purpose**; the
**destination**; the **output channel and its observability reference**;
the **current privacy instruction/decision version**; and the **current
mode epoch and generation**.

**The final SACL decision binds to that same exact payload version**,
and additionally to: the **`material_sensitivity`**; the **addressed
stream**; the **active stream set**; the **shared / private-path
classification**; the **current SACL state and version**; the **PBR
version and permitted categories**; the **Ness-presence result** where
required; and the **top-security owner references** where required.

**The delivery claim and every attempt must reference:** that **exact
payload version**, the **final §7Q decision reference**, the **final SACL
decision reference**, and the **current fence and owner versions.**

**Absolutely: no content may be changed, replaced, extended, reordered,
or transformed after either final gate.** **Any validator or other
component that changes the answer must act BEFORE the final §7Q gate — a
change after approval RETURNS the operation to the final §7Q stage**
(§6D).

### 6C. LIFECYCLE

**States** [proposed]: `requested` → `privacy_prefiltered` → `access_scoped`
→ `retrieved` → `formed` → (**`privacy_transform_required`** ⟳) →
`privacy_final_passed` → `access_final_passed` →
`fence_and_owner_versions_revalidated` → **`delivery_claimed`** →
**`attempt_started`** → **`delivered`** | **`withheld`** |
**`discarded`** | **`failed`** | **`delivery_unknown`**.

**`delivery_unknown` is an UNRESOLVED, PROTECTIVE, NONTERMINAL state.**
It cannot be both terminal and later resolvable, so it is **not
terminal**: the parent **remains open**, honestly, **without pretending
that delivery succeeded or failed.** **It is NEVER silently converted to
`failed` or `delivered`, and NEVER retried**, without one of the
permitted channel-owner facts.

**Allowed transitions out of `delivery_unknown` — and only these:**

| From | Trigger (a **channel-owner** fact — never an inference) | To |
|---|---|---|
| `delivery_unknown` | **A late POSITIVE channel confirmation** | **`delivered`** (write the confirmation receipt) |
| `delivery_unknown` | **Positive channel proof that NOTHING was written** | **Fresh validation** → a **NEW child attempt** with a **NEW claim**, under the **same parent and the same stable delivery key** |
| `delivery_unknown` | **Verified same-token channel DEDUPLICATION** guarantee | **Fresh validation** → a **NEW child attempt** with a **NEW claim**, under the **same stable token** |
| `delivery_unknown` | **No safe proof and no deduplication guarantee** | **Remain `delivery_unknown`. DO NOT RESEND.** |

**Ness's request alone is NOT proof of non-delivery** and never resolves
this state. **A later new user request is a SEPARATE NEW output
operation** — it does not resolve, retry, or replay the uncertain one.

**Terminal results** are `delivered`, `withheld`, `discarded`, and
`failed`: **a parent has AT MOST ONE winning terminal result.** **Any
non-terminal state EXCEPT `delivery_unknown`** may go to `discarded` (a
restriction), `withheld` (a gate refuses **and nothing permitted
remains**), or `failed`.

**`delivery_unknown` is EXCLUSIVE — it leaves ONLY through the four rows
above.** A **privacy restriction, access reduction, close, restart, or
any other later change**:

- **blocks every future retry**, and may make the protected payload
  unavailable;
- **does NOT rewrite unknown delivery reality as `failed`, `discarded`, or
  `withheld`** — **N.H does not get to decide what the world did**;
- **does NOT prevent a later channel confirmation from recording the
  historical fact that delivery occurred** (→ `delivered`, on that
  proof);
- **grants no new output permission.**

**After positive proof of NON-delivery**, the **current gates may then
decide that no new output is permitted at all** — producing the
appropriate terminal result (`withheld`, `discarded`, or `failed`) **for
that decision**, not as a guess about the earlier attempt.

**The retry route, legally:** **current checks → fresh claim → attempt
started → channel result.** **Retries are child attempts under the same
parent and the same stable delivery key** — never a new logical delivery
identity.

### 6F. ONE FRESH CLAIM PER ACTUAL ATTEMPT

**Why:** a claim **binds per-attempt gate, fence, and owner-version
facts**, while a legitimate retry may run under **new** facts. **Therefore
one old claim can NEVER authorize a later attempt.**

**The binding, precisely:**
- **one stable `output_operation_id`** per logical output;
- **one stable `delivery_idempotency_key`** across the **whole** logical
  output;
- **one new `delivery_attempt_id`** per attempt;
- **one FRESH `delivery_claim_id`** per attempt;
- **each claim is bound to exactly ONE intended `delivery_attempt_id`.**

**Every `delivery_claim_record` references:** the **parent operation**;
the **stable delivery key**; the **intended attempt id**; the **exact
immutable payload version**; the **final §7Q decision**; the **final SACL
decision**; the **current privacy, SACL, PBR, and observability
versions**; the **current mode epoch and generation**; the **current
delivery fence**; its **creation time**; and its **claim status**.

**The claim is IMMUTABLE and APPEND-ONLY — it is never edited.** The
`delivery_claim_record` is written once with **initial status `active`**,
and every later state change is a **separate append-only
`delivery_claim_state_event`** [proposed] carrying **`spent`** |
**`invalidated`** | **`abandoned`**, its basis, and its time. **The
LATEST VALID state event determines whether the claim may still be
used.** **The `delivery_dispatch_intent_event` makes the claim `spent`
BEFORE channel contact** (§7C). **Claim-state records are COORDINATION
ONLY — never privacy, access, or delivery authority.** They record which
claim (if any) may still stand behind its one intended attempt; **they
never decide privacy, access, or delivery reality.**

**The attempt event references that exact claim.** **The confirmation,
confirmed-non-delivery, and uncertainty records each reference BOTH the
attempt AND its claim.**

**The dispatch seam — the ordered truth (§7C):** after the claim is
flushed, a **`delivery_dispatch_intent_event`** [proposed] is created and
flushed **before the channel is contacted**, referencing the **parent**,
the **stable delivery key**, the **claim**, the **intended
`delivery_attempt_id`**, the **exact `delivery_payload_ref`**, and the
**current validation facts**. **Once that event is durable, the claim
becomes `spent`** (a `delivery_claim_state_event`) **and may never be
automatically reused.**

**Claim reuse and invalidation:**
- **Crash BEFORE the dispatch-intent event:** **no channel contact was
  made.** The **same active claim may be reused ONLY when EVERY fact bound
  into it is still current AND the intended attempt never began.**
- **Crash AFTER the dispatch-intent event but before a provable channel
  result:** → **`delivery_unknown` — EVEN WHEN the local
  `delivery_attempt_event` is missing.** **The absence of that event is
  NEVER evidence that no call happened**, and **never grounds for an
  automatic resend.**
- **If ANY bound fact changed** (gate decision, fence, epoch, generation,
  privacy/SACL/PBR/observability version): **that unused claim is
  `invalidated`**, and a **new claim and a new attempt** are created
  **after fresh checks**.
- **Positive proof of non-delivery** → a **new child attempt with a new
  claim**, under the same parent and stable delivery key.
- **A channel-idempotent retry after an unknown result** → also a **new
  attempt with a new claim**, under the **same stable token**.
- **An old, `spent`, `invalidated`, `abandoned`, or stale claim can NEVER
  authorize a later attempt.**

**A confirmed-not-delivered child result may return the parent to fresh
gate and fence validation** (§6C's retry route). **An unknown result
follows §6C's `delivery_unknown` rules.**

### 6D. THE TRANSFORMATION LOOP

If the final §7Q gate requests a **safer transformation** (Master §7Q's
own *"produce a safer version"* path):

1. The operation enters **`privacy_transform_required`**.
2. A **NEW immutable payload version** is created (the old version is
   never edited).
3. **The final §7Q gate runs AGAIN on that new version.**
4. **Only after §7Q passes** does the **final SACL gate run on that same
   version.**
5. **Only that exact approved version may proceed** to the claim.

**A transformation is NOT a terminal `withheld` result** — it becomes
`withheld` **only when no permitted output remains at all.**

### 6E. TRANSACTIONS, CHECKPOINTS, AND WHAT IS AUTHORITY

Each stage commits its own **append-only stage checkpoint** carrying the
**owner's decision reference**. **The only stage that changes the outside
world is the channel write (§7).**

**Live authority is held ONLY by its owners** — §7Q/B7 (privacy), SACL
(access/PBR), the B-INT-5 PMA (mode, fence, epoch/generation), BAI
(lease), and **the output-channel owner (delivery reality)**. **Every
B-INT-6 record is coordination or history — never authority**, and **no
log ever restores a gate result, a fence, or a delivery right.**

## 7. SENDING INTENT versus CONFIRMED DELIVERY — THREE DISTINCT TRUTHS

**The honest distinction v1_0 collapsed:** *reserving the right to send*
is not *having sent*, and *having handed bytes to a channel* is not
*knowing they became visible*. B-INT-6 therefore keeps **three separate
truths**, each with its own record:

| # | Truth | Proposed record | What it proves — and what it does NOT |
|---|---|---|---|
| 1 | **Delivery claim** — the one logical attempt is **durably reserved BEFORE the channel is contacted** | **`delivery_claim_record`** [proposed] | Proves **only that sending was AUTHORIZED and RESERVED** (both gates passed on the exact payload version; fence and owner versions valid). **It says NOTHING became visible. A pre-write claim is NEVER called a delivery fact.** |
| 2 | **Delivery attempt started** — **control was actually handed to the channel** | **`delivery_attempt_event`** [proposed] | Proves the call was made under `delivery_attempt_id`. **It does not prove any byte was written or seen.** |
| 3 | **Confirmed delivery** — a **positive, channel-OWNED acknowledgment** that the write became visible or was durably accepted | **`delivery_confirmation_receipt`** [proposed] | **This — and only this — is the durable confirmed-delivery point.** |

**Two facts stated plainly:**
- **The first channel write is the IRREVERSIBLE EXPOSURE POINT.** Before
  it, everything is cancellable at zero cost to Ness's privacy; after it,
  nothing can be recalled.
- **No local record, by itself, can prove generic external delivery.**
  B-INT-6 does not pretend otherwise.

**What may honestly be promised:**
- **Exactly-once VISIBLE delivery may be claimed ONLY where the
  output-channel owner supports a VERIFIED IDEMPOTENCY CONTRACT keyed to
  the same stable delivery token** (`delivery_idempotency_key`, §6A).
- **Otherwise, B-INT-6 guarantees exactly this and no more: NO BLIND
  RESEND, and AT MOST ONE automatic attempt after an uncertain result.**
  **It does not guarantee impossible universal exactly-once delivery.**

**The four outcomes, exactly:**

1. **Crash after the claim, before `attempt_started`:** **no channel call
   occurred.** The **same parent** may retry — **only after ALL current
   gates and fences are rechecked** (§6D's gates, §6B's binding, the
   fence and owner versions). The stable delivery key is unchanged, so no
   second copy can arise.
2. **Crash after `attempt_started`, before a provable channel outcome:**
   → **`delivery_unknown`** — an **UNRESOLVED, NONTERMINAL** state (§6C).
   **NO automatic resend.** A `delivery_uncertainty_record` [proposed] is
   written, **referencing BOTH the attempt AND its claim** (references and
   a non-reconstructive descriptor only — **never the payload**). **The
   parent stays open, honestly, until a channel-owner fact resolves it.**
3. **Positive proof that NOTHING was written:** a
   `delivery_non_delivery_receipt` [proposed] is written (**referencing
   both the attempt and its claim**), and the **same parent** may retry —
   **after fresh checks, with a NEW claim and a NEW attempt** under the
   **same stable delivery key** (§6F).
4. **Positive confirmed delivery:** write the
   **`delivery_confirmation_receipt`** and finish **`delivered`**.
   **A confirmed delivery is NEVER sent again.**

**Resolving an uncertain delivery — the corrected rule.** **Ness's
instruction is NOT sufficient proof that the first copy was not
delivered, and is no longer accepted as one.** An uncertain old payload
may be resent **only** when:

- **the channel owner POSITIVELY PROVES non-delivery**; **or**
- **the channel owner GUARANTEES deduplication through the same stable
  idempotency token.**

**Otherwise it remains `delivery_unknown`, permanently.** And: **a later
new user request is NOT recovery or replay of the uncertain old
payload** — it is a **new logical output operation**, with its own
identity, its own gates, and its own freshly formed payload.

### 7C. THE DISPATCH SEAM — ORDERED, AND HONEST ABOUT WHAT IT PROVES

**The required order, exactly:**

1. **Revalidate** the exact payload version, the final §7Q decision, the
   final SACL decision, the privacy/SACL/PBR/observability versions, the
   mode epoch/generation, and the delivery fence.
2. **Create and flush the fresh `delivery_claim_record`**, bound to **one
   intended `delivery_attempt_id`**.
3. **Create and flush the `delivery_dispatch_intent_event`** —
   referencing the **parent**, the **stable delivery key**, the **claim**,
   the **intended attempt**, the **exact payload version**, and the
   **current validation facts**.
4. **Once the dispatch-intent event is durable, the claim becomes
   `spent`** (a `delivery_claim_state_event`) **and may NEVER be
   automatically reused.**
5. **Contact the channel**, using the intended attempt id and the stable
   delivery token.
6. **When the channel confirms it ACCEPTED the handoff**, append the
   **`delivery_attempt_event`**.
7. **Record confirmed delivery, confirmed non-delivery, or uncertainty
   ONLY from channel-owner facts.**

**What each record proves — and does not:**
- **Dispatch intent** proves **only that N.H was ABOUT TO contact the
  channel.**
- **Attempt started** proves **the channel ACCEPTED the handoff.**
- **Neither proves visible delivery.**
- **Only a positive channel acknowledgment proves confirmed delivery.**

**The crash rules at this seam:**
- **Crash BEFORE the dispatch intent:** the **active claim may be reused
  ONLY if all bound facts remain current AND the intended attempt never
  began.**
- **Crash AFTER the dispatch intent but before a provable channel
  result:** **treat it as `delivery_unknown` — EVEN WHEN the local
  `delivery_attempt_event` is missing.**
- **NEVER automatically resend merely because `delivery_attempt_event` is
  absent** — its absence proves nothing about the world.
- **A resend requires positive channel proof of non-delivery, or verified
  same-token deduplication.**
- **Where the channel supports an ATOMIC IDEMPOTENT DISPATCH CONTRACT,
  record it and use it** — **but NEVER assume every channel supports
  one.**

### 7A. REVALIDATION IMMEDIATELY BEFORE EVERY ACTUAL WRITE

**After the final SACL gate and immediately before EVERY actual channel
write**, these are revalidated together — and any mismatch **blocks the
write**:

- the **current §7Q privacy instruction / decision version**;
- the **SACL state / version**;
- the **PBR version**;
- the **observability version**;
- the **mode epoch / generation**;
- the **delivery fence** (`released`, under this epoch and committed
  generation).

### 7B. STREAMED OR UNIT-WISE OUTPUT

**Exactly one of these two, never something looser:**

- **Either** every written unit is an **UNCHANGED SLICE of ONE fully
  pre-approved immutable payload version** (§6B) — the whole payload
  passed §7Q-then-SACL before the first byte;
- **or** **each unit separately passes the final §7Q gate FIRST and the
  final SACL gate SECOND before it is written.**

**Merely rechecking the fence and the generation is NOT sufficient for
newly generated units** — new content requires new gate passes, in the
settled order. **A restriction arriving mid-stream stops all further
writes at once**, and **already-written bytes cannot be recalled — which
is exactly why both gates and the fence check run before the first
write.** **No final interface behavior is invented here.**

## 8. RESTRICTIVE CHANGES — THE MORE RESTRICTIVE RESULT WINS IMMEDIATELY

**On any** privacy restriction, **SACL downgrade**, **PBR change**,
**speaker change**, **addressed-stream change**, **Ness-presence loss**,
**observability change**, **mode-generation change**, **close**,
**suspension**, **step-up loss**, or **restart**:

- **the more restrictive result wins IMMEDIATELY;**
- **stale retrieval and formed output are cancelled;**
- **material above the new ceiling is discarded BEFORE the next
  output-channel write** — carrying Master's own rule exactly: **SACL
  compares the new level against each in-progress operation's
  `material_sensitivity`; if the new level is below it, the operation is
  flagged for immediate discard, the output-generation component
  receives the discard signal before any output channel is written, and
  NO partial output from a higher-sensitivity operation is delivered;**
- **no previously rejected or discarded draft is ever replayed later;**
- **no old epoch or old generation may deliver** (the B-INT-5 fence);
- **restriction does NOT wait for successful logging** — **the
  restriction applies first, delivery stays blocked, and the record is
  written or carried forward afterwards, without ever reopening
  access.**

**Cancellation propagation:** the cancellation signal reaches **exactly
the operations carrying the `mode_authority_dependency_ref`** on the
affected mode session (accepted B-INT-5 §9A) — **separately authorized
background work is not swept up**, and **nothing background work
produces may enter an interactive path without current privacy, access,
and delivery checks.**

## 9. RETRY BEFORE DELIVERY

- **A technical retry BEFORE any channel write reuses the SAME parent
  `output_operation_id` and the SAME stable `delivery_idempotency_key`**
  — nothing became visible, so nothing can duplicate. **Each attempt gets
  its own `delivery_attempt_id` AND its own FRESH `delivery_claim_id`**
  (§6F) — **an old, spent, invalidated, or stale claim can never authorize
  a later attempt.** The current epoch, generation, and owner versions are
  attached to **that attempt and its claim** as validation facts — **never
  to the stable key** (§6A).
- **A retry never reuses a stale gate result.** On every attempt, the
  **current** §7Q decision, the **current** SACL decision, the **fence**,
  and the **owner versions** are obtained again — **against the same
  exact immutable payload version** (§6B). **A gate pass is never cached
  across a restriction.**
- **A fresh gate pass or a new generation NEVER licenses a second visible
  copy** — the stable delivery key holds the duplicate scope.
- Retry **classification and values are the accepted B9 rules, consumed
  by reference** — **no count, gap, or deadline is invented here.**
- **After an uncertain result: at most ONE automatic attempt** (§7),
  and **only** where the channel owner's idempotency contract or a
  positive non-delivery proof makes it safe. **Otherwise: no resend.**
- **After a confirmed delivery there is no retry** — the operation is
  terminal.

## 10. RESTART AND CRASH BEHAVIOR

**After a real application, process, or machine restart — exactly:**
- **the epoch necessarily changes** (B-INT-5 mints a new
  `mode_runtime_epoch_id`);
- **every old ACTIVE claim becomes INVALID**, and **no old claim may be
  reused** — its bound epoch is dead;
- **no old formed payload may be replayed**;
- **recovery either FAILS the old operation safely, or — where recovery is
  still valid — creates a NEW immutable payload version, re-runs the
  final §7Q gate FIRST and the final SACL gate SECOND, revalidates all
  current owners and the fence, and creates a NEW claim and a NEW attempt
  under the SAME stable logical parent and delivery key.**
- **`delivery_unknown` operations are NOT rewritten by the restart** —
  they remain unresolved (§6C).

**Same-claim reuse is permitted ONLY during a still-live runtime where NO
dispatch intent exists and EVERY bound fact remains current** (§6F, §7C).

**Also, always:** **no old live gate result, delivery fence, or mode
authority is restored from history**; **unfinished output operations are
failed or safely recovered ONLY from committed truth**; and **current
privacy, SACL, PBR, observability, and B-INT-5 facts must be obtained
again.** Master's own
SACL rule is carried: **on SACL restart, all streams → guest and all
in-progress operations are discarded**; B-INT-5's rule is carried: **the
runtime epoch is new and the mode begins Dry.**

| # | Crash boundary | Committed truth | Exact recovery action |
|---|---|---|---|
| 1 | Before stage 1 | The admitted operation only | **Fail** the operation. Nothing was considered. |
| 2 | After §7Q prefilter, before SACL scope | The §7Q eligibility **reference** (its owner's record) | **Fail.** The old result is **history, not authority** — a new operation re-asks §7Q from current facts. |
| 3 | After SACL scope, before retrieval | The scope reference | **Fail.** Nothing retrieved. |
| 4 | During retrieval | Whatever LMAC's targets committed (reads) | **Fail.** Retrieved candidates die with the epoch; **nothing may be formed from them.** |
| 5 | After retrieval, before forming | Retrieval-intersection record (references only) | **Fail.** No draft exists. |
| 6 | During forming | Nothing deliverable | **Fail.** The partial draft is **discarded, never replayed.** |
| 7 | After forming, before the final §7Q gate | The **`delivery_payload_ref`** (the one immutable version) in the operation's protected working area | **Fail and discard.** **A payload version that never passed both final gates can never be delivered later.** |
| 8 | After §7Q pass, before the SACL gate | The §7Q final-gate reference | **Fail and discard** — **a privacy pass NEVER substitutes for the access gate.** |
| 9 | After SACL pass, before fence revalidation | Both final-gate references | **Fail and discard** — the fence was never revalidated, and the epoch is now dead. |
| 10 | After fence/owner revalidation, before the **delivery claim** | Both gate decisions + the revalidation | **Fail and discard.** No claim exists → **nothing was ever reserved, and nothing is deliverable.** |
| 11 | **After the delivery CLAIM, before `attempt_started`** | The **`delivery_claim_record`** — proving **only that sending was authorized for ONE intended attempt** | **No channel call occurred.** **The same claim may be reused ONLY if EVERY bound fact is still current and that intended attempt never began.** **If any bound fact changed, the unused claim is `invalidated`** and a **NEW claim + NEW attempt** are created after fresh checks (§6F) — always under the **same stable delivery key**. |
| 11b | **After the dispatch-intent event, before any channel result** | The **`delivery_dispatch_intent_event`** — proving **only that N.H was about to contact the channel**; the claim is now **`spent`** | → **`delivery_unknown`, EVEN IF `delivery_attempt_event` is MISSING.** **The absent attempt event is NOT evidence that no call happened.** **No automatic resend.** The claim can never be reused. |
| 12 | **After `attempt_started`, before a provable channel outcome** | The **`delivery_attempt_event`** and its claim — control reached the channel; **visibility is UNKNOWN** | → **`delivery_unknown`** (**unresolved, NONTERMINAL**). Write the `delivery_uncertainty_record` (**no payload**; references the attempt **and** its claim). **NO automatic resend.** The parent **stays open** until a **channel-owner fact** resolves it (§6C). **Ness's request is not such a fact.** |
| 13 | Positive proof that **nothing was written** | The channel's **negative acknowledgment** (`delivery_non_delivery_receipt`) | The **same parent** retries with a **NEW claim and a NEW attempt** after fresh checks — **never by reusing the spent claim** (§6F). |
| 14 | **After a CONFIRMED delivery**, before the receipt/terminal record flushes | The channel's **positive acknowledgment** | Complete the **`delivery_confirmation_receipt`** and the terminal `delivered` record **idempotently**. **Never deliver again.** |
| 15 | After the terminal record, before acknowledgment to the caller | The terminal record | Absorb the replay; **no second delivery.** |

## 11. COORDINATION RECORDS — B-INT-6-OWNED ONLY

**No second authority is created.** §7Q/B7 owns privacy decisions; SACL
owns access levels, PBR state, and its own gate results; the B-INT-5 PMA
owns the mode, the epoch/generation, and the delivery fence; LMAC owns
**nothing** (stateless, no cross-query cache); BAI owns leases; **and the
OUTPUT-CHANNEL OWNER owns delivery reality — B-INT-6 never asserts
visibility on its behalf.** **Every
gate result below is a REFERENCE to its owner's record — never a copy,
never a second store.**

**All records:** append-only unless marked live-state; **carry
references, never private content**; obey **§7Q and §25** access rules;
carry the **epoch + committed generation**; **add no evidence weight**.

1. **`output_operation`** [proposed] — the **one parent** (live-state
   until terminal): `output_operation_id`, **`delivery_idempotency_key`**
   (the settled exact field), purpose,
   destination, the **B-INT-5 handoff references**, `state`,
   `terminal_reason`, audit refs. **Exactly one terminal parent record
   per logical output.** Owner: **ODC**.
2. **`output_stage_event`** [proposed] — append-only child checkpoints
   (one per stage), each carrying the **owner's gate-result reference**.
   **Never a second parent truth.**
3. **`retrieval_intersection_record`** [proposed] — what LMAC was
   permitted to consider: the §7Q eligibility ref, the SACL scope ref,
   and the **identities** of admitted material. **References only — no
   content, and no candidate that was excluded is described in a way
   that reveals it existed.**
4. **`delivery_payload_ref`** [proposed] — a **version-identified
   reference** to the **ONE exact immutable payload** in the operation's
   protected working area (§6B). **A transformation creates a NEW version;
   no version is ever edited.** **The payload NEVER enters an ordinary
   log.**
5. **`delivery_claim_record`** [proposed] — the **reservation of the one
   logical attempt, written BEFORE the channel is contacted**: the
   `output_operation_id`, the **stable `delivery_idempotency_key`**, the
   **exact `delivery_payload_ref` version**, **both final gate-decision
   references**, the fence reference, and the per-attempt validation
   facts. **It proves only that sending was AUTHORIZED and RESERVED — it
   is NEVER a delivery fact.**
6. **`delivery_attempt_event`** [proposed] — **control was handed to the
   channel**, under a `delivery_attempt_id`. **It does not prove
   visibility.**
7. **`delivery_confirmation_receipt`** [proposed] — **the channel
   acknowledgment PROVES delivery reality; this receipt RECORDS that
   proof.** It is the **durable confirmed-delivery point**, and **the
   parent may enter `delivered` ONLY by referencing it.** (**It is not the
   only record permitted to contain the word "delivered" — but it is the
   ONLY accepted proof supporting that terminal state.**)
8. **`delivery_non_delivery_receipt`** [proposed] — the channel owner's
   **positive proof that NOTHING was written**, **referencing both the
   attempt and its claim**. **It AUTHORIZES NOTHING** — it **proves only
   that the earlier attempt did not deliver, and thereby makes a retry
   ELIGIBLE.** **The new attempt is AUTHORIZED by fresh §7Q, SACL,
   owner-version, mode, and fence checks** (§6F), and requires a **new
   claim** — **never a reuse of the spent one.**
8b. **`delivery_uncertainty_record`** [proposed] — the honest ambiguity
   (§7): what is unknown, what was **not** done, and the **only** two
   admissible resolutions (channel-owner proof of non-delivery, or its
   verified idempotency contract). **No payload, ever.**
9. **`discard_event`** [proposed] — cancellation/discard, with the
   triggering restriction **by reference** and the
   `material_sensitivity` comparison outcome.
10. **`duplicate_delivery_prevented`** [proposed] — a replay refused.
   **It references: the stable `delivery_idempotency_key`; the relevant
   `delivery_claim_id` and `delivery_attempt_id`; and, where present, the
   `delivery_confirmation_receipt` or the channel owner's idempotency
   result.** (**There is no `delivery_commit_record` in this design.**)
   **No evidence weight.**
11. **`output_recovery_event`** [proposed] — recovery as **one recorded
   operation**, naming the crash boundary (the **fifteen** of §10) and the
   committed truth found. **Append-only history, never authority.**

## 12. §0B / B-INT-11 LOGGING — ON EVERY PARTICIPATING SIDE

**One real operation → ONE parent log.** Stages, retries, and recovery
are **append-only child events** under that parent — never second
parents.

| Operation | The one record | Owner |
|---|---|---|
| Output operation admitted | `output_operation` (`requested`) | ODC |
| §7Q pre-retrieval eligibility | **§7Q/B7's own privacy-decision record** + stage event (referencing it) | **§7Q/B7** / ODC |
| SACL retrieval scope supplied | **SACL's own record** + stage event | **SACL** / ODC |
| Retrieval through LMAC | **LMAC's routing record** (in the shared operational log; LMAC owns no store) + `retrieval_intersection_record` | **LMAC** / ODC |
| Output formed | stage event + **`delivery_payload_ref` (the ONE immutable version)** | ODC |
| Privacy transformation required | stage event (`privacy_transform_required`) + a **NEW `delivery_payload_ref` version**; **final §7Q then final SACL re-run on it** | **§7Q/B7** / ODC |
| **§7Q final gate (first factor)** | **§7Q/B7's decision record** + stage event | **§7Q/B7** / ODC |
| **SACL final gate (second factor)** | **SACL's decision record** + stage event | **SACL** / ODC |
| Fence revalidation | stage event referencing **B-INT-5's fence** | ODC |
| Delivery **claimed** — **a FRESH claim for ONE intended attempt** (nothing visible yet) | `delivery_claim_record` (`claim_status = active`, bound to its intended `delivery_attempt_id`) | ODC |
| Claim **invalidated** (a bound fact changed before dispatch) | append-only **`delivery_claim_state_event`** (`invalidated`) — **the immutable claim record is never edited** (+ a new claim for the new attempt) | ODC |
| **Dispatch intent** (about to contact the channel) | **`delivery_dispatch_intent_event`** + a `delivery_claim_state_event` (`spent`) — **flushed BEFORE channel contact** | ODC |
| Delivery **attempt started** (the channel **accepted the handoff**) | `delivery_attempt_event` (`delivery_attempt_id`, referencing its exact claim and dispatch intent). **It proves acceptance of the handoff — not visibility.** | **channel** (the acceptance) / ODC (the record) |
| Delivery **confirmed** (positive channel acknowledgment) | **`delivery_confirmation_receipt`** (referencing the attempt **and** its claim) + `output_operation` → `delivered` | **channel owner** (the acknowledgment) / ODC (the receipt) |
| Confirmed **NOT delivered** | **`delivery_non_delivery_receipt`** (referencing the attempt **and** its claim) | **channel owner** / ODC |
| Delivery **unknown** (unresolved, nonterminal) | `delivery_uncertainty_record` + `output_operation` → `delivery_unknown` — **the parent stays open** | ODC |
| Withheld | `output_operation` → `withheld` + the refusing gate's reference | ODC |
| Discarded (restriction) | `discard_event` + `output_operation` → `discarded` | ODC |
| Duplicate refused | `duplicate_delivery_prevented` — referencing the **stable delivery key**, the **claim and attempt**, and (where present) the **confirmation receipt or channel idempotency result** | ODC |
| Retry (pre-delivery) | append-only child **attempt** under the **same parent and the same stable delivery key** — with fresh per-attempt validation facts (B9 classification by reference) | ODC |
| Crash recovery | `output_recovery_event` | ODC |
| Fail-closed halt | `output_operation` → `failed` + its stage event | ODC |

**Log rules, binding:** logs **carry references, never private payloads
or withheld content**; they **obey §7Q and §25**; they **add no evidence
weight**; **no log is ever evidence for itself**; **no record logs "the
log was logged"** as a new real operation; and **no log ever restores a
gate result, a fence, or a delivery right.**

## 13. DISCLOSURE SAFETY — WHAT THE OUTPUT MAY NEVER REVEAL

- **Shared or observable output uses `shared_output_level`** (the
  minimum across active streams).
- **An individual stream's level is usable ONLY on an owner-confirmed
  private and unobservable path.**
- **Personal Mode NEVER turns a shared path into a private one**
  (accepted B-INT-5; the observability classification belongs to its
  owner).
- **PBR failure or uncertainty FAILS CLOSED**; the per-output category
  check runs **at output time** against the active PBR.
- **A required Ness-presence loss drops the applicable known-person path
  IMMEDIATELY** — Master: if Ness's stream drops below the required
  level, the known person's stream **drops to guest simultaneously**.
- **Hidden material is NEVER indirectly acknowledged** — Master's own
  rule: the content-generation component **never sees content above its
  permitted level and cannot reveal its existence — not through direct
  statement, not through structural gaps, not through implied
  omission.** **N.H does not say "I cannot tell you"** and **does not
  answer in wording that reveals additional hidden material exists.**
- **The response is formed from permitted material only.**
- **Privacy runs before relevance; the final §7Q runs before the final
  SACL.**
- **Top-security still requires its complete separate owner truths**
  (**both** the current SACL Gate 1 decision **and** the BAI lease).
- **A model-provider refusal is a MOUTH LIMITATION, recorded separately
  — it is never an N.H privacy rule and never evidence that the material
  is forbidden** (Master §7Q).

## 14. FAIL-CLOSED REQUIREMENTS

Withhold, discard, or halt — never proceed — when: the **B-INT-5 handoff
is stale, missing, or incompatible**; the **fence is not `released`**, or
is released under **another epoch or generation**; the **SACL state
version or observability version changed**; **§7Q cannot determine
authorization**; **SACL is unavailable, stale, conflicting, or
suspicious**; a **PBR is missing, stale, or unverifiable**; the
**Ness-presence requirement is unmet**; the **addressed stream or active
stream set changed**; **LMAC cannot honor the intersection**; a **gate
result cannot be tied to this operation, epoch, and generation**;
**top-security is required but either owner truth is absent or
incompatible**; the **delivery outcome is unknown** (→ §7, never a blind
resend); **required audit history cannot be written** (→ **restriction
still applies first**); or **any authority owner required for this
operation is unavailable**.

**Never treat unknown as success. Never deliver first and check
afterwards.**

## 15. MUST-NEVERS

B-INT-6 must never: change A7, B7, §7Q, SACL, PBR rules, or B-INT-5;
**reverse the gate order**; **let SACL decide privacy**; **let §7Q
decide speaker access**; let a pass from one gate substitute for the
other; **let LMAC own authorization or keep a cross-query cache**;
create a **hidden route around the pre-retrieval limits**; create a
**second output path**, privacy authority, access authority, SACL state,
PBR store, LMAC store, or delivery authority; **reconstruct B-INT-5
authority from logs**; replay a discarded or withheld draft; deliver
under an old epoch or generation; deliver twice; **blindly resend on an
unknown outcome**; put private content in a log; reveal that hidden
material exists; wait for logging before applying a restriction;
complete **B-INT-7, B-INT-8, CY-I, B-CYCLE-4, or Bundle 5**; edit an
authority, accepted, Map, plan, or closure file; or begin
implementation.

## 16. DEPENDENCIES INTENTIONALLY LEFT OPEN

ChatGPT's independent audit and any correction it finds; Ness's later
acceptance; accepted-source placement and a closure receipt; **B-INT-7**;
**B-INT-8**; **CY-I consolidation**; **B-CYCLE-4**; **Bundle 5 final
consistency review and closure**; later versioned **Map/Master
integration**; the **exact channel/transport contract** and what counts
as a positive delivery acknowledgment (**its owner's, not invented
here**); **final interface and streaming behavior**; **exact retry,
timeout, and backoff values** (accepted **B9**); **exact serialization,
naming, and technology**; and **all code, schemas, databases, stores,
migrations, tests, runtime work, and live-disk changes.**

## 17. WHOLE-FILE CONSISTENCY CHECK (DRAFTING CHECKS, NOT CERTIFICATION)

- **Privacy-first / SACL-second proof:** the order is **quoted from
  Master §25.4's Output Gate** and wired as stages 5 → 6, with §7Q's
  Layer 1 at stage 1 and Layer 2 at stage 5; **neither gate widens the
  other**, and **a pass from one never substitutes for the other** (§3,
  §4, crash boundary 8) — consistent in drafting.
- **B-INT-5 handoff proof:** all seventeen handoff facts are consumed by
  reference; **a stale/missing/incompatible handoff fails closed**; and
  **authority is never reconstructed from logs** (§5, §10, §14) —
  consistent in drafting.
- **Known-person / PBR / multi-speaker proof:** `shared_output_level`
  for shared or observable paths; an individual level **only** on an
  owner-confirmed private unobservable path; the **per-output PBR
  category check at output time**; **PBR failure fails closed**; and
  **Ness-presence loss drops the known-person path simultaneously**
  (§13) — consistent in drafting.
- **Discard proof:** Master's `material_sensitivity` comparison and
  **discard-before-any-output-channel-write** are carried verbatim in
  behavior; **no partial output from a higher-sensitivity operation is
  delivered**; **restriction does not wait for logging** (§8) —
  consistent in drafting.
- **Retry proof:** pre-delivery retries reuse the parent identity but
  **never a stale gate result**; values are B9's by reference; **after
  confirmed delivery there is no retry** (§9) — consistent in drafting.
- **Restart proof:** nothing live is restored from history; unfinished
  operations fail or recover only from committed truth; **old drafts are
  never replayed**; all facts are re-obtained; SACL's restart-to-guest
  and B-INT-5's new-epoch/Dry rules are carried (§10) — consistent in
  drafting.
- **The channel-dispatch crash gap is closed** — the
  `delivery_dispatch_intent_event` is flushed **before** any channel
  contact and **spends the claim**; **dispatch intent proves only intent,
  the attempt event proves only handoff acceptance, and neither proves
  visibility**; **a crash after dispatch intent is `delivery_unknown` even
  when the attempt event is missing**, and **an absent attempt event is
  never grounds for an automatic resend**; an atomic idempotent dispatch
  contract is **used where the channel offers one and never assumed**
  (§4, §6F, §7C, crash 11b) — consistent in drafting.
- **`delivery_unknown` is exclusive** — the generic non-terminal sentence
  now **explicitly excludes it**; a restriction, reduction, close, or
  restart **blocks retries and may make the payload unavailable, but
  never rewrites unknown delivery reality as `failed`/`discarded`/
  `withheld`**, and **never prevents a later channel confirmation from
  recording that delivery occurred** (§6C) — consistent in drafting.
- **The records and authority wording are exact** — the claim is
  **immutable and append-only** with separate append-only
  `delivery_claim_state_event`s (`spent`/`invalidated`/`abandoned`,
  **coordination only**); `output_operation` carries the settled
  **`delivery_idempotency_key`**; the **non-delivery receipt authorizes
  nothing — it only makes a retry ELIGIBLE**, while **fresh §7Q, SACL,
  owner-version, mode, and fence checks authorize**; **the channel
  acknowledgment proves delivery reality and the receipt records it**,
  with `delivered` reachable **only by referencing that receipt**; restart
  **invalidates every old claim and replays no payload**; and the crash
  table now names `delivery_payload_ref` (§6F, §10, §11) — consistent in
  drafting.
- **No universal exactly-once overclaim remains** — the stage table's
  final rows are the truthful sequence (revalidate → fresh claim → hand
  to channel → outcome → receipt only on positive acknowledgment); the
  duplicate scope is **bounded**: exactly-once visible delivery is
  promised **only** under a verified channel idempotency contract on the
  same stable token, and otherwise the guarantee is **no blind resend and
  no automatic duplicate attempt after an unknown result**; and
  `duplicate_delivery_prevented` now references the **stable key, the
  claim and attempt, and the receipt or channel idempotency result** —
  **no `delivery_commit_record` exists anywhere in this design** (§4, §6A,
  §11) — consistent in drafting.
- **`delivery_unknown` is honest and NONTERMINAL** — the parent may
  remain **open** without pretending success or failure; it is **never
  silently made `failed` or `delivered`, and never retried**, except on a
  **channel-owner fact** (late positive confirmation → `delivered`;
  proven non-delivery → new claim + new attempt; verified same-token
  deduplication → new claim + new attempt); **Ness's request is not such a
  fact**, and **a later user request is a separate new operation** (§6C,
  §7, crash 12) — consistent in drafting.
- **One fresh claim per actual attempt** — a claim binds per-attempt gate,
  fence, and owner-version facts, so **an old claim can never authorize a
  later attempt**; each claim is bound to exactly one intended
  `delivery_attempt_id`, carries `claim_status` (`active` | `spent` |
  `invalidated` | `abandoned` — **bookkeeping, not a second delivery
  authority**), and is **invalidated** the moment any bound fact changes;
  confirmation, non-delivery, and uncertainty records each reference
  **both the attempt and its claim** (§6F, §9, §11) — consistent in
  drafting.
- **Sending intent is separated from confirmed delivery** — the **claim**
  reserves and proves only authorization; the **attempt** proves only that
  control reached the channel; the **confirmation receipt** (the channel
  owner's positive acknowledgment) is the **only** durable
  confirmed-delivery point. **The first write is the irreversible exposure
  point.** **No local record proves external delivery**, **exactly-once
  visible delivery is claimed only under a verified channel idempotency
  contract**, and otherwise the guarantee is **no blind resend + at most
  one automatic attempt** (§7, §11, crash 11–15) — consistent in drafting.
- **The uncertain-delivery rule is honest** — **`delivery_unknown` persists
  unless the channel owner positively proves non-delivery or guarantees
  deduplication on the same stable token**; **Ness's instruction is NOT
  such proof and is no longer accepted as one**; and **a later new user
  request is a NEW operation, not a replay** (§7) — consistent in drafting.
- **Both gates bind to ONE exact immutable payload** — `delivery_payload_ref`
  is version-identified; the §7Q decision binds to operation, version,
  purpose, destination, channel/observability, privacy-decision version,
  and epoch/generation; the SACL decision binds to that **same** version
  plus sensitivity, addressed stream, active stream set, path
  classification, SACL version, PBR version/categories, Ness-presence, and
  top-security owners; **nothing may change after either gate**, and **any
  component that changes the answer must act BEFORE final §7Q — a later
  change returns the operation to that gate** (§6B, §6D) — consistent in
  drafting.
- **The transformation loop is closed** — a §7Q-requested safer version
  creates a **new immutable version**, re-runs **final §7Q then final
  SACL** on it, and **only that approved version proceeds**; a
  transformation is **not** terminal `withheld` unless nothing remains
  (§6D) — consistent in drafting.
- **Streaming is safe** — a written unit is **either an unchanged slice of
  one fully pre-approved payload or separately gated §7Q-then-SACL**; a
  fence/generation recheck **alone is not sufficient** for newly generated
  units (§7B) — consistent in drafting.
- **Duplicate identity is stable across retries** — the logical key holds
  **no mutable authorization facts**; epoch, generation, and the SACL/PBR/
  privacy/observability versions are **per-attempt validation facts**;
  **the duplicate scope is identical across every pre-delivery retry**; and
  **a new generation or fresh gate pass never licenses a second visible
  copy**. **One parent → exactly one winning terminal result** (§6A, §6C,
  §9) — consistent in drafting.
- **No second authority:** every gate result is a **reference to its
  owner**; LMAC stays **stateless with no cross-query cache**; **no
  privacy, access, SACL, PBR, LMAC, or delivery authority is duplicated**
  (§11) — consistent in drafting.
- **One operation → one parent log; no recursive logging; no record is
  evidence for itself** (§12) — consistent in drafting.
- **No new policy, no invented Ness question, no implementation** — the
  governing files revealed **no genuine unresolved meaning choice** for
  this scope (§0, §16) — consistent in drafting.

---

*End of `NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md`
— `CANDIDATE — NOT ACCEPTED — NOT ADOPTED — NOT BUILT`, awaiting
ChatGPT's independent audit of this actual file and Ness's later
acceptance. Privacy decides what may be considered before relevance ever
looks; privacy speaks first at the door and access speaks second; the
fence is checked one last time; and only then does a word leave. When
the ceiling drops mid-sentence, the sentence dies before it is written —
and what was never permitted is never hinted at, never explained, and
never missed aloud.*

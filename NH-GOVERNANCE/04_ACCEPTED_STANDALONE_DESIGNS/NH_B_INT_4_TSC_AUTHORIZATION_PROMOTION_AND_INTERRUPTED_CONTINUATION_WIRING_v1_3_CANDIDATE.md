# NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md

## 0. STATUS BLOCK

**Status:** `CANDIDATE — NOT ACCEPTED — NOT ADOPTED — NOT BUILT.`

**B-INT-4 only.** **Mechanical wiring only.** **No new policy** — this
file asks Ness nothing and decides no meaning. **No implementation** —
no code, database, schema activation, migration, test, or Cursor
instruction exists or is created. **No Bundle 5 closure. No B-CYCLE-4
closure. B-INT-5, B-INT-6, B-INT-7, and B-INT-8 remain open.**

**Date:** July 13, 2026.

**Register item:** B-INT-4 — TSC authorization and promotion wiring
(Bundle 5 — privacy, security, access, and TSC authority).

**Version note (v1_3):** one final narrow correction pass on v1_2 only
(v1_2 SHA-256
`e888b866c812269db3ec46c615f52b8b4cff38a0d93a305d4254d9d0127a303f`;
1,087 lines; 75,485 bytes — **preserved unchanged, as are v1_0 and
v1_1**), closing two IMPORTANT contradictions and a stale footer.
**(1) Operation state versus claim state.** v1_2 repeatedly said the
authorization **operation** becomes "`failed` (or `released`)", but
`released` is **not** in the operation's controlled list — a genuine
contradiction. v1_3 separates them exactly: **the operation becomes
durably terminal as `failed`** (its controlled list is unchanged and
`released` is **not** added to it), while **`released` and
`superseded` remain claim states only**; the claim's release or
supersession stays **append-only and explicitly linked**, and a new
token creates a **new authorization operation connected through the
superseding claim**. The one-session-one-winner rule is unchanged.
**(2) No invented BAI event during recovery.** v1_2 had recovery
recording `bai_token_consume_blocked` for a pre-receipt crash — but
that event is **BAI-owned** and describes a **live in-process consume
attempt** in which a required condition failed and the token stayed
**unconsumed**. After a restart there is no BAI state, no token, and
no live attempt, so **the coordinator must never manufacture it**, and
"consume blocked" would not honestly describe a receipt-write failure
after an uncertain or in-memory consumption. In v1_3, recovery records
a pre-receipt crash **truthfully, through mechanisms that already
exist**: the existing **`tsc_authorization_stage_event`** (with the
exact failure/recovery reason), the existing
**`tsc_crossstore_recovery_event`** with **`action_taken =
blocked_fail_closed`**, the **operation → `failed`**, and the **claim
→ `released`/`superseded`**. A `bai_token_consume_blocked` event that
**BAI genuinely wrote before the crash may be referenced**, but
**recovery never creates or backfills it on BAI's behalf**; **no new
security-audit event name is invented**; and **missing BAI audit
history is never treated as proof that a consumption attempt
occurred.** Rule B's new biometric flow and new token are unchanged.
**(3) The footer** now names this v1_3 file (the historical v1.1/v1.2
references inside the version history are deliberately untouched).
**Every other v1_2 authorization, promotion, privacy, recovery,
duplicate-prevention, continuation, and logging mechanism remains
unchanged; no policy or meaning changed; v1_0, v1_1, and v1_2 remain
unchanged historical candidates.**

**Version note (v1_2):** one narrow correction pass on v1_1 only
(v1_1 SHA-256
`a9f4b22b1295be5b78e5a64e8f27eda644f2d27229f42a2dac17f3b793bea0c4`;
966 lines; 66,431 bytes — **preserved unchanged, as is v1_0**),
closing two IMPORTANT audit issues that were the same unfinished
consequence of Master §25.6: **if BAI's state dies at restart, then
neither its memory nor its token survives.**
**(1) The crash-recovery record no longer names volatile BAI as
authoritative.** v1_1's `tsc_crossstore_recovery_event` still allowed
`authoritative_store = bai`, contradicting the rest of v1_1 and Master
V10. In v1_2 **`bai` is removed from the post-crash controlled values
and `security_audit_receipt` is added** — an authorization recovery
event may use it **only** when it references a **complete, flushed,
integrity-verified `bai_token_consumed` receipt**, whose verified
binding must appear in `committed_state_found`. **BAI may still make
the live consumption decision inside the running process, but it is
never a post-crash source of truth**, and a **missing or unverifiable
receipt yields `blocked_fail_closed`, never `completed_forward`.**
**(2) A pre-receipt crash can no longer resume with the vanished
token.** v1_1 said recovery "re-runs A1 from scratch under the same
claim" and may proceed to A2 — unsafe, because the original one-time
token **no longer exists** after restart. In v1_2, a crash before the
durable receipt commits means **no authorization exists and the
original token is gone**: it is **never reconstructed, resurrected, or
reused**; the old operation becomes **durably terminal (`failed` /
`released`)**; the old claim is **safely released or superseded**; and
because the session was **never successfully authorized**, **Master
§20's Rule B applies as written (first condition — applied, not
broadened)**: continuing requires a **new biometric authorization flow
and a newly created one-time token**, producing a **new
`authorization_operation_id`** that may take over **only through an
append-only linked supersession**. A **receipt-write failure inside
the same running process fails closed the same way** — the uncertain
or in-memory-consumed token is **never retried**, and a new token is
required.
**The three v1_1 corrections remain intact** (the durable receipt as
the commit point and sole post-crash proof; the one-winner session
claim; B15 as the sole item-promotion and completion authority).
**No accepted policy or meaning changed**, and **v1_0 and v1_1 remain
unchanged historical candidate evidence.**

**Version note (v1_1):** one narrow correction pass on v1_0 only
(v1_0 SHA-256
`6b4e9543fb842110995f8a6d8789501dc77ba403ca414f8a6ab7a02d9cee689d`;
782 lines; 52,091 bytes — **preserved unchanged as historical
candidate evidence**), closing three IMPORTANT audit issues.
**(1) Durable authorization proof after BAI forgets.** Master V10
§25.6 states plainly that **BAI-owned state is "In-memory only.
Nothing persists across restarts"** — so v1_0 was wrong to make a
volatile "BAI consumed-token record" the authoritative post-crash
proof. v1_1 makes the **append-only, flushed security-audit event
`bai_token_consumed`, carrying a complete verified consumption
receipt, the authorization commit point and the sole durable
post-crash proof** (Master §26 requires every event **written and
flushed immediately before the producing function returns**). BAI
stays in-memory-only exactly as Master requires, and **volatile BAI
state is never a recovery source of truth.**
**(2) Exactly one successful token consumption per session.** v1_0's
`authorization_operation_id = f(session_id, bai_token_id)` stopped one
token being spent twice but **did not stop two different valid tokens
both being consumed for the same session.** v1_1 adds a **durable
session-level authorization claim keyed by `session_id` + `purpose`**,
written **before** any consumption, with a uniqueness constraint
admitting **exactly one winner** — coordination only, **granting no
authority of its own** and **creating no second authorization
authority**: it merely serializes access to BAI's accepted authority.
**(3) B15 is the sole item-promotion truth.** v1_0's
`tsc_item_promotion_binding` carried its own disposition, lifecycle,
and `promoted_root_id`, and recovery resolved from it — a **second
promotion checkpoint** beside B15's accepted `promotion_state`. In
v1_1 the binding is an **immutable cross-store identity/reference map
only**; **B15's item lifecycle and `promotion_state` rows are the sole
authority** for every item's status, for crash recovery, and for the
completion gate; the pass record is a **purely informational
append-only summary** that decides nothing.
**No accepted meaning or policy changed; no new Ness policy choice was
introduced; all other v1_0 mechanisms are preserved** — the two
separate phases, no new fingerprint after successful authorization,
automatic promotion, ready-item independence, §7Q/B7 exclusion
handling, §7E + B11 as the only route to `append_root()`, per-item B15
commits, retry rules A/B/C, completion only with zero blocked items,
accepted B15 archive creation, separately authorized A16 permanent
sealing, interrupted sessions preserved exactly, new linked
continuation sessions, no inspection path, no destruction, and
B-INT-5 through B-INT-8 and all implementation remaining open.

## 1. PLAIN PURPOSE

B-INT-4 **connects the already-designed permission machinery to the
already-designed TSC session store and the permanent-memory
entrance.** It designs no permission, no store, and no memory — it
designs the wires between them, and the guarantees those wires must
hold.

It must guarantee that:

- **permission is checked and safely recorded first;**
- **promotion begins only after successful permission;**
- **promotion is a separate, resumable process;**
- **ready items can continue while blocked items wait;**
- **no item enters memory twice;**
- **a crash loses no committed work and invents nothing;**
- **an interrupted session is sealed forever exactly as written;**
- **a resumed conversation begins in a new, linked session.**

## 2. GOVERNING AUTHORITY, REPOSITORY POINT, AND SOURCES

Authority order: (1)
`01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` — **Master V10
governs all conflicts, regardless of stale internal status wording**;
(2) `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; (3)
`01_AUTHORITATIVE/cursorrules`; (4)
`01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`.

**Repository point:** `nesgeva/NH-GOVERNANCE`, branch `main`, head
**`7a34bcc3e57006cec32abd8c032fa81c0e2bcf03`**, verified at task
start. The complete delta from the previously verified head
(`86985df3…`) was inspected: it added **exactly the accepted A15
source and its closure receipt**, with no modification, deletion, or
rename of any existing file, and **no B-INT-4 candidate exists** in
the repository.

**Sources read at this head** (SHA-256 first-8): Master V10
`2d9ed4c6` — the complete §7E-TSC design, with §§11–20 and §§23–29
read directly (including §16 authorization, §17 promotion sequence,
§18 dependency ordering, §19 partial promotion and idempotency, §20
automatic retry rules, §23–24 archive and duplicate protection, §26
the security-audit event cluster, §27 startup recovery, §28
fail-closed, §29 integration), plus the BAI, SACL, SIA,
security-audit, §7Q, §7E, `append_root()`, startup-recovery, and
Other-Speaker material governing TSC promotion; Defaults `6cd09329`;
`cursorrules` `5050d088`; Companion `cdcc6134`; Map v1.6 `33af648d`;
the eight-bundle plan `2d6483d1`.

**Accepted packages verified present, and consumed rather than
reopened:** **A7 v1.1** `3deacafb`, **A26 v1.1** `41e1f67d`, **A16**
`1b539f57`, **B15 v1.4** `46cf4633`, **B7 v1.3** `7fda28e9`, **A15
v1.1** `9010e9e7` — each with its closure receipt. Also consumed by
reference: **B11 v1.4** `baca06e5` (the active writable-batch
architecture and its `append_root()` contract) and the **accepted B9**
retry architecture and values `e8f4c3de`.

**Nothing in this file redesigns** what fingerprint authorization
means, BAI token policy, SACL recognition policy, A26's separation of
identity and Personal Mode, §7Q privacy meaning, B7 protected
handling, B15's store structure, A16's archive event names, §7E,
`append_root()`, the sealed root store, the TSC lifecycle, blocker
meanings, retry policy, or permanent archive-sealing policy.

## 3. THE COORDINATOR AND THE TWO PHASES

**The TSC Authorization Coordinator (TAC) [proposed]** is the
component B-INT-4 wires: a **stateless-in-authority coordinator** that
owns **no memory, no payload, and no authority of its own**. It holds
only the cross-store coordination records catalogued in §9. Every
decision belongs to its accepted owner: **BAI** owns token validity
and consumption; **SACL** owns recognized-Ness confirmation; **B7/§7Q**
owns privacy and exclusion decisions; **§7E** owns pre-ingest and the
route to `append_root()`; **B11** owns the active writable batch and
the append contract; **B15** owns the session store, its lifecycle,
blockers, checkpoints, and the archive mechanism; the **security audit
system** owns the §26 events.

**Two phases, never one transaction (Master §16 → §17):**
**Phase 1 — authorization** ends the moment authority exists and is
durably recorded. **Phase 2 — promotion** is a separate, resumable
lifecycle that *begins automatically* once Phase 1 succeeded. They are
**never described, implemented, or recovered as a single
transaction.**

## 4. PHASE 1 — AUTHORIZATION WIRING

### 4.1 The requirement (exactly Master §16)

Promotion requires **both conditions simultaneously at token
consumption**:

1. **one valid one-time BAI token**, purpose **exactly**
   `tsc_promotion:<session_id>` — existing, valid, **unused**,
   unexpired, unrevoked, and purpose-bound to **that exact session**;
2. **a fresh, non-stale recognized-Ness SACL confirmation at
   token-consumption time.**

Both are **re-checked inside the authorization boundary immediately
before consumption** — never trusted from an earlier check.

### 4.2 Failure path

If **either** requirement fails:

- **the token is not consumed;**
- **promotion does not begin;**
- **`bai_token_consume_blocked` is recorded by BAI** (its accepted
  fields: session_id, token_purpose, reason) — **this is the live,
  in-process case: a required condition failed and the token remained
  unconsumed. It is BAI's event, written only here, and never
  manufactured by recovery (§4.5);**
- **the session remains exactly in its prior waiting state** —
  `sealed` **or** `interrupted`;
- **an interrupted session is never rewritten as normally sealed**
  (Master §16: failure to authorize does not rewrite an interrupted
  session into a normal sealed session);
- **it continues waiting indefinitely.**

### 4.3 Success path

- **the token is consumed exactly once;**
- **`bai_token_consumed` is recorded;**
- **the session becomes `authorized`;**
- **`authorized_at` is recorded;**
- **`sacl_recognized_ness_confirmed_at` records the exact confirmation
  used** (the confirmation's own identity is bound into the
  consumption evidence — §4.4);
- **`cache_authorization_received` is recorded** (accepted fields
  including session_id and bai_token_id);
- **automatic promotion becomes eligible to begin;**
- **no additional Ness action is required** — no second click, no
  second fingerprint, no manual approval.

### 4.4 Authorization identity, the session claim, and the durable-receipt protocol

**Two identities, two jobs.**

- **`authorization_claim_id`** [proposed] — the **session-level
  serialization slot**, keyed by **`session_id` + `purpose`**. Its
  uniqueness constraint permits **at most one active-or-successful
  authorization operation per session and purpose**. It is written
  **before any token is consumed**. **It is coordination only: it
  grants no authority by itself, and it is not a second authorization
  authority — it merely serializes access to BAI's accepted
  authority.**
- **`authorization_operation_id`** [proposed] — derived
  deterministically from `session_id` + `bai_token_id`, and **attached
  to the winning claim**. It identifies *this attempt with this token*.

**The one-winner rule (session level).** **Only the token attached to
the winning claim may be consumed.** A **second token presented for a
session that is already claimed or authorized is never consumed**: the
request **either returns the existing authorization reference or fails
closed**. **Concurrent requests cannot both win** — the claim's
uniqueness constraint admits exactly one. Therefore **one session can
never have two successful durable consumption receipts.** A
**replacement token may take over only when** the earlier operation is
**durably terminal before consumption**, **or** its **unconsumed token
was revoked and the old claim was safely superseded**. **A token that
is already durably consumed can never be replaced by consuming another
token for the same authorization.** **Every supersession or release is
append-only and explicitly linked** (§8, record 1). **No claim and no
retry may authorize a different session** — the purpose string binds
the claim, the token, and the operation to `<session_id>`.

**BAI and B15 remain separate stores and are NOT merged to simulate one
database transaction.** **And BAI's own state is in-memory only —
Master V10 §25.6: "Nothing persists across restarts" — so BAI's
volatile token map can never be the post-crash proof of anything.**
Durability comes from the **append-only security-audit history**, whose
events Master §26 requires to be **written and flushed immediately
before the producing function returns**.

**The durable consumption receipt is the authorization commit point.**
The existing audit event **`bai_token_consumed`** carries a **complete
verified consumption receipt** binding, at minimum:
`authorization_operation_id`; the **exact `session_id`**; the **exact
`bai_token_id`**; the **exact purpose `tsc_promotion:<session_id>`**;
the **exact SACL confirmation identity**; the **SACL confirmation
timestamp**; the **BAI consumption timestamp**; the
**requester/coordinator identity**; and the **receipt schema/version
plus an integrity reference**. **BAI does not report successful
consumption until that receipt is committed and flushed.** **A failed
or unverifiable receipt write means no durable authority exists, and
B15 must not become `authorized`.**

| Step | Store / owner | Action | Idempotency and one-winner |
|---|---|---|---|
| **A0 — Session claim** | Coordinator (durable claim slot) | Write `tsc_authorization_claim` [proposed] keyed by `session_id` + `purpose`, state `claimed`. **Before any token is touched.** Grants **no authority**. | **Unique on (`session_id`, `purpose`) for active/successful states** — exactly one winner; a concurrent loser is refused and recorded, and returns the existing authorization reference or fails closed. |
| **A1 — Attach and validate (no side effects)** | BAI + SACL + B15 | Attach the token to the winning claim (`authorization_operation_id`). BAI validates the token per §4.1; SACL supplies a **fresh** recognized-Ness confirmation **now**; B15 confirms the session is `sealed` or `interrupted`. **No authority is consumed to test whether downstream work might succeed.** | Read-only; the stage checkpoint is an append-only child event, never a second parent truth. |
| **A2 — Consumption + durable receipt (THE COMMIT POINT)** | **BAI** (live decision, in-process only) + **security-audit history** (durability) | BAI consumes the one-time token **and the `bai_token_consumed` receipt is committed and flushed** with every field above. **Consumption is not reported successful until the receipt is durable.** **If the receipt cannot be written and verified, the attempt fails closed: B15 does not become `authorized`, and the uncertain or in-memory-consumed token is NEVER retried — a new token is required.** | **BAI's in-memory consume admits one winner within the run; only the durable receipt survives.** A receipt already durable for this `authorization_operation_id` → **idempotent success, no second consumption**. A receipt bound to a *different* operation or session → **refused, fail-closed**. **A2 is never re-attempted across a restart with the original `bai_token_id` — that token no longer exists (Master §25.6).** |
| **A3 — TSC authorization commit (one whole B15 transaction)** | **B15** | **One atomic B15 transaction containing all of it:** `lifecycle_status` `sealed`\|`interrupted` → `authorized`; `authorized_at`; `bai_token_id`; `sacl_recognized_ness_confirmed_at`; **the `lifecycle_events` row**; and **the `cache_authorization_received` audit reference**. **Precondition, enforced: a verified durable `bai_token_consumed` receipt bound to this exact `authorization_operation_id`, session, and purpose must exist.** **There is no committed A3 state in which B15's lifecycle row or audit reference is missing — the accepted B15 transaction is whole or it did not happen.** | Operation-keyed: a replay whose transition is already committed for this `authorization_operation_id` is **absorbed and recorded as duplicate-prevention** → **exactly one `cache_authorization_received`**. |
| **A4 — Completion** | Coordinator | The claim → `authorized_complete`; the `tsc_authorization_operation` parent reaches its **single terminal state**, referencing the durable receipt and the B15 transition. **Any external acknowledgment still missing may be repaired idempotently** — the B15 transaction itself remains whole. | Terminal-once; a replayed completion is absorbed. |

### 4.5 Which committed record is authoritative at every crash point

**After a restart, BAI's volatile state is never the source of truth.**
The durable chain is: **the claim → the flushed `bai_token_consumed`
receipt → B15's committed transaction.**

- **Crash before the durable receipt commits** (including after the
  claim, after validation, and during or immediately after an
  in-memory consumption): **no authorization exists — and the original
  token is gone.** Master §25.6 clears **all** BAI token state on
  restart, so the `one_time_authorization_token` itself **no longer
  exists** and **must never be reconstructed, resurrected, or treated
  as reusable**. Therefore:
  - **Recovery must NOT proceed to A2 using the original
    `bai_token_id`.** The absent-or-unverifiable receipt means **no
    authority was ever granted**, and an absent receipt is **never**
    evidence that the prior token is safely reusable.
  - **The old authorization operation becomes durably terminal as
    `failed`** — precisely because **no verified consumption receipt
    exists**. (`failed` is the operation's terminal value; **`released`
    and `superseded` are claim states, never operation states.**)
  - **The reason is recorded truthfully, through mechanisms that
    already exist** — **never by manufacturing a BAI-owned event**:
    the existing **`tsc_authorization_stage_event`** (§8, record 3)
    carries the **exact failure/recovery reason**, and the existing
    **`tsc_crossstore_recovery_event`** (§8, record 8) records
    **`action_taken = blocked_fail_closed`**. **`bai_token_consume_blocked`
    is NOT written by recovery**: it is **BAI's event, for a live
    in-process consume attempt in which a required condition failed and
    the token remained unconsumed**. If BAI **genuinely wrote** such an
    event **before** the crash, recovery **may reference it** — but
    recovery **never creates or backfills it on BAI's behalf**, and
    **missing BAI audit history is never treated as proof that a
    consumption attempt occurred.**
  - **The old claim grants no authority**, and **the claim** — not the
    operation — **becomes `released` or `superseded`, through an
    append-only, explicitly linked record, before another claim can
    win.**
  - **Because the session was never successfully authorized, Rule B
    applies** — this is **Master §20's first condition, applied, not
    broadened**. Continuing **requires a new biometric authorization
    flow and a newly created valid one-time token.**
  - **The new token creates a new `authorization_operation_id`**, and
    the new operation may take over **only through an append-only
    linked supersession** of the old unconsumed / no-receipt claim.
    **The one-session-one-winner rule remains enforced throughout.**
  - **The session stays exactly in its prior waiting state** (`sealed`
    or `interrupted` — **never rewritten**), waiting indefinitely.
- **Receipt-write failure inside the same running process (no crash):**
  **the same fail-closed rule.** **B15 does not become `authorized`**;
  **the uncertain or in-memory-consumed token is never retried**; **a
  new token is required**; and **BAI state is never reconstructed from
  coordinator records.** The coordinator's claim may say *which
  operation owned the attempt* — it **never substitutes for the
  receipt** and **grants no authority.**
- **Crash after the durable receipt commits but before B15 commits:**
  **the flushed `bai_token_consumed` receipt is authoritative —
  authority *was* granted, and it survives the restart.** Recovery
  verifies the receipt (session, purpose, token, SACL identity and
  timestamp, integrity reference) and **forward-completes the B15
  transaction exactly once**, **without another fingerprint**. It
  **never re-consumes** and **never issues new authority**.
- **Crash after B15 commits:** **B15's committed transaction plus the
  verified receipt are authoritative.** The transaction is whole by
  construction; only an **external acknowledgment** may be missing, and
  it is repaired idempotently. No new token, no second event.
- **A receipt that is missing, partial, contradictory, wrong-session,
  wrong-purpose, or unverifiable → fail closed:** no authorization, no
  promotion, recorded honestly, session untouched.

**Every split outcome named in the task is structurally prevented:**
consumed-but-never-authorized (A3 forward-completable from the durable
receipt); authorized-without-a-consumed-token (A3's enforced
receipt precondition); **two tokens consumed for one session** (the
session-level claim's one-winner constraint); two consumptions of one
token (receipt-keyed idempotency); two
`cache_authorization_received` events (operation-keyed absorb); retry
authorizing *another* session (purpose and claim bind
`<session_id>`); stale SACL reuse (freshness evaluated **at
consumption time**, never inherited).

## 5. PHASE 2 — PROMOTION WIRING

**Promotion is a separate lifecycle after authorization. Phase 1 and
Phase 2 are never one transaction.**

### 5.1 Promotion start (Master §17)

From `authorized`, **automatically** — **no second confirmation click,
no fingerprint request, no manual approval**:

1. **Re-check the required security conditions automatically** (SACL
   recognized-Ness currently holds; per Rule A, temporary absence
   **pauses safely**, it does **not** cancel the recorded
   authorization).
2. **Run §7Q/B7 exclusion checks on each item** — **B7 owns the
   decision; the TSC records the result and never makes the privacy
   decision itself.**
3. **Resolve the fingerprint blocker** — `pending_fingerprint_authorization`
   is cleared by the authorization transition.
4. **Items whose only blocker was the fingerprint → `ready`.**
5. **Items with any remaining blocker → `blocked`** — and **no item
   with `speaker_unresolved` may promote**, ever.
6. **Session → `promoting`; `promotion_started_at` recorded;
   `cache_promotion_started` recorded.**

### 5.2 Item processing — separate durable commits

**Order (Master §17, §18):** ascending **`sequence_position`**; a
**parent contribution promotes before its child**; a **blocked parent
defers its child to a later pass** — the child is **never permanently
skipped**; **BOP roots are interleaved by `occurred_at`.**

**Excluded item.** Excluded material moves to **B7 sealed protected
storage** under the correct protection (B7's accepted six-step
crash-safe transfer is **used, not redesigned**). TSC and §7E retain
**only** non-reconstructive `exclusion_metadata`, the **opaque
protected reference**, and handling history. **Excluded content never
reaches `append_root()`.** Item → `excluded`; audit:
`tsc_privacy_exclusion_applied`, `cache_promotion_item_excluded`.

**Blocked item.** Remains `blocked`; recorded in `promotion_state` as
**pending-blocked**; **skipped for this pass**; **unrelated `ready`
items continue**; **clearing the blocker later resumes it
automatically**; **no new fingerprint is required merely because it
waited.** Audit: `cache_promotion_item_blocked`.

**Ready item.**
1. Use the stable **`preingest_capture_id`**.
2. **Derive or preserve the accepted §7E `capture_id`** from it
   (Master §19: `preingest_capture_id` derives the §7E `capture_id`
   used as input to `append_root()`).
3. Attach the accepted **structural source metadata** — **without
   changing the sealed root schema** (no eighth field; no new root
   fields).
4. **§7E performs its existing checks** (its envelope, its blockers,
   its lifecycle).
5. **`append_root()` is called only through the accepted
   root-ingestion path** — the **B11 contract**: WB1 (atomic ownership
   generation + reservation + root-ID commit) → WB2 (commit-fenced
   append into the **active writable batch**, never a sealed batch) →
   WB3 (the single terminal parent operational record).
6. **Rely on `append_root()` idempotency** — **no second root-writing
   path is created**; an already-present item is silently absorbed.
7. **Record `promoted_root_id`;** item → `promoted`; **commit the item
   checkpoint separately.** Audit: `cache_promotion_item_promoted`.

**Boundaries, absolute:** **no raw content moves into the B15
database**; **no TSC item bypasses §7E**; **no TSC component writes
directly into the root store except through the accepted
`append_root()` contract.**

### 5.3 Promotion operation identity and duplicate prevention

- **`session_promotion_operation_id`** [proposed] — deterministic from
  `session_id` + `authorization_operation_id`. **One authorized
  session has exactly one promotion operation**; every retry and
  recovery reuses it.
- **`item_promotion_operation_id`** [proposed] — deterministic from
  `session_promotion_operation_id` + the item identity
  (`contribution_id` | `output_id` | `bop_link_id`).
- **Idempotency keys.** Item promotion's key is the stable
  **`preingest_capture_id`**, from which the §7E `capture_id` is
  derived — **the same identity `append_root()`'s idempotency uses.**
  Authorization's key is `authorization_operation_id`. Continuation's
  key is `continuation_link_operation_id` (§7).
- **The identity relationship, end to end:**
  `session_id` → **`preingest_capture_id`** (per item; unique) →
  **§7E `capture_id`** (derived, §19) → **`append_root()` idempotency**
  → **`root_id`** ( = `promoted_root_id`, unique-when-present in B15)
  → **item checkpoint** — **B15's `promotion_state.phase` and item
  lifecycle row, which are the SOLE authority for that item's status**
  — with `item_promotion_operation_id` serving only as an **immutable
  cross-store reference map** (§8, record 5) that *points at* B15's
  authoritative row, and **B11's `ingest_operation_id`** identifying
  the append itself. **The binding record is never a second promotion
  checkpoint and never a recovery source of truth.**
- **Retry attempt identity** — owned by the **accepted B9 retry-state
  architecture**; B-INT-4 creates **no new retry record** and **invents
  no retry count**: it references B9's episode/attempt identity from
  its own operation record, and the audit event is Master's existing
  `tsc_retry_started`. **A retry attempt is an append-only child event
  under the one parent operation — never a second parent truth, never
  evidence.**
- **Recovery identity** — `recovery_operation_id` [proposed]: recovery
  **is itself one recorded operation**, recorded as a child of the
  operation it recovers.

**A replay must:** recover the **existing root identifier** where a
prior append succeeded; **fill the missing checkpoint exactly once**;
**never create another root**; **never count a duplicate event as new
evidence** (audit: `tsc_duplicate_promotion_prevented`); and **never
turn retry count into evidence weight.**

### 5.4 Partial promotion and crash recovery — every boundary

**Recovery trusts committed and verified truth only. It reconstructs
no conversation content and never pretends an uncertain step
completed.** It **resumes from the first item not already `promoted`,
`excluded`, or currently `blocked`** (Master §19). It uses the
**accepted B15 archive-recovery design** rather than creating another
archive mechanism.

| # | Crash boundary | Authoritative committed truth | Recovery action |
|---|---|---|---|
| 1 | Before `cache_promotion_started` | B15: session `authorized` | Begin promotion automatically (§27). Nothing was started; nothing is assumed. |
| 2 | After `promoting`, before the first item | B15: session `promoting`; no item checkpoints | Resume the loop at the first non-terminal item. |
| 3 | Before an item submission | B15: item `ready` | Submit that item; nothing was sent. |
| 4 | After §7E accepts the item, before `append_root()` | §7E's pre-ingest record (its own lifecycle) | Re-submit under the **same derived `capture_id`**; `append_root()` idempotency prevents any duplicate root. |
| 5 | **After `append_root()` succeeds, before `promoted_root_id` is saved in B15** | **The sealed root store** (for the root's existence) **and B15's `promotion_state` row** (for the item's status — **the sole promotion authority**) | **Derive the §7E `capture_id` from `preingest_capture_id` (§19); run the idempotency lookup against the root store; recover the existing `root_id`; and commit the missing checkpoint into B15 exactly once — never write another root.** The B-INT-4 binding record is consulted **only as a reference map** to find the identities; **it is never the checkpoint and never resolves the item's status.** |
| 6 | After the item checkpoint, before its audit record | B15's committed checkpoint | Append **only** the missing audit anchor, idempotently. No second promotion. |
| 7 | Between two items | Per-item commits | Nothing lost, nothing repeated; resume at the first non-terminal item. |
| 8 | While a blocker clears | B15 class-5 atomic transition + its history row | Either it committed or it did not; an item mid-clear is still `blocked` until committed. Re-read committed state; guess nothing. |
| 9 | While an excluded item transfers into protected storage | **B7's per-step sealed-isolation checkpoint** | Resume **at the committed step** (B7's accepted six-step order). The item stays output-blocked and non-promotable; it **never reaches `append_root()`**. |
| 10 | After all items finish, before the completion event | B15 item checkpoints | Re-verify **no `blocked` item remains**, then write the completion event **once** (idempotent). |
| 11 | After completion, before archive creation | B15: session `promoted` | Run the **accepted B15** archive creation: create and verify the frozen snapshot, then transition. |
| 12 | After archive creation, before `archived` | The **verified** snapshot | B15's **idempotent repair**: reuse the verified snapshot; complete the lifecycle to `archived`. Never recreate. |
| 13 | After `archived` is committed, before acknowledgment | B15: `archived` + the archive-control manifest | Terminal. The acknowledgment replay is absorbed; **the frozen database is never reopened**; effective archive-layer state is read from the **latest verified manifest** (B15). |

### 5.5 Retry rules (Master §20, carried exactly)

**Rule A — already-authorized interrupted promotion.** **Resume
automatically after restart.** **No new fingerprint. No new manual
SACL action.** Current SACL conditions are **checked automatically**;
if recognized-Ness conditions are **temporarily absent**, promotion
**pauses safely until they recover** (audit:
`tsc_retry_security_paused` → `tsc_retry_security_resumed`). **A crash
never cancels the already-recorded authorization.**

**Rule B — new authorization required.** New biometric authorization
is required **only** when **the session was never successfully
authorized**, **or the original BAI token was revoked before promotion
began**. **This condition is never broadened.** **A crash before the
durable receipt commits falls squarely inside its FIRST condition** —
the session was **never successfully authorized**, and the original
one-time token **no longer exists** (Master §25.6) — so a **new
biometric flow and a newly created token** are required, producing a
**new `authorization_operation_id`** that supersedes the old claim
through an **append-only link**. This is Rule B **applied**, not
widened: an authorization that **did** complete durably is **never**
re-asked for a fingerprint merely because of a crash, a wait, or a
retry (Rule A).

**Rule C — temporary technical failure.** **Retry automatically after
the accepted backoff**, using the **accepted bounded attempt limit by
reference** (**accepted B9 values — no retry count is invented here**);
**security conditions are re-checked automatically**;
`promotion_failed` transitions back to `promoting`; **only the failed
or unfinished work resumes**; **no new fingerprint** while the original
successful authorization remains valid. Audit: `tsc_retry_started`.

**After attempts are exhausted, or for a non-retryable failure:** the
session **remains `promotion_failed`**; **Ness is notified privately,
without exposing content** (`tsc_ness_private_notice_sent`;
`cache_promotion_failed`); **Ness may request another attempt** — and
**requesting another attempt is not itself biometric authorization**
for an already-authorized session (it transitions back to `promoting`
after the required security checks).

### 5.6 Completion gate

**While any item remains `blocked`:** the session **stays
`promoting`**; **no `cache_promotion_completed`**; **no retained
archive**; **no `promoted` state**; **no `archived` state.**

**Completion occurs only when the gate reads and verifies B15's
authoritative item lifecycle and `promotion_state` rows directly** —
**every item `promoted` or `excluded`; no item `blocked`; no
unresolved failure remaining.** **The gate never reads its answer from
the B-INT-4 pass record or any other coordination record; a missing or
stale pass record cannot change behavior.** Then: session → `promoted`;
`promotion_completed_at`; `cache_promotion_completed`; **retained
archive creation runs through the accepted B15 mechanism**;
`tsc_retained_archive_created`; session → `archived`.

**B-INT-4 never permanently seals the archive.** Permanent sealing
remains a **later, separate authorization** using the **accepted A16
names** (`tsc_archive_seal_authorized` → `tsc_archive_sealed`) through
**B15's accepted archive-control manifest path**.

## 6. INTERRUPTED-CRASH CONTINUATION SEAM

**The interrupted session:** an `active` session found at restart
**becomes `interrupted`**; `sealed_at` = **the restart time**;
**`cache_sealed` is written with reason `interrupted_crash`**; **every
committed item is preserved exactly**; **nothing is reconstructed**;
it is **never reopened**; it is **never rewritten into a normal sealed
session**; and it **waits indefinitely for its own authorization**.

**The resumed conversation:** creates a **new TSC session** with a
**new `session_id`** and its **own new B15 database**; records
**`continuation_of_session_id` = `<interrupted session_id>`**; records
**`cache_interrupted_linked`**; **remains a separate mutable session
until it is itself sealed**; and is **later authorized and promoted
separately**.

**Continuation-link operation identity:**
`continuation_link_operation_id` [proposed] — derived
**deterministically from the interrupted `session_id` + the durable
resume-event identity** (the recorded resume trigger). This is what
makes the seam safe:

- **Idempotency / duplicate prevention:** the continuation creation is
  **keyed to the resume-event identity**. A **replay of the same resume
  event** finds the existing continuation session and is **absorbed**
  — **two continuation sessions can never be created for one resume
  operation**.
- **Legitimate later continuations versus duplicate retries:** a
  **genuinely new resume event has a new durable identity** → a **new**
  continuation operation and a **new** session (legitimately, a chain
  of continuations may exist). A **replay of the same resume-event
  identity** is a duplicate → absorbed. **The discriminator is the
  resume-event identity, never the interrupted session id.**
- **Crash recovery before the new session exists:** the continuation
  operation record (keyed by `continuation_link_operation_id`) exists
  or it does not. If the new database was not created, recovery
  creates it **once**, under the same operation identity. **Crash
  after the new session exists but before the link or audit
  committed:** recovery completes **only** the missing
  `continuation_of_session_id` link and the `cache_interrupted_linked`
  audit anchor, **idempotently** — never a second session.
- **Records:** the coordination record of §8 (record 7), plus the
  existing audit events `cache_sealed` (reason `interrupted_crash`),
  `tsc_session_created`, and `cache_interrupted_linked` — **written by
  their existing owners, not duplicated here.**

**The link grants no authority.** **The two databases are never
combined.** **No mutable state is copied between them.**
**Authorization, blockers, retries, and promotion checkpoints never
transfer** from one session to the other — each session is authorized
and promoted **entirely separately**, and the link is **provenance
only**.

## 7. REQUIRED INTERFACE CONTRACTS

Each boundary states: **request → response**, decision owner,
operation identity, idempotency key, preconditions, committed result,
failure result, retry class, recovery, audit references, privacy
level. **All record identifiers travel as references — never
payloads.** Privacy level, unless stated otherwise: **references and
structural metadata only; no conversation content; records obey §7Q
and §25 access rules.**

**C1 — BAI → authorization coordinator.**
Request: `{ session_id, bai_token_id, purpose = "tsc_promotion:<session_id>", authorization_operation_id }`. Response: `{ token_state, purpose_binding, validity, consumption_evidence_ref | refusal_reason }`.
**Owner of the decision: BAI** (validity, purpose binding, one-time consumption) — **but BAI's state is in-memory only (Master §25.6) and is therefore never the post-crash proof.** Identity: `authorization_operation_id`, **attached to the winning `authorization_claim_id`**. Idempotency key: the **durable `bai_token_consumed` receipt** for that operation; a second consume for the same operation returns the existing receipt, a different operation or session is **refused**.
Preconditions: **the winning session claim**, plus a token that exists, is valid, unused, unexpired, unrevoked, and purpose-bound to **this exact session**. Committed result: **the complete `bai_token_consumed` receipt committed and flushed** (operation id, session id, token id, purpose, SACL confirmation identity and timestamp, BAI consumption timestamp, requester identity, schema/version, integrity reference) — **and BAI does not report success until it is durable**. Failure: **not consumed** — and **BAI writes `bai_token_consume_blocked` only for this live, in-process case, where a required condition failed and the token remained unconsumed.** **A failed or unverifiable receipt write means no durable authority exists** — and it is **NOT** recorded as a blocked consume (that would misdescribe it): it is recorded as an operation `failed` + claim `released`/`superseded` + `tsc_crossstore_recovery_event` with `action_taken = blocked_fail_closed`. **Recovery never writes `bai_token_consume_blocked` on BAI's behalf.** Retry class: re-validation is retryable **within the same running process only**; a revoked/expired/wrong-purpose/wrong-session token is **terminal** (→ Rule B); **a receipt-write failure is terminal for that token — the uncertain or in-memory-consumed token is never retried, and a new token is required.** Recovery: **the flushed, integrity-verified audit receipt — never BAI's volatile memory and never a coordinator record — is the sole post-crash authority on whether authority exists.** **After a restart the original token no longer exists (Master §25.6) and is never reconstructed, resurrected, or reused; a pre-receipt crash therefore requires a new biometric flow and a new one-time token (Rule B, first condition).** Privacy: identifiers only; **no session content in the receipt.**

**C2 — SACL → authorization coordinator.**
Request: `{ session_id, authorization_operation_id, purpose }`. Response: `{ recognized_ness_confirmed: bool, confirmation_id, confirmed_at, freshness_state }`.
**Owner: SACL** (recognition and freshness). Identity/idempotency: the confirmation's own `confirmation_id`, bound into C1's consumption. Preconditions: a **current** recognized-Ness session. Committed result: the confirmation identity + timestamp recorded as `sacl_recognized_ness_confirmed_at`. Failure: absent/stale/conflicting/unverifiable → **no consumption** (fail-closed). Retry: retryable by re-asking **now**; **a stale confirmation is never reused**. Recovery: obtain a **fresh** confirmation; never inherit. Privacy: identity/security metadata; **never a wellbeing input** (the C-WIS-SEP separation binds).

**C3 — coordinator → B15 TSC store (authorization commit).**
Request: `{ authorization_operation_id, session_id, bai_token_id, sacl_confirmation_id, confirmed_at, consumption_evidence_ref }`. Response: `{ lifecycle_status, authorized_at, event_refs }`.
**Owner: B15** (the store transition). Identity: `authorization_operation_id`. Idempotency: operation-keyed absorb → **exactly one** `cache_authorization_received`. Preconditions: session `sealed`|`interrupted` **and a verified durable `bai_token_consumed` receipt bound to this exact operation, session, and purpose — nothing else may substitute for it** (not BAI's memory, not the coordinator's claim, not an operation record). Committed: **one whole atomic B15 transaction** — `authorized`, `authorized_at`, `bai_token_id`, `sacl_recognized_ness_confirmed_at`, **the lifecycle row, and the `cache_authorization_received` audit reference, together**; **no committed state exists in which the lifecycle row or the audit reference is missing.** Failure: refuse and record; **the session's prior waiting state is preserved unchanged** (an interrupted session is never rewritten as sealed). Retry: retryable (idempotent). Recovery: **forward-completable exactly once from the durable receipt**, with no new fingerprint; a missing **external acknowledgment** is repaired idempotently. Privacy: structural.

**C4 — B15 → B7/§7Q exclusion evaluation.**
Request: `{ session_promotion_operation_id, item refs, purpose = promotion_eligibility }`. Response: `{ per-item decision: permitted | excluded | held, exclusion_metadata (non-reconstructive), opaque_protected_ref (where sealed), decision_ref }`.
**Owner: B7/§7Q** — **the TSC never makes the privacy decision; it records the result.** Identity: `item_promotion_operation_id`. Idempotency: per item + decision version. Preconditions: session `authorized`/`promoting`. Committed: the item's disposition + `tsc_privacy_exclusion_applied` where applied. Failure: **classification cannot complete → fail closed**: the item stays **blocked**, never promoted, never silently permitted. Retry: retryable per B9. Recovery: re-ask B7; **B7's own six-step transfer checkpoints govern any in-flight sealing.** Privacy: **excluded content never leaves B7's protection**; only opaque references and non-reconstructive metadata cross this boundary.

**C5 — B15 → §7E (pre-ingest submission).**
Request: `{ item_promotion_operation_id, preingest_capture_id, derived capture_id, accepted structural source metadata }`. Response: `{ accepted | rejected | blocked, §7E lifecycle state, capture_id }`.
**Owner: §7E** (its envelope and checks). Identity: `item_promotion_operation_id`. Idempotency: the stable `preingest_capture_id` → derived `capture_id`. Preconditions: item `ready`; no active blocker; **not excluded**. Committed: §7E accepts the item for promotion. Failure: **if §7E does not confirm acceptance → fail closed** (item not promoted; recorded). Retry: retryable. Recovery: re-submit under the **same** derived `capture_id`. Privacy: **no raw content enters B15**; payload stays in §7E.

**C6 — §7E → `append_root()` (through the accepted B11 path).**
Request: `{ capture_id, validated root fields, ingest_operation_id (B11) }`. Response: `{ root_id, append_committed | append_duplicate_absorbed | append_rejected | append_interrupted | append_indeterminate }`.
**Owner: `append_root()` / B11** — **the only root-writing path**; the **active writable batch** is selected by B11; **the sealed batch is never appended to.** Identity: B11's `ingest_operation_id` (parent) with its **single terminal record** (WB3). Idempotency: `append_root()`'s own, plus B11's root-ownership authority and commit fence. Preconditions: B11's claim, generation, and fence. Committed: the root exists in the active batch. Failure: rejected/interrupted/indeterminate → **no assumed success**. Retry: per B9 by reference; **never a second root-writing path**. Recovery: **idempotency lookup recovers the existing `root_id`.** Privacy: root content is §7E's; B-INT-4 passes references and identities.

**C7 — `append_root()` → B15 checkpoint.**
Request: `{ item_promotion_operation_id, root_id, ingest_operation_id, outcome }`. Response: `{ checkpoint committed }`.
**Owner: B15 — and B15 alone is the authoritative per-item promotion state** (`promotion_state.phase`, `promoted_root_id`, and the item lifecycle row; the atomic item transition and the crash-recovery checkpoint are B15's accepted machinery). Identity: `item_promotion_operation_id` (a reference only). Idempotency: `promoted_root_id` **unique when present** (B15's constraint). Preconditions: a **verified** append outcome. Committed: **B15** records `promoted_root_id` + item `promoted` + `cache_promotion_item_promoted`. Failure: **if the append result cannot be verified, or a checkpoint contradicts the root store → fail closed and halt that item** (recorded; never guessed). Retry: retryable. Recovery: **crash boundary 5 — resolved from the root store and B15, never from a B-INT-4 record.** Privacy: identifiers only.

**C8 — B15 → retained-archive mechanism.**
Request: `{ session_promotion_operation_id, session_id, completion evidence }`. Response: `{ archive identity, integrity hash, verified: bool }`.
**Owner: B15** (its **accepted** archive creation, freeze, and content-free append-only archive-control manifest). Identity: B15's `transition_operation_id`. Idempotency: that same key — **no duplicate manifest version, no duplicate A16 event**. Preconditions: **no blocked item remains**; `cache_promotion_completed` written. Committed: `tsc_retained_archive_created`; session → `archived`. Failure: **archive verification fails → the archive stays inaccessible, the failure is recorded, and no completion is claimed.** Retry: per B15's accepted recovery. Recovery: **B15's accepted archive recovery — no second archive mechanism is created here.** Privacy: **the retained archive is never exposed to ordinary reasoning**; **no inspection path exists.**

**C9 — interrupted-session recovery → continuation-session creation.**
Request: `{ interrupted_session_id, resume_event_id }`. Response: `{ new_session_id, continuation_of_session_id, link_ref }`.
**Owner: the coordinator (creation) + B15 (both stores).** Identity: `continuation_link_operation_id` (interrupted `session_id` + `resume_event_id`). Idempotency: that key — **one resume event → at most one continuation session.** Preconditions: the interrupted session is durably `interrupted`. Committed: the new session exists with its link; `tsc_session_created`; `cache_interrupted_linked`. Failure: **identity conflict → fail closed**, recorded, no session created. Retry: retryable under the same key. Recovery: create-once, then complete the link/audit idempotently. Privacy: **no state, content, authority, blocker, retry, or checkpoint crosses**; the link is provenance only.

**C10 — every component → security and operational logs.**
Request: one record per real operation (§10). **Owner: the audit system** for the §26 events; **the coordinator** only for its own coordination records (§9). Idempotency: operation-keyed; a replay is absorbed and recorded as duplicate-prevention, **never as new evidence**. Privacy: **references, never sensitive payloads**; **§7Q and §25 access rules govern the logs themselves**; **logs add no evidence weight** and **never log the logging**.

## 8. RECORD CATALOG — B-INT-4-OWNED COORDINATION RECORDS ONLY

**Nothing here duplicates an existing accepted record.** The §26 audit
events (`cache_sealed`, `cache_authorization_received`,
`cache_promotion_started`, `cache_promotion_item_*`,
`cache_promotion_completed`, `cache_promotion_failed`,
`tsc_retry_started`, `tsc_retry_security_paused`/`_resumed`,
`tsc_retained_archive_created`, `tsc_duplicate_promotion_prevented`,
`tsc_privacy_exclusion_applied`, `tsc_ness_private_notice_sent`,
`tsc_session_created`, `cache_interrupted_linked`,
`bai_token_consumed`, `bai_token_consume_blocked`) are **written by
their existing owners and referenced here, never re-created**. B15's
`promotion_state`, `blockers`, `lifecycle_events`, and manifest;
B7's decision records; B11's claim/ownership/fence records and WB3
terminal record; and **B9's retry episode/attempt records** are all
**consumed by reference** — B-INT-4 adds **no retry record and no
retry count**. **In particular, B15 is the sole authority for every
item's promotion state** (`promotion_state.phase`, `promoted_root_id`,
the atomic item lifecycle transition, and the crash-recovery
checkpoint): **no record below is a second promotion checkpoint, and
none may override or substitute for a B15 row.**

All records below are **`[proposed]` candidate-level mechanical
names**. Common to all: **privacy/access level — structural
coordination metadata only; references, never conversation content;
subject to §7Q access rules and §25 authorization**; **corrections are
new linked records, never rewrites** (`supersedes_ref`, optional);
**schema_version** required.

**1. `tsc_authorization_claim` [proposed]** — *the session-level
one-winner serialization slot. **Coordination only — it grants no
authority and is not a second authorization authority; it serializes
access to BAI's accepted authority.*** Fields:
`authorization_claim_id` (required; unique); `session_id` (required);
`purpose` (required; controlled: exactly `tsc_promotion:<session_id>`);
`state` (required; **current-state**; controlled: `claimed` |
`consumed_pending_commit` | `authorized_complete` | `released` |
`superseded` | `failed`); `attached_authorization_operation_id`
(required from A1 — **only the token attached to the winning claim may
be consumed**); `durable_receipt_ref` (required from A2);
`supersedes_claim_ref` / `superseded_by_claim_ref` (optional —
**every supersession or release is append-only and explicitly
linked**); `created_at`; `terminal_at` (optional).
**Uniqueness constraint: at most ONE active-or-successful claim per
(`session_id`, `purpose`).** **Idempotency meaning:** concurrent
requests cannot both win — the loser is refused and either **returns
the existing authorization reference or fails closed**; **one session
can therefore never hold two successful durable consumption
receipts.** **Replacement rule:** a different token may take over
**only** when the earlier operation is **durably terminal before
consumption**, **or** its **unconsumed** token was revoked and the old
claim was **safely superseded** — **a token already durably consumed
can never be replaced by consuming another token for the same
authorization.** **Recovery meaning:** the claim tells recovery which
single operation owns this session's authorization — **but it grants no
authority and NEVER substitutes for the durable receipt.** **When no
verified receipt exists (a pre-receipt crash or a failed receipt
write), the owning OPERATION becomes durably terminal as `failed`
(record 2), and THIS CLAIM becomes `released` or `superseded` — by an
append-only, explicitly linked record — before another claim can
win;** the new
attempt requires a **new token and a new `authorization_operation_id`**
(Rule B, first condition). **No claim and no retry may authorize a
different session.** **Relationship:** references BAI's accepted
authority and the audit receipt; duplicates neither; **BAI state is
never reconstructed from this or any coordinator record.**

**2. `tsc_authorization_operation` [proposed]** — *the cross-store
authorization parent.* Fields: `authorization_operation_id`
(required; unique; = f(`session_id`, `bai_token_id`)); `session_id`
(required); `bai_token_id` (required); `purpose` (required; controlled:
exactly `tsc_promotion:<session_id>`); `state` (required;
**current-state**; controlled: `intent_committed` | `validated` |
`authority_consumed` | `tsc_committed` | `complete` | `blocked` |
`failed` — **a pre-receipt crash or a failed receipt write drives this
record to the durable terminal value `failed`, never to a resumed
consumption of the original token. `released` and `superseded` are NOT
operation values and are not added here: they belong to the claim
(record 1)**); **`authorization_claim_ref`
(required — the winning claim, record 1)**; `sacl_confirmation_ref` (optional until A2; required from
A2); **`durable_receipt_ref` (required from A2 — the flushed
`bai_token_consumed` audit receipt; THIS, not BAI's volatile memory, is
the durable proof)**;
`tsc_transition_ref` (required from A3); `audit_event_refs`
(required — pointers to the owner-written §26/BAI events);
`created_at`, `terminal_at` (optional). Role: **one terminal parent
operational record**; stage progress is recorded by record 3.
**Idempotency meaning:** the unique operation id, attached to the one
winning claim, is the anchor that
makes A2→A3 completable exactly once. **Recovery meaning:** the state
plus the **durable receipt** tells recovery whether authority exists
and how to forward-complete (§4.5) — **volatile BAI state is never
consulted.** **Relationship:** references the claim, the audit receipt,
and B15's transition; duplicates none of them.

**3. `tsc_authorization_stage_event` [proposed]** — *append-only child
checkpoints.* Fields: `stage_event_id` (required);
`authorization_operation_id` (required, FK); `stage` (required;
controlled: `intent` | `validation` | `consumption` |
`tsc_commit` | `completion` | `blocked` | `recovery`); `outcome`
(required); `basis_ref` (required); `at` (required). **Append-only;
never a second parent truth.** Recovery meaning: the last committed
stage is where recovery resumes.

**4. `tsc_promotion_operation` [proposed]** — *the session-level
promotion parent.* Fields: `session_promotion_operation_id` (required;
unique; = f(`session_id`, `authorization_operation_id`));
`session_id`; `authorization_operation_id` (required — **promotion
cannot exist without it**); `state` (required; **current-state**;
controlled: `starting` | `promoting` | `paused_security` |
`retrying` | `completed` | `failed`); `b9_retry_episode_ref`
(optional — **B9 owns retries**); `audit_event_refs` (required);
`started_at`; `terminal_at` (optional). Role: **one terminal parent
record per authorized session's promotion.** Idempotency: the unique
id — retries and recoveries **reuse** it. Recovery: identifies the
one in-flight promotion; never a second.

**5. `tsc_item_promotion_binding` [proposed]** — *an **immutable
cross-store identity/reference map only**. **NOT a promotion
checkpoint, NOT a status record, and NEVER a recovery source of
truth** — **B15 alone owns every item's promotion state.*** Fields:
`item_promotion_operation_id` (required; unique;
= f(`session_promotion_operation_id`, item identity));
`session_promotion_operation_id` (required, FK); `item_ref` (required)
and `item_type` (required; controlled: `contribution` | `nh_output` |
`bop_root`); **`b15_promotion_state_ref` (required — the pointer to the
AUTHORITATIVE B15 `promotion_state` row and item lifecycle row)**;
`preingest_capture_id` (required — the stable idempotency key);
`derived_capture_id` (required — the §7E `capture_id` derived per §19);
`ingest_operation_id` (optional — B11's append parent);
`related_record_refs` (optional — references to B7, §7E, B11, or audit
records). **Immutable: written once, never updated.** **It carries no
disposition, no lifecycle state, no status, and no authoritative
`promoted_root_id`** — every one of those lives **only** in B15, whose
`promotion_state.phase`, `promoted_root_id`, and item lifecycle row are
the **sole** truth for `submitted` / `confirmed` / `promoted` /
`excluded` / `blocked` / `failed`. **Idempotency meaning:** one item →
one binding → one identity chain, so a replay resolves the *same*
identities. **Recovery meaning:** it is a **map, not an answer** —
recovery reads the identities here, then **resolves the item's actual
status from B15 and the root's existence from the root store**, never
from this record. **Relationship:** points at B15's accepted rows,
§7E's capture, B7's protected reference, and B11's append;
**duplicates none of them and overrides none of them.**

**6. `tsc_promotion_pass_record` [proposed]** — *an **append-only
operational summary only. It decides nothing.*** Fields: `pass_id`
(required); `session_promotion_operation_id` (required, FK);
`pass_ordinal` (required); `items_promoted`, `items_excluded`,
`items_deferred_blocked`, `blocked_items_remaining` (required —
**every count is DERIVED from verified B15 state at the moment of
writing, and is INFORMATIONAL ONLY**); `derived_from_b15_at`
(required — the read point); `at`. **Append-only.** **It never decides
whether promotion is complete; it never overrides an item row; and a
missing or stale pass record cannot change behavior** — the completion
gate (§5.6) reads and verifies **B15's authoritative item lifecycle and
`promotion_state` rows directly**. **Recovery meaning:** a readable
history of passes, nothing more; a later pass picks up the deferred
children of previously blocked parents **as determined from B15**, so a
blocked item is never permanently skipped.

**7. `tsc_continuation_link_operation` [proposed]** — *the
continuation seam's coordination parent.* Fields:
`continuation_link_operation_id` (required; unique; = f(interrupted
`session_id`, `resume_event_id`)); `interrupted_session_id`
(required); `resume_event_id` (required — **the durable discriminator**
between a legitimate later continuation and a duplicate retry);
`new_session_id` (optional until created; required at terminal);
`state` (required; **current-state**; controlled: `intent` |
`session_created` | `linked` | `complete` | `blocked` | `failed`);
`audit_event_refs` (required — `tsc_session_created`,
`cache_interrupted_linked`); `at`. **Idempotency meaning: one resume
event → at most one continuation session.** **Recovery meaning:**
create-once, then complete the link and audit idempotently.
**Relationship:** references B15's `continuation_of_session_id` field
and the existing audit event; duplicates neither. **Carries no
authority and no promotion state.**

**8. `tsc_crossstore_recovery_event` [proposed]** — *recovery as one
recorded operation.* Fields: `recovery_operation_id` (required);
`recovered_operation_ref` (required — the authorization, promotion,
item, or continuation operation); `crash_boundary` (required;
controlled: the thirteen boundaries of §5.4 plus the authorization
boundaries of §4.5); **`authoritative_store` (required; controlled:
`security_audit_receipt` | `b15` | `root_store` | `b7` |
`coordinator` — **`bai` is NOT a permitted value: BAI-owned state is
in-memory only and is cleared on restart (Master §25.6), so it can
never be a post-crash source of truth**)**; `committed_state_found`
(required — **for an authorization recovery event it must carry the
receipt reference and its verified binding to
`authorization_operation_id`, `session_id`, `bai_token_id`, the exact
purpose `tsc_promotion:<session_id>`, the SACL confirmation identity
and timestamp, the consumption timestamp, and the receipt
schema/version plus integrity reference**); `action_taken` (required;
controlled: `completed_forward` | `resumed` | `blocked_fail_closed` |
`absorbed_duplicate`); `at`. **Rules, binding:** an **authorization**
recovery event may use `authoritative_store = security_audit_receipt`
**only when it references a complete, flushed, integrity-verified
`bai_token_consumed` receipt**; **a missing or unverifiable receipt
produces `blocked_fail_closed`, never `completed_forward`**; the
**coordinator claim may identify which operation owns the attempt, but
it grants no authority and never substitutes for the receipt**; and
**BAI may make the live consumption decision inside the running
process, but is never a post-crash recovery source of truth.**
**Append-only child** of the operation it
recovers — **never a second parent truth, never evidence weight.**

**9. `tsc_coordination_duplicate_absorbed` [proposed]** — *cross-store
replay absorbed.* Fields: `event_id`; `operation_ref` (required);
`idempotency_key_matched` (required); `absorbed_action` (required);
`at`. **Append-only.** Scope: **only** the coordination replays
B-INT-4 owns (authorization, continuation, pass-level). **Item- and
root-level duplicates use the existing
`tsc_duplicate_promotion_prevented` and B11's
`append_duplicate_absorbed`** — not duplicated here. **Adds no
evidence weight.**

## 9. FULL-TRANSPARENCY LOGGING (B-INT-11, DIRECTLY WIRED)

**One real operation → exactly one operational record.** Retry
attempts, stage checkpoints, and recovery actions are **append-only
child events under their parent operation** — never second parent
truths. The mapping, explicitly:

| Operation | The one record | Owner |
|---|---|---|
| Session claim (one-winner) | `tsc_authorization_claim` created (`claimed`) | B-INT-4 |
| Authorization requested | `tsc_authorization_operation` created, attached to the winning claim | B-INT-4 |
| Authorization validation | `tsc_authorization_stage_event` (`validation`) | B-INT-4 (child) |
| Blocked token consumption **(live, in-process only)** | `bai_token_consume_blocked` — **written by BAI alone, only when a live consume attempt fails a required condition and the token stays unconsumed** — + stage event (`blocked`). **Never written by recovery, never backfilled, and never used for a receipt-write failure.** | **BAI** (event) / B-INT-4 (child) |
| Pre-receipt crash / receipt-write failure **(recovery)** | `tsc_authorization_stage_event` (exact reason) + `tsc_crossstore_recovery_event` (`action_taken = blocked_fail_closed`) + operation → `failed` + claim → `released`/`superseded`. **No BAI-owned event is created; a genuinely pre-existing `bai_token_consume_blocked` may be referenced only.** | B-INT-4 |
| Token consumption **(the durable commit point)** | **`bai_token_consumed` — the complete consumption receipt, committed and flushed before success is reported** + stage event (`consumption`) | **BAI / security-audit history** (durable) / B-INT-4 (child) |
| TSC authorization commit | `cache_authorization_received` + B15 `lifecycle_events` row | **B15 / audit** |
| Promotion start | `tsc_promotion_operation` created + `cache_promotion_started` | B-INT-4 / audit |
| Privacy/exclusion decision use | B7's decision record (referenced) + `tsc_privacy_exclusion_applied` + `cache_promotion_item_excluded` | **B7 / audit** |
| Blocker-caused non-use | `cache_promotion_item_blocked` + `tsc_promotion_pass_record` deferral entry | **audit** / B-INT-4 |
| Item submission | `tsc_item_promotion_binding` (created **once, immutable — identities only**) + **B15's `promotion_state` advance (the authoritative status)** | B-INT-4 (map) / **B15 (truth)** |
| Duplicate absorption | `tsc_duplicate_promotion_prevented` (item/root) or `tsc_coordination_duplicate_absorbed` (coordination) | **audit** / B-INT-4 |
| Item promotion success | `cache_promotion_item_promoted` + **B15's checkpoint (`promotion_state.phase` = confirmed, `promoted_root_id`) — the sole status truth** | **audit / B15** |
| Item failure | `cache_promotion_item_failed` | **audit** |
| Retry scheduling | **B9's retry episode record** (referenced) | **B9** |
| Retry execution | `tsc_retry_started` | **audit** |
| Automatic pause | `tsc_retry_security_paused` + operation state `paused_security` | **audit** / B-INT-4 |
| Automatic resume | `tsc_retry_security_resumed` | **audit** |
| Completion | `cache_promotion_completed` + promotion operation terminal record — **written only after the gate verifies B15's authoritative rows directly** | **audit** / B-INT-4 |
| Archive creation | `tsc_retained_archive_created` + **B15's** manifest version | **B15 / audit** |
| Interrupted sealing | `cache_sealed` (reason `interrupted_crash`) | **audit** |
| Continuation creation | `tsc_session_created` + `tsc_continuation_link_operation` | **audit** / B-INT-4 |
| Continuation linking | `cache_interrupted_linked` | **audit** |
| Crash recovery | `tsc_crossstore_recovery_event` — **authorization recovery records `authoritative_store = security_audit_receipt` (never `bai`), carrying the verified receipt binding; a missing or unverifiable receipt records `blocked_fail_closed`** | B-INT-4 (child) |
| Fail-closed halt | the operation's terminal `blocked`/`failed` state + its stage event | B-INT-4 |

**Log rules, binding:** records **carry references, not sensitive
payloads**; they **obey §7Q and §25 access rules** (the logs are
themselves subject to privacy and authorization); they **add no
evidence weight**; **repetition adds no certainty**; **no record ever
logs "the log was logged"** as another real operation; all are
**append-only and connected** to their session and operation; and
**active/cold handling is consumed by reference from the accepted
logging rules — no new cooling policy is invented here.**

## 10. FAIL-CLOSED REQUIREMENTS

The wiring **stops or waits safely** — never proceeds — when: the
**BAI token** is missing, invalid, used, revoked, wrong-purpose, or
wrong-session; **the durable `bai_token_consumed` receipt cannot be
committed and flushed, or is missing, partial, contradictory,
wrong-session, wrong-purpose, or unverifiable** (**no durable authority
exists → B15 must not become `authorized`; the uncertain or
in-memory-consumed token is NEVER retried; a new token is required; and
an absent receipt is NEVER read as evidence that the prior token is
safely reusable**); **any attempt would reconstruct BAI state from
coordinator records, or treat a restart-vanished token as reusable**;
**any attempt would have recovery write or backfill a BAI-owned event
(`bai_token_consume_blocked`) that BAI did not itself write during a
live consume — recovery records the truth instead through the stage
event, the recovery event (`blocked_fail_closed`), the operation's
`failed` terminal state, and the claim's `released`/`superseded`
state, and invents no new audit event name**; **the session
authorization claim is lost, contradictory, or already held by another
operation**; the **SACL confirmation** is absent, stale,
conflicting, or unverifiable; the **TSC state** is unexpected (Master
§28: a readable but unknown lifecycle value **fails closed into
interrupted sealing**); **§7Q/B7 classification cannot complete**; the
**blocker state cannot be verified**; **§7E does not confirm
acceptance**; the **`append_root()` result cannot be verified**; the
**root-store idempotency lookup fails**; a **checkpoint contradicts the
root store**; **archive verification fails** (the archive stays
inaccessible, honestly reported); a **continuation identity conflicts**;
the **required audit history cannot be written**; or **any authority
owner is unavailable**.

**Never treat "unknown" as success. Never consume authority merely to
test whether downstream work might succeed. Never expose session
content in an error, a notification, or a log.**

## 11. MUST-NEVERS

B-INT-4 must never: merge authorization and promotion into one
transaction; require another fingerprint solely because of a crash or
retry after successful authorization; promote before successful
authorization; bypass BAI or SACL; invent authorization authority;
promote blocked or unresolved-speaker material; let one blocked item
stop unrelated ready items; duplicate a root; rewrite a sealed or
interrupted session; transfer authorization between continuation
sessions; reconstruct lost material; inspect a sealed TSC; create an
inspection token or path; expose retained archives to ordinary
reasoning; permanently seal an archive automatically; create deletion,
destruction, or tombstone behavior; redesign B7, B15, A16, A26, §7E,
BAI, SACL, or `append_root()`; complete B-INT-5, B-INT-6, B-INT-7, or
B-INT-8; claim B-CYCLE-4 or Bundle 5 complete; or begin
implementation.

## 12. EXPLICITLY OPEN AFTER THIS CANDIDATE

ChatGPT's independent audit; any real correction it requires; Ness's
later acceptance; accepted-source placement and a closure receipt;
**B-INT-5, B-INT-6, B-INT-7, B-INT-8**; **Bundle 5 consistency review,
consolidation, and closure**; **B-CYCLE-4 whole-cycle consolidation**;
later Map/Master integration; the exact implementation technology for
cross-store coordination; exact thread/process scheduling; exact
timeout, retry, and backoff **values owned elsewhere** (accepted B9);
exact serialization and final implementation names; and **every code,
schema activation, migration, database, test, runtime, and live-disk
task.**

## 13. DRAFTING CONSISTENCY CHECKS (NOT INDEPENDENT CERTIFICATION)

These are the drafter's own no-loss and consistency checks — **not
independent verification, not certification, not proof of
enforcement**:

- **Two separate phases preserved** — authorization ends at authority;
  promotion is its own resumable lifecycle; never one transaction
  (§3, §4, §5) — consistent in drafting.
- **Master §§16–20 and §§27–29 rules preserved** — the two conditions,
  the exact failure and success paths, the promotion sequence, the
  dependency ordering, §19's `preingest_capture_id` → `capture_id`
  derivation and pick-up rule, retry rules A/B/C, startup recovery,
  fail-closed on unknown state, and the integration boundaries — all
  carried by reference, none rewritten — consistent in drafting.
- **B15 consumed, not duplicated** — its store, lifecycle, blockers,
  checkpoints, archive mechanism, and manifest are called; no second
  store or archive path is created (§5, §7 C3/C7/C8) — consistent in
  drafting.
- **B7 consumed, not duplicated** — B7 owns every privacy/exclusion
  decision and the sealed transfer; the TSC records results only
  (§5.2, §7 C4) — consistent in drafting.
- **§7E and `append_root()` used, never bypassed** — one entry, one
  root-writing path, through B11's accepted contract (§5.2, §7
  C5/C6) — consistent in drafting.
- **Every transaction boundary covered** — A0–A4 and the per-item
  commits, each atomic with its own record (§4.4, §5.2) — consistent
  in drafting.
- **Every crash point covered** — the authorization boundaries of §4.5
  and the thirteen promotion boundaries of §5.4, each naming its
  authoritative committed truth — consistent in drafting.
- **Durable authorization proof survives BAI's memory loss** — BAI
  stays **in-memory only** per Master §25.6; the **flushed
  `bai_token_consumed` receipt** (Master §26: written and flushed
  before the producing function returns) is the **commit point and the
  sole post-crash proof**; a failed or unverifiable receipt means **no
  authority and no `authorized` transition**; **volatile BAI state is
  never a recovery source of truth** (§4.4, §4.5, §7 C1, §8 records
  1–2, §9, §10) — consistent in drafting.
- **No recovery record may name BAI as authoritative** — `bai` is
  **removed** from `authoritative_store`; `security_audit_receipt` is
  the authorization value and is permitted **only** with a complete,
  flushed, integrity-verified receipt whose binding appears in
  `committed_state_found`; **a missing or unverifiable receipt yields
  `blocked_fail_closed`, never `completed_forward`**; the claim
  identifies ownership but **never substitutes for the receipt**
  (§8 record 8, §9, §10) — consistent in drafting.
- **Operation state and claim state are separate and consistent** —
  the **operation** goes durably terminal as **`failed`** (its
  controlled list is unchanged; `released` was **not** added to it),
  while **`released` and `superseded` are claim states only**, applied
  through an append-only explicitly linked record, after which a new
  token opens a **new operation connected through the superseding
  claim** (§4.5, §8 records 1–2, §10) — consistent in drafting.
- **Recovery never fabricates a BAI-owned event** —
  `bai_token_consume_blocked` is written **only by BAI, only for a live
  in-process consume attempt whose required condition failed with the
  token unconsumed**; recovery **never creates or backfills it**, never
  uses it for a receipt-write failure, and **invents no new audit event
  name**; a genuinely pre-existing event may be **referenced**, and
  **missing BAI audit history is never proof that a consumption attempt
  occurred** — recovery instead records the stage event, the recovery
  event (`blocked_fail_closed`), the operation `failed`, and the claim
  `released`/`superseded` (§4.2, §4.5, §7 C1, §8, §9, §10) —
  consistent in drafting.
- **A pre-receipt crash never resurrects the vanished token** — the
  original one-time token is **gone at restart** and is never
  reconstructed or reused; the old operation goes **durably terminal**;
  the claim is **released or superseded by an append-only link**; and
  **Rule B's first condition applies as written** — a **new biometric
  flow and a new token** produce a **new `authorization_operation_id`**,
  with the one-winner rule enforced throughout; an in-process
  receipt-write failure fails closed the same way (§4.4 A2, §4.5, §5.5
  Rule B, §7 C1/C3, §8 records 1–2, §10) — consistent in drafting.
- **Exactly one successful token consumption per session** — the
  durable claim keyed by (`session_id`, `purpose`) admits **one
  winner**, is written **before** consumption, grants **no authority**,
  and permits replacement **only** when the earlier operation is
  durably terminal before consumption or its unconsumed token was
  revoked and the claim safely superseded; **a durably consumed token
  can never be replaced**; supersessions are append-only and linked
  (§4.4, §8 record 1) — consistent in drafting.
- **B15 is the sole per-item promotion and completion authority** —
  the binding record is an **immutable identity map** with no status,
  no lifecycle, and no authoritative `promoted_root_id`; the pass
  record is **informational only and decides nothing**; crash boundary
  5, C7, and the completion gate all resolve from **B15's rows and the
  root store** (§5.3, §5.4, §5.6, §7 C7, §8 records 5–6, §9) —
  consistent in drafting.
- **Duplicate authorization, duplicate roots, duplicate continuation
  sessions, and duplicate events all prevented** — the session claim's
  one-winner constraint, receipt-keyed idempotency, operation-keyed
  absorbs, `append_root()` idempotency plus B15's unique
  `promoted_root_id`, and the resume-event-keyed continuation
  (§4.4, §5.3, §6) — consistent in drafting.
- **Blocked-item independence preserved** — blocked items defer;
  unrelated ready items progress; children of blocked parents return
  in a later pass and are never permanently skipped; completion waits
  for zero blocked items (§5.2, §5.6) — consistent in drafting.
- **Automatic authorized continuation and retry preserved** — Rule A
  resumes without a new fingerprint; Rule C retries automatically
  within the accepted bounded limit; Rule B is not broadened (§5.5) —
  consistent in drafting.
- **Interrupted and continuation sessions kept separate** — sealed
  forever as written, never reopened, never rewritten; the new session
  is separate, linked, and separately authorized; no authority,
  blocker, retry, or checkpoint transfers (§6) — consistent in
  drafting.
- **Complete component-specific §0B logging** — all twenty-three
  operations mapped to exactly one record each, with owners, no
  recursive logging, no evidence weight, references not payloads
  (§9) — consistent in drafting.
- **All policy and implementation choices left open where required** —
  no retry count invented, no threshold chosen, no technology
  selected, no Ness question asked (§12) — consistent in drafting.

---

*End of `NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md`
— `CANDIDATE — NOT ACCEPTED — NOT ADOPTED — NOT BUILT`, awaiting
ChatGPT's independent audit of this actual file and Ness's later
acceptance. Permission is asked once and recorded before anything
moves; promotion then runs by itself, item by item, losing nothing and
inventing nothing; what was interrupted stays exactly as it was, and
the conversation that resumes begins somewhere new — linked, but
never inheriting what it did not earn.*

# NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md

**Status:** DESIGN CANDIDATE — NOT ADOPTED — NOT IMPLEMENTED — NOT
AUTHORITATIVE — NOT INTEGRATED — NOT `PACKAGE_COMPLETE`. Requires ChatGPT's
independent audit and Ness's explicit acceptance.

**Package ID:** B16 — Quarantine-Promotion Evidence Architecture
(Bundle 1 of the confirmed eight-bundle dependency plan).

**Date:** July 6, 2026.

**Governing authority order:** (1) `NH_MASTER-20_CORRECTED_v10.md`;
(2) `NH_DECISION_DEFAULTS-S19_v2_2.md`; (3) `cursorrules`;
(4) `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`.
Subordinate sources/context: `NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`;
`NH_REPLACEMENT_EIGHT_BUNDLE_DEPENDENCY_PLAN_v1_0_CANDIDATE.md`; the accepted
B24 v7 package (`7f5762e5…2171`) and its closure record (`83d79db9…d7e0`);
the accepted B11 v1.4 package (`baca06e5…4a87`) and its closure record
(`cf95a4f8…21f1`); the accepted A2 v1.8 package and its closure record, used
only for preservation/no-reopen boundaries. All source identities were
hash-verified on disk immediately before this candidate was written.

**Purpose in plain terms:** B16 is the safe mechanical gate that lets a
reading move from quarantine/waiting status into production/usable status —
without false success, duplicate promotion, silent influence, lost evidence,
privacy bypass, or rewriting history.

---

## §1 — Frozen standalone scope

B16 owns **only** the mechanics of the quarantine-to-production promotion
seam: promotion evidence structure, promotion identity, transaction
boundaries, idempotency, duplicate prevention, crash recovery,
partial-completion recovery, fail-closed behavior, and §0B logging.

**What B16 is:** a DUMB mechanical gate. It moves a reading's derived
usability status based on the presence, integrity, and binding of recorded
evidence. It carries role and provenance from its sources.

**What B16 is not:** B16 never interprets a reading, never judges its
content, never decides what evidence content counts as "passing," never
makes the promotion decision itself, never creates or writes to a production
readings store, and never implements anything. The promotion **decision** is
made under Ness's authority and recorded; B16 gates mechanically on that
record's verified existence, integrity, and binding.

**Seam vs. cycle:** B16 defines the **per-reading promotion seam** — the
mechanical contract any later connected flow composes. The **connected
end-to-end promotion cycle** (including any batch-level promotion decision
wiring) remains **B-CYCLE-6**, explicitly open (§12). This resolves the
map's CY-G split without conflict: B16 = the seam's mechanical contract;
B-CYCLE-6 = the future full-cycle wiring; C2 = the marker-gate
implementation.

**Settled facts this design builds on (preserved, not reopened):**
- Quarantine vs. production is a real boundary; readings are written to
  quarantine only on the live path; the production readings store
  (`.nh_readings_store.jsonl`) is **absent by design** and must never be
  created as a side effect (Master §6B, cursorrules §1C).
- **Dual production authorization** is required before production writes may
  begin: (1) the `.nh_readings_production_authorized` marker, created only
  by Ness as a deliberate filesystem act — necessary, never sufficient; and
  (2) an approved full PROPOSED CHANGE dry-run. Fail-closed if the marker is
  absent. Removing the marker disables future production writes without
  altering readings already stored. Marker presence never substitutes for
  per-session write/change approval.
- **§11 item 27:** promotion evidence must come from the **gold set**, a
  **held-out set**, and **manual inspection**.
- The `append_reading()` marker-gate check is DECIDED but NOT YET
  IMPLEMENTED — that implementation is **C2**, not B16.
- The 12-field reading schema v1 is sealed as accepted; readings are
  append-only and point at roots via `reads` (root ids verified to exist);
  `idempotency_key` is unique per store.
- Per accepted A2 v1.8: a reading's lifecycle eligibility is derived or
  event-based, never a mutable field; tellings inherit eligibility from the
  parent reading by reference and can never be more promoted than it; one
  identity across locations.

---

## §2 — Preservation and no-reopen boundaries

| Preserved item | B16's obligation |
|---|---|
| **B11 (accepted v1.4)** | Not reopened. No root-producing write occurs in B16; roots are referenced by identity only, read-only. Nothing here touches batches, claims, fences, or the root-ownership authority. |
| **B24 (accepted v7)** | Not reopened. B24's validator-first boundary, benchmark architecture, and acceptance-evidence records are consumed **by reference as evidence inputs** (§5.3); their mechanics are unchanged. Validator success authorizes only a controlled quarantine experiment, never production trust — B16 does not weaken this. |
| **A2 (accepted v1.8)** | Not reopened. B16's promotion representation is exactly A2-compatible: an append-only external record from which the reading's effective state is **derived**; the reading record is never mutated; tellings continue to inherit by reference; no independent telling promotion state exists. |
| **Root schema (seven fields, sealed)** | Untouched. No root is read as content here beyond existence/identity verification; no root field, file, store, marker, or index entry changes. |
| **Reading schema (12 fields, v1)** | Untouched. **No new schema field is invented.** All promotion state lives in **external B16 records** (claim events, evidence snapshot, production-eligibility record) — consistent with A2's derived/event-based lifecycle rule and with the governing files' external-record pattern. |
| **Master V10 / Defaults / cursorrules / map** | Not modified, not integrated into. This is a standalone design candidate only. |
| **TSC** | The TSC authorization/promotion seam (B-INT-4 / CY-D) is a **separate seam** and is untouched. B16 creates no TSC inspection path of any kind; nothing here reads sealed TSC contents. |
| **A29 / B-HOLD / B9 / B10 / B1–B26 retrieval** | Not decided (§12). |

---

## §3 — Identities

### §3.1 The quarantined reading under consideration

- **`reading_id`** — the reading's permanent `id` (12-field schema). One
  identity across locations and across all lifecycle states, per A2.
- **`reading_idempotency_key`** — the reading's store-unique key, carried as
  corroborating identity evidence.
- **`reading_integrity_ref`** [proposed] — an externally computed integrity
  reference over the complete immutable reading record as stored in
  quarantine. It detects a damaged, swapped, or altered record; it is
  **evidence about** the reading, never a new reading field.
- The reading's **root references** (`reads` list) are part of its identity
  context: each referenced root must exist by identity in its owning sealed
  or B11-governed batch. Verification is **read-only by identity** — no root
  content is consumed here and no root is touched.

### §3.2 The promotion claim — one canonical claim per reading

`promotion_claim` [proposed] — **one permanent claim per `reading_id`**,
keyed by `promotion_claim_key` [proposed], deterministic from `reading_id` +
the single promotion operation type. It serializes every promotion attempt
for that reading **before** any production-eligibility record can exist.

| Field [all proposed] | Content |
|---|---|
| `promotion_claim_key` | Deterministic: `reading_id` + promotion operation type — immutable |
| `reading_integrity_ref` | Bound at claim establishment; every later attempt checked against it |
| `claim_status_events` | Append-only status events (never edited) |
| `reservation_events` | Append-only reservation/phase events (§5.2) |
| `evidence_snapshot_ref` | Bound when B16-2 commits (§5.3) |
| `production_eligibility_ref` / committed refs | Bound once, at the terminal committed transition |

### §3.3 Operation identities — parent and children

- **`promotion_operation_id`** [proposed] — the **parent** end-to-end
  operation: one caller invocation of the promotion seam. Attempt-specific;
  never the duplicate-prevention identity (that is the claim).
- **Child operation identities** [proposed `promotion_child_op_id`] — every
  separately executed internal real operation carries one stable unique
  child ID referencing its parent: the B16-0 lookup where it acts, the B16-1
  reservation boundary, the B16-2 evidence-verification boundary, the B16-3
  commit boundary, a reservation release/cancellation, a recovery
  resolution. Each child receives **exactly one** §0B operational log; the
  parent ID is never reused as a child's; no operation ID — parent or
  child — ever carries two operational logs (§10). This mirrors the accepted
  B11 v1.4 parent/child contract without reopening it.

---

## §4 — Promotion-candidate lifecycle

All statuses are **derived from the claim's append-only events** — never a
mutable field on the reading, never an edit to any stored record.

| Status [all proposed] | Meaning |
|---|---|
| `quarantined` | Baseline. The reading exists in quarantine with **no committed promotion**. Not a B16-created record — it is the derived absence of one. |
| `promotion_requested` | A durable promotion request event exists for the claim; no reservation, no rights, no production effect. |
| `promotion_reserved` | **Exactly one** live reservation exists (§5.2 single-winner compare-and-commit). No production effect. |
| `promotion_evidence_checked` | The immutable evidence snapshot (§5.3) is committed and bound to the claim and reservation. Still no production effect. |
| `promotion_committed` | **Terminal, absorbing, idempotent success:** the production-eligibility record exists with its complete matching trail (§5.4). Repeats return `duplicate_absorbed`. |
| `promotion_rejected` | Attempt-terminal with recorded cause (evidence failure, decision refusal, integrity conflict). The reading **remains quarantined** and never becomes production through this attempt. Whether and when a new attempt is permitted is **policy owned elsewhere** (A29 / B9, §12); mechanically, a later attempt is a new request under the **same permanent claim**, lookup-first over the recorded history. |
| `dependency_blocked_held` | Non-terminal waiting: a required dependency (hold condition, missing authorization, A29-gated readiness) blocks progress. **Fail-closed: a held candidate never becomes production by waiting.** Hold lifecycle, release mechanics, and release policy are **B-HOLD / A29** (§12) — B16 defines only this fail-closed waiting semantic and the recorded blocked event. |
| `promotion_interrupted` | The attempt ended before B16-3 with durable evidence of non-commit (crash, lost race, released reservation). Safe technical re-attempt under the same claim; substantive retry **policy** remains B9's (§12). |
| `indeterminate_recovery_required` | Evidence unreadable or contradictory. No reservation, no commit, no production effect; resolution only through §8 — never by guessing. |

**Lifecycle proofs (each carried mechanically below):**
1. **No promotion without evidence** — B16-3 refuses without a committed,
   integrity-valid, claim-bound evidence snapshot (§5.3–§5.4).
2. **No duplicate promotion can commit** — one permanent claim per reading;
   single-winner reservation; one production-eligibility record ever per
   claim; commit verifies the durable reservation fence immediately before
   committing (§5.2, §5.4, §6).
3. **A crash cannot create false production status** — production status is
   derived only from a validated committed record with its complete trail;
   every pre-commit crash leaves derived status unchanged (§8).
4. **No production record without a matching claim/evidence trail** — an
   orphan record is invalid, grants nothing, and fails closed (§8 row 15).
5. **A committed promotion is terminal and idempotent** — absorbing lookup
   at B16-0; duplicates return the committed result (§5.1, §6).
6. **A rejected or held reading does not silently become production** —
   rejection and hold are recorded, derived-status-visible, and excluded by
   the production-consumption gate (§7).
7. **Recovery never rewrites or reconstructs a reading** — lookup-first,
   append-only resolution everywhere (§8).

---

## §5 — Transaction boundaries

| # | Boundary [proposed] | Commit content | If absent / refused |
|---|---|---|---|
| B16-0 | **Promotion-status lookup** | Read-only, side-effect-free lookup of the claim's derived status. Found `promotion_committed` → return `duplicate_absorbed` with the committed production-eligibility ref — no reservation, no new records. Found reserved under another live attempt → this attempt commits nothing (`promotion_interrupted`, claim ref returned). Found held/blocked → `dependency_blocked_held` returned. No claim → the durable request event is appended (establishment; no rights granted). | Claim status unprovable (events unreadable) → **fail closed**, `indeterminate_recovery_required` (§9) |
| B16-1 | **Atomic promotion reservation** | **One compare-and-commit boundary**: from no-live-reservation, create one reservation binding `{promotion_claim_key, reading_id, reading_integrity_ref, promotion_operation_id + child ID}` in phase `reserved`. **At most one live reservation per claim, ever; concurrent attempts admit exactly one winner; losers observe the winner and append nothing.** A crash after B16-1 leaves a discoverable reservation with no rights beyond proceeding. | No committed reservation → no evidence check, no commit; refused while another live reservation exists |
| B16-2 | **Evidence-snapshot verification commit** | Verify every required evidence input (§5.3), then commit **one immutable `promotion_evidence_snapshot` record** [proposed] with its own integrity reference, bound to the claim and this reservation; reservation phase advances `reserved` → `evidence_checked` by compare-and-commit. The snapshot is the **only** evidence set B16-3 may commit against — evidence cannot be swapped after checking. | Any required input missing, unreadable, unauthorized, integrity-failed, or contradictory → `promotion_rejected` (recorded cause) or `dependency_blocked_held` or `indeterminate_recovery_required` per §9 — never a partial pass |
| B16-3 | **Production-eligibility commit (the commit point)** | Entry is one compare-and-commit of the reservation `evidence_checked` → `commit_fenced` (§5.2). The commit then **verifies the durable fence immediately before committing** and appends **one `production_eligibility_record`** [proposed] `{reading_id, promotion_claim_key, evidence_snapshot_ref, parent + child operation IDs, timestamp, record schema version}`; the claim's terminal `promotion_committed` transition is bound to this commit and is recovery-completable from the record evidence alone. The quarantined reading is **not moved, edited, deleted, copied, or rewritten**; no production store is created or written. | Fence not won (release won) → no commit ever for that reservation; commit attempted without a durable fence or with a snapshot/claim mismatch → refused and logged; not reached → nothing durable, caller outcome per §4 |
| B16-4 | **Parent terminal log commit** | The mandatory §0B **single terminal operational record of the parent** `promotion_operation_id` — `promotion_committed` / `promotion_duplicate_absorbed` / `promotion_rejected` / `promotion_interrupted` / `promotion_blocked_held` / `promotion_indeterminate` — durably appended after the child operations and canonical records resolve, **before** any acknowledgement. Exactly one terminal record per parent operation. | Committed but terminal log absent → **no success acknowledgement yet**; recovery appends only the missing terminal idempotently (§8 row 4); logging failure never invalidates the committed record |
| B16-PR | **Post-commit indexes/coverage** | Rebuildable production-eligibility indexes and coverage material for reading-side gates. **Never gates success; never the duplicate-prevention or status authority.** | Incomplete → committed promotions remain fully valid; rebuild idempotently (§8 row 17) |

### §5.2 Reservation phases and the commit fence

The reservation moves only through the **three legal append-only paths**
(pattern preserved from accepted B11 v1.4, applied to this seam without
reopening B11):

1. `reserved` → `released` (normal release/cancellation, legal **only**
   from `reserved` or `evidence_checked`);
2. `reserved` → `evidence_checked` → `commit_fenced` → `committed`
   (successful promotion);
3. `reserved`/`evidence_checked` → `commit_fenced` →
   `recovery_released_no_commit` [proposed] — a **distinct recovery-only
   terminal**, committable only when all four hold: exclusive recovery
   authority is active; no live executor can still complete the operation;
   the exact claim and snapshot identities were checked; commit non-existence
   is **conclusively proven**. Otherwise `indeterminate_recovery_required`.

Fencing and release compete on the **same authoritative phase; exactly one
wins**. Once `commit_fenced`: release is forbidden; no second reservation
may be created; only commit completion or the strict recovery release may
proceed. A delayed executor holding a stale pre-fence view cannot commit —
the commit boundary verifies the durable `commit_fenced` phase immediately
before committing. Once `released` or `recovery_released_no_commit`: fencing
and commit are forbidden for that reservation, permanently; a later attempt
is a **new** request/reservation under the same permanent claim.

### §5.3 Required evidence inputs (the snapshot's mandatory contents)

The B16-2 snapshot must verify and bind, by reference and integrity — B16
verifies **presence, integrity, authorization, and binding**; it never
judges content:

1. **Reading identity + integrity:** `reading_id`, `reading_idempotency_key`,
   `reading_integrity_ref` matching the claim's bound value.
2. **Root references:** every root id in the reading's `reads` list verified
   to **exist by identity** — read-only; no root content consumed; no root
   or batch record touched (B11 preserved).
3. **Gold-set results evidence reference** — the recorded B24-architecture
   acceptance evidence for the applicable gold-set run (settled §11 item 27
   source #1). B24's mechanics are consumed by reference, unchanged.
4. **Held-out set results evidence reference** (settled source #2).
5. **Manual-inspection record reference** (settled source #3) — the recorded
   inspection outcome. The inspection itself is performed under Ness's
   authority; B16 verifies the record, never performs or scores inspection.
6. **Recorded promotion decision reference** [proposed
   `promotion_decision_ref`] — the recorded **passing decision**, made under
   Ness's acceptance authority. B16 gates on its verified existence and
   binding to this reading; what constitutes "passing" is **policy, open**
   (A29 / Ness — §12).
7. **Dual production-authorization evidence:** (a) verification that the
   Ness-only `.nh_readings_production_authorized` marker is present —
   recorded as a verification event; **necessary, never sufficient**; its
   runtime code enforcement remains C2; and (b) the reference to the
   approved PROPOSED CHANGE dry-run record. **Promotion without both
   protections is a MUST-NEVER** — either absent → fail closed, no commit.
8. **Privacy/access authorization:** the §7Q internal-use authorization for
   this operation, with §7Q before §7R and SACL scope honored where
   applicable. Unauthorized → fail closed (§9); never bypassed.
9. **Hold/dependency check:** the A29/B-HOLD interface slot — if a hold or
   dependency block is recorded for this reading, the attempt resolves
   `dependency_blocked_held`; release policy and mechanics stay open (§12).

The snapshot is **one immutable append-only record** carrying all references
plus its own integrity reference. Missing, unreadable, or contradictory
inputs never produce a partial snapshot.

---

## §6 — Idempotency and duplicate-prevention points (ten)

| Point | Key / mechanism |
|---|---|
| Promotion claim | `promotion_claim_key` — one permanent claim per reading, ever; establishment converges, never duplicates |
| Request event | claim + request identity — repeat requests are lookup-first no-ops returning current derived status |
| Reservation (B16-1) | claim + one compare-and-commit from no-live-reservation; exactly one winner; at most one live reservation per claim |
| Evidence snapshot (B16-2) | claim + reservation identity — one snapshot per reservation; repeat verification finds the committed snapshot |
| Commit fence (B16-3 entry) | reservation identity + one compare-and-commit `evidence_checked` → `commit_fenced`; competes with release; exactly one winner ever |
| Production-eligibility record (B16-3) | `promotion_claim_key` — **one record ever per claim**; duplicate commit attempts absorb against it |
| Recovery release | reservation identity — at most one `recovery_released_no_commit` ever; duplicate recovery is a no-op |
| Parent terminal log (B16-4) | `promotion_operation_id` — exactly one terminal record per parent; child logs are never second parent logs |
| Child-operation log | `promotion_child_op_id` — exactly one operational log per child; retries locate the existing log by identity |
| Recovery run | `recovery_run_id` + per-action lookup-first — every repeat is a no-op returning committed findings |

---

## §7 — No silent production influence

- **Production-consumption gate:** any production reasoning, retrieval,
  state, or output path may consume a reading **only** when its derived
  status is `promotion_committed` through a **validated complete trail**
  (claim + snapshot + production-eligibility record, integrity-checked).
  Requested, reserved, evidence-checked, rejected, held, interrupted, and
  indeterminate candidates are **excluded fail-closed** — exclusion is the
  gate's mechanical default, not a best-effort filter (§8 row 20).
- The Master's quarantine boundary is preserved unchanged: quarantined
  readings are not automatically available to production functions; nothing
  in B16 relaxes LMAC, §7Q, §7R, or §7P.
- **Promotion records are not content:** the claim, snapshot, eligibility
  record, and logs are machine-state evidence about the promotion. They are
  never readable as production content, never inputs to interpretation, and
  never make the reading more true (§10, §11).
- Tellings inherit unchanged per A2: a telling becomes production-eligible
  only through its parent reading's derived committed status — never
  independently, never earlier.

---

## §8 — Recovery matrix (lookup-first; idempotent; no rewrite; no reconstruction; no false success; fail-closed on unreadable or contradictory evidence)

**Protocol:** every recovery action carries a `recovery_run_id`, inspects
the claim's committed events **first**, acts by appending only, and never
touches the quarantined reading, any root, any accepted record, or any
committed evidence.

| # | Crash / condition | Resolution |
|---|---|---|
| 1 | Crash before any promotion claim/request exists | Nothing to undo; no derived status changed; the next attempt runs B16-0 normally |
| 2 | Claim/request durable, evidence check absent (reservation may or may not exist) | Lookup-first: no reservation → status `promotion_requested`, next attempt proceeds via B16-1; live reservation in `reserved` → resume B16-2 under it or release it (legal path 1) and resolve `promotion_interrupted` |
| 3 | Evidence snapshot committed, production commit absent | Reservation `evidence_checked`: resume B16-3 (fence → commit) if the snapshot still validates, or release (legal only pre-fence) → `promotion_interrupted`; if already `commit_fenced` → resolve per rows 4/6 mechanics: complete from commit evidence or strict recovery release under the four proofs; missing proof → `indeterminate_recovery_required` |
| 4 | Production-eligibility record present, parent terminal log absent | **No success acknowledgement yet.** Complete the claim's terminal `promotion_committed` transition from the record evidence idempotently, then append exactly one missing parent terminal (B16-4); only then acknowledge |
| 5 | Terminal log present, acknowledgement absent | The outcome is durable and committed: recovery returns the recorded terminal outcome to the caller; nothing is re-executed; no second terminal is written |
| 6 | Duplicate promotion attempt (same reading, any time) | B16-0 absorbs: committed → `duplicate_absorbed` with the existing eligibility ref; live reservation → `promotion_interrupted` (claim ref); rejected/held history → returned as derived status; **no second claim, reservation-winner, or eligibility record can exist** |
| 7 | Conflicting promotion attempts (race) | The B16-1 compare-and-commit admits exactly one reservation winner; losers observe and append nothing; at the commit point, fence-vs-release admits exactly one; conflicting **evidence** (contradictory records for one claim) → `indeterminate_recovery_required`, fail closed — no winner guessed |
| 8 | Promotion rejected | Attempt-terminal with recorded cause; reservation released; the reading remains quarantined; derived status shows the rejection; re-attempt permission is policy (A29/B9, §12) — mechanically a later new request under the same claim, lookup-first |
| 9 | Promotion held / dependency-blocked | `dependency_blocked_held` recorded; reservation released or never granted per where the block surfaced; **waiting never becomes production**; release mechanics/policy stay B-HOLD/A29 (§12) |
| 10 | Quarantined reading missing or unreadable | Fail closed: `indeterminate_recovery_required`; no commit, no reconstruction, no substitute record; the condition is surfaced; the claim's history is preserved |
| 11 | Root reference missing or unreadable (a `reads` id cannot be verified) | Evidence check fails → `promotion_rejected` (recorded cause: unverifiable root reference) or `indeterminate_recovery_required` if the verification itself cannot be safely read; no root is created, repaired, or guessed; B11's authorities are consulted read-only |
| 12 | B24 acceptance evidence (gold-set / held-out results) missing or failed | Evidence check fails closed → `promotion_rejected` with recorded cause, or `dependency_blocked_held` where the evidence is pending rather than failed; B24's records are never fabricated, inferred, or substituted |
| 13 | Contradictory evidence (any two bound inputs disagree; snapshot integrity mismatch) | `indeterminate_recovery_required`; fail closed; both versions preserved append-only; no guessing which is correct |
| 14 | Privacy/access block (§7Q/SACL refusal) | Fail closed: the attempt resolves `promotion_rejected` (cause: unauthorized) or `dependency_blocked_held` per the refusal class; **never bypassed, never retried around the gate**; the block event is logged under §7Q's own visibility rules |
| 15 | Production-eligibility record present **without** complete promotion evidence (orphan) | The record is **invalid and grants nothing**: derived status is not `promotion_committed`; production consumption stays excluded; the orphan is marked by an append-only invalidation event with cause; `indeterminate_recovery_required` pending resolution; nothing is deleted — history preserved |
| 16 | Promotion evidence present without a production record (snapshot committed, no eligibility record) | = row 3: resume or release per the reservation phase; the snapshot alone grants nothing |
| 17 | Post-commit index/coverage incomplete (B16-PR) | Committed promotions remain fully valid; rebuild the rebuildable material idempotently; **never** treat index state as status authority |
| 18 | Duplicate recovery run | `recovery_run_id` + lookup-first over append-only events: every repeat is a no-op returning committed findings — no second release, no second terminal, no re-execution |
| 19 | Attempted promotion of an already production-committed reading | B16-0 absorbs (`duplicate_absorbed`); no new reservation; the committed record and trail are returned; nothing is re-committed |
| 20 | Attempted use of a quarantined reading before promotion | The production-consumption gate (§7) excludes it fail-closed; the attempt is refused and logged; no partial or provisional influence occurs |

---

## §9 — Fail-closed matrix

| Condition | Behavior |
|---|---|
| Evidence missing (any §5.3 input absent) | No snapshot; `promotion_rejected` (recorded cause) or `dependency_blocked_held` where pending; never a partial pass |
| Evidence contradictory | `indeterminate_recovery_required`; no guessing (§8 row 13) |
| Evidence unreadable | `indeterminate_recovery_required`; fail closed until provable |
| Evidence unauthorized (§7Q/SACL) | Refused; never bypassed (§8 row 14) |
| Hold / dependency block recorded | `dependency_blocked_held`; waiting never becomes production (§8 row 9) |
| Dual authorization incomplete (marker absent **or** dry-run approval absent) | **No commit — MUST-NEVER**; fail closed with the missing protection named |
| Claim events / snapshot / eligibility record unreadable | Derived status unprovable → `indeterminate_recovery_required`; production consumption stays excluded |
| Orphan production-eligibility record | Invalid; grants nothing (§8 row 15) |
| Commit attempted without durable fence, or with claim/snapshot mismatch | Refused and logged; nothing commits |
| Production store absent (it is, by design) | B16 never creates, writes to, or authorizes it; eligibility is a record, not a store write |

---

## §10 — §0B operational logging

**Binding distinction (preserved from the governing files and accepted
B11 v1.4 without reopening it):** claim status events, reservation phase
events, evidence snapshots, and production-eligibility records are
**canonical transaction/state records** — machine facts required to
establish state. They are not §0B operational logs and are **never extra
evidential votes**. Separately, **every real operation emits exactly one
append-only §0B operational log** under its own stable operation identity:
child logs for B16-0 (where it acts), B16-1, B16-2, B16-3, a release, and a
recovery resolution — each under its own `promotion_child_op_id` referencing
the parent; **B16-4 is the single terminal operational record of the
parent** `promotion_operation_id`. A child log is never a second parent log;
no operation ID ever carries two operational logs; retries and recovery
locate the existing log by identity and never append another. Writing a log
generates no further log; a genuinely separate later operation receives its
own.

| Record [all proposed] | Covers |
|---|---|
| `promotion_requested` | Each durable request event's operational log (establishment/lookup child where it acts) |
| `promotion_claim_reserved` | Each B16-1 reservation child log — the single winner's grant; losers' observations resolve into their own attempts' terminals |
| `promotion_evidence_checked` | Each B16-2 child log — one log carrying the full snapshot commit with all bound references |
| `promotion_committed` | The B16-3 child log — one log carrying the fence win, the eligibility-record append, and the claim terminal together (one atomic operation, one log) |
| `promotion_rejected` | Each rejection outcome, with recorded cause class |
| `promotion_interrupted` | Each pre-commit termination with durable non-commit evidence |
| `promotion_indeterminate` | Each fail-closed indeterminate resolution |
| `promotion_blocked_held` | Each dependency/hold block event (mechanics-only; policy stays A29/B-HOLD) |
| `promotion_duplicate_absorbed` | Each B16-0 absorption against a committed promotion |
| `recovery_applied` / `recovery_noop` | Each recovery resolution child operation — applied actions vs. lookup-only no-ops, keyed by `recovery_run_id` |
| `fail_closed_event` | Each §9 fail-closed occurrence, with the named missing/failed condition |
| Parent terminal (B16-4) | `promotion_committed` / `promotion_duplicate_absorbed` / `promotion_rejected` / `promotion_interrupted` / `promotion_blocked_held` / `promotion_indeterminate` — exactly one per parent, before acknowledgement |

**Logging rules:** one real operation → one operational log; no
log-about-logging; **no double evidence** — a log, a state record, or their
repetition never makes the reading more true, never strengthens the
interpretation, and never serves as evidence for the reading's content;
records link by operation/claim/reading **identities only**, never copying
reading or root content; §7Q internal-use, visibility, identity, and
authority restrictions govern every record's access, including logs of
privacy blocks; active/cold lifecycle follows §0B and is not redesigned
here.

---

## §11 — Boundary rules and must-nevers

- **Privacy/access:** §7Q before §7R; visible-output order §7Q first, SACL
  second; SACL scope before retrieval where applicable. Every B16 operation,
  record, and log obeys them. A privacy refusal is a fail-closed outcome,
  never a bypassable obstacle.
- **DUMB/SMART:** B16 is DUMB machinery — it establishes machine-state and
  provenance facts (statuses, references, integrity checks) and never
  interprets. It never turns the promotion decision, the evidence, or the
  logs into a judgment about the reading's meaning or truth. SMART
  judgments (what passes, what "enough" means, what the reading says)
  belong to their policy owners and to Ness.
- **Root/reading separation:** roots are referenced by identity only,
  read-only; root evidence and prior-reading context stay separate; no root
  record, batch, seal, or index changes; B11's seam and authorities are
  consumed read-only and unchanged.
- **Quarantine/production separation:** preserved absolutely. The reading
  never moves, never mutates; status is derived from external append-only
  records; the production readings store is neither created nor written nor
  authorized here; promotion without both dual-authorization protections is
  a MUST-NEVER.
- **No-double-evidence:** the promotion trail is evidence **that a
  promotion occurred**, never evidence that the reading's interpretation is
  correct; derived material is never independent evidence for the
  interpretation that produced it; repetition adds no certainty.
- **TSC:** authorization and promotion remain separate seams; B16 creates no
  TSC inspection path and reads no sealed TSC content.
- **Must-nevers:** no false production success; no duplicate promotion
  commit; no silent production influence from quarantine; no production
  store as a side effect; no reading or root history rewritten; no privacy
  bypass; no implementation or disk action.

---

## §12 — Explicit open dependencies (recorded, not solved)

- **A29** — what "enough" means for holding or responsible reading, and the
  policy content of the promotion decision/pass thresholds. B16 defines the
  seam those connect to; it closes none of their policy.
- **B-HOLD** — hold lifecycle, release mechanics, recovery, and duplicate
  prevention for held objects. B16 records only the fail-closed
  `dependency_blocked_held` semantic and its interface slot.
- **B9** — retry-state architecture and all retry values. B16's
  `promotion_interrupted` permits technical re-attempt under the same
  claim; every retry **policy** and value stays B9's.
- **B10** — reread operation identity and recovery (untouched here).
- **B-CYCLE-6** — the connected end-to-end promotion flow, including any
  batch-level promotion decision wiring that composes this per-reading seam.
- **B1/B26** — retrieval ranking and degraded-retrieval behavior downstream
  of the production-consumption gate.
- **C2** — the `append_reading()` marker-gate implementation (decided, not
  implemented; Register C).
- **Physical production representation and any storage-engine choice** —
  future implementation work under the dual authorization; the eligibility
  record defined here is a design contract, not a store.
- Exact evidence-record formats/locations, threshold values, and tuning —
  declared later configuration/calibration where not already settled.
- Any coding, migration, disk verification, store creation, or
  implementation — separately authorized, after design completion.

---

## §13 — Worked state traces (proofs)

**Trace 1 — no promotion without evidence.** An attempt reaches B16-3 with
no committed snapshot: the fence entry requires phase `evidence_checked`,
which only the B16-2 snapshot commit produces — refused; nothing commits.
An attempt whose snapshot is missing input #7a (marker verification):
B16-2 fails closed with the missing protection named; no snapshot exists;
B16-3 is unreachable.

**Trace 2 — racing attempts, one reservation, one commit.** Attempts A and
B both find claim(R) with no live reservation and race B16-1. The
compare-and-commit admits exactly one (A); B observes and appends nothing
(`promotion_interrupted`). A proceeds through B16-2 and wins the fence at
B16-3; a delayed release arriving after the fence is refused. **One
eligibility record ever exists for claim(R).**

**Trace 3 — crash cannot create false production status.** Crashes after
the request (row 2), after the reservation (row 2), after the snapshot
(rows 3/16), and mid-fence (row 3) each leave derived status short of
`promotion_committed`; the production-consumption gate excludes the reading
throughout. Only the committed eligibility record with its validated trail
changes what production may consume.

**Trace 4 — orphan record grants nothing.** A `production_eligibility_record`
is found whose claim has no matching snapshot binding. Validation fails; the
derived status is **not** committed; consumption stays excluded; an
append-only invalidation event records the orphan; resolution proceeds
fail-closed (row 15). A record can never appear as valid without its trail.

**Trace 5 — committed is terminal and idempotent.** After commit, every
later attempt for R absorbs at B16-0 (`duplicate_absorbed`, row 19); every
duplicate recovery run is a no-op (row 18); nothing re-commits, and the one
record is returned each time.

**Trace 6 — rejected and held never leak.** A rejection (failed held-out
evidence, row 12) and a hold (row 9) each leave the reading quarantined
with recorded derived status; the §7 gate excludes both; waiting or
re-requesting changes nothing until a new attempt lawfully commits under
the same claim with fresh verified evidence.

**Trace 7 — recovery never rewrites.** Every row of §8 resolves by reading
committed append-only events and appending resolution records. The
quarantined reading's bytes, the roots it references, prior snapshots, and
prior logs are never edited, reconstructed, or deleted — including the
orphan case, which is marked, not erased.

**Trace 8 — one parent, one log each, before acknowledgement.** A full
successful pass: children C0 (lookup/establishment), C1 (reservation), C2
(snapshot), C3 (fenced commit) each emit exactly one child log; B16-4 then
writes the single parent terminal; only then is the caller acknowledged. A
crash between C3 and B16-4 yields no acknowledgement until recovery appends
the one missing terminal (row 4).

---

## §14 — Frozen closure-checklist self-audit (not a final verdict; ChatGPT's independent audit and Ness's explicit acceptance are pending)

| # | Checklist item | Status |
|---|---|---|
| 1 | B16's standalone scope stated clearly | §1 — met |
| 2 | B11, B24, A2, Master V10, Defaults, cursorrules, and the map preserved | §2 — met; nothing reopened, changed, or integrated |
| 3 | Quarantine-to-production promotion identity defined | §3 (reading identity; one permanent claim per reading; parent/child operation identities) — met |
| 4 | Transaction boundaries defined | §5 (B16-0…B16-4 + B16-PR, with the reservation-fence contract) — met |
| 5 | Idempotency and duplicate prevention defined | §6 (ten points; one eligibility record ever per claim) — met |
| 6 | Crash and partial-completion recovery defined | §8 (twenty rows; lookup-first; no rewrite) — met |
| 7 | Fail-closed behavior defined | §9 + §5.3 — met |
| 8 | Silent production influence from quarantine prevented | §7 production-consumption gate + §8 row 20 — met |
| 9 | Root/reading separation preserved | §11 (identity-only, read-only root references) — met |
| 10 | Quarantine/production separation preserved | §7, §11 (derived status; no move/mutation; no store) — met |
| 11 | DUMB/SMART boundaries preserved | §1, §11 (B16 is DUMB; decisions/judgments stay with their owners) — met |
| 12 | Privacy/access boundaries preserved | §5.3 input 8, §8 row 14, §10, §11 — met |
| 13 | §0B one-operation/one-log and no-double-evidence obeyed | §10 (parent/child; canonical records vs. logs; logs add no truth) — met |
| 14 | A29, B-HOLD, B9, B10, B-CYCLE-6, B1/B26, and implementation choices left open | §12 — met |
| 15 | No code, migration, store, runtime action, Master update, or map update created | §15 — met |

**CRITICAL-severity self-check — no issues found by this self-check.** No
authority is violated; no accepted B11/B24/A2 rule is changed; no root or
reading history is modified; false production success is structurally
impossible (status derives only from a validated committed trail; orphans
grant nothing); duplicate promotion cannot commit (one claim, one
reservation winner, one fence winner, one eligibility record ever);
quarantined material cannot silently influence production (fail-closed
consumption gate); recovery is lookup-first, append-only, and fail-closed on
unreadable or contradictory evidence; privacy/access gates are never
bypassed; no implementation or disk action exists anywhere in this design.

**IMPORTANT-severity self-check — no issues found within the frozen
scope.** Promotion identity, all transaction boundaries, ten idempotency
points, twenty recovery rows, the fail-closed matrix, and the §0B structure
are present and mutually consistent; the dual-authorization MUST-NEVER is
carried verbatim in substance; the three settled evidence sources are bound
as snapshot inputs by reference without redesigning B24.

**MINOR-severity, non-blocking notes (recorded per the severity standard):**
all new identifiers are `[proposed]` pending later naming; the lifecycle
names follow the instruction's suggested vocabulary; evidence-record
formats/locations and threshold values are correctly left to later
configuration/calibration and policy owners; the seam-vs-cycle split with
B-CYCLE-6 is recorded in §1.

---

## §15 — Delivery statement

**Created:** exactly one new file —
`NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md`
(this file).

**Changed:** nothing existing. No authoritative, accepted, map, plan,
closure, historical, or candidate file was modified, overwritten, renamed,
moved, patched, normalized, or deleted. No commit, push, or upload was
performed. No code, migration, production store, quarantine-store change,
seal action, marker action, terminal command, or implementation artifact was
created. Source identities were hash-verified on disk immediately before
writing (B11 v1.4 `baca06e5…`, its closure record `cf95a4f8…`, B24 v7
`7f5762e5…`, its closure record `83d79db9…`, the confirmed plan
`2d6483d1…`) and remain untouched.

---

*`NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md` —
DESIGN CANDIDATE — NOT ADOPTED — NOT IMPLEMENTED — NOT `PACKAGE_COMPLETE`.
The Bundle-1 quarantine-promotion evidence seam: one permanent promotion
claim per reading; single-winner reservation with a commit fence; an
immutable bound evidence snapshot carrying the three settled evidence
sources, the recorded decision, the dual production authorization, privacy
authorization, and the hold interface; one production-eligibility record
ever, from which status is derived without moving or mutating anything; a
fail-closed production-consumption gate; twenty lookup-first recovery rows;
and parent/child one-operation/one-log §0B structure — with A29, B-HOLD,
B9, B10, B-CYCLE-6, B1/B26, C2, and all implementation choices explicitly
open, and B11, B24, A2, Master V10, Defaults, cursorrules, and the map
preserved untouched. Awaiting ChatGPT's independent audit and Ness's
explicit acceptance.*

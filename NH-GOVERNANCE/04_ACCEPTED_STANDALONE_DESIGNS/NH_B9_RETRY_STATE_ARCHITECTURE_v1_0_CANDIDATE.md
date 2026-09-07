# NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md

**Status:** DESIGN CANDIDATE — NOT ADOPTED — NOT IMPLEMENTED — NOT
AUTHORITATIVE — NOT INTEGRATED — NOT `PACKAGE_COMPLETE`. Requires ChatGPT's
independent audit and Ness's explicit acceptance.

**Package ID:** B9 — Retry-State Architecture (Bundle 1 of the confirmed
eight-bundle dependency plan).

**Date:** July 6, 2026.

**Governing authority order:** (1) `NH_MASTER-20_CORRECTED_v10.md`;
(2) `NH_DECISION_DEFAULTS-S19_v2_2.md`; (3) `cursorrules`;
(4) `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`. Subordinate:
the Design and Wiring Map v1.6 candidate; the eight-bundle plan; accepted
B24 v7, B11 v1.4, B16 v1.0 and their closure records; accepted A2 v1.8 for
preservation boundaries. Source identities hash-verified on disk before
writing.

**Purpose in plain terms:** B9 is the "try again safely" system. It prevents
infinite loops, duplicate work, false success, hidden re-execution, and lost
crash state — without deciding any retry count, delay, budget value, or
whether a substantive rejection deserves another chance.

---

## §1 — Frozen standalone scope

B9 owns **only** the mechanical retry-state architecture for N.H operations
that fail, time out, crash, are interrupted, are rejected, are
dependency-blocked, or become indeterminate: outcome classification for
retry purposes, retry identity, retry-state records, transaction boundaries,
idempotency, duplicate prevention, crash recovery, partial-completion
recovery, fail-closed behavior, and §0B logging.

**What B9 is:** DUMB bookkeeping and admission control **around** existing
seams. A retry attempt executes **through the source seam's own boundaries
under the seam's own canonical identity** — B9 never creates an alternate
execution path, never re-implements a seam, and never weakens a seam's
duplicate defense.

**What B9 is not:** B9 decides no retry count, no wait/backoff value, no
retry budget value, no final fallback point, no substantive-retry policy, no
A29 "enough," and no A25 reread mode. This design directly realizes the
Master's open item — "the queue representation for nonterminal technical
failures, retry count, timing, backoff, and trigger mechanism" — by
designing the **representation, identities, records, boundaries, and
recovery** while leaving every **value** and every **policy trigger** as
declared configuration/policy inputs (§12).

**Settled facts this design builds on (preserved, not reopened):**
- A handled retryable technical failure is **held for the retry policy and
  is never auto-treated as a crash-interrupted pass** — crash recovery and
  handled-failure retry are separate (Master §7G-A; CY-A settled).
- The failed reading job stays `in_progress` with a recorded retryable pass
  failure; terminal jobs are never re-selected; job-level reading
  idempotency (`reading_idempotency_key`) holds across any number of
  attempts.
- **Until the separately designed bounded acceptance-failure retry rule is
  adopted, a substantively rejected proposal is terminal** (Master open
  item 2; §7G). B9 preserves this exactly and defines only the record shape
  and authorization slot a future adopted rule would use.
- B11 v1.4's `interrupted` and B16 v1.0's `promotion_interrupted` permit
  technical re-attempt under the **same canonical key**; every retry policy
  and value was reserved to B9 — B9 now carries the mechanics, values still
  open.

---

## §2 — Preservation and no-reopen boundaries

| Preserved item | B9's obligation |
|---|---|
| **B11 (accepted v1.4)** | Not reopened. A retried ingestion runs WB0–WB4 under the same `capture_id` claim; B11's claims, generations, fences, and root-ownership authority are the duplicate defense — B9 adds bookkeeping only. |
| **B16 (accepted v1.0)** | Not reopened. A retried promotion runs B16-0…B16-4 under the same promotion claim; `promotion_interrupted` classifies as technical-retryable here without changing B16. |
| **B24 (accepted v7)** | Not reopened. A B24/acceptance rejection classifies as **terminal substantive** here; nothing in B9 re-runs, weakens, or bypasses the acceptance boundary. |
| **A2 (accepted v1.8)** | Not reopened; nothing here touches telling identity or lifecycle. |
| **Master V10 / Defaults / cursorrules / map** | Not modified, not integrated into. Root schema (seven fields) and reading schema (twelve fields) untouched; all B9 state lives in external records. |
| **A29 / A25 / Story-Layer thresholds** | Not decided (§12). |

---

## §3 — Outcome classification for retry purposes

B9 consumes each source operation's **own durable terminal outcome** and
classifies it — classification is mechanical routing, never a judgment
about meaning:

| Retry class [proposed] | Source outcomes (by reference) | Retryability |
|---|---|---|
| `terminal_success` | committed / `duplicate_absorbed` / completed — **including an honest `insufficient_context` fallback reading, which is a valid completed outcome** | Never retried. A retry request absorbs against the committed result. |
| `terminal_substantive` | Acceptance-check rejection (fabrication, malformed, incomplete, unsupported certainty, mode violation, channel confusion — the distinct recorded reasons); identity conflict; permanent schema-invalid re-presentation | **Not machine-retryable.** Terminal until a separately adopted policy authorizes otherwise (Master open item 2). B9 defines the authorization slot only (§5, R1). |
| `technical_retryable` | `is_technical_and_potentially_retryable = true` pass failures; model/service timeout; unavailable or stale index; interrupted processing; B11 `interrupted`; B16 `promotion_interrupted`; lost races; write failures marked technical | Retryable **only** through R1 admission under an existing declared budget configuration. |
| `dependency_blocked_held` | B-HOLD live hold; B16 `dependency_blocked_held`; any recorded dependency block | **Not retried.** Waits on the block's own release interface; a retry request while blocked is refused and recorded. |
| `privacy_refused` | §7Q / SACL refusal | **Not machine-retryable and never retried around.** Only a genuinely changed, recorded authorization state permits a new attempt — as a new admission with that record referenced. |
| `indeterminate` | Any seam's `indeterminate_recovery_required` | **Never retried.** Recovery-first, fail-closed: no admission until the seam's own recovery resolves the state. |

**Three retry classes of attempt:**
1. **Technical retry** — machine-admissible re-attempt of a
   `technical_retryable` outcome, same source identity, under a declared
   budget (§5 R1).
2. **Substantive retry** — a meaning-level re-attempt of a
   `terminal_substantive` outcome. **Whether this ever occurs is policy,
   open** (Master item 2; A29-adjacent). B9 defines only the record shape:
   admission requires a recorded, adopted policy reference **plus** a
   per-case authorization reference; absent either, admission fails closed.
3. **Policy-authorized retry** — an explicitly authorized re-attempt (for
   example, Ness-directed) carrying its recorded authorization reference.

---

## §4 — Identities and records

- **`retry_group_id`** [proposed] — one canonical group per **source
  operation duplicate-prevention identity**: deterministic from
  {the seam's canonical key, the seam's operation class}. Examples: the
  reading job's `enqueue_key`; B11's ingestion claim key; B16's
  `promotion_claim_key`; B10's reread claim key. One group ever per source
  identity; establishment converges.
- **`attempt_id`** [proposed] — deterministic {`retry_group_id`, attempt
  number}. Each admitted attempt links to the **seam parent operation** it
  launches (that seam operation keeps its own parent/child identities and
  logs — B9 references them by identity, never duplicates them).
- **`retry_request_op_id`** [proposed] — the parent operation of one retry
  request (lookup → admission → outcome recording → disposition), with
  child operation IDs per separately executed step, each with exactly one
  §0B operational log (the accepted parent/child pattern, consumed without
  reopening B11 v1.4).
- **`retry_state_record`** [proposed] — one append-only record set per
  group: source identity and class; classified prior outcomes (by
  reference); attempt entries {attempt_id, class, admission evidence —
  budget ref or authorization refs, seam parent-op ref, durable outcome
  ref, resulting class}; disposition events. **Canonical state records, not
  operational logs, never extra evidential votes.**
- **Declared inputs (values open, §12):** `retry_budget_ref` [proposed] —
  the configuration record naming count/timing/backoff for a class+seam;
  `retry_policy_ref` / `retry_authorization_ref` [proposed] — the adopted
  policy and per-case authorization for substantive or policy-authorized
  retries. **B9 requires these records to exist and be referenced; it never
  supplies defaults.**

---

## §5 — Transaction boundaries

| # | Boundary [proposed] | Commit content | If absent / refused |
|---|---|---|---|
| R0 | **Group lookup** | Read-only: establish-or-find the group; read the latest classified outcome. `terminal_success` → absorb (return the committed result; no attempt). `terminal_substantive` without adopted policy + authorization refs → refuse with recorded status. `dependency_blocked_held` → refuse; wait on release. `indeterminate` → refuse; recovery-first. `privacy_refused` → refuse absent a recorded changed-authorization reference. | Group evidence unreadable → fail closed; no admission on unprovable state |
| R1 | **Attempt admission (one compare-and-commit)** | Atomically: verify the class is admissible; verify **no live attempt exists for the group** (at most one at a time); verify the required reference exists — `retry_budget_ref` for technical, `retry_policy_ref` + `retry_authorization_ref` for substantive/policy-authorized — and is satisfied per its own declared terms; commit the attempt entry {attempt_id, admission evidence}. Concurrent admissions: exactly one winner; losers observe and append nothing. **A missing or unconfigured budget/policy reference → fail closed: no attempt, no silent default, no hidden automatic retry.** | No committed admission → no execution of any kind under B9's name |
| R2 | **Attempt execution** | The admitted attempt runs **the source seam's own boundaries under the seam's own canonical identity** (same `enqueue_key` / claim key), launching a new seam parent operation referenced from the attempt entry. B9 adds nothing to the seam's path; the seam's idempotency guarantees at most one committed result per identity across all attempts. | Seam refusal/failure resolves through the seam's own contract; B9 records the outcome at R3 |
| R3 | **Outcome recording** | Lookup-first against the seam's **durable terminal evidence**; append the attempt's outcome reference and resulting class. Never inferred, never guessed: no durable seam terminal → the attempt is unresolved (rows 3, 17). | Contradictory or unreadable seam evidence → group `indeterminate`, fail closed |
| R4 | **Disposition + parent terminal log** | Append the group disposition event where changed, then the retry request's **single parent terminal operational log** — before any acknowledgement. Exactly one terminal per `retry_request_op_id`. | Terminal absent → no acknowledgement; recovery appends only the missing terminal (row 5) |

---

## §6 — Idempotency and duplicate-prevention points (nine)

| Point | Key / mechanism |
|---|---|
| Retry group | `retry_group_id` — one group ever per source identity; establishment converges |
| Attempt admission | group + one compare-and-commit; at most one live attempt; deterministic `attempt_id` |
| Execution | **the seam's own canonical identity** — the sole duplicate-execution defense; unlimited attempts can commit at most the one result |
| Outcome recording | attempt + durable seam terminal reference — lookup-first, append-once |
| Absorption | `terminal_success` groups absorb every later request against the committed result |
| Budget/authorization reference | admission binds the exact reference record used; a repeat admission attempt finds the committed entry |
| Parent terminal (R4) | `retry_request_op_id` — exactly one terminal per request |
| Child-operation log | child op ID — exactly one log per child; retries of B9's own steps locate the existing log |
| Recovery run | `recovery_run_id` + lookup-first — repeats are no-ops returning committed findings |

---

## §7 — Interaction rules with adjacent seams

- **B24 / acceptance rejection:** classifies `terminal_substantive`; the
  rejected proposal never silently becomes anything; the recorded distinct
  rejection reason is carried by reference. **Terminal until an adopted
  rule exists** — B9 changes nothing about that rule's content or timing.
- **B16 `promotion_interrupted`:** `technical_retryable`; an admitted
  attempt is a new promotion parent operation under the **same promotion
  claim** — B16's claim absorbs or completes exactly as B16 specifies.
- **B-HOLD:** a live hold on the source or its inputs →
  `dependency_blocked_held`; **B9 never retries around a hold** and never
  triggers release; release is B-HOLD's interface under A29's policy.
- **B10 rereads are not retries.** A retry re-attempts the **same**
  canonical identity to complete its one outcome. A reread is a **new**
  operation identity (a new reread claim per recorded trigger) producing a
  **new reading layer**. B9 refuses "retry" requests that name a completed
  reading — the correct instrument there is a B10 trigger, and B9 says so
  in its refusal record without creating one.
- **§7H "scheduled automatic retry":** that trigger class is mechanically
  **served by B9's technical retry while the original operation remains
  open/incomplete** (job `in_progress`, no committed reading). Where a
  completed reading exists (including an honest `insufficient_context`
  fallback), later re-examination is B10's territory under a recorded
  trigger — never a B9 retry.

---

## §8 — Recovery matrix (lookup-first; idempotent; no rewrite; no false success; fail-closed on unreadable or contradictory evidence)

| # | Crash / condition | Resolution |
|---|---|---|
| 1 | Crash before any retry-state record | Nothing to undo; the source seam's own state is untouched and authoritative; the next request runs R0 normally |
| 2 | Retry-state record exists, attempt not started (admission committed, no seam operation launched) | Lookup finds the admitted attempt with no seam parent-op ref → launch the seam operation under the same identity (R2), or release the admission by appending an attempt-abandoned entry with cause; the seam's idempotency makes either path safe |
| 3 | Attempt started, no terminal (seam operation launched, no durable seam terminal) | The attempt is **unresolved**: resolve through the **seam's own recovery** first; B9 records only what the seam's durable evidence then proves; no outcome is invented; the group admits nothing new while an attempt is live |
| 4 | Attempt terminal exists, parent (retry-request) log missing | Append the missing R4 terminal idempotently from the recorded disposition; only then acknowledge |
| 5 | Terminal log exists, acknowledgement missing | The outcome is durable: return the recorded terminal; nothing re-executes; no second terminal |
| 6 | Duplicate retry request | R0 absorbs or refuses per the group's current class; no second live attempt can be admitted; the request receives the recorded status |
| 7 | Retry after committed success | Absorbed: the committed result is returned (`terminal_success`); no attempt, no re-execution |
| 8 | Retry after permanent rejection | Refused: `terminal_substantive` stays terminal; the refusal names the missing adopted-policy/authorization references; nothing runs |
| 9 | Retry while dependency-held | Refused and recorded; the group waits on the hold's release interface; no attempt is admitted |
| 10 | Retry after indeterminate state | Refused: recovery-first; the source seam's `indeterminate_recovery_required` must resolve through its own §11-class process before any admission |
| 11 | Retry after privacy/access refusal | Refused absent a recorded changed-authorization reference; **never retried around**; the refusal is logged under the gate's own visibility rules |
| 12 | Retry after timeout | Timeout is `technical_retryable`: normal R1 admission under the declared budget; the seam's identity guarantees no duplicate result |
| 13 | Conflicting retry attempts (race) | The R1 compare-and-commit admits exactly one; losers observe and append nothing; conflicting **evidence** about the group → `indeterminate`, fail closed |
| 14 | Retry budget unavailable / unconfigured / exhausted-per-its-terms | **Fail closed:** no attempt, no silent default, no invented number; the fail-closed event names the missing/exhausted reference; the group's disposition records the block |
| 15 | Missing source operation (group references an identity no seam knows) | Fail closed: `indeterminate`; nothing is fabricated; the condition is surfaced for resolution against the seam's own records |
| 16 | Missing or contradictory prior outcome | Unreadable → fail closed pending the seam's evidence; contradictory (two durable terminals claimed for one identity) → `indeterminate`, surfaced — the seam's own duplicate defenses make this an integrity incident, never a coin-flip |
| 17 | Downstream seam operation completed but the retry record is incomplete | Lookup-first against the seam's durable terminal: complete R3/R4 idempotently from that evidence; the seam's result is authoritative; nothing re-runs |
| 18 | Duplicate recovery run | `recovery_run_id` + lookup-first over append-only records: repeats re-read committed state and re-apply nothing |
| 19 | **Attempted hidden automatic retry without authorization** | **Refused and logged as a fail-closed event.** No execution path exists under B9 without a committed R1 admission carrying its budget/authorization reference; an attempt to bypass R1 is recorded as the violation it is |

---

## §9 — Fail-closed matrix

| Condition | Behavior |
|---|---|
| Budget/policy/authorization reference missing, unreadable, or unconfigured | No admission; no default; fail-closed event naming the reference |
| Group or outcome evidence unreadable | No admission on unprovable state; `indeterminate` pending the seam's evidence |
| Contradictory outcome evidence | `indeterminate`; surfaced; never resolved by guessing |
| Live attempt unresolved | No new admission for the group; seam recovery first |
| Source held / blocked / privacy-refused | Refused per §3 classes; never retried around |
| Admission bypass attempted | Refused + logged (§8 row 19) |

---

## §10 — §0B operational logging

Canonical state records (the group's retry-state records, attempt entries,
disposition events) are machine facts — **not** operational logs and never
extra evidential votes. **Every real B9 operation emits exactly one
append-only §0B operational log** under its own identity: child logs for
lookup-where-it-acts, admission, outcome recording, and recovery
resolution — each under its own child op ID referencing the parent
`retry_request_op_id`; **R4 is the single parent terminal.** The launched
seam operation's logs belong to the seam under its own identities — B9
references them and never duplicates them (no double evidence; a retry
record never makes any outcome more true; repetition adds no certainty).
Records link by identities only; §7Q internal-use, visibility, and
authority restrictions govern every record's access; no log-about-logging.

| Record [proposed] | Covers |
|---|---|
| `retry_requested` / `retry_absorbed` / `retry_refused` | Each R0 resolution with its class and status |
| `retry_attempt_admitted` | Each R1 winner, with the exact budget/authorization reference bound |
| `retry_attempt_outcome_recorded` | Each R3 recording against durable seam evidence |
| `retry_group_disposition` | Each disposition change (canonical state event) |
| `retry_terminal` (R4) | The single parent terminal per request, before acknowledgement |
| `recovery_applied` / `recovery_noop` / `fail_closed_event` | Recovery resolutions and every §9 occurrence, including row 19 violations |

---

## §11 — Boundaries and must-nevers

DUMB throughout: B9 routes and records; it never judges meaning, never
decides that a rejection deserves another chance, never re-scores evidence.
Privacy/access gates are never bypassed and govern B9's own records. No
retry makes an outcome more true. Must-nevers: no infinite loop (admission
requires a satisfied declared budget); no duplicate work (the seam's
identity is the defense); no false success (outcomes only from durable seam
terminals); no hidden re-execution (row 19); no lost crash state
(lookup-first over append-only records); no implementation or disk action.

---

## §12 — Explicit open dependencies (recorded, not solved)

- **Exact retry counts, wait/backoff values, budgets, and the authorized
  fallback point** — declared configuration/calibration values, not
  invented here; the Master's deferred value set stays deferred.
- **Whether a substantive rejection is ever retried for meaning reasons**,
  and that rule's content — the future bounded acceptance-failure retry
  rule (Master open item 2); until adopted, terminal stays terminal.
- **A29** ("enough") and **A25** (reread mode) — untouched.
- **The retry trigger's activation policy** (when the machine initiates an
  admissible technical retry) — B9 defines the admission mechanics; the
  activation schedule/trigger values are declared configuration.
- **B-CYCLE wiring; B1/B26 retrieval behavior; B-CYCLE-6 beyond the B16
  seam; C2; all implementation and disk/runtime choices.**

---

## §13 — Frozen closure-checklist self-audit (not a final verdict; independent audit and explicit acceptance pending)

| # | Item | Status |
|---|---|---|
| 1 | Standalone scope stated clearly | §1 — met |
| 2 | Master V10, Defaults, cursorrules, map, B11, B16, B24, A2 preserved | §2 — met |
| 3 | Operation identity defined | §4 (group, attempt, parent/child) — met |
| 4 | Transaction boundaries defined | §5 (R0–R4) — met |
| 5 | Idempotency defined | §6 (nine points) — met |
| 6 | Duplicate prevention defined | §5 R1, §6, §7 (seam identity as sole execution defense) — met |
| 7 | Crash recovery defined | §8 — met |
| 8 | Partial-completion recovery defined | §8 rows 2–5, 17 — met |
| 9 | Fail-closed behavior defined | §9 — met |
| 10 | Component-specific §0B logging defined | §10 — met |
| 11 | No-double-evidence preserved | §10 — met |
| 12 | Privacy/access boundaries preserved | §3 (`privacy_refused`), §8 row 11, §10, §11 — met |
| 13 | A29, A25, thresholds, final values, full B-CYCLE wiring, implementation left open | §12 — met |
| 14 | No code, migration, store, marker action, disk action, Master update, or map update | §14 — met |

**CRITICAL-severity self-check — no issues found by this self-check.** No
authority violated; no accepted rule changed; Ness-owned policy undecided
everywhere it appears; false success impossible (durable seam terminals
only); duplicate execution impossible (seam identity governs); unsafe loops
impossible (no admission without a satisfied declared budget; fail-closed on
absence); nothing overwritten; no silent use of held material (held →
refused); no privacy bypass; no implementation or disk action.

**IMPORTANT-severity self-check — no issues found within the frozen
scope.** Identity, boundaries, nine idempotency points, nineteen recovery
rows, fail-closed matrix, and §0B structure present and mutually
consistent; the B9/B10 and B9/B-HOLD boundaries are stated explicitly (§7)
and match the coordination note.

**MINOR notes:** all identifiers `[proposed]`; the Master's deferred value
set is echoed, not filled.

---

## §14 — Delivery statement

**Created:** this file only (one of the four instructed Bundle-1 fast-pass
files). **Changed:** nothing existing — no authoritative, accepted, map,
plan, closure, or candidate file modified; no commit/push/upload; no code,
migration, store, marker, seal, terminal, or runtime action. Sources
hash-verified before writing and untouched.

---

*`NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md` — DESIGN CANDIDATE. The
Bundle-1 retry-state seam: outcome classes routing to absorb/refuse/admit;
one group per source identity with the seam's own key as the sole duplicate
defense; admission only under existing declared budget or recorded
policy+authorization references, fail-closed otherwise; nineteen
lookup-first recovery rows; one-operation/one-log with no double evidence —
with every retry value, the substantive-retry rule, A29, A25, and all
implementation explicitly open, and B11, B16, B24, A2, Master V10,
Defaults, cursorrules, and the map preserved untouched. Awaiting ChatGPT's
independent audit and Ness's explicit acceptance.*

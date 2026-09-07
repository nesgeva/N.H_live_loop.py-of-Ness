# NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md

**Status:** DESIGN CANDIDATE — NOT ADOPTED — NOT IMPLEMENTED — NOT
AUTHORITATIVE — NOT INTEGRATED — NOT `PACKAGE_COMPLETE`. Requires ChatGPT's
independent audit and Ness's explicit acceptance.

**Package ID:** B10 — Reread Operation Identity and Recovery (Bundle 1 of
the confirmed eight-bundle dependency plan).

**Date:** July 6, 2026.

**Governing authority order:** (1) `NH_MASTER-20_CORRECTED_v10.md`;
(2) `NH_DECISION_DEFAULTS-S19_v2_2.md`; (3) `cursorrules`;
(4) `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`. Subordinate: the
Design and Wiring Map v1.6 candidate; the eight-bundle plan; accepted B24
v7, B11 v1.4, B16 v1.0 and their closure records; accepted A2 v1.8 for
preservation boundaries. Source identities hash-verified on disk before
writing.

**Purpose in plain terms:** B10 is the "read this again later, but do not
overwrite the old reading and do not pretend it is the same event" system.

---

## §1 — Frozen standalone scope

B10 owns **only** reread operation identity and recovery: what a reread is
mechanically; its trigger, claim, and layer identities; append-only
layering beside prior readings; transaction boundaries; idempotency;
duplicate prevention; crash recovery; partial-completion recovery;
fail-closed behavior; and §0B logging.

**What B10 is:** the mechanical identity-and-recovery structure around
§7H's already-settled Reread Lifecycle. §7H is **consumed, not redesigned**:
a reread never happens without an explicit recorded reason; the bounded
trigger types are §7H's (manual; condition-based; scheduled automatic retry
for temporary technical conditions only, never reinterpretation; plus
eligibility on Ness rejecting a reading); every reread records trigger
type, reason, initiator, new evidence/changed condition, previous reading
IDs, configuration, and timestamp; a reread creates a **new** reading and
never overwrites, edits, or deletes an earlier one; a revisable reading may
remain unrevisited indefinitely.

**What B10 is not:** B10 does not decide the A25 reread mode-assignment
rule; does not design the condition-based relevance rules, scheduling, or
orchestration (§7H leaves them open against the §7R vocabulary); does not
decide retrieval ranking or degraded-retrieval behavior (B1/B26); does not
decide Story-Layer firmness or scoring; and never judges whether a new
reading is "better" than an old one — readings coexist as visible history.

**This design directly realizes Master open item 5:** "Reread job identity
and enqueue key are separately designed and must not reuse the new-root
`enqueue_key`." B10 defines that separate identity. The map's note that
B10 "cannot be completed until A25" is honored precisely: the
**identity/claim/trigger/layer/recovery mechanics here are
standalone-complete**, while **reread execution is dependency-blocked at
the mode slot until an A25-adopted rule exists** (§5 RR2) — the package
carries whatever mode A25 produces and biases nothing.

---

## §2 — Preservation and no-reopen boundaries

| Preserved item | B10's obligation |
|---|---|
| **B11 (accepted v1.4)** | Not reopened. No root is created, modified, or re-ingested; roots are referenced by identity, read-only. The sealed root record — **including its existing `re_reads` field — is never modified and is never read as B10 reread state**; all reread state lives in external B10 records and in the new readings themselves. |
| **B24 (accepted v7) / §7G acceptance** | Not reopened. The reread proposal passes the same Reading Proposal Acceptance Check as any reading — distinct rejection reasons, honest `insufficient_context` fallback as a valid completed outcome, rejected proposal terminal until the future adopted rule — all unchanged. |
| **B16 (accepted v1.0)** | Not reopened. The reread's output is a quarantine reading like any other; production eligibility later flows only through the B16 seam. |
| **A2 (accepted v1.8)** | Not reopened. New readings sit beside old ones; telling eligibility continues to derive from its parent reading; no identity is re-minted. |
| **Reading schema (12 fields)** | Untouched. The reread's reading uses **existing fields only** — `idempotency_key`, `reads`, `derived_from`, `produced_by` — no thirteenth field, no new accepted schema field. |
| **Master V10 / Defaults / cursorrules / map** | Not modified, not integrated into. |
| **A25 / §7H relevance rules / B1/B26 / Story-Layer thresholds** | Not decided (§12). |

**Preserved principles (carried mechanically):** memory only adds;
classification never locks; old readings stay visible as history; reread
creates a new layer beside old layers, never an overwrite; Ness is not
turned into a manual clerk — the manual trigger is available at will, but
nothing requires Ness to drive routine mechanics.

---

## §3 — What a reread is, mechanically

A reread is a **new reading operation** over an already-ingested root,
carrying its **own operation identity** (never the new-root identity),
launched only from an explicit recorded trigger, and producing **exactly
one new reading record** appended beside all prior readings of that root in
the quarantine readings destination through the normal validated reading
path. The new reading is a **new layer**: it references the root via
`reads`, carries its provenance and the previous reading IDs per §7H's
required record set through the existing `produced_by` / `derived_from`
fields, and leaves every earlier reading untouched and visible.

**A reread is not a retry.** A retry (B9) re-attempts the **same**
operation identity to complete its single outcome — it can never add a
layer. A reread is a **new identity per recorded trigger** — it can never
complete or replace an old operation's outcome. A "reread" request for an
operation that never completed is refused here and belongs to B9; §7H's
scheduled-automatic-retry trigger class is mechanically served by B9 while
the original operation remains open, and becomes B10 territory only where a
completed reading already exists.

---

## §4 — Identities

- **`reread_trigger_record`** [proposed] — required before anything else;
  no trigger record, no reread. Append-only, carrying §7H's full required
  set: `trigger_type` (the §7H set, by reference: `manual` /
  `condition_based` / `scheduled_automatic_retry` / `on_rejection`);
  trigger reason; initiator; new evidence or changed condition references;
  the **previous reading IDs**; configuration reference; timestamp. The
  **content rules** for condition-based relevance and scheduling remain
  §7H/§7R/A25-territory — B10 fixes only the record shape and the rule that
  the record must exist.
- **`reread_claim_key`** [proposed] — deterministic:
  `stable_hash(root_id + trigger_record_id + "reread_job_v1")`. **One
  canonical claim per {root, trigger}.** Explicitly and permanently
  **distinct from the new-root `enqueue_key = stable_hash(root_id +
  "reading_job_v1")`** — the two can never collide because the operation
  type strings differ and the reread key binds the trigger identity.
- **Reread reading idempotency:** `reread_reading_idempotency_key =
  stable_hash(reread_claim_key + "reading_v1")` [proposed], assigned to the
  new reading's **existing** `idempotency_key` field — one reading ever per
  {root, trigger}, across any number of attempts, mirroring the settled
  §7G-A pattern without touching the schema.
- **How rereads are distinguished from duplicate reading attempts:** same
  trigger → same claim → the one reading absorbs (a duplicate request, not
  a new layer). A **new trigger record** → a new claim → a legitimate new
  layer. A request with **no** trigger record → refused. A request naming
  the new-root identity → refused as misrouted (that identity belongs to
  the original operation and B9).
- **`reread_operation_id`** [proposed] — the parent per caller invocation;
  child operation IDs per separately executed step (claim, snapshot,
  execution/acceptance, layer commit, recovery resolution), each with
  exactly one §0B operational log; the parent terminal is single (the
  accepted parent/child pattern, consumed without reopening B11 v1.4).
- **`reread_layer_record`** [proposed] — the external append-only record
  binding {claim, trigger, the new `reading_id`, the previous reading IDs}
  — the layer's identity trail, beside (never inside) the reading.

---

## §5 — Transaction boundaries

| # | Boundary [proposed] | Commit content | If absent / refused |
|---|---|---|---|
| RR0 | **Lookup** | Read-only: find the claim for {root, trigger}. Committed layer exists → `duplicate_absorbed` (the existing reading and layer record returned). Live claim under another attempt → this attempt appends nothing (`reread_interrupted`, claim ref). No trigger record → refused. | Claim evidence unreadable → fail closed |
| RR1 | **Reread claim commit (one compare-and-commit)** | Atomically establish the claim binding {`reread_claim_key`, root identity, trigger record ref, previous reading IDs, integrity refs, parent op}. Exactly one winner per claim; losers observe and append nothing. A live hold on the root or its readings → `dependency_blocked_held`, no claim (B-HOLD authority). | No committed claim → nothing proceeds |
| RR2 | **Instruction + context snapshot** | Build the reread instruction: **`reread_mode_ref` [proposed] — the mode assigned by whatever rule A25 adopts; until an adopted A25 rule exists, this boundary resolves `dependency_blocked_held` (recorded, fail-closed) — no mode is invented and `thread_membership_v1` is not borrowed (it governs new-root passes only).** With a mode: §7Q internal-use authorization via LMAC, then §7F context retrieval, then §7R relevance — order preserved. Commit the context snapshot with honest coverage. Retrieval **system failure** → the pass closes technical-failed per the settled rule (job-level state preserved; retry interplay = B9); the refined stop/retry/degraded behavior remains **B26**, open. | Unauthorized → refused, never bypassed; unreadable snapshot state → fail closed |
| RR3 | **Execution + acceptance** | Mouth proposal from the snapshot, then the **Reading Proposal Acceptance Check exactly as settled** (§7G/B24, unchanged): accepted → RR4; `insufficient_context` → the honest fallback reading is produced and proceeds to RR4 as a valid completed outcome; **rejected** → the distinct reason is recorded, the proposal never becomes a reading, the attempt closes substantive-terminal (future retry rule = the Master's open item; B9's classification applies). | Mouth/system failure → technical-failed, claim remains resumable |
| RR4 | **Layer commit (the commit point)** | One compare-and-commit entry against the claim (no prior layer), then: the one new reading written through the **normal validated reading path to the quarantine destination** with `idempotency_key = reread_reading_idempotency_key` and provenance in existing fields; plus the append-only `reread_layer_record`. **Nothing is overwritten, edited, deleted, moved, or replaced** — the attempt is refused if it would target an existing reading record rather than append (row 17). The claim's terminal is bound to this commit, recovery-completable from the reading + layer evidence. | Write failure → technical-failed; duplicate found by idempotency → recover the existing `reading_id`, complete the layer record idempotently |
| RR5 | **Parent terminal log** | The single §0B terminal of the parent `reread_operation_id` — `reread_committed` / `reread_duplicate_absorbed` / `reread_rejected` / `reread_interrupted` / `reread_blocked_held` / `reread_indeterminate` — durably appended after the children resolve, **before acknowledgement**. | Terminal absent → no acknowledgement; recovery appends only the missing terminal |
| RR-PR | **Post-commit indexes/coverage** | Rebuildable view/index material (e.g., the §7I newest-usable surfacing consumes the new layer). Never gates success; never the status authority. | Rebuild idempotently |

---

## §6 — Idempotency and duplicate-prevention points (eight)

| Point | Key / mechanism |
|---|---|
| Trigger record | trigger identity — append-only; one record per real trigger occurrence |
| Reread claim | `reread_claim_key` {root, trigger} — one claim ever; establishment converges |
| Claim commit (RR1) | one compare-and-commit; exactly one winner |
| Layer / reading | `reread_reading_idempotency_key` → the reading's `idempotency_key` — one reading ever per claim across all attempts |
| Layer record | claim identity — one layer record per claim, completed idempotently from reading evidence |
| Parent terminal (RR5) | `reread_operation_id` — exactly one |
| Child-operation log | child op ID — exactly one log per child |
| Recovery run | `recovery_run_id` + lookup-first — repeats are no-ops |

---

## §7 — Recovery matrix (lookup-first; idempotent; no rewrite; no reconstruction; no false success; fail-closed on unreadable or contradictory evidence)

| # | Crash / condition | Resolution |
|---|---|---|
| 1 | Crash before the reread claim | Nothing to undo; the trigger record (if written) is harmless and reusable; the next attempt runs RR0 → RR1 |
| 2 | Claim exists, context snapshot absent | Resume RR2 under the claim (mode slot permitting), or release the claim with a recorded cause → `reread_interrupted`; nothing was produced |
| 3 | Snapshot exists, reread output absent | Resume RR3 from the committed snapshot, or close technical-failed; the snapshot binds the context — no silent re-assembly with different context under the same claim |
| 4 | Reread output exists, layer record absent | The reading's `idempotency_key` proves the layer's reading: recover `reading_id`, complete the `reread_layer_record` idempotently, proceed to RR5 |
| 5 | Layer committed, terminal log absent | Append the single missing parent terminal from the committed evidence; only then acknowledge |
| 6 | Terminal log exists, acknowledgement absent | Return the recorded terminal; nothing re-executes; no second terminal |
| 7 | Duplicate reread request, same trigger | RR0 absorbs against the committed layer (`duplicate_absorbed`) or observes the live claim (`reread_interrupted`); one layer per trigger, ever |
| 8 | Reread request with a new trigger | A legitimate new claim: RR1 proceeds; the new layer will sit beside all earlier ones; nothing about prior layers changes |
| 9 | Source reading missing/unreadable (a previous-reading ID cannot be verified) | Fail closed for this attempt: the trigger record's evidence set cannot be honestly bound → `reread_rejected` (recorded cause) or `indeterminate_recovery_required` if the store state itself is unreadable; nothing reconstructed |
| 10 | Root missing/unreadable | Fail closed: the root's existence-by-identity is a precondition; `indeterminate_recovery_required`; B11's authorities are consulted read-only; nothing fabricated |
| 11 | Retrieval timeout / degraded context | The settled rule applies: technical-failed, claim resumable, honest recording; **whether to stop, retry, or proceed degraded is B26's open design** — B10 does not proceed silently degraded |
| 12 | Privacy/access refusal | Refused per the gate; never bypassed; `reread_rejected` (unauthorized) or blocked per the refusal class; logged under the gate's own visibility rules |
| 13 | Reread output malformed / rejected by the acceptance check | The distinct rejection reason is recorded; the proposal never becomes a reading; substantive-terminal per the settled rule; the honest `insufficient_context` fallback path remains the only written alternative and only when genuinely warranted |
| 14 | Reread held by B-HOLD | `dependency_blocked_held` at RR1/RR2; no claim proceeds while a live hold exists; release is B-HOLD's interface under A29 |
| 15 | Conflicting reread attempts (race on one claim) | RR1's compare-and-commit admits exactly one; losers append nothing; contradictory claim **evidence** → `indeterminate_recovery_required`, fail closed |
| 16 | Duplicate recovery run | `recovery_run_id` + lookup-first: repeats re-read committed state and re-apply nothing |
| 17 | **Attempted overwrite of an old reading** | **Refused and logged as a fail-closed violation.** No B10 path writes into, edits, deletes, or replaces any existing reading record; the only write is the append of the one new reading + layer record |

---

## §8 — Fail-closed matrix

| Condition | Behavior |
|---|---|
| No trigger record | Refused — a reread never happens without an explicit recorded reason |
| A25 mode rule not yet adopted | `dependency_blocked_held` at RR2; no mode invented; nothing borrowed from `thread_membership_v1` |
| Root / prior reading unverifiable | Fail closed (§7 rows 9–10) |
| Retrieval system failure | Technical-failed per the settled rule; B26 owns refinement |
| Acceptance rejection | Substantive-terminal; recorded distinct reason; never silently a reading |
| Hold present | Blocked; B-HOLD authority |
| Privacy refusal | Refused; never bypassed |
| Any overwrite path | Refused + violation log (§7 row 17) |

---

## §9 — §0B operational logging

Canonical state records (trigger records, claims, snapshots, layer records)
are machine facts — not operational logs, never extra evidential votes.
Every real B10 operation emits **exactly one** append-only §0B log under
its own identity: child logs for the claim, snapshot, execution/acceptance,
layer commit, and recovery resolution — each under its own child op ID
referencing the parent `reread_operation_id`; **RR5 is the single parent
terminal.** No log-about-logging; no double evidence — a reread, its
records, and its logs never make any reading more true, and the new layer
is never evidence that the old layer was wrong (both remain visible
history). Records link by identities only; §7Q governs access to every
record, including logs of privacy blocks.

| Record [proposed] | Covers |
|---|---|
| `reread_trigger_recorded` | Each §7H-complete trigger record |
| `reread_claim_committed` / `reread_claim_absorbed` | RR1 winners; RR0 absorptions |
| `reread_snapshot_committed` | Each RR2 snapshot with honest coverage |
| `reread_acceptance_result` | Each RR3 outcome — pass, honest fallback, or distinct rejection reason (the acceptance layer's own records remain its own) |
| `reread_layer_committed` | The RR4 commit — one log carrying the reading append + layer record together |
| `reread_terminal` (RR5) | The single parent terminal, before acknowledgement |
| `recovery_applied` / `recovery_noop` / `fail_closed_event` | Recovery resolutions and every §8 occurrence, including row-17 violations |

---

## §10 — Boundaries and must-nevers

DUMB structure around a SMART act: the reading itself is the engine's SMART
work under §7G's unchanged rules; B10's machinery routes, records, and
recovers, and never interprets. Root evidence and prior-reading context
stay separate per the settled two-channel rule. Quarantine/production stay
separate: the new layer lands in quarantine; promotion is only the B16
seam. Must-nevers: no overwrite, edit, deletion, or replacement of any
reading; no reread without a recorded trigger; no mode invention ahead of
A25; no silent degraded context; no privacy bypass; no reinterpretation
under the scheduled-automatic-retry class; no implementation or disk
action.

---

## §11 — Explicit open dependencies (recorded, not solved)

- **A25** — the reread mode-assignment rule; RR2 stays blocked until it is
  adopted; B10 carries whatever A25 produces.
- **§7H's open relevance rules, retry limits, scheduling, and
  orchestration** — declared against the §7R vocabulary when addressed;
  the trigger-record shape here is ready for them.
- **B1/B26** — retrieval parameter values and the system-failure
  stop/retry/degraded design.
- **B9 interplay values** — technical-failure retry values remain B9-open
  configuration.
- **Story-Layer firmness/thresholds; B-CYCLE wiring (including
  B-CYCLE-8's full reread cycle); B16 promotion beyond the seam; C2; all
  implementation and disk/runtime choices.**

---

## §12 — Frozen closure-checklist self-audit (not a final verdict; independent audit and explicit acceptance pending)

| # | Item | Status |
|---|---|---|
| 1 | Standalone scope stated clearly | §1 — met |
| 2 | Master V10, Defaults, cursorrules, map, B11, B16, B24, A2 preserved | §2 — met |
| 3 | Operation identity defined | §4 (trigger, claim, layer, parent/child) — met |
| 4 | Transaction boundaries defined | §5 (RR0–RR5 + RR-PR) — met |
| 5 | Idempotency defined | §6 (eight points) — met |
| 6 | Duplicate prevention defined | §4 (trigger-vs-duplicate distinction), §5 RR1/RR4, §6 — met |
| 7 | Crash recovery defined | §7 — met |
| 8 | Partial-completion recovery defined | §7 rows 2–5 — met |
| 9 | Fail-closed behavior defined | §8 — met |
| 10 | Component-specific §0B logging defined | §9 — met |
| 11 | No-double-evidence preserved | §9 — met |
| 12 | Privacy/access boundaries preserved | §5 RR2, §7 row 12, §9 — met |
| 13 | A29, A25, thresholds, final values, full B-CYCLE wiring, implementation left open | §11 — met |
| 14 | No code, migration, store, marker action, disk action, Master update, or map update | §13 — met |

**CRITICAL-severity self-check — no issues found by this self-check.** No
authority violated; no accepted rule changed; no Ness-owned policy decided
(A25 blocked-open; §7H rules consumed); false success impossible (terminal
only from durable commit evidence); duplicate layers impossible (one claim
per trigger; one reading per claim by idempotency); **no reading is ever
overwritten or replaced — the overwrite path is a refused, logged
violation**; no silent use of held material; no privacy bypass; no
implementation or disk action.

**IMPORTANT-severity self-check — no issues found within the frozen
scope.** Identity, boundaries, eight idempotency points, seventeen recovery
rows, fail-closed matrix, and §0B structure present and consistent; the
retry-vs-reread boundary is stated identically here, in B9 §7, and in the
coordination note.

**MINOR notes:** all identifiers `[proposed]`; §7H's open rules echoed, not
filled; the reread key's exact hash composition is a proposed form
satisfying the settled separation requirement.

---

## §13 — Delivery statement

**Created:** this file only (one of the four instructed Bundle-1 fast-pass
files). **Changed:** nothing existing — no authoritative, accepted, map,
plan, closure, or candidate file modified; no commit/push/upload; no code,
migration, store, marker, seal, terminal, or runtime action. Sources
hash-verified before writing and untouched.

---

*`NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md` — DESIGN
CANDIDATE. The Bundle-1 reread seam: a recorded §7H trigger before
anything; one claim per {root, trigger} under a key that can never collide
with the new-root identity; one new reading layer per claim, appended in
quarantine beside untouched history; mode execution blocked-open on A25;
seventeen lookup-first recovery rows; one-operation/one-log with no double
evidence — with A25, §7H's relevance/scheduling rules, B1/B26, retry
values, and all implementation explicitly open, and B11, B16, B24, A2,
Master V10, Defaults, cursorrules, and the map preserved untouched.
Awaiting ChatGPT's independent audit and Ness's explicit acceptance.*

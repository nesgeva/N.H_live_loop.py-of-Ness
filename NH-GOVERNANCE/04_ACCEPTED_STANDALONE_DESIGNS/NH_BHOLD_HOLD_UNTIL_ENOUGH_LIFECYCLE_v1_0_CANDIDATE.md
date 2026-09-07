# NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_v1_0_CANDIDATE.md

**Status:** DESIGN CANDIDATE — NOT ADOPTED — NOT IMPLEMENTED — NOT
AUTHORITATIVE — NOT INTEGRATED — NOT `PACKAGE_COMPLETE`. Requires ChatGPT's
independent audit and Ness's explicit acceptance.

**Package ID:** B-HOLD — "Hold-Until-Enough" Lifecycle (§7B Part 5,
mechanical only; Bundle 1 of the confirmed eight-bundle dependency plan).

**Date:** July 6, 2026.

**Governing authority order:** (1) `NH_MASTER-20_CORRECTED_v10.md`;
(2) `NH_DECISION_DEFAULTS-S19_v2_2.md`; (3) `cursorrules`;
(4) `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`. Subordinate: the
Design and Wiring Map v1.6 candidate; the eight-bundle plan; accepted B24
v7, B11 v1.4, B16 v1.0 and their closure records; accepted A2 v1.8 for
preservation boundaries. Source identities hash-verified on disk before
writing.

**Purpose in plain terms:** B-HOLD is the "waiting shelf." It does not
decide what "enough" means — A29 does. B-HOLD only makes sure waiting items
are not lost, forced, duplicated, or secretly used too early.

---

## §1 — Frozen standalone scope

B-HOLD owns **only** the mechanics that follow A29's future policy: where
the held object lives; hold and held-item identity; hold-reason identity;
the hold lifecycle; hold-request and release operation identity;
transaction boundaries; idempotency; duplicate prevention; crash recovery;
partial-completion recovery; fail-closed behavior; the release interface;
blocked-use behavior while held; §0B logging; and no-double-evidence
behavior.

**What B-HOLD is not (the map's own boundary, preserved exactly):** B-HOLD
does **not** choose the threshold or the release policy — **A29 decides
what counts as "enough to read responsibly" and which kind of insufficiency
causes holding rather than producing an `insufficient_context` reading.**
B-HOLD decides no wait duration, no release criteria content, no retry
values, no reread mode, and no promotion policy.

---

## §2 — Preservation and no-reopen boundaries

| Preserved item | B-HOLD's obligation |
|---|---|
| **B11 (accepted v1.4)** | Not reopened. A hold never touches roots, batches, claims, or stores; held items are referenced by identity only. |
| **B16 (accepted v1.0)** | Not reopened. B16's `dependency_blocked_held` is the **promotion-side view** of a live hold; B-HOLD is the authority that check consults. Neither redefines the other. |
| **B24 (accepted v7)** | Not reopened. A hold is not a quality verdict and never substitutes for, delays into, or reverses an acceptance outcome. |
| **A2 (accepted v1.8)** | Not reopened. Telling identity/lifecycle untouched; a held parent reading simply blocks new use downstream by derivation. |
| **Root & reading schemas** | Untouched. **A hold never moves, copies, edits, re-stores, or re-writes the held item.** The mechanical answer to "where does the held object live" is: **exactly where its own seam already put it** — the hold itself lives entirely in external append-only hold records referencing the item by identity. |
| **Master V10 / Defaults / cursorrules / map** | Not modified, not integrated into. |
| **A29 / final values / promotion policy** | Not decided (§11). |

---

## §3 — Identities

- **`hold_id`** [proposed] — one identity per hold.
- **`held_item_ref`** [proposed] — typed reference:
  {`item_class` ∈ root | reading | capture-reference | promotion-candidate
  | other-typed, item identity, integrity reference where the item class
  carries one}. The item is never touched; the reference points at it.
- **`hold_reason_id`** [proposed] — a typed reason record whose **class
  taxonomy is mechanical** [proposed classes: `awaiting_context_evidence`;
  `awaiting_policy_condition` (the A29-gated class);
  `dependency`; `authorized_manual_hold`] while the **content of any
  condition — what suffices, when, and why — is policy, open** (A29 for the
  policy class; the requesting seam's own recorded cause otherwise).
- **Canonical hold claim:** **one live hold per {`held_item_ref`,
  `hold_reason_id`}** — duplicate requests absorb against it. **Distinct
  reasons may coexist** as separate holds on one item (conflicting-reason
  requests are separate holds, not a conflict to resolve); the item is
  **use-blocked while any live hold exists**.
- **`hold_operation_id`** / **`release_operation_id`** [proposed] — the
  parent operations of one hold request and one release request, each with
  child operation IDs per separately executed step and exactly one §0B log
  per operation (the accepted parent/child pattern, consumed without
  reopening B11 v1.4).

---

## §4 — Hold lifecycle

Statuses are **derived from append-only hold events** — never a field on
the held item, never an edit anywhere.

| Status [proposed] | Meaning |
|---|---|
| `hold_requested` | A durable request event exists; no blocking yet |
| `held` | The blocked-marking record is committed — the enforcement fact the gates consult; the item is excluded from new use |
| `release_requested` | A durable release request exists; still held |
| `released` | Terminal for **this hold** (the item becomes usable only when **zero** live holds remain) |
| `hold_request_rejected` | The request was refused (malformed, unverifiable item, unauthorized) with recorded cause |
| `indeterminate_recovery_required` | Hold evidence unreadable/contradictory; fail closed — the item is treated as held for use purposes until resolved (blocking errs safe) |

**Append-only honesty:** a hold blocks **new** use going forward. It never
retroactively invalidates, rewrites, or hides anything committed before it;
history stays visible.

---

## §5 — Transaction boundaries

**Hold path:**

| # | Boundary [proposed] | Commit content | If absent / refused |
|---|---|---|---|
| H0 | **Lookup** | Read-only: find any hold for {item, reason}. Live → absorb (`hold_duplicate_absorbed`). Released → a new request is a new hold (new `hold_id`) if its reason record stands. | Evidence unreadable → fail closed (treated held for use; no new commit) |
| H1 | **Hold-claim commit (one compare-and-commit)** | Atomically establish the hold: {`hold_id`, `held_item_ref` verified to exist by identity, `hold_reason_id`, requester operation ref}. Exactly one winner per {item, reason}; losers absorb. Item unverifiable → `hold_request_rejected`. | No committed claim → nothing blocks |
| H2 | **Blocked-marking commit** | The append-only enforcement record consulted by every gate (§6). From this commit the item is `held`. | Absent → the hold is requested-but-not-enforcing; recovery resumes or rejects (row 2) |
| H3 | **Parent terminal log** | The single §0B terminal of `hold_operation_id` — before acknowledgement. | Absent → no acknowledgement; recovery appends only the missing terminal |

**Release path:**

| # | Boundary [proposed] | Commit content | If absent / refused |
|---|---|---|---|
| HR0 | **Lookup** | Read-only: find the live hold. Already released → `release_duplicate_absorbed`. No such hold → refused with recorded status. | Unreadable → fail closed (stays held) |
| HR1 | **Release-evidence verification** | Verify — by existence, integrity, and binding to **this** hold — the required **release-evidence reference**: for the `awaiting_policy_condition` class, the recorded A29-condition-met record; for `authorized_manual_hold`, the recorded authorized release; for `dependency`, the recorded resolution of the named dependency. **B-HOLD never judges the condition's content — only that the record exists, is intact, and binds.** **If the hold's class is A29-gated and no adopted A29 condition/record type exists, release fails closed and the item stays held** (row 11). | Missing/unbound evidence → release refused; contradictory → `indeterminate_recovery_required` |
| HR2 | **Release commit (one compare-and-commit)** | Atomically: verify the hold is still live and the evidence still binds **immediately before committing**, then append the release event. Exactly one release ever per hold; a racing second release absorbs. | Not committed → still held |
| HR3 | **Parent terminal log** | The single §0B terminal of `release_operation_id` — before acknowledgement. | As H3 |

---

## §6 — Blocked-use behavior while held (the enforcement interface)

While **any** live hold exists on an item, the following are **excluded
fail-closed** — exclusion is the mechanical default the consulting gate
reads from the H2 record, never a best-effort filter:

- **Ordinary reading:** a reading-pass instruction must not target a held
  root/source (the §7G-A instruction path consults hold state; the wiring
  of that consultation into each cycle is cycle-level work, open — the
  authority record is defined here).
- **Promotion:** a B16 attempt on a held reading resolves B16's own
  `dependency_blocked_held` — B-HOLD is the consulted authority; B16's seam
  is unchanged.
- **Retry:** B9 refuses admission for held sources (B9 §3's
  `dependency_blocked_held` class); **a retry request while held is
  refused and recorded, never queued around the hold.**
- **Reread:** B10 refuses/blocks a claim on a held root or reading
  (B10 RR1).
- **Retrieval/output surfacing:** the governing §7Q/§7R gates consult the
  hold state and exclude the item from new surfacing; the gates' own rules
  are unchanged — B-HOLD supplies the fact, the gates govern.
- **Any silent use attempt → refused and logged as a violation**
  (row 20). No path may consume a held item "just this once."

---

## §7 — Distinctions (required; none of these may be equated with a hold)

| Thing | What it is | Why it is not a hold |
|---|---|---|
| **Hold-until-enough (this package)** | A recorded decision that an item should **wait** before being read/used, per A29's future policy | — |
| **B24 / acceptance rejection** | A quality verdict on a **produced proposal** with a distinct recorded reason | A verdict on output, not a waiting state on input; terminal per the settled rule |
| **B9 retry** | Re-attempting the **same** failed/incomplete operation identity | Completion of past work, not deferral of future work; held sources are refused by B9 |
| **B10 reread** | A **new** reading operation over an already-read source, new identity, new layer | Adds beside history; a hold prevents new work instead |
| **B16 `dependency_blocked_held`** | The **promotion-side view** of a block, including a live hold | The consumer's status word, not the shelf itself; B-HOLD is the consulted authority |
| **§7G `insufficient_context`** | An **honest, revisable, WRITTEN reading** produced when root+context genuinely cannot ground an interpretation — a valid completed outcome | The read happened and produced its honest record; a hold means the read (or use) does not happen yet. **Which insufficiency holds vs. writes that reading is exactly A29's decision** — B-HOLD never makes it |
| **§7E pre-ingest holding** | Raw-capture staging **before root ingestion**, inside §7E's own seam | A different seam with its own rules, untouched here; B-HOLD operates on already-ingested/produced items by reference |
| **TSC authorization holding** | The sealed third-party session cache awaiting its **separate** authorization/promotion seam (B-INT-4/CY-D) | A separate seam, untouched; B-HOLD creates no TSC path and reads no sealed TSC content |

---

## §8 — Idempotency and duplicate-prevention points (eight)

| Point | Key / mechanism |
|---|---|
| Hold claim | {`held_item_ref`, `hold_reason_id`} — one live hold ever per pair; duplicates absorb |
| Blocked marking (H2) | `hold_id` — one enforcement record per hold |
| Release evidence binding (HR1) | `hold_id` + the exact evidence reference — bound once |
| Release commit (HR2) | `hold_id` + one compare-and-commit — exactly one release ever; duplicates absorb |
| Parent terminals (H3/HR3) | one per `hold_operation_id` / `release_operation_id` |
| Child-operation log | child op ID — exactly one log per child |
| New-hold-after-release | a new `hold_id` requires its own standing reason record — no resurrection of a released hold |
| Recovery run | `recovery_run_id` + lookup-first — repeats are no-ops |

---

## §9 — Recovery matrix (lookup-first; idempotent; no rewrite; no false success; fail-closed on unreadable or contradictory evidence)

| # | Crash / condition | Resolution |
|---|---|---|
| 1 | Crash before any hold record | Nothing to undo; nothing blocks; the next request runs H0 normally |
| 2 | Hold record exists, item not yet marked blocked (H1 committed, H2 absent) | Resume H2 idempotently under the claim, or reject the hold with recorded cause; until H2 commits, gates see no enforcement record — honestly not yet held |
| 3 | Item blocked, terminal log absent (H2 committed, H3 absent) | Append the single missing parent terminal from the committed evidence; only then acknowledge; the block was already enforcing |
| 4 | Terminal log exists, acknowledgement absent | Return the recorded terminal; nothing re-executes |
| 5 | Duplicate hold request (same item, same reason) | H0/H1 absorb against the live hold (`hold_duplicate_absorbed`); one live hold per pair |
| 6 | Conflicting hold reasons (same item, different reasons) | Not a conflict: separate holds coexist; the item stays blocked while any lives; each releases independently on its own evidence |
| 7 | Release requested, release evidence absent | HR1 refuses; the hold stays live; the refusal names the missing evidence class; nothing partially releases |
| 8 | Release evidence exists, release commit absent | Resume HR2 idempotently — the compare-and-commit re-verifies liveness and binding immediately before committing |
| 9 | Release committed, terminal log absent | Append the single missing HR3 terminal; only then acknowledge; the release was already effective |
| 10 | Duplicate release request | HR0 absorbs (`release_duplicate_absorbed`); exactly one release ever per hold |
| 11 | **Release blocked by A29/open policy** | The A29-gated class has no adopted condition/record type yet → **release fails closed; the item stays held**; the block is recorded; nothing is invented to unblock it |
| 12 | Held item missing/unreadable | The hold record stands; use remains blocked (blocking errs safe); the item's own seam owns its integrity condition; `indeterminate_recovery_required` for any release until the item state is provable |
| 13 | Privacy/access refusal (on hold or release operations) | Refused per the gate; never bypassed; logged under the gate's own visibility rules |
| 14 | Held item attempted for ordinary reading | Refused fail-closed at the instruction path per §6; attempt logged |
| 15 | Held item attempted for promotion | B16 resolves `dependency_blocked_held` per its own seam; B-HOLD's record is the consulted authority; attempt logged on B16's side per B16 |
| 16 | Held item attempted for retrieval/output | Excluded by the consulting gates per §6; attempt logged |
| 17 | Retry request while held | Refused and recorded (B9's held class); never queued around the hold |
| 18 | Reread request while held | Refused/blocked at B10 RR1; recorded |
| 19 | Duplicate recovery run | `recovery_run_id` + lookup-first: repeats re-read committed state and re-apply nothing |
| 20 | **Attempted silent use while held** | **Refused and logged as a fail-closed violation.** No consuming path exists that does not consult the enforcement record; a bypass attempt is recorded as the violation it is |

---

## §10 — Fail-closed matrix and §0B logging

**Fail-closed:** unverifiable item → request rejected; unreadable hold
evidence → treated held for use, no new commits, `indeterminate` pending
proof; missing/unbound release evidence → still held; A29 unadopted for the
policy class → still held (row 11); privacy refusal → refused, never
bypassed; any silent-use or bypass attempt → refused + violation log.

**Logging:** hold/release claims, enforcement records, and release-evidence
bindings are **canonical state records** — machine facts, never extra
evidential votes, never operational logs. Every real operation emits
**exactly one** §0B log under its own identity: child logs per step under
their child op IDs referencing the parent; H3/HR3 are the single parent
terminals. **No double evidence:** a hold, its records, and its logs never
make the held item more or less true, more or less important — waiting is
not a verdict. Records link by identities only; §7Q governs access to every
record.

| Record [proposed] | Covers |
|---|---|
| `hold_requested` / `hold_committed` / `hold_duplicate_absorbed` / `hold_request_rejected` | The hold path outcomes |
| `hold_enforcement_marked` | Each H2 commit — the fact the gates consult |
| `release_requested` / `release_evidence_bound` / `release_committed` / `release_duplicate_absorbed` / `release_refused` | The release path outcomes, including row-11 policy blocks |
| `hold_terminal` / `release_terminal` | The single parent terminals, before acknowledgement |
| `blocked_use_refused` | Every §6/§9 rows 14–18, 20 refusal — the attempted class named |
| `recovery_applied` / `recovery_noop` / `fail_closed_event` | Recovery resolutions and every fail-closed occurrence |

---

## §11 — Explicit open dependencies (recorded, not solved)

- **A29** — the meaning of "enough"; which insufficiency holds vs. produces
  an `insufficient_context` reading; the content of the policy-class
  release condition and its record type. Until adopted, policy-class
  releases fail closed (row 11).
- **The policy threshold for hold vs. `insufficient_context`** — A29's,
  restated for clarity: B-HOLD never selects it.
- **Exact release criteria, wait durations, and any hold-related tuning** —
  policy/configuration, open.
- **B9 retry values; A25/B10 reread mode policy; B16 promotion policy
  beyond the seam; B-CYCLE wiring (including how each cycle's instruction
  path consults the enforcement record); B1/B26; C2; all implementation and
  disk/runtime choices.**

---

## §12 — Frozen closure-checklist self-audit (not a final verdict; independent audit and explicit acceptance pending)

| # | Item | Status |
|---|---|---|
| 1 | Standalone scope stated clearly | §1 — met |
| 2 | Master V10, Defaults, cursorrules, map, B11, B16, B24, A2 preserved | §2 — met |
| 3 | Operation identity defined | §3 (hold, item, reason, parent/child, release) — met |
| 4 | Transaction boundaries defined | §5 (H0–H3, HR0–HR3) — met |
| 5 | Idempotency defined | §8 (eight points) — met |
| 6 | Duplicate prevention defined | §3 (one live hold per pair), §5, §8 — met |
| 7 | Crash recovery defined | §9 — met |
| 8 | Partial-completion recovery defined | §9 rows 2–3, 7–9 — met |
| 9 | Fail-closed behavior defined | §10 — met |
| 10 | Component-specific §0B logging defined | §10 — met |
| 11 | No-double-evidence preserved | §10 (waiting is not a verdict) — met |
| 12 | Privacy/access boundaries preserved | §9 row 13, §10 — met |
| 13 | A29, A25, thresholds, final values, full B-CYCLE wiring, implementation left open | §11 — met |
| 14 | No code, migration, store, marker action, disk action, Master update, or map update | §13 — met |

**CRITICAL-severity self-check — no issues found by this self-check.** No
authority violated; no accepted rule changed; A29 undecided everywhere it
appears (policy-class release fails closed until adopted); no false
success; no duplicate holds or releases (one live hold per pair; one
release ever); **no silent use of held material — every consuming class is
excluded fail-closed and a bypass attempt is a logged violation**; nothing
moved, copied, edited, or rewritten (the held item lives where its seam put
it; the hold lives in external records); no privacy bypass; no
implementation or disk action.

**IMPORTANT-severity self-check — no issues found within the frozen
scope.** Identity, boundaries, eight idempotency points, twenty recovery
rows, fail-closed matrix, the eight-way distinctions table, and the §0B
structure are present and consistent; the B9/B10/B16 interfaces match those
packages' own wording and the coordination note.

**MINOR notes:** all identifiers `[proposed]`; the reason-class taxonomy is
mechanical routing vocabulary, not policy content.

---

## §13 — Delivery statement

**Created:** this file only (one of the four instructed Bundle-1 fast-pass
files). **Changed:** nothing existing — no authoritative, accepted, map,
plan, closure, or candidate file modified; no commit/push/upload; no code,
migration, store, marker, seal, terminal, or runtime action. Sources
hash-verified before writing and untouched.

---

*`NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_v1_0_CANDIDATE.md` — DESIGN
CANDIDATE. The Bundle-1 waiting shelf: holds live in external append-only
records while items stay exactly where their seams put them; one live hold
per {item, reason} with coexisting distinct reasons; release only on
verified bound evidence, failing closed while A29 is unadopted; every
consuming class excluded fail-closed while held, with silent use a logged
violation; twenty lookup-first recovery rows; one-operation/one-log with
waiting never a verdict — with A29, release criteria, durations, retry
values, reread policy, promotion policy, and all implementation explicitly
open, and B11, B16, B24, A2, Master V10, Defaults, cursorrules, and the map
preserved untouched. Awaiting ChatGPT's independent audit and Ness's
explicit acceptance.*

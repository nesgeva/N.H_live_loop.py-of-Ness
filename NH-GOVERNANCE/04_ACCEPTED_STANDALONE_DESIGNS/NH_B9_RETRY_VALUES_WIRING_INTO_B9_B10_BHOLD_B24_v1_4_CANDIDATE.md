# NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md

## 0. STATUS BLOCK

**Status:** CANDIDATE — unaudited; awaiting ChatGPT's independent audit of
this actual file and Ness's explicit acceptance afterward. **Governed
values-wiring package only:** it maps Ness's decided retry values onto the
accepted B9 retry-state mechanics and their accepted B10/B-HOLD/B24 seams
**without rewriting, patching, replacing, or modifying any accepted
source.** Not accepted, not adopted, not authoritative, not integrated,
not implemented, not `PACKAGE_COMPLETE`. **Until this candidate is
independently audited and explicitly accepted by Ness, the accepted
defaults continue to govern: no declared budget exists, so B9's R1
admission continues to fail closed (B9 §8 row 14), and a substantively
rejected proposal remains terminal under the settled rule.** Nothing
runtime is unblocked, built, integrated, or implemented by this file.

**Version note (v1_4):** narrow correction of v1_3 only, closing the one
remaining IMPORTANT anchor-and-admission contradiction from ChatGPT's
independent audit. v1_3 correctly made a later same-identity episode's
first B9-admitted re-attempt `episode_attempt_ordinal = 1`, with no
scheduled gap before ordinal 1 and the episode deadline beginning only
at ordinal 1's durable failure — yet §§6, 7, 14, 19, and 20 still
required every admission to bind actual gap-anchor and deadline
evidence, which cannot exist yet at that ordinal-1 admission. v1_4
defines the special ordinal-1 admission mechanically and consistently
(§6, §7, §10, §14, §15, §16, §19, §20): the later episode opens only
through the committed real-change consumption record and only with the
source seam's confirmation of unchanged canonical inputs; its ordinal-1
admission atomically binds the group, the next unused permanent
`attempt_number`, `attempt_id`, `retry_episode_id`,
`episode_attempt_ordinal = 1`, the exact retry-budget configuration,
the consumption authorization, and two explicit durable states —
`no_gap_before_ordinal_1` and
`deadline_pending_from_first_durable_failure` — **in place of** actual
gap-anchor and deadline evidence, which is never claimed to exist; no
waiting gap is invented and the 7-minute/15-minute clock is not started
earlier. Ordinal-1 outcome behavior and four distinguished crash-
recovery cases are defined; ordinals 2 and 3 continue to bind the real
durable evidence exactly as designed; the initial episode is unchanged
(the seam's original execution stays recorded by reference, never a B9
admission, and its durable technical failure supplies the actual
deadline and gap evidence for ordinals 2 and 3). No value, allowance,
or seam meaning changed. v1_3 (SHA-256
`cf274230c9fe52ddd04545f093fc2d24ddec22acd20bb596e630a7f26c22a175`;
1,032 lines; 62,712 bytes) is preserved unchanged as historical
candidate provenance.

**Version note (v1_3):** narrow correction of v1_2 only, closing the one
remaining IMPORTANT attempt-numbering defect from ChatGPT's independent
audit. v1_2 permitted a later same-identity bounded episode under the
same `retry_group_id` but did not define how the permanent group-wide
attempt numbers coexist with the fresh episode's three-position budget
and two-gap schedule. v1_3 makes the distinction explicit (§5, and
consistently in §4, §6, §7, §9, §10, §14, §15, §19, §20): the permanent
`attempt_number` inside accepted B9's `attempt_id` stays monotonically
increasing across the whole group and never resets or repeats; a
separate proposed `episode_attempt_ordinal`, bound to
`retry_episode_id` and limited to 1–3 for a technical episode, applies
that episode's attempt allowance and waiting-gap schedule; the gate
counts only that exact episode's ordinals; gaps are indexed by the
ordinal — none before ordinal 1, the first declared gap before ordinal
2, the second before ordinal 3 — never by a group-wide number such as
4, 5, or 6; the initial episode's original execution is ordinal 1 by
reference, with B9-admitted retries as ordinals 2 and 3; a later
same-identity episode's first admitted re-attempt is ordinal 1 under
the next unused permanent number, with its fresh deadline beginning at
that ordinal-1 attempt's durable failure; changed canonical inputs open
a new group with normal initial-episode semantics and never continue or
renumber the old group; admission atomically binds group, permanent
number, `attempt_id`, episode, ordinal, and the exact budget, gap, and
deadline evidence, with one winner and full lookup-first
reconstruction — no reset, collision, skipped-bound interpretation, or
in-memory-only counter. No value, policy, allowance, or seam meaning
changed. v1_2 (SHA-256
`7c2a3cbbb2eefc043ea2ce0cb46702a492682d108146479fcd7bfbf93b683fc2`;
888 lines; 53,636 bytes) is preserved unchanged as historical candidate
provenance.

**Version note (v1_2):** narrow correction of v1_1 only, closing the two
remaining IMPORTANT defects from ChatGPT's independent audit. (1) The
last closed-list contradiction is removed: the §4
`real_change_categories` configuration row still described the six
categories as a closed enumeration; it now states the already-correct
v1_1 rule — the named categories are "such as" examples, not a closed
list; `other_real_change` is permitted with a required truthful written
explanation and supporting evidence references; every category requires
evidence references; repetition or passage of time alone is never a
real change. A full-file sweep found no other contradicting wording.
(2) The elapsed-time deadline is made equally explicit on the
substantive bad/unsafe/unsupported-draft path (§4, §6, §7, §9, §14,
§15, §19, §20): the attempt allowance remains exactly one careful
retry; the deadline is the same 7 minutes live chat / 15 minutes
background-nightly; the clock begins at the durable
first-failure/rejection record that begins that episode; both the
one-retry allowance and the deadline are verified before admission;
"immediate" means no scheduled waiting gap and never a deadline bypass;
a deadline passed before admission (crash, delay, or recovery) admits
nothing and records truthful time exhaustion; a deadline passing after
the careful retry has started forces no cancellation, overrides no
source-seam timeout or terminal rule, and admits no further retry.
Nothing else changed in meaning; no new time, attempt number, policy,
concept, fallback condition, or identity rule is introduced. v1_1
(SHA-256
`11bae39baf312b381ecd8d5449957698aa30cc0736e253a51c549122e69e075d`;
805 lines; 48,109 bytes) is preserved unchanged as historical candidate
provenance.

**Version note (v1_1):** corrects the five IMPORTANT problems ChatGPT's
independent audit found in v1_0, in one organized pass, under Ness's
approved values as carried by the correction instruction: (1) a **real
elapsed-time deadline** — 7 minutes live chat / 15 minutes
background-nightly from the episode's first recorded failure — is now a
true stop gate racing the attempt limit; the gap values are minimum
waiting gaps only (§3, §4, §6, §7, §9); (2) Ness's real-change examples
are preserved as **"such as" — non-exhaustive** — with a truthful
`other_real_change` catch-all requiring a written explanation and
evidence references (§3, §10); (3) records stay **truly append-only** —
the mutable `consumed_by_episode_ref` field is removed and replaced by a
separate append-only real-change **consumption record** with one atomic
winner (§10, §14); (4) **source-operation identity is preserved
correctly** — unchanged canonical inputs may continue under the same
identity; input-altering changes create a new linked operation identity
under the source seam, and for B10 a new trigger and claim (§10, §11);
(5) the **B24 fallback boundary is narrowed** — the insufficiency
assessment can open only for an eligible B24 proposal after its
authorized careful-retry sequence truthfully ends, never from protected
or unrelated outcome classes (§13). Nothing else changed in meaning.
v1_0 (SHA-256
`97fba39974b77c7f5ed748e483450cc9a557c11c4e0706ccf7f0e7543cb554e0`;
627 lines; 35,932 bytes) is preserved unchanged as historical candidate
provenance.

**Date:** July 12, 2026.

**Package ID:** B9 retry-values wiring into B9, B10, B-HOLD, and B24 —
the "B9 values" gap recorded **DECIDED by Ness** in the accepted Bundle 1
normalization record §6, mapped here onto the accepted mechanics
(Bundle 1; the value-level policy gap attached to accepted B9).

**Intended repository placement:** `05_ACTIVE_CANDIDATE/`
(the physical move into the repository is Ness's action).

## 1. GOVERNING AUTHORITY ORDER

1. `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`
   (adopted by Ness June 29, 2026; governing)
2. `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`
3. `01_AUTHORITATIVE/cursorrules`
4. `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`

The current Design and Wiring Map is subordinate to these files.

## 2. SOURCES READ — IDENTITIES RECALCULATED BEFORE WRITING

All read from the governance repository snapshot at branch `main`, commit
`db13036a8d786f2384a02cb7aef0eefe00c412f6`, byte-verified July 12, 2026:

- **Accepted B9:** `NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md`
  — SHA-256
  `78c5d0b74d91e9390d9ebdf4d1c6ae04dd2632ad86c8efa83f01cfbd9974e606`;
  351 lines; 25,308 bytes — **recalculated; matched exactly; read in
  full** (§3 classes, §4 identities and declared inputs, §5 R0–R4, §6,
  §7 seams, §8 rows 1–19, §9, §10, §12). Its closure receipt
  (`2f9fa7df2d190bf6defae31e8e8a10f78df71a0ef8cb22fc8150f413f7e3c30e`)
  — read.
- **Accepted B10:** `NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md`
  — SHA-256
  `215b74841321656a8b7fb1cbf4b9ac9b43259315864cd9f85f5ce86b43d10001`;
  329 lines; 23,681 bytes — **recalculated; matched exactly; read in
  full.** Its closure receipt
  (`da62a1e8216924f9e9f3182f925e7a1e5063355418a7302eb58f86eee54adeea`)
  — read.
- **Accepted B-HOLD:** `NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_v1_0_CANDIDATE.md`
  — SHA-256
  `406ab00f640eaae013902782e9ec6ca652ea680c10b0f68699d56391a9e1efce`;
  317 lines; 21,649 bytes — **recalculated; matched exactly; read in
  full.** Its closure receipt
  (`4774720eab9ce276e09a3dde20abf59f71e562a462ad7b4fbe2462dccf14e6c9`)
  — read.
- **Accepted B24:** `NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md`
  — SHA-256
  `7f5762e5bc3d7d0fa554ad41426d2cc2f14fb7753a79b67fbd675f6c6b8a2171`;
  1,938 lines; 137,507 bytes — **recalculated; matched exactly**; read
  targeted in the sections this wiring touches: §2.8/§2.10 (the
  insufficiency assessment and its B9-authorized fallback point),
  §3.3/§3.3B/§3.4 (settled rejection categories; boundary-reason
  separation), §5.3 (reject / retry slot / deterministic fallback), and
  §5.4 (the permanently distinct outcomes). Its closure record
  (`83d79db9f5edcad85d603f7cfe93ea3afeeebec6a60f6f4aa64db632b7e5d7e0`)
  — read.
- **Coordination note** (accepted):
  `NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md` —
  SHA-256
  `95491b9b621a814a8ac96fb5dba2cb4a9dc6b53ab519111a1aa067c1bbb1ef8c`
  (the `04_` and `05_` copies are byte-identical) — **read in full.**
  Its closure record
  (`6defb8d417f8da26d86d48918ac6098c07abadd6826f2ec35ac2d00d1931efef`)
  — read.
- **Bundle 1 normalization record v1_1** (accepted for its recording
  scope):
  `NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_CANDIDATE_v1_1.md`
  — SHA-256
  `6828b9bd88cf867d20bfee31b67d13e97e0c573316b43d2298e4764785abeec3` —
  **§6 (the B9 normalized decision record) read verbatim and preserved
  in §3 below.** Its acceptance record
  (`d759d99d6d01cfe0371c5f4261912f2a4e11cabc10ec3fd8cc249bd5d522d7f7`)
  — read.
- **Accepted A29** (where B-HOLD consumes it):
  `NH_A29_HOLD_UNTIL_ENOUGH_POLICY_v1_0_CANDIDATE.md` — SHA-256
  `31d5a12455d1532effe7df2216223942da1a555f38910929ff4b6761d0015d65` —
  the automatic track/check/release rule and the A29/B-HOLD ownership
  split, consumed unchanged for the §12 seam.
- **Correction base:**
  `NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_3_CANDIDATE.md` —
  SHA-256
  `cf274230c9fe52ddd04545f093fc2d24ddec22acd20bb596e630a7f26c22a175`;
  1,032 lines; 62,712 bytes — **recalculated; matched the correction
  instruction's expected identity exactly; read in full; preserved
  unchanged as historical candidate provenance; corrected by this
  v1_4.**
- **Superseded draft:**
  `NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_2_CANDIDATE.md` —
  SHA-256
  `7c2a3cbbb2eefc043ea2ce0cb46702a492682d108146479fcd7bfbf93b683fc2`;
  888 lines; 53,636 bytes — **recalculated; read in full; preserved
  unchanged as historical candidate provenance; corrected by v1_3.**
- **Superseded draft:**
  `NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_1_CANDIDATE.md` —
  SHA-256
  `11bae39baf312b381ecd8d5449957698aa30cc0736e253a51c549122e69e075d`;
  805 lines; 48,109 bytes — **recalculated; read in full; preserved
  unchanged as historical candidate provenance; corrected by v1_2.**
- **Superseded draft:**
  `NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_0_CANDIDATE.md` —
  SHA-256
  `97fba39974b77c7f5ed748e483450cc9a557c11c4e0706ccf7f0e7543cb554e0`;
  627 lines; 35,932 bytes — **recalculated; read in full; preserved
  unchanged as historical candidate provenance; corrected by v1_1.**
- **Master V10** (SHA-256
  `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c`),
  **Defaults v2_2**
  (`6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696`),
  **cursorrules**
  (`5050d08825b93acd72a79d07946e43c8cbe537e079517ccfe66bcae8e30e96e9`),
  **Companion**
  (`cdcc6134e273014472ad288dc349ce0c7c525638a73929f7dede52d30d040aeb`)
  — present, consulted, governing. **Map v1_6**
  (`33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865`)
  and the **eight-bundle plan**
  (`2d6483d133bb3992ba079db43e7d663e8016cf8bf693f7b4c9c98005bcb88415`)
  — read, subordinate.

## 3. NESS-APPROVED VALUES — PRESERVED EXACTLY

**Ness-approved decision, recorded in the accepted Bundle 1
normalization record v1_1 §6 and carried identically by the governing
task instruction; preserved verbatim:**

> - N.H uses both a time limit and an attempt limit; whichever is reached
>   first stops the retry.
> - Technical failures get up to 3 total attempts: original try + 2
>   retries.
> - Bad/unsafe/unsupported answer drafts must be recorded as rejected/bad
>   attempts with the rejection reason, then get 1 careful retry.
> - Extra retries after the normal limit are allowed only if something
>   real changed, such as new memory, new instruction from Ness, better
>   context, fixed missing evidence, repaired tool/file/search problem, or
>   a solved blocker.
> - Live chat technical retry gaps: 10 seconds, then 30 seconds.
> - Background/nightly technical retry gaps: 1 minute, then 3 minutes.
> - Bad/unsafe answer draft retry happens carefully right away after
>   recording the rejected draft and reason.
> - N.H may stop early if retrying is clearly useless or unsafe.
> - If retries are used up and N.H still cannot finish safely, it must
>   stop, say why, keep the work record, and save the unfinished state so
>   it can continue later only if something real changes.
> - No fake success, no hidden failure, no endless retry, no turning a
>   rejected draft into the final answer.

The governing correction instruction carries Ness's approved values
with the **time limit made explicit and complete**:

- Every retry episode has **both an attempt limit and an elapsed-time
  limit; whichever is reached first stops retrying.**
- **The live-chat elapsed-time maximum is 7 minutes.**
- **The background/nightly elapsed-time maximum is 15 minutes.**
- **The elapsed-time clock begins when the first attempt fails and the
  retry episode begins.**
- The 10-second/30-second and 1-minute/3-minute values are **minimum
  waiting gaps between attempts — they are not the total deadline**
  (§4, §6).
- The recorded real-change list ("such as new memory, …") is **examples,
  not a closed list** — a non-exhaustive "such as" preserved exactly
  (§10); repetition alone is never a real change.

**No retry count, delay, gap, deadline, or wall-clock number beyond
these explicit Ness values exists anywhere in this package, and none is
invented.**

## 4. THE RETRY-BUDGET CONFIGURATION RECORD — VERSIONED, DECLARED

**The record:** `b9_retry_budget_config` [proposed] — the declared,
versioned configuration record that accepted B9's existing
`retry_budget_ref` (and, for the substantive rule, `retry_policy_ref`)
references at R1. Append-only and versioned: a change is a **new
version record**, never an edit; every admission binds the exact
version it used; no silent change is possible.

**Record shape [all field names proposed — value carriage only]:**

| Field | Content |
|---|---|
| `config_id` / `config_version` / `schema_version` | The record's identity and version |
| `technical_max_total_attempts` | `3` — total attempts including the original (§5) |
| `technical_gap_schedule.live_chat` | `[10 seconds, 30 seconds]` — **minimum waiting gap** before episode ordinal 2, before episode ordinal 3 (§5, §6) |
| `technical_gap_schedule.background_nightly` | `[1 minute, 3 minutes]` — **minimum waiting gap** before episode ordinal 2, before episode ordinal 3 (§5, §6) |
| `elapsed_time_max.live_chat` | `7 minutes` — the episode's real stop deadline (§6, §7) |
| `elapsed_time_max.background_nightly` | `15 minutes` — the episode's real stop deadline (§6, §7) |
| `elapsed_clock_start` | `episode_first_failure_record` — the clock begins when the first attempt fails and the retry episode begins (§6) |
| `substantive_careful_retry_limit` | `1` — exactly one careful retry per rejected draft/proposal episode |
| `substantive_retry_timing` | `immediate_after_durable_rejection_record` — no scheduled waiting gap; the durable record is the prerequisite; **immediate never bypasses the episode deadline** (§7) |
| `early_stop_permitted` | `true` — recorded early stop per §8 |
| `continuation_rule` | `real_change_record_required` — per §10 |
| `real_change_categories` | The named §3 examples — a non-exhaustive "such as" list — **plus the truthful catch-all `other_real_change`** (a written explanation and supporting evidence references required); **every category requires evidence references; repetition or passage of time alone is never a real change** (§10) |

**How these values provide the accepted dual bound (mechanical
explanation, required):** the retry episode is bounded by **both** an
attempt limit and an elapsed-time limit, and whichever is reached first
stops retrying — realized as two independent admission gates that must
**both** permit, checked **before starting every retry** (§7). The
**attempt gate** is the count bound: durable attempt records <
`technical_max_total_attempts`. The **time gate is a real deadline, not
a gap sum**: `episode_deadline = the episode's first durable failure
record + elapsed_time_max` for the episode's recorded class (§6) — 7
minutes live chat, 15 minutes background/nightly. The 10 s/30 s and
1 min/3 min values are **minimum waiting gaps only** between attempts;
they never define or extend the deadline. No retry begins after either
limit has been reached. **When the deadline passes while waiting**, the
episode stops without starting the next retry, and truthful time
exhaustion is recorded (§9). **When the deadline passes while an attempt
is already running**, nothing is force-cancelled and no source-operation
timeout or terminal rule is overridden — that attempt finishes under its
governing source seam, and no further retry is admitted afterward. **The
execution duration of a source operation is bounded by that operation's
own existing timeout rules, which remain with their existing owner —
this package neither sets nor changes any source-operation execution
timeout.**

## 5. ATTEMPT-COUNT SEMANTICS — PERMANENT NUMBERS AND EPISODE ORDINALS

Two distinct counters exist, and they never substitute for one another:

- **`attempt_number` — permanent, group-wide, monotonic:** the number
  inside accepted B9's existing `attempt_id = {retry_group_id, attempt
  number}`, unchanged. It increases monotonically across the whole
  retry group — across every episode — and **never resets and never
  repeats.** Each admission binds the next unused number (§7).
- **`episode_attempt_ordinal` [proposed] — the per-episode position:**
  bound to `retry_episode_id`; the position at which that episode's
  attempt allowance and waiting-gap schedule apply. For a technical
  episode it is limited to **1, 2, or 3** under Ness's existing
  three-total-attempt value. It restarts at 1 in each new episode
  **without ever touching the permanent number.**

**Initial episode:**

- **The source seam's original execution is episode ordinal 1, by
  reference** — the seam's own first execution, never a B9 admission.
  When its durable outcome classifies `technical_retryable`, B9's group
  records it (R0 group establishment / R3-pattern recording) as
  ordinal 1, holding permanent attempt number 1.
- **B9-admitted technical retries are episode ordinals 2 and 3** — at
  most 2 retries, exactly as decided — carrying permanent attempt
  numbers 2 and 3. Permanent group attempt numbers remain unique.

**Later same-identity episode (after a real recorded change, §10):**

- It stays under the **same `retry_group_id`** only when the source
  seam confirms that the canonical inputs are unchanged (§10).
- Its **first admitted re-attempt is episode ordinal 1**, even though
  it is a B9-admitted execution rather than the source operation's
  historical first execution; its **permanent `attempt_number` is the
  next unused monotonically increasing number in the group** — never a
  reset, never a reuse.
- Further attempts in that episode use **ordinals 2 and 3** and the
  existing two waiting gaps; the episode receives the already-defined
  fresh deadline, **beginning when its own ordinal-1 attempt durably
  fails** (§6).

**Changed canonical inputs (§10):** a new source-operation identity and
therefore a **new retry group**, with normal initial-episode semantics
in that new group; attempts inside the old group are **never continued
or renumbered.**

- **The technical attempt gate counts per episode:** committed attempts
  belonging to **that exact episode**, counted by
  `episode_attempt_ordinal` — it never recounts attempts from
  predecessor episodes; three committed ordinals close that episode's
  allowance.
- **Counting is derived from durable records only:** the permanent next
  number, the episode ordinal, and the per-episode count are all
  reconstructed lookup-first from committed attempt entries and the
  recorded original outcome — never an in-memory counter, never a
  guess, never a skipped-bound interpretation, never a collision.
- **At most one live attempt per group** — accepted B9 R1, consumed
  unchanged; no value in this package weakens it.
- **The classes are bounded separately, exactly as decided:** the one
  careful substantive retry is a single admitted attempt in its own
  bounded substantive sequence (limit 1); it neither consumes nor
  extends the technical schedule, and technical attempts never consume
  the careful-retry allowance.

## 6. SCHEDULE IDENTIFICATION AND DURABLE CLOCK ANCHORS

- **`schedule_class`** [proposed] ∈ {`live_chat`,
  `background_nightly`} — recorded on each durable attempt-outcome
  record **at the moment the outcome is durably recorded**, taken from
  the source operation's own recorded execution context (the live-chat
  front door versus background/nightly processing, per the seam/cycle
  that ran it). B9 consumes the recorded class; it never guesses one. A
  missing or unreadable class → **no admission; fail closed; no default
  class** (§15).
- **Minimum-gap anchor (a wait floor, never a deadline):**
  `next_admission_not_before = outcome_record.committed_at +
  technical_gap_schedule[recorded class][next episode_attempt_ordinal − 1]`
  [proposed] — **indexed by the episode ordinal, never by the permanent
  group-wide attempt number** (a group-wide number such as 4, 5, or 6
  never indexes the two-entry schedule): **no scheduled technical gap
  exists before ordinal 1**; the first declared gap applies before
  ordinal 2; the second before ordinal 3. Computed at admission time
  from durable records only.
  **At a later same-identity episode's ordinal-1 admission no such
  anchor exists — no earlier outcome exists inside that episode — and
  none is claimed: the admission binds the explicit durable state
  `no_gap_before_ordinal_1` [proposed] in its place (§7); no waiting
  gap is invented.**
  Recovery recomputes the identical anchor from the same records; no
  in-memory timer exists to lose; **no anchor exists without a durable
  outcome record.**
- **Episode deadline anchor (the real stop deadline — technical and
  substantive careful-retry episodes alike):**
  `episode_deadline = episode_first_failure_record.committed_at +
  elapsed_time_max[deadline class]` [proposed] — **the elapsed-time
  clock begins at the durable first-failure/rejection record that
  begins that episode**: the first durable technical-failure record for
  a technical episode; the durable B24 rejection record for a
  substantive careful-retry episode. That record is the clock's start,
  and its recorded `schedule_class` fixes the episode's deadline class
  once (7 minutes live chat; 15 minutes background/nightly). One clock
  per episode — a continuation episode (§10) has its own clock,
  beginning at that episode's own first durable failure/rejection
  record. Recovery recomputes the identical deadline from the same
  records; no second clock, no averaging, no extension.
  **At a later same-identity episode's ordinal-1 admission the deadline
  does not yet exist — its clock has not started — and no deadline
  evidence is claimed: the admission binds the explicit durable state
  `deadline_pending_from_first_durable_failure` [proposed] in its place
  (§7). The deadline record is created only from ordinal 1's first
  durable `technical_retryable` failure, which also fixes the episode's
  `schedule_class`; the 7-minute/15-minute clock is never started
  earlier, and if ordinal 1 succeeds or ends in a non-technical
  outcome, no episode deadline is ever created (§7).**
- **How the 10 s / 30 s and 1 min / 3 min gaps and the 7 min / 15 min
  deadlines are stored and consumed:** stored once, declaratively,
  inside the versioned §4 configuration record; consumed by reference at
  each R1 admission, which binds the exact config version, the exact
  gap-anchor evidence, and the exact deadline evidence it used — **or,
  at a later same-identity episode's ordinal-1 admission, the explicit
  `no_gap_before_ordinal_1` and
  `deadline_pending_from_first_durable_failure` states in their place
  (§7).** Gap 1
  (10 s live / 1 min background) is the minimum wait before **episode
  ordinal 2**; gap 2 (30 s live / 3 min background) is the minimum wait
  before **episode ordinal 3** — of each technical episode, initial or
  later (§5); the deadline (7 min live / 15 min background) bounds the
  whole episode from its first failure. Nothing else consumes them.
- **Class recorded per anchor:** if successive outcomes of one group are
  recorded in different execution contexts, the **gap** consumed for the
  next admission is the one for the class recorded **on the most recent
  durable outcome — the anchor's own record**, while the **deadline
  class stays fixed at the episode's first failure record.** No
  averaging, no third schedule, no invented value.

## 7. ADMISSION — BOTH GATES MUST PERMIT (WIRING ONTO B9 R0/R1)

**Technical retry admission** (class `technical_retryable`) — R1 commits
an attempt entry only when **all** of the following hold, each consumed
from accepted B9 or supplied by these values:

1. The group's latest classified outcome is `technical_retryable`
   (accepted §3 routing — held, privacy-refused, indeterminate, terminal
   classes refuse per accepted R0, unchanged).
2. **No live attempt exists for the group** (accepted R1, unchanged).
3. No live hold exists on the source or its inputs (§12; accepted
   B9/B-HOLD, unchanged).
4. **Attempt gate (per episode):** committed attempts of **that exact
   episode**, counted by `episode_attempt_ordinal`, <
   `technical_max_total_attempts` (= 3 per episode; the initial
   episode's ordinal 1 is the seam's original execution, by reference) —
   attempts from predecessor episodes are **never recounted** (§5).
5. **Minimum-gap gate:** now ≥ the §6 gap anchor for this admission —
   a wait floor only, never a deadline; **indexed by the episode
   ordinal** (no scheduled gap before ordinal 1; the first declared gap
   before ordinal 2; the second before ordinal 3).
6. **Deadline gate:** now < the §6 `episode_deadline`. **Both the
   attempt limit and the deadline are checked before starting every
   retry; no retry begins after either limit has been reached —
   whichever is reached first stops retrying.** A deadline that passes
   **while waiting** stops the episode without starting the next retry,
   with truthful time exhaustion recorded (§9). A deadline that passes
   **while an attempt is running** forces nothing: the attempt finishes
   under its governing source seam (no forced cancellation, no override
   of the seam's own timeout and terminal rules), and no further retry
   is admitted afterward.
7. The bound `retry_budget_ref` resolves to an existing, readable §4
   config version (accepted row 14 fail-closed, now with declared
   content).
8. The episode is neither exhausted nor early-stopped (§8–§9) — or a
   **new** episode is opened under an unconsumed real-change record
   (§10).

**Admission binding (one atomic compare-and-commit, one winner):** each
admitted attempt atomically binds `retry_group_id`; the **next unused
permanent `attempt_number`**; the resulting `attempt_id`;
`retry_episode_id`; `episode_attempt_ordinal`; and the exact
budget-config version, gap-anchor evidence, and deadline evidence
used — **except a later same-identity episode's ordinal-1 admission,
which binds the two explicit durable states below in place of the
gap-anchor and deadline evidence that cannot yet exist.** Concurrent
admissions still admit exactly one winner (accepted R1); losers observe
and append nothing. **No reset, collision, or skipped-bound
interpretation is possible:** the permanent next number, the episode
ordinal, the per-episode count, and the correct ordinal-indexed gap are
all reconstructed lookup-first from durable records — never from an
in-memory-only counter (§5, §14).

**Later-episode ordinal-1 admission (special, mechanically explicit):**
a later same-identity technical episode may open **only** through the
committed §10 real-change consumption record, and **only** when the
source seam confirms that the canonical inputs are unchanged (§10). Its
ordinal-1 admission is one atomic compare-and-commit binding:

1. `retry_group_id`;
2. the **next unused permanent `attempt_number`**;
3. the resulting `attempt_id`;
4. `retry_episode_id`;
5. `episode_attempt_ordinal = 1`;
6. the exact retry-budget configuration version;
7. the real-change consumption authorization — the committed §10
   consumption record;
8. the explicit durable state **`no_gap_before_ordinal_1`** [proposed] —
   no scheduled waiting gap applies before ordinal 1, and none is
   invented;
9. the explicit durable state
   **`deadline_pending_from_first_durable_failure`** [proposed] — the
   episode deadline does not yet exist and will be created only from
   ordinal 1's first durable `technical_retryable` failure; the
   7-minute/15-minute clock is not started earlier.

**No actual gap-anchor evidence and no actual deadline evidence exist
at this admission, and none is claimed.** One winner; losers observe
and append nothing.

**Ordinal-1 outcome behavior (later same-identity episode):** if
ordinal 1 **succeeds**, the operation completes normally through its
seam; no episode deadline is ever created and no further retry is
admitted. If ordinal 1 **durably fails as `technical_retryable`**, that
durable failure record becomes the episode's **deadline anchor**, the
source of its fixed **`schedule_class`**, and the **outcome anchor**
from which the first waiting gap before ordinal 2 is calculated —
ordinals 2 and 3 then bind the real durable gap-anchor and deadline
evidence before admission, exactly as already designed. If ordinal 1
ends in a **protected, terminal, held, privacy-refused, or
indeterminate** outcome, it routes through that existing outcome's own
rules (§3 classes; §12; §15; accepted B9) — **no technical deadline
path is manufactured.**

**Substantive careful-retry admission** (class `terminal_substantive`,
the bad/unsafe/unsupported draft or proposal rejection) — accepted B9
requires a recorded, adopted policy reference **plus** a per-case
authorization reference; this wiring **realizes — never modifies — that
slot**:

- `retry_policy_ref` → this package's decided rule content (once
  accepted): exactly **1** careful retry per rejected-draft episode.
- `retry_authorization_ref` → **the durable B24 rejection record of this
  exact case** (its identity bound at admission): the recorded rejected
  draft/proposal together with its exact distinct rejection reason
  (§13). **No durable rejection record → no admission** — the record is
  the prerequisite, exactly as decided ("recorded first").
- **Both gates checked before admitting the careful retry — whichever
  is reached first stops retrying:** (a) the **attempt allowance** —
  exactly one careful retry per episode, none yet admitted; and (b) the
  **episode deadline** — now < the §6 deadline, whose clock began at
  the durable rejection record that begins this episode (7 minutes live
  chat; 15 minutes background/nightly). No careful retry begins after
  either limit has been reached.
- **Timing — immediate, never a deadline bypass:** the careful retry is
  admissible at the first admission evaluation after the rejection
  record durably exists; **no scheduled waiting gap applies.**
  "Immediate" is measured from durable readiness, never from a
  wall-clock promise, and never before the record exists — **and it
  does not bypass the deadline gate.**
- **Deadline passed before admission:** if a crash, delay, or recovery
  causes the episode deadline to pass before the careful retry is
  admitted, the careful retry is **not started**; truthful **time
  exhaustion** is recorded (§9, §15).
- **Deadline passes after the careful retry has started:** nothing is
  force-cancelled and no source-seam timeout or terminal rule is
  overridden — the attempt finishes under its governing source seam,
  and **no further retry is admitted afterward.**
- **Careful — mechanically carried:** the admitted careful attempt
  mandatorily references the rejection record as input context, so the
  re-attempt is made in full view of the recorded defect. How the
  producing pass uses it is the seam's own SMART work, unchanged.
- **Exactly one:** a second substantive admission for the same episode
  is refused — terminal substantive stands (§13), reopenable only per
  §10.

## 8. EARLY STOP — RECORDED, TERMINAL FOR THE EPISODE

N.H may stop early when retrying is clearly useless or unsafe: recorded
as a group disposition event [proposed: `retry_early_stopped`] carrying
the recorded cause class (`clearly_useless` / `unsafe`) and its evidence
references, followed by the accepted R4 parent terminal for the
requesting operation. An early stop **ends admission for the episode**;
it is never recorded as success, never hidden, and never disguised as
exhaustion — the disposition names the real cause. Because the episode's
own durable finding is that retrying is clearly useless or unsafe,
continuing without anything real changing would contradict that recorded
finding: **continuation after an early stop uses the same §10 gate as
exhaustion — a new bounded episode under a real recorded change.** No
new policy is created by this; it is the mechanical consequence of the
recorded cause.

## 9. EXHAUSTION — STOP, SAY WHY, KEEP THE RECORD, SAVE THE STATE

**Exhaustion** = the episode can admit no further attempt: the attempt
gate is reached (that exact episode's three committed ordinals, or the
one careful retry already
admitted); **the episode deadline is reached — on the technical and the
substantive careful-retry paths alike** — while waiting (the next
retry — including a careful retry not yet admitted because a crash,
delay, or recovery consumed the window — never starts; truthful **time
exhaustion** is recorded) or while an attempt is running (that attempt
finishes under its governing source seam — no forced cancellation, no
override of the seam's own timeout and terminal rules — and no further
retry is admitted afterward); the one careful retry was rejected again;
or an early stop was recorded — with no committed success.

- **Recorded:** the group disposition event [proposed:
  `retry_episode_exhausted`] names which gate stopped it and references
  the attempts' durable outcomes; accepted B9's refusal/fail-closed
  recording (row 14 pattern: the exhausted reference is named) applies
  unchanged.
- **Says why:** the R4 parent terminal and the disposition carry the
  recorded why; surfacing to Ness follows the existing output and §7Q
  gates — no new surface is invented, and nothing is silent (no hidden
  failure).
- **Keeps the work record; saves the unfinished state:** the source
  seam's own durable state **is** the preserved unfinished state —
  accepted B9's settled facts stand: the failed job stays `in_progress`
  with its recorded pass failure; terminal jobs are never re-selected;
  nothing is deleted or rewritten (true destruction remains prohibited).
  This wiring adds only that the exhaustion disposition **references**
  that preserved seam state, so a later continuation finds everything
  lookup-first.
- **No fake success, no hidden failure, no endless retry, and a rejected
  draft never becomes the final answer** — carried as absolute here and
  in §13.

## 10. THE REAL-CHANGE RECORD AND NEW BOUNDED EPISODES

**The record:** `b9_real_change_record` [proposed] — the durable record
without which no continuation after exhaustion or early stop exists.
**It is append-only and immutable: no field of it is ever edited after
creation** — consumption lives in a separate record (below).

| Field [proposed] | Content |
|---|---|
| `change_record_id` | Stable identity |
| `change_category` | One of the **named examples** — `new_memory` / `new_ness_instruction` / `better_context` / `fixed_missing_evidence` / `repaired_tool_file_search` / `solved_blocker` — **or the truthful catch-all `other_real_change`**. Ness's list is "such as": **examples, not a closed list.** Any value outside this vocabulary is malformed |
| `change_explanation` | **Required for `other_real_change`:** a written explanation of what genuinely changed; optional but recordable for the named examples |
| `change_evidence_refs` | References to the real change's own durable records (the new memory's identity, the recorded Ness instruction, the repaired tool's recovery record, …) — **required for every category, including `other_real_change`**; references only, never copies, never re-scored. **Repetition alone is never a real change** — mere passage of time, repeated desire, or a re-request carries no evidence of change and is refused |
| `target_group_ref` | The exhausted/early-stopped retry group this record may reopen |
| `recorded_at` / `schema_version` | Timestamp; schema version |

**The consumption record:** `b9_real_change_consumption_record`
[proposed] — a **separate append-only record**; the real-change record
itself is never mutated.

| Field [proposed] | Content |
|---|---|
| `consumption_record_id` | Stable identity |
| `real_change_record_ref` | The consumed `change_record_id` |
| `consumer_ref` | What the consumption opened: the **new retry episode** (same source identity, §"identity rule" below) **or the new source operation** (changed canonical inputs) |
| `claim_result` | The atomic claim's committed result — the single winner's commit evidence |
| `committed_at` / `schema_version` | Timestamp; schema version |

- **Single consumption — one winner, mechanically, append-only:**
  `real_change_consumption_key = stable_hash(change_record_id +
  "consumption_v1")` [proposed] — **exactly one committed consumption
  record can ever exist per real-change record**, enforced lookup-first
  with one atomic compare-and-commit; racing consumers admit exactly one
  winner; losers observe the committed consumption and append nothing; a
  reuse attempt against a consumed record is **refused and logged.**
  Every further continuation requires its own **new, unconsumed**
  real-change record — which is what prevents a single change from
  becoming endless authorization. **No record is edited to mark
  consumption; the consumption record is the consumption.**
- **A new bounded episode, never an extension:** the new episode carries
  `episode_number`, `predecessor_episode_ref`, and
  `authorizing_change_ref` [proposed], and receives a **fresh bounded
  budget under the same §4 values — its `episode_attempt_ordinal`
  positions restart at 1 (§5): it opens only through the committed
  consumption record and only with the source seam's confirmation of
  unchanged canonical inputs; its ordinal-1 admission uses the §7
  special binding — the explicit `no_gap_before_ordinal_1` and
  `deadline_pending_from_first_durable_failure` durable states in place
  of gap-anchor and deadline evidence that cannot yet exist; its first
  admitted re-attempt is
  ordinal 1, a B9-admitted execution rather than the source operation's
  historical first execution; further attempts are ordinals 2 and 3
  under the existing two waiting gaps; every attempt's permanent
  `attempt_number` continues the group's monotonic sequence with the
  next unused number, never resetting or repeating; and its own fresh
  episode deadline begins when its ordinal-1 attempt durably fails
  (§6, §7)** — the exhausted episode's records stand untouched and are
  never reopened, recounted, or extended. The bound is preserved
  because every episode is itself bounded and every episode after the
  first requires its own consumed change record.
- **Same identity or new identity — the canonical-input rule:** a
  continuation re-attempts under the **same source-operation identity
  only when it is still genuinely the same operation and its canonical
  inputs are unchanged** — a repaired temporary technical condition may
  stay under the same identity **only when the governing source seam
  confirms its canonical inputs are unchanged** (the seam's canonical
  key binds its inputs; the seam, not B9, is the authority on that
  confirmation). **A change that alters the canonical input** — new
  memory, a new Ness instruction, better context, new or repaired
  evidence, or another input-altering change — **must create a new
  source-operation identity under that source seam, linked by reference
  to the earlier failed operation. Inputs are never silently changed
  inside the old identity** — a different input set is a different
  operation. The consumption record's `consumer_ref` names whichever it
  truthfully is: the new episode of the old identity, or the new linked
  operation. **A new source-operation identity is a new retry group,
  using normal initial-episode semantics in that new group (§5);
  attempts inside the old group are never continued or renumbered.**
- **Boundaries preserved:** a real-change record is admission
  authorization only. It is never evidence (no re-scoring, no double
  evidence — repetition and change records add no certainty to any
  outcome); it is **not** a bypass of the other accepted classes — a
  live hold still refuses (§12), `privacy_refused` still requires the
  gate's own recorded changed-authorization state (accepted B9 §3,
  unchanged; that record belongs to the gate, not to this record type),
  and `indeterminate` still resolves only through the seam's own
  recovery.

## 11. SEAM — B10 (RETRY IS NEVER A REREAD)

Consumed exactly as accepted B9 §7, B10 §3, and the coordination note
state — no value in this package changes it:

- A B9 retry re-attempts the **same incomplete canonical operation**
  under the seam's own identity to complete its one outcome. **It never
  creates a reread trigger, a reread claim, or a reading layer** — and
  mechanically cannot: the seam's canonical identity admits at most the
  one committed result.
- **A completed reading — including the honest `insufficient_context`
  fallback — can be examined again only through B10**, under a recorded
  §7H trigger. B9 refuses a "retry" request naming a completed reading
  and says so in its refusal record without creating a trigger.
- §7H's scheduled-automatic-retry trigger class remains served by B9's
  technical retry **only while the original operation is open and
  incomplete**; these values give that service its bounds and nothing
  more.
- **Changed information is never another retry inside the old reread
  claim:** for B10, new or changed information creates a **new valid
  §7H trigger and a new claim** under B10's existing rules — the
  new-trigger/new-claim path — never a re-entry, extension, or mutation
  of the old reread claim, and never a B9 retry represented in its
  place.

## 12. SEAM — B-HOLD (NO RETRY AROUND A HOLD; RELEASE MANUFACTURES NOTHING)

- **A live hold refuses admission:** class `dependency_blocked_held`
  (accepted B9 §3/R0; accepted B-HOLD §6/§9 row 17) — the retry request
  while held is **refused and recorded** (`retry_refused`), never
  silently queued around the hold.
- **The refusal is free of side effects on both sides:** it consumes
  **no** attempt count, starts **no** gap anchor, opens **no** episode,
  and touches **no** hold record — so hold time never silently expands,
  resets, or consumes a hidden retry budget, and the retry budget is
  never silently drained by a hold.
- **Release alone manufactures nothing:** B-HOLD's release is its own
  evidence-verified interface under accepted A29's automatic
  track/check/release rule — consumed, untouched. After release, no
  success exists that did not commit, and **no automatic retry fires
  from the release event itself**: any later admission is a fresh R0/R1
  evaluation under the group's recorded state — attempt counts stand,
  anchors stand, exhaustion and early stops stand, and a real-change
  record is still required where §10 requires one.

## 13. SEAM — B24 (RECORD FIRST; ONE CAREFUL RETRY; DISTINCTIONS PRESERVED)

- **Durable record first:** the bad/unsafe/unsupported draft or proposal
  and its **exact distinct rejection reason** — B24's settled categories
  (`fabrication_invention`; `malformed_output`; `incomplete_output`;
  `unsupported_certainty`; `positional_semantic_confusion`;
  `reading_mode_violation`; `evidence_self_contradiction`), populated
  only on `rejected` — are durably recorded through B24's own records
  **before** the one careful retry can be admitted; the admission binds
  that record as its per-case authorization (§7). **The rejected draft
  never becomes the answer** — no path promotes it, exactly as accepted.
- **If the careful retry passes B24:** normal processing continues
  through the seam unchanged — B9 records the outcome; nothing else
  happens under B9's name.
- **If it is rejected again:** the episode is **terminal substantive** —
  it stays terminal unless a later real recorded change authorizes a new
  bounded episode (§10). Nothing else reopens it; B-HOLD is never a way
  to park it (coordination note §2.3, consumed).
- **`insufficient_context` only through the governed path:** it may be
  produced **only** through B24's governed insufficiency-assessment path
  (§2.10) on an externally adjudicated, committed
  `genuine_insufficiency_confirmed` — never otherwise. **Technical retry
  exhaustion, provider failure, malformed validation configuration, or
  an unsafe/rejected draft is never relabeled `insufficient_context`**:
  technical stays `technical_failure`; privacy/relevance stays
  `authorization_failed`; an invalid validator configuration stays
  `indeterminate_unvalidated` with its `validation_boundary_reasons`; a
  proposal defect stays `rejected`. Rejection count is never proof of
  insufficiency (accepted B24, consumed).
- **The authorized fallback point [proposed — narrowed; filling exactly
  the slot accepted B24 §2.10/§5.3 defers to B9]:** the insufficiency
  assessment and B24's deterministic fallback may open **only for an
  eligible B24 proposal, and only after its authorized careful-retry
  sequence has truthfully ended** — the durable rejection record exists
  and the one careful retry was consumed and rejected again — **and
  B24's own accepted fallback conditions are reached**, through B24's
  unchanged mechanics and invocation conditions. **Membership in a class
  B9 does not retry never opens the fallback.** Privacy refusal, missing
  authorization (`authorization_failed`), a live B-HOLD, `indeterminate`
  recovery, technical failure, validation-boundary failure
  (`indeterminate_unvalidated`), and every other protected terminal
  outcome **remain their own outcomes and never open the insufficiency
  assessment.** B24's accepted five-way distinction — **proposal
  rejection / technical failure / authorization failure /
  validation-boundary failure / genuine insufficiency** — is preserved
  verbatim; the fallback never converts between them. Reaching the
  fallback point is a **timing fact, never evidence**; rejection count
  alone never proves insufficient context; **only B24's separately
  authorized external adjudication result
  `genuine_insufficiency_confirmed` may produce `insufficient_context`.**
  No new fallback meaning exists or is invented.

## 14. IDENTITY, IDEMPOTENCY, CONCURRENCY, CRASH RECOVERY, PARTIAL COMPLETION

**Consumed unchanged from accepted B9:** `retry_group_id`, `attempt_id`,
`retry_request_op_id`, the retry-state record set, R0–R4, the nine
idempotency points, and all nineteen §8 recovery rows.

**Added by this wiring [all proposed]:**

- **Identities:** the §4 config record identity {`config_id`,
  `config_version`}; the §10 change record identity and the §10
  consumption record identity (`real_change_consumption_key`); the
  episode identity `retry_episode_id = {retry_group_id, episode_number}`
  and the per-attempt `episode_attempt_ordinal` bound to it (§5) —
  alongside the accepted permanent `attempt_id`; all derived from the
  durable disposition and attempt chain — never from memory.
- **Idempotency:** each admission atomically binds {`retry_group_id`,
  the next unused permanent `attempt_number`, `attempt_id`,
  `retry_episode_id`, `episode_attempt_ordinal`, config version,
  gap-anchor evidence, deadline evidence} — **a later same-identity
  episode's ordinal-1 admission binds, in place of the last two, the
  explicit `no_gap_before_ordinal_1` and
  `deadline_pending_from_first_durable_failure` states (§7)**; a repeat
  identical admission
  finds the committed entry (accepted point, now with bound values);
  real-change consumption commits a **separate append-only consumption
  record** under its uniqueness key with exactly one winner — **no
  record is ever edited**; config, change, and consumption records are
  append-only — repeats converge, edits do not exist.
- **Concurrency:** accepted single-winner R1 unchanged; racing
  consumptions of one change record admit exactly one committed
  consumption record; losers observe and append nothing.
- **Crash recovery (lookup-first, on top of accepted rows 1–19):**
  the **permanent next `attempt_number`**, the
  **`episode_attempt_ordinal`**, the **per-episode count**, the
  **correct ordinal-indexed gap**, the episode deadline, episode state,
  and consumption bindings are all reconstructed from durable records
  only — **no reset, no collision, no skipped-bound interpretation, no
  in-memory-only counter**; a crash
  between the durable rejection record and the careful-retry admission
  leaves the unconsumed rejection record findable — the admission may
  then proceed **only while the episode deadline (§6) has not passed; a
  deadline that passed during the crash/delay window admits nothing,
  and truthful time exhaustion is recorded** (row 2 pattern); a crash between change-record creation
  and consumption leaves the change record unconsumed and findable, and
  a crash between the consumption commit and the episode's first
  admission leaves the committed consumption record findable —
  lookup-first completes idempotently from it; a crash mid-attempt
  resolves through the seam's own recovery first (accepted row 3), with
  no admission while the attempt is live.
- **Later-episode ordinal-1 recovery (four distinguished cases,
  lookup-first):** (1) **Real-change consumption committed, ordinal-1
  admission absent** — resume or complete the same ordinal-1 admission
  idempotently, using its explicit `no_gap_before_ordinal_1` and
  `deadline_pending_from_first_durable_failure` states; nothing else is
  admitted. (2) **Ordinal-1 admission committed, no durable source
  outcome** — resolve through the source seam's own recovery first
  (accepted row 3); admit nothing else while the attempt is live or
  unresolved. (3) **Ordinal-1 durable `technical_retryable` failure
  exists, but its derived deadline record, gap bindings, or related B9
  records are incomplete** — reconstruct them lookup-first and append
  only the missing records from that durable outcome; nothing is
  recalculated differently. (4) **Ordinal-1 success or another terminal
  outcome exists** — complete the matching disposition idempotently;
  **never create a deadline or a later retry that the outcome does not
  permit.**
- **Partial completion:** per accepted rows 2–5 and 17 — the seam's
  durable terminal is authoritative; B9's records complete idempotently
  from that evidence; nothing re-runs.

## 15. FAIL-CLOSED MATRIX (VALUES LAYER, ON TOP OF ACCEPTED B9 §9)

| Condition | Behavior |
|---|---|
| §4 config record missing, unreadable, or version-unbound | No admission; no default; fail-closed event naming the reference (accepted row 14, unchanged) |
| `schedule_class` missing or unreadable on the anchor record | No admission; fail closed; **no default class** |
| Anchor evidence missing (no durable outcome record) | No admission; no anchor exists to satisfy |
| Attempt gate reached (three ordinals committed in that exact episode; predecessor episodes never recounted) | Exhaustion disposition (§9); further requests refused with recorded status |
| **Episode deadline reached while waiting** (technical and substantive careful-retry paths alike) | The next retry never starts; **truthful time exhaustion** recorded; exhaustion disposition (§9) |
| **Careful retry requested after the episode deadline** (a crash, delay, or recovery consumed the window before admission) | Not started; **truthful time exhaustion** recorded; exhaustion disposition (§9) |
| **Episode deadline passes while an attempt is running** | Nothing force-cancelled; no source-seam timeout or terminal rule overridden; the attempt finishes under its seam; **no further retry admitted afterward** |
| Careful retry requested without a durable rejection record | Refused — the per-case authorization is missing (accepted R1, unchanged) |
| Second substantive admission for one episode | Refused — terminal substantive stands |
| Real-change record missing; category outside the named examples and `other_real_change`; `other_real_change` without a written explanation; evidence references absent (repetition alone); or already consumed (a committed consumption record exists) | Refused; no new episode; reuse attempts logged |
| **Later-episode ordinal-1 admission without the committed consumption record, or without the source seam's confirmation of unchanged canonical inputs** | Refused; no episode opens; nothing bound |
| **Ordinal 1 of a later episode ends protected, terminal, held, privacy-refused, or indeterminate** | Routed through that outcome's own existing rules; **no technical deadline path manufactured**; no further technical retry admitted from it |
| Contradictory episode or consumption evidence (including a permanent `attempt_number` collision or repeat, or an `episode_attempt_ordinal` collision or reset inside one episode) | `indeterminate`, surfaced, never guessed (accepted row 16 pattern) |
| Any attempt to bypass R1, a hold, a privacy gate, or the acceptance boundary | Refused + violation log (accepted row 19; B-HOLD row 20; gates unchanged) |

## 16. §0B OPERATIONAL LOGGING (VALUES LAYER)

Accepted B9's §10 log set is consumed unchanged (`retry_requested` /
`retry_absorbed` / `retry_refused`; `retry_attempt_admitted` — now
binding the exact config version and anchor evidence, or, for a later
same-identity episode's ordinal-1 admission, the explicit
`no_gap_before_ordinal_1` and
`deadline_pending_from_first_durable_failure` states (§7);
`retry_attempt_outcome_recorded`; `retry_group_disposition`;
`retry_terminal`; `recovery_applied` / `recovery_noop` /
`fail_closed_event`). Added canonical state/disposition events
[proposed]: `retry_budget_config_recorded` (each config version);
`real_change_recorded`; `real_change_consumed` (each committed
**consumption record** — the append-only consumption commit, with the
consumer bound; never an edit of the change record);
`retry_early_stopped`; `retry_episode_exhausted` (naming the stopping
gate — attempt gate, **time deadline**, careful-retry rejection, or
early stop). One
append-only log per real operation; canonical state records are never
operational logs and never extra evidential votes; **no double
evidence** — a change record, a config record, or any amount of
repetition never makes an outcome more true; §7Q governs access to every
record; no silent internal operation.

## 17. RELEASE CONDITION — DESIGN-LEVEL ONLY

**Until this candidate is independently audited and explicitly accepted
by Ness, the accepted defaults stand unchanged:** R1 fails closed with
no declared budget (accepted row 14), the substantive rule's terminal
stays terminal, and every accepted fail-closed boundary governs. Once
accepted, this package's values are the declared configuration and
adopted-rule content that accepted B9's `retry_budget_ref` /
`retry_policy_ref` slots reference — **at design level only.** Master,
map, Defaults, and cursorrules integration, and every implementation,
remain open and separately authorized; nothing runtime is unblocked,
built, integrated, or implemented by this file.

## 18. MUST REMAIN OPEN (NONE CLOSED OR BIASED HERE)

- **Source-operation execution timeouts** — with their existing owners,
  untouched (§4).
- **B1/B26** retrieval quantities, system-failure stop/retry/degraded
  design — open with their owners.
- **A25, A29, A31, and every other Ness policy** — consumed only where
  accepted; nothing decided, reopened, or biased.
- **The A25/B10 manual-reread compatibility path and B10's mode slot** —
  not this package's; open under its own governed work.
- **A1** — remains BLOCKED per its blocker record; untouched and not a
  dependency of this package.
- **B-CYCLE-8, the final Bundle 1 audit, Bundle 1 completion, and
  whole-system wiring** — open (including where each cycle's activation
  actually runs; these values give the bounds and gaps, not the cycle
  wiring).
- **Master V10 / map / Defaults / cursorrules integration** — open;
  later, separately authorized, Ness-accepted work.
- **The sealed 5,521-root batch** — untouched; never reopened, changed,
  or appended to.
- **All coding, migration, runtime, PC, store, marker, production, and
  implementation work** — unauthorized; awaiting Ness's separate
  implementation authorization.
- No other open Register-A/B item is closed or biased by this candidate.

## 19. DESIGN-COMPLETE CONDITION FOR THIS CANDIDATE

This candidate is design-complete **for the B9 retry-values wiring**
when: Ness's values are preserved exactly with their recorded provenance
and no invented number (§3); the versioned budget/configuration record
is defined and consumed by reference (§4) with the dual bound realized
as a **real elapsed-time deadline racing the attempt limit** — both
checked before every retry, gaps as minimum waits only, truthful time
exhaustion recorded, mid-attempt deadlines forcing nothing — and
source-operation timeouts left with their owner; the attempt-count
semantics distinguish the **permanent monotonic `attempt_number`**
(inside accepted `attempt_id`, never reset or reused) from the
**per-episode `episode_attempt_ordinal`** (1–3) — the initial episode's
original execution as ordinal 1 by reference, later same-identity
episodes restarting at ordinal 1 under the next unused permanent
number, the gate counting only that exact episode's ordinals, gaps
indexed by ordinal and never by a group-wide number, and admission
atomically binding group, permanent number, `attempt_id`, episode,
ordinal, and the exact budget, gap, and deadline evidence — **with the
later-episode ordinal-1 admission binding, in place of gap and deadline
evidence that cannot yet exist, the explicit no-gap and
deadline-pending durable states, opening only through the committed
consumption record with seam-confirmed unchanged inputs, its deadline
created only from ordinal 1's first durable technical failure, its
success creating no deadline, and its protected or terminal outcomes
routed through their own rules** (§5, §6, §7);
schedule identification,
the minimum-gap anchors, and the episode deadline anchor — beginning at
the durable first-failure/rejection record of each episode, on both
paths — are defined with the declared storage and consumption (§6);
admission requires the
attempt, minimum-gap, and deadline gates plus the accepted rules, and
the careful retry realizes B9's policy+authorization slot with the
durable rejection record as the per-case reference, **checked against
both its one-retry allowance and the episode deadline — "immediate"
meaning no scheduled waiting gap and never a deadline bypass, a
deadline passed before admission admitting nothing with truthful time
exhaustion, and a mid-retry deadline forcing nothing and admitting no
further retry** (§7); early stop
(§8), exhaustion with unfinished-state preservation and recorded why
(§9), and the real-change rule — **non-exhaustive "such as" categories
with a truthful `other_real_change`, a separate append-only consumption
record with one atomic winner, a new bounded episode never an
extension, and the canonical-input identity rule** (§10) — are all
defined; the B10, B-HOLD, and B24 seams carry every stated requirement,
including the new-trigger/new-claim rule for changed information, the
preserved five-way distinction, and the **narrowed fallback point
unreachable from protected or unrelated outcomes** (§11–§13); identity,
idempotency, concurrency, crash recovery, and partial completion are
answered lookup-first with nothing ever edited (§14); the fail-closed
matrix and §0B set are defined (§15–§16); the release condition stays
design-level behind audit and acceptance (§17); and every §18 item
remains open — subject to ChatGPT's independent audit and Ness's
explicit acceptance.

## 20. CHANGE REPORT AND SELF-AUDIT

**File created:**
`NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md` —
the only file created by this task item, from the verified v1_3, which
is preserved unchanged as historical candidate provenance (v1_0, v1_1,
and v1_2 likewise preserved). **Nothing
existing was
modified:** accepted B9, B10, B-HOLD, and B24 and their closure records,
the coordination note, the normalization record and its acceptance
record, accepted A29, accepted A25 and the accepted connection chain,
Master V10, Defaults, `cursorrules`, the Companion, the map, the plan,
and every accepted, closure, active-candidate, and historical file — all
preserved byte-identically; nothing committed, pushed, moved, renamed,
overwritten, or deleted.

**Self-audit:** authority order preserved — PASS. Ness's values
preserved verbatim from the accepted normalization §6 and the governing
correction instruction, including the 7-minute and 15-minute elapsed
maxima and the clock-start rule; no retry count, delay, gap, deadline,
or wall-clock number invented beyond them; source-operation timeouts
left with their owner — PASS. **The 7/15-minute values are real stop
deadlines, not retry gaps**: the deadline gate and the attempt gate are
both checked before every retry and race correctly — whichever is
reached first stops retrying; the gaps are minimum waits only; a
deadline passing while waiting stops the episode with truthful time
exhaustion; a deadline passing mid-attempt forces no cancellation and
overrides no source-seam timeout or terminal rule, and admits no
further retry — **and the deadline gate applies to the technical and
substantive careful-retry paths alike, each episode's clock beginning
at its own durable first-failure/rejection record** — PASS.
**Permanent `attempt_number` monotonic across the group inside accepted
`attempt_id`, never reset or reused; `episode_attempt_ordinal` (1–3)
applies each episode's allowance and gaps; the initial episode's
original execution is ordinal 1 by reference with B9 retries as
ordinals 2 and 3; a later same-identity episode — seam-confirmed
unchanged canonical inputs only — restarts at ordinal 1 under the next
unused permanent number, with its fresh deadline at its ordinal-1
attempt's durable failure; changed canonical inputs open a new group
with initial-episode semantics and never continue or renumber the old
group; the gate counts only that exact episode's ordinals; gaps index
by ordinal — none before 1, the first before 2, the second before 3 —
never by a group-wide number such as 4, 5, or 6; admission atomically
binds group, permanent number, `attempt_id`, episode, ordinal, and the
exact budget, gap, and deadline evidence with one winner — the
later-episode ordinal-1 admission binding, in their place, the explicit
no-gap and deadline-pending durable states; everything
reconstructed from durable records — no reset, collision, skipped-bound
interpretation, or in-memory-only counter** — PASS.
**Later-episode ordinal-1 admission consistent:** it opens only through
the committed consumption record with the source seam's confirmation of
unchanged canonical inputs; it atomically binds group, the next unused
permanent number, `attempt_id`, episode, `episode_attempt_ordinal = 1`,
the exact budget configuration, the consumption authorization, and the
explicit `no_gap_before_ordinal_1` and
`deadline_pending_from_first_durable_failure` durable states; no actual
gap-anchor or deadline evidence is claimed to exist at that admission;
no waiting gap is invented and the 7-minute/15-minute clock is never
started earlier; ordinal-1 success creates no deadline and admits
nothing further; an ordinal-1 durable technical failure becomes the
deadline anchor, the schedule-class source, and the gap anchor for
ordinal 2, with ordinals 2 and 3 binding the real durable evidence
exactly as designed; protected, terminal, held, privacy-refused, or
indeterminate ordinal-1 outcomes route through their own rules with no
manufactured technical deadline; the four recovery cases resolve
lookup-first, appending only missing records; and the initial episode
is unchanged — the seam's original execution stays recorded by
reference, never a B9 admission, its durable technical failure
supplying the actual deadline and gap evidence for ordinals 2 and 3 —
PASS. At most 2 technical
retries per episode; gap anchors and the
episode deadline from durable records only — PASS. Careful retry:
durable rejection record
first; exactly one; **both the one-retry allowance and the episode
deadline verified before admission; "immediate" means no scheduled
waiting gap and never a deadline bypass; a deadline passed before
admission (crash, delay, or recovery) admits nothing and records
truthful time exhaustion; a mid-retry deadline forces nothing and
admits no further retry;** immediate from durable readiness; realizes —
never
modifies — B9's policy+authorization slot; a rejected draft never
promoted — PASS. Early stop and exhaustion recorded with real causes;
unfinished state preserved in the seam's own durable records; says why
through existing gates; no fake success, no hidden failure — PASS.
**Real change stays non-exhaustive** — the named examples are "such as";
`other_real_change` is supported truthfully with a required written
explanation and evidence references; every category requires evidence
references; repetition or passage of time alone is never a real
change — **stated without contradiction everywhere, including the
corrected §4 configuration row; a full-file sweep found no remaining
closed-list wording** — PASS. **Every record is truly append-only**: no
`consumed_by_episode_ref` or any later-edited field exists; consumption
is a separate append-only consumption record with one atomic winner per
change record, lookup-first; the original real-change record is never
mutated — PASS. **Canonical inputs govern identity**: same identity only
while genuinely the same operation with seam-confirmed unchanged
canonical inputs; input-altering changes create a new linked
source-operation identity; inputs never silently changed inside the old
identity — PASS. B10 seam: same-operation re-attempt only; no trigger,
claim, or layer created; completed readings only via B10; **changed
information creates a new valid trigger and claim, never another retry
inside the old reread claim** — PASS. B-HOLD seam: refused and recorded,
never queued around; no count, anchor, or hold record side effects;
release manufactures no success and no automatic retry — PASS. B24
seam: five-way distinction preserved with accepted vocabulary; no
relabeling into `insufficient_context`; **the fallback is unreachable
from privacy refusal, missing authorization, B-HOLD, indeterminate
recovery, technical failure, validation-boundary failure, or any other
protected or unrelated outcome — it opens only for an eligible B24
proposal after its authorized careful-retry sequence truthfully ends**,
and only `genuine_insufficiency_confirmed` produces
`insufficient_context` — PASS. One live attempt per group; accepted
identities, boundaries, and all nineteen recovery rows consumed
unchanged; additions idempotent and lookup-first — PASS. Fail-closed
with no defaults anywhere a reference or class is missing — PASS. §0B
one-operation/one-log with no double evidence — PASS. Candidate status;
nothing accepted, adopted, integrated, implemented, or
`PACKAGE_COMPLETE`; no closure receipt created; all §18 items open
(including A1, the final Bundle 1 audit, Master/map integration,
B-CYCLE work, and all implementation); sealed batch protected; no
implementation or hidden integration began — PASS.

---

*End of `NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md`
— CANDIDATE, unaudited, awaiting ChatGPT's independent audit and Ness's
explicit acceptance. Accepted B9, B10, B-HOLD, and B24 are not modified;
until acceptance the accepted fail-closed defaults continue to govern and
a substantively rejected proposal remains terminal; nothing is
integrated, implemented, or unblocked at runtime by this file.*

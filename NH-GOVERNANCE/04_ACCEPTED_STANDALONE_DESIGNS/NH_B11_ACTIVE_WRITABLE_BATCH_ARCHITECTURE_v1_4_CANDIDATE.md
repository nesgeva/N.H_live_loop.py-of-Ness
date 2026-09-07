# NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md

## §1 — Status, authority, scope, and no-implementation statement

**Status:** DESIGN CANDIDATE — NOT ADOPTED — NOT IMPLEMENTED — NOT
`PACKAGE_COMPLETE`. Requires ChatGPT's independent audit and Ness's explicit
acceptance.

**Package ID:** B11 — Active Writable-Batch / Sealed Multi-Box Architecture
(Bundle 1 — Memory and reading foundation; first Bundle-1 standalone
candidate).

**Date:** July 3, 2026.

**Corrects:** `NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_3_CANDIDATE.md`
(verified on disk before this correction as byte-identical: SHA-256
`5ee2bee15fafaea0849a5e0e58b2b6610c600c3593c3a00063a3ade664ff8c5c`, 1,407
lines, 124,301 bytes). v1.0 (`518c639d…ce17`), v1.1 (`1bbc02b1…05fe`), v1.2
(`eef8e9bd…280f`), and v1.3 are all preserved unchanged as historical
candidate provenance. v1.4 is one bounded mechanical correction pass
applying exactly the five verified consequential defects from ChatGPT's
independent re-audit of v1.3 — two CRITICAL: (1) recovery row 37 "cleared
the fence and cancelled" a `commit_fenced` generation, a transition the
append-only phase model made illegal; (2) WB0/WB1/WB2 operational logs all
rode the single parent `ingest_operation_id`, breaking one-operation/one-log
— and three IMPORTANT: (3) the claim↔`root_id` binding was one-directional,
letting a cancelled-and-retried claim reserve a second identity; (4) the LB1
vocabulary, §9.1 stale-plan wording, and the §6.4 "two simultaneous
actives" invariant contradicted the corrected selection and abandonment
rules; (5) `bootstrap_incomplete` was used as though it were a batch state.
The frozen scope, fourteen-item closure checklist, blocking standard,
prohibitions, and open dependencies of the original instruction are
unchanged. No unrelated improvement was added.

**Task type:** Implementation-neutral mechanical architecture. No Ness concept
or policy decision is required, requested, or made by this package.

**Governing authority order:**
1. `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` (adopted by Ness June 29
   2026; governing; its stale internal adoption sentence is superseded)
2. `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`
3. `01_AUTHORITATIVE/cursorrules`
4. `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`

**Sources read for this candidate:** the four governing files (Master §6B
root-store schema and state, §7E/TSC ingestion boundary rules, §0B, §7Q,
§11 designed-but-not-built items incl. the batch-mechanics slot; Defaults
§3B/§3C root record and store; cursorrules; Companion §6B); the current map
`NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` (C-STORE row, B11
register entry, B10/B16/B21/B23/B1/B26 adjacent entries); the workflow
`NH_FULL_DESIGN_COMPLETION_WORKFLOW_v1_0.md` (B11 universal prerequisite);
the confirmed eight-bundle plan
`NH_REPLACEMENT_EIGHT_BUNDLE_DEPENDENCY_PLAN_v1_0_CANDIDATE.md` (SHA-256
`2d6483d133bb3992ba079db43e7d663e8016cf8bf693f7b4c9c98005bcb88415`; content
accepted July 1 2026; file confirmed by Ness July 3 2026 — Bundle 1, B11
deliberately early); the accepted A2 v1.8 package and closure record; the
accepted B24 v7 package (SHA-256 `7f5762e5bc3d7d0fa554ad41426d2cc2f14fb775
3a79b67fbd675f6c6b8a2171`) and closure record; the A2 status pointer v1.1.
Actual files govern; all local copies hash-verified before writing.

**Authority corrections applied (as instructed):** Master V10 governs every
conflict; the existing 5,521-root batch is **permanently sealed for future
ingestion** — never reopened, unsealed, or appended to; historical wording in
Decision Defaults §3C ("Only Ness may lift the seal as a deliberate separate
act") and any similar `cursorrules` wording is **recorded drift**, not the
governing B11 design (correctable only through a future versioned Defaults/
cursorrules candidate — see §16); A2 v1.8 and B24 v7 are accepted and
package-complete for their standalone scopes and are not reopened, modified,
reinterpreted, or expanded here.

**No implementation:** this file contains architecture only. No code, no
patch-ready pseudocode, no store creation, no migration, no disk
modification, no seal action, no terminal commands, no runtime artifacts. No
storage engine, programming language, filesystem layout, index technology,
or immediate code API is chosen.

---

## §1A — Correction matrices

### §1A.0 — v1.3 → v1.4 (this correction)

| # | Severity | v1.3 defect | v1.4 resolution | Sections |
|---|---|---|---|---|
| 1 | CRITICAL | Row 37 and Trace 2 had recovery "clear the committed fence and cancel the generation," but the phase model defined only `granted → cancelled` and `granted → commit_fenced → committed` — the recovery exit was illegal, and row 7 cancelled reservations without distinguishing `granted` from `commit_fenced` | **Third legal path** `granted → commit_fenced → recovery_released_no_commit` [proposed] — a distinct recovery-only terminal phase, never ordinary `cancelled`, committable only under the four strict row-37 proofs (exclusive recovery authority; no live writer; exact batch and reserved `root_id` checked; root non-commit conclusively proven); on commit the generation is permanently unable to append, its reservation and completion right are extinguished, the claim may return to `available_uncommitted`, the canonical `root_id` stays bound to the same claim, and a later WB1 may regrant; missing proof → `indeterminate_recovery_required`; ordinary cancellation stays legal only from `granted`; row 7 explicitly applies only while `granted`; duplicate recovery of the release is a no-op | §8.0, §8.1, §9.3, §11 (rows 7, 37, 40), §11A, §12, §14 |
| 2 | CRITICAL | Only the parent `ingest_operation_id` existed while §14 defined WB0/WB1/WB2 operational logs plus the WB3 terminal — several operational logs under one operation identity | **Parent/child operation hierarchy:** `ingest_operation_id` = the parent end-to-end seam invocation; every separately executed internal real operation (claim establishment/lookup, the WB1 boundary, the WB2 boundary, a cancellation, a recovery resolution, target resolution) carries its own stable child operation ID referencing the parent and receives **exactly one** operational log; WB3 is the **single terminal operational record of the parent**, written after the children and canonical records resolve; a child log is never a second parent log; no operation ID ever has two operational logs; retries and recovery find the existing log by identity | §7.2, §7.3, §7.4, §8.1, §11 protocol, §14, §11A |
| 3 | IMPORTANT | The authority guaranteed one claim per `root_id` but not one `root_id` per claim — a cancelled-and-retried claim could present a second identity, stranding the first | **One-to-one binding:** the first successful WB1 binds one immutable `reserved_root_id` to the permanent claim and reserves it in §8.2A atomically; every later generation and retry must reuse it; same claim + different `root_id`, or same `root_id` + different claim → rejected before append as an identity conflict; contradictory authoritative evidence → `indeterminate_recovery_required`; the canonical payload-integrity reference explicitly covers the complete prepared seven-field payload while `root_id` is bound independently; every "embeds the claim + generation reference" wording replaced — associations live in external B11 transaction/ownership evidence, the root stays exactly seven fields | §8.0, §8.2A, §7.3, §11 (row 43), §11A, §12 |
| 4 | IMPORTANT | LB1 still carried `shutdown_seal_successor` requiring an LB-P plan (contradicting §6.3/§9.2A); §9.1 kept "superseded with no effects"; §6.4 claimed two simultaneous `active` batches are prevented while Trace 9 legitimately has two LB3-activated candidates | **Vocabulary and invariant corrected:** LB1 reasons are `no_active` (genesis and post-shutdown/reactivation, under the idempotent LB1 creation plan alone) and `rotation` (under the committed LB-P plan); `shutdown_seal_successor` explicitly superseded and unable to authorize any path; §9.1 carries the honest stale-plan rule; the invariant is **two simultaneous writable selections are prevented** — multiple activated-but-never-selected candidates may temporarily exist, are never writable (§5.3), close via the legal abandonment, and are never treated as a same-epoch selection fork | §6.1, §6.4, §9.1, §11 (rows 3, 4, 48), §11A |
| 5 | IMPORTANT | `bootstrap_incomplete` was used as though it were a batch lifecycle state, though `batch_state` does not include it | **Separate `bootstrap_completion_status`** [proposed] (`incomplete` / `complete` / `recovery_required`) — derived from the bootstrap record set, never a `batch_state`: before the bootstrap state event no canonical historical state exists; after it the state is `sealed`; completion becomes `complete` only when registration, state event, bootstrap manifest, **and** the required §8.2B historical root-ownership coverage all validate; a sealed batch with incomplete bootstrap metadata stays never-writable and excluded from completeness claims; no partial step touches anything historical | §4.5, §5.1, §8.2B, §10.1, §11 (rows 54–55), §12, §14, §11A |

### §1A.1 — v1.2 → v1.3 (preserved provenance)

| # | Severity | v1.2 defect | v1.3 resolution | Sections |
|---|---|---|---|---|
| 1 | CRITICAL | The write-ahead alternative let a delayed executor whose "current generation" check preceded cancellation still append after the claim returned to `available_uncommitted` and a new generation was granted — "a cancelled generation can never commit" was asserted, not mechanically guaranteed | **Per-generation append commit fence:** generations carry append-only phases `granted` / `commit_fenced` / `cancelled` / `committed`; WB2 begins only through one compare-and-commit `granted` → `commit_fenced`; cancellation only through `granted` → `cancelled`; both compete on the same authoritative state and exactly one wins; a fenced generation forbids cancellation, return-to-available, and regrant; a cancelled generation forbids fencing and append; the append boundary verifies the durable `commit_fenced` generation **immediately before committing**; eight fence recovery rows with strict clear-fence conditions | §7.3, §7.6, §8.0, §8.1, §11 (rows 18, 22, 35–42), §11A, §12, §14 |
| 2 | CRITICAL | `root_id` global uniqueness was claimed while the only `root_id → batch_id` structure was the post-commit, non-gating PR index — two different claims could present or generate the same `root_id` | **Canonical pre-commit root-ownership authority (§8.2A):** one permanent entry per `root_id` binding the owning claim key, canonical payload integrity, and status `reserved_for_claim` / `committed_to_batch`; WB1 atomically verifies-or-reserves the `root_id` for its claim inside the generation/reservation boundary; a different claim presenting the same `root_id` is rejected before WB2; cancellation never releases the `root_id`; WB2 requires the fence **and** matching root ownership, then commits the entry to the owning batch; registry failure/coverage/conflict fails admission closed; the PR index stays rebuildable and non-authoritative; the 5,521 historical `root_id` values receive an external bootstrap-registration contract (§8.2B) with coverage-before-writes fail-closed and no invented capture claims; all associations live outside the seven-field root (§8.2C) | §7.3, §8.1, §8.2, §8.2A–C, §8.3, §8.4, §10.2, §11 (rows 43–46), §11A, §12, §14, §16 |
| 3 | IMPORTANT | LB4 always committed selection **and** predecessor cutoff, but genesis, reactivation, and post-shutdown successor selection have no writable predecessor to cut off | **Two LB4 modes of one selection authority:** mode A (initial/reactivation) commits only the new selection against expected `none/genesis` or the exact existing epoch, verifies the predecessor cannot admit, creates no cutoff, and never touches the historical batch; mode B (rotation cutover) keeps the atomic selection+cutoff under LB-P; a post-shutdown successor is a reactivation-creation path governed by its idempotent LB1 creation plan — never a new rotation/seal plan and never a second cutoff; seven new recovery rows | §4.3, §6.1, §6.3, §9.2A, §11 (rows 47–53), §11A, §12, §14 |
| 4 | IMPORTANT | Recovery rows closed activated-but-never-selected batches `invalid` while §5.2 had no legal `active → invalid` transition; "stale plan has no effects" overstated erasure | **Bounded never-selected abandonment:** `active → invalid` is legal only when all seven conditions are proven (LB3-activated; never selected at any epoch; zero WB1 reservations; zero roots; no unresolved generation; conclusively prevented by a competing selection or stale plan; evidence recorded); an ever-selected batch can never use it; the honest stale-plan rule — no **new** effects, existing external records preserved, losing candidates closed only through the legal transition, nothing silently erased | §5.2, §6.1, §6.3, §11 (rows 3, 27, 28, 34), §11A, §12 |
| 5 | IMPORTANT | Discovery (§10.1) validates every batch through its manifest, but the historical bootstrap created only a registration and a state event — no manifest | **External bootstrap manifest** (third append-only record) carrying the applicable §4.2 machine facts — identity, version, origin class, `schema_compat_ref = v1`, in-place location, references to the registration and state event, verified seal evidence, externally recorded seal summary and root-count/integrity references, and the records-existing-facts statement; completion ordering registration → state event → manifest; the batch is fully discoverable only when the complete set validates; partial sets resume idempotently or rest `bootstrap_incomplete`/`recovery_required` with no writability and no false completeness claim | §4.5, §10.1, §11 (rows 54–55), §11A, §12 |
| 6 | IMPORTANT | Overlapping active log names (`plan_committed` vs `rotation_plan_committed`; separate selection and cutoff logs for one atomic LB4; claim-commit vs append-commit) blurred one-operation/one-log | **Canonical state records vs §0B operational logs separated:** manifests, state events, claim/ownership/fence events, root-ownership entries, and cutoff records are machine facts establishing state — not extra operational logs and never extra evidential votes; every atomic combined boundary emits **one** operational log carrying all of its effects (one LB-P log; one rotation-LB4 log with selection+cutoff; one mode-A selection log explicitly recording no new cutoff; one shutdown-LB5 log; one WB1 log with grant+root-ID reservation+batch reservation; one WB2 result; one WB3 terminal per `ingest_operation_id`); duplicate vocabulary merged or marked superseded | §14, §11A |

### §1A.2 — v1.1 → v1.2 (preserved provenance)

| # | Severity | v1.1 defect | v1.2 resolution | Sections |
|---|---|---|---|---|
| 1 | IMPORTANT | WB0 "acquired" a live-owned claim while WB1 separately committed the reservation said to carry ownership — `owning_reservation_ref` could not point to a durable reservation before WB1 existed; no recovery covered a crash between them; `cancelled` and `mismatch` were modeled as claim states, conflicting with claim reuse and with `committed` finality; the canonical payload-integrity reference was unbound | **Complete claim lifecycle:** the permanent claim binds `claim_key` + immutable canonical `payload_integrity_ref` from establishment; authoritative statuses `available_uncommitted` / `owned_uncommitted` / terminal `committed` / `indeterminate_recovery_required`, with mismatches as **attached integrity incidents**, never states; **WB0 establishes with no owner and no append right** (a crash leaves a harmless reusable claim); **WB1 is one atomic compare-and-commit** creating the ownership generation and its matching reservation together; WB2 commits only for the currently effective generation; cancellation is an atomic per-generation boundary returning the claim to `available_uncommitted`; transfer = cancel → available → later WB1; ten new recovery rows | §6.4, §7.3, §7.5, §7.6, §8.0, §8.1, §8.3, §8.4, §9.3, §11 (rows 7, 16–25), §11A, §12, §14 |
| 2 | IMPORTANT | §4.5's `(none — bootstrap) → sealed` violated §5.2, which allowed only `(none) → preparing` | **One narrowly bounded legal transition** `(none — historical bootstrap) → sealed`, valid only under seven simultaneously required conditions (pre_b11_historical origin; committed bootstrap registration; store and `.nh_roots.sealed` referenced in place and verified; recording cause; no ordinary lifecycle operation performed; nothing historical changed); for every non-historical batch `(none) → sealed` remains illegal | §4.5, §5.2, §10.1, §11A Trace 6 |
| 3 | IMPORTANT | Successor creation and LB4 ran "under the rotation plan" while the plan committed only at LB5; shutdown sealing ran LB5 without any admission cutoff, leaving in-flight reservations unclassifiable | **LB-P rotation/seal-plan commit** precedes every dependent action (identity, target batch, cause class, expected epoch/batch, successor intent, provenance, trigger reference — no numeric values invented); rotation order LB-P → successor LB1–LB3 → LB4 → LB5 → drain → verification → LB6; **shutdown LB5 atomically commits the admission-cutoff marker + admission stop + `active`→`sealing` + plan reference**; one stable `admission_cutoff_id` classifies every reservation (LB4 cutoff for rotation, LB5 cutoff for shutdown); nine new recovery rows | §5.3, §6.1, §7.6, §8.1, §9.1, §9.2, §9.2A, §9.3, §11 (rows 26–34), §11A, §12, §14 |

### §1A.3 — v1.0 → v1.1 (preserved provenance)

| # | Severity | v1.0 defect | v1.1 resolution | Sections |
|---|---|---|---|---|
| 1 | CRITICAL | The WB2 key was called global, but reservations were keyed per epoch and the global index existed only post-commit (WB3) — the same identity could reserve in two epochs and commit an immutable root in two batches, unrepairably | **Global ingestion claim (§8.0, WB0):** one canonical claim keyed to the authoritative §7E `capture_id` + operation type, acquired-or-found atomically **before** any per-batch reservation; exclusive live ownership across all batches and epochs; append-only lifecycle; durable transfer/cancellation on rotation; one linearization rule binding WB2 to the claim's `committed` transition; the post-commit index is rebuildable material, never the first duplicate defense; claim-coverage failure → new admission fails closed; recovery inspects the claim first | §7.2, §7.3, §8.0, §8.1, §8.3, §8.4, §11, §11A, §12, §14 |
| 2 | IMPORTANT | Writability demanded the current selection epoch while drain let pre-rotation reservations commit into the now-unselected batch — mutually inconsistent | **One cutover protocol:** ordinary **admission** requires the active currently selected batch; a durable pre-cutoff WB1 reservation is a **bounded completion right** for that exact claim and exact old batch; LB4 commits the successor selection **and** the predecessor's admission-cutoff as one durable boundary; completions validate reservation, claim ownership, payload integrity, batch identity, and cutoff relationship; cancelled reservations lose the right before claim transfer; LB6 still requires every pre-cutoff reservation proven committed or durably cancelled | §5.3, §6.1, §6.4, §7.6, §9.2, §9.3, §11 rows 10/12 |
| 3 | IMPORTANT | Fork recovery "determined one winner" even when chain evidence cannot identify one | **No invented winner:** a same-epoch fork immediately blocks ordinary writes; retention only on committed integrity/provenance proof that the other record was never validly committed; equally valid records → no timestamp/identifier/order/lexical tie-breaker; both batches non-writable or `recovery_required`; roots preserved; no reservation cancelled or redirected by guess; fail-closed pending a later separately authorized repair mechanism (not designed here) | §4.4, §11 row 4, §11A, §12, §14, §16 |
| 4 | IMPORTANT | §4.5 placed `state: sealed` inside the historical batch's registration record, bypassing the derived-state event chain | **Bootstrap-registration contract:** external registration assigns the permanent `batch_id` and references the store and `.nh_roots.sealed` in place; an external append-only **bootstrap state event** canonically establishes `sealed` (`origin_class = pre_b11_historical`), explicitly recording a pre-existing condition — performing no sealing and modifying nothing; the historical batch thereafter obeys the same derived-state and registry-validation rules; permanently ineligible for selection or writes | §4.5, §5.1, §10.1, §11A |
| 5 | IMPORTANT | The §0B append-operation record completed in WB3 while WB4 could acknowledge after WB2 — success could be reported before the permanent operation record existed | **Terminal log before acknowledgement:** the terminal outcome record is durably appended (WB3) before WB4 returns that outcome; index/counters/coverage are separated as rebuildable post-commit work (PR) that never gates acknowledgement; root committed without its terminal log → no success acknowledgement until recovery appends the missing log idempotently; logging failure never uncommits the root; exactly one terminal log per real operation | §7.3, §7.4, §11 rows 8/9, §11A, §14 |

---

## §2 — Preservation inventory and settled rules (consumed, never weakened)

| Settled rule (source) | B11 relationship |
|---|---|
| The existing 5,521-root batch is sealed: `.nh_roots.sealed` exists; `append_root()` refuses while it does (Master §6B; map C-STORE) | Preserved untouched. B11 represents the batch as permanently sealed **without modifying it** (§4.5). No future write path may target it (§6, §9, §12). |
| Seven-field root schema, v1, sealed: `id` (uuid4) · `subject` (provenance batch tag — never reinterpreted) · `timestamp` (ISO 8601) · `content` · `re_reads` (`[]` = root) · `source_title` (string/None) · `role` (speaker; required on new writes) (Master §6B; Defaults §3B) | Referenced, never altered. Schema changes require a new `schema_version` and deliberate Ness adoption — outside B11 (open: B21). B11 validates shape against the declared `schema_compat_ref` only. |
| `append_root()` is called by §7E's internal path **only**; TSC and every other producer route through §7E; no direct file writes ever (Master TSC §29–§30; map C-STORE) | Preserved. B11 sits **between** §7E's eligibility outcome and the shared `append_root()` commit boundary as the mandatory batch-targeting seam (§7, §13). |
| RAW CAPTURE ≠ ROOT INGESTION; capture exclusion, authorization, blockers, speaker resolution, and eligibility are upstream (§7E; Defaults §3C) | Preserved. B11 consumes committed upstream evidence references and never re-decides them (§3, §7). |
| No root with `role = "unknown"`; no 8th field without a new `schema_version`; roots immutable once written; no destruction (Master §6B, §7Q) | Preserved. B11's mechanical validation refuses nonconforming payloads; recovery never rewrites a committed root (§11). |
| Atomic append; schema-validate before append; idempotency via record identity; duplicate-key refusals logged (map C-STORE) | Preserved and generalized across batches (§7, §8). |
| Quarantine and production stay separate; root evidence and prior-reading context stay separate (Master; B24 v7) | Preserved. B11 handles **roots only**; readings, quarantine, and promotion are other components (B16, C-READ). |
| §0B: one real operation → one append-only record; no recursive log-about-logging; no double evidence; logs never add truth weight; §7Q/§25 govern log access; active/cold per §0B (Master §0B) | Consumed as settled (§14, §15). Not redesigned. |
| DUMB does not interpret; SMART does not turn interpretation into fact (Master §0A) | B11 is entirely DUMB machinery (§15). |
| B11 must be complete before any second batch or any new live-root stream may write (map; workflow Phase 13; plan Bundle 1 boundary) | This package is that completion, as design only. |

---

## §3 — B11 ownership and non-ownership boundaries

**B11 owns (mechanical only):** batch identity; batch manifests and lifecycle
states; the canonical active-batch authority and selection; safe successor
creation; the root-write targeting seam and its transaction boundaries;
global cross-batch identity and mechanical duplicate prevention; sealing and
rotation mechanics; cross-batch discovery, identity lookup, and
index-registration structure; crash and partial-completion recovery for all
of the above; fail-closed behavior; component-specific §0B logging.

**B11 never owns (stays upstream, downstream, or in other packages):**
whether raw material qualifies to become a root (capture exclusion,
authorization, blockers, speaker resolution, §7E eligibility — upstream);
semantic meaning, relevance, truth, or semantic eligibility of content
(SMART/§7G/§7R — never B11); semantic near-duplicate policy (open; B11
prevents mechanically identical / identity-equivalent duplicate commits
only); retrieval ranking and retrieval-service failure policy (B1/B26);
reading production, validation, quarantine, promotion (C-READ, B24 — closed
standalone, B16 — open); reread wiring (B10, after A25); hold mechanics
(B-HOLD, after A29); retry **policy** and numerical retry values (B9); future
root-schema versions (B21); Person-Box cross-batch mechanics (B23); storage
engine, filesystem layout, index technology, capacity/time thresholds
(implementation/calibration — declared later, not invented here).

**DUMB statement (binding):** B11 moves, validates, identifies, stores,
seals, locates, and records. It never interprets meaning, determines
relevance, establishes truth, or chooses whether material is semantically
eligible. Every B11 record is a machine/provenance fact.

---

## §4 — Batch identity and manifest contract

### §4.1 Batch identity

- `batch_id` [proposed]: permanent, system-generated, globally unique across
  every batch that has ever existed in this N.H instance — active, sealing,
  sealed, interrupted, recovered, or invalid. Never reused, never reassigned,
  never derived from location. The generation scheme is an implementation
  choice; the uniqueness and permanence contract is binding.
- **Identity ≠ location:** the registry (§4.3) maps `batch_id` to an opaque,
  versioned `location_descriptor` [proposed]. Moving or re-hosting a batch's
  storage produces a **new location record for the same `batch_id`**; the
  identity, manifest chain, and every root's provenance are unaffected.
  Storage technology never leaks into identity.

### §4.2 Batch manifest

`batch_manifest` [proposed] — machine/provenance facts **only**; never
semantic evidence; never a copy or summary of root content:

| Field [all proposed] | Content |
|---|---|
| `batch_id` | The permanent identity |
| `manifest_version` | Version of this manifest record; manifests evolve append-only (a corrected manifest is a new version referencing its predecessor, never an edit) |
| `schema_compat_ref` | The exact root `schema_version` this batch accepts (v1 seven-field for the first successor; changes only via B21 + Ness adoption) |
| `created_at` / `creator_operation_ref` | Creation provenance (links the LB1 plan and LB2 commit, §5) |
| `initial_state_event_ref` | Pointer into the append-only state chain (§5) |
| `seal_summary` | Populated only at LB6: final `root_count`, content-integrity summary reference, seal timestamp, sealing-operation ref |
| `predecessor_batch_ref` / `successor_batch_ref` | Rotation lineage (successor set append-only at LB6/LB4 of the successor) |
| `origin_class` | `b11_created` / `pre_b11_historical` (§4.5) |

A manifest carries **no** root text, no interpretations, no relevance or
importance markers. A manifest, index, log, or checkpoint is never an
evidential vote about any root's content (§15).

### §4.3 Canonical active-batch authority

`batch_registry` [proposed] — the **single durable canonical authority** for
(a) which batches exist (one append-only `batch_registration` per batch) and
(b) which batch is the current active write target:

- `active_selection_record` [proposed]: append-only; carries
  `selection_epoch` [proposed] (strictly monotonic), the selected `batch_id`,
  the selecting operation ref, and the expected predecessor epoch.
- **Single-current invariant:** exactly one committed selection per epoch;
  the current selection is the highest committed epoch in an unbroken chain.
- **Serialized commit:** a selection commits through one durable
  compare-and-commit boundary against the exact expected prior state — the
  committed predecessor selection at exactly epoch N (rotation and
  reactivation), or the expected `none/genesis` state for the very first
  selection (§6.1 LB4 mode A). Two concurrent
  selectors cannot both commit N+1: the loser observes the winner's committed
  record and **adopts it** (idempotent convergence), never creating a rival.
- **Manifests are not activeness authority:** a batch's own records never
  make it active; only a current registry selection does. A batch claiming
  activeness without being the current selection is a mismatch (§12).

### §4.4 Conflicting, duplicate, stale, and missing claims — detection

| Condition | Detection | Effect |
|---|---|---|
| Two selection records claim the same epoch | Registry chain scan finds a fork | **Immediate fail-closed for ordinary writes**; recovery §11 row 4 — retention only on committed integrity/provenance evidence, **never an invented winner**; equally valid records leave both batches non-writable pending a later separately authorized repair (§16) |
| A selection points at a batch whose current state ≠ `active` | Cross-check selection ↔ state chain | Fail closed; recovery resolves by evidence |
| A writer holds a stale epoch | Every reservation binds `selection_epoch`; the append boundary re-checks it against current | Reservation refused/`interrupted`; caller re-resolves |
| No committed current selection | Registry lookup returns none | No ordinary writes; creation path §6 or recovery §11 row 5 |
| A batch's files/directories exist without a committed manifest + activation + selection | Writability rule §5.3 | Not writable — existence is never writability |

### §4.5 The existing 5,521-root batch — represented without modification

The pre-B11 batch enters the registry through the **bootstrap-registration
contract** — three external append-only records, touching nothing inside
the historical batch:

1. **External bootstrap registration** [proposed]: assigns the permanent
   `batch_id`; `origin_class: pre_b11_historical`; references the existing
   root store (`location_descriptor`) and the existing `.nh_roots.sealed`
   marker **in place** as `seal_evidence_ref`; `schema_compat_ref: v1`. The
   registration record carries **no state field** — state is never stored in
   a registration.
2. **External bootstrap state event** [proposed]: one append-only
   `batch_state_event` `{batch_id, from_state: (none — bootstrap),
   to_state: sealed, cause: bootstrap_records_pre_existing_seal,
   evidence_refs: [seal_evidence_ref], operation ref, timestamp}`. The event
   **records a pre-existing sealed condition; it performs no sealing and
   modifies nothing** — not the batch, not its store file, not its seal
   marker.
3. **External bootstrap manifest** [proposed]: one append-only
   `batch_manifest` satisfying the applicable §4.2 machine-fact contract for
   the historical batch: the permanent `batch_id`; `manifest_version`;
   `origin_class = pre_b11_historical`; `schema_compat_ref = v1`; the
   existing location reference (in place); the bootstrap-registration
   reference; the bootstrap-state-event reference; the verified
   seal-evidence reference; an **externally recorded** seal summary with
   root-count and integrity references; and the explicit statement that the
   manifest **records existing facts and performs no creation or sealing**.

**Bootstrap-completion ordering and status:** (1) registration →
(2) bootstrap state event → (3) bootstrap manifest referencing both. A
separate **`bootstrap_completion_status`** [proposed] — derived from the
bootstrap record set and the §8.2B coverage evidence, **never a
`batch_state`** — carries `incomplete` / `complete` / `recovery_required`.
Before the bootstrap state event exists, no canonical historical batch
state is yet established; after the legal event, the batch state is
`sealed` and never changes again. Completion status becomes `complete`
**only when the registration, the state event, the bootstrap manifest, and
the required §8.2B historical root-ownership coverage all validate**; until
then it is `incomplete` (or `recovery_required` on contradictory evidence),
the batch is excluded from completeness claims, and it remains never
writable — while its canonical `sealed` state stays accurate. The batch is
**fully discoverable only at completion status `complete`** (§10.1). A
crash leaving a partial set never affects historical bytes, never creates
writability, and never permits a false completeness claim: recovery resumes
the sequence idempotently or the status rests `incomplete` /
`recovery_required` (§11 rows 54–55). No partial bootstrap step touches
historical roots, files, seal markers, or existing indexes.

**Legality (the §5.2 bounded historical-bootstrap transition):** this event
is legal **only when all seven conditions hold simultaneously**:
(1) `origin_class = pre_b11_historical`; (2) the external bootstrap
registration is already committed; (3) the existing historical root-store
location is referenced **in place**; (4) the existing `.nh_roots.sealed`
evidence is **verified and referenced**; (5) the event's cause explicitly
states that it records a pre-existing sealed condition; (6) no ordinary
creation, activation, sealing, LB5, or LB6 operation is being performed;
(7) no historical byte, root, store, marker, identity, or index entry is
changed. Discovery and recovery validate these conditions whenever the
bootstrap event is examined (§10.1).

From that event forward, the historical batch participates in **the same
derived-state and registry-validation rules as every other batch** (§5.1):
its current state derives from its event chain exactly like any batch, and
discovery validates it identically (§10.1). It remains permanently
ineligible for active selection or ordinary writes — the registry cannot
select a `sealed` batch and the append boundary independently refuses sealed
targets (§6.4, §12); `sealed` is terminal for writability (§5.2).

---

## §5 — Lifecycle and legal-transition table

### §5.1 States

`batch_state` [proposed]: `preparing` / `active` / `sealing` / `sealed` /
`recovery_required` / `invalid`.

Current state is **derived from an append-only chain of
`batch_state_event`s** [proposed] (event: batch_id, from_state, to_state,
cause, operation ref, timestamp, evidence refs). No state field is ever
edited in place. **This rule has no exceptions:** the pre-B11 historical
batch's `sealed` state is established by its external bootstrap state event
(§4.5) and derived through the identical chain rule thereafter. The
separate `bootstrap_completion_status` (§4.5) is bootstrap metadata about
the external record set — **it is not a `batch_state` and adds no state to
this list**.

### §5.2 Legal and illegal transitions

| From → To | Legality | Durable evidence required |
|---|---|---|
| (none) → `preparing` | Legal — only via LB1 plan + LB2 manifest commit | Creation plan + committed manifest |
| (none — historical bootstrap) → `sealed` | **Legal only for the pre-B11 historical batch**, under all seven §4.5 legality conditions simultaneously; it records a pre-existing sealed condition and performs nothing. **For every non-historical batch, `(none) → sealed` remains illegal.** | Committed bootstrap registration + verified `.nh_roots.sealed` reference + the bootstrap state event with its recording cause |
| `active` → `invalid` (never-selected abandonment) | **Legal only when all seven are proven:** the batch was activated by LB3; it was **never** the committed selected batch at any epoch; it admitted **no** WB1 reservation; it committed **no** root; it owns **no** unresolved claim generation; a competing valid selection or stale-plan result **conclusively prevents** it from becoming the intended selection; and the invalidation event records that superseding selection or stale-plan evidence. **An `active` batch that was ever selected can never use this transition** — it follows normal cutoff, sealing, recovery, or integrity-failure rules. | Activation event + absence proofs (zero reservations, zero roots, zero live generations) + the superseding selection or stale-plan evidence, all recorded in the invalidation event |
| `preparing` → `active` | Legal — only via LB3 validation + activation event, then LB4 selection makes it the write target | Validation results + activation event + (for writes) current selection |
| `preparing` → `invalid` | Legal (abandoned or failed preparation; cause recorded) | Abandonment/failure event |
| `active` → `sealing` | Legal — only via LB5 seal-start within a committed rotation/seal plan | Rotation/seal plan + sealing event |
| `sealing` → `sealed` | Legal — only via LB6 after drain + verification (§9) | Drain-complete evidence + verification results + seal event + final manifest version |
| `sealing` → `recovery_required` | Legal on detected interruption | Recovery-detection event |
| any → `recovery_required` | Legal on crash-evidence detection; transient | Detection event |
| `recovery_required` → the state proven by evidence, or `invalid` | Legal — recovery resolves only to what committed records prove (§11) | Recovery-run records |
| `sealed` → anything writable (`active` / `preparing` / `sealing`) | **Illegal — no ordinary operation exists that performs it.** Sealing is irreversible through ordinary operation. | — |
| `invalid` → any writable state | **Illegal** | — |
| `preparing` → `sealed` | **Illegal** (a never-activated batch is abandoned to `invalid`, never sealed as if used) | — |
| `active` → `sealed` (skipping `sealing`) | **Illegal** — drain and verification are mandatory | — |
| `sealed` → `invalid` | Legal only as an integrity-failure **marking** (batch flagged, excluded from coverage claims); it never restores writability and never alters the batch's bytes | Integrity-failure event |

### §5.3 Writability rules (binding — admission and completion are distinct)

**Ordinary write-admission rule:** a batch admits a **new** WB1 reservation
**iff**: a committed valid manifest exists **and** its derived current state
is `active` **and** it is the current registry selection at the epoch the
writer resolved.

**Pre-cutoff completion rule:** a durable WB1 reservation granted **before**
the batch's committed admission cutoff (`admission_cutoff_id` — the LB4
cutover for rotation, the LB5 cutoff for shutdown-seal; §9.2/§9.2A) is a
**bounded
completion right** — its WB2 may complete into that exact batch (typically
while the batch is `sealing`), subject to the full §7.6 completion
validation. This right belongs only to that exact reservation and its exact
global claim; no unreserved or newly retried write may use it.

**No batch becomes writable merely because a file or directory exists.**
Failing admission while holding no valid pre-cutoff completion right → the
write does not proceed (§12).

---

## §6 — Active-batch selection and creation contract

### §6.1 Lifecycle transaction boundaries

| # | Boundary [proposed] | Commit content |
|---|---|---|
| LB-P | **Rotation/seal-plan commit** | One durable, idempotent plan **before any dependent action**: plan identity; target active batch; cause class (`rotation` / `shutdown_seal`); expected current selection epoch and active batch; whether a successor is intended; operation identity and provenance; the later configuration/calibration **trigger reference** (no numerical value invented). No successor creation, cutoff, seal-start, cancellation, or lineage update proceeds without it; a stale plan (expected epoch changed) is superseded and authorizes no **new** effects (§11 row 34) |
| LB1 | **Creation-plan commit** | New `batch_id`, reason (`no_active` / `rotation`), expected predecessor epoch, creator operation ref. **`rotation` successors are created only under the existing committed LB-P rotation plan** (plan ref carried); **genesis and post-shutdown/reactivation successors use `no_active`** — governed solely by this idempotent LB1 creation plan, feeding LB4 mode A (§6.3, §9.2A). *(Superseded vocabulary: `shutdown_seal_successor` — retired so it can never authorize a rotation-plan path or a second cutoff.)* |
| LB2 | **Manifest commit** | The §4.2 manifest; state `preparing` |
| LB3 | **Activation commit** | Mechanical validation results (manifest integrity; `schema_compat_ref` matches the currently adopted root schema version; `batch_id` uniqueness) + `activated` state event |
| LB4 | **Selection commit — one authority, two mechanically distinct modes** | **Mode A — initial/reactivation selection** (no writable predecessor exists: no selection record yet, or the current selection points at a batch already proven non-admitting through an existing cutoff, `sealing`, `sealed`, `invalid`, or a governed recovery state): commits **only** the new active selection via the §4.3 compare-and-commit against expected `none/genesis` (first selection) or the exact existing selection epoch (reactivation); **creates or rewrites no predecessor cutoff**; never modifies the historical batch; verifies the predecessor cannot admit new reservations. **Mode B — rotation cutover** (used only while a currently selected `active` predecessor still admits writes): **one durable boundary** that atomically commits the successor selection at epoch N+1 **and** the predecessor's admission-cutoff marker [proposed], both linked to the committed LB-P rotation plan; from this commit no new reservation may target the predecessor, while durably pre-cutoff reservations retain their §5.3 completion right. In both modes, concurrent selectors produce exactly one winner |
| LB5 | **Seal-start commit** | Under the committed LB-P plan: the `sealing` state event. **Rotation path:** admission was already cut at LB4; LB5 records the transition. **Shutdown-seal path (§9.2A):** LB5 **atomically** commits the batch's `admission_cutoff_id` marker + admission stop + `active`→`sealing` + the plan reference — one boundary, so shutdown reservations are classifiable against a durable cutoff |
| LB6 | **Seal commit** | Final counts + integrity summary + `sealed` event + final manifest version + successor lineage refs |
| LB7 | **Index-registration commit** | §10 registration of a batch with an index, with coverage status |

### §6.2 Selection of an already-valid active batch

Resolve the registry → current selection exists, chain unbroken, selected
batch's derived state is `active`, manifest valid → return
`{batch_id, selection_epoch}` to the write path. Idempotent and read-only.

### §6.3 Detecting absence and creating a successor safely

When no valid writable active batch exists (the fresh post-5,521-seal
genesis state, or after a shutdown seal or cutoff without a successor):
LB1 → LB2 → LB3 → **LB4 mode A** (initial/reactivation selection), in order,
each idempotent under its key (§8.1), each durable before the next begins.
**This path is governed solely by its idempotent LB1 creation plan** (reason
`no_active`) — it is a no-valid-active/reactivation creation path, **not** a
sealing operation: it requires no LB-P rotation/seal plan (whose schema
targets an active writable batch), it creates **no** cutoff, and it never
adds a second cutoff to a sealed or already-cut-off predecessor, whose prior
cutoff remains unchanged. Interruption at any point recovers by lookup-first
(§11 rows 1–3, 47–53): a committed step is discovered and continued, an
uncommitted step authorizes nothing, and a losing concurrent creator adopts
the committed winner — the losing activated-but-never-selected candidate is
then closed **only** through the bounded legal never-selected abandonment
transition (§5.2), its invalidation event recording the superseding
selection; its `batch_id` is never reused; nothing already recorded is
silently erased.

### §6.4 Refusal and prevention rules

- **Ambiguity → refuse:** any §4.4 condition stops ordinary selection; no
  guess, no default, no fallback (§12).
- **Two simultaneous writable selections are prevented four ways:** the
  single-current registry invariant + epoch compare-and-commit (§4.3);
  **exclusive claim ownership generations** (§8.0 — at most one currently
  effective ownership generation per ingestion identity across all batches
  and epochs, each created atomically with exactly one matching
  reservation); reservation binding of
  `{batch_id, selection_epoch, claim ref, ownership generation}` (§7); and
  the append-boundary check — ordinary admission refuses stale epochs and
  any non-selected target, while a pre-cutoff completion passes only the
  full §7.6 validation. **Multiple LB3-activated but never-selected
  candidate batches may temporarily coexist in derived state `active`** —
  they are never writable (§5.3 requires the current selection), they close
  only through the legal §5.2 never-selected abandonment, and valid
  unselected candidates are **never** treated as a same-epoch selection
  fork (a fork is two **committed selection records** at one epoch, §4.4).
- **No fallback to the sealed 5,521-root batch, ever:** the registry never
  selects a `sealed` batch (illegal by §5.2), and the append boundary
  independently refuses any `sealed` target — two independent locks.

---

## §7 — Root-write targeting, transaction boundaries, and outcome contract

### §7.1 Position of the seam

§7E — and **every** future root-producing caller, always via its §7E-side
eligibility path — resolves its write **through B11** before reaching the
shared `append_root()` commit boundary. B11 receives: the prepared root
payload (conforming to the seven-field schema per `schema_compat_ref`);
committed upstream evidence **references** (capture authorization, exclusion
result, blocker clearance, speaker resolution, §7E eligibility outcome); and
a stable caller-domain ingest-identity basis. B11 validates mechanically
(existence, shape, identity, target state) and **never** re-decides upstream
meaning or eligibility.

### §7.2 Operation identity and idempotency

- `ingest_operation_id` [proposed]: the **parent** end-to-end operation —
  one caller invocation of the B11 ingestion seam; attempt-specific, never
  the duplicate-prevention identity.
- **Child operation identities** [proposed `child_op_id`]: every separately
  executed internal B11 real operation carries **one stable unique child
  operation ID referencing its parent `ingest_operation_id`** — claim
  establishment/lookup (WB0); the WB1 generation + root-ID + batch
  reservation boundary; the WB2 fence + append + finalization boundary; a
  cancellation; a recovery resolution; a target resolution or any other
  separately executed B11 action. Each child receives **exactly one** §0B
  operational log under its own child ID; the parent ID is never reused as
  though it were the same real operation; no operation ID ever carries two
  operational logs (§14).
- **Canonical ingestion identity:** the authoritative **§7E `capture_id`** is
  the canonical basis for one root-ingestion identity — the same identity
  the existing pattern already reuses on retry so the append boundary
  absorbs the duplicate.
- `ingest_idempotency_key` [proposed]: **deterministically bound to the
  authoritative `capture_id` and the one root-ingestion operation type** —
  nothing else. **`schema_version` is not a key component**: a schema change
  must never silently permit a second root for the same capture.
  Root-schema evolution remains **B21**; any future deliberately authorized
  migration or derived-root operation must receive **its own explicitly
  designed identity** from that later package (§16). The key is **global
  and epoch-independent** (§8.0): a retry after rotation finds the one
  claim and the already-committed root wherever it lives, never a second
  commit.

### §7.3 Write-path transaction boundaries

| # | Boundary [proposed] | Commit content | Failure meaning |
|---|---|---|---|
| WB0 | **Claim establishment or lookup** (§8.0) | If no claim exists: atomically **establish** the one permanent claim in `available_uncommitted`, binding the immutable `claim_key` and the canonical `payload_integrity_ref`. **WB0 grants no append right and creates no owner** — a crash after WB0 leaves a harmless, reusable `available_uncommitted` claim. Found `committed` with matching payload identity → `duplicate_absorbed` (existing `root_id` + owning batch), no reservation. Found uncommitted with matching integrity → continue to WB1. Found `owned_uncommitted` under another attempt's generation → this attempt appends nothing (`interrupted`, claim ref). Integrity conflict → `rejected` + attached mismatch incident (§8.4). | Claim cannot be verified (ledger/coverage cannot show free-or-committed) → **new root admission fails closed** (§12) |
| WB1 | **Atomic ownership-generation + reservation + root-ID commit** (§8.0, §8.2A) | **One compare-and-commit boundary** that simultaneously: transitions the claim `available_uncommitted` → `owned_uncommitted`; creates one new unique `ownership_generation_id` in phase `granted`; commits the matching batch reservation; **binds — at the claim's first successful WB1 — one immutable `reserved_root_id` to the permanent claim and atomically reserves that same identity in the canonical root-ownership authority** (`reserved_for_claim`; every later generation and retry under this claim must reuse the same `reserved_root_id`; the same claim presenting a **different** `root_id`, or a **different** claim presenting this `root_id`, is rejected here — before any append); and binds the reservation to `{batch_id, selection_epoch, payload_integrity_ref, upstream evidence refs, ownership generation, reserved_root_id}` — durable **before** append; enters the batch's in-flight ledger (§9). **It is impossible to have a durable live owner without its matching durable reservation, or a durable reservation without its matching live generation.** Concurrent WB1 attempts permit exactly one winner; losers observe the winner and append nothing. | No committed WB1 → no ownership, no append; ordinary admission refused for a stale epoch or non-`active` batch; refused while the claim is `owned_uncommitted` under another generation; refused on a root-ID conflict (§8.2A) |
| WB2 | **Commit-fenced root-append + claim + root-ownership commit** | Entry is **one compare-and-commit of the currently effective generation `granted` → `commit_fenced`** — the per-generation append commit fence (§8.0). The physical shared `append_root()` boundary (schema-validated, atomic, duplicate-absorbing) then **verifies the durable `commit_fenced` generation immediately before committing** and requires that the §8.2A root-ownership entry for the reserved `root_id` **belongs to this same claim**; on success it transitions that entry to `committed_to_batch{batch_id}` and binds the claim's terminal `committed{root_id, batch_id}` transition, recovery-completable from the append evidence. **A generation that is not durably `commit_fenced` — stale, cancelled, superseded, pre-fence — can never append.** **This is the commit point.** | Fence not won (cancellation won `granted` → `cancelled`) → no append ever for that generation; append attempted without a durable fence or with a mismatched root-ownership entry → refused and logged; not reached → nothing durable; caller outcome per §7.5 |
| WB3 | **Parent terminal operation-log commit** | The mandatory §0B **single terminal operational record of the parent** `ingest_operation_id` — `append_committed` / `append_duplicate_absorbed` / `append_rejected` / `append_interrupted` / `append_indeterminate` — durably appended **after the required child operations and canonical state records resolve**; **exactly one terminal record per parent operation** (§14); child-operation logs are not second parent logs, and writing WB3 creates no log-about-logging operation | Root committed but the parent terminal log absent → **no success acknowledgement yet**; recovery finds the existing logs by operation identity and appends only the missing parent terminal idempotently (§11 row 8); logging failure never deletes or uncommits the root |
| WB4 | **Acknowledgement commit** | The terminal outcome (§7.5) returned to the caller — only after the matching WB3 terminal record is durable (§7.4) | No committed acknowledgement → caller resolves by lookup, never by blind re-send |
| PR | **Post-commit rebuildable registrations** (non-gating) | Global identity-index entry (`root_id` → owning `batch_id`); batch counters/checkpoint; coverage records — **recoverable post-commit work, separated from the mandatory terminal log**; never the first duplicate defense (§8.3) and never a gate on WB4 | Gaps are honest (`partial` coverage) and reconciled idempotently (§11 row 9); the root's durability and the claim's committed state are unaffected |

### §7.4 Acknowledgement rule

A terminal outcome is returned to the caller **only after the parent's
matching WB3 terminal operation record is durable** — for success outcomes
that means WB2 durably exists **and** the parent's `append_committed` /
`append_duplicate_absorbed` record is durably appended. Root durability is established at WB2 and is
never undone by a later logging or indexing failure; but **no function
reports success before the permanent operation record exists**. PR
registrations never gate acknowledgement; where they are incomplete, the
acknowledgement carries the honest coverage status.

### §7.5 Caller outcome vocabulary [proposed]

| Outcome | Meaning |
|---|---|
| `committed` | WB2 durable in the identified batch; root identity + owning `batch_id` returned |
| `duplicate_absorbed` | The global claim for this `ingest_idempotency_key` is `committed` (found at WB0 or at the WB2 boundary): a root already durably exists in **some** batch; the existing root identity + owning batch returned; no reservation, no second commit |
| `rejected(reason)` | Mechanical refusal: schema nonconformance; missing/invalid upstream evidence refs; sealed/stale/invalid target; identity collision (§8.4). Never a semantic judgment. |
| `interrupted` | The attempt ended **before** WB2 with durable evidence of non-commit — including finding the claim `owned_uncommitted` under another attempt's ownership generation (claim ref returned) or having its own generation cancelled at a cutover; safe to retry under the **same key**, where WB0 lookup-first resolves it against the claim's current status (technical re-attempt; substantive retry policy remains B9's) |
| `indeterminate` | Whether WB2 occurred cannot be safely established; **fail closed** — no blind retry; resolution only by lookup under the global key (§11 row 7) |

### §7.6 Sealing while a write is in flight — pre-cutoff completion

The applicable **admission cutoff** (`admission_cutoff_id` — committed at
the LB4 cutover for rotation, or atomically inside LB5 for shutdown-seal,
§9.2/§9.2A) ends new-reservation admission for the batch. A WB1 reservation
**durably granted before that cutoff** retains the §5.3 bounded completion
right; the admission ledger's total order over reservation grants and the
cutoff marker makes the pre/post relation **provable** for every
reservation. Each such completion at WB2 must validate **all of**: (1) the
original durable reservation; (2) that the reservation's **ownership
generation is the claim's currently effective generation and wins the WB2
commit fence** (`granted` → `commit_fenced`, §8.0); (3) the
payload-integrity reference; (4) the old batch's identity as the reservation
recorded it; (5) the cutoff relationship — the grant is provably
pre-cutoff. **No unreserved or post-cutoff attempt may use this exception**;
a stale unreserved writer remains refused. A pre-cutoff reservation that is
**cancelled loses the completion right at the atomic cancellation boundary
(§8.0) — which returns the claim to `available_uncommitted` — before any
successor WB1 may grant a new generation**; the caller receives
`interrupted` and retries under the same key — exclusive, non-overlapping
generations make exactly one eventual commit possible. LB6 cannot commit
while any pre-cutoff reservation is unresolved (§9.3).

### §7.7 What B11 never decides here

Whether the material qualified to become a root; what it means; whether it is
relevant; whether it should later be read, held, promoted, or retried on
substantive grounds. Upstream evidence is consumed as committed references
only.

---

## §8 — Cross-batch identity and duplicate-prevention contract

### §8.0 The global ingestion claim — one permanent claim, statuses, and ownership generations

`global_ingestion_claim` [proposed] — **one canonical permanent claim per
`ingest_idempotency_key`**, keyed **independently of batch and selection
epoch**, serializing every ingestion identity **before** any batch-specific
append can occur. The claim binds, **from first establishment**:

| Field [all proposed] | Content |
|---|---|
| `claim_key` | Deterministic from the authoritative §7E `capture_id` + the single root-ingestion operation type (§7.2) — immutable |
| `payload_integrity_ref` | The **canonical, immutable** payload-integrity reference bound at establishment — computed over the **complete prepared seven-field root payload (all seven authoritative fields)**; every later attempt under this key is checked against it (§8.4). `root_id` is additionally bound **independently and unambiguously** as `reserved_root_id`, never derived solely from this reference |
| `reserved_root_id` [proposed] | The **one immutable canonical `root_id` of this claim**, bound at the claim's first successful WB1 and atomically reserved in the §8.2A authority; **every later generation and retry under this claim must reuse it** — the claim can never present a second identity |
| `claim_status_events` | Append-only status events (never edited) |
| `ownership_generation_events` | Append-only generation events — each generation has a unique `ownership_generation_id` [proposed] and moves only through the **three legal append-only paths**: `granted → cancelled` (normal cancellation); `granted → commit_fenced → committed` (successful append); `granted → commit_fenced → recovery_released_no_commit` [proposed] (strict recovery-only resolution, §8.0 release rule — a distinct terminal phase, never ordinary `cancelled`); no phase event is ever edited |
| `current_ownership_generation` | The **at most one** currently effective generation, if any — derived from the generation events |
| `committed_root_id` / `owning_batch_id` | Bound once, at the terminal `committed` transition |

**Authoritative claim statuses (derived from the append-only events):**

| Status | Meaning |
|---|---|
| `available_uncommitted` | The claim exists; **no current owner; no committed root**. Freshly established by WB0, or returned to by an atomic generation cancellation. Harmless and reusable. |
| `owned_uncommitted` | **Exactly one** durable ownership generation and **exactly one** matching durable WB1 reservation exist — created together in one boundary |
| `committed` | **Terminal successful state**: one `root_id` in one owning `batch_id`. Never replaced, hidden, weakened, or reopened — by anything, including later mismatch incidents |
| `indeterminate_recovery_required` | No new ownership and no append permitted; resolution only through §11 |

An **integrity-conflict condition blocks safely as an attached incident**
(§8.4) — it is **not** a lifecycle status and can never displace a valid
`committed` state.

**Binding rules:**
- **WB0 establishes; it never owns.** Establishment is atomic (concurrent
  establishers converge on the one claim; losers adopt it); WB0 grants no
  append right and creates no owner — **a crash after WB0 leaves a harmless
  reusable `available_uncommitted` claim** (§11 row 16).
- **WB1 is one atomic boundary** creating the generation and its matching
  reservation together (§7.3-WB1): a durable owner without its reservation,
  or a reservation without its live generation, is structurally impossible;
  concurrent WB1s yield exactly one winner.
- **Generations never overlap.** At most one currently effective generation
  exists per claim, across all batches and epochs; a new generation can be
  granted **only** while the claim is `available_uncommitted`.
- **Cancellation is per-generation, atomic, and never terminal for the
  claim.** Cancellation may begin **only** through one compare-and-commit
  transition of the currently effective generation from `granted` to
  `cancelled` — the same authoritative phase state the WB2 fence competes
  on. **Normal cancellation is legal only from `granted`; a `commit_fenced`
  generation never transitions to ordinary `cancelled`** (its only exits are
  `committed` or the strict recovery release below). The committed
  cancellation proves no root committed under that generation, extinguishes
  its completion right, and transitions the claim `owned_uncommitted` →
  `available_uncommitted`. Only after that boundary
  may a later WB1 grant a new generation — in the same batch or a successor.
  **Once a generation is `cancelled`, WB2 fencing and root append are
  forbidden for it, permanently.**
- **"Transfer" is exactly:** (1) atomic cancellation of the old generation
  and reservation; (2) claim `available_uncommitted`; (3) a later atomic WB1
  creates the new generation and successor reservation. **Never a second
  claim; never an edited event.**
- **The append commit fence (WB2 ↔ `committed`) — one atomic
  per-generation fence before the physical append.** WB2 may begin **only**
  through one compare-and-commit transition of the currently effective
  generation from `granted` to `commit_fenced`. **Fencing and cancellation
  compete on the same authoritative generation phase; exactly one can
  win.** Once `commit_fenced` exists: cancellation of that generation is
  forbidden; the claim cannot return to `available_uncommitted`; no
  replacement generation may be granted; only append completion or §11
  recovery resolution may proceed. Once `cancelled` exists: fencing and
  root append are forbidden; the claim may return to
  `available_uncommitted`; a later WB1 may create a new generation. The
  physical append boundary **verifies the durable `commit_fenced`
  generation immediately before committing**, and the append transaction
  **records the claim, generation, fence, and ownership associations in
  external B11 transaction/ownership evidence — the immutable root itself
  remains exactly the seven authoritative fields (§8.2C)** — so a delayed
  executor holding a stale pre-fence view cannot append; its entry attempt
  fails the fence compare-and-commit (the generation is no longer
  `granted`). The claim's terminal `committed{root_id, batch_id}`
  transition is bound to the fenced append and is **recovery-completable
  from the append evidence alone**. A stale, cancelled, superseded,
  pre-fence, released, or non-current generation **can never append** —
  mechanically, not by assertion — so no second batch can ever commit the
  same claim.
- **The strict recovery release (`commit_fenced` →
  `recovery_released_no_commit`) — the only exit from a fence besides
  `committed`.** This recovery-only terminal transition may commit **only
  when all four row-37 conditions hold**: exclusive recovery authority is
  active; no live writer can still complete the old operation; the exact
  target batch and reserved `root_id` were checked; and root non-commit is
  **conclusively proven**. On commit: the released generation is
  **permanently unable to append**; its reservation and bounded completion
  right are extinguished; the claim may transition back to
  `available_uncommitted`; **its canonical `reserved_root_id` remains bound
  to the same claim for retry**; and a later WB1 may create a new
  generation for that same claim and root identity. If any required proof
  is missing, the claim remains `indeterminate_recovery_required`.
  Duplicate recovery of a committed release is a no-op; no recovery may
  rewrite, reconstruct, or blindly repeat a root append.
- **The claim is the first duplicate defense.** The post-commit PR index
  remains rebuildable material and is never the mechanism preventing
  duplicate commits.
- **Fail closed:** if the claim, its events, or their coverage cannot prove
  an identity's status, **new root admission stops** (§12).
- **Recovery inspects the claim first:** before retrying, transferring,
  cancelling, or acknowledging any ingestion, recovery reads the claim's
  committed status and generation events (§11 protocol).

### §8.1 Idempotency and duplicate-prevention points (eighteen)

| Protected point | Key binds to |
|---|---|
| Creation plan (LB1) | plan intent + expected predecessor epoch |
| Manifest commit (LB2) | `batch_id` |
| Activation (LB3) | `batch_id` + validation-set version |
| Selection (LB4) | `selection_epoch` + `batch_id` (compare-and-commit) |
| Claim establishment (WB0) | **global** `ingest_idempotency_key` — one permanent claim ever, batch- and epoch-independent; establishment converges, never duplicates |
| Ownership generation + reservation + root-ID reservation (WB1) | claim identity + one atomic compare-and-commit from `available_uncommitted` — creates the unique `ownership_generation_id` (phase `granted`), its matching reservation, and the §8.2A `root_id` reservation for the same claim, together; at most one effective generation per claim |
| Append commit fence (WB2 entry) | `ownership_generation_id` + one compare-and-commit `granted` → `commit_fenced`; competes with cancellation on the same phase; exactly one winner ever |
| Recovery release (§8.0) | `ownership_generation_id` — at most one committed `recovery_released_no_commit` ever per generation; duplicate recovery over it is a no-op |
| Child-operation log (§7.2, §14) | `child_op_id` — exactly one operational log per child operation; retries and recovery locate the existing log by identity, never appending another |
| Root-ownership entry (§8.2A) | `root_id` — one permanent ownership entry ever; reserve/verify idempotent under the owning claim key; commit idempotent under the fenced append |
| Rotation/seal plan (LB-P) | plan identity + expected epoch/batch — duplicate execution is a no-op; a stale plan is superseded with no effects |
| Root append + claim commit (WB2) | claim ownership (linearization rule §8.0); absorbing under the **global** key |
| Parent terminal operation log (WB3) | `ingest_operation_id` — exactly one terminal record per **parent** operation; child logs are never second parent logs |
| Index registration (LB7/PR) | `batch_id` + index identity (+ `root_id` per entry) — rebuildable, non-gating |
| Seal-start (LB5) | rotation/seal plan identity |
| Seal commit (LB6) | `batch_id` |
| Recovery run | `recovery_run_id` [proposed] + finding-set identity |
| Acknowledgement (WB4) | `ingest_operation_id` |

### §8.2 Root identity scope

`root_id` is unique **system-wide across all batches** — the existing 5,521
roots keep their identities; every future identity is generated never to
collide with any existing root in any batch (uniqueness contract binding;
generation scheme open to implementation). **Uniqueness is enforced before
append by the canonical root-ownership authority (§8.2A)** — one permanent
ownership entry per `root_id`; **exactly one batch owns each root**. The
rebuildable retrieval index (§10, PR) serves lookup and is never the
uniqueness authority.

### §8.2A Canonical root-ownership authority (pre-commit)

`root_ownership_registry` [proposed] — one canonical, durable, **pre-commit**
root-identity authority, separate from the rebuildable retrieval index:

| Field [all proposed] | Content |
|---|---|
| `root_id` | The permanent root identity — **one ownership entry per `root_id`, ever** |
| `owning_claim_key` | The §8.0 claim that owns this identity |
| `payload_integrity_ref` | The canonical payload-integrity reference (matching the claim's) |
| `status` | `reserved_for_claim` / `committed_to_batch` |
| `owning_batch_id` | Bound when WB2 succeeds |
| provenance / conflict records | Append-only; every reservation, commit, and rejected conflicting presentation |

**Binding behavior:**
- A `root_id` is **bound to its claim before any root append**: WB1
  atomically verifies-or-reserves it for the same claim inside the
  ownership-generation/reservation boundary (§7.3-WB1).
- **The binding is one-to-one, enforced in both directions:** one `root_id`
  → one permanent owning claim, **and** one permanent ingestion claim → one
  canonical `reserved_root_id` (§8.0), bound immutably at the claim's first
  successful WB1. **A different claim presenting the same `root_id`, or the
  same claim presenting a different `root_id`, is rejected before WB2** —
  recorded in the entry's append-only conflict records as an
  integrity/identity conflict. Where the authoritative evidence itself is
  contradictory rather than a bad retry, the claim fails closed as
  `indeterminate_recovery_required` — no identity is guessed.
- **Cancellation of a generation does not release the `root_id`**: the
  permanent claim retains its reserved identity for safe retries; the
  identity is never reassigned to another claim.
- WB2 may commit **only** when both hold: the generation holds the commit
  fence (§8.0), **and** the root-ownership entry belongs to that same
  claim. On success WB2 transitions the entry to
  `committed_to_batch{owning_batch_id}` with the same root and batch.
- Registry failure, incomplete coverage, or conflict → **admission fails
  closed** (§12).
- The PR/global retrieval index remains rebuildable and non-authoritative;
  it is **never** the pre-commit uniqueness authority.

### §8.2B Historical root-ID bootstrap-registration contract

The existing 5,521 `root_id` values enter the canonical authority through an
**external bootstrap registration**: the authority records the
already-existing `root_id → historical batch_id` ownership **externally** —
no historical root, field, file, store, seal marker, or index entry is
modified; no root is copied or migrated. **Actual scanning and population
remain later authorized implementation/disk-verification work** (§16).
**No future root writing is permitted until historical root-identity
coverage is verified complete, or any gap is honestly fail-closed** (§12).
This coverage validation is the fourth requirement of the historical
batch's `bootstrap_completion_status` (§4.5): only when the registration,
state event, manifest, **and** this coverage all validate does the status
become `complete`.
Historical root-ID ownership and B11 ingestion-claim identity remain
**distinct**: no B11 `capture_id` claim is invented for a historical root
when no authoritative capture mapping exists.

### §8.2C Seven-field schema protection

The root record itself remains **exactly the seven sealed fields**. Every
durable association among claim key, ownership generation, commit fence,
`root_id`, owning batch, and payload-integrity reference lives in B11
transaction/ownership records **outside** the root record. No claim,
generation, or fence field is ever embedded into the seven-field root.

### §8.3 Duplicate detection — before and after sealing

- **At write time — the claim decides, pre-commit:** WB0 consults the
  **global claim ledger** (batch- and epoch-independent). Claim `committed`
  anywhere → `duplicate_absorbed`, pointing at the owning batch, with no
  reservation. Claim `owned_uncommitted` → no second ownership generation. Repeated ingestion
  under the same stable identity therefore commits **at most once, ever,
  anywhere — enforced before any immutable append**, not repaired after it.
- **After sealing:** claims of sealed roots remain `committed`; a later
  ingestion attempt of already-sealed material absorbs against the sealed
  owner at WB0 — it never writes a copy into the active batch. The PR
  identity index additionally serves lookup and provenance (§10) as
  rebuildable, non-authoritative material — never the pre-commit uniqueness
  authority (§8.2A is).

### §8.4 Collision and mismatch

The claim's canonical `payload_integrity_ref` is **immutable** from
establishment. A later attempt using the same claim key with a **different**
payload-integrity reference is `rejected` and logged as an **attached
integrity incident** (`mismatch_incident` [proposed]) — an incident record
linked to the claim, **never a lifecycle status**: it must not replace,
hide, weaken, or reopen a terminal `committed` claim. When the claim is
already `committed`, later **valid matching** retries still find that
committed state and return `duplicate_absorbed`. When the claim is
**uncommitted** and the authoritative §7E capture evidence itself is
contradictory or unverifiable, the claim transitions to
`indeterminate_recovery_required` and admission fails closed — **no
guessing which payload is correct**. Same `root_id` presented with different
content-integrity — or by a different claim — is `rejected` **before
append** through the §8.2A root-ownership authority (`identity_collision`
[proposed]), with both integrity references recorded in its append-only
conflict records and the condition surfaced for governed review. Never a silent overwrite; never a silent second identity;
never a second claim.

### §8.5 Visibility is not weight

A root visible through multiple batch indexes, manifests, recovery
checkpoints, or logs is **one root with one evidential presence**. Batch
manifests, logs, indexes, and recovery records are machine-provenance
records; they are **never additional evidential votes** about the root or its
content (§0B no-double-evidence; the same rule B24 v7 enforces for operation
records). B11 introduces no mechanism by which multiplicity of references
increases weight.

### §8.6 Semantic deduplication — not B11

B11 prevents **mechanically identical or identity-equivalent** duplicate
commits only. Whether two differently-captured contents are semantically the
same is a meaning judgment: not decided here, not decidable by DUMB
machinery, and open where not already governed elsewhere.

---

## §9 — Sealing and rotation contract

### §9.1 Triggers

Rotation/sealing begins only from a committed **rotation/seal plan — the
LB-P boundary, before any dependent action**. The committed plan carries:
plan identity; the target active batch; the cause class (`rotation` —
successor intended — or `shutdown_seal` — seal without successor; writes
then fail closed until a successor exists); the expected current selection
epoch and active batch; whether a successor is intended; operation identity
and provenance; and the **trigger reference** to later declared
configuration/calibration — the **numerical capacity, time, and performance
thresholds are declared later values**, not invented here (§16). No
successor creation, cutoff, seal-start, cancellation, or lineage update may
proceed without the committed plan. A stale plan whose expected epoch has
changed is superseded and **authorizes no new effects** — already-created
external candidate records remain preserved; an activated but never-selected
candidate closes only through the legal bounded §5.2 abandonment
transition; nothing is erased (§11 row 34).

### §9.2 Preferred successor-first sequence (keeps a write target available)

1. **LB-P committed rotation plan** — before anything else.
2. **LB1–LB3 for the successor** under that committed plan (prepared,
   validated, activated — not yet selected).
3. **LB4 cutover commit** — one durable boundary committing the successor
   selection (epoch N+1) **and** the old batch's admission-cutoff marker.
   From this single commit: all **new** reservations resolve to the
   successor; no new reservation may target the old batch; reservations
   durably granted **before** the cutoff retain their bounded completion
   right (§5.3, §7.6). There is no window in which both batches admit. The
   LB4 cutover carries the plan's stable `admission_cutoff_id` [proposed].
4. **LB5 seal-start** on the old batch (`sealing`).
5. **Drain** (§9.3): every reservation classified against the LB4 cutoff
   resolves.
6. **Verification** (§9.4).
7. **LB6 seal commit** on the old batch.

### §9.2A Shutdown-seal path (no successor at cutover time)

1. **LB-P committed shutdown-seal plan.**
2. **LB5 — one atomic boundary** committing together: the batch's
   `admission_cutoff_id` marker; the admission stop; the transition
   `active` → `sealing`; and the reference to the committed shutdown-seal
   plan. Because the cutoff is inside LB5, every reservation is classifiable
   against a durable cutoff: reservations durably granted **before** this
   LB5 cutoff retain their bounded completion right; **no reservation may be
   granted after it**.
3. **Drain** (§9.3) against the LB5 cutoff → **Verification** (§9.4) →
   **LB6 seal commit.**
4. Ordinary writes fail closed from the LB5 cutoff until a successor
   commits LB1–LB3 and the **LB4 mode-A** initial/reactivation selection —
   a no-valid-active creation path governed solely by its idempotent LB1
   creation plan (§6.3), **not** another rotation/seal plan and **not** a
   second cutoff of this batch (its LB5 cutoff remains unchanged) — and
   never falling back to any sealed batch.

**One `admission_cutoff_id` contract:** rotation reservations are classified
against the LB4 cutoff; shutdown-seal reservations against the LB5 cutoff;
the admission ledger's total order over grants and the cutoff marker lets
every reservation **prove** whether it was committed before or after the
applicable cutoff; no write gap can fall back to a sealed batch; no
unreserved or post-cutoff attempt can use the completion exception (§7.6).

A seal-without-successor path runs LB5 → drain → verification → LB6 directly;
ordinary writes fail closed from LB5 until a successor commits LB4.

### §9.3 Drain

Every WB1 reservation classified as **pre-cutoff** against the applicable
`admission_cutoff_id` (LB4 for rotation, LB5 for shutdown-seal) is resolved
exactly one way: `committed` (its WB2 completed into the old batch under the
full §7.6 validation — reservation, currently effective ownership
generation, payload integrity, batch identity, cutoff relationship) or
**cancelled through the atomic per-generation cancellation boundary (§8.0)
— legal only while the generation remains `granted`** — which proves no
root committed under that generation, extinguishes the completion right,
and returns the claim to `available_uncommitted`; **only then** may a later
WB1 grant a successor generation; the caller receives `interrupted` and
retries under the same key. A reservation whose generation is already
`commit_fenced` resolves **only** by append completion or the strict §8.0
recovery release (row 37) — never by ordinary drain cancellation. **LB6 requires every
pre-cutoff reservation proven committed or cancelled; an indeterminate
reservation blocks the seal** and resolves only through §11 row 10 — never
by guessing.

### §9.4 Verification before seal

Durable-batch verification records: root count vs the reservation/append
ledger; content-integrity summary computed and referenced; identity-index
coverage for the batch complete **or honestly marked** (§10.4). Verification
failure → `recovery_required`, never a forced seal.

### §9.5 Irreversibility and gap rules

- **Sealed is irreversible through ordinary operation** — no B11 operation
  transitions `sealed` toward writability (§5.2), and the append boundary
  independently refuses sealed targets.
- A sealed batch **remains readable, never writable**.
- **A gap never redirects writes into a sealed batch:** with no current
  `active` selection, ordinary root writing **fails closed** (§12) — it never
  falls back to any sealed batch, including the 5,521-root batch.
- **A failed successor never re-opens the old batch:** if the successor
  fails after LB5, the old batch continues its path to `sealed` (or
  `recovery_required` → evidence-proven state); writes stay failed-closed
  until a **new** successor commits LB1–LB4.

---

## §10 — Cross-batch reading and index-registration contract

### §10.1 Discovery

The `batch_registry` enumerates every registered batch — active, sealing,
sealed (including the pre-B11 historical batch), recovery-required, invalid —
each with its manifest reference and derived state. Discovery validates
each manifest; an invalid manifest marks the batch (§5.2) and excludes it
from any completeness claim, with a §14 event. **The historical batch is
validated through its complete bootstrap record set** — registration,
bootstrap state event, bootstrap manifest, and the §8.2B coverage evidence
(§4.5); until all validate, its `bootstrap_completion_status` is
`incomplete` (or `recovery_required`): excluded from completeness claims,
never writable, its bytes untouched — while its canonical `batch_state`
remains accurately `sealed` once the legal bootstrap state event exists
(and no canonical state at all before it). **Discovery must not claim that
every batch has a manifest unless the historical bootstrap manifest
actually exists and validates.**

### §10.2 Identity lookup and provenance

Cross-batch root lookup by identity resolves through the rebuildable
**global identity index** (PR): `root_id` → owning `batch_id` (+ location
descriptor via the registry). The **canonical ownership answer** — which
claim and which batch own a `root_id` — is the pre-commit §8.2A authority;
the retrieval index serves reading and is never the uniqueness authority. Every retrieval result and audit record **carries the owning
batch's identity** — provenance is preserved end-to-end; batch boundaries
survive reading.

### §10.3 Index registration (LB7)

A batch participates in unified reading only after a committed
`index_registration` [proposed] per index: `{batch_id, index_identity,
registered_at, coverage_status, evidence refs}`. Registration is idempotent
(§8.1) and reconstructible after a crash by mechanical scan of the batch's
committed contents — reconciliation is idempotent and marks coverage honestly
while incomplete (§11 row 13).

### §10.4 Honest coverage status [proposed]

`coverage_status` per batch per index: `complete` / `partial` / `stale` /
`missing` / `conflicting`. B11 **detects and marks**; it never hides a gap,
never claims completeness it cannot evidence, and never silently omits a
batch. What a retrieval service does with degraded coverage (ranking,
failure, degraded-context presentation) is **B1/B26**, not B11 — B11 supplies
the structural truth only.

### §10.5 One memory system, separate immutable boxes

Unified reading is a **union across batch boundaries via indexes and the
registry** — roots are never flattened, merged, copied, or re-homed to
provide unified reading; sealed batches are never physically combined; batch
boundaries are preserved during retrieval and audit. All sealed batches are
separate immutable batches participating in one N.H memory system.

---

## §11 — Crash and partial-completion recovery matrix

**Protocol (every row):** lookup-first at the committed destinations under
the relevant identity; **for every ingestion, recovery inspects the global
claim (§8.0) before retrying, transferring, cancelling, or acknowledging
anything**; a committed record is discovered and continued — never
re-executed; an uncommitted plan authorizes nothing; resolution is
idempotent under `recovery_run_id` + per-action keys; recovery **never
rewrites a committed root** and **never regenerates or reconstructs missing
root content** — material not durably captured is an honest gap (the settled
rule: what was not captured before a crash is not reconstructed).

| # | Crash / partial state | Resolution |
|---|---|---|
| 1 | Before a batch manifest becomes valid (LB1 committed, LB2 absent/incomplete) | Plan discovered → complete LB2 idempotently, or close the plan `invalid` (cause: abandoned preparation) if its predecessor epoch moved on; nothing writable existed |
| 2 | Valid new manifest, no activation/selection (LB2 done, LB3/LB4 absent) | Validate → LB3 → LB4 via the normal path; or mark `invalid` if superseded; the batch was never writable meanwhile (§5.3) |
| 3 | Activation done, selection absent (LB3 done, LB4 absent) | Retry the applicable LB4 mode under the plan's key; if another selection won the epoch, adopt it and close this never-selected batch **only through the bounded legal §5.2 abandonment transition**, its invalidation event recording the superseding selection (never two writable selections; nothing silently erased) |
| 4 | Same-epoch selection fork — two **committed selection records** at one epoch | **Ordinary writes block immediately.** Recovery may retain one record **only** when committed integrity/provenance evidence proves the other was never validly committed, is malformed, or fails its required integrity/authorization contract. **If both records remain equally valid: no winner is chosen** — not by timestamp, batch identifier, file order, lexical order, or any invented tie-breaker; both affected batches remain non-writable or `recovery_required`; existing roots remain preserved; **no reservation is cancelled or redirected on a guess**; the conflict stays fail-closed for a later separately authorized repair mechanism (§16, not designed here). Valid LB3-activated but never-selected candidates are **not** a fork and are never treated as one (§6.4) |
| 5 | No active batch | Ordinary writes fail closed; creation path §6.3 runs; sealed batches are never a fallback |
| 6 | Batch manifest/state mismatch (state chain contradicts manifest or registry) | `recovery_required`; resolve only to the state the committed evidence proves; unresolvable → `invalid` + fail-closed marking; bytes untouched |
| 7 | Write reserved, root not committed (WB1 durable, WB2 absent) — **applies only while the generation remains `granted`** | **Claim first:** the claim's events prove non-commit (`owned_uncommitted`, generation `granted`, no terminal event, append lookup empty) → the generation is cancelled through the atomic §8.0 boundary (claim → `available_uncommitted`), the reservation resolves `interrupted`, and the same key may retry via WB0→WB1. **A `commit_fenced` generation never takes this path** — it resolves per rows 37–38. If the claim status or append destination cannot be safely read → claim `indeterminate_recovery_required`, outcome `indeterminate`, fail closed; resolve only by later successful lookup |
| 8 | Root committed, terminal log and/or acknowledgement absent (WB2 durable; WB3/WB4 absent) | **Claim first**, then root lookup finds the durable root; the claim's `committed` transition is completed from the append evidence if missing; the **missing WB3 terminal record is appended idempotently** (exactly one per operation); **only then** is `committed`/`duplicate_absorbed` acknowledged. Never a second append; a logging gap never uncommits the root |
| 9 | Root committed, PR registrations absent/partial (WB2 durable; index/counters incomplete) | Complete the **PR** registrations idempotently (identity-index entry, counters, reservation resolution); coverage marked `partial` until done; PR never gates the WB3 terminal log or WB4 acknowledgement; the root's durability is unaffected |
| 10 | Sealing started with pre-cutoff reservations unresolved (LB4 cutover + LB5 done) | Resume the drain (§9.3): each pre-cutoff reservation resolved `committed` (WB2 + claim evidence exist; §7.6 validation replayed) or `cancelled` (proven absent; ownership durably cancelled **before** any claim transfer); undeterminable → claim `indeterminate_recovery_required`, reservation `unresolved`, **the seal cannot commit**; fail closed pending resolution |
| 11 | Seal committed, successor selection absent (LB6 done, no LB4 for a successor) | Writes fail closed (row 5 behavior); successor creation runs §6.3; the sealed batch never re-admits |
| 12 | Cutover committed, prior batch's sealing evidence incomplete (LB4 cutover done; old batch stuck pre-LB6) | New writes safely target the successor; the old batch completes drain → verification → LB6, or resolves `recovery_required` per evidence; it never re-admits new reservations (**admission stopped at the LB4 cutoff**), while surviving pre-cutoff reservations keep only their §7.6-validated completion right |
| 13 | Crash during index reconciliation | Re-run reconciliation idempotently (per-entry keys); coverage stays honestly `partial`/`stale` until complete; no duplicate entries |
| 14 | Duplicate recovery execution | `recovery_run_id` + per-action lookup-first make the second run a no-op that returns the committed findings |
| 15 | Corrupted / incomplete / unverifiable manifest or checkpoint evidence | The affected batch → `recovery_required`; claims are reduced to what verifiable evidence supports; unverifiable evidence never supports writability or completeness; if integrity cannot be established → `invalid` marking + fail closed; committed roots inside remain preserved and readable to the extent their own integrity verifies; nothing is rewritten or reconstructed |
| 16 | **Claim established (WB0), WB1 absent** | Nothing to undo: the claim is `available_uncommitted` with **no owner and no append right** — harmless and reusable; the same key's next attempt runs WB0 lookup → WB1 normally |
| 17 | **Concurrent WB1: one generation/reservation committed, another attempt did not** | The atomic WB1 admits exactly one winner; the loser's attempt has **no durable generation and no reservation** — it observes the winner (claim `owned_uncommitted`) and resolves `interrupted`, appending nothing |
| 18 | Ownership generation + reservation committed, WB2 absent | **If the generation phase is `granted`** (= row 7): cancellation (`granted` → `cancelled`) → claim `available_uncommitted` → retry; or proceed by winning the WB2 fence (`granted` → `commit_fenced`) where the batch still admits the completion right. **If the phase is already `commit_fenced`, cancellation is forbidden** — resolve per rows 37–38 |
| 19 | **Cancellation committed, no replacement owner yet** | The claim rests `available_uncommitted` — correct and harmless; a later WB0 lookup → WB1 grants the next generation when an attempt arrives |
| 20 | **Crash during cancellation** | The cancellation boundary is atomic: it either committed (generation cancelled; claim `available_uncommitted`) or it did not (the generation remains current and effective) — lookup-first over the claim's events decides; a partially cancelled generation cannot exist; unreadable evidence → `indeterminate_recovery_required`, fail closed |
| 21 | **Crash after cancellation, before successor WB1** | = row 19: reusable `available_uncommitted` claim; nothing dangling; the retry path re-runs WB0 → WB1 |
| 22 | **Stale cancelled generation attempts WB2 fencing or append after a newer generation exists** | The fence compare-and-commit refuses it — its durable phase is `cancelled`, not `granted`; the physical append boundary would independently refuse it for lacking a durable `commit_fenced` phase verified immediately before commit; nothing commits; the refusal is logged (§14); the newer generation is unaffected |
| 23 | Root committed, claim's terminal transition incomplete | The terminal `committed{root_id, batch_id}` transition is completed **from the append evidence alone**, idempotently (§8.0 linearization rule); then WB3/WB4 proceed per row 8 |
| 24 | **Committed claim receives a later payload mismatch** | The later attempt is `rejected`; a `mismatch_incident` is **attached** to the claim; the terminal `committed` state is never replaced, hidden, weakened, or reopened; later **valid matching** retries still return `duplicate_absorbed` |
| 25 | Duplicate recovery over any claim state (rows 16–24) | `recovery_run_id` + per-action lookup-first over the claim's append-only events make every repeat a no-op returning the committed findings — no duplicated ownership, no re-cancellation, no second terminal transition |
| 26 | **LB-P plan committed, successor creation not begun** | Lookup finds the plan → resume LB1 under it, or supersede the plan if its expected epoch has changed (row 34); no effects existed yet |
| 27 | Plan committed, successor partially prepared (LB1/LB2/LB3 incomplete) | Lookup-first per boundary (rows 1–2 mechanics) under the plan's identity: complete the next boundary idempotently, or supersede the plan (no **new** effects) and close the never-selected successor **only through the legal §5.2 abandonment transition** with the stale-plan evidence recorded; already-created external records remain preserved |
| 28 | Successor ready, LB4 absent | Retry the applicable LB4 mode under the plan (idempotent compare-and-commit); if another selection won the epoch, adopt it, supersede this plan (no **new** effects), and close the losing never-selected candidate only through the legal §5.2 abandonment transition; the old batch kept admitting until a mode-B cutover actually committed — no cutoff, no orphaned completion rights |
| 29 | LB4 cutover committed, LB5 absent | The old batch is durably cut off (no new reservations) but not yet `sealing`: commit LB5 idempotently under the plan; pre-cutoff reservations keep their completion rights throughout |
| 30 | **Shutdown plan committed, LB5 cutoff absent** | Nothing depended yet: retry the atomic LB5 (cutoff + admission stop + `sealing` + plan ref) idempotently; the batch remains ordinarily writable until LB5 actually commits |
| 31 | **Shutdown LB5 partially or indeterminately committed** | LB5 is **one atomic boundary**: either the cutoff/stop/`sealing`/plan-ref committed together or none did — lookup decides; if the evidence cannot be safely read, the batch → `recovery_required` and **admission fails closed** pending resolution; no reservation is classified against an unproven cutoff |
| 32 | Shutdown cutoff committed with reservations in flight | Drain per §9.3 against the LB5 `admission_cutoff_id`: each pre-cutoff reservation proven committed or cancelled through the atomic boundary; indeterminate blocks LB6 (row 10 mechanics) |
| 33 | Duplicate plan execution | The plan identity makes the repeat a no-op returning the committed plan and its progress |
| 34 | **Stale plan — expected epoch/batch has changed** | The plan is superseded and **authorizes no new effects**: no further successor creation, cutoff, seal-start, cancellation, or lineage update proceeds under it. **Already-created external candidate-batch records remain preserved**; an activated but never-selected candidate is closed **only** through the bounded legal §5.2 abandonment transition with the stale-plan evidence recorded; **nothing is silently erased**; a new plan is required against current state |
| 35 | **Crash before the WB2 fence** (generation `granted`, no fence event) | = row 18 `granted` branch: cancel or fence by compare-and-commit; nothing appended; nothing to clear |
| 36 | **Fence compare-and-commit indeterminate** (cannot prove whether `granted` → `commit_fenced` committed) | The generation phase is authoritative and append-only: lookup decides committed-or-not; if the phase evidence itself is unreadable → claim `indeterminate_recovery_required`, admission for this identity fails closed; no cancellation, no regrant, no append proceeds on a guess |
| 37 | **Fence committed, root absent** | Recovery may commit the **distinct recovery-only terminal transition `commit_fenced` → `recovery_released_no_commit`** (§8.0 — never ordinary `cancelled`) **only when all four hold**: exclusive recovery authority is active; no live writer can still complete the old operation; the exact target batch and reserved `root_id` were checked; and root non-commit is **conclusively proven** at the append destination. On commit: the released generation is permanently unable to append; its reservation and completion right are extinguished; the claim may return to `available_uncommitted` with its `reserved_root_id` intact for retry. Otherwise the claim remains `indeterminate_recovery_required`. The release never rewrites, reconstructs, or re-appends anything |
| 38 | **Fence committed, root present, claim terminal transition absent** | Complete the claim's `committed{root_id, batch_id}` transition and the §8.2A `committed_to_batch` transition **from the append evidence**, idempotently; then WB3/WB4 per row 8 |
| 39 | **Fence evidence unreadable** | Claim `indeterminate_recovery_required`; admission for this identity fails closed; no cancellation, regrant, or append until the phase can be proven |
| 40 | **Duplicate recovery over a fenced generation** | `recovery_run_id` + lookup-first over the append-only phase events: a repeat run re-reads the same committed phases and re-applies nothing — no second fence, no second append, no second release; a committed `recovery_released_no_commit` is found and returned, never re-executed |
| 41 | **Attempted cancellation after fencing** | Refused by the phase compare-and-commit — the generation is `commit_fenced`, not `granted`; the claim cannot return to `available_uncommitted`; only append completion or row-37 resolution proceeds; the attempt is logged |
| 42 | **Attempted regrant while a fence remains unresolved** | Refused: the claim is `owned_uncommitted` (or `indeterminate_recovery_required`) — never `available_uncommitted` while a fenced generation is unresolved; no replacement generation may be granted; resolve rows 37–39 first |
| 43 | **Root-ownership entry reserved, its generation cancelled or recovery-released** | The entry **remains reserved for the same claim** (§8.2A — neither cancellation nor the §8.0 recovery release ever frees the `root_id`); the claim's safe retry re-uses **the same `reserved_root_id`** at the next WB1 — a different identity under this claim is rejected (§8.2A one-to-one); no reassignment to any other claim |
| 44 | **Root-ownership entry and claim disagree** (entry `committed_to_batch` while the claim lacks its terminal transition, or vice versa) | Lookup-first at the append destination decides: root present → complete both transitions from the append evidence (row 38); root conclusively absent → the `committed_to_batch` mark is contradicted by its own required evidence → `indeterminate_recovery_required`, fail closed for this identity; nothing is rewritten |
| 45 | **Root-ownership registry unreadable, incomplete, or conflicted** | **Admission fails closed** (§12); committed roots remain preserved and readable per their own integrity; resolution only by restoring provable registry evidence — never by guessing ownership |
| 46 | **Historical root-ID coverage incomplete or unverifiable** (§8.2B) | **New root writing fails closed** until coverage is verified complete or the gap is honestly recorded as fail-closed; no historical byte is touched; no capture claim is invented for a historical root |
| 47 | **Genesis selection with no predecessor** | LB4 mode A retries idempotently against expected `none/genesis`; no cutoff exists or is created; a crash before commit leaves nothing selected — writes remain fail-closed until the selection commits |
| 48 | **Initial-selection race** (two mode-A selectors) | The §4.3 compare-and-commit admits exactly one; the loser adopts the winner; the losing activated-but-never-selected candidate closes via the legal §5.2 abandonment transition (row 3). The temporary coexistence of activated-but-never-selected candidates is normal and is **never** a same-epoch selection fork (§6.4, §4.4) |
| 49 | **Post-shutdown successor selection** | Runs the §6.3 reactivation-creation path under its idempotent LB1 creation plan; LB4 mode A verifies the shut-down predecessor is non-admitting through its **existing LB5 cutoff — which remains unchanged**; no second cutoff, no rotation/seal plan, no sealing operation |
| 50 | **Reactivation while the prior batch is still draining but already cut off** | Legal: mode A verifies the predecessor's committed cutoff proves non-admission; the drain of pre-cutoff reservations continues into the old batch under §7.6/§9.3 unaffected by the new selection; LB6 still requires the drain to resolve |
| 51 | **Duplicate reactivation selection** | The mode-A compare-and-commit against the exact existing epoch makes the repeat a no-op returning the committed selection |
| 52 | **Stale reactivation attempt** (expected epoch no longer current) | Refused by the compare-and-commit; the attempt adopts the actual current selection; nothing is created |
| 53 | **Accidental attempt to create another cutoff for a sealed or already-cut-off predecessor** | Refused: mode A creates no cutoff by definition; mode B requires a currently selected `active` predecessor that still admits — a `sealed`, cut-off, `sealing`, or `invalid` predecessor fails that precondition; the existing cutoff remains the only cutoff; the attempt is logged |
| 54 | **Partial historical bootstrap set** (registration and/or state event and/or manifest missing) | Resume the §4.5 ordering idempotently (registration → state event → manifest) or the separate `bootstrap_completion_status` rests `incomplete` / `recovery_required` (§4.5 — never a `batch_state`): historical bytes untouched; no writability; excluded from completeness claims; no false completeness; the canonical `batch_state` stays accurate — `sealed` once the legal bootstrap state event exists, and none before it |
| 55 | **Historical bootstrap manifest invalid or contradicting the registration/state event** | `bootstrap_completion_status` → `recovery_required`; the batch is excluded from completeness claims; discovery reports the honest completion status while the canonical `batch_state` remains `sealed`; nothing historical is modified; resolution only by correcting the external records through new appends |

---

## §11A — Worked state traces (correction proofs)

**Trace 1 — normal cancellation wins from `granted`.** Generation G1 is
`granted`. Cancellation's compare-and-commit `granted → cancelled` wins
against any concurrent fence attempt on the same authoritative phase.
G1 can never fence or append (rows 22, 41 by symmetry); the claim returns
to `available_uncommitted`; a later WB1 may grant G2. The path used is the
first legal path — no fence existed, no release was needed.

**Trace 2 — fence wins, root conclusively absent: the strict recovery-only
release.** G1 wins the fence (`granted → commit_fenced`), then dies before
`append_root()`. Ordinary cancellation is illegal from `commit_fenced` (row
41). Recovery proves all four row-37 conditions — exclusive authority, no
live writer, exact batch + `reserved_root_id` checked, non-commit
conclusively proven — and commits the **distinct terminal**
`commit_fenced → recovery_released_no_commit`: G1 is permanently unable to
append; its reservation and completion right are extinguished; the claim
returns to `available_uncommitted` **with the same `reserved_root_id`
bound**; a later WB1 grants G2 for the same claim and identity. Any missing
proof → `indeterminate_recovery_required` instead. Nothing is rewritten,
reconstructed, or blindly re-appended.

**Trace 3 — duplicate recovery over the release is a no-op.** A second
recovery run over G1 reads the append-only phase events, finds the
committed `recovery_released_no_commit`, and returns it — no second
release, no second fence, no re-execution (row 40); `recovery_run_id` +
lookup-first make the repeat evidence-reading only.

**Trace 4 — one parent, separately identified children, one log each.** A
caller invokes the seam: parent `ingest_operation_id` P. The WB0
establishment/lookup runs as child C0; the WB1
generation+root-ID+reservation boundary as child C1; the WB2
fence+append+finalization as child C2 — each with its own stable
`child_op_id` referencing P, each emitting **exactly one** operational log
(§14). WB3 then records the **single parent terminal** for P. Four real
operations, four logs, one terminal — canonical state records throughout
are machine facts, not extra logs.

**Trace 5 — no operation ID receives two operational logs.** A retry of
child C1 after a crash locates C1's existing log by its `child_op_id` and
appends nothing new; recovery resolving P locates P's terminal by
`ingest_operation_id` — if present it is returned, if absent exactly one is
appended (row 8). No identity — parent or child — ever accumulates a second
operational log; writing WB3 creates no further logging operation.

**Trace 6 — the same claim retrying with a different `root_id` is rejected
before append.** Claim K bound `reserved_root_id` R1 at its first WB1. G1
is cancelled. K's retry arrives presenting R2: the WB1 verify-or-reserve
fails the §8.2A one-to-one check (one claim → one canonical `root_id`); the
attempt is rejected as an identity conflict, recorded append-only; R1 stays
K's identity; R2 reserves nothing. Contradictory authoritative evidence —
rather than a bad retry — would instead fail closed as
`indeterminate_recovery_required`.

**Trace 7 — the same claim safely reuses its original `root_id` after
cancellation or release.** After Trace 1's cancellation or Trace 2's
release, claim K is `available_uncommitted` and R1 remains
`reserved_for_claim` K (row 43). K's retry at WB1 reuses R1, gains G2, and
the fenced append commits R1 into exactly one batch — one capture, one
claim, one identity, one root, one owner.

**Trace 8 — associations stay external to the seven-field root.** The
fenced append commits the root with exactly its seven authoritative fields.
The claim key, generation, fence, ownership, and integrity associations are
recorded in the external B11 transaction/ownership evidence (§8.0, §8.2A,
§8.2C) — nothing is embedded into, appended to, or altered in the root
record itself.

**Trace 9 — a post-shutdown successor uses `no_active`, no LB-P plan, no
second cutoff.** Batch B was shutdown-sealed under its LB5 cutoff CUT-2.
The successor path runs the §6.3 reactivation creation: **LB1 with reason
`no_active`** (the superseded `shutdown_seal_successor` cannot authorize
anything), governed solely by that idempotent creation plan — no LB-P
rotation/seal plan exists or is required; LB4 **mode A** verifies B is
non-admitting through CUT-2, which remains unchanged, and commits only the
new selection. Any attempt to cut B again fails mode B's precondition
(row 53).

**Trace 10 — two LB3 candidates may coexist; only one becomes the selected
writable target.** Candidates X and Y both reach derived state `active` via
LB3 — a normal, legal, temporary coexistence (§6.4). Neither is writable:
§5.3 requires the current registry selection. The mode-A compare-and-commit
admits exactly one (say Y); X closes through the legal never-selected
abandonment with Y's selection recorded (row 48). At no moment did two
writable selections exist, and recovery never mistook X and Y for a
same-epoch selection fork — no committed selection records forked.

**Trace 11 — partial historical bootstrap: separate completion status,
accurate batch state.** The registration and the legal bootstrap state
event exist; the manifest does not yet. The canonical `batch_state` is
accurately `sealed` (established by the event); the separate
`bootstrap_completion_status` is `incomplete` — the batch is excluded from
completeness claims and never writable; discovery reports the honest
status; nothing historical is touched. When the manifest and the §8.2B
coverage validate, the status becomes `complete`; the batch state remains
`sealed`, unchanged. Before the state event existed, no canonical
historical state was claimed at all.

**Trace 12 — duplicate recovery over every corrected boundary remains
idempotent and fail-closed.** Re-running recovery over: a released
generation (Trace 3); a parent or child operation log (Trace 5); a rejected
second `root_id` (the conflict record is found, not re-created); a
`no_active` reactivation selection (row 51); a partial bootstrap set (rows
54–55) — each is `recovery_run_id` + lookup-first over append-only
evidence: committed findings are returned, nothing re-executed; unreadable
or contradictory evidence fails closed as `recovery_required` /
`indeterminate_recovery_required`; no root is rewritten; no content
invented; no ownership duplicated; no false success acknowledged; nothing
historical modified.

**Retained proofs (v1.1–v1.3, still binding):** **R1 — same-epoch fork, no
invented winner** (two committed selection records at one epoch; evidence-
only retention; no tie-breaker; both non-writable; roots preserved; repair
mechanism open in §16). **R2 — one `capture_id`, one root, one batch**
(non-overlapping generations, atomic WB1, cancel-or-release before regrant,
and the fence make a second commit structurally impossible). **R3 — no
terminal outcome before the parent's durable §0B record.** **R4 — fencing
and cancellation race: exactly one wins** on the single authoritative
phase. **R5 — root appended, finalization incomplete:** the claim terminal,
§8.2A `committed_to_batch`, and the parent terminal log complete
idempotently from the append evidence before acknowledgement. **R6 — a
stale cancelled generation can neither fence nor append** (`cancelled` is
terminal; the append verifies the durable fence immediately before
committing). **R7 — two different claims presenting the same `root_id`:**
the second is rejected before append by the §8.2A authority. **R8 — the
historical coverage gate:** new writes fail closed until §8.2B coverage is
verified complete. **R9 — genesis selection creates no predecessor
cutoff** (LB4 mode A against expected `none/genesis`; the historical batch
untouched).

---

## §12 — Fail-closed matrix

**Rule:** ordinary root writing **stops rather than guesses**. Fail-closed
never means destruction, silent omission, false success, or reverting to the
5,521-root batch. Already-durable roots remain preserved. Every fail-closed
event is recorded (§14).

| Condition | Behavior |
|---|---|
| Active target ambiguous (§4.4) | No reservation issued; caller receives `rejected(ambiguous_target)` or the seam refuses to resolve; recovery §11 row 4/5 |
| Manifest integrity cannot be established | Batch excluded from selection and coverage; writes to it refused |
| Batch `schema_compat_ref` unknown or mismatched to the payload's `schema_version` | Write `rejected(schema_incompatible)`; no coercion, no silent conversion |
| Seal state contradictory | Batch → `recovery_required`; no writes; no forced seal |
| Global claim ledger or its coverage cannot prove an identity free or already committed (§8.0) | **New root admission fails closed** — no acquisition, no reservation; outcome `indeterminate` only if WB2 status itself is unknowable, otherwise refusal before WB1 |
| Same-epoch selection fork with equally valid records | Ordinary writes blocked on both batches; no invented winner; fail-closed pending the later separately authorized repair (§16) |
| A stale, cancelled, superseded, pre-fence, or non-current ownership generation reaches WB2 | Refused: fencing requires the durable phase `granted` on the currently effective generation, and the append boundary verifies the durable `commit_fenced` phase immediately before committing; nothing commits; refusal logged |
| Rotation/seal plan is stale (expected epoch/batch changed) | The plan is superseded and authorizes no **new** effects; already-created external records are preserved; never-selected candidates close only via the legal §5.2 abandonment; nothing silently erased; a new plan is required |
| Fence evidence unreadable, or regrant attempted while a fence is unresolved | Claim `indeterminate_recovery_required`; no cancellation, regrant, or append; admission for this identity fails closed (§11 rows 39, 42) |
| Root-ownership registry failure, incomplete coverage, or conflict (§8.2A) | **Admission fails closed**; committed roots preserved; no ownership guessed |
| The same claim presents a different `root_id`, or the same `root_id` arrives under a different claim (§8.2A one-to-one) | Rejected **before append** as an integrity/identity conflict, recorded append-only; contradictory authoritative evidence → `indeterminate_recovery_required` — no identity guessed |
| Historical root-ID coverage incomplete or unverifiable (§8.2B) | **New root writing fails closed** until coverage is verified complete or the gap is honestly recorded; the historical `bootstrap_completion_status` stays `incomplete` / `recovery_required` while the canonical `batch_state` remains accurately `sealed`; nothing historical touched |
| Attempt to create a second cutoff for a sealed or already-cut-off predecessor | Refused (mode A creates none; mode B's precondition fails); the existing cutoff stands; attempt logged |
| Shutdown LB5 evidence partially readable / indeterminate | The batch → `recovery_required`; admission fails closed; no reservation is classified against an unproven cutoff |
| Write result indeterminate | `indeterminate`; no blind retry; lookup-first resolution only |
| Required upstream authority/eligibility evidence refs missing | `rejected(upstream_evidence_missing)` — B11 never substitutes its own judgment |
| Recovery would require modifying a sealed batch | The recovery action is refused; the condition is recorded and surfaced; sealed bytes are never touched |

---

## §13 — Interface and caller/callee wiring matrix

**B11 is the mandatory write seam** — every root-producing path resolves
through it to the shared `append_root()` boundary; **no direct file writes;
no path bypasses the shared B11/§7E write boundary.**

| Caller (via its §7E-side path) | Caller supplies | B11 validates (mechanical only) | B11 returns | Caller retains |
|---|---|---|---|---|
| C-7E catalog / pre-ingest promotion | Seven-field payload; eligibility + authorization + blocker-clearance refs; stable ingest-identity basis; provenance labels | Shape vs `schema_compat_ref`; evidence-ref existence; identity/idempotency; target state | §7.5 outcome + root identity + owning `batch_id` | Eligibility meaning; pre-ingest holding; blocker policy |
| C-13 / C-14 live conversation | Same, per live-turn capture identity | Same | Same | Capture policy; provenance-label meaning (A33/B17) |
| C-9A image ingestion | Same, per image-capture identity | Same | Same | Image capture/eligibility policy |
| Research entry (C-8 / CY-C) | Same, from the isolation path | Same | Same | Isolation rules (B13); research policy |
| Mobile Manual Sync (C-23 / CY-H) | Same, per sync-item identity | Same | Same | Sync scope/policy (A20) |
| TSC promotion (C-TSC / CY-D) | Same — TSC promotes **through §7E only**, never calling the boundary directly | Same | Same | TSC authorization, promotion, two-phase rules (settled; B-INT-4) |
| BOP observation roots | Same, per `capture_id`-style identity (the existing duplicate-absorption pattern preserved) | Same | Same | BOP DUMB capture boundaries |
| OOP outcome roots | Same | Same | Same | OOP boundaries |
| Every other future root-producing cycle | Same contract | Same | Same | Its own policy — B11 designs none of it |

B11 additionally serves **read-side structural consumers** (§7F retrieval,
audit, B23 later): discovery, identity lookup, provenance, coverage status
(§10) — never ranking, never failure policy, never semantic selection.

---

## §14 — Component-specific §0B logging matrix

One real operation → one append-only operational record; records link by
operation / batch / root **identities only** — never copying private root
content; no recursive log-about-logging; no double evidence; a log never
increases the truth or evidential weight of its subject; §7Q internal-use,
visibility, identity, and authority restrictions govern every record's
access; active/cold lifecycle follows §0B and is **not redesigned here**.

**Canonical state records vs §0B operational logs (binding distinction):**
manifests, batch-state events, claim status events, ownership-generation and
fence events, root-ownership entries, and admission-cutoff records are
**canonical transaction/state records** — machine facts required to
establish state. They are **not** additional §0B operational logs and are
**never** additional evidential votes. Separately, **every real operation
emits exactly one append-only §0B operational log**; for an atomic combined
boundary, that one log carries **all** of the boundary's effects: one LB-P
plan-commit log (with cause class); one rotation-LB4 log carrying both the
successor selection and the predecessor cutoff; one mode-A
initial/reactivation log carrying the selection and **explicitly recording
that no new cutoff was created**; one shutdown-LB5 log carrying cutoff,
admission stop, and sealing transition; one WB1 log carrying generation
grant, root-ID reservation, and batch reservation; one WB2 result for the
fence/append/claim/root-ownership commit operation; and one mandatory WB3
terminal outcome log per `ingest_operation_id`. **Operation-identity
hierarchy (§7.2):** the WB0, WB1, WB2, cancellation, recovery-resolution,
and target-resolution logs are **child-operation logs**, each under its own
stable `child_op_id` referencing the parent `ingest_operation_id`; **WB3 is
the single terminal operational record of the parent**; a child log is
never a second parent log; **no operation ID — parent or child — ever
carries two operational logs**; retries and recovery locate the existing
log by operation identity and never append another. Writing a log generates
no further log; a genuinely separate later operation receives its own.

| Record [all proposed] | Captures |
|---|---|
| `batch_creation_requested` / `prepared` / `validated` / `activated` / `rejected` / `failed` | The LB1–LB3 lifecycle with reasons |
| **One LB4 operational log per selection boundary** (supersedes logging `active_selection_committed` + `admission_cutoff_committed` as two logs for one atomic LB4) | Rotation mode B: one log carrying **both** the successor selection and the predecessor's `admission_cutoff_id`, linked to the LB-P plan. Mode A: one log carrying the initial/reactivation selection and **explicitly that no new cutoff was created**. `selection_not_committed` (incl. adopted-winner convergence) records non-commit outcomes. The selection and cutoff records themselves are canonical state records, not extra logs. The shutdown LB5 cutoff is carried in the LB5 log below |
| `claim_established` / `claim_found_committed` / `claim_found_owned` / `claim_found_available` | The WB0 establishment/lookup outcomes (no ownership at WB0) |
| `ownership_generation_granted` / `commit_fence_won` / `ownership_generation_cancelled` / `generation_recovery_released` / `claim_available_again` / `claim_committed` / `stale_or_unfenced_generation_refused` / `claim_indeterminate` | **Canonical §8.0 state events** (machine facts, not extra operational logs): the WB1 grant, the fence compare-and-commit winner, the per-generation cancellation, the strict recovery-only release, the availability return, the terminal transition, and every refusal of a stale/cancelled/released/unfenced generation at fencing or append |
| `root_ownership_reserved` / `root_ownership_committed` / `root_identity_conflict` / `historical_root_ownership_registered` / `historical_coverage_gap_fail_closed` | Canonical §8.2A/§8.2B records: each pre-commit `root_id` reservation and commit, each rejected conflicting presentation (append-only conflict records), the external historical registrations, and the operational fail-closed event when coverage cannot be proven |
| `mismatch_incident_recorded` | Each attached integrity incident (§8.4) — linked to the claim, never a status, never touching a terminal `committed` state |
| `plan_committed` / `plan_duplicate_noop` / `plan_superseded` | **The single LB-P plan-commit log** (with cause class) per plan — supersedes `rotation_plan_committed`; each idempotent duplicate no-op; each stale-plan supersession (no **new** effects; existing records preserved) |
| `selection_fork_detected` | Each same-epoch fork with the evidence findings; never a guessed winner |
| `selection_candidates_evaluated` | Batches evaluated and not selected during selection (use and non-use) |
| `append_target_resolved` | Each write-path resolution `{batch_id, selection_epoch}` |
| **One WB1 operational log per reservation boundary** | A **child-operation log** under its own `child_op_id` (parent-referenced), carrying all three atomic effects together: the ownership-generation grant, the §8.2A root-ID reservation, and the batch reservation |
| **One operational log per other separately executed child operation** | WB0 claim establishment/lookup, a cancellation, a recovery resolution, a target resolution — each under its own stable `child_op_id` referencing the parent; exactly one log per child |
| **One WB2 operational result per commit operation** | A **child-operation log** under its own `child_op_id` (parent-referenced), carrying the fence win, the physical append, the claim terminal transition, and the root-ownership `committed_to_batch` transition — one atomic operation, one log; the parent's mandatory WB3 terminal follows per `ingest_operation_id` |
| `append_committed` / `append_duplicate_absorbed` / `append_rejected` / `append_interrupted` / `append_indeterminate` / `append_recovered` | The **mandatory WB3 terminal record of the parent ingestion operation** — durably appended after the child operations and canonical records resolve and **before** WB4 returns the outcome; keyed by the parent `ingest_operation_id`; **exactly one terminal record per parent operation**, duplicates suppressed; child logs are never second parent logs |
| `sealing_initiated` / `sealing_blocked` / `sealing_interrupted` / `seal_committed` / `seal_recovered` | The LB5–LB6 lifecycle. **The shutdown-path LB5 emits one operational log carrying the cutoff (`admission_cutoff_id`), the admission stop, and the sealing transition together** |
| *(superseded vocabulary)* `rotation_plan_committed` / `successor_selected` | **Merged (C6):** the LB-P plan-commit log is the single plan log — `rotation_plan_committed` is superseded by it; successor-lineage facts live in the LB4 operational log and the canonical manifest/state records, never in a second operational log for the same operation |
| `manifest_verified` / `index_verified` / `verification_failed` | §9.4 / §10 verification outcomes |
| `bootstrap_registration_recorded` / `bootstrap_state_event_recorded` / `bootstrap_manifest_recorded` / `bootstrap_completion_status_recorded` | The §4.5 historical three-record set (canonical state records) and the honest recording of the separate `bootstrap_completion_status` (`incomplete` / `complete` / `recovery_required`) — completion metadata, never a `batch_state` |
| `state_mismatch_detected` / `identity_collision_detected` / `fail_closed_event` | Every §4.4 / §8.4 / §12 condition |
| `index_registration_committed` / `coverage_status_changed` | LB7 and honest coverage transitions |
| `recovery_run_started` / `recovery_action_applied` / `recovery_noop_duplicate` / `recovery_completed` | §11 runs, idempotent actions, and no-op duplicates |
| `refused_append_seal_blocked` / `refused_append_schema_invalid` / `refused_append_duplicate_key` | The existing refused-append record classes, preserved and generalized across batches |

---

## §15 — Privacy, authority, DUMB/SMART, and no-double-evidence boundaries

- **Privacy/authority:** batch manifests, registry records, indexes, and §14
  logs are internal records governed by §7Q internal-use authorization and
  §25 identity/security authorization where applicable; they carry
  identities and machine facts, never root text; visible surfacing of
  anything derived from them follows the settled output gates (owned
  elsewhere — consumed, not redesigned).
- **DUMB/SMART:** every B11 mechanism in this file is DUMB — identity,
  state, commit, verification, and bookkeeping over recorded facts. B11
  performs no interpretation, no relevance judgment, no truth
  establishment, no semantic eligibility choice; nothing in B11 converts a
  record into meaning.
- **Root/reading separation:** B11 handles sealed-root storage boxes only;
  readings, quarantine, and production remain separate stores and separate
  components; nothing here touches quarantine/production authorization.
- **No double evidence:** §8.5 binds — manifests, logs, indexes, checkpoints,
  and duplicate-visibility never add evidential weight; one root, one
  presence, one owner batch.

---

## §16 — Explicit open dependencies (recorded, not solved)

- A1 remaining artifact / audit / versioning / sealing work.
- Story-Layer firmness scale, evidential thresholds, scoring meaning.
- A25 reread-mode policy and B10 reread operation identity.
- A29 hold-until-enough policy and B-HOLD mechanics.
- B9 substantive-rejection retry policy and all numerical retry values
  (B11's `interrupted` permits technical re-attempt under the same key;
  every retry **policy** and value stays B9's).
- B16 quarantine-promotion evidence architecture and B-CYCLE-6.
- B21 future root-schema work (incl. the recorded `subject`-field rename
  consideration — a future `schema_version` + Ness adoption; not done here).
- B23 Person-Box cross-batch mechanics (consumes §10's identity/provenance
  interface later).
- B1/B26 retrieval ranking and retrieval-service failure policy (consume
  §10.4's honest coverage; own everything downstream of it).
- A24 Layer-2/Layer-3 handoff and decommissioning policy.
- Exact models, hardware, storage engine, index technology, filesystem
  layout, batch capacity/time/performance thresholds, and tuning values —
  declared later configuration/calibration, never invented here.
- C4 future `cursorrules` correction and the recorded Defaults §3C
  seal-wording drift — correctable only via future versioned candidates.
- The **same-epoch selection-fork repair mechanism** — a later, separately
  authorized design; until then equally-valid forks remain fail-closed
  (§4.4, §11 row 4).
- **Historical root-ID scanning and population** of the §8.2B external
  ownership records — later authorized implementation/disk-verification
  work; until coverage is verified complete, new root writing fails closed
  (§8.2B, §11 row 46, §12).
- Any deliberately authorized **migration or derived-root identity** for
  future schema versions — explicitly designed in B21-era work; never a
  silent second root for the same `capture_id` here.
- Any coding, migration, disk verification, production-store creation, or
  implementation — separately authorized, after design completion.

---

## §17 — Frozen closure-checklist self-audit (not a final verdict; ChatGPT's independent audit and Ness's acceptance are pending)

| # | Frozen checklist item | Self-check result |
|---|---|---|
| 1 | Purpose and standalone scope explicit | §1–§3 — met |
| 2 | 5,521-root batch permanently sealed and untouched | §2, §4.5, §6.4, §9.5, §12 — met; represented by a new external record only; two independent locks against ever targeting it |
| 3 | Future batches = separate immutable batches in one memory system | §5, §9.5, §10.5 — met |
| 4 | Every future root-producing path wired through B11 | §7.1, §13 — met; no-bypass rule explicit |
| 5 | Identity, manifests, lifecycle, selection, sealing, rotation complete | §4–§6, §9 — met within frozen scope |
| 6 | Operation identity and transaction boundaries explicit | LB-P, LB1–LB7 (LB4 in two modes), WB0–WB4 + PR, parent/child operation identities, §7.2 — met |
| 7 | Idempotency and cross-batch duplicate prevention explicit | §8 (eighteen points; global claim; one-to-one claim↔root binding; append commit fence with the strict recovery release; pre-commit §8.2A root-ownership authority) — met |
| 8 | Crash and partial-completion recovery complete and safe | §11 (fifty-five rows; lookup-first; no rewrite; no reconstruction) — met |
| 9 | Indeterminate/contradictory states fail closed without loss or false success | §7.5, §11, §12 — met |
| 10 | Cross-batch reading/index registration preserves boundaries and honest completeness | §10 — met |
| 11 | DUMB/SMART, root/reading, quarantine/production, privacy, relevance, authority boundaries preserved | §2, §3, §15 — met |
| 12 | §0B logging: one-operation/one-log, no double evidence | §14, §8.5 — met |
| 13 | Dependencies outside B11 open and accurately named | §16 — met |
| 14 | No code, migration, store creation, seal action, disk modification, or authoritative integration | §1, §19 — met |

**Checklist re-run (v1.4):** all fourteen items re-verified against the
corrected text — items 5–9 and 12 now rest on the three legal generation
paths with the strict recovery-only release, the parent/child operation
hierarchy under one-operation/one-log, the one-to-one claim↔`root_id`
binding, the corrected LB1 vocabulary and writable-selections invariant,
and the separate `bootstrap_completion_status`; the §11A traces (twelve,
plus nine retained proofs) carry the required proofs. The §17 counts above
state the actual v1.4 contract: five generation phases across three legal
paths, eighteen idempotency points, fifty-five recovery rows.

**CRITICAL-severity self-check — no issues found by this self-check.** The
sealed batch cannot be selected, targeted, re-opened, or modified by any
defined operation, including every recovery path; **every generation
transition is legal under the three defined paths — recovery exits a fence
only through the strict `recovery_released_no_commit` terminal under the
four row-37 proofs, never through ordinary cancellation (Traces 1–3, R4,
R6)**; **every operational log has exactly one operation identity — the
parent/child hierarchy makes one-operation/one-log mechanically verifiable
(Traces 4–5)**; no two claims can ever commit the same `root_id` and no
claim can ever hold two identities — the §8.2A binding is one-to-one in
both directions, decided pre-commit (Traces 6–7, R7), with new writes
failing closed until historical coverage is proven (R8); the same
`capture_id` cannot commit into two batches (R2); mismatch incidents never
displace a terminal `committed` claim; ambiguity and indeterminacy fail
closed without loss, destruction, silent omission, false success, or
fallback — including same-epoch forks, which never receive an invented
winner (R1); recovery never rewrites or reconstructs; the seven-field root
carries no B11 field, and every association lives in external evidence
(Trace 8, §8.2C); no policy was invented and no authority weakened.

**IMPORTANT-severity self-check — no issues found within the frozen scope.**
Boundaries LB-P/LB1–LB7 (LB4 in two modes)/WB0–WB4+PR, the eighteen
idempotency points, the 55-row recovery matrix, the fail-closed conditions,
the caller matrix, and the §14 record set are mutually consistent; the LB1
vocabulary matches the two selection modes with `shutdown_seal_successor`
retired (Trace 9, R9); multiple never-selected candidates may coexist while
only one writable selection is possible, and recovery never mistakes them
for a fork (Trace 10); the honest stale-plan rule holds in §6.1, §9.1, §11,
and §12 alike; the separate `bootstrap_completion_status` keeps the
canonical batch state accurate while gating discoverability on the full
record set plus §8.2B coverage (Trace 11); duplicate recovery is a no-op
everywhere (Trace 12); no terminal outcome precedes the parent's durable
record (R3).

**MINOR-severity, non-blocking notes (recorded per the severity standard; no
version churn requested):** all new identifiers are `[proposed]` pending
later naming; the illustrative successor-first sequence and the
`shutdown_seal` variant are structural, with trigger values open (a
seal-without-successor still runs the same cutoff/drain rules); the
`subject`-field rename remains a B21-era consideration only.

---

## §18 — Design-complete-for-B11 condition

B11 is design-complete for its frozen standalone scope when: this candidate's
contracts (§4–§15) stand as written; ChatGPT's independent audit of this
actual file returns PASS against the frozen checklist; and Ness explicitly
accepts the package. B11's completion **unlocks** (but does not begin,
authorize, or design) the writing paths of every future root-producing front
door and cycle, which remain blocked on their own packages and on separately
authorized implementation. Nothing in B11's completion lifts any seal,
creates any store, or authorizes any code.

---

## §19 — Delivery / change report

**Created:** exactly one new file —
`NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md` (this file).

**Correction report — every section changed in v1.4:** header/§1 (Corrects
block); §1A (v1.4 matrix §1A.0; prior matrices renumbered §1A.1–§1A.3 as
provenance); §4.5 (`bootstrap_completion_status` contract with the §8.2B
coverage as the fourth completion requirement); §5.1 (status-is-not-a-state
note); §6.1 (LB1 reasons `no_active`/`rotation`; `shutdown_seal_successor`
retired); §6.4 (writable-selections invariant; candidate coexistence);
§7.2 (parent/child operation identities); §7.3 (WB1 one-to-one
`reserved_root_id` binding; WB3 parent terminal); §7.4 (parent wording);
§8.0 (three legal generation paths; `reserved_root_id` field;
payload-integrity coverage statement; cancellation legal only from
`granted`; the strict recovery-release rule; external-evidence wording
replacing "embeds"); §8.1 (eighteen points; release and child-log rows;
parent WB3); §8.2A (bidirectional one-to-one binding); §8.2B (coverage
feeds completion status); §9.1 (honest stale-plan rule); §9.3
(fenced-reservation drain rule); §11 (rows 3, 4, 7, 37, 40, 43, 48, 54, 55);
§11A (twelve traces + nine retained proofs); §12 (one-to-one conflict row;
bootstrap-status wording); §14 (hierarchy preamble; child-log annotations;
release event; parent terminal; completion-status record); §17 (counts to
the actual v1.4 contract; re-run and refreshed audit); §19 (this report).
All other sections are byte-preserved from v1.3; prior correction-report
content is superseded by this one while v1.1–v1.3 remain intact on disk.

**Changed:** nothing existing. v1.0 (SHA-256 `518c639d…ce17`), v1.1
(`1bbc02b1…05fe`), v1.2 (`eef8e9bd…280f`), and v1.3 (`5ee2bee1…8c5c`) are
preserved byte-identical as historical candidate provenance. No
authoritative, accepted, map, plan, closure, historical, or prior-candidate
file was modified, overwritten, renamed, moved, patched, normalized, or
deleted. No commit, push, or upload was performed. No code, migration,
production store, historical-store modification, seal action, terminal
command, or implementation artifact was created. Local source copies were
hash-verified before writing (v1.3 `5ee2bee1…`, v1.2 `eef8e9bd…`, v1.1
`1bbc02b1…`, v1.0 `518c639d…`, B24 v7 `7f5762e5…`, its closure record
`83d79db9…`, the confirmed plan `2d6483d1…`, the A2 pointer `35d1a10a…`)
and remain untouched.

**No implementation occurred:** no code, no pseudocode intended as
implementation, no stores, no migrations, no production artifacts, no
terminal commands, no disk-change instructions, no seal action, no model or
technology adoption.

**Status claim:** DESIGN CANDIDATE only — not accepted, not adopted, not
`PACKAGE_COMPLETE`; those statuses require ChatGPT's independent audit and
Ness's explicit acceptance.

---

*`NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md` — DESIGN
CANDIDATE — NOT ADOPTED — NOT IMPLEMENTED — NOT `PACKAGE_COMPLETE`. The
Bundle-1 active writable-batch seam, corrected per ChatGPT's five-defect
re-audit of v1.3: the three legal generation paths with the strict
recovery-only release out of a fence; the parent/child operation hierarchy
making one-operation/one-log mechanically verifiable; the bidirectional
one-to-one claim↔`root_id` binding with all associations external to the
seven-field root; the corrected LB1 vocabulary, honest stale-plan rule, and
writable-selections invariant; and the separate `bootstrap_completion_status`
that never masquerades as a batch state — with the 5,521-root batch
permanently sealed and untouched, and v1.0 through v1.3 preserved
byte-identical. Awaiting ChatGPT's independent re-audit and Ness's explicit
acceptance.*

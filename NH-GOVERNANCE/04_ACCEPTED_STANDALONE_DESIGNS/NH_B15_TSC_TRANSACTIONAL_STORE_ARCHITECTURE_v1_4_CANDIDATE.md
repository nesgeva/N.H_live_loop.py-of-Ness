# NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md

## 0. STATUS BLOCK

**Status:** `CANDIDATE — NOT ACCEPTED — NOT ADOPTED — NOT BUILT.`
Mechanical architecture candidate: the concrete transactional-store
structure for the accepted §7E-TSC design. **Mechanics only, following
settled design:** it decides no new N.H meaning or policy, asks Ness
nothing, reopens no accepted TSC/A15/A16/A26/A7 content, completes no
B-INT package, and begins no implementation. No code, live database,
production schema activation, migration, test, or Cursor instruction
exists or is created. Independent of, and not merged with, the
separately prepared B7 candidate.

**Date:** July 13, 2026.

**Version note (v1_4):** narrow archive-control recovery completion
of v1_3 only (v1_3 SHA-256
`f1a3952b39fcd380a20fb606f961210db2e78106fe67ce352cfdd7c30c0fdb82`;
939 lines; 54,483 bytes — preserved unchanged, as are v1_0 through
v1_2; B7 v1_3 received ChatGPT PASS and is not touched), per
ChatGPT's audit. All v1_3 schemas, attribution rules, ordering,
promotion behavior, the database freeze boundary, the A16 names, and
the automatic authorized-promotion behavior are preserved. **Three
completions:** (1) the archive control manifest now carries its
**complete design-level schema** (§8 class 9) — thirteen fields with
required/optional marking and the uniqueness and idempotency
constraints, including `transition_operation_id` as the idempotency
key and the exact required content of the initial `archived` manifest
(prior `promoted`, references `tsc_retained_archive_created`, no
authorization applicable, no A16 seal events) versus a
permanent-seal manifest version (prior `archived`, a valid separate
authorization reference required, both active A16 event references
required); (2) **archive-creation crash recovery** is defined for
every boundary — crash before the `archived` commit; unverified
snapshot; verified snapshot with the database still `promoted`;
frozen `archived` database without its initial manifest; a doubled
initial-manifest attempt; a manifest failing integrity verification —
trusting committed and verified state only, never reopening the
frozen database, creating a missing initial manifest idempotently,
and failing honestly inaccessible when verification fails (§9); (3)
**permanent-seal crash recovery** is defined as an ordered idempotent
operation with every crash point covered, the effective state
remaining `archived` until a valid manifest version referencing the
completed authorized transition verifies, resumption only while the
separate authorization remains valid under its owning authority,
duplicate retries reusing the same `transition_operation_id`, no
duplicate A16 events or manifest versions ever written, and the
frozen database never modified — plus **invalid-manifest handling**:
the latest **verified** manifest governs; a damaged, contradictory,
or unverifiable newer manifest is never silently accepted, the
archive stays inaccessible, the last verified history is preserved,
and the control-integrity failure is recorded and reported (§9,
§11). **No schema field of the thirteen tables, no lifecycle value,
no ordering or promotion rule changed; no new policy.**

**Version note (v1_3):** narrow consistency correction of v1_2 only
(v1_2 SHA-256
`8dddb67d20131b7c04fc1a686d17e4e52b5ad901f2769dc2017d9d4193d14633`;
836 lines; 47,884 bytes — preserved unchanged, as are v1_0 and v1_1),
per ChatGPT's audit. Every corrected v1_2 schema, attribution,
transaction, ordering, and recovery rule is preserved; only the
archive-lifecycle authority and the automatic-promotion wording are
made coherent. (1) **One explicit authority split for archive
state:** before the archive freeze, the SQLite database and
`sessions.lifecycle_status` are authoritative through the successful
transition to `archived`; the archive-creation transaction verifies
promotion completion, creates and verifies the frozen encrypted
snapshot, sets `archived`, commits the final in-database lifecycle
and audit references through `tsc_retained_archive_created`, and
freezes database and snapshot read-only. After the freeze, the frozen
database is never modified again; a separate **content-free,
append-only archive control manifest** becomes authoritative for
post-archive control state only — the latest valid manifest version
determines the effective archive-layer lifecycle (initial:
`archived`; later separately authorized: `permanently_sealed`); the
frozen database's own row remains an immutable record that the
archive reached `archived` and is never rewritten to claim
`permanently_sealed`; the logical session lifecycle still includes
`permanently_sealed`; the manifest is structural control metadata
only and never a second memory system. (2) **Post-archive audit
references corrected:** rows enter the in-database
`security_audit_refs` only through the archive-freeze transaction;
after the freeze, `tsc_archive_seal_authorized` and
`tsc_archive_sealed` are recorded in the external append-only
security audit/control history and referenced by the manifest — the
v1_2 wording that had `security_audit_refs` anchoring post-freeze
events is removed (§5 table 13, §6, §8 class 9, §9, §11, §12, §13
aligned). (3) **The unqualified "auto-promote" must-never is replaced
with the precise prohibition:** never promote before successful
authorization, never bypass BAI/SACL, never independently invent
promotion authority — while the accepted automatic start after
authorization, automatic continuation, and automatic retry of
temporary retryable failures are explicitly preserved. A full-file
sweep found no other frozen-row-authority, post-archive-write, or
all-automatic-promotion-forbidden remnant. **No schema field,
lifecycle value, ordering rule, or recovery rule changed.**

**Version note (v1_2):** correction pass on v1_1 only (v1_1 SHA-256
`676e622ed84f09fed711813666254a2331cc4975e97e04d43dd3b291f5f5d036`;
603 lines; 33,665 bytes — preserved unchanged, as is v1_0), applying
ChatGPT's re-audit requirements. **The corrections:** (1) **exact
accepted Master field names restored throughout §5** — every
`[proposed]` shortened substitute is gone (`preingest_ref` →
`preingest_capture_id` / `bop_preingest_capture_id`;
`sequence_number` → `sequence_position`; `participant_id` current
pointer → `contributor_stream_id` capture-time stream identity;
`item_state` → `item_lifecycle_status`; `person_box_ref` →
`assessed_person_box_id`; `sia_event_ref` → `sia_assessment_event_id`;
no generic `output_ref`), with the full accepted field lists for
tables 1–10 carried verbatim from the Master's schema blocks read on
disk, including the previously missing `sessions` fields
(`bai_token_id`, `sacl_recognized_ness_confirmed_at`,
`tsc_schema_version`, `notes`); (2) **the proposed blocker
replacements removed** — the accepted `blocker_type` set
(`pending_fingerprint_authorization`, `speaker_unresolved`,
`content_under_review`, `technical_hold`), accepted statuses
(`active`, `resolved`, `waived_by_exclusion`), accepted fields
(`resolution_method`, `resolution_event_ref`), and accepted
`blocker_history` events (`blocker_added`, `blocker_resolved`,
`resolution_attempt_failed`, `blocker_waived`) restored exactly;
`privacy_exclusion_pending` and the `raised`/`resolved`/`reopened`
vocabulary are gone; (3) **capture-time attribution made immutable**
— the `participant_id` current pointer, the "latest non-superseded"
rule, and the attribution-update transaction are removed; later
evidence appends; later resolution may clear `speaker_unresolved` and
supply the promoted `role` via §7E but never rewrites or transfers
identity, certainty, or permission between streams; (4) **sealing
scoped precisely** — captured rows, positions, structure, stream
identity, capture-time attribution, and raw references are immutable
at sealing, while the accepted forward lifecycle (authorization,
blocker resolution, lifecycle transitions, promotion checkpoints,
retries, recovery, audit references) remains appendable through valid
recorded transactions; the whole-file freeze is `archived`'s; the
permanent seal is recorded outside the frozen snapshot; (5) **startup
recovery replaced with the exact accepted §27 behavior** — including
automatic promotion start from `authorized`, automatic resume from
`promoting`, automatic retry of temporary retryable
`promotion_failed` with attempts remaining, the idempotent
promoted-with-archive repair, unknown-readable-state fail-closed
interrupted sealing, and corruption quarantine — removing v1_1's
"sealed/authorized both wait" and blanket "promotion_failed waits"
wording; (6) **promotion crash recovery completed** — deriving the
§7E `capture_id` from `preingest_capture_id`, idempotency lookup,
recovering the existing `root_id`, committing the missing state
exactly once, never another root, with the full accepted ordering
preserved. The single session-wide allocator stays, as the additive
`sessions.next_sequence_position` field issuing accepted
`sequence_position` values. **No table added or removed; no accepted
mechanism weakened; no policy invented.**

**Instruction provenance, stated honestly:** the governing v1.2
correction instruction document arrived with empty content twice (in
the pre-compaction conversation and again in the re-sent message);
its full requirements were carried into this file from Claude's
contemporaneous verbatim-requirements record made while the
instruction was in context, and every accepted field list, lifecycle
value, blocker value, event name, and recovery rule was then
independently re-verified against the Master's own schema and §27
blocks read on disk at the pinned head — the Master, not memory, is
the source of every accepted name in §5 and §9. This provenance is
flagged for ChatGPT's re-audit.

**Register item:** B15 — Bundle 5 mechanical work (Bundle 5 —
Privacy, security, access, and TSC authority). Map: *"B15 — TSC
transactional-DB structural choice (ACID/crash-safe/local-only
requirement settled; specific store is a structural pick)."* → C-TSC.

**Intended repository placement:** `05_ACTIVE_CANDIDATE/`
(the physical move into the repository is Ness's action).

**Pinned repository baseline:** `nesgeva/NH-GOVERNANCE`, branch
`main`, head `bbf4e900a00d1082d11829bfd33ca339d8b98b00` — confirmed
current by `git ls-remote` before writing.

## 1. GOVERNING AUTHORITY AND SOURCE INVENTORY

**Authority order:** (1) `NH_MASTER-20_CORRECTED_v10.md` (adopted by
Ness June 29, 2026); (2) `NH_DECISION_DEFAULTS-S19_v2_2.md`;
(3) `cursorrules`; (4) `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`.

**Sources read for this candidate, byte-verified at the pinned head:**
Master V10 (`2d9ed4c6…`) — the §7E-TSC design: the store model and
"All items in one place" boundary, §3 Transactional Database Model
(logical thirteen-table schema; "the choice of specific technology
(SQLite, embedded key-value store with transaction support, or
equivalent) is a build-time decision; the architectural requirement
is: ACID transactions, crash-safe writes, local-only operation, and no
network dependency"), §4 session record schema, §12 session and item
lifecycles, §13 normal sealing, §14 interrupted sealing and linked
continuation, §24 duplicate protection, §25 privacy precedence, §26
security audit events (including the superseded/adopted archive-event
vocabulary), §27 startup recovery, and §11 item 35; the Map v1.6
(`33af648d…`) — C-TSC context, **B15** and **B-INT-4** register
entries; the eight-bundle plan (`2d6483d1…`, Bundle 5);
`06_OPERATIONAL_INSTRUCTIONS/NH_CLAUDE_PROJECT_INSTRUCTIONS_v1_2_CANDIDATE.md`
(`80480613…`); **accepted A26** and **accepted A7** with their closure
receipts (identity/mode boundary and privacy rules, by reference);
**the supplied accepted A16 candidate**
`NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_v1_0_CANDIDATE.md`
(verified SHA-256
`1b539f57a7d31daba7c8da15d0dcdf988eba2e560c5d9532e3db42a28bcf96e6`;
read in full).

**Honest A16 status:** the A16 vocabulary package was **accepted by
Ness after ChatGPT's PASS**, and its adopted active names
(`tsc_archive_seal_authorized`, `tsc_archive_sealed`) are used here as
the active archive-event vocabulary. At the pinned head, the A16 file
**has not yet been committed to GitHub and has no closure receipt
yet**; this candidate relies on the verified supplied file and records
that status plainly.

## 2. PURPOSE AND PLAIN MEANING

B15 is the box the session lives in. The accepted TSC design says what
the temporary session cache does; B15 picks and shapes the actual
store that does it — one small local database per session that either
fully records a step or fully doesn't, survives crashes without
inventing anything, holds only the session's skeleton (never the
words themselves), and, once sealed, never changes what was
captured — only the accepted forward lifecycle still moves.

## 3. THE MECHANICAL CHOICE — SQLITE, ONE DATABASE FILE PER SESSION

**Choice:** the TSC structural store is **SQLite, one database file
per TSC session.** This is the structural pick the accepted design
explicitly left as a build-level decision under fixed requirements —
a mechanical selection, **not policy**, because every governing
requirement was already accepted: ACID transactions; crash-safe
writes; local-only operation; no network dependency; per-session
isolation; startup examinability. SQLite satisfies them as a
requirement class: single local file per session, serverless, no
network surface, transactional with durable commits.

**Required guarantees the later concrete settings must satisfy**
(binding on implementation; exact mechanisms open): **ACID
transactions**; **durability at commit** (write-ahead-log or
rollback-journal class durability such that a committed transaction
survives power loss); **crash atomicity** (an interrupted transaction
leaves no partial state visible); **local-only, zero network
dependency**; **one self-contained file per session**, individually
examinable at startup recovery; **encryption at rest for the retained
archive state** (the archived session file is encrypted; key handling
sits with the settled §25/BAI security machinery, not invented here);
**integrity checkability** (the file can be verified for structural
corruption and schema-version match). **Explicitly open:** exact
SQLite version, journal/WAL mode and synchronous settings, page and
cache tuning, the encryption library and mode, file naming and
directory layout, and every other pragma or tuning value — build-time
work under these guarantees.

## 4. THE STORE BOUNDARY — STRUCTURE ONLY, NEVER PAYLOADS

The per-session database holds **structural and organizational records
only**: references into the §7E pre-ingest store (where every raw
conversation contribution and BOP observation payload lives under
`"pending_fingerprint_authorization"`); speaker-attribution
**references**; branch and reply links; blocker states and their
history; lifecycle states; promotion progress with resulting
`root_id`s; and references to security audit events. **It never
stores:** raw conversation text, BOP payload content, audio, excluded
content, or credentials. It is an organizational extension of §7E for
one session — **never a second cache, never a second memory, never a
bypass** around §7E, §7Q, or the sealed root store. Excluded material
routes to sealed protected storage under §7Q/B7; the TSC keeps only
non-reconstructive exclusion metadata and opaque references, per the
settled §7E-TSC §25 precedence rule.

## 5. LOGICAL SCHEMA — THE THIRTEEN ACCEPTED TABLES, EXACT ACCEPTED FIELDS

Every table: **no destructive delete exists** on any row anywhere
(corrections and resolutions are new rows or state-transition updates
recorded in the append-only companions); all cross-references are
enforced foreign keys within the session file; identifiers are stable
within the session. **Tables 1–10 carry the exact accepted Master
§7E-TSC field names, read verbatim on disk from the accepted schema
blocks — nothing renamed, nothing shortened, nothing substituted.**
Tables 11–13 are named in the accepted thirteen-table list with stated
purposes but no accepted field-level schema; their field lists below
are B15 design-level, clearly labeled. Exact column types and
serialization are implementation-facing.

**1. `sessions`** — exactly one row per file (enforced: single-row
constraint). **Exact accepted fields:** `session_id` (uuid4, PK);
`session_mode` (`"voice"` | `"text"` | `"mixed"`); `started_at`;
`sealed_at` (nullable); `authorized_at` (nullable);
`promotion_started_at` (nullable); `promotion_completed_at`
(nullable); `lifecycle_status` (`"active"` | `"sealed"` |
`"authorized"` | `"promoting"` | `"promoted"` | `"promotion_failed"` |
`"interrupted"` | `"archived"` | `"permanently_sealed"` — the accepted
set; **no `deleted` value exists**); `continuation_of_session_id`
(uuid4 or null); `interruption_recorded` (boolean); `bai_token_id`
(uuid4 or null); `sacl_recognized_ness_confirmed_at` (timestamp or
null); `tsc_schema_version` (`"tsc_v1"`); `notes` (string or null).
**Additive allocator field [B15 design-level, additive only]:**
`next_sequence_position` — the **single session-wide ordering
allocator**: a current-state counter, read-incremented-committed
atomically inside the same transaction as each ordered append, issuing
every accepted `sequence_position` value used by `contributions` and
`nh_outputs` so ordered rows across both tables share one monotonic
session timeline (the accepted design's interleaved full-session
order); aborted transactions may leave harmless gaps — ordering
requires monotonicity, never density. It adds a field; it renames and
removes nothing. Current-state row; every status change also writes
`lifecycle_events`. Recovery meaning: the single authoritative session
state at restart (§9).

**2. `contributions`** — one row per natural conversation
contribution. **Exact accepted fields:** `contribution_id` (uuid4,
PK); `session_id` (FK); `sequence_position` (integer — ordinal
position within this session; 1-based; set at capture time; **never
changed**; issued by the §5-table-1 allocator so it is unique across
`contributions` **and** `nh_outputs` and monotonic on one shared
timeline); `occurred_at`; `duration_ms` (nullable);
`contributor_stream_id` (FK → `participants.stream_id` — **always the
physical stream identity captured at the moment of contribution;
never a nullable person pointer, never rewritten, never transferred to
another stream**); `role` (`"ness"` | `"participant"` | `"nh_output"`
| `"unknown"` — no root is ever written with `role = "unknown"`; §7E
speaker resolution supplies the promoted role); `content_type`
(`"voice"` | `"text"` | `"nh_text"` | `"nh_voice"` | `"other"`);
`preingest_capture_id` (uuid4 — the capture_id of this contribution's
§7E pre-ingest record; the payload lives there, never here;
**required, unique**); `word_count` (nullable); `character_count`
(nullable); `reply_to_contribution_id` (uuid4 or null);
`branch_level` (integer); `item_lifecycle_status` (`"held"` |
`"ready"` | `"promoting"` | `"promoted"` | `"excluded"` | `"blocked"`
— the accepted item lifecycle; `promotion_failed` is session-level
only, never an item value); `promoted_root_id` (uuid4 or null;
**unique when present**); `exclusion_metadata` (JSON or null —
non-reconstructive metadata describing the type of exclusion; no
excluded content); `content_hash` (SHA-256 of raw_content at capture
time). Duplicate prevention: unique `preingest_capture_id` and unique
(`session_id`, `sequence_position`).

**3. `participants`** — one row per detected participant stream.
**Exact accepted fields:** `stream_id` (uuid4, PK); `session_id`
(FK); `first_seen_at`; `last_seen_at`; `declared_role` (`"ness"` |
`"third_party"` | `"unknown"`); `assessed_person_box_id` (uuid4 or
null — linked, never copied); `assessed_certainty` (float [0.0, 1.0]
or null); `identity_status` (`"confirmed_known"` |
`"assessed_probable"` | `"unresolved"` | `"below_threshold"` |
`"unknown"`); `permission_boundary_record_version` (integer or null);
`sia_stream_id_ref` (uuid4 or null). Streams are structurally
separate: **no identity, certainty, or permission ever transfers
between streams** (accepted §21).

**4. `attribution_assessments`** — **append-only**; one row per
speaker-attribution event. **Exact accepted fields:** `assessment_id`
(uuid4, PK); `session_id` (FK); `stream_id` (FK); `contribution_id`
(FK or null); `assessed_at`; `assessed_person_box_id` (uuid4 or
null); `assessed_certainty` (float [0.0, 1.0]);
`certainty_dimensions` (JSON object); `uncertainty_flags` (JSON
array); `anti_spoofing_suspicion_level` (`"none"` | `"low"` |
`"medium"` | `"high"`); `sia_assessment_event_id` (uuid4 — the SIA
authority record; authority lives in SIA, not here). **Capture-time
attribution is immutable:** attribution certainty is recorded at the
moment of capture and **never upgraded retrospectively within the
TSC** (accepted §7). Later evidence is **appended** as new assessment
rows and `sia_event_links` rows; **no "latest non-superseded" current
pointer exists, no assessment supersedes another inside the TSC, and
no attribution-update transaction rewrites captured rows.** Later
resolution may clear the `speaker_unresolved` blocker and supply the
promoted `role` through the §7E speaker-resolution rule — it never
rewrites or transfers identity, certainty, or permission between
streams.

**5. `branch_links`** — one row per reply/branch relationship. **Exact
accepted fields:** `link_id` (uuid4, PK); `session_id` (FK);
`child_contribution_id` (FK); `parent_contribution_id` (FK or null);
`link_type` (`"direct_reply"` | `"continuation"` | `"interruption"` |
`"branch_open"` | `"branch_close"` | `"context_reference"`);
`confidence` (`"certain"` | `"inferred"` | `"uncertain"`);
`confidence_basis` (string). Append-only. `sequence_position`
establishes total chronological order; branch links express reply
structure without changing the chronological record; the
parent-before-child promotion dependency is enforced (accepted §8,
§18).

**6. `bop_preingest_links`** — one row per BOP observation root in the
§7E pre-ingest store. **Exact accepted fields:** `link_id` (uuid4,
PK); `session_id` (FK); `bop_preingest_capture_id` (uuid4 — the
capture_id of the BOP observation root's §7E pre-ingest record; this
root is HELD in §7E pre-ingest, not yet in the sealed store;
**required, unique**); `linked_contribution_id` (uuid4 or null);
`occurred_at`; `event_type` (string — the BOP event_type for
reference; classification metadata, never payload);
`relationship_type` (`"concurrent"` | `"precedes_contribution"` |
`"follows_contribution"` | `"session_level"`).

**7. `sia_event_links`** — one row per SIA assessment event linked to
a contribution moment. **Exact accepted fields:** `link_id` (uuid4,
PK); `session_id` (FK); `sia_assessment_event_id` (uuid4 — in the
security audit log; not held in §7E; SIA assessment events are not
promoted as roots; unique); `linked_contribution_id` (uuid4 or null);
`assessed_at`; `relationship_type` (`"assessment_at_contribution"` |
`"session_level"` | `"between_contributions"`). Append-only;
reference only — SIA's records stay SIA's.

**8. `nh_outputs`** — one row per N.H response or output within the
session. **Exact accepted fields:** `output_id` (uuid4, PK);
`session_id` (FK); `sequence_position` (integer — **interleaved with
contributions in the full session order**; issued by the **same**
§5-table-1 allocator, making cross-table uniqueness and one timeline
structurally enforced); `produced_at`; `output_type`
(`"text_response"` | `"voice_response"` | `"action_result"` |
`"translation_output"` | `"system_message"`);
`addressed_to_stream_id` (uuid4 or null); `access_level_at_output`
(`"top_security"` | `"recognized_ness"` | `"known_person"` |
`"guest"`); `preingest_capture_id` (uuid4 — the capture_id of this
output's §7E pre-ingest record, held under
`"pending_fingerprint_authorization"`; **always present and unique —
no generic `output_ref` alternative exists**); `item_lifecycle_status`
(`"held"` | `"ready"` | `"promoting"` | `"promoted"` | `"excluded"` —
the accepted output set); `promoted_root_id` (uuid4 or null; unique
when present). N.H outputs are promoted as roots with `role = "nh"`.

**9. `blockers`** — one row per active-or-resolved blocker per item.
**Exact accepted fields:** `blocker_id` (uuid4, PK); `session_id`
(FK); `item_id` (uuid4); `item_type` (`"contribution"` |
`"nh_output"` | `"bop_root"` | `"session"`); `blocker_type` — **the
exact accepted set and nothing else:**
`"pending_fingerprint_authorization"` | `"speaker_unresolved"` |
`"content_under_review"` | `"technical_hold"`; `added_at`; `status`
(`"active"` | `"resolved"` | `"waived_by_exclusion"`); `resolved_at`
(timestamp or null); `resolution_method` (string or null);
`resolution_event_ref` (uuid4 or null). The proposed
`privacy_exclusion_pending` replacement from v1_1 is **removed** — the
accepted `"content_under_review"` covers content whose classification
is pending, `"technical_hold"` covers mechanical faults, and
`"waived_by_exclusion"` is the accepted status when §7Q exclusion
resolves an item out of promotion. `"pending_fingerprint_authorization"`
is raised at capture on every item and resolved by the accepted
authorization transition; `"speaker_unresolved"` resolves only through
§7E's speaker-resolution rule, never TSC logic. **Rule, structurally
enforced:** an item with any `"active"` blocker cannot transition to
`promoting`; no item ever reaches `promoted` while
`"speaker_unresolved"` is active.

**10. `blocker_history`** — **append-only** resolution history.
**Exact accepted fields:** `history_id` (uuid4, PK); `blocker_id`
(FK); `event_type` — **the exact accepted set and nothing else:**
`"blocker_added"` | `"blocker_resolved"` |
`"resolution_attempt_failed"` | `"blocker_waived"`; `event_at`;
`event_detail` (string); `event_ref` (uuid4 or null — what resolved
it: e.g., the authorization event, an attribution assessment, a §7Q
classification outcome, a recovery record). The v1_1 proposed
`raised` / `resolved` / `reopened` event vocabulary is **removed**.
Never edited.

**11. `lifecycle_events`** — accepted purpose: *"append-only lifecycle
state log for the session."* **Fields [B15 design-level — the Master
names the table and purpose without an accepted field list]:**
`lifecycle_event_id` (PK); `session_id` (FK); `from_status`;
`to_status`; `at`; `reason_ref` (e.g., seal reason; authorization
event; failure record; recovery record). Every
`sessions.lifecycle_status` change has exactly one row here — the
audit trail behind the current-state field. Recovery meaning: the
last committed row must agree with `sessions.lifecycle_status`;
disagreement is an integrity failure (§9).

**12. `promotion_state`** — accepted purpose: *"one row per item
tracking promotion progress"* (the accepted §17/§20 promotion
machinery names it for pending-blocked recording and per-item failure
tracking). **Fields [B15 design-level — no accepted field list]:**
item reference (PK; unique per item: the item's `item_type` +
identifier); `session_id` (FK); `phase` (`not_started` | `checked` |
`submitted` | `confirmed` | `excluded` | `blocked` | `failed` — the
per-item checkpoint; item failures are tracked here and in the
failure audit event, never as an item lifecycle value);
`promoted_root_id` (nullable; **unique when present** — the settled
duplicate protection); `attempted_at`; `confirmed_at`;
`failure_reason` (nullable). Per-item checkpoint for crash-safe
promotion (§8 class 8, §9); `append_root()` idempotency plus the
unique `promoted_root_id` make double promotion structurally
impossible.

**13. `security_audit_refs`** — accepted purpose: *"references to
security audit log entries from TSC operations."* **Fields [B15
design-level — no accepted field list]:** `audit_ref_id` (PK);
`session_id` (FK); `event_name` (from the settled §26 active set
**plus the A16-adopted `tsc_archive_seal_authorized` and
`tsc_archive_sealed`**; the superseded deletion/tombstone names are
never written as active events); `audit_log_ref`; `at`. Append-only;
the audit log itself lives outside the session file — this table only
anchors the cross-references. **Rows enter this table only up to and
through the archive-freeze transaction (§8 class 9); after the
freeze, nothing is ever appended to the frozen database — post-freeze
events (`tsc_archive_seal_authorized`, `tsc_archive_sealed`) live in
the external append-only security audit/control history and are
referenced by the archive control manifest (§11), never by new rows
here.**

## 6. SESSION ISOLATION

One session, one database file; a session's records never mix into
another session's file; no cross-session queries exist at the store
layer; continuation sessions (`continuation_of_session_id`) are
separate files linked by identifier only — two immutable units, each
sealed, authorized, and promoted separately; no shared mutable state
between session files; interrupted sessions stay their own sealed
files; the store layer offers no aggregate multi-session view (any
later authorized aggregate reads audit-log and sealed-store records,
not TSC internals); **before the archive freeze, a session file's
effective lifecycle is exactly its `sessions` row; after the freeze,
the frozen row remains the immutable record that the session reached
`archived`, and the effective archive-layer state comes from the
latest verified version of the append-only archive control manifest
(§11)**; nothing outside the accepted lifecycle can touch a
sealed file's content; and the retained-archive boundary (§11)
governs everything after `archived`.

## 7. CONCURRENCY AND OWNERSHIP

**Single-writer ownership:** exactly one owning TSC process/component
holds write access to a session file at a time; ownership is taken at
session open or recovery and recorded; **no concurrent writers ever**.
Within the owner, writes are serialized per session. Readers during
`active`: only the owning session machinery; there is no general
read API into a live session. After sealing, captured content is
immutable while the accepted forward lifecycle (authorization,
blocker resolution, promotion, recovery — §8 class 6) proceeds
through the single owner; after `archived`, the frozen snapshot is
read-only and access exists only through the bounded
archive-access path (§11). Lock behavior: the store's file/database
lock enforces single-writer at the storage layer as a backstop to the
ownership rule; a lock conflict is a terminal ownership error, never
silently retried into dual ownership. Ownership hand-off (e.g.,
recovery after crash) requires the previous owner to be provably gone
(process-instance identity recorded) before the new owner proceeds.
No background process mutates a session file outside the owner. All
promotion writes to the **sealed root store** go through
`append_root()` under its own idempotency — the TSC file records
progress; it never becomes a second writer to long-term memory.

## 8. TRANSACTION BOUNDARIES — THE NINE OPERATION CLASSES

Each class is one atomic transaction per step, with its
`lifecycle_events` / history row committed in the same transaction as
the state it records; each carries the session's operation identity
plus a per-step idempotency key so replays are detected, skipped, and
logged:

1. **Session creation** — create file; write single `sessions` row
   (`active`); first `lifecycle_events` row; `tsc_session_created`
   audit ref. Idempotency: `session_id`.
2. **Contribution append** — insert `contributions` row (+ optional
   `branch_links`) with its unique `preingest_capture_id` and
   capture-time `contributor_stream_id`, taking its
   `sequence_position` from the session allocator (§5 table 1) with
   the allocator increment committed **in the same transaction** as
   the insert; `nh_outputs` appends follow this same atomic
   allocator-plus-insert pattern. Replay hits the unique key →
   duplicate-prevention record.
3. **BOP link append** — insert `bop_preingest_links` row; same
   unique-reference protection (`bop_preingest_capture_id`).
4. **Attribution evidence append** — insert `attribution_assessments`
   row (append-only) and/or `sia_event_links` row, one transaction.
   **No current-pointer update exists and no captured row is
   rewritten:** capture-time stream identity
   (`contributor_stream_id`), capture-time assessments, certainty,
   and uncertainty are immutable; later evidence only accumulates
   beside them. Where later resolution satisfies §7E's
   speaker-resolution rule, the `speaker_unresolved` blocker
   transition (class 5) records it — supplying the promoted `role`
   for §7E — while identity, certainty, and permission never rewrite
   and never transfer between streams.
5. **Blocker transitions** — `blockers` state change (`"active"` →
   `"resolved"` or `"waived_by_exclusion"`) + `blocker_history` row
   (accepted event vocabulary: `"blocker_added"` /
   `"blocker_resolved"` / `"resolution_attempt_failed"` /
   `"blocker_waived"`), atomically; item `item_lifecycle_status`
   change to/from `blocked` in the same transaction.
6. **Sealing** — verify all items `held`/`blocked`; set
   `lifecycle_status` and `sealed_at`; `lifecycle_events` row;
   `cache_sealed` audit ref with the correct seal reason — one
   transaction. **What sealing makes immutable, exactly:** the
   captured contribution and output rows, their `sequence_position`
   values, the branch structure, stream identity, capture-time
   attribution, and the raw references (`preingest_capture_id`,
   `content_hash`) are immutable from this commit — nothing captured
   is ever edited, renumbered, reattributed, or removed. **What
   remains appendable, exactly — through valid recorded transactions
   only, per the accepted lifecycle itself:** the authorization
   transition (class 7), blocker resolutions (class 5), session
   lifecycle transitions, promotion checkpoints (class 8), retry
   records, recovery records, and audit references — the accepted
   design's own post-sealing operations (§16, §17, §20, §27 of the
   accepted TSC design all write to a sealed session). Sealed is not
   whole-file byte-frozen; it is captured-content-frozen with the
   accepted forward lifecycle still able to progress. The whole-file
   read-only freeze arrives at `archived` (§8 class 9, §11).
7. **Authorization transition** — record `bai_token_id` and
   `sacl_recognized_ness_confirmed_at` on the `sessions` row per the
   accepted §16; `sealed`/`interrupted` → `authorized`;
   `authorized_at` = now; event row; `cache_authorization_received`
   audit ref. (The token/SACL two-phase wiring itself is **B-INT-4**
   — this class only defines the store-side atomic transition.)
8. **Per-item promotion progress** — for each item, in ascending
   `sequence_position` with the parent-before-child overlay and BOP
   interleaving by `occurred_at` (accepted §17/§18): `promotion_state`
   phase advance (`checked` → `submitted` → `confirmed` with
   `promoted_root_id`, or `excluded`/`blocked`/`failed`) + item
   `item_lifecycle_status` change + the matching audit ref
   (`cache_promotion_item_*`) — **one transaction per item**, so a
   crash between items loses nothing and repeats nothing; a blocked
   parent defers its child to the next retry pass (never skipped
   permanently); unrelated `ready` items keep progressing; session
   `promoting` entry/exit and `cache_promotion_started`/`_completed`/
   `_failed` are their own transactions, and `cache_promotion_completed`
   is never written while any `blocked` item remains.
9. **Archive transitions — the authority split.** **The
   archive-creation transaction (the last in-database write):**
   verify promotion completion; create and verify the frozen
   encrypted snapshot; set the database session state to `archived`;
   commit the final in-database lifecycle and audit references
   through `tsc_retained_archive_created`; freeze the database and
   snapshot read-only — one committed sequence, after which **the
   frozen database is never modified again.** **The initial archive
   control manifest** is then written: a separate **content-free,
   append-only** structural control record. **Complete design-level
   manifest schema — every version carries:** `manifest_version_id`
   (required; unique; PK of the version); `session_id` (required);
   `archive_identity` (required — the frozen snapshot's identity);
   `archive_integrity_hash` (required — the verified snapshot hash);
   `prior_effective_state` (required); `new_effective_state`
   (required); `transition_operation_id` (required; **unique — the
   idempotency key of the transition**: one archive-layer transition,
   one id; every retry of the same transition reuses it, so a
   duplicate version for the same transition is structurally
   impossible); `archive_event_refs` (required — the external
   audit/control-history events this version rests on);
   `authorization_ref` (conditional — see below);
   `previous_manifest_version_ref` (required except on the initial
   version, where it is absent — the chain is linear: each version
   references exactly one predecessor);
   `previous_manifest_integrity_hash` (required wherever
   `previous_manifest_version_ref` is present — chain integrity);
   `created_at` (required); `manifest_integrity_data` (required —
   what verification of this version checks). **The initial
   `archived` manifest, exactly:** `prior_effective_state` =
   `promoted`; `new_effective_state` = `archived`;
   `archive_event_refs` references `tsc_retained_archive_created`;
   `authorization_ref` is **not applicable** (the archive transition
   rides the already-authorized promotion — no A16 permanent-seal
   event is required or permitted here); no
   `previous_manifest_version_ref`. **A permanent-seal manifest
   version, exactly:** `prior_effective_state` = `archived`;
   `new_effective_state` = `permanently_sealed`; a **valid separate
   `authorization_ref` is required**; `archive_event_refs` must
   include **both** active A16 event references —
   `tsc_archive_seal_authorized` **and** `tsc_archive_sealed`.
   **The separately authorized
   permanent seal** is a later manifest version — authorization
   recorded in the external append-only security audit/control
   history as `tsc_archive_seal_authorized`, completion as
   `tsc_archive_sealed`, both referenced by the new manifest version
   whose new effective state is `permanently_sealed` — **never
   automatic, never a write into the frozen database, never a rewrite
   of the frozen `sessions` row** (which remains the immutable record
   that the archive reached `archived`). The latest **verified**
   manifest version determines the effective archive-layer lifecycle
   (creation and seal crash recovery, and invalid-manifest handling:
   §9); the
   manifest holds no conversation payload, no ordinary memory, and no
   interpretation — structural control metadata only, never a second
   memory system.

## 9. INTEGRITY AND RECOVERY — THE EXACT ACCEPTED §27 BEHAVIOR

Startup recovery scans session files individually and trusts **only
committed state — nothing is reconstructed**. The per-state actions
are the accepted §27 rules exactly:

- `"active"` → crash during live session: **seal as `interrupted`**
  (`sealed_at` = restart time; `cache_sealed` written with
  `"interrupted_crash"`; everything committed before the crash
  preserved exactly).
- `"sealed"` or `"interrupted"` → **no action; the session waits for
  Ness's fingerprint authorization.**
- `"authorized"` → crash between authorization and promotion start:
  **begin promotion automatically.**
- `"promoting"` → crash during promotion: **resume automatically**
  (accepted §20 case A), with security conditions checked
  automatically first — if SACL no longer reports a recognized-Ness
  session, promotion pauses until conditions recover naturally; no
  new fingerprint, no new Ness action.
- `"promotion_failed"` → inspect the recorded failure class and follow
  the accepted §20: **a temporary retryable technical failure with
  attempts remaining retries automatically** after the declared
  backoff and, after the required security checks, transitions
  `"promotion_failed"` → `"promoting"` without a new fingerprint;
  **when retries are exhausted or the failure is non-retryable, the
  session remains `"promotion_failed"` and Ness may request a new
  attempt** — for an already-authorized session the requested attempt
  transitions back to `"promoting"` after the required security
  checks, which is not itself biometric authorization; new biometric
  authorization is required only when the session was never
  successfully authorized or the original BAI token was revoked
  before promotion began.
- `"promoted"` with no retained archive → **create the retained
  archive, verify it, write `tsc_retained_archive_created`, then
  transition to `"archived"`.**
- `"promoted"` with a retained archive that successfully exists but
  the state not yet transitioned → **idempotently repair the
  lifecycle to `"archived"`;** no new fingerprint for an
  already-completed archive transition.
- `"archived"` / `"permanently_sealed"` → normal terminal states; no
  ordinary runtime access; **no action.** (For an archived session,
  the effective archive-layer state is read from the latest verified
  archive control manifest version — §11; the frozen database is
  opened for nothing.)
- **Any readable but unknown `lifecycle_status` value → fail closed:
  seal as `interrupted`** (the accepted §28 unknown-state rule).
- **Structural corruption or integrity failure → quarantine the file
  read-only,** write a failure record, promote nothing from it, guess
  nothing, and inform Ness through the normal reporting path.

**Promotion crash recovery — per-item, exactly once:** per-item
`promotion_state` is the checkpoint. `confirmed` items stand.
`submitted` items — where `append_root()` may have succeeded but the
checkpoint commit is missing — are recovered by **deriving the §7E
`capture_id` from the item's `preingest_capture_id`** (the accepted
§19 derivation), performing the idempotency lookup against the sealed
store, **recovering the existing `root_id`, and committing the
missing `confirmed` state with that `promoted_root_id` exactly once —
never writing another root.** Unstarted items remain; the loop picks
up from the first item not yet `"promoted"`, `"excluded"`, or
`"blocked"`. Recovery preserves the accepted ordering completely:
ascending `sequence_position`; parent-before-child (a blocked
parent's child defers to the next retry pass, never skipped
permanently); BOP roots interleaved by `occurred_at`; unrelated
`ready` items keep progressing; and session completion —
`cache_promotion_completed`, the retained archive, `"promoted"`,
`"archived"` — **waits until no `blocked` item remains.**

**Archive-creation crash recovery — every boundary, trusting
committed and verified state only, never reopening or rewriting the
frozen database:**
- **Crash before the database commits `archived`:** the
  archive-creation transaction did not commit; the database is still
  authoritatively `promoted`. Per the accepted §27 rule, recovery
  creates and verifies the archive and completes the transition. An
  unverified partial snapshot from the crashed attempt is never
  trusted — it is superseded by a freshly created and verified one.
- **Snapshot exists but is not verified:** an unverified snapshot has
  no authority. Verify it; on verification failure, recreate it from
  the still-authoritative database, then proceed.
- **Verified snapshot exists but the database still says
  `promoted`:** the accepted idempotent repair — complete the
  in-database `archived` commit and the freeze; the verified snapshot
  is reused, not recreated.
- **Database committed `archived` and froze, but the initial manifest
  was not written:** create the missing initial manifest
  **idempotently from the verified archived database and the verified
  snapshot** — its `transition_operation_id` is derived
  deterministically from the session's archive transition, so any
  retry produces the same id; the frozen database is read for
  verification only, never reopened for writing.
- **Initial manifest write attempted twice:** the second attempt hits
  the `transition_operation_id` uniqueness constraint — recognized,
  skipped, recorded as a duplicate-prevention operation; exactly one
  initial version exists.
- **Manifest exists but fails integrity verification:** it is not
  accepted; **the archive is kept inaccessible, the failure is
  recorded and reported honestly, and no completed archive-control
  transition is claimed** until a verified manifest exists.

**Permanent-seal crash recovery — the ordered idempotent operation:**
(1) validate the separate authorization under its owning authority;
(2) record `tsc_archive_seal_authorized` in the external append-only
audit/control history; (3) perform the permanent-seal operation
idempotently; (4) record `tsc_archive_sealed`; (5) commit and verify
the new manifest version; (6) **only then** is the effective
archive-layer state treated as `permanently_sealed`. Crash coverage:
- **After authorization but before sealing completes:** resume the
  already-authorized incomplete operation **only while its
  authorization remains valid under the owning authority**; otherwise
  the session remains safely `archived` and a fresh authorization is
  required.
- **After sealing completes but before the completion event:** the
  retry reuses the same `transition_operation_id`; the idempotent
  seal step recognizes completion; `tsc_archive_sealed` is recorded
  exactly once.
- **After both events but before the manifest version:** write the
  manifest version referencing the completed authorized transition —
  same `transition_operation_id`, so no duplicate version can arise.
- **During manifest writing:** a partially written version fails
  verification and is never accepted (invalid-manifest handling
  below); the retry writes the version under the same
  `transition_operation_id`.
- **After successful manifest commit but before acknowledgment:** the
  committed verified version already governs; the acknowledgment
  replay is duplicate-detected and skipped.
Standing rules: **the effective state remains `archived` until a
valid manifest version referencing the completed authorized
transition verifies**; duplicate retries reuse the same
`transition_operation_id`; **no duplicate A16 events** (event
recording is keyed to the same transition id) **and no duplicate
manifest versions are ever written**; **the frozen SQLite database is
never modified.**

**Invalid-manifest handling:** the latest **verified** manifest
version governs the effective archive-layer state. When a newer
manifest version is damaged, contradictory, or unverifiable: it is
**never silently accepted**; **the archive is kept inaccessible**;
the last verified manifest history is preserved untouched; the
control-integrity failure is recorded and reported through the
normal reporting path; and **neither a new permanent seal nor a
successful recovery is claimed until verification succeeds.**

**Integrity checks at open:** structural corruption check;
`tsc_schema_version` match; single-`sessions`-row invariant;
`lifecycle_events` tail agrees with `lifecycle_status`; foreign-key
and unique-constraint validity. Partial-completion recovery is
per-item (class 8); duplicate prevention is structural (unique
`preingest_capture_id` / `bop_preingest_capture_id`, unique
`promoted_root_id`, unique (`session_id`, `sequence_position`),
idempotency keys); every recovery action is itself one recorded
operation.

## 10. APPEND-ONLY VERSUS CURRENT STATE

**Append-only, never edited:** `attribution_assessments`,
`branch_links`, `sia_event_links`, `blocker_history`,
`lifecycle_events`, `security_audit_refs`, and all §12 log records —
and, from sealing onward, every captured contribution and output row,
`sequence_position`, branch structure, stream identity, capture-time
attribution, and raw reference (§8 class 6).
**Current-state, transition-only:** `sessions.lifecycle_status` and
`sessions.next_sequence_position` (increment-only, atomically with
each ordered append),
`contributions.item_lifecycle_status` and
`nh_outputs.item_lifecycle_status`,
`blockers.status`, `promotion_state.phase` — each permitted to change
only along its accepted state machine, with every transition's
companion history row committed atomically alongside it. **No current
attribution pointer exists** — attribution evidence only accumulates
(§5 table 4). No row in
any table is ever destructively deleted; corrections are superseding
rows; the accepted no-destruction law binds the store absolutely.

## 11. THE RETAINED-ARCHIVE BOUNDARY

After promotion, the retained archive is created and the session
becomes `archived`: the structural database is sealed read-only; the
retained archive is **encrypted at rest** (§3 guarantee; key handling
per the settled security machinery); it is never active memory; LMAC,
§7F, §7G, Person-Boxes, Computed View, and all normal operational
components have **no read path** to it; access exists only through
`tsc_archive_access_authorized` for bounded machine-level integrity,
verification, recovery, or audit functions that expose nothing to a
person and return nothing to ordinary reasoning; **inspection remains
prohibited entirely** (no token, no mechanism, no path); the archive
is never re-submitted to §7E and can never double-promote (unique
`promoted_root_id` + runtime isolation); **after the freeze, the
effective archive-layer lifecycle is determined by the latest valid
version of the content-free, append-only archive control manifest
(§8 class 9; a damaged or unverifiable newer version is never
silently accepted — the archive stays inaccessible per §9's
invalid-manifest handling)** — the frozen database's own row stays
the immutable
record that the archive reached `archived` and is never rewritten;
`archived` → `permanently_sealed` happens only as a later separately
authorized manifest version, with the A16-adopted events
(`tsc_archive_seal_authorized` → `tsc_archive_sealed`) recorded in
the external append-only security audit/control history and
referenced by that manifest version — **never automatic, never a
write into the frozen database, never deletion, never destruction, no
`deleted` state, no tombstone**; the logical session lifecycle still
includes `permanently_sealed`; the manifest carries structural
control metadata only — no conversation payload, no ordinary memory,
no interpretation, never a second memory system;
the superseded historical names stay provenance-only and are never
written as active events; and archives wait indefinitely — no
auto-expiry.

## 12. LOGGING (§0B) — ONE OPERATION, ONE RECORD

Every real store operation produces exactly one append-only
operational record; logs are structural evidence of what the machinery
did, **never content evidence and never interpretation**; no record
contains conversation text, BOP payloads, excluded content, or
credentials — references and opaque identifiers only; all records
obey §7Q access rules. The record set [proposed], each with stable
id, schema version, operation identity, and timestamps: session
creation; contribution append; BOP link append; attribution
evidence append; blocker added; blocker resolved; blocker waived;
sealing; interruption sealing;
continuation link; authorization transition; promotion started;
per-item promotion result; promotion completed; promotion failed;
retained-archive creation; archive-control-manifest version written;
archive-access authorization use;
archive-seal authorization; archive sealed; plus duplicate-prevention,
crash-recovery, integrity-check, and quarantine records for the
recovery machinery (§9). Security-audit events remain the settled §26
set plus the two A16-adopted names — anchored through
`security_audit_refs` only up to and through the archive-freeze
transaction; after the freeze they live in the external append-only
security audit/control history, referenced by the archive control
manifest (§8 class 9, §11).

## 13. INTERFACES — THE STORE'S SIDE OF THE CONTRACTS

Store-side contracts (request/response shape: owner-identified,
operation-identified, idempotency-keyed step requests → committed-state
acknowledgments with record ids), for later wiring to: **§7E
pre-ingest** (reference registration; payloads never cross);
**BOP** (observation-link appends); **SIA** (attribution-assessment
references; authority stays SIA's); **§7Q/B7** (privacy precedence:
exclusion metadata non-reconstructive; excluded content routes to
sealed protected storage, never into the session file); **BAI/SACL
authorization** (the store-side `sealed` → `authorized` transition;
the two-phase token/SACL wiring is **B-INT-4**, not completed here);
**`append_root()` and the sealed root store** (promotion submissions
under its idempotency; `promoted_root_id` capture); **the security
audit log** (event refs); **startup recovery** (§9's per-file scan);
**archive integrity functions** (the bounded
`tsc_archive_access_authorized` path only); **the archive control
manifest** (append-only version writes carrying effective
archive-layer state; content-free — §8 class 9, §11). B7's enforcement
contracts and all B-INT wiring remain open and are consumed by
reference only.

## 14. MUST-NEVERS

The store must never: hold raw conversation or BOP payload content;
hold excluded content or credentials; become a second memory, cache,
or §7E bypass; write to the sealed root store except through
`append_root()` promotion; double-promote an item; promote a
`speaker_unresolved` or otherwise blocked item; **promote a session
before successful authorization, bypass BAI/SACL authorization, or
independently invent promotion authority** (the accepted automatic
behavior after authorization is explicitly preserved: successful
authorization begins promotion automatically, an already-authorized
interrupted promotion resumes automatically, and temporary retryable
failures retry automatically while attempts remain — §9);
auto-expire or auto-seal permanently; create a `deleted` state,
destructive delete, or tombstone; write the superseded archive-event
names as active events; edit, renumber, reattribute, or remove any
captured row after sealing, or mutate an archived snapshot; rewrite
capture-time attribution or transfer identity, certainty, or
permission between streams; allow a
second concurrent writer; reconstruct uncommitted state after a
crash; hide an integrity failure or proceed on unknown state; expose
the retained archive to any ordinary component or any person; skip a
lifecycle or blocker history row; let a log carry payload content or
act as content evidence; decide policy, identity, meaning, or
relevance; complete B-INT-4 or any other B-INT package; or start
implementation.

## 15. DESIGN-COMPLETE CONDITION

B15 is complete for its mechanical scope only when the accepted TSC
lifecycle can run on this store crash-safely and honestly: every step
atomic with its history; every restart resuming from committed truth
only; no duplication, no loss claims, no destruction, no payload
leakage, no archive exposure; and the A16-adopted vocabulary carried
exactly. This candidate asserts readiness for that condition
**pending ChatGPT's independent audit and Ness's later combined
Bundle 5 acceptance** — nothing is closed by this file.

## 16. EXPLICITLY OPEN

ChatGPT's independent audit of this actual file; any verified
correction; Ness's later combined acceptance; receipts and
accepted-source copies (including A16's own not-yet-existing closure
receipt and its GitHub commit — stated honestly in §1); **B-INT-4;
B-INT-5; B-INT-6; B-INT-7; B-INT-8**; Bundle 5 consistency and
closure; later Map or Master integration; all build-time values
(SQLite version, journal/synchronous settings, tuning, encryption
library and mode, file layout, retry values by reference); exact
column types, serialization, and final naming; all implementation and
coding.

## 17. REQUIRED VERIFICATION, CHANGE REPORT, AND SELF-AUDIT

**Drafting checks (no-loss and consistency checks performed by the
drafter — not independent verification, not enforcement proof):**
SQLite one-file-per-session recorded as a
mechanical structural pick under the accepted fixed requirements, with
the required guarantee set stated and all tuning open (§3) —
consistent in drafting.
Store boundary holds references only; §7E remains the payload home;
no second memory or bypass (§4) — consistent in drafting. Tables 1–10
carry the exact accepted Master field names, values, and controlled
vocabularies verbatim from the schema blocks read on disk — no
proposed substitute, shortened name, or invented value remains;
tables 11–13 carry clearly labeled B15 design-level schemas under
their accepted purposes; no table added or removed; ordering issued
by the single session-wide allocator (`next_sequence_position`,
additive only) so cross-table `sequence_position` uniqueness is
structural; the blocker and blocker-history vocabularies are exactly
the accepted sets (§5) — consistent in drafting. Accepted session and
item lifecycles carried exactly, including no `deleted` state,
`promotion_failed` as session-level only, and the
`speaker_unresolved` promotion bar (§5, §8, §9) — consistent in
drafting. Capture-time attribution immutable; no current pointer; no
retrospective upgrade; no cross-stream transfer (§5 table 4, §8 class
4, §10, §14) — consistent in drafting. Session
isolation and single-writer ownership enforced, with sealing scoped
to captured content while the accepted forward lifecycle proceeds
(§6, §7, §8 class 6) — consistent in drafting. Nine transaction
classes, each atomic with its
history row and idempotency key; per-item promotion checkpointing
with the accepted ordering, blocked-parent deferral, and the
no-blocked-items completion gate (§8) — consistent in drafting.
Recovery is the accepted §27 behavior exactly — automatic promotion
start from `authorized`, automatic resume from `promoting`, automatic
retry of retryable `promotion_failed` with attempts remaining,
idempotent archive repair, unknown-readable-state fail-closed
interrupted sealing, corruption quarantine — plus the exactly-once
`capture_id`-derivation crash recovery for missing checkpoints (§9) —
consistent in drafting.
Append-only versus current-state split explicit; no destructive
delete anywhere (§10) — consistent in drafting. Retained-archive
boundary complete and coherent under one authority split:
in-database authority through the archive-freeze transaction; the
content-free append-only manifest authoritative for effective
archive-layer state after the freeze; the frozen database and its
row never modified or rewritten; A16-adopted seal events recorded in
the external audit/control history and referenced by the manifest;
encrypted at rest, isolated, inspection prohibited, superseded
names provenance-only (§5 table 13, §6, §8 class 9, §9, §11, §12,
§13) — consistent in drafting. The promotion prohibition precise —
no promotion before authorization, no BAI/SACL bypass, no invented
authority — with the accepted automatic start, continuation, and
retry after authorization preserved (§9, §14) — consistent in
drafting. The manifest schema complete — thirteen fields with
required/optional marking, `transition_operation_id` uniqueness as
the transition idempotency key, a linear integrity-hashed version
chain, and the exact initial-versus-permanent-seal version contents
(§8 class 9) — consistent in drafting. Archive-creation and
permanent-seal crash recovery cover every named boundary, trusting
committed and verified state only, creating a missing initial
manifest idempotently, resuming a seal only under still-valid
authorization, writing no duplicate A16 event or manifest version,
never modifying the frozen database, and failing honestly
inaccessible on any unverifiable snapshot or manifest (§9) —
consistent in drafting.
One-operation-one-record logging with no payload content in any log
(§12) — consistent in drafting. B-INT-4 and all B-INT wiring left
open (§13, §16) — consistent in drafting. A16 status stated honestly
(§1) — consistent in drafting.

**Change report:** this v1_4 file was produced by copying the
identity-verified v1_3 base and applying only the archive-control
recovery completion and its connected references (title; the v1_4
version note; §8 class 9 — the complete thirteen-field manifest
schema with constraints and the exact initial-versus-seal version
contents, plus the latest-verified alignment; §9 — archive-creation
crash recovery for every boundary, the ordered idempotent
permanent-seal operation with every crash point, and invalid-manifest
handling; §11 — the verified-manifest and inaccessible-on-failure
cross-references; the §17 check lines; this block; the end line).
Every v1_3 schema field, lifecycle value, attribution rule,
transaction class, ordering rule, promotion rule, freeze boundary,
and A16 name is preserved untouched. v1_0 through v1_3 are preserved
unchanged as historical candidate evidence; **B7 v1_3 (ChatGPT PASS)
is not touched.**
Nothing existing was modified: Master V10, Defaults, cursorrules, the
Companion, the Map, the workflows and plan, accepted A7/A26 and their
receipts, the supplied accepted A16 candidate, the A15 package files,
all historical candidates, and every prior receipt remain
byte-identical at the pinned head `bbf4e900…`. Nothing was committed
or pushed; no receipt or accepted-source copy was created; no code,
live database, schema activation, migration, test, or Cursor
instruction was created; no implementation began.

**Self-audit (drafter's checks — not independent verification):**
mechanics only — no new meaning, no Ness question, no
reopened accepted content — consistent in drafting. The structural
pick justified as
mechanical under already-accepted requirements — consistent in
drafting. Thirteen
tables, two lifecycles, sealing/interruption/continuation, duplicate
protections, privacy precedence, audit vocabulary (including the two
A16-adopted names and only those), and startup recovery all carried
from the accepted design read on disk without alteration — consistent
in drafting. Fail-closed
direction everywhere; nothing reconstructed; nothing destroyed —
consistent in drafting. Exactly one file for B15; zero repository
modifications — consistent in drafting.

---

*End of
`NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md` —
`CANDIDATE — NOT ACCEPTED — NOT ADOPTED — NOT BUILT`, awaiting
ChatGPT's independent re-audit of this actual file and Ness's later
combined Bundle 5 acceptance. v1_0 through v1_3 are preserved
unchanged as historical candidate evidence. One small local SQLite file per
session, one shared timeline from one allocator, every accepted name
exactly as the Master wrote it:
every step whole or not at all, every restart honest, every payload
elsewhere, every blocker respected, every promotion exactly once,
every archive sealed and silent — and nothing, ever, deleted. B-INT-4
through B-INT-8 and all implementation remain open. Nothing existing
changed; nothing was implemented.*

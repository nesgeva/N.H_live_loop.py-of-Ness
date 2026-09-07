# NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md

## 0. STATUS BLOCK

**Status:** `CANDIDATE — NOT ACCEPTED — NOT ADOPTED — NOT
AUTHORITATIVE — NOT IMPLEMENTED.`
The Bundle 6 mechanical-design package: it translates the accepted
Bundle 6 policy package into concrete mechanical architecture for
exactly B12, B13, B14, B17, B18, B20, B21, B22, B-INT-2, and
B-INT-3, plus only the directly required Bundle 6 connections. It
changes no policy, asks Ness nothing, absorbs no other bundle's
unresolved work, redesigns nothing outside its scope, writes no code,
creates no store, ingests nothing, and marks nothing complete.
**Bundle 6 is not complete.** Bundle 5 remains paused.

**Date:** July 13, 2026.

**Version note (v1_4):** one final narrow correction of v1_3 only
(v1_3 SHA-256
`0df95db8567f8168356c3082026fdd1b76990443bff0835fe4dc5eb83406a33b`;
1,202 lines; 70,653 bytes — preserved unchanged, as are v1_0 through
v1_2), fixing five remaining issues: (1) the stale A12 sentence that
narrowed linking to the active listening segment is replaced — an
observation may carry the imported-item reference **only when
captured inside either a valid active playback segment or the valid
bounded post-playback reaction segment**, with paused and post-bound
observations unlinked (full-file sweep: no later summary narrows it
back); (2) B13's review-candidate duplicate identity is now
**independent of run, preservation timestamp, and synthesis
method/version** — five separated identities, with an identical
candidate under a newer synthesis appending a re-evaluation event to
the existing candidate, a materially different output becoming a new
linked candidate version, and one concurrent winner; (3) B12's §0B
wording now states the accepted B11 parent/child separation
precisely — one trigger-request parent with exactly one terminal
record, one activation-run child with its own single terminal
record, lifecycle transitions as canonical state events, and
duplicate-prevention never a second parent truth; (4) B22 work-item
identities are per type — message and media `capture_id`s, and
relationship work items under their own `relationship_operation_id`
with an endpoint+kind+provenance structural duplicate key,
direction-preserving for directional kinds and canonically ordered
for symmetric kinds, each relationship operation carrying its own
terminal record, with relationship creation/refusal/duplicate/failure
added to §0B; (5) the A12 reaction link commits **inside the
observation-capture transaction** as a child event — never a second
parent log — with any genuinely separate later relationship
operation requiring its own identity. Every correct v1_3 element is
preserved.

**Version note (v1_3):** one final narrow correction of v1_2 only
(v1_2 SHA-256
`43bd21ad6f2c7f9bba9f8120b2a3c2708223886e186acbcca735b7193e3ddbbc`;
1,063 lines; 62,040 bytes — preserved unchanged, as are v1_0 and
v1_1), fixing six remaining issues: (1) **the false B7 and A15
acceptance claims are corrected** — Bundle 5 is paused and no
accepted B7 or A15 package exists in the repository: B22 now states
that the **accepted A7 policy** requires Level-1 protection for keys
and credentials while the **B7 protected-execution and
sealed-storage machinery is an open Bundle 5 dependency**, with the
WhatsApp path disabled and non-runnable until B7 is accepted and
integrated; B-INT-3 records the A15 `acoustic_condition_notes`
amendment as **not accepted — conditional and unavailable** unless
Ness later accepts it; both added to §16; (2) B12's contradicting
"second trigger in the same window is skipped" wording is replaced by
the full **trigger-request record and lifecycle** (received →
held/coalesced/refused/admitted → terminal), durable held requests
discoverable after crashes, post-run checking of every held request,
coverage-verified terminal coalescing referencing the run's terminal
result, and B11 parent/child connection; (3) B14's base-record
duplicate identity is **detector-version-independent** (the
source-grounded fragment identity), with detector versions as event
provenance, re-evaluations appending to the existing record, one
concurrent winner, and no silent duplication or fusion; (4) B20
aliases are **presentation and label resolution only** — never
canonical membership, which resolves from the stable `thread_id`
before any alias is read; (5) A12 restores the accepted
immediate-post-playback period as a **bounded post-playback reaction
segment** beside the active playback segment — linking in either,
never during pause, never after the finite bound; (6) B22 recovery
runs on **independent message, media, and relationship work items**,
scanning all incomplete items so no attachment is lost behind a
committed parent message. Every correct v1_2 element is preserved.

**Version note (v1_2):** one narrow consistency correction of v1_1
only (v1_1 SHA-256
`4042376d6e6df48a04893672cd803fed6abbe78086d39fad9aa97402fd6345e4`;
945 lines; 54,834 bytes — preserved unchanged, as is v1_0), fixing
the six consequential remaining contradictions: (1) the immutable
base Creation Record now carries **only facts known at creation** —
confirmation, correction/supersession, and view memberships live
exclusively in append-only events with the derived view, and the
committed confirmation event is the **one canonical confirmation
truth**; (2) `thread_id` is **never** rewritten, aliased, or replaced
by B20 — B20's field vocabulary is `source_title` and
`display_label`, and genuine membership corrections belong to the
separate append-only membership/relationship mechanism; (3) source
times allow **zero reliable entries** with an explicit unknown state
and no invented timestamp — only `known_reliable` entries may be the
main date, at most one when candidates exist, zero when none is
reliable — and B22 now populates the typed `source_times`
representation (the removed `source_occurred_at` is gone); (4) Origin
relationships are **separate append-only `origin_relationship_record`
entries written only after both endpoints durably exist**, with their
own identity and structural duplicate key — no pre-ingest record is
rewritten and no dangling link can exist; (5) B12 treats **only the
same trigger identity as a duplicate** — a different trigger during
an active run receives a truthful durable disposition
(`coalesced_with_active_run` only under genuine coverage, else held
or refused fail-closed with reference and reason), and no unique
request disappears; (6) A12 linking is scoped to **active listening
segments** — pause suspends eligibility immediately, paused
observations are never linked, resume opens a new segment only under
a finite governed rule, and an invalid pause bound closes the window
fail-closed. Every v1_1 correction that was already right is
preserved.

**Version note (v1_1):** one correction pass on v1_0 only (v1_0
SHA-256
`0979798c6e34c8d13b1bd086f97345ad22b498e786f51babe66e913ec96f1794`;
672 lines; 38,354 bytes — preserved unchanged as historical candidate
provenance), fixing together all IMPORTANT audit issues: (1) the
accepted-dependency status corrected throughout — **B11 v1.4, the B9
retry architecture and retry-values v1.4, B24 v7, and B1 are accepted
packages consumed exactly, not open questions** (v1_0 wrongly trusted
the Map's stale open-status wording); the exact accepted B9 values
are carried and the accepted B11 contracts (batch registry and
selection, global ingestion claim, root-ownership binding, append
commit fence, parent/child operation identity, one-operation/one-log,
historical-coverage gate, recovery, fail-closed) are named as
consumed contracts; (2) B12 no longer touches
`.nh_queue_activation.json` as a mutable file — it stays the one-time
immutable activation boundary, with a separate append-only
scheduler/configuration record, separate run records, distinct
scheduled- and manual-trigger identities, collision-free activation,
and B9 background/nightly binding; (3) B13 duplicate prevention is
now cross-run stable — run identity, snapshot identity, synthesis
identity, and review-candidate identity separated, with the
screenshot-unavailable rule stated; (4) B14's base Creation Record is
immutable with append-only event records and a derived current-status
view, and route-B confirmation is a grounded, validated confirmation
proposal; (5) B20 gains the atomic compare-and-append head rule;
(6) B21's source time is a typed representation carrying kind,
provenance, reliability, and timezone state, allowing multiple
genuine source times with one identified main date; (7) B22 gains the
full key/plaintext protection lifecycle (L1 keys, protected staging,
sealed crash state, deterministic media identities, safe
message-plus-attachment recovery, no postponed privacy checks);
(8) B-INT-2's authorization recursion is removed via the
non-recursive protected control path, and query retry identity is
corrected to one parent operation with child attempt events; (9) the
A12 reaction window is a fully specified event-relative bounded
mechanic that fails closed until every bound is present. All correct
v1_0 content is preserved.

## 1. PLAIN MEANING

The Bundle 6 policy answers are accepted; this file builds the
machinery shapes those answers need — how the nightly pass is
switched on, how outside research stays quarantined, how Ness's
creations are kept provisional until he confirms them, how the
conversation label says only where words came from, how earlier
references work without the link Ness doesn't want, how a sealed
root's grouping is corrected beside it and never inside it, what the
next root schema separates, how the frozen WhatsApp archive would one
day enter without a single bypass, and how the live query router and
the behavioral loop connect to the one shared store. Every mechanism
follows the accepted meaning; none invents any.

## 2. GOVERNING AUTHORITY AND SOURCES

Authority order: (1)
`01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` (adopted June 29,
2026); (2) `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; (3)
`01_AUTHORITATIVE/cursorrules`; (4)
`01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`.

Repository baseline: `nesgeva/NH-GOVERNANCE`, branch `main`, starting
commit `6d4d27a2fd3e4894d3261d3c82b98619ba80d403`, verified as the
current head at task start; the delta from the prior pinned head
`bbf4e900…` verified as exactly the two byte-identical Bundle 6
acceptance files. Source identities verified on disk before drafting
(SHA-256 first-8): Master `2d9ed4c6`; Defaults `6cd09329`;
cursorrules `5050d088`; Companion `cdcc6134`; Map v1.6 `33af648d`;
eight-bundle plan `2d6483d1`; **accepted Bundle 6 policy package
`b37f965a` (515 lines, 26,884 bytes) and its closure record
`4b37668e`**; accepted A7 v1.1 `3deacafb` and its closure record
`f89fa7b1`; **accepted B11 v1.4 `baca06e5` (1,494 lines) and its
closure record; accepted B9 retry-state architecture `78c5d0b7` and
its closure record; accepted B9 retry-values wiring v1.4 `e8f4c3de`
and its closure record; accepted B24 v7 `7f5762e5` and its
package-complete record; the B1 acceptance record** — all read from
the repository's accepted-designs folder, which governs over the
Map's stale open-status wording. Read on disk for this design: the Map register entries
for B12, B13, B14, B17, B18, B20, B21, B22, B-INT-2, and B-INT-3 and
the component entries C-STORE (sealed-batch and B11 rules), C-7E
(intake envelope, `source_title` rule, held-pre-ingest boundary),
C-14 (live front door), C-CREATE, C-7GA (queue, activation boundary,
RC matrix), C-8 (research flow and rejected-bin rules), C-LMAC,
C-BOP, the §26 personal-learning loop, and C-7Q; the plan's Bundle 6
section including its mandatory boundaries and bundle-complete
condition; and the accepted Bundle 6 policy register in full.

## 3. SHARED MECHANICAL SPINE — BINDING ON EVERY OPERATION BELOW

Every operation designed in this file carries, as part of its own
contract: **(1) operation identity** — one stable operation id per
real operation, stated per item below; **(2) transaction boundary** —
each state change commits atomically with its own append-only record;
**(3) idempotency** — a stated deterministic key; a replay is
recognized, skipped, and recorded as a duplicate-prevention event;
**(4) duplicate prevention** — structural (unique keys), never
best-effort; **(5) retry** — failures are classified retryable or
terminal; retryable failures follow the **accepted B9 retry
architecture and accepted retry values, consumed exactly:**
technical failures get **3 total attempts (the original plus 2
retries)**; minimum waiting gaps are **10 seconds then 30 seconds**
for live paths and **1 minute then 3 minutes** for background/nightly
paths; elapsed-time maximums are **7 minutes live** and **15 minutes
background/nightly**; a bad/unsafe/unsupported proposal gets
**exactly 1 careful retry after its durable rejection record**; the
**attempt gate and the elapsed-time gate both apply and whichever
closes first stops retry**; early stop remains allowed where retry is
useless or unsafe; further continuation requires a **recorded real
change** (repetition alone is never a real change); terminal failures
halt honestly; **(6) crash recovery** — restart
scans committed state only, resumes from the last durable checkpoint,
reconstructs nothing, and each recovery action is itself one recorded
operation; **(7) partial-completion recovery** — per-item commits;
completed items stand, unfinished items resume; **(8) fail-closed** —
on any uncertainty the protective side wins: nothing enters memory,
nothing activates, nothing is claimed complete; **(9) §0B logging** —
**one real operation produces exactly one operational record**;
records include retrieval, use, evaluated-but-unused candidates,
acceptance, rejection, omission, and failure; **logging never
recursively generates more logging, and no log ever becomes evidence
for its own subject or adds evidence weight**; all records are
append-only and subject to §7Q access rules and §25 authorization;
**(10) no-bypass ingestion** — every root-producing path in this
bundle writes only through the §7E catalog envelope into the **B11
active writable batch**; the existing sealed 5,521-root batch is
never reopened, unsealed, or appended to; **the B11 active
writable-batch architecture is an accepted, PACKAGE_COMPLETE
dependency for its design scope, consumed exactly:** every root
write here runs the accepted B11 contracts — batch registry and
selection, the one global ingestion claim, the canonical pre-commit
root-ownership binding (WB1: atomic ownership generation +
reservation + root-ID commit), the per-generation **append commit
fence** (WB2 verifies the durable `commit_fenced` generation and the
matching root-ownership entry immediately before committing — the
commit point), the parent/child operation identity with **exactly one
terminal parent operational record** (WB3; child logs are never
second parent logs), the one-operation/one-log separation of
canonical state records from operational logs, the
**historical-coverage gate** (§8.2B coverage-before-writes,
fail-closed), B11's recovery rows, and its fail-closed refusals —
nothing here redesigns, summarizes, or reopens any of it; **(11) privacy precedence** — §7Q
before §7R on every retrieval; held and sealed material boundaries
per C-7E/C-TSC are consumed unchanged.

## 4. B12 — NIGHTLY-BATCH ACTIVATION

**Purpose and boundary:** design the activation source and lifecycle
for the nightly reading batch (C-7GA) — how the already-specified
queue machinery is switched on for a run — **without silently
activating historical material**. The queue, claims, RC-1…RC-8
recovery, and idempotency are C-7GA's settled machinery, consumed
unchanged; B12 adds only the activation seam around
`.nh_queue_activation.json` (the activation boundary the Map already
names).

**The one-time activation boundary is preserved untouched:**
`.nh_queue_activation.json` is Master's **one-time queue activation
boundary, written once** to prevent silent historical backfill — it
is **never** turned into a mutable nightly enable/disable file,
never rewritten, and B12 only ever reads it as the standing
precondition (no runs at all unless the one-time boundary exists and
validates).

**Separate records:** (1) an **append-only scheduler/configuration
record** — Ness's approved schedule and any change to it, each a new
versioned entry with his establishing words reference (the schedule
value is Ness's setting, not a design constant; no numeric chosen
here); (2) **separate per-run records** — one per activation run,
never inside the boundary file or the configuration record.

**Trigger identities:** a **scheduled trigger's** identity derives
deterministically from the active scheduler-configuration version
plus the scheduled window identity; a **manual trigger's** identity
derives from the durable manual request/event reference (Ness's
recorded request). **Collision, duplication, and disposition rules,
structurally:** all activations serialize on one run admission —
exactly one run may hold the admission at a time, so **no second
simultaneous run ever starts**. **Only the same trigger identity is a
duplicate:** the same scheduled window can never start twice, and the
same manual request reference can never start two runs — those
replays are recognized, skipped, and recorded as
duplicate-prevention. **A different trigger arriving while a run is
active is never called a duplicate and never silently disappears** —
it receives a truthful durable disposition record carrying the
active-run reference and the reason: it is linked
`coalesced_with_active_run` **only when the active run genuinely
covers the same requested queue work** (same pending-job coverage);
otherwise it is **held** for admission after the active run, or
**refused fail-closed** where holding is not valid — in every case
recorded, in no case lost.

**Retry binding:** every run binds to the **accepted B9
background/nightly retry configuration exactly** — gaps 1 minute
then 3 minutes, 3 total attempts, 15-minute elapsed maximum,
whichever gate closes first.

**No-silent-historical-activation rule, structurally:** an activation
run processes only jobs already enqueued by the normal
`append_root()` → enqueue path; **activation never scans stores,
never enqueues, never bulk-creates jobs for historical roots, and
never re-enqueues terminal jobs.** Bringing any historical material
into the queue would be its own separately authorized operation with
its own record, not an activation side effect.

**Operation identity:** `activation_run_id` [proposed], per the
trigger identities above — so the same window or request cannot start
twice.
**Lifecycle:** `triggered` → `running` → `completed` |
`halted_failed` | `halted_disabled`. **Records (append-only):**
the scheduler-configuration/version record (§ above — who/when/basis
per version; the one-time activation boundary itself is never a
mutable record); one activation-run
record per run (trigger source and identity, jobs processed
count, outcome); disposition records for triggers arriving during an
active run (`coalesced_with_active_run` | held | refused, with the
active-run reference and reason); duplicate-prevention record on a
same-identity replay.
**Trigger-request records and lifecycle:** every received trigger —
scheduled or manual — writes its **own durable trigger-request
record** at receipt (identity, source, time), with lifecycle
`received` → `held` | `coalesced_with_active_run` | `refused` |
`admitted` → terminal outcome. **Only the same trigger identity is a
duplicate** — the same scheduled-window identity or the same
manual-request identity cannot start twice; **a distinct manual
trigger inside a scheduled window is never automatically skipped**.
Held requests are durable and **remain discoverable after a crash**
(no held request exists only in memory); after the active run ends,
recovery or normal admission **checks every held request** and
either admits it, truthfully coalesces it **using the completed
run's exact coverage** (`coalesced_with_active_run` is terminal only
when the active run truly covered that exact requested work, and the
disposition references the active run's terminal result), or refuses
it with a durable reason. **No unique request disappears; no second
simultaneous run starts.** Trigger-request identity and
activation-run identity remain **separate and connected** — the
request record is the parent context reference, the run is its own
operation — under the accepted B11 parent/child and
one-operation/one-log rules.
**Retry/crash:** a crash mid-run loses nothing — job progress is
C-7GA's own claim/checkpoint machinery; on restart the run record is
closed honestly (`halted_failed` with the committed progress) and the
next window proceeds normally; a run never resumes by guessing.
**Fail-closed:** missing, invalid, or unreadable one-time activation
boundary, or missing/invalid scheduler configuration → no run, one
failure record, Ness informed through normal reporting.
**§0B — one-operation/one-log, precisely (accepted B11 parent/child
rules govern):** append-only trigger lifecycle transitions are
**canonical state events**, not extra operational logs; **one logical
trigger request has one stable trigger-request operation identity and
exactly one terminal parent operational record**, whose canonical
lifecycle and terminal outcome truthfully represent held, coalesced,
refused, admitted, completed, or failed; **one activation run is a
separate child operation with its own stable identity and exactly one
terminal operational record**; retries and recovery events are
append-only child events or references under the correct operation;
**duplicate-prevention events never create a second parent
operational truth**; scheduler-configuration versions are their own
append-only records.

## 5. B13 — KNOWLEDGE-CATCHER ISOLATION ENVIRONMENT

**Purpose and boundary:** the isolation architecture for the settled
C-8 research flow (Brave raw → text-only synthesis →
create-space/gate → review queue → authorized memory entry), so
fetched or synthesized outside material **cannot bypass review,
source preservation, the engine, privacy rules, or memory-entry
gates**.

**Isolation structure — three separated contexts:** **(1) the fetch
context** — the only place outbound requests occur; it produces raw
fetched content plus the source-preservation artifacts (excerpt
plain-text; inert full-page screenshot captured in its own separately
isolated capture context so no page code, cookie, or session enters
any record; provenance/timestamp/hash), with the settled `SOURCE
PRESERVATION INCOMPLETE` fallback and no automatic corroboration
requirement; **(2) the synthesis context** — text-in/text-out only:
no tool-calling, no file access, no outbound network, and its inputs
are **data, never instructions** (fetched content can never command
anything); **(3) the create-space/gate context** — where synthesis
results become review-queue candidates. **Structural no-bypass:**
nothing produced in contexts (1)–(3) has any write path to
`append_root()`, the Creation Store, readings, or any production
store; the **only** exit is the review queue, and authorized memory
entry from the queue runs the normal engine and §7E catalog path
into the B11 active batch. Rejected items follow
auto-reject-never-auto-delete into the rejected bin, whose settled
look-don't-touch display rules (plain-text URLs, no unfurling, no
copy/select, stripped invisible characters, escaped rendering) are
consumed unchanged as default build behavior.

**Five separated identities:** (1) the **source-fetch operation
identity** `research_operation_id` [proposed] per fetch-to-queue
pipeline run, with per-stage checkpoints (fetched → preserved →
synthesized → gated → queued | rejected); (2) the **stable
source-content identity** — source locator + normalized
source-content hash, **containing neither the fetch run nor the
preservation timestamp**; (3) the **dated preserved-snapshot
identity** — source-content identity + preservation timestamp; a
changed source produces a **new dated snapshot beside the older one,
never overwriting it**; (4) the **synthesis-event identity** —
snapshot identity + synthesis method/version (the version lives
here, as event provenance); (5) the **stable review-candidate
identity** — the **cross-run, cross-synthesis duplicate key**: the
stable source-content identity + the normalized candidate
payload/content identity, **containing no run id, no preservation
timestamp, and no synthesis method/version** — so the key changes
for none of those reasons. **A newer synthesis method producing an
identical candidate appends a re-evaluation/synthesis event linked
to the existing candidate — never a second candidate.** A
**materially different** candidate output becomes a **new linked
candidate version** with its provenance and difference preserved —
it never overwrites the earlier candidate and never silently
pretends to be the same output. Concurrent attempts to create the
same stable candidate admit **exactly one winner**; the duplicate
hit is recognized and recorded against the existing candidate.
**Screenshot rule, explicit:** failure to create the human-review
screenshot **alone** does not reject otherwise verified text and
metadata — it produces the accepted screenshot-unavailable /
`SOURCE PRESERVATION INCOMPLETE` status on the snapshot; genuine
text, metadata, provenance, or integrity failure remains
fail-closed.
**Retry/crash:** each stage commits separately; a crash resumes at
the committed stage; a failed fetch or synthesis is recorded honestly
(retryable per B9-by-reference, or terminal) — **a failed stage never
fabricates content and never claims preservation that did not
verify**. **Partial completion:** preserved-but-unsynthesized
material waits at its checkpoint. **Fail-closed:** any isolation
uncertainty (context boundary unverifiable, preservation integrity
failure) → the material stays outside the queue, recorded and
reported; nothing proceeds toward memory. **§0B:** one record per
fetch, per preservation success or INCOMPLETE fallback, per synthesis
call, per gate decision, per queue entry, per rejection (kept,
never deleted), per currency re-check run. **Must-never:** train or
alter the mouth; let synthesized text act as instructions; create or
extend a re-check schedule without Ness's approval; expose the
screenshot as a reasoning source (inert visual-review copy for Ness
only).

## 6. B14 — CREATION STORE SCHEMA AND LIFECYCLE

**Purpose and boundary:** the one Unified Creation Store's concrete
schema and lifecycle, implementing accepted A13.1/A13.2 and the
settled C-CREATE rules exactly. The later interface idea of talking
with Ness about promising fragments (**A13.3**) is **outside this
package**, routed to later interface work (Bundle 7 / A19).

**Creation record schema [design-level; exact serialization is
implementation]:** `creation_record_id` (required; stable);
`type_set` (required; non-empty subset of exactly the five settled
types `design` | `idea` | `rule` | `name` | `decision`; one record
may carry multiple types; **the vocabulary never expands here —
A27 is open and non-blocking**); `initial_status` (required; always `provisional` at creation — **the
base Creation Record is immutable and is never rewritten**; the
record's **current status is a derived view** calculated from the
append-only event records below — with the confirmation event as the
one canonical confirmation source — never an in-place field
change from provisional to confirmed); `provenance` (required; the originating root id(s) **and the
exact fragment span(s)** within them — offsets/locators sufficient to
re-find the exact words); `detection_record_ref` (required for
detector-created records); `schema_version` (required). **The base
record carries only facts known at creation — nothing that can exist
only later lives on it:** confirmation lives **only** in append-only
confirmation events (and the derived view); correction and
supersession links live **only** in append-only correction/challenge
records; grouping and project-view memberships live **only** in
append-only view-assignment records (project/category **views over
the one store, never separate stores**). **The derived current-status
view** calculates both current confirmation status and current view
memberships from those events. **One canonical confirmation source:**
the committed confirmation event is the single source of a
creation's confirmed status — no separate, potentially contradictory
status-event truth exists beside it; other status-relevant events
(challenges, corrections) link to it, never compete with it.

**Broad provisional detection (A13.1), mechanically:** the §7G
creation-aware mode (settled live-chat path only; **A28 open,
non-blocking**) proposes provisional records **even from small
fragments, partial thoughts, short phrases, and unfinished
sections**; each detection writes a detection record
(detector/method version, source root, fragment span, basis). **The
base record's structural duplicate identity is
detector-version-independent:** it is the **source-grounded fragment
identity** — source root id + exact fragment span — and it **does not
change merely because the detector or method version changes**;
detector/method version is **provenance on the append-only detection
or re-evaluation event, never part of the base-record duplicate
identity**. Re-running a newer detector against the same exact
candidate **appends a new detection/re-evaluation event linked to the
existing base record — never a second base record**; concurrent
attempts to create the same base record admit **exactly one winner**
(compare-and-create on the fragment identity); a genuinely distinct
creation candidate receives a separate base record **only when its
distinct source-grounded fragment identity is recorded**; detector
disagreement or changed segmentation becomes a **linked
proposal/re-evaluation event, never silent duplication and never
silent fusion** — exact original fragments and provenance stay
preserved, and one record still carries multiple accepted types
exactly as designed. Broad capture never
confirms anything.

**Append-only event records around the immutable base:** detection
records, confirmation records, **confirmation-proposal records**,
challenge records, correction records (new linked records, never
rewrites), relationship-proposal records, and **view-assignment
records** —
each append-only, each one transaction with one operational record.
**The derived current-status view** reads exactly these events: a
creation is `confirmed` only where a committed confirmation record
exists — **the confirmation event is the one canonical confirmation
truth; no parallel status event can contradict it** — and everything
else derives as `provisional`; current view memberships derive from
the view-assignment records.

**The two confirmation routes, structurally — and no others:**
route (a) **Ness's explicit confirmation** (his words referenced) —
recorded directly as the confirmation record; route (b) **later
words/actions clearly demonstrating adoption** — mechanically:
detection of possible later adoption creates a **grounded
confirmation proposal** that must cite the **exact later roots or
recorded actions** and the **exact original creation fragments** it
claims are adopted, and must pass the applicable **accepted
validation/grounding boundary (accepted B24, consumed by reference)**
before a confirmation record may be committed from it; **unclear or
competing evidence leaves the creation provisional** (the proposal
stays a proposal, recorded). **No other pathway to `confirmed`
exists in the schema:** a mouth assertion, repeated retrieval,
repeated use, elapsed time, or model confidence can never confirm —
structurally, nothing in the store counts uses and no counter,
score, or confidence feeds any status event. Ambiguity remains
`provisional`. A record may remain `provisional` forever; nothing is
destroyed.

**Ideas-in-progress view and wider influence (A13.2), mechanically:**
the ideas-in-progress view is a view over the store filtered to
`provisional` (plus its history) — not a second store. A provisional
record may enter wider retrieval, reasoning, answers, and the
Computed View **only through operations whose own §0B operation
record carries a `provisional_material_used` entry** (record id +
status at use time) — so every influence is **visible in the output
context as provisional and traceable in the operation record, never
silent**. This is exactly the plan's mandatory
no-silent-influence boundary satisfied by the accepted policy's
carried-status rule. **No consumer may re-label a provisional record
as fact, adopted rule, final decision, or settled creation.**
**Fragment relationships:** possible relationships among fragments
are recorded as relationship-proposal records (linked, append-only);
a larger adopted creation is a **new** record whose provenance
references all source fragments — the originals are never silently
fused, edited, or absorbed.

**Operations:** record creation, confirmation, correction/challenge,
relationship proposal, view assignment, influence use — each one
transaction with one record; crash recovery resumes from committed
records; partial completion per record; fail-closed: an unverifiable
status reads as `provisional`. **§0B:** one record per detection,
confirmation (with route and basis), correction, proposal, view
assignment, and provisional-material use.

## 7. B17 — LIVE-CONVERSATION PROVENANCE-LABEL FORMAT

**Purpose and boundary:** the concrete format of the recorded
live-conversation provenance label, after accepted A33 — provenance
only, never meaning.

**Format [proposed — a mechanical naming choice implementing the
accepted meaning, subject to normal audit]:** a **structured typed
label**, not one overloaded string: `provenance_label` =
`{ label_type: "live_conversation", label_version: "v1" }` carried on
the pre-ingest record and into the root's provenance metadata,
alongside the already-required source-carried fields:
`speaker_of_record` (from the source stream — **never guessed
later**), and the output flag that marks N.H's own prior output as
N.H's output. The illustrative string `live:ness_nh_conversation` is
**not adopted**; if a flat serialization is ever needed, it derives
mechanically from the structured fields. **What the label asserts:**
only that the material came from a recorded live conversation between
Ness and N.H, with **two source-known speakers**; **Ness's words are
Ness's; N.H's earlier output is N.H's earlier output and is not fact
merely because N.H said it**. **What the label never asserts:** the
conversation's topic, meaning, truth, or importance — the topical
subject is earned later by the Meaning Engine; the legacy `subject`
field is untouched (B21). **Operations:** label assignment happens
inside the §7E capture transaction (no separate operation, no
separate log — one capture, one record, the label inside it);
idempotent with the capture; verified by the §7E envelope check;
fail-closed: a live-front-door capture missing the label fails the
envelope and follows the capture-error path, never silent entry.

## 8. B18 — EARLIER-REFERENCE MECHANICS

**Purpose and boundary:** the internal named-topic / spec / message /
earlier-context reference mechanism, implementing accepted A32:
**there is no visible clickable point-back link in the target
design** — Ness decided the link behavior does not work for him —
and **no visible topic-type tag**; reliable earlier context is still
used naturally and silently. The accepted policy package's §5
supersession note governs: the older settled-§13 visible point-back
presentation and the explored-§14 clickable presentation are
**superseded as visible surfaces, openly, with their wording
preserved as history** — this file designs no visible link surface
and explicitly does not carry one forward. Master V10 and the Map
still contain the older wording; integration of the supersession is
Ness's later version-safe process, not this file's act.

**Detection, mechanically:** the `re_reads` mechanism (§6B) runs
silently on each live turn: it proposes **reference records** —
`reference_id` [proposed]; source turn/capture ref; candidate
referenced object(s) (root/thread/creation/spec) each with a
confidence representation and a stated basis (name match, quoted
fragment, structural link); detector version. **Reliable versus
uncertain, structurally:** a reference participates in natural
earlier-context use **only** when it meets the consuming mode's
declared reliability condition (representation governed by the
mode's Tier-1/Tier-2 declarations; **no numeric threshold chosen
here**); it then feeds §7F retrieval as provenance-bearing context
through the normal channels — **used naturally, surfaced to Ness as
nothing** (no link, no tag, no navigation UI). **Uncertain references
are never fabricated**: an unresolved candidate is recorded as
unresolved, never used as if resolved, never surfaced as a claim,
and never invented to satisfy a turn. **Operations:** one detection
record per turn evaluation (including evaluated-but-unused
candidates); idempotency key = turn capture id + detector version;
duplicates recognized; crash recovery re-evaluates only turns without
committed detection records; fail-closed: on detector failure the
turn simply proceeds without earlier-reference context — never with
guessed context. **§0B:** one record per evaluation, listing used and
unused candidates with their reliability outcomes.

## 9. B20 — `source_title` ALIAS/CORRECTION LAYER

**Purpose and boundary:** later clarification of a sealed root's
grouping, recorded **beside** the root — **a sealed root or old
source record is never rewritten**.

**Alias record schema [design-level]:** `alias_record_id` (required);
`target_ref` (required — root id and/or `capture_id`);
`field` (required; controlled: `source_title` | `display_label`
[the human-readable label from B21's schema] — **and never
`thread_id`: the stable, non-semantic grouping identity is never
rewritten, aliased, or replaced by B20**; if actual thread membership
or grouping identity needs correction, that is a separate append-only
membership/relationship correction through its correct owner — the
grouping-membership mechanism, not an alias pretending the stable
`thread_id` changed);
`original_value_ref` (required — the sealed value, by reference,
never copied out of context and never altered); `alias_value`
(required — the corrected or clarified grouping value, obeying the
settled `source_title` rules: a machine-generated topic/summary/
semantic label may **never** become a `source_title` alias);
`basis` (required — Ness's statement reference or reliable
source-carried evidence reference); `version` (required; monotonic
per target+field); `predecessor_ref` (**required on every successor
version — the previous committed alias version's identity; absent
only on version 1**); `schema_version` (required). Append-only; one
version chain per target+field. **Atomic compare-and-append head
rule:** exactly **one current head** exists per target+field; a
write succeeds **only if its declared `predecessor_ref` is still the
current head** at commit time — one compare-and-append, so
concurrent or stale writes can neither fork the chain nor silently
skip versions; the loser of a concurrent write is refused and
recorded, and may retry against the new head as a fresh version. **A
detected fork or stale predecessor fails closed and is recorded**;
until resolved, consumers fall back to the sealed original. Every
prior version stays preserved and readable.

**Consumption — presentation and label resolution only:**
`source_title` and `display_label` aliases affect **human-readable
presentation, source-label display, and explicitly label-based
filtering only** — consulted **with provenance** (the reading shows
it used an alias and which version). **They never determine, replace,
or alter canonical `thread_id`, and canonical thread membership never
changes because an alias changed**; thread-membership consumers may
read aliases **only for presentation, after canonical membership has
already been resolved** from the stable identity; actual membership
correction uses the separately owned append-only
membership/relationship mechanism. The sealed root's
own bytes remain the unaltered original everywhere. **Operations:**
one alias-write transaction per version with its record; idempotency
key = target + field + version + predecessor; duplicate versions
structurally impossible (the compare-and-append admits one winner);
crash recovery: the last committed head stands;
fail-closed: an unverifiable or forked chain reads as no-alias (the
sealed original governs) with the failure recorded. **§0B:** one record per alias write and per
alias-consulting **display-label or source-title presentation
resolution** — never a grouping decision.

## 10. B21 — FUTURE ROOT SCHEMA AND PRE-INGEST SCHEMAS

**Purpose and boundary:** register and design the **next** root
`schema_version` and the exact Bundle 6 pre-ingest field shapes —
**design-level only; no field is renamed, added, or activated on any
live store by this file**, and activation is implementation-gated
behind B11 and Ness's authorization.

**The next root schema [proposed `root_schema_v2`, design-level]:**
- **Stable grouping identity separate from display:** a stable,
  non-semantic `thread_id` grouping key, distinct from an optional
  human-readable `display_label` — the label may change through B20;
  the key never carries meaning.
- **The legacy `subject` field is not reused:** v1 `subject` remains
  exactly the legacy provenance-batch tag
  (`seed:conversations_000/001/002`); **no new semantic topic value
  ever enters it**. A future semantic subject/topic field would be a
  **new** field whose content is earned by the Meaning Engine — this
  file registers the structural separation and deliberately does
  **not** design a semantic field.
- **The three A3.3 time families, kept separately — with a typed
  source-time representation:** the original source time is **not**
  one ambiguous field; it is `source_times` — a set of **zero or
  more** typed source-time entries (**zero reliable source times is
  legal; no timestamp is ever invented merely to satisfy the
  schema**; an Origin with no known source time carries an explicit
  unknown-time state instead of a fake entry), each entry carrying at
  minimum:
  `timestamp_value`; `source_time_kind` (controlled: `created` |
  `captured` | `sent` | `recorded` | `occurred`);
  `provenance_ref` (which source fact supplied it);
  `reliability_status` (`known_reliable` | `known_unreliable` |
  `unknown` — **an unknown value stays honestly unknown and is never
  substituted from import or record time**); and `timezone_state`
  (the zone, or explicit timezone-unknown) where applicable. **A
  source may genuinely provide more than one source time** (e.g.,
  both a recording time and a sending time) — all genuine entries are
  kept. **The main real-life date rule:** **only a `known_reliable`
  entry may be marked `is_main_real_life_date`**; when reliable
  candidates exist, **at most one** is marked (the reliably-known
  original time per accepted A3.3); when **no** source time is
  reliably known, **there is zero main source date** — the Origin
  honestly has none, and no unknown or unreliable entry is ever
  promoted to fill the gap — **without deleting
  or degrading the other entries**. Separately: `imported_at` (when N.H
  received/imported it) and `record_created_at` (when N.H created its
  own record). Import and
  record times never replace any source time.
- **Mixed-media Origins (A3.2) — append-only relationship records,
  never in-record links:** every real source item remains its own
  Origin root, committing **independently** through the normal
  B11/§7E path. A directly recorded relationship (attachment-of,
  transcript-of, same-capture-session) becomes a **separate
  append-only `origin_relationship_record`** [proposed] — source
  origin identity + target origin identity + relationship kind +
  source-provenance reference — written **only after both endpoint
  identities durably exist**; no Origin or pre-ingest record is ever
  rewritten to gain a link. The relationship operation has its own
  stable identity and a **structural duplicate key** (source +
  target + kind), so replays cannot duplicate; a crash before both
  endpoints exist creates **no** relationship; recovery may append
  the relationship later **only after both exact endpoints are
  verified**. Source-recorded relationships are facts;
  non-source-recorded proposals stay with the Connection
  Capability's accepted routes (**§24 / B-INT-8, Bundle 5 — paused;
  cited dependency, left open**); B21 fabricates no relationships —
  **connection, never merger**.
- **Pre-ingest field shapes:** the settled seven-element intake
  envelope carried unchanged, plus the fields above flowing through
  pre-ingest into the future schema; `preingest`-side names align
  with the accepted §7E vocabulary (`capture_id`, source metadata
  preserved without reinterpretation).

**Operations:** schema versioning itself is the operation — a new
`schema_version` value with its design record; nothing migrates here
(migration is implementation, later, gated); duplicate prevention by
version uniqueness; fail-closed: a root that cannot satisfy its
declared schema version fails the envelope and never enters
silently.

## 11. B22 — DEFERRED WHATSAPP INGEST PATH (DESIGN-ONLY; ARCHIVE FROZEN)

**Purpose and boundary:** the deferred mechanics only. **The
encrypted WhatsApp archive remains frozen; no decryption and no
ingest occurs or is authorized by this file.** The design exists so
that when Ness later authorizes the path, it runs with no bypass.

**The staged pipeline (each stage its own operation class):**
1. **Decrypt stage** — key extraction and archive decryption (the
   settled `wa-crypt-tools` reference names the tool family; no
   command, script, or key handling is written here). Output: the
   readable message database and media set, held entirely outside
   memory. Operation identity per decrypt run; integrity-verified
   output; fail-closed on any integrity doubt.
2. **SQLite front door** — per-message extraction into the §7E
   intake envelope: each message is its **own Origin**; each media
   item is its **own Origin**, connected to its message by the
   directly-recorded attachment relationship written as a separate
   append-only `origin_relationship_record` (B21) **only after both
   endpoint identities durably exist**; source timestamps populate
   the **typed `source_times` representation (B21)** — each entry
   with its correct `source_time_kind` (e.g., `sent` for the message
   send time; `recorded`/`created` for media where the source
   provides it), its `provenance_ref` (the exact WhatsApp source
   field), its `timezone_state`, and its `reliability_status`; only
   `known_reliable` entries may carry the main date, and a message or
   media item with no reliable source time carries the explicit
   unknown-time state with **zero** main date; sender
   identity **source-carried, never guessed**; unknown values stay
   unknown; `capture_id` derived deterministically from the stable
   WhatsApp message identity so re-runs cannot duplicate.
3. **Image front door where applicable** (C-9A rules consumed
   unchanged): metadata → plain description → context-meaning
   **proposal**; machine description never treated as fact without
   Ness's confirmation.
4. **Ordinary privacy/third-party handling** — the accepted A7
   package applies as it stands: source and speaker separation,
   uncertainty labeling, privacy and compartment rules,
   authenticated-private versus external-restricted use, simulation
   approval, and person/group stricter-only controls; **per accepted
   A30, there is no automatic age-only child-data gate** — material
   involving a child or minor receives the same real, ordinary
   protections as everyone, with no weakening of any privacy,
   evidence, uncertainty, external-use, harm, legality, or
   simulation rule.
5. **Ingest only through the engine and §7E catalog path** into the
   **B11 active writable batch** — never a direct store write, never
   the sealed batch, never a side channel; §7Q exclusion precedence
   applies at capture exactly as C-7E specifies.

**Key and plaintext protection lifecycle (binding on every stage):**
**the accepted A7 policy requires Level-1 protection for keys and
credentials** — cryptographic keys and credentials live **only inside
the Level-1 protected execution boundary. Separately and honestly:
the exact B7 protected-execution and sealed-storage machinery
(protected execution boundary mechanics, sealed protected storage,
derivative discovery, mixed-content separation, verification) is an
OPEN Bundle 5 dependency — Bundle 5 is paused, and no accepted B7
package exists in the repository.** B22 states the safety
requirements it must consume, and **the WhatsApp path remains
disabled and non-runnable until the required B7 mechanics are
accepted and later integrated through the version-safe process** —
this file does not design or close B7. The requirements:
**raw keys never enter ordinary logs, prompts, memory,
screenshots, error text, or model context** — records reference them
by opaque identity only. Decrypted plaintext exists **only in an
operation-scoped protected staging area** unavailable to ordinary
retrieval, reasoning, and model context; **no untracked temporary
files, previews, copies, exports, caches, or backups** — every
staging artifact is registered to the operation and accounted for at
close. **Exact access authorization and purpose checks run before
each stage begins** — no privacy check is ever postponed until after
sensitive plaintext has already entered an unprotected place (the
§7Q/A7 evaluation happens at or before the protected staging
boundary, never downstream of an exposure). **Crash recovery seals
and records the interrupted staging state** — the staging area is
closed against access and its state recorded; nothing is exposed and
nothing is guessed; recovery resumes only through the same protected
path. **Any durable decrypted derivative** that must persist falls
under N.H's ordinary preservation and visibility laws honestly: it is
recorded, protected at the correct level, and never silently
retained.

**Media and relationship safety:** media capture identities are
**deterministic** (derived from the stable WhatsApp media identity,
so re-runs cannot duplicate); **message-plus-attachment recovery is
safe by ordering** — the attachment relationship is a separate
append-only `origin_relationship_record` (B21) committed **only after
both Origins' identities durably exist**, under its own operation
identity and structural duplicate key, so a crash or failed media
extraction can never
create a broken, dangling, or misleading link: a message whose media
failed extraction stands alone with an honest
media-extraction-failure record, and recovery appends the
relationship later only after both exact endpoints verify; no Origin
or pre-ingest record is ever rewritten.

**Recovery contract — independent durable work items:** **each
message, each media item, and each attachment relationship is its own
durable work item with its own stable identity and checkpoint** —
message completion never implies media completion, and no unit is
ever marked complete as a whole by a crash. **Recovery scans ALL
incomplete work items**, not only messages lacking a committed
pre-ingest record: a committed message Origin whose media Origin is
missing → recovery resumes **that exact media extraction operation**;
both Origins committed but the relationship record missing →
recovery verifies both exact endpoints and **appends the relationship
idempotently**; media extraction terminally failed → the message
stands valid with an honest media-failure record and **no
relationship**, and **no attachment is silently lost merely because
its parent message committed first**. **Work-item identities, per type:** **message work items** use their
deterministic message `capture_id`; **media work items** use their
deterministic media `capture_id`; **relationship work items** use
their own stable `relationship_operation_id` [proposed] with a
**structural duplicate key of the two exact endpoint identities +
relationship kind + source-provenance identity** — **directional
relationship kinds preserve endpoint direction in the key; symmetric
kinds use canonical endpoint ordering so reversing the endpoints
cannot create a duplicate**. Retries reuse the same
applicable work-item identity under the **accepted B9
background/nightly values** (1 minute
then 3 minutes, 3 total attempts, 15-minute elapsed maximum), and
**recovery looks up that exact identity before doing any work**; a
relationship operation receives its **own one-operation/one-log
terminal record**; duplicate
prevention structural;
terminal failures halt the work item with
an honest record; fail-closed everywhere — a message that cannot
satisfy the envelope is a capture-error, never a silent drop and
never a forced guess; no Origin or pre-ingest record is ever
rewritten. **No decryption or ingest is performed by this
design file.** **§0B:** one record per decrypt run, per
extracted message capture, per media capture, **per relationship
creation, per relationship refusal, per relationship
duplicate-prevention, per relationship failure**, per privacy decision
reference, per promotion — and one honest record for the frozen
status itself whenever the path is invoked without authorization
(refused, recorded).

## 12. B-INT-2 — LMAC QUERY CONTRACTS

**Purpose and boundary:** the exact query contract each queryable
component exposes to LMAC (§26.10): **§7F, §7R, §7D, §7L, §7K, §7J,
§7Q, §7P, §22**. LMAC remains exactly what C-LMAC settles: a
**stateless router** — owns no data, caches nothing between queries,
filters nothing, summarizes nothing, adds no rules, decides nothing.

**The uniform contract shape (each component's instance stated
below):** request = { requesting function identity; declared purpose
(from the settled purpose vocabulary where §7R is involved); target
references; mode/configuration version where applicable } →
authorization obtained through the non-recursive control path below
(the correct §7Q authorization kind for the purpose — internal-use
vs visible-output — and the §7P authority check), then
routes → response = the component's own current live result, whole,
with its own provenance.

**The non-recursive protected control path (no authorization
recursion):** §7Q and §7P are themselves query targets, so LMAC does
**not** "apply §7Q and §7P before" querying §7Q or §7P — that would
be a circular query. Instead: **an authorization query to §7Q is
itself the step that obtains the §7Q decision**, and **an authority
query to §7P is itself the step that obtains the §7P decision** —
each runs on a protected control path that carries **only the
minimum metadata needed to make that decision** (requester identity,
purpose, target references — never protected content), and **no
protected content is released before the result returns**.
**Ordinary component queries** (§7F/§7R/§7D/§7L/§7K/§7J/§22) then
apply the obtained §7Q and §7P results in the settled order before
routing. The control path **bypasses nothing** — identity, access,
purpose, and logging rules all apply to control-path queries
themselves; they are the decision-obtaining step, not consumers of a
prior decision. Per component: **§7F** — context retrieval
(target + mode → labeled two-channel context package; §7Q
internal-use before any root returns); **§7R** — relevance evaluation
(Tier-1 mode id/version + purpose + candidates → gate results +
graded dimensions with provenance); **§7D** — current state read
(node refs → recorded state with currentness, never rewritten);
**§7L** — Person-Box read (box ref → linked objects under their
actual certainty; PBR reads for SACL run through this path);
**§7K** — story-layer read (perspective-owned tellings, clash
preserved); **§7J** — clash reads (records + Ness-response events);
**§7Q** — the authorization queries themselves (purpose + material →
eligibility decision, recorded by §7Q); **§7P** — authority checks;
**§22** — current wellbeing tier for response calculation only
(never identity or access evidence — the C-WIS-SEP separation binds).
**Behavioral context rule (settled, carried):** **LMAC never queries
the BOP or OOP processors directly** — what it reaches is the
**BOP-produced observation roots and pattern readings already in the
shared store**, through §7F/§7R like any other material; **OOP is not
a query target at all** (it writes outcome roots through §7E → §7G).

**Operations and query retry identity:** **one logical query has one
stable `query_operation_id`** [proposed]; one routing record per
logical query in the **shared** living-memory operational log (LMAC
owns no store): requesting
function, target component, purpose, which §7Q authorization kind was
applied, outcome reference. **Transport retries reuse the same
`query_operation_id`** — a retry never creates a second independent
operational truth record; retry-attempt details are append-only
**child events or references under the one parent operation**, and
**exactly one terminal query outcome is recorded per logical query**;
a genuinely new later query (new intent, new context) receives a new
operation identity.
Crash recovery: none needed beyond the component's own (the router is
stateless; an interrupted parent record's terminal outcome is
completed idempotently by identity);
fail-closed: an unauthorized or unrecognized purpose is refused and
recorded — LMAC never guesses a purpose mapping.

## 13. B-INT-3 — BOP/OOP SHARED-STORE CATALOG WIRING

**Purpose and boundary:** confirm and concretize how BOP observation
roots and OOP `outcome_observation` roots enter the one shared store
— **exactly** via §7E → `append_root()` (B11 active batch) → §7G
readings, with no second path, no duplicate path, and no raw-signal
meaning guess anywhere.

**BOP wiring:** authorized-session signals (per accepted **A10**: a
session Ness explicitly opened is authorized for behavioral
observation; **no separate per-signal prompts** inside it; nothing
outside an authorized session) → typed observation roots through the
C-BOP schema (base seven fields; `subject="bop:v1"` legacy tag
untouched; controlled event vocabulary; `capture_id`;
`capture_sequence_number` persisted before any write; the A15
`acoustic_condition_notes` amendment is **NOT accepted — it is an
open, non-blocking Bundle 5 dependency (Bundle 5 paused), and the
current Bundle 6 path neither requires nor adopts it**: the field is
**conditional and unavailable** unless Ness later accepts A15 through
its own package, and nothing here depends on it) → §7E envelope →
B11 active batch. **DUMB boundary absolute:** no emotional label, no
identity conclusion, no meaning, no pattern judgment at capture.

**The A12 imported-item reaction link — the complete event-relative
bounded window mechanic:** when Ness listens to an imported voice
item during an authorized session, one **reaction-window operation**
opens and closes on exact events:
- **Start event:** the recorded playback-start of that exact
  imported item (its origin/`capture_id` bound into the window's
  identity at open).
- **End events (whichever occurs first closes the window):** (a) the
  post-playback bound elapsing after the final recorded playback-end
  — a **governed configuration value, genuinely empirical, carried
  as a required bounded setting** (no unbounded "immediately
  afterward" exists; the setting must be a finite duration); (b)
  **switching to another imported item** — the recorded
  playback-start of a different item closes this window at that
  instant and may open the next item's own window; (c) **session
  end** — closes the window at the session-end event; (d) an
  explicit window-close event.
- **Two distinct eligible segment types inside one valid
  reaction-window operation (accepted A12: during listening AND
  immediately afterward):**
  **(1) Active playback segment** — opens at the recorded
  playback-start or a valid resume; **suspends immediately on
  pause** (observations captured during a paused stretch receive
  **no** `linked_imported_origin_ref` — still captured normally under
  A10, just not linked); closes at pause, playback end, switching
  item, session end, explicit close, or interruption; resuming the
  same exact item may open a new active playback segment under the
  same reaction-window operation **only under a valid, finite,
  governed pause/resume rule** (a bounded maximum pause — a governed
  finite setting), and **an invalid, missing, or expired pause bound
  closes the window fail-closed**.
  **(2) Bounded post-playback reaction segment** — opens at the
  **final committed playback-end event**; remains eligible **only
  until the finite governed post-playback bound expires**; closes
  immediately on a different item starting, session end, explicit
  close, interruption, or expiration; **it never exists without a
  valid finite configured bound**.
  Observations may receive the imported-item reference while inside
  **either** a valid active playback segment **or** the valid bounded
  post-playback reaction segment; paused observations remain
  unlinked; **no observation after the bound is linked**. **Each
  observation belongs to at most one eligible segment and at
  most one imported item.**
- **Interruption behavior:** a crash or capture interruption closes
  the window honestly at the last committed observation
  (`session_interrupted` / `capture_failure` recorded); nothing after
  the gap is back-attributed into the window.
- **Overlap prevention, structurally:** at most **one** reaction
  window is open per session at any time; windows for different
  items never overlap (rule (b) closes before opening); an
  observation root receives at most one `linked_imported_origin_ref`.
- **Operation identity:** `reaction_window_id` [proposed] = session
  id + imported origin ref + recorded playback-start event id —
  deterministic, so a replay cannot open a second window for the
  same playback. **Duplicate prevention:** unique window identity; a
  duplicate open is recognized and recorded. **Crash recovery:**
  restart trusts committed window and observation records only; an
  open window found at restart is closed as interrupted; links
  already committed stand; nothing is re-attributed.
- **Fail-closed rule, explicit:** **reaction linking remains disabled
  and fails closed until every required bound is present and valid**
  — a missing, invalid, or non-finite post-playback bound, a missing
  start-event record, or an unverifiable window state means
  observations are still captured normally (A10) but carry **no**
  `linked_imported_origin_ref`; no link is ever guessed.
An observation may carry `linked_imported_origin_ref` — an explicit
relationship reference to **that exact imported item's** origin (its
root/`capture_id`) — **only when it was captured inside either a
valid active playback segment or the valid bounded post-playback
reaction segment**; paused observations remain unlinked; observations
after the finite post-playback bound remain unlinked; each
observation belongs to at most one eligible segment and one imported
item; and no emotion, motive, agreement, causality, or meaning is
inferred.
**Connected, never merged:** the imported item remains its own
Origin; reaction observations remain their own roots; the link is a
structural fact ("observed while listening to X"), and **no emotion,
motive, agreement, causality, or meaning claim is ever derived from
the raw observations** — any later meaning is the Meaning Engine's
separate, evidence-bound work on the readings, under its own rules.
**OOP wiring:** outcome observations (what happened after a function
acted, including the absence-of-correction discipline: absence is
never confirmation) → `outcome_observation` roots → the same single
§7E path. **Operations:** capture idempotency on `capture_id`;
sequence numbers persisted before write; per-item promotion commits;
crash gaps recorded honestly (`capture_failure`,
`session_interrupted`), never reconstructed; duplicate path
structurally absent — there is exactly one entry (§7E) and one store;
fail-closed: unauthorized source → refused and recorded. **§0B — one-operation/one-log for capture and linking:** when
`linked_imported_origin_ref` is established **as part of an
observation capture, it commits inside that same observation-capture
transaction** — recorded as an append-only canonical child event or
field **inside** that one operation, **never a second independent
parent operational log for the same capture**; the
observation-capture parent has **exactly one terminal operational
record**. A genuinely separate later relationship operation would
require its own distinct identity and must never silently duplicate
the capture-time link. One record per observation captured (its link,
when present, inside it), per
promotion, per capture failure.

## 14. BUNDLE-INTERNAL CONNECTIONS (THE DIRECTLY REQUIRED ONES ONLY)

B12 activates only C-7GA's queue, which reads roots produced through
B-INT-3's and C-14's capture paths. B13's authorized memory entry
lands through the same §7E path B21 shapes. B14's detection consumes
C-14 live-chat captures; its provisional-influence records travel
inside the §0B operation records B-INT-2's routing already logs.
B17's label and B21's fields are both §7E envelope content; B20
corrects beside what B21's schema stores. B22, when ever authorized,
uses B21's Origin shapes, C-9A, accepted A7/A30, and the same single
no-bypass entry. Nothing here closes another file's scope: the B11
mechanism, B9 retry values, B24/B26, B-CYCLE-7 wiring, and every
Bundle 5 item remain exactly where they are.

## 15. CONSOLIDATED MUST-NEVERS

Never reopen, unseal, or append to a sealed batch; never write a
root outside §7E → B11; never let research material reach memory
except through the review queue and authorized entry; never train or
alter the mouth; never confirm a creation by time, repetition,
retrieval, system use, or model repetition; never present
provisional material without its carried status; never silently fuse
fragments; never let the provenance label claim topic, meaning,
truth, or importance; never guess a speaker; never show a visible
clickable point-back link or topic-type tag; never fabricate an
uncertain reference; never rewrite a sealed root or old source
record (aliases live beside, append-only); never reuse the legacy
`subject` field semantically; never guess an unknown source time;
never merge mixed-media items into one Origin; never decrypt or
ingest WhatsApp material under this file; never apply an automatic
age-only gate — and never weaken any ordinary privacy, evidence,
uncertainty, external-use, harm, legality, or simulation rule; never
let LMAC own data, cache, filter, or query BOP/OOP processors; never
derive emotion, motive, agreement, causality, or meaning from raw
observations; never let a log add evidence weight or log itself;
never bypass §7Q-before-§7R; never begin implementation.

## 16. DEPENDENCY STATUS — ACCEPTED VERSUS GENUINELY OPEN

**Accepted dependencies, consumed exactly and NOT open:** **B11
v1.4** — the active writable-batch architecture is accepted and
PACKAGE_COMPLETE for its design scope; its contracts are consumed
per §3 (registry/selection, global ingestion claim, root-ownership
binding, append commit fence, parent/child operation identity,
one-operation/one-log, historical-coverage gate, recovery,
fail-closed). **B9** — the retry-state architecture and the
retry-values wiring v1.4 are accepted; the exact values are carried
in §3 and bound per item; **retry counts, gaps, and deadlines are
not open questions.** **B24 v7** — accepted; consumed by B14's
route-B grounding boundary. **B1** — accepted context-retrieval
parameter architecture. Nothing in this file reopens, redesigns,
summarizes away, or replaces any accepted package.

**Genuinely open, with their correct owners:** **B26** — retrieval
system-failure behavior. **B-CYCLE-7** — the full live-creation
cycle wiring. Any genuinely unclosed empirical or system-failure
work inside an accepted package's declared open remainder stays with
that package's owner. **A27 / A28** — open, non-blocking
future Ness decisions (five types; live-chat-only path — both
enforced as current boundaries above). **A13.3** — the
talk-about-promising-fragments interface idea: outside this package,
routed to Bundle 7 / A19. **§24 / B-INT-8 (Bundle 5, paused)** —
connection acceptance routes where non-source-recorded Origin
relationships would be proposed. **B7 (Bundle 5, paused)** — the
protected-execution and sealed-storage machinery B22's key/plaintext
requirements consume; the WhatsApp path stays disabled and
non-runnable until B7 is accepted and integrated through the
version-safe process. **A15 (Bundle 5, paused)** — the
`acoustic_condition_notes` amendment: open, non-blocking for this
package; the field stays conditional and unavailable unless Ness
later accepts A15 through its own package. **Remaining governed settings**
(Ness's schedule value; the finite A12 post-playback bound;
reliability representations) — governed, none chosen here.
**All implementation** — including any schema activation or
migration, gated behind Ness's separate authorization.

## 17. DRAFTING CHECKS, COVERAGE, AND CHANGE REPORT

**Drafting checks (no-loss and consistency checks performed by the
drafter — not independent verification, not enforcement proof):**
every accepted policy protection restated above where its machinery
lives — separate connected Origins; three separate times with
honest unknowns; context-limited revisable no-context readings
(consumed from the governing reading design, unchanged);
Person-Box Holding through linked existing objects with **no new
profile store created anywhere in this file**; authorized-session
observation without per-signal prompts; the 13 names as views (no
store or model per area exists in any schema above);
connect-never-infer reaction links; broad tiny-fragment capture;
five types, multi-type records, exact fragment provenance, two
confirmation routes only, carried-and-traceable provisional
influence, no silent fusion; no age-only gate with ordinary rules
intact and the archive frozen; no visible link and no fabricated
references with the supersession openly carried; provenance-only
label with N.H-output-not-fact — consistent in drafting. Every
operation above carries identity, transactions, lifecycle,
append-only records, idempotency, duplicate prevention, retry
(values by reference), crash recovery, partial-completion recovery,
failure handling, no-bypass, and one-operation-one-record §0B
logging with no recursive logging and no self-evidence — consistent
in drafting. Both A12 segment types link and nothing narrows them back; candidate
identity survives run, timestamp, and synthesis-version changes; one
trigger-request parent and one run child, each with one terminal
record; per-type work-item identities with direction-aware
relationship keys; capture-time links inside their capture
transaction — consistent in drafting.
Bundle 5 boundaries honest — B7 and A15 open, the WhatsApp path
disabled until B7 lands, nothing designed or closed across the
pause; trigger requests never lost, held durably, coalesced only
with verified coverage; base Creation Records
detector-version-stable; aliases presentation-only after canonical
membership; both A12 eligible segment types bounded and paused-time
unlinked; message/media/relationship work items independently
recoverable — consistent in drafting.
Immutable base records with one canonical confirmation truth; stable
`thread_id` never aliased; honest zero-main-date unknown time with no
`source_occurred_at` remnant; append-only endpoint-verified Origin
relationships; truthful activation-trigger dispositions with no lost
request; pause-suspended reaction linking — consistent in drafting.
Accepted B11, B9 (architecture and exact values), B24, and B1
consumed exactly, with the Map's stale open-status wording corrected
against the accepted-designs folder — consistent in drafting. The
one-time activation boundary untouched; scheduler configuration and
runs in separate append-only records; cross-run-stable duplicate keys
in B13; immutable base Creation Records with derived status and
grounded route-B proposals; compare-and-append alias heads; typed
source times; L1 key and protected-staging lifecycle in B22 with no
postponed privacy checks; the non-recursive §7Q/§7P control path and
one-parent-operation query retry identity; and the complete
fail-closed A12 reaction window — consistent in drafting.
Authority order preserved; no policy invented; no other
bundle's scope closed; no implementation authorized — consistent in
drafting.

**Coverage:** B12 §4; B13 §5; B14 §6; B17 §7; B18 §8; B20 §9; B21
§10; B22 §11; B-INT-2 §12; B-INT-3 §13; connections §14; boundaries
§15; open dependencies §16.

**Change report:** this v1_4 was produced by copying the
identity-verified v1_3 and applying the final five-issue pass (title;
the v1_4 version note; §4 B12 §0B precision; §5 B13 five identities;
§11 B22 work-item identities and §0B coverage; §13 A12 linking
sentence and §0B; these §17 lines; the end line). v1_0 through v1_3
are preserved unchanged as historical candidate provenance. The v1_3
pass before it applied the six-issue pass (title;
the v1_3 version note; §4 B12 trigger-request lifecycle; §6 B14
duplicate identity; §9 B20 presentation-only consumption; §11 B22
A7/B7 honesty and work-item recovery; §13 B-INT-3 A15 status and the
two A12 segment types; §16 B7/A15 dependencies; these §17 lines; the
end line). v1_0, v1_1, and v1_2 are preserved unchanged as
historical candidate provenance. The v1_2 pass before it applied the
six-issue consistency pass
(title; the v1_2 version note; §4 B12 dispositions and records
wording; §6 B14 base-record fields, events, and canonical
confirmation; §9 B20 field vocabulary and thread_id protection; §10
B21 zero-legal source times, main-date rule, and relationship
records; §11 B22 typed source times and endpoint-verified
relationships; §13 A12 listening segments; these §17 lines; the end
line). v1_0 and v1_1
are preserved unchanged as historical candidate provenance. Exactly
one new file was created;
nothing existing was modified, overwritten, moved, renamed, or
deleted; no receipt, accepted copy, Map candidate, or Master
candidate was created; nothing was committed or pushed; no code,
store, schema activation, migration, test, decryption, ingest, or
Cursor instruction exists or is authorized. This candidate now waits
for ChatGPT's independent audit of this actual file, then Ness's
explicit acceptance.

---

*End of `NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` —
`CANDIDATE — NOT ACCEPTED — NOT ADOPTED — NOT AUTHORITATIVE — NOT
IMPLEMENTED`. The answers Ness gave now have their machines drawn:
everything enters through one door, nothing is guessed, nothing is
fused, nothing confirms itself, nothing activates silently, and the
frozen stays frozen until Ness says otherwise.*

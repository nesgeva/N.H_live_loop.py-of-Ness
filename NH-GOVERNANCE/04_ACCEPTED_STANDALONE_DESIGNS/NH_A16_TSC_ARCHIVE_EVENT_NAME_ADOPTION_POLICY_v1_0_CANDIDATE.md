# NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_v1_0_CANDIDATE.md

## 0. STATUS BLOCK

**Status:** `CANDIDATE — NOT ADOPTED — NOT BUILT.` Standalone A16
policy package recording Ness's July 13, 2026 adoption of the two
active TSC archive-event names. **A vocabulary adoption only:** it
renames nothing retroactively, rewrites no historical record, and
redesigns nothing in the TSC lifecycle. Not accepted, not adopted as a
package, not authoritative, not integrated, not implemented; no code,
migration, schema-production, or live-system work is performed or
authorized. Independent of, and not merged with, the separately
prepared A15 candidate.

**Date:** July 13, 2026.

**Register item:** A16 — Bundle 5 policy work (Bundle 5 — Privacy,
security, access, and TSC authority — the current unfinished bundle).
The Map's A16 entry reads: *"TSC archive-event rename
(`tsc_archive_seal_authorized` / `tsc_archive_sealed`). Adopt or not
(§7E-TSC §26)."* — Ness has now decided: **adopt.**

**Intended repository placement:** `05_ACTIVE_CANDIDATE/`
(the physical move into the repository is Ness's action).

**Pinned repository snapshot:** `nesgeva/NH-GOVERNANCE`, branch
`main`, commit `bbf4e900a00d1082d11829bfd33ca339d8b98b00` — the
verified head named by the governing task instruction, confirmed by
`git ls-remote` before writing.

## 1. GOVERNING AUTHORITY AND SOURCES READ

**Governing authority order:**
1. `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` (adopted by Ness
   June 29, 2026; governing)
2. `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`
3. `01_AUTHORITATIVE/cursorrules`
4. `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`

**Read for this candidate, byte-verified at the pinned snapshot:** the
complete Master **§7E-TSC** archive lifecycle and audit-event material
— §12 session lifecycle (`archived` → `permanently_sealed`; no
`deleted` state), §24 duplicate protection, §25 privacy precedence,
**§26 Security Audit Events in full** (the active event set, the
superseded-names provenance block, the required corrected meanings,
and the proposed-replacement-names PENDING REVIEW block), §27 recovery
context, the §7E-TSC provenance header, and Master §11 item 35; the
Map v1.6 **A16** register entry and **C-TSC** references; the
eight-bundle plan's Bundle 5 section; the four governing files per
this session's verified reads. All shared repository files are
byte-identical across this session's pinned commits; the only changes
between pins are Ness's own commits of previously delivered files.

## 2. THE APPROVED A16 DECISION — RECORDED EXACTLY

On July 13, 2026, Ness accepted the proposed active TSC archive-event
names. **The settled active vocabulary for future design and later
implementation is:**

- **`tsc_archive_seal_authorized`** — the separate authorization to
  permanently seal the retained TSC archive; **it does not authorize
  destruction or deletion.**
- **`tsc_archive_sealed`** — the retained archive was permanently
  sealed and the required history record was written; **it was not
  deleted, destroyed, or replaced with a tombstone.**

These two names resolve the Master §7E-TSC §26 "PENDING REVIEW — NOT
formally adopted vocabulary" status: the proposal is now Ness-adopted
at policy level through this candidate, pending this package's own
audit and acceptance. **No additional TSC event name is invented,
proposed, or adopted here.** The accepted active names do **not**
create a `deleted` lifecycle state and carry the Master's required
corrected meanings exactly: authorization to permanently **seal** (not
delete); archive permanently **sealed with a history record written**
(not deleted with a tombstone).

## 3. HISTORICAL NAMES — PROVENANCE ONLY, NEVER REWRITTEN

The historical names remain preserved **only as provenance**:

- `tsc_archive_deletion_authorized`
- `tsc_archive_deleted` — including the old `tombstone_written: true`
  wording.

They were superseded for active use by the no-destruction law and are
retained in `NH_ACCEPTED_TSC_DESIGN_v1.md` §26 for provenance only,
exactly as Master §7E-TSC §26 records. **Historical records and files
using those old names must never be rewritten or renamed.** No
historical event, file, log, or accepted design is rewritten,
re-labeled, or edited by this adoption; anything already written under
the old names stays byte-identical forever, readable through its own
provenance.

## 4. THE EVENT LADDER — FIVE DISTINCT EVENTS, DISTINGUISHED

The adopted names slot into the settled §7E-TSC event set without
changing any other event. The five events that matter here, each with
its own distinct job:

1. **`cache_sealed`** — **normal session sealing** of the active TSC
   at session end, with its settled `seal_reason` values
   (`"normal_close"` / `"interrupted_crash"` /
   `"interrupted_app_close"`). This is everyday session closure — not
   archive sealing.
2. **`tsc_retained_archive_created`** — **creation of the retained
   archive** after successful promotion (`archive_location_ref`,
   `created_at`); the session moves toward its `archived` terminal
   operational state.
3. **`tsc_archive_access_authorized`** — **bounded machine-purpose
   access** to the retained archive: permitted only for bounded
   machine-level integrity, verification, recovery, or audit functions
   that do not expose the conversation to a person and do not return
   it to ordinary N.H reasoning. No human browsing. Unchanged.
4. **`tsc_archive_seal_authorized`** *(adopted active name)* — the
   **separate authorization** for permanent archive sealing:
   `archived` → `permanently_sealed` may follow only through this
   separately authorized path; it never happens automatically, and it
   authorizes no destruction or deletion.
5. **`tsc_archive_sealed`** *(adopted active name)* — the **completed
   permanent sealing**: the archive is permanently sealed and the
   required history record is written. Nothing is deleted, destroyed,
   or tombstoned.

## 5. THE NO-DESTRUCTION DESIGN — PRESERVED COMPLETELY

All of the following stands exactly as settled, unchanged by the
rename:

- **Retained archives are preserved permanently.** Archives are never
  deleted; **no `deleted` lifecycle state exists.**
- **`archived` may later become `permanently_sealed` only through the
  separately authorized path** — never automatically.
- **Sealing history records contain no preserved conversation
  content** — they document the seal authorization and outcome only.
- **TSC inspection remains prohibited** entirely (the June 29, 2026
  prohibition; the old `tsc_inspection_*` cluster stays superseded; no
  inspection token, mechanism, or authorized path exists or is
  created).
- **`tsc_archive_access_authorized` remains limited** to bounded
  machine-level integrity, verification, recovery, or audit functions
  that do not expose the conversation to a person and do not return
  it to ordinary N.H reasoning.
- **The retained archive never becomes active memory** and is not
  queryable by LMAC, §7F, §7G, Person-Boxes, Computed View, or normal
  operational components; the settled duplicate protections stand
  (per-item `promoted_root_id`, `append_root()` idempotency, runtime
  isolation, no §7E re-submission).

## 6. WHAT THE RENAME DOES — AND DOES NOT — DO

The adoption settles two active event **names and their meanings**,
nothing more. It does **not** redesign the TSC lifecycle,
authorization model, promotion flow, retry behavior, recovery
behavior, storage design, or access rules — every one of those stands
exactly as accepted in §7E-TSC. It changes no controlled identifier
outside the exact accepted replacement, adds no event, removes no
event, and alters no event's field set. It presents no destruction or
tombstone wording as active behavior anywhere.

## 7. MASTER AND MAP STATUS — UNEDITED, HISTORICALLY INTACT

Master V10 (§7E-TSC §26's "PENDING REVIEW" block, the §7E-TSC status
line, and §11 item 35) and the Map's A16 register entry **retain their
historical pending wording on disk, unedited, until later versioned
integration** through the normal route. This candidate records the
adoption; it does not touch the files that still describe the names as
proposed. Ness's later explicit adoption governs over that stale
internal wording, exactly as the standing governance rule provides.

## 8. EXPLICITLY OPEN

- ChatGPT's independent audit of this actual file;
- Ness's separate acceptance of this package;
- the acceptance receipt and accepted-source placement;
- **B7**; **B15**; **B-INT-4**; **B-INT-5**; **B-INT-6**; **B-INT-7**;
  **B-INT-8**;
- Bundle 5 closure;
- later Map or Master integration of the adopted vocabulary;
- every implementation and coding task (including any future writing
  of these events by real machinery — none exists and none is begun).

## 9. MUST-NEVER BOUNDARIES

This candidate — and any later work consuming it — must never: edit,
overwrite, rename, move, or delete any existing file; modify Master
V10, Defaults, cursorrules, the Companion, the Map, workflow files,
accepted packages, or historical candidates; rewrite or rename
historical events, logs, or provenance files; invent additional TSC
event names or alter controlled identifiers beyond the exact accepted
replacement; create a `deleted` state, destruction path, tombstone
behavior, inspection path, or archive query path; treat folder
placement as acceptance; create an acceptance receipt from within this
file; mark this package accepted, adopted, authoritative, integrated,
implemented, or built; mark Bundle 5 complete; begin B7, B15, or any
B-INT package; or write code, migrations, production schemas, patches,
tests, or Cursor instructions.

## 10. REQUIRED CHECKS — VERIFIED BEFORE DELIVERY

1. **Exactly two new active archive-event names** — yes:
   `tsc_archive_seal_authorized` and `tsc_archive_sealed`; nothing
   else added (§2, §6).
2. **Historical names preserved and not renamed retroactively** — yes
   (§3).
3. **No deletion state** — yes; `deleted` does not exist and is not
   created (§4, §5).
4. **No destruction or tombstone wording presented as active
   behavior** — yes; both appear only as historical provenance (§3)
   and explicit negations (§2, §5).
5. **Inspection remains prohibited** — yes (§5).
6. **Retained archive remains isolated from ordinary N.H** — yes
   (§5).
7. **No accidental redesign of the TSC lifecycle** — yes (§6; the
   ladder in §4 restates settled events without changing any).

## 11. STATUS, CHANGE REPORT, AND SELF-AUDIT

**Status:** `CANDIDATE — NOT ADOPTED — NOT BUILT` — awaiting ChatGPT's
independent audit of this actual file and Ness's explicit acceptance
afterward.

**File created:**
`NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_v1_0_CANDIDATE.md` —
one of exactly two independent files created in this controlled
drafting run (the other being the separate A15 candidate; no policy
from either package leaks into the other). **Nothing existing was
modified:** Master V10, Defaults, cursorrules, the Companion, the Map,
the plan, every accepted package, and all historical candidates and
provenance files remain byte-identical at the pinned snapshot
`bbf4e900…`. Nothing was committed, pushed, moved, renamed,
overwritten, or deleted. No acceptance receipt was created; no Map or
Master integration occurred; no coding or implementation began.

**Self-audit:** decision recorded exactly with both adopted names and
their exact meanings — PASS. Historical names identified as provenance
only, never rewritten — PASS. Five-event ladder distinguished without
redesigning anything — PASS. No-destruction, no-deletion,
no-tombstone, no-inspection, and full archive isolation preserved —
PASS. Master and Map pending wording left intact pending later
versioned integration — PASS. B15, B-INT-4, and all implementation
left open — PASS. All seven required checks verified — PASS.

---

*End of
`NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_v1_0_CANDIDATE.md` —
`CANDIDATE — NOT ADOPTED — NOT BUILT`, awaiting ChatGPT's independent
audit and Ness's acceptance. The active vocabulary is settled:
authorization seals, sealing seals — nothing deletes, nothing is
destroyed, nothing is inspected, and the retained archive stays
outside ordinary N.H forever. History keeps its old names untouched.
Nothing existing changed; nothing was implemented.*

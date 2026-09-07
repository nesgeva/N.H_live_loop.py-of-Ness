# NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md

## 0. STATUS BLOCK

**Status:** CANDIDATE — unaudited; awaiting ChatGPT's independent audit of
this actual file and Ness's explicit acceptance afterward. **Standalone
A25 design package only.** Not accepted, not adopted, not authoritative,
not integrated into Master V10, the Design and Wiring Map, Decision
Defaults, or `cursorrules`. **It does not modify B10**, fills no B10 slot,
and authorizes no implementation, code, store, disk, runtime, PC, or UI
work, and no tuning value of any kind.

**Version note (v1_2):** corrects only an internal overlap inconsistency
inside §5 — two earlier sentences still made the modes sound mutually
exclusive (the wider-context explanation's "is not directly contradicted
or corrected" and the boundary's "without direct contradiction"), which
conflicted with Ness's approved dual-assignment rule. v1_2 makes the two
relationships independently tested and explicitly not mutually
exclusive; wider-context does not require the absence of direct bearing
and may apply with or without `direct`. **No settled decision changed:**
the seven-line decision, the dual-assignment rule, the two semantic
modes, and every boundary stand exactly as approved. v1_0 and v1_1
(v1_1 SHA-256
`8ef859ff97943c9fd6a2e49de73cea5034a76cc4cb79783ab08baa2e6f543cfa`;
239 lines; 12,814 bytes) are preserved unchanged as historical candidate
provenance.

**Version note (v1_1):** v1_1 records Ness's approved dual-assignment
rule for genuine overlap cases — both existing modes recorded together,
never a third mode (§5) — and corrects the trigger wording so nothing
claims a total trigger count or that A25 "adds no fourth trigger" (§6,
§7): A25 does not add, remove, rename, or reclassify any trigger, and the
accepted B10 trigger vocabulary (including `on_rejection`) stands exactly
as accepted. **No other A25 meaning changed.** v1_0 (SHA-256
`3f3c8f20df47976a6ed3e415084d066f2e12465a05e83a110912665142c10949`;
213 lines; 11,166 bytes) is preserved unchanged as historical candidate
provenance.

**Date:** July 11, 2026.

**Package ID:** A25 — reread mode assignment (Register A; Bundle 1 policy
side; the Master §7H scope boundary's "separately adopted reread
mode-assignment rule"; the open slot gating the accepted B10 package's
`reread_mode_ref`).

**Intended repository placement:** `05_ACTIVE_CANDIDATE/`
(the physical move into the repository is Ness's action).

## 1. GOVERNING AUTHORITY ORDER

1. `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`
   (adopted by Ness June 29, 2026; governing)
2. `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`
3. `01_AUTHORITATIVE/cursorrules`
4. `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`

## 2. SOURCES READ FOR THIS CANDIDATE

All read from the governance repository snapshot byte-verified twice on
July 11, 2026, except where noted:

- `05_ACTIVE_CANDIDATE/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_CANDIDATE_v1_1.md`
  (SHA-256 `6828b9bd88cf867d20bfee31b67d13e97e0c573316b43d2298e4764785abeec3`)
  — §5, the recorded A25 normalized decision, read verbatim and preserved
  in §4 below.
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_ACCEPTANCE_RECORD_v1_0.md`
  (fetched copy SHA-256
  `d759d99d6d01cfe0371c5f4261912f2a4e11cabc10ec3fd8cc249bd5d522d7f7`)
  — read in full; confirms the v1.1 record is accepted for its recording
  scope only, with A25 decided and awaiting integration.
- Accepted **B10** package and closure record:
  `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md`
  (SHA-256 `215b74841321656a8b7fb1cbf4b9ac9b43259315864cd9f85f5ce86b43d10001`)
  and `…_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
  (SHA-256 `da62a1e8216924f9e9f3182f925e7a1e5063355418a7302eb58f86eee54adeea`)
  — the `reread_mode_ref` slot at RR2, the fail-closed
  `dependency_blocked_held` default, and B10's what-it-is-not boundaries,
  all consumed without reopening.
- `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`
  (CY-F and the B10/A25 entries) and Master V10 §7H — consumed unchanged.

## 3. PURPOSE AND SCOPE

**What this package is.** It is the standalone A25 policy package: it
preserves and defines Ness's settled reread mode-assignment decision —
the two reread modes and the boundary between them — filling exactly the
policy slot that Master §7H leaves to "a separately adopted reread
mode-assignment rule" and that the accepted B10 package holds fail-closed
at `reread_mode_ref`.

**What this package does not do:** it does not modify B10 or fill its
mode slot (that is the separate governed A25-to-B10 connection); it
invents no trigger types, thresholds, schedules, detection mechanisms,
relevance rules, retrieval configurations, or implementation details; it
reopens nothing accepted; it integrates nothing and adopts nothing.

## 4. NORMALIZED DECISION RECORD — NESS'S SETTLED A25 DECISION

**Ness-approved decision — recorded in the accepted Bundle 1
normalization record (v1.1 §5) and carried identically by the governing
task instruction; preserved verbatim:**

> - N.H uses both direct reread mode and wider-context reread mode.
> - Direct reread mode applies when new information directly changes,
>   corrects, limits, or contradicts an old reading.
> - Wider-context reread mode applies when new information may materially
>   change the surrounding meaning/context of an old reading, even without
>   direct contradiction.
> - This is not permission to reread everything.
> - Every reread must have a real recorded reason.
> - Old readings are never overwritten, edited, or deleted.
> - A reread creates a new reading/layer beside the old one.

## 5. THE TWO MODES — DEFINED

Both modes are reread modes inside the settled §7H reread lifecycle. A
mode describes **a relationship between a piece of new information and
an existing old reading**; each mode is assigned by its own
relationship, checked independently, and by nothing else.

- **`direct` reread mode** — assigned when the new information **directly
  changes, corrects, limits, or contradicts the old reading itself.** The
  old reading's own content is what the new information bears on:
  something it asserted is changed, corrected, narrowed, or contradicted.
- **`wider-context` reread mode** — assigned when the new information
  **may materially change the surrounding meaning or context of the old
  reading, even without direct contradiction.** The old reading's own
  content does not need to be directly contradicted or corrected for
  this mode to apply; a material surrounding-context change is
  sufficient. Direct bearing may also exist in the same case, in which
  case both modes are recorded.

**The two relationships are tested independently:** *direct bearing on
the old reading's own content*, and *material change to its surrounding
meaning or context.* **They are not mutually exclusive.**

**Genuine overlap — Ness's approved dual-assignment rule:** `direct` is
recorded whenever the direct relationship applies; `wider-context` is
recorded whenever the surrounding-context relationship applies; **when
both relationships apply in the same real case, both modes are recorded
together.** Neither mode erases, replaces, or hides the other, and **no
third semantic mode exists or is created** — a dual assignment is the
two existing modes together, nothing else. Every reread still requires a
real recorded reason, and this remains no permission to reread
everything. The exact storage encoding of an assignment (single or dual)
inside B10's `reread_mode_ref` remains part of the later governed
A25-to-B10 connection, not this standalone package.

## 6. BOUNDARY RULES — WHAT THE MODES ARE NOT

- **Not blanket permission.** Neither mode is permission to reread
  everything. When new information neither directly bears on an old
  reading nor materially changes its surrounding meaning, this rule
  assigns no reread.
- **Every reread requires a real recorded reason.** The settled §7H
  record set stands: trigger type, reason, initiator, new-evidence
  reference, previous reading IDs, configuration reference, timestamp.
  A mode never substitutes for a reason; it accompanies one.
- **No trigger change of any kind.** A25 does not add, remove, rename,
  or reclassify any trigger. Master §7H names the manual, condition-based
  (materially relevant new information; time alone never qualifies), and
  scheduled-automatic-retry (temporary technical conditions only, never
  reinterpretation) triggers, and separately records the rejection path;
  the accepted B10 package carries its accepted trigger vocabulary,
  including `on_rejection`. A25 consumes those settled representations
  unchanged and decides only reread mode assignment.
- **Append-only, always.** Old readings are never overwritten, edited,
  or deleted. A reread creates a new reading/layer beside the old one,
  through the settled lifecycle and the accepted B10 mechanics. Rejection
  of a reading never proves the opposite; readings coexist as visible
  history.
- **Nothing quantitative is created.** No threshold, score, schedule,
  frequency rule, relevance rule, detection mechanism, or "materially"
  metric exists in this package. How a mode-relevant condition is
  detected or evaluated remains where the settled architecture leaves it
  (§7H/§7R territory and later governed work) — open, not decided or
  biased here.

## 7. RELATIONSHIP TO SETTLED ARCHITECTURE (PRESERVED, UNCHANGED)

- **Master §7H** — its named triggers, its separately recorded
  rejection path, the record set, and the new-reading-beside-old rule
  stand exactly as settled. §7H's scope
  boundary is honored: `thread_membership_v1` governs new-root passes
  only and is not borrowed for rereads.
- **Accepted B10** — its reread operation identity, claim, trigger-record,
  layer, and recovery mechanics stand exactly as accepted. B10's
  `reread_mode_ref` slot at RR2 continues to resolve fail-closed
  (`dependency_blocked_held`) **until the separate governed A25-to-B10
  connection fills it** — this package does not fill it. B10 carries
  whatever mode A25 produces and biases nothing; this package produces
  the two modes above.
- **How an assigned mode configures a reread pass's context retrieval**
  (the §7F/§7R steps at B10's RR2, including the map's earlier
  bare/local-context framing of this open slot) is **part of the later
  governed connection and integration work** — an open slot with a named
  owner, not decided here.

## 8. OPEN DEPENDENCIES (EXPLICIT; NONE CLOSED HERE)

- **The separate governed connection of A25 into B10** — filling
  `reread_mode_ref`, its mode-to-retrieval configuration, and the release
  of B10's fail-closed default — open; later governed work requiring its
  own versioned candidate, audit, and Ness acceptance.
- **B9 retry-value wiring** into B9, B10, B-HOLD, and B24 — open.
- **Full-cycle composition (B-CYCLE-8 / CY-F)** and **Master / map /
  Defaults / cursorrules integration** — open; later, separately
  authorized work.
- **Coding, runtime, store, and PC work** — none authorized; all await
  Ness's separate implementation authorization.
- **Condition-based relevance rules, scheduling, orchestration, and
  degraded-retrieval behavior** (§7H/§7R; B26) — open with their settled
  owners, untouched.
- No other open Register-A/B item is closed or biased by this package.

## 9. DESIGN-COMPLETE CONDITION FOR THIS PACKAGE

This package is design-complete for the A25 policy when: Ness's decision
is preserved verbatim without added meaning (§4); the two modes and their
independently tested relationships are defined strictly from that
decision (§5); the not-blanket,
recorded-reason, no-trigger-change, append-only, and
nothing-quantitative boundaries hold (§6); the settled §7H and accepted B10 architecture stand
unchanged with the connection work left open and owned (§7); and every
dependency in §8 remains open — subject to ChatGPT's independent audit
and Ness's explicit acceptance.

## 10. CHANGE REPORT AND SELF-AUDIT

**File created:** `NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md`
— the only file created by this task, from the verified v1_1 (v1_0 and
v1_1 preserved unchanged as historical candidate provenance). **Nothing existing was modified:** Master V10,
Defaults, `cursorrules`, the Companion, the map, every accepted package
and closure record (including B10 and the Bundle 1 records), the complete
A1 chain, and all historical candidates remain byte-identical.

**Self-audit:** authority order preserved — PASS. Decision preserved
verbatim from the accepted record; no new meaning — PASS. No new trigger
types, thresholds, schedules, relevance rules, detection mechanisms, or
implementation details invented — PASS. B10 not modified; its fail-closed
mode-slot default explicitly left standing — PASS. Dual assignment
recorded as the two existing modes together; no third semantic mode; no
storage encoding chosen — PASS. No trigger added, removed, renamed, or
reclassified — PASS. Append-only and
recorded-reason rules carried unchanged — PASS. All named dependencies
left open with owners — PASS. Candidate status; nothing marked accepted,
adopted, integrated, or complete — PASS. No implementation, PC, store, or
runtime action — PASS.

---

*End of `NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md` —
CANDIDATE, unaudited, awaiting ChatGPT's independent audit and Ness's
explicit acceptance. B10 is not modified; its mode slot remains
fail-closed until the separate governed connection. All authority,
accepted, and historical files remain unchanged; no implementation was
performed.*

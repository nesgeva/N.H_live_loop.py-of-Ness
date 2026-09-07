# NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md

## 0. STATUS BLOCK

**Status:** `CANDIDATE — NOT ADOPTED — NOT BUILT.` Standalone A15
policy package recording Ness's July 13, 2026 acceptance of the
proposed BOP `acoustic_condition_notes` amendment **at policy/design
level**. It activates no schema, changes no production system, creates
no capture path, and selects no threshold or algorithm. Not accepted
as a package, not adopted, not authoritative, not integrated, not
implemented. Independent of, and not merged with, the separately
prepared A16 candidate.

**Date:** July 13, 2026.

**Version note (v1_1):** narrow correction of v1_0 only, closing the
one IMPORTANT issue from ChatGPT's independent audit of the actual
v1_0 file (SHA-256
`c32a6cd90c92f3f3ab1f2b45dd6dde63d086ff7affe1d43d7fad9478b59a3fa5`;
268 lines; 12,963 bytes — preserved unchanged as historical candidate
evidence). v1_0's §7 said a condition record must never "become **or
feed**" an identity, spoofing, or similar conclusion — the words "or
feed" accidentally prohibited the accepted intended use of these
measurements as physical, provenance-bearing context, contradicting
§5's lawful downstream-use rule (for example, a high-noise measurement
helping SIA judge whether a weak voice match could be caused by poor
recording quality). v1_1 replaces the overbroad ban with the precise
boundary: a record never **itself asserts** and is never **sufficient
by itself** to establish any such conclusion; downstream components
**may** use it as bounded provenance-bearing physical context under
their own accepted authority, evidence, uncertainty, and validation
rules; no silent conversion into interpretation or fact; every
downstream use preserves the measurement, method, version, threshold,
measured value, certainty scope, and source provenance; and the record
remains DUMB physical evidence even when a SMART or identity component
later considers it alongside other evidence. §5, §7, the required
checks, and the self-audit were aligned; **nothing else changed** —
the six fields, the five controlled names, all open items, and every
other boundary stand exactly as in v1_0.

**Register item:** A15 — Bundle 5 policy work (Bundle 5 — Privacy,
security, access, and TSC authority — the current unfinished bundle).
The Map's A15 entry reads: *"BOP `acoustic_condition_notes` amendment.
Accept or reject (§25.1; pending, must not be activated)."* — Ness has
now decided: **accept.**

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
complete Master **§25.1 BOP** material — what BOP is and is not, the
authorized-session and authorized-signal-source rules, the v1
controlled event vocabulary, the observation root schema and BOP
payload (including `signal_measurements`, `simultaneous_bundle_id`,
`observation_quality`, `third_party_flag`), the corrected `capture_id`
and durable `capture_sequence_number` idempotency rule, the DUMB
boundary, the failure/recovery/idempotency rules, and the **"Proposed
BOP Schema Amendment (PENDING SEPARATE REVIEW — NOT ACCEPTED)"**
paragraph this decision resolves; Master §25.12 (the settled pattern
for formally adopted vocabulary additions); the Map v1.6 **A15**
register entry and **C-BOP / C-SIA** references; the eight-bundle
plan's Bundle 5 section; the four governing files per this session's
verified reads. All shared repository files are byte-identical across
this session's pinned commits.

## 2. THE APPROVED A15 DECISION — RECORDED EXACTLY

On July 13, 2026, Ness accepted the proposed BOP
`acoustic_condition_notes` amendment. **At policy/design level:**

For voice-channel `signal_measurements`, BOP may record an **optional
list** of physical acoustic-condition records. Each record carries
exactly these six fields:

- `condition_name`
- `detection_method`
- `detection_version`
- `threshold_value`
- `measured_value`
- `certainty`

The accepted **controlled condition names** — exactly five, a closed
list to which this candidate adds nothing:

- `high_ambient_noise`
- `close_microphone`
- `far_microphone`
- `room_reverb_present`
- `signal_compression_heavy`

These are **deterministic descriptions of measurable recording
conditions only.** This resolves the Master §25.1 pending-amendment
paragraph's "requires separate consistency review before adoption"
status: the review is done and the amendment is Ness-accepted at
policy level through this candidate, pending this package's own audit
and acceptance. The Master retains its historical pending wording on
disk, unedited, until later versioned integration.

## 3. THE SIX FIELDS — PLAIN OPERATIONAL LANGUAGE

- **`condition_name`** — which of the five measurable recording
  conditions this record is about. Nothing outside the closed list.
- **`detection_method`** — what actually measured it: the named
  deterministic method that produced the classification.
- **`detection_version`** — which version of that method ran, so the
  same input can be checked against the same tool later.
- **`threshold_value`** — the line the measurement was compared
  against to decide the condition was present.
- **`measured_value`** — what was actually measured on this signal.
  Together with the threshold, it makes the classification
  reproducible: anyone can re-check how it was produced.
- **`certainty`** — how confident the measurement is **that the
  physical condition classification is correct — and nothing else.**
  It is not identity confidence, not speaker confidence, not emotional
  confidence, not truth confidence, and not evidence authority.

Every recorded classification must carry the detection method and
version and the threshold and measured value needed to check how it
was produced — no bare labels, ever.

## 4. PLACEMENT AND PRESERVED BOP STRUCTURE — NOTHING ELSE CHANGES

- The condition records live **inside voice-channel physical
  `signal_measurements`** only, as an optional list. Absence of the
  field is normal and means nothing.
- **One observation root per signal channel** stands; the settled
  simultaneous-bundle behavior (`simultaneous_bundle_id` /
  `simultaneous_bundle_position`, reconstructible bundles,
  single-role constraint) stands.
- The **base seven-field sealed root schema is unchanged**; the notes
  ride inside the existing BOP payload structure.
- The existing **BOP capture identity, durable sequence, idempotency,
  failure, and crash-recovery rules are preserved exactly**:
  `capture_id` construction; `capture_sequence_number` persisted in a
  local durable log before any write; same-`capture_id` retry with
  `append_root()` absorbing duplicates; `capture_failure` roots with
  honest gaps; `session_interrupted` on restart; nothing reconstructed
  after a crash.
- **`observation_quality` and `third_party_flag` handling are
  preserved exactly**, including honest incompleteness recording and
  the settled third-party handling values; BOP roots keep following
  the same sensitivity, deletion, protection-level, and
  no-destruction rules as all roots, with §7Q internal-use
  authorization for internal processing and §7Q visible-output rules
  when anything is actually surfaced.
- **Recording these notes does not authorize recording from an
  otherwise unauthorized source.** The settled authorized-session and
  authorized-signal-source rules stand unchanged; unfinished typing is
  never observed; no new capture path exists.

## 5. THE DUMB BOUNDARY — COMPLETE AND UNTOUCHED

These measurements may provide **physical recording-condition
context** — never conclusions. An acoustic-condition record must never
**itself assert** — and must never be **treated as sufficient by
itself to establish** — any of the following:

- identity conclusions;
- speaker-change conclusions;
- spoofing conclusions;
- imitation-risk conclusions;
- emotion;
- intention;
- communicative meaning;
- importance;
- behavioral-pattern conclusions;
- reasons why something occurred.

BOP produces only typed raw roots; it does not interpret, does not
conclude, and holds no data of its own — the settled §25.1 DUMB
boundary stands completely. **The precise downstream boundary:**
downstream components **may use** a condition record as
provenance-bearing physical recording-condition context under their
own accepted authority, evidence, uncertainty, and validation rules —
for example, a `high_ambient_noise` measurement may help SIA judge,
under SIA's own settled rules, whether a weak voice match could be
explained by poor recording quality. Downstream components **must not
silently convert** the physical measurement into an interpretation or
fact; anything interpretive built on it belongs to §7G or SIA under
their own settled rules, labeled, uncertain, and rejectable. **Every
downstream use must preserve** the original measurement, its
detection method, detection version, threshold value, measured value,
certainty scope, and source provenance. **The condition record remains
DUMB physical evidence even when a SMART or identity component later
considers it alongside other evidence** — never a fact smuggled in
through a signal note. A noisy room stays a noisy room; it may inform
a bounded judgment made elsewhere, but it never quietly becomes
"someone else was speaking," "Ness was upset," or "this matters."

## 6. EXPLICITLY OPEN

- **Exact numeric threshold values, detection algorithms, calibration
  data, device-specific tuning, hardware variation handling,
  false-positive handling, performance limits, and all implementation
  mechanics** — later technical design, testing, and build work; not
  selected by this policy package.
- **No schema or production system is changed merely because this
  candidate exists** — activation happens only through later,
  separately authorized implementation work.
- ChatGPT's independent audit of this actual file; Ness's separate
  acceptance of this package; the acceptance receipt and
  accepted-source placement.
- **B7**; **B15**; **B-INT-4**; **B-INT-5**; **B-INT-6**; **B-INT-7**;
  **B-INT-8**; Bundle 5 closure; later Map or Master integration;
  every implementation and coding task.

## 7. MUST-NEVER BOUNDARIES

This candidate — and any later work consuming it — must never: edit,
overwrite, rename, move, or delete any existing file; modify Master
V10, Defaults, cursorrules, the Companion, the Map, workflow files,
accepted packages, or historical candidates; add condition names
beyond the five accepted ones or alter the six record fields; choose
empirical thresholds or algorithms; create or widen any capture or
recording authorization; let a condition record **itself assert**, or
be treated as **sufficient by itself** to establish, an
identity, speaker-change, spoofing, imitation-risk, emotion, meaning,
intent, importance, pattern, or causation conclusion, or be silently
converted into an interpretation or fact — lawful provenance-bearing
contextual use under the receiving component's own accepted rules
stands per §5;
weaken the DUMB
boundary, capture identity, idempotency, failure, or crash-recovery
rules; treat folder placement as acceptance; create an acceptance
receipt from within this file; mark this package accepted, adopted,
authoritative, integrated, implemented, or built; mark Bundle 5
complete; begin B7, B15, or any B-INT package; or write code,
migrations, production schemas, patches, tests, or Cursor
instructions.

## 8. REQUIRED CHECKS — VERIFIED BEFORE DELIVERY

1. **Exactly five controlled physical condition names** — yes; the
   closed list in §2; nothing added anywhere in this file.
2. **Exactly the accepted record fields** — yes; the six fields in
   §2/§3; none added, none removed.
3. **DUMB boundary preserved** — yes (§5; §25.1's boundary restated
   completely and untouched).
4. **No identity, spoofing, emotion, meaning, intent, importance, or
   causation conclusion added** — yes; the notes never independently
   assert or establish any such conclusion and are never sufficient
   by themselves, while lawful bounded provenance-bearing contextual
   use under downstream components' own accepted rules is preserved
   (§5, §7).
5. **Method/version/threshold/measured value/certainty preserved** —
   yes; every classification must carry them (§3).
6. **No numeric threshold or algorithm invented** — yes; all
   empirical and mechanical choices explicitly open (§6).
7. **No unauthorized capture path created** — yes (§4; recording
   notes ≠ authorization; source rules unchanged).
8. **Recovery and idempotency rules preserved** — yes (§4; capture
   identity, durable sequence, retry, dedup, crash behavior all
   restated unchanged).

## 9. STATUS, CHANGE REPORT, AND SELF-AUDIT

**Status:** `CANDIDATE — NOT ADOPTED — NOT BUILT` — awaiting ChatGPT's
independent audit of this actual file and Ness's explicit acceptance
afterward.

**File created:**
`NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md`
— the only file created by this correction task, produced by copying
the identity-verified v1_0 base and applying only the precise-boundary
correction and its dependent edits (title; version note; §5 list
intro and downstream-boundary paragraph; §7 must-never item; check 4;
this section; the end line). v1_0 is preserved unchanged as historical
candidate evidence, and the A16 candidate is untouched. **Nothing
existing was modified:** Master V10, Defaults, cursorrules, the
Companion, the Map,
the plan, every accepted package, and all historical candidates remain
byte-identical at the pinned snapshot `bbf4e900…`. Nothing was
committed, pushed, moved, renamed, overwritten, or deleted. No
acceptance receipt was created; no Map or Master integration occurred;
no coding or implementation began; no schema or production system
changed.

**Self-audit:** decision recorded exactly — optional field, six exact
record fields, five exact controlled names, deterministic physical
classifications only — PASS. Each field explained in plain operational
language with certainty scoped to the physical classification alone —
PASS. Placement inside voice-channel `signal_measurements` with
one-root-per-channel, bundles, base schema, capture identity, durable
sequence, idempotency, failure, and crash recovery all preserved —
PASS. Observation-quality and third-party handling preserved — PASS.
DUMB boundary complete and intact, now with the precise downstream
boundary: never itself asserts, never sufficient by itself, lawful
bounded provenance-bearing contextual use preserved, no silent
conversion, full measurement provenance preserved in every use, DUMB
even when considered by SMART or identity components — PASS. All
empirical and implementation
choices left open; no threshold or algorithm chosen; no capture path
created — PASS. All eight required checks verified — PASS.

---

*End of
`NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md`
— `CANDIDATE — NOT ADOPTED — NOT BUILT`, awaiting ChatGPT's
independent audit and Ness's acceptance. v1_0 is preserved unchanged
as historical candidate evidence. BOP may now, at design level,
note the room the sound was recorded in — noisy, close, far,
reverberant, compressed — with the method, version, threshold, and
measured value that make every note checkable. The notes describe the
recording, never the person: they never themselves assert identity,
spoofing, emotion, meaning, importance, or "why," and are never
sufficient alone — though downstream components may weigh them as
bounded, provenance-bearing physical context under their own accepted
rules. Thresholds, algorithms, and all build work remain open. Nothing
existing changed; nothing was implemented.*

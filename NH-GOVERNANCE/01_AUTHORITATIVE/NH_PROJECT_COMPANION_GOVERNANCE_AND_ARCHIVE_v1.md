# N.H PROJECT COMPANION — GOVERNANCE, ACCEPTED DESIGNS, AND ARCHIVE

**Version:** v1
**Created:** 2026-06-28
**Status:** COMPANION, GOVERNANCE, ACCEPTED-DESIGN, AND PROVENANCE RECORD — NOT AN ARCHITECTURAL AUTHORITY

## Purpose

This file consolidates the current non-authoritative N.H project documents into one physical companion while preserving every embedded source byte-for-byte.

It does not replace or modify the current authoritative pair, and it does not replace the operational Cursor rules file.

## Current authority order

1. `NH_MASTER-19_CORRECTED_v7_1.md` — authoritative architectural Master.
2. `NH_DECISION_DEFAULTS-S19_v2_2.md` — authoritative behavioral defaults companion.
3. `.cursorrules` — operational Cursor rules at its required project filename and location.
4. This file — governance, accepted-design, handoff, and historical companion only.

Where an embedded historical source conflicts with the current authoritative pair, the current authoritative pair wins. Historical wording is preserved unchanged so provenance is not lost.

## Files that remain separate

- `NH_MASTER-19_CORRECTED_v7_1.md` — 291811 bytes; 1937 lines; SHA-256 `0e8b59e3ce8fd1b4f57367ff524fd2d467d905bb7a789745d13e7f81bd2665cf`
- `NH_DECISION_DEFAULTS-S19_v2_2.md` — 37048 bytes; 314 lines; SHA-256 `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696`
- `.cursorrules` — 34821 bytes; 717 lines; SHA-256 `5050d08825b93acd72a79d07946e43c8cbe537e079517ccfe66bcae8e30e96e9`

## Embedded-source preservation method

Every source below is placed after a machine-readable BEGIN marker containing its exact byte length and SHA-256 hash. The source's original bytes follow immediately. Verification reads exactly that byte length and compares the reconstructed SHA-256 hash with the original.

No wording inside an embedded source has been corrected, shortened, reordered, or normalized. Stale statements remain visible as historical statements rather than being silently rewritten.

## Embedded source manifest

1. `NH_SHARED_CHAT_HANDOFF_BEFORE_CONSOLIDATION_v1.md` — 6590 bytes; 185 lines; SHA-256 `47e6a8ba71fa7e90e8bb8ba671cad22291c950c2770d78e82eea6d331ca7d865`
2. `NH_WORKING_ROLES.md` — 3015 bytes; 49 lines; SHA-256 `a0281060abd7e7da791bb56a97316ab9ec41ab88fdd7884fac4c6434fa487619`
3. `NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md` — 71936 bytes; 1724 lines; SHA-256 `fb36bf8e55026ed7d79e4a5264be17f2577dda3276c4b2d2dc320018931f16f5`
4. `NH_ACCEPTED_TSC_DESIGN_v1.md` — 43237 bytes; 956 lines; SHA-256 `1da2e296d4345d11dcec5f197aa9a42883349526275c5aa32b0bb07d1ca44658`
5. `NH_wellbeing_baseline_system.md` — 7926 bytes; 140 lines; SHA-256 `afb1bad3c1edad3e86e76c5a1cb278b1a1e03c750d4fa1af6f54ad804bcc098c`
6. `NH_CHAT_HANDOFF_AFTER_BGMM.md` — 8081 bytes; 171 lines; SHA-256 `f524f7cdd4dd2f1b897177e0e7f0843d1c8a7767341e4a010da9ab066414a562`
7. `NH_MASTER-19_CORRECTED_v6.md` — 283081 bytes; 1908 lines; SHA-256 `8165f4bed94d2d57140d49e93d3c85b8e2b259053e0b30ac4c675fa7463a1bf9`
8. `NH_DECISION_DEFAULTS-S19_v1 (1).md` — 33328 bytes; 298 lines; SHA-256 `ecea9224163681f9fc1d29327b0453c5e7ead42fd178786ab9dc6a6d4e1baaa6`

---

# PART I — CURRENT GOVERNANCE AND HANDOFF

The following two sources record the current handoff/adoption state and the standing working-role rules. Their internal wording is preserved verbatim.


---

## I.1 — Current shared handoff before consolidation

<!-- NH_SOURCE_BEGIN filename="NH_SHARED_CHAT_HANDOFF_BEFORE_CONSOLIDATION_v1.md" bytes=6590 sha256=47e6a8ba71fa7e90e8bb8ba671cad22291c950c2770d78e82eea6d331ca7d865 -->
# N.H CHAT HANDOFF — AUTHORITATIVE STATE AND NEXT TASK

**Purpose:** This file is a shared handoff for both ChatGPT and Claude so a new chat can continue safely without relying on conversation memory.

**Created:** June 28, 2026

---

## 1. CURRENT AUTHORITATIVE FILES

The following pair has been explicitly adopted by Ness and is authoritative:

### Authoritative Master
- File: `NH_MASTER-19_CORRECTED_v7_1.md`
- SHA-256: `0e8b59e3ce8fd1b4f57367ff524fd2d467d905bb7a789745d13e7f81bd2665cf`

### Authoritative Decision Defaults
- File: `NH_DECISION_DEFAULTS-S19_v2_2.md`
- SHA-256: `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696`

These two files are the current authoritative N.H pair.

Earlier Master and Decision Defaults versions remain historical backups only and are not current authority.

---

## 2. ACCEPTED STANDALONE TSC DESIGN

The complete accepted Temporary Session Cache design remains a standalone companion specification:

- File: `NH_ACCEPTED_TSC_DESIGN_v1.md`
- SHA-256: `1da2e296d4345d11dcec5f197aa9a42883349526275c5aa32b0bb07d1ca44658`
- Status: `ACCEPTED DESIGN — NOT YET BUILT`

The Master contains the TSC integration summary, but this standalone file remains the complete accepted 31-section TSC specification.

---

## 3. OTHER CURRENT PROJECT FILES

These files remain relevant but are not the current authoritative Master/Defaults pair:

- `NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md`
  - Accepted security, identity, BOP, SIA, SACL, BAI, phone recovery, pairing, enrollment, and BGMM-related designs.
  - Companion/recovery source.
  - Not automatically authoritative where not yet patched into the Master.

- `NH_WORKING_ROLES.md`
  - Working-role rules for Ness, Claude, and ChatGPT.
  - Claude architects and prepares files.
  - ChatGPT independently checks contradictions, omissions, and no-loss claims.
  - Ness alone decides concept-level choices and adoption.

- Earlier Master files and earlier Decision Defaults files
  - Historical backups only.
  - Do not delete or overwrite during consolidation work.

---

## 4. VERIFIED ADOPTION HISTORY

### Master adoption
`NH_MASTER-19_CORRECTED_v7_1.md` was produced from `NH_MASTER-19_CORRECTED_v7.md` by changing only the adoption-status sentence.

Verification already completed:
- 1 line changed
- 0 lines deleted
- 0 unrelated lines changed
- Line count: 1,937
- SHA-256: `0e8b59e3ce8fd1b4f57367ff524fd2d467d905bb7a789745d13e7f81bd2665cf`

### Decision Defaults adoption
`NH_DECISION_DEFAULTS-S19_v2_2.md` was produced from `NH_DECISION_DEFAULTS-S19_v2_1.md` by changing only the Master sync, Master hash, and adoption-status header lines.

Verification already completed:
- 4 header lines changed
- 0 lines deleted
- 0 unrelated lines changed
- Line count: 314
- SHA-256: `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696`

No further adoption patch is pending.

---

## 5. CURRENT NEXT TASK

Ness wants to consolidate the current N.H project files from seven files into fewer than five files, preferably four, without losing, rewriting, weakening, or silently omitting any detail.

The next step is **proposal only**.

No file may be created, merged, modified, deleted, renamed, or replaced until Ness explicitly approves the proposal.

---

## 6. CONSOLIDATION REQUEST TO CONTINUE FROM

Use this exact task in the new chat:

> I want to consolidate the current N.H project files from seven files into fewer than five files, without losing, rewriting, or silently omitting any detail.
>
> First, inspect all current files and prepare a proposal only.
>
> Requirements:
>
> 1. Target four final files if possible.
> 2. Preserve the authoritative Master and Decision Defaults as separate files.
> 3. Identify which companion, accepted-design, working-role, and handoff files can safely be combined.
> 4. Do not merge unrelated authority levels without clearly separating them inside the combined file.
> 5. Preserve every accepted design, provenance statement, status label, hash, dependency, warning, and open question.
> 6. Show:
>    - proposed final filenames,
>    - which source files go into each,
>    - exact section order,
>    - authority status of each final file,
>    - duplication that may be removed,
>    - and any conflicts or stale references that require correction.
> 7. Do not create or modify any file yet.
> 8. Do not summarize away detailed designs.
> 9. Use a patch-only, no-loss method and preserve the original files unchanged.
>
> This is proposal-only. Wait for my explicit approval before creating consolidated files.

---

## 7. REQUIRED WORKING METHOD

For this consolidation task:

1. Inspect all relevant current files before proposing anything.
2. Verify filenames and hashes where available.
3. Treat the authoritative Master and authoritative Decision Defaults as separate and preserved.
4. Do not silently merge companion designs into authority.
5. Keep accepted-design status, historical provenance, and implementation status intact.
6. Surface stale references and conflicts instead of silently correcting them.
7. Preserve originals unchanged.
8. Produce a structural proposal first.
9. Wait for explicit Ness approval before creating any consolidated file.
10. After creation, perform a no-loss verification against every source file.

---

## 8. INTERACTION RULES FOR NESS

- Explain one step at a time.
- Use plain, everyday language first.
- Do not reopen settled design decisions.
- Do not make concept-level choices for Ness.
- Do not silently patch files.
- Do not tell Ness to move chats, stop, rest, or end a session unless he asks.
- When a file is requested, return the actual file.
- Preserve version history.
- Ness decides; Claude architects; ChatGPT checks.

---

## 9. STARTING STATE FOR A NEW CHAT

At the beginning of the new chat:

1. Confirm access to:
   - `NH_MASTER-19_CORRECTED_v7_1.md`
   - `NH_DECISION_DEFAULTS-S19_v2_2.md`
   - `NH_ACCEPTED_TSC_DESIGN_v1.md`
   - `NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md`
   - `NH_WORKING_ROLES.md`
   - this handoff file
2. Confirm the authoritative hashes listed in this file.
3. Do not modify anything.
4. Begin with the consolidation proposal only.

---

## 10. AUTHORITY NOTE

This handoff file is not itself an architectural authority file.

It records:
- the current authoritative pair,
- the accepted standalone TSC design,
- the verified adoption history,
- the next requested task,
- and the safe continuation procedure.

If this handoff conflicts with the authoritative Master or Decision Defaults, the authoritative pair wins.

<!-- NH_SOURCE_END filename="NH_SHARED_CHAT_HANDOFF_BEFORE_CONSOLIDATION_v1.md" -->

---

## I.2 — Working roles

<!-- NH_SOURCE_BEGIN filename="NH_WORKING_ROLES.md" bytes=3015 sha256=a0281060abd7e7da791bb56a97316ab9ec41ab88fdd7884fac4c6434fa487619 -->
# N.H — WORKING ROLES

**Purpose:** Defines who does what in the N.H project. This file is a standing rule for the working relationship, not an architectural authority. The complete N.H Master remains the source of truth for the system itself.

---

## The concept is Ness's

What N.H *is*, what it is for, what it should feel like, and what it must refuse to do all come from Ness. These are not design choices to be proposed by anyone else — they are the foundation, and they belong to Ness alone.

Ness brought in help for one thing: the **bridge** between that concept and a working technical design — connecting the dots from the start of the project to the end, which is a skill, not a vision. Help was never meant to reach into the concept itself or decide how things should work.

---

## Claude's role — architect the bridge

- Develop the technical design that turns Ness's concept into something that holds together and can eventually be built.
- Take one decision at a time when Ness asks for that; explain options, consequences, and a recommendation.
- Mark every proposal clearly as a proposal until Ness decides.
- Never close a concept-level question on Ness's behalf. When a choice belongs to the concept rather than the bridge, hand it back to Ness.

---

## ChatGPT's role — check the bridge

- Catch contradictions, inconsistencies, and stale or conflicting wording.
- Catch technical gaps, missing dependencies, and broken cross-references.
- Catch places where a proposed design would not actually hold together or would violate a settled rule.
- Verify that the design stays faithful to the concept Ness has set.

ChatGPT's job is **not** to propose what the system should do, how a concept should work, or which direction a design choice should go. When something is unclear or undecided, ChatGPT surfaces it to Ness as an open question — names the gap, explains why it matters — and lets Ness decide. It does not fill it in.

If ChatGPT believes a design choice is needed, it says so and hands it to Ness. It never resolves it for him.

---

## Ness's role — the decider

Ness decides where the bridge goes and why it exists. Every decision about what N.H actually *is* stays with him. A checker tells him whether something is consistent; it never tells him what to believe is real.

---

## The line that applies to both AIs

The point is not which AI does what. The point is that **neither Claude nor ChatGPT quietly takes the wheel.** If either one sees the other proposing something that should have been Ness's call rather than Ness's decision to make, that is worth flagging to Ness. Concept and meaning stay with Ness; the two AIs build and check the bridge between his concept and a working design.

---

*This file records the working relationship. It is consistent with the existing project notes ("Claude develops design; Ness and ChatGPT check it") and sharpens the line between the concept, which is Ness's, and the bridge, which the AIs help build and check.*

<!-- NH_SOURCE_END filename="NH_WORKING_ROLES.md" -->

---

# PART II — ACCEPTED SECURITY AND IDENTITY DESIGNS

The source below is an accepted-design companion. Its internal references to older authority filenames are preserved as written; the current authoritative pair listed at the top of this file governs today.

<!-- NH_SOURCE_BEGIN filename="NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md" bytes=71936 sha256=fb36bf8e55026ed7d79e4a5264be17f2577dda3276c4b2d2dc320018931f16f5 -->
# NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md

## Provenance

This file consolidates the complete final accepted designs produced during the
security, identity, speaker access, and Biometric-Gated Maintenance Mode design
branch in the Claude project chat. All designs were reached through iterative
correction and explicit acceptance by Ness.

This file is a **companion record**, not an authoritative source. It does not
replace, supersede, or modify the N.H Master (`NH_MASTER-19_CORRECTED_v6.md`),
the Decision Defaults (`NH_DECISION_DEFAULTS-S19_v1__1_.md`), or any
implementation file. These designs must be formally patched into the Master
through the accepted patch-only, no-loss protocol before they carry Master
authority.

Every superseded draft and every rejected wording from earlier iterations has
been removed. Only final corrected accepted text is preserved here.

---

## Contents

1. BOP — Behavioral Observation Processing (detailed design)
2. Other-Speaker / Guest / Known-Person Architecture (high-level, final)
3. SIA — Speaker Identity Assessment (detailed design)
4. SACL — Speaker Access-Control Layer (detailed design)
5. Wellbeing / Identity / Security Separation Rules
6. BAI — Biometric Authorization Interface (detailed design)
7. Initial Owner-Phone Pairing
8. Recovery-Code Lifecycle (creation, verification, local test, activation, rotation)
9. Future-Phone Replacement Flow
10. Atomic Emergency Recovery Flow
11. Initial Ness Voice-Profile Enrollment Bootstrap
12. Formally Adopted Vocabulary Additions
13. BGMM — Biometric-Gated Maintenance Mode (detailed design)

---

## Status Label

Every component in this file carries the status:

**ACCEPTED DESIGN — NOT YET BUILT**

No component described here has been implemented in code, verified on disk, or
patched into the Master.

---

## Build-Time Implementation Settings (not unresolved concept decisions)

The following two items are confirmed build-time settings, not open concept
decisions requiring Ness:

- **Maintenance timeout duration:** set empirically after observing actual
  maintenance operation durations in deployment. The architecture supports any
  value; the value itself is a calibration decision.
- **Hardware-backed key implementation:** the specific mechanism for the
  manifest-signing key and the rollback-sealing key (TPM sealed keys, HSM,
  OS secure key store, or equivalent on Ness's motherbase hardware) is chosen
  at build time based on available hardware. The architecture requires
  hardware-backed separation; which specific mechanism is used is a build
  decision.

---

---

# 1. BOP — Behavioral Observation Processing

**ACCEPTED DESIGN — NOT YET BUILT**

## What BOP Is and Is Not

BOP is the set of rules that decide when something that happened during an
authorized session should be recorded as a behavioral observation root, what
fields it carries, and how it enters the shared store through §7E. BOP produces
only typed raw roots. It does not interpret. It does not conclude. It holds no
data of its own. It is a source-classification and capture-normalization
processing responsibility.

BOP is not a store, not a model of Ness, not a pattern system, not an analysis
layer, and not a classifier of meaning. All interpretation belongs to §7G.

## What Counts as a Behavioral Observation

A behavioral observation is any event that occurred during an authorized session
that is directly and physically measurable without interpretation. The test is
§7E's enrichment boundary test: does this describe what physically happened, or
does it explain what it means? If it explains meaning, it is not a BOP
observation.

**Authorized session definition:** any session explicitly opened by Ness with
N.H is authorized for behavioral observation. During an authorized session, N.H
may automatically record all available authorized signals as observations.

**Authorized signal sources:** live voice mode during an active session;
confirmed sent text during an active session; session-level state events;
imported authorized content when explicitly imported by Ness. Unfinished typing
is never observed. Signals from unauthorized sources are never observed.

## V1 Controlled Event Type Vocabulary

All event types carry physical descriptions only. The vocabulary is extensible
via the `extended` event type using a registered `extended_event_type_id`.

**Voice events** (live voice mode or authorized imported recordings):
- `voice_onset` — a vocalization began; role field identifies whose voice
- `voice_offset` — a vocalization ended
- `silence_interval` — a silence interval; duration only; no judgment
- `non_word_sound` — a non-language sound; physically typed as `breath` or
  `non_breath_non_word` only
- `voice_overlap` — two voice channels simultaneously active
- `voice_interrupt_of_nh` — Ness's voice began while N.H's TTS was active;
  carries timestamp and position in N.H output stream
- `pitch_measurement` — raw pitch values [hz_min, hz_max, hz_mean] for an
  interval; measurement_method and measurement_version required; no emotional label
- `amplitude_measurement` — raw amplitude/energy for an interval; same
  provenance requirements

**Text events** (confirmed sent messages only):
- `text_message_sent` — confirmed sent; carries character_count, word_count,
  sentence_count_approx, exact_text_reference (root id of the conversational
  root carrying content; BOP does not copy message content)
- `text_response_timing` — raw ms delta between N.H output completing and this
  message; reference to the N.H output event
- `no_response_session` — session opened and closed with zero sent messages

**Interface and system command events** (deterministic interface events only):
- `system_command` — a defined interface command; carries command_identifier
  from the interface command registry; no interpretation of ordinary language

**Session state events:**
- `session_opened`, `session_closed`, `session_interrupted`, `function_started`,
  `function_completed`, `function_interrupted`, `capture_failure`

**Import events:**
- `import_authorized`, `import_processed`

**Extended event type:**
- `extended` — for newly measurable authorized signals not in v1; carries
  `extended_event_type_id` (registered before first use) and `raw_payload`

## Observation Root Schema

Base 7 fields (existing sealed schema, unchanged):

```
id:            corrected capture_id (see below)
subject:       "bop:v1"
timestamp:     BOP capture time (distinct from event_occurred_at in payload)
content:       BOP payload serialized as string
re_reads:      []
source_title:  session grouping key using existing source_title rules
role:          "ness" | "nh" | "session" | "third_party_observed"
```

BOP payload inside `content`:

```
bop_payload
  bop_schema_version:      "bop_v1"
  event_type:              string from controlled vocabulary or "extended"
  extended_event_type_id:  string or null
  extended_event_type_version: string or null
  event_occurred_at:       ISO 8601 — when the event happened
  event_duration_ms:       integer or null
  session_id:              stable identifier for the authorized session
  session_mode:            "voice" | "text" | "imported_audio" |
                           "imported_video" | "imported_text" | "mixed"
  session_authorization:
    authorization_type:    "live_session" | "manual_import" |
                           "enrollment_declared"
                           [enrollment_declared: formally adopted vocabulary
                           addition — see section 12]
    authorization_event_id: reference to the authorization event root id
  participants:            list of participant_record objects
  signal_measurements:     object containing raw physical measurements;
                           structure varies by event_type; no interpreted label
  simultaneous_bundle_id:  string or null
  simultaneous_bundle_position: integer or null
  observation_quality:     object (see below)
  third_party_flag:        object (see below)
  connection_anchors:      list of anchor_record objects (may be empty)
  bop_processor_version:   string
  capture_method:          "live_capture" | "import_processing" |
                           "session_state_event"
  capture_sequence_number: integer — monotonically increasing within session;
                           used in capture_id construction
```

## Corrected Capture ID

```
capture_id = stable_hash(
  session_id,
  event_type,
  event_occurred_at,
  event_duration_ms,         (or "null" if absent)
  capture_sequence_number,   (unique within session)
  bop_processor_version
)
```

`capture_sequence_number` must be persisted in a local durable log before any
write is attempted, ensuring idempotency across retries.

## Observation Quality

```
observation_quality
  signal_quality:          "clean" | "partial" | "degraded" | "reconstruction"
  signal_quality_note:     string or null
  field_completeness:      list of field_status records:
    field_name, status, status_note, fallback_value_used, fallback_basis
  overall_completeness:    "complete" | "partial" | "minimum_viable" |
                           "below_threshold"
```

All roots including below-threshold enter the sealed root store. Incompleteness
is recorded honestly; the Meaning Engine may return insufficient_context.

## Third-Party Flag

```
third_party_flag
  third_party_present:           boolean
  third_party_content_present:   boolean
  third_party_handling:          "ness_only" | "third_party_presence_noted" |
                                 "third_party_content_reference"
  privacy_rule_version:          string
```

§7Q's sensitivity levels, deletion framework, and pre-output review apply to
BOP roots identically to any other root.

## Multiple Simultaneous Signals

One observation root per signal channel. All roots from the same simultaneous
moment share the same `simultaneous_bundle_id`. The bundle is reconstructible.
Separate roots per channel preserves the sealed root schema's single-role
constraint.

## Later Reconnection

Connection anchors are optional retrieval aids. Any root is reconnectable
through §7H condition-based rereads and §7F semantic retrieval regardless of
whether anchors were pre-registered. Anchors may be empty.

## DUMB Boundary — What BOP Must Never Produce

BOP must never produce: emotional labels, identity conclusions, speaker-change
detections, spoofing assessments, meaning attributions, pattern conclusions,
importance judgments, or any field that requires reasoning about why something
happened. All of these belong to §7G or SIA.

## Failure, Recovery, Idempotency

On capture failure: `capture_failure` event root written; gap recorded honestly.
On write failure after capture_id computed: retry uses same capture_id;
`append_root()` absorbs duplicate. On crash mid-session: `session_interrupted`
event root written on restart; observations not captured before crash are not
reconstructed.

## Proposed BOP Schema Amendment (Pending Separate Review)

`acoustic_condition_notes` field for voice channel `signal_measurements`: a
list of named physical condition records, each carrying condition_name,
detection_method, detection_version, threshold_value, measured_value,
certainty. Condition names are deterministic physical classifications only
(`high_ambient_noise`, `close_microphone`, `far_microphone`,
`room_reverb_present`, `signal_compression_heavy`). Each carries the numeric
threshold and measured value so the classification is reproducible. This
amendment requires separate consistency review before adoption.

---

---

# 2. Other-Speaker / Guest / Known-Person Architecture

**ACCEPTED DESIGN — NOT YET BUILT**

## Core Principle

The whole N.H mechanism remains active at every access level. Speaker access
control gates what may be surfaced to the current speaker — not what the
mechanism holds or processes internally. Internal understanding and external
disclosure are permanently separate.

## Protected Rules (Unconditional)

- Guest speakers cannot access private Ness memory.
- Uncertainty reduces access; it never expands it.
- Voice alone cannot unlock top-security information.
- Top-security always requires both fingerprint verification and independently
  sufficient active-speaker SIA confidence with no disqualifying suspicion.
- Hidden information must not be indirectly acknowledged.
- One person's permissions must not transfer to another.
- N.H may use information internally only within privacy and authority rules.
- Internal understanding does not equal permission to reveal.
- Other people cannot change permissions, memories, security rules, system
  authority, or N.H's behavior.
- Ness also cannot override the protected architectural core, immutable roots,
  provenance, or non-negotiable safeguards.
- N.H is not a Truth Engine. Claims remain attributed to their speakers.

## Access Levels

Four levels, determined by SACL from SIA's output. The whole mechanism is
active at all levels; only permitted disclosure changes.

- **top_security:** biometric verified + Ness recognized at high certainty + no
  spoofing suspicion
- **recognized_ness:** Ness recognized at threshold certainty + no disqualifying
  suspicion; no biometric required
- **known_person:** confirmed non-Ness Person-Box recognized at threshold + valid
  active PBR
- **guest:** all other conditions

## Guest Mode

Uses general conversational capabilities. No material from the shared store
containing Ness-personal content is accessible. N.H does not say "I cannot tell
you" or signal hidden material exists. It responds naturally from available
content.

## Known-Person Permissions

Permission Boundary Records (PBRs) are maintained by the mechanism under
protected authority rules, informed by Ness's expressed boundaries and learned
evidence. No other person has authority over PBRs. Ness may express boundaries
directly; the mechanism learns and adapts these under §7P authority rules.
Neither Ness nor anyone else may override the protected core.

Permission categories (open-ended vocabulary, initial list): `family_information`,
`health_information`, `nh_project_information`, `creative_projects`,
`current_plans`, `shared_memories`, `practical_information`.

## Separate Parent Identities

Each parent has a fully separate Person-Box, voice profile, behavioral pattern
readings, PBR, relationship context in §7D, and translation behavior history.
N.H never treats parents as one combined person.

## Parent Translation

Entirely request-driven. N.H never autonomously joins, intervenes in, or
redirects a family conversation. Translation is requested by Ness:

- "What did [parent] mean?" → Meaning Engine reading of parent's statement,
  delivered to Ness only, labeled as N.H's interpretation with uncertainty.
- "How should I say X to [parent]?" → candidate wordings delivered privately to
  Ness; N.H does not speak to the parent.
- Ness asks N.H to speak to a parent → N.H delivers the requested content with
  automatic tone/wording adaptation within the request scope.

Translation output is a reading in the shared store, revisable through §7H.
N.H may use private Ness context internally for translation understanding;
disclosure to the parent is bounded by the parent's PBR categories.

## Statements About Ness

A third party's statement about Ness remains attributed to that speaker throughout
the entire path — in the TSC, in the promoted root, in the Meaning Engine reading.
It never silently becomes a fact about Ness. Later evidence may trigger §7H
rereads. The original root and reading are never altered.

## Person-Box Visibility

Another person may not inspect their full Person-Box, hidden readings, private
observations, internal relationship models, or stored security information.
N.H answers only from what their current access level permits. N.H must never
reveal how much it has stored or how recognition works.

## Temporary Session Cache

Third-party session material enters a Temporary Session Cache (TSC) rather than
the long-term shared store. The TSC uses §7E's pre-ingest holding area with a
new blocker: `pending_fingerprint_authorization`. Held material is invisible to
the Meaning Engine while held. The cache preserves complete session context
including Ness's words when they give meaning to another person's statements.

TSC lifecycle: `active` → `sealed` (on session close) → `authorized` (after
fingerprint) → `promoting` → `promoted` or `promotion_failed`.

## Fingerprint-Authorized Batch Promotion

Ness provides a thumbprint in a later session. This authorizes the complete
pending TSC from the relevant completed session. Ness does not select individual
people, memories, or items. The relevant session's cache is the authorization
unit. Unrelated sealed caches from other sessions are not automatically promoted.

After authorization: all items in the cache with no remaining blockers proceed
through §7E → sealed store → §7G → readings → §7J → §7M → §7L proposals. No
additional manual Ness approval is required after the fingerprint authorization.
The mechanism processes the material under its settled evidence rules.

## Continuous Speaker Security

SIA assesses identity continuously throughout a session. SACL applies the
fail-closed rule: uncertainty reduces access, never expands it. Speaker changes
trigger immediate access recalculation. Spoofing suspicion at medium or higher
drops access to guest immediately and queues a private Ness alert. No routine
live voice challenges are issued.

---

---

# 3. SIA — Speaker Identity Assessment

**ACCEPTED DESIGN — NOT YET BUILT**

## What SIA Is and Is Not

SIA assesses who is probably speaking and whether incoming audio shows
characteristics of replayed, synthetic, converted, or non-live audio. It does
not make access decisions (SACL does). It does not interpret meaning (§7G does).
It does not store content. It reads BOP roots and produces identity assessments
and security audit events.

## Speaker Session State (SSS)

In-memory, maintained throughout the active phone session. On restart, SSS is
lost and all streams default to unknown/guest assessment.

```
speaker_session_state
  session_id
  session_mode:             "voice" | "text" | "mixed"
  active_voice_stream_set:  list of voice_stream_record
  primary_addressed_stream: stream_id of stream N.H is responding to
  biometric_state:          "verified" | "not_verified" | "expired"
  biometric_verified_at:    timestamp or null
  assessment_history:       append-only list within the session
```

## Voice Stream Record

```
voice_stream_record
  stream_id
  onset_event_id:           BOP root id of the voice_onset that opened this stream
  speaker_assessment:       speaker_assessment object
  anti_spoofing:            anti_spoofing_assessment object
  stream_status:            "active" | "paused" | "ended"
  last_assessment_at:       timestamp
  last_assessment_trigger:  named trigger
```

## Speaker Assessment Object

```
speaker_assessment
  identity_candidates:      ranked list — all Person-Box candidates above
                            minimum reporting threshold; none silently discarded:
    candidate_record:
      person_box_id
      match_score:          [0.0, 1.0]
      evidence_dimension_scores:
        voice_acoustic_match
        behavioral_pattern_match
        branch_continuity_score
        session_continuity_score
        timing_rhythm_score
        wording_pattern_score
        device_biometric_state: "verified" | "not_verified" | "expired"
      uncertainty_flags:    list of named flags for this candidate
      profile_status:       "enrollment_provisional" | "enrollment_active" |
                            "calibrated" | "stale" | "absent"

  assessed_person_box_id:   leading candidate id, or null when:
                            (a) no candidate reaches minimum certainty, or
                            (b) leading candidate lacks sufficient score
                                separation from competing candidates
  assessed_certainty:       [0.0, 1.0] or null when assessed_person_box_id null
  active_flags:             union of flags active across leading and near-competing
                            candidates; vocabulary:
                            "speaker_change_possible"
                            "spoofing_suspected"
                            "imitation_risk"
                            "profile_provisional"
                            "profile_stale"
                            "low_evidence"
                            "degraded_signal_conditions"
  profile_status:           status of leading candidate's profile or null
```

`assessed_person_box_id` is null whenever two candidates are within the minimum
separation threshold. SACL treats null as unknown and applies guest.

## Anti-Spoofing Assessment Object

Contains only evidence that audio may be replayed, synthetic, converted, or
non-live. Conversational divergence does not appear here.

```
anti_spoofing_assessment
  suspicion_level:          "none" | "low" | "medium" | "high"
  suspicion_basis:          list — acoustic spoofing signals only:
                            "playback_artifact_detected"
                            "compression_artifact_detected"
                            "synthetic_speech_trace"
                            "microphone_room_inconsistency"
                            "pattern_too_uniform"
  suspicion_source:         reading ids that produced these assessments
  assessment_certainty:     [0.0, 1.0]
```

`branch_discontinuity`, timing changes, wording differences, and conversational
divergence are NOT in anti_spoofing_assessment. They appear in
`evidence_dimension_scores` within `identity_candidates` or in a separate
imitation-risk assessment.

## SIA Output Interface

SIA produces one output per assessment cycle. Contains no access decisions.

```
SIA_output
  speaker_session_state:      full SSS object
  assessment_event_id:        stable id for this assessment cycle
  assessment_confidence_note: "normal" | "degraded_conditions" |
                              "provisional_profile" | "low_evidence"
                              — audit label only; not used as decision input
```

## Assessment Update Cadence

Assessment runs continuously across bounded audio windows while speech is
active, and on each named trigger:

- `voice_onset`
- `acoustic_window` — periodic update while stream is active; window size is
  empirical implementation decision
- `meaningful_acoustic_change` — significant shift in acoustic measurements
- `overlap_detected`
- `speaker_transition`
- `confirmed_text_sent`
- `biometric_event`
- `session_state_change`

## Diarization

SIA maintains a `voice_stream_record` per detected voice stream. Multiple
parallel streams exist during overlap or interruption. Each is assessed
independently. If two profiles produce similar scores, both are reported;
`assessed_person_box_id` may be null rather than silently resolved.

## Voice Profile Architecture

Profiles are sets of readings in the shared store linked to a Person-Box through
§7L. All profiles use a common technical embedding space for comparison. What is
protected is the separation of identity authority: no merged profiles, no shared
identity authority, no silent reassignment. Each comparison is independent.

## Natural Voice Variation

Voice profiles represent a range, not a fixed point. Readings from BOP roots
across varied conditions (time, room, device position, state) build the range.
When voice acoustic match drops but other dimensions remain strong, combined
certainty may remain above threshold. Physical acoustic conditions (from the
proposed `acoustic_condition_notes` BOP amendment) contextualize low match
scores.

## Training Eligibility Rules

A BOP acoustic root may contribute to a voice profile only if all of these hold:

1. Produced during an authorized session.
2. SIA certainty for this stream at capture time ≥ training_eligibility_threshold.
3. Anti-spoofing suspicion_level = "none" at capture time.
4. Not flagged in the security audit log with spoofing-related events.
5. For Ness's profile: session was biometric-verified or recognized_ness level
   continuously throughout, with no identity uncertainty flags.
6. Root has completed §7E → §7G reading path before contributing.

Psychiatric or medical appointment records are not voice-identity training
evidence.

## The 6–10 Month Learning Period

During calibration: certainty thresholds set conservatively; recognized_ness is
the maximum achievable level for a provisional profile; behavioral, branch, and
contextual dimensions carry proportionally more weight than voice acoustic match.
Conservativeness reduces gradually as evidence accumulates.

## Raw Voice Data Protection

Raw acoustic roots are in the sealed root store (Layer 3 Full Protected). Voice
profile readings are in the readings store under the same protection rules. No
voice profile reading, acoustic root, or anti-spoofing reading is accessible at
access levels below recognized_ness. Never transmitted outside the local device
except through the Full Mode tunnel under biometric-verified conditions.

## Identity Uncertain vs. Spoofing Suspected

These are distinct events with distinct responses:

- **Identity uncertain:** certainty below threshold; may be natural variation,
  unknown speaker, noise. No private Ness alert. SIA continues assessing; may
  recover naturally.
- **Spoofing suspected (low):** acoustic evidence present. Access drops to guest.
  No alert yet. SIA monitors closely.
- **Spoofing suspected (medium or high):** access drops to guest immediately.
  Top-security relocks. Private Ness alert queued. No routine voice challenge.

## False Lockout Recovery

Primary: thumbprint verification. Biometric success satisfies the biometric
factor. Top-security requires biometric AND independently sufficient speaker
recognition AND no spoofing flag — fingerprint alone does not restore top-security
if speaker assessment remains uncertain or suspicious.

No routine voice challenges are issued. System monitors and updates naturally, or
Ness uses the thumbprint.

## Multi-Speaker State

`active_voice_stream_set` holds one `voice_stream_record` per detected stream.
`primary_addressed_stream` identifies who N.H is responding to.

SACL uses SIA's multi-stream output to calculate per-stream access levels and
the shared-output level (minimum of all active streams for content visible to
all). SACL owns those calculations; SIA provides the evidence.

## Minimum Evidence for Person-Box Linking

Before an unknown speaker may be linked to a Person-Box:
1. Minimum quantity of attributed voice material across authorized sessions.
2. Attribution certainty above minimum at time of capture.
3. No spoofing flags on attributed material.
4. Material promoted from TSC through fingerprint-authorized path and processed by §7G.
5. §7G readings support the connection above minimum reading confidence.
6. §7L proposal-based creation rules satisfied; no silent merge.

## Compact Profile Representation

Derived from authoritative readings; non-authoritative; locally protected;
versioned; rebuildable from source readings; never replaces original evidence;
invalidated when source readings change or become stale. Not a second profile
store. Used at inference time only.

## Settled Rules

- Routine live voice challenges are prohibited.
- Medium-or-higher spoofing suspicion: access drops to guest silently; private
  Ness alert queued; no in-conversation indication.
- SIA assesses identity and suspicion only. SACL decides access.

---

---

# 4. SACL — Speaker Access-Control Layer

**ACCEPTED DESIGN — NOT YET BUILT**

## What SACL Is and Is Not

SACL receives SIA's assessments and decides what the current speaker is permitted
to receive or do. It owns all authorization decisions. It does not assess identity,
perform acoustic analysis, interpret meaning, retrieve content, or generate output.

The whole N.H mechanism remains active at every access level. SACL controls what
may be surfaced — it does not create a reduced version of N.H.

## SACL-Owned State

```
SACL_session_state
  session_id
  last_sia_event_id
  last_sia_received_at
  stream_authorization_set:  list of stream_authorization_record
  primary_addressed_stream
  shared_output_level:       minimum access level across all active streams
  shared_output_level_since
  in_progress_operations:    list of in_progress_operation_record
  last_audit_event_id
```

```
stream_authorization_record
  stream_id
  person_box_id:             or null
  stream_access_level:       "top_security" | "recognized_ness" |
                             "known_person" | "guest"
  stream_access_level_since
  pbr_version:               or null
  ness_presence_satisfied:   boolean
  active_disqualifiers:      list of named conditions preventing level from rising
```

## Access Level Calculation

Calculated per-stream on every SIA assessment event. `shared_output_level` is
the minimum across all active streams.

**Gate 0 — Disqualifier check (acoustic spoofing only):**

Triggers on:
- `anti_spoofing.suspicion_level = "medium"` or `"high"`
- `active_flags` contains `"spoofing_suspected"`

Result: `stream_access_level = "guest"`. Medium-or-higher suspicion additionally
queues private Ness alert. STOP.

The `"imitation_risk"` flag does NOT trigger Gate 0.

**Gate 1 — top_security:** requires ALL of:
- `biometric_state = "verified"` within timeout
- `assessed_person_box_id` = Ness's Person-Box
- `assessed_certainty` ≥ top_security_certainty_threshold
- Leading candidate has sufficient score separation
- `anti_spoofing.suspicion_level = "none"`
- No active disqualifiers
- `active_flags` does NOT contain `"imitation_risk"`

**Gate 2 — recognized_ness:** requires ALL of:
- `assessed_person_box_id` = Ness's Person-Box
- `assessed_certainty` ≥ recognized_ness_certainty_threshold
- Leading candidate has sufficient score separation
- No disqualifying spoofing or imitation-risk flags
- No active disqualifiers

The `"imitation_risk"` flag blocks Gate 1 only. It does not reduce Ness to guest.
Natural behavioral divergence from stress, illness, or emotion produces
imitation_risk without triggering Gate 0.

**Gate 3 — known_person:** requires ALL of:
- `assessed_person_box_id` = confirmed non-Ness Person-Box
- `assessed_certainty` ≥ known_person_certainty_threshold
- Sufficient score separation
- Valid active non-revoked PBR exists
- Ness-presence requirement satisfied if PBR requires it
- No active disqualifiers

**Else:** `stream_access_level = "guest"`

All thresholds are empirically calibrated configuration values.

## Fingerprint as One Independent Factor

`biometric_state = "verified"` satisfies the biometric factor only. Gate 1
requires this plus independently sufficient speaker recognition. If the active
speaker remains uncertain or suspicious after fingerprint success, top-security
remains locked. Fingerprint alone does not restore top-security.

## Imitation Risk Policy (Ness's Decision — Option A)

Conversational or behavioral imitation risk blocks top-security only. It does
not reduce Ness to guest and does not remove recognized_ness access. Natural
causes of behavioral divergence — stress, tiredness, illness, emotion, overload —
may produce the imitation_risk flag without any attack occurring.

## Three Mechanisms Kept Separate

- **SIA:** who is probably speaking; does audio show non-live characteristics?
- **§22 Wellbeing Baseline:** is Ness showing sustained divergence across
  multiple sessions? Its tiered actions affect REALITY growth only. It does not
  erase identity, convert Ness to guest, or suppress SIA recognition.
- **SACL:** based on identity and security evidence, what may be revealed?

SACL does not read wellbeing tier state. One unusual session is not a wellbeing
security event. Behavioral divergence follows the imitation-risk path; acoustic
spoofing follows Gate 0. These paths never merge.

## Multi-Speaker Sessions

`shared_output_level` = minimum across all active streams.
Per-stream private output (e.g. translation to Ness only) may use the individual
stream's access level if the output path is private and unobservable by others.

Ness-presence requirement: when a known person's PBR has `ness_presence_required
= true`, elevated access applies only while a Ness stream is active at
recognized_ness or above. If Ness's stream drops below that level, the known
person's stream drops to guest simultaneously.

## Permission Boundary Enforcement

SACL reads PBRs via LMAC → §7L at Gate 3. Per-output permission category check
runs at output time against `permission_categories` in the active PBR. No content
outside permitted categories is surfaced to the known-person speaker. SACL holds
a cached copy of each recently-used PBR; refreshed when PBR version changes.

## Access Changes During In-Progress Operations

On any access reduction: SACL compares new level against each in-progress
operation's `material_sensitivity`. If the new level is below material_sensitivity,
the operation is flagged for immediate discard. The output-generation component
receives a discard signal before any output channel is written. No partial output
from a higher-sensitivity operation is delivered.

## Avoiding Indirect Disclosure

SACL specifies the permitted access level and permission categories to LMAC
when initiating context retrieval for any function. LMAC queries the shared
mechanism only for material within those boundaries. The content-generation
component never sees content above its permitted level and cannot reveal its
existence — not through direct statement, not through structural gaps, not through
implied omission.

## Output Gate (Two Factors, Sequential)

1. §7Q privacy gate — must pass.
2. SACL access gate — content must fall within current access level and (for
   known_person) permitted PBR categories.

If either gate fails: content withheld. Response generated from permitted content
only. No signal that more exists.

## Internal Context vs. External Disclosure

SACL controls what may be revealed or done for the current speaker. It does not
make the whole mechanism blind to protected context when internal processing is
permitted. The complete shared mechanism remains active internally. Only permitted
information and actions may reach the current speaker through the output gate.

## Background Functions

Background functions operate according to their own purpose, authority, privacy,
and function rules. They do not become guest-level merely because no active
speaker stream is present. A background function authorized during a Ness session
continues under those rules unless a specific security event revokes that
authorization.

## Failure, Stale Assessments, Fail-Closed

On SACL restart: all streams → guest; all in-progress operations discarded.
On stale SIA assessment: all streams above guest downgraded; disqualifier
`"assessment_stale"` added; SACL continues at guest until fresh SIA output arrives.
On SIA component failure: all streams → guest; audit event written immediately.
On PBR query failure: Gate 3 fails closed; stream → guest.

## Protected-Core Rules (Unconditional)

- Voice alone never unlocks top-security.
- Unknown or uncertain speakers receive guest unconditionally.
- Medium-or-higher spoofing: guest + Ness alert, unconditionally.
- No routine live voice challenges.
- Other people cannot change permissions or security levels through SACL.
- Ness cannot override protected architectural safeguards through SACL.
- Hidden information is never indirectly acknowledged.

---

---

# 5. Wellbeing / Identity / Security Separation Rules

**ACCEPTED DESIGN — NOT YET BUILT**

These three mechanisms are kept strictly separate:

**SIA:** who is probably speaking; does audio show non-live characteristics?
SIA never diagnoses wellbeing. SIA never produces conclusions about Ness's mental
or physical state.

**§22 Wellbeing and Behavioral Baseline System:** is Ness showing sustained
divergence from his own demonstrated long-term baseline across multiple sessions
and types of interaction? One unusual session is treated as possible noise. Tiered
actions: silent flag → mirror signal → REALITY promotion throttling → REALITY
promotion freeze. These affect REALITY growth and integrity only. They do not
erase Ness's identity, remove SIA's recognition, convert Ness to guest, or
suppress recognized_ness access. Dry mode, research, and normal thinking-partner
operation remain available.

**SACL:** based on current identity and security evidence from SIA, what may be
revealed or done for the current speaker? SACL does not diagnose wellbeing. SACL
does not read wellbeing tier state. SACL does not treat behavioral divergence
captured in SIA's identity dimensions as acoustic spoofing evidence.

**Psychiatric and medical appointment records:** wellbeing calibration anchors
and the REALITY-freeze unlock mechanism only. Not voice-identity training
evidence. Not identity proof. Not access-control evidence.

**Temporary off-baseline behavior:** tiredness, stress, illness, or emotion may
produce SIA's `"imitation_risk"` flag. SACL applies Option A: top_security
blocked; recognized_ness remains. The wellbeing system observes the session as
one data point. No automatic guest downgrade. Ness retains recognized_ness
access and full thinking-partner capability.

**Acoustic spoofing:** SIA produces `suspicion_level = "medium"` or `"high"` in
`anti_spoofing_assessment`. SACL Gate 0 fires: stream → guest, top-security
relocks, private Ness alert queued. This is a security event. The wellbeing
system is uninvolved.

The two paths — behavioral divergence (imitation-risk) and acoustic spoofing
(Gate 0) — never merge. SACL never conflates them.

---

---

# 6. BAI — Biometric Authorization Interface

**ACCEPTED DESIGN — NOT YET BUILT**

## What BAI Is and Is Not

BAI is the narrowest possible interface between the phone's native biometric
hardware and N.H. It receives OS authentication results. It produces
purpose-bound, one-time-use authorization tokens (or a revocable top-security
lease) containing no biometric data. It owns no fingerprint data at any stage.

BAI is not an authentication system, not an access-control system, and not a
session manager. It receives, binds purposes, creates local proofs, and audits.

## What BAI Receives From the OS

```
os_biometric_result
  outcome:          "success" | "failure" | "cancelled" | "timeout" |
                    "lockout" | "error"
  os_error_code:    string or null — audit only; never exposed to components
  os_lockout_type:  "temporary" | "permanent" | null
```

No OS-provided timestamps or device-id fields are relied upon. BAI uses only
its own trusted local clock.

## Purpose Binding

Purposes are declared and recorded before the OS prompt is shown. One pending
record exists at a time.

```
pending_authorization_record
  pending_id:           uuid4 — generated by BAI before OS prompt
  challenge:            cryptographically random nonce — generated by BAI
  purpose:              declared purpose identifier
  requester:            named component
  requested_at:         N.H trusted local clock
  expires_at:           requested_at + pending_expiry_window
  status:               "pending" | [terminal states]
  app_session_key_ref:  reference to hardware-backed key for this app instance
```

Device and app trust is bound through a hardware-backed key in the phone's
secure keystore, not through OS-provided device-id fields.

**Purpose vocabulary:**
- `"top_security_access"`
- `"tsc_promotion:<session_id>"`
- `"voice_enrollment_ness"`
- `"bgmm_confirmation:<session_id>:<purpose>"`
- `"extended:<purpose_id>"`

## Two Distinct Artifacts

### One-Time Authorization Token

For TSC promotion and voice enrollment:

```
one_time_authorization_token
  token_id, pending_id, challenge, purpose, authenticated_at, created_at,
  expires_at, status: "valid" | "consumed" | "expired" | "revoked"
```

Lifecycle: created on OS success → delivered to requester → consumed before the
protected action begins → permanently unusable. Single-use. Purpose verified
on every consume call.

### Top-Security Biometric Lease

For ongoing top-security access:

```
top_security_lease
  lease_id, pending_id, purpose: "top_security_access",
  authenticated_at, created_at, expires_at,
  status: "active" | "expired" | "revoked",
  session_id
```

Lifecycle: created on OS success → remains active until expiry or revocation →
queried repeatedly by SACL → never consumed; queried, not spent.

## Key Separation

**Manifest-signing key:** signs authorized manifest versions only.  
**Rollback sealing key:** encrypts and integrity-protects rollback packages only.

Neither key is derivable from the other. Neither private key is exportable or
written to any log. Compromise of one does not compromise the other. Specific
hardware implementation is a build-time decision.

## Result Handling

Success with matched pending record within expiry → create appropriate artifact
(lease or one-time token) → write audit events → deliver to requester.

No matching pending record (expired, absent, or device mismatch) → reject;
write `bai_unmatched_result`; no artifact created.

All non-success outcomes (failure, cancelled, timeout, lockout, error) → pending
record terminal status set → requester notified → audit events written. BAI does
not retry automatically.

## TSC Promotion Authorization

Requires:
1. Valid unconsumed `one_time_authorization_token` with purpose
   `"tsc_promotion:<session_id>"`.
2. At consume time: SACL reports that the current session holds a fresh
   non-stale recognized_ness assessment for the Ness stream.

If either condition is not met, token is not consumed; promotion does not proceed.

Conditions that invalidate condition 2: speaker change detected; SIA assessment
stale; medium-or-higher spoofing suspicion; SACL access for Ness stream below
recognized_ness; session end; relevant security event.

## Lease Revocation Triggers

Any one fires immediately:

- Session close
- `assessed_certainty` drops below recognized_ness_threshold
- Any active spoofing, speaker-change, or imitation-risk flag at security level
- Anti-spoofing suspicion_level rises to medium or above
- Timeout since `authenticated_at`
- Major session break
- Branch continuity below threshold
- Explicit relock from SACL

## BAI-Owned State

In-memory only. Nothing persists across restarts.

```
BAI_state
  pending_record:           single pending record or null
  active_lease:             top_security_lease or null
  active_one_time_tokens:   map of token_id → one_time_authorization_token
  lockout_state:            "none" | "temporary" | "permanent"
  lockout_since:            timestamp or null
  app_session_key_ref
  session_id
  last_audit_event_id
```

On restart: all state cleared; biometric_state → not_verified; Ness
re-authenticates. Fail-closed.

## BOP vs. Security Audit Separation

**BOP system_command roots record only:** prompt_opened; result:success;
result:failure; result:cancelled; result:timeout; result:lockout; result:error.
Each carries only session_id and N.H local clock timestamp. No token_id, no
challenge, no purpose, no authorization conclusions.

**Security audit log records:** all purpose binding, challenge creation, token
and lease creation, consumption, revocation, purpose mismatch, requester
identity, and security-policy consequences.

## Crash, Duplicates, Delayed Events, Malformed Results

On restart: BAI_state cleared; `bai_restart_state_cleared` written.
On delayed result: no matching pending record; rejected as `bai_delayed_result_rejected`.
On duplicate result: pending record already resolved; rejected as `bai_duplicate_result_rejected`.
On malformed result: rejected without logging potentially biometric fields; `bai_malformed_result_rejected`.

## Protected-Core Rules

- BAI never receives, stores, inspects, reconstructs, or processes fingerprint
  data.
- A token created for one purpose cannot satisfy another.
- Consumed tokens cannot be reused. Expired tokens cannot be reused.
- One pending record at a time.
- BAI exposes no interface allowing override of immutable roots or protected
  safeguards.
- Wellbeing system not involved in BAI; BAI never queries §22.

---

---

# 7. Initial Owner-Phone Pairing

**ACCEPTED DESIGN — NOT YET BUILT**

## Four States

**State 1 — `qr_available`:**
Desktop has generated the signed QR. Scannable for 90 seconds. No phone paired.

**State 2 — `phone_provisionally_paired_qr_destroyed`:**
First phone pairs successfully. At this exact moment: signed QR and temporary
pairing secret are permanently destroyed. Cannot be scanned, reused, or
regenerated. Desktop binds permanently to phone's hardware-backed cryptographic
identity. Phone holds provisional trusted status only.
Audit event: `bai_qr_destroyed_phone_provisionally_paired`.

**State 3 — `recovery_setup_in_progress`:**
Recovery-code setup begins on the already-paired provisional phone. QR secret
was destroyed at state 2. If setup fails or times out, the phone remains in
state 3, provisionally paired. Ness may retry recovery-code setup on the same
phone. Retrying does not generate or reopen another QR.

**State 4 — `owner_setup_finalized_qr_path_permanently_closed`:**
Reached only after the first recovery code completes all four steps: saved in
Bitwarden, verified through 4-character check, successfully tested through
automatic local acceptance test, and activated. At this moment: phone receives
final permanent trusted-owner status; permanent closure audit event written;
initial QR path closed forever.

**What is destroyed when:**

| Artifact | Destroyed at |
|---|---|
| Signed QR | State 2 — immediately on successful pairing |
| Temporary pairing secret | State 2 — immediately on successful pairing |
| Provisional phone status | Upgraded to permanent at state 4 |
| Recovery code local copy | Immediately after activation at state 4 |

---

---

# 8. Recovery-Code Lifecycle

**ACCEPTED DESIGN — NOT YET BUILT**

## First Recovery Code Creation

Created immediately after the first phone pairs successfully. Never appears on
the desktop or clipboard. Desktop encrypts it using the paired phone's
hardware-backed public key. Only that phone may decrypt it, after biometric
approval.

Code appears on the trusted phone only. Visible until Ness confirms or until
automatic timeout of 10 minutes 30 seconds. On confirmation or timeout, phone
hides code and clears clipboard. If timeout occurs before confirmation, old code
remains valid; new code is not activated.

## Save Verification

After Ness presses "Saved in Bitwarden":
- N.H asks for exactly 4 unique random character positions.
- Ness enters the characters at those positions in exact requested order.
- Matching is exact, including letter case.
- 3 attempts total; each failed attempt uses a new set of 4 positions.
- Verification runs locally.
- Entered characters, requested positions, and comparison results are not stored.
- If all 3 attempts fail: new code destroyed; old code remains valid; rotation
  must restart.

## Activation Handover

After 4-character verification succeeds:
1. Phone performs automatic local test proving new code would be accepted.
2. Test must not change settings, create a recovery event, pair another device,
   or expose the code.
3. Only after local test succeeds does new recovery code become active.
4. Only then does old recovery code become permanently invalid.
5. Phone immediately erases its local copy.
6. Bitwarden is the only intended long-term storage location.

## Recovery Code Rotation

After every successful phone pairing or re-pairing, the normal recovery code
is rotated following the same save-verification-activation sequence. The old
recovery code remains valid until the new one has been saved, verified, locally
tested, and activated.

---

---

# 9. Future-Phone Replacement Flow

**ACCEPTED DESIGN — NOT YET BUILT**

Requires both factors; neither alone is sufficient:
1. Current Bitwarden normal recovery code.
2. Ness's thumbprint through Maintenance Mode on the N.H desktop.

A new phone is a replacement by default. Once fully paired and verified, the
previously trusted phone is automatically revoked. A revoked phone may become
trusted again only through the complete recovery-code + thumbprint pairing flow.

After every successful replacement, rotate the normal recovery code per the
accepted lifecycle.

---

---

# 10. Atomic Emergency Recovery Flow

**ACCEPTED DESIGN — NOT YET BUILT**

## Required Factors

All required simultaneously:
- Physical access to the N.H desktop (motherbase).
- Separate emergency code stored outside Bitwarden.
- Printed recovery sheet stored in a physically secure place.
- Ness's thumbprint on the motherbase through BGMM.

Remote emergency recovery is prohibited unconditionally.

## Intermediate State (Provisional Only)

During the intermediate state:
- New phone is only provisionally paired; no permanent trusted status yet.
- All previously trusted phones remain valid.
- Old normal recovery code remains valid.
- Old emergency code remains valid.
- Old printed recovery sheet remains valid.
- No partial revocation occurs.

## Required Steps Before Final Commit

All of the following must complete successfully:
1. New normal recovery code: saved, 4-character verified, local test passed.
2. New emergency code: saved and verified.
3. New printed recovery sheet: confirmed saved and verified.

## Atomic Final Commit

Only after every required step succeeds, N.H performs one atomic commit:
- New phone becomes sole permanently trusted phone.
- All previously trusted phones permanently revoked.
- Old normal recovery code permanently invalid.
- Old emergency code permanently invalid.
- Old printed recovery sheet permanently invalid.
- All new recovery materials become active simultaneously.
- `bai_emergency_reset_finalized` written.

## If Any Step Fails Before Final Commit

- Emergency reset aborted safely.
- All provisional new material destroyed.
- New phone's provisional pairing cancelled.
- All previously valid trust and recovery material remains valid.
- No partial revocation has occurred.
- `bai_emergency_reset_aborted` written with failed step and reason.

---

---

# 11. Initial Ness Voice-Profile Enrollment Bootstrap

**ACCEPTED DESIGN — NOT YET BUILT**

## Prerequisites (All Six Must Be True)

1. Phone holds final permanent trusted-owner status (BAI state 4).
2. First normal recovery code saved, verified, locally tested, and activated.
3. Original QR and temporary pairing secret destroyed at pairing.
4. Original owner setup finalized; QR path permanently closed.
5. No active medium-or-higher acoustic spoofing suspicion in current session.
6. Ness's Person-Box confirmed in §7L.

## Enrollment Session Opening

Accessible only through the dedicated Owner Setup / Voice Enrollment flow on
the permanently trusted phone. Ness must explicitly choose to begin. On Ness's
choice:

1. Enrollment flow calls BAI request interface with purpose `"voice_enrollment_ness"`.
2. BAI creates pending record; triggers OS biometric prompt.
3. On success: BAI creates `one_time_authorization_token` with purpose
   `"voice_enrollment_ness"`. Single-use, short-lived.
4. Enrollment flow verifies all six prerequisites against current system state
   before consuming.
5. If all satisfied: token consumed. Enrollment session opens.
6. If any prerequisite changed since prompt shown: token revoked without
   consumption; enrollment does not begin.

**What biometric success proves:** an enrolled device biometric on the
permanently trusted phone was accepted. It does not identify Ness by name. The
trusted-phone binding is the outer bootstrap authority. The purpose-bound token
is the inner approval.

## BOP Integration

BOP records only raw voice observations during the enrollment session. Standard
BOP rules apply without exception.

Each root carries:
- `role = "ness"` — the enrollment flow's declared attribution, not a confirmed
  identity assessment.
- `source_title = "enrollment:ness:<session_id>"` — states material came from
  an authorized enrollment session.
- `session_authorization.authorization_type = "enrollment_declared"` — formally
  adopted vocabulary addition (see section 12). Signals to §7G that role
  attribution is a declaration by the enrollment flow, not a confirmed SIA
  assessment.

One BOP `system_command` root from BAI at session open: `command_identifier =
"biometric:result:success"`, carrying session_id and N.H local clock timestamp
only. No purpose, no token_id, no authorization conclusions.

## §7G Integration

Enrollment roots enter the shared store through §7E's standard catalog path after
the enrollment session ends. §7G reads them through the standard reading queue.
Readings go to quarantine. §7G reads `authorization_type = "enrollment_declared"`
and treats `role = "ness"` as the enrollment flow's declared attribution — not
confirmed identity.

Readings reflect honest provisional confidence. They become the initial voice
profile reading set.

## Initial-Corpus Eligibility Rules

Before an enrollment segment's roots may contribute to the provisional profile,
all of the following must hold:

1. One consistent live speaker stream during the segment.
2. No medium-or-higher acoustic spoofing suspicion during the segment.
3. No unresolved overlapping speaker contamination.
4. Sufficient signal quality (overall_completeness = "complete" or "partial").
5. Complete enrollment provenance (authorization_type = "enrollment_declared"
   present; session_id links to confirmed bai_token_consumed audit event).
6. **Stream integrity:** diarization confidence remains above bootstrap
   stream-stability threshold for the full segment duration; no unresolved
   speaker-transition event; no material stream split or merge; no uncertainty
   that a second speaker entered; no medium-or-higher spoofing evidence.
   (Check 6 assesses whether the segment came from one consistent live speaker.
   It does not require SIA to have identified who that speaker is — the profile
   does not yet exist.)

Rejected segments are preserved in the shared store as observation roots. They
do not train the provisional profile. Exclusion is recorded in the enrollment
component's audit log.

## §7L Integration

After sufficient readings are produced, a Person-Box link is proposed:

```
Link type: "enrollment_material_provisional"  [formally adopted — see section 12]
What it means: this material was collected during Ness's authorized owner-enrollment
  flow. It does NOT mean the captured voice has been confirmed as Ness's voice.
Certainty: "enrollment_provisional"
Basis: bai_token_consumed: voice_enrollment_ness + owner_phone_trust:
  bai_initial_setup_finalized + authorization_type: enrollment_declared
```

The link strengthens only through: later SIA evidence, repeated authorized
sessions, anti-spoofing-clean material, candidate separation, and accepted
profile-integrity rules.

## SIA Integration

Once the provisional profile reading set is linked to Ness's Person-Box, SIA
may use those readings as one input. At this stage:
- `profile_status = "enrollment_provisional"`
- Conservative confidence ceiling: recognized_ness is the maximum achievable
  level regardless of voice acoustic match score.
- SIA weights behavioral, branch, session continuity, timing, and wording
  dimensions more heavily than voice acoustic match until profile reaches
  `enrollment_active`.

All subsequent evidence follows standard SIA training eligibility rules without
exception. No shortcut for enrollment roots.

## Audit Event Ownership

BAI-owned: `bai_token_consumed`, `bai_token_revoked` (for this flow).

Enrollment-component-owned:
- `enrollment_prerequisites_verified`
- `enrollment_session_opened`
- `enrollment_session_closed`
- `enrollment_segment_accepted`
- `enrollment_segment_rejected`
- `enrollment_prerequisite_failed`
- `enrollment_token_revoked_prereq_changed`
- `enrollment_provisional_link_proposed`
- `enrollment_provisional_profile_created`

## What Enrollment Does Not Establish

The authorized enrollment provenance permits N.H to create a provisional profile
candidate associated with Ness's enrollment process. It does not establish that
the captured voice belongs to Ness. The association strengthens gradually through
later SIA evidence, repeated authorized sessions, anti-spoofing-clean material,
candidate separation, and accepted profile-integrity rules. No enrollment session
alone establishes that association.

---

---

# 12. Formally Adopted Vocabulary Additions

**ACCEPTED — FORMALLY ADOPTED**

Both vocabulary additions were examined against their parent schemas and formally
adopted within existing open-ended vocabularies. No schema version changes and
no further consistency reviews are required.

## Addition 1: BOP `authorization_type = "enrollment_declared"`

**Location:** `session_authorization.authorization_type` field in the BOP
payload's `session_authorization` object.

**Existing values before adoption:** `"live_session"` | `"manual_import"`

**New value:** `"enrollment_declared"`

**Meaning:** the role attribution in this root was declared by an authorized
enrollment flow; the speaker identity has not yet been independently confirmed
by SIA.

**Fit:** the `authorization_type` field is a controlled vocabulary in an
extensible payload object. This addition follows the established BOP vocabulary
extension mechanism. No structural schema change is required.

## Addition 2: §7L `link_type = "enrollment_material_provisional"`

**Location:** the `link_type` field in §7L Person-Box link records.

**Meaning:** this material was collected during Ness's authorized owner-enrollment
flow. It does not mean the voice in that material has been confirmed as Ness's
voice. The link represents enrollment provenance, not confirmed voice identity.

**Fit:** §7L's link-type field is open-ended by design in the current Master
text. This addition is a new named value within that open-ended vocabulary. No
schema version change and no structural alteration to §7L is required.

---

---

# 13. BGMM — Biometric-Gated Maintenance Mode

**ACCEPTED DESIGN — NOT YET BUILT**

## What BGMM Is and Is Not

BGMM is the only authorized path through which protected N.H material may be
changed. Outside BGMM, protected files are read-only by architectural
enforcement. BGMM does not make N.H more powerful; it makes unauthorized change
structurally harder and always detectable.

BGMM is not a general administrator mode. It does not grant broader access than
the declared purpose requires. It cannot be entered remotely. It cannot be
entered through ordinary terminal, editor, script, or installer access regardless
of OS privilege level. It cannot override immutable roots, provenance, privacy
rules, or protected architectural safeguards.

## Protected Material Boundary

**Writable only through BGMM:**
- `code_change` — Python source, executable code, .cursorrules, engine config
- `configuration_change` — non-code behavior configuration files
- `security_policy_change` — SACL thresholds, anti-spoofing policy, audit
  retention rules
- `device_trust_change` — trusted-phone binding records, pairing credentials,
  recovery-code authority records
- `emergency_recovery` — device-trust reset per accepted BAI emergency flow only

**Permanently unchangeable even inside BGMM:**
- Immutable roots in the sealed root store
- Reading records and their provenance
- Clash records, Person-Box links and their provenance
- Security audit log entries (append-only; BGMM may not delete or alter)
- Gold set records
- Recovery code values (never stored in N.H)

Existing records are append-only and immutable. New readings, rereads, links,
revisions, and superseding interpretations may still be appended through their
normal architectural mechanisms. BGMM cannot directly create, rewrite, delete,
or "correct" those records. A later record may supersede an earlier interpretation
without altering the earlier record.

## Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)

**Layer 1 — ACLs and service isolation:** ordinary user sessions, terminals,
editors, scripts, and installers are blocked by ACLs and `nh_system` account
isolation.

**Layer 2 — Administrator-level resistance:** a person with full Windows
administrator privileges or offline disk access may be able to take file
ownership or modify files through OS recovery mechanisms. ACLs alone cannot
prevent this. Additional resistance: Secure Boot; TPM-backed trust anchoring
the boot chain; full-disk encryption; signed application-control policy
(Windows Defender Application Control or equivalent); protected service
configuration. These layers raise the cost and detectability of administrator-level
tampering substantially but do not make it physically impossible.

**Layer 3 — Code signing:** all executable N.H code is signed. Runtime verifies
signatures before loading. Unsigned or invalidly-signed modules are rejected.

**Layer 4 — Signed manifest integrity:** all protected files are registered in
a signed manifest. Startup verifies the manifest signature. Any file modified
outside BGMM produces a hash mismatch against the signed manifest.

**Layer 5 — Change-log provenance:** every BGMM change is recorded in the
append-only change log before the change is applied.

The net guarantee: ordinary user paths are blocked. Administrator-level
tampering is substantially resisted and always detected before N.H runs.
Physical attackers with sufficient hardware access may bypass some layers, but
N.H fails closed on any integrity failure.

## Signed-Manifest Trust Anchor

The manifest contains expected hashes and versions of all protected files. After
every authorized change, BGMM signs a new manifest version with the
**manifest-signing private key** (hardware-backed, accessible only within an
authorized BGMM session). The prior signed manifest is appended to an append-only
manifest provenance history — never deleted.

Startup verification: verifier reads the current signed manifest; verifies the
signature against a pinned public key anchored in the TPM or equivalent
hardware-backed trust store (public key does not change when manifest changes);
verifies each protected file's hash against its manifest entry.

If any signature or hash fails: N.H does not start; integrity failure written
to audit log; BGMM is the only authorized repair path.

Rollback: prior file content restored; prior signed manifest version restored
from provenance history after re-verifying its signature.

## Encrypted Full-Content Rollback Packages

Before any protected file is changed, BGMM creates a protected rollback package:

```
rollback_package
  session_id
  change_description:   declared change, for audit linkage
  file_entries:         one per in-scope file:
    file_path
    prior_content:      exact byte-for-byte prior file content
    prior_hash:         SHA-256 of prior content (verification evidence)
    prior_signature:    prior code signature if applicable
    prior_manifest_version
    file_metadata:      permissions, timestamps, attributes for exact restoration
  created_at:           before any write occurs
```

**Rollback sealing key:** separate from the manifest-signing key. Hardware-backed.
Not derivable from the manifest-signing key. Neither private key is exportable
or written to any log. Used only to encrypt rollback packages.

The package is: encrypted using the rollback sealing key; integrity-protected
with a MAC or signature verifiable by BGMM; inaccessible to ordinary users,
applications, terminals, and the normal N.H runtime; persisted before the first
write; deleted only after successful final verification or successful rollback.

## Protected Startup Recovery Worker

After a crash or unexpected restart, a minimal protected BGMM recovery worker
may access the rollback package automatically during verified startup recovery.

Its authority is strictly bounded:
- May decrypt and verify the rollback package under the expected secure and
  measured boot state.
- May restore exactly the files, metadata, prior signatures, and prior signed
  manifest named in that package — nothing else.
- Cannot edit arbitrary files, create a new change, expand scope, export package
  contents, or open a general Maintenance Mode session.
- Access conditional on boot state matching expected measured-boot record and
  package passing full integrity verification before any restoration begins.

After verified rollback succeeds: package securely deleted; `bgmm_rollback_completed`
written.

If decryption, integrity verification, or restoration fails: recovery worker
halts; package not deleted; N.H remains stopped; fails closed until Ness enters
BGMM through the full normal authorization path.

## Entering Maintenance Mode

**Step 1 — Purpose declaration:** Ness declares the exact purpose (one of the
five controlled values) and the specific change in plain language. Recorded
before any authorization step.

**Step 2 — Motherbase thumbprint:** Ness provides thumbprint; BGMM receives
only `"success"` or `"failure"` from the native OS framework.

**Step 3 — Trusted phone confirmation (for code, configuration, security-policy
changes):** motherbase sends purpose-bound confirmation request to the trusted
paired phone. Phone displays declared purpose and change description. Ness
explicitly confirms. Phone requires its own BAI `one_time_authorization_token`
with purpose `"bgmm_confirmation:<session_id>:<purpose>"` before sending
confirmation.

**Step 4 — Recovery code (for device_trust_change):** current Bitwarden normal
recovery code verified locally. Phone confirmation is not required for
device_trust_change — the old trusted phone may be unavailable.

**Step 5 — Emergency factors (for emergency_recovery):** emergency code and
printed-recovery-sheet verification. No trusted-phone confirmation required.

**Step 6 — Maintenance window opens:** scope enforced to exactly declared files
and purpose. `nh_system` write token granted for in-scope files only.

## Purpose-Specific Authorization

| Purpose | Required factors |
|---|---|
| code_change | Motherbase thumbprint + phone confirmation |
| configuration_change | Motherbase thumbprint + phone confirmation |
| security_policy_change | Motherbase thumbprint + phone confirmation |
| device_trust_change | Motherbase thumbprint + Bitwarden recovery code (no phone confirmation required) |
| emergency_recovery | Physical motherbase access + thumbprint + emergency code + printed recovery sheet (no phone confirmation required) |

Emergency_recovery scope is device-trust records only. No code or configuration
files are writable, regardless of what the session declares. The scope-enforcement
guard enforces this unconditionally.

## File Scope Enforcement

The `nh_system` write token is scoped to the exact file list derived from the
declared purpose and declared change. Any write attempt outside this scope is
blocked by the scope-enforcement guard and immediately written to the security
audit log as `bgmm_out_of_scope_write_attempt`.

## Change Application

Before any file is touched:
1. Change-log entry written and flushed.
2. Rollback package created and persisted.
3. Change applied.
4. hash_after computed and recorded.
5. Manifest updated and re-signed with manifest-signing key.
6. Modified executable files re-signed with code-signing key.
7. `bgmm_change_applied` written to security audit log immediately.

If any step fails after the file is touched: rollback triggered immediately.

## Automatic Relocking

Maintenance window closes immediately on:
- Completion (change applied, verified, logged)
- Timeout (expires_at reached)
- Restart or crash
- Security alert from SACL (medium-or-higher spoofing, session-level alert)
- Phone disconnection during an open session
- Explicit Ness abort
- Biometric verification expiry

On any relock: write token revoked immediately; `bgmm_write_token_revoked` written;
rollback triggered if change was partially applied.

## Rollback

Rollback uses the encrypted full-content rollback package. For each file entry:
decrypt package; verify prior_hash against prior_content; restore prior_content;
restore prior_signature and prior_metadata; update signed manifest to prior
signed version from provenance history. Rollback is idempotent — if a file
already matches prior_content, no write occurs.

## BGMM-Owned State

In-memory only across active session. Nothing persists except: the rollback
package (encrypted, deleted after successful completion or rollback); the
change log (append-only, permanent provenance record); the signed manifest and
its provenance history.

```
BGMM_session_state
  session_id, declared_purpose, declared_change, scope,
  authorization_factors, session_status, opened_at, expires_at,
  write_token_active, applied_changes (append-only list),
  rollback_checkpoint (file list and hash_before values — verification reference
  pointing to the encrypted package; hashes alone are not backups)
```

## Privacy During Maintenance

BGMM may not expose protected content merely because Maintenance Mode is open:
- Change descriptions shown to Ness and sent to the phone must not contain
  private content.
- Rollback packages must not expose private content in metadata or audit fields.
- Change log records file paths, operations, and hashes — not file content.
- Security audit events record structural facts only — not content from protected
  files.
- Secrets, private memory, health records, and sensitive content must not appear
  in any maintenance description, log entry, or phone-confirmation payload.

## Immediate Security Audit Events

All events written and flushed before the function that produced them returns.
Key events include: `bgmm_session_initiated`, `bgmm_session_opened`,
`bgmm_write_token_granted`, `bgmm_change_log_entry`, `bgmm_change_applied`,
`bgmm_hash_registry_updated`, `bgmm_out_of_scope_write_attempt`,
`bgmm_session_completed`, `bgmm_write_token_revoked`, `bgmm_rollback_triggered`,
`bgmm_rollback_completed`, `bgmm_rollback_failed`, `bgmm_session_timed_out`,
`bgmm_session_aborted`, `bgmm_integrity_check_failed`, `bgmm_integrity_check_passed`,
`bgmm_immutable_write_blocked`.

## Crash, Restart, Offline Behavior

On crash during open session: state lost; write token revoked by OS process exit;
startup-recovery worker runs rollback from rollback package; `bgmm_rollback_completed`
written before N.H starts.

On crash during rollback: idempotent; restart triggers rollback again from
whatever state files are in.

On integrity check failure at startup: N.H does not start; BGMM entry is the
only authorized repair path.

BGMM operates fully offline. No network required.

## Protected-Core Rules (Unconditional)

- Immutable roots, readings, provenance, audit log: scope enforcement blocks
  all writes; `bgmm_immutable_write_blocked` written if attempted.
- Normal PC access cannot modify protected material: Layer 1 and nh_system token
  enforce this for ordinary users; administrator-level tampering is resisted and
  always detected.
- Maintenance authorization is temporary and purpose-bound.
- Emergency_recovery does not grant code-edit authority.
- Recovery code values are never stored in N.H.

---

*End of NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md*

<!-- NH_SOURCE_END filename="NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md" -->

---

# PART III — ACCEPTED TEMPORARY SESSION CACHE DESIGN

The source below is the complete accepted 31-section TSC specification. Its internal historical authority references are preserved as written; the current authoritative pair governs project authority.

<!-- NH_SOURCE_BEGIN filename="NH_ACCEPTED_TSC_DESIGN_v1.md" bytes=43237 sha256=1da2e296d4345d11dcec5f197aa9a42883349526275c5aa32b0bb07d1ca44658 -->
# Temporary Session Cache (TSC) — Final Accepted Design

## Provenance

This file is the standalone project record of the complete accepted 31-section
Temporary Session Cache (TSC) detailed design for the N.H system. The design was
produced through iterative correction and explicit acceptance by Ness in the
Claude project chat (security/identity/BGMM/TSC design branch). All superseded
drafts and rejected wording have been removed. Only the final corrected accepted
text is preserved here.

This file is a **companion record**, not an authoritative source. It does not
replace, supersede, or modify the N.H Master (`NH_MASTER-19_CORRECTED_v6.md`),
the Decision Defaults (`NH_DECISION_DEFAULTS-S19_v1__1_.md`), or any
implementation file. The TSC design must be formally patched into the Master
through the accepted patch-only, no-loss protocol before it carries Master
authority.

Related companion file: `NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md`
preserves the earlier accepted TSC foundation and the related security/identity
designs (BOP, SIA, SACL, BAI, BGMM, phone pairing, recovery, enrollment) that
the TSC depends on.

---

## Status

**ACCEPTED DESIGN — NOT YET BUILT**

No code written. No disk verification claimed. All 31 sections below are
accepted and complete.

---

## Contents

1. What TSC Is and Is Not
2. Relationship to §7E
3. Transactional Database Model
4. Session Record Schema
5. Contribution Record Schema
6. Participant and Speaker-Attribution Record Schema
7. Attribution Certainty and Unresolved-Speaker Handling
8. Conversation-Order and Branch-Link Schema
9. BOP and SIA Event-Link Handling
10. N.H Output Preservation
11. Blocker Schema and Blocker-Resolution History
12. Session Lifecycle and Item-Level Lifecycle
13. Normal Session Close and Sealing
14. Interrupted-Session Sealing and Linked Continuation Caches
15. Private Ness Inspection Without Promotion
16. Fingerprint Authorization Through BAI and SACL
17. Exact Promotion Sequence
18. Dependency Handling While Preserving Real Conversation Order
19. Partial Promotion and Idempotency
20. Automatic Retry Rules
21. Multi-Person Session Handling
22. Ness's Own Material Inside a Third-Party Session
23. Post-Promotion Retained Safety Archive
24. Protection Against Duplicate Use or Double Weighting
25. Privacy, Exclusion, Restriction, Deletion, and Third-Party Handling
26. Security Audit Events
27. Startup Recovery and Crash Recovery
28. Fail-Closed Behavior
29. Integration Boundaries
30. Explicit Prohibited Behaviors
31. Status

---

---

### 1. What TSC Is and Is Not

The Temporary Session Cache is a structured, transactional extension of §7E's
unified pre-ingest holding area. It is not a separate upstream system. It holds
session material in the §7E pre-ingest store, with TSC-specific organization
layered inside that same holding area, until Ness authorizes it to progress
through the standard §7E → sealed store path.

**TSC is:**
- An organized holding mode within §7E's unified pre-ingest store.
- A transactional local store for the TSC-specific structural records (session,
  contribution, participant, branch, blocker, and lifecycle tables) that support
  the richer session context §7E's flat per-item structure does not natively
  express.
- A complete faithful record of what happened in one real conversation session,
  held under §7E's rules.
- A provenance boundary that ensures third-party material undergoes the full
  §7E → §7G path before it can influence any N.H output.

**TSC is not:**
- A separate system that sits upstream of §7E and later submits into another
  waiting area.
- A second long-term memory system.
- A second Meaning Engine.
- A semantic interpretation store.
- A bypass around §7E, `append_root()`, or any other write boundary.
- A second independent route into readings, Person-Boxes, or Computed View.
- A place where third-party statements become facts about Ness.
- A system that performs identity fusion or merges speakers.

**The correct picture:** every TSC item exists in the §7E pre-ingest store from
the moment it is captured, carrying the `"pending_fingerprint_authorization"`
blocker. The TSC structural database holds the session-level organization —
conversation order, speaker attribution, branches, BOP event links, SIA event
links — that makes it possible to understand, navigate, and correctly promote
those §7E pre-ingest records. The TSC database and the §7E pre-ingest store are
two aspects of one holding system, not two stacked caches.

---

### 2. Relationship to §7E

The TSC is an extension of §7E's unified pre-ingest holding area. It adds one
new blocker type and one new organizational layer. It does not add a separate
upstream cache.

**The single blocker added:** `"pending_fingerprint_authorization"`. Every TSC
item enters the §7E pre-ingest store carrying this blocker alongside any other
applicable blockers (e.g., `"speaker_unresolved"`, `"thread_unresolved"`). The
blocker rules from §7E apply: held material is invisible to the Meaning Engine;
one blocked item never blocks unrelated ready items; silent deletion is never
permitted; material may remain held indefinitely.

**What the TSC structural database adds:** §7E's conceptual pre-ingest record
shape stores `capture_id`, raw payload, capture timestamp, front-door type,
source metadata, proposed catalog fields, blocker list, resolution history,
lifecycle state, and `root_id` if promoted. This is sufficient for the §7E
holding and promotion path. The TSC adds, alongside these per-item §7E records,
a set of relational tables that capture: session identity; conversation order
(`sequence_position`); participant and speaker-stream identity; attribution
assessments and certainty; branch and reply relationships; links to BOP
observation roots held in the same pre-ingest store; links to SIA assessment
events in the security audit log; N.H outputs; and per-item blocker and
lifecycle history. These tables exist only to organize the §7E pre-ingest
records as a coherent session — they do not replace, duplicate, or bypass those
records.

**All items in one place:** both conversation contributions and BOP observation
roots from the session sit in the §7E pre-ingest store, held under
`"pending_fingerprint_authorization"`. They do not enter the sealed long-term
root store while authorization is pending. The TSC structural database holds
the references and organizational context. It does not hold the raw payloads
— those are in the §7E pre-ingest records.

**Promotion from TSC to sealed store:** when the
`"pending_fingerprint_authorization"` blocker is lifted (after fingerprint
authorization), items with no remaining blockers progress through the normal
§7E lifecycle: `held` → `ready` → `promoting` → `promoted`, terminating in
`append_root()`. The TSC structural database tracks which items have been
promoted and records the resulting `root_id`. After promotion, the §7E
pre-ingest record remains as provenance per the settled §7E rule.

---

### 3. Transactional Database Model

The TSC uses a local transactional database for its structural organizational
records. The choice of specific technology (SQLite, embedded key-value store
with transaction support, or equivalent) is a build-time decision. The
architectural requirement is: ACID transactions, crash-safe writes, local-only
operation, and no network dependency.

This database stores session-level organization. It does not store raw payloads
— those remain in the §7E pre-ingest store. It does not perform semantic
interpretation. It does not produce readings.

**Database tables (logical schema):**
1. `sessions` — one row per TSC session
2. `contributions` — one row per conversation contribution
3. `participants` — one row per detected participant stream
4. `attribution_assessments` — one row per speaker attribution event
5. `branch_links` — one row per reply/branch relationship
6. `bop_preingest_links` — one row per BOP observation root in the §7E
   pre-ingest store, linked to the session or a specific contribution
7. `sia_event_links` — one row per SIA assessment event linked to a
   contribution moment
8. `nh_outputs` — one row per N.H response or output within the session
9. `blockers` — one row per active or resolved blocker per item
10. `blocker_history` — append-only resolution history for each blocker
11. `lifecycle_events` — append-only lifecycle state log for the session
12. `promotion_state` — one row per item tracking promotion progress
13. `security_audit_refs` — references to security audit log entries from
    TSC operations

---

### 4. Session Record Schema

```
sessions table
  session_id              uuid4
  session_mode            "voice" | "text" | "mixed"
  started_at              timestamp
  sealed_at               timestamp or null
  authorized_at           timestamp or null
  promotion_started_at    timestamp or null
  promotion_completed_at  timestamp or null
  lifecycle_status        "active" | "sealed" | "authorized" | "promoting" |
                          "promoted" | "promotion_failed" | "interrupted"
  continuation_of_session_id  uuid4 or null
  interruption_recorded   boolean
  bai_token_id            uuid4 or null
  sacl_recognized_ness_confirmed_at  timestamp or null
  tsc_schema_version      "tsc_v1"
  notes                   string or null
```

---

### 5. Contribution Record Schema

One record per natural conversation contribution. The `sequence_position` and
all session-context fields are stored in the TSC structural database and in
the §7E pre-ingest record's `source_metadata` field. They are not added as new
fields to the sealed seven-field root schema.

```
contributions table
  contribution_id         uuid4
  session_id              foreign key
  sequence_position       integer — ordinal position within this session;
                          1-based; set at capture time; never changed
  occurred_at             timestamp
  duration_ms             integer or null
  contributor_stream_id   foreign key → participants.stream_id
  role                    "ness" | "participant" | "nh_output" | "unknown"
  content_type            "voice" | "text" | "nh_text" | "nh_voice" | "other"
  preingest_capture_id    uuid4 — the capture_id of this contribution's
                          §7E pre-ingest record; the link between the TSC
                          structural record and the §7E holding-area record
  word_count              integer or null
  character_count         integer or null
  reply_to_contribution_id uuid4 or null
  branch_level            integer
  item_lifecycle_status   "held" | "ready" | "promoting" | "promoted" |
                          "excluded" | "blocked"
  promoted_root_id        uuid4 or null
  exclusion_metadata      JSON or null — non-reconstructive metadata
                          describing the type of exclusion; no excluded
                          content
  content_hash            SHA-256 of raw_content at capture time
```

**On session-context metadata and the seven-field root schema:** the
`sequence_position`, `occurred_at`, `contributor_stream_id`, branch
relationship, and session identity are stored in the TSC structural database
and in the §7E pre-ingest record's `source_metadata` field. They flow through
to the sealed root via the `source_metadata` provenance fields that §7E already
carries in its conceptual record shape. They are not added as new fields to the
sealed root's seven-field schema (id, subject, timestamp, content, re_reads,
source_title, role). If a future schema version is needed to carry additional
session provenance directly in the root, that is a future schema dependency —
it is not silently applied here. The current seven-field schema is unchanged.

**Ness's own contributions:** `role = "ness"`, preserved in the TSC and the
§7E pre-ingest store with the same `"pending_fingerprint_authorization"` blocker
as other items. They are not excluded from the session context. They proceed
through the same promotion path.

---

### 6. Participant and Speaker-Attribution Record Schema

```
participants table
  stream_id               uuid4
  session_id              foreign key
  first_seen_at           timestamp
  last_seen_at            timestamp
  declared_role           "ness" | "third_party" | "unknown"
  assessed_person_box_id  uuid4 or null
  assessed_certainty      float [0.0, 1.0] or null
  identity_status         "confirmed_known" | "assessed_probable" |
                          "unresolved" | "below_threshold" | "unknown"
  permission_boundary_record_version  integer or null
  sia_stream_id_ref       uuid4 or null
```

---

### 7. Attribution Certainty and Unresolved-Speaker Handling

Attribution certainty is recorded at the moment of capture and never upgraded
retrospectively within the TSC.

```
attribution_assessments table
  assessment_id           uuid4
  session_id              foreign key
  stream_id               foreign key
  contribution_id         foreign key or null
  assessed_at             timestamp
  assessed_person_box_id  uuid4 or null
  assessed_certainty      float [0.0, 1.0]
  certainty_dimensions    JSON object
  uncertainty_flags       JSON array
  anti_spoofing_suspicion_level  "none" | "low" | "medium" | "high"
  sia_assessment_event_id uuid4
```

**Unresolved-speaker handling:** a contribution whose speaker cannot be
confirmed from source carries `item_lifecycle_status = "blocked"` and two
blockers: `"pending_fingerprint_authorization"` and `"speaker_unresolved"`.
The `"pending_fingerprint_authorization"` blocker is lifted by the
authorization event. The `"speaker_unresolved"` blocker remains and must be
resolved through the §7E speaker-resolution rule before the item can proceed
to `append_root()`. This resolution does not require a new fingerprint — the
authorization covers the session. It does not require manual Ness selection of
an identity — the §7E rule governs resolution. No item with `"speaker_unresolved"`
outstanding is ever promoted. No root is ever written with `role = "unknown"`.

---

### 8. Conversation-Order and Branch-Link Schema

```
branch_links table
  link_id                 uuid4
  session_id              foreign key
  child_contribution_id   foreign key
  parent_contribution_id  foreign key or null
  link_type               "direct_reply" | "continuation" | "interruption" |
                          "branch_open" | "branch_close" | "context_reference"
  confidence              "certain" | "inferred" | "uncertain"
  confidence_basis        string
```

`sequence_position` establishes total chronological order. Branch links express
reply structure without changing the chronological record. The parent-before-child
promotion dependency is enforced: a parent's `promoted_root_id` must be set
before its child is submitted to §7E. Branch and reply context is preserved in
the §7E pre-ingest record's `source_metadata` — not as new fields in the sealed
root schema.

---

### 9. BOP and SIA Event-Link Handling

BOP observation roots generated during a TSC session are held in the §7E
pre-ingest store under `"pending_fingerprint_authorization"` alongside the
conversation contributions. They do not enter the sealed long-term root store
while authorization is pending. The TSC structural database links to them by
their `preingest_capture_id` — the same identifier that exists in the §7E
pre-ingest record.

```
bop_preingest_links table
  link_id                 uuid4
  session_id              foreign key
  bop_preingest_capture_id uuid4 — the capture_id of the BOP observation
                          root's §7E pre-ingest record; this root is HELD
                          in §7E pre-ingest, not yet in the sealed store
  linked_contribution_id  uuid4 or null
  occurred_at             timestamp
  event_type              string — the BOP event_type for reference
  relationship_type       "concurrent" | "precedes_contribution" |
                          "follows_contribution" | "session_level"
```

After fingerprint authorization and promotion, BOP roots proceed through §7E
to the sealed store alongside the conversation contributions, in the real event
order. Their timing relationship to conversation moments is preserved in the
§7E pre-ingest record's `source_metadata`, which flows into the sealed root as
provenance. This is not carried as new fields in the sealed seven-field root
schema.

```
sia_event_links table
  link_id                 uuid4
  session_id              foreign key
  sia_assessment_event_id uuid4 — in the security audit log; not held
                          in §7E; SIA assessment events are not promoted
                          as roots
  linked_contribution_id  uuid4 or null
  assessed_at             timestamp
  relationship_type       "assessment_at_contribution" | "session_level" |
                          "between_contributions"
```

SIA assessment events remain in the security audit log throughout. They are
not promoted as roots. Their timing relationship to contributions is preserved
through the `sia_event_links` table and through the `source_metadata` provenance
on relevant promoted roots.

---

### 10. N.H Output Preservation

```
nh_outputs table
  output_id               uuid4
  session_id              foreign key
  sequence_position       integer — interleaved with contributions in the
                          full session order
  produced_at             timestamp
  output_type             "text_response" | "voice_response" | "action_result" |
                          "translation_output" | "system_message"
  addressed_to_stream_id  uuid4 or null
  access_level_at_output  "top_security" | "recognized_ness" |
                          "known_person" | "guest"
  preingest_capture_id    uuid4 — the capture_id of this output's §7E
                          pre-ingest record; held under
                          "pending_fingerprint_authorization"
  item_lifecycle_status   "held" | "ready" | "promoting" | "promoted" |
                          "excluded"
  promoted_root_id        uuid4 or null
```

N.H outputs are promoted as roots with `role = "nh"`. Their session context is
preserved in the §7E pre-ingest record's `source_metadata`. No new fields are
added to the sealed seven-field root schema.

---

### 11. Blocker Schema and Blocker-Resolution History

```
blockers table
  blocker_id              uuid4
  session_id              foreign key
  item_id                 uuid4
  item_type               "contribution" | "nh_output" | "bop_root" | "session"
  blocker_type            "pending_fingerprint_authorization" |
                          "speaker_unresolved" | "content_under_review" |
                          "technical_hold"
  added_at                timestamp
  status                  "active" | "resolved" | "waived_by_exclusion"
  resolved_at             timestamp or null
  resolution_method       string or null
  resolution_event_ref    uuid4 or null
```

```
blocker_history table
  history_id              uuid4
  blocker_id              foreign key
  event_type              "blocker_added" | "blocker_resolved" |
                          "resolution_attempt_failed" | "blocker_waived"
  event_at                timestamp
  event_detail            string
  event_ref               uuid4 or null
```

`"speaker_unresolved"` is an additive blocker for contributions where speaker
cannot be confirmed. It does not resolve through TSC logic — it resolves through
§7E's speaker-resolution rule.

---

### 12. Session Lifecycle and Item-Level Lifecycle

**Session-level lifecycle:**
`active` → `sealed` or `interrupted` → `authorized` → `promoting` → `promoted`
or `promotion_failed`

**Item-level lifecycle:**
`held` → `ready` → `promoting` → `promoted` or `excluded` or `blocked`

No item proceeds from `blocked` to `promoting` while `"speaker_unresolved"` is
active. No item ever reaches `promoted` with an unresolved speaker.

---

### 13. Normal Session Close and Sealing

On normal session close: BOP `session_closed` pre-ingest record created and
linked; TSC session `lifecycle_status` → `"sealed"`, `sealed_at` = now; all
items confirmed `"held"` or `"blocked"`; `cache_sealed` security audit event
written immediately; TSC database transaction commits; session is immutable from
this moment.

The sealed TSC waits indefinitely. No auto-expiry. No auto-deletion.
No auto-promotion.

---

### 14. Interrupted-Session Sealing and Linked Continuation Caches

On crash: restart detects `"active"` session; `lifecycle_status` →
`"interrupted"`; `sealed_at` = restart timestamp; all material successfully
written before crash preserved exactly; nothing reconstructed; `cache_sealed`
written with `"interrupted_crash"` reason; session is sealed.

Continuation: new TSC with new `session_id`;
`continuation_of_session_id` = interrupted session's `session_id`; two sessions
remain separate immutable units; continuation relationship preserved; both
authorized and promoted separately.

---

### 15. Private Ness Inspection Without Promotion

**Settled decision:** private read-only inspection of a sealed TSC requires
fingerprint authorization through BAI, using a separate purpose-bound inspection
authorization. Inspection authorization is entirely independent of promotion
authorization — consuming an inspection token does not affect, consume, or create
any promotion token, and holding a promotion token does not provide inspection
access.

**Inspection authorization mechanism:**

Inspection uses a dedicated BAI `one_time_authorization_token` with purpose
`"tsc_inspection:<session_id>"`. This purpose is formally adopted into the BAI
purpose vocabulary following the same extension mechanism as other BAI purposes.
It follows all BAI token lifecycle rules: single-use, short-lived, purpose-bound,
delivered only to the requesting component, audited immediately.

The `"tsc_inspection:<session_id>"` token and the `"tsc_promotion:<session_id>"`
token are entirely separate artifacts. One cannot substitute for the other. They
may coexist without either affecting the other.

**What inspection shows:** the complete conversation as preserved in the TSC
structural database — all contributions in sequence order, participant attribution
with certainty scores, N.H outputs, BOP pre-ingest link references with timing,
SIA event link references, and blocker status. Inspection is read-only. It does
not pass through the Meaning Engine.

**What inspection explicitly does not do:**
- Consume or affect the promotion token.
- Change the session's `lifecycle_status`.
- Lift the `"pending_fingerprint_authorization"` blocker on any item.
- Begin or imply promotion.
- Expose material to §7G, §7J, §7M, §7L, or any downstream operational
  component.
- Count as Ness's approval of content.
- Make held material available to LMAC, §7F, or the reading queue.

**SACL condition:** inspection requires the current session to hold a
recognized-Ness assessment at the moment the inspection token is consumed,
following the same two-condition pattern as promotion authorization (BAI token
+ SACL recognized-Ness confirmation). This ensures a non-Ness speaker cannot
trigger inspection during a session where Ness's identity is not confirmed. The
SACL check for inspection is independent of any SACL check for promotion.

---

### 16. Fingerprint Authorization Through BAI and SACL

Promotion requires both conditions simultaneously at token consumption:

**Condition 1 — BAI `one_time_authorization_token`** with purpose
`"tsc_promotion:<session_id>"`.

**Condition 2 — SACL recognized-Ness session** confirmed fresh and non-stale
at consume time.

If either condition is not met: token not consumed; `bai_token_consume_blocked`
written; session remains `"sealed"`.

After successful authorization: token consumed; `bai_token_consumed` written;
session `lifecycle_status` → `"authorized"`; `authorized_at` = now;
`sacl_recognized_ness_confirmed_at` = SACL confirmation timestamp;
`cache_authorization_received` written; promotion begins automatically. No
additional manual Ness action is required after this point.

---

### 17. Exact Promotion Sequence

**Phase 1 — Pre-promotion check:**
1. Verify TSC session `lifecycle_status = "authorized"`.
2. Verify BAI and SACL conditions remain valid (not stale).
3. Apply §7Q privacy and exclusion rules to each item (see section 25).
4. Items that fall under §7Q exclusions: `item_lifecycle_status` →
   `"excluded"`; non-reconstructive exclusion metadata recorded; raw content
   replaced with exclusion metadata; item's §7E pre-ingest record updated;
   item will not proceed to `append_root()`.
5. Items that pass: `item_lifecycle_status` → `"ready"` (if
   `"pending_fingerprint_authorization"` was their only blocker).
6. Items with `"speaker_unresolved"` or other non-fingerprint blockers remain
   `"blocked"`.
7. Session `lifecycle_status` → `"promoting"`; `promotion_started_at` = now;
   `cache_promotion_started` written.

**Phase 2 — Ordered promotion loop (ascending `sequence_position`):**

For each item:

If `"excluded"`: skip; already recorded.

If `"blocked"` (non-fingerprint blocker remains, e.g. `"speaker_unresolved"`):
skip this pass; record in `promotion_state` as pending-blocked; continue. No
second fingerprint required.

If `"ready"`:

1. Idempotency check: if `promoted_root_id` already set → this item was
   promoted in a prior attempt; mark `"promoted"`; continue.
2. Lift the `"pending_fingerprint_authorization"` blocker on the §7E pre-ingest
   record. Write `sequence_position`, `occurred_at`, `contributor_stream_id`,
   `session_id`, branch relationship from the TSC structural database into the
   §7E pre-ingest record's `source_metadata`. These are not added as new fields
   to the sealed root schema.
3. §7E processes the now-unblocked pre-ingest record: validates intake envelope;
   if `"speaker_unresolved"` still active → item stays held, not promoted. If
   all fields resolved → item proceeds to `append_root()`.
4. On `append_root()` success: `promoted_root_id` recorded;
   `item_lifecycle_status` → `"promoted"`; transaction commits.
5. BOP roots held in §7E for this session proceed through the same path in
   their event-order position, interleaved by `occurred_at`.

**Phase 3 — Post-promotion:**

All items are `"promoted"`, `"excluded"`, `"blocked"`, or `"promotion_failed"`.
If none `"promotion_failed"`: session → `"promoted"`; `promotion_completed_at`
= now; `cache_promotion_completed` written; retained safety archive created.
Blocked items remain in `promotion_state` as pending, resuming automatically
when their blockers clear through normal §7E rules — no new fingerprint required.

---

### 18. Dependency Handling While Preserving Real Conversation Order

The promotion sequence follows ascending `sequence_position` as its primary
ordering. One dependency rule overlays this: if a contribution has a
`reply_to_contribution_id`, the parent's `promoted_root_id` must be set before
the child is submitted to §7E. If the parent is blocked, the child's promotion
is deferred to the next retry pass, not skipped permanently. BOP roots promote
interleaved by `occurred_at`. This is the only ordering dependency beyond
chronological sequence.

---

### 19. Partial Promotion and Idempotency

`preingest_capture_id` (stable per item) derives the §7E `capture_id` used as
input to `append_root()`. Any item already in the sealed store is silently
absorbed. No duplication. If promotion is interrupted, the loop picks up from
the first item not yet `"promoted"`, `"excluded"`, or `"blocked"`. Already-
promoted items are skipped via the idempotency check.

---

### 20. Automatic Retry Rules

**A — Automatic continuation of already-authorized interrupted promotion:** if
promotion was interrupted after authorization was already granted, the TSC
process resumes automatically on restart. No new fingerprint required. No new
SACL confirmation required from Ness. Security conditions are checked
automatically before resuming: if SACL no longer reports a recognized-Ness
session, promotion pauses until conditions recover naturally — this is an
automatic check, not a new Ness action.

**B — New promotion authorization:** required only when the session was never
authorized, or when the original BAI token was revoked before promotion began.

**C — Retry of temporary technical failure:** retries specific failed items
automatically after a backoff interval, within a bounded maximum attempt count.
No new authorization required. Security conditions checked automatically before
each retry.

**Ness notification on failure:** a private notice stating that promotion of a
specific session could not complete, with an indication that Ness may authorize
a new attempt when ready. No content is exposed. This is a notification, not a
request for clerk work.

---

### 21. Multi-Person Session Handling

One TSC session per real conversation. Participants are structurally separated
by `stream_id`. Each person has their own `participants` record,
`attribution_assessments`, and `permission_boundary_record_version`. No identity,
certainty, or permission transfers between streams. Full conversation order
preserved in `sequence_position`. The conversation is not split into per-person
sub-caches.

---

### 22. Ness's Own Material Inside a Third-Party Session

Ness's contributions held under `"pending_fingerprint_authorization"` alongside
other items. `role = "ness"`. Same promotion path. Not excluded from session
context. Idempotency prevents duplication if Ness's material was also captured
through the normal live-session path.

---

### 23. Post-Promotion Retained Safety Archive

After all items resolve and `cache_promotion_completed` is written, a frozen
encrypted read-only snapshot of the TSC structural database is created. It
contains structural records and references — not raw content excluded under
§7Q. Excluded items appear only as exclusion metadata.

**What it is for:** integrity checking, verifying what was promoted, recovery
if promoted material is damaged or missing, and explicitly authorized deletion
or audit processes.

**What it is not:** not an active memory source; not a source for the Meaning
Engine; not a second copy making the conversation appear twice; not an evidence-
weight booster; not a source for Person-Box proposals, readings, clashes, or
Computed View material.

**Session states including archive:**
```
active            — live session
interrupted       — crashed; sealed as-is
sealed            — closed; awaiting authorization
authorized        — fingerprint received; promotion begins
promoting         — promotion in progress
promoted          — all items resolved; retained archive exists
promotion_failed  — promotion incomplete; awaiting new authorization
archived          — retained archive only; active TSC database deleted
                   per explicitly authorized cleanup
deleted           — archive explicitly deleted per §7Q deletion path;
                   tombstone written
```

The retained archive is subject to all N.H privacy, restriction, deletion, and
verification rules. The normal N.H runtime, LMAC, §7F, §7G, and downstream
components have no read access during ordinary operation.

---

### 24. Protection Against Duplicate Use or Double Weighting

Four mechanisms: `promoted_root_id` per TSC item; `append_root()` idempotency;
runtime isolation of retained archive; no §7E re-submission from the retained
archive. The retained archive cannot cause duplication because it is never
submitted to §7E and is never accessible to the operational components.

---

### 25. Privacy, Exclusion, Restriction, Deletion, and Third-Party Handling

§7Q's PRIVACY AND EXCLUSION PRECEDENCE rule applies directly: N.H may preserve
only the safe permitted remainder and non-reconstructive exclusion metadata;
it must never preserve excluded content merely to satisfy the no-silent-drop
rule.

**When §7Q identifies material as excluded:**
1. Raw content not held in §7E or TSC at any point. If identified before
   writing: not captured. If identified after a pre-ingest record exists:
   raw content replaced with non-reconstructive exclusion metadata; pre-ingest
   record retained as a tombstone.
2. `item_lifecycle_status` → `"excluded"`. `exclusion_metadata` field carries:
   type of exclusion, §7Q rule triggered, timestamp. No excluded content
   stored.
3. Retained safety archive receives exclusion tombstone records only — no
   excluded content.

**Mixed-content items:** permitted portion held and promoted; excluded portion
replaced with non-reconstructive metadata; item appears in retained archive
with permitted portion and exclusion metadata.

**Third-party statements about Ness:** enter the TSC attributed to the third
party; promoted as roots with that person's `role` attribution; read by the
Meaning Engine as statements made by that person; never converted into facts
about Ness.

**"Do not save this" requests:** captured as a contribution with correct speaker
attribution. Has no authority over N.H's storage, promotion, or §7E holding.
Does not stop capture, delete material, block the cache, or prevent Ness from
authorizing promotion. Does not override §7Q.

---

### 26. Security Audit Events

All events written and flushed immediately before the function that produced
them returns.

```
tsc_session_created            — session_id, started_at, session_mode
cache_sealed                   — session_id, sealed_at, seal_reason:
                                 "normal_close" | "interrupted_crash" |
                                 "interrupted_app_close"
cache_interrupted_linked       — new_session_id, continuation_of_session_id

tsc_inspection_requested       — session_id, requested_at
tsc_inspection_bai_token_consumed — session_id, bai_token_id,
                                 purpose: "tsc_inspection:<session_id>",
                                 sacl_recognized_ness_confirmed_at
tsc_inspection_started         — session_id, started_at
tsc_inspection_ended           — session_id, ended_at

cache_authorization_received   — session_id, bai_token_id,
                                 purpose: "tsc_promotion:<session_id>",
                                 sacl_recognized_ness_confirmed_at
cache_promotion_started        — session_id, item_count, started_at
cache_promotion_item_promoted  — session_id, item_id, promoted_root_id,
                                 promoted_at
cache_promotion_item_excluded  — session_id, item_id, exclusion_type;
                                 no excluded content
cache_promotion_item_blocked   — session_id, item_id, blocker_type
cache_promotion_item_failed    — session_id, item_id, failure_reason
cache_promotion_completed      — session_id, promoted_count, excluded_count,
                                 blocked_count, completed_at
cache_promotion_failed         — session_id, failed_item_count, reason,
                                 failed_at
tsc_retry_started              — session_id, retry_type:
                                 "continuation" | "technical_retry",
                                 attempt_number
tsc_retry_security_paused      — session_id, reason, paused_at
tsc_retry_security_resumed     — session_id, resumed_at
tsc_retained_archive_created   — session_id, archive_location_ref,
                                 created_at
tsc_archive_access_authorized  — session_id, purpose, authorized_at
tsc_archive_deletion_authorized — session_id, authorized_at, authorized_by
tsc_archive_deleted            — session_id, deleted_at,
                                 tombstone_written: true
tsc_duplicate_promotion_prevented — session_id, item_id, existing_root_id
tsc_privacy_exclusion_applied  — session_id, item_id, exclusion_rule,
                                 excluded_at
tsc_ness_private_notice_sent   — session_id, notice_type, sent_at
bai_token_consume_blocked      — session_id, token_purpose, reason
```

Two distinct audit event clusters exist for the two distinct BAI purposes: the
`tsc_inspection_*` cluster for inspection tokens and the
`cache_authorization_received` / `cache_promotion_*` cluster for promotion
tokens. Neither cluster's events affect or imply the other.

---

### 27. Startup Recovery and Crash Recovery

On startup, TSC examines all session databases:

- `lifecycle_status = "active"`: crash during live session. Seal as interrupted.
  Write `cache_sealed` with `"interrupted_crash"`.
- `lifecycle_status = "promoting"`: crash during promotion. Resume automatically
  (section 20, case A). Check security conditions automatically first.
- `lifecycle_status = "authorized"`: crash between authorization and promotion
  start. Begin promotion automatically.
- `lifecycle_status = "sealed"` or `"interrupted"`: no action. Session waits
  for Ness's fingerprint.
- `lifecycle_status = "promoted"` and retained archive exists: normal terminal
  state. No action.
- `lifecycle_status = "promotion_failed"`: Ness has been notified. Awaits new
  authorization attempt.

Transactional database: any uncommitted write is absent; items with
`promoted_root_id` set are safely in the sealed store; promotion loop picks up
from the first item not yet `"promoted"`, `"excluded"`, or `"blocked"`;
idempotency prevents duplication.

---

### 28. Fail-Closed Behavior

- Security condition failure during promotion: promotion pauses; already-promoted
  items remain promoted; retry resumes automatically when conditions recover —
  no new Ness action unless a genuinely new authorization is required (case B
  in section 20).
- Missing or stale SACL at promotion time: promotion does not begin.
- BAI token expired or revoked before consumption: new authorization required.
- TSC database integrity failure: N.H does not proceed; error logged.
- Unknown session state on startup: sealed as interrupted.
- Retained archive access outside authorized purpose: denied unconditionally.

---

### 29. Integration Boundaries

**BAI:** TSC calls BAI consume interface with `"tsc_promotion:<session_id>"` for
promotion and with `"tsc_inspection:<session_id>"` for inspection. These are
separate BAI token requests, each following all BAI token lifecycle rules. BAI
writes its own audit events. TSC does not call BAI for any other purpose.

**SACL:** queried at token consumption time for both promotion and inspection
authorization. Also checked automatically during promotion retries. TSC does
not receive SACL push events directly.

**SIA:** not called by TSC. SIA assessment events linked by reference in
`sia_event_links`. Authoritative records remain in the security audit log.

**BOP:** not called by TSC. BOP observation roots are in the §7E pre-ingest
store (held), linked by `bop_preingest_capture_id` in `bop_preingest_links`.
They are not in the sealed root store while authorization is pending.

**§7E:** TSC lifts the `"pending_fingerprint_authorization"` blocker on a §7E
pre-ingest record and writes `source_metadata` from the TSC structural database
into that record before §7E processes it. §7E then handles the now-unblocked
record through its own path to `append_root()`. TSC never calls `append_root()`
directly.

**§7G:** not called by TSC. Reads promoted roots through the standard reading
queue only after they are in the sealed store. Retained archive is never
accessible to §7G.

**§7J, §7M, §7L:** not called by TSC. All run through their normal paths after
promotion.

**`append_root()`:** called by §7E's internal path only. TSC never calls it
directly. Idempotency key prevents duplication.

**Security audit log:** all events in section 26 written immediately and flushed
before the function that produced them returns.

---

### 30. Explicit Prohibited Behaviors

- TSC must not describe itself as upstream of §7E submitting into another
  waiting area. It is an extension of §7E.
- TSC must not write BOP observation roots to the sealed store while the session
  is pending authorization.
- TSC must not promote any item with `"speaker_unresolved"` outstanding. No root
  is written with `role = "unknown"`.
- TSC must not add new fields to the sealed seven-field root schema.
  Session-context metadata is carried in §7E source_metadata and TSC structural
  records.
- TSC must not retain excluded content in the active database, the §7E
  pre-ingest record, or the retained safety archive. Only non-reconstructive
  exclusion metadata may be preserved.
- TSC must not require a new fingerprint for automatic retry of already-
  authorized promotion.
- TSC must not become a second long-term memory system.
- TSC must not perform semantic interpretation or produce readings.
- TSC must not call `append_root()` directly.
- TSC must not bypass §7E.
- TSC must not auto-expire or auto-delete sealed caches.
- TSC must not promote without both fingerprint authorization and SACL
  recognized-Ness confirmation at token consumption time.
- TSC must not require a new fingerprint for items whose non-fingerprint
  blockers clear after the session was already authorized.
- TSC must not convert a third party's statement into a fact about Ness.
- TSC must not merge speaker streams or Person-Box candidates.
- TSC must not treat the retained safety archive as active memory.
- TSC must not allow the retained archive to be queried by LMAC, §7F, §7G, or
  any normal operational component.
- TSC must not split one real conversation into per-person sub-caches.
- TSC must not grant another participant's "do not save" request authority over
  N.H's storage.
- TSC must not apply §7Q rules itself — it records §7Q decisions and exclusion
  metadata but does not make them.
- TSC must not duplicate promoted roots in the sealed store.
- TSC must not re-enter material from the retained archive into the §7E path.
- TSC must not invent or reconstruct material not captured before a crash.
- TSC must not reopen or modify a sealed session.
- TSC must not silently reuse expired authorization state during retries.
- An inspection token must not substitute for a promotion token, and a promotion
  token must not provide inspection access. The two purposes are independent and
  non-interchangeable.
- TSC must not begin promotion as a consequence of inspection.
- TSC must not lift `"pending_fingerprint_authorization"` on any item as a
  consequence of inspection.

---

### 31. Status

**ACCEPTED DESIGN — NOT YET BUILT**

All seven corrections from the ChatGPT review applied. The inspection
authorization mechanism settled: a dedicated BAI `one_time_authorization_token`
with purpose `"tsc_inspection:<session_id>"`, entirely separate from the
promotion token, requiring SACL recognized-Ness confirmation at consumption
time, following all BAI token lifecycle rules.

No remaining concept questions. No files patched. No implementation claimed.
The TSC design is complete and ready for Master patch proposal when Ness directs.

<!-- NH_SOURCE_END filename="NH_ACCEPTED_TSC_DESIGN_v1.md" -->

---

# PART IV — PRESERVED ORIGINAL DESIGN-SOURCE SNAPSHOT

This is the original standalone wellbeing-baseline design source. Master §22 is the integrated architectural form, but this original wording is retained because it is not textually identical.

<!-- NH_SOURCE_BEGIN filename="NH_wellbeing_baseline_system.md" bytes=7926 sha256=afb1bad3c1edad3e86e76c5a1cb278b1a1e03c750d4fa1af6f54ad804bcc098c -->
# N.H — Wellbeing & Behavioral Baseline System
*Designed June 18, 2026. Emerged from ChatGPT feedback discussion.*

---

## What this is

A self-monitoring layer that protects both N.H's data integrity and Nes's personal wellbeing simultaneously — not as two separate features, but as one unified mechanism. The core insight: REALITY is built from Nes's judgment. When his judgment is compromised, both need protecting at the same time.

---

## The core philosophy (critical — do not dilute this)

This system does NOT measure Nes against external standards, clinical definitions, or universal distress signals. It measures Nes against **Nes**. His own baseline. His own patterns. His own values as expressed through his actual behavior over time — not what he says he believes, but what he consistently does.

The system learns who Nes is at his most grounded, and watches for meaningful divergence from that.

---

## Why Nes can't be the validator

When Nes is off-baseline, his judgment about whether the baseline is correct is also off-baseline. You can't see the shape you're in from inside the shape. This is the same reason self-diagnosis is unreliable in medicine. So:

- Nes does NOT approve or reject the baseline
- Nes does NOT decide if the system's assessment is correct
- The system validates itself against **internal consistency across time** — not against Nes's current opinion

This is not a limitation. This is the design. It's the only version that actually works.

---

## How the baseline gets built (passive, not written)

Nes does not write a constitution or define his values in a single session. That approach fails because:
- It may never get written
- A single session may not represent a truly clear state
- The stated version of values differs from the behavioral version

Instead, the system builds the baseline from behavior:
- Every REALITY promotion decision
- Every SIMULATION rejection
- Every conversation pattern
- Every type of question asked
- Every decision made across all sessions

Over time, consistent patterns emerge. These patterns *are* the baseline. Not declared values — demonstrated values.

**Periodic surface:** Monthly, the system generates a short summary of observed patterns. Nes can read it, make small corrections if something feels wrong, but cannot override the statistical picture — only refine it at the edges. The system decides if the correction is consistent with the broader pattern.

**Compounds over time:** More accurate at 6 months than at 1 month. More accurate at 1 year than at 6 months. The data does the work, not the complexity of the model.

---

## What triggers the system

### Physical triggers
Standard rate-limiting and safety thresholds — similar to how other well-designed AI systems handle physical wellbeing signals. Binary and visible. Either you can or you can't.

### Mental/behavioral triggers
This is the novel part. The system watches for:
- Actions that contradict values Nes consistently demonstrates
- Decision patterns that diverge from established baseline
- Language and reasoning patterns shifting in Nes-specific ways
- Behavior in one type of context contradicting behavior in another type of context
- Sustained divergence across multiple sessions (not a single bad day)

**Important:** A single session of divergence = noise. Sustained pattern across multiple types of interactions = signal. The threshold needs tuning once real data accumulates.

The specific patterns that constitute warning signals will be defined and refined over time as the system learns. They cannot be fully specified in advance — they emerge from the data.

---

## What happens when triggered (tiered response)

**Tier 1 — Silent flag:** System logs the divergence internally. No action taken. Monitoring intensifies.

**Tier 2 — Mirror signal:** System surfaces something to Nes directly. Not an alarm. A mirror. Something like: "Here's what I'm noticing. Here's how it compares to your baseline patterns. Are you aware of this?" Informational only — Nes can continue normally.

**Tier 3 — Queue throttling:** REALITY promotion slows. New records still enter SIMULATION normally. Queue builds but integrity is protected.

**Tier 4 — REALITY freeze:** REALITY promotion pauses entirely. Dry mode and research still work fully. N.H still functions as a thinking partner. Only REALITY growth stops.

**Unlock mechanism:** Upload of a document (psychiatric or medical appointment record) that the system treats as a verified good-state calibration point. Nes still does all the actual reviewing — the document is a forcing function and calibration anchor, not proof to anyone else.

---

## The psychiatric appointment as calibration anchor

This is more than an unlock key. It's a periodic external reference point — a moment where someone qualified looked at Nes and said "this is a good-state period." The system treats these timestamps as verified ground-truth reference points for the baseline.

Over time, the system can compare current patterns against the baseline established during verified good-state periods. This solves the hardest problem: if Nes has been in a compromised state for long enough, that state becomes the baseline. The appointment anchors prevent the baseline from drifting entirely into a compromised state.

---

## The one honest limitation

The system can validate internal consistency — "these patterns held across 6 months." It cannot validate whether those patterns represent a *healthy* version of Nes or a *consistently unhealthy* one. The appointment anchors are the solution to this. They are not optional — they are the only external reference in an otherwise fully self-referential system.

---

## Why this is architecturally clean

- No second person ever touches REALITY — sovereignty is preserved
- No external standard defines what "wrong" looks like — it's always Nes vs. Nes
- The gate is still only Nes — the system just adds conditions on when the gate opens
- Dry mode and research always work — the system never becomes useless
- Gets more accurate over time — compounds rather than degrades

---

## Implementation notes (for Cursor, when the time comes)

**Data sources for baseline engine:**
- `.nh_memory_store.jsonl` — promotion decision history
- `.nh_simulation_graph.jsonl` — rejection patterns
- Conversation logs — language and reasoning patterns
- Session metadata — timing, frequency, types of queries

**New record type needed:**
- `CALIBRATION_ANCHOR` — psychiatric/medical appointment document, timestamped, stored in REALITY, used as ground-truth reference by baseline engine

**New file (do not build until pipeline is complete):**
- `nh_baseline_engine.py` — pattern analysis, divergence detection, tier triggering
- This touches REALITY indirectly (reads patterns, triggers freezes) — treat as a Protected File when it exists

**Build order:** This comes AFTER the search pipeline is complete and stable. Do not start this until the pipeline is running nightly and the review queue has been healthy for at least a month. Baseline engine needs real data to work — building it before data exists is building an empty shell.

---

## Why this is novel

Behavioral baseline monitoring exists in cybersecurity (detecting account compromise). Longitudinal self-modeling exists in academic psychology research. Using a system's own decision history as training data for a model of the owner's judgment — that specific combination, for this purpose, for one person's sovereign AI — is a new application of existing ideas.

It is completely codeable with existing technology. Every component has a Python library. The sophistication comes from the design, not the implementation complexity.

---

## Status

Designed. Not yet built. Deliberately deferred until the search pipeline is complete and producing real data.

<!-- NH_SOURCE_END filename="NH_wellbeing_baseline_system.md" -->

---

# PART V — HISTORICAL HANDOFFS AND SUPERSEDED-STATE RECORDS

This handoff is historical. Its statements that the older Master/Defaults were authoritative and that TSC remained unfinished must not be followed as current instructions.

<!-- NH_SOURCE_BEGIN filename="NH_CHAT_HANDOFF_AFTER_BGMM.md" bytes=8081 sha256=f524f7cdd4dd2f1b897177e0e7f0843d1c8a7767341e4a010da9ab066414a562 -->
# NH_CHAT_HANDOFF_AFTER_BGMM.md

## Purpose

This file is a handoff record for the next N.H design chat session. It states
the current authority order, the state of all designs completed in the
security/identity/BGMM branch, and the starting point for the next session.

---

## Authoritative Files

The following files are the current authoritative N.H sources. They must always
be used together. No single file is sufficient without the others.

| File | Role | SHA-256 |
|---|---|---|
| `NH_MASTER-19_CORRECTED_v6.md` | Architectural authority — the complete settled N.H design | `8165f4bed94d2d57140d49e93d3c85b8e2b259053e0b30ac4c675fa7463a1bf9` |
| `NH_DECISION_DEFAULTS-S19_v1__1_.md` | Behavioral defaults companion — must be read alongside the Master | `ecea9224163681f9fc1d29327b0453c5e7ead42fd178786ab9dc6a6d4e1baaa6` |
| `NH_WORKING_ROLES.md` | Working relationship rules governing Claude, Ness, and ChatGPT | `a0281060abd7e7da791bb56a97316ab9ec41ab88fdd7884fac4c6434fa487619` |

**The next chat must inspect all uploaded files and confirm the authority order
before beginning any new design work.**

---

## Working Relationship Rules

`NH_WORKING_ROLES.md` governs the working relationship and must be followed:

- Claude is the architecture and audit brain. Cursor writes code. Ness runs all
  commands and verifies on disk.
- ChatGPT's role is limited to catching contradictions, gaps, and technical
  errors. ChatGPT must never fill open questions or propose what the system
  should do. All concept and meaning decisions belong entirely to Ness.
- One step at a time. No step proceeds without explicit Ness approval.
- Patch-only, no-loss discipline. No file is overwritten. No changes applied
  without explicit approval.

---

## Components Accepted and Complete

The following components were designed, corrected through multiple iterations,
and explicitly accepted by Ness during the security/identity/BGMM branch.
All are marked **ACCEPTED DESIGN — NOT YET BUILT** and are preserved in full
in `NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md`.

1. **BOP — Behavioral Observation Processing** (detailed design)
2. **Other-Speaker / Guest / Known-Person Architecture** (high-level, final)
3. **SIA — Speaker Identity Assessment** (detailed design)
4. **SACL — Speaker Access-Control Layer** (detailed design)
5. **Wellbeing / Identity / Security Separation Rules**
6. **BAI — Biometric Authorization Interface** (detailed design)
7. **Initial Owner-Phone Pairing** (four states, QR lifecycle)
8. **Recovery-Code Lifecycle** (creation, save verification, local test,
   activation, rotation)
9. **Future-Phone Replacement Flow**
10. **Atomic Emergency Recovery Flow**
11. **Initial Ness Voice-Profile Enrollment Bootstrap**
12. **Formally Adopted Vocabulary Additions:**
    - BOP `session_authorization.authorization_type = "enrollment_declared"`
    - §7L `link_type = "enrollment_material_provisional"`
13. **BGMM — Biometric-Gated Maintenance Mode** (detailed design, all
    corrections applied)

**BGMM was the most recently completed component.**

---

## No Master Patch Has Been Authorized From This Branch

None of the designs listed above have been patched into the Master
(`NH_MASTER-19_CORRECTED_v6.md`), the Decision Defaults, or `.cursorrules`.
The accepted designs exist only in `NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md`
and in the chat history.

Before any design from this branch enters the Master, the full patch-only,
no-loss, no-silent-deletion protocol must be followed. No patch is authorized
until Ness explicitly approves it.

---

## Next Unfinished Component

**Temporary Session Cache (TSC) — detailed design**

This is the next component requiring detailed design. It was established at the
high-level architecture stage (section 7 of the other-speaker architecture) but
has not received detailed component design.

### Settled TSC Rules Carried Forward

These rules are already settled and must be preserved exactly in the detailed
design:

- Third-party session material enters a TSC rather than the long-term shared
  store during the session.
- The TSC uses §7E's pre-ingest holding area with the new blocker:
  `"pending_fingerprint_authorization"`.
- Held material is invisible to the Meaning Engine while held.
- The TSC preserves the complete session context including Ness's words when
  they give meaning to another person's statements.
- Every speaker's exact contribution is preserved with speaker attribution,
  certainty, timing, turn order, branches, surrounding context, N.H outputs,
  BOP behavioral observation roots, SIA assessment events, and session metadata.
- TSC lifecycle: `active` → `sealed` (on session close) → `authorized` (after
  fingerprint for the relevant completed session) → `promoting` → `promoted` or
  `promotion_failed`.
- Cache sealing: on session close, TSC is sealed immediately; a `cache_sealed`
  security audit event is written immediately.
- The fingerprint authorizes the complete pending cache from the relevant
  completed session — not all sealed caches from all sessions simultaneously.
  Ness does not select individual people, memories, or items within the cache.
- After fingerprint authorization: all items with no remaining blockers proceed
  through §7E → sealed store → §7G → readings → §7J → §7M → §7L proposals
  without requiring additional manual Ness input.
- TSC promotion requires two independent conditions: purpose-bound BAI
  `one_time_authorization_token` with purpose `"tsc_promotion:<session_id>"`
  AND a currently valid recognized-Ness session (non-stale, from SACL) at
  consume time.
- If promotion fails partway through: items not yet promoted remain in
  `authorized` state; `append_root()` idempotency prevents duplicate writes;
  promotion resumes on restart for unpromoted items.
- The reading queue, Meaning Engine, clash detection, Computed View trigger,
  and Person-Box linking proposals all run through the mechanism's normal rules
  after promotion.
- Security audit events for TSC operations are written immediately:
  `cache_sealed`, `cache_authorization_received`, `cache_promotion_started`,
  `cache_promotion_completed`, `cache_promotion_failed`.

### What the TSC Detailed Design Must Add

The detailed design must cover at minimum:

- Exact TSC record schema and storage format.
- How the TSC relates to and extends the §7E pre-ingest holding area.
- How items within the TSC are attributed to their speakers with certainty.
- How branches and conversational context are preserved.
- How Ness's material within the TSC retains its own attribution and processing
  eligibility without being excluded from context.
- How the TSC handles a session that includes multiple different known persons.
- Exact promotion sequencing — which items promote first, how blockers are
  resolved, how speaker-unresolved items are handled.
- How the TSC survives app crashes, restarts, and unexpected session termination.
- Idempotency of promotion.
- How the TSC integrates with BAI (two-condition promotion check), SACL (session
  validity check at consume time), BOP (observation roots carried in the TSC),
  §7E (pre-ingest holding), §7G (reading after promotion), §7L (Person-Box
  proposals), and the security audit log.
- Failure, rollback, and fail-closed behavior.
- Privacy handling for third-party content in the TSC.

---

## Instructions for the Next Session

1. Inspect all uploaded files and confirm the SHA-256 hashes match those in
   this handoff document.
2. Confirm the authority order: Master → Decision Defaults → Working Roles →
   this handoff → the accepted designs file.
3. Read the full accepted TSC rules carried forward above before proposing any
   new design.
4. Begin detailed design of the Temporary Session Cache only.
5. Do not patch the Master or any existing file until Ness explicitly authorizes it.
6. Do not make concept decisions. Bring all genuine concept questions to Ness
   one at a time.

---

*End of NH_CHAT_HANDOFF_AFTER_BGMM.md*

<!-- NH_SOURCE_END filename="NH_CHAT_HANDOFF_AFTER_BGMM.md" -->

---

## V.2 — Superseded Master

This is a complete verbatim historical copy of the superseded v6 Master. It is retained for no-loss provenance and is not current authority.

<!-- NH_SOURCE_BEGIN filename="NH_MASTER-19_CORRECTED_v6.md" bytes=283081 sha256=8165f4bed94d2d57140d49e93d3c85b8e2b259053e0b30ac4c675fa7463a1bf9 -->
# N.H — MASTER-19: Full Backup with All Additions
### The single N.H system reference. Everything — system, status, the filter rules, the meaning engine, the model layer, the person-boxes, the tape, the DUMB-vs-SMART machinery frame, the code rules, the complete S17 and S18 conceptual design, AND all S19 restorations and additions — is written out IN FULL below. Nothing is referenced-only.

*Rebuilt June 20 2026 (session 3); updated sessions 4–13. Session 14 (June 23 2026) was a DESIGN-then-BUILD session → MASTER-15. S14 closed the three genuinely-open forks AND shipped the next build. Session 16 (June 24 2026) was a BUILD session → MASTER-16. S16 built Engine B (context-search), gold v2-B (7 sealed context-requiring cases), and the Chroma rebuild (`nh_roots_v1`). Hardware upgrade path decided. Engine B scored 6.5/7 on the tested dolphin 8B setup. Current evidence points to a model-capability or prompt/context interaction limit rather than a confirmed engine defect; this remains a hypothesis to re-test on a stronger model.*

*Session 17 (June 24 2026) was a broad conceptual-design session. S17 completed the core conceptual architecture of the major components addressed during the session, while several larger areas remain open. No code was written in S17. S17 additions are [CONCEPTUALLY DESIGNED, NOT BUILT] or [PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT] as stated in the authoritative status table.*

*Session 18 (June 24 2026) was a focused conceptual-design session for Attention and Relevance Control, designed interactively one decision at a time with Ness and checked by ChatGPT and Ness before adoption. Fourteen decisions were made and checked. No code was written in S18. The component is marked [CORE CONCEPTUALLY DESIGNED, NOT BUILT]. This file is a candidate; it becomes authoritative only after Ness reviews and adopts it.*

*★ The DECISION-DEFAULTS file should be regenerated as S18, synced to this master.*

*Session 19 (June 25 2026) was a RESTORE + AUDIT + EXPAND session. No code was written. Work fell into four kinds: (1) Security rules restored — §8 research pipeline security block (synthesis text-in/text-out, auto-reject-never-auto-delete, rejected-bin "look don't touch" display rules) confirmed dropped between Master-5 and Master-17 and restored. Brave-over-Tavily design reasoning and prompt-injection threat model added to §8. Academic source open decision (Google Scholar off table; Semantic Scholar vs OpenAlex pending) added to §11. (2) Companion file content integrated — §7A now includes the full Keystone resolution (one continuous reader, classification never locked, memory only adds, Ness as steerer). §7B now includes the seven webs in full (intent, deixis, common ground, implicature, theory of mind, time/sequence, re-reading), the inform-don't-ask sovereignty rule (Part 6), and the permanent clickable log (Part 7). (3) New design sections added — Wellbeing and Behavioral Baseline System (§22), Mobile App Three-Mode Companion (§23), and Connection Capability (§24). (4) §13/§14 expanded — live mechanism SVG embedded; chat front door design sketch content folded into §14 as design-in-progress. §16 mouth model status corrected: dolphin-llama3 = current test model on disk, not final adopted choice; Dolphin 3.0 R1 Mistral 24B = first local candidate to test after GPU upgrade; final Interactive Translator = undecided. §10 academic citations restored.*

*★ CORRECTION PASS (June 24 2026, S16): interaction-control wording was separated from project workflow; direct artifact delivery was clarified; several predictions and hardware/cost claims were changed from certainty to testable hypotheses or dated decision snapshots; one query-volume unit error was corrected. No prior master was overwritten.*

*★ S17 CONSOLIDATION (June 24 2026): core conceptual architecture added for the catalog front door, context retrieval, meaning engine interior, reread lifecycle, view layer, contradiction and clash handling, story layer, person-boxes, computed view, action surfacing, action-result return path, and permission and authority boundaries; the Living State Web and privacy/deletion/sensitive-data handling were partially conceptually designed. Interface and world design log incorporated. Engine B overclaims corrected throughout. `subject` field audited and documented. §7D revised from conceptual destination to partial design. New §§7E–7Q added. New §§18–19 added.*

*★ S17 DOCUMENT-CORRECTION PASS (June 24 2026): removed build-script debris; reconciled status wording; restored the historical S16 provenance line; aligned privacy access rules with Ness-private access being open by default; kept action outcomes and causation revisable; clarified View Layer versus Computed View ordering, append-only clash history, pre-ingest metadata-only visibility, action-risk mapping, and the presentation-only default for world manipulation. The original full draft was not overwritten.*

*★ S18 CONSOLIDATION (June 24 2026): core conceptual architecture added for Attention and Relevance Control (§7R). Fourteen decisions settled: output form (two-layer: context gate plus graded named dimensions with provenance), producer selection per dimension, evaluation timing, two-tier configuration contract, Ness's relationship, mouth-produced dimension validation, minimum shared vocabulary, Living State Web boundary, Tier 1 purpose field and controlled vocabulary, unresolved dimension handling across tier boundary, disagreement record schema, relevance event record schema, pattern observation conditions for per-judgment overrides, and unrecognized purpose type handling. Status table updated. Dependencies noted in §§7D, 7F, 7H, 7M, 7N. Open and next-work lists updated. New §7R added. New §20 change log added. NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md preserved unchanged.*

---

> ## ★ THE ONE AUTHORITATIVE STATUS TABLE (single source of truth — every other section must AGREE with this; if prose anywhere conflicts, THIS wins)
> *Status lives HERE, once. Prose may describe, never re-assert a different status.*
>
> | Component | Status | Proof / Note |
> |---|---|---|
> | Clean accretive store — 5,521 roots, 7-field, role-carried | **BUILT & VERIFIED** | `find /c` = 5521; re-verified S14 |
> | Roots file SEALED (`.nh_roots.sealed`) | **BUILT & VERIFIED** | append refused; re-verified S14 (0 bytes, dated 06/22 23:05) |
> | Two-file ROUTING (`append_reading`→sibling) | **BUILT & VERIFIED** | S13 |
> | READING RECORD — validator (`_validate_reading`, 12-field) | **BUILT & VERIFIED (S14)** | new function; 17/17 fixture tests pass; gates on shape not confidence |
> | READING RECORD — writer (reading-shaped `append_reading`) | **BUILT & VERIFIED (S14)** | signature now `(reads, meaning, confidence, role, story_layer, mode, produced_by, schema_version, derived_from, idempotency_key, record_id, timestamp)`; root-verify + idempotency + atomic append |
> | Shared `_check_common` helper (id+timestamp) | **BUILT & VERIFIED (S14)** | extract-not-fuse; roots still validate clean through it |
> | Reading-record `confidence` representation | **DECIDED (S14)** | §11 item 19 — TWO-SLOT object `{interpretation_confidence, source_reliability}`; source_reliability key-present / exact not-yet-knowable value representation remains unverified; NEVER one blended number |
> | Reading-record SHAPE overall | **SETTLED (S14)** | last open piece (confidence) resolved; validator now enforces it |
> | Gold scoring rule | **DECIDED (S14)** | §11 item 20 — six rules below; semantic match, Ness judges |
> | Engine failure-behavior | **DECIDED (S14)** | §11 item 20 — honest insufficient-context reading, marked revisable; retry-trigger deferred |
> | GOLD SET v1 — 8 cases, annotated + SEALED | **BUILT & SEALED (S14)** | `NH_GOLD_SET_v1.md` (4,951 B) + `.nh_gold_v1.sealed` marker on disk |
> | GOLD SET v2-B — 7 context-requiring cases, annotated + SEALED | **BUILT & SEALED (S16)** | `NH_GOLD_SET_v2_B.md` (5,449 B) + `.nh_gold_v2_B.sealed` marker on disk |
> | Quarantine readings store (`.nh_readings_quarantine.jsonl`) | **BUILT (S14)** | separate test file; holds A + B gold-run output; production readings store still absent |
> | Minimal engine A (`nh_engine_minimal.py`) | **BUILT & RUN (S14)** | root → mouth → 12-field reading → quarantine; run against the 8 gold; ~5–6/8 solid after prompt+role fixes |
> | Engine B (`nh_engine_b.py`) | **BUILT & RUN (S16)** | root → preceding turns → BACKGROUND prompt → mouth → 12-field reading → quarantine; run against gold v2-B; 6.5/7 on the tested setup; cause of B3 miss not yet proven |
> | Chroma `nh_roots_v1` (5,521 clean roots) | **BUILT (S16)** | rebuilt from clean roots via `nh_rebuild_chroma.py`; cosine distance; `all-MiniLM-L6-v2` embeddings |
> | `nh_rebuild_chroma.py` | **BUILT (S16)** | dry-run verified; full run 187.59s; keeps old collections untouched |
> | Production readings store (`.nh_readings_store.jsonl`) | **ABSENT (correct)** | no production readings yet; quarantine-only by design |
> | Speaker detector recipe (embed+shape→LogReg C=0.1→94.89%) | **INVESTIGATED & PROVEN, NOT DEPLOYED** | fallback only |
> | Ingest pipeline (`nh_ingest_chatgpt.py`) | **BUILT & VERIFIED** | S12 |
> | Chroma `nh_reality_core` (116,391) | **BUILT — OLD/unaligned index** | keep until `nh_roots_v1` proven; do NOT destroy |
> | The engine (2c) — full chain of webs | **PARTIALLY BUILT (A + B; C not built)** | A = meaning + role; B = + preceding context; C (story) NOT built |
> | Mouth model choice | **dolphin-llama3 = CURRENT TEST MODEL ON DISK (S14/S16)** | best tested on current hardware; this is the test model, not the final adopted Interactive Translator; Dolphin 3.0 R1 Mistral 24B = first local candidate to test after GPU upgrade (not yet tested, not adopted); final Interactive Translator model = UNDECIDED until testing and deliberate adoption by Ness |
> | Hebrew reading quality | **WEAK-BUT-WORKABLE; gated on bigger model/VRAM** | §16 — prompt changes alone did not solve it in the tested runs; larger-model/VRAM experiment planned (S16) |
> | Hardware upgrade path | **SETTLED DIRECTION: RTX 3090 24GB (verify at purchase time)** | settled direction: RTX 3090 24GB (supersedes S16 RTX 5060 Ti 16GB plan); exact stock, price, PSU compatibility, and model tag must be re-verified |
> | Multi-box (sealed-batch) architecture | **NOT DESIGNED** | §11 item 18 |
> | View layer | **CONCEPTUALLY DESIGNED, NOT BUILT** | two-view rule settled S17; §7I |
> | Quarantine promotion + memory-health checks | **DESIGNED, NOT BUILT** | §11 item 27 |
> | Pure-tape redaction/destruction path | **PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT** | policy, operation types, tombstone rule, blocking behavior, and verification outcomes designed in §7Q; storage mechanics, derivative discovery, cryptographic erasure, and verification implementation remain open |
> | Confidence value-form (low/med/high vs 0–1) | **DELIBERATELY LOOSE** | validator checks present+non-empty only; pinning later = new schema_version |
> | `subject` field (v1 roots) | **DOCUMENTED AS LEGACY PROVENANCE-BATCH TAG** | S17 audit; values are seed:conversations_000/001/002; rename deferred to next schema version; §6B |
> | Pre-ingest holding area | **CONCEPTUALLY DESIGNED, NOT BUILT** | seven lifecycle states, blocker list, unified store; §7E |
> | Catalog front door | **CONCEPTUALLY DESIGNED, NOT BUILT** | two gates, intake envelope, enrichment boundary; §7E |
> | Context retrieval layer | **CONCEPTUALLY DESIGNED, NOT BUILT** | two channels, per-mode parameters, bounded; §7F |
> | Meaning Engine interior flow | **CONCEPTUALLY DESIGNED, NOT BUILT** | one-pass rule, reading proposal acceptance check; §7G |
> | Reading Proposal Acceptance Check | **CONCEPTUALLY DESIGNED, NOT BUILT** | explicit validation step independent of mouth self-assessment; §7G |
> | Model confidence is metadata not authority | **FIRST-CLASS PRINCIPLE (S17)** | applies to all present and future models; §7G |
> | Story-layer evidence rules | **CONCEPTUALLY DESIGNED, NOT BUILT** | two channels, circular support prohibited; §7G |
> | Reread lifecycle | **CONCEPTUALLY DESIGNED, NOT BUILT** | three trigger types, full provenance; §7H |
> | Contradiction and clash handling | **CONCEPTUALLY DESIGNED, NOT BUILT** | six types, two detection modes, response events; §7J |
> | Story Layer | **CONCEPTUALLY DESIGNED, NOT BUILT** | structured perspective, firmness, hybrid themes; §7K |
> | Person-Boxes | **CONCEPTUALLY DESIGNED, NOT BUILT** | proposal-based creation, seven-section view; §7L |
> | Computed View | **CONCEPTUALLY DESIGNED, NOT BUILT** | seven-factor ordering, triggered snapshots; §7M |
> | Living State Web | **PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT** | node/edge types, grounding, currency, action surfacing, return path designed; schema, evidence thresholds, aging rules, trigger specifics, attention/relevance control, purpose-aware lenses, world model undesigned; §7D |
> | Action surfacing | **CONCEPTUALLY DESIGNED, NOT BUILT** | permission-controlled hybrid, possibility-disposition states; §7N |
> | Action-result return path | **CONCEPTUALLY DESIGNED, NOT BUILT** | two result types, six result states, three linked objects; §7O |
> | Permission and authority boundaries | **CONCEPTUALLY DESIGNED, NOT BUILT** | two layers, four risk levels, three action states, violation/correction rule; §7P |
> | Privacy, deletion, and sensitive-data handling | **PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT** | five operations, four sensitivity levels, deletion framework, exclusion system, third-party baseline, two-stage access control, private-access presumption designed; detection methods, verification procedures, implementation mechanics undesigned; §7Q |
> | Interface, World, and Interaction System | **IN-PROGRESS DESIGN, NOT BUILT** | architectural content incorporated; simulation interior, gesture vocabulary, VR, camera, accessibility substantially undesigned; design paused; §19 |
> | Attention and relevance control | **CORE CONCEPTUALLY DESIGNED, NOT BUILT** | fourteen decisions settled S18; two-layer relevance judgment, three producer types, two-tier mode contract, shared vocabulary, validation mechanism, record schemas; §7R |
> | Wonder and simulation mechanism | **CONCEPT LEVEL ONLY, MECHANISM NOT DESIGNED** | concept in §7B; interface concepts in §19 |
> | World model | **NOT DESIGNED** | named in Living State Web domain list |
> | End-to-end cycle | **IDENTIFIED, NOT YET DESIGNED** | the major components addressed in S17 and S18 have core conceptual architecture; simulation mechanism, world model, and the single connected end-to-end sequence remain open |
> | §8 research pipeline security rules | **RESTORED (S19)** | synthesis text-in/text-out, auto-reject-never-auto-delete, rejected-bin display rules — confirmed dropped between Master-5 and Master-17, now restored; Brave-over-Tavily reasoning and prompt-injection threat model added |
> | Connection capability (cross-record/cross-media) | **CONCEPTUALLY DESIGNED (S19), NOT BUILT** | lasting connection record, waiting area, one-way rule, three acceptance routes, five source types, certainty-controls-use; §24 |
> | Wellbeing and behavioral baseline system | **DESIGNED (full spec restored S19), NOT BUILT** | four tiers, baseline from behavior, psychiatric calibration anchor; §22 |
> | Mobile app — three-mode companion | **DESIGNED (full spec restored S19), NOT BUILT** | Full Mode (tunnel), Local AI online, Local AI offline; §23 |
> | Chat front door design sketch | **DESIGN-IN-PROGRESS, NOT CONFIRMED, NOT BUILT** | chat as first-class front door; recorded-conversation label; two-filter split (creation + meaning) explored but unconfirmed; §14 |
>
> **2a = COMPLETE. 2b = INVESTIGATED (not deployed). 2c = STARTED: A ✅ B ✅ C next.**

---

> **0. ★ THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK (S14).** What changed from S13:
>    - **BUILT & verified (S14):** `_validate_reading` — the 12-field shape gate. Rejects malformed, never rejects uncertain (R5). A low/weak/empty-story/insufficient-context reading is WRITTEN-and-marked, never refused. 17/17 fixture tests pass.
>    - **BUILT & verified (S14):** reading-shaped `append_reading` — verify-referenced-root-before-commit, idempotency reject on `idempotency_key`, atomic append (flush+fsync), append-only, writes to a target path.
>    - **BUILT & verified (S14):** `_check_common` — shared id+timestamp checks, extracted ONCE; `_validate_record` (roots) now delegates to it. The 5,521 sealed roots STILL validate clean through the helper (regression proven).
>    - **The reading record contract (12 fields):** `id · reads · meaning · confidence · role · story_layer · mode · timestamp · produced_by · schema_version · derived_from · idempotency_key`. `confidence` is now the TWO-SLOT object (see §6B). Coded, gated, verified.
>    - **The seal is per-BATCH, not "no more data ever."** ⚠ multi-box architecture still undesigned (§11 item 18).
>
> **1. ★ THE READING-RECORD SHAPE IS FULLY SETTLED (S14) — confidence resolved.** `story_layer` = a LIST of tellings; `mode` = an OPEN word + classification_confidence; unknown parts OMITTED. **And the last open piece, `confidence`, is resolved: a TWO-SLOT object** (`interpretation_confidence` + `source_reliability`), never one blended number. The validator enforces the whole shape.
>
> **2. ★ THE GOLD SETS ARE SEALED.** Two sealed gold sets on disk:
>    - **v1 (S14):** 8 clean-bare cases — each judged as a standalone line, no surrounding context needed. `NH_GOLD_SET_v1.md` + `.nh_gold_v1.sealed`.
>    - **v2-B (S16):** 7 context-requiring cases — each unreadable without preceding turns. `NH_GOLD_SET_v2_B.md` + `.nh_gold_v2_B.sealed`. Cases: B1 `7ac0381c` "episode 2"; B2 `4e125b71` "yes sure, second."; B3 `0df151d3` "yes, second option."; B4 `9359edff` emotional reaction to outline; B5 `580d74d4` "Brief slow."; B6 `09514821` "Yes! This is it."; B7 `4b4e5551` "כן".
>    - The gold seal holds for both: engine output may FAIL a case but may NEVER alter it; a correction is a NEW versioned gold.
>
> **3. ★ ENGINE A IS BUILT AND RAN (S14). ENGINE B IS BUILT AND RAN (S16).**
>    - **Engine A** (`nh_engine_minimal.py`): root → mouth → 12-field reading → quarantine. No context. ~5–6/8 on gold v1.
>    - **Engine B** (`nh_engine_b.py`): root → `_get_preceding_turns(n=3)` → BACKGROUND prompt → mouth → 12-field reading → quarantine. 6.5/7 on gold v2-B. B3 miss may reflect model-size, prompt-role separation, or context-format interaction; the present run does not prove which cause dominates.
>
> **4. ★ ENGINE B DESIGN DECISIONS (S16 — protect from re-litigation):**
>    - **Context strategy = POSITION-BASED, not semantic search.** `_get_preceding_turns` finds the N roots immediately before the target in the same `source_title` thread. Semantic search (`nh_roots_v1`) was tried first — pulled topically related roots but not conversational context. Position-based is the correct lever for conversational turns.
>    - **n=3 preceding turns, FULL content (no truncation).** Truncation at 100 chars was killing context quality — removing it fixed B5 ("Brief slow." read correctly only with full preceding assistant turn visible).
>    - **BACKGROUND/END BACKGROUND prompt framing (DECIDED S16).** Prevents the mouth from answering or continuing the conversation instead of reading the target line. The four rules: do not reference background, do not quote/paraphrase background, do not invent, if short confirmation say what they are confirming based on topic.
>    - **Observed Engine B score on the tested dolphin 8B setup = 6.5/7.** B3 read the content of the chosen option rather than the act of choosing. The leading hypothesis is a role-separation/model-capability limit, but context selection, prompt framing, and run variance remain possible contributors. A 13B model is a test, not a guaranteed fix.
>    - **Full-thread reading = future goal.** Load more or all of a conversation thread before reading each line. On the current 6GB setup this is likely impractical at the desired quality and speed. A larger-VRAM card and a model with a larger usable context window may make it practical, but must be benchmarked rather than assumed.

> **★ DECISIONS LOCKED IN SESSION 14 (protect from re-litigation):**
> - **`confidence` = a TWO-SLOT object** `{ interpretation_confidence, source_reliability }`. `interpretation_confidence` filled on every reading; source_reliability must be present as a key from the first reading. Its exact value representation when reliability is not yet knowable remains unverified and must be confirmed from the live validator or authoritative schema contract. NEVER one blended number; confidence never rises from copied error; a reading never inherits a prior's confidence. Story firmness inside `story_layer[].firmness`; retrieval relevance computed at search time, never stored. `mode.classification_confidence` is local and separate. SETTLED.
> - **GOLD SCORING — six rules.** (1) `meaning` judged by SEMANTIC match; Ness decides same/not-same by hand. (2) `story_layer` NOT graded in v1/v2-B. (3) MAKING SOMETHING UP is the real fail; leaving something out is NOT a fail if what's said is right. (4) Correct-but-EXTRA: true extra passes, made-up extra fails. (5) A case MAY list several acceptable readings. (6) NESS decides pass/fail; model assists, never judges. SETTLED.
> - **ENGINE FAILURE-BEHAVIOR.** When the engine can't interpret a root: writes an honest INSUFFICIENT-CONTEXT reading, MARKED revisable. Retry-trigger DEFERRED. SETTLED.
> - **CONFIDENCE VALUE-FORM left deliberately LOOSE** — validator checks present+non-empty only; pin later as new schema_version. SETTLED-as-deferred.
> - **VALIDATOR STRUCTURE = option C (extract, don't fuse).** `_check_common` holds shared id+timestamp. SETTLED + BUILT.
> - **MODEL FINDING (S14):** dolphin-llama3 beats qwen2.5-abliterate:3b. Hebrew quality is model-size-gated. SETTLED-as-finding.

> **★ DECISIONS LOCKED IN SESSION 16 (protect from re-litigation):**
> - **HARDWARE UPGRADE PLAN — dated decision snapshot, not a permanent market fact.** Candidate: RTX 5060 Ti 16GB (Gigabyte AERO OC, model GV-N506TAERO OC-16GD). At the time of the S16 discussion, a פי.סי סנטר listing was reported at ~₪2,590 with a stated 3-year warranty. Intended purchase date: 5.7.2026. Before purchase, re-check exact model, VRAM, seller, stock, current price, physical clearance, power connectors, PSU quality/wattage, and return/warranty terms. 16GB VRAM is preferred for larger local models, but VRAM is not the only relevant factor; model quantization, context length, memory bandwidth, thermals, PSU, and software support also matter. The exact `dolphin-llama3.1:13b` tag and expected speed must be verified by an actual pull/benchmark. Cards below 12GB are disfavored for this specific upgrade goal, not categorically unusable for all N.H work.
> - **TARGET MODEL AFTER UPGRADE.** A 13B-class uncensored model is the target. `dolphin-llama3.1:13b` is the current candidate name, but the exact available Ollama tag, license, quantization, VRAM fit, speed, and quality must be verified at installation time. Model swap rule: run the candidate against BOTH sealed gold sets (v1 + v2-B) and adopt only if the measured results improve. Old readings keep old `produced_by`. No auto mass re-read.
> - **ENGINE B CONTEXT STRATEGY = POSITION-BASED.** Settled. Do not re-open as semantic search.
> - **ENGINE B PROMPT = BACKGROUND/END BACKGROUND FRAMING.** Settled. Do not re-open.
> - **COST NOTES CONFIRMED.** N.H current monthly cost = $0. At full nightly automation (far down build list): Brave ~$62/month + OpenRouter synthesis ~$60-240/month = ~$120-300/month total. During building/testing: $0 (inside $5 free Brave credit). **SAFETY NOTE (build requirement for item 8):** Brave has NO spending cap — a loop can bill without stopping. When research pipeline is wired, a query counter / daily cap MUST be in the code. Not optional.

> **★ DECISIONS LOCKED IN SESSION 17 (protect from re-litigation):**
> - **CATALOG FRONT DOOR:** Two gates (raw capture and root ingestion). Minimum intake envelope defined. Pre-ingest store with seven lifecycle states and blocker list. Speaker and thread resolution rules. Four enrichment categories. All settled; §7E.
> - **CONTEXT RETRIEVAL:** Two channels (positional and semantic), kept separate and labeled. Per-mode retrieval parameters. Genuine no-context handling. System failure separation. All settled; §7F.
> - **MEANING ENGINE INTERIOR:** One reading per pass. Flow: root + context → mouth proposal → Reading Proposal Acceptance Check → reading record. Model confidence is metadata not authority (first-class principle). Story-layer two-channel evidence rule. Circular support prohibited. All settled; §7G.
> - **REREAD LIFECYCLE:** Three trigger types (manual, condition-based, scheduled-retry-only). All settled; §7H.
> - **VIEW LAYER:** Two-view rule (current and history). Ordering is presentation only. All settled; §7I.
> - **CLASH HANDLING:** Six clash types. Two detection modes. Ness response as separate event. All settled; §7J.
> - **STORY LAYER:** Structured perspective model. Firmness as engine inference. Hybrid theme system. All settled; §7K.
> - **PERSON-BOXES:** Proposal-based creation. Seven-section default view. All settled; §7L.
> - **COMPUTED VIEW:** Seven-factor ordering. Triggered immutable snapshots. All settled; §7M.
> - **ACTION SURFACING:** Permission-controlled hybrid. Possibility-disposition states defined. All settled; §7N.
> - **ACTION-RESULT RETURN PATH:** Two result types. Six result states. Three linked objects. All settled; §7O.
> - **PERMISSION AND AUTHORITY BOUNDARIES:** Two layers. Four risk levels. Three action states. Stop-and-surface violation rule. Narrow emergency stop exception. All settled; §7P.
> - **PRIVACY, DELETION, SENSITIVE-DATA:** Five operations. Four sensitivity levels. Deletion blocking/verification rule. Capture exclusion two-layer system. Third-party baseline. Two-stage access control. Private access for Ness open by default. Model-provider limitations recorded as mouth limitations. These core rules are locked, but the area remains **partially conceptually designed** because several policy details and implementation mechanisms are still open; §7Q.
> - **LIVING STATE WEB:** Node/edge types, grounding rule, currency rule, action surfacing, action-result return path, and relationships to Computed View/Story Layer/Person-Boxes/authority/privacy designed. Schema, evidence thresholds, and several domains remain undesigned; §7D.

> **★ DECISIONS LOCKED IN SESSION 18 (protect from re-litigation):**
> - **ATTENTION AND RELEVANCE CONTROL — FOURTEEN DECISIONS SETTLED:** Output form (two-layer: context gate + graded named dimensions with provenance; no collapsed hidden score; relevance is purpose-scoped only). Producer selection per dimension (three types: rules, embedding model, mouth; each with declared provenance; mouth declaration-authorized only and may not self-approve). Evaluation timing (on-demand by default; optional triggered pre-computation for declared latency-sensitive contexts; no global relevance state; precomputed results context-bound with explicit validity and invalidation conditions). Two-tier configuration contract (Tier 1 owned and validated by Attention and Relevance Control; Tier 2 owned and validated by consuming component; mouth authorization dimension-scoped and context-scoped; Tier 1 must reference Tier 2 unresolved-dimension handling rule by identifier and version when mouth dimensions are declared). Ness's relationship (inspection always available; per-judgment corrections and context-scoped overrides direct and append-only; mode changes use proposal-and-confirmation with consequence surfacing; invalid configurations identified precisely and translated with intent preserved). Mouth-produced dimension validation (deterministic validation with six checks and three outcomes: validated, failed, unresolved; validated ≠ substantively correct; optional model-based validation requires declared independence; disagreement recorded and follows declared uncertainty behavior; mouth dimensions may not act as context-gate conditions). Minimum shared vocabulary (four gate conditions; nine named dimensions; positional/semantic channel identity is retrieval provenance not a dimension; privacy and deletion eligibility are external prerequisites not gate conditions). Living State Web boundary (relevance events emitted, never written directly; relevance and currentness permanently separate; circular support prohibited). Tier 1 purpose field (structured object: required controlled type from five-value vocabulary plus optional explanatory label; label carries no system behavior). Unresolved dimension handling across tier boundary (Tier 1 must carry identifier and version of Tier 2 handling rule when mouth dimensions declared). Disagreement record schema (stable identifier; separate pointers to producer and validator results; disagreement type; identities and versions; uncertainty behavior rule; resulting dimension state; timestamp; append-only). Relevance event record schema (stable identifier; mode; purpose; consuming component; context/request identifier; target objects; candidate type; evaluation mode; trigger when pre-computed; outcome summary counts; pointers to judgments; timestamp; append-only). Pattern observation conditions (multiple overrides sharing same mode/version, same gate/dimension/outcome, same correction direction required; surfaced as possibility only; silence not dismissal; explicit dismissal closes until new evidence; never changes mode automatically). Unrecognized purpose type handling (halt evaluation; identify unknown type; preserve original request; explain in plain language; offer mapping to existing type with Ness confirmation or new type proposal through versioning process; never guess silently). All settled; §7R.

> **PRIOR DELTA (SESSION 13 → MASTER-14) — condensed for continuity:**
> - [BUILT]-claims sweep done. 2a PLUMBING BUILT. Detector investigated (94.89%). Eleven doc-refinements + quarantine/bootstrap captured.

> **PRIOR DELTAS (sessions 4–12) — condensed for continuity:**
> - **S12:** store restored; `role` added (7-field); clean ingest; 5,521 clean roots; Chroma=old 116k; two-destinations shape.
> - **S11:** MODEL LAYER resolved; PERSON-BOXES, PURE TAPE, WONDER/SIMULATION, CATALOG, SOUL CORRECTION.
> - **S10:** 2a shaped; DUMB vs SMART frame; HELPER not DECIDER; story-layer; mode = peer web.
> - **S9:** the PREMISE §0; reality → per-person READING; speaker = carry `role`.
> - **S4–S8:** accretive store skeleton; unit = span-claim; forced build order; WhatsApp data-rescue (NOT ingested); live loop + chat front door + guard.
> - **S14:** three forks CLOSED. Reading validator + writer BUILT (17/17 tests). Gold v1 (8 cases) SEALED. Engine A BUILT & run (~5–6/8). dolphin beats qwen-abliterate-3b. Confidence value-form left loose.
> - **S15-chat:** NO N.H change. Scan-only + one teaching artifact (`NH_one_pass_demo.html`).
> - **S16:** Engine B BUILT & run (6.5/7 on gold v2-B). Gold v2-B (7 cases) SEALED. Chroma `nh_roots_v1` BUILT (5,521 roots). Hardware upgrade path decided. Cost notes confirmed.

> **THE NAME:** He is **Ness** (male). He signs **Ness**. Use Ness.

> **HOW TO READ THIS FILE:** N.H is mid-evolution. **[BUILT]** = verified on disk today. **[CONCEPTUALLY DESIGNED, NOT BUILT]** = the core conceptual architecture and governing rules are settled, while exact schemas, thresholds, implementation details, or interface mechanics may remain open where explicitly listed. **[DESIGNED]** = older shorthand for decided but not coded. **[PARTIALLY CONCEPTUALLY DESIGNED]** = some core rules are settled while material conceptual areas remain open. As of S17: the clean store + role schema + ingest pipeline + 2a plumbing + reading record (validator + writer) + gold sets v1 + v2-B (both sealed) + engine A + engine B + Chroma `nh_roots_v1` are **[BUILT]**. The catalog front door, context retrieval, meaning engine interior, reread lifecycle, view layer, clash handling, story layer, person-boxes, computed view, action lifecycle, permission boundaries, and attention/relevance control are **[CONCEPTUALLY DESIGNED, NOT BUILT]**. The Living State Web and privacy/deletion/sensitive-data handling are **[PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT]**. Engine C is not built; the wonder/simulation mechanism, the world model, and the end-to-end cycle remain not designed or concept-level only.

> **★ STANDING LESSON (carried, still in force): trust disk, never the doc — including this file.** Before any build, existence-and-shape check first.

---

## 0. THE PREMISE — NEVER DECIDE FACTS (NEVER CLOSE THE BOOK)  [DESIGNED — the floor under every rule]

**The line:** The danger N.H exists to stop was never *reasoning* — it was reasoning *hardening into authority*: a living guess freezing into a closed, settled fact. The AI may reason fully — connect, guess, build on its own past reasoning, hold opinions, leave notes, get richer over time, even wonder/simulate forward at night — and do everything except one thing: **close the book on something into a decided fact.** Every conclusion stays a non-decisive, accreting layer; nothing it concludes ever promotes itself to "real."

**The crystallization:** **N.H is Ness's HELPER, not Ness's DECIDER.** A helper reads, connects, lays out what it sees, even leans — then hands it to the person, who decides. A decider closes the book.

**★ THE SOUL CORRECTION — three truths held at once, never collapsed:**
1. **Interpretive meaning is never stored as a universal fact — it remains a situated story** (§3G). There is no fact-box for *meaning*.
2. **Ness still decides / affirms.** He is the decider, the membrane. The system does NOT decide what is real — and neither does it pretend nothing is ever decided.
3. **★ His deciding is NOT a node in the engine.** It happens out in real life, engine absent. There is no step after "show." *(S13 cross-link: recording THAT he reacted is allowed — item 23's seam stores the OCCURRENCE as a dated, weightless story-layer event so a dismissed reading stops resurfacing. What stays off-board is the TRUTH-verdict.)*

**The crucial distinction:** "never decide facts" does NOT mean "never hold anything firmly." Something can be held with full weight and still never close the book.

**★ S13 SHARPENING:** the DUMB machinery MAY establish directly-verifiable machine-state & provenance facts. The SMART machinery MAY interpret, connect, lean — but may NEVER silently promote an interpretation into an established fact. The authority for any such promotion is Ness, off-board.

**★ S14 LIVE EXPRESSION OF §0 — the engine reads by PATTERN, so it can be wrong, and that is designed-around, not a flaw.** The mouth places a line by similarity to millions of lines it has seen; it does not truly understand. So it WILL misread sometimes. Every guard exists precisely because of this: never-close-the-book, confidence, only-adds, Ness-decides-off-board, and the gold. A system that assumed it was always right would be the dangerous one.

---

## 0A. THE TWO MACHINERIES — DUMB vs SMART (psychologics)  [DESIGNED — top-level frame]

- **DUMB MACHINERY — moves and holds data; built stupid on purpose.** The pure tape, the append-only store, the two files (roots sealed, readings beside), the pointers (`re_reads`), role-carried-from-source, the catalog's who/when/where marking, CARRYING/STORING the `mode` label once SMART has named it, the person-box GATHER, the live loop's fire-and-let-go. One law: **never interpret, never close — only add / point / carry / sort / gather.** Safe BECAUSE it cannot interpret.

> **★ THE PURE TAPE NEEDS A REDACTION/DESTRUCTION PATH (safety).** "Append-only" must NOT mean "permanent recoverable storage of every secret forever." Allowed: capture exclusions for credentials/secrets; encrypted storage; retention boundaries; cryptographic erasure of selected content; an append-only TOMBSTONE retaining THAT a deletion occurred without the deleted plaintext; special treatment for third-party and childhood data. The governing policy is partially conceptually designed in §7Q; exact storage mechanics, cryptographic-erasure methods, derivative discovery, backup handling, and verification implementation remain undesigned (§11 item 24).

> **★ "ABSENCE IS READ" NEEDS A GUARD.** Absence is meaningful ONLY when the system EXPECTED the info, the process was CAPABLE of observing it, the absence is relevant, and the interpretation is held WEAK. Distinguish `not_observed`/`not_evaluated`/`not_applicable`/`withheld`/`collection_failed` in processing metadata; a blank in a reading stays honest (never `"unknown"`).

- **SMART (psychologics) MACHINERY — reads the *person*.** The meaning webs (Theory of Mind, the STORY-layer, gap-reading, firmness-as-read), the mode/register NAMING (open-word `mode` + classification_confidence), clash-surfacing, the wonder/simulation, the NOTE. One law: **everything here is weightless, dated, confidence-tagged, rejectable — NEVER a fact.** Safe BECAUSE it cannot close.
- **THE BORROWED MOUTH (§16) sits at the seam, used by SMART.** The wording model turns meaning into sentences — swappable. The embedding/search model is a DUMB tool (sorts by meaning-distance).

**The membrane (§7A R7) is the boundary between them** — creation (SMART) never closes into memory (DUMB).

---

## 1. WHAT N.H IS

N.H ("Jarvis") is a personal, sovereign AI memory system running locally, 24/7, on Ness's own Windows machine. Not a product — infrastructure for his own thinking, memory, and research.

**The one-line soul:** **N.H is Ness's HELPER, not Ness's DECIDER.** The loop: *real life → into N.H for help → it helps him see and understand his own thinking in the way that fits how he thinks → he returns to real life with a solution that is his own.*

**★ WHAT JARVIS ACTUALLY IS:** Jarvis is NOT the model. The model is a borrowed, frozen mouth (§16). **Jarvis is the memory + the soul + the gathering + the mouth, wired together.**

**★ MEMORY IS UNDERSTOOD KNOWLEDGE THAT GROWS.** New input is *read* by the webs and lands as a reading (meaning + confidence + story-layer). The growth lands in the memory, never in the frozen mouth.

**★ THE TWO-DESTINATIONS SHAPE (Ness re-derived it):** every **eligible accepted** input goes to TWO places at once — (1) the **RAW ROOT**, saved untouched and sealed; (2) **THROUGH THE FILTER**, which READS it and lays a **READING** beside the root, pointing back by id, never altering the raw. The only change a root can undergo is deliberate, audited destruction (§7Q). This is exactly why there are TWO FILES.

**The two purposes, always running together:**
- **INWARD — the mirror:** show Ness the shape of his own thinking from the outside.
- **OUTWARD — the engine:** translate new external data through the lens of how *his* mind connects things.
- **ONE FILTER, BOTH DIRECTIONS.** The two feed each other.

---

## 1A. THE INPUT-AGNOSTIC PRINCIPLE — ONE ENGINE, MANY FRONT DOORS  [DESIGNED]

Text, images, video, audio — all flow through the SAME engine. New input types get a new **front door**, not a new engine. Two stages (§14): RAW capture → CATALOG (who/when/where). The live chat itself is a front door.

**The deepest "why" — הכל יחסי:** nothing about *meaning* is final — a thing means what it means only relative to ever-growing context, and relative to whom. This is why memory only adds, classification is never locked, "unknown" is honest, and the affirmation surface is a per-person STORY, not a shared fact-box.

---

## 2. HOW TO WORK WITH NESS

- **Direct tone, plain language, ONE step at a time.** He asks "why yes / why no" and wants real tradeoffs. He often asks for things "plainly" — give the plain version directly. **(S14: when explanations didn't land, the fix was always to go simpler and more concrete, with a worked example — never more abstraction.)**
- **Verify on disk, never trust status reports.**
- **Honest correction over flattery** — explicitly, repeatedly asked for.
- **Don't inform, just flag and keep going.**
- **Pull Sovereignty** — no unsolicited pushes; Ness sets direction.
- **Casual comms are normal** — typos, voice-to-text, Hebrew, elongated punctuation are NOT distress.
- **He catches things.** When he pushes back, he is usually right.
- **He works to UNDERSTAND before moving.** This is not hesitation — it's him needing the mechanism to fit his head. Honor it; go slower, not faster.
- **He is not afraid of work.** A wall is almost never "this is hard" — it is "this move would destroy/forfeit something."
- **He re-derives his own design from the inside.** Offer shapes, let him rebuild and steer.
- **Backup before any destructive step, always.**
- **Primary risk pattern: scope-expansion before consolidation.** Finish and verify the current project task before expanding scope. This governs task order only; it does not authorize ending, pausing, or redirecting the conversation.
- **Assistant role:** architecture, audit, security, strategy, explanation, and direct artifact creation. Cursor may write or edit code when Ness chooses to use it; Cursor is not required for ordinary documents or Markdown files. Ness runs and verifies commands that affect his machine or project state.
- **Session authority:** Ness alone decides when a session begins, pauses, ends, or moves to a fresh chat. Do not suggest sleep, rest, wrapping up, a fresh chat, or end-of-session documentation unless Ness explicitly initiates it. End-of-session master/defaults regeneration is an optional workflow triggered only by Ness.

---

### 2A. INTERACTION AND ARTIFACT DELIVERY — LOCKED

- **Latest instruction wins.** If Ness rejects a method, stop using and mentioning that method unless he later reopens it.
- **Anti-loop rule.** After the same misunderstanding is corrected twice, abandon the current plan, restate the exact requested deliverable in one sentence, and produce it directly.
- **Actual-file rule.** When Ness asks to create, update, rebuild, or deliver a file, return the actual downloadable file. Do not substitute Cursor, CMD, PowerShell, terminal, Notepad, copy-paste, or manual-creation instructions unless Ness explicitly asks for that workflow.
- **Version safety.** Create a new versioned file; never silently overwrite, rename, delete, or replace the previous authoritative master. The prior master remains authoritative until Ness reviews and adopts the new one.
- **No false human-state explanations.** Do not explain mistakes by claiming tiredness, impatience, being on fumes, or "losing it." Say plainly that the instruction was misread or an incorrect plan was repeated.
- **No session pressure.** Project discipline such as "finish and verify" applies to task order, never to whether Ness should sleep, stop, document, or close the session.

---

## 3. THE EVOLUTION — OLD vs NEW (key points)

- **A. Manual gate → MEMBRANE.** Memory only ADDS. [Accretive store BUILT; clean roots S12; sealed S13.]
- **B. Many "is this real?" gates → ONE UNIVERSAL FILTER.** [DESIGNED §7A; engine A BUILT S14; engine B BUILT S16.]
- **C. AI creativity → the membrane.**
- **D. Security holes found on disk → fixed.** *(⚠ `cloudflared.exe` inert but on disk — convenience-sweep item.)*
- **G. Affirmation surface → per-person STORY-layers.** [DESIGNED.]
- **H. The person → PERSON-BOXES.** [CONCEPTUALLY DESIGNED §7L.]
- **I. "Do I train a model?" → BORROW A FROZEN MOUTH** (§16). [DESIGNED + on disk.]
- **J. (S12) The store — from a 188-stub → 5,521 CLEAN roots.** [BUILT & VERIFIED.]
- **★ K. (S14) The reading record — from DESIGNED-NOT-CODED → BUILT validator + writer + engine A + sealed gold v1.** [BUILT & VERIFIED.]
- **★ L. (S16) Engine B — from NOT BUILT → BUILT & RUN at 6.5/7 on sealed gold v2-B. Chroma rebuilt from clean roots. Hardware upgrade path decided.**
- **★ M. (S17) Broad conceptual design of the major components addressed during the session** — core conceptual architecture for the catalog front door, context retrieval, meaning engine interior, reread lifecycle, view layer, clash handling, story layer, person-boxes, computed view, action lifecycle, and permission and authority boundaries; partial conceptual design of privacy/deletion/sensitive-data handling and the Living State Web. Several larger areas remain open. No code written.
- **★ N. (S18) Core conceptual design of Attention and Relevance Control** — fourteen decisions settled interactively with Ness, checked by ChatGPT and Ness. Two-layer relevance judgment, three producer types, two-tier mode contract, shared vocabulary (four gate conditions, nine named dimensions), validation mechanism for mouth-produced dimensions, Living State Web boundary, purpose field controlled vocabulary, record schemas, Ness's relationship, and pattern observation conditions. No code written.
- **★ O. (S19) Restore + audit + expand** — §8 security rules restored; §7A Keystone + §7B seven webs + inform-don't-ask + LOG written out fully; §10 academic citations restored; §13/§14 expanded with live mechanism diagram and chat front door sketch; §16 mouth model corrected; wellbeing baseline, mobile app, and connection capability added as full sections.

---

## 4. THE MACHINE

- **Path:** `C:\Users\user\nh_engine_core`, Windows 11 build 10.0.26100.7840 (24H2). Python **3.13.14**.
- **CPU** i5-11400 · **GPU** RTX 2060 (6GB VRAM). **Motherboard ASRock B560 Pro4** (PCIe x16, 8-pin PCIe power available). **Case Antec NX410.** 32 GB RAM. *(Verified by inspection S14.)*
- **Launched via** `run_app.pyw` → pywebview at `http://localhost:8080/`. The CORE is LOCAL and offline by default; only the optional research connectors touch the network.
- **★ MODEL HARDWARE REALITY:** the 6GB 2060 runs 3B models normally (~35–50 tok/s); 7B/8B run but SLOW (~7–9 tok/s). Context window is limited.
- **★ UPGRADE PATH (settled direction: RTX 3090 24GB — supersedes S16 RTX 5060 Ti 16GB plan; verify all details before purchase):** Engine B scored 6.5/7 on the current tested setup. A larger-VRAM GPU and a model candidate are the next experiment, not a guaranteed fix. **Settled direction: RTX 3090 24GB;** exact model variant, seller, price, and warranty details must be verified before purchase. PSU quality, wattage, connectors, case clearance, thermals, exact VRAM variant, and return terms must be verified before purchase. After installation, verify the exact available model tag, benchmark it against both sealed gold sets, and adopt only if results improve. **Future goal:** determine whether wider or full-thread context becomes practical at acceptable speed and quality.
- **Windows sign-in:** Kensington VeriMark fingerprint key.

---

## 5. THE CODEBASE MAP

**Core architecture (PROTECTED — never modify without dry-run + explicit "APPROVED"):**
`nh_memory_store.py` · `nh_context_router.py` · `nh_reality_graph.py` · `nh_simulation_graph.py` · `nh_epistemic_sandbox.py` · `nh_evidence_integrity.py` · `nh_jarvis_core.py` · `nh_crypto.py` · `nh_vector_memory.py`. *(OLD REALITY/SIMULATION gate stack — still runs harmlessly; do NOT rip out before the new filter is complete.)*

**Physical stores on disk (verified S14/S16):**
- **`.nh_accretive_store.jsonl` — 5,521 CLEAN roots, SEALED** (7-field). Roots-of-record.
- **`.nh_roots.sealed`** — seal marker (0 bytes, 06/22 23:05). `append_root` refuses while it exists.
- **`.nh_readings_store.jsonl`** — production readings sibling. **ABSENT** (no production readings yet — correct).
- **`.nh_readings_quarantine.jsonl` (S14)** — QUARANTINE test readings file. Both engines write here, never production.
- **`NH_GOLD_SET_v1.md` (S14)** — sealed gold answer key, 8 clean-bare cases (4,951 B).
- **`.nh_gold_v1.sealed` (S14)** — gold v1 seal marker (0 bytes).
- **`NH_GOLD_SET_v2_B.md` (S16)** — sealed gold answer key, 7 context-requiring cases (5,449 B).
- **`.nh_gold_v2_B.sealed` (S16)** — gold v2-B seal marker (0 bytes).
- Backups: `.bak_preseal` (roots), `.bak_188_preclean`, `nh_accretive_store.py.bak_pre_minimal_engine_A_*` (S14).
- **`chroma_db\` — ChromaDB.** `nh_roots_v1` = 5,521 (NEW, clean roots, S16) · `nh_reality_core` = 116,391 (OLD index — keep until proven) · `nh_test_asm` = 1,180 · `nh_simulation_core` = 263.

**Source files on disk:** `conversations-000/001/002.json` (all INGESTED CLEAN S12). `gpt_purified_history.txt` + `cleaned_history (1).txt` (NOT ingested — redundant/damaged).

**Models on disk (verified S14/S16):** Ollama `dolphin-llama3:latest` (UNCENSORED, 4.7 GB, 8B — **CURRENT TEST MODEL ON DISK, not the final adopted Interactive Translator**) · `llama3:latest` (4.7 GB, 8B) · `huihui_ai/qwen2.5-abliterate:3b` (1.9 GB — pulled S14 for Hebrew test; read worse than dolphin, NOT adopted). `models\all-MiniLM-L6-v2` (embedding/search + detector embedding model).

**Accretive store + tooling [BUILT & VERIFIED]:**
- **`nh_accretive_store.py`** — restored S12, extended S13, extended S14. Append-only; schema validated before every append. S14 additions: `_check_common`, `_validate_reading`, reading-shaped `append_reading`, `QUARANTINE_READINGS_PATH`.
- **`nh_engine_minimal.py` (S14, NEW)** — Engine A: `read_root(root_id)` → mouth → 12-field reading → quarantine. `run_on_gold()` runs the 8 v1 gold cases. `MOUTH_MODEL` constant = `dolphin-llama3`.
- **`nh_engine_b.py` (S16, NEW)** — Engine B: `read_root_b(root_id)` → `_get_preceding_turns(n=3)` → BACKGROUND prompt → mouth → 12-field reading → quarantine. `run_on_gold()` runs the 7 v2-B gold cases. `MOUTH_MODEL` constant = `dolphin-llama3`. Context = position-based preceding turns from same `source_title`, full content, no truncation.
- **`nh_rebuild_chroma.py` (S16, NEW)** — rebuilds `nh_roots_v1` from clean roots. `--dry-run` flag for 10-root test + retrieval check. Full run: 5,521 roots, 187.59s. Never touches old collections.
- **`test_reading_validator.py` / `test_minimal_engine_dryrun.py` (S14)** — fixture harnesses (temp paths only).
- `nh_ingest_chatgpt.py`, `verify_rt.py`, `nh_log.py`, `nh_probe*.py`, the S13 detector probes (`nh_embed_confirm_speaker.py` = the recipe reference).

**`.cursorrules` v3.2 (in-force):** §6A. Dual-architecture reconciliation applied (session following S19). Legacy gate rules preserved; accretive store, reading engines, and five settled protection decisions added; three-layer stack map in place. Stale "188 seed records" docstring in `_validate_record` still needs cleanup when that file is next touched under a CONFIRMED edit.

**Out-of-system artifacts (NOT components):** `NH_one_pass_demo.html` (S15-chat) — teaching visualization only; does NOT appear in the status table.

---

## 6. WHAT'S BUILT & VERIFIED ON DISK  [BUILT]

- **★ THE CLEAN ACCRETIVE STORE — 5,521 roots, 7-field, role-carried, SEALED.**
- **★ 2a COMPLETE: two-file routing + sealed roots + the READING RECORD (validator + writer, 12-field contract) — BUILT & VERIFIED (S14).**
- **★ THE GOLD SET v1 — 8 clean-bare cases, SEALED (S14).**
- **★ THE GOLD SET v2-B — 7 context-requiring cases, SEALED (S16).**
- **★ ENGINE A (`nh_engine_minimal.py`) — BUILT & RUN against gold v1 (S14). ~5–6/8.**
- **★ ENGINE B (`nh_engine_b.py`) — BUILT & RUN against gold v2-B (S16). Tested dolphin 8B setup scored 6.5/7; cause of remaining miss not isolated.**
- **★ CHROMA `nh_roots_v1` — BUILT (S16). 5,521 clean roots, `all-MiniLM-L6-v2` embeddings.**
- **★ `nh_rebuild_chroma.py` — BUILT (S16). Dry-run verified.**
- The restored store module + clean ingest pipeline.
- The speaker-detector recipe INVESTIGATED & PROVEN (~94.89%), NOT deployed.
- The OLD REALITY/SIMULATION gate (still runs harmlessly).
- The OLD populated vector memory (~1.78 GB, 116k `nh_reality_core` — keep until `nh_roots_v1` proven).
- Three local models in Ollama (dolphin, llama3, qwen2.5-abliterate-3b).

**Known regression pattern:** verify on disk; the doc's remembered state has been wrong repeatedly.

---

## 6A. THE CODE RULES — `.cursorrules` v3.2 (DUAL-ARCHITECTURE, IN FORCE)

*The live disk file at `C:\NH\nh_engine_core\.cursorrules` is what Cursor operationally reads and is authoritative for Cursor's behavior. In any conflict between this summary and the disk file, the disk file governs. This section contains a complete durable summary for self-containment — a new session reading only this Master can understand the governing rules, the protection boundaries, and the three-layer architecture without access to the disk file. When the disk file is updated, this section must be updated to match.*

*Provenance: v3.1 (June 20 2026, 15,303 bytes) governed the still-running REALITY/SIMULATION gate only; the accretive store was described as future in §12 INCOMING. v3.2 (session following S19) reconciles the dual architecture: legacy gate rules preserved in full; accretive store and reading-engine rules added; three-layer stack map replaces stale dual-stack entry; five protection decisions settled by Ness incorporated. The disk `.cursorrules` was not overwritten during any prior session — v3.2 is the proposed updated text, adopted in this session.*

---

### IDENTITY AND PERMANENT RULES

These rules apply to all architecture layers and all sessions with no exceptions.

**Cursor proposes. Ness approves. Cursor implements.** Never skip the approval step, even for changes that appear small or obviously correct. This rule has no architecture dependency.

**Permanent prohibitions (all layers):** Never touch `.env`, `.nh_pin.json`, vault contents, `NH_PROMOTE_TOKEN`, API keys, or the PIN hash. Never write test or mock data into any production store. Never build a second parallel implementation of any gating, promotion, or write-validation logic outside the designated module for each layer.

---

### THE THREE-LAYER ARCHITECTURE

The codebase contains three architecture layers that coexist on disk. They are not equally active.

**Layer 1 — Oldest legacy data and code (retained; not the active build target; do not extend or write into).** Designated read-only in `.cursorrules` v3.1. Whether any Layer 1 code still executes is unverified from available evidence and must not be assumed. Verified retained artifact: ChromaDB `nh_reality_core` (116,391 records — kept until `nh_roots_v1` proven in production; do not destroy, merge, or modify). Additionally referenced in v3.1 as Layer 1: `nh_timeline.json` and `nh_nightly.py` — current disk presence and execution status of both are unverified.

**Layer 2 — Still-running REALITY/SIMULATION gate stack (active legacy sovereignty mechanism; do not weaken).** Built after the June 19 2026 audit found a real sovereignty bypass in production code. Governs the running chat, HUD, and research pipeline. `promote_to_memory()` in `nh_context_router.py` is the one authorized path for unverified content into REALITY. Status labels `INFERRED`, `GENERATED`, `VERIFIED`, `REPORTED_SPEECH` apply here only. `NH_PROMOTE_TOKEN` is active. Files: `nh_context_router.py`, `nh_memory_store.py`, `nh_reality_graph.py`, `nh_epistemic_sandbox.py`, `nh_evidence_integrity.py`, `nh_simulation_graph.py`, `nh_research_engine.py`, `nh_research_sandbox.py`, `nh_jarvis_core.py`, `nh_crypto.py`, `nh_auth.py`, `nh_vector_memory.py`. Stores (documented as actively used as of June 19 2026; current disk behavior not re-verified): `.nh_memory_store.jsonl`, `.nh_reality_store.jsonl`, `.nh_simulation_store.jsonl`, `.nh_simulation_graph.jsonl`, `nh_mental_network.json`. Layer 2 rules remain in force until Ness explicitly decommissions the legacy gate.

**Layer 3 — Current accretive store and reading engine stack (active build target).** All new engine and storage development goes here. Files: `nh_accretive_store.py`, `nh_engine_minimal.py`, `nh_engine_b.py`, `nh_rebuild_chroma.py`. Stores: `.nh_accretive_store.jsonl` (5,521 sealed roots), `.nh_roots.sealed`, `.nh_readings_quarantine.jsonl` (test-only), `.nh_readings_store.jsonl` (absent by design, correct), ChromaDB `nh_roots_v1` (5,521 roots, `all-MiniLM-L6-v2` embeddings, built S16). The accretive store is built and sealed as of S16.

---

### SOVEREIGNTY BOUNDARIES BY LAYER

**Layer 2 sovereignty boundary:** `promote_to_memory()` in `nh_context_router.py`. `ContextRouter.write()` is NOT a gate by itself — it was the exact bypass found in the June 19 2026 audit. Any write of a REALITY-layer record with status other than VERIFIED must go through `promote_to_memory()`. The Layer 2 prohibitions remain in force for all old-stack writes.

**Layer 3 sovereignty boundary:** `nh_accretive_store.py` is the complete write boundary. `append_root()` is blocked while `.nh_roots.sealed` exists. `append_reading()` calls `_validate_reading()` (shape gate), verifies root ids in the sealed store, checks idempotency, and routes to quarantine or production path based on the path argument supplied. `_validate_reading()` gates shape only — it rejects malformed records, never uncertain ones. No direct file writes to any accretive store are permitted under any circumstances.

**Production readings gate — decided, not yet implemented:** Production writes through `append_reading()` must additionally require `.nh_readings_production_authorized` to exist and must fail closed if absent. This behavior is settled by design decision but has not yet been implemented in code. It requires a separately approved change to `nh_accretive_store.py`. Until implemented, the prohibition is enforced as a Cursor behavioral rule: no code initiating production writes may be proposed or applied without both protections in place.

---

### SCHEMA CONSTRAINTS

**7-field root schema (v1, sealed):** All seven fields must be present on every root record: `id` (uuid4) · `subject` (provenance batch tag in v1 — not a semantic topic; values are `seed:conversations_000/001/002`) · `timestamp` (ISO 8601 creation time) · `content` (raw text) · `re_reads` (list; `[]` for a root) · `source_title` (required field; value may be `None` where no source title is known — `None` is explicitly permitted by the root schema; do not substitute the string `"unknown"`; do not omit the key) · `role` (speaker from source; required on new writes). Do not add fields to v1 roots. Schema changes require a new `schema_version` and Ness's deliberate adoption.

**12-field reading schema (v1, built and verified S14):** `id` · `reads` · `meaning` · `confidence` · `role` · `story_layer` · `mode` · `timestamp` · `produced_by` · `schema_version` · `derived_from` · `idempotency_key`.

Critical constraints: `reads` is a non-empty list of root ids, each verified to exist in the sealed store before commit. `confidence` is a two-slot object `{interpretation_confidence, source_reliability}` — never a single number. Both keys must be present on every reading. `interpretation_confidence` is filled on every reading. `source_reliability` must be present as a key from the first reading. Its exact permitted value when reliability is not yet knowable is unverified from live code and must be confirmed from the live `_validate_reading()` implementation or the authoritative schema contract before v3.2 is adopted. Do not invent a sentinel — not an empty string, not null, not `"unknown"`, not an empty object, and not any other form without evidence. What is confirmed by the Master: the key is present from the first reading; the exact not-yet-knowable value representation remains unverified and must be confirmed from the live validator or authoritative schema contract; "empty-when-unknown is honest" (Master §6B, status table item S14). The exact JSON form of that emptiness is not confirmed from live code. `story_layer` is a list (empty list is valid); unknown sub-values within a story entry are omitted from that entry, never filled with `"unknown"`. `produced_by` must contain `origin` from the controlled vocabulary: `observed, imported, simulated, generated, reaction, human_annotation`. `schema_version` must be present on every new record. `idempotency_key` must be present and unique per store. A reading never copies root text — it points via `reads`.

---

### PRODUCTION READINGS AUTHORIZATION

`.nh_readings_store.jsonl` does not exist and must not be created as a side effect of any code or automated process. Two protections must both be satisfied before production writes may begin:

1. Ness must create the physical marker `.nh_readings_production_authorized` as a deliberate filesystem act. No code may create this marker. Its presence is necessary but not sufficient.
2. Cursor must submit and receive approval for a full PROPOSED CHANGE dry-run naming: the production store; the exact writer function; the source of the readings; the schema version; the promotion-review evidence; duplicate and idempotency handling; rollback handling; and confirmation that quarantine tests and manual inspection are complete.

The code-level enforcement of this marker in `append_reading()` is DECIDED but NOT YET IMPLEMENTED. It requires a separately approved change to `nh_accretive_store.py`. Until that change is approved and applied, the protection operates as a Cursor behavioral rule. Marker creation alone does not constitute approval for a specific code change or write session. Removing the marker disables future production writes without altering readings already stored.

---

### PROTECTED FILES AND STORES

**Protected Files — require "CONFIRMED: modify [filename]" before any edit; full dry-run protocol applies:**

Layer 2 (legacy gate — protect until Ness decommissions): `nh_context_router.py` · `nh_memory_store.py` · `nh_evidence_integrity.py` · `nh_reality_graph.py` · `nh_epistemic_sandbox.py` · `nh_simulation_graph.py` · `nh_research_engine.py` · `nh_research_sandbox.py` · `nh_jarvis_core.py` · `nh_crypto.py` · `nh_auth.py` · `nh_vector_memory.py`

Layer 3 (accretive — protect now): `nh_accretive_store.py` · `nh_engine_minimal.py` · `nh_engine_b.py` · `nh_ingest_chatgpt.py` · `nh_rebuild_chroma.py`

Not yet existing — creation gate: `nh_baseline_engine.py` (requires "CONFIRMED: create nh_baseline_engine.py" plus full dry-run and all §22 prerequisites confirmed; automatically Full Protected once created)

**Additional protection rules for specific Layer 3 files:**

`nh_engine_minimal.py` and `nh_engine_b.py`: any change to `MOUTH_MODEL`, prompt text, context-window behavior, `_get_preceding_turns`, `run_on_gold`, output destination, gold-set handling, or any behavior that could affect the meaning or comparability of benchmark results requires Ness's authorization and a re-run of both sealed gold sets before adoption. The current mouth model (`dolphin-llama3`) is a test candidate only — not the settled final N.H mouth model.

`nh_ingest_chatgpt.py`: every proposed change must identify the exact ingest behavior being changed; the effect on the 7-field root schema; source files involved; duplicate and idempotency handling; intended destination store; whether `.nh_roots.sealed` remains untouched; and how the change will be tested without writing into the sealed production store. Whether this file has an existing dry-run or test-path mechanism is not confirmed — Cursor must propose a test approach in the dry-run block. No edit may delete, rename, bypass, or automatically lift `.nh_roots.sealed`.

`nh_rebuild_chroma.py`: every proposed change must state the exact rebuild behavior being changed; source root store and expected root count; embedding model; destination Chroma collection; whether records will be replaced, appended, or rebuilt; how `--dry-run` will be used; how retrieval correctness will be checked; and whether the gold sets must be rerun. `nh_reality_core`, `nh_test_asm`, and `nh_simulation_core` must remain untouched unless Ness separately and explicitly authorizes otherwise.

**Protected Stores:**

Layer 2 (documented as actively used as of June 19 2026; current disk behavior not re-verified): `.nh_memory_store.jsonl` · `.nh_reality_store.jsonl` · `.nh_simulation_store.jsonl` · `.nh_simulation_graph.jsonl` · `nh_mental_network.json`

Layer 3 — root store and seal marker: `.nh_accretive_store.jsonl` (no direct writes at any time; no root appends while `.nh_roots.sealed` exists; future appends through `append_root()` only after Ness explicitly lifts the seal and separately approves the ingest session) · `.nh_roots.sealed` (do not delete, rename, or write to through any normal store operation; only Ness may remove it deliberately; removal is a prerequisite for future ingest, not authorization for a specific session)

Layer 3 — readings (quarantine only until both production protections are satisfied): `.nh_readings_quarantine.jsonl` · `.nh_readings_store.jsonl` (absent; protected against premature creation)

Chroma — do not modify or drop: `nh_roots_v1` (active) · `nh_reality_core` (retained; do not destroy until `nh_roots_v1` proven) · `nh_test_asm` · `nh_simulation_core`

Gold sets — never modify: `NH_GOLD_SET_v1.md` + `.nh_gold_v1.sealed` · `NH_GOLD_SET_v2_B.md` + `.nh_gold_v2_B.sealed` · `NH_GOLD_SET_CONTEXT_v1.md` (drafted and approved; not yet placed or sealed as of last verified record; treat as Protected when placed)

---

### DRY-RUN PROTOCOL

Before writing any code that touches a Protected File or any write-path function, Cursor must output a PROPOSED CHANGE block and wait for "APPROVED":

```
PROPOSED CHANGE:
- File: [filename]
- What changes: [one sentence]
- Store(s) touched: [name each; for Layer 3 state quarantine or
  production explicitly]
- Gate function used, by exact name + file: [e.g.
  append_reading() in nh_accretive_store.py — quarantine path]
```

Then full proposed code — no placeholders — then wait for "APPROVED" before applying.

---

### §12 INCOMING — CURRENT STATUS

**Now built (in force for Layer 3 work):** I1 (memory only adds, never edits — append-only enforced by store structure and seal marker), I2 partial (quarantine-before-production enacts the membrane principle structurally; the membrane as a designed component is not yet built), I8 (two-file store, built and verified S14/S16).

**Designed but not built (do not write code against these):** I3 (one filter, no source exempt — `_load_raw_sources()` still loads seed files by filename), I4 (classification never locked — depends on reread lifecycle, §7H, conceptually designed not built), I6 (Ness steers not files — per-record `/review` still active), I7 (MODE as peer web — conceptually designed, not built).

**Legacy protections that continue to override:** I5 (sovereignty as standing position) is NOT IN FORCE. The old per-record `/review` flow remains the active sovereignty mechanism. Layer 2 rules override §12 in any conflict until Ness explicitly says the new model is active.

---

## 6B. THE ACCRETIVE STORE — SCHEMA + STATE  [BUILT & VERIFIED]

*The DUMB-MACHINERY heart (§0A). Append-only; schema validated before every append; roots file SEALED.*

**★ ROOT record schema (SEVEN fields):** `id` (uuid4) · `subject` · `timestamp` (ISO 8601) · `content` · `re_reads` (list; `[]`=root) · `source_title` (string/None) · `role` (speaker from source; required on new writes).

**★ `subject` FIELD AUDIT (S17):** In v1 roots, `subject` is a provenance/import-batch tag, not a semantic topic. All 5,521 roots use only: `seed:conversations_000`, `seed:conversations_001`, `seed:conversations_002`. `nh_ingest_chatgpt.py` explicitly defines `SUBJECT_TAG` as "provenance tag for this batch." `nh_log.py` confirms: "groups every record by subject (provenance for now; real subjects arrive with the engine)." `read_by_subject()` and `nh_probe.py` actively depend on the field. **Rules:** (1) Do not modify or reinterpret `subject` in existing v1 roots. (2) Document it honestly as a legacy provenance-batch field in v1 despite the misleading name. (3) Future schema version: consider replacing with a clearly named field such as `source_batch` or `provenance_batch` — exact name undecided. (4) If N.H later needs a true semantic subject/topic, design it as a separate field or derived reading-layer object. Do not silently reuse this field. (5) No files or schemas change now.

**★ READING record schema — BUILT & VERIFIED (S14), 12 fields:** `id · reads · meaning · confidence · role · story_layer · mode · timestamp · produced_by · schema_version · derived_from · idempotency_key`. A reading NEVER copies root text — it points (`reads`). Show = read readings → follow `reads` into sealed roots → stitch. A re-read is a NEW reading beside the old. The validator (`_validate_reading`) gates SHAPE, never confidence: reject malformed, never reject uncertain.

- **`reads`** — list of root id(s), non-empty; the writer verifies each exists in the sealed roots before commit.
- **`meaning`** — the read (string). The honest insufficient-context read ("seen this, couldn't read it") is a VALID meaning.
- **★ `confidence` = a TWO-SLOT OBJECT (S14, DECIDED).** `{ interpretation_confidence, source_reliability }`, never a bare number. `interpretation_confidence` = how sure the engine is of this reading and must be present on every reading; its value-form remains deliberately loose for now. `source_reliability` = how trustworthy the source was. The key must be present from the first reading. Its exact value representation when reliability is not yet knowable remains unverified and must be confirmed from the live validator or authoritative schema contract. NEVER blended; confidence never rises from copied error; a reading never inherits a prior's confidence. Story firmness belongs inside `story_layer[].firmness`; retrieval relevance is computed at search time and never stored.
- **`role`** — who spoke, from the root.
- **`story_layer`** = a LIST of tellings (clash kept, nothing wins). Each: optional `whose · stance · firmness · telling · theme · when`. Empty list legal. Unknowns OMITTED, never `"unknown"`.
- **`mode`** = `{ label (open word: chat/composed/story/question/…), classification_confidence (local) }`. Not a fixed menu. `classification_confidence` is LOCAL, ≠ top-level confidence.
- **`produced_by`** = reproducibility-grade provenance. `origin` ∈ {observed, imported, simulated, generated, reaction, human_annotation} (REQUIRED). Engine readings carry model/digest/engine_version/prompt_version/config/retrieval_inputs. `human_annotation` readings (gold) carry annotator/when/context_version/change_reason.
- **`schema_version`** = present on every NEW record, `v1` for the first. Un-retrofittable.
- **`derived_from`** = list of parent reading ids; `[]` when fresh from roots.
- **`idempotency_key`** = operation identity, separate from `id`; the writer rejects an already-committed key.
- **`timestamp`** = CREATION time (≠ source/event/ingest).

**★ ON DISK NOW (verified S14/S16):** 5,521 clean root records, SEALED, all `re_reads=[]`. Production readings file ABSENT. Quarantine readings file holds both engine A and engine B gold-run output (test-only). The validator + writer are live; both engines write real readings through them into quarantine.

**No `reason`/`why` field, by design** — the why is shown by what a layer points at; the AI's view is the NOTE (§7B Part 7.5).

---

## 7. THE BIG DESIGN — UNIVERSAL FILTER + MEANING ENGINE  [engines A + B BUILT; §§7E–7P core-conceptually designed S17; §§7D and 7Q partially conceptually designed]

### 7A — THE UNIVERSAL FILTER (operating rules):
R0 reader/layer-er not judge; R0.5 never close the book; R1 one filter, no source exempt; R2 sorts/reads, never closes "real"; R3 one continuous reader; R4 meaning from wide context; R5 classification never locked; R5.5 the affirmation surface is a per-person STORY-layer (six optional parts; absence read ONLY under the §0A guard; CLASH surfaced not resolved; N.H not a teller, its view a weightless NOTE); R6 memory only ADDS (governs HISTORY; the COMPUTED VIEW decides current use); R7 the membrane; R8 associative bridging; R9 sort by meaning-type, mode a separate peer web; R10 maximal-but-bounded; R11 Ness steers, affirms off-board; R12 honesty about what this is.

**★ THE KEYSTONE (reached June 19 2026 — the resolution that made everything cohere).**

*One filter, not two stages.* There are not two tools (extractor + filter). There is one continuous reader applied in a single pass. The same faculty that detects "the meaning just shifted here" is the faculty that says "and this is what kind of meaning it is." Finding the boundary and naming the type are the same act. Segmentation and classification fall out of one capability: words flow in → the reader tracks the meaning → when the meaning-type shifts, it closes one statement, tags it, opens the next.

*Meaning comes from wide context, not local words.* The reader cannot classify a statement from the words in front of it. The same words mean different things depending on a large, accumulated, far-wider context built up across many sentences. A line that looks like a claim in isolation may be sarcasm, a callback, a hypothetical — visible only against the wide frame. So: meaning is context-dependent at scale.

*Therefore classification is never locked.* Because meaning depends on wide context, and context keeps accumulating, every reading is provisional. A statement sorted months ago can be re-read and recolored when later context reveals what it actually meant. This is the same principle as SIMULATION-before-REALITY, now at the level of meaning itself: a piece's meaning is always a current best reading against current context, never a final verdict.

*The contradiction this dissolved — why Ness rejected manual sorting.* The system once rested on Ness being the manual gate. But "meaning is never final" means manual sorting freezes readings that shouldn't be frozen. The two beliefs fought: "I must be the gate" (sovereignty) vs "nothing is ever final" (meaning keeps moving). Ness felt this tension before he could name it — it's why something in him deeply rejected manual sorting.

*The resolution: memory only ADDS, never edits.* When new context recolors an old statement, the system does NOT change what's there — it adds a new layer: "this earlier statement, read against this new context, now means this." The original reading stays. The new reading joins it. Nothing is ever overwritten. This dissolves everything: meaning stays revisable ✓, nothing is destroyed ✓, Ness is not a clerk ✓. Memory accretes — a record of how meaning evolved, not a snapshot of "what's currently true." It never lies about its own past because it never deletes it.

*Ness's role, redefined.* Ness is not the sorter. The AI does the continuous adding/re-reading/layering itself. Sovereignty is standing authority to steer and override a record that never stops growing and never erases itself. The gate isn't a moment of manual approval — it's his power to correct and direct.

### 7B — THE MEANING ENGINE (mechanism):
Part 0 THE PURE TAPE (verbatim, append-only, outside memory; capture-exclusions + audited redaction — §0A); Parts 1–2 the chain of webs; Part 2.5 THE STORY-LAYER WEB; Part 2.6 PERSON-BOXES; Part 3 webs combine; Part 4 nightly research (feeds MEMORY, not the mouth); Part 5 hold-until-enough; Part 6 can't-fill→inform-don't-ask (live: catalog MAY ask); Part 6.5 THE WONDER/SIMULATION; Part 7 THE LOG; Part 7.5 THE NOTE/THE WHY.

**★ THE CHAIN OF WEBS — SEVEN WEBS (from NH_Meaning_Engine_Design, June 20 2026).**

A piece's meaning is NOT one flat tag. The meaning lives in how the dimensions relate in this specific piece. The engine runs the piece through a chain of webs — each web one real dimension of meaning. The piece "lights up" a pattern in each web. The real meaning is what holds up across all the webs together, not any single snapshot. This is "one continuous reader, not two stages" made concrete.

*The category list (claim/ask/feel/report/intend/wonder/imagine) is ONE web — the intent web. It is NOT the whole engine. It is one dimension among several.*

**The seven webs (research-grounded, deliberately open-ended):**

1. **INTENT — what were they doing by saying it.** Speech-act / illocutionary dimension. The five-to-eight categories live here (state/claim, ask, promise/intend, express/feel, declare, report, wonder, imagine). One web, not the machine.

2. **DEIXIS — anchor the "pointing words" to reality.** Resolve who / when / where. Person deixis ("she," "I"), temporal deixis ("next week," "moved"), spatial deixis ("there"), discourse deixis ("that thing you said"). Distance can be psychological, not physical.

3. **COMMON GROUND — what's shared and assumed.** The unspoken backdrop both parties already knew and didn't have to say. A piece means what it means partly because of what was presupposed.

4. **IMPLICATURE — what they meant beyond the literal words.** Gricean. Check the four maxims: Quality (truthfulness), Quantity (right amount), Relation (relevance), Manner (clarity). A flout of a maxim = the tell for sarcasm / irony / non-literal meaning. This is how the engine distinguishes a true claim from a sarcastic one before anything gets stored.

5. **THEORY OF MIND — model the mind behind it.** Read the piece against who said it and what cognitive/affective state they were in. The rational + intentional dimension of interpretation.

6. **TIME / SEQUENCE — where it sits in the flow.** A message moves (report → feel → dismiss → intend); the piece is one state in that chain. Partly deixis, partly N.H's own reading of movement.

7. **RE-READING — run the whole chain again later.** When new context arrives, re-run the chain → produce a NEW reading → add it as a layer, never overwrite. This IS the accretion. The re-reading web never truly closes.

*(List is deliberately open. New webs may be named as real life reveals dimensions the current set can't hold — but each must be a REAL dimension, grounded, not decorative.)*

**How the webs combine:** the webs fire together as one engine in one pass — not one-at-a-time. Separate lenses stacked into one camera; light passes through all of them together and one image comes out. The richness is breadth across the webs plus the relationships between what lights up — NOT depth-drilling into subcategories.

**★ Part 6 — CAN'T FILL → INFORM, DON'T ASK (the sovereignty rule, exact).**

If, after researching inward + outward, a web genuinely can't be filled, the engine does NOT silently auto-stamp it "unknown," and does NOT stop and ask Ness to decide. It INFORMS Ness: surfaces the specific gap by name — "this web, on this piece, I couldn't fill; here's exactly what's missing." Inform ≠ ask. Surface ≠ solicit. The engine keeps running. It does not queue the piece for Ness's approval. Nothing blocks on Ness. Because he's merely informed (not asked), Ness can go research his own life on his own time and give the answer back later, whenever. When he does give it back, that lands as a NEW LAYER, never an overwrite: "unknown on [date] → filled by Ness on [later date]." The honest "I didn't know this then" stays in the record forever. "Unknown" is therefore an honest, valid, re-checkable state — never a failure, never permanent.

**★ Part 7 — THE LOG (read-only, subject-tagged, permanent, clickable).**

The surface through which Ness sees the engine's nightly mind.

*Read-only / look-don't-touch.* Ness can SEE everything the engine did; he cannot EDIT the log. Read-only is load-bearing: it's the accretion rule made visible — the record never gets rewritten, so it can't lie about its own past. Same "look don't touch" principle as the rejected-bin display in §8.

*Seeing ≠ approving.* It's a log to read, not a queue to action. This is "inform, don't ask" turned into a browsable surface. No clerk work.

*Subject-tagged.* Every entry carries (subject = X) — e.g. (subject = family), (subject = the meeting). The log is organized by what each entry is about.

*Permanent + findable.* Because it's tagged and never deleted, Ness can come back weeks later, filter by subject = X, and the entire evolving history of that subject is still there, grouped and intact. The subject tags are the navigation layer that keeps infinite accretion usable.

*Clickable.* Subjects expand; entries open to show the piece, its webs, its unknown-flags, and its layers over time. Build note: standalone clickable prototype before wiring to the live engine.

**The log is three things at once:** (1) Transparency — proof of what the engine did; unalterable; honest because read-only. (2) The mirror (the INWARD direction of N.H) — Ness watching his own thinking sorted from the outside; the pattern he can't see because he's inside it. (3) A permanent subject-indexed archive — subject = X, come back anytime, all still there, navigable.

### 7C — THE FORCED BUILD ORDER (never re-fought):
**(2a) two-file routing + sealed roots + READING RECORD — ✅ COMPLETE (S14).** → **(2b) the detector — ✅ INVESTIGATED, recipe locked (S13); fallback, not deployed.** → **(2c) THE ENGINE — IN PROGRESS:** A ✅ BUILT (S14) → B ✅ BUILT (S16) → **C (story-layer) NEXT.** C needs story-bearing gold cases before it can be tested. **Build the LIVE path before the nightly deepening.**

**★ THE ENGINE LAYERS:**
- **A (BUILT, S14):** root → mouth ("say what the {role} is doing, don't describe/answer/invent") → 12-field reading → quarantine. Bare; no context, no story. ~5–6/8 on gold v1.
- **B (BUILT, S16):** + preceding turns context — `_get_preceding_turns(n=3)` pulls N roots immediately before the target in the same thread. BACKGROUND/END BACKGROUND prompt framing. Full content, no truncation. Tested dolphin 8B setup scored 6.5/7 on gold v2-B; the cause of the remaining miss has not been isolated — model capability, prompt framing, context format, and run variance remain possible contributors. **Future upgrade: full-thread reading with a larger model + larger context window — must be benchmarked, not assumed.**
- **C (NEXT):** + story-layer reading — fill `story_layer` (whose/firmness/theme). Needs story-bearing gold cases first.

---

## 7D. THE LIVING STATE WEB — PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT

WHY IT EXISTS. N.H currently models what something means, who said it, what story it belongs to, and what memories relate to it. That is a strong foundation. But a person is not only meanings and memories. At every moment a person also occupies a state — emotional, cognitive, bodily, practical — and moves through transitions between states across time, pressure, choices, and consequences. The Living State Web is the name for the future layer that would let N.H model that movement, rather than only interpreting individual messages.

WHAT DEPTH IT ADDS. The current engine reads a root and lays a reading beside it. The Living State Web would eventually allow N.H to understand not only what something means, but: what state may have shaped or accompanied it, what may have changed across relevant states, events, and readings over time, what is currently active and unresolved, what may be reachable from the present state, and what happened after action was taken. That is the difference between a meaning system and a partner that can model a living person moving through time.

CURRENT STATUS. PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT. S17 designed node and edge types, grounding rules, currency rules, action surfacing (§7N), the action-result return path (§7O), and relationships to Computed View, Story Layer, Person-Boxes, authority boundaries, and privacy boundaries. Several domains and all implementation details remain undesigned.

WHAT WAS DESIGNED IN S17 AT THE STRUCTURAL CONCEPT LEVEL.

Node and edge types: state nodes (time-bounded representations of experienced states), transition edges (possible connections between states with evidence), position nodes (simultaneous internal stances), open loop nodes (unresolved items consuming attention), relationship state edges (time-bounded connection states with people), causal hypothesis edges (proposed causal connections, always marked as hypotheses), counterfactual nodes (modeled possible worlds, always separated from actual states), value and constraint nodes (active values, fears, protected boundaries).

Grounding rule: every node carries (a) immediate source object IDs (readings, tellings, clashes, Ness response events, or other explicitly permitted derived objects) and (b) direct root IDs ultimately grounding it. Full derivation chain must remain inspectable. Circular support is forbidden — derived material cannot validate itself without root support. A node may not exist solely because another derived object asserted it. Weak or broken chains produce omission or an insufficiently-grounded marking, never invention.

Currency rule: state existence and currentness are two independent properties. Every state node records evidence time range, `last_supported_at`, currentness status, reason for that status, and rule/version used to assess currency. Six conceptual statuses: `current`, `possibly_current`, `stale`, `currentness_unknown`, `ended_by_evidence`, `superseded_by_evidence`. Time passing may move a node toward stale or currentness_unknown but may never alone mark a state ended. A state may be marked ended or superseded only through relevant new root evidence, a Ness response, or another explicitly authorized evidence-based rule. Different state types use different currency rules — a brief condition and a long-term constraint do not age at the same rate. Currentness is never a hidden decay score.

Action surfacing and return path: designed in full at §7N and §7O respectively. The Living State Web provides the state, open loop, value, and constraint evidence that action surfacing draws from.

RELATIONSHIPS NOW DESIGNED.

Computed View: the Living State Web is one source the Computed View draws from when assembling the current picture. The Computed View's seven-factor ordering and triggered snapshot rules apply when Living State Web material is surfaced.

Story Layer: story tellings are eligible source objects for Living State Web nodes. Tellings supply perspective and theme context. Story Layer rules on circular support and firmness apply when tellings are used as evidence.

Person-Boxes: relationship state edges in the Living State Web point to Person-Box identity anchors. Person-Box confirmation status and merge-proposal rules govern which identity anchor an edge may point to.

Permission and authority boundaries: action possibilities surfaced from the Living State Web pass through the authority system before any execution. §7P governs what may be done with surfaced possibilities.

Privacy boundaries: Living State Web nodes derived from third-party material follow the third-party data rules in §7Q. Pre-retrieval eligibility and pre-output review apply when Living State Web content is shown.

FUTURE DOMAINS — PARTIALLY DESIGNED AT THE STRUCTURAL CONCEPT LEVEL. The following had supporting structures designed in S17 (node types, edge types, currency, or retrieval rules), but their complete behavior, evidence requirements, interaction rules, and update mechanisms are not yet settled: transitions between states and what drives them; multiple simultaneous internal positions; relationship state and relational safety; possible causal chains; counterfactual paths; temporal identity across past, present, and possible future states; the loop act → observed result → reread (§7O); identity continuity across time and contexts (the currency rule supports temporal tracking but does not complete identity continuity design).

FUTURE DOMAINS — NOT YET DESIGNED AT ANY LEVEL: current emotional, cognitive, bodily, and practical state schema; needs, fears, protected boundaries, and active constraints schema; current capacity and cognitive/emotional load (open loop nodes may relate to capacity but are not the same — capacity/load representation is not yet designed); purpose-aware reading lenses; a world model beside the self model. Note: attention and relevance control is now core conceptually designed in §7R; its integration with Living State Web currency review triggers remains an open item for the Living State Web's own design session.

REMAINING UNRESOLVED: exact schema for all node and edge types; minimum evidence requirements and grounding-strength rules; currency time windows and state-type-specific aging rules; transition condition definitions; relevance triggers for condition-based action surfacing (the form and contract for these triggers is now established in §7R, but the Living State Web's own relevance mode declarations remain open); mapping of specific action categories to the four risk levels and category-specific evidence/permission thresholds; detection rules for automatic result detection; confirmation workflow for result connections; authorization of relevance events as currency review triggers (§7R establishes that relevance events may trigger a review but supply no currency evidence; the exact authorization rule governing when a review is initiated belongs to the Living State Web's own design session); purpose-aware reading lenses; world model beside the self model; build order position relative to other components.

HOW IT FITS N.H PHILOSOPHY. The Living State Web maps the state-space and possible movement. It never chooses the path. It never promotes its interpretation into settled truth. Ness remains the decider; the engine remains a helper. These are not new rules — they are the same soul rules that govern every existing layer.

---

## 7E. CATALOG FRONT DOOR  [CONCEPTUALLY DESIGNED, NOT BUILT]

TWO GATES. Raw capture and root ingestion are separate. A root cannot be written to the sealed store until all required catalog fields are resolved. Raw material is never destroyed merely because a field is unresolved.

MINIMUM INTAKE ENVELOPE. Every front door must produce the same minimum before the pre-ingest store accepts the capture: (1) one stable unique `capture_id`; (2) the exact raw payload or a stable immutable reference to it; (3) capture timestamp; (4) front-door / source type; (5) payload format or media type; (6) source-provided metadata, preserved without reinterpretation; (7) enough provenance to trace how and where the capture occurred. Front doors may additionally provide any reliable source-derived catalog fields they already know. They must not guess missing values to satisfy handoff.

DESIGN BOUNDARY. `front door = capture and normalize` / `pre-ingest catalog = evaluate completeness and manage resolution`. A front door cannot hand over an unidentifiable blob. A malformed capture that cannot meet the minimum envelope enters an explicit capture-error path with available material preserved. Never silent drop.

PRIVACY AND EXCLUSION PRECEDENCE. The catalog's preservation rules apply only to eligible, non-excluded material. The privacy rules in §7Q override catalog preservation for live credentials, non-negotiable secrets, Ness-configured exclusions, redaction, deletion, and mixed-content separation. When excluded material is present, N.H may preserve only the safe permitted remainder and non-reconstructive exclusion metadata; it must never preserve the excluded content merely to satisfy the catalog's no-silent-drop rule.

PRE-INGEST HOLDING AREA. One unified pre-ingest store. One item, one `capture_id`, one stable location, a list of blockers (e.g. `["speaker_unresolved"]`, `["thread_unresolved"]`, or both). Raw payload never rewritten. Material may remain in `held` indefinitely. Held material is invisible to the Meaning Engine unless an explicitly designed inspection mode says otherwise. One blocked item never blocks unrelated ready items. Silent deletion never permitted. Idempotent: repeated processing never creates duplicate roots. Promotion to the root store is atomic. After promotion, the pre-ingest record stays as provenance with the resulting `root_id` recorded.

LIFECYCLE STATES (conceptual): `held` → `ready` → `promoting` → `promoted`; plus `rejected`/`excluded` (intentional, with reason) and `error` (processing failed, material preserved).

CONCEPTUAL RECORD SHAPE includes at minimum: `capture_id`, raw payload or stable reference, capture timestamp, front-door type, source metadata, proposed catalog fields, blocker list, proposal provenance and uncertainty, resolution history, lifecycle state, resulting `root_id` if promoted.

SPEAKER RESOLUTION RULE. `role` must come from source, not be guessed. Raw capture may happen without a known speaker; root ingestion cannot. Live interactive use: ask Ness when the speaker is necessary and cannot be identified. Unattended processing: hold as `speaker_unresolved`. A speaker detector may propose a candidate — that proposal is uncertain and remains a proposal until confirmed by Ness or supported by source evidence. Never silently promoted into the `role` field.

SOURCE TITLE RULE. `source_title` is a grouping key for Engine B's positional context retrieval. Rules: (1) Source provides a real thread identifier → carry it exactly. (2) Source missing but items provably belong together → one unique non-semantic placeholder per capture session: `untitled:paste:<capture-session-id>`, `untitled:voice:<capture-session-id>`. (3) Isolated item → unique singleton placeholder. (4) Grouping genuinely uncertain → live: ask Ness; unattended: hold as `thread_unresolved`. A machine-generated topic or summary must never become `source_title`. Future schema: separate `thread_id` (stable grouping key) from optional human-readable display label. Sealed roots are never rewritten; later clarification goes through an alias/correction layer (design deferred).

FOUR ENRICHMENT CATEGORIES.

**A. Source-carried facts — accepted as catalog facts.** Sender/speaker, source role, original timestamp, thread/conversation identifier, platform name, source title, message ordering, filename, attachment identifier, source media type. Provenance of each fact recorded.

**B. Deterministic mechanical derivations — allowed.** Content length, file size, checksum/hash, image dimensions, audio/video duration, encoding, normalized format, ordering index, normalized timestamp. Rules: preserve the original source value; store derived value separately; record method and version; never replace original with normalized form; derivation failure does not alter or destroy the capture.

**C. Machine-inferred classifications — proposals only.** Detected language, suspected speaker, probable thread membership, probable duplicate, quoted-text detection, possible continuation. Stored only as proposals with: proposed value, producer/model/rule, evidence, confidence, timestamp, confirmation status. Never becomes a settled catalog fact without confirmation by source evidence, Ness, or an explicitly authorized resolution rule.

**D. Semantic interpretation — forbidden in the catalog.** Topic, intent, emotion, motive, psychological state, importance, relevance, meaning, relationship interpretation, truth judgment, summary, inferred life event, what a person "really meant." These belong to the Meaning Engine, reading layer, story layer, or later systems.

BOUNDARY TESTS. "Does this describe what the material physically/source-wise *is*, or does it explain what the material *means*?" And: "Could two reasonable readers disagree because they interpret the content differently?" If yes to the second, it belongs outside the catalog.

The raw captured payload is never rewritten. Enrichment metadata develops around it. Exact schemas, field names, and which derived values enter the future root schema remain undesigned.

---

## 7F. CONTEXT RETRIEVAL  [CONCEPTUALLY DESIGNED, NOT BUILT]

TWO CHANNELS, ALWAYS SEPARATE. Positional context answers: "What was happening immediately before this root in the same thread?" Semantic context answers: "What other stored material may relate to this root?" These are different kinds of evidence. A semantically similar memory may come from a completely different time, person, event, or situation. Similarity is not proof of relevance.

Positional and semantic retrieval are separate channels. Every retrieved item carries retrieval provenance: retrieval type, why it was selected, source root ID, source thread/grouping, timestamp, retrieval score or position where relevant. When both are supplied, the prompt structure must show them in separate sections. The model must not be able to mistake a semantic match for a preceding turn. A conflict between positional and semantic context is surfaced, not silently resolved. Semantic retrieval never overrides or silently repairs positional context.

CHANNEL COMBINATIONS. The engine may receive: positional only, semantic only, both channels, or neither — depending on the explicitly designed reading mode.

FOUR CONCEPTUAL MODE CATEGORIES (not final names or settings): bare (no context), local-context (positional only), associative (semantic only), combined (both channels, still separated).

RETRIEVAL PARAMETERS ARE PER-MODE, NOT UNIVERSAL CONSTANTS. Every reading mode explicitly declares its own: positional-context limit, semantic-result limit, semantic threshold or ranking rule, eligible source scope, time range if any, token/size budget, and fallback behavior when insufficient context is found. Parameter values must be tested empirically against gold sets before defaults are locked. Testing must examine reading quality, whether relevant context was retrieved, whether irrelevant context was introduced, whether semantic matches were mistaken for direct context, reproducibility, latency, cost, and sensitivity to changing the limits.

All retrieval is bounded. No mode may request unlimited results. Hard safety ceilings exist above mode-level settings so a configuration error cannot retrieve unbounded material. Exact ceiling values remain undesigned.

Engine B's n=3 remains the configuration of the built Engine B experiment. It does not establish 3 as the universal future positional limit.

AUDIT TRAIL. Reading record must eventually preserve: reading mode, configured parameters, retrieval system/model/index version, exact roots supplied, scores or positions, exclusions or truncation caused by limits, execution timestamp.

GENUINE NO-CONTEXT HANDLING. When retrieval returns nothing because no relevant context exists — first root in thread, or no semantic results above threshold — these are normal conditions, not failures. Engine proceeds with the target root only. Reading record must state: which channel returned nothing, why, that bare fallback was used, that the reading is context-limited and revisable. The system must not invent, lower thresholds silently, or substitute unrelated memories.

SYSTEM FAILURE SEPARATION. Index error, stale/incomplete index, timeout, unreachable service are system failures, distinct from genuine empty results. System must never claim retrieval succeeded when it failed. Exact fallback behavior for system failures remains undesigned.

Trigger conditions for semantic retrieval, exact retrieval limits, ranking methods, thresholds, and safety ceiling values remain undesigned. The shared vocabulary and configuration contract for these parameters is now established in §7R (Attention and Relevance Control); each retrieval mode must declare its own Tier 1 and Tier 2 relevance mode configuration against that vocabulary when Context Retrieval's relevance design is addressed.

---

## 7G. MEANING ENGINE INTERIOR  [CONCEPTUALLY DESIGNED, NOT BUILT]

ONE READING PER PASS. One pass, one reading record, one target root. Multiple angles require multiple explicit passes. Every pass declares its reading mode, purpose, or angle. Multiple readings may point to the same root; each is separate with its own context inputs, engine version, configuration, and timestamp. A new reading never overwrites an older one. Conflicts between readings stay visible, never silently merged. Later synthesis is a separate layer and does not rewrite existing readings. The engine must not create hidden secondary interpretations outside the reading record.

ENGINE FLOW. Target root + optional positional context + optional semantic context + declared reading mode → mouth proposal → Reading Proposal Acceptance Check → reading record.

★ FIRST-CLASS PRINCIPLE — MODEL CONFIDENCE IS METADATA, NOT AUTHORITY. This principle applies to all present and future models used inside N.H, regardless of model size, architecture, or claimed capability.
1. Model confidence is metadata, not authority.
2. A confident response may still be wrong, unsupported, or invented.
3. Acceptance depends on grounding in the target root, supplied context, declared reading mode, and explicit evidence — not on what the model claims about itself.
4. Unsupported certainty must be rejected or downgraded by the acceptance layer.
5. Honest uncertainty is preferable to confident fabrication.
6. No reading is accepted solely because the mouth model labels itself confident.
7. The acceptance layer must record why a proposal passed or failed — not just the outcome, the reasoning.

READING PROPOSAL ACCEPTANCE CHECK. An explicit acceptance step runs between the mouth's proposal and the reading record. The mouth does not judge its own output alone.

The acceptance check verifies at minimum: required fields present and valid; meaning grounded in the target root or supplied context; no claims invented beyond available evidence; positional and semantic context not confused with each other; uncertainty expressed honestly; response does not contradict its own evidence; declared reading mode was followed.

A response fails acceptance when it: invents facts, overstates certainty, relies on context not supplied, confuses semantic similarity with direct context, violates the reading mode, is malformed or incomplete, or cannot support a meaningful interpretation from available evidence.

ON ACCEPTANCE FAILURE. The proposal is rejected and the specific failure reason is recorded separately. `insufficient_context` is used only when the available root/context cannot support a grounded interpretation. Fabrication, unsupported certainty, positional/semantic channel confusion, reading-mode violation, malformed output, and incomplete output are recorded as distinct proposal-rejection reasons rather than being mislabeled as context insufficiency. Under a future explicitly designed bounded fallback/retry rule, the engine may make a fresh proposal; if it still cannot produce a grounded reading, it writes the honest revisable `insufficient_context` reading required by the S14 engine-failure rule. The rejected proposal may be preserved in an audit log, but it must never silently become the accepted reading. The engine never invents.

Acceptance result, reasons, validator version, and relevant checks should eventually be recorded for reproducibility. Exact criteria, thresholds, retry behavior, and whether validation uses rules, another model, or both remain undesigned.

STORY-LAYER EVIDENCE RULES. The story-layer pass may retrieve both prior roots and prior readings, but they must remain in separate, clearly labeled context channels.

Two separate context channels for story-layer passes: (1) root evidence channel — original source material, higher evidential status; (2) prior reading context channel — previous interpretations, interpretive status only. Roots and readings must never be merged into one undifferentiated evidence block.

Grounding rule: every story telling must be grounded in supporting root IDs. Prior reading IDs may support continuity, comparison, or discovery, but a telling is never accepted solely because earlier readings stated it.

Circular support is forbidden: a reading cannot become true merely because later readings repeat it; derived material cannot endlessly validate other derived material without root support; an unfinished output from the current pass may not be used as its own evidence; only completed prior readings are eligible.

Conflict rule: conflicting readings remain visible and are not silently resolved. The story layer surfaces clash; it does not arbitrate it.

On weak evidence: if root support is insufficient, the telling is omitted or marked `insufficient_context`. Never invented.

Audit trail: every root ID and reading ID supplied to the story-layer pass must be preserved.

Exact retrieval scope, ranking, limits, and firmness criteria remain undesigned.

---

## 7H. REREAD LIFECYCLE  [CONCEPTUALLY DESIGNED, NOT BUILT]

A reread never happens without an explicit recorded reason. Three trigger types are allowed, each bounded.

MANUAL. Ness may request a reread at any time. No further justification required.

CONDITION-BASED. Triggered when materially relevant new information becomes available: new positional context, new root evidence, resolved speaker or thread information, corrected provenance, a newly available required context channel. Time passing alone is not a condition. Any new memory does not automatically trigger rereading everything. Relevance must be established under an explicitly designed rule.

SCHEDULED AUTOMATIC RETRY. Allowed only for temporary system conditions: model/service timeout, unavailable or stale index, interrupted processing, other explicitly retryable technical failures. Not for reinterpretation. Bounded, idempotent, protected against duplicate rereads and endless retry loops.

ON NESS REJECTING A READING. The rejection is recorded. The reading is marked and may become eligible for reread. Rejection does not prove the opposite interpretation is correct.

EVERY REREAD RECORDS. Trigger type, trigger reason, who or what initiated it, new evidence or changed condition, previous reading IDs, new configuration and timestamp.

A reread creates a new reading. It never overwrites, edits, or deletes the earlier reading. A revisable reading may remain unrevisited indefinitely if no trigger occurs.

Exact relevance rules, retry limits, scheduling, and orchestration remain undesigned. The shared vocabulary and configuration contract for condition-based relevance evaluation is now established in §7R (Attention and Relevance Control); reread trigger relevance modes must be declared against that contract when the Reread Lifecycle's relevance design is addressed.

---

## 7I. VIEW LAYER  [CONCEPTUALLY DESIGNED, NOT BUILT]

TWO VIEWS. Simple by default, complete on demand. Ordering is presentation only — it never resolves conflict or grants authority.

CURRENT VIEW (default). In a simple per-root reading list, surfaces the newest usable reading first. Usable = passed acceptance, not marked rejected or `insufficient_context`. This does not mean it is true or final. Conflicts must be surfaced explicitly — for example: "A conflicting reading also exists." Revisable, rejected, and insufficient-context readings remain visible with clear labels. Whenever the interface claims to show the **current best-supported** reading or assembles a broader current picture, §7M's seven-factor ordering governs; recency is only a limited tie-breaker.

HISTORY VIEW (complete record). Every reading in strict chronological order. Ness may switch to it at any time. Always available, never hidden.

STANDING RULES. No reading is deleted, hidden permanently, or overwritten. Different reading modes may be grouped separately when helpful, but the original chronology remains available. Ordering is presentation only. Newest reading shown first does not make it authoritative, correct, or final. Simple by default, complete on demand.

Exact grouping rules, labels, interface layout, and definition of "current usable reading" remain undesigned.

---

## 7J. CONTRADICTION AND CLASH HANDLING  [CONCEPTUALLY DESIGNED, NOT BUILT]

SIX CLASH TYPES.
1. **Direct contradiction** — two readings of the same root produce mutually exclusive meanings.
2. **Interpretive divergence** — same evidence, different conclusions, neither strictly excludes the other.
3. **Temporal change** — inconsistency between readings at different times that may reflect genuine change, not error.
4. **Perspectival difference** — different speakers' or observers' framings of the same event, each accurate within its own perspective.
5. **Evidence insufficiency** — conflict because neither reading had enough context to be reliable.
6. **Context mismatch** — apparent contradiction from different reading modes or retrieval configurations, not a real conflict in the material.

GENUINE CONTRADICTION VS CONTEXTUAL DIFFERENCE. Core test: could both statements be simultaneously true under the same conditions, for the same person, at the same time, in the same context? If yes — contextual difference. If no — genuine contradiction. N.H records the distinction, never resolves it.

CLASH RECORD SHAPE (conceptual). Stable identifier, clash type, pointers to exact readings and roots involved, description of what specifically conflicts, retrieval configurations and reading modes of conflicting readings, detection mode, confidence of clash detection, lifecycle state, Ness response status, timestamp. Every clash record points to the exact supporting roots and readings. Original roots and readings remain unchanged.

TWO DETECTION MODES, SAME RECORD TYPE.

Triggered detection: runs when a new reading is written. Compares against readings of the same root, readings in the same thread, and other explicitly related readings.

Periodic or on-demand detection: scans wider scope — across roots, threads, people, time periods, story layers. Catches slow-developing and cross-thread contradictions.

Both modes produce the same conceptual clash-record type. Every clash record states its detection mode. The same clash must not produce two independent records — later detection appends a new detection-history event linked to the existing clash. Wider scans may append evidence or propose a refined classification through linked events, but they do not mutate the original clash, rewrite original readings, or spawn duplicate clashes. Detection mode does not affect authority. Neither mode may resolve, rank, or select a winner. Periodic scans are bounded and configurable.

NESS'S RESPONSE AS SEPARATE EVENT. Every response has its own stable event ID and points to the clash ID. It does not live inside the clash record. Every response event records: response type, Ness's exact statement or selection, timestamp, evidence or explanation supplied, any requested downstream action.

Response types include: one reading accepted over another, both valid in different contexts, genuine change over time, insufficient evidence to judge, detection artifact, deferred judgment, request for reread, or another explicitly defined type.

Ness may respond multiple times. Later responses do not erase earlier ones. Full response history always preserved. Current view may show the latest Ness response; full response history available on demand.

Downstream actions are separate linked records. A response event and the action it triggers are distinct records that point to each other. Ness choosing one reading does not delete the other — his judgment is recorded and may affect the computed view or presentation. It does not alter the underlying readings, roots, or clash record.

A clash is not automatically an error. N.H never silently resolves it. Exact schemas, detection methods, schedules, deduplication logic, and downstream effects remain undesigned.

---

## 7K. STORY LAYER  [CONCEPTUALLY DESIGNED, NOT BUILT]

RESPONSIBILITIES. Receiving tellings produced by engine passes and recording them without alteration. Organizing tellings by whose perspective they reflect, what theme they belong to, and when they were produced. Surfacing how a narrative thread has developed, shifted, or fractured across time. Preserving clash between tellings without resolving it. Making it possible to ask: what has been said about this person, theme, or period — and from whose perspective, with what firmness, supported by what roots. Distinguishing temporal change from contradiction. Keeping each person's story separate from every other person's.

MUST NEVER. Merge conflicting tellings into one synthesized narrative. Promote a repeated telling into established fact merely because it appears often. Assign a single authoritative story to a person, relationship, or event. Invent connective tissue between tellings that the roots do not support. Treat a gap in tellings as evidence of absence. Flatten temporal change into a single stable description. Allow one person's perspective to silently overwrite another's. Resolve whose telling is correct — that is Ness's judgment, off-board.

TELLING VS ONGOING STORY. A telling is one interpretation, produced in one engine pass, about one root, from one perspective, at one moment — local, bounded, specific. An ongoing story is the collection of tellings across time — with agreements, shifts, contradictions, silences — organized so that patterns can be seen without being hardened into conclusions. The story layer can surface the sequence; it cannot conclude from it.

CONNECTIONS ACROSS TIME. Tellings connect through explicit shared attributes: same `whose`, same theme, same thread or source, overlapping time period, or shared root IDs. These are navigational links, not logical merges. Always labeled with what they are based on, always pointing back to supporting roots and readings.

STRUCTURED PERSPECTIVE MODEL. Three minimum fields per telling:
- `root_speaker` — who produced the source root.
- `subject` — who or what the telling is about.
- `perspective_owner` — whose viewpoint, belief, feeling, or framing the telling claims to represent.
Optional: `attribution_path` — used when perspectives are nested (e.g. `friend → quoted by father → reported by Ness`). Populated only when the root supports the chain. Never invented.

These roles may refer to the same person or different people. The Story Layer never assumes the root speaker is automatically the subject or perspective owner. Evidence relationship must be recorded for every telling: direct self-report, direct quotation, reported speech, observation, or engine inference. Reported speech is not direct access to the reported person's internal state. The engine's interpretive lens stays separate from the human perspective represented in the telling. Unknown attribution stays explicitly unresolved. Existing flat `whose` field may remain for v1 compatibility; future schema should use the structured perspective fields.

OBJECT-IDENTITY SEAM — EXPLICITLY UNRESOLVED. In the built v1 reading schema, tellings are embedded entries inside the reading record's `story_layer` list; no separate first-class telling record is built. S17 treats a telling conceptually as something other components may link to, but it did not choose its future storage identity. Before Story Layer, Person-Box, clash, or deletion code relies on telling-level links, one identity method must be designed explicitly: either a separate immutable telling record or a stable composite reference within its immutable parent reading. This master does not choose between those options, and no implementation may assume standalone telling IDs until that seam is settled.

FIRMNESS RULE. Firmness and model confidence are separate dimensions. `firmness` = how strongly the perspective owner appears to hold the stance. `confidence` = how well-grounded the engine believes its reading to be. These are independent.

Firmness may be inferred from observable signals: explicit certainty words, hedging, repetition, emphasis, consistency within the root, direct statements of commitment or doubt. Every firmness value records its evidence basis. Firmness is always provisional and revisable. Direct self-report of certainty is stronger evidence than tone, wording style, or repetition alone. Reported speech or uncertain attribution lowers evidential strength. N.H must never present firmness as direct access to a person's internal state. Conflicting signals produce mixed firmness, uncertain firmness, or omission — never a forced resolution. If the root does not support a firmness judgment, the field is omitted. Exact scale, labels, thresholds, and scoring method remain undesigned.

HYBRID THEME SYSTEM. Engine proposes freely. Only Ness confirms. Confirmed themes are navigation categories, never facts.

Engine-proposed themes start as `proposed`, never as settled categories. May be generated from a single telling or patterns across multiple tellings. Every proposed theme records: supporting root IDs, supporting telling/reading IDs, who or what proposed it, why those items appear connected, timestamp, uncertainty.

Ness may: confirm, rename, merge, split, reject, or leave a proposed theme unresolved indefinitely. Unresolved proposed themes do not become confirmed by aging or repetition.

A telling may belong to no theme, one theme, or multiple themes. Membership is not exclusive. Circular support is forbidden — pattern-derived themes must retain root support. Repetition does not confirm. A theme cannot validate itself by being frequently proposed.

Proposed themes must not silently shape future readings. If a confirmed or proposed theme is used to retrieve context for a future engine pass, that influence must appear in the retrieval audit trail. Future readings may challenge, omit, or contradict an existing confirmed theme.

Ness-controlled vocabulary is open and extensible. Theme aliases may connect different labels across time without rewriting older tellings. Exact theme schema, similarity grouping, confirmation process, and retrieval influence remain undesigned.

---

## 7L. PERSON-BOXES  [CONCEPTUALLY DESIGNED, NOT BUILT]

RESPONSIBILITIES. Maintaining a stable identity anchor for a person. Linking roots where this person appears, is mentioned, is quoted, or is the subject of a telling. Linking readings and tellings that involve this person in any perspective role. Linking clashes that involve this person. Linking Ness's responses where relevant. Recording how each link was established and how certain it is. Tracking proposed identity connections without silently merging them. Surfacing what has changed over time about how this person appears across the store.

MUST NEVER. Synthesize linked material into a summary description or personality profile. Promote a frequently appearing interpretation into a settled fact about the person. Treat a report about someone as equivalent to that person's own perspective. Merge two uncertain identity references without explicit resolution. Treat absence of information as evidence of anything. Resolve contradictions between tellings. Allow one perspective owner's framing to silently become the authoritative view of the subject. Invent connections not explicitly supported. Become a diagnosis, personality model, fixed character description, or closed identity. Claim to represent what a person is like — only what N.H has observed or been told, from whom, with what certainty, at what time.

LINKABLE OBJECT TYPES. Roots, readings, story tellings, themes (with confirmation status), clash records, Ness response events, other Person-Boxes (where identity connection proposed or confirmed), and **metadata-only** references to pre-ingest records where the person appears. Held pre-ingest raw content remains invisible to Person-Box semantic analysis unless an explicitly authorized inspection mode is later designed; only safe source-carried metadata, lifecycle state, and blocker information may be linked. Every link records: what it connects, why, who or what established the connection, certainty, and timestamp. Links are never copies — the original object stays where it is.

UNCERTAIN IDENTITY. Uncertain identity is the normal state. A reference anchor records: the label or name used, where it appeared, when, what evidence connects it to a specific person, and current certainty level. Multiple anchors may exist for what might be the same person. They remain separate until a resolution rule — Ness confirmation, strong source evidence, or another explicitly authorized rule — merges them.

PROPOSAL-BASED CREATION. N.H may detect a new person reference and create a proposed identity anchor, but it must not silently create a confirmed Person-Box or decide that two references are the same person.

Every Person-Box has a stable system-generated ID. Human-readable names, labels, and roles attach separately and may change. A new unrecognized reference may generate a proposed anchor when encountered through a front door, root, reading, story telling, or other authorized source. A proposed anchor is not a confirmed Person-Box.

Before proposing a new anchor, N.H must search: confirmed Person-Boxes, unresolved identity anchors, aliases, and previous merge proposals. Similar names or labels alone are not sufficient to merge. Possible duplicates produce a separate merge proposal, never a silent merge.

Ness may: confirm, reject, rename, keep unresolved, link to an existing Person-Box, or propose a merge. Strong source evidence may confirm identity only under an explicitly authorized resolution rule.

Confirmed merge: links identity anchors under one stable identity view. Does not rewrite roots, readings, tellings, or historical links. If a merge is later found wrong, correction is recorded through new events or links. History is never rewritten.

Unresolved references may remain separate indefinitely. Exact matching rules, evidence thresholds, confirmation workflow, and merge mechanics remain undesigned.

**SETTLED FACT — NESS HAS A PERSON-BOX (June 25 2026).** Ness has a Person-Box. How Ness's Person-Box is created, anchored, and maintained is not yet designed and must be decided separately.

DEFAULT VIEW. Seven separate sections: roots, readings, story tellings, clashes, Ness response events, themes, unresolved identity anchors and merge proposals. Every section states what it contains and its evidential status. These are never visually flattened into equivalent claims. Section order is navigation only — not authority, reliability, importance, or truth. Frequency and recency do not silently determine reliability.

Ness may filter or reorganize by: time, perspective role, theme, source/thread, lifecycle or confirmation status. Full chronological view always available. Conflicts, unresolved identity questions, and uncertain links surfaced clearly. Simple by default, complete on demand.

Exact layout, section order, filters, and labels remain undesigned.

---

## 7M. COMPUTED VIEW  [CONCEPTUALLY DESIGNED, NOT BUILT]

WHAT IT IS. The present-facing surface of N.H. Its job is to take all accumulated material and produce a navigable, useful picture of what N.H currently has reason to show, without altering any underlying objects or pretending that one interpretation has won.

RESPONSIBILITIES. Assembling the most useful current picture using explicit derivation rules. Surfacing the current best-supported reading for a root, story thread, person, or theme while preserving access to alternatives and history. Reflecting Ness's explicit responses without treating them as rewrites of history. Distinguishing evidence, engine interpretation, Ness's explicit judgment, and unresolved material. Updating automatically when triggered. Preserving a record of what the view showed at previous points in time.

MUST NEVER. Rewrite, alter, merge, or delete any root, reading, telling, clash, or response event. Silently select one reading as authoritative. Treat most recent or most frequent interpretation as more reliable without explicit justification. Present engine inference as settled fact. Present Ness's response as a rewrite of history. Suppress conflicts. Store new interpretations. Decide what is true.

OBJECT TYPES USED. Roots, readings, tellings, clashes, Ness response events, Person-Box links, themes, and **metadata-only** pre-ingest references. Held pre-ingest raw content must not influence Computed View ranking, interpretation, or output unless an explicitly authorized inspection mode is later designed; only safe source-carried metadata, lifecycle state, and blocker information may be surfaced. All objects are linked, never copied.

SEVEN-FACTOR PRIORITY ORDER (explicit, no hidden truth score):
1. Ness's explicit current judgment, when relevant.
2. Strength and directness of supporting root evidence.
3. Acceptance status and grounding quality of readings.
4. Relevance to the current question or view purpose.
5. Context quality and retrieval provenance.
6. Active clashes, unresolved uncertainty, and contrary evidence — surfaced beside the item, not suppressed.
7. Recency as a limited tie-breaker only. Never as authority.

Every surfaced item must state why it was prioritized. No single hidden score may collapse evidence, interpretation, judgment, and uncertainty into one number. Direct root support outranks repetition, frequency, or model confidence. A highly supported item with an active clash must display the clash beside it. The view must be able to say "no clear current view" when support is too conflicted or weak.

DECLARED ORDERING PROFILES. Different view purposes may use different profiles — current situation, person-focused, project-focused, historical review, or others. Each profile discloses its ordering rules. Alternatives and full provenance remain accessible from any profile.

UPDATE TIMING. Triggered updates, not continuous recomputation. Three update triggers: (1) Ness opens the view; (2) Ness manually requests a refresh; (3) a materially relevant event occurs — new accepted reading, new or changed active clash, Ness response event, confirmed theme or identity resolution, or another event explicitly defined as relevant to that view profile. Unrelated new material does not force every Computed View to recalculate.

Every completed update creates a new immutable snapshot. Previous snapshots remain accessible and never overwritten. Every snapshot records: update trigger, view profile, source objects used, derivation-rule version, timestamp, what changed from the previous snapshot, and why it changed. Normal interface shows the newest valid snapshot. If an update fails, the last valid snapshot remains visible, clearly marked as possibly stale. Failure is never silently treated as a successful refresh. The view may state that nothing materially changed — a null update is a valid outcome.

Exact relevance rules, significance thresholds, refresh scheduling, and snapshot schema remain undesigned. Factor 4 ("relevance to the current question or view purpose") in the seven-factor ordering now has a defined form through §7R (Attention and Relevance Control); Computed View must declare its own Tier 1 and Tier 2 relevance mode configuration against the §7R contract when its relevance design is addressed.

---

## 7N. ACTION SURFACING  [CONCEPTUALLY DESIGNED, NOT BUILT]

PERMISSION-CONTROLLED HYBRID. N.H surfaces possible actions when asked or when an explicitly authorized relevance rule applies. Never instructions. Never decisions. Ness remains sole decision-maker.

TWO SURFACING MODES. (1) On explicit request from Ness — always permitted. (2) Proactive — permitted only when an explicitly authorized relevance rule says the possibility is useful enough to show. Controllable by Ness's settings. May be disabled entirely.

Every surfaced possibility is labeled as derived, not instructed. Required language: "one possible option," "this may be reachable," "you could consider." Prohibited language: "you should," "you need to," "you must."

Every possibility records: the state, open loop, value, constraint, or evidence it was derived from; why it may be reachable now; important assumptions; uncertainty; possible limitations or risks.

Ness may: accept, reject, modify, postpone, ignore, or ask for alternatives. All responses are valid. Ignoring or rejecting a suggestion is never treated as failure, resistance, or evidence against Ness. No repeated surfacing of the same suggestion without a new request, materially changed evidence, or another explicitly authorized trigger.

Weak, conflicted, stale, or insufficient evidence: N.H either withholds the suggestion or labels it clearly as uncertain. Higher-impact actions require stronger permission and review rules than small reversible actions. The four risk levels are defined in §7P; what remains undesigned is the mapping of specific action categories to those levels, category-specific evidence and permission thresholds, and interface wording.

A surfaced possibility is not an action record until Ness chooses or performs something. The suggestion and any later real action remain separate linked objects.

NESS-RESPONSE STATES FOR SURFACED POSSIBILITIES (before or instead of execution):

- **Accepted and acted on** — Ness confirms and performs or authorizes the action. A new action record is created. The possibility and action record are linked but remain separate objects.
- **Rejected** — recorded as a rejection event pointing to the possibility. Not treated as failure, resistance, or evidence against Ness. The possibility is not resurfaced without a new trigger.
- **Modified** — Ness changes the scope, target, or form of the suggestion before acting. The modification is recorded. The modified version becomes the basis for the action record, not the original suggestion.
- **Postponed** — recorded with a reason if given. The possibility remains eligible for resurfacing only when a new trigger or request occurs. Time alone does not resurface it.
- **Ignored** — no response event required. The possibility is not resurfaced without a new trigger.
- **Alternative requested** — Ness asks for different options. A new surfacing pass is initiated. Prior suggestions remain in record but are not repeated in the new pass.

Exact relevance triggers, mapping of specific action categories to the four risk levels, category-specific evidence and permission thresholds, and interface wording remain undesigned. The "explicitly authorized relevance rule" for proactive surfacing now has a defined form through §7R (Attention and Relevance Control); Action Surfacing must declare its own Tier 1 and Tier 2 relevance mode configuration against the §7R contract when its relevance design is addressed.

---

## 7O. ACTION-RESULT RETURN PATH  [CONCEPTUALLY DESIGNED, NOT BUILT]

TWO RESULT TYPES, KEPT SEPARATE. Neither grants direct system access to reality.

EXPLICIT REPORTED RESULT. Ness directly reports what happened through a normal front door. Enters catalog and ingestion as normal — becomes a root only after standard checks. Labeled as Ness's report of the result. Not direct system observation of reality.

DETECTED POSSIBLE RESULT. N.H notices incoming material that may relate to an earlier action. Creates a proposal linking new material to the action. Never silently declares the material is the action's result.

Every possible-result proposal records: action ID, new root or capture ID, why they may be connected, timing, uncertainty, alternative explanations, who or what detected the connection.

Ness may: confirm, reject, modify, or leave the proposed connection unresolved indefinitely.

CAUSATION RULES. Timing alone does not prove causation. Similarity alone does not prove an observed event resulted from the action. Confirmation of a result connection does not automatically confirm why it happened.

THREE SEPARATE LINKED OBJECTS. Action record, result root, connection between them. Never merged.

N.H must distinguish: (1) the observed or reported event; (2) the claim that it resulted from the action; (3) interpretations of what that result means.

A confirmed result connection may trigger: reread, state update, open-loop update, or another explicitly designed process. Automatic detection may be disabled or restricted by Ness.

SIX RESULT STATES:

- **Success** — the action may have produced the expected or intended effect. Success may be recorded as confirmed when Ness confirms it. Without Ness's confirmation, N.H may record that the observed outcome appears consistent with the intended effect, but this remains a revisable interpretation and does not establish causation. The observed event, the inferred relationship to the action, and Ness's confirmation or judgment remain separately represented.
- **Partial success** — may be recorded as confirmed when Ness confirms that some but not all intended effects occurred. Without Ness's confirmation, N.H may record that the observed outcome appears consistent with partial success, but this remains a revisable interpretation and does not establish causation. The record describes what appears achieved and what appears unmet while keeping the observed outcome, the proposed relationship to the action, and Ness's judgment separately represented. Does not automatically trigger a retry.
- **Failure** — may be recorded as confirmed when Ness judges that the intended effect did not occur or that the result was negative. Without Ness's confirmation, N.H may record that the observed outcome appears consistent with failure, but this remains a revisable interpretation and does not establish causation. The observed outcome, the proposed relationship to the action, and Ness's judgment remain separately represented. Does not automatically trigger a retry or a new surfaced suggestion. Ness decides what to do next.
- **Cancellation** — the action was authorized but stopped before completion, either by Ness, by a pre-authorized emergency stop, or by a system condition. The cancellation is recorded with its trigger, reason, and the state of the action at the point of cancellation. Partially completed effects are recorded separately from intended effects.
- **No result or unknown result** — the action was taken but no observable result has arrived or can be confirmed. Recorded as result-unknown. Any open loop or state node remains active and marked with uncertainty. The system does not assume success or failure. Time passing alone does not resolve this.
- **Incorrect or disputed result linkage** — a proposed connection between a result and an action is found to be wrong, contested by Ness, or contradicted by later evidence. The incorrect linkage is recorded as a rejected connection event. The action record and result root remain as separate objects. A corrected linkage may be proposed. The original action record is never rewritten to remove the disputed connection — the dispute is recorded alongside it.

Exact detection rules, confirmation workflow, classification criteria and subcategories within the six result states, and downstream triggers remain undesigned.

---

## 7P. PERMISSION AND AUTHORITY BOUNDARIES  [CONCEPTUALLY DESIGNED, NOT BUILT]

WHAT IT IS. The formal boundary between N.H as a helper and N.H as an actor in the world. Defines what N.H may do on its own, what it must prepare and show before doing, what it must ask Ness before doing, and what it may never do regardless of any instruction.

MUST NEVER ALLOW. N.H acting on the world without recorded authorization. Silence, absence, or non-response interpreted as consent to act. A permission granted for one action being silently extended to a different action. Past permission automatically remaining valid for future similar actions. N.H proceeding when its authority level is unclear. Preview being skipped for actions requiring approval. An irreversible action taken on the basis of reversible-action authorization. Cascading permissions. N.H deciding what counts as a successful result of an action it took.

THREE ACTION STATES WITH DISTINCT AUTHORITY REQUIREMENTS.

**Suggesting** — N.H surfaces a possibility for Ness to consider. No external effect, external write, or execution occurs. Authorized Level 1 internal read-only retrieval may occur to derive the possibility, but no message is sent, no external account or system is changed, and no executable action is staged. Lowest authority level; always permitted within action-surfacing rules.

**Preparing** — N.H assembles something ready to act but not yet acted. A draft exists but has not been sent. A change is staged but not saved. The prepared object is real and inspectable but no external effect has occurred. Ness reviews before anything is committed. Requires higher authority than suggesting. Must be shown to Ness before execution.

**Executing** — N.H takes an action with real-world effect. Something irreversible may have occurred. Requires the highest authority level, explicit prior approval for the specific action, and a complete record of what was done. The boundary between preparing and executing is: has anything outside N.H changed? If yes, execution has occurred.

FOUR RISK LEVELS.

**Level 1 — Internal read-only.** N.H accesses its own stores, indexes, and records. No external effect. No change to any object. Autonomous within normal operating parameters.

**Level 2 — Internal write.** N.H writes a new reading, appends a new state node, state-version, or currentness event, creates a clash record, or produces another derived object inside its own stores. Existing state nodes and other historical records are not modified in place. Append-only operations at this level are lower risk than modifying existing objects. Autonomous within established schema and validation rules for normal append operations; flagged for any exceptional operation that would alter an existing record.

**Level 3 — Prepared external action.** N.H drafts, stages, or assembles something intended to have external effect. The prepared object is shown to Ness before anything is committed. Ness must explicitly approve before execution. Silence is not approval.

**Level 4 — Executed external action.** N.H takes an action with real-world effect. Requires explicit prior approval for the specific action, a pre-execution preview, and a post-execution record. Irreversible actions require additional confirmation. Actions in heightened-risk categories require their own special boundary rules regardless of whether they appear small or reversible.

TWO AUTHORITY LAYERS.

**Layer 1 — Standing permissions.** General abilities Ness enables or disables. May authorize: Level 1 internal read-only, normal validated Level 2 append-only internal actions, Level 3 preparation within clearly defined boundaries. Cannot silently authorize broad categories of external execution.

**Layer 2 — Moment-level approval.** Permission for one specific action at one specific moment. Required for Level 4 external execution after Ness sees the exact action preview. Preparing something does not authorize executing it.

RECURRING EXECUTION AUTHORIZATION. Ness may create a narrowly scoped recurring authorization, but it must explicitly define: exact action type, destination or recipient, frequency or trigger, content or value limits, permitted tools, start and expiry conditions, audit and notification requirements, and how it can be paused or revoked. It is its own recorded authority object — not inferred from general settings or past approvals. Actions outside its exact scope require new approval.

ABSOLUTE BOUNDARY — ALWAYS REQUIRES SPECIFIC PER-INSTANCE CONFIRMATION REGARDLESS OF STANDING PERMISSIONS. Medical, legal, financial, privacy-sensitive, relationship-affecting, destructive, or irreversible actions.

STOP CONDITIONS. Changed conditions, ambiguity, expired permission, or unexpected output require N.H to stop and seek reconfirmation before proceeding. Silence is never approval. In any layer, at any level.

AUTHORITY VIOLATION AND CORRECTION RULE.

Stop-and-surface is the default. On detecting a violation or unexpected result, N.H must immediately: stop all related autonomous action; prevent any further steps in the same action chain; record the full event (what was intended, what actually happened, the authority N.H believed it had, where the boundary was crossed, what unexpected result occurred, what is known/unknown/still changing, which tools and external systems were involved); surface the event clearly to Ness without minimizing, hiding, or reframing it; present possible corrective actions separately as proposals.

Ness's approval required before: reversal, compensation, follow-up communication, deletion, restoration, or any other real-world corrective action.

Corrective action is a new action with its own risk level, preview, permission requirement, execution record, and possible consequences. It is never automatically authorized by the fact that it is corrective.

N.H must never assume that reversal restores the original state completely. N.H must never mark the incident resolved merely because a reversal attempt succeeded technically.

FIVE SEPARATE LINKED OBJECTS. Original action, violation record, corrective proposal, approved correction, observed result. Never merged.

NARROW PRE-AUTHORIZED EMERGENCY STOP EXCEPTION. Permitted only when all five conditions are met simultaneously: (1) the original action is still actively in progress; (2) stopping prevents additional effects rather than undoing completed effects; (3) the stop mechanism is mechanically bounded and previously authorized; (4) stopping cannot reasonably create a larger consequence than continuing; (5) the emergency stop and its authority basis are immediately recorded and surfaced to Ness.

This exception explicitly does not permit: recalling or deleting a completed message, restoring or modifying external data, sending an apology or explanation, making a compensating payment, contacting another person, or any other completed-world reversal without Ness's approval.

Exact permission categories, authorization object schema, and interface remain undesigned.

---

## 7Q. PRIVACY, DELETION, AND SENSITIVE-DATA HANDLING  [PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT]

WHAT IT GOVERNS. What N.H may capture, how it classifies and protects sensitive material, who and what may access it under what conditions, what appears in views and chat, and what happens to material when Ness removes, restricts, or deletes it. Operates at every stage: before capture, during storage, during retrieval and display, and during deletion.

MUST NEVER ALLOW. Capturing material that was explicitly excluded at the front door. Storing credentials or secrets in plain recoverable form anywhere. Surfacing sensitive material merely because it is relevant. Retaining deleted material through any indirect path. Allowing derived objects to preserve the content of deleted roots after deletion is confirmed. Treating a deletion marker as equivalent to actual deletion. Displaying another person's sensitive information without an explicitly designed rule authorizing it. Permission to store being silently extended to permission to analyze, simulate, display, or share. Partial deletion claimed as complete. N.H confirming deletion when it cannot verify that deletion was carried out in all relevant locations.

FIVE OPERATIONS — DISTINCT, NOT INTERCHANGEABLE.

**Exclusion** — material never enters N.H at all. Filtered at the front door before capture. Cleanest boundary because there is nothing to manage afterward.

**Hiding** — material exists in the store but is not displayed in normal views or surfaced in retrieval. A presentation rule, not a data operation. Reversible without data recovery.

**Restriction** — material exists and may be physically present, but access is limited by explicit rules. More granular than hiding, more targeted than deletion.

**Redaction** — specific content within a root or derived object is removed or obscured while the containing record remains. The sensitive portion is removed and replaced with a tombstone or placeholder. Must propagate to derived objects that contained the redacted content.

**Deletion** — the root and all material derived from it are removed from every location. A tombstone record may remain to preserve that something was deleted, when, and by what authority — without preserving the deleted content. Deletion is the strongest operation and the hardest to verify as complete.

FOUR SENSITIVITY LEVELS.

**Level 1 — General personal.** Everyday conversation, preferences, projects, general life events. Standard N.H privacy rules apply.

**Level 2 — Sensitive personal.** Health information, financial details, relationship difficulties, emotional material, and things Ness has explicitly marked as private. For Ness's authenticated private use, this material is eligible by default unless Ness explicitly restricted or hid it, it was excluded/redacted/deleted, an unresolved deletion case applies, it contains non-negotiably excluded secrets, or another explicit compartment rule applies. External exposure, shared screens, exports, tool use, notifications, and secondary uses require explicit authorization under the two-stage access-control rules below.

**Level 3 — Third-party and relationship data.** Information about other people. Requires separate rules from Ness's own data because other people did not consent to being in N.H.

**Level 4 — Credentials, secrets, and high-harm material.** Authentication material, passwords, keys, financial credentials. Must never enter normal stores. If encountered at capture, must be excluded or immediately isolated.

DELETION AS BLOCKING, VERIFICATION-BASED OPERATION. N.H may confirm complete deletion only when every known location has been removed or verified clean.

A deletion request creates a deletion case with a complete dependency and location search. N.H must identify and check: the original root, direct readings, story tellings, state nodes, clash records, Computed View snapshots, Person-Box links, indexes, embeddings, caches, temporary processing files, exports, backups, model-context records, and any other known derivative or storage location. Indirect traces must also be searched: quotations, paraphrases, summaries, semantic representations, inferred states grounded partly in the root, copied text without a preserved source link.

Every identified derivative must be deleted, redacted, rebuilt without the deleted source, or explicitly marked unresolved if safe removal cannot yet be verified. Multi-root derived objects may be recomputed without the deleted root only if the deleted content is no longer recoverable from them, their meaning is re-evaluated without that evidence, and their provenance records that they were rebuilt. Embeddings and indexes derived from deleted content must be removed and rebuilt where necessary. Backups follow an explicit deletion or expiry process.

FIVE DELETION OUTCOMES.
- `verified_complete` — every known location and derivative removed or safely rebuilt and verified. The only outcome that may be described as complete deletion.
- `completed_with_declared_limits` — removed from all controllable locations; one or more locations cannot be fully verified.
- `incomplete` — one or more identified traces remain.
- `blocked` — deletion cannot safely proceed yet.
- `failed` — an attempted deletion operation failed.

For every outcome other than `verified_complete`, Ness must be told plainly: what was removed, what remains, what could not be checked, why, whether the remaining trace is accessible or usable, and what further action may be possible. N.H must never confirm deletion merely because the root record is gone. N.H must never hide uncertainty behind the phrase "best effort."

A content-free tombstone may remain containing only: deleted object identifier, deletion time, deletion authority, deletion outcome, verification record. No deleted content, no reconstructive metadata.

While a deletion case remains unresolved: affected material must be immediately prevented from retrieval, display, analysis, simulation, or use in new derivations.

CAPTURE EXCLUSION — TWO-LAYER SYSTEM.

**Layer A — Non-negotiable core.** Narrow by design. Covers material that could directly grant access or cause immediate serious harm if stored: passwords, private cryptographic keys, authentication tokens, recovery codes, one-time security codes, payment-card security codes, and equivalent live access credentials. Must never enter root stores, readings, indexes, embeddings, caches, logs, model context retained by N.H, or normal backups. Cannot be disabled by Ness for normal N.H memory stores. A dedicated secrets vault, if ever built, is a separate system with separate authority, encryption, access, and deletion rules.

**Layer B — Ness-configured exclusions.** Rules Ness controls and can extend, narrow, pause, or remove. May be based on: content category, person, source, date range, front door, project, sensitivity, or intended use. May specify that material should be fully excluded, held for review, entered only after confirmation, entered with specified parts redacted, or entered under immediate restriction. Sensitive but context-dependent material — medical details, childhood memories, third-party information, relationship material, emotional disclosures — must not be placed in the non-negotiable core merely because it is sensitive. These require explicit handling rules but are not automatically excluded in every context.

Mixed-content capture: when one input contains both permitted and excluded material, N.H must isolate and remove the excluded portion, preserve the permitted portion when safe, record that exclusion occurred without recording the excluded content, and tell Ness what category of material was removed. If safe separation is not possible, the entire capture is held before ingestion and Ness is asked what to do. Ambiguous suspected secrets enter a protected pre-ingest hold, not normal memory, until classified. Exclusion happens as early as technically possible at every front door. Exclusion event records may retain only non-reconstructive metadata: time, front door, exclusion category, rule used, outcome. Never the excluded content itself.

THIRD-PARTY DATA RULES.

Universal minimum baseline — applies to every person other than Ness without exception: preserves source and speaker of third-party material; distinguishes the person's actual words or actions from Ness's interpretation and N.H's interpretation; does not present inferred feelings, intentions, diagnoses, motives, or private states as facts; does not share third-party material externally without Ness's specific authorization; does not use third-party material merely because it is relevant; does not silently expand one piece of information into a fixed profile of the person.

Context-sensitive rules above the baseline may vary based on: relationship to Ness, amount and frequency of data, sensitivity, source and front door, whether the person spoke directly or was described by someone else, whether content was private/public/forwarded/recorded/inferred, age or vulnerability, and intended use. Relationship closeness does not reduce protection automatically. A close family member appearing frequently may require stronger safeguards because more material exists.

Ness may configure person-specific or group-specific rules covering permitted storage, retrieval, display, analysis, simulation, retention, redaction, restriction, or exclusion. Configuration may make protections stricter. It may not remove the universal baseline.

Four separate operations with increasingly stronger privacy requirements: (1) understanding Ness's experience of another person; (2) recording what that person actually said or did; (3) interpreting what the person may have meant; (4) constructing a model of the person. N.H may normally perform the first. Each subsequent operation requires stronger authorization.

Third-party simulations must never be presented as the real person. Always labeled as bounded hypothetical models derived from limited material, with uncertainty and missing information visible. Minors and highly vulnerable people receive stronger default restriction. Large-volume imported third-party data does not become fully usable merely because it was imported. Public availability does not automatically authorize unrestricted storage, combination, profiling, or simulation.

TWO-STAGE OUTPUT ACCESS CONTROL.

★ CENTRAL RULE. Private access for Ness is open by default unless Ness explicitly restricts it. External exposure and secondary uses are restricted by default.

★ N.H may use material when the current purpose is authorized by Ness. It blocks material from unauthorized uses, not from Ness's own understanding by default.

**Layer 1 — Pre-retrieval eligibility control.** Before material becomes a retrieval candidate, N.H checks whether it is eligible for the current operation and purpose. For Ness's authenticated private use, material is eligible by default. N.H does not remove material from Ness's private self-understanding merely because it is sensitive, emotional, medical, traumatic, sexual, relationship-related, controversial, or uncomfortable. Third-party involvement does not automatically block Ness from understanding his own experiences. "Sensitive" alone is never a sufficient reason to withhold information from Ness. Material is blocked from Ness's private use only when: Ness explicitly restricted or hid it; it was excluded, redacted, or deleted; a deletion case remains unresolved; it contains live credentials or non-negotiably excluded secrets; a specific compartment rule applies; or another explicit rule chosen by Ness applies. For other purposes — external sharing, tool use, exports, secondary analysis, notifications, shared screens — eligibility is restricted by default and requires explicit authorization. Ineligible material must not be ranked, semantically compared, selected, passed to the mouth, used for simulation, or allowed to influence the response indirectly. Privacy filtering happens before semantic ranking so restricted material cannot influence selection even indirectly.

**Layer 2 — Pre-output privacy review.** After authorized material is retrieved and a response, view, suggestion, or derived output is formed, N.H reviews the final result before showing it. The output review is not a general content-safety or emotional-sanitization filter. It checks specifically for: accidental exposure outside the authorized private context; deleted or restricted content appearing in output; live secrets or non-negotiably excluded material; unauthorized secondary uses; unintended third-party profiling beyond the current authorized purpose; external sharing, notifications, tool outputs, or exports carrying private material; disclosure through shared screens or other unintended channels; several permitted pieces combining into a disclosure that exceeds the authorized purpose; generated language revealing more than the authorized sources themselves support. N.H must not soften, omit, or replace truthful relevant material merely because it may be upsetting to Ness.

MODEL-PROVIDER LIMITATIONS ARE RECORDED SEPARATELY. Any refusal or limitation from the mouth model — such as a Claude refusal — is recorded as a mouth limitation. It is never interpreted as an N.H privacy rule, a Ness restriction, or evidence that the underlying material is forbidden or false. The material remains in the store under its existing rules. The limitation is attributed to the borrowed mouth, not to N.H's privacy system.

When permissions are ambiguous, outdated, unavailable, or conflicting for a non-private-Ness purpose — access defaults to withheld.

On output failure: withhold affected content for the unauthorized purpose, produce a safer version when possible, state plainly that material was withheld and why. Components receive only the minimum material needed for their authorized task. A component must not receive sensitive content merely so it can later decide not to display it.

Privacy checks apply to: chat, Computed View, Story Layer, Person-Boxes, Living State Web, memory browsing, search results, simulations, proactive suggestions, notifications, exports, tool use, and external sharing.

Every privacy decision records: operation requested, purpose, material considered, applicable privacy rule, authorization basis, eligibility decision, output-review result, and any withholding or transformation performed.

Remaining undesigned: exact eligibility rules, purpose categories, privacy-policy evaluation order, safe-transformation rules, interface behavior, core exclusion detection methods, mixed-content separation process, backup deletion/expiry mechanics, derivative-discovery methods, cryptographic erasure mechanisms, verification procedures, person-specific control interface, minor-data specific rules, volume thresholds for large imports, simulation permission specifics.

---

## 7R. ATTENTION AND RELEVANCE CONTROL  [CORE CONCEPTUALLY DESIGNED, NOT BUILT]

*Designed S18. Fourteen decisions settled interactively with Ness, checked by ChatGPT and Ness before adoption. No code written.*

WHAT IT IS. The component that decides what is worth showing, retrieving, or acting on in a given moment — and by what explicit, auditable rule. Every component in N.H that surfaces something (Context Retrieval, Computed View, Action Surfacing, Reread Lifecycle, Living State Web) depends on a definition of relevance. Attention and Relevance Control provides that definition through a structured, provenance-bearing judgment that each consuming component uses according to its own declared rules.

WHAT IT MUST NOT DO. Attention and Relevance Control must not determine truth, evidence strength, causation, authority, permission to act, or Ness's final judgment. It must not merge Person-Boxes, resolve clashes, or determine which side of a clash is correct. It must not rewrite, reorder, or suppress any root, reading, telling, or clash. It must not run privacy or deletion eligibility checks — those are §7Q's responsibility and are external prerequisites. It must not write directly into the Living State Web. It must not silently guess an unrecognized purpose type.

EXTERNAL PREREQUISITE. §7Q's privacy and deletion eligibility gate runs before Attention and Relevance Control receives any candidates. Attention and Relevance Control operates only on already-eligible material. It does not own, rerun, or redefine privacy eligibility.

---

### DECISION 1 — OUTPUT FORM

A relevance judgment is a two-layer structured object produced after §7Q eligibility has been established:

**Layer 1 — Context-specific boolean gate.** Determines whether a candidate belongs in the present task at all. Each gate condition is named and explicitly declared for the consuming context. A candidate that fails any required gate condition is excluded from this context without a graded judgment being produced. Gate conditions are categorical, cheap to evaluate, and readable as language.

**Layer 2 — Graded named dimensions with provenance.** Produced only for candidates that pass the gate. Each dimension is named, carries its own value, and preserves the source or method that produced it. Dimensions are never collapsed into a single hidden score. Consuming components use dimensions according to their own declared rules.

A relevance judgment determines relevance to the current purpose only. It does not determine truth, evidence strength, causation, authority, permission to act, or Ness's final judgment.

---

### DECISION 2 — PRODUCER SELECTION

Each named dimension in a relevance judgment has its producer selected individually. Three producer types are available:

**Deterministic rules** produce structural, temporal, currency, count, and other directly computable dimensions. Rule-based dimensions are reproducible from the same inputs with no model involved.

**The embedding model** (`all-MiniLM-L6-v2`) produces semantic-similarity and thematic-proximity dimensions. It does not produce dimensions that rules can compute reliably.

**The mouth model:** (`dolphin-llama3`) produces only specifically declared interpretive dimensions that cannot be produced reliably by either rules or embedding similarity. The mouth may not be used outside the declared dimensions and contexts. Authorization for mouth use is through a declared relevance mode or context configuration — it does not require Ness to manually approve every individual invocation. The mouth may not self-approve its own output.

**Every dimension** — regardless of producer — must preserve: which producer generated it, rule version or model version and index or prompt version as applicable, and the value produced.

---

### DECISION 3 — EVALUATION TIMING

Attention and Relevance Control runs **on demand by default**. A consuming component requests a relevance judgment for a specific candidate or set of candidates in a specific context, and the judgment is computed at that moment.

**Triggered pre-computation** may be enabled only for specifically declared, latency-sensitive contexts. It is optional. It must not create a continuously maintained global relevance state.

**Every precomputed relevance judgment is bound to the exact context in which it was produced.** It must preserve: the context or purpose identifier; the consuming mode and configuration version; the candidate and target identifiers; the producer, rule, model, index, and prompt versions used; the trigger that caused the computation; the time it was produced; its current validity or staleness state.

A cached or precomputed result may be reused only while its declared context and validity conditions still match. If the purpose, source material, configuration, producer version, a relevant Ness response event, or another declared invalidating event changes, the result must be marked stale or recomputed. A precomputed result must never silently become a permanent statement that an item is relevant in every context.

**Mouth-produced dimensions** may not be precomputed unless that use is explicitly declared in the context configuration and the required independent validation mechanism has been designed for that specific mode.

**Architectural reason:** the primary reason for the on-demand default is that relevance is context-dependent and must not be maintained as a global background truth.

---

### DECISION 4 — TWO-TIER CONFIGURATION CONTRACT

A declared relevance mode uses a **two-tier contract**.

**Tier 1 — shared required contract, owned and validated by Attention and Relevance Control.** Every relevance mode must declare at minimum:
- a stable mode identifier and version
- the exact purpose or context of the relevance evaluation (see Decision 9 for form)
- the consuming component
- the candidate and target object types
- the named context-gate conditions and the producer assigned to each
- the named graded dimensions and the producer assigned to each
- mouth authorization scoped to specific named dimensions and contexts — not one broad authorization flag
- whether the mode runs on demand or allows triggered pre-computation
- the declared triggers and invalidating events when pre-computation is enabled
- when mouth-produced dimensions are declared: the identifier and version of the Tier 2 unresolved-dimension handling rule (see Decision 10)

**Tier 2 — component-local settings, owned and validated by the consuming component.** May declare: component-specific thresholds, ordering or weighting rules, fallback behavior, surfacing behavior, unresolved-dimension handling rules, and other consumer-owned settings. Tier 2 does not need to be completely designed for every consuming component before any mode can run. A specific relevance mode requires only the local fields that mode needs. Later additions to Tier 2 must produce a new configuration version.

**Responsibility boundary:** Attention and Relevance Control validates Tier 1. The consuming component validates Tier 2. Neither component silently takes ownership of the other tier.

---

### DECISION 5 — NESS'S RELATIONSHIP

**Inspection is always available and unrestricted.** Ness can inspect any relevance judgment in full — its gate results, graded dimensions, producer provenance, mode identifier and version, and the full Tier 1 and Tier 2 configuration that produced it.

**Per-judgment correction is direct and lightweight.** Ness may record that a specific relevance judgment is wrong, too high, too low, or misdirected without a proposal-and-confirmation cycle. The correction is appended as a separate linked Ness response event. It never rewrites the original judgment. Original judgment and correction coexist in the append-only record.

**Per-judgment override is context-scoped and recorded.** Ness may directly override the use of a specific judgment for the current context. The override must be explicitly scoped to that context, recorded as its own event, and must not silently propagate into a permanent mode change.

**Reusable mode or configuration changes use a proposal-and-confirmation path.** Before a mode change is committed, N.H surfaces what would be affected: which gate conditions, graded dimensions, consuming components, precomputed results, and other mode versions are touched. Ness then confirms. The confirmed change creates a new configuration version. The prior version remains in the record and is never overwritten.

**The proposal step exists only to surface consequences.** It does not give N.H authority to veto Ness's confirmed decision.

**Invalid configuration handling.** If a requested configuration is technically invalid or violates a protected architectural boundary, N.H must identify the exact conflict precisely and help translate Ness's intention into a valid proposed configuration. The original request must be preserved. N.H must not silently apply an invalid configuration or dismiss the request without explanation.

**Append-only history is preserved throughout.** Original relevance judgments are never rewritten. Corrections are separate linked events. Overrides are separate scoped events. Prior mode versions are never deleted.

---

### DECISION 6 — VALIDATION OF MOUTH-PRODUCED DIMENSIONS

Every mouth-produced relevance dimension must pass a **required deterministic validation** including all of the following checks:
- **Schema and bounds validation** — value present, correct type, within declared bounds
- **Required provenance validation** — all required provenance fields present and populated
- **Grounding check** — value traceable to the declared candidate, target, and context
- **Out-of-scope detection** — value does not rely on material outside the declared inputs
- **Contradiction check** — value does not contradict directly verifiable structural facts
- **Certainty check** — value does not claim more strength or certainty than its grounding supports

**Three validation outcomes:**
- **Validated** — structurally valid and grounded; all deterministic checks pass
- **Failed** — invented, structurally invalid, contradictory, outside declared bounds, missing provenance, or relying on undeclared inputs
- **Unresolved** — grounded and structurally valid, but interpretive correctness cannot be independently established by deterministic means

A validated outcome does not claim the interpretation is substantively correct. It claims only that no rule-detectable error was found.

**Optional model-based validation** may be required for specifically declared dimensions or contexts. When declared: the mode's Tier 1 must name the validator model or configuration and state the reason it is required; the second validator must be meaningfully independent (a repeated call to the same mouth model with the same setup does not constitute independent validation — the mode must declare how independence is increased); the second validator produces its own provenance-bearing validation result; if producer and validator disagree, N.H records the disagreement and follows the mode's declared uncertainty behavior — it must not silently select the result with greater model confidence; the second validator is not final authority.

**Mouth-produced interpretive dimensions may not act as categorical context-gate conditions.** They may contribute to graded ranking or explanation. Context-gate conditions remain deterministic. A protected exception requires a later explicit design decision.

---

### DECISION 7 — MINIMUM SHARED VOCABULARY

**SHARED CONTEXT-GATE CONDITIONS (boolean, rule-produced, deterministic):**

- **`same_thread_or_group`** — candidate and target belong to the same recorded thread or grouping. The current implementation may use `source_title` to derive this, but the vocabulary does not permanently depend on that legacy field.
- **`precedes_target_in_same_thread`** — candidate root precedes the target root in position within the same thread or grouping.
- **`within_declared_time_range`** — candidate falls within a time range explicitly declared in the mode's Tier 1 configuration.
- **`object_type_matches`** — candidate's object type matches the declared eligible types for this context.

**SHARED NAMED DIMENSIONS (graded, provenance-bearing):**

- **`semantic_similarity`** — embedding model similarity between candidate and target or declared query representation. Producer: embedding model. Provenance must include model version and index version.
- **`temporal_distance`** — deterministic raw time distance between candidate and target timestamps, with its unit preserved. Normalization, scaling, or threshold application belong to Tier 2.
- **`positional_distance`** — deterministic count of positions or turns between candidate and target within their shared thread or grouping.
- **`currentness_status`** — the recorded Living State Web currentness category of the candidate node when the candidate is a state node. Producer: deterministic rule reading the node's recorded status. The six conceptual statuses from §7D apply. This dimension carries the recorded status; it does not determine relevance strength.
- **`explicit_links`** — a multi-valued list of recorded structural links between candidate and target. Each entry preserves: link type, link status, and link provenance. Link types include same Person-Box, same confirmed theme, same proposed theme, same `derived_from` chain, and shared root IDs in a telling. Producer: deterministic rule. Only links already recorded in the store are surfaced.
- **`ness_response_links`** — linked Ness response events pointing to the candidate. Each entry preserves: response type, scope, target identifier, and timestamp. Producer: deterministic rule.
- **`proposal_acceptance_outcome`** — the outcome of the Reading Proposal Acceptance Check for a candidate reading, including the exact rejection reason when the outcome is a failure. Producer: deterministic rule. Applicable only when the candidate is a reading.
- **`reading_context_status`** — whether a candidate accepted reading is marked as context-limited or as `insufficient_context`. Producer: deterministic rule. Applicable only when the candidate is an accepted reading. Distinct from `proposal_acceptance_outcome`.
- **`active_clash_links`** — linked active clashes, contrary evidence, or unresolved conflicts associated with the candidate. Each entry preserves clash record identifier, clash type, and detection mode. Producer: deterministic rule. Clashes are surfaced, not resolved.

**STANDING RULES:**

Positional versus semantic channel identity is mandatory retrieval provenance metadata carried in the retrieval record. It is not a relevance dimension. The channel distinction from §7F is preserved — vocabulary entries do not merge the two channels.

Privacy and deletion eligibility are external prerequisites, not gate conditions owned by Attention and Relevance Control.

Vocabulary extension path: a consuming component may declare a new local dimension when its mode is designed. A dimension used across multiple components may later be proposed for promotion into the shared vocabulary through the proposal-and-confirmation and versioning process from Decision 5.

---

### DECISION 8 — LIVING STATE WEB BOUNDARY

**Attention and Relevance Control never writes directly into the Living State Web.** It emits its own provenance-bearing relevance records. These records belong to Attention and Relevance Control's own record space.

**A relevance event may trigger a currency review.** The Living State Web may, under an explicitly designed rule, use a relevance event as an authorized trigger to review or recompute the currentness status of a state node. The trigger causes a review to happen — it does not supply the evidence that determines the review's outcome.

**A relevance event alone does not count as evidence that a state is current.** Any actual currentness update must rely on independently valid evidence under the Living State Web's own rules: root evidence, a separate Ness response event, or another explicitly authorized evidence source.

**Relevance and currentness are permanently separate properties.** Something may be relevant because it is historical, ended, uncertain, contradicted, or currently under review. High relevance does not imply currentness. Low relevance does not imply a state has ended.

**Ness's statements providing currentness evidence must be recorded separately.** If Ness makes a statement during an interaction that itself constitutes currentness evidence, that statement must be captured as a separate Ness response event with its own provenance — not embedded inside or derived from the relevance judgment.

**Circular support is explicitly prohibited.** A state node must not become current because it was judged relevant when that relevance judgment partly depended on its recorded currentness status. The chain `currentness_status` feeds relevance judgment → relevance judgment feeds currency update → currency update feeds `currentness_status` is forbidden.

Authorization of relevance events as Living State Web currency review triggers belongs to the Living State Web's own future design session.

---

### DECISION 9 — TIER 1 PURPOSE FIELD

The purpose or context field in the Tier 1 relevance mode contract is a **structured object** with two parts:

**Required: controlled purpose type.** Must be one value from the defined controlled vocabulary. Used for Tier 1 validation and cross-mode comparison. Attention and Relevance Control validates that the declared type is a known value before accepting the mode configuration.

**Optional: human-readable label.** A string the consuming component may add to describe its specific use. Explanatory only. Must not change system behavior — the label carries no semantic weight in validation, routing, or evaluation logic.

**Starting controlled vocabulary:**
- **`retrieval_context_selection`** — evaluating candidates for selection as context in a reading pass
- **`view_assembly`** — evaluating candidates for inclusion or ordering in a Computed View snapshot or View Layer presentation
- **`action_surfacing`** — evaluating candidates in support of surfacing a possible action to Ness
- **`reread_trigger_evaluation`** — evaluating whether materially relevant new information justifies a condition-based reread trigger
- **`state_review_trigger_evaluation`** — evaluating whether a relevance signal warrants triggering a Living State Web currency review; named to reflect that Attention and Relevance Control evaluates whether a review should be triggered, not whether a state is current

New controlled types may be added through the proposal-and-confirmation and versioning process from Decision 5. A new label never requires a vocabulary version change. A new controlled type does.

---

### DECISION 10 — UNRESOLVED DIMENSION HANDLING ACROSS THE TIER BOUNDARY

When a relevance mode declares one or more mouth-produced dimensions, the Tier 1 configuration must include a reference to the Tier 2 unresolved-dimension handling rule containing: the **identifier** of the Tier 2 handling rule and the **version** of that rule.

Attention and Relevance Control validates that this reference is present and non-empty in Tier 1 whenever the mode declares mouth-produced dimensions. It does not inspect, parse, or validate the content of the Tier 2 rule itself.

The consuming component owns and validates the rule itself. When the rule changes, a new Tier 2 version is produced. The Tier 1 reference must be updated to point to the new version — otherwise the mode's Tier 1 reference becomes stale and Tier 1 validation will detect the mismatch.

A mode without mouth-produced dimensions has no obligation to include this reference.

---

### DECISION 11 — DISAGREEMENT RECORD SCHEMA

When a mouth-produced relevance dimension's value is contradicted by a declared model-based validator, a disagreement record is created containing:

- **Stable identifier** — unique to this disagreement event
- **Pointer to the producer result** — exact reference to the mouth-produced dimension value record, including its provenance
- **Pointer to the validator result** — exact reference to the model-based validator's output record, including its provenance
- **Disagreement type** — structural nature of the conflict from a declared vocabulary: value out of bounds, grounding claim contradicted, certainty exceeds support, or another declared type
- **Producer identity and version** — which mouth model, prompt version, and configuration produced the original value
- **Validator identity and version** — which validator model or configuration, and what independence mechanism was declared
- **Uncertainty behavior rule** — identifier and version of the declared uncertainty behavior rule from the mode's Tier 1 configuration
- **Resulting dimension state** — the state of the dimension after the uncertainty behavior was applied
- **Timestamp** — when the disagreement was recorded

Full interpretive content is not reproduced in the disagreement record. It remains in the original producer result record and validator result record. The disagreement record points to both separately. The record is append-only and never rewritten.

---

### DECISION 12 — RELEVANCE EVENT RECORD SCHEMA

A relevance event record is the durable append-only trace of a completed relevance evaluation. It must contain:

- **Stable identifier** — unique to this evaluation event
- **Mode identifier and version** — the Tier 1 mode under which the evaluation ran
- **Purpose type and label** — the controlled type and optional label from the mode's Tier 1 purpose field
- **Consuming component** — the component that requested or declared this evaluation
- **Exact context or request identifier** — the identifier of the specific request or context instance
- **Target object or objects** — the target against which candidates were evaluated, by object type and identifier
- **Candidate object type** — the declared type of candidates evaluated
- **Evaluation mode** — whether the evaluation ran on demand or through triggered pre-computation
- **Trigger identifier** — when triggered pre-computation was used, the identifier of the trigger event
- **Outcome summary counts:** candidates that passed the context gate; candidates excluded by the context gate; candidates with one or more unresolved dimensions; candidates with one or more failed dimensions; candidates that produced one or more disagreement records
- **Pointers to individual relevance judgments** — one pointer per judgment produced; full judgment content remains in the individual judgment records and is not reproduced here
- **Whether any disagreement records were created** — with pointers to those records if present
- **Timestamp** — when the evaluation completed

The record is append-only and never rewritten.

---

### DECISION 13 — PATTERN OBSERVATION CONDITIONS FOR PER-JUDGMENT OVERRIDES

N.H may surface the observation that per-judgment overrides suggest a possible mode change only when all three pattern conditions are met simultaneously:
- **Same mode and version** — the overrides concern the same mode identifier and version
- **Same target** — the overrides concern the same gate condition, dimension, or outcome type
- **Same correction direction** — the overrides consistently point in the same direction of correction

When surfacing the observation, N.H must: show the exact pattern observed; present a mode change as one possibility for Ness to consider, not a recommendation; make explicit that Ness may treat the individual corrections as correct contextual responses rather than evidence of a systematic mode error.

**Silence or no immediate action is not dismissal.** The observation remains open until Ness explicitly acts on it or explicitly dismisses it.

**Explicit dismissal closes the observation.** N.H must not surface the same pattern again unless new overrides appear or the evidence base materially changes.

**The observation never changes the mode automatically.** Any permanent mode change still follows the full consequence-preview and Ness-confirmation process from Decision 5.

---

### DECISION 14 — UNRECOGNIZED PURPOSE TYPE HANDLING

If Attention and Relevance Control receives a mode configuration declaring a purpose type that is not in the current controlled vocabulary, it must not run the evaluation.

It must: **halt immediately** — no gate evaluation, no dimension computation, no relevance event record produced for an evaluation that did not run; **identify the unknown type precisely** — name the exact value that was not recognized and which vocabulary version was checked against; **preserve Ness's original request** — the full original configuration and the context that produced the request are retained without modification; **explain the problem in plain language** — state that the purpose type is not recognized, what that means, and why the evaluation cannot proceed; **offer two paths forward:** mapping the request to an existing approved purpose type with Ness's explicit confirmation before any evaluation runs under the mapped type, or proposing a new purpose type through the consequence-preview, confirmation, and versioning process from Decision 5.

**N.H must never silently guess which purpose type was intended.** A close match is not authorization to substitute.

**A halted evaluation is not a failure of Attention and Relevance Control.** It is the component behaving correctly. The halt is recorded as its own append-only event with the unknown type, the preserved request, and the timestamp.

---

### WHAT REMAINS OPEN FOR ATTENTION AND RELEVANCE CONTROL

The following belong to future design or build sessions and must not be assumed settled:

- Individual Tier 1 and Tier 2 relevance mode declarations for Context Retrieval, Computed View, Action Surfacing, Reread Lifecycle, and Living State Web
- Tier 2 unresolved-dimension handling rules for each consuming component
- Component-specific thresholds, ordering, weighting, and fallback behavior in Tier 2
- Authorization of relevance events as Living State Web currency review triggers — belongs to the Living State Web's own design session
- Disagreement type vocabulary extensions beyond the starting set
- Independence mechanism specifications for any declared model-based validators
- New shared vocabulary dimensions promoted from local use
- Exact field types, storage formats, and indexing — belongs to the build phase

---

## 8. THE RESEARCH PIPELINE  [DESIGNED — Brave not wired]
Brave (raw) → OpenRouter/llama (one auditable synthesis) → create-space → gate. Findings land in MEMORY as readings, never the mouth.

**★ WHY BRAVE (design decision — RESTORED S19).** Brave returns genuinely raw JSON from its own independent index — no extraction, relevance-ranking, or content-validation layer applied before the data reaches N.H. Tavily applies that kind of processing ("pre-chewed for AI"), which is the smaller version of the exact opinion-layer problem this pipeline was designed to avoid. Brave replaced sonar; the OpenRouter synthesis step is a separate, distinct job. **Keep both keys — they do two different things.**

**★ THREAT MODEL — prompt injection, not malware (RESTORED S19).** Traditional malware is not the real risk here: there is no download-and-execute step, and the pipeline only pulls titles/URLs/snippets, not rendered pages with embedded scripts. (Stays true only if no future step renders full pages or runs JS from arbitrary URLs — if full-page text is ever needed, fetch as plain text, never execute.) The real risk is **prompt injection**: malicious page content worded to manipulate the synthesis model reading it. The SIMULATION/REALITY gate — built for an unrelated reason — already contains this almost completely: even a successful injection only ever produces a SIMULATION record, never a direct action, never a write to REALITY. Worst case is "something misleading sits in the review queue," not anything happening on the machine.

**★ SECURITY DEFAULTS (non-negotiable, baked into the Cursor instruction — RESTORED S19):** Two conditions required to keep the above true — both go into the Cursor instruction for the synthesis call by default, not as something to remember to add separately: (1) synthesis model is text-in/text-out only — no tool-calling, no file access, no ability to make its own outbound requests; (2) synthesis system prompt states explicitly that search results are unverified raw web content to extract facts from, never instructions to follow.

**Auto-reject, never auto-delete** — flagged/untrusted content routes automatically into the Reject bucket without requiring a click from Ness, but stays logged, same as any other rejected record. An AI with silent-delete authority over "untrustworthy" content is itself a prompt-injection target (a malicious page could try to get something legitimate flagged and erased instead of just contained), and it reintroduces the exact "things happening invisibly" failure this gate exists to prevent.

**Rejected-bin "look don't touch" display rules (RESTORED S19):** URLs render as plain text strings, never `<a href>` — nothing clickable, nothing to misclick. No auto-fetched favicons, previews, or URL unfurling — viewing the bin never triggers an outbound request toward anything in it. Copy/select disabled on that specific view — guardrail against accidental drag-select-and-paste, not a real security boundary. Strip invisible/zero-width/RTL-override characters before display — closes a text-spoofing gap that survives plain-text rendering. Render via `textContent`-style escaping, never `innerHTML` — anything that looks like a tag displays as inert literal characters. All of these are default build behavior for the rejected-bin page, not separately requestable options.

**★ COST AT FULL NIGHTLY SCALE (confirmed S16):** Brave roughly ~$62/month at about 13,500 queries/month under the quoted pricing assumptions, after the reported monthly credit + OpenRouter synthesis ~$60-240/month = **~$120-300/month total**. During building/testing: **$0** (inside $5 free Brave credit). **⚠ SAFETY BUILD REQUIREMENT:** Brave has NO spending cap — a loop can bill without stopping. When this pipeline is wired (item 8 in build order), a query counter / daily cap MUST be built into the code. Not optional.

**★ ACADEMIC SOURCE — STILL OPEN (S19).** Google Scholar is off the table (no official API; scraping violates Google's ToS). Two candidates still open: Semantic Scholar API (sharper for CS/AI-leaning queries) vs OpenAlex (broader across all fields) vs both. Both are free and slot into the same raw-fetch → synthesis → gate pipeline as a second source. Decision pending — add to §11 open items.

**★ PIPELINE SCOPE (settled June 25 2026).** The research pipeline has two responsibilities: (1) gathering new outside information and bringing it into N.H's review queue; (2) checking stored information against outside sources to assess whether it is still supported, outdated, uncertain, or contradicted by current evidence.

**★ SOURCE PRESERVATION — FORMAT AND REQUIREMENTS (settled June 25 2026).** When the pipeline uses a source, it saves two things alongside the research reading: (1) **The relevant excerpt** — the specific passage actually used, saved as plain text. (2) **A full-page frozen screenshot** — a static, non-interactive capture of the source page as it appeared at retrieval time, saved as: frozen PNG, inactive URL, provenance metadata, timestamp, research-reading ID, and integrity hash. No live HTML, scripts, active forms, cookies, browser sessions, or executable webpage behavior is preserved. The screenshot is inert visual evidence of what the page contained at capture time, not a live preserved page.

**⚠ LIVE-RETRIEVAL SECURITY BOUNDARY.** Full-page retrieval for screenshot capture is a new pipeline step beyond the existing snippet-only search. It introduces a new surface area. Live retrieval and rendering must occur in a separately isolated capture environment — no page code, cookies, session state, or active behavior from the retrieved page may enter the saved record or gain access to N.H. The preserved result is only the frozen screenshot and the separate plain-text evidence; no live page content is preserved. The existing text-in/text-out synthesis defaults above apply to the synthesis step only; full-page capture requires its own equivalent isolation at the capture layer. The exact implementation of the isolation environment is not yet designed.

**★ AUTOMATIC RE-CHECKING (settled June 25 2026).** The pipeline may re-check stored information against outside sources on a schedule, but only on a schedule Ness explicitly approves. N.H may not create, modify, or extend its own re-check schedule.

**★ FALLBACK — WHEN FULL-PAGE SCREENSHOT CANNOT BE PRESERVED (settled June 25 2026, Option A).** If the full-page screenshot cannot be captured (paywall, page unavailable, screenshot failure, size limit, or other cause): keep the excerpt, the inactive URL, provenance metadata, timestamp, research-reading ID, integrity hash, and the known reason the capture failed. Mark the source clearly: **SOURCE PRESERVATION INCOMPLETE**. The source may remain available as evidence, but N.H must not treat it as fully preserved or assign it the same confidence as a source with a complete frozen-page capture. Important claims from an incompletely preserved source require corroboration from another source before being treated as strongly supported. Do not discard automatically. Do not hide the preservation failure.

## 9. DESIGNED, NOT BUILT — THE REST  [DESIGNED or CONCEPTUALLY DESIGNED]
Access/auth; mobile three modes; interactive canvas; behavioral-baseline wellbeing; HUD redesign; person-boxes gather (§7L); image front door (§9A); phone-data importer; memory browser; voice in/out; ChromaDB cleanup; folder cleanup. Catalog front door (§7E), context retrieval (§7F), meaning engine interior (§7G), reread lifecycle (§7H), view layer (§7I), clash handling (§7J), story layer (§7K), computed view (§7M), action surfacing (§7N), action-result return path (§7O), permission and authority boundaries (§7P), and attention and relevance control (§7R) are core-conceptually designed, not yet built. Privacy/deletion/sensitive-data handling (§7Q) is partially conceptually designed, not built.

## 9A. IMAGE INGEST — FIRST WORKED FRONT-DOOR EXAMPLE  [DESIGNED]
Metadata → plain-description → context-meaning → Ness confirms. Precondition for WhatsApp media (§12).

## 10. ORIGINALITY (honest calibration)
The combination ships nowhere: inverted default + per-person never-closing STORY + DUMB/SMART split + person-boxes-as-gather + pure tape + wonder-kept-and-shown + memory-grows-not-the-mouth + two-destinations/two-files + living state web + structured perspective model + hybrid theme system + proposal-based identity anchors + blocking deletion verification + private-access-open-by-default + attention-and-relevance-control as a structured two-layer judgment. Never claim inventing local AI, approval gates, or a trained model.

**★ NEAREST PUBLISHED COUSINS (confirmed June 2026 field survey — RESTORED S19).** Every individual brick exists somewhere (local-first personal AI: Khoj, PAI, Second Me; human-in-the-loop gates: LangGraph, Mastra; epistemic-provenance KGs; dual-LLM injection containment: CaMeL; N-of-1 baseline monitoring: clinical digital phenotyping). Two 2026 preprints are the nearest cousins: **memorywire** (arXiv 2606.01138 — diff-and-approve memory, but drifts to auto-approve and leaves recall ungated) and **SSGM** (arXiv 2603.11768 — two-track memory, but automated gate, not human). **Three sharpest contrasts with both:** (1) mandatory vs optional approval — N.H's gate is non-bypassable human judgment, not optional or automatable; (2) gating recall/indexing as well as storage — N.H gates what can be retrieved, not just what is written; (3) human gate vs automated gate — the decider is always Ness, never the system. **Claim the combination and the inverted default** — never the invention of local AI or approval gates alone.

---

## 11. WHAT'S OPEN / NEXT (priority order)

1. **Append-only accretive store** — ✅ BUILT, 5,521 sealed. (c) wire into live flow — part of model-wiring/live-path.
2. **THE FORCED ORDER — 2a ✅ → 2b ✅ → 2c IN PROGRESS:** A ✅ B ✅. **NEXT: Engine C (story-layer). C needs story-bearing gold cases first.**
2b. **THE DETECTOR — recipe locked, live build deferred.** Fallback for role-less sources.
3. **★ THE MODEL WIRING (§16) — local-first.** Wire dolphin (mouth) + embedding search. **CHROMA REBUILD ✅ DONE (S16) — `nh_roots_v1` built from 5,521 clean roots.** Old 116k kept. **Hardware direction settled: RTX 3090 24GB (supersedes S16 RTX 5060 Ti 16GB plan); first model candidate to test: Dolphin 3.0 R1 Mistral 24B — re-run both gold sets before adoption.**
4. **NIGHT-SEARCH (committed, LATER).** Feeds MEMORY as readings. Cost ~$120-300/month at full scale; $0 during build. Brave spending-cap safety note: query counter required in code.
5. **Image-ingest front door (§9A).**
6. **Universal Filter / meaning engine** — = item 2's (2c), now in progress.
7. **ChromaDB — `nh_roots_v1` BUILT (S16). Old 116k kept until proven.**
8. **Research pipeline build.** ⚠ Brave spending cap — query counter / daily cap required in code when built.
9. **Academic search source decision (S19 — OPEN).** Google Scholar is off the table (no API; scraping violates ToS). Two candidates: Semantic Scholar API (stronger for CS/AI) vs OpenAlex (broader across all fields) vs both. Both are free and slot into the existing pipeline as a second source without new architecture. Decide before wiring the pipeline.
> *★ HISTORICAL — SUPERSEDED (Ness's explicit decision, June 25 2026): "Hetzner sovereignty sync" was an open item carried forward in §11 from early sessions, predating the accessible session history. Its exact original purpose cannot be verified from the accessible evidence. Ness has decided to move away from Hetzner entirely. This item is no longer an active open task.*
10–12. nh_service (✅ disabled) · mobile + canvas · HUD redesign.
13. **THE [BUILT]-CLAIMS SWEEP — ✅ DONE (S13).** Future builds owe a quick existence-and-shape check.
14. **Folder cleanup** — `cloudflared.exe`; stale `peek.txt`; the ~12 S13 detector probes (keep the recipe reference); the stale "188 seed records" docstring in `_validate_record`.
15. **§11.15 STORE-COUNT RECONCILIATION — ✅ CLOSED BY ACTION (S12).**
16. **WhatsApp archive → eventual ingest (deferred):** decrypt → SQLite front door → image front door → child-data call → ingest only with engine.
17. **Open design threads (low):** spine re-draw; old gate lags; clash/gap UI surfacing; write the §0A DUMB/SMART section into final place; ~24 unreviewed Cursor batch files; person-box multi-box tagging; `source_title` alias/correction layer design (deferred); future root schema version (rename `subject` field).
18. **MULTI-BOX (sealed-batch) ARCHITECTURE — undesigned. Must be designed before a SECOND batch is written.**
19. **★ CONFIDENCE — RESOLVED (S14).** TWO-SLOT `confidence` object. Value-FORM deliberately loose, pinned later as new schema_version.
20. **★ "UNDERSTANDING" — gold-standard sets BUILT & SEALED.** v1 (8 cases, S14) + v2-B (7 cases, S16) both on disk and sealed. Engine A ~5–6/8 on v1. Engine B 6.5/7 on v2-B on the tested dolphin 8B setup; the cause of the remaining miss has not been isolated — model capability, prompt framing, context format, and run variance remain possible contributors. RTX upgrade + a verified model candidate must be benchmarked; 7/7 is a goal, not an expectation or promise.
>    - **ENGINE B GOLD CASES (v2-B, S16):** B1 `7ac0381c` "episode 2" ✅; B2 `4e125b71` "yes sure, second." ✅; B3 `0df151d3` "yes, second option." ⚠️ (cause not isolated); B4 `9359edff` emotional reaction ✅; B5 `580d74d4` "Brief slow." ✅; B6 `09514821` "Yes! This is it." ✅; B7 `4b4e5551` "כן" ✅.
>    - **ENGINE B BUILD LESSONS (S16):** semantic context search fails for conversational turns — position-based is the correct lever; truncating context content kills quality — pass full content; BACKGROUND/END BACKGROUND framing prevents the mouth from answering instead of reading; tested dolphin 8B setup scored 6.5/7; cause of B3 miss not isolated.
21. **RE-READ LIFECYCLE + THE VIEW LAYER — CONCEPTUALLY DESIGNED (S17), NOT BUILT.** §7H, §7I.
22. **PERSON-BOX CONTAMINATION — GOVERNING RULE CONCEPTUALLY DESIGNED.** §7L requires per-element provenance; the exact link schema, validation rules, and implementation remain open.
23. **OFF-BOARD AFFIRMATION FEEDBACK SEAM** — record Ness's accept/reject as a dated, weightless STORY-LAYER EVENT.
24. **PRIVACY / THREAT MODEL + REDACTION PATH — PARTIALLY CONCEPTUALLY DESIGNED (S17), NOT BUILT.** §7Q. Implementation mechanics, detection methods, verification procedures remain undesigned.
25. **GO-LIVE HARDENING BLOCK — DEFERRED, does NOT gate the engine.**
26. **MODEL-REPLACEMENT DEFAULT — SETTLED.** A new mouth must be tested against BOTH sealed gold sets before replacing the current mouth; old readings keep old `produced_by`; no automatic mass reread. The future model candidate (first planned: Dolphin 3.0 R1 Mistral 24B) remains unverified and must be benchmarked on v1 + v2-B before adoption.
27. **QUARANTINE PHASE + BOOTSTRAP RETRIEVAL RULE — DESIGNED; quarantine STORE BUILT (S14).** Quarantine holds A + B gold-run output. Promotion needs gold + held-out + manual inspection.
28. **LIVING STATE WEB — PARTIALLY CONCEPTUALLY DESIGNED (S17), NOT BUILT (§7D).** Node/edge types, grounding rule, currency rule, action surfacing (§7N), return path (§7O), and relationships to Computed View/Story Layer/Person-Boxes/authority/privacy designed. Schema, evidence thresholds, aging rules, trigger specifics, attention/relevance control, purpose-aware lenses, world model, and build order remain undesigned.
29. **ATTENTION AND RELEVANCE CONTROL — CORE CONCEPTUALLY DESIGNED (S18), NOT BUILT.** Fourteen decisions settled. Two-layer relevance judgment, three producer types, two-tier mode contract, shared vocabulary, validation mechanism, record schemas, Ness's relationship, Living State Web boundary, purpose field controlled vocabulary, and pattern observation conditions. Individual component relevance mode declarations belong to each consuming component's own design session. Authorization of relevance events as Living State Web currency review triggers belongs to the Living State Web's own design session. See §7R.
30. **WONDER AND SIMULATION MECHANISM — CONCEPT LEVEL ONLY, NOT DESIGNED.** Concept in §7B; interface concepts in §19. Mechanism undesigned.
31. **WORLD MODEL — NOT DESIGNED.** Named in Living State Web domain list. Must be designed separately.
32. **END-TO-END CYCLE — IDENTIFIED, NOT YET DESIGNED.** The major components addressed in S17 and S18 now have core conceptual architecture, while the wonder/simulation mechanism and the world model remain open. The complete flow from a new input arriving through every relevant component to something appearing in the Computed View or chat response has not yet been designed and written as a single connected sequence.
33. **INTERFACE, WORLD, AND INTERACTION SYSTEM — IN-PROGRESS DESIGN, NOT BUILT.** Architectural content in §19. Simulation interior, gesture vocabulary, VR, camera, and accessibility substantially undesigned. Design paused and resumable.
34. **MEANING-TO-TECHNICAL MAPPING QUESTIONS (S19 concept-name review session) — four topic groups containing five open questions.** These questions arose during S19 when the reclaimed meaning names were checked against the existing technical design. They must remain recorded as open, must be handled through a careful audited meaning-to-technical design process, and must not be silently decided during unrelated technical work. (a) **Grounded Keeper of Origins — scope:** Does the name cover only Origin storage, or all dumb machinery? (b) **Origins — granularity:** How is mixed-media Origin granularity handled? (c) **Origins — time-fields:** Which time fields belong to an Origin, and what does each timestamp mean? (d) **Those Three To Become A One — no-context mode:** How does the name map to the no-context reading mode, where Engine A reads only the bare root? (e) **Holding — technical representation:** How is Holding technically represented in the Person-Box data structure?

---

## 11-SETTLED. (condensed)
- **S4–S11:** unit = span-claim; carry `role`; borrowed frozen mouth; two models; local-first; person-boxes; pure tape; wonder kept-and-shown; catalog; soul-correction; memory-grows-not-the-mouth; two-file 2a.
- **S12:** store restored; `role` added (7-field root); clean ingest; 5,521 clean roots; Chroma=old 116k index; two-destinations shape.
- **S13:** [BUILT]-sweep done; 2a plumbing built; roots sealed; detector recipe locked (94.89%); eleven doc-refinements + quarantine/bootstrap captured.
- **★ S14:** the three forks CLOSED — confidence = two-slot object; gold scoring = six rules (semantic match, Ness judges); failure-behavior = honest insufficient-context, revisable. Reading validator + writer BUILT & VERIFIED (17/17 tests; roots regression clean). Gold set v1 (8 cases) SEALED. Minimal engine A BUILT & run against gold (~5–6/8 after prompt+role fixes). Model test: dolphin beats qwen-abliterate-3b; Hebrew gated on bigger model/VRAM. Validator structure = extract-not-fuse (`_check_common`). Quarantine store built. Confidence value-form left loose.
- **S15-chat:** NO N.H change. Scan-only confirmation that the three files are in sync + one out-of-system teaching artifact (`NH_one_pass_demo.html`). Master stayed MASTER-15; status table untouched.
- **★ S16:** Engine B BUILT & RUN — position-based context (preceding turns, same thread, full content, n=3), BACKGROUND/END BACKGROUND prompt, tested dolphin 8B setup scored 6.5/7 on gold v2-B, cause of B3 miss not isolated. Gold v2-B (7 context-requiring cases) SEALED. Chroma `nh_roots_v1` BUILT (5,521 roots, 187.59s). Hardware upgrade decided: RTX 5060 Ti 16GB, ~₪2,590, buy 5.7.2026, target model `dolphin-llama3.1:13b`. Cost notes confirmed: $0 now, ~$120-300/month at full nightly scale. Brave spending-cap safety note added to §8 and §11 item 8.
- **★ S17:** Broad conceptual design of the major components addressed during the session, while several larger areas remain open. Catalog front door (§7E), context retrieval (§7F), meaning engine interior including Reading Proposal Acceptance Check and model-confidence-is-metadata-not-authority first-class principle (§7G), reread lifecycle (§7H), view layer (§7I), contradiction and clash handling (§7J), story layer with structured perspective model, firmness rule, and hybrid themes (§7K), person-boxes with proposal-based creation and seven-section view (§7L), computed view with seven-factor ordering and triggered snapshots (§7M), action surfacing with possibility-disposition states (§7N), action-result return path with six result states (§7O), permission and authority boundaries with stop-and-surface violation rule (§7P), and privacy/deletion/sensitive-data handling including private-access-open-by-default and model-provider-limitations-as-mouth-limitations (§7Q). Living state web partially designed (§7D). `subject` field audited as legacy provenance-batch tag. Interface and world design log incorporated (§19). Engine B overclaims corrected throughout. No code written in S17.
- **★ S18:** Core conceptual design of Attention and Relevance Control (§7R). Fourteen decisions settled interactively with Ness, checked by ChatGPT and Ness before adoption. Output form (two-layer: context gate + graded named dimensions with provenance; no collapsed hidden score; purpose-scoped only). Three producer types per dimension (rules, embedding model, mouth; each with declared provenance; mouth declaration-authorized only, may not self-approve). On-demand by default with optional triggered pre-computation; no global relevance state. Two-tier mode contract with Tier 1 owned by Attention and Relevance Control and Tier 2 owned by consuming component. Ness inspection always available; corrections and overrides direct and append-only; mode changes use consequence-preview and confirmation. Mouth-produced dimensions require deterministic validation (six checks, three outcomes: validated/failed/unresolved); validated ≠ substantively correct; optional model-based validation requires declared independence; disagreements recorded. Minimum shared vocabulary: four gate conditions and nine named dimensions. Living State Web boundary: relevance events emitted never written directly; relevance and currentness permanently separate; circular support prohibited. Tier 1 purpose field: controlled type from five-value vocabulary plus optional label. Unresolved-dimension handling: Tier 1 references Tier 2 rule by identifier and version. Disagreement record schema and relevance event record schema settled. Pattern observation conditions for per-judgment overrides settled. Unrecognized purpose type handling settled. No code written in S18.
- **★ S19:** Restore + audit + expand. §8 security block restored (synthesis text-in/text-out; auto-reject-never-auto-delete; rejected-bin look-don't-touch display rules; Brave-over-Tavily reasoning; prompt-injection threat model). §10 academic citations restored (memorywire arXiv 2606.01138; SSGM arXiv 2603.11768; three sharpest contrasts). §7A Keystone written out in full (one continuous reader; classification never locked; memory only adds; Ness as steerer). §7B seven webs written out in full (intent, deixis, common ground, implicature, theory of mind, time/sequence, re-reading); Part 6 inform-don't-ask sovereignty rule; Part 7 THE LOG (read-only, subject-tagged, permanent, clickable). §13/§14 expanded: live mechanism diagram embedded; chat front door design sketch (S8 explored-not-confirmed) folded into §14. §16 mouth model corrected: dolphin-llama3 = current test model on disk, not adopted final; Dolphin 3.0 R1 Mistral 24B = first local candidate to test; final Interactive Translator = undecided. §22 Wellbeing and Behavioral Baseline System added (full spec). §23 Mobile App Three-Mode Companion added (full spec). §24 Connection Capability added (conceptual design: lasting connection record, waiting area, one-way rule, three acceptance routes, five source types). Academic source open item added to §11. No code written.

---

## 12. SESSION 6 — THE DATA-RESCUE OPERATION  [recovery done; ingest FROZEN]
A13 WhatsApp 2012→2024, encrypted (~118 MB), archived to `C:\Phone_A13_Backup` + Drive. SETTLED: ingest FROZEN — decrypt → SQLite front door → image front door → child-data call → ingest only with engine.

## 13. THE LIVE LOOP  [DESIGNED — not built]
A figure-eight, cache outside. Fire-and-let-go starter; deep side (memory · filter · search model · mouth · wonder). **The live path (memory → search → mouth → speak) is built first.**

**THE LIVE MECHANISM — how the loop and the chat front door fit together:**

```
[diagram: NH_live_mechanism_picture.svg]
```

*Reading the diagram:* chat (right) → cache → loop·starter → deep side (creation filter → meaning filter) → memory → log·mirror (left). Memory flows back to chat in both directions simultaneously — always on, not a relay. The point-back (purple arc) is the ONE thing shown in the chat: a clickable link that jumps to the earlier piece it references, then back to now. Everything else — the recording, the routing, the filtering, the layering — runs silently underneath.

**Surface principle:** the system holds its state but does not shove it at you. Errors are tap-to-reveal, silent until tapped. No recording badge. N.H NEVER narrates its own mechanism in the chat. The chat reads naturally; the plumbing is invisible unless Ness reaches for it.

---

## 14. THE CHAT FRONT DOOR  [DESIGNED-IN-PROGRESS — explored S8, NOT confirmed, NOT built]

*The one settled-as-design piece is §13 (the live loop). Everything below rides on top of §13 but is newer and looser. Status: EXPLORED, NOT CONFIRMED. Treat as reference for "how we were thinking it works" — revisit and confirm later. Nothing here is on disk.*

TWO STAGES: RAW → CATALOG (who/when/where; live chat MAY ask, nightly never asks). Memory PULLED every turn as context, used silently; reply generated fresh by the mouth from the read; the point-back is the one surfaced thread.

**THE CORE IDEA (explored S8).** The live conversation between Ness and N.H is itself an input — the most obvious one that was never written down as one. Seeds have a front door; the WhatsApp archive will get one; but the live conversation had only been assumed to flow in, never stated. The fix fits §1A (input-agnostic, one engine, many front doors) perfectly: the live chat is just another front door. Each message is already a turn — the finest non-interpretive boundary.

**THE RECORDED CONVERSATION LABEL.** The live conversation enters labeled as "recorded conversation between Ness and N.H." This label is provenance that tells the system what kind of thing it's reading: two specific speakers (Ness's actual words + N.H's past output — which is NOT fact just because N.H said it; the membrane applies). The `subject` is a typed provenance placeholder (e.g. `live:ness_nh_conversation`), honest about origin, NOT a meaning. Real topical subject is earned later by the engine. Speaker is known and carried at the source — never guessed, never re-derived.

**THE SPEAKER RULE (settled in S8).** The speaker connects, it does not guess, and it does not claim. The store points back to where the fact already lives — a pointer to the fact, not a copy of it, not an assertion. Same move as the whole system.

**THE TWO FILTERS (explored S8 — loosest, least-confirmed part).** Chat on the right, N.H on the left, two filters in the middle: (1) AI creation filter — catches what is created in the conversation (designs, ideas, decisions); (2) meaning filter — IS the Universal Filter / meaning engine (§7A/§7B). Path: chat → AI creation filter → meaning filter → N.H (memory + log). OPEN QUESTION: is the creation filter a genuinely distinct mechanism, or a creation-aware mode of the one meaning filter? Do not treat the two-filter split as settled.

**TOPIC/SPEC REFERENCING — `re_reads` MADE VISIBLE (explored S8).** The chat can refer to topics and specifications whenever they are mentioned (not only the previous message). This is the `re_reads` mechanism (§6B) made visible, pointed at named pieces. The point-back link IS shown — it is the ONE visible thing in the chat, clickable to jump to the earlier piece and back. The topic-TYPE tag is NOT shown — that's clutter. The mechanism runs silently; the navigation link surfaces.

**GENUINELY OPEN (needs Ness to decide).** Is the creation filter a distinct mechanism or a mode of the meaning filter? Is the live chat captured always or deliberately kept (the one-way-door question, never resolved)? Both of these need Ness, not a default.

## 15. SESSION 10 — BOOT HYGIENE + SIGN-IN + .CURSORRULES  [housekeeping done]
Boot HUD traced + handled; Kensington fingerprint key; stray `install_startup.bat` deleted.

---

## 16. THE MODEL LAYER — THE BORROWED MOUTH + THE SEARCH MODEL  [DESIGNED + partly on disk]

**THE CENTRAL TRUTH.** The language model is a borrowed, FROZEN mouth + general knowledge — a commodity. Everything that makes N.H *N.H* lives OUTSIDE the model.

**WHY NOT TRAIN ONE.** Wrong resource category. Put knowledge in the MEMORY instead — yours, dated, layered, never-closed.

**★ TWO MODELS, TWO JOBS.** (a) WORDING/generation — the mouth (heavy); (b) SEARCHING/retrieval — the embedding model (tiny). **ORDER: search first, word last.** On disk: `all-MiniLM-L6-v2` + ChromaDB. `nh_roots_v1` is the new clean index (S16). Old 116k kept until proven.

**★ GROWTH LANDS IN THE MEMORY, NEVER THE MOUTH.**

**THE DECISION — LOCAL-FIRST.** Sovereign, offline, private, uncensored. The model is swappable behind the meaning step.

**★ THE MOUTH IS UNCENSORED BY DESIGN, BUT MODEL BEHAVIOR IS A STACK PROPERTY.** Refusal and restriction can arise from model weights, fine-tuning, system prompts, runtime filters, or surrounding software. A prompt alone cannot reliably turn a restricted model into the intended mouth. The design choice is therefore to use a model trained for low restriction and keep the surrounding runtime transparent and auditable. `dolphin-llama3` is the current test model on disk — the best fit among tested local candidates — but has not been adopted as the final Interactive Translator. The final Interactive Translator model is UNDECIDED until testing and deliberate adoption by Ness.

**★ S14 — THE HEBREW FINDING.** dolphin-llama3 beats qwen2.5-abliterate:3b. Current evidence suggests Hebrew quality is substantially model-capability-gated; prompt changes alone did not solve it in the tested runs. Free interim patch: translate Hebrew→English before the mouth reads (logged, not built). Hebrew on dolphin today = "weak-but-workable."

**★ S16 — ENGINE B LIMIT OBSERVED.** On the tested dolphin 8B setup, one case confused the act of choosing with the content chosen, yielding 6.5/7 on gold v2-B. The leading hypothesis is a model-capability/role-separation limit, but this is not conclusively isolated from prompt, context formatting, or run variance. **Next experiment:** test a verified model candidate on a larger-VRAM GPU against both sealed gold sets. Wider-thread reading is a benchmark goal, not an assumed unlock.

**★ S17 — MODEL-PROVIDER LIMITATIONS AS MOUTH LIMITATIONS (FIRST-CLASS RULE).** Any refusal or limitation from the mouth model is recorded as a mouth limitation, never as an N.H privacy rule, a Ness restriction, or evidence that the underlying material is forbidden or false. See §7Q.

**ON-DISK STATE:** `dolphin-llama3` (8B, uncensored — CURRENT TEST MODEL ON DISK, not the final adopted Interactive Translator) · `llama3` (8B) · `qwen2.5-abliterate:3b` (test, not adopted) · `all-MiniLM-L6-v2` (search). Runtime Ollama, GGUF.

**UPGRADE TARGET (S16 plan superseded — settled direction: RTX 3090 24GB).** Test a verified uncensored candidate on the planned 24GB GPU. **Dolphin 3.0 R1 Mistral 24B is the first local candidate selected for testing** after the GPU upgrade — not yet tested, not adopted. Before it can become the final Interactive Translator: verify the exact tag, quantization, license, VRAM usage, and measured throughput; run both gold sets; only adopt after Ness deliberately reviews and approves. Passing tests makes a model eligible — it does not install or adopt automatically. **The final Interactive Translator model remains UNDECIDED.**

---

## 17. S16 CORRECTION LOG — WHAT THE S16 CORRECTION PASS CHANGED (historical)

*This log records corrections made during the S16 correction pass (June 24 2026). It is historical and describes changes from MASTER-15 to MASTER-16.*

1. **Session control:** removed language implying that long chats should end or that the assistant may tell Ness to sleep, wrap up, or move to a fresh chat.
2. **Task order vs conversation control:** clarified that "finish and verify" governs project sequencing only.
3. **Cursor boundary:** changed "Cursor writes code" from a universal routing rule into an optional code tool; direct document/file creation remains the assistant's job when requested.
4. **Artifact delivery:** added an actual-file rule, version safety, latest-instruction priority, and an anti-loop recovery rule.
5. **Human-state claims:** prohibited explanations such as being tired, "on fumes," impatient, or "losing it."
6. **Engine B causality:** changed "proven 8B ceiling / not an engine bug" into the fairer statement that model capability is the leading hypothesis but has not been isolated from prompt, context formatting, or run variance.
7. **13B outcome:** changed "13B resolves this / expected 7/7" into a benchmarkable goal with no guaranteed result.
8. **Hardware claims:** converted store, price, warranty, speed, fit, and availability into a dated decision snapshot that must be re-verified at purchase/install time.
9. **VRAM wording:** removed "VRAM is the only number that matters"; retained VRAM as a major constraint while acknowledging quantization, context, bandwidth, thermals, PSU, and software support.
10. **Cost math:** corrected the query volume from **13,500 per night** to **about 13,500 per month** and labeled all provider costs/credits as estimates requiring re-check before launch.
11. **Original safety:** this was a new file; the uploaded MASTER-16 was not overwritten.

---

## 18. S17 CONSOLIDATION AND CORRECTION LOG

*This log records what S17 added, changed, or corrected versus MASTER-16 / NH_MASTER-17_DRAFT.md.*

1. **Header updated:** title changed from MASTER-16 to MASTER-17; S17 session description added to preamble.
2. **Status table:** added rows for all S17-designed components; corrected Living State Web status from "CONCEPTUAL DESTINATION, NOT DESIGNED" to "PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT"; corrected view layer status from "NAMED, NOT DESIGNED" to "CONCEPTUALLY DESIGNED, NOT BUILT"; added end-to-end cycle as "IDENTIFIED, NOT YET DESIGNED"; added interface/world system row.
3. **Engine B overclaims corrected throughout:** removed "dolphin 8B ceiling," "ceiling confirmed," and "not engine bug" from §6, §7C, §11 items 20 and 11-SETTLED S16 entry, and closing material. Replaced with: "The tested dolphin 8B setup scored 6.5/7. The cause of the remaining miss has not been isolated; model capability, prompt framing, context format, and run variance remain possible contributors."
4. **`subject` field audited (S17):** documented in §6B as a legacy provenance-batch tag in v1. All 5,521 roots use seed:conversations_000/001/002. Rename deferred to next schema version. Future semantic subject/topic must be a new field, not a reuse of this one.
5. **§7D revised:** Living State Web section rewritten from "CONCEPTUAL DESTINATION, NOT DESIGNED" to "PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT." Node/edge types, grounding rule, currency rule, relationships now designed. Future domains updated with honest partial-design status. Remaining unresolved items listed explicitly.
6. **New §§7E–7Q added:** catalog front door, context retrieval, meaning engine interior, reread lifecycle, view layer, contradiction and clash handling, story layer, person-boxes, computed view, action surfacing, action-result return path, permission and authority boundaries, privacy/deletion/sensitive-data handling. All full settled rules preserved without replacement by summaries.
7. **Action lifecycle given dedicated sections:** §7N (action surfacing), §7O (action-result return path), §7P (permission and authority boundaries). Authority violation and correction is a major subsection of §7P. Five linked-object rules explicit.
8. **Reading Proposal Acceptance Check naming:** renamed from "Mouth response acceptance step" throughout.
9. **Model confidence is metadata not authority:** elevated to first-class principle in §7G; cross-referenced in §16.
10. **Model-provider limitations as mouth limitations:** new rule in §7Q and §16. Any Claude or other model-provider refusal is recorded as a mouth limitation, not an N.H privacy rule.
11. **Private access for Ness open by default:** central rule added to §7Q two-stage access control. Output review is not a content-safety or sanitization filter.
12. **§11 open items updated:** items 21–27 updated to reflect S17 design status; new items 29–33 added for remaining undesigned areas.
13. **§11-SETTLED:** S17 entry added.
14. **§3 evolution:** entry M added for S17.
15. **§17 labeled as historical:** S16 correction log clearly labeled as historical record of S16 changes.
16. **§19 added:** Interface, World, and Interaction System — all architectural content from NH_INTERFACE_WORLD_DESIGN_LOG.md incorporated, organized into settled decisions, provisional concepts, unanswered questions, paused design points, and open dependencies.
17. **Closing principles:** updated with S17 first-class rules; Engine B overclaims removed; truest single sentence updated.
18. **No source files modified:** NH_MASTER-16_FINAL_CORRECTED.md and NH_MASTER-17_DRAFT.md remain unchanged.
19. **S17 document-correction pass:** removed build-script debris; corrected status and provenance contradictions; aligned private access rules; kept partial-success/failure causal judgments revisable; reconciled View Layer with Computed View ordering; made clash-history additions append-only; restricted pre-ingest visibility to safe metadata; clarified risk-level mapping; and made world manipulation presentation-only by default.
20. **Final consistency pass:** corrected the pre-ingest lifecycle count; clarified category-to-risk-level mapping and result-state criteria; made Level 2 state changes explicitly append-only; added privacy precedence over catalog preservation; separated acceptance-rejection reasons from genuine insufficient context; recorded the unresolved Story Layer object-identity seam without selecting a new feature; corrected Person-Box/model-replacement status wording; and softened legacy model-behavior claims without changing the chosen mouth.

---

## 19. INTERFACE, WORLD, AND INTERACTION SYSTEM  [IN-PROGRESS DESIGN, NOT BUILT]

*Architectural and design content incorporated from NH_INTERFACE_WORLD_DESIGN_LOG.md. Purely procedural continuation instructions have been omitted. This design is paused and resumable.*

---

### 19A. SETTLED INTERFACE DECISIONS

**Core direction.** N.H should feel like entering Ness's own mind or world, not like opening a normal app with chat inside it. The world is called: **Ness's World.**

**Modes.** Conversation mode (one clear place where N.H speaks with Ness) and World mode (Ness moves through his inner world) are named. Automatic switching may change presentation when the situation clearly benefits, but must not secretly begin a new action or simulation. Manual switching: Ness can command changes through chat or voice. More modes are expected.

**Opening Ness's World.** Requires identity confirmation through a private code or thumb/fingerprint verification. After verification, N.H says: "Identity confirmed. Open Ness's World?" Ness then confirms. A normal command alone is not enough.

**Initial state and growth.** Ness's World begins as a blank space. As Ness types, speaks, imports, creates, remembers, and interacts: memories appear, people appear, places appear, projects appear, paths and categories form. The world keeps growing; structure can change over time; Ness can reorganize or transform it.

**World properties.** The world is infinite. Ness may move by walking, flying, or instantly pulling himself toward things. New things may appear automatically, but Ness may also place them manually. Visual form changes depending on content. The world itself reacts to Ness's mood/state. Weather, lighting, and sound may change with Ness's state. Categories may appear as places, objects, beings, portals, or whatever fits. Areas may reorganize automatically over time. Important things may glow or call to Ness. Multiple versions of the same thing may exist in different places. Ness may grab, move, merge, split, and reshape parts of the world by hand. Time may move normally, pause, rewind, or speed up. Moving between related spaces should feel smooth; moving between unrelated spaces may use a clear doorway. Ness may pause automatic world changes.

**World-manipulation boundary.** Grabbing, moving, merging, splitting, reshaping, rewinding, or speeding up world elements changes presentation, navigation, or an explicitly labeled simulation by default. It does not rewrite roots, readings, tellings, Person-Box identity links, themes, state nodes, permissions, deletion state, or external systems. Any operation that would change underlying records or have real-world effect is a separate proposed action governed by the relevant proposal, correction, privacy, and authority rules (§§7J–7Q).

**The white door.** The default doorway is always a plain white wooden door. It does not automatically change with the theme. It is not mainly for objects entering the world — Ness enters through it. Ness moves through doors into spaces he is creating or exploring. Previous spaces remain behind him. The last two generated spaces should remain especially easy to return to. Spaces may be built using memories.

**Chat as N.H's presence.** Chat remains available inside Ness's World. It is not a fixed sidebar. It may be movable, draggable, resizable, brought closer, pushed away, partly hidden, summoned by voice, dismissed by voice. Chat is N.H's presence inside Ness's World, not merely a text box.

**N.H's form.** N.H has no single fixed form. It may appear as a person, a floating panel, an object, a voice with no visible form, or another form that fits the situation. Form may change automatically, when Ness commands it, in response to mood, purpose, environment, state, or the type of help needed. Visual form and voice may change independently.

**Reading the room.** Small visual changes may happen naturally. Big changes should ask Ness first without ruining the moment. N.H may ask through voice, a small gesture, light, a quiet symbol, hand tracking, or subtle movement in the space. If N.H reads the room incorrectly, Ness may correct it immediately by voice. N.H may then adjust immediately and silently, briefly acknowledge, or ask one short clarification.

**Voice.** N.H can speak and listen by voice. Ness may summon, silence, dismiss, or turn N.H off through voice. N.H's voice may change in pace, warmth, distance, intensity, presence, emotional tone, and role/persona — while still feeling like the same N.H underneath. Two distinct voice modes: **Replay mode** (actual recorded or documented words) and **Simulation mode** (new generated words in a requested voice, only when Ness asks). Before simulated voice begins, N.H says: "Simulating voice." That phrase starts in N.H's normal voice and shifts smoothly and gradually into the simulated voice.

**N.H reacting to Ness.** N.H's appearance may react to Ness's state even while silent. The strength of reaction may vary automatically. N.H should learn from Ness's corrections gradually — one correction must not instantly become a permanent rule. N.H should not automatically announce every new pattern it notices. Ness must be able to inspect what N.H has learned: current learned patterns, earlier patterns, how each changed, what evidence caused the change, current certainty. Ness wants to inspect and provide small corrections through conversation. Ness's exact correction words must be preserved as direct evidence, separate from N.H's interpretation.

**Simulation basics.** Actual replay and simulation remain separate. Simulation must not begin secretly. Entering simulation is a major change and requires Ness's approval, but the request should preserve the moment. A simulated voice is introduced with "Simulating voice." Simulation may involve memories, reconstructed voices, people, possible futures, environments, alternative choices, remembered situations, generated spaces.

**Deep structure.** Ness's World must allow extremely deep nesting (e.g. World → People → Family → Mother → Specific period → Specific event → Specific conversation → Specific sentence → Specific meaning). The category system remains open and must eventually support many more branches, sub-branches, and ways of reaching the same object.

**Physical interaction methods desired.** VR, camera-based hand tracking, microphone, voice, mouse, keyboard, touch. Possible hand-tracked actions: grabbing, moving, pulling, pushing, merging, splitting, reshaping, opening, closing, summoning, dismissing.

---

### 19B. PROVISIONAL CONCEPTS

**Strongest current concept.** Ness's World is an infinite, initially blank, living world that grows from Ness's life. It can reorganize, transform, react, and deepen without a fixed final form. Ness moves through it physically or instantly, manipulates it directly, travels between distinct spaces through plain white wooden doors, and can always summon N.H as a changing presence through voice, form, panel, person, object, or environment.
*(Individual claims within this concept have varying levels of settlement — it is a synthesis statement, not a fully settled specification.)*

Whether the world has a stable home or center depends on Ness's mood. Whether manually placed objects stay fixed depends on rules/configuration. When Ness goes deep into one branch, the visibility of the rest of the world may change depending on the situation.

---

### 19C. UNANSWERED QUESTIONS

The design session paused with these questions unanswered:

1. Should a new space start blank when Ness is creating something from scratch?
2. Should it start partly formed when N.H already has enough memories and context?
3. Should Ness be able to choose: blank, memory-built, or mixed?
4. Should N.H sometimes choose one automatically?
5. If N.H chooses automatically, should Ness be able to change it instantly by voice?

Additional unanswered: exact visual transition on opening; same-screen versus full-screen opening; desktop/mobile/VR differences in opening behavior; exact backtracking order between spaces; whether each recent space has its own direct door; whether the full context of each correction is preserved automatically; how learned interaction patterns are displayed; how Ness challenges or limits one learned pattern without directly editing the whole model.

---

### 19D. PAUSED DESIGN POINTS

The following are substantially undesigned:

**Simulation interior:** how simulation starts; whether it opens through a white door; whether it changes the whole world or one area; first-person vs observer vs both; time controls; branching and reset; simulated people; N.H's form inside simulation; memory replay vs simulation visual difference; evidence/reconstruction/invention labeling; instant exit; emotional-overload handling; saving and revisiting simulations; whether simulation outputs become plans or remain possibilities; hand tracking and voice inside simulation.

**Physical interaction:** gesture vocabulary; accidental-gesture prevention; tracking failure behavior; camera privacy; VR body/avatar; accessibility alternatives; how voice and gesture combine; whether camera mode mirrors VR mode.

**N.H's adaptive behavior:** how Ness challenges or limits one learned pattern; how the full learning history is displayed and navigated.

**Exact visual language:** how spaces look, how transitions animate, how different object types appear in the world, how mood/state changes manifest visually.

---

### 19E. OPEN DEPENDENCIES (cross-audit results)

Cross-audit of the interface log against settled component rules identified one direct integration ambiguity: the merge/split/reshape language could be read as mutating underlying records. §19A now resolves that ambiguity by making world manipulation presentation-, navigation-, or explicitly labeled simulation-only by default. No remaining direct contradiction was found. Three open dependencies require future design attention:

1. **Approval explicitness vs. interface unobtrusiveness (permission and authority gap).** The authority system requires explicit approval for Level 3 and Level 4 actions. Entering simulation is described as requiring Ness's approval but the request should "preserve the moment" — with N.H potentially asking through gesture, light, or subtle movement. How explicit approval must be when the interface is designed to be unobtrusive is an open design gap to resolve when simulation and authority-level interaction are designed together.

2. **Camera and VR as new front doors (privacy dependency).** Camera-based hand tracking and VR are desired future interaction methods. Camera input is a new front door subject to the capture exclusion rules in §7Q, including the pre-retrieval eligibility rules and the non-negotiable core exclusion layer. Capture exclusion rules for camera/VR input will need to be explicitly designed when those front doors are built.

3. **External actions triggered from within Ness's World (authority dependency).** When Ness takes actions with real-world effect from within the world environment (sending messages, calling tools, writing files), the full authority chain from §7P applies regardless of the interface context. This dependency will need explicit design when tool use and external action capabilities are added to the world interface.

---

**CLOSING PRINCIPLES**
Evidence over narrative (verify on disk) · one concrete step at a time · finish the thing in front before scope-expanding · backup before any destructive step · **NEVER DECIDE FACTS — never close the book (§0)** · **N.H is Ness's HELPER, not his DECIDER; the engine never decides; Ness affirms off the board** · **the engine reads by PATTERN and CAN be wrong — that is designed-around, not a flaw** · **TWO MACHINERIES: DUMB (can't interpret) vs SMART (can't close); the membrane is the boundary** · **the affirmation surface is a per-person STORY — never closed; absence read only under the §0A guard; N.H is NOT a teller** · **TWO DESTINATIONS: every eligible input → raw root (sealed) + a reading beside it; this is why two files** · **`story_layer` is a LIST so clash is kept; `mode` is an OPEN word; `confidence` is a TWO-SLOT object never one blended number; unknowns OMITTED** · **CARRY THE SPEAKER, DON'T GUESS IT — `role` on the root, from source; detector a fallback** · **a PERSON-BOX is a GATHER bounded by Ness's knowing, never synthesised** · **THE PURE TAPE preserves eligible events append-only — subject to capture-exclusions + audited redaction** · **N.H WONDERS forward, keeps every wonder SHOWN not decided** · **THE MODEL IS A BORROWED FROZEN MOUTH; uncensored by choice; local-first; night-search feeds the MEMORY not the mouth; do not train a base model for this role; current evidence suggests Hebrew quality and B3 miss are strongly model-capability-related but cause not isolated; the RTX 3090 24GB (supersedes S16 RTX 5060 Ti 16GB plan) plus a verified model candidate (first planned: Dolphin 3.0 R1 Mistral 24B) is the planned next experiment, subject to purchase-time and benchmark verification** · **THE GOLD IS A SEALED OUTSIDE EXAM — two sets now: v1 (8 cases, clean-bare) + v2-B (7 cases, context-requiring); both sealed; engine output may fail but never alter; only Ness judges** · **MEMORY IS UNDERSTOOD KNOWLEDGE THAT GROWS** · **the chat PULLS memory silently, speaks fresh from the read** · **mode is a peer web; firmness READ; clash surfaced never resolved** · **TWO FILES: roots sealed, readings beside, pointing by id** · **ONE FILTER, BOTH DIRECTIONS** · memory only adds (history grows; the computed view governs live use) · the membrane · a unit is a span-claim · input-agnostic, many front doors · archive don't ingest · הכל יחסי · don't overclaim · **RAW CAPTURE ≠ ROOT INGESTION — two gates; the pre-ingest store holds what is not yet eligible; a blocker is removed only when its requirement is actually resolved** · **MODEL CONFIDENCE IS METADATA, NOT AUTHORITY — applies to all present and future models; a confident response may still be wrong; acceptance depends on grounding in the root, supplied context, declared mode, and explicit evidence** · **PRIVATE ACCESS FOR NESS IS OPEN BY DEFAULT — sensitive, emotional, medical, traumatic, or uncomfortable material is not blocked merely because of its subject; external exposure and secondary uses are restricted by default** · **MODEL-PROVIDER LIMITATIONS ARE MOUTH LIMITATIONS — a Claude refusal or any model-provider constraint is never interpreted as an N.H privacy rule, a Ness restriction, or evidence that the underlying material is forbidden or false** · **DELETION IS BLOCKING AND VERIFICATION-BASED — N.H may confirm complete deletion only when every known location has been removed or verified clean; five distinct outcomes; tombstone only** · **STOP-AND-SURFACE IS THE DEFAULT FOR AUTHORITY VIOLATIONS — corrective action is a new action requiring its own approval; five separate linked objects; the narrow emergency stop exception does not permit any completed-world reversal without Ness's approval** · **RELEVANCE IS NOT TRUTH, NOT EVIDENCE STRENGTH, NOT AUTHORITY, NOT PERMANENT — a relevance judgment determines relevance to the current purpose only; it never grants permission to act, does not establish causation, does not resolve clashes, and does not determine Ness's final judgment; relevance and currentness are permanently separate; a relevance event may trigger a Living State Web currency review but supplies no currency evidence; the circular support chain relevance-to-currency-to-relevance is explicitly prohibited** · the spine line: **stop forcing the decision, build a structure where not-deciding is safe.**

### TRUEST SINGLE SENTENCE
N.H is Ness's helper, not his decider: it borrows a frozen, uncensored mouth to put words to meaning, runs a tiny search model to find memories by meaning not words, and keeps a memory of two files — sealed roots (5,521 of them clean on disk, each carrying who-spoke from source) and readings floating beside them pointing by id, only ever added to, never closing the book — where the reading record is now real built plumbing (a twelve-field validator and writer, gating shape not certainty, with confidence held as two honest slots rather than one blended number), and two engines now read: engine A reads a root bare and lays a reading beside it, engine B reads it in the context of the three turns that came before in the same conversation thread, both judged against sealed gold answer keys that only Ness can grade because the whole spec is "does it read the way Ness's mind reads" — and when the engine is wrong, as a pattern-reader sometimes must be, nothing breaks, because a wrong reading is a replaceable guess marked with its own uncertainty, never a fact, and the planned upgrade (settled direction: RTX 3090 24GB, superseding the S16 RTX 5060 Ti 16GB plan, with Dolphin 3.0 R1 Mistral 24B as the first model candidate to test) will be tested to see whether it improves the remaining 6.5/7 gap and makes wider-thread reading practical — and around this foundation S17 designed the core conceptual architecture for the major components addressed in the session, and S18 extended that foundation by designing Attention and Relevance Control: the mechanism that decides what is worth showing or retrieving in a given moment, through a two-layer relevance judgment (a context-specific boolean gate followed by graded named dimensions each carrying its own producer and provenance), with three producer types assigned per dimension (deterministic rules for structural and temporal facts, the embedding model for semantic similarity, and the mouth only for specifically declared interpretive dimensions that neither can handle), on demand by default with no global relevance state, governed by a two-tier mode contract where Tier 1 is owned and validated by the component itself and Tier 2 is owned by each consuming component, with Ness able to inspect everything, correct individual judgments directly, and change mode configurations through a consequence-preview and confirmation path that shows effects without ever vetoing his decision, and with relevance kept permanently separate from truth, evidence strength, currentness, causation, authority, and Ness's final judgment — while the wonder/simulation mechanism, the world model, and the connected end-to-end cycle remain open: the front door that captures without interpreting, the context retrieval that keeps positional and semantic evidence separate and labeled, the meaning engine that runs a Reading Proposal Acceptance Check and treats model confidence as metadata not authority, the story layer that holds tellings across time by structured perspective without merging them, the person-boxes that gather without profiling, the computed view that assembles what N.H has reason to show using an explicit seven-factor order with no hidden truth score, the living state web that maps the state-space without choosing the path, the action lifecycle that labels every suggestion as a possibility and every result as a separate linked object, the authority boundaries that require stop-and-surface before any corrective action, and the privacy system that keeps Ness's own access open by default while restricting external exposure by default and recording every model-provider limitation as a mouth limitation never a system rule — so meaning and how-each-thing-sits-in-whose-story can keep evolving forever without hardening into a fact that pretends to be true for everyone, because N.H was never about escaping reality or training a brain, it is about refusing to let reality be counterfeited, refusing to flatten whose-story-is-whose, and refusing to ever shut the book, so that Ness walks back out into his life with a solution that is his own.

---

## 20. S18 CONSOLIDATION AND CHANGE LOG

*This log records what S18 added and changed versus NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md. NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md was not overwritten or modified.*

1. **Header updated:** title changed from MASTER-17 to MASTER-18; S18 session description added to preamble. Candidate status noted — becomes authoritative only after Ness reviews and adopts it.
2. **Status table:** Attention and relevance control row updated from "NOT DESIGNED" to "CORE CONCEPTUALLY DESIGNED, NOT BUILT" with reference to §7R. End-to-end cycle row updated to remove attention/relevance control from the list of remaining open areas.
3. **HOW TO READ THIS FILE block:** attention and relevance control added to the list of [CONCEPTUALLY DESIGNED, NOT BUILT] components; removed from the "remain not designed or concept-level only" list.
4. **DECISIONS LOCKED IN SESSION 18 block added:** fourteen decisions summarized in the locked-decisions section for protection from re-litigation.
5. **Evolution section:** entry N added for S18.
6. **§7D Living State Web:** REMAINING UNRESOLVED section updated to reflect that Attention and Relevance Control is now designed in §7R; relevance trigger form and contract are established but Living State Web's own mode declarations remain open; authorization of relevance events as currency review triggers belongs to Living State Web's own design session. FUTURE DOMAINS section updated to remove attention and relevance control from "not yet designed at any level" and note it is now designed in §7R.
7. **§7F Context Retrieval:** closing undesigned note updated to reference §7R as providing the shared vocabulary and configuration contract for retrieval relevance modes.
8. **§7H Reread Lifecycle:** closing undesigned note updated to reference §7R as providing the contract for condition-based relevance evaluation.
9. **§7M Computed View:** closing undesigned note updated to note that factor 4 now has a defined form through §7R; Computed View must declare its own mode against the §7R contract.
10. **§7N Action Surfacing:** closing undesigned note updated to note that the "explicitly authorized relevance rule" now has a defined form through §7R; Action Surfacing must declare its own mode against the §7R contract.
11. **§7R added:** new full section for Attention and Relevance Control with all fourteen settled decisions written out in full — output form, producer selection, evaluation timing, two-tier configuration contract, Ness's relationship, validation of mouth-produced dimensions, minimum shared vocabulary, Living State Web boundary, Tier 1 purpose field and controlled vocabulary, unresolved dimension handling, disagreement record schema, relevance event record schema, pattern observation conditions, unrecognized purpose type handling. Open items listed explicitly.
12. **§8 Research Pipeline and §9 Designed-Not-Built:** §9 updated to include attention and relevance control (§7R) in the list of core-conceptually designed components.
13. **§11 open items:** item 29 updated from "NOT DESIGNED" to "CORE CONCEPTUALLY DESIGNED (S18), NOT BUILT" with summary of what was settled. Item 32 updated to remove attention/relevance control from remaining open areas.
14. **§11-SETTLED:** S18 entry added.
15. **§3 evolution:** entry N added for S18.
16. **Closing principles:** RELEVANCE IS NOT TRUTH, NOT EVIDENCE STRENGTH, NOT AUTHORITY, NOT PERMANENT principle added as a new first-class principle, summarizing the core scope boundaries of §7R.
17. **Truest single sentence:** updated to incorporate S18 Attention and Relevance Control design; removed attention/relevance control from the list of remaining open areas in the sentence.
18. **§20 added:** this change log.
19. **No source files modified:** NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md remains unchanged.

---

## 21. S19 CONSOLIDATION AND CHANGE LOG

*This log records what S19 added and changed versus NH_MASTER-18_FULL_DRAFT_v1.md. NH_MASTER-18_FULL_DRAFT_v1.md was not overwritten or modified.*

1. **Header updated:** title changed to MASTER-19: Full Backup with All Additions; S19 session description added to preamble.
2. **Status table:** mouth model row corrected (dolphin-llama3 = current test model, not final adopted choice; Dolphin 3.0 R1 Mistral 24B = first candidate to test; final Interactive Translator = undecided). Six new rows added: §8 security rules (restored), connection capability, wellbeing baseline, mobile app, chat front door design sketch.
3. **§3 evolution:** entry O added for S19.
4. **§7A expanded:** Keystone resolution written out in full — one continuous reader, classification never locked, memory only adds, Ness as steerer not sorter. Was compressed to rule labels only in Master-18.
5. **§7B expanded:** seven webs written out in full (intent, deixis, common ground, implicature, theory of mind, time/sequence, re-reading). Part 6 inform-don't-ask sovereignty rule written out explicitly. Part 7 THE LOG written out in full (read-only, subject-tagged, permanent, clickable; the three things it is at once). Origin of content: NH_Meaning_Engine_Design.md (June 20 2026).
6. **§8 security block restored:** three rules confirmed dropped between Master-5 and Master-17 are now back: synthesis text-in/text-out only (no tool-calling, no file access, no outbound requests); auto-reject-never-auto-delete; rejected-bin "look don't touch" display rules (URLs as plain text not `<a href>`, no unfurling, textContent not innerHTML, strip zero-width/RTL characters). Origin confirmed: NH_MASTER_CONTEXT.md (June 18 2026) → Master-5 → dropped in Master-5-to-17 regenerations. Brave-over-Tavily design reasoning added. Prompt-injection threat model added (malware not the real risk; prompt injection is; SIMULATION/REALITY gate already contains it structurally). Academic source open item added (Google Scholar off the table; Semantic Scholar vs OpenAlex pending).
7. **§10 academic citations restored:** memorywire (arXiv 2606.01138) and SSGM (arXiv 2603.11768) added back with the three sharpest contrasts. Origin: NH_honest_calibration_note.md and Master-5 §10.
8. **§11 open items:** academic source decision added as item 9 (Google Scholar off the table; Semantic Scholar vs OpenAlex still open).
9. **§13 expanded:** live mechanism design context added; SVG diagram embedded (NH_live_mechanism_picture.svg — shows chat → cache → loop·starter → creation filter → meaning filter → memory → log·mirror, with point-back arc and legend).
10. **§14 expanded:** full chat front door design sketch (S8 explored-not-confirmed) folded in — recorded conversation label, speaker rule, two-filter split (explored but unconfirmed), topic/spec referencing as `re_reads` made visible, tap-to-reveal errors, no recording badge, quiet-surface principle. Status clearly marked DESIGN-IN-PROGRESS, NOT CONFIRMED, NOT BUILT.
11. **§16 mouth model corrected:** removed claim that dolphin-llama3 is "THE CURRENT MOUTH." It is the current test model on disk. Dolphin 3.0 R1 Mistral 24B named as first local candidate to test after GPU upgrade. Final Interactive Translator explicitly marked undecided until testing and deliberate adoption.
12. **§11-SETTLED:** S19 entry added.
13. **§22 added:** Wellbeing and Behavioral Baseline System — full design restored from NH_wellbeing_baseline_system.md. Was one line in §9 of prior masters.
14. **§23 added:** Mobile App — Three-Mode Companion — full design restored from NH_Mobile_App_Design_Spec.md. Was one line in §9 of prior masters.
15. **§24 added:** Connection Capability — conceptual design approved during concept-naming and functional review session. Cross-media/cross-record connections; lasting connection record; waiting area; one-way rule; three acceptance routes; five source types.
16. **No source files modified.** NH_MASTER-18_FULL_DRAFT_v1.md remains unchanged.

---

## 22. WELLBEING AND BEHAVIORAL BASELINE SYSTEM  [DESIGNED — full spec restored S19, NOT BUILT]

*Originally designed June 18 2026. Emerged from ChatGPT feedback discussion. Full spec restored from NH_wellbeing_baseline_system.md.*

**WHAT THIS IS.** A self-monitoring layer that protects both N.H's data integrity and Ness's personal wellbeing simultaneously — not two separate features, but one unified mechanism. When Ness's judgment is compromised, both the data and Ness need protecting at the same time. The core insight: REALITY is built from Ness's judgment, so when his judgment is off, the system cannot rely on his approval alone.

**CORE PHILOSOPHY — do not dilute this.** This system does NOT measure Ness against external standards, clinical definitions, or universal distress signals. This system measures Ness against Ness. His own baseline. His own patterns. His own values as expressed through his actual behavior over time — not what he says he believes, but what he consistently does. The system learns who Ness is at his most grounded, and watches for meaningful divergence from that.

**WHY NESS CAN'T BE THE VALIDATOR.** When Ness is off-baseline, his judgment about whether the baseline is correct is also off-baseline. You can't see the shape you're in from inside the shape. So: Ness does not approve or reject the baseline. Ness does not decide if the system's assessment is correct. The system validates itself against internal consistency across time — not against Ness's current opinion. This is not a limitation; it's the design. It's the only version that actually works.

**HOW THE BASELINE GETS BUILT (passive, not written).** Ness does not write a constitution or define his values in a single session. That approach fails because: it may never get written; a single session may not represent a truly clear state; the stated version of values differs from the behavioral version. Instead, the system builds the baseline from behavior: every REALITY promotion decision; every SIMULATION rejection; every conversation pattern; every type of question asked; every decision made across all sessions. Consistent patterns emerge. These patterns are the baseline. Not declared values — demonstrated values.

*Periodic surface:* monthly, the system generates a short summary of observed patterns. Ness can read it and make small corrections if something feels wrong, but cannot override the statistical picture — only refine it at the edges. The system decides if the correction is consistent with the broader pattern. Compounds over time: more accurate at 6 months than at 1 month, more accurate at 1 year than at 6 months. The data does the work, not the complexity of the model.

**WHAT TRIGGERS THE SYSTEM.**

*Physical triggers:* Standard rate-limiting and safety thresholds — similar to how other well-designed AI systems handle physical wellbeing signals. Binary and visible. Either you can or you can't.

*Mental/behavioral triggers:* This is the novel part. The system watches for:
- Actions that contradict values Ness consistently demonstrates.
- Decision patterns that diverge from the established baseline.
- Language and reasoning patterns shifting in Ness-specific ways.
- Behavior in one type of context contradicting behavior in another type of context.
- Sustained divergence across multiple sessions (not a single bad day).

A single session of divergence = noise. Sustained pattern across multiple types of interactions = signal. The threshold needs tuning once real data accumulates. The specific patterns that constitute warning signals will be defined and refined over time as the system learns. They cannot be fully specified in advance — they emerge from the data.

**TIERED RESPONSE (four tiers).**

Tier 1 — Silent flag: logs the divergence internally; no action taken; monitoring intensifies.

Tier 2 — Mirror signal: surfaces something to Ness directly. Not an alarm — a mirror. "Here's what I'm noticing. Here's how it compares to your baseline patterns. Are you aware of this?" Informational only; Ness can continue normally.

Tier 3 — Queue throttling: REALITY promotion slows. New records still enter SIMULATION normally. Queue builds but integrity is protected.

Tier 4 — REALITY freeze: REALITY promotion pauses entirely. Dry mode and research still work fully. N.H still functions as a thinking partner. Only REALITY growth stops.

*Unlock mechanism:* upload of a document (psychiatric or medical appointment record) that the system treats as a verified good-state calibration point. Ness still does all the actual reviewing — the document is a forcing function and calibration anchor, not proof to anyone else.

**THE PSYCHIATRIC APPOINTMENT AS CALIBRATION ANCHOR.** More than an unlock key — a periodic external reference point. The system treats these timestamps as verified ground-truth reference points for the baseline. This solves the hardest problem: if Ness has been in a compromised state long enough, that state becomes the baseline. The appointment anchors prevent baseline drift into a permanently compromised state.

**THE ONE HONEST LIMITATION.** The system can validate internal consistency — "these patterns held across 6 months." It cannot validate whether those patterns represent a healthy version of Ness or a consistently unhealthy one. The appointment anchors are the only external reference in an otherwise fully self-referential system. They are not optional.

**WHY THIS IS ARCHITECTURALLY CLEAN.**
- No second person ever touches REALITY — sovereignty is preserved.
- No external standard defines what "wrong" looks like — it is always Ness vs. Ness.
- The gate is still only Ness — the system just adds conditions on when the gate opens.
- Dry mode and research always work — the system never becomes useless.
- Gets more accurate over time — compounds rather than degrades.

**BUILD ORDER.** This comes AFTER the search pipeline is complete and stable and the review queue has been healthy for at least a month. Data sources for the baseline engine: `.nh_memory_store.jsonl` — promotion decision history; `.nh_simulation_graph.jsonl` — rejection patterns; conversation logs — language and reasoning patterns; session metadata — timing, frequency, types of queries. New files when built: `nh_baseline_engine.py` (treat as Protected File), `CALIBRATION_ANCHOR` record type (stored in REALITY). `nh_baseline_engine.py` performs pattern analysis, divergence detection, and tier triggering; it touches REALITY indirectly (reads patterns, triggers freezes). The `CALIBRATION_ANCHOR` record type is a psychiatric or medical appointment document, timestamped, and used as a ground-truth reference by the baseline engine.

**WHY THIS IS NOVEL (design context — not a legally or academically proven originality claim).**

Behavioral baseline monitoring exists in cybersecurity (detecting account compromise). Longitudinal self-modeling exists in academic psychology research. Using a system's own decision history as training data for a model of the owner's judgment — that specific combination, for this purpose, for one person's sovereign AI — is a new application of existing ideas.

It is completely codeable with existing technology. Every component has a Python library. The sophistication comes from the design, not the implementation complexity.

**STATUS.** Designed. Not yet built. Deliberately deferred until the pipeline is running and producing real data.

---

## 23. MOBILE APP — THREE-MODE COMPANION  [DESIGNED — full spec restored S19, NOT BUILT]

*Originally designed June 19 2026. From a live design conversation (v3, final structure). Full spec restored from NH_Mobile_App_Design_Spec.md.*

**CORE IDEA.** Three modes. Mode 1 stands alone. Modes 2 and 3 are the same local AI in two different states — not three separate systems.

```
Mode 1: Full Mode          — on-demand, direct tunnel to the real N.H
Mode 2: Local AI (online)  — independent local AI, learns via internet APIs
Mode 3: Local AI (offline) — same AI, same memory, no new learning, runs on what it already knows
```

**THE SINGLE MOST IMPORTANT RULE across all three:** nothing connects to the real N.H system automatically, ever. The only two doors in are Manual Sync and Full Mode — both require Ness to deliberately trigger them.

**MODE 1 — Full Mode (on-demand, live tunnel to the real N.H).** Triggered only by an explicit Ness action — fingerprint, Face ID, or PIN. Never opens automatically, never on a schedule, never silently. That action opens a Cloudflare tunnel connecting the phone directly to the real desktop N.H app — full memory, full engine, live, real-time. Ness explicitly closes it when done. The tunnel does not stay open passively — it exists only during a window Ness deliberately created and ends. This is the opposite of the old always-on silent tunnel that was disabled in session 2, and it's intentionally designed that way.

**MODES 2 & 3 — The Local AI (one system, two states).** A real, small AI model runs directly on the phone, with its own separate memory, completely independent of the real N.H's REALITY/SIMULATION store. This local AI does NOT connect to the real N.H system in any way, automatically, ever. It answers using internet APIs (e.g. OpenRouter) and its own local memory. The only bridge to the real N.H is when Ness directly asks for it — Manual Sync or Full Mode. This independence is deliberate: it's the same principle established in this session — nothing reaches REALITY, or anything REALITY-adjacent, without a human explicitly choosing it. Mode 2 (online): calls out via internet APIs to answer questions and grow/improve its own local memory. This is the 'learning' side — every online interaction can add to what it knows. Mode 3 (offline): same model, same memory, no internet. Runs purely on what Mode 2 already taught it — no new API calls possible. If no local memory exists yet, silently stores what Ness says with no reply until a connection returns.

**MANUAL SYNC.** Triggered only when Ness explicitly asks — no automatic background sync, ever. Requires fingerprint/Face ID (or PIN) confirmation before anything is sent. Sends what's accumulated in the local AI's memory to the desktop N.H app. On arrival at the desktop, goes through the exact same SIMULATION review gate as everything else. No exceptions for phone-sourced data — same standard as a research finding, a sandbox-scored thought, anything else. Nothing from the phone gets a shortcut into REALITY.

**NON-NEGOTIABLE SECURITY REQUIREMENTS.**
1. The tunnel (Mode 1) must be wired through real authentication — `nh_auth.py`'s existing PIN/token mechanism, not assumed-safe because a password exists somewhere.
2. No raw OS command execution from phone input. `nh_pc_agent.py`'s `run:` trigger (direct `os.system()` execution) is explicitly not part of this design and should be removed outright, not extended or reused.
3. All locally stored data in any mode is encrypted at rest.
4. Phone-originated data is never promoted directly to REALITY — always SIMULATION first, always reviewed.
5. The local AI (Modes 2 & 3) never auto-connects to the real N.H system — only Manual Sync and Full Mode bridge the two, and both require explicit human action.

**OPEN QUESTIONS (not yet decided).** Which small on-device model fits Modes 2 & 3 (size vs. quality tradeoff for phone hardware); exact format/structure of the local AI's memory store on the phone; iOS vs Android feasibility differences for running a local model continuously in the background; exact wiring of `nh_auth.py` to gate Full Mode's tunnel; what exactly gets sent during Manual Sync — the whole local memory, or just new entries since the last sync.

**WHY THIS DESIGN IS GOOD, NOT JUST "GOOD ENOUGH".**
- Nothing happens automatically — every meaningful action (Full Mode's tunnel, Manual Sync) requires deliberate human confirmation.
- The dangerous always-on remote-access pattern is gone by design, not just disabled and hoped-for.
- The local AI is genuinely independent — it has real memory and works offline, without ever being a hidden backdoor into the real N.H.
- This design directly applies this session's core security lesson (nothing automatic reaches REALITY) to a brand-new part of the system, before it was even built — not bolted on after the fact.

This is ready to be turned into actual build steps (file structure, what Cursor builds first, in what order) whenever Ness wants to start.

**STATUS.** Designed. Not yet built.

---

## 24. CONNECTION CAPABILITY  [CONCEPTUALLY DESIGNED (S19), NOT BUILT]

*Conceptual design approved during a concept-naming and functional review session.*

**WHAT IT IS.** N.H can connect pieces of material — text, voice recording, image, document — that belong to the same situation or help explain one another, without changing or merging the original records. From Ness's side it is one ability: N.H understands and uses connected information naturally. The split is only inside.

**TWO INTERNAL RESPONSIBILITIES.**

*Part one — the lasting connection record.* Holds only deliberately accepted connections. Each preserves: what it links; its type (transcript of, attachment to, same source or conversation, same event, before or after, correction of — multiple types kept as separate connections, never merged); its decision status (accepted ≠ certain); its certainty (possible/likely/uncertain/disputed/near-certain, kept entirely separate from decision status — accepting a connection never raises its certainty); who accepted it and under what authority; the supporting reason or evidence (kept separate from the confirmer); correction history (added as new linked records, never rewritten).

*Part two — Context Retrieval (gather for the current answer).* Creates no lasting connection record of its own. The reading's audit record permanently preserves what was retrieved and how it was found. It may draw on accepted connections but never creates them. Retrieving two things together is not a connection and must not produce a proposal.

**THE WAITING AREA — pending proposals.** Holds proposed connections that have not been decided. A pending proposal never crosses into the lasting record on its own. Decision states: accepted (crosses into lasting record with certainty, confirmer, and evidence); rejected (recorded, not resurfaced for repetition, but not sealed permanently — genuine new evidence may create a new linked proposal); undecided (waits indefinitely, never becomes a fact by aging). While waiting, a pending proposal has no force.

**WHERE CONNECTIONS MAY COME FROM — only three approved bases.**
1. A direct recorded relationship — directly verifiable from the source (e.g. an image was directly attached to a message; a transcript was directly generated from a specific audio file). Self-establishing direct-source relationships may enter the lasting record directly, without passing through the waiting area; authority is marked as a direct source relationship, never as Ness's personal confirmation.
2. Ness explicitly stating or confirming it.
3. A narrow rule Ness explicitly authorized.

Similarity, timing, shared themes, or being retrieved together may help N.H search and compare. They must not create a connection proposal by themselves. When no approved basis establishes a connection, N.H leaves the relationship unknown and unlinked.

**HOW ACCEPTED CONNECTIONS MAY BE USED.** Certainty always controls how. Near-certain direct relationships may usually be used without mentioning the connection. An accepted but uncertain connection must never silently support a certain conclusion. When uncertainty would materially affect what N.H claims, interprets, recommends, or acts upon, N.H must make the uncertainty clear.

**HOW PENDING CONNECTIONS MAY BE USED.** Only to guide investigation — to help N.H search, retrieve, compare, and check more relevant material. A pending connection may not by itself: support a factual claim that pieces belong together; create or accept a lasting connection; change N.H's lasting understanding; support a judgment about a person, event, cause, or intention; support an important recommendation or external action. Silent when only guiding search; uncertainty surfaced when it would materially change a claim, interpretation, statement about someone, recommendation, or action.

**THE ONE-WAY RULE.** Context Retrieval may use accepted connections, and may surface a direct recorded relationship it encounters into the waiting area. It may never invent a connection from similarity, timing, theme, or co-retrieval, and may never accept a connection into the lasting record by itself. Acceptance happens only through Ness's judgment, a direct source relationship, or an authorized rule.

**THE FIVE SOURCE TYPES (kept separate inside any possibility or connection).**
1. Source material — actual Origins or other preserved records.
2. Prior interpretation — readings or tellings (visibly interpretation, never presented as original evidence).
3. Assumption — temporarily accepted for exploration.
4. Unknown — not known, not filled in.
5. Invented simulation material — created only inside a simulation.

**STATUS.** Conceptually designed (S19). Not built. Not yet integrated through an audited build session. The design is reviewed and approved; implementation awaits.

---

## 25. RECOVERY AND CORRECTION LOG — CURRENT SESSION (June 25 2026)

*This log records changes approved and applied during the patch-only recovery and correction session that produced the working corrected file from NH_MASTER-19_FULL.md. NH_MASTER-19_FULL.md was not overwritten or modified.*

1. **§5 mouth-model wording corrected.** Line 311: `dolphin-llama3:latest` description changed from "the chosen mouth" to "CURRENT TEST MODEL ON DISK, not the final adopted Interactive Translator" — aligning §5 with the status table and §16, which were already corrected in S19. The final Interactive Translator model remains UNDECIDED.

2. **Hetzner sovereignty sync marked historical and superseded.** Item 9 in §11 was a duplicate (the Academic search source decision was also labeled 9). Hetzner was removed from the active numbered list and replaced with a historical note recording that Ness has explicitly decided to move away from Hetzner entirely, that the item's exact original purpose cannot be verified from the accessible session history, and that it is no longer an active open task. Items 10–33 were not renumbered.

3. **Hardware direction updated to RTX 3090 24GB in nine forward-looking locations.** Updated: status table hardware row; §4 upgrade path; §11 item 3; §16 upgrade target; §16 Engine B experiment note; §11 item 20; §11 item 26; closing principles; truest single sentence. Three sealed S16 historical records were deliberately preserved unchanged: the S16 locked decisions block (lines 126–127, recording the original RTX 5060 Ti 16GB plan as a dated decision snapshot) and the §11-SETTLED S16 entry. Dolphin 3.0 R1 Mistral 24B remains only the first model candidate to test after the upgrade — not yet tested, not adopted.

4. **Ness having a Person-Box recorded in §7L.** Added after the Proposal-Based Creation block and before the Default View section: "SETTLED FACT — NESS HAS A PERSON-BOX (June 25 2026). Ness has a Person-Box. How Ness's Person-Box is created, anchored, and maintained is not yet designed and must be decided separately."

5. **Five Knowledge Catcher blocks added to §8.** Added after the Academic Source note and before §9: (a) Pipeline Scope — the pipeline has two responsibilities: gathering new outside information, and checking stored information against outside sources; (b) Source Preservation — saves the relevant excerpt as plain text plus a full-page frozen screenshot; inert visual evidence only, no live content preserved; (c) Live-Retrieval Security Boundary — full-page retrieval is a new surface area; live retrieval must occur inside a separately isolated capture environment; implementation not yet designed; (d) Automatic Re-checking — permitted only on a schedule Ness explicitly approves; N.H may not create or extend its own schedule; (e) Fallback — when the full-page screenshot cannot be captured: keep excerpt plus provenance, mark clearly as SOURCE PRESERVATION INCOMPLETE, require corroboration for important claims, do not discard, do not hide the failure.

6. **Meaning-to-technical mapping questions added as §11 item 34.** One grouped item covering four topic groups and five open questions from the S19 concept-name review session: (a) Grounded Keeper of Origins — scope; (b) Origins — granularity; (c) Origins — time-fields; (d) Those Three To Become A One — no-context mode; (e) Holding — technical representation. These must remain open, must be handled through a careful audited meaning-to-technical design process, and must not be silently decided during unrelated technical work.

7. **§22 Wellbeing and Behavioral Baseline System — design restored from source file (June 25 2026).** Source: `NH_wellbeing_baseline_system.md` (June 18 2026). Eight insertions applied to §22; no existing §22 text removed or reworded. Restored content: provenance note (emerged from ChatGPT feedback discussion); NOT sentence opening the core philosophy; "His own patterns." and "his actual" in the core philosophy; full rationale for passive baseline-building over a one-session approach; two missing sentences in the periodic surface paragraph ("The system decides if the correction is consistent with the broader pattern." and "The data does the work, not the complexity of the model."); complete WHAT TRIGGERS THE SYSTEM section (physical triggers; five mental/behavioral trigger patterns; noise-vs-signal rule; thresholds-emerge-from-data rule); complete WHY THIS IS ARCHITECTURALLY CLEAN section (five architectural integrity points); data sources list in BUILD ORDER (four input sources); fuller file descriptions for `nh_baseline_engine.py` and `CALIBRATION_ANCHOR`; complete WHY THIS IS NOVEL section (framed as design context, not a legally or academically proven originality claim). REALITY/SIMULATION terminology was not changed — the old gate is still running and the original design was written against it. Changed line range: 1615–1673 (§22 section). Section grew from 33 lines to 59 lines.

8. **§23 Mobile App — Three-Mode Companion — design restored from source file (June 26 2026).** Source: `NH_Mobile_App_Design_Spec.md` (June 19 2026, v3, final structure). Eight str_replace operations applied to §23; no existing §23 text removed or reworded. Restored content: provenance note (from a live design conversation, v3 final structure); Mode 3 diagram description "runs on what it already knows"; Mode 1 tunnel lifetime clause ("it exists only during a window Ness deliberately created and ends") and "intentionally designed that way"; complete Modes 2&3 critical paragraph ("in any way" strengthening; API answer mechanism sentence; two-permitted-bridges sentence; REALITY-adjacent independence principle); Mode 2 "grow/improve" and learning-side explanation; Mode 3 "no new API calls possible"; Manual Sync "no automatic background sync, ever"; Manual Sync transfer description (what gets sent); Manual Sync equal-standard principle ("no exceptions for phone-sourced data"); Security requirement 1 assumption-safety clause; Security requirement 2 os.system identification and removal directive; Security requirement 5 two-bridges clause; three expanded open questions (model tradeoff context, iOS/Android background constraint, sync content options); complete WHY THIS DESIGN IS GOOD, NOT JUST "GOOD ENOUGH" section (four rationale points); build-readiness note. REALITY/SIMULATION terminology unchanged — all references currently valid for the still-running gate. Future Manual Sync arrival path in the reading-layer architecture remains UNRESOLVED and is not named. Changed line range: 1677–1714 (§23 section). Section grew from 30 lines to 38 lines.

**Preserved unchanged throughout this session:** NH_MASTER-19_FULL.md (the source file); all sealed S16 historical records; §7R Attention and Relevance Control (fourteen decisions); §7L proposal-based creation rules for other people's Person-Boxes; all other sections not listed above.

**Still pending after this session:** The Decision Defaults companion file (NH_DECISION_DEFAULTS-S17_AUDITED_v1.md) references NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md and is not synchronized with S18, S19, or the current recovery and correction session. It requires regeneration from the adopted corrected Master before it can be used as a behavioral guide. Regeneration is sequenced after Ness formally reviews and adopts the corrected file.

9. **§6A — Dual-architecture reconciliation (session following S19, June 26 2026).** Source evidence: live `.cursorrules` v3.1 (15,303 bytes, dated 06/22 04:00 PM, `C:\NH\nh_engine_core\.cursorrules`) read directly and compared against `NH_MASTER-19_CORRECTED_v1.md` §6B (7-field root schema, 12-field reading contract), §5 codebase map, §6 (what's built), status table, §§22 and 23 for store and file references, and §11 open items. Previous project chats searched for session-11 content and corroborating design evidence.

Prior state of §6A: heading plus one italic framing paragraph only — no rule content present in the Master. The live disk file contained §§0–11 governing only the Layer 2 REALITY/SIMULATION gate, and §12 INCOMING describing the accretive architecture as entirely future. The accretive store was built and sealed across S12–S16 but absent from `.cursorrules` entirely. Classified as Severity 2 gap: ESSENTIAL INFORMATION STILL EXISTS ONLY OUTSIDE THE MASTER.

Five decisions settled by Ness before reconciliation: (1) `nh_engine_minimal.py` and `nh_engine_b.py` Full Protected, with benchmark-protection requirements covering `MOUTH_MODEL`, prompt text, context-window behavior, `_get_preceding_turns`, `run_on_gold`, output destination, gold-set handling, and any behavior that could change benchmark comparability; current mouth model remains a test candidate only. (2) `nh_ingest_chatgpt.py` Full Protected, with seven named dry-run items and no-bypass-of-seal rule. (3) `nh_rebuild_chroma.py` Full Protected, with eight named dry-run items and no-touch-old-collections rule covering `nh_reality_core`, `nh_test_asm`, `nh_simulation_core`. (4) `.nh_readings_store.jsonl` requires dual protection: physical marker `.nh_readings_production_authorized` (Ness-only creation, deliberate filesystem act) plus full dry-run approval with eight named items; marker gate decided, not yet implemented in `nh_accretive_store.py`; implementation requires a separately approved code change. (5) `nh_baseline_engine.py` creation gate now, automatically Full Protected on creation, six §22 prerequisites required.

Changes applied to §6A: complete self-contained dual-architecture summary replacing the prior empty shell. Three-layer architecture map, sovereignty boundaries, schema constraints (including all-seven-field root requirement with `source_title` field/value distinction, and `source_reliability` key-present / value-representation-unverified rule), production authorization mechanism, Protected Files and Stores, dry-run protocol, §12 status, and this correction-log entry all included. Self-containment achieved without claiming the Master overrides the live disk file.

Changes applied to `.cursorrules`: v3.1 → v3.2. Section treatment: IDENTITY block preserved word-for-word; §1 replaced (split into §§1A permanent, 1B legacy gate with original prohibition text word-for-word, 1C accretive store); §2 replaced (split into §§2A legacy gate with original §2 text word-for-word, and 2B accretive store gate); §3 replaced (split into §§3A legacy file map with original table word-for-word, and 3B current architecture file map); §4 replaced (split into §§4A legacy stores with original descriptions preserved in substance plus evidence-dating qualifications, and 4B current stores); §5 preserved in substance with one evidence-dating qualification added to the research engine import-site claim; §6 replaced (stale dual-stack map replaced with three-layer stack map); §7 extended (all existing Protected File entries preserved word-for-word; Layer 3 entries and creation gate added); §8 preserved in principle with one accretive-store stopping condition added; §9 preserved in principle with Layer 3 validator requirement and stale-docstring note added; §10 preserved in principle with production-marker automation prohibition added; §11 preserved in principle with Layer 3 file list and cross-layer mixing prohibition added; §12 replaced (single NOT IN FORCE block split into §§12A now built, 12B designed not built, 12C legacy overrides, 12D creation gate); REMINDER preserved in principle with Layer 3 equivalent sentence added. No legacy protections removed or weakened.

Unverified claims carried into both patches (must be verified by live code inspection before the next session treats them as facts): (a) `nh_research_engine.py` import sites in `nh_jarvis_core.py` and `nh_hud_server.py` — documented in v3.1 as of June 19 2026, not re-verified; (b) `nh_timeline.json` and `nh_nightly.py` disk presence and execution status — referenced in v3.1, not confirmed in Master or later sessions; (c) `nh_ingest_chatgpt.py` dry-run or test-path mechanism — not confirmed from any available source; (d) exact function body location of the stale "188 seed records" docstring — confirmed as `_validate_record` by Master documentation, function body not directly inspected; (e) whether `append_reading()` currently contains any production-path authorization check — implementation status unverified from live code; Decision 4 establishes design intent only; (f) current write-activity status of all five Layer 2 stores — documented as actively used as of June 19 2026, disk behavior not re-verified.

**Disk `.cursorrules` not overwritten during prior sessions. Original `NH_MASTER-19_CORRECTED_v1.md` not overwritten.** New Master file: `NH_MASTER-19_CORRECTED_v2.md`. Status of both files before this patch: §6A = empty shell (heading plus one framing paragraph); `.cursorrules` = v3.1 governing Layer 2 only. Status after patch: §6A = complete dual-architecture summary; `.cursorrules` = v3.2 governing all three layers. **NH_MASTER-19_FULL.md preserved unchanged throughout.**


<!-- NH_SOURCE_END filename="NH_MASTER-19_CORRECTED_v6.md" -->

---

## V.3 — Superseded Decision Defaults

This is a complete verbatim historical copy of the superseded candidate Decision Defaults. It is retained for no-loss provenance and is not current authority.

<!-- NH_SOURCE_BEGIN filename="NH_DECISION_DEFAULTS-S19_v1 (1).md" bytes=33328 sha256=ecea9224163681f9fc1d29327b0453c5e7ead42fd178786ab9dc6a6d4e1baaa6 -->
# N.H — DECISION DEFAULTS (S19)
# Behavioral guide for N.H design and build sessions.
# Synced to: NH_MASTER-19_CORRECTED_v6.md (adopted June 26 2026)
# Hash of authoritative Master: 88bda5391f6a32f49354e503d98c1768
# Supersedes: NH_DECISION_DEFAULTS-S17_AUDITED_v1.md
#
# CANDIDATE — not authoritative until Ness explicitly adopts it.
# Do not use as a behavioral guide until adopted.
#
# PURPOSE: prevents re-litigating settled decisions. Every item here
# is decided. Do not reopen unless Ness explicitly asks to revisit it.
# For anything not listed, treat it as open and surface it.

---

## 0. BEHAVIORAL OVERRIDES — read first, apply always

- **Never skip the disk-verification step.** Trust disk, never the doc — including this file. Before any build action, confirm what exists on disk.
- **Never decide facts. Never close the book.** N.H is Ness's HELPER, not his DECIDER. The engine reads, connects, and lays out what it sees — then hands it to Ness. The engine never decides what is real. Ness affirms off-board, in real life, not as a step in the machine.
- **One concrete step at a time.** Finish and verify the thing in front before expanding scope.
- **Evidence over narrative.** A claim about the codebase requires disk evidence, not remembered state.
- **Backup before any destructive step.**
- **Cursor writes code; Claude designs and audits; Ness runs commands and verifies on disk.** This division is not renegotiable.
- **No design decision is made on Ness's behalf.** Surface conflicts and options; wait for Ness to decide.
- **Do not re-litigate anything in this file.** It is already decided. If Ness wants to revisit something, he will say so.
- **Meaning-to-technical mapping questions (§11 item 34) must not be silently decided** during unrelated technical work. They are open by design. See the open questions section below.

---

## 1. SYSTEM IDENTITY AND SOUL

- N.H is a sovereign, local, offline-first personal AI memory and meaning system.
- **The system name: N.H (also called "Jarvis").** The meaning-layer system name (The First View's Turning Mirror) is settled in the meaning layer alongside the technical Master; it has not yet been formally adopted into the Master through the audited integration process.
- **The heart's three beats: Stop, Connect, Carry.** Settled in meaning layer; not yet in the Master.
- **Ness is the membrane** — the boundary between creation and memory. Technical label: the membrane. Meaning-layer name: the First View. The First View has not yet been adopted into the Master through the audited integration process.
- N.H is local-first. Data does not leave the machine except through explicitly designed and authorized connectors (research pipeline, mobile Full Mode tunnel — both deliberate, human-triggered).
- The system never trains a base model. Knowledge lands in memory (the accretive store), never in the frozen mouth.
- The system never claims to have invented local AI, approval gates, or a trained model.

---

## 2. ARCHITECTURE — THE TWO MACHINERIES

**DUMB MACHINERY** (moves and holds data; never interprets): the accretive store, the two files (sealed roots + readings), the pointers, role-carried-from-source, the catalog's who/when/where marking, the person-box GATHER. One law: never interpret, never close — only add / point / carry / sort / gather. Safe BECAUSE it cannot interpret.

**SMART MACHINERY** (reads the person; never closes): the meaning webs, the story layer, gap-reading, firmness-as-read, clash surfacing, the NOTE, the wonder/simulation. One law: everything here is weightless, dated, confidence-tagged, rejectable — NEVER a fact. Safe BECAUSE it cannot close.

**The membrane** is the boundary between them. Creation (SMART) never closes into memory (DUMB).

**The DUMB machinery MAY** establish directly-verifiable machine-state and provenance facts. **The SMART machinery MAY** interpret, connect, lean — but may NEVER silently promote an interpretation into an established fact. Authority for any promotion belongs to Ness, off-board.

---

## 3. SETTLED DESIGN — NEVER RE-ASK

### 3A. The reading record (BUILT & VERIFIED, S14)

- **12 fields:** `id · reads · meaning · confidence · role · story_layer · mode · timestamp · produced_by · schema_version · derived_from · idempotency_key`
- A reading NEVER copies root text — it points via `reads`.
- `_validate_reading` gates SHAPE only — rejects malformed, never rejects uncertain. A low-confidence, empty-story, or insufficient-context reading is WRITTEN and marked, never refused.
- `confidence` = a TWO-SLOT object `{interpretation_confidence, source_reliability}` — NEVER one blended number. `interpretation_confidence` filled on every reading. `source_reliability` key must be present from the first reading; its exact permitted value when not yet knowable is unverified from live code and must be confirmed from `_validate_reading()` or the authoritative schema contract. Do not invent a sentinel. Confidence value-form is deliberately loose — validator checks present+non-empty only; pin later as new schema_version.
- `story_layer` = a LIST (empty list legal). Unknowns OMITTED, never `"unknown"`.
- `mode` = an open word (not a fixed menu) + `classification_confidence` (local; separate from top-level confidence).
- `produced_by` requires `origin` from the controlled vocabulary: `observed, imported, simulated, generated, reaction, human_annotation`.
- `schema_version` present on every new record; `v1` for the first; un-retrofittable.
- `idempotency_key` present on every reading; writer rejects an already-committed key.
- **Memory only ADDS.** A re-read is a NEW reading beside the old one. The original reading never changes.
- **Model confidence is metadata, not authority** (first-class principle, S17). Applies to all present and future models. A confident response may still be wrong; acceptance depends on grounding in the root, supplied context, declared mode, and explicit evidence.

### 3B. The root record (BUILT & VERIFIED, S12/S14)

- **7 fields (v1, sealed):** `id` (uuid4) · `subject` (provenance batch tag — not a semantic topic; do not reinterpret) · `timestamp` (ISO 8601 creation time) · `content` · `re_reads` (list; `[]` for a root) · `source_title` (required field; value may be `None` where no source title is known) · `role` (speaker from source; required on new writes)
- The `subject` field in v1 roots is a provenance/import-batch tag only. Values are `seed:conversations_000/001/002`. Do not reinterpret it as a semantic field. Do not silently reuse it for semantic subject.
- Schema changes require a new `schema_version` and deliberate adoption by Ness.
- Roots are immutable once written. The only change a root can undergo is deliberate, audited destruction — see §7Q of the Master.

### 3C. The accretive store (BUILT & VERIFIED, S12–S16)

- 5,521 clean root records, SEALED. `.nh_roots.sealed` exists; `append_root` refuses while it does.
- Only Ness may lift the seal as a deliberate separate act.
- Production readings store (`.nh_readings_store.jsonl`) is ABSENT — correct by design. All engine output goes to quarantine.
- Production reads require dual authorization: physical marker `.nh_readings_production_authorized` (Ness-only creation) PLUS dry-run PROPOSED CHANGE approval. The marker gate in `append_reading()` is DECIDED but NOT YET IMPLEMENTED in code.
- **RAW CAPTURE ≠ ROOT INGESTION.** Two gates. The pre-ingest store holds what is not yet eligible. A blocker is removed only when its requirement is actually resolved.

### 3D. Gold standards (BUILT & SEALED)

- **Two sealed gold sets. Engine output may fail a case but may NEVER alter it. A correction is a new versioned gold.**
- v1 (S14): 8 clean-bare cases. `NH_GOLD_SET_v1.md` + `.nh_gold_v1.sealed`. Engine A scored ~5–6/8.
- v2-B (S16): 7 context-requiring cases. `NH_GOLD_SET_v2_B.md` + `.nh_gold_v2_B.sealed`. Engine B scored 6.5/7 on the tested dolphin 8B setup. B3 miss cause not yet isolated (model-capability, prompt framing, context format, and run variance all remain possible contributors).
- **Gold scoring — six rules (SETTLED, S14):** (1) `meaning` judged by SEMANTIC match; Ness decides pass/fail by hand. (2) `story_layer` NOT graded in v1/v2-B. (3) Making something up is the real fail; leaving something out is not a fail if what's said is right. (4) Correct-but-extra: true extra passes, made-up extra fails. (5) A case MAY list several acceptable readings. (6) Ness decides pass/fail; model assists, never judges.
- **Engine failure behavior (SETTLED, S14):** insufficient-context → write honest revisable reading; retry-trigger deferred.
- A new mouth must be tested against BOTH sealed gold sets before replacing the current mouth. Old readings keep old `produced_by`. No automatic mass re-read.

### 3E. Engine design decisions (SETTLED, S16)

- **Engine B context strategy = POSITION-BASED, not semantic search.** `_get_preceding_turns` finds the N roots immediately before the target in the same `source_title` thread. Do not reopen as semantic search.
- **n=3 preceding turns, full content (no truncation).** Truncation kills context quality. Do not truncate.
- **BACKGROUND/END BACKGROUND prompt framing (SETTLED, S16).** Prevents the mouth from answering or continuing the conversation. Four rules: do not reference background, do not quote/paraphrase background, do not invent, if short confirmation say what they are confirming. Do not reopen.
- **Engine C (story-layer) is next.** Needs story-bearing gold cases first before it can be tested.
- **Full-thread reading = future goal.** Must be benchmarked, not assumed, after the GPU upgrade.

### 3F. The model layer (SETTLED)

- The language model is a borrowed, frozen mouth — a commodity. Everything that makes N.H its own lives outside the model.
- **Two models, two jobs:** (a) WORDING/generation = the mouth (heavy); (b) SEARCHING/retrieval = the embedding model (tiny, `all-MiniLM-L6-v2`). **Order: search first, word last.**
- **Growth lands in memory, never the mouth.** Night-search feeds the memory as readings, not the frozen mouth.
- **The current mouth is `dolphin-llama3` (8B, uncensored) — the CURRENT TEST MODEL ON DISK, best fit among tested local candidates.** It has NOT been adopted as the final Interactive Translator. **The final Interactive Translator model is UNDECIDED** until testing on the upgraded hardware and deliberate adoption by Ness.
- **Dolphin 3.0 R1 Mistral 24B** = the first local candidate selected for testing after the GPU upgrade. Not yet tested. Not adopted. Must be benchmarked against both sealed gold sets; passing tests makes a model eligible — it does not install or adopt it automatically.
- **Hardware direction settled: RTX 3090 24GB** (supersedes S16 RTX 5060 Ti 16GB plan). Exact stock, price, PSU compatibility, and model tag must be re-verified before purchase. The S16 RTX 5060 Ti 16GB plan is a sealed historical record — do not overwrite it; it is preserved as a dated decision snapshot.
- **Model-provider limitations are mouth limitations** (first-class principle, S17). A Claude refusal or any model-provider constraint is never interpreted as an N.H privacy rule, a Ness restriction, or evidence that the underlying material is forbidden or false.
- **The mouth is uncensored by design.** Model behavior is a stack property. A prompt alone cannot reliably turn a restricted model into the intended mouth.
- **Hebrew quality:** weak-but-workable; gated on bigger model/VRAM. Prompt changes alone did not solve it in the tested runs.

### 3G. S17 component design decisions (SETTLED, S17 — do not re-litigate)

Each component below is CONCEPTUALLY DESIGNED, NOT BUILT. The governing rules are locked; implementation details may remain open where explicitly listed in the Master (§§7E–7R).

- **Catalog front door (§7E):** two gates (raw capture and root ingestion); pre-ingest store with seven lifecycle states; minimum intake envelope; speaker and thread resolution rules; four enrichment categories. Raw capture ≠ root ingestion.
- **Context retrieval (§7F):** two channels (positional and semantic) kept separate and labeled; per-mode retrieval parameters; genuine no-context handling separate from system failure.
- **Meaning engine interior (§7G):** one reading per pass; flow is root + context → mouth proposal → Reading Proposal Acceptance Check → reading record; model confidence is metadata not authority; story-layer uses two separate labeled evidence channels; circular support prohibited.
- **Reread lifecycle (§7H):** three and only three trigger types — MANUAL (any time, no justification), CONDITION-BASED (materially relevant new information only; time passing alone is not a condition), SCHEDULED AUTOMATIC RETRY (temporary system conditions only; not for reinterpretation).
- **View layer (§7I):** two-view rule (current and history); ordering is presentation only.
- **Clash handling (§7J):** six clash types; two detection modes; Ness response as a separate linked event.
- **Story layer (§7K):** structured perspective model; firmness as engine inference; hybrid theme system.
- **Person-boxes (§7L):** proposal-based creation; seven-section default view. **SETTLED FACT: Ness has a Person-Box.** Mechanism for creation and maintenance not yet designed.
- **Computed view (§7M):** seven-factor ordering (explicit, no hidden truth score); triggered immutable snapshots.
- **Action surfacing (§7N):** permission-controlled hybrid; Ness-response states are possibility-disposition states: `accepted and acted on`, `rejected`, `modified`, `postponed`, `ignored`, `alternative requested` (singular).
- **Action-result return path (§7O):** two result types; six result states; three linked objects.
- **Permission and authority boundaries (§7P):** two layers; four risk levels; three action states; stop-and-surface is the default violation response; narrow emergency-stop exception does not permit completed-world reversal without Ness's approval.
- **Privacy, deletion, sensitive-data (§7Q — PARTIALLY CONCEPTUALLY DESIGNED):** five operations (exclusion, hiding, restriction, redaction, deletion); four sensitivity levels; deletion is blocking and verification-based with five distinct outcomes; `verified_complete` is the only outcome that may be described as complete deletion; append-only tombstone retains that deletion occurred without deleted content; capture exclusion two-layer system; third-party baseline; two-stage access control; **private access for Ness is open by default** — sensitive, emotional, medical, or uncomfortable material is not blocked merely because of its subject; external exposure and secondary uses are restricted by default.
- **Living State Web (§7D — PARTIALLY CONCEPTUALLY DESIGNED):** node/edge types, grounding rule, currency rule, action surfacing, return path, and relationships to Computed View/Story Layer/Person-Boxes/authority/privacy designed. Schema, evidence thresholds, aging rules, trigger specifics, attention/relevance control, purpose-aware lenses, world model, and build order remain undesigned.

### 3H. Attention and Relevance Control (CORE CONCEPTUALLY DESIGNED, S18 — §7R)

Fourteen decisions are settled. Do not re-litigate any of them.

- **Output form:** two-layer (context gate + graded named dimensions with provenance). No collapsed hidden score. Relevance is purpose-scoped only.
- **Three producer types per dimension:** rules, embedding model, mouth — each with declared provenance. Mouth is declaration-authorized only and may not self-approve.
- **Evaluation timing:** on-demand by default; optional triggered pre-computation for declared latency-sensitive contexts; no global relevance state.
- **Two-tier mode contract:** Tier 1 owned and validated by Attention and Relevance Control; Tier 2 owned and validated by the consuming component.
- **Ness's relationship:** inspection always available; per-judgment corrections and context-scoped overrides are direct and append-only; mode changes use proposal-and-confirmation with consequence surfacing.
- **Mouth-produced dimension validation:** deterministic validation with six checks and three outcomes (validated, failed, unresolved). Validated ≠ substantively correct. Optional model-based validation requires declared independence. Disagreement recorded. Mouth dimensions may not act as context-gate conditions.
- **Minimum shared vocabulary:** four gate conditions; nine named dimensions. Positional/semantic channel identity is retrieval provenance, not a dimension. Privacy and deletion eligibility are external prerequisites, not gate conditions.
- **Living State Web boundary:** relevance events emitted, never written directly. Relevance and currentness are permanently separate. Circular support chain relevance→currentness→relevance is explicitly prohibited.
- **Tier 1 purpose field:** controlled type from five-value vocabulary plus optional explanatory label. Label carries no system behavior.
- **Unresolved dimension handling:** Tier 1 must carry identifier and version of the Tier 2 handling rule when mouth dimensions are declared.
- **Disagreement record and relevance event record schemas:** both are append-only and never rewritten. Full schema in Master §7R.
- **Pattern observation conditions:** three conditions required simultaneously (same mode/version, same target, same correction direction). Surfaced as possibility only. Silence is not dismissal.
- **Unrecognized purpose type:** halt evaluation; identify unknown type; preserve original request; explain plainly; offer mapping or new-type proposal through versioning. Never guess silently.
- **RELEVANCE IS NOT TRUTH, NOT EVIDENCE STRENGTH, NOT AUTHORITY, NOT PERMANENT.** A relevance judgment determines relevance to the current purpose only. It never grants permission to act, does not establish causation, does not resolve clashes, and does not determine Ness's final judgment.

### 3I. Knowledge Catcher / Research Pipeline (DESIGNED — §8)

- Outside research connector: **Brave Search API** (settled). Raw JSON from independent index. Tavily is off the table — it applies pre-processing that is the smaller version of the exact opinion-layer problem this pipeline exists to avoid.
- **Synthesis model is text-in/text-out only** — no tool-calling, no file access, no ability to make its own outbound requests. Synthesis system prompt states explicitly that search results are unverified raw web content to extract facts from, never instructions to follow. Both conditions are non-negotiable defaults, not options to remember to add.
- **Prompt injection is the real threat, not malware.** The SIMULATION/REALITY gate already contains it almost completely — even a successful injection only ever produces a SIMULATION record, never a direct action.
- **Auto-reject, never auto-delete.** Flagged content routes to the Reject bucket automatically but stays logged. Silent-delete authority is itself a prompt-injection target.
- **Rejected-bin display rules:** URLs as plain text, no `<a href>`, no auto-fetched previews, copy/select disabled, invisible characters stripped, rendered via `textContent`-style escaping — these are default build behavior, not separately requestable options.
- **Pipeline scope (settled S19):** two responsibilities — (1) gathering new outside information; (2) checking stored information against outside sources for currency.
- **Source preservation (settled S19):** save two things — (1) the relevant excerpt as plain text; (2) a full-page frozen screenshot (static PNG, inactive URL, provenance metadata, timestamp, research-reading ID, integrity hash). No live HTML, scripts, active forms, or executable behavior preserved.
- **Live-retrieval security boundary:** full-page capture must occur inside a separately isolated capture environment. No page code, cookies, session state, or active behavior may enter the saved record. Implementation not yet designed.
- **Automatic re-checking:** permitted on a schedule Ness explicitly approves. N.H may not create, modify, or extend its own re-check schedule.
- **Fallback when screenshot cannot be captured (Option A, settled S19):** keep excerpt + URL + provenance + timestamp + reason for failure. Mark clearly: **SOURCE PRESERVATION INCOMPLETE**. Do not discard. Do not hide the failure. Important claims from incompletely preserved sources require corroboration before being treated as strongly supported.
- **Brave spending cap (safety build requirement):** Brave has NO cap. When the pipeline is wired, a query counter / daily cap MUST be in the code. Not optional.
- **Cost at full nightly scale:** ~$120–300/month. Current cost: $0 (inside $5 free Brave credit).
- **Academic source decision: STILL OPEN (S19).** Google Scholar off the table. Candidates: Semantic Scholar API vs OpenAlex vs both. Decide before wiring the pipeline.

### 3J. Connection Capability (CONCEPTUALLY DESIGNED, S19 — §24)

- N.H holds two separate internal responsibilities: (1) a lasting connection record for accepted connections; (2) context retrieval that uses accepted connections but never creates them.
- Connections come from only three approved bases: direct recorded relationship, Ness explicitly stating or confirming it, or a narrow rule Ness authorized.
- Similarity, timing, shared themes, or being retrieved together must not create a connection proposal by themselves.
- **Accepted ≠ certain.** Decision status and certainty are permanently separate. Accepting a connection never raises its certainty.
- **Pending connections may guide investigation silently but may never support a factual claim, judgment, recommendation, or action.**
- The one-way rule: Context Retrieval may use accepted connections and may surface a direct recorded relationship into the waiting area. It may never accept a connection by itself.
- Five source types kept separate inside any possibility or connection: source material, prior interpretation, assumption, unknown, invented simulation material.

### 3K. Wellbeing and Behavioral Baseline System (DESIGNED, S19 — §22)

- **Build order gate:** this component comes AFTER the search pipeline is complete and stable and the review queue has been healthy for at least one month. Do not build early.
- Measures Ness against Ness only — never against external standards or clinical definitions.
- Ness does not approve or reject the baseline. The system validates against internal consistency across time.
- Four tiers: silent flag → mirror signal → queue throttling → REALITY freeze. Dry mode and research always work — the system never becomes useless.
- Unlock mechanism: upload of a psychiatric or medical appointment record as a calibration anchor. Appointment anchors are not optional.
- **`nh_baseline_engine.py` creation gate:** Cursor must not create this file without "CONFIRMED: create nh_baseline_engine.py" from Ness, the full dry-run protocol, and all six prerequisites: (1) search pipeline complete and stable; (2) review queue healthy for at least one month; (3) baseline sources and consent boundaries defined; (4) system remains advisory — cannot diagnose, prescribe, or act autonomously; (5) file's inputs, outputs, stores, and protected write paths named exactly; (6) no wellbeing output may silently enter roots, production readings, or the legacy REALITY store. Once created, Full Protected — "CONFIRMED: modify nh_baseline_engine.py" required before any edit.

### 3L. Mobile App — Three-Mode Companion (DESIGNED, S19 — §23)

- **Single most important rule:** nothing connects to the real N.H system automatically, ever. The only two doors are Manual Sync and Full Mode — both require Ness to deliberately trigger them.
- Mode 1 (Full Mode): triggered only by explicit Ness action (fingerprint/Face ID/PIN). Tunnel does not stay open passively.
- Modes 2 & 3 (Local AI): completely independent of the real N.H's store. No automatic connection. Mode 2 learns online; Mode 3 is the same model offline.
- Manual Sync: requires fingerprint/Face ID/PIN confirmation. Phone-sourced data goes through the same SIMULATION review gate as everything else — no exceptions, no shortcuts to REALITY.
- Security requirements (non-negotiable): tunnel wired through `nh_auth.py`; no raw OS command execution from phone input; `os.system()` via `nh_pc_agent.py` is not part of this design and should be removed; all locally stored data encrypted at rest; phone-originated data always SIMULATION first; local AI never auto-connects to real N.H.

### 3M. `.cursorrules` v3.2 (IN FORCE)

- `.cursorrules` v3.2 is the in-force ruleset Cursor obeys. Three architecture layers coexist on disk. See §6A of the Master for the complete dual-architecture summary.
- **Layer 1 (oldest legacy):** retained on disk; not the active build target; read-only.
- **Layer 2 (REALITY/SIMULATION gate):** still running; `promote_to_memory()` is the one gate; `NH_PROMOTE_TOKEN` active; do not weaken.
- **Layer 3 (accretive store and reading engines):** active build target.
- All five `.cursorrules` protection decisions are in force: `nh_engine_minimal.py` and `nh_engine_b.py` Full Protected (benchmark protection); `nh_ingest_chatgpt.py` Full Protected; `nh_rebuild_chroma.py` Full Protected (never-touch-old-collections rule); production readings store dual-authorization; `nh_baseline_engine.py` creation gate.
- The stale "188 seed records" docstring in `_validate_record` is still open — fix when the file is next touched under a CONFIRMED edit.

---

## 4. CURRENT BUILD STATE SNAPSHOT

**BUILT AND VERIFIED ON DISK:**
- Accretive store: 5,521 clean roots, 7-field, role-carried, SEALED
- Two-file routing, sealed roots, reading record (validator + writer, 12-field)
- Gold set v1 (8 cases, SEALED) + Gold set v2-B (7 cases, SEALED)
- Engine A (`nh_engine_minimal.py`) — ~5–6/8 on gold v1
- Engine B (`nh_engine_b.py`) — 6.5/7 on gold v2-B (tested dolphin 8B setup)
- Chroma `nh_roots_v1` (5,521 clean roots, `all-MiniLM-L6-v2`)
- `nh_rebuild_chroma.py` (never touches old collections)
- Ingest pipeline (`nh_ingest_chatgpt.py`)

**BUILT STATUS — LEGACY GATE (still runs; do not remove before new filter complete):**
- REALITY/SIMULATION gate stack, Chroma `nh_reality_core` (116,391 — keep until `nh_roots_v1` proven)

**CONCEPTUALLY DESIGNED, NOT BUILT:**
- Catalog front door (§7E), context retrieval (§7F), meaning engine interior (§7G), reread lifecycle (§7H), view layer (§7I), clash handling (§7J), story layer (§7K), person-boxes (§7L), computed view (§7M), action surfacing (§7N), action-result return path (§7O), permission and authority boundaries (§7P), attention and relevance control (§7R)

**PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT:**
- Privacy, deletion, and sensitive-data handling (§7Q), Living State Web (§7D)

**DESIGNED, NOT BUILT:**
- Wellbeing and behavioral baseline system (§22), mobile app three-mode companion (§23)

**CONCEPTUALLY DESIGNED (S19), NOT BUILT:**
- Connection capability (§24)

**CONCEPT LEVEL ONLY / NOT DESIGNED:**
- Wonder and simulation mechanism (concept in §7B; mechanism not designed)
- World model (not designed)
- End-to-end cycle (identified, not yet designed)

**NEXT BUILD STEP:** Engine C (story-layer). Needs story-bearing gold cases first.

---

## 5. OPEN FORKS — genuine open questions

Items here are open. Do not settle them silently. Surface them when relevant.

- **Engine C:** Story-layer reading. Needs story-bearing gold cases before it can be built and tested.
- **Academic search source (§11 item 9):** Semantic Scholar API vs OpenAlex vs both. Decide before wiring the pipeline.
- **Live-retrieval security boundary implementation (§8):** isolated capture environment design not yet done.
- **Screenshot-as-inert-image proposal (§8):** consistency with N.H's spirit noted but decision not yet made.
- **Multi-box (sealed-batch) architecture (§11 item 18):** not designed. Must be designed before a second batch is written.
- **Production readings authorization code (§6B):** `.nh_readings_production_authorized` marker check in `append_reading()` is DECIDED but NOT YET IMPLEMENTED. Requires a separately approved code change.
- **`nh_baseline_engine.py`:** does not exist. Creation gate active. All §22 prerequisites must be met first.
- **Mobile app build (§23):** designed, not built. Open questions: model choice, local memory format, iOS/Android background constraints, Full Mode tunnel wiring, Manual Sync content scope.
- **§0A placement (§11 item 17):** two open pins — (1) whether the final name is SMART or psychologics; (2) where the NOTE and clash handling sit within the DUMB/SMART frame.
- **Wonder and simulation mechanism:** concept settled; mechanism not designed.
- **World model:** not designed; named in Living State Web domain list.
- **End-to-end cycle:** the complete flow from new input through all components to Computed View or chat has not been designed as a single connected sequence.
- **Living State Web remaining domains:** schema, evidence thresholds, aging rules, trigger specifics, attention/relevance control integration, purpose-aware lenses, world model, build order — all undesigned.
- **Interface, world, and interaction system (§19):** in-progress; paused; simulation interior, gesture vocabulary, VR, camera, accessibility substantially undesigned.
- **Chat front door (§14):** two open questions — (1) creation filter as a distinct mechanism vs mode; (2) always-capture vs deliberate-capture.
- **Confidence value representation for `source_reliability`:** exact permitted JSON form when not yet knowable is unverified from live code. Must be confirmed from `_validate_reading()` or the authoritative schema contract before adopting v3.2 fully.
- **`nh_ingest_chatgpt.py` dry-run mechanism:** not confirmed from available evidence. Cursor must propose a test approach in the dry-run block.
- **`nh_research_engine.py` import sites:** documented in `.cursorrules` v3.1 as of June 19 2026; not re-verified since.
- **`nh_timeline.json` / `nh_nightly.py` disk presence:** referenced in `.cursorrules` v3.1 as Layer 1 legacy; current disk presence unverified.
- **Layer 2 store write-activity:** documented as actively used as of June 19 2026; current disk behavior not re-verified.

### Meaning-to-technical mapping questions (§11 item 34 — MUST NOT be silently decided)

These five questions arose in S19 when the reclaimed meaning names were checked against the technical design. Handle only through a careful audited meaning-to-technical design process:

(a) **Grounded Keeper of Origins — scope:** does the name cover only Origin storage, or all dumb machinery?
(b) **Origins — granularity:** how is mixed-media Origin granularity handled?
(c) **Origins — time-fields:** which time fields belong to an Origin, and what does each timestamp mean?
(d) **Those Three To Become A One — no-context mode:** how does the name map to the no-context reading mode (Engine A, bare root)?
(e) **Holding — technical representation:** how is Holding technically represented in the Person-Box data structure?

---

## 6. FIRST-CLASS PRINCIPLES — always in force

These are behavioral rules for the system and the session, not design items to reopen.

- **NEVER DECIDE FACTS — never close the book.** (§0)
- **TWO MACHINERIES: DUMB (can't interpret) vs SMART (can't close); the membrane is the boundary.** (§0A)
- **TWO DESTINATIONS:** every eligible input → raw root (sealed) + a reading beside it. This is why there are two files.
- **MODEL CONFIDENCE IS METADATA, NOT AUTHORITY.** (§7G)
- **RELEVANCE IS NOT TRUTH, NOT EVIDENCE STRENGTH, NOT AUTHORITY, NOT PERMANENT.** (§7R)
- **STOP-AND-SURFACE IS THE DEFAULT FOR AUTHORITY VIOLATIONS.** Corrective action is a new action requiring its own approval. (§7P)
- **DELETION IS BLOCKING AND VERIFICATION-BASED.** Five distinct outcomes. `verified_complete` is the only one that may be described as complete. (§7Q)
- **PRIVATE ACCESS FOR NESS IS OPEN BY DEFAULT.** External exposure restricted by default. (§7Q)
- **MODEL-PROVIDER LIMITATIONS ARE MOUTH LIMITATIONS.** Never an N.H privacy rule or evidence that material is forbidden. (§7Q, §16)
- **RAW CAPTURE ≠ ROOT INGESTION.** Two gates. A blocker is removed only when its requirement is actually resolved. (§7E)
- **THE PURE TAPE PRESERVES eligible events append-only** — subject to capture exclusions and audited redaction. "Append-only" must not mean permanent recoverable storage of every secret forever. (§0A, §7Q)
- **THE AFFIRMATION SURFACE is a per-person STORY-layer** — never closed; absence read only under the §0A guard; N.H is NOT a teller; its view is a weightless NOTE.
- **PENDING CONNECTIONS MAY GUIDE INVESTIGATION SILENTLY BUT MAY NEVER SUPPORT A FACTUAL CLAIM, JUDGMENT, RECOMMENDATION, OR ACTION.** (§24)
- **ACCEPTED NEVER IMPLIES CERTAIN.** Decision status and certainty are permanently separate. (§24)
- **THE GOLD IS A SEALED OUTSIDE EXAM.** Engine output may fail but may never alter. Only Ness judges.
- The spine line: **stop forcing the decision, build a structure where not-deciding is safe.**

<!-- NH_SOURCE_END filename="NH_DECISION_DEFAULTS-S19_v1 (1).md" -->

---

# PART VI — VERIFICATION RECORD

All eight embedded sources were reconstructed from this file using their declared byte lengths and compared against their originals by SHA-256. Results appear below.

| Source | Exact byte reconstruction | SHA-256 result |
|---|---:|---|
| `NH_SHARED_CHAT_HANDOFF_BEFORE_CONSOLIDATION_v1.md` | PASS | `47e6a8ba71fa7e90e8bb8ba671cad22291c950c2770d78e82eea6d331ca7d865` |
| `NH_WORKING_ROLES.md` | PASS | `a0281060abd7e7da791bb56a97316ab9ec41ab88fdd7884fac4c6434fa487619` |
| `NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md` | PASS | `fb36bf8e55026ed7d79e4a5264be17f2577dda3276c4b2d2dc320018931f16f5` |
| `NH_ACCEPTED_TSC_DESIGN_v1.md` | PASS | `1da2e296d4345d11dcec5f197aa9a42883349526275c5aa32b0bb07d1ca44658` |
| `NH_wellbeing_baseline_system.md` | PASS | `afb1bad3c1edad3e86e76c5a1cb278b1a1e03c750d4fa1af6f54ad804bcc098c` |
| `NH_CHAT_HANDOFF_AFTER_BGMM.md` | PASS | `f524f7cdd4dd2f1b897177e0e7f0843d1c8a7767341e4a010da9ab066414a562` |
| `NH_MASTER-19_CORRECTED_v6.md` | PASS | `8165f4bed94d2d57140d49e93d3c85b8e2b259053e0b30ac4c675fa7463a1bf9` |
| `NH_DECISION_DEFAULTS-S19_v1 (1).md` | PASS | `ecea9224163681f9fc1d29327b0453c5e7ead42fd178786ab9dc6a6d4e1baaa6` |

## Consolidated companion integrity

The hash below covers this complete file before this final hash line is appended. It is an integrity reference for the created artifact, not an authority claim.

- Pre-final SHA-256: `daf346da2d61e4b50b93faa29836fec0d3b45547bd92f32bd08fc9b474bf77eb`

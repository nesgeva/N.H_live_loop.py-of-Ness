# NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md

## 0. STATUS BLOCK

**Status:** `CANDIDATE — NOT ACCEPTED — NOT ADOPTED — NOT BUILT.`

**B-INT-7 only.** **Mechanical wiring only.** **No new policy** — the
meaning is settled in Master §25.11/§25.12; this file asks Ness nothing
and invents no question. **No implementation.** **B-INT-8 and Bundle 5
closure remain open. B29 is not completed here.**

**Date:** July 13, 2026.

**Register item:** B-INT-7 — voice-enrollment bootstrap wiring (Bundle 5).

**Version note (v1_1):** one combined correction pass on v1_0 only (v1_0
SHA-256
`d3948bfd8cdcb5ba2239ee5e00ca0654d0f698fd82e55c41b6b2330ab9a0a3bb`;
840 lines; 54,106 bytes — **preserved unchanged**), containing **exactly
three correction groups** and **no redesign of accepted meaning**.
**(1) The link/profile ORDER is corrected to Master's.** Master §25.11
says plainly: *"Once the provisional profile reading set is **linked** to
Ness's Person-Box, SIA may use those readings as one input."* v1_0
reversed this — it created the SIA profile first, had the proposal
reference that profile, and then let SIA consume the proposal: a circular
sequence. v1_1 uses the settled order: **readiness → an immutable,
non-authoritative `enrollment_profile_input_bundle` [proposed] → the §7L
link PROPOSAL → §7L's OWN COMMITTED LINK TRUTH → only then SIA's
provisional profile → only then `enrollment_provisional_profile_created`.**
**A proposal record or acknowledgment ALONE is never enough**, and a
**refused, pending, stale, contradictory, or unverifiable link result
BLOCKS SIA profile creation.** **(2) The B29 / BOP / BAI ownership
boundaries are restored.** v1_0 sent microphone capture straight from the
coordinator to BOP. v1_1 defines three separate interfaces — **EC → B29**
(B29 owns the microphone, the device, cleanup, transport, and the
physical capture start/stop result), **B29 → BOP** (BOP owns the DUMB
observation records and owns **no** microphone), and **BAI → BOP** (BAI
alone sources the `biometric:result:success` system-command observation;
**the EC may coordinate its timing but may NEVER fabricate or become its
source**). **B29 is interfaced, not completed.** **(3) The capture-start
crash seam is closed.** v1_0 had no durable boundary proving whether the
microphone actually began — so an absent BOP observation could be misread
as proof it never started. v1_1 adds an EC-owned
**`enrollment_capture_intent_event`** [proposed] flushed **before** the
request to B29, a **B29-sourced `enrollment_capture_started`** [proposed
interface fact], and the honest three-way result (**started / confirmed
not started / unknown**) — with **"absence of a BOP observation is NOT by
itself proof that the microphone never started."** The **session
lifecycle and the parent-operation lifecycle are separated**, terminal
results cannot regress, and the audit-event wording now says **nine
SETTLED events plus additional PROPOSED coordination/recovery events**.
**No policy, meaning, or accepted boundary changed.**

## 1. PLAIN PURPOSE

B-INT-7 connects the already-designed pieces of N.H's **first authorized
voice enrollment**: the **permanently trusted owner phone** → **Ness's
explicit choice to begin** → **BAI's purpose-bound biometric token** →
**all six prerequisites** → **a safely opened enrollment session** →
**BOP's raw observations** → **§7E and B11's only root-writing path** →
**§7G quarantine readings** → **the six initial-corpus eligibility
checks** → **a provisional Person-Box link** → **SIA's provisional
profile and its conservative ceiling.**

**And it exists to make one thing impossible:** turning **biometric
approval**, **declared enrollment provenance**, **one recording**,
**acoustic similarity**, or **a provisional link** into **proof that the
voice belongs to Ness.**

**Master §25.11 says it plainly, and this file carries it whole:** *"The
authorized enrollment provenance permits N.H to create a provisional
profile candidate associated with Ness's enrollment process. It does not
establish that the captured voice belongs to Ness… No enrollment session
alone establishes that association."*

## 2. GOVERNING AUTHORITY, REPOSITORY POINT, AND FILES READ

Authority order: (1) `NH_MASTER-20_CORRECTED_v10.md` — **Master V10
governs every conflict, regardless of stale wording in older files**; (2)
`NH_DECISION_DEFAULTS-S19_v2_2.md`; (3) `cursorrules`; (4)
`NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`.

**Repository point:** `nesgeva/NH-GOVERNANCE`, branch `main`, head
**`6916d58247aa9a62b895834d15479af309b8578f`**, verified at task start
(latest commit: *Accept and close B-INT-6 package*). The complete delta
from `ab4a6ab7…` was inspected: **exactly the two B-INT-6 acceptance
files.** **A full-repository search found no B-INT-7 candidate, no
accepted copy, no closure receipt, and no file claiming to complete this
wiring** — the only B-INT-7 mentions are as an **open dependency** in the
Map, the plan, and accepted packages. **This is the first.**

**Actual files read (not summaries).** **Master V10** `2d9ed4c6`:
**§25.11 Initial Ness Voice-Profile Enrollment Bootstrap in full** (the
six prerequisites; the session-opening sequence; what biometric success
proves; BOP integration; §7G integration; the six initial-corpus
eligibility rules; §7L integration; SIA integration; audit-event
ownership; *What Enrollment Does Not Establish*); **§25.12 Formally
Adopted Vocabulary Additions** (BOP `authorization_type =
"enrollment_declared"`, joining `live_session` | `manual_import`; §7L
`link_type = "enrollment_material_provisional"` — **both formally
adopted, no schema change required**); **§25.1 BOP in full**; **§25.3
SIA**; **§25.4 SACL** (Gates 0–3, the `guest` rule, restart-to-guest);
**§25.5** wellbeing/identity/security separation; **§25.6 BAI in full** —
including **"One pending record exists at a time"**, the
`pending_authorization_record` (`pending_id`, `challenge`, `purpose`,
`requester`, `requested_at`, `expires_at`, `status`,
`app_session_key_ref` — *"device and app trust is bound through a
hardware-backed key in the phone's secure keystore"*), the
`one_time_authorization_token` lifecycle, **Result Handling** (*"no
matching pending record → reject; write `bai_unmatched_result`; no
artifact created"*; *"BAI does not retry automatically"*), and **"BAI
state: In-memory only. Nothing persists across restarts."**; the
owner-phone **pairing / recovery / replacement / emergency-recovery**
sections; **§7E**, **§7G / §7G-A**, **§7L**, **§7Q**, **§9**, **§0B**;
and the **Other-Speaker** material on overlap, stream separation, and
unresolved speakers. **Map v1.6** `33af648d`: C-BOP, C-SIA, C-SACL,
C-BAI, C-PAIR, C-ENROLL, C-7E, C-7G, C-7L, C-7Q, C-STORE (**the B11
active-writable-batch prerequisite**), B-INT-7, B-INT-11, I.4. **Accepted
packages, consumed without reopening:** **A15 v1.1** `9010e9e7` +
receipt; **B7 v1.3** `7fda28e9` + receipt; **B11 v1.4** `baca06e5` +
receipt; **B9** retry architecture and values `e8f4c3de`; **B24 v7**
`7f5762e5`; **A26 v1.1** `41e1f67d` + receipt; **B-INT-5 v1.5**
`c4497281` + receipt; **B-INT-6 v1.3** `4edaaadc` + receipt. Also:
`NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md` (**preserved
supporting history, subordinate to Master V10**) and the eight-bundle
plan `2d6483d1` (Bundle 5). **Where an accepted receipt establishes a
current status, that receipt governs over any older status wording.**

## 3. THE ENROLLMENT COORDINATOR — AND WHAT IT IS NOT

The **Enrollment Coordinator (EC)** [proposed] is the component B-INT-7
wires. **It owns no authority of any kind.** It holds only its own
coordination records (§20) and the **nine enrollment-owned audit
events** Master §25.11 names.

**It is not** the owner of phone trust, recovery status, QR state, the
spoofing assessment, or the Person-Box. **It is not** a session manager
for BAI, an access-control system, a voice-identity authority, a
privacy authority, a root store, a reading queue, or a profile store.
**BAI is likewise none of those things** — Master is explicit: the
trusted-phone binding is the **outer bootstrap authority**, the
purpose-bound token is the **inner approval**, and **biometric success
does not identify Ness by name.**

## 4. THE SIX PREREQUISITES AND THEIR REAL OWNERS

**Exactly the six settled prerequisites (Master §25.11), each owned
elsewhere:**

| # | Prerequisite | **Owner of the fact** | What the EC does |
|---|---|---|---|
| 1 | **The phone holds final permanent trusted-owner status (BAI state 4).** | **BAI / pairing (C-PAIR, C-BAI)** — bound through the **hardware-backed keystore key**, never an OS device-id field | **Reads and references it.** Never asserts it. |
| 2 | **The first normal recovery code was saved, verified, locally tested, and activated.** | **Pairing / recovery owner (C-PAIR)** | Reads and references. |
| 3 | **The original QR and temporary pairing secret were rendered permanently inert at pairing.** | **Pairing owner (C-PAIR)** | Reads and references. |
| 4 | **Original owner setup is finalized; the QR path is permanently closed.** | **Pairing owner (C-PAIR)** — `bai_initial_setup_finalized` | Reads and references. |
| 5 | **No active medium-or-higher acoustic spoofing suspicion in the current session.** | **SIA** (the assessment) / **SACL** (its Gate 0 disqualifier effect) | Reads and references. **Never re-decides it.** |
| 6 | **Ness's Person-Box is confirmed in §7L.** | **§7L** | Reads and references. |

**The result is a versioned snapshot, not a copy of authority:**
**`enrollment_prerequisite_snapshot`** [proposed] — `snapshot_id`;
`snapshot_version`; **one entry per prerequisite carrying the OWNER's
reference AND the owner's current version/event identity**; `taken_at`;
`all_six_satisfied` (boolean). **The EC records the snapshot; it does not
become the owner of any fact inside it.** Audit: **`enrollment_prerequisites_verified`**.

## 5. THE OPENING SEQUENCE — EXACTLY

1. **Ness explicitly chooses "begin"** in the **dedicated Owner Setup /
   Voice Enrollment flow on the permanently trusted phone** — the only
   entry point. The choice is recorded as a **durable explicit-begin
   event** with its own stable identity.
2. **Create one stable `enrollment_operation_id` and one PROSPECTIVE
   `enrollment_session_id`.** **This reservation grants NO authority.**
   It exists to make a **repeated tap or a replay** unable to open a
   second session (§6).
3. **Verify all six prerequisites BEFORE asking BAI** → the snapshot of
   §4; `enrollment_prerequisites_verified`.
4. **Call BAI with purpose exactly `voice_enrollment_ness`.**
5. **BAI creates its SINGLE pending record** (Master: *"One pending
   record exists at a time"*) — `pending_id`, `challenge`, `purpose`,
   `requester`, `expires_at`, `app_session_key_ref` — **and invokes the
   native OS biometric prompt.** **The EC never creates a pending record
   and never bypasses this rule**: if BAI already holds one, the EC's
   request is refused and recorded.
6. **On biometric success, BAI creates one short-lived, single-use
   `one_time_authorization_token` bound exactly to
   `voice_enrollment_ness`.** (A success with **no matching pending
   record** → BAI rejects, writes `bai_unmatched_result`, **and no
   artifact exists** — this is what defeats a replayed old prompt.)
7. **Immediately before consumption, RE-READ and REVALIDATE all six
   prerequisite owners** — the owners themselves, not the snapshot.
8. **If ANY prerequisite changed:** **do not consume the token**;
   **revoke it through BAI** (`bai_token_revoked`); record
   **`enrollment_token_revoked_prereq_changed`** and
   **`enrollment_prerequisite_failed`** with the failing prerequisite
   **by reference, exposing no private material**; **do not open the
   session.**
9. **If all six still hold:** **consume the token exactly once**;
   **durably flush the BAI-owned `bai_token_consumed` proof**; **bind
   that proof to the enrollment operation and session** (§6A); **and only
   then commit `enrollment_session_opened`.**
10. **Microphone enrollment capture may begin ONLY after the
    session-open commit exists and is current.**

**The meanings, preserved exactly (Master §25.11):** **OS biometric
success proves only that an enrolled device biometric was accepted on the
permanently trusted phone.** **It does not identify Ness by name.**
**Trusted-phone binding is the outer bootstrap authority; the
purpose-bound token is the inner approval.** **BAI is not a session
manager, an access-control system, or a voice-identity authority.**

## 6. DURABLE AUTHORIZATION AND DUPLICATE PREVENTION

**BAI's live token state is IN-MEMORY ONLY (Master §25.6: "Nothing
persists across restarts") and is NEVER post-crash proof.** Durability
comes from the **security-audit history**, whose events are **written and
flushed before the producing function returns.**

### 6A. THE DURABLE AUTHORIZATION CHAIN

**In order, each link durable:** the **explicit Ness begin-event
reference** → the **prerequisite snapshot and its owner versions** → the
**BAI pending-authorization reference (`pending_id`)** → the **token
reference** → **the flushed `bai_token_consumed` event for purpose
`voice_enrollment_ness` — THE durable proof** → the **enrollment
operation and session identity** → the **committed
`enrollment_session_opened` event.**

**The token-consumption proof must bind — directly, or through an
integrity-protected companion reference:** `enrollment_operation_id`;
`enrollment_session_id`; the **token and pending-record references**; the
**purpose `voice_enrollment_ness`**; the **trusted-phone binding
reference** (the hardware-backed `app_session_key_ref`); the
**prerequisite-snapshot reference**; **BAI's trusted-local timestamps**;
the **requester identity**; and the **audit schema/version and integrity
reference**.

**Mechanically, honestly:** where BAI's own `bai_token_consumed` fields do
not natively carry every item above, the binding is completed by an
**integrity-protected companion record** —
**`enrollment_authorization_binding`** [proposed] — which **references
the BAI event and is referenced by it or by the session-open commit**,
and which is itself integrity-protected and append-only. **This creates
no second BAI authority: BAI still owns the consumption fact; the
companion only makes the binding verifiable after a restart.**

**No biometric data, challenge, private key, or raw token material ever
enters a log.**

### 6B. WHAT IS PREVENTED, AND BY WHAT

| Must not happen | The mechanism that prevents it |
|---|---|
| **One explicit begin action opening two sessions** | The **`enrollment_begin_claim`** [proposed] — a coordination slot keyed to the **durable explicit-begin event identity**, admitting **exactly one** prospective session. **It grants no authority.** |
| **Two tokens successfully opening the same enrollment session** | The session-open commit is **keyed to the one `bai_token_consumed` proof** bound to this operation. A **second, different** consumption proof for an already-opened session is **refused and recorded**. |
| **One token opening two sessions** | The consumption proof is **bound to exactly one `enrollment_session_id`**; a second session referencing it is refused. |
| **Replay of an old successful prompt** | **BAI's own rule:** a result with **no matching pending record within expiry** → **rejected, `bai_unmatched_result`, no artifact.** The EC never manufactures a pending record. |
| **A token consumed after a prerequisite changed** | **Step 7's re-read of the owners immediately before consumption**; any change → **revoke, do not consume** (step 8). |
| **A session opening without durable token-consumption evidence** | The **`enrollment_session_opened` commit's enforced precondition** is a **verified, flushed `bai_token_consumed`** bound to this operation and session. |
| **Stale phone or recovery state being reused** | The snapshot carries **owner versions**; step 7 re-reads the **owners**, not the snapshot. |
| **A second BAI pending record bypassing BAI's one-pending rule** | **The EC never creates pending records.** It requests; **BAI enforces its own one-at-a-time rule** and refuses. |

**The coordination claim may serialize the opening operation, but it
grants no authority and NEVER becomes a second BAI or enrollment
authority.**

### 6C. THE CRASH SEAM BETWEEN CONSUMPTION AND CAPTURE

**If the durable `bai_token_consumed` proof exists but the session-open
commit does NOT:**
- **the token remains SPENT** (BAI's rule: consumed is permanently
  unusable);
- **microphone capture does NOT start after restart;**
- **the session is NOT silently opened;**
- an honest **`enrollment_aborted_before_capture`** [proposed] outcome is
  recorded — **[proposed] because the governing files provide no name for
  this exact outcome**, and reusing `enrollment_session_closed` would
  falsely imply a session existed;
- **a later session requires a NEW explicit Ness begin action and a FRESH
  BAI token.**

**If the session-open commit exists but capture never began:**
- **close the session honestly with ZERO captured voice segments**
  (`enrollment_session_closed`);
- **do not claim enrollment material exists;**
- **do not automatically restart the microphone.**

**No crash or recovery path may activate capture without a current
explicit enrollment session opened through the settled flow.**

### 6D. THE CAPTURE-START SEAM — HONEST ABOUT WHAT IS KNOWN

**The gap v1_0 left:** nothing durably proved whether the microphone
**actually began**, so **an absent BOP observation could be misread as
proof that it never started.** It is not.

**The ordered capture-start sequence:**

1. **Revalidate immediately before capture:** the **current session-open
   commit**; **privacy capture permission** (§7Q/B7); the
   **trusted-phone / security state** where still applicable; and **no
   stop or cancellation condition.**
2. **Flush the EC-owned `enrollment_capture_intent_event`** [proposed].
3. **It proves ONLY that the EC was ABOUT TO request capture** — nothing
   more.
4. **Send the capture request to B29** (§I5A).
5. **B29 supplies a capture-start result: `started` | `confirmed_not_started`
   | `unknown`.**
6. A **B29-owned / B29-sourced `enrollment_capture_started`** [proposed
   interface fact] **proves ONLY that the microphone pipeline accepted and
   began the capture operation.**
7. **BOP observations remain the evidence of observations ACTUALLY
   COMMITTED.**
8. **A capture-start acknowledgment does NOT prove that any voice segment
   was successfully recorded.**

**The crash rules at this seam:**
- **Crash BEFORE the capture intent:** **no capture request occurred** →
  **close the opened session with ZERO captured segments.**
- **Crash AFTER the intent but before a provable B29 outcome:** **mark
  capture-start reality as UNKNOWN.** **Do NOT claim that capture never
  began.** **Do NOT reopen the microphone.** **Preserve any BOP
  observation that actually committed.** **Close or interrupt honestly.**
- **`confirmed_not_started`:** close with **zero captured segments**.
- **`started`, then a crash:** **interrupt the session**; **preserve
  exactly the committed BOP observations**; **reconstruct no missing
  audio**; **never resume the same microphone session.**
- **The absence of a BOP observation is NEVER, by itself, proof that the
  microphone did not start.**

**A later attempt always requires:** a **new explicit Ness begin action**;
**fresh prerequisites**; a **new BAI pending record**; a **fresh token**;
and a **new session identity.**

## 7. THE BOP CAPTURE BOUNDARY

**BOP remains DUMB physical observation machinery — and it does NOT own
the microphone.** **B29 owns the voice pipeline**: microphone activation
and deactivation, device interaction, cleanup and transport, and the
physical capture-start/stop result (§I5A). **B29 passes the authorized
observation stream to BOP** (§I5B). During the
enrollment session BOP **records raw voice observations only**, and
**decides nothing** — **not identity, not speaker ownership, not spoofing
conclusions, not meaning, emotion, intent, importance, or profile
membership.** Its **stable `capture_id`, durable sequence, channel rules,
bundle rules, observation-quality handling, failure roots, crash
handling, and idempotency are used UNCHANGED**, and **BOP writes directly
to no memory store.**

**Every enrollment root carries exactly the settled provenance (§25.11):**
- **`role = "ness"`** — **the enrollment flow's DECLARED attribution.
  Never described as confirmed identity, and never an SIA conclusion.**
- **`source_title = "enrollment:ness:<session_id>"`**
- **`session_authorization.authorization_type = "enrollment_declared"`**
  — the **formally adopted §25.12 value**, signalling to §7G that the
  role attribution is a **declaration by the enrollment flow, not a
  confirmed SIA assessment.**

**At session opening, stage exactly ONE BOP `system_command` observation
from BAI:** `command_identifier = "biometric:result:success"`; the
**session id**; the **N.H trusted-local timestamp**; **no purpose; no
token id; no claim that Ness was identified; no authorization conclusion
inside the BOP root.** **Its capture identity is stable and
deterministic** — derived from the **session id + the command identifier
+ the single session-open commit** — **so recovery can never create it
twice.**

**A15 (accepted), consumed exactly:** optional voice-channel
`signal_measurements.acoustic_condition_notes` may carry **only the
accepted six fields** and the **five controlled physical-condition
names**. They are **DUMB physical recording-condition evidence**. They may
be considered downstream **only as bounded, provenance-bearing physical
context under the receiving component's own accepted rules**, and they
**never themselves assert — and are never sufficient by themselves to
establish — identity, speaker change, spoofing, imitation risk, emotion,
intent, meaning, importance, behavioral pattern, or causation.** **No
threshold, detection algorithm, calibration value, or device tuning is
chosen here.**

## 8. THE SESSION LIFECYCLE

**Every state below is a state of an ENROLLMENT PROCESS. No state means
"the voice was confirmed as Ness's."**

| State [proposed] | Entered when | Fact supplied by |
|---|---|---|
| `requested` | Ness's explicit begin is recorded | **Ness** (via the trusted-phone flow) |
| `prerequisites_verified_initial` | The six-owner snapshot is taken and all six hold | **The six owners** (§4) |
| `biometric_pending` | BAI holds its single pending record; the OS prompt is up | **BAI** |
| `token_issued` | BAI created the single-use `voice_enrollment_ness` token | **BAI** |
| `prerequisites_rechecked` | The six owners are re-read immediately before consumption | **The six owners** |
| `token_consumed_durably` | The **flushed** `bai_token_consumed` proof exists and is bound | **BAI** (+ the integrity-protected binding) |
| `session_opened` | `enrollment_session_opened` is committed | **EC** (on BAI's durable proof) |
| `capture_intent_flushed` | The EC's `enrollment_capture_intent_event` is durable (§6D) | **EC** — **proves only that it was about to request capture** |
| `capturing` | **B29 reported `started`**; capture is running | **B29** (the start) / **BOP** (the observations) |
| `capture_start_unknown` | The intent is durable but **no provable B29 outcome** exists | **Nobody yet** — **the truth is UNKNOWN; it is never assumed to be "never started"** |
| `closing` / `closed` | Capture stopped; `enrollment_session_closed` committed | **EC** |
| `interrupted` | A crash or a safety change ended the session | **EC**, on the owner's event |
| `aborted_before_capture` | Token spent, **no session-open commit** (§6C) | **EC** |
| `roots_pending_submission` | The frozen observation set awaits §7E | **EC** |
| `roots_partially_committed` | Some roots appended, some not | **B11 / `append_root()`** |
| `roots_committed` | Every frozen observation has a verified `root_id` | **B11 / `append_root()`** |
| `readings_pending` / `readings_partially_completed` | Roots enqueued / partially read | **§7G-A** |
| `profile_readiness_pending` | Eligible accepted readings exist; readiness not yet established | **The profile-integrity owner** (§12) |
| `profile_input_bundle_created` | The immutable, non-authoritative input bundle exists (§12A) | **EC** (coordination only — **no identity evidence**) |
| `provisional_link_proposed` | `enrollment_provisional_link_proposed` | **EC proposes; §7L owns the outcome** |
| `provisional_link_committed` | **§7L's OWN committed link truth exists** | **§7L** — **a proposal or acknowledgment ALONE is not enough** |
| `provisional_profile_created` | **SIA committed the profile** (only after the committed link), then `enrollment_provisional_profile_created` | **SIA** (the profile) / EC (the event — **never written merely because readiness was reached**) |
| `completed` | **ALL of:** the §7L-owned committed link; the SIA-owned committed profile; and **both** enrollment audit events | **§7L + SIA** |
| `blocked` | A protective condition holds (fail-closed) | Whichever **owner** raised it |
| `failed` | Terminal failure, honestly recorded | **EC** |

### 8A. TWO SEPARATE LIFECYCLES

**The ENROLLMENT SESSION lifecycle may end as exactly one of:** **closed
normally**, **interrupted**, or **aborted before capture**.

**The WHOLE ENROLLMENT OPERATION lifecycle MAY CONTINUE after a closed OR
interrupted session** — through **root submission → readings →
eligibility → readiness → the §7L link → SIA profile creation.**
**`interrupted` does NOT automatically destroy valid committed
observations, and it does NOT prevent unaffected eligible segments from
proceeding through the normal root/reading path.** (What it does prevent
is any segment **affected** by the safety change from contributing to the
provisional profile — §9, §11.)

### 8B. LEGAL TRANSITIONS

- **Only LEGAL NONTERMINAL states may transition.**
- **Committed historical facts NEVER regress** — a committed observation,
  root, reading, eligibility decision, link, or profile stands.
- **`completed`, `blocked`, `failed`, and any other declared
  parent-terminal result CANNOT later be overwritten.**
- **Session-terminal status and parent-operation-terminal status are
  DISTINCT** — a session may be `interrupted` while its parent operation
  goes on to `completed`.
- **One parent operation has AT MOST ONE winning terminal result.**
- **No state may be entered by inference from a coordination record** —
  each requires its **owner's** committed fact.

## 9. MID-SESSION SAFETY CHANGES

**Consumed owner events (never re-decided here):** **trusted-phone loss,
replacement, or revocation** (BAI/C-PAIR); **recovery or owner-setup
state becoming invalid** (C-PAIR); **a QR / temporary-secret integrity
contradiction** (C-PAIR); **medium-or-higher spoofing suspicion**
(SIA/SACL Gate 0); **the Person-Box prerequisite becoming missing or
contradictory** (§7L); **BAI/session integrity failure** (BAI); **privacy
capture exclusion** (§7Q/B7); **application or machine restart.**

**Protective behavior, immediately:**
- **stop new enrollment capture at once;**
- **do NOT wait for logging before stopping** — the stop lands first, the
  record follows;
- **preserve only the already-committed observations, exactly;**
- **never reconstruct missing audio;**
- **close or interrupt the session honestly;**
- **do not allow affected segments to contribute to the provisional
  profile;**
- **do not silently resume the same capture session.**

**A later enrollment attempt requires Ness's explicit begin action, a
fresh prerequisite check, a fresh token, and a NEW session identity.**

**Enrollment is NOT a TSC session:** **the TSC lifecycle, the TSC
database, and the TSC archive mechanism are not reused, referenced as
authority, or imitated here.**

## 10. SESSION CLOSE AND ROOT ENTRY

**Enrollment roots enter the shared memory system only AFTER the session
ends.** The exact handoff:

1. **Stop capture** and **commit the session-close or interruption
   fact.**
2. **Freeze the set of actually captured BOP observation references** —
   an immutable set. **Nothing is added to it afterwards.**
3. **Submit each observation through §7E's standard catalog path.**
4. **Use the accepted B11 active-writable-batch architecture** — its
   **global ingestion claim**, **root-ownership binding**, and **append
   commit fence**.
5. **Never append to, reopen, or alter the sealed 5,521-root batch.**
6. **`append_root()` is the ONLY root-writing path.**
7. **Each BOP `capture_id` is preserved as the END-TO-END duplicate
   identity** — capture → §7E → append → checkpoint.
8. **Record the verified `root_id` outcome.**
9. **Enqueue each committed root through the standard §7G-A reading
   queue.**
10. **Readings go to QUARANTINE — never directly to production.**

**Every captured observation root is preserved through the normal path —
even when its segment is later rejected from provisional-profile
training.**

**The distinction, made explicit and never blurred:**
- **§7Q/B7 capture exclusion** may **prevent or protect** material —
  **that is B7's privacy authority, and B-INT-7 does not duplicate it.**
- **Enrollment-segment rejection** means **only: "do not use this segment
  for the provisional profile."**
- **Profile rejection is NOT deletion, destruction, hiding, or removal
  from the shared observation record.**

**No second staging store, root store, profile store, or reading queue is
created.**

## 11. THE INITIAL-CORPUS ELIGIBILITY GATE — ALL SIX CHECKS

Before a segment's roots or readings may contribute to the provisional
profile, **all six settled checks must hold (Master §25.11):**

1. **One consistent live speaker stream** for the segment.
2. **No medium-or-higher acoustic spoofing suspicion** during the
   segment.
3. **No unresolved overlapping-speaker contamination.**
4. **`overall_completeness` is exactly `complete` or `partial`.**
5. **`authorization_type = "enrollment_declared"` is present**, and the
   segment's **`session_id` links to a confirmed durable
   `bai_token_consumed` event.**
6. **Stream integrity:** diarization confidence remains **above the
   bootstrap stream-stability threshold for the FULL segment**, with **no
   unresolved speaker-transition event**, **no material stream split or
   merge**, **no unresolved uncertainty that a second speaker entered**,
   and **no medium-or-higher spoofing evidence.**

**The crucial meaning, carried verbatim from Master:** **check 6
establishes that the segment came from ONE CONSISTENT LIVE SPEAKER. It
does NOT identify WHO that speaker is — the identity profile does not yet
exist at bootstrap.**

**Exactly one outcome per segment**, recorded with the existing
enrollment-owned events: **`enrollment_segment_accepted`** or
**`enrollment_segment_rejected`**. **A rejection record carries the reason
and source references — and NO raw voice payload.**

**Replay safety:** the decision is **keyed to the immutable segment
identity**, so **a replay RECOVERS the prior outcome** rather than
evaluating the same segment into **two competing profile-membership
results**.

## 12. READING, PROVISIONAL PROFILE, AND THE READINESS BOUNDARY

**After the roots commit:** §7G reads them **through the standard queue**;
**the role remains DECLARED enrollment attribution, not confirmed
identity**; readings **carry honest provisional confidence**; **rejected
reading proposals follow the accepted §7G / B9 / B24 behavior**; **no
rejected proposal is silently treated as a valid profile reading**; **no
`insufficient_context` reading is invented merely to force profile
creation**; and **accepted readings remain QUARANTINE readings unless
separately promoted through the normal production-promotion
architecture.**

**The provisional profile is built from ELIGIBLE ACCEPTED READINGS and
their provenance references — never from copied raw audio, and never from
logs.** **Voice profiles remain the accepted SIA / linked-reading
structure: no second independent voice-profile database is created.**

**The "sufficient readings" boundary — mechanics without numbers.**
Master says the link is proposed *"after sufficient readings are
produced."* B-INT-7 therefore defines the **readiness state and the owner
handoff**, and **nothing more**:

- **`enrollment_profile_readiness`** [proposed] — a record naming
  **exactly which eligible accepted readings were counted**
  (`counted_reading_refs`, a **set keyed by reading identity**, so
  **duplicate counting is structurally impossible**), the **eligibility
  decision reference** for each, and the **readiness outcome**.
- **The readiness RULE and its values belong to the accepted
  profile-integrity and SIA rules** — **B-INT-7 chooses no number of
  readings, no duration, no score threshold, no confidence threshold, no
  calibration value, and no acoustic algorithm.** These are **later
  configuration/calibration owned there**.
- **It fails closed:** if readiness **cannot be established** — the rule
  is unavailable, the counted set cannot be verified, or an eligibility
  decision is missing — **no profile is created and no link is
  proposed.**
- **This is NOT A29's general hold-until-enough policy** and must never be
  classified as it. **A29 governs the Meaning Engine's holding of a
  reading; this is the enrollment bootstrap's readiness for a provisional
  profile.**

**Readiness creates NO profile and NO audit event about a profile.** It
produces exactly one thing: the input bundle below.

### 12A. THE IMMUTABLE, NON-AUTHORITATIVE INPUT BUNDLE

**`enrollment_profile_input_bundle`** [proposed] — created once readiness
is established, and **immutable thereafter**. **It contains ONLY:**

- the **exact eligible accepted reading references**;
- the **eligibility-decision references**;
- the **enrollment operation and session references**;
- the **prerequisite and authorization evidence**;
- the **readiness reference**.

**It is COORDINATION ONLY:** **it is NOT an SIA profile**; **it is NOT
another profile store**; and **it adds NO identity evidence whatsoever.**
It exists so the §7L proposal can reference an **exact, frozen input
set** — **never an already-created profile.**

## 13. THE PERSON-BOX LINK — PROPOSED BY THE EC, COMMITTED BY §7L

**The settled order (Master §25.11), and the correction it forces:**
Master says *"Once the provisional profile reading set is **LINKED** to
Ness's Person-Box, SIA may use those readings as one input."* **The link
comes FIRST. The profile comes after.** Nothing here may invert that.

**The EC proposes exactly the settled link (§25.11/§25.12):**

- **`link_type = "enrollment_material_provisional"`**;
- **certainty = `enrollment_provisional`**;
- **one stable `provisional_link_proposal_id`** — so **a replay cannot
  create a duplicate link**;
- **meaning, stated in the link itself:** *the material was collected
  through Ness's authorized enrollment flow;* **it does NOT mean the
  captured voice was confirmed as Ness's voice**;
- **basis:** the **confirmed `bai_token_consumed` for
  `voice_enrollment_ness`**; **owner-phone trust /
  `bai_initial_setup_finalized`**; and **`authorization_type =
  "enrollment_declared"`.**

**The proposal references the `enrollment_profile_input_bundle` (§12A) —
NOT an already-created SIA profile** — plus: the **confirmed Ness
Person-Box**; the **enrollment operation and session**; the **exact
eligible reading set**; the **exact eligibility decisions**; and the
**prerequisite and authorization evidence**.

Audit: **`enrollment_provisional_link_proposed`**.

**§7L OWNS the proposal outcome and the actual link state.** **The EC
proposes; it never approves or merges, and it never becomes a §7L
authority.**

**A proposal record or an acknowledgment ALONE IS NOT ENOUGH.** **SIA may
proceed only on a CURRENT, §7L-OWNED, COMMITTED LINK TRUTH** confirming
that the provisional material is linked to Ness's **confirmed** Person-Box
(§14).

**A refused, pending, stale, contradictory, or unverifiable link result
BLOCKS SIA profile creation.** **Fail closed — never proceed on the
proposal alone.**

## 14. THE SIA HANDOFF AND THE CONSERVATIVE CEILING

**SIA may consume the readings ONLY AFTER a current, §7L-owned COMMITTED
LINK truth exists** (§13) — **never on a proposal, and never on an
acknowledgment.** Once that committed link confirms the provisional
material is linked to Ness's confirmed Person-Box, **SIA may consume the
readings as ONE INPUT under its existing rules**, and **only then may SIA
commit the actual provisional profile.** At this stage:

- **`profile_status = "enrollment_provisional"`;**
- **`recognized_ness` is the MAXIMUM achievable access classification
  while the profile remains provisional — regardless of acoustic match
  score;**
- **the ceiling is NOT an automatic grant of `recognized_ness`** — SACL
  still decides, through its own Gates, whether that level is reached at
  all;
- **behavioral, branch, session-continuity, timing, and wording
  dimensions remain weighted MORE HEAVILY than acoustic match** until the
  accepted rules move the profile to `enrollment_active`;
- **all later evidence follows ordinary SIA training-eligibility rules —
  no shortcut exists for enrollment material;**
- **SIA restart returns SIA to unknown, and SACL applies `guest` until a
  valid fresh assessment exists.**

**Only AFTER SIA's profile commit may the enrollment component write
`enrollment_provisional_profile_created`.** **That event is NEVER written
merely because readiness was reached**, and never because a proposal
exists.

**The `completed` parent state requires ALL of:** the **§7L-owned
committed provisional link**; the **SIA-owned committed provisional
profile**; and **both related enrollment audit events**
(`enrollment_provisional_link_proposed` and
`enrollment_provisional_profile_created`).

**The rule or threshold that changes `enrollment_provisional` to
`enrollment_active` is NOT invented here.**

## 15. ACCESS AND MODE BOUNDARIES

**Enrollment must never, by itself:** prove the voice belongs to Ness;
automatically grant `recognized_ness`; exceed the `recognized_ness`
ceiling while provisional; grant top-security; create a BAI biometric
lease; open Personal Mode; turn a shared or observable channel into a
private one; replace PIN, fingerprint, SACL, PBR, or any other accepted
factor; make voice a **hard lockout** factor; make voice the **sole
identity proof**; authorize external actions; or **bypass B-INT-5 or
B-INT-6.**

**Any user-visible enrollment status or failure message passes the
accepted B-INT-6 privacy-first, SACL-second output chain** — including
its **final §7Q gate, its final SACL gate, the B-INT-5 fence
revalidation, and its no-indirect-disclosure rule.**

## 16. PRIVACY AND RAW-VOICE PROTECTION

**§7Q and accepted B7 apply throughout, and B7's authority is not
duplicated:**
- **capture exclusion is checked BEFORE capturing;**
- **raw voice remains INSIDE the protected B29/BOP capture boundary
  defined by their accepted roles — it NEVER enters an EC record or an
  ordinary log, and it crosses only through the minimum necessary
  protected interface;**
- **coordination records carry references and structural facts only;**
- **minimum necessary material crosses each boundary;**
- **excluded or protected material follows B7's accepted handling;**
- **ordinary components never receive sensitive content merely to decide
  not to use it;**
- **hidden or protected material is never indirectly disclosed;**
- **logs and failure notices contain no raw voice and no reconstructive
  description.**

## 17. OPERATION IDENTITIES AND IDEMPOTENCY

| Identity | Scope / idempotency key |
|---|---|
| **`enrollment_operation_id`** [proposed] | **One stable parent per logical enrollment.** Key: the **durable explicit-begin event identity**. |
| **`enrollment_session_id`** [proposed] | One per opened session; **prospective at reservation, authoritative only at the session-open commit.** |
| **Explicit-begin event** | Its own durable identity — **the anti-double-tap key** (§6B). |
| **`enrollment_begin_claim`** [proposed] | Keyed to the begin-event identity; **one active claim; grants no authority.** |
| **BAI `pending_id` / token reference** | **BAI's own**, consumed by reference. **One pending at a time — BAI's rule.** |
| **`enrollment_prerequisite_snapshot`** [proposed] | `snapshot_id` + version; owner refs + owner versions. |
| **Segment identity** [proposed] | **Immutable**; the eligibility decision is keyed to it (§11). |
| **BOP `capture_id`** | **BOP's own — the END-TO-END duplicate identity** through §7E and `append_root()`. |
| **B11 `ingest_operation_id`** | **B11's own** (WB1–WB3), consumed by reference. |
| **§7G enqueue / reading refs** | **§7G-A's own.** |
| **Eligibility-decision identity** [proposed] | Keyed to the **segment identity** → replay recovers the prior outcome. |
| **`enrollment_profile_readiness`** [proposed] | Keyed to the counted **reading-identity set** → no duplicate counting. |
| **`enrollment_profile_input_bundle` id** [proposed] | One per readiness outcome; **immutable** → a replay **recovers the same bundle**, never a new one. |
| **`provisional_link_proposal_id`** [proposed] | One per enrollment operation → **replay cannot duplicate the link**; recovery **queries §7L with it**. |
| **Provisional-profile build identity** [proposed] | One per operation, keyed to the **committed link + the linked reading set** → SIA is called **idempotently**; **no duplicate profile**. |
| **Capture-control refs** (§I5A) + **`enrollment_capture_intent_event`** [proposed] + **B29's `enrollment_capture_started`** [proposed interface fact] | Intent is EC-owned and proves only *about to request*; the start fact is **B29-sourced**; **BOP's `capture_id`** remains the evidence of what was actually observed. |
| **`enrollment_recovery_operation_id`** [proposed] | Recovery is **itself one recorded operation**. |

**One real enrollment operation has ONE parent operational log.** Stage,
segment, ingest, reading, profile, link, retry, and recovery records are
**children — never competing parent truths.** **No log or coordination
record is evidence for itself, and repetition NEVER increases identity
confidence.**

## 18. AUDIT-EVENT OWNERSHIP — PRESERVED EXACTLY

**BAI owns:** `bai_token_consumed`, `bai_token_revoked`.

**Master supplies NINE SETTLED enrollment-owned audit events** (the
complete settled catalog — **the file's proposed coordination events do
NOT extend it**):
`enrollment_prerequisites_verified`; `enrollment_session_opened`;
`enrollment_session_closed`; `enrollment_segment_accepted`;
`enrollment_segment_rejected`; `enrollment_prerequisite_failed`;
`enrollment_token_revoked_prereq_changed`;
`enrollment_provisional_link_proposed`;
`enrollment_provisional_profile_created`.

**Other owners keep their normal records:** **BOP** (observation/capture);
**§7E** (pre-ingest lifecycle); **B11 / `append_root()`** (root-ingestion
truth); **§7G** (queue and reading outcomes); **§7L** (Person-Box link
state); **SIA** (profile and identity-assessment state); **SACL** (access
state); **B7/§7Q** (privacy decisions); the **security-audit system** (its
durable history).

**In ADDITION to those nine settled events, this file proposes a small
number of mechanical recovery/coordination events** — **which are NOT
part of Master's settled catalog, do NOT change identity policy, and do
NOT become new authority**: **`enrollment_aborted_before_capture`**
(§6C), **`enrollment_capture_intent_event`** (§6D), and the
**B29-sourced `enrollment_capture_started`** interface fact (§6D, §I5A).
**The complete catalog is therefore NOT "exactly nine" — it is nine
settled events PLUS these proposed coordination events**, each clearly
marked.

**No existing event is renamed.** **`[proposed]` marks only names the
governing files genuinely do not provide** — the three above, the EC's
coordination records (§20), and the internal state names of §8. **Every required security-audit
event is written and flushed according to its accepted owner's rules
BEFORE that owner reports success.**

## 19. THE INTERFACE TABLE

*(Each: caller → receiver; decision owner; request → response; identity;
idempotency; precondition; success truth; failure truth; retry class;
recovery; audit; privacy.)*

**I1 — Trusted-phone enrollment UI → EC.** Request `{ explicit_begin_event_ref, trusted_phone_binding_ref }` → Response `{ enrollment_operation_id, prospective_session_id | refusal }`. **Owner: Ness** (the choice). Identity: `enrollment_operation_id`; idempotency: the **begin-event identity**. Precondition: the request comes **only** from the dedicated Owner Setup / Voice Enrollment flow on the **permanently trusted phone**. Success: the operation and claim exist (**no authority**). Failure: refused and recorded. Retry: a new tap is **absorbed** by the claim. Recovery: no session opens. Audit: the begin event. Privacy: structural.

**I2 — EC → the six prerequisite owners.** Request `{ operation_ref }` → Response `{ per-prerequisite: owner_ref, owner_version, satisfied }`. **Owners: BAI/C-PAIR, C-PAIR ×3, SIA/SACL, §7L.** Identity: `snapshot_id`. Precondition: none. Success: `all_six_satisfied = true` → `enrollment_prerequisites_verified`. Failure: **`enrollment_prerequisite_failed`; no BAI call.** Retry: re-read the owners (never the snapshot). Recovery: re-verify from the owners. Privacy: references only.

**I3 — EC → BAI.** Request `{ purpose = "voice_enrollment_ness", requester, operation_ref, session_ref }` → Response `{ pending_id | refusal }`, then `{ token_ref | failure }`. **Owner: BAI.** Idempotency: **BAI's one-pending-record rule** — a second request while one is pending is **refused**. Precondition: the six verified. Success: token issued. Failure: **BAI does not retry automatically**; the pending record reaches a terminal status and the requester is notified. Recovery: **no token survives a restart** (in-memory only). Audit: BAI's. Privacy: **no challenge, key, or biometric datum crosses.**

**I4 — BAI → the security-audit history.** Request: the consumption fact → Response: the **flushed `bai_token_consumed`**. **Owner: BAI (the decision) + the audit system (durability).** **This flushed event — never BAI's memory — is the post-crash proof** (§6A). Failure: **if it cannot be flushed and verified, NO durable authority exists → the session must not open.**

**I5A — EC → B29 (the capture-control boundary).** Request — **and it may carry ONLY these**: `{ enrollment_operation_ref, enrollment_session_ref, current committed session-open ref, current privacy/capture-eligibility decision ref, enrollment provenance refs (role / source_title / authorization_type), destination BOP observation context, current cancellation/stop refs }` → Response `{ capture_start_result: started | confirmed_not_started | unknown }`. **Owner: B29** — **B29 owns microphone activation and deactivation, device interaction, cleanup and transport mechanics, the physical capture-start and capture-stop result, and future latency, interruption, and microphone-error mechanics.** **B-INT-7 chooses NONE of B29's hardware, algorithms, cleanup method, timeout, channel technology, or final field names** — it defines **only this boundary and its fail-closed behavior.** Identity: `enrollment_operation_id` + `enrollment_session_id`. Precondition: **the session-open commit exists and is current**, capture is privacy-permitted, and no stop condition holds (§6D). Failure: **fail closed — no capture.** Recovery: **never reopen the microphone automatically.** Audit: the EC's capture-intent event (§6D) + B29's own records. Privacy: **references only — no audio, ever.**

**I5B — B29 → BOP (the observation boundary).** Request: the **authorized physical observation stream** → Response: **committed BOP observations.** **Owner: BOP** — BOP owns **DUMB physical observation records, the stable `capture_id`, durable ordering, observation-quality fields, failure observations, and idempotent observation truth.** **BOP does NOT own** the microphone hardware, voice-pipeline activation, cleanup algorithms, identity, spoofing conclusions, meaning, or profile membership. Idempotency: **BOP's `capture_id`.** **Raw voice remains inside the protected B29/BOP capture boundary defined by their accepted roles; it NEVER enters an EC record or an ordinary log, and it crosses only through the minimum necessary protected interface.**

**I5C — BAI → BOP (the biometric system-command boundary).** **Caller: BAI. Receiver: BOP.** **Trigger:** the **committed enrollment-session opening that references BAI's durable consumed-token proof.** **Command:** `biometric:result:success`. **Fields — exactly two:** the **session ID** and the **N.H trusted-local timestamp**. **Forbidden inside it:** **purpose; token ID; biometric data; any authorization conclusion; any claim that Ness was identified.** **Identity:** one **stable, deterministic `capture_id`** derived from the **session-open truth + the command identity** — so **recovery can never create it twice.** **The EC may coordinate the TIMING, but it may NEVER fabricate this observation and NEVER become its source: it is BAI's fact, passed to BOP.**

**I6 — BOP → the enrollment capture set.** Request: committed observations → Response: the **frozen reference set** at close. **Owner: BOP** (the observations); **EC** (the freeze). Idempotency: the set is **immutable once frozen**.

**I7 — Session close → §7E.** Request `{ frozen capture_ids, provenance }` → Response `{ accepted | rejected | blocked }`. **Owner: §7E.** Idempotency: the **`capture_id`**. Precondition: the close/interruption fact is committed. Failure: **fail closed** — no root, recorded. Privacy: §7Q exclusion applies **at capture**, per B7.

**I8 — §7E → B11 / `append_root()`.** Request `{ capture_id-derived identity, validated root fields, ingest_operation_id }` → Response `{ root_id | append_duplicate_absorbed | rejected | indeterminate }`. **Owner: B11 / `append_root()` — the ONLY root-writing path**; the **active writable batch** is B11's; **the sealed batch is never touched.** Idempotency: `append_root()`'s own + B11's fence. Recovery: **idempotency lookup recovers the existing `root_id`** — **never a second root.**

**I9 — Root commit → §7G-A.** Request `{ root_id }` → Response `{ enqueued }`. **Owner: §7G-A.** Idempotency: the root identity. Success: queued. **Readings go to QUARANTINE.**

**I10 — §7G outcomes → the eligibility gate.** Request `{ reading refs, root provenance }` → Response `{ per-segment: accepted | rejected + reason }`. **Owner: the EC's gate, using the six checks — but every underlying FACT belongs to its owner** (SIA for spoofing/diarization, BOP for completeness, the audit history for the token link). Idempotency: **the immutable segment identity.** Failure: **reject with reason; the roots are preserved.**

**I11 — Eligibility gate → readiness → the input bundle.** Request `{ eligible accepted reading set + provenance refs }` → Response `{ readiness | not-ready }`. **Owner: the accepted profile-integrity / SIA rules** (the readiness rule and its values — **no number is chosen here**). On readiness, the EC creates the **immutable `enrollment_profile_input_bundle`** (§12A) — **coordination only; not a profile; no identity evidence.** **Fails closed** when readiness cannot be established. **No raw audio crosses. NO PROFILE IS CREATED AT THIS STAGE.**

**I12 — EC → §7L (the link proposal).** Request `{ link_type = "enrollment_material_provisional", certainty = enrollment_provisional, basis, the input-bundle reference, the confirmed Person-Box, operation/session refs, eligibility decisions }` → Response `{ proposal recorded }`, and **later** `{ COMMITTED link truth | refused | pending }`. **Owner: §7L** — **it owns both the proposal outcome and the actual link state.** Idempotency: `provisional_link_proposal_id` (recovery **queries §7L with it**). **The EC only PROPOSES.** **A proposal or acknowledgment ALONE authorizes nothing.**

**I13 — §7L committed link → SIA (the profile), then SACL.** Request `{ committed link truth, the linked reading set, the input bundle, the build identity }` → Response `{ committed provisional profile | refused }`. **Owner: SIA** (the profile). **Precondition — enforced: a CURRENT, §7L-OWNED, COMMITTED LINK.** **A refused, pending, stale, contradictory, or unverifiable link result BLOCKS profile creation.** Idempotency: the **build identity** → **no duplicate profile.** **Only after SIA's commit** may the EC write `enrollment_provisional_profile_created`. **SIA → SACL crosses only through their accepted boundary:** SIA supplies assessments; **SACL alone decides access**; the provisional **`recognized_ness` CEILING is SIA's profile-status effect — never an EC decision, and never an automatic grant.**

**I14 — Status / failure output → the B-INT-6 chain.** Every user-visible enrollment status or failure goes through **§7Q-first, SACL-second, fence-revalidated** delivery. **No raw voice, no protected material, no indirect disclosure.**

## 20. THE COORDINATION RECORDS [PROPOSED] — AND THEIR OWNER

**All owned by the EC. None is an authority. None duplicates an accepted
record.** All are append-only, carry **references not payloads**, obey
§7Q/§25, and **add no evidence weight**:

0a. **`enrollment_capture_intent_event`** — flushed **before** the B29
   capture request; **proves ONLY that the EC was about to request
   capture** — never that the microphone started (§6D).
0b. **`enrollment_profile_input_bundle`** — the **immutable,
   non-authoritative** input reference set (§12A): **not a profile, not a
   store, and it adds NO identity evidence.**

1. **`enrollment_operation`** — the **one parent** (live-state until
   terminal): identities, the §8 state, terminal reason, audit refs.
2. **`enrollment_stage_event`** — append-only child checkpoints.
3. **`enrollment_begin_claim`** — the one-begin-one-session slot (§6B).
4. **`enrollment_prerequisite_snapshot`** — versioned owner refs (§4).
5. **`enrollment_authorization_binding`** — the **integrity-protected
   companion** binding the BAI consumption proof to this operation and
   session (§6A). **BAI still owns the consumption fact.**
6. **`enrollment_capture_set`** — the **frozen, immutable** set of
   captured observation references at close.
7. **`enrollment_segment`** — the **immutable segment identity** the
   eligibility decision keys to.
8. **`enrollment_eligibility_decision`** — one per segment; mirrors the
   owned `enrollment_segment_accepted` / `_rejected` events; **reason and
   references, no payload.**
9. **`enrollment_profile_readiness`** — the counted reading set (§12).
10. **`enrollment_recovery_event`** — recovery as **one recorded
    operation**, naming the crash boundary (the twenty of §21).
11. **`enrollment_duplicate_absorbed`** — a replay absorbed. **No evidence
    weight.**

**One [proposed] audit event** is added only because the governing files
provide no name: **`enrollment_aborted_before_capture`** (§6C).

## 21. THE CRASH AND RESTART TABLE

**Universal rules for every row:** **reconstruct no missing audio**;
**replay no old microphone capture**; **create no duplicate root, reading,
profile, or link proposal**; **never infer success from a coordination
record**; **never automatically reopen the microphone after restart**;
**fail closed on missing, stale, contradictory, or unverifiable
authority.**

| # | Crash boundary | Authoritative committed truth | Exact recovery action |
|---|---|---|---|
| 1 | Before the prerequisite snapshot | The begin event only | Stay idle. **No session, no BAI call.** A later attempt is a **new begin**. |
| 2 | After initial prerequisites, before the BAI request | The snapshot | **Fail the operation.** The snapshot is **evidence of a check, not authority**; a new attempt re-reads the owners. |
| 3 | With BAI pending | **BAI's pending record — which is IN-MEMORY and dies** | **Nothing survives.** No token, no session. New begin + new pending + fresh token required. |
| 4 | After token creation, before the final prerequisite check | **Nothing durable** (the token is in-memory) | **The token is gone with BAI's memory.** No session. New begin required. |
| 5 | After prerequisite failure or token revocation | `enrollment_prerequisite_failed` / `enrollment_token_revoked_prereq_changed` (+ `bai_token_revoked`) | Terminal, honestly. **No session.** A new attempt is a **new operation**. |
| 6 | **After durable token consumption, before the session-open commit** | **The flushed `bai_token_consumed` + its integrity-protected binding** | **The token remains SPENT. Do NOT open the session. Do NOT start capture.** Record **`enrollment_aborted_before_capture`**. **New begin + fresh token required** (§6C). |
| 7 | After the session-open commit, before the system-command observation | `enrollment_session_opened` | The session exists. The BAI `system_command` root is staged under its **deterministic capture identity** — **so recovery creates it once, never twice.** **Capture still requires the current open session.** |
| 7b | **After the capture-intent event, before a provable B29 outcome** | The **`enrollment_capture_intent_event`** — proving **only that the EC was about to request capture** | **Capture-start reality is UNKNOWN.** **Do NOT claim capture never began.** **Do NOT reopen the microphone.** **Preserve any BOP observation that actually committed.** Close or interrupt **honestly** (§6D). |
| 8 | During capture (B29 reported `started`) | Whatever **BOP** durably committed | **Stop.** Committed observations are **preserved exactly**; **the gap is recorded honestly** (BOP's failure/interruption roots). **The microphone is not reopened, and the same capture session is never resumed.** |
| 9 | After some observations commit, before session close | The committed observations | **Close as `interrupted`** with the **frozen actually-captured set**. **Nothing is invented to fill the gap.** **The PARENT OPERATION may still proceed with those valid observations** (§8A). |
| 10 | After close, before §7E submission | The close fact + the frozen set | Resume submission from the **frozen set** — it is immutable, so nothing is added or lost. |
| 11 | During partial §7E / B11 ingestion | Per-item §7E/B11 commits | **Resume at the first `capture_id` without a verified `root_id`.** **No duplicate root** (`append_root()` idempotency). |
| 12 | After root append, before its enrollment checkpoint | **The root store** (the root exists) | **Recover the existing `root_id` by idempotency lookup** and commit the missing checkpoint **exactly once**. **Never a second root.** |
| 13 | After roots commit, before §7G enqueue | The verified `root_id`s | Enqueue the missing roots. **Idempotent on the root identity.** |
| 14 | During partial reading completion | §7G's committed reading outcomes | Resume the queue. **No reading is duplicated; no reading is invented.** |
| 15 | **After readiness, before the §7L proposal** | The **readiness record and the immutable `enrollment_profile_input_bundle`** (§12A) | **Recover the SAME immutable input bundle** — never rebuild a different one. Then propose **once**, under the stable `provisional_link_proposal_id`. **No profile exists yet, and none may be created.** |
| 16 | **After proposal submission** | `enrollment_provisional_link_proposed` | **Query §7L using the stable `provisional_link_proposal_id`.** **Absorb any replay — no duplicate link.** **§7L owns the outcome.** |
| 17 | **After the §7L link COMMIT, before profile creation** | **§7L's committed link truth** | **Recover the committed link and call SIA IDEMPOTENTLY** (same build identity, same linked reading set). **No duplicate profile.** |
| 18 | **During SIA provisional-profile creation** | Whatever **SIA** durably committed | **Recover an already-committed profile, OR retry the SAME build identity from the SAME linked reading set** — **never from logs, never from raw audio.** Only after SIA's commit may `enrollment_provisional_profile_created` be written. |
| 19 | **Restart while an enrollment session was active** | The committed observations + the session-open commit (+ the capture-intent event and any B29 start result) | **The SESSION is `interrupted` and closed honestly**; **the microphone is NOT reopened**; **committed observations are preserved exactly**; **if no provable B29 outcome exists, capture-start reality is recorded as UNKNOWN — never as "never started"** (§6D). **The PARENT OPERATION may still continue** through roots → readings → eligibility → readiness → link → profile (§8A). **A new capture requires a NEW explicit enrollment operation** — new begin, fresh prerequisites, new pending, fresh token, **new session identity** — **never a reopening of the interrupted session.** |
| 20 | **A contradiction between an enrollment record and its actual owner** | **THE OWNER'S RECORD — always** | **Fail closed.** The EC's record is **coordination, not truth**. Record the contradiction; **block**; **never resolve it in the EC's favour.** |

## 22. RETRY BEHAVIOR

**Accepted B9 retry classifications and values are consumed BY
REFERENCE** — **no count, timeout, backoff, enrollment duration, or
sample target is invented here.**

**A technical retry may reuse the same stable parent operation ONLY
where** no fresh explicit Ness action is required **and** no security
authority is being recreated (e.g. re-submitting a frozen observation to
§7E after a transient failure).

**Never reuse:** an **expired, revoked, or consumed token**; **stale
prerequisite facts**; a **prior biometric result**; a **prior active
microphone session**; **stale SIA/SACL state**; or a **failed or
interrupted capture as though it continued.**

**A new enrollment session ALWAYS requires:** a **new explicit Ness begin
action**; **fresh prerequisite checks**; a **new BAI pending record**; a
**fresh token**; and a **new session identity.**

## 23. FAIL-CLOSED REQUIREMENTS

Stop, block, or close honestly when: **any prerequisite is missing,
stale, contradictory, or unverifiable**; **BAI already holds a pending
record**; **the biometric result has no matching pending record**; **the
`bai_token_consumed` event cannot be flushed and verified**; **the
authorization binding cannot be verified**; **a prerequisite changed
between the prompt and consumption**; **the session-open commit is absent
or not current**; **BOP cannot capture safely**; **§7Q/B7 excludes the
capture**; **§7E does not confirm acceptance**; **`append_root()`'s result
cannot be verified**; **an eligibility fact's owner is unavailable**;
**readiness cannot be established**; **§7L or SIA is unavailable**; **an
enrollment record contradicts its owner**; or **any required audit event
cannot be written and flushed.**

**Never treat unknown as success. Never let a coordination record stand
in for an owner's fact.**

## 24. MUST-NEVERS

Never: change Master V10, the Defaults, `cursorrules`, the Companion, the
Map, or any accepted file; create another authority for phone trust,
biometrics, privacy, identity, access, Person-Boxes, roots, or readings;
**treat biometric success as named identity**; **treat enrollment
provenance as confirmed voice identity**; **treat `role = "ness"` as an
SIA conclusion**; let BOP decide identity or spoofing; **let A15 physical
notes become identity facts**; store raw voice in logs; create a second
root-writing path; write to the sealed historical batch; bypass §7E, B11,
§7G, or quarantine; **silently discard rejected enrollment segments**;
**let rejected segments train the profile**; let logs or repeated copies
increase evidence weight; create a second profile store; auto-open
Personal Mode; unlock top-security; **claim the provisional ceiling is an
automatic access grant**; invent empirical values; complete **B-INT-8 or
Bundle 5**; complete **B29**; begin implementation; create code,
patch-ready pseudocode, schemas on disk, databases, stores, migrations,
tests, or Cursor instructions; mark this accepted, adopted, integrated,
implemented, or `PACKAGE_COMPLETE`; or commit or push.

## 25. EXPLICITLY OPEN AFTER B-INT-7

ChatGPT's independent audit; Ness's later acceptance; accepted-source
placement and a closure receipt; **B-INT-8**; **Bundle 5 final
consolidation and closeout**; later **Map/Master integration**;
**B29 REMAINS OPEN AND IS NOT COMPLETED BY B-INT-7** — its microphone,
device interaction, cleanup, transport, transcription, latency, timeout,
channel technology, algorithms, TTS, final field names, and complete
voice-pipeline mechanics are **B29's own work**; B-INT-7 defines **only
the boundary and its fail-closed behavior** (**its interfaces to B29/BOP
but does NOT complete B29**); exact microphone hardware and device
behavior; exact enrollment prompts and interface wording; **exact sample
count, duration, and quality thresholds**; **exact diarization and
spoofing algorithms**; **the exact profile-activation threshold**
(`enrollment_provisional` → `enrollment_active`); exact channel
technology; exact serialization and final implementation names; and
**every code, schema activation, database, store, migration, test, runtime
task, Cursor instruction, and live-disk change.**

## 26. FULL-FILE CONSISTENCY AND NO-LOSS SWEEP (DRAFTING CHECKS)

- **Correction 1 — the ORDER now matches Master §25.11 exactly:**
  readiness → the **immutable, non-authoritative
  `enrollment_profile_input_bundle`** → the §7L **PROPOSAL** → **§7L's
  OWN COMMITTED LINK TRUTH** → **only then** SIA's provisional profile →
  **only then** `enrollment_provisional_profile_created`. **The circular
  v1_0 sequence (profile → proposal referencing that profile → SIA
  consuming the proposal) is GONE.** **A proposal or acknowledgment alone
  is never enough**, and a **refused, pending, stale, contradictory, or
  unverifiable link BLOCKS the profile** (§12A, §13, §14, I11–I13, §8,
  crash 15–18) — consistent in drafting.
- **Correction 2 — the ownership boundaries hold:** **B29 owns the
  microphone**, the device, cleanup, transport, and the physical
  start/stop result (I5A); **BOP owns the DUMB observation records and
  owns NO microphone** (I5B); **BAI alone sources the
  `biometric:result:success` system-command — two fields, no purpose, no
  token, no biometric data, no identity claim — and the EC may coordinate
  its timing but NEVER fabricate or become its source** (I5C). **Raw voice
  stays inside the protected B29/BOP capture boundary** and never enters
  an EC record or ordinary log (§16). **B29 is interfaced, not
  completed** (§25) — consistent in drafting.
- **Correction 3 — the capture-start seam is honest:** the EC's
  **`enrollment_capture_intent_event`** proves only *about to request*;
  **B29's `enrollment_capture_started`** proves only that the pipeline
  began; **BOP observations remain the evidence of what was actually
  committed**; the three-way **started / confirmed-not-started /
  unknown** result is recorded truthfully; and **the absence of a BOP
  observation is NEVER proof that the microphone did not start** (§6D,
  crash 7b–9, 19). **The two lifecycles are separate** — a session may be
  `interrupted` while the parent operation continues to `completed`;
  **only legal nonterminal states transition; committed facts never
  regress; terminal results are never overwritten; one parent has at most
  one winning terminal result** (§8A, §8B). **The catalog is nine SETTLED
  events plus clearly marked PROPOSED coordination events — never
  "exactly nine"** (§18) — consistent in drafting.
- **The six prerequisites are carried verbatim, each with its real
  owner**, and the snapshot **records** rather than **owns** them (§4) —
  consistent in drafting.
- **The opening sequence matches Master §25.11 step for step**, with the
  prerequisite **re-read immediately before consumption** and the session
  opening **only after the durable proof is flushed** (§5) — consistent in
  drafting.
- **BAI's in-memory-only state is never post-crash proof** — the **flushed
  `bai_token_consumed`** is, bound through an **integrity-protected
  companion** that creates **no second BAI authority** (§6A, §6C, crash
  3/4/6) — consistent in drafting.
- **BAI's one-pending-record rule is respected, never bypassed**, and a
  replayed prompt dies on `bai_unmatched_result` (§6B) — consistent in
  drafting.
- **Nothing in this file turns biometric approval, `role = "ness"`,
  `enrollment_declared`, one recording, acoustic similarity, or the
  provisional link into proof of Ness's voice** — and **no lifecycle state
  says so either** (§1, §7, §8, §11, §13, §14) — consistent in drafting.
- **BOP stays DUMB**; the BAI `system_command` root carries **no purpose,
  no token id, no identity claim**, and has a **deterministic capture
  identity** so recovery cannot duplicate it (§7, crash 7) — consistent in
  drafting.
- **A15 is consumed exactly** — six fields, five names, physical evidence
  only, **never identity** — **and no threshold is chosen** (§7) —
  consistent in drafting.
- **Roots enter only after the session ends, only through §7E → B11 →
  `append_root()`, and never into the sealed batch; readings go to
  quarantine** (§10) — consistent in drafting.
- **All six eligibility checks are carried, including check 6's exact
  meaning** — one consistent live speaker, **not who** (§11) — consistent
  in drafting.
- **Rejected segments are preserved as roots; rejection is not deletion**,
  and **privacy exclusion (B7) is a different thing entirely** (§10, §11)
  — consistent in drafting.
- **The readiness boundary is mechanical only** — the counted set prevents
  duplicate counting, the rule and values belong to the accepted
  profile-integrity/SIA owners, it **fails closed**, and it is **not
  A29** (§12) — consistent in drafting.
- **The link is proposed, never approved, by the EC**; **`recognized_ness`
  is a CEILING, not a grant**; **SIA restart → unknown, SACL → guest**
  (§13, §14) — consistent in drafting.
- **Every identity has an idempotency scope; one parent log with child
  events; no record is evidence for itself; repetition adds no identity
  confidence** (§17, §20) — consistent in drafting.
- **Audit ownership is exactly Master's** — two BAI events, nine
  enrollment events, everything else with its owner; **only genuinely
  unnamed things are `[proposed]`** (§18) — consistent in drafting.
- **All twenty crash boundaries name an authoritative committed truth and
  an exact recovery action**, and **an owner-contradiction always fails
  closed in the OWNER's favour** (§21) — consistent in drafting.
- **No empirical value, threshold, algorithm, count, or duration is
  invented anywhere**; **B29 is interfaced, not completed**; **no new Ness
  question is asked** — the governing files revealed **no genuine
  unresolved meaning choice** blocking this package (§12, §14, §25) —
  consistent in drafting.

---

*End of `NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_0_CANDIDATE.md`
— `CANDIDATE — NOT ACCEPTED — NOT ADOPTED — NOT BUILT`, awaiting
ChatGPT's independent audit of this actual file and Ness's later
acceptance. The phone is trusted, Ness chooses to begin, the fingerprint
opens one narrow purpose-bound door, and a microphone records a voice that
N.H does not yet claim to know. Every root is kept, every rejected segment
is kept, nothing is reconstructed, and the profile that grows from it is
called what it is: provisional — a record of how the material arrived, not
a claim about whose voice it carries.*

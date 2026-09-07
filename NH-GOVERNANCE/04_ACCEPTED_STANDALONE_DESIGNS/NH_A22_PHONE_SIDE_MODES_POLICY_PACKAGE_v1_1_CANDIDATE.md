# N.H — A22 PHONE-SIDE MODES POLICY PACKAGE

**File:** `NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md`
**Version:** v1.1
**Register:** A22 — Five phone-side modes (Map Register A; component C-9) — **policy layer only**
**Intended placement:** `05_ACTIVE_CANDIDATE/`
**Date:** July 18 2026
**Status:** `CANDIDATE — NOT ACCEPTED — NOT ADOPTED — NOT AUTHORITATIVE — NOT INTEGRATED — NOT IMPLEMENTED`

**V1.1 CORRECTION NOTE (July 18 2026 — two bounded corrections only).** v1.1 was created by a direct copy of the untouched v1.0 candidate (SHA-256 `19e196cd50433f02c4609444b33072901da8ac3a827824bd3934f91d72fe1c61`, 211 lines, 14,615 bytes) and applies exactly the two corrections from the independent audit: **(1)** §5 now preserves **all five** Master V10 §7P emergency-stop conditions — v1.0 omitted the cannot-create-a-larger-consequence condition; **(2)** §§2, 3, and 7 now state the exact Master V10 §23 **two-door** mobile boundary — Manual Sync and Full Mode are the only doors into real N.H, and A22 creates no third. All other v1.0 meaning, structure, decisions, removals, boundaries, and deliberately open mechanical work are preserved unchanged. v1.0 remains preserved as history.

---

## 0. WHAT THIS FILE IS, AND WHAT IT IS NOT

This is a **policy-only standalone candidate** recording later standalone Ness decisions for A22 — the behavior policy of the phone-side modes. It exists for standalone review.

**Authority order governing this candidate:** (1) `NH_MASTER-20_CORRECTED_v10.md` — the current authoritative immutable Master, explicitly adopted by Ness on June 29 2026; (2) `NH_DECISION_DEFAULTS-S19_v2_2.md`; (3) `cursorrules`; (4) `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`. The Design and Wiring Map v1.6 is subordinate cross-reference. Master V10 governs every conflict.

Master V10 §9 carries the five phone-side mode names as **RECOVERED NAMES ONLY — BEHAVIOR NOT DESIGNED**: emergency record, breathing reminder, stealth toggle, night lockout, kill switch. Those five names were recovered placeholders whose behavior was not yet designed. **This candidate records Ness's later standalone A22 decisions about that feature set and its behavior policy.** It does not edit Master V10, does not modify the Map, and does not claim that Master or Map integration has already happened. The Master's frozen §9 wording remains untouched until a future separately authorized integration.

This candidate:

- supersedes **no** accepted or authoritative file by itself;
- authorizes **no** coding, implementation, store, migration, production schema, or Cursor instruction;
- becomes accepted **only** after ChatGPT independently audits the actual file and Ness explicitly accepts it;
- performs **no** Bundle 7 closure — A22 is one policy item inside Bundle 7's open scope.

---

## 1. UPDATED A22 FEATURE SET (Ness decision — standalone)

| Feature | A22 decision |
|---|---|
| **Emergency Record** | **REMAINS** |
| **Stealth Toggle** | **REMAINS** |
| **Breathing Reminder** | **REMOVED from A22** |
| **Night Lockout** | **REMOVED from A22** |
| **Kill Switch** | **REMAINS — essential specifically for Full Mode** |
| **Cloudflare Tunnel Off** | **ADDED — a separate ordinary Full Mode control** |

Breathing Reminder and Night Lockout are **removed**. They are not paused, not renamed, not deferred, and not waiting for later design. No replacement breathing, bedtime, focus, wellbeing, or phone-usage restriction feature is introduced by this package, and none is planned within A22.

A22's policy scope is therefore exactly four controls: Emergency Record, Stealth Toggle, Cloudflare Tunnel Off, and the Full Mode Kill Switch.

---

## 2. EMERGENCY RECORD — POLICY

Emergency Record records the active phone call.

**It MUST:**

- begin only when Ness deliberately starts it;
- stay private on the phone after recording;
- ask Ness exactly once, after the call, what to do with the recording.

**It MUST NOT:**

- start automatically, on a schedule, on a trigger, or silently — never;
- enter real N.H automatically;
- treat the recording as N.H material merely because it exists on the phone.

**The single after-call question offers exactly three choices:**

1. `Keep private` — the recording stays on the phone, private. Nothing is sent.
2. `Send whole call` — the complete recording is sent toward real N.H by Ness's deliberate action.
3. `Choose parts` — Ness deliberately selects parts; **only the selected parts** are sent.

**Excerpt marking.** Parts sent under `Choose parts` must be clearly marked as **excerpts of a longer call, not the complete call**. The excerpt marking is provenance: what was sent is a deliberately selected portion, and that fact stays visible.

**Sending is a deliberate transfer, not an entry.** Sending the whole call or selected parts into real N.H requires Ness's deliberate action **and** satisfaction of all existing protections: identity and authorization (Master §25; accepted B-INT-5 identity and Personal-Mode access wiring), privacy and capture-exclusion precedence (§7Q), provenance (Bundle 6 — the speaker and source are carried from the source, never guessed), and intake (§7E — the envelope is the only entry into root stores; the B11 active writable batch only; the sealed 5,521-root batch is never appended to).

**Sending uses the two existing doors only (Master §23).** There are exactly two doors from the phone side into real N.H — **Manual Sync** and **Full Mode** — and **A22 creates no third connection door**. Deliberate Ness action is required for both, but deliberate action alone does not create another permitted door: sending the whole call or selected excerpts cannot use a new direct A22-specific connection route. Any eventual transfer into real N.H must use one of those two existing authorized doors. This policy package does not choose which of the two doors carries each transfer; the exact routing and lifecycle remain later mechanical design (§6), and no later mechanical design may expand the two-door boundary or create an automatic connection.

**Sending does not permit direct entry into REALITY or any final memory layer.** Sent material never lands directly in REALITY, the sealed root store, the readings store, or any final memory layer. While Layer 2 remains active, `promote_to_memory()` remains the one authorized path for unverified content into REALITY (Master §12); nothing in A22 bypasses it.

---

## 3. STEALTH TOGGLE — POLICY

Stealth Toggle silently captures surrounding voices and sound.

**It MUST:**

- begin only when Ness deliberately activates it;
- produce **no spoken or audible N.H response** while active;
- keep the recording and any local understanding private on the phone.

**It MAY:**

- understand the live situation locally, on the phone;
- show silent text on the phone screen.

**It MUST NOT:**

- start automatically — never;
- speak, chime, or otherwise audibly respond;
- allow real N.H to remember or use the material merely because Stealth Toggle was active.

**When Ness stops Stealth Toggle, it provides exactly three choices:**

1. `Keep private` — recording and local understanding stay on the phone.
2. `Send whole recording` — the complete recording is sent toward real N.H by Ness's deliberate action.
3. `Choose parts` — Ness deliberately selects parts; only the selected parts are sent, clearly marked as excerpts rather than the complete recording.

Real N.H receives or uses Stealth material **only** after Ness deliberately sends the complete recording or selected parts **and** the existing identity, authorization, privacy, provenance, and intake protections in §2 above are satisfied. The same boundaries apply in full: any eventual transfer must use one of the two existing authorized doors — **Manual Sync or Full Mode** — with no A22-specific third route and with no door assignment chosen in this package; and there is no direct entry into REALITY or any final memory layer, ever.

**Speaker attribution.** Statements captured from another person must preserve their correct speaker attribution — the speaker is carried from the source, never guessed (Master carry-the-speaker rule; Bundle 6 A33 provenance-label meaning). Another person's statements **must never silently become facts about Ness**, and the third-party baseline (§7Q) applies in full: actual words are distinguished from interpretation, and nothing inferred is presented as fact.

---

## 4. CLOUDFLARE TUNNEL OFF — POLICY (ordinary Full Mode disconnect)

Cloudflare Tunnel Off is the **ordinary** Full Mode disconnect control. It is a normal end-of-session control, not an emergency control.

**It DOES, when Ness activates it:**

- close the current Cloudflare Tunnel;
- invalidate and end the current remote Full Mode phone session;
- end the phone's access to real N.H through that session.

**It DOES NOT:**

- activate by anyone or anything other than Ness;
- stop real N.H from running locally on the desktop;
- shut down the computer;
- stop or erase the independent local phone companion (Master §23 Modes 2/3) or its local memory;
- delete, rewrite, or alter any memory, root, reading, log, or record;
- reconnect automatically — a new Full Mode session requires a new deliberate Ness action (Master §23: the tunnel exists only inside a window Ness deliberately created and ends).

**Real N.H continues running locally after Tunnel Off.** Only the phone's remote session ends.

---

## 5. FULL MODE KILL SWITCH — POLICY (deliberate emergency hard stop)

The Kill Switch is **essential specifically for Full Mode**. It is **separate from Cloudflare Tunnel Off**: Tunnel Off is the ordinary disconnect; the Kill Switch is the deliberate emergency hard stop, activated by Ness from the phone.

**Required meaning — the Kill Switch MUST:**

- immediately end the phone's Full Mode access;
- close the Cloudflare Tunnel;
- invalidate and reject the current Full Mode session;
- stop and lock the real N.H software and active N.H services on the desktop;
- prevent further unfinished steps in the active phone-originated operation **where stopping can safely prevent additional effects**;
- leave the Windows computer powered on;
- require a **new deliberate Ness action** before N.H or Full Mode may restart or reconnect.

**The Kill Switch MUST NOT:**

- power off the entire computer;
- delete memories, roots, readings, logs, files, or records;
- rewrite history;
- undo, or claim to undo, completed real-world actions;
- send apologies, corrective messages, reversals, deletions, restorations, or compensation;
- automatically restart N.H;
- automatically reopen the tunnel;
- weaken any existing identity, access, privacy, gate, or Layer 2 protection.

**Master V10's narrow emergency-stop boundary applies (§7P).** The Kill Switch is a pre-authorized emergency stop in exactly the Master's narrow sense: it may stop something still actively underway to prevent **further** effects; it may not silently reverse completed actions, and any corrective action is a **new action requiring Ness's separate approval**. The emergency stop is permitted **only when all five §7P conditions apply simultaneously**: **(1)** the original action is still actively in progress; **(2)** stopping prevents additional effects rather than undoing completed effects; **(3)** the stop mechanism is mechanically bounded and previously authorized; **(4)** stopping cannot reasonably create a larger consequence than continuing; **(5)** the emergency stop and its authority basis are immediately recorded and surfaced to Ness. How condition (4) is tested, thresholded, detected, or enforced is **not designed here** — those enforcement mechanics remain open for B30 (§6). Completed-world reversal and corrective actions require Ness's separate approval — the Kill Switch changes nothing about that.

**The independent local phone companion remains separate.** Stopping desktop N.H does not erase, merge, or alter the phone companion's local memory (Master §23: the local AI is completely independent of REALITY/SIMULATION and never auto-connects).

---

## 6. MECHANICAL WORK THAT STAYS OPEN (deliberately not designed here)

This is a policy package. **B30 mechanics are not chosen or designed inside it.** The following matters are explicitly left for **B30 (Mobile Full-Mode mechanical owner)** and later mechanical design, and are **mechanical architecture matters, not new Ness policy questions**:

- exact `nh_auth.py` wiring;
- secure delivery of Tunnel Off and Kill Switch commands;
- behaviour when the tunnel is frozen, unreachable, or already failing;
- tunnel creation and closure sequence;
- session invalidation mechanics;
- safe N.H service-stop order;
- handling of unfinished operations;
- accidental-activation protection;
- exact button interaction;
- exact interface labels, icons, and placement;
- operation identities;
- append-only logging and §0B records;
- idempotency;
- duplicate prevention;
- timeout and failure behaviour;
- crash recovery;
- partial-stop recovery;
- verification that N.H actually stopped;
- deliberate restart and reconnection mechanics;
- the **C11** dangerous-path-removal dependency (`nh_pc_agent.py` raw `run:` trigger — removed and verified before mobile/Full Mode go-live; a pre-go-live code task, never performed during design; blocks B30 go-live).

No implementation is invented for any of these. Their exact routing, records, and failure behavior are owned by the mechanical design that will carry them.

---

## 7. BOUNDARIES, DEPENDENCIES, AND STATUS

- **A22 policy behaviour is specified for standalone review.** That is this file's entire function.
- **No coding or implementation is authorized** by this candidate — anywhere, for anything.
- **No Master or Map integration is performed.** Master V10 §9's frozen wording stands until a separately authorized future integration.
- **No accepted or authoritative file is superseded by this candidate itself.**
- **Acceptance path:** this candidate becomes accepted only after ChatGPT audits the actual delivered file and Ness explicitly accepts it. Ness runs any commit.
- **A22 completion does not close Bundle 7.** A20 (mobile open questions), A21 (final Interactive Translator model), A23 (conversation-rehearsal mechanism), A24 (legacy-layer coexistence and handoff policy), B29 (voice-pipeline mechanical owner), B30 (Mobile Full-Mode mechanical owner), B-INT-10 (legacy-layer coexistence design), and all other unfinished Bundle 7 work remain separate and open.
- **Layer 2 remains active and protected** (Master §12): the still-running REALITY/SIMULATION gate stack is not weakened by anything in this package and remains in force until Ness separately and explicitly authorizes its decommissioning (the decommissioning decision itself is A24).
- **Nothing connects automatically to real N.H — ever, and there are exactly two doors in** (Master §23): **Manual Sync** and **Full Mode**, both requiring deliberate Ness action. Deliberate action alone does not create another permitted door. **A22 creates no third connection door**, assigns no transfer to a specific door, and does not decide Manual Sync content scope (that is A20); no later mechanical design may expand the two-door boundary or create an automatic connection. Every A22 control preserves this rule exactly.

---

## 8. SOURCES AND PROVENANCE

Governing sources read for this candidate, at repository head `d2c48f40ae20845c10f950ddd7c9c0221f33f83b`: Master V10 (`2d9ed4c6…` — §9 five phone-side modes and voice pipeline status; §12 layer model and Layer 2; §23 mobile three-mode companion and the nothing-automatic rule; §25 raw-voice-data protection and the Full-Mode-tunnel transmission boundary; §7P permission/authority boundaries, stop-and-surface, and the narrow emergency-stop exception; §7Q third-party baseline and capture-exclusion precedence; §7E intake envelope); Decision Defaults S19 v2.2; cursorrules v3.2; Map v1.6 (C-9 component entry; Register A items A20–A24; Register B items B29, B30; B-INT-10; Register C item C11); the eight-bundle dependency plan v1.0; accepted Bundle 5 records — B-INT-5 identity and Personal-Mode access wiring v1.5 with its closure record, and the Bundle 5 final consolidation and closeout v1.1; accepted Bundle 6 records — the Bundle 6 policy decisions v1.0 (A33 provenance-label meaning) and the Bundle 6 final consolidation closeout v1.2 (live-capture row: §7E envelope as the only entry; B11 active writable batch only; speaker carried from source).

**No-loss statement:** this candidate is a new standalone file. It changes no existing file, reopens no settled decision, and invents no policy beyond the Ness decisions it records. The five-name recovery status in Master V10 remains frozen as history; the A22 decisions recorded here await their own acceptance and, later, their own separately authorized integration.

*Claude builds the bridge. Ness chooses where it goes. ChatGPT checks that the bridge still matches the chosen destination.*

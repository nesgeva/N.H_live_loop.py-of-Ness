# NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md

## 0. STATUS BLOCK

**Status:** `CANDIDATE` — not accepted, not adopted, not authoritative,
not integrated, not implemented. **Policy record only.** It records
Ness's newly approved **A26** decision about how the existing **§25
identity system** and the existing **§9 Dry/Personal/step-up access
model** work together. It changes no existing rule, redesigns no
existing gate, invents no mechanics, chooses no neighboring policy,
completes no B-INT-5 work, creates no acceptance receipt, marks
nothing complete, and authorizes no code, build, store, UI, or
live-system work. Master V10, the Map, the Defaults, cursorrules, and
every accepted file remain byte-identical.

**Date:** July 13, 2026.

**Version note (v1_1):** narrow correction of v1_0 only, closing one
important overreach found by ChatGPT's independent audit of the actual
v1_0 file. v1_0 stated that a §25 `recognized_ness` assessment is the
identity **precondition** for Personal Mode and that "identity
verification" for Personal Mode **means** the §25 layer establishing
recognized Ness plus Ness's explicit opening act. Those claims
prematurely chose how the existing identity factors connect and could
displace the settled §9 factor hierarchy (fingerprint = strongest
factor; PIN = normal gate; voice = soft convenience factor, never a
hard lockout). **A26 does not decide the exact working combination
among PIN, §25 recognition, fingerprint, and Ness's explicit Personal
Mode opening act — that remains later B-INT-5 mechanical design,
bound to preserve the §9 hierarchy and the §25 rules.** v1_1 removes
the overreaching claims (§4.1, §4.2, §4.3, §8 check 1), carries the
decision in its corrected six-statement form with a stated-clearly
boundary list (§2), keeps the exact everyday sentence (§3), adds the
factor-combination and final-factor-sequence items to the open list
(§6) and the corresponding must-nevers (§7), binds B-INT-5 to the
preservation constraint (§5), and adds safety check 7 (§8). **The
approved decision is unchanged in substance; no other boundary
changed.** v1_0 (SHA-256
`5a1dd006ffd779097cc8e35a6b07189a250456dd780ce2dd72d2b9dd63df4de8`;
321 lines; 16,680 bytes) is preserved unchanged as historical
candidate provenance.

**Register item:** A26 — Bundle 5 policy work (Bundle 5 — Privacy,
security, access, and TSC authority — the current unfinished bundle;
this is in-order Bundle 5 work and closes nothing else in Bundle 5).

**Intended repository placement:** `05_ACTIVE_CANDIDATE/`
(the physical move into the repository is Ness's action).

**Pinned repository snapshot for all disk verification:**
`nesgeva/NH-GOVERNANCE`, branch `main`, commit
`f7ce911574b937394ec933273717b0abebf2dc4a`.

## 1. GOVERNING AUTHORITY AND SOURCES READ

**Governing authority order:**
1. `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`
   (adopted by Ness June 29, 2026; governing — Master V10 wins every
   conflict)
2. `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`
3. `01_AUTHORITATIVE/cursorrules`
4. `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`

**Sources read, byte-verified at the pinned snapshot** (every shared
file confirmed byte-identical across this session's pinned commits
`5108f575…` → `af0f1a5a…` → `f97882c7…` → `f7ce9115…`):

- **Master V10** (`2d9ed4c6…`; 5,736 / 506,934) — read for this
  candidate specifically: the **§9 recovered access and
  authentication model** block (Dry/Personal/step-up, factor
  hierarchy, raw-vs-derived boundary, exact-quote exception,
  trusted-app-only, zero-copy, code-level Dry/Personal separation);
  **§25** — 25.1 BOP (status and boundaries), **25.3 SIA** in full,
  **25.4 SACL** in full (gates, in-progress-operation discard, output
  gate order, fail-closed set, protected-core rules), 25.5
  Wellbeing/Identity/Security separation (recognition-suppression
  boundary), 25.6 BAI with the **Top-Security Biometric Lease** and
  its revocation triggers; and **§7Q** in full (earlier this session;
  byte-identical), including the Level-2 default-eligibility sentence
  and the ★ CENTRAL RULE.
- **Defaults S19 v2_2** (`6cd09329…`; full, earlier this session).
- **cursorrules** (`5050d088…`; targeted, design-phase rules).
- **Companion** (`cdcc6134…`; targeted, governance and roles).
- **Map v1.6** (`33af648d…`) — the **A26**, **B-INT-5**, **A7**,
  **A15**, and **A16** Part II register entries read verbatim on disk
  for this candidate; security-group component context from earlier
  session reads.
- **Eight-bundle plan** (`2d6483d1…`) — full earlier this session;
  the **Bundle 5** section re-read on disk for this candidate.

No summary was substituted for an available file.

## 2. THE APPROVED A26 DECISION — RECORDED FAITHFULLY

The Map's A26 entry reserved to Ness the choice between "one combined
model, separate layers, or distinct mechanisms with a defined
boundary" for the relationship between the §9 access model and the
§25 SIA/SACL/BAI architecture. **Ness has decided: separate
cooperating layers, with the boundary defined below.** The decision,
recorded faithfully and without expansion:

1. **The §25 identity/access system and the §9 mode system are
   separate cooperating layers.**
2. **N.H determining or recognizing who is present does not
   automatically open Personal Mode.**
3. **Ness separately and explicitly opens Personal Mode.**
4. **Inside the properly authenticated private Personal Mode context,
   §7Q's existing private-access default and all existing exceptions
   apply unchanged** — Ness's normal private information is eligible
   by default for his authenticated private use, **except** where an
   existing explicit restriction, exclusion, redaction,
   deletion-from-view, compartment rule, unresolved case, or
   protected-secret rule applies.
5. **Personal Mode does not unlock top-security.**
6. **Uncertainty reduces access, and protected output stops before
   private information is exposed.**

**Stated clearly — what A26 decides and what it leaves open:**

- recognition alone is **insufficient** to open Personal Mode;
- an **explicit opening act is additionally required**;
- A26 does **not** declare `recognized_ness` to be the only possible
  identity proof or a universally mandatory factor;
- A26 does **not** declare PIN, voice recognition, fingerprint, or
  any single factor sufficient by itself;
- the exact working combination among PIN, §25 recognition,
  fingerprint, and Ness's explicit Personal Mode opening act is **not
  decided by A26** — it remains later B-INT-5 mechanical design;
- **B-INT-5 must preserve the existing §9 factor hierarchy**
  (fingerprint = strongest factor; PIN = normal gate; voice = soft
  convenience factor, never a hard lockout) **and the §25 security
  rules** while designing how the two layers cooperate;
- top-security continues to require its already-settled
  fingerprint-plus-independent-identity conditions.

## 3. THE EVERYDAY RESULT, PLAINLY

N.H may recognize Ness and still remain outside Personal Mode. Ness
chooses when to open his private N.H. Opening Personal Mode does not
automatically unlock top-security material.

Put simply: **"N.H knowing it is Ness and Ness choosing to open his
private N.H are two different things."** The vault above them
(top-security) has its own separate key. If N.H ever becomes unsure
who is present while the private N.H is open, it goes quiet about
private things first and sorts out identity second.

## 4. HOW THIS FITS THE EXISTING RULES — CONSISTENCY RECORDED, NOTHING CHANGED

**4.1 With §25 (SIA / SACL / BAI).** Identity determination stays
entirely SIA's; access-level decisions stay entirely SACL's; the four
settled access levels (`top_security` / `recognized_ness` /
`known_person` / `guest`), the Gate 0–3 calculations, the
imitation-risk Option-A rule, the multi-speaker minimum rule, the
protected-core rules, and the fail-closed set (restart → guest; stale
assessment → downgrade; SIA failure → guest) are untouched. A26 adds
only the **layer boundary**: knowing who is present — at whatever
level and on whatever factor evidence the settled §25 rules produce —
never itself opens Personal Mode. A26 does **not** select which §25
level or which identity factor participates in the Personal Mode
opening, does not make `recognized_ness` a mandatory precondition, and
does not redefine any level; the exact working combination is B-INT-5
mechanical design under the constraints in §2. Nothing in this
candidate raises, lowers, or re-derives any §25 level.

**4.2 With §9.** The recovered accepted §9 model is untouched: Dry
Mode (no personal data accessed), Personal Mode (full personal access
after identity verification), graduated temporary step-up, the factor
hierarchy (fingerprint strongest; PIN normal; voice soft, never hard
lockout), the raw-versus-derived boundary, the exact-quote exception,
trusted-app-only access, zero-copy behavior, and the real code-level
Dry/Personal separation all stand exactly as written. A26 defines the
**layer relationship** only: §9's "identity verification" for
Personal Mode keeps its settled §9 meaning under the settled factor
hierarchy, and A26 adds that an **explicit opening act by Ness is
additionally required** on top of whatever identity verification the
later mechanics use. A26 does **not** decide the exact working
combination among PIN, §25 recognition, fingerprint, and the explicit
opening act — that remains B-INT-5 mechanical design, which must
preserve the §9 factor hierarchy and the §25 security rules. What
exact information is reachable in Dry Mode beyond §9's own stated
rules is **not defined here** and is not invented here.

**4.3 With §7Q.** Inside the properly authenticated private Personal
Mode context, the existing §7Q rules operate exactly as already
written — this candidate
adds no new eligibility and removes none. The §7Q ★ CENTRAL RULE
("Private access for Ness is open by default unless Ness explicitly
restricts it. External exposure and secondary uses are restricted by
default.") and the §7Q Level-2 sentence ("For Ness's authenticated
private use, this material is eligible by default unless Ness
explicitly restricted or hid it, it was excluded/redacted/deleted, an
unresolved deletion case applies, it contains non-negotiably excluded
secrets, or another explicit compartment rule applies.") are consumed
unchanged. A26's contribution is only to make the **context** concrete:
"Ness's authenticated private use" — the authorized authenticated
private-use context in which that default applies — is **the properly
authenticated private Personal Mode context: Personal Mode explicitly
opened by Ness**, under whatever identity-verification mechanics
B-INT-5 later designs within the settled §9 factor hierarchy and §25
rules. Every §7Q exception category
binds unchanged; external-exposure and secondary-use defaults are
untouched; §7Q's protections are not weakened in any way.

**4.4 With top-security.** Top-security remains the separate higher
gate exactly as settled: SACL Gate 1 (biometric verified within
timeout, Ness's Person-Box, certainty at or above the top-security
threshold, sufficient score separation, no spoofing suspicion, no
disqualifiers, no imitation-risk flag), the Top-Security Biometric
Lease with its full revocation-trigger set, and the settled rule that
**fingerprint alone does not restore top-security** when speaker
assessment remains uncertain or suspicious. Opening Personal Mode
satisfies none of Gate 1's conditions by itself and unlocks no
top-security material.

**4.5 Fail-closed direction.** "Uncertainty reduces access, never
expands it" is the same direction §25 already enforces (unknown or
uncertain speakers receive guest unconditionally; stale assessments
downgrade; on any access reduction, in-progress operations above the
new level are discarded **before any output channel is written**). A26
carries that same direction across the mode joint: an identity-
confidence drop while Personal Mode is open must stop protected output
safely **before** anything private is exposed. The exact mechanical
form of that stop at the mode layer belongs to B-INT-5 (§6) — the
direction is decided; the mechanics are not designed here.

**4.6 Everyday availability preserved.** The §25.5 separation rules
stand untouched: wellbeing-tier actions never erase identity, never
convert Ness to guest, and never suppress recognized_ness access; Dry
Mode, research, and normal thinking-partner operation remain
available. Guest and known-person protections (Gate 0, Gate 3, PBR
category enforcement, Ness-presence requirement, no indirect
disclosure) are preserved without modification.

## 5. WHAT THIS DECISION UNLOCKS — B-INT-5

The Map's B-INT-5 entry is the mechanical wiring "that follows
whichever relationship Ness chooses in A26 — one combined model,
separate layers, or distinct mechanisms with a defined boundary," with
the explicit dependency **A26 → B-INT-5** (→ C-9 / CY-I). With A26
decided as **separate cooperating layers with the boundary in §2**,
B-INT-5's dependency is satisfied at policy level and its design work
is unlocked — as later, separate, Bundle 5 mechanical work under the
plan (alongside B-INT-6's settled §7Q-first, SACL-second output
chain). **B-INT-5 must preserve the existing §9 factor hierarchy and
the §25 security rules while designing how the two layers cooperate,
including the exact working combination among PIN, §25 recognition,
fingerprint, and Ness's explicit opening act — none of which is chosen
here. Nothing of B-INT-5 is designed, begun, or completed inside this
policy file.**

## 6. EXPLICITLY OPEN FOR THE LATER B-INT-5 PACKAGE

All of the following remain open, unanswered, and unbiased here:

- the exact open/close sequence for Personal Mode;
- the exact working combination among PIN, §25 recognition,
  fingerprint, and Ness's explicit Personal Mode opening act, and the
  final factor sequence;
- the exact safe response when identity confidence changes;
- session timing, timeout, restart, and crash behavior;
- operation records and duplicate prevention;
- interface wording and visible indicators;
- the exact connection between mode state and retrieval/output gates.

Also untouched and unchosen, each remaining with its own register
owner: **A7** (§7Q privacy eligibility, evaluation order, and
influence-removal policy — none of its reserved policy areas is
answered here), **A15** (the BOP `acoustic_condition_notes` amendment
— pending, not activated, not decided here), and **A16** (the TSC
archive-event rename — not adopted or rejected here). All §25
thresholds remain empirically calibrated configuration values; every
other Bundle 5 item (B7, B15, B-INT-4, B-INT-6, B-INT-7, B-INT-8)
remains exactly as the plan holds it.

## 7. MUST-NEVER BOUNDARIES

This candidate — and any later work consuming it — must never:

- change Master V10, the Map, the Defaults, cursorrules, or any
  accepted file, or overwrite or rename any existing file;
- invent which exact information is available in Dry Mode;
- invent the exact command, button, voice phrase, timeout, automatic
  closing rule, restart behavior, screen indicator, fingerprint
  prompt, or final factor sequence (B-INT-5 and its owners);
- declare `recognized_ness` the only possible identity proof or a
  universally mandatory factor, declare PIN, voice recognition,
  fingerprint, or any single factor sufficient by itself, or displace
  the settled §9 factor hierarchy;
- redesign guest, known-person, recognized-Ness, or top-security
  rules, gates, thresholds, or leases;
- weaken §7Q's protection rules, exception categories, or
  external-exposure defaults;
- treat recognition as Ness as silently opening Personal Mode, or
  treat Personal Mode as unlocking top-security;
- let uncertainty widen access anywhere;
- choose A7, A15, or A16, or complete B-INT-5 inside this policy
  file;
- create an acceptance receipt, or mark this candidate accepted,
  adopted, authoritative, integrated, implemented, or Bundle 5
  complete;
- write code or begin building.

## 8. REQUIRED SAFETY CHECKS — VERIFIED

1. **No conflict with §7Q's open-by-default rule for Ness:** verified
   — the decision's statement 4 applies §7Q's existing default
   *inside* the properly authenticated private Personal Mode context
   and carries §7Q's
   own exception list unchanged; the ★ CENTRAL RULE and the Level-2
   sentence were re-read on disk and are consumed, not modified
   (§4.3). Requiring Ness's explicit opening act gates the **context**,
   not the eligibility within it.
2. **Recognition alone is not silently treated as opening Personal
   Mode:** verified — decision statements 2–3 and the stated-clearly
   list say it directly; no
   sentence in this candidate creates an automatic, implied, or
   default opening path; the opening act's exact form is open (§6).
3. **Top-security still requires fingerprint plus the existing
   identity conditions:** verified — §4.4 records Gate 1, the
   Biometric Lease and its revocation triggers, and the settled
   fingerprint-alone-is-not-enough rule, all unchanged; Personal Mode
   satisfies none of them.
4. **Uncertainty fails closed:** verified — decision statement 6
   points the same direction as §25's settled fail-closed set,
   including discard-before-output on access reduction (§4.5); no
   path here expands access under uncertainty.
5. **All existing guest and known-person protections preserved:**
   verified — Gate 0, Gate 3, PBR category enforcement, the
   Ness-presence requirement, unconditional guest for
   unknown/uncertain speakers, and no-indirect-disclosure stand
   untouched (§4.1, §4.6).
6. **All authority files unchanged:** verified — Master V10, the
   Defaults, cursorrules, the Companion, the Map, and the plan were
   byte-verified at the pinned snapshot before and after writing;
   nothing was edited, and this candidate integrates into none of
   them.
7. **The §9 factor hierarchy is preserved and no factor combination
   is chosen:** verified — the stated-clearly list (§2) declares no
   single factor sufficient and `recognized_ness` not universally
   mandatory; §4.1 and §4.2 select no §25 level and no factor as the
   Personal Mode precondition; the combination and the final factor
   sequence are carried open in §6; B-INT-5 is bound to preserve the
   §9 hierarchy and the §25 rules (§5).

## 9. STATUS

`CANDIDATE` — awaiting ChatGPT's independent audit of this actual file
and Ness's explicit acceptance afterward. Until then it changes
nothing.

## 10. CHANGE REPORT AND SELF-AUDIT

**File created:**
`NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md`
— the only file created by this task, produced by copying the
identity-verified v1_0 base (SHA-256 `5a1dd006…4de8`; 321 lines;
16,680 bytes) and applying only the overreach correction and its
dependent edits (title; status-block version note; §2 corrected
decision form plus stated-clearly list; §3 exact everyday sentence;
§4.1, §4.2, §4.3 corrected; §5 B-INT-5 preservation constraint; §6
factor-combination and final-factor-sequence opens; §7 added
must-nevers; §8 corrected references plus check 7; this §10; the end
line). v1_0 is preserved unchanged as historical candidate provenance.
**Nothing existing was modified:** Master V10, the
Decision Defaults, cursorrules, the Companion, the Map v1.6, the
eight-bundle plan, every accepted package, every acceptance and
closure record, and all historical candidates remain byte-identical at
the pinned snapshot `f7ce9115…`. Nothing was committed, pushed, moved,
renamed, overwritten, or deleted. No mechanics, commands, indicators,
timeouts, thresholds, or interface elements were invented; no
neighboring policy (A7, A15, A16) was chosen; B-INT-5 was identified
but not begun; no acceptance receipt was created; no code was written
and no building began.

**Self-audit:** decision recorded faithfully in its corrected form, in
Ness's approved terms, matching exactly one of the three options the
A26 register entry reserved, with the stated-clearly boundary list
present — PASS. No §25 level and no identity factor selected as the
Personal Mode precondition; the §9 factor hierarchy preserved intact;
the exact factor combination left to B-INT-5 under an explicit
preservation constraint — PASS. Fit with §7Q, §9, §25 explained by
reference with all existing rules consumed unchanged and re-read on
disk (§9 block; §25.3; §25.4; 25.5 boundary; Biometric Lease; §7Q
central rule and Level-2 sentence) — PASS. B-INT-5 identified with its
register wording and dependency, unlocked but untouched — PASS. All
seven B-INT-5-facing opens carried without answers; A7/A15/A16 named
and unchosen — PASS. All seven required safety checks verified with
disk-grounded statements — PASS. Exactly one candidate file created;
zero repository modifications; no implementation or integration —
PASS.

---

*End of
`NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md`
— `CANDIDATE`, unaudited, awaiting ChatGPT's independent audit of this
actual file and Ness's explicit acceptance afterward. v1_0 is
preserved unchanged as historical candidate provenance. The A26
decision is recorded in its corrected form: identity and mode are
separate cooperating layers; recognition never opens Personal Mode by
itself; Ness opens it explicitly; inside the properly authenticated
private Personal Mode context §7Q's existing default applies with all
its exceptions; Personal Mode does not unlock top-security;
uncertainty only ever reduces access and protected output stops before
private exposure. No single factor is declared sufficient, no factor
combination is chosen, and the §9 factor hierarchy stands untouched —
the exact combination is B-INT-5's later work under an explicit
preservation constraint. B-INT-5 is unlocked, not begun. Nothing
existing changed; nothing was implemented.*

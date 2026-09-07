# NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md

## 0. STATUS BLOCK

**Status:** `CANDIDATE — NOT ADOPTED — NOT BUILT.` Complete standalone
A7 concept-and-policy package covering privacy, visible use, internal
influence, third-party information, safe transformation, pause/restore
behavior, interpretation, simulation permission, and large imported
collections. It records Ness's approved A7 decisions exactly,
preserves every compatible settled rule from Master V10 and the
current Map, and states each Ness-approved supersession of older
Master wording explicitly and narrowly. **Master V10 itself is not
edited by this candidate** — supersessions are recorded here, history
stays intact, and integration is later versioned work. Not accepted,
not adopted, not authoritative, not integrated, not implemented; no
code, schema-finalization, store, UI, or live-system work is performed
or authorized.

**Date:** July 13, 2026.

**Version note (v1_1):** narrow correction pass on v1_0 only, applying
the four corrections from ChatGPT's independent audit of the actual
v1_0 file. (1) **Visible suppression and internal influence removal
fully separated:** §4.9 had listed "removed influence" among the
conditions closing Ness's visible private use — too broad and in
conflict with the settled scope rule; v1_1 makes influence removal a
separate internal-use control that blocks visible output only when
Ness's instruction includes visible output, states both directions of
the separation (§4.2, §4.9), and corrects the easy-language section so
the two are separate, combinable controls. (2) **Sensitivity-to-
handling mapping corrected:** v1_0's "no automatic mapping" overreach
is replaced by the accurate policy — the settled four sensitivity
levels and material types continue to select their already-defined
protections; only the automatic minor/vulnerability restriction is
rejected. (3) **A7 closed at the policy level:** the two "concept
remnants" (finer purpose taxonomy; complete control catalog) were
misclassified — purpose policy and person-specific control policy are
sufficiently settled; representations and refinements are B7 mechanics
or optional later versions; no new Ness question exists. (4) **Live
secrets stated precisely** in the easy-language section: ordinary
reading, retrieval, reasoning, and model context cannot access Level-1
secrets; only an authorized protected-boundary function handles them;
only the minimum safe result leaves; the raw secret stays unavailable
to ordinary components. **Exactly two Master supersessions remain,
unchanged (§6). No approved decision, boundary, or settled rule was
reopened or weakened.** v1_0 (SHA-256
`6ac3ce1127fb1405f7d8499209a7bab9085d3b93d9ac925979cb42ae2bead800`;
639 lines; 34,496 bytes) is preserved unchanged as historical
candidate evidence.

**Register item:** A7 — Bundle 5 policy work (Bundle 5 — Privacy,
security, access, and TSC authority — the current unfinished bundle).
The B7 mechanical package remains separate and open.

**Intended repository placement:** `05_ACTIVE_CANDIDATE/`
(the physical move into the repository is Ness's action).

**Pinned repository snapshot for all disk verification:**
`nesgeva/NH-GOVERNANCE`, branch `main`, commit
`4f267a2744c5bc932e299f3f87c2a03d8d9e591e`.

## 1. GOVERNING AUTHORITY AND SOURCES READ

**Governing authority order:**
1. `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`
   (adopted by Ness June 29, 2026; governing — Master V10 wins every
   conflict, including the recorded D2 vocabulary divergence: §7Q's
   six privacy operations and history-record deletion vocabulary
   govern over the Defaults' older five-operation wording)
2. `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`
3. `01_AUTHORITATIVE/cursorrules`
4. `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`

**Sources read, byte-verified at the pinned snapshot** (every shared
file confirmed byte-identical across all this session's pinned
commits; the only repository changes across pins are Ness's own
commits of previously delivered files, each verified byte-identical to
its delivered copy):

- **Master V10** (`2d9ed4c6…`; 5,736 / 506,934) — for this candidate
  specifically: **§7Q in full**, including the deletion history-record
  and unresolved-case rules, the CAPTURE EXCLUSION two-layer system,
  the THIRD-PARTY DATA RULES (universal baseline, context-sensitive
  variance list, Ness configuration, the four-operations ladder, the
  simulation/minors/large-volume/public-availability sentence), the
  TWO-STAGE OUTPUT ACCESS CONTROL (★ CENTRAL RULE, ★ purpose rule,
  Layer 1, Layer 2), the model-provider-limitation rule, the
  fail-closed and record rules, and the "Remaining undesigned" list;
  the **§9** recovered access-model block; **§11 item 30**
  (wonder/simulation scratch-space boundary); the **"#### 25.
  Privacy, Exclusion, Restriction, Deletion, and Third-Party
  Handling"** TSC-region precedence subsection; plus the earlier
  session reads (§25.3 SIA, §25.4 SACL, BAI/Biometric Lease, §0–§0B,
  §7D–§7R).
- **Defaults S19 v2_2** (`6cd09329…`; full, earlier this session).
- **cursorrules** (`5050d088…`; targeted, design-phase and protection
  rules).
- **Companion** (`cdcc6134…`; targeted, governance and roles).
- **Map v1.6** (`33af648d…`) — for this candidate specifically: the
  **C-7Q** component entry in full; the **A7** and **B7** Part II
  register entries verbatim; **B-INT-6** (§7Q-first, SACL-second
  chain); **D2** (privacy-vocabulary divergence); plus the session's
  earlier entry reads.
- **Eight-bundle plan** (`2d6483d1…`; full earlier; Bundle 5 section
  re-read).
- **Accepted A26 package** (`41e1f67d…`, in
  `04_ACCEPTED_STANDALONE_DESIGNS/` at the pin) — the identity/mode
  layer boundary this candidate must stay consistent with.
- Relevant accepted packages by reference: Bundle 2 (§7Q before
  relevance), Bundle 1/B24 and B-INT-6 (§7Q first, SACL second),
  Bundle 4 (§7N/§7P action boundaries).

No summary was substituted for an available file.

## 2. PURPOSE AND PLAIN MEANING

A7 is the concept-and-policy layer of N.H's privacy system: the rules
for what N.H may read, keep, connect, say, transform, pause, restore,
interpret, and — only with approval — simulate; how other people's
information is handled inside Ness's private N.H; and what never
leaves the private context without the right authorization. B7 later
builds the enforcement machinery under these rules. In one sentence:
**Ness's private N.H is open to Ness by default and closed to the
outside by default, it obeys Ness's natural words about what to pause
and what to bring back, it may think about people honestly as long as
guesses stay guesses, and it never quietly turns anyone into a fixed
profile or a secret simulation.**

## 3. THE SETTLED FOUNDATION — PRESERVED WITHOUT LOSS

All of the following stands exactly as settled; this candidate
consumes it unchanged and builds only on top of it:

1. **Six privacy operations** (exclusion, sealed isolation, hiding,
   restriction, redaction, deletion-as-non-destructive-visibility-
   removal) with **two protection levels** (L1 live
   secrets/credentials inside a protected execution boundary, opaque
   ids, never destroyed; L2 private personal, available to Ness after
   identity verification with no per-access permission) and **four
   sensitivity levels** (general / sensitive-personal / third-party /
   credentials-high-harm).
2. **No destruction, ever.** Deletion is visibility removal with a
   full derivative/index/embedding/cache/export/backup search, five
   recorded outcomes, and a history record whose content remains
   preserved — never a content-free tombstone. Unresolved deletion
   cases: immediate visible-output prevention; internal preservation
   and connections continue unless Ness separately instructs.
3. **Capture exclusion, two layers:** Layer A non-negotiable core
   (live credentials → sealed protected storage, never ordinary
   stores/logs/indexes/backups, cannot be disabled, never destroyed);
   Layer B Ness-configured exclusions; sensitive-but-context-dependent
   material is **not** auto-excluded merely for being sensitive;
   mixed-content isolation with protected pre-ingest holds;
   non-reconstructive metadata only in ordinary records.
4. **Third-party universal minimum baseline** — for every person other
   than Ness, without exception: preserve source and speaker;
   distinguish the person's actual words or actions from Ness's
   interpretation and from N.H's interpretation; never present
   inferred feelings, intentions, diagnoses, motives, or private
   states as facts; no external sharing without Ness's specific
   authorization; relevance alone never authorizes use; no silent
   expansion into a fixed profile. Ness may configure person- or
   group-specific rules that make protection **stricter**; nothing
   removes the baseline.
5. **★ CENTRAL RULE:** private access for Ness is open by default
   unless Ness explicitly restricts it; external exposure and
   secondary uses are restricted by default. **★** N.H may use
   material when the current purpose is authorized; it blocks
   material from unauthorized uses, not from Ness's own understanding
   by default.
6. **Two-stage visible-output control:** Layer 1 pre-retrieval
   eligibility (Ness's private use eligible by default; "sensitive"
   alone is never a sufficient reason to withhold from Ness; the
   settled block-conditions list; other purposes restricted by
   default; ineligible material never reaches the mouth, views,
   exports, or visible output; **privacy filtering runs before
   semantic ranking**), then Layer 2 pre-output review (the settled
   specific checks; not an emotional-sanitization filter; truthful
   relevant material is never softened, omitted, or replaced merely
   because it may upset Ness).
7. **Visible suppression ≠ internal influence removal.** Deletion,
   hiding, restriction, and sealed isolation do not automatically
   remove internal influence, internal retrieval for internal
   reasoning, internal analysis, internal simulation, or internal
   connections; stopping internal influence requires a **separate
   explicit influence-removal instruction from Ness with recorded
   scope** — settled in Master §7Q and kept as the backbone of §4.2
   below.
8. **Order of gates, settled:** capture exclusion as early as
   technically possible at every front door; §7Q authorization before
   relevance on every operation (accepted Bundle 2); §7Q as the
   **first** sequential output factor and SACL as the **second**
   (accepted B24 / B-INT-6); the in-progress-operation discard path on
   any access reduction (§25.4); §25/A26 identity-and-mode layers
   beneath it all — private use presupposes the properly
   authenticated private Personal Mode context (accepted A26).
9. **Mouth limitations are mouth limitations.** Any model-provider
   refusal is recorded as a limitation of the borrowed mouth — never
   an N.H privacy rule, a Ness restriction, or evidence about the
   material.
10. **Fail-closed defaults:** ambiguous, outdated, unavailable, or
    conflicting permissions for any non-private-Ness purpose →
    withheld; on output failure → withhold for the unauthorized
    purpose, produce a safer version when possible, state plainly
    that material was withheld and why; components receive only the
    minimum material needed — never sensitive content "so they can
    decide not to show it."
11. **Coverage and records:** privacy checks apply to chat, Computed
    View, Story Layer, Person-Boxes, Living State Web, memory
    browsing, search results, simulations, proactive suggestions,
    notifications, exports, tool use, and external sharing; every
    privacy decision records operation, purpose, material, rule,
    authorization basis, eligibility decision, output-review result,
    and any withholding or transformation.
12. **Simulation scratch-space boundary (§11 item 30):** ordinary
    real-reading paths may not use the simulation scratch space;
    Wonder mode may; scratch-space output cannot enter memory
    directly. The recovered §9 personality-related simulation
    (conversation rehearsal) keeps its settled constraints and falls
    under §4.6's approval rule.
13. **Public availability does not automatically authorize**
    unrestricted storage, combination, profiling, or simulation; and
    imported third-party data never becomes fully usable **merely**
    because it was imported — normal rules apply to it like to
    everything else.

## 4. THE APPROVED A7 DECISIONS — ENCODED EXACTLY

### 4.1 Topic pause and restoration

When Ness naturally says something like "Do not talk about this," N.H
treats it as a **reversible pause** on bringing up, displaying, or
discussing the affected topic. The material remains preserved. N.H
must not independently restore a paused topic. Ness may restore it
naturally — with wording such as "Bring this topic back," by directly
reopening the topic himself, or through other wording whose meaning is
clear from context. If Ness's later words clearly reopen the topic,
N.H may continue without asking. If two reasonable meanings remain
**and they would create meaningfully different privacy behavior**, N.H
asks one short clarification. **No formal command phrases are
required** — ordinary language, understood in context, is the
interface.

### 4.2 Scope follows Ness's actual meaning

A pause may affect only visible discussion, or it may also stop
internal retrieval, reasoning, connection, simulation, or influence —
**depending on Ness's instruction**. Visible hiding or silence must
not automatically be treated as internal influence removal (§3 item 7
stands), **and an internal-use restriction does not automatically hide
the material visibly — the two are separate controls that may be
combined when Ness's wording clearly combines them.** A stronger
influence-removal instruction must be followed
according to its stated or contextually clear scope. Scope may apply
to one subject, one person, one source, one purpose, one period, one
operation, or a broader area. N.H uses ordinary language
understanding and surrounding context to read the scope — and does
**not guess** where ambiguity would materially alter privacy (§4.1's
one short clarification applies).

### 4.3 Safe general wording

N.H may use a safer, more general, **truthful** version when exact
private wording or the source should not be exposed. The transformed
version must preserve the real meaning. It must not mislead, distort,
falsely soften, erase an important fact, exaggerate, or create a
different conclusion. When no safe transformation can preserve the
meaning, N.H must withhold the affected part for that visible purpose
— or ask a short clarification when appropriate. This is the
concept-level answer to §7Q's open "safe-transformation rules" slot.

### 4.4 Ness's private self-understanding

N.H may use information about other people to help Ness understand
his own experiences **without asking for separate permission merely
because another person is involved**. Third-party involvement alone
must not block Ness's private self-understanding (this confirms and
carries the settled §7Q Layer-1 sentence). Always preserved: speaker,
source, evidence, uncertainty, and the four-way separation between —
**what the person actually said or did; what Ness believes or
experienced; what N.H interprets; and what remains unknown.**

### 4.5 Natural interpretation without permission

N.H may naturally offer possible explanations of what another person
may have meant, felt, intended, believed, or been trying to do —
**without asking Ness for permission first**. These must always remain
clearly presented as possibilities or interpretations, never as
established facts. N.H adapts to the conversation; Ness never needs to
issue a separate "interpret this person" command. N.H must not
silently convert one interpretation into a permanent truth, diagnosis,
motive, identity claim, or fixed profile. Alternative explanations and
missing evidence remain visible when relevant.

**Supersession, stated openly (see §6.1):** this decision
intentionally goes beyond the older Master §7Q wording that each
subsequent operation in the four-operation ladder "requires stronger
authorization." That older requirement is **superseded for ordinary
bounded interpretation** (operation 3) — **but not for full
simulation** (operation 4), which keeps its approval gate (§4.6).
Recording what a person actually said or did (operation 2) stays
governed by the existing capture, ingest, and third-party rules,
untouched here.

### 4.6 Full simulation requires approval

A **full or detailed simulation of another person requires Ness's
clear approval before it begins.** This includes: extended roleplay as
the person; generated dialogue in that person's voice or manner;
detailed prediction of multiple likely responses; or constructing and
interacting with a hypothetical version of how that person thinks. A
full simulation must **never begin secretly**. While running, it must
remain clearly labeled as hypothetical, limited by the available
information, uncertain, and **not the real person** (the settled
labeling rule stands). Approved simulations remain inside the settled
scratch-space boundary (§3 item 12).

**The boundary, defined so neither side leaks into the other:**
ordinary conversational interpretation — offering, in N.H's own voice,
labeled possibilities about what a person may have meant, felt,
intended, or believed, including a brief "they might respond X or Y"
level of possibility — is **not** a full simulation and requires no
permission. It becomes a **full simulation** — and requires approval
first — when N.H speaks **as** the person or in their voice or manner,
sustains an extended enacted exchange with a constructed version of
them, builds a detailed multi-branch prediction of their responses, or
constructs a hypothetical model of their thinking that Ness interacts
with. Detailed simulation must never be quietly mislabeled as ordinary
interpretation; ordinary interpretation must never be accidentally
blocked by the simulation gate.

### 4.7 No automatic child-or-vulnerability restriction

**Removed and superseded (see §6.2):** the prior rule that minors or
people classified as highly vulnerable automatically receive stronger
default restrictions merely because of age or vulnerability. Ness did
not approve that rule; it was inserted without his decision. Age,
minority status, disability, distress, dependence, or a broad label
such as "vulnerable" must not **by itself** create a separate privacy
class, an automatic block, an automatic weakening of analysis, or a
special simulation prohibition. The same normal evidence, uncertainty,
privacy, external-sharing, interpretation, and simulation-permission
rules apply to everyone. **This does not authorize harm, illegal
conduct, external disclosure, or unsupported factual claims** — those
remain governed by their own existing rules, all untouched. The
"minor and vulnerable person rules" slot is **not retained as an
unresolved policy slot**: automatic category-based special restriction
is **rejected**. Ness retains, as always, the settled power to
configure stricter person-specific or group-specific rules explicitly
— by his decision, never by a category label acting on its own.

### 4.8 Large imported third-party collections

A large import — including years of messages involving one person —
may be used **normally** for broad context, general understanding, and
longitudinal pattern recognition. The amount of material alone must
not force N.H to pause and ask for a narrow purpose before internal or
private-Ness use. Large volume does not itself remove normal
uncertainty, source-separation, privacy, provenance, or simulation
requirements (§3 item 13 stands: importing waives nothing). N.H must
not silently turn the collection into an infallible or fixed profile
of the other person. **No special large-volume permission threshold is
retained merely because the collection is large** — §7Q's open
"volume thresholds for large imports" slot is answered: there is no
volume-based gate.

### 4.9 Private versus external use

Private authenticated use for Ness remains **open by default** unless
Ness has paused, hidden, restricted, redacted, deleted from view,
excluded, or compartmentalized the relevant material — inside the
properly authenticated private Personal Mode context per the accepted
A26 package. **An influence-removal instruction is a separate control
on internal use, not a visible-use switch:** it blocks only the
internal uses included in the scope Ness actually gave, and it blocks
visible output only when Ness's instruction also includes visible
output. A visible pause does not automatically stop internal use; an
internal-use restriction does not automatically hide the material
visibly; the two may be combined when Ness's wording clearly combines
them (§4.2). External sharing, exports,
notifications, shared screens, tool use, and other secondary visible
uses remain **restricted by default** and require the correct
authorization. **Storage permission must not silently become
external-display permission.**

### 4.10 Safe failure behavior

When visible use is not permitted, N.H withholds the affected material
for that purpose and produces a safe truthful version when possible
(§4.3). N.H states plainly when material was withheld and why —
**unless doing so would itself expose the protected information.**
Privacy uncertainty must reduce exposure, never increase it. N.H must
not claim that material was removed, paused, transformed, restored, or
blocked **unless the relevant operation was actually completed and
recorded.**

## 5. IN EASY OPERATIONAL TERMS

- **What N.H may read:** everything its front doors are permitted to
  capture, under Ness's Layer-B exclusion, hold, and redaction rules —
  with one hard boundary for live secrets: **ordinary N.H reading,
  retrieval, reasoning, and model context cannot access live
  credentials or equivalent Level-1 secrets.** Only an authorized
  function operating inside the protected execution boundary may
  handle them; only the minimum safe result may leave that boundary;
  the raw secret remains unavailable to ordinary N.H components.
- **What N.H may keep internally:** everything it read, preserved
  forever without destruction — including paused, hidden, restricted,
  and deleted-from-view material, which stays inside, out of sight.
- **What N.H may say visibly:** to Ness in his private context — by
  default, anything, however sensitive, unless Ness paused, hid,
  restricted, redacted, deleted-from-view, excluded, compartmentalized
  it, or a live-secret/unresolved-case rule applies. To anyone or
  anything else — nothing private, unless the specific external use
  was properly authorized.
- **What changes when Ness pauses a topic:** N.H stops bringing it
  up, showing it, and discussing it. The material stays preserved and
  keeps working quietly inside, unless Ness said otherwise.
- **How Ness restores it:** by saying so in his own words, or simply
  by reopening the topic. If the reopening is clear, N.H continues
  without asking; if two readings would change privacy behavior, N.H
  asks one short question.
- **How stronger influence removal differs:** a visible pause and an
  influence-removal instruction are **separate controls**. A pause
  silences a topic in visible output; an influence-removal instruction
  pulls it out of N.H's internal thinking for the stated scope. They
  may be used together or separately, according to Ness's meaning:
  silence never becomes influence removal on its own, and removing
  internal influence never hides the material visibly on its own —
  each takes Ness's instruction, with its scope recorded.
- **When safe generalization is allowed:** whenever the exact private
  wording or source shouldn't surface but the truth still should — as
  long as the general version keeps the real meaning and changes no
  conclusion. If that's impossible, withhold that part or ask.
- **How third-party interpretations work:** N.H may freely say "she
  may have meant…, he might have felt…" as labeled possibilities,
  keeping who-said-what, what's evidence, and what's unknown visibly
  separate — and never hardening a guess into a fact or profile.
- **Interpretation versus full simulation:** talking *about* a person
  in possibilities is free; speaking *as* the person, staging
  extended exchanges with a built version of them, or detailed
  multi-branch response prediction is a full simulation — it starts
  only after Ness clearly approves, never secretly, always labeled
  not-the-real-person.
- **How large imported histories are used:** normally. Years of
  messages are context and patterns, not a trigger for special
  permission questions — and never an infallible profile.
- **What stays protected from external use:** everything private, by
  default — sharing, exporting, notifying, shared screens, and tools
  each need their own correct authorization; being stored never means
  being shown outward.
- **What happens when meaning or permission is unclear:** for Ness's
  own private use, N.H asks one short question only where the
  difference materially changes privacy behavior; for any external or
  secondary use, unclear means withheld.

## 6. SUPERSESSIONS — EXPLICIT AND NARROW

Master V10 is **not edited** by this candidate. The following two
Ness-approved supersessions are recorded here, openly, for later
integration through the normal versioned route; the Master's original
wording remains historically intact on disk.

**6.1 The four-operation "stronger authorization" requirement —
superseded for ordinary bounded interpretation only.** Master §7Q
states: *"Four separate operations with increasingly stronger privacy
requirements: (1) understanding Ness's experience of another person;
(2) recording what that person actually said or did; (3) interpreting
what the person may have meant; (4) constructing a model of the
person. N.H may normally perform the first. Each subsequent operation
requires stronger authorization."* By Ness's decision (§4.5), the
stronger-authorization requirement is superseded **for operation 3 as
ordinary bounded interpretation**: N.H may interpret naturally,
without separate permission, with all labeling, uncertainty, and
non-hardening rules intact. The requirement **stands** for operation 4
— constructing a model of the person — which is the approval-gated
full simulation of §4.6. Operation 2 remains governed by the existing
capture and third-party rules; operation 1 was always permitted.

**6.2 Automatic minor/vulnerability restriction — rejected and
removed.** Master §7Q states: *"Minors and highly vulnerable people
receive stronger default restriction."* By Ness's decision (§4.7),
that sentence is superseded and the rule removed: no automatic
category-based special restriction exists, and the related "minor-data
specific rules" open slot is closed as **rejected**, not retained.
Within the §7Q context-sensitive variance list, "age or vulnerability"
is likewise superseded **as an automatic driver** — those facts alone
change nothing; Ness's explicit person- or group-specific
configuration remains the only path to different handling. Every other
sentence around the superseded one — the simulation labeling rule, the
large-volume-waives-nothing rule, the public-availability rule —
stands preserved (§3 item 13).

No other Master rule is superseded. Every remaining §7Q rule read for
this candidate is preserved in §3 or carried forward unchanged.

## 7. THE A7 POLICY SLOTS — ALL ANSWERED

The Map's A7 register entry and C-7Q reserve these policy areas; their
status after this candidate:

- **Eligibility rules** — answered: the settled defaults (§3 items
  5–6) plus pause/restore (§4.1), scope (§4.2), and private-versus-
  external (§4.9).
- **Influence-removal scope** — answered (§4.2): scope follows Ness's
  stated or contextually clear meaning across
  subject/person/source/purpose/period/operation/broader; visible
  suppression never becomes influence removal alone.
- **Sensitivity-to-handling mapping** — answered: **the settled four
  sensitivity levels and material types continue to select their
  already-defined protections.** Live credentials and equivalent
  secrets remain inside the Level-1 protected boundary and outside
  ordinary memory and reasoning (§3 items 1, 3); third-party material
  continues to receive the universal third-party baseline (§3 item
  4); sensitive personal material continues to receive the settled
  private-versus-external handling (§3 items 5–6; §4.9). Sensitivity
  alone does not justify withholding truthful material from Ness in
  his authenticated private context (§3 item 6). Age, minority
  status, disability, distress, dependence, or a "vulnerable" label
  alone do not create the rejected extra restriction (§4.7; §6.2).
  Ness's explicit pause, restriction, exclusion, redaction,
  compartment, influence-removal, or person-specific instruction
  continues to govern according to its scope. Ness's rejection of the
  minor/vulnerability rule is **not** broadened into rejection of the
  four sensitivity levels, credential protection, the third-party
  baseline, or any other settled handling rule.
- **Privacy-policy evaluation order** — answered at concept level as
  the settled order, confirmed: capture exclusion earliest at every
  front door → §7Q authorization before relevance → Layer-1
  eligibility before retrieval, with privacy filtering before
  semantic ranking → Layer-2 pre-output review → SACL second → 
  delivery. Implementation sequencing within components is B7's.
- **Safe-transformation rules** — answered (§4.3).
- **Minor / vulnerable-person rules** — closed as **rejected** (§4.7,
  §6.2); no open slot retained.
- **Large-import volume thresholds** — answered: **none exist**
  (§4.8).
- **Simulation-permission specifics** — answered (§4.6): approval
  before start, never secret, labeling, and the
  interpretation/simulation boundary.
- **Purpose categories** — answered and **sufficiently settled for
  A7**: authenticated private Ness use is default-open under its
  stated exceptions; external and secondary purposes — sharing,
  export, notification, shared screen, tool use, and similar outward
  uses — are separately restricted and require the correct
  authorization. Exact labels, storage representation, or future
  finer configuration versions are optional later refinements and do
  **not** keep A7 open.
- **Person-specific control policy** — answered and **sufficiently
  settled for A7**: Ness may govern the six privacy operations; pause
  and restoration; visible scope; internal influence-removal scope;
  person-, group-, source-, purpose-, period-, and operation-specific
  scope; full-simulation approval; and stricter person- or
  group-specific protections (never weaker than the third-party
  baseline, §3 item 4). **Natural language is the control method at
  policy level** (§4.1–§4.2). The exact interface layout, control
  catalog representation, schemas, records, buttons, menus, parsing,
  storage, and enforcement belong to B7 mechanics.

**With the answers above, A7 is complete at the policy level in this
candidate: no A7 policy question remains open, and no new question is
put to Ness. B7's mechanics remain fully open (§9).** This is a
statement about policy content only — the candidate itself remains
`CANDIDATE — NOT ADOPTED — NOT BUILT`, awaiting audit and acceptance,
and nothing is marked package-complete by this file.

## 8. MUST-NEVER BOUNDARIES

This candidate — and any later work consuming it — must never:

- change the no-destruction rule, erase history, or redefine deletion
  as destruction;
- merge visible suppression with internal influence removal;
- weaken live-secret or credential protection (Layer A and L1 stand
  absolutely);
- weaken identity or access control (§25, SACL, A26 untouched);
- weaken authorization for external sharing or action (§7P and the
  external-restricted default untouched);
- let relevance override privacy (§7Q stays before relevance and
  before output, always);
- present guesses about another person as facts, or let an
  interpretation silently harden into truth, diagnosis, motive,
  identity claim, or profile;
- turn a person's data into a fixed profile automatically — at any
  volume;
- begin a full simulation without Ness's approval, run one secretly,
  or mislabel detailed simulation as ordinary interpretation;
- reintroduce automatic category-based restriction for minors or
  "vulnerable" people under any wording;
- claim a privacy operation happened unless it actually completed and
  was recorded;
- start implementation, write code, or create schemas that pretend
  build details are final;
- modify the Master, Map, Defaults, cursorrules, accepted packages,
  or historical files;
- mark this candidate accepted, complete, adopted, integrated, or
  authoritative.

## 9. OPEN FOR B7 — MECHANICAL WORK, VISIBLY OPEN

All of the following remain open for the later B7 package, which must
design them under this policy without inventing policy:

- exact record schemas;
- durable command and scope representation;
- policy-evaluation order implementation;
- protected execution and sealed-storage mechanics;
- derivative discovery;
- mixed-content separation;
- backup handling;
- verification procedures;
- interface controls;
- idempotency;
- transaction boundaries;
- crash and partial-completion recovery;
- duplicate prevention;
- indexes and retrieval enforcement;
- exact logging field formats;
- enforcement across all components;
- build-time thresholds and implementation choices.

**No A7 policy question remains open** (§7): purpose policy and
person-specific control policy are sufficiently settled at the policy
level, and no new question is put to Ness about either. A7's neighbors
A15 and A16 remain open and unchosen; every other Bundle 5 item
remains as the plan holds it; Bundle 5 itself remains open.

## 10. REQUIRED INTERNAL CHECKS — VERIFIED BEFORE DELIVERY

1. **Authority check** — no authoritative or accepted file changed:
   verified; all sources re-hashed byte-identical at the pinned
   snapshot before and after writing.
2. **No-loss check** — all compatible settled §7Q rules preserved:
   verified; §3 carries the full settled foundation, and §6 confirms
   nothing beyond the two named sentences is superseded.
3. **Supersession check** — every Ness-approved change identified
   clearly and narrowly: verified; exactly two supersessions (§6.1
   operation-3-only; §6.2 category-restriction rejection), each with
   the exact Master wording quoted and its narrow extent stated.
4. **Privacy-order check** — exact-purpose privacy authorization
   remains before relevance and output: verified (§3 item 8; §7
   evaluation order).
5. **Visible-versus-internal check** — no accidental merging:
   verified (§3 item 7; §4.2; §5; §8).
6. **Interpretation-versus-simulation check** — ordinary adaptive
   interpretation allowed without permission; full simulation
   approval-gated with a defined boundary: verified (§4.5, §4.6).
7. **Third-party check** — source, speaker, uncertainty, and
   fact-versus-interpretation separation intact: verified (§3 item 4;
   §4.4; §4.5).
8. **External-use check** — private Ness use never silently
   authorizes sharing, export, notification, tool use, or shared
   display: verified (§4.9; §5; §8).
9. **No-category-restriction check** — no hidden reintroduction of
   automatic child/vulnerability restrictions anywhere in this file:
   verified (§4.7; §6.2; §8).
10. **Large-import check** — volume alone creates no new permission
    gate: verified (§4.8; §7).
11. **Phase check** — no coding, production design, or implementation
    authorization: verified (§0; §8; §9).
12. **Open-dependency check** — B7 mechanics visibly open: verified
    (§9).

## 11. STATUS, CHANGE REPORT, AND SELF-AUDIT

**Status:** `CANDIDATE — NOT ADOPTED — NOT BUILT` — awaiting ChatGPT's
independent audit of this actual file and Ness's explicit acceptance
afterward.

**File created:**
`NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`
— the only file created by this task, produced by copying the
identity-verified v1_0 base (SHA-256 `6ac3ce11…d800`; 639 lines;
34,496 bytes) and applying only the four audit corrections and their
dependent edits (title; status-block version note; §4.2 both-direction
separation; §4.9 influence-removal separation; §5 live-secrets bullet
and influence-removal bullet; §7 heading, sensitivity-mapping bullet,
purpose bullet, person-specific bullet, and the A7-policy-complete
statement; §9 remnant paragraph; this §11; the end line). v1_0 is
preserved unchanged as historical candidate evidence. **Nothing
existing was modified:** Master V10, the
Decision Defaults, cursorrules, the Companion, the Map v1.6, the
eight-bundle plan, every accepted package (including A26), every
acceptance and closure record, and all historical candidates remain
byte-identical at the pinned snapshot `4f267a27…`. Nothing was
committed, pushed, moved, renamed, overwritten, or deleted. No policy
question was put back to Ness, and no new Ness policy question was
introduced: A7 is complete at the policy level (§7) while every B7
mechanical dependency remains open (§9).

**Self-audit:** all ten approved decision areas encoded exactly, in
Ness's terms, with the everyday result stated plainly — PASS. Settled
foundation carried without loss, including the six operations, both
protection levels, the four sensitivity levels selecting their defined
protections, the third-party baseline, both output layers, the
influence-removal separation now stated in both directions, the gate
order, the mouth-limitation rule, and the scratch-space boundary —
PASS. Exactly two supersessions,
quoted and narrow, with Master history untouched — nothing else
superseded — PASS. Visible-versus-internal separation consistent
across the full file (§3, §4.2, §4.9, §5, §8) — PASS. The
interpretation/simulation boundary defined in both directions — PASS.
Category-based automatic restriction rejected with the slot closed,
while the sensitivity levels, credential protection, third-party
baseline, and harm/illegality/external-disclosure/unsupported-claims
rules stand untouched — PASS. Volume-based gates removed while
volume-waives-nothing stands — PASS. A26 consistency preserved — PASS.
A7-versus-B7 ownership clean: A7 policy complete, every B7 mechanical
dependency visibly open — PASS. No-loss against v1_0 verified by full
diff review — PASS.
All twelve required internal checks verified — PASS. Exactly one
candidate file created; zero repository modifications; no
implementation or integration — PASS.

---

*End of
`NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`
— `CANDIDATE — NOT ADOPTED — NOT BUILT`, awaiting ChatGPT's
independent audit of this actual file and Ness's explicit acceptance
afterward. v1_0 is preserved unchanged as historical candidate
evidence. Ness's private N.H stays open to him by default and closed
outward by default; pauses and restorations follow his natural words;
visible pause and internal influence removal are separate controls
that combine only when Ness's wording combines them; interpretation
stays free and labeled; full simulation waits for his approval; no
category label restricts anyone automatically, while the settled
sensitivity levels keep their defined protections; no volume of
imported history creates a gate or a fixed profile; and when anything
is unclear, privacy uncertainty always reduces exposure. A7 is
complete at the policy level; B7's machinery remains open. Nothing
existing changed; nothing was implemented.*

# NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_v1_0_CANDIDATE.md

## 1. STATUS BLOCK

**Status:** CANDIDATE — unaudited; awaiting ChatGPT's independent audit of
this actual file and Ness's explicit acceptance afterward. Standalone
Bundle 2 completion **design** candidate only. Not accepted, not adopted,
not authoritative, not integrated into Master V10, the Design and Wiring
Map, Decision Defaults, or cursorrules. Authorizes no implementation, no
code, no patch-ready implementation, no Cursor work, no migration, no
production store, no model change, no runtime, no UI build, no tuning, and
no live-disk action. No existing file was modified, overwritten, renamed,
moved, or deleted.

**Date:** July 9, 2026.

**Intended repository placement:** `05_ACTIVE_CANDIDATE/`
(the physical move into the repository is Ness's action).

## 2. PLAIN EVERYDAY MEANING

This file finishes the **design** of Bundle 2 — how N.H picks what to look
at when Ness asks it something. In plain words: N.H must not be blind. It
may look around nearby related material, and it may also use older
patterns from Ness's history — but it must always keep "this is happening
now" separate from "this is an older pattern," label every memory by
strength, admit honestly when something is only maybe-related or a weak
echo, warn when newer evidence may have changed an old pattern, be
stricter for real-life action suggestions than for understanding, and —
when the retrieval machinery itself breaks — retry a bounded amount, then
stop safely and say so, never pretending it found context it didn't find.
Nothing here is built yet; this is the blueprint for ChatGPT to audit and
for Ness to accept or reject.

## 3. AUTHORITY AND SOURCE INVENTORY

**Governing authority order:**
1. `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`
   (adopted by Ness June 29, 2026 — the standing adoption correction
   applies: any stale wording saying Master V10 is not adopted is
   superseded; Master V10 governs conflicts)
2. `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`
3. `01_AUTHORITATIVE/cursorrules`
4. `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`

The Design and Wiring Map (v1.6) is used as **subordinate working
material only**.

**Sources read for this candidate:**
- Master V10 / map **C-7F** (Context Retrieval: two channels, four modes,
  conflict rule, per-mode declaration list, logging list,
  empty-vs-failure distinction, ceilings, must-nevers, open slots to
  B1/B26/A4);
- Master V10 §7R / map **C-7R** (the settled fourteen-decision relevance
  design: two-layer output, producers, two-tier contract, validation,
  record schemas, five-value purpose vocabulary, four gate conditions and
  nine named dimensions settled in Master §7R — cited, not restated;
  RELEVANCE-IS-NOT list; §7Q external prerequisite; Living State Web
  boundary);
- map **B-INT-1** entry (instantiation of A4 declarations against the
  settled contract for the five consumers) and the map's **A4** entry;
- the accepted **A4 policy package**
  `NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md`
  (SHA-256 `c754b27e…553f`) and
  `NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_ACCEPTANCE_RECORD_v1_0.md`
  (SHA-256 `f9d3fe04…4e62`);
- the accepted **B1 package**
  `NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md`
  (SHA-256 `da0aa4d2…a753`) and
  `NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_ACCEPTANCE_RECORD_v1_0.md`
  (SHA-256 `6c21ea02…677c`) — all four read from the hash-verified
  accepted working copies;
- the accepted **Bundle-1 normalization v1_1** and its acceptance record
  (for the Ness-decided **B9 retry values**, recorded and awaiting
  integration, and the decided **A25** reread modes);
- the accepted **eight-bundle plan**
  (`NH_REPLACEMENT_EIGHT_BUNDLE_DEPENDENCY_PLAN_v1_0_CANDIDATE.md`) —
  consumed through its verified Bundle-2 composition (A4 / B1 / B26 /
  B-INT-1) carried in the governed instruction channel; **honest note:**
  the plan file itself is still not returned by this worker's connected
  project-knowledge index;
- Ness's newly approved Bundle 2 decisions — carried verbatim in
  ChatGPT's prepared instruction for this task (§7).

## 4. BUNDLE 2 SCOPE AND COMPLETION CONDITION

**Bundle 2 establishes how N.H selects permitted, purpose-relevant
material without being blind, random, unsafe, or pretending success.**
It covers:

- **A4** — per-component relevance declaration policy (**accepted**, §5);
- **B1** — retrieval channels, parameter structure, audit fields, safety
  ceilings (**accepted**, §6);
- **B26** — context-retrieval system-failure behavior (**designed here**,
  §8, §13);
- **B-INT-1** — instantiation of accepted relevance modes against the
  settled §7R contract for Context Retrieval, Computed View, Action
  Surfacing, Reread, and Living State Web (**designed here at design
  level**, §9–§12).

**Completion condition:** Bundle 2's design is complete when the four
items above are each accepted at their declared scope and consistent with
one another — with every empirical value, formal Tier 1/Tier 2 declaration
record, integration pass, and implementation step still explicitly outside
it (§16–§17). This candidate does not declare that condition met; ChatGPT
audits, Ness decides.

## 5. ACCEPTED A4 — BY REFERENCE ONLY (NOT REWRITTEN)

Accepted A4 v1.1 (identity in §3) settles **Option C**: one shared
relevance language plus a **mandatory component-specific declaration**
carrying component identity, purpose (from the settled five-value
vocabulary), selected mode, reason, uncertainty behavior, allowed
use boundary, logging/audit, and fail-closed behavior. No component may
invent a private hidden meaning of "relevant"; relevance is
purpose-scoped only; §7Q runs before §7R and relevance never widens
access; A4 wrote **no** actual component declarations. **This candidate
consumes A4 exactly as accepted and changes nothing in it.**

## 6. ACCEPTED B1 — BY REFERENCE ONLY (NOT REWRITTEN)

Accepted B1 v1.0 (identity in §3) settles the **safe structure** of §7F
retrieval: the two always-separate channels (positional / semantic) with
the settled non-merge and conflict-surfacing rules; the versioned per-mode
configuration record with bounded-quantity **slots** (all values open);
the per-run append-only audit record that makes hidden retrieval behavior
structurally detectable; the versioned safety-ceiling mechanism
(minimum-precedence, configuration-time rejection, runtime
defense-in-depth, governed change only); A4 consumption by reference; and
the explicit B1/B26 seam. **This candidate consumes B1 exactly as
accepted and changes nothing in it.**

## 7. NESS-APPROVED BUNDLE 2 DECISIONS (CARRIED VERBATIM; NORMALIZED BELOW)

**Verbatim decision block (preserved exactly as carried in the task
instruction):**

> N.H must not be blind.
> When Ness asks N.H something, N.H may look around nearby related
> material, not only the exact current sentence.
> N.H may use both current situation material and older patterns.
> It must keep them separate. It must not mix "this is happening now"
> with "this is an older pattern."
> Older patterns may support real-life suggestions.
> But if a suggestion is based on an older pattern, N.H must show a
> side-drawer note saying that the support comes from an older pattern.
> Maybe-related memories may be mentioned carefully.
> If N.H is unsure whether something is connected, it may still mention
> it as "maybe related," but must not treat it as proof.
> Weak memories / weak echoes:
> In normal chat, N.H should use simple wording such as "maybe related."
> In the side drawer, N.H may use a more precise label such as "weak
> echo."
> The side drawer must make clear that weak echoes are not strong
> evidence.
> Older pattern width:
> N.H may show:
> strong repeated patterns;
> one similar old memory;
> weak possible echoes;
> but each must be labeled by strength.
> Changed or replaced older patterns:
> If newer evidence may have changed or replaced an older pattern, N.H
> must say so.
> It must not treat an old pattern as automatically current when later
> material may have changed it.
> Action suggestions are stricter than understanding.
> For understanding Ness, N.H may look more widely.
> For real-life action suggestions, N.H must be stricter, consistent with
> Master V10 §7N/§7P.
> Final action strictness rule:
> Old or weak material may support gentle protective suggestions, such as
> pause, wait, take space, or do not answer yet.
> Active steps, such as send this message, confront someone, make a plan,
> change a relationship step, or take an external action, need
> current-situation support too.
> Side-drawer warning placement:
> When an action suggestion is supported by old, weak, maybe-related, or
> changed-pattern material, the warning/note should appear only in the
> side drawer so the main answer stays clean.
> The main answer must still obey Master V10 and must not overstate
> certainty.
> B26 retrieval-failure decision:
> If context retrieval has a system failure, N.H may perform bounded safe
> retry handling. If retrieval still fails, N.H stops safely, records the
> failure, and must not pretend retrieval succeeded.
> No degraded continuation after failed retry is allowed unless a
> separate later Ness-approved rule explicitly authorizes it.

**Normalized statements (no new meaning added):**
1. **Not blind:** relevance-gated looking-around is permitted — nearby
   related material, not only the exact current sentence.
2. **Two piles, never mixed:** *current situation* material and *older
   pattern* material are both usable and **always kept separate and
   labeled**.
3. **Older patterns may support suggestions** — with a mandatory
   **side-drawer note** naming the older-pattern support.
4. **Maybe-related is mentionable, never proof.**
5. **Wording split:** normal chat says simple things like "maybe
   related"; the side drawer may carry the precise label "weak echo,"
   and must state that weak echoes are not strong evidence.
6. **Strength labeling is mandatory** across the width: strong repeated
   pattern / one similar old memory / weak possible echo.
7. **Changed/replaced flag:** when newer evidence may have changed or
   replaced an older pattern, N.H says so; old patterns are never
   auto-current.
8. **Asymmetry:** understanding may look widely; **real-life action
   suggestions are stricter** (Master §7N/§7P consistent).
9. **Final action strictness:** old/weak material may support
   **protective suggestions** only (pause, wait, take space, don't
   answer yet); **active suggestions** (send, confront, plan, change a
   relationship step, external action) additionally require
   **current-situation support**.
10. **Placement:** old/weak/maybe-related/changed-pattern warnings for
    action suggestions live **in the side drawer**, keeping the main
    answer clean — while the main answer still obeys Master V10 and
    never overstates certainty.
11. **B26 decision:** bounded safe retry on retrieval system failure;
    still failing → **stop safely, record, never pretend success**;
    **no degraded continuation after failed retry** unless a separate
    later Ness-approved rule explicitly authorizes it.

## 8. B26 — CONTEXT-RETRIEVAL SYSTEM-FAILURE DESIGN (STRUCTURE ONLY)

**Purpose and owner.** B26 owns what happens when the retrieval machinery
itself breaks. It is the failure-side counterpart of accepted B1's
healthy-run structure, joined at B1's empty-vs-failure marker slot.

**8.1 The two outcomes, kept clearly apart (settled, preserved):**
- **Normal empty result** — retrieval **worked** and found nothing. A
  normal condition: the reading proceeds with target-only/bare context
  exactly as already governed, marked context-limited/revisable. Not a
  failure; none of the failure path below applies.
- **System failure** — index failure, stale/incomplete index, timeout,
  unreachable retrieval service, or an equivalent technical failure. The
  machinery did not do its job; the failure path below applies. For a
  system failure N.H must never substitute unrelated material, never
  lower standards silently, and never claim context was retrieved.

**8.2 Failure-state recording.** Each system failure creates one
append-only **retrieval failure record** bound to the run's B1 audit
record and its operation identity, carrying: the failure class (from the
list above, plus an explicit `equivalent_technical_failure` class for
honest classification of unlisted technical breakage), detection detail,
index/model/system version provenance, the attempt number and retry
lineage, timestamp, and the resulting state. Classification is recorded
fact, never interpretation; a failure record is never evidence about the
meaning of any content.

**8.3 Bounded retry handling (structure; values by reference, not
re-chosen).** Retry re-attempts the **same operation identity** under the
already-designed retry-state architecture (accepted B9 mechanics), with
budgets and timing drawn from the **Ness-decided B9 retry values**
recorded in the accepted Bundle-1 normalization v1_1 (technical failures:
dual time-and-attempt limit, whichever first; up to 3 total attempts —
original plus 2 retries; live-chat gaps 10 then 30 seconds;
background/nightly gaps 1 then 3 minutes; early stop when retrying is
clearly useless or unsafe; extra attempts only on the real-change
exception). **No retry count or timing is chosen here** — B26 binds to
those settled values by reference; their operational integration into the
running machinery remains the pending B9-values integration work.

**8.4 Stop-after-failed-retry (Ness's decision, binding).** When the
bounded retry is exhausted and retrieval still fails: the operation
**stops safely**; a terminal failure state is committed; the reason is
stated through the governed surface; the work record is kept; the
unfinished state is saved so the operation can continue later **only if
something real changes** (the settled real-change exception). **No
degraded continuation after failed retry** — the reading pass does not
proceed on partial or substituted context for that retrieval — unless a
separate later Ness-approved rule explicitly authorizes it. Until any such
rule exists, this path **fails closed**.

**8.5 Crash recovery.** The committed records are the authoritative
state. On restart, any in-flight retrieval attempt found without a
committed outcome resolves to a recorded failure state for that attempt —
never to assumed success and never to a half-supplied context package.
Recovery inspects the retry lineage before any further attempt, so a
crash can neither manufacture an extra retry nor erase a used one.

**8.6 Duplicate prevention and idempotency.** One operation identity, at
most one committed terminal outcome. Attempts are numbered inside one
lineage; a completed operation (success or terminal failure) is never
silently re-run under the same identity; a later real-change resumption is
a **new** operation carrying a lineage pointer to the old one. Re-running
recovery is idempotent: it re-derives the same committed state and writes
no duplicate outcome.

**8.7 Partial-completion recovery.** If failure strikes mid-assembly
(some items already retrieved), the partial material is recorded in the
failure record **for audit only** — it is never supplied as context,
never presented as a complete or "good enough" package, and never
silently merged into a later attempt's results. The run resolves to the
failure path; a later successful attempt supplies a fresh, complete,
honestly-audited package.

**8.8 No-pretend-success enforcement (structural).** The reading pass may
consume a context package **only** from a retrieval run whose B1 audit
record shows a committed successful outcome. Failure states are not
convertible into success by anything downstream; there is no code path in
this design where failed retrieval yields usable context.

**8.9 Relationships.** To **B1**: B26 populates the failure side of B1's
empty-vs-failure marker and adds the failure record; it changes nothing
in B1's healthy-run structure. To the **retry-state architecture (B9)**:
B26 is a consumer of the accepted mechanics and the recorded values, by
reference, adding no new retry meanings. **No implementation is
authorized** anywhere in this section.

## 9. B-INT-1 — RELEVANCE INSTANTIATION / WIRING (DESIGN LEVEL ONLY)

**What B-INT-1 does here:** it instantiates the accepted A4 policy and
Ness's §7 decisions against the settled §7R contract for the five
consuming parts — **in design language**. It defines each part's
behavior; it does **not** author the formal Tier 1/Tier 2 declaration
records (the concrete selections from the settled four-gate-condition /
nine-dimension vocabulary, with ids and versions). Those declaration
records are the remaining authoring step (§16), written later consistent
with this design, keeping accepted A4's reservation intact.

**Instantiation rules common to all five parts:**
- purpose is one of the settled five-value vocabulary — one purpose type
  per part below, no new types invented;
- §7Q authorization always runs first; nothing becomes surfaceable merely
  by being relevant; §7Q-then-SACL order on visible output stands;
- the two retrieval channels stay separate end-to-end; channel identity
  is provenance, not a dimension;
- every supplied item carries its **strength/status label** (§11) and its
  provenance; labels are honest metadata **for Ness**, never hidden
  instructions or hidden authority for the system;
- uncertainty is recorded and labeled, never smoothed over; validation
  outcomes (validated/failed/unresolved) are consumed as settled;
- failure is safe per §8: bounded retry, then stop, never pretend;
- everything logs per §14.

## 10. PER-CONSUMING-PART BEHAVIOR

**Overview table:**

| Part | Purpose type (settled) | Looks how widely | Chat vs side drawer | Strictness |
|---|---|---|---|---|
| Context Retrieval | `retrieval_context_selection` | Widely, within mode limits and ceilings | Feeds both; labels attach at source | Understanding-wide |
| Computed View | `view_assembly` | Widely, internal only | Neither, unless Ness asks to look | Internal; never volunteered |
| Action Surfacing | `action_surfacing` | Strictly | Clean main suggestion; warnings in side drawer | Strictest (§7N/§7P) |
| Reread | `reread_trigger_evaluation` | Trigger-bound only | Neither; lifecycle records | Never blanket |
| Living State Web | `state_review_trigger_evaluation` | Review-trigger-bound | Neither; emits events only | Never writes state |

**10.1 Context Retrieval (§7F).**
*Everyday:* when Ness asks something, N.H may look around — what came
just before in that conversation, and what else in permitted memory may
relate — instead of staring only at the exact sentence.
*Design:* purpose `retrieval_context_selection`; useful material =
§7Q-authorized roots from the positional channel (current thread
adjacency → feeds **current situation**) and the semantic channel (older
related material → feeds **older pattern / one similar old memory / weak
echo / maybe related**, by declared strength). Labeling: every supplied
item carries channel provenance plus its §11 label; positional and
semantic never blend; conflicts surface. Uncertainty: below-threshold or
unresolved matches are supplied only where the mode's declaration allows,
always labeled weak/maybe-related, never as proof. Chat vs drawer:
retrieval itself talks to no one — its labels ride with the items so
downstream surfaces can obey §11–§12. Fails safely per §8. Logs per B1's
audit record. Must not: merge channels, exceed limits/ceilings, lower
thresholds silently, substitute unrelated material, or treat retrieval
presence as evidence of truth.

**10.2 Computed View (§7M).**
*Everyday:* N.H's private working picture of how things seem. It may use
relevant current and older material to stay informed, but it never
narrates itself into the conversation; Ness may deliberately ask to look
at it.
*Design:* purpose `view_assembly`; useful material = authorized readings,
tellings, and state summaries relevant to assembling the internal view.
Labeling: view entries preserve their sources' §11 labels — an entry
resting on an older pattern stays marked so; changed/replaced flags ride
along; nothing hardens into fact. Uncertainty: carried visibly inside the
view, never resolved by assembly. Chat vs drawer: **neither, unless Ness
asks** — the view is an internal tool used silently; when Ness requests a
look, the shown material carries its labels and side-drawer-grade notes
per §11. Fails safely: an assembly that cannot complete honestly is
marked incomplete; no silent gap-filling. Logs: assembly events per §14.
Must not: surface itself unprompted, launder an older pattern into a
current fact, or act as evidence for any reading.

**10.3 Action Surfacing (§7N, with §7P authority).**
*Everyday:* when N.H suggests something Ness might do, the suggestion
must be honest about what it stands on. Old or weak history can back
gentle protective ideas — pause, wait, take space, don't answer yet.
Anything active — send this message, confront someone, make a plan,
change a relationship step, act externally — needs support from what is
happening **now**, not history alone.
*Design:* purpose `action_surfacing`; useful material = current-situation
items (always) plus older patterns / one similar old memory / weak echoes
/ maybe-related items (as support only, labeled). **Strictness split
(Ness's decision, binding):** *protective suggestions* may rest on old or
weak material; *active suggestions* carry **current support required** —
no current-situation support, no active suggestion. Labeling and
placement: the main answer stays clean and never overstates certainty;
when a suggestion's support includes old, weak, maybe-related, or
changed/replaced-pattern material, the **side-drawer note** carries that
warning (§11–§12). Uncertainty: an unclear support base downgrades the
suggestion toward protective or withholds it. Fails safely: retrieval
failure means no invented support — suggestions that would have needed
the failed context are not surfaced. Logs: each surfaced suggestion
records its support items with labels. Must not: present a suggestion as
an instruction; escalate a protective framing into an active one via
wording; hide support weakness from the drawer; bypass §7P authority
(higher-impact actions need stronger review/permission; suggesting,
preparing, and executing stay separate; silence is never consent).

**10.4 Reread (§7H).**
*Everyday:* N.H rereads an old understanding only when something real
calls for it — new information that directly touches it, or new context
that may change its surroundings — never "just rereading everything."
*Design:* purpose `reread_trigger_evaluation`; useful material = the new
trigger material and its relation to the old reading. The decided A25
policy (recorded in the accepted Bundle-1 normalization; integration
pending) supplies the two modes — direct and wider-context — and this
part evaluates relevance **only** to decide whether a real, recordable
trigger exists and which mode fits. Labeling: trigger relations use §11
labels; a weak echo or maybe-related item may *prompt evaluation* but a
reread needs a real recorded reason. Changed/replaced flags are natural
reread triggers — flagged, evaluated, never auto-applied. Uncertainty: no
reason, no reread. Chat vs drawer: none — this is lifecycle machinery;
its outputs are records. Fails safely: evaluation that cannot complete
stops without scheduling anything. Logs: trigger, reason, mode, decision.
Must not: blanket-reread, overwrite/edit/delete old readings (a reread
creates a new reading/layer beside the old), or perform B10 wiring here.

**10.5 Living State Web (§7D).**
*Everyday:* N.H's sense of "where things stand" gets nudged to re-check
itself when relevant new material appears — but relevance only rings the
doorbell; it never walks in and changes the state.
*Design:* purpose `state_review_trigger_evaluation`; useful material =
authorized new/changed items bearing on a tracked state's currentness.
Labeling: candidate triggers carry §11 labels; **newer evidence may have
changed this / may have replaced this** are exactly the flags this part
raises for review. Uncertainty: uncertain relevance yields at most a
labeled review suggestion. Chat vs drawer: none directly — this part
**emits relevance events only**; the settled §7D machinery owns any state
change; relevance and currentness stay permanently separate; the
relevance→currentness→relevance circular chain stays prohibited. Fails
safely: no event, no review pressure; failure never fabricates staleness
or freshness. Logs: emitted events per the settled schemas. Must not:
write state directly, treat an old pattern as automatically current, or
let a relevance score stand in for a currentness judgment.

## 11. SIDE-DRAWER LABELING RULES (REQUIRED LABELS, DEFINED)

The **side-drawer note** is a design concept: a clearly marked
supplementary note surface, separate from the main answer, carrying
support/provenance warnings for Ness. Its mechanical/UI realization is
open (§16). Labels are honest metadata for Ness — **never hidden
instructions, never hidden authority, never facts.**

- **current situation** — material from what is happening now (the live
  thread/present context). The only label that can satisfy **current
  support required**.
- **older pattern** — a repeated pattern from history. Strong support for
  understanding; for actions, protective-grade unless current support
  also exists. Its use in a suggestion always earns a side-drawer note.
- **one similar old memory** — a single past instance that resembles the
  present. Weaker than a repeated pattern; labeled as exactly one
  instance.
- **maybe related** — connection uncertain; mentionable carefully, never
  proof. The normal-chat wording for weak connections.
- **weak echo** — the side drawer's precise label for a faint match; the
  drawer must state that weak echoes are **not strong evidence**.
- **newer evidence may have changed this** — an older pattern whose
  content later material may have altered; must be said, never silently
  treated as current.
- **newer evidence may have replaced this** — an older pattern later
  material may have superseded; same duty.
- **protective suggestion** — gentle, low-impact, reversible self-care
  moves (pause, wait, take space, do not answer yet); may rest on old or
  weak material.
- **active suggestion** — outward steps (send this message, confront
  someone, make a plan, change a relationship step, take an external
  action); requires current-situation support in addition to any history.
- **current support required** — the marker that an active suggestion's
  support base must include current-situation material; unmet means the
  suggestion is withheld or downgraded to protective.
- **side-drawer note** — the note itself: names the support kind
  (older-pattern / weak / maybe-related / changed / replaced), keeps the
  main answer clean, and never contradicts it.

## 12. NORMAL-CHAT WORDING RULES

- Normal chat uses **simple wording**: "maybe related," "this reminded
  me of an older pattern," "not sure this connects." Precise grading
  vocabulary ("weak echo," strength tiers, changed/replaced flags) lives
  in the side drawer.
- The main answer **stays clean**: warnings about old/weak/maybe-related/
  changed-pattern support for a suggestion appear **only in the side
  drawer** — but the main answer still fully obeys Master V10 and
  **never overstates certainty**; keeping it clean never means making it
  more confident than the evidence.
- Chat never presents an older pattern as a present fact, never presents
  a possibility as proof, and never hides that a suggestion is a
  possibility for Ness to judge — Ness remains the sole decision-maker.

## 13. FAILURE, RETRY, CRASH RECOVERY, IDEMPOTENCY, DUPLICATE PREVENTION, PARTIAL-COMPLETION RECOVERY

Consolidated obligations across Bundle 2 (§8 carries the full B26 design):

- **Failure classes** recorded honestly; empty ≠ failure, permanently.
- **Retry** only as bounded structure under the accepted B9 mechanics
  with the Ness-decided values by reference; early stop when clearly
  useless or unsafe; real-change exception only.
- **Stop-after-failed-retry**: terminal commit, stated reason, kept
  record, saved unfinished state; **no degraded continuation** absent a
  separate later Ness-approved rule; fail closed meanwhile.
- **Crash recovery**: committed records authoritative; in-flight resolves
  to recorded failure, never assumed success; lineage inspected before
  any further attempt.
- **Idempotency**: one operation identity → at most one committed
  terminal outcome; recovery re-derivation writes no duplicates.
- **Duplicate prevention**: attempts numbered in one lineage; resumption
  after real change is a new operation with a lineage pointer.
- **Partial completion**: partial retrievals audit-recorded only — never
  supplied, never merged, never "good enough."
- These disciplines bind every part in §10 wherever it performs an
  operation; nothing here weakens any accepted crash-recovery,
  duplicate-prevention, or fail-closed rule anywhere else.

## 14. LOGGING / §0B RECORD OBLIGATIONS

- **One real operation, one append-only log record**, everywhere: each
  retrieval attempt, failure record, terminal commit, view assembly
  event, surfaced suggestion with its labeled support set, reread
  trigger/decision, and emitted state-review event.
- Records carry operation identity, versions/provenance, applied
  parameters or declarations, supplied/considered items **with their §11
  labels**, enforcement events, and honest outcomes (including
  empty-vs-failure and stop-after-failed-retry).
- Logs are **not truth evidence**; repetition adds no certainty; a label,
  a retrieval, a failure, or a suggestion is never double-counted as
  support; derived material is never independent evidence for the
  interpretation that produced it.
- All records obey §7Q access/authorization (and §25 where applicable);
  log visibility follows the settled look-don't-touch Log surface;
  nothing operates silently.

## 15. BOUNDARIES AND MUST-NEVERS (BINDING)

Master V10 boundaries preserved in full: **relevance is not truth, not
evidence strength, not causation, not permission to act, and not Ness's
judgment**; privacy/access gates run **before** relevance can surface
anything, and sensitive or unauthorized material is never surfaced merely
because it is relevant; **action suggestions are possibilities, never
instructions**; **Ness remains the sole decision-maker**; weak, stale,
conflicted, or insufficient evidence is **withheld or clearly labeled**;
**higher-impact actions need stronger review/permission** than small
reversible or protective suggestions; **suggesting, preparing, and
executing remain separate**; **silence is never consent**.

Additionally: A4 and B1 are not rewritten; no new purpose types; no
empirical limits, thresholds, budgets, spans, retry counts, or tuning
values chosen beyond the already-settled B9 values consumed by reference;
nothing integrated into Master V10, the map, Defaults, or cursorrules;
Bundle 2 not marked accepted or authoritative; no implementation, code,
patch-ready implementation, or production store; no later dependency
outside Bundle 2 closed; no weakening of privacy, access control, action
authority, no-loss, crash recovery, duplicate prevention, or fail-closed
behavior anywhere; **old patterns, weak echoes, and maybe-related
memories never become facts; side-drawer labels never become hidden
instructions or hidden authority.**

## 16. STILL-OPEN DEPENDENCIES

- **Formal per-component Tier 1/Tier 2 declaration records** — authoring
  the concrete A4 declarations (settled-vocabulary selections, ids,
  versions) for the five parts, consistent with §10, reserved to Ness's
  acceptance path;
- **the uncertainty-behavior policy for any mouth-produced dimensions**,
  per declaration (reserved to Ness, per the map's A4 entry);
- **every empirical value** — B1 limits/thresholds/budgets/spans and all
  ceiling values (gold-set-tested before locking); any B26 bound not
  already covered by the Ness-decided B9 values;
- **B9-values and A25 operational integration** (recorded decisions,
  pending integration; the settled defaults continue meanwhile);
- **any degraded-continuation rule after failed retry** — currently
  none; fail-closed stands unless Ness later explicitly authorizes one;
- **side-drawer mechanical/UI realization** and the mechanical
  serialization/naming of the structures designed here (B-INT-1's
  implementation-facing step, plus later schema work);
- **Master V10 / map / Defaults / cursorrules integration** of every
  accepted Bundle-1 and Bundle-2 package and of this candidate if
  accepted;
- **final model/provider choices; benchmark thresholds; storage, runtime,
  UI, tuning; all implementation** — nothing authorized;
- **A1** remains blocked (Bundle 1), untouched here; no dependency of any
  later bundle is closed.

## 17. DESIGN-COMPLETE-WHEN CHECKLIST FOR BUNDLE 2

- [ ] A4 accepted at its standalone scope (**done**, by reference).
- [ ] B1 accepted at its standalone scope (**done**, by reference).
- [ ] Ness's Bundle 2 relevance/labeling/strictness decisions recorded
      verbatim and normalized without added meaning (**this candidate,
      §7**).
- [ ] B26 failure path designed structure-complete with no new values
      and fail-closed stop-after-failed-retry (**this candidate, §8,
      §13**).
- [ ] B-INT-1 design-level instantiation for all five parts, consistent
      with A4, B1, §7R, and §7 (**this candidate, §9–§12**).
- [ ] ChatGPT's independent audit of this actual file — **pending**.
- [ ] Ness's explicit acceptance — **pending**.
- [ ] Formal declaration records, empirical values, integrations, and
      implementation — **explicitly outside Bundle 2's design scope,
      listed open in §16**.

## 18. CLAUDE SELF-AUDIT CHECKLIST (internal)

- **Authority & adoption correction:** order stated; Master V10 governing
  and adopted June 29, 2026; map subordinate. **PASS.**
- **A4/B1 untouched:** consumed by reference; summaries add no new
  content; nothing rewritten or reopened. **PASS.**
- **Ness decisions verbatim:** §7 block carried exactly; normalization
  adds no meaning; all eleven required labels defined (§11). **PASS.**
- **No new values:** no limit, threshold, budget, span, or tuning number
  chosen; retry values consumed by reference to the recorded Ness B9
  decision only. **PASS.**
- **B26 complete at structure level:** all thirteen required design
  items present (§8, §13); empty-vs-failure preserved; no degraded
  continuation; fail closed. **PASS.**
- **B-INT-1 within bounds:** five parts instantiated in design language;
  purpose types settled-only; formal declarations left open; no wiring
  implementation. **PASS.**
- **Boundaries intact:** all thirteen Master boundaries carried (§15);
  §7Q before relevance; possibilities-never-instructions; labels never
  facts/instructions/authority. **PASS.**
- **No integration / no implementation / nothing modified:** only this
  file created; no authority, accepted, or historical file touched;
  Bundle 2 not marked accepted. **PASS.**
- **Honest sourcing:** plan consumed via verified composition, noted;
  accepted files read from hash-verified copies, identities listed.
  **PASS.**

## 19. CHANGE REPORT

**File created:**
`NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_v1_0_CANDIDATE.md`
— the only file created by this task; first version; no prior Bundle-2
completion file exists or was modified. **Contents:** accepted A4 and B1
preserved by reference (§5–§6); Ness's new Bundle 2 decisions recorded
verbatim and normalized (§7); B26 designed at structure level with the
stop-after-failed-retry fail-closed rule (§8, §13); B-INT-1 instantiated
at design level for the five consuming parts with the required labels,
side-drawer rules, and chat-wording rules (§9–§12); logging, boundaries,
opens, and checklists (§14–§18). **Sources untouched:** Master V10,
Defaults, cursorrules, the Companion, the map v1.6, all accepted packages
and closure/acceptance records, the A1 blocker record, and all historical
candidates remain unmodified; nothing was integrated; no implementation,
code, disk, store, model, or runtime action occurred.

---

*End of
`NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_v1_0_CANDIDATE.md`
— CANDIDATE, unaudited. This file makes Bundle 2 ready for ChatGPT's
independent audit of the actual file; nothing is accepted automatically;
Ness decides after the audit. All authority, accepted, and historical
files remain unchanged; no implementation was performed.*

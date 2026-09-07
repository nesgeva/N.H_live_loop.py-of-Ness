# N.H — Live Loop Detailed Design Interview Decision v1.1

**Filename:** `NH_LIVE_LOOP_DETAILED_DESIGN_INTERVIEW_DECISION_v1_1.md`  
**Decision owner:** Ness  
**Decision date:** 2026-08-13  
**Status:** NESS-APPROVED LIVE-LOOP WORKING-ROLE DECISION — PRESERVED INPUT — NOT YET BUILT  
**Supersedes:** `NH_LIVE_LOOP_DETAILED_DESIGN_INTERVIEW_DECISION_v1_0.md` (2026-08-09), **for live-loop working-role purposes only**. v1.0 is preserved unchanged as history and must not be edited, renamed, moved or deleted.  
**Intended location:** `/home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP/NESS_DESIGN_INPUTS/`  
**Not authority:** This file does not replace Master V10, the Decision Defaults, `cursorrules`, the Companion Governance file, the Design and Wiring Map, the Full Design-Completion Workflow, or any accepted N.H design. Higher N.H authority wins every architectural conflict. This file does not modify Master or the Map, silently or otherwise.  
**Not implementation authorization:** This decision defines how the future design loop should behave. It does not authorize implementation of N.H production features, production stores, Master/Map integration, acceptance, adoption, or deployment.  
**Scope:** This is a workflow/role decision for the N.H design loop. It changes who works out the mechanical design inside that loop. It does not change what N.H is, and it does not change any accepted N.H architectural design.

---

# 0. Revision note — what changed from v1.0 to v1.1

## 0.1 The preserved predecessor

v1.0 is preserved byte-for-byte as the historical record of the earlier approved role:

- `NH_LIVE_LOOP_DETAILED_DESIGN_INTERVIEW_DECISION_v1_0.md`
- SHA-256 `eee9cce861d66b9877d7318a228a8b21425264fca465ee90047ab012fd96bdd6`
- 630 lines, 20973 bytes
- Decision date 2026-08-09

Its wording is historically accurate and is not withdrawn as history. It is superseded only as the current working rule.

## 0.2 What v1.0 said about the design-work role

v1.0 assigned the mechanical design solution to Claude. Its own words included:

> "Then Claude/controller designs the retry machinery mechanically." (v1.0 §5)

> "Claude creates the new versioned candidate in the safe disposable workspace" as the step immediately after the interview clears, with no intervening design-specification stage. (v1.0 §14)

> "Then Claude designs it, Codex checks it, mechanical problems are fixed automatically…" (v1.0 §22)

That was the approved role at the time. It is now historical.

## 0.3 What v1.1 changes

Ness has changed the design-work role. In every operative statement, the role:

> **"Claude designs the mechanical solution"**

is replaced by:

> **"ChatGPT/GPT-5.6 Sol determines the exact mechanical design specification; Claude applies/drafts that specification."**

The seven changes introduced by v1.1 are:

1. **Question discovery becomes an explicit, package-bounded inventory duty** owned by the OpenAI/ChatGPT reasoning role, performed against the real current sources, before any Claude design work may begin (§3A).
2. **A single completeness claim no longer unlocks Claude.** A fresh, independent OpenAI/ChatGPT coverage review must challenge the question inventory before the package may continue (§3B).
3. **The OpenAI/ChatGPT reasoning role owns the mechanical design solution** and must produce the exact bounded mechanical design specification Claude is to apply (§5A).
4. **Claude becomes the execution/drafting worker** and must stop rather than invent an unspecified consequential design choice (§5B).
5. **Mechanical corrections follow the same division:** audit finding → GPT-prepared bounded correction specification → Claude applies it → fresh independent audit (§15A).
6. **ChatGPT design content may never widen Claude's safety envelope.** The controller keeps sole ownership of every safety boundary (§18A).
7. **No second Ness-question system exists.** The existing Piece-3 interview machinery remains the only path by which a question reaches Ness, and the new coverage review feeds into it rather than around it (§16A).

## 0.4 What v1.1 does not change

Everything else in v1.0 is preserved: Ness's ownership of meaning, the mandatory source check, the definition of a genuine Ness question, the prohibition on asking Ness to solve mechanics, the absence of a question limit, manageable groups, adaptive follow-up questions, the ban on reopening settled choices, dependency handling, answer preservation, the separation of Ness's exact answer from interpretation, the routing protection, the stop condition, the separation of acceptance from design, and the build order.

No Piece-3 behavior other than the role division and the added coverage challenge is changed by this file.

---

# 1. Decision summary

Ness wants the future N.H live design loop to use a **deep, interactive design interview** whenever a feature or package contains many genuinely unresolved user-facing behavior choices, and to keep the mechanical design work in the hands of the reasoning role rather than the drafting role.

The loop must not rush from a short feature idea directly into a large finished design by inventing the missing behavior.

Instead, it must:

1. deeply inspect the current N.H design first;
2. determine what is already settled;
3. determine what is mechanically implied;
4. determine what can be solved mechanically without Ness;
5. identify every genuinely open choice that changes how N.H behaves for Ness, as a complete package-bounded inventory;
6. subject that inventory to a fresh independent coverage challenge before Claude may work;
7. ask Ness the surviving genuine questions in manageable groups;
8. use Ness's answers to refine the next questions;
9. continue until the feature's meaning and intended behavior are sufficiently settled that the remaining design work is mechanical;
10. have the OpenAI/ChatGPT reasoning role work out the **exact bounded mechanical design specification** from the settled sources;
11. only then allow Claude to apply that specification to the one permitted new versioned candidate;
12. run an independent audit of the actual candidate;
13. correct mechanical blockers only through a GPT-prepared correction specification, where authorized;
14. return to Ness if the audit exposes another genuinely open user-facing choice;
15. stop only when the current package is fit for its bounded job.

There is **no arbitrary total-question limit**.

If a complex feature genuinely requires many Ness decisions, the loop must ask as many as are actually necessary.

It must not reduce design quality merely to keep the interview short.

Claude does not decide what the N.H design should be. Claude expresses a design that has already been determined.

---

# 2. Why this behavior exists

N.H is a system whose meaning, behavior, permissions, priorities, privacy, and user experience belong to Ness.

The AI roles can solve a large amount of mechanical architecture.

They must not silently decide what Ness wants merely because a feature contains many missing details.

For a complex feature, a short idea such as:

> "I want N.H to understand music with me"

may leave many real experience questions open, such as:

- when N.H should speak;
- when it should stay quiet;
- what should be remembered;
- what should remain temporary;
- what should happen automatically;
- what requires permission;
- what happens when meanings conflict;
- how later changes should appear;
- what belongs to private memory;
- what should be surfaced in another project;
- how uncertainty should feel in actual use.

These are not database or coding questions.

They affect what N.H actually is.

Ness wants to decide them.

The role change in v1.1 exists for a second, related reason: a model that is simultaneously deciding the design and writing the file has both the opportunity and the incentive to close a gap quietly. Separating the role that determines the design from the role that writes it makes an invented decision visible as a mismatch between a specification and a file, rather than invisible inside a single act of authorship.

---

# 2A. The corrected working-role division

## Ness — owns meaning

Ness alone owns:

- what N.H is;
- what it should mean;
- user-facing behavior;
- policy;
- permissions;
- privacy choices;
- priorities;
- genuine trade-offs;
- acceptance;
- adoption;
- permission to build.

The interview must ask Ness only genuine choices.

Ness must not be asked to solve ordinary mechanics.

## The OpenAI/ChatGPT reasoning role — finds the choices and determines the mechanics

The OpenAI/ChatGPT reasoning role — currently **GPT-5.6 Sol**, reached through the existing read-only/ephemeral Codex CLI transport — owns:

- independent source review of the real current files;
- the complete package-bounded inventory of consequential design points;
- classification of each point;
- detection of genuine Ness choices;
- the fresh independent coverage challenge of that inventory;
- determination of the **exact bounded mechanical design specification** Claude is to apply;
- preparation of any bounded mechanical **correction** specification;
- independent audit of the actual candidate.

The Codex CLI is the transport that gives that model bounded, read-only access to the repository. It is not itself the conceptual design role.

## Claude — applies and drafts

Claude owns:

- reading the real relevant sources for verification and context;
- faithful application of the supplied mechanical design specification to the one permitted new versioned candidate;
- the ordinary consistency and document edits necessary to express that specified design;
- preservation of everything outside the bounded specification;
- an honest report of what it changed;
- stopping when the specification does not actually determine the answer.

Claude does not choose what N.H should do.

## The controller — owns the safety envelope

The controller owns every safety boundary, and no design content from any model may widen it. See §18A.

## Relationship to the existing project role files

The N.H Full Design-Completion Workflow already places mechanical-architecture **requirements** with the reviewing/reasoning role and **drafting** with Claude ("Mechanical architecture | Ness reviews outcome | ChatGPT defines requirements/audits | Claude drafts"). v1.1 sharpens that line for the live loop: the requirement set must be an exact bounded design specification, complete enough that drafting it involves no consequential design choice.

Two earlier role statements point the other way and are recorded here openly rather than resolved silently:

- The adopted **Decision Defaults (S19 v2.2), §0** states: *"Cursor writes code; Claude designs and audits; Ness runs commands and verifies on disk. This division is not renegotiable."*
- The **Companion Governance** file's embedded `NH_WORKING_ROLES.md` describes Claude as the role that develops the technical design, and states that the checking role's job is *not* to propose what the system should do or which direction a design choice should go.

Neither statement is edited, weakened, or overridden by this file, and neither is withdrawn as a record. Both were written about the N.H design/build sessions and the Cursor/Claude/Ness division, not about the live design loop's internal two-AI split, which did not exist when they were written.

This decision governs the **live-loop working role only**. It does not change the authority order, does not change the Decision Defaults, and does not claim architectural authority. If Ness wants the Defaults wording itself changed, that is a separate authorized Defaults step, not something this file performs.

The tension is a workflow tension, not an architectural one. Nothing here lets either AI decide meaning — which is the boundary those role statements exist to protect, and which §2A preserves in full by keeping every genuine choice with Ness.

---

# 3. Mandatory source check before any Ness question

Before the loop asks Ness a design-interview question, it must perform the normal N.H source check.

At minimum, it must inspect all relevant parts of:

1. `NH_MASTER-20_CORRECTED_v10.md`;
2. the current Design and Wiring Map and relevant dependencies;
3. the currently adopted Decision Defaults;
4. relevant `cursorrules`;
5. relevant accepted standalone packages;
6. relevant acceptance, closure, receipt, and working records;
7. earlier Ness decisions relevant to the feature;
8. later accepted work that may supersede an older status note.

The loop must not ask a question merely because one model did not immediately know the answer.

It must classify each issue first as one of:

- already settled;
- mechanically implied by settled rules;
- mechanical work;
- waiting on another choice;
- genuinely open for Ness;
- future/non-blocking;
- later implementation/build work.

Only **genuinely open Ness choices** belong in the design interview.

Nothing may be taken off the Ness-decision path on a model's unsupported say-so. A classification that removes or parks an issue must be grounded in real settled source.

---

# 3A. The question stage must actively look for Ness choices before Claude may work

Before any Claude design or correction work for a package, the OpenAI/ChatGPT reasoning role must inspect the **actual current sources** and produce a **complete package-bounded inventory of consequential design points**.

For each point in the inventory it must record a classification from the same list used in §3:

- settled;
- mechanically implied;
- mechanical work;
- waiting on another choice;
- genuinely open for Ness;
- future/non-blocking;
- later implementation/build work.

The inventory is bounded by the current package. It is not an invitation to inventory all of N.H.

## The test for a genuine Ness choice

> If two or more materially different N.H behaviours remain compatible with the settled sources, **and** choosing between them changes what N.H means, does, permits, protects, remembers, surfaces, prioritizes, or feels like for Ness in real use, that choice belongs to Ness.

Such a choice must not be silently converted into mechanical work.

## The test for something that is not a Ness choice

> If only the internal mechanism differs, and the difference does not change the user-facing meaning or policy consequence, Ness is not asked.

The distinction is the consequence, not the vocabulary. A point described in implementation language may still hide a policy consequence; a point described in experience language may still be fully settled by source.

---

# 3B. One model saying "complete" is not enough

A first question-discovery pass is **not by itself sufficient** to unlock Claude.

After the package's exhaustive question inventory appears complete, a **fresh, independent OpenAI/ChatGPT coverage review** must challenge that inventory against the same current package and the same relevant sources.

## What the coverage review is looking for

Specifically:

- a user-facing choice the first inventory omitted;
- two materially different N.H behaviours hidden inside something labelled mechanical;
- a policy consequence hidden behind an implementation or mechanical description;
- a previously answered choice that does not actually settle the new situation;
- a dependency that makes a question premature;
- a supposed open choice that is already settled in source.

## What happens to what it finds

If the coverage review finds a possible missing genuine choice:

1. Claude remains blocked for that package;
2. the possible gap enters the **existing Piece-3 question-validation/source-check path**;
3. it must **not** become a direct Ness question built from raw model prose.

Only the existing validated interview machinery may put a question to Ness.

If the coverage review confirms that no additional currently necessary Ness choice exists, the package may continue.

## What this is and is not

This is an additional coverage challenge. It is not a mathematical claim that AI can never overlook anything. It reduces the chance that a single pass silently converts a real Ness choice into mechanical work; it does not make that impossible, and no later stage may treat a completed coverage review as proof that nothing was missed.

The review must be genuinely fresh and independent of the pass it is challenging. A review that merely restates the first inventory has not been performed.

---

# 4. What counts as a genuine Ness question

A question belongs to Ness when the answer materially changes one or more of these:

- what N.H means;
- what N.H does;
- what N.H does automatically;
- what requires permission;
- what N.H remembers;
- what stays temporary;
- what N.H may surface;
- what remains private;
- how N.H behaves when uncertain;
- what N.H prioritizes;
- how a feature feels in real use;
- how N.H responds to conflicting meanings;
- what control Ness has over the feature;
- what is allowed to affect future behavior;
- what should happen after rejection, postponement, silence, correction, or change of mind.

The governing test is the one stated in §3A: two or more materially different behaviours remain compatible with the settled sources, and the choice between them changes N.H's meaning or policy consequence for Ness in real use.

Examples of appropriate interview questions:

- Should N.H normally wait for Ness to ask before commenting on a song, or may it sometimes make a relevant observation while the song is playing?
- If Ness later gives the same media moment a different personal meaning, should both meanings normally appear together, or should one be the default view while history remains available?
- Should a project-linked media reference automatically surface when that project opens, or only when it passes the normal relevance rules?
- When N.H is unsure whether Ness returned to an earlier thought branch, should it ask, show the uncertainty, or stay quiet unless the distinction matters?
- In a creation workspace, when should N.H consider something merely a draft versus ready for Ness to confirm?

These questions affect actual N.H behavior.

---

# 5. What the loop must NOT ask Ness to solve

Ness must not be used as the mechanical architect.

The loop must not ask Ness to choose ordinary implementation/design mechanics such as:

- JSON schemas;
- internal field names;
- transaction IDs;
- hash structures;
- idempotency keys;
- retry counters;
- crash-recovery internals;
- duplicate-protection mechanics;
- queue structure;
- database layout;
- storage-engine details;
- file-descriptor mechanics;
- path-normalization logic;
- internal logging schemas;
- exact internal state-machine encoding;
- mechanical version-number derivation;
- test harness structure;
- ordinary validation code;
- ordinary provenance plumbing;
- ordinary controller bookkeeping.

If one of those mechanical choices contains a genuinely different user-facing policy consequence, the loop may ask Ness about **the consequence**, not the mechanical mechanism.

Example:

Wrong:

> Which retry state machine should we use?

Correct, only if genuinely open:

> If a temporary research failure happens, do you want N.H to retry later automatically under the existing approved schedule, or wait for you?

Then the **OpenAI/ChatGPT reasoning role determines the retry machinery mechanically** and states it as an exact bounded design specification; **Claude drafts that specification into the candidate**; the controller enforces the safety envelope throughout.

*(v1.0 §5 ended this example with "Then Claude/controller designs the retry machinery mechanically." That was the earlier approved role and is superseded here. See §0.)*

---

# 5A. Who determines the mechanical design solution

Once the Ness interview is clear for the current package, the OpenAI/ChatGPT reasoning role — currently **GPT-5.6 Sol** through the existing read-only/ephemeral Codex CLI transport — owns working out the exact mechanical design solution from:

- the governing N.H sources;
- accepted dependencies;
- Ness's settled answers;
- the current package scope;
- correctly open/deferred items.

It must produce the **exact bounded mechanical design specification that Claude is to apply**.

## Selecting among mechanical alternatives

For genuinely mechanical alternatives, the reasoning role may select the safest coherent solution that satisfies the settled N.H requirements.

That mechanical selection is **not** a Ness question, unless the alternatives have materially different Ness-facing meaning or policy consequences — in which case it was never a mechanical alternative, and it belongs in the interview under §3A.

## What the specification must be

The specification must be exact and bounded enough that applying it requires no consequential design choice. If it is not, Claude is required to stop rather than complete it (§5B).

The specification determines **design content only**. It cannot determine anything about Claude's operating envelope (§18A).

---

# 5B. Claude's execution/drafting role and the mandatory stop

Claude does **not** independently decide what the N.H design should be.

## Claude's job

- read the real relevant sources for verification and context;
- receive the exact current mechanical design specification prepared by the OpenAI/ChatGPT reasoning role;
- apply that specification faithfully to the one permitted new versioned candidate;
- make only the ordinary consistency/document edits necessary to express that specified design;
- preserve everything outside the bounded specification;
- report what it changed.

## What Claude must not do

Claude must not:

- choose between materially different N.H behaviours;
- invent an architecture not specified by the ChatGPT/GPT design specification;
- fill an unspecified policy or design gap;
- broaden the package;
- turn an open item into a decided item;
- create a new mechanical solution merely because it prefers one.

## The mandatory stop

If Claude discovers that the supplied specification is ambiguous, contradictory, incomplete, or requires another consequential design choice, **Claude must stop rather than decide it**.

- For an **initial candidate**, Claude must create **no candidate** in that state.
- For a **seeded correction**, Claude must leave the seeded target **byte-identical** rather than inventing a correction.

The issue returns to the OpenAI/ChatGPT reasoning role for design review.

If that review discovers a genuine Ness choice, it returns through Piece 3.

Stopping is the correct outcome, not a failure. A candidate that exists because Claude closed a gap on its own is worse than no candidate.

---

# 6. Many questions are allowed and expected

There is no rule that a feature should require only a few questions.

If a feature genuinely contains:

- 10 open behavior choices;
- 20 open behavior choices;
- 40 open behavior choices;
- or more,

the loop may ask all of them if they remain genuinely necessary after the full source check and the coverage challenge.

The loop must not:

- compress several distinct meaning choices into one vague question merely to shorten the process;
- guess answers for Ness;
- manufacture defaults because the interview is becoming long;
- silently copy another product's behavior;
- treat model preference as Ness preference;
- stop asking while a material user-facing ambiguity remains.

The goal is not "few questions."

The goal is:

> **No unnecessary questions, and no missing necessary questions.**

---

# 7. Questions must be asked in manageable groups

Even when many questions are required, the loop should not dump one enormous questionnaire on Ness unless Ness explicitly asks for that format.

Instead, it should ask questions in **small, coherent groups**.

A group should contain questions that naturally belong together, for example:

- automatic behavior;
- memory behavior;
- privacy behavior;
- uncertainty behavior;
- project linking;
- interface experience.

The exact group size is not fixed.

The loop should choose a size that is practical to answer without overwhelming Ness.

The loop must preserve completeness across groups.

"Manageable groups" must never become an excuse to silently drop later questions.

---

# 8. Later questions must use earlier Ness answers

The interview is adaptive.

The loop must not generate a giant questionnaire once and then blindly work through it.

The intended pattern is:

**source audit → ask → Ness answers → re-evaluate → ask the next needed questions**

A Ness answer may:

- settle several later questions automatically;
- make an earlier hypothetical question irrelevant;
- expose a new genuine behavior question;
- reveal a dependency;
- change the natural package boundary;
- show that something previously thought open is actually mechanically implied.

The loop must incorporate the answer before deciding what to ask next.

---

# 9. The loop should explain why it is asking

Before a feature interview begins, the loop should give Ness a plain-language summary such as:

> I checked the current N.H design.
>
> Some parts of this feature are already settled and will be preserved.
>
> Some details are mechanical and I will not bother you with them.
>
> I found a set of genuine behavior choices that the current N.H design does not answer.
>
> We will go through those in manageable groups. Your answers may settle or reveal later questions.

The exact wording may vary.

The important requirement is that Ness should understand:

- what was checked;
- what is already settled;
- what is mechanical;
- why questions remain;
- what those questions change in real use.

For an individual question, when useful, the loop should briefly state:

- **Already settled:** the relevant surrounding rule;
- **Still open:** the exact missing behavior;
- **Why Ness is needed:** what changes for actual N.H use;
- **Question:** the one real choice.

---

# 10. The interview must not reopen settled choices

A deep interview is not permission to redesign all of N.H.

The loop must preserve settled decisions.

It must not ask Ness to choose again merely because:

- a different model prefers another answer;
- an older file used different wording;
- the current feature could theoretically be designed another way;
- a candidate exposes a choice that authority already settled;
- the loop wants extra confirmation;
- the new coverage review would like a second opinion on something source already answers.

If the current N.H sources already answer the question, the loop must report the answer and continue.

---

# 11. The interview must respect dependencies

Some questions should not be asked yet.

If a detail depends on another unresolved feature or package, the loop should:

1. identify the dependency;
2. leave the dependent detail open;
3. continue with work that is actually unlocked;
4. return to the dependent question at the correct time.

It must not force Ness to answer a hypothetical question without the information needed to understand its real consequences.

---

# 12. Answer preservation

Ness's answers must be preserved so the loop can reliably continue later.

The Piece-3 controller design must provide a durable, inspectable way to preserve:

- the exact question asked;
- why it was classified as genuinely open;
- relevant source grounding;
- Ness's exact answer;
- any normalized/structured interpretation used by the controller;
- consequences mechanically derived from that answer;
- whether the answer settled the question;
- what remains open;
- which later design package uses the decision.

The exact schema and storage mechanics are **not decided by this file**.

Those are mechanical design work, and under §5A the OpenAI/ChatGPT reasoning role determines them.

But the user-facing requirement is settled:

> Ness must not have to repeatedly reconstruct prior design answers from memory or old chats.

The system must be able to resume the design interview from preserved decisions.

---

# 13. Exact-answer preservation versus interpretation

When Ness answers, the raw answer and the system's interpretation of that answer must not silently become the same thing.

The design must preserve the distinction between:

- **Ness's actual answer**;
- **controller/AI structured interpretation**;
- **mechanical consequences derived from the answer**.

If the interpretation is uncertain in a way that could change N.H behavior, the loop must clarify with Ness rather than pretending certainty.

If the interpretation is mechanically obvious and does not change meaning, the loop should proceed without unnecessary clarification.

---

# 14. Returning from the interview to automatic design

The interview does not replace the automatic design path.

It unlocks it.

Once the loop determines that the current feature/package has enough settled meaning for the remaining work to be mechanical, and the fresh coverage challenge in §3B has confirmed no additional currently necessary Ness choice:

1. the controller prepares the bounded design task and binds it to the package, the sources and the exact target path;
2. **the OpenAI/ChatGPT reasoning role determines the exact bounded mechanical design specification** from the governing sources, accepted dependencies, Ness's settled answers, the current package scope, and the correctly open/deferred items (§5A);
3. **Claude applies that specification** to the one permitted new versioned candidate in the safe disposable workspace, making only the edits necessary to express it (§5B);
4. the controller verifies/promotes the candidate according to its current safety rules;
5. the OpenAI/ChatGPT reasoning role independently audits the actual candidate;
6. validated mechanical blockers may enter the authorized automatic correction loop **only through a GPT-prepared correction specification** (§15A);
7. a fresh independent audit checks each corrected candidate.

No Ness question is needed merely because mechanical work exists.

If step 2 cannot produce an exact bounded specification without making a consequential design choice, the package does not proceed to step 3. It returns to §3B and, if a genuine choice is found, to Piece 3.

*(v1.0 §14 went from the cleared interview directly to "Claude creates the new versioned candidate," with no intervening design-specification stage. Step 2 above is the change.)*

---

# 15. If the audit finds a new genuine Ness choice

During audit, the OpenAI/ChatGPT reasoning role may discover that a candidate filled in something the real sources did not settle.

If that issue changes N.H meaning, behavior, permissions, privacy, priorities, or user experience, it must not be sent to Claude as an ordinary mechanical correction.

The controller must stop the automatic correction path for that issue and route it to the question-validation/design-interview stage.

The controller must **not** convert raw model prose directly into a Ness question.

Before Ness sees a question:

1. the issue must be independently classified;
2. relevant current N.H sources must be checked;
3. settled answers must be removed;
4. mechanical questions must be removed;
5. dependencies must be identified;
6. the remaining question must be rewritten in clear everyday language;
7. Ness must be told what the choice changes in real use.

The same applies when the discovery is made while preparing a correction specification rather than during the audit itself (§15A).

---

# 15A. Mechanical corrections follow the same role division

A design audit finding is **not** sufficient by itself to tell Claude "figure out a fix."

For every mechanically correctable blocker:

1. the fresh OpenAI/ChatGPT reasoning role audits the actual candidate;
2. the OpenAI/ChatGPT reasoning role prepares an **exact bounded correction specification** from the real settled sources;
3. only then may Claude apply that specified correction;
4. Claude may not independently choose a different design solution;
5. a fresh independent audit checks the resulting actual candidate.

If preparing the correction specification exposes a genuine Ness choice, automatic correction stops for that issue and it returns to Piece 3 through §15.

If the supplied correction specification is ambiguous, contradictory, incomplete, or requires another consequential design choice, Claude leaves the seeded target **byte-identical** and the issue returns to the reasoning role (§5B).

A byte-identical corrected candidate is a legitimate stop, not a defect to be worked around.

---

# 16. No automatic Ness question from a model route

A model may signal:

- `chatgpt_review_required`;
- `genuinely_open_for_ness`;
- or an equivalent future route.

That signal is **not itself permission to ask Ness**.

It means:

> stop automatic mechanical handling and perform the required independent question-validation/source-check stage.

Only after that stage confirms the issue is genuinely open may the live loop ask Ness.

The same rule applies to anything raised by the fresh coverage review in §3B: a coverage finding is a routing signal into question validation, never a question.

This protects Ness from:

- fake choices;
- duplicate questions;
- model confusion;
- stale-source questions;
- mechanical questions;
- policy invention.

---

# 16A. One interview system only

There must be **no second, competing Ness-question system**.

The existing Piece-3 machinery remains the only path by which a question reaches Ness:

**source check → genuine-question validation → manageable question group → exact answer preservation → fresh re-evaluation → clearance.**

The new coverage review of §3B feeds possible missed choices **into** that existing path. It does not run alongside it, does not bypass it, and does not surface anything to Ness itself.

No Ness-facing question may be raw model prose. Every Ness-facing form is constructed by the controller from validated values, as the existing machinery already requires.

---

# 17. Interview stop condition

The design interview for a package is ready to stop when:

- all currently blocking genuine Ness decisions for that package are settled;
- the fresh independent coverage challenge (§3B) has been performed and confirms no additional currently necessary Ness choice;
- no relevant user-facing behavior ambiguity remains that must be decided now;
- remaining open matters are correctly classified as:
  - dependent;
  - future/non-blocking;
  - or implementation work;
- the remaining current-package design work is mechanical, in the sense that an exact bounded mechanical design specification can be determined from settled sources without another consequential choice.

The loop does not need to settle every future detail in the universe.

It must settle what the current bounded package genuinely needs.

Reaching the stop condition unlocks the mechanical design-specification stage (§5A). It does not unlock Claude directly.

---

# 18. Acceptance remains separate

Completing a design interview does not mean Ness accepted a candidate.

A Claude-created candidate is still only a candidate.

An audit PASS is still only an audit result.

The live loop must never turn:

- "Ness answered the interview";
- "ChatGPT/GPT prepared the mechanical design specification";
- "Claude applied the specification";
- "the audit returned PASS";

into:

- accepted;
- adopted;
- `PACKAGE_COMPLETE`;
- Master-integrated;
- Map-integrated;
- implementation-authorized.

Ness's later explicit acceptance/adoption remains separate. No Master or Map integration happens automatically, and no implementation begins without separate Ness authorization.

---

# 18A. ChatGPT design content may not control Claude's safety envelope

The controller continues to own and enforce:

- which package is being worked on;
- package/source binding;
- the exact target path;
- the one-file write boundary;
- the disposable workspace;
- Claude tool/permission restrictions;
- provider/model configuration;
- source-state fences;
- no-overwrite protection;
- candidate verification and promotion;
- journal integrity;
- no Git changes;
- no acceptance/adoption;
- no implementation;
- the lifetime correction cap.

The ChatGPT/GPT mechanical design specification may determine **only the bounded design content to be expressed in the candidate**.

It must never be able to widen:

- file access;
- tool permissions;
- target paths;
- authority order;
- correction count;
- Git permissions;
- implementation permission;
- acceptance or adoption;
- any other controller safety boundary.

A design specification that attempts to alter any of the above is not a design specification. The controller must refuse it rather than execute the design content it carries.

This separation is the reason the role change in v1.1 is safe: the reasoning role gains authority over **what the design says**, and gains no authority whatever over **what the loop is allowed to do**.

---

# 19. Relationship to future feature-intent files

This behavior is especially important for files such as:

`NH_FUTURE_FEATURE_DESIGN_INTENT_FOR_LIVE_LOOP_v1_0.md`

That file intentionally describes large feature intentions without mechanically settling every behavior detail.

When the live loop processes such a feature-intent file, it must not treat missing detail as permission for any AI role to invent a complete user experience — not for Claude to invent it while drafting, and not for the reasoning role to bury it inside a mechanical design specification.

It must use this Detailed Design Interview Decision to determine when a real interactive Ness interview is required.

---

# 20. Build order approved by Ness

*The statuses below are preserved as recorded in v1.0 at its decision date. This file does not restate or update live controller status; current controller state is tracked in the controller's own records, not here.*

## Piece 1 — Automatic independent design audit

Status as recorded in v1.0:

**DONE / independent re-audit PASS**

Piece 1 provides the independent audit of a newly created candidate.

## Piece 2 — Automatic correction → fresh re-audit loop

Status as recorded in v1.0:

**CURRENT BUILD WORK**

Piece 2 handles validated mechanical blockers automatically:

audit BLOCKED  
→ **GPT-prepared bounded correction specification**  
→ bounded Claude application of that specification  
→ new versioned candidate  
→ fresh independent audit  
→ repeat within the safety limit  
→ PASS or stop safely.

Under v1.1, the correction-specification step is part of this loop rather than something Claude derives for itself (§15A). Everything else about Piece 2 — including the lifetime correction cap and every other safety boundary — is unchanged by this decision.

Piece 2 must be completed and independently audited before Piece 3 begins.

## Piece 3 — Detailed Ness Design Interview / Question Validation

**This decision continues to authorize Piece 3 as the next controller behavior to design/build after Piece 2 passes.**

Piece 3 must provide the behavior defined in this file, including:

- genuine-question detection;
- complete relevant source checking;
- the complete package-bounded question inventory (§3A);
- the fresh independent question-coverage challenge before Claude unlocks (§3B);
- question validation;
- manageable grouped interviews;
- adaptive later questions;
- answer preservation;
- resume behavior;
- dependency handling;
- routing from audit-discovered genuine choices back to Ness;
- routing from coverage-review findings into the existing validation path, never around it (§16A);
- return from settled interview state into the mechanical path via the GPT design-specification stage (§14).

Piece 3 must be separately implemented and independently audited.

## Controlled combined test

After Pieces 1–3 are complete, a real combined live-model test requires Ness's separate explicit authorization.

The test should prove at minimum:

1. a genuine open design issue reaches the interview stage;
2. settled/mechanical issues do not become Ness questions;
3. Ness's answer is preserved;
4. the loop can resume from the preserved answer;
5. the fresh coverage challenge actually runs, and a possible missed choice it raises blocks Claude and enters the existing validation path rather than reaching Ness as raw prose;
6. the OpenAI/ChatGPT mechanical design specification is produced before Claude does any design work;
7. Claude applies the specification faithfully and reports what it changed;
8. Claude stops — creating no candidate, or leaving a seeded target byte-identical — rather than inventing an unspecified consequential design choice;
9. the independent audit works;
10. mechanical blockers are corrected only through a GPT-prepared correction specification;
11. a newly discovered genuine question returns to the interview rather than being mechanically invented;
12. no design content from any model widens a controller safety boundary.

## Interface

The browser/user interface comes **after** Pieces 1–3 are working.

The interface should be built around the real workflow rather than forcing the workflow to fit a prematurely designed UI.

The future interface may then show states such as:

- checking current N.H;
- question inventory in progress;
- coverage review in progress;
- questions ready;
- waiting for Ness;
- answer preserved;
- ChatGPT/GPT preparing the mechanical design specification;
- Claude applying the specified design;
- auditing;
- ChatGPT/GPT preparing a correction specification;
- Claude applying the specified correction;
- question validation required;
- PASS;
- waiting for Ness acceptance.

The exact interface design remains future work.

---

# 21. What is approved now versus what is not

## Approved by Ness in this decision

Ness approves:

- the Detailed Design Interview behavior described here;
- asking as many genuine user-facing questions as necessary;
- asking them in manageable groups;
- adaptive follow-up questions based on earlier answers;
- complete source checking before questions;
- keeping mechanical architecture away from Ness;
- the complete package-bounded question inventory before any Claude design work;
- the fresh independent question-coverage challenge as a required unlock condition;
- routing every coverage finding through the existing Piece-3 validation path;
- **the OpenAI/ChatGPT reasoning role (currently GPT-5.6 Sol through the existing read-only/ephemeral Codex CLI transport) determining the exact bounded mechanical design specification**;
- **Claude acting as the execution/drafting worker that applies that specification**;
- Claude stopping rather than inventing an unspecified consequential design choice;
- the same role division for mechanical corrections;
- the controller retaining sole ownership of every safety boundary;
- preserving answers for resume/continuation;
- returning audit-discovered genuine choices to the interview path;
- building this as controller **Piece 3 after Piece 2 passes**;
- delaying the browser/interface until Pieces 1–3 work.

## Not approved merely by this decision

This file does not authorize:

- editing `nh_loop.py` or any controller code on the strength of this record alone;
- beginning any controller repair, including Repair 11;
- running a live provider/controller test;
- beginning Piece 3 before Piece 2 passes;
- a particular Piece-3 code architecture;
- a particular schema/file format for question records or design specifications;
- any change to the five-round lifetime correction cap;
- any change to existing same-session correction behavior;
- any change to GPT/Claude model or provider settings;
- any change to the existing interview journal;
- any widening of Claude's tool, path, or write permissions;
- production N.H implementation;
- production stores;
- changing N.H authority files;
- hidden Master/Map integration;
- acceptance/adoption of any feature design or candidate;
- recording any separate acceptance not stated in this file;
- Git operations of any kind;
- building the browser/interface now.

Everything in that second list remains a separate, later, separately authorized step.

---

# 22. Plain-language final rule

## The workflow in plain language

1. Ness chooses what N.H should mean and do.
2. ChatGPT/GPT checks the real project and finds all genuine choices.
3. Ness answers only the choices that really belong to him.
4. A fresh second check looks for important Ness choices the first pass may have missed.
5. When the meaning is settled, ChatGPT/GPT works out the exact mechanical design.
6. Claude applies that design to the file.
7. ChatGPT/GPT checks the actual result.
8. If a new real Ness choice appears, the process returns to Ness.
9. Nothing is accepted until Ness accepts it.

## The rule itself

When N.H needs to know **what Ness wants**, ask Ness properly.

When N.H only needs to know **how to build the mechanics**, do the mechanical work without bothering Ness.

If the real design needs many Ness choices, ask many — but in manageable groups, after checking what is already known, after a fresh second check for anything the first pass missed, and remember the answers so Ness does not have to keep rebuilding the design from old chats.

The interview continues until the feature is clear enough that the remaining work is mechanical.

Then ChatGPT/GPT-5.6 Sol works out exactly what that mechanical design is, Claude applies it to the file, a fresh independent check audits the actual result, mechanical problems are fixed through a prepared correction specification rather than invented, and any genuinely new Ness choice comes back through the interview.

Ness remains the person who decides what N.H is.

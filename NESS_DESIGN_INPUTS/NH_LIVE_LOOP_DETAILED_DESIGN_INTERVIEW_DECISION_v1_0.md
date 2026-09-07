# N.H — Live Loop Detailed Design Interview Decision v1.0

**Filename:** `NH_LIVE_LOOP_DETAILED_DESIGN_INTERVIEW_DECISION_v1_0.md`  
**Decision owner:** Ness  
**Decision date:** 2026-08-09  
**Status:** NESS-APPROVED LIVE-LOOP BEHAVIOR DECISION — PRESERVED INPUT — NOT YET BUILT  
**Intended location:** `/home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP/NESS_DESIGN_INPUTS/`  
**Not authority:** This file does not replace Master V10, Decision Defaults, `cursorrules`, the Companion Governance file, the Design and Wiring Map, or any accepted N.H design.  
**Not implementation authorization:** This decision defines how the future design loop should behave. It does not authorize implementation of N.H production features, production stores, Master/Map integration, acceptance, adoption, or deployment.

---

# 1. Decision summary

Ness wants the future N.H live design loop to use a **deep, interactive design interview** whenever a feature or package contains many genuinely unresolved user-facing behavior choices.

The loop must not rush from a short feature idea directly into a large finished design by inventing the missing behavior.

Instead, it must:

1. deeply inspect the current N.H design first;
2. determine what is already settled;
3. determine what is mechanically implied;
4. determine what Claude/controller can solve mechanically;
5. identify every genuinely open choice that changes how N.H behaves for Ness;
6. ask Ness those genuine questions in manageable groups;
7. use Ness's answers to refine the next questions;
8. continue until the feature's meaning and intended behavior are sufficiently settled that the remaining design work is mechanical;
9. then allow Claude to create the versioned design candidate;
10. run independent Codex audit;
11. automatically correct mechanical blockers where authorized;
12. return to Ness if the audit exposes another genuinely open user-facing choice;
13. stop only when the current package is fit for its bounded job.

There is **no arbitrary total-question limit**.

If a complex feature genuinely requires many Ness decisions, the loop must ask as many as are actually necessary.

It must not reduce design quality merely to keep the interview short.

---

# 2. Why this behavior exists

N.H is a system whose meaning, behavior, permissions, priorities, privacy, and user experience belong to Ness.

Claude and Codex can solve a large amount of mechanical architecture.

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

Then Claude/controller designs the retry machinery mechanically.

---

# 6. Many questions are allowed and expected

There is no rule that a feature should require only a few questions.

If a feature genuinely contains:

- 10 open behavior choices;
- 20 open behavior choices;
- 40 open behavior choices;
- or more,

the loop may ask all of them if they remain genuinely necessary after the full source check.

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
- the loop wants extra confirmation.

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

The eventual Piece-3 controller design must provide a durable, inspectable way to preserve:

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

Those are mechanical design work.

But the user-facing requirement is settled:

> Ness must not have to repeatedly reconstruct prior design answers from memory or old chats.

The system must be able to resume the design interview from preserved decisions.

---

# 13. Exact-answer preservation versus interpretation

When Ness answers, the raw answer and the system's interpretation of that answer must not silently become the same thing.

The future design should preserve the distinction between:

- **Ness's actual answer**;
- **controller/AI structured interpretation**;
- **mechanical consequences derived from the answer**.

If the interpretation is uncertain in a way that could change N.H behavior, the loop must clarify with Ness rather than pretending certainty.

If the interpretation is mechanically obvious and does not change meaning, the loop should proceed without unnecessary clarification.

---

# 14. Returning from the interview to automatic design

The interview does not replace Claude/Codex.

It unlocks them.

Once the loop determines that the current feature/package has enough settled meaning for the remaining work to be mechanical:

1. the controller prepares the bounded design task;
2. Claude creates the new versioned candidate in the safe disposable workspace;
3. the controller verifies/promotes it according to its current safety rules;
4. Codex independently audits the actual candidate;
5. mechanical blockers may enter the authorized automatic Claude-correction loop;
6. a fresh Codex audit checks each corrected candidate.

No Ness question is needed merely because mechanical work exists.

---

# 15. If Codex finds a new genuine Ness choice

During audit, Codex may discover that a candidate filled in something the real sources did not settle.

If that issue changes N.H meaning, behavior, permissions, privacy, priorities, or user experience, it must not be sent to Claude as an ordinary mechanical correction.

The controller must stop the automatic correction path for that issue and route it to the future question-validation/design-interview stage.

The controller must **not** convert raw Codex prose directly into a Ness question.

Before Ness sees a question:

1. the issue must be independently classified;
2. relevant current N.H sources must be checked;
3. settled answers must be removed;
4. mechanical questions must be removed;
5. dependencies must be identified;
6. the remaining question must be rewritten in clear everyday language;
7. Ness must be told what the choice changes in real use.

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

This protects Ness from:

- fake choices;
- duplicate questions;
- model confusion;
- stale-source questions;
- mechanical questions;
- policy invention.

---

# 17. Interview stop condition

The design interview for a package is ready to stop when:

- all currently blocking genuine Ness decisions for that package are settled;
- no relevant user-facing behavior ambiguity remains that must be decided now;
- remaining open matters are correctly classified as:
  - dependent;
  - future/non-blocking;
  - or implementation work;
- the remaining current-package design work is mechanical.

The loop does not need to settle every future detail in the universe.

It must settle what the current bounded package genuinely needs.

---

# 18. Acceptance remains separate

Completing a design interview does not mean Ness accepted a candidate.

A Claude-created candidate is still only a candidate.

A Codex PASS is still only an audit result.

The live loop must never turn:

- "Ness answered the interview";
- "Claude completed the design";
- "Codex returned PASS";

into:

- accepted;
- adopted;
- `PACKAGE_COMPLETE`;
- Master-integrated;
- Map-integrated;
- implementation-authorized.

Ness's later explicit acceptance/adoption remains separate.

---

# 19. Relationship to future feature-intent files

This behavior is especially important for files such as:

`NH_FUTURE_FEATURE_DESIGN_INTENT_FOR_LIVE_LOOP_v1_0.md`

That file intentionally describes large feature intentions without mechanically settling every behavior detail.

When the future live loop processes such a feature-intent file, it must not treat missing detail as permission for Claude to invent a complete user experience.

It must use this Detailed Design Interview Decision to determine when a real interactive Ness interview is required.

---

# 20. Build order approved by Ness

Ness approved the following controller-development order:

## Piece 1 — Automatic Codex design audit

Status at the time of this decision:

**DONE / independent Codex re-audit PASS**

Piece 1 provides the independent audit of a newly created candidate.

## Piece 2 — Automatic Claude correction → fresh Codex re-audit loop

Status at the time of this decision:

**CURRENT BUILD WORK**

Piece 2 handles validated mechanical blockers automatically:

Codex BLOCKED  
→ bounded Claude correction  
→ new versioned candidate  
→ fresh Codex audit  
→ repeat within the safety limit  
→ PASS or stop safely.

Piece 2 must be completed and independently audited before Piece 3 begins.

## Piece 3 — Detailed Ness Design Interview / Question Validation

**This decision authorizes Piece 3 as the next controller behavior to design/build after Piece 2 passes.**

Piece 3 must provide the behavior defined in this file, including:

- genuine-question detection;
- complete relevant source checking;
- question validation;
- manageable grouped interviews;
- adaptive later questions;
- answer preservation;
- resume behavior;
- dependency handling;
- routing from audit-discovered genuine choices back to Ness;
- return from settled interview state into the mechanical Claude/Codex path.

Piece 3 must be separately implemented and independently audited.

## Controlled combined test

After Pieces 1–3 are complete, a real combined live-model test requires Ness's separate explicit authorization.

The test should prove at minimum:

1. a genuine open design issue reaches the interview stage;
2. settled/mechanical issues do not become Ness questions;
3. Ness's answer is preserved;
4. the loop can resume from the preserved answer;
5. mechanical design proceeds afterward;
6. Codex audit works;
7. mechanical blockers can be corrected;
8. a newly discovered genuine question returns to the interview rather than being mechanically invented.

## Interface

The browser/user interface comes **after** Pieces 1–3 are working.

The interface should be built around the real workflow rather than forcing the workflow to fit a prematurely designed UI.

The future interface may then show states such as:

- checking current N.H;
- questions ready;
- waiting for Ness;
- answer preserved;
- Claude designing;
- Codex auditing;
- Claude correcting;
- ChatGPT/question validation required;
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
- preserving answers for resume/continuation;
- returning audit-discovered genuine choices to the interview path;
- building this as controller **Piece 3 after Piece 2 passes**;
- delaying the browser/interface until Pieces 1–3 work.

## Not approved merely by this decision

This file does not authorize:

- beginning Piece 3 before Piece 2 passes;
- a particular Piece-3 code architecture;
- a particular schema/file format for question records;
- production N.H implementation;
- production stores;
- changing N.H authority files;
- hidden Master/Map integration;
- acceptance/adoption of future feature designs;
- pushing/committing repository changes without separate permission where required;
- building the browser/interface now.

---

# 22. Plain-language final rule

When N.H needs to know **what Ness wants**, ask Ness properly.

When N.H only needs to know **how to build the mechanics**, do the mechanical work without bothering Ness.

If the real design needs many Ness choices, ask many — but in manageable groups, after checking what is already known, and remember the answers so Ness does not have to keep rebuilding the design from old chats.

The interview continues until the feature is clear enough that the remaining work is mechanical.

Then Claude designs it, Codex checks it, mechanical problems are fixed automatically, and any genuinely new Ness choice comes back through the interview.

Ness remains the person who decides what N.H is.

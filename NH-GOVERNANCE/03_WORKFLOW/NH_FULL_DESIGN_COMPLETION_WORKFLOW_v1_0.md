# N.H — FULL DESIGN-COMPLETION AND BUILD WORKFLOW
## Version 1.0 — Prepared June 30, 2026

**Purpose:** This file defines the complete physical and intellectual workflow for finishing N.H safely and efficiently—from the current design-completion phase, through consolidation and adoption, and later into implementation.

**Status:** Approved operating method expressed as a full working procedure. This file is not architectural authority and does not modify Master V10.

---

# 1. THE PERMANENT ROLE MODEL

## Ness

Ness is:

- concept creator;
- policy decider;
- priority setter;
- final acceptance authority;
- adoption authority;
- implementation authorization authority.

Ness’s normal task is to answer genuine concept questions and approve or reject completed packages.

Ness does not need to solve technical architecture.

## ChatGPT

ChatGPT is:

- full-file reviewer;
- dependency coordinator;
- genuine-open-question detector;
- plain-language explainer;
- Claude-instruction writer;
- independent no-loss and wiring auditor;
- progress controller.

ChatGPT must protect Ness from repeated questions, fake choices, mechanical burdens, and silent concept drift.

## Claude

Claude is:

- technical architecture drafter;
- schema and contract designer;
- file-preparation worker;
- versioned-candidate creator;
- first-pass self-auditor.

Claude must not make Ness’s decisions.

## Cursor — later only

Cursor is:

- later code writer and patch executor;
- governed by `cursorrules`;
- inactive during design completion except for separately authorized disk inspection.

---

# 2. THE THREE PROJECT SPACES TO CREATE

## 2.1 ChatGPT Project

Upload or retain:

1. `NH_MASTER-20_CORRECTED_v10.md`
2. `NH_DECISION_DEFAULTS-S19_v2_2.md`
3. `cursorrules`
4. `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`
5. the current full Design and Wiring Map
6. `NH_CHATGPT_PROJECT_INSTRUCTIONS_v1_0.md`
7. accepted standalone design packages
8. current Claude output being audited

Paste the paste-ready instruction portion or use the entire ChatGPT instructions file as project knowledge.

ChatGPT is the place where:

- the next dependency is selected;
- Ness makes concept decisions;
- Claude instructions are prepared;
- Claude outputs are audited;
- progress is tracked.

## 2.2 Claude Project

Upload or retain:

1. the same four governing files;
2. the current full Design and Wiring Map;
3. `NH_CLAUDE_PROJECT_INSTRUCTIONS_v1_0.md`;
4. the exact current standalone accepted decisions relevant to the task;
5. the exact ChatGPT-prepared task instruction;
6. the source file Claude must transform.

Claude is the place where:

- technical design files are created;
- new versioned candidates are prepared;
- scoped corrections are applied;
- self-audit reports are generated.

Do not load several same-named competing map versions without clearly identifying the current source.

## 2.3 Local archive

Maintain folders such as:

- `/AUTHORITATIVE/`
- `/CURRENT_WORKING_MAP/`
- `/ACCEPTED_STANDALONE_DESIGNS/`
- `/CANDIDATES_UNDER_REVIEW/`
- `/HISTORICAL_PROVENANCE/`
- `/AUDIT_REPORTS/`
- `/LATER_IMPLEMENTATION/`

Do not move or rename existing protected files merely to match this example. The folder model is organizational guidance, not permission to modify the current archive.

---

# 3. PHASE 0 — PROTECT THE BASELINE

Before continuing design:

1. Confirm the current authoritative filenames.
2. Preserve Master V10 unchanged.
3. Preserve Decision Defaults unchanged.
4. Preserve `cursorrules` unchanged.
5. Preserve historical Masters.
6. Preserve the current map source.
7. Identify accepted standalone decisions not yet integrated.
8. Record the current date and project state.
9. Do not begin code or disk modifications.

**Physical action for Ness:** Upload the governing files and the three new workflow/instruction files into the correct AI projects. Do not edit the authoritative files.

---

# 4. PHASE 1 — ESTABLISH THE LIVE STATUS

ChatGPT compares:

- Master V10;
- current map;
- accepted standalone packages;
- current-session decisions;
- any completed work not reflected in the map.

Every register item receives a live status:

- `OPEN`
- `UNDER_REVIEW`
- `DECIDED_CONCEPT`
- `MECHANICS_PARTIAL`
- `PACKAGE_COMPLETE`
- `INTEGRATED_IN_CANDIDATE`
- `ADOPTED`
- `IMPLEMENTATION_BLOCKED`
- `READY_FOR_LATER_BUILD`
- `BUILT_UNVERIFIED`
- `BUILT_VERIFIED`

The map itself is not silently edited. The live status may be kept in a separate progress ledger.

**Physical action for Ness:** Ask ChatGPT:  
“Reconcile the current project status against the full Master, full map, and all accepted standalone decisions.”

---

# 5. PHASE 2 — SELECT THE NEXT DEPENDENCY PACKAGE

ChatGPT uses the full dependency map.

Selection criteria:

1. genuine open Ness decision;
2. useful downstream unlock;
3. bounded scope;
4. no premature implementation;
5. no need to invent another policy;
6. no reopened settled rule;
7. no fake option.

Priority is dynamic, not a rigid A1-to-A33 numerical march.

Foundational items often unlock more work, but ChatGPT must verify the current state before each selection.

**Physical action for Ness:** Say:  
“Continue with the next safest dependency package.”

---

# 6. PHASE 3 — PRE-QUESTION FULL AUDIT

Before asking the question, ChatGPT reads:

- full Master V10;
- full current map;
- relevant Defaults;
- relevant `cursorrules`;
- relevant accepted packages;
- all affected components;
- all affected B-STRUCT items;
- all affected B-INT items;
- all affected B-CYCLE items;
- design-complete conditions.

ChatGPT classifies the issue:

- settled;
- implied;
- mechanical;
- dependent;
- genuine concept;
- future/non-blocking;
- later implementation.

Only a genuine concept reaches Ness.

**Quality gate:** If the issue is mechanical, ChatGPT or Claude owns it. Ness is not asked.

---

# 7. PHASE 4 — NESS MAKES ONE CONCEPT DECISION

ChatGPT presents:

1. plain meaning;
2. already-settled boundaries;
3. exact unresolved remainder;
4. realistic example;
5. real options;
6. consequence of each;
7. mechanical recommendation only if appropriate;
8. one direct question.

Ness approves, rejects, modifies, or pauses.

**Physical action for Ness:** Answer in ordinary language. Ness does not need technical terminology.

---

# 8. PHASE 5 — FORMALIZE THE ACCEPTED DECISION

ChatGPT creates a normalized decision record.

Minimum fields:

- ID;
- date;
- source question;
- Ness’s exact answer;
- normalized rule;
- examples;
- affected components;
- affected registers;
- unlocked mechanics;
- blocked mechanics;
- must-nevers;
- integration status;
- authority status.

ChatGPT confirms plainly what was decided.

No authoritative file changes yet.

---

# 9. PHASE 6 — DEFINE THE UNLOCKED MECHANICAL PACKAGE

ChatGPT determines exactly which mechanical work is unlocked.

The package may include:

- B-STRUCT schema;
- identity/reference design;
- lifecycle;
- state machine;
- transaction boundaries;
- idempotency;
- duplicate prevention;
- crash recovery;
- retry;
- partial-completion recovery;
- fail-closed behavior;
- §0B logging;
- upstream/downstream interfaces;
- UI mechanics;
- testable design-complete condition.

Anything still dependent on another Register-A item remains explicitly open.

**Critical rule:** Do not force-finish a B item by choosing another policy silently.

---

# 10. PHASE 7 — CHATGPT PREPARES THE CLAUDE INSTRUCTION

Before Claude works, ChatGPT writes one precise, ready-to-send task message.

It must state:

- authority order;
- exact source files;
- exact accepted decision;
- exact scope;
- exact output file;
- exact permitted changes;
- exact forbidden changes;
- no-loss requirements;
- mechanical completeness requirements;
- open dependencies;
- verification stages;
- delivery requirements.

**Physical action for Ness:** Copy the exact ChatGPT instruction into the Claude Project without paraphrasing it.

---

# 11. PHASE 8 — CLAUDE CREATES THE VERSIONED PACKAGE

Claude:

1. reads the instruction;
2. reads full relevant sources;
3. creates preservation inventory;
4. drafts only approved scope;
5. leaves unresolved policies open;
6. adds complete recovery/logging/wiring;
7. creates a new versioned file;
8. runs self-audit;
9. reports changes and dependencies.

**Physical action for Ness:** Download Claude’s actual file and upload it into the ChatGPT Project for audit.

Do not rely on screenshots or Claude’s summary alone.

---

# 12. PHASE 9 — CHATGPT INDEPENDENT AUDIT

ChatGPT audits the actual file against:

- Master V10;
- map;
- exact Ness decision;
- exact Claude instruction;
- source file;
- prior package versions.

Audit dimensions:

1. authority;
2. concept fidelity;
3. no loss;
4. scope;
5. schema;
6. wiring;
7. operation identity;
8. transactions;
9. idempotency;
10. duplicate prevention;
11. crash recovery;
12. retry;
13. partial completion;
14. fail-closed;
15. logging;
16. privacy/relevance/authority order;
17. DUMB/SMART;
18. root/reading;
19. quarantine/production;
20. no implementation.

ChatGPT gives Ness:

- one or two simple sentences;
- severity;
- one consolidated correction message if needed.

---

# 13. PHASE 10 — CORRECTION LOOP

If errors exist:

1. Ness sends ChatGPT’s exact correction instruction to Claude.
2. Claude creates a new corrected version or applies the permitted scoped correction.
3. Previous candidate remains preserved.
4. Claude reports only the correction.
5. ChatGPT re-audits the corrected file.
6. Repeat only until consequential issues are resolved.

Do not regenerate the whole architecture for a local correction unless the correction truly affects the whole file.

---

# 14. PHASE 11 — CLOSE THE PACKAGE

A package closes when:

- Ness decision is preserved;
- all unlocked mechanics are designed;
- still-open dependencies are named;
- Claude file passes audit;
- no authoritative file was modified;
- no code was written;
- Ness accepts the standalone package.

The package status becomes `PACKAGE_COMPLETE`.

“Package complete” does not mean the whole component or whole N.H system is complete if other policies remain.

**Physical action for Ness:** Say whether the package is accepted.

---

# 15. PHASE 12 — REPEAT THROUGH BLOCKING REGISTER-A WORK

Repeat Phases 2–11.

Recommended broad order, always subject to full dependency recheck:

## Meaning and memory foundation

- telling identity;
- meaning-to-technical mapping;
- hold-until-enough;
- grounded-enough acceptance;
- relevance modes;
- Person-Box evidence;
- Ness Person-Box;
- Living State Web;
- clash-response effects;
- Creation policy;
- reread modes;
- topic/provenance behavior.

## Privacy, authority, and learning

- privacy/influence removal;
- action risk;
- learning policies;
- BOP/OOP amendments;
- TSC naming;
- access-model relationship;
- layer coexistence/handoff.

## World, Wonder, voice, and mobile

- Wonder;
- world model;
- Ness’s World;
- mobile;
- voice model;
- phone modes;
- conversation rehearsal;
- WhatsApp child-data policy.

This order is a planning aid, not authority.

A27 and A28 are non-blocking future-governance notes unless Ness chooses to open them.

---

# 16. PHASE 13 — COMPLETE B-STRUCT

After enough policies are decided, close remaining structural mechanics.

For every B-STRUCT item verify:

- all policy inputs exist;
- schema is complete;
- IDs are stable;
- references do not duplicate evidence;
- lifecycle is complete;
- recovery is explicit;
- §0B logging is complete;
- dependencies are closed or explicitly reserved.

Special universal prerequisite:

**B11 active writable-batch architecture must be complete before any new root-producing front door or cycle is allowed to write.**

---

# 17. PHASE 14 — COMPLETE B-INT CROSS-COMPONENT WIRING

Complete B-INT-1 through B-INT-11.

Each integration must specify:

- exact caller/callee;
- contract;
- gate order;
- operation identity;
- failure propagation;
- stale-state behavior;
- restart behavior;
- duplicate prevention;
- logging on each side;
- no double evidence.

Mandatory cross-checks:

- §7Q before §7R;
- §7Q first and SACL second for delivery;
- SACL scope before retrieval where applicable;
- LMAC stateless;
- BOP/OOP write through shared store;
- §7D source evidence correct;
- §7M downstream of §7D;
- TSC two-phase and crash continuation;
- voice enrollment path;
- Layer-2/Layer-3 coexistence;
- component-specific logging everywhere.

---

# 18. PHASE 15 — COMPLETE B-CYCLE END-TO-END PATHS

Complete B-CYCLE-1 through B-CYCLE-9 where applicable.

Every cycle must include:

- operation identity;
- start event;
- durable checkpoints;
- transaction boundaries;
- idempotency;
- duplicate prevention;
- crash at every stage;
- retry;
- partial completion;
- fail-closed;
- final state;
- logs;
- no-double-evidence.

The key cycles include:

- chat intake → response;
- research;
- mobile Manual Sync;
- TSC promotion;
- action → result;
- quarantine → production;
- creation;
- reread;
- Wonder, only after A17 permits a route.

---

# 19. PHASE 16 — SYSTEM-WIDE CONSISTENCY AND NO-LOSS AUDIT

ChatGPT performs an independent whole-project audit.

The audit must compare:

- Master V10;
- Decision Defaults;
- `cursorrules`;
- current map;
- every standalone accepted package;
- every Register-A decision;
- every Register-B design;
- every B-INT;
- every B-CYCLE;
- every controlled identifier;
- every open/future/implementation item.

The audit searches for:

- contradiction;
- lost design;
- duplicated design;
- stale authority;
- wrong owner;
- unowned open slot;
- circular evidence;
- direct-write bypass;
- missing operation identity;
- incomplete recovery;
- duplicate execution;
- missing logging;
- privacy/relevance inversion;
- Layer mixing;
- premature implementation.

Produce a full audit report and a single correction plan.

---

# 20. PHASE 17 — CONSOLIDATE INTO A NEW MAP CANDIDATE

Only after standalone packages and wiring are complete:

1. ChatGPT prepares a very precise consolidation instruction.
2. Claude creates a new versioned Design and Wiring Map candidate.
3. The old map remains untouched.
4. Claude includes every accepted package.
5. Claude updates register status without erasing provenance.
6. Claude preserves all open future notes.
7. ChatGPT performs a full line-level and concept-level audit.
8. Claude corrects verified issues.
9. Ness reviews and explicitly accepts the new working map.

This still does not modify Master V10.

---

# 21. PHASE 18 — DECIDE WHETHER A NEW MASTER CANDIDATE IS NEEDED

After the complete design map is accepted, ChatGPT determines whether the accepted standalone and map work should be integrated into a new Master candidate.

If yes:

1. ChatGPT prepares a protected Master-candidate instruction.
2. Claude derives a new version from Master V10.
3. Master V10 remains untouched.
4. No-loss comparison is mandatory.
5. The candidate clearly states that it is not adopted.
6. ChatGPT independently audits it.
7. Ness alone adopts it.

Do not create a new Master after every small package. Consolidate at a stable milestone.

---

# 22. PHASE 19 — IMPLEMENTATION READINESS GATE

Implementation may begin only when all are true:

- every blocking concept is decided;
- dependent mechanics are complete;
- all integration wiring is complete;
- all cycles are complete;
- Layer coexistence is defined;
- full no-loss audit passes;
- Ness accepts the complete design;
- Ness explicitly authorizes implementation.

Then create a separate implementation plan.

Design order is not automatically build order.

---

# 23. PHASE 20 — LIVE DISK VERIFICATION

Before code:

- verify actual project path;
- verify files;
- verify stores;
- verify seals;
- verify validators;
- verify engine files;
- verify gold files;
- verify Chroma;
- verify Layer-2 activity;
- verify protected paths;
- verify stale documentation claims;
- record hashes and current state.

Trust disk, never remembered status.

No code instruction should depend on an unverified live fact.

---

# 24. PHASE 21 — IMPLEMENT ONE PROTECTED COMPONENT AT A TIME

Later implementation loop:

1. select one build package;
2. verify design and dependencies;
3. verify disk;
4. ChatGPT prepares exact Cursor instruction;
5. Cursor produces a dry-run proposal;
6. Ness approves protected changes;
7. Cursor applies change;
8. tests run on non-production paths;
9. ChatGPT audits code and behavior;
10. Claude updates architecture documentation only through a new versioned candidate when authorized;
11. component is integrated;
12. move to next component.

No “build the whole system” coding pass.

---

# 25. PHASE 22 — TESTING AND PROMOTION

Testing layers include:

- unit tests;
- schema tests;
- idempotency tests;
- duplicate-prevention tests;
- crash checkpoint tests;
- retry tests;
- privacy/access tests;
- cross-layer tests;
- gold tests;
- held-out tests;
- manual inspection;
- full-cycle tests;
- failure injection;
- restart recovery.

Production reading promotion requires:

- gold evidence;
- held-out evidence;
- manual inspection;
- memory-health architecture;
- physical authorization marker;
- separate approved change.

Passing tests makes a candidate eligible. It never self-adopts or self-promotes.

---

# 26. PHASE 23 — GO-LIVE

Before go-live:

- security and identity boundaries verified;
- dangerous mobile command path removed and verified;
- production gates active;
- rollback/recovery tested;
- logs working;
- privacy gates working;
- fail-closed behavior tested;
- legacy Layer 2 status explicitly governed;
- Ness authorizes activation.

Go-live is a separate explicit decision.

---

# 27. PHYSICAL HANDOFF LOOP FOR NESS

For ordinary design work, Ness physically does only this:

1. In ChatGPT, say:  
   **“Continue with the next safest dependency package.”**
2. Answer the one genuine concept question.
3. Copy ChatGPT’s exact Claude instruction.
4. Paste it into the Claude Project.
5. Download Claude’s actual output file.
6. Upload the file into the ChatGPT Project.
7. Read ChatGPT’s plain audit result.
8. If needed, copy the correction instruction back to Claude.
9. Approve the completed package.
10. Repeat.

Ness should not manually edit the design files between Claude and ChatGPT. Manual editing makes no-loss verification harder.

---

# 28. STANDARD READY-TO-USE PROMPTS

## 28.1 Start next package in ChatGPT

> Continue with the next safest dependency package. Before asking me anything, thoroughly review the full authoritative Master V10, the full current Design and Wiring Map, all accepted standalone decisions, and the complete dependency map. Determine what is settled, implied, mechanical, dependent, or genuinely open. Ask me only the genuinely unresolved concept choice, in plain language, one decision at a time. Do not modify any file or begin coding.

## 28.2 Ask ChatGPT to prepare Claude instruction

> I accept this decision. Normalize it, identify every component and Register-B item it unlocks, leave every still-dependent policy open, and prepare one exact ready-to-send instruction for Claude. Define authority, scope, no-loss rules, versioned output filename, verification stages, and final audit requirements. Do not modify an authoritative file.

## 28.3 Ask ChatGPT to audit Claude output

> Audit this actual Claude output against the full Master V10, full current Wiring Map, the accepted decision, and the exact instruction Claude received. Check concept fidelity, no-loss, wiring, dependencies, operation identity, transactions, idempotency, duplicate prevention, crash recovery, retry, fail-closed behavior, logging, and phase discipline. Explain any consequential issue simply, then give me one consolidated exact correction message for Claude.

## 28.4 Ask Claude to execute only the exact task

Use the exact message prepared by ChatGPT without summarizing or paraphrasing it.

---

# 29. FILE NAMING AND STATE RULES

## 29.1 Suggested states

- `DRAFT`
- `CANDIDATE`
- `AUDITED_CANDIDATE`
- `ACCEPTED_STANDALONE`
- `ADOPTED_AUTHORITATIVE`
- `HISTORICAL`

Do not use `FINAL` as a substitute for adoption.

## 29.2 Suggested filenames

Standalone decision package:

`NH_ACCEPTED_<PACKAGE_NAME>_v1.md`

New working candidate:

`NH_<FILE_NAME>_v<version>_CANDIDATE.md`

Audit:

`NH_AUDIT_<TARGET_FILE>_v<version>.md`

Progress ledger:

`NH_DESIGN_COMPLETION_PROGRESS_v<version>.md`

A filename does not create authority. Ness’s adoption does.

---

# 30. PACKAGE QUALITY CHECKLIST

A package is ready to close only if:

- [ ] Ness decided the real policy.
- [ ] Settled boundaries are preserved.
- [ ] No fake choice remains.
- [ ] Mechanical scope is explicit.
- [ ] Remaining dependencies are named.
- [ ] Record identities are stable.
- [ ] References do not duplicate evidence.
- [ ] Transaction boundaries are explicit.
- [ ] Idempotency is explicit.
- [ ] Duplicate prevention is explicit.
- [ ] Crash recovery is explicit.
- [ ] Retry is explicit.
- [ ] Partial completion is explicit.
- [ ] Fail-closed behavior is explicit.
- [ ] §0B logging is explicit.
- [ ] Privacy/relevance/authority order is correct.
- [ ] DUMB/SMART boundary is correct.
- [ ] Root/reading boundary is correct.
- [ ] Quarantine/production boundary is correct.
- [ ] No code was written.
- [ ] Actual file was delivered.
- [ ] ChatGPT audited the file.
- [ ] Ness accepted the package.

---

# 31. WHO DECIDES WHAT — QUICK MATRIX

| Work | Ness | ChatGPT | Claude | Cursor |
|---|---|---|---|---|
| Define N.H concept | Decides | Checks consistency | Does not decide | No role |
| Choose policy | Decides | Explains genuine choice | Leaves open until decided | No role |
| Select next safe dependency | Controls priority | Recommends after full audit | No role | No role |
| Mechanical architecture | Reviews outcome | Defines requirements/audits | Drafts | No role |
| Versioned design file | Accepts | Specifies/audits | Creates | No role |
| Adopt authoritative file | Sole authority | Verifies readiness | Never adopts | Never adopts |
| Code implementation | Authorizes | Specifies/audits | Architecture support only | Writes code later |
| Protected file change | Approves | Verifies instruction | Does not bypass | Executes under rules |
| Disk truth | May run/authorize checks | Requires evidence | Must not assume | Verifies later |

---

# 32. FASTEST-SAFE PRINCIPLES

To move quickly without creating future rework:

1. Read full authority before each question.
2. Ask only genuine concept decisions.
3. Complete unlocked mechanics immediately.
4. Leave dependent policy open.
5. Use standalone packages.
6. Audit actual files, not summaries.
7. Correct locally rather than regenerate globally.
8. Consolidate only at milestones.
9. Keep design and implementation separate.
10. Never trade no-loss for speed.

The fastest route is the route that avoids needing to rebuild the architecture later.

---

# 33. CURRENT STARTING POINT — REVERIFY BEFORE USE

As of June 30, 2026:

- Master V10 is authoritative and immutable.
- The current map is a candidate working artifact.
- A1 Engine C substantive gold cases were accepted in conversation.
- The standardized standalone gold file, final mechanical audit, versioning, and sealing remained.
- Accepted live-memory/live-quarantine decisions existed outside the map.
- Provisional Meaning Engine web-expansion work existed outside the map.
- A2 was a logical candidate for the next dependency package, but the dependency map does not permanently mandate it as first.

This status is informational only and must be updated from actual current files and Ness’s latest decisions.

---

# 34. THE ENTIRE WORKFLOW IN ONE LINE

**ChatGPT verifies and frames → Ness decides → ChatGPT specifies → Claude designs and creates the versioned file → ChatGPT independently audits → Ness accepts/adopts → only after the full design is complete does Cursor implement under protected approval.**

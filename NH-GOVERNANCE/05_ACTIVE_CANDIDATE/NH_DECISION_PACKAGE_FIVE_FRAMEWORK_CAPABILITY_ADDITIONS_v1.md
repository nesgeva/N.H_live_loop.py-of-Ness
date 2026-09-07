# N.H DECISION PACKAGE — FIVE FRAMEWORK CAPABILITY ADDITIONS

**Filename:** `NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md`  
**Status:** Ness-approved standalone strategic direction decision; not yet mechanically designed as five complete packages; not integrated; not implemented  
**Date:** 2026-08-04  
**Authority owner:** Ness  
**Origin:** Architectural review of the public `nesgeva/NH-GOVERNANCE` repository, followed by Ness's explicit acceptance of the direction  

## Authority order

1. `NH_MASTER-20_CORRECTED_v10.md`
2. `NH_DECISION_DEFAULTS-S19_v2_2.md`
3. current `cursorrules`
4. `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`
5. the current Design and Wiring Map, subordinate to the files above
6. accepted standalone packages and their acceptance or closure records, within their stated scopes

Master V10 governs every conflict. This package does not overwrite, silently patch, supersede, or integrate into any governing file. Any later integration must use a new versioned candidate, preserve this file unchanged, undergo independent audit, and require Ness's separate acceptance or adoption where applicable.

---

## 1. What this package is

This package records Ness's accepted strategic direction that N.H should eventually gain five framework-level capabilities:

1. an Authority Integrity Control Plane;
2. a Unified Durable Operation Kernel;
3. a Provenance-First Multi-Index Memory Fabric;
4. a Bounded Self-Healing Execution Laboratory;
5. a Governed Capability Registry and Sandboxed Tool Forge.

These are additions to the future N.H architecture. They are intended to make N.H's already-settled safety, memory, provenance, recovery, privacy, and human-authority rules work together as one coherent, enforceable, testable framework.

This is a **strategic direction package**, not five finished mechanical designs. It settles that these capability directions belong in N.H's future design, subject to the boundaries in this file. It does not settle every schema, identifier, interface, threshold, storage choice, retry value, tool permission, model choice, or implementation detail.

---

## 2. Why these additions are needed

N.H already contains unusually strong design for:

- Ness remaining the decider;
- models remaining replaceable and non-authoritative;
- raw source material remaining separate from interpretations;
- memory adding new layers instead of silently rewriting history;
- confidence remaining metadata rather than authority;
- relevance remaining purpose-scoped rather than truth;
- privacy, access, and protected-output gates;
- operation identity, retry, duplicate prevention, crash recovery, and fail-closed behavior in multiple packages;
- quarantine and separate authorization before production use;
- explicit provenance and append-only operational history.

The accepted architectural finding is that N.H does **not** primarily need more uncontrolled autonomy. Its larger need is to turn these existing rules into shared framework mechanisms that are consistently applied across components.

The five additions therefore strengthen coherence and enforcement. They must not create a second competing architecture, a parallel authority path, or a model-controlled substitute for Ness.

---

## 3. Existing architecture preserved

Nothing in this package reopens or replaces the existing accepted or governing designs for:

- B9 retry-state architecture;
- B11 active writable-batch architecture;
- B16 quarantine-promotion evidence architecture;
- B-HOLD hold-until-enough lifecycle;
- the §7E intake and pre-ingest boundary;
- the §7F positional and semantic retrieval channels;
- the §7G Meaning Engine and Reading Proposal Acceptance Check;
- the §7H reread lifecycle;
- §7Q privacy, exclusion, restriction, redaction, deletion, and influence boundaries;
- §7R attention and relevance control;
- TSC, SIA, SACL, BAI, LMAC, BOP, OOP, or related accepted packages;
- the Layer 2 / Layer 3 protection boundary;
- the live dual-model handoff decision;
- any accepted bundle, integration package, cycle package, closure record, or earlier Ness decision.

Where an addition shares mechanics with an accepted package, the later work must **reuse, unify, or reference the accepted mechanism**. It must not quietly redesign it or build a parallel version.

---

# ADDITION 1 — AUTHORITY INTEGRITY CONTROL PLANE

## 4. Purpose

The Authority Integrity Control Plane is the deterministic part of N.H that answers:

> Which exact file, version, decision, package, or record governs this operation, and what evidence proves that status?

Its purpose is to prevent stale status wording, duplicated authority statements, misplaced candidates, missing closure records, or incomplete project context from causing N.H or an assisting model to follow the wrong rule.

## 5. What it should add

The later mechanical design should provide a machine-readable authority and artifact ledger capable of recording or deriving, at minimum:

- exact filename and controlled path;
- exact content identity or hash;
- version and lineage;
- artifact class, such as authority, candidate, accepted standalone package, closure record, working map, historical record, or implementation artifact;
- current status;
- governing authority above it;
- explicit supersession or replacement relationships;
- the acceptance, adoption, or closure evidence that changed its status;
- dependency relationships;
- scope of authority or accepted effect;
- whether the artifact may currently be read, modified, integrated, implemented, or only preserved;
- the repository or local snapshot against which the status was verified;
- contradictions, missing evidence, or unresolved authority state.

It should support a deterministic pre-operation check that either:

- returns the verified governing set and an authority snapshot reference; or
- stops and reports that authority cannot be proven safely.

## 6. Relationship to current N.H design

This control plane operationalizes existing rules that already require:

- actual files over remembered descriptions;
- Master V10 over subordinate artifacts;
- candidates not becoming authority automatically;
- preserved version history;
- no hidden integration;
- explicit Ness acceptance or adoption;
- one package at a time;
- status claims supported by evidence.

It does not create new architectural authority. It verifies and exposes the authority that Ness and the governing records already established.

## 7. Must-nevers

The Authority Integrity Control Plane must never:

- decide that a candidate is accepted or adopted merely because its wording sounds final;
- edit a governing, accepted, or historical file;
- repair a contradiction silently;
- select a policy winner when the governing evidence is genuinely contradictory;
- invent a missing acceptance record;
- turn repository placement into authority by itself;
- treat a model's summary as proof of file state;
- overwrite history while reconciling status.

When evidence is incomplete or contradictory, it must fail closed, preserve the conflicting evidence, and surface the exact problem.

## 8. Timing

The decision is recorded now. Detailed design should occur before final whole-system consolidation because every later implementation, audit, migration, and tool call benefits from a reliable authority snapshot.

Implementation remains blocked until the complete N.H design is accepted and Ness separately authorizes building.

---

# ADDITION 2 — UNIFIED DURABLE OPERATION KERNEL

## 9. Purpose

The Unified Durable Operation Kernel is the shared DUMB execution machinery underneath N.H operations.

Its purpose is to make operation identity, waiting, cancellation, retry, duplicate prevention, checkpointing, crash recovery, stale-result rejection, and terminal evidence work consistently across the system instead of being reinvented separately by every component.

It is not a reasoning model, policy engine, meaning engine, or autonomous planner.

## 10. What it should add

The later mechanical design should define a common operation envelope and lifecycle that can be specialized by existing components. Candidate fields or references to design later include:

- canonical `operation_id`;
- operation class and version;
- parent and child operation relationships;
- branch or conversation identity;
- generation or revision number;
- authority snapshot reference;
- policy and authorization references;
- canonical input identity;
- component-owned duplicate-prevention identity;
- idempotency key for external or stored effects;
- checkpoint and recovery references;
- current durable state;
- waiting or hold reason;
- cancellation generation;
- stale-after or invalidation condition;
- retry-group and attempt references where B9 applies;
- committed effect references;
- terminal evidence reference;
- one-operation/one-log §0B relationship.

The kernel should provide shared mechanics for operations such as:

- live conversation turns;
- heavy/light model handoffs;
- asynchronous reading jobs;
- research runs;
- root ingestion;
- TSC promotion;
- quarantine promotion;
- rereads;
- action execution and action-result return;
- mobile synchronization;
- later validation and self-healing laboratory runs.

## 11. Relationship to B9 and other accepted mechanics

This addition does **not** mean creating a second retry system.

- B9 remains the accepted retry-state architecture for retry classification, admission, attempt state, and recovery.
- B11 remains authoritative within its accepted scope for active writable batches and ingestion claims.
- B16 remains authoritative within its accepted scope for quarantine promotion.
- B-HOLD remains authoritative within its accepted scope for holds and release.
- Component-owned canonical identities remain the actual duplicate-prevention authority at their seams.

The Unified Durable Operation Kernel should provide a common framework in which these accepted mechanics plug in. It should reference and enforce them, not replace or weaken them.

## 12. Dual-model effect

For the accepted live dual-model architecture, the kernel should eventually make it possible to:

- open one identified live operation;
- attach new relevant user information to that operation;
- increment or replace the active generation when the conversation meaning changes;
- cancel or supersede obsolete heavy-model work;
- reject a heavy-model brief produced for an older generation;
- prevent duplicate final delivery;
- recover safely after a process or machine interruption;
- use a declared fallback when the heavy or light model is unavailable.

The exact cancellation policy, latency thresholds, and model-routing choices remain later design work.

## 13. Must-nevers

The operation kernel must never:

- choose substantive policy;
- decide that a rejected interpretation deserves another attempt;
- bypass privacy, access, relevance, acceptance, or production gates;
- treat technical success as substantive correctness;
- create a parallel execution path around a component's canonical seam;
- infer a terminal outcome without durable evidence;
- acknowledge success before the required terminal evidence is committed;
- use retry to bypass a hold, privacy refusal, substantive rejection, or indeterminate recovery state.

## 14. Timing

The strategic direction is accepted now. Its detailed mechanical design should be developed in dependency order and reconciled with B9, B11, B16, B-HOLD, B-INT, and B-CYCLE work before final system wiring closes.

Implementation occurs only after design completion and separate Ness authorization.

---

# ADDITION 3 — PROVENANCE-FIRST MULTI-INDEX MEMORY FABRIC

## 15. Purpose

The Provenance-First Multi-Index Memory Fabric is a set of rebuildable ways to find and organize N.H's preserved records without turning an index into memory authority.

Its purpose is to let N.H retrieve the right material through several clearly separated forms of structure instead of relying on one universal vector search.

## 16. Accepted direction

The future memory architecture should support multiple coordinated index or view channels over the same preserved source records. These may include:

1. **Thread and positional index** — exact source order, conversation neighborhood, and sequence.
2. **Semantic index** — conceptual similarity, clearly labeled as retrieval evidence only.
3. **Temporal index** — original source time, import time, N.H record time, validity or currentness intervals, and later evidence.
4. **Entity and Person-Box reference index** — references to people or objects without automatic identity merging.
5. **Accepted-connection graph** — only relationships admitted through the existing approved connection routes.
6. **Story, theme, telling, and clash index** — revisable perspective structures, not facts.
7. **Operational and provenance index** — which process retrieved, rejected, transformed, used, or did not use material.
8. **Future state or world views** — only after their governing policy and mechanics are separately settled.

The exact number, technologies, schemas, and storage layouts remain mechanical design choices.

## 17. Retrieval-plan record

A later design should allow each answer-producing or decision-support operation to preserve a retrieval-plan record containing, where relevant:

- declared purpose and mode;
- permitted sources and privacy scope;
- index channels consulted;
- channel versions and health state;
- query or selection parameters;
- retrieved record identities;
- exclusion and omission reasons;
- degraded or incomplete retrieval status;
- connection or relationship basis;
- the evidence passed to the model;
- the final context actually used.

This record must be operational provenance, not a second evidential vote for the retrieved material.

## 18. Relationship to current retrieval and memory rules

This addition preserves:

- position-based context for conversational sequence where already settled;
- positional and semantic channels remaining separate and labeled;
- roots remaining immutable;
- readings remaining linked additions;
- every real source item remaining its own Origin;
- related mixed media being connected rather than merged;
- original, import, and record times remaining distinct;
- similarity or co-retrieval not creating an accepted connection;
- Person-Boxes remaining linked views rather than second memory stores;
- model-produced relationships remaining proposals unless an accepted route admits them.

Indexes are derived machinery. The preserved roots, accepted records, and governing provenance remain above them.

## 19. Rebuild and degradation rule

Each index must be rebuildable from permitted source records and declared accepted relationships.

Index loss, corruption, staleness, or partial availability must produce:

- a visible degraded-state record;
- bounded fallback behavior;
- no claim of complete retrieval;
- no fabricated missing relationship;
- no deletion or rewriting of source memory.

## 20. Must-nevers

The memory fabric must never:

- merge two Origins because they are similar;
- accept a person identity or relationship from embeddings alone;
- turn a theme or repeated interpretation into a fact;
- allow an index to become the only surviving copy of memory;
- silently mix simulated, Wonder-origin, rejected, provisional, held, or unauthorized material with ordinary evidence;
- hide which retrieval channel produced an item;
- treat ranking as truth, certainty, authority, or permission;
- use a derived operational log as additional evidence for its own subject.

## 21. Timing

Detailed design belongs alongside the remaining memory, retrieval, Story, Person-Box, Living State, and whole-cycle wiring work. It should be completed before implementation of large-scale long-term memory behavior.

The initial implementation should begin with the smallest necessary channels and preserve room for later indexes without changing source identities.

---

# ADDITION 4 — BOUNDED SELF-HEALING EXECUTION LABORATORY

## 22. Purpose

The Bounded Self-Healing Execution Laboratory is a disposable local environment in which an AI coding agent may perform a controlled loop:

> run → observe failure → diagnose → make a bounded patch → test → repeat

Its purpose is to reduce repetitive manual correction while preventing an agent from gaining production authority or changing the rules by which it is judged.

## 23. What it should add

Each laboratory run should begin from an immutable run contract specifying at minimum:

- exact task and success condition;
- exact source snapshot and identity;
- disposable workspace path;
- files the agent may read;
- files the agent may modify;
- files and paths it must never access or modify;
- allowed commands and interpreters;
- network state and outbound-access rules;
- test and verification commands;
- protected tests the agent cannot edit;
- maximum attempt, time, compute, and cost budgets;
- correction-cycle accounting;
- required heartbeat or progress evidence where appropriate;
- required trajectory and artifact outputs;
- stop conditions;
- escalation conditions;
- final independent-verifier requirements.

A run should preserve a complete append-only trajectory of:

- observations;
- commands;
- file changes;
- test results;
- failures;
- corrections;
- budget consumption;
- checkpoints;
- terminal evidence.

## 24. Completion rule

The laboratory must not declare success merely because the agent says the task is complete or because one chosen test passes.

A successful run should require all declared conditions, including:

- the requested behavior passes;
- protected regression tests pass;
- protected safety tests pass;
- frozen-file identities remain unchanged where required;
- the patch stays within authorized scope;
- no forbidden access occurred;
- the final candidate and trajectory are complete;
- an independent deterministic verifier confirms the evidence.

The laboratory returns a candidate patch or artifact and its evidence. It does not accept, adopt, merge, deploy, or install it.

## 25. Relationship to the operation kernel and B9

The laboratory should eventually use the Unified Durable Operation Kernel for run identity, checkpoints, cancellation, recovery, duplicate prevention, budgets, and terminal evidence.

B9 may govern retry of technical laboratory operations. B9 does not by itself authorize an agent to redesign or patch code. The laboratory's patch authority comes only from the immutable run contract approved for that run.

## 26. Must-nevers

The laboratory agent must never be allowed to:

- modify N.H authority, accepted, closure, or historical files;
- access secrets, credentials, protected private stores, or live personal data unless a later narrowly authorized test explicitly requires a safe fixture substitute;
- write to production stores;
- weaken, delete, skip, replace, or rewrite protected tests;
- broaden its own permissions;
- alter its attempt, time, compute, or cost ceiling;
- commit, push, merge, deploy, or publish unless a separate later workflow explicitly authorizes that exact action;
- mark its own output accepted, adopted, verified, or production-ready;
- use network or provider access not declared in the run contract;
- hide failed cycles or rewrite the trajectory.

## 27. Timing

This capability is accepted as a future addition, but its implementation belongs to the later building and validation phase.

Its detailed design should be prepared only after the Authority Integrity Control Plane and Unified Durable Operation Kernel have sufficiently stable contracts, because the laboratory depends on reliable authority snapshots, operation state, budgets, and evidence.

---

# ADDITION 5 — GOVERNED CAPABILITY REGISTRY AND SANDBOXED TOOL FORGE

## 28. Purpose

The Governed Capability Registry is the single declared inventory of what N.H may call, what each capability may access, and under which authority and safety conditions it may run.

The Sandboxed Tool Forge is a future controlled path for producing candidate tool adapters without allowing generated code to become an active N.H capability automatically.

## 29. Capability registry contract

Every callable capability should eventually have a versioned contract containing, at minimum:

- stable tool or capability identity;
- version and executable identity or hash;
- owning N.H component;
- purpose and permitted operation classes;
- input and output schemas;
- read scope;
- write or effect scope;
- local, isolated, tunneled, or external execution location;
- permitted data classifications;
- privacy and access prerequisites;
- risk level;
- authentication and authorization requirements;
- explicit Ness-approval requirement where applicable;
- timeout, rate, cost, and resource ceilings;
- idempotency and duplicate-prevention behavior;
- reversibility, compensation, or irreversibility status;
- retry and recovery contract;
- required logs and evidence;
- installation, suspension, revocation, and replacement state;
- dependencies and incompatibilities.

The operation presented to a model should include only the capabilities permitted for the current identity, purpose, mode, authority snapshot, privacy state, and authorization.

## 30. Sandboxed tool-forge lifecycle

A model-generated or AI-assisted tool must remain a non-callable candidate until it passes a controlled lifecycle such as:

1. bounded proposal;
2. isolated source candidate;
3. static and dependency checks;
4. schema and contract validation;
5. unit and integration tests;
6. adversarial and permission-boundary tests;
7. protected-file and secret-access verification;
8. independent audit;
9. Ness's explicit acceptance for the stated scope;
10. separately authorized signed registration or installation.

The exact signing, packaging, and registration mechanics remain later design work.

## 31. Relationship to current N.H boundaries

This addition must preserve:

- no automatic connection to real N.H;
- no raw unrestricted command execution from user or phone input;
- §7P action-risk and permission boundaries;
- §7Q privacy and internal-use rules;
- SACL and BAI access requirements where applicable;
- LMAC remaining stateless within its accepted role;
- tool output remaining evidence or proposed material according to its origin, never automatically authoritative;
- external research remaining isolated and prompt-injection resistant;
- provider limitations remaining provider limitations rather than N.H policy.

## 32. Must-nevers

The registry or tool forge must never:

- expose every installed tool to every model or operation;
- allow a model to install or activate a tool it generated;
- permit undeclared file, network, credential, device, or store access;
- accept vague natural-language permissions where an exact capability boundary is required;
- allow token, credential, or authorization passthrough outside the intended audience and purpose;
- treat tool-call success as proof that the result is true or safe;
- allow a tool to create another active tool without the full candidate lifecycle;
- bypass Ness's required approval for sensitive or irreversible actions;
- create a second parallel gate around the accepted authority, access, privacy, or write-validation modules.

## 33. Timing

The capability registry's conceptual contracts should be designed before broad tool integration or autonomous action building.

The Sandboxed Tool Forge itself is a later implementation capability and should follow stable authority, operation, access, and laboratory foundations.

---

## 34. Dependency and work order

The accepted broad order is:

### Stage 1 — Record and preserve now

- Preserve this standalone decision package.
- Do not modify Master V10, the Map, Defaults, `cursorrules`, or accepted packages.
- Record that the five additions are accepted future directions.

### Stage 2 — Design in dependency order

1. Authority Integrity Control Plane.
2. Unified Durable Operation Kernel, reconciled with B9 and other accepted seam mechanics.
3. Provenance-First Multi-Index Memory Fabric, coordinated with retrieval and memory packages.
4. Governed Capability Registry contracts.
5. Bounded Self-Healing Execution Laboratory.
6. Sandboxed Tool Forge after the registry and laboratory foundations exist.

This is a dependency direction, not permission to begin all packages immediately or to mix them into one giant design.

### Stage 3 — Whole-system wiring

At the correct Bundle 8 or final whole-system wiring stage:

- connect each accepted detailed package to the existing components;
- ensure there is no duplicate authority, retry, index, permission, or logging mechanism;
- complete B-INT and B-CYCLE relationships;
- perform whole-system contradiction, no-loss, duplicate-execution, recovery, privacy, authority, and stale-state audits;
- create new versioned Map or Master candidates only under separate authorization.

### Stage 4 — Later implementation

Only after the complete design is accepted and Ness separately authorizes building:

- implement the authority control plane;
- implement the shared operation kernel;
- implement the initial memory indexes;
- implement the capability registry;
- implement the bounded laboratory;
- implement the tool forge only after its prerequisites are proven.

No stage in this file grants implementation permission by itself.

---

## 35. How detailed design will be produced

The five additions must not be mechanically designed as one uncontrolled mega-package.

For each addition, when its dependency point is reached:

1. ChatGPT checks the complete governing and relevant project files.
2. ChatGPT classifies what is already settled, mechanically implied, genuinely open, or later implementation work.
3. Ness answers only genuinely open meaning or policy choices.
4. ChatGPT prepares one exact bounded instruction for Claude.
5. Claude creates a new versioned candidate without modifying existing authority or accepted files.
6. ChatGPT independently audits Claude's actual file.
7. Ness decides whether to accept the package.
8. Integration and implementation remain separately authorized steps.

This package itself was created by ChatGPT because it records Ness's accepted direction. Claude is reserved for the later detailed mechanical candidates.

---

## 36. What is settled by this package

The following are settled as Ness-approved strategic direction:

- N.H should eventually have all five named capability additions.
- Their purpose is to unify and enforce existing N.H rules, not to grant uncontrolled autonomy.
- The Authority Integrity Control Plane must verify authority without creating it.
- The Unified Durable Operation Kernel must unify shared mechanics without replacing accepted component seams.
- The Multi-Index Memory Fabric must use derived, rebuildable views while preserved records remain authoritative.
- The Self-Healing Laboratory must be disposable, bounded, independently verified, and unable to deploy its own work.
- The Capability Registry must expose only purpose-authorized tools.
- Generated tools must remain non-callable candidates until separately accepted and registered.
- Detailed designs will be produced later, one bounded package at a time.
- Implementation requires later, separate permission from Ness.

---

## 37. What remains open

This package does not decide:

- final controlled component or Register IDs;
- exact schemas or field names;
- exact databases, index engines, graph stores, or workflow libraries;
- exact retry counts, timeouts, budgets, or backoff values;
- exact authority-manifest storage and update mechanism;
- exact operation state machine;
- exact memory-index count or build order beyond the broad dependency direction;
- exact thresholds for entity, connection, Story, State, or world retrieval;
- exact laboratory runtime, agent, container, or virtual-machine technology;
- exact tool packaging, signing, or installation technology;
- exact model choices;
- exact UI or inspection surfaces;
- whether a later detailed design exposes a genuine meaning or policy question for Ness;
- any still-open World, Wonder, action, mobile, voice, or Layer handoff policy not already settled elsewhere.

Those remain for their correct future packages and dependency points.

---

## 38. Adoption and implementation boundary

This standalone package records Ness's accepted direction.

It does **not**:

- modify or supersede Master V10;
- modify the current Design and Wiring Map;
- modify Decision Defaults or `cursorrules`;
- modify an accepted package or closure record;
- assign final Register IDs;
- claim that any of the five detailed designs is complete;
- authorize Claude to create all five designs now;
- authorize coding, implementation, migration, installation, production stores, live-disk changes, tool activation, deployment, or GitHub changes;
- accept any specific library, model, database, agent framework, or external protocol;
- close Bundle 8 or the complete N.H design.

Any future changed version of this package must be a new versioned file. This v1 must remain preserved unchanged.

---

## 39. Compact locked statement

> N.H will eventually add five framework-level capabilities: a deterministic authority checker, one durable operation kernel, a provenance-first multi-index memory fabric, a bounded self-healing execution laboratory, and a governed capability registry with a sandboxed tool-creation path. These additions exist to make N.H's current safety, memory, provenance, privacy, recovery, and Ness-authority rules work together as one coherent and testable framework. They must not create uncontrolled autonomy, parallel authority, automatic truth, automatic memory promotion, automatic tool activation, or production self-modification. Each detailed design will be created later as its own bounded versioned package, audited independently, accepted separately by Ness, and implemented only after separate build authorization.

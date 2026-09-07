# NH_LIVE_DESIGN_LOOP_CLAUDE_DESIGN_CODEX_AUDIT_ROLE_SPLIT_SUPERSESSION_v1_6_CANDIDATE.md

## 1. STATUS, PURPOSE, AND NESS-APPROVED DECISION

**Status:** CANDIDATE — NOT ACCEPTED — NOT ADOPTED — NOT AUTHORITATIVE — NOT INSTALLED — NOT IMPLEMENTED.

**Design owner and acceptance authority:** Ness.

**Scope:** one narrow role-split amendment to the current N.H live design loop. This file changes the default pre-initial-design path from a provider-backed Codex T3 mechanical-specification call to a provider-free local T3 task envelope, after which Claude independently designs the mechanics and a fresh independent Codex audit challenges the result.

**This file is design only.** It changes no live state, authority, controller, journal, package, or store. It authorizes no implementation or installation.

### 1.1 Ness-approved role split

The approved design direction this candidate expresses is:

```text
controller/question clearance
  -> provider-free local T3 creates the exact bounded task envelope
  -> Claude independently designs the mechanical solution inside that envelope
  -> fresh independent Codex reconstructs the requirements from sources
     and audits Claude's actual candidate
  -> Ness alone accepts or rejects
```

The role split is exact:

- **Ness owns** meaning, policy, priorities, permissions, privacy choices, genuine trade-offs, acceptance, adoption, and permission to build.
- **The controller owns** identities, currentness proofs, authority/source bindings, package and dependency bindings, question-clearance proofs, settled-answer bindings, the target candidate path, allowed and forbidden work, the design-only boundary, provider lifecycle, recovery, and every fail-closed gate.
- **Claude owns** independent mechanical design inside the controller-proved envelope and creation of the one permitted candidate plus its bound plain-language acceptance explanation in the same call.
- **Fresh Codex owns** independent reconstruction and challenge after the candidate exists. Codex does not merely compare Claude with an earlier Codex-authored solution.

Claude may choose mechanics only where all consequential Ness-facing meaning is already settled. Claude may not convert an open choice into a mechanical choice merely by writing an architecture for it.

### 1.2 Why this amendment is narrow

The accepted continuation design already places T3 between question clearance and initial Claude design. Its state-machine position remains; it becomes local/deterministic, makes zero provider calls, binds proved facts, lets Claude derive mechanics, and leaves fresh Codex as the independent check.

No second preparation engine, interview system, provider lifecycle, recovery system, source-discovery system, authority-identity system, dependency-manifest system, candidate-custody system, replay engine, or promotion path is introduced.

### 1.3 Provenance of this candidate

**Correction base:** `…ROLE_SPLIT_SUPERSESSION_v1_5_CANDIDATE.md` — SHA-256 `f4ed589f97b56ea61006bac514a12ce64694678115664e756ae50db5c2d4e08a`, `80308` bytes, `767` lines, recomputed from disk before this file was written.

**All six predecessors are preserved byte-identically** and none is edited, moved, re-headed, or incorporated as authority: v1.5 as above; `…v1_4_CANDIDATE.md` — SHA-256 `9cad68647e937a931ea2a72f92d51571c9916dbbfe1bdd3c7cf5167997262d75`, `71153` bytes, `698` lines; `…v1_3_CANDIDATE.md` — SHA-256 `9af2730eabd2394751269578bd8f944f98c84776cfc7fd6616bf0e48515974d3`, `59329` bytes, `651` lines; `…v1_2_CANDIDATE.md` — SHA-256 `fde90eb0b526dbd22434ac9dac2da2a8ae79caad255cb8425ccd72461d3af309`, `52633` bytes, `618` lines; `…v1_1_CANDIDATE.md` — SHA-256 `39a8ee5afa3349fc0e0ee00133835b25bb5427ef428560e4a36ac8379b6110f1`, `39949` bytes, `565` lines; `…v1_0_CANDIDATE.md` — SHA-256 `cdeb1afd99c17abae0095732bb54a3c7b83d82c732be493f35f906869d856405`, `102676` bytes, `1727` lines.

**Everything v1.3, v1.4 and v1.5 corrected is preserved here, unchanged in substance:** the acceptance-surface / speed-decision provenance (§2.4, §2.4a, §3.1, §7.4); the restart-safe STOP custody closure (§6.5 `STOP-CLOSURE-EXACT`, all seven rules); the v1.11 continuation-lineage rebase (§2.1, §2.2, §3.2, §8.5); the accepted §8.8 chain and its **IA/EV/JR/LR** field ownership (§2.5, §5.2, §5.3); the three-object separation with T4's corrected three-key `extra_inputs` (§5.4a); and the T4 prompt-material correction `T4-PROMPT-ENVELOPE` with `ENVELOPE-DIGEST-AGREEMENT` and its zero-provider refusal matrix (§5.4b). No governing source proved a conflict with any of them.

**v1.6 corrects one identity-boundary defect and nothing else.**

v1.5 §5.4 said: *"The work-item and provider-request identities therefore change whenever any envelope input changes."* **That is mechanically too broad, and it contradicts accepted §8.8.** P-SB12 fixes the blast radius deliberately: source and input facts that live outside `WORK_ITEM_KEYS` change `required_inputs_sha256`, hence the future `provider_request_identity`, **and nothing else**; §15.4 says the same of the stage-specific `extra`; and §28.2 item 2 records why it matters — had such movement moved work-item identity, an unrelated file change could have reset a bounded output-retry budget, "a real weakening, named and avoided."

**§5.4c states the corrected boundary exactly**, and §§5.4, 8.4, 9.4 and 10.1 carry its necessary consistency fallout. Nothing is added to the work-item identity contract, and everything §5.4b established stays exactly as it is.

---

## 2. GOVERNING BASIS AND ACCEPTED PREDECESSOR

### 2.1 Sources checked

This candidate was prepared against the real current files below. Their different standings are preserved rather than flattened:

| Source | Identity / standing used here |
|---|---|
| `NH_MASTER-20_CORRECTED_v10.md` | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c`; its own status caveat remains; this file adopts nothing |
| `NH_DECISION_DEFAULTS-S19_v2_2.md` | `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696`; adopted behavioral defaults |
| `cursorrules` | `5050d08825b93acd72a79d07946e43c8cbe537e079517ccfe66bcae8e30e96e9`; in-force project protections |
| `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | `cdcc6134e273014472ad288dc349ce0c7c525638a73929f7dede52d30d040aeb`; governance/archive distinctions |
| `NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865`; candidate Map; not promoted here |
| `NH_LIVE_LOOP_DETAILED_DESIGN_INTERVIEW_DECISION_v1_1.md` | `00160bff6187784ebfc8ad6babbf8f190b8ac5be9fc1711d1023a835d2620551`; Ness-approved preserved role input; only §3 clauses are candidates for supersession |
| continuation v1.8 | `448daa63b4899d4639dc5b7612985cb34e97732dcf4cbeac2c224c54f8ae51e2`, 303,820 bytes, 2,826 lines; **earlier accepted** for the standalone continuation-design scope |
| v1.8 closure receipt | `940cf3a29b0d41836322e6a55dbe9c56d491e840848d6ec80c2d24b4a9663dd4`; exact acceptance proof for v1.8, dated August 22, 2026; its §6 item 1 is the source-binding item the accepted §8.8 package later closes |
| continuation v1.9 | `711b89d30d36130eb2e9506e817429a5813e700b7c62fbbff97b340dc82a12ed`, 380,415 bytes, 3,249 lines; historical intermediate version, preserved unchanged |
| continuation v1.10 | `fafc27314aa09b3b4c3a7f2128b7faf495f0a6d3bedab5976e7d0465216ede64`, 443,388 bytes, 3,608 lines; historical intermediate version, preserved unchanged |
| **accepted continuation v1.11** | `1554a0802cc381666eab0e628ccca3adde025af03398e3c50a96dd522a89f548`, 485,472 bytes, 3,801 lines; **the later explicitly accepted continuation design** for that same standalone scope, and the layer this amendment supersedes against (§2.2, §3.2) |
| accepted §8.8 source-binding-currentness design | `5a49dd70765ecdfef97aa9cac0d4a0757ffe68842ef5d083397401df325c21bc`, 230,807 bytes, 3,137 lines; accepted standalone companion design (§2.5) |
| §8.8 package-complete closure receipt | `c8302a44eea4d33c9aa1238cd43aa6f234968add30f34b8535f1d374c6728749`, 19,484 bytes, 279 lines; exact acceptance proof dated August 24, 2026 |
| Build-vs-Borrow decision v1.0 | `7d3ac829fc08921a44ce6e1fc7b8f33673b6a5f7779e55d3325717571e96022b`; Ness-approved |
| accepted acceptance-surface `v1_15` | `b10727441ddf7502ff7525c79b0b71043b559502660dcc7c3b9001f0633ffcc6`, 409,297 bytes, 2,338 lines; **the later explicitly accepted acceptance-surface source**, proved by accepted continuation v1.11 §1 and §2.4 |
| acceptance-surface `v1_14` and its receipt | `c4f055f271cbeea246291986b1b11367fcfb1748466f346e642176df2b36b46a` / `72eeac903629beef4bec2cc8fe27fca78e9dfcecd85ebed37ad56946e38d2e3f` (August 21, 2026); **historical accepted provenance**, preserved unchanged and superseded as the governing acceptance-surface source by `v1_15` |
| Ness's later live-loop speed decision | stated by Ness for this amendment; no separate preserved decision file exists yet, so it carries no file identity — see §2.4a |
| installed controller sources whose **named mechanisms** this candidate reuses, read only and **not authority for any behavior** | `nh_loop.py` `74cc45e284531d038faa54abf1349f96eec94820d585a09e6b6e83e7fabf9e3f`; `nh_supervisor/canonical.py` `4f4cad66fbfe57026848b08afffba1d55a779f14817493f3b62c13bbf3f29fa6` |

### 2.2 Accepted predecessor and authority boundary

**The current accepted mechanical predecessor is v1.11**, not v1.8. The standing of the continuation lineage, stated exactly and without rewriting any version:

- Ness **earlier explicitly accepted v1.8** for the standalone continuation-design scope, proved by the separate closure receipt named in §2.1.
- Ness **later explicitly accepted v1.11** for **that same standalone continuation-design scope**, after an independent ChatGPT audit. That later acceptance is recorded by the accepted §8.8 design at its §0.5 — "the v1.11 acceptance fact this file relies on and never reopens" — and the accepted §8.8 closure receipt (§2.5) proves that design's own accepted standing.
- v1.9 and v1.10 are **historical intermediate versions**, preserved byte-identically with their own actual historical standings. Calling them "unaccepted history" as a statement about the current layer would be wrong now that a later version of the same lineage is accepted.

This amendment therefore supersedes **against v1.11** (§3.2). It does not rewrite v1.8, v1.9, v1.10 or v1.11, and it does not blanket-supersede v1.11: every v1.11 rule not named in §3.2 — including every correction v1.9, v1.10 and v1.11 introduced — remains fully operative.

The internal `CANDIDATE — NOT ACCEPTED` line frozen inside v1.8 and v1.11 is **historical pre-acceptance file text**. A separate acceptance record, not an in-place edit, proves the later accepted standing, exactly as the accepted §8.8 design states at its §0.5. This candidate follows the same version-safe discipline in both directions: it makes no claim of acceptance merely because a candidate file exists, and it does not read a frozen internal status line as proof that an accepted design is unaccepted.

### 2.3 Governing principles applied

This amendment creates no new governing principle. It applies the existing rules: disk proof over memory; Ness as decider; settled decisions not reopened; open meaning surfaced; mechanical facts derived locally; model prose not authority; versioned no-overwrite candidates; design distinct from build/adoption; durable provider custody/recovery; and independent audit before Ness acceptance.

### 2.4 Later behavior preserved by reference — and its exact standing

Each behavior below is preserved without redesign and bound to the exact record or decision that governs it. Identities are in §2.1.

| Later behavior | Governing source | Standing |
|---|---|---|
| Build-vs-Borrow / external-alternatives check | Ness-approved `NESS_DESIGN_INPUTS/NH_LIVE_LOOP_BUILD_VS_BORROW_EXTERNAL_ALTERNATIVES_DECISION_v1_0.md`, `7d3ac829…`, 8,642 bytes, 244 lines | Referenced only; not restated, not redesigned |
| The fresh independent audit judges the exact candidate and the **exact fixed explanation bytes** together — the joint candidate/explanation audit | accepted acceptance-surface **`v1_15` §7.8**, with its §7.1 content-stage row and §14 Phase A step A2 | Accepted standalone design. Referenced only |
| Part 7 is controller-derived, part 8 is controller-owned fixed material, the final assembly authors nothing and admits no provider, subprocess, or network wait, and the acceptance action itself invokes no model | accepted acceptance-surface **`v1_15` §6.5a, §7.1a–§7.1b, §7.8, §22.3 item 7** | Accepted standalone design. **Preserved unchanged; nothing below touches it** |
| Claude's candidate-producing and correction calls also produce the bound **semantically variable** explanation material, in that same call | **Ness's later live-loop speed decision (§2.4a).** It fills the *who, and in which call* slot that accepted `v1_15` §22.3 item 7 expressly leaves open, inside the *what and when* `v1_15` already fixes | Governing for this amendment: §6.1 requires it, §7.1–§7.2 audit it |
| A blocking fresh Codex audit itself carries the complete bounded mechanical correction instructions, with no separate correction-specification provider call | **Ness's later live-loop speed decision (§2.4a).** It supersedes Detailed Interview Decision v1.1 §15A **only** as to that separate provider call (§3.1) | Governing for this amendment: §7.4 states the preserved route |

Every installed provider, custody, terminal, retry, reconciliation, lease, retirement, and no-duplicate protection is likewise preserved by reference.

### 2.4a The later Ness decision this amendment records

For this live-loop speed change Ness explicitly settled two behaviors:

1. **the candidate-producing and correction Claude calls also produce the bound acceptance-explanation material**, so no separate explanation provider call is opened;
2. **the blocking fresh Codex audit itself carries the complete bounded correction instructions**, so no separate correction-specification provider call is opened.

Both are recorded here as **Ness's decision, and as nothing else**. Neither is derived from, justified by, or attributed to installed controller code: code that happens to implement a behavior never settles it, and this candidate makes no such claim anywhere.

**Its exact standing, stated honestly.** This decision was made for this amendment and is **not yet preserved as its own dated `NESS_DESIGN_INPUTS` record**, so it carries no file identity or hash of its own (§2.1). Preserving it as a separate decision record is a real open item and is owed. This candidate does not create that record, does not backfill one, and does not disguise its absence behind a code reference.

### 2.5 The accepted §8.8 source-binding-currentness package

Accepted v1.11 §8.8 and §26 item 1, and the v1.8 closure receipt's §6 item 1, carry forward one open mechanical question: whether a scope's binding should carry its newest validation's source facts rather than its anchor's, and what actually owns "is the source current".

**That question is now closed within its own standalone scope.** `NH_LIVE_DESIGN_LOOP_SOURCE_BINDING_CURRENTNESS_MECHANICAL_DESIGN_v1_3_CANDIDATE.md` (§2.1) was independently audited PASS and **explicitly accepted by Ness on August 24, 2026**, and marked `PACKAGE_COMPLETE` for that standalone mechanical-design scope by its own closure receipt. Its accepted bytes currently reside in the isolated design workspace `/home/ness/NH_LIVE_DESIGN_LOOP_SOURCE_BINDING_CURRENTNESS_DESIGN_v1_0_WORKSPACE/` rather than in `NH-GOVERNANCE/`; its receipt states plainly that this is a **placement** fact, not a standing fact, and no move is authorized here.

**Why it is in this amendment's governing chain.** The local T3 envelope binds source and currentness facts, and accepted §8.8 is the design that owns them. This amendment therefore verifies every such envelope field against it (§5.2–§5.4) and **treats accepted design, not installed code, as the authority wherever §8.8 governs a mechanic** — including where installed code is known to disagree with it.

**What this amendment does not do.** It does not redesign, extend, reinterpret, weaken, or re-open §8.8; it adds no field to it; and it takes no position on any item §8.8 leaves open. `PACKAGE_COMPLETE` there means the design work is finished and accepted **as a design**: nothing is adopted, integrated, installed, implemented, or authorized by it, and nothing is by this file either.

---

## 3. EXACT CLAUSES SUPERSEDED

This section is exhaustive. If a clause is not listed here, this candidate does not supersede it.

### 3.1 Detailed Interview Decision v1.1

If accepted, this candidate supersedes only the parts of `NH_LIVE_LOOP_DETAILED_DESIGN_INTERVIEW_DECISION_v1_1.md` that assign the exact mechanical solution to a pre-Claude OpenAI/ChatGPT/Codex specification step, make Claude only the applier of that prior solution, or require a separate correction-specification provider call:

- **§0.3 items 3–5; §1 steps 10–13; §2A; §5A; §14 steps 2–3; and repeated role wording in §§20–22:** pre-Claude Codex no longer chooses mechanics. Local T3 binds the envelope, Claude designs mechanics, and fresh Codex audits.
- **§5B only where it forbids Claude from choosing mechanics inside already-settled boundaries:** replaced by §6. Claude still stops on open Ness choices, authority conflicts, envelope contradictions, and out-of-scope work.
- **§15A only where it requires a separate correction-specification provider call:** under Ness's later decision (§2.4a), the blocking fresh Codex audit itself carries the complete bounded mechanical correction instructions, Claude performs one new-version correction, and a fresh independent Codex re-audits it. **Nothing else in §15A is superseded.** Its finding identities and evidence binding, its rule that Claude may not independently choose a different design solution, its correction caps and custody, its recovery rules, its return of a genuine Ness choice to Piece 3 through §15, its treatment of a byte-identical corrected candidate as a legitimate stop, and its fresh independent re-audit all remain exactly as Ness approved them.

This candidate does **not** supersede the Detailed Interview Decision's genuine-question definition, package-bounded inventory duty, separate validation, fresh independent coverage, no-question-limit rule, manageable interview behavior, settled-answer preservation, exact-answer versus interpretation separation, or single Piece-3 interview path.

### 3.2 Accepted continuation design v1.11

If accepted, this candidate supersedes only these rules of the **currently accepted** continuation design, v1.11 (§2.2). Each clause below was re-read in the v1.11 bytes and carries the same clause number and meaning it carried in v1.8, so the rebase changes the governing layer, not the surgical target. **Nothing else in v1.11 is superseded** — every correction and invariant v1.9, v1.10 and v1.11 introduced, including `T1-ACTIONABLE-ROOT` (§9.3a), the four non-actionable classifications, the T4 derived exhaustion field and its §7.4 guard, `close_open_consumption()`, the B9 retry values and exhaustion meaning, `LOOP_NEEDS_USER_ACTION`, Row D.1, T2 Paths A/B/C, E1–E5, and the Accept transaction, remains fully operative:

- **§7.2 T3 row; §7.4–§7.5 only where the command necessarily opens a provider request:** T3/command remain, but successful preparation is local envelope proof.
- **§13.1 and §§13.3–13.6c:** replaced by §5. Controller package/root/clearance selection in §13.2 and the §13.5 target/no-overwrite protections remain. This includes §13.4's `finalize_claude_instruction()` binding whose one operative design-content input was the model-authored `mechanical_design_specification`: that input becomes the controller-built canonical envelope (§5.4b), and the instruction stays controller-built under `PROMPT-NO-SECOND-BUILDER`.
- **§14.5 I8 and §14.5b only where they bind initial Claude to a provider-produced specification/T3 custody:** bind the reconstructable local envelope instead.
- **§14.5 I1 and I2, and §14.5a `INIT-RESULT-KEYS`, only where they admit exactly one candidate-producing result shape:** one second, disjoint `STOP` shape is added (§6.4). I1/I2 exactness is preserved per arm; I3–I7 and I10 keep full force on `CANDIDATE` and are inapplicable to `STOP`; I8 and I9 apply unchanged to both.
- **§7.6a `CLOSURE-INITIAL-PENDING` only where `candidate_custody_recorded` is the sole downstream closure of an `initial_design` custody:** `STOP` closes through the existing `review_signal_recorded` carrier instead (§6.5). `CLOSURE-READONLY` and every other §7.6a rule remain, and no new event type is created.
- **§17.2–§17.3a and §18 Rows F–H only for new provider-backed T3 positions:** new T3 is locally recomputed; historical T3 remains replayable; T4-and-later recovery remains.
- **§19.1 and §20.3 only for new `codex_next_design_task_preparation` dispatch:** no new T3 provider request; the same worker command receives a local result.
- **§23 R-9/R-9a only where prepared task means Codex-authored mechanics:** initial Claude still requires a current controller-proved envelope and cannot choose path/scope/authority/policy.
- **§§24–25 only for provider-backed T3 implementation/rehearsal:** later work uses §§9–10 here; this file changes no code/tests. v1.11's own added rehearsal `R115` and every non-T3 rehearsal row remain.

**Not superseded, and expressly preserved:** v1.11 §8.8 and §26 item 1 are not resolved by this amendment. They are closed within their own standalone scope by the separately accepted §8.8 package (§2.5), which this amendment binds to rather than redesigns.

### 3.3 What “superseded” does not mean

The named old clauses remain true historical evidence of the rules in force when their files were accepted or written. They are not erased, rewritten, reclassified, or treated as mistakes. A later acceptance of this candidate would establish a newer narrow rule for future operation only.

---

## 4. NEW ROLE SPLIT

### 4.1 T1 and T2 remain unchanged

Package selection, package binding, question discovery, question validation, and fresh independent coverage happen through their existing accepted/current routes. This amendment neither localizes nor merges those provider calls. It does not change the separate-fresh-coverage requirement.

T3 is reached only when the existing controller proves one package/root/scope, dependency clearance, completed question validation, completed fresh coverage, unlocked interview clearance, exact settled-answer binding, current source/relevant-source closure, and no Ness/action/authority/safety blocker.

This candidate invents no way to manufacture any of those proofs.

### 4.2 Local T3 owns constraint assembly, not design

Local T3 answers only:

> What exact already-proved facts and boundaries must the next Claude design obey?

It does **not** answer:

> What mechanical architecture should Claude choose inside those boundaries?

Local T3 may copy, reference, canonicalize, and digest controller-owned facts. It may perform deterministic checks. It may refuse when a required fact is absent, ambiguous, stale, contradictory, or no longer current. It may not reason through competing architectures, invent a design requirement, resolve an open Ness choice, summarize away a binding, or contact any provider.

### 4.3 Claude owns bounded mechanical design

Claude receives the exact envelope and the existing relevant source material. The envelope reaches Claude as the exact canonical §5.3 object carried in the controller-built prompt material and bound by `prompt_material_sha256` (§5.4b); the sources reach it by the existing source-supply route, unchanged. Inside that settled envelope, Claude independently chooses and expresses the safest coherent mechanical design.

That independence is intentional. Claude is not an uncritical transcriber of a Codex-authored architecture. It must read the actual sources, understand the constraints, and produce a design that satisfies them. The envelope limits what Claude may decide; it does not pre-decide every mechanism for Claude.

### 4.4 Fresh Codex owns independent challenge

After Claude's candidate and same-call acceptance explanation are durably held, a fresh Codex audit independently reconstructs what the package requires from the governing sources and controller bindings. It then tests Claude's chosen mechanics against those requirements.

Independence means Codex is not asked whether Claude faithfully copied Codex's earlier solution. There is no earlier Codex solution. Codex may agree with Claude, find a stronger mechanical alternative, identify a contradiction, find a hidden Ness choice, or block the candidate with complete correction instructions.

### 4.5 Ness remains the only acceptance/adoption authority

Neither local T3, Claude, nor Codex can accept, adopt, integrate, mark package complete, change Master/Map standing, authorize implementation, or move past an explicit Ness acceptance boundary. A Codex PASS establishes audit status only. It never substitutes for Ness's acceptance.

---

## 5. PROVIDER-FREE LOCAL T3 ENVELOPE

### 5.1 T3 state and command remain

The accepted state-machine position remains:

```text
LOOP_TASK_PREPARATION_REQUIRED
  -> prepare-next-design-task
  -> LOOP_INITIAL_DESIGN_REQUIRED
```

The command name remains `prepare-next-design-task`. The worker's branch remains. The change is that the command performs a bounded local derivation and **must make zero provider calls**.

`prepare-next-design-task` is not added to, or retained in, any set whose meaning is “this command may contact a provider.” `codex_next_design_task_preparation` remains recognizable only where needed to replay and recover historical records created under the old design. No new provider kind replaces it.

### 5.2 Existing owners supply the inputs

T3 consumes only values already proved by existing owners:

| Envelope concern | Existing owner reused |
|---|---|
| selected package identity, root, and scope | admitted selection plus the accepted v1.11 transition/package binder (§8.9 binding 3), whose `package_scope_id`, `package_key`, `package_id` and `scope_root_path` are **IA** fields owned by Q's first authenticated package validation under accepted §8.8 §12.1a |
| authority order and required authority sources | existing preflight/authority resolution |
| exact source binding and currentness | **accepted §8.8** — §7 field-by-field ownership, §8 the source/currentness reconstruction algorithm, §10 manifest and required-source-path semantics, §11 validation-set / standing / settled-decision semantics, §12 the transition binding, §15 provider frozen-input semantics. The relevant-source closure is **not** owned by §8.8 and keeps its existing owner |
| question validation | existing Piece-3 validation record and its exact scope/binding |
| fresh independent coverage | existing coverage record and its exact scope/binding |
| settled Ness answers | existing exact-answer and structured-decision binding |
| dependency clearance | existing dependency plan and controller-proved selection/clearance state |
| target candidate path | existing controller candidate grammar, version allocation, containment, and no-overwrite checks |
| allowed/forbidden work and design-only boundary | existing package scope, authority rules, live-loop decision, v1.11 §22, and controller safety text |
| Build-vs-Borrow applicability and evidence | existing Build-vs-Borrow trigger/preparation mechanism |
| later audit binding | existing request `extra_inputs`, prompt-material, required-input, work-item, and provider-request identity machinery |

T3 does not rediscover sources, rebuild authority order independently, invent dependencies, reinterpret Ness's answers, or decide Build-vs-Borrow policy. If an existing owner cannot supply an exact required proof, T3 refuses with the existing truthful blocker/hold semantics.

### 5.3 The canonical envelope — one exact frozen field table

One canonical controller object under the single version tag `NH_LOCAL_T3_TASK_ENVELOPE_V1`, whose top-level key set is exactly these twelve keys, no more and no fewer. Every field binds an **existing** identity, digest, or already-proved value, produced by the §5.2 owner and re-proved at use; a field the controller cannot prove exactly refuses the envelope rather than being defaulted.

| # | Exact key | Type | Owner | Exact existing identity/value bound | Ordering |
|---|---|---|---|---|
| 1 | `envelope_version` | scalar | fixed | the fixed string `NH_LOCAL_T3_TASK_ENVELOPE_V1` | — |
| 2 | `package` | object | **IA** | exactly `package_key`, `package_id`, `package_scope_id`, `scope_root_path`, `package_binding_sha256`. Under accepted §8.8 §7 and §12.1a the first four are **immutable anchor-derived** — Q's **first** authenticated `validation_recorded`, via `package_source_binding.scope_root_path` for the root — and **never move after a Q revalidation**; `package_id` null is a real value | fixed key set |
| 3 | `package_root_identity` | list | selection proof | one `{path, sha256, bytes}` per proved root seed — the existing **byte-identity** proof, never file content. Not a §8.8-owned field | sorted by `path`; duplicate path refuses |
| 4 | `authority_required_files_sha256` | scalar | the existing digest of the controller's own preflight authority resolution — `_authority_binding_digest()` over `resolve_required_files()`, the same `required_files_binding` the `extra_inputs` seam carries (v1.11 §9.5c `EXTRA-INPUTS-SEAM`). Accepted §8.8 §10.4 keeps this deliberately separate from `required_source_paths` and does not touch it | — |
| 5 | `source_currentness` | object | **IA** + **EV** + **LR** | exactly `anchor_source_binding_sha256` (**IA** chain source identity, never moves), `effective_validation_set_id` and `effective_source_manifest_sha256` (**EV**, from `effective_validation(Q)`), `effective_source_binding_sha256`, and `source_state_current` (**LR**, freshly live-reproved). The reconstruction is **accepted §8.8 §8**, and §8.8 governs it **in preference to installed code**, which §8.8 records as not yet implementing it (its P-SB2) | fixed key set |
| 6 | `relevant_source_closure` | object | existing owner | exactly `closure_sha256` and `paths` from the existing `derive_relevant_source_closure()` result. **Accepted §8.8 does not own or move this field**, and no §8.8 coverage is claimed for it | `paths` sorted |
| 7 | `required_source_paths` | list | **EV** | `effective_validation(Q).source_paths_checked` — accepted §8.8 §7 / §10.2 `SBC-MANIFEST-OWNER`; it **moves** with the effective validation. Governing-authority coverage stays separate (field 4, §8.8 §10.4) | sorted; duplicates refuse |
| 8 | `question_clearance` | object | **EV** + **JR** | exactly `unlocked`, `validation_set_id`, `coverage_review_validation_set_id`, `coverage_review_current`, `standing_chain_sha256`. Accepted §8.8 §11.1 makes `validation_set_id` **EV** — `effective_validation(Q).validation_set_id`, the set the Piece-3 gate is actually deciding about — while §11.2 keeps `standing_chain_sha256` / `piece3_standing_sha256` **JR** and **global**, never package-scoped | fixed key set |
| 9 | `settled_decision_binding_sha256` | scalar | **JR** | `settled_decision_binding_digest(derive_settled_decision_binding(state, Q, …))`, carried with the clearance and, per accepted §8.8 §11.3, derived **fresh per scope at every boundary the clearance is re-proved at**. An empty binding is a legitimate value | — |
| 10 | `unsatisfied_dependency_keys` | list | **JR** | the existing `unsatisfied_dependency_keys` of that same clearance; a non-empty list refuses the envelope | sorted |
| 11 | `target` | object | controller-derived | exactly `target_path` and `target_rule_id` — the §5.5 controller-derived path and the fixed string `NH_LOCAL_T3_INITIAL_TARGET_V1` | fixed key set |
| 12 | `work_boundary` | object | controller-proved | exactly `one_file_only`, `design_only`, `build_vs_borrow_required` — three booleans proved from the existing package scope, the existing design-only rules, and the existing Build-vs-Borrow trigger | fixed key set |

**Owner labels are accepted §8.8's, used exactly as it defines them** — **IA** immutable anchor-derived · **EV** current/effective-validation-derived · **JR** current journal/replay-derived · **LR** freshly live-reproved. Two accepted §8.8 rules bind this table and are not restated as new design: `SBC-ONE-OWNER-PER-FIELD` — every field has exactly one canonical owner, and a reader wanting a different epoch of the same fact reads a different field rather than reinterpreting this one; and `SBC-BINDING-FIELDWISE-ONLY` — **this envelope is never described as "derived from the effective validation" wholesale.** Its **IA** fields are anchor-derived and its **EV** fields are effective-validation-derived, always, and the two are never swapped. No field is moved for symmetry.

**"Bytes" means identity, not content.** Package and root bytes mean the existing `{path, sha256, bytes}` hash-and-length proof the installed closure and seed readers already produce. Complete source bytes are never embedded; sources reach Claude by the existing source-supply route, unchanged.

The envelope carries no candidate bytes, no provider custody, no authority registry, no dependency manifest, and no second durable store. The `CANDIDATE`/`STOP` role contract (§6.4) belongs to the controller-owned instruction, not to an envelope field.

### 5.4 Envelope identity and reconstruction

One narrow compatibility binding is required because the initial Claude request previously bound a provider-produced task specification. The replacement binding is:

`local_task_envelope_sha256`

It is exactly `digest_of("NH_LOCAL_T3_TASK_ENVELOPE_V1", envelope)` under the one existing method — `SHA256(canonical_json([DOMAIN_LABEL, EXACT_INPUT_OBJECT]))`, canonical JSON meaning sorted keys, `(",", ":")` separators, `ensure_ascii=True`, over an exact key set that raises on a missing or extra key. That is the method accepted `v1_15` §8.1 reuses and the installed `canonical.canonical_json()` / `sha256_hex()` / `digest_of()` path implements. **No second serialization, no alternate digest path, no new hashing scheme.**

The complete canonical envelope and `local_task_envelope_sha256` enter the initial-design request's bound input material through the existing seam v1.11 §9.5c `EXTRA-INPUTS-SEAM` provides. They are not model-authored result fields. Any envelope input change therefore moves the canonical envelope, `local_task_envelope_sha256`, `required_inputs_sha256` and `prompt_material_sha256`, and with them the future `provider_request_identity` — **but not `work_item_identity`**, which §5.4c states exactly.

Before Claude dispatch, the controller reconstructs the envelope from current authenticated state and current byte proofs and requires exact identity equality. A stored or remembered envelope is never accepted merely because it once passed. That is the same discipline accepted §8.8 §7 states for a request's frozen source facts — owner **TO**, per stage, **reconstructed, never remembered**.

### 5.4a Three objects, never collapsed — and what T4's `extra_inputs` must still carry

This is the one adjacent correction the lineage rebase mechanically forced, and it is reported rather than folded in silently.

Accepted §8.8 §15.2 fixes three separate objects that must never be collapsed, under `SBC-INVENTORY-NOT-EXTRA`:

1. the **base required-input inventory**, identical in shape for every stage — `candidate_sha256` and `candidate_bytes` (**CC**), `source_binding_sha256` (**IA**), `source_manifest_sha256` (**EV**), `settled_decision_binding_sha256` (**JR**), `required_source_paths` (**EV**), plus the `extra` slot;
2. the stage-specific **`extra_inputs`** that rides that `extra` slot;
3. the stage-specific **prompt material**, a **separate** digest over a **different** inventory.

The durable `required_inputs_sha256` is (1) **plus** (2). It is never described as (2) alone and never as (3). v1.3's single-seam phrasing collapsed them, and that phrasing is withdrawn here.

**T4's `extra_inputs`, corrected.** Accepted §8.8 §15.2b fixes T4's keys as `prepared_target_path` · `prepared_specification_sha256` · `frozen_source_binding_sha256`. This amendment changes **exactly one** of them: `prepared_specification_sha256` — the digest of a provider-produced specification that no longer exists — becomes `local_task_envelope_sha256`. **`prepared_target_path` and `frozen_source_binding_sha256` both remain**, and the base inventory's six fields remain untouched. Dropping `frozen_source_binding_sha256` would silently weaken accepted §8.8; it is preserved, and its staleness meaning under §8.8 §15.2d — binding 3's **IA** source identity plus the **EV** trio through the base inventory — is preserved with it.

The prompt-material digest stays separate and keeps its own inventory, and the installed re-derivation of **both** digests — which refuses on either mismatch before one byte leaves the machine — is unchanged. **Its T4 contents are not unchanged, and §5.4b states exactly why and exactly what replaces them:** accepted §8.8 §15.2c records that T4's prompt-material `extra` carries `mechanical_design_specification`, and this amendment removes the object that key names.

### 5.4b T4 prompt material after the provider-produced specification is gone

Accepted §8.8 §15.2c fixes the T4 prompt-material inventory as `template_identity`, `controlled_instruction_ids`, the candidate triple, `blocking_finding_refs`, `target_candidate_path`, the authorized triple, `correction_specification_sha256`, `routed_signal_refs`, `validation_set_id`, `piece3_standing_sha256`, and its own `extra` — which for T4 is `specialized_prompt_kind` plus `prepared_target_path` **and `mechanical_design_specification`**. That last key names the model-authored design content the provider-backed T3 result carried. **This amendment removes that result, so the key names nothing.** Leaving it in place would let a new local-T3 operation depend on an object no stage produces; leaving the envelope out would mean the exact material Claude reads is bound by no digest at all.

**`T4-PROMPT-ENVELOPE`.** For a new local-T3 initial-design request, the T4 prompt-material `extra` is exactly:

| Key | Value |
|---|---|
| `specialized_prompt_kind` | unchanged |
| `prepared_target_path` | unchanged — the §5.5 controller-derived target |
| `local_task_envelope` | **the exact canonical `NH_LOCAL_T3_TASK_ENVELOPE_V1` object of §5.3** |

**One key replaces one key.** `mechanical_design_specification` is removed and `local_task_envelope` takes its place. **Every other field of the prompt-material inventory keeps its existing content and its existing owner**, and no field is added to or removed from the inventory itself.

**`NO-SECOND-ENVELOPE-REPRESENTATION`.** `local_task_envelope` is the **same object** `local_task_envelope_sha256` digests, in the **same** canonical serialization of §5.4 — not a summary, not a re-rendering, not a flattened or prose form, and not a second envelope identity. There is one envelope, one canonical form, and one digest.

**The instruction stays controller-built.** The bytes actually sent remain controller-built and ride the prompt inventory's `extra` slot, inside `prompt_material_sha256`, under accepted v1.11 §9.5b `PROMPT-CONTROLLER-BUILT-AND-BOUND` and `PROMPT-NO-SECOND-BUILDER`. No second prompt builder is created. The change is strictly narrowing: the one operative design-content input that used to be **model-authored** prose is now a **controller-built** object.

#### 5.4b.1 The three objects, and where the envelope sits in each

Accepted §8.8's separation is preserved absolutely; the envelope appears in exactly one of the three as content, and in exactly one as a digest:

| Accepted §8.8 object | Envelope's presence | Unchanged parts |
|---|---|---|
| **A** — base required-input inventory | **none.** No envelope content and no envelope digest is added here | its six fields keep their §8.8 owners exactly |
| **B** — T4 `extra_inputs` | the **digest only**: `local_task_envelope_sha256` | still exactly three keys — `prepared_target_path` · `local_task_envelope_sha256` · `frozen_source_binding_sha256` (§5.4a). **No fourth key is added**, and the complete envelope is never placed here |
| **C** — T4 prompt material | the **exact canonical content**: `extra.local_task_envelope` | every other prompt-inventory field unchanged |

`required_inputs_sha256` remains **A plus B** and is never described as B alone or as C. `prompt_material_sha256` remains a separate digest over C. The two are never collapsed, and neither is derived from the other.

#### 5.4b.2 `ENVELOPE-DIGEST-AGREEMENT` — one object proved across both inventories

Before dispatch, and again on every restart and re-entry, the controller:

1. **rebuilds** the canonical envelope from current authenticated state and current byte proofs, exactly as §5.4 already requires — never from a remembered copy, and never from the prompt bytes it is checking;
2. **re-derives** `digest_of("NH_LOCAL_T3_TASK_ENVELOPE_V1", envelope)` from that rebuilt object;
3. **requires** that digest to equal the `local_task_envelope_sha256` carried in **B**;
4. **requires** the rebuilt object to equal, exactly, the `local_task_envelope` carried in **C**;
5. **recomputes** `required_inputs_sha256` over A **plus** B and requires equality with the prepared record's value;
6. **recomputes** `prompt_material_sha256` over C and requires equality with the prepared record's value.

Steps 5 and 6 are the accepted v1.11 §9.5c `EXTRA-INPUTS-RECONSTRUCTION` proofs and the installed dual-digest refusal accepted §8.8 §15.2c names; steps 2–4 are the one new cross-proof this correction adds, and they add **no new digest, no new inventory field, and no new identity** — only an equality between two values that already exist.

#### 5.4b.3 Refusal before Claude is contacted

Any divergence refuses. Nothing is repaired, re-rendered, normalized, or "fixed up", and no partial dispatch occurs:

| Divergence found at reconstruction | Result |
|---|---|
| rebuilt envelope ≠ the `local_task_envelope` carried in **C** | **refuse; zero provider contacts** |
| `digest_of(rebuilt envelope)` ≠ `local_task_envelope_sha256` in **B** | **refuse; zero provider contacts** |
| recomputed `required_inputs_sha256` ≠ the prepared record's | **refuse** — accepted v1.11 §23 R-7b |
| recomputed `prompt_material_sha256` ≠ the prepared record's | **refuse** — accepted v1.11 §23 R-7b |

A refusal never rewrites the prepared record. Under accepted v1.11 `EXTRA-INPUTS-STALE-NOT-SILENT`, an earlier attempt's saved result is **stale rather than reused**, and the position is re-entered under the ordinary bounded request-identity and provider-lifecycle rules. Because any envelope input change changes the rebuilt object, it changes `local_task_envelope_sha256`, `required_inputs_sha256` **and** `prompt_material_sha256` together — a stale envelope can therefore never reach Claude through any one of the three.

#### 5.4b.4 Historical records keep their own semantics

**`NO-NEW-PATH-ON-OLD-SPECIFICATION`.** No new local-T3 operation reads, requires, defaults, or fabricates `mechanical_design_specification` or `prepared_specification_sha256`. They are absent from the new path, not empty in it.

Historical provider-backed T3/T4 records keep both keys and **reconstruct under their original semantics**, exactly as §8.1 already requires. They are never rewritten, converted into envelopes, or re-digested under the new form, and the historical schema rows needed to authenticate and explain them remain.

### 5.4c `ENVELOPE-IDENTITY-BOUNDARY` — which identity an envelope change moves, and which it does not

Accepted §8.8 P-SB12 fixes the blast radius exactly. `identity.WORK_ITEM_KEYS` carries `source_binding_sha256`, `validation_set_id`, `piece3_standing_sha256`, `routed_signal_refs`, the candidate triple and the other already-governed work-item fields — and **not** `source_manifest_sha256`, **not** `required_source_paths`, and **not** the stage-specific `extra`. Re-owning those source facts therefore changes `required_inputs_sha256`, hence the future `provider_request_identity`, **and nothing else**. §15.4 `SBC-FREEZE-BY-COMMITMENT-NOT-RECOVERY` states the same of the live source freeze that rides the `extra` slot: **`work_item_identity` is unaffected by it**, so the work item, its retry series and its bounded output-retry budget do not move when the repository moves. §28.2 item 2 records why that was chosen: had such input movement moved work-item identity, an unrelated file change could have reset a bounded output-retry budget — "a real weakening, named and avoided."

`local_task_envelope_sha256` lives in exactly that `extra` slot (§5.4a **B**); the canonical envelope lives in the prompt material (§5.4b **C**). **Neither is a work-item field.**

**`ENVELOPE-IDENTITY-BOUNDARY`.**

1. A material change to the canonical local T3 envelope changes the **canonical envelope object** and, with it, **`local_task_envelope_sha256`**.
2. Because `local_task_envelope_sha256` is in T4 `extra_inputs`, that change changes **`required_inputs_sha256`**.
3. Because the exact envelope content is in T4 prompt material, that change also changes **`prompt_material_sha256`**.
4. Both are already inputs of `provider_request_identity`, so the change produces the appropriate new/future **`provider_request_identity`** under the existing provider-request identity rules. **No new identity layer and no second request identity is created.**
5. **An envelope change does not, by itself, change `work_item_identity`.**
6. `work_item_identity` remains governed **exclusively** by the existing accepted work-item object and `WORK_ITEM_KEYS`, with their existing field ownership. This amendment adds nothing to either.

| Change | envelope object | `local_task_envelope_sha256` | `required_inputs_sha256` | `prompt_material_sha256` | `provider_request_identity` | `work_item_identity` |
|---|---|---|---|---|---|---|
| an **EV** source fact moves — e.g. `required_source_paths` or `source_manifest_sha256` — with every work-item-owned field unchanged | changes | changes | changes | changes | new/future one | **unchanged** |
| the controlled T4 target moves, where the existing `WIM-INITIAL` rules permit that comparison | changes | changes | changes | changes | new/future one | **changes — for the existing `target_candidate_path` rule** |

The second row is not a counter-example and not a new dependency. `target_candidate_path` is an existing work-item-owned field of `WIM-INITIAL`; when it moves, work-item identity moves **for that existing work-item rule**, exactly as it did before this amendment. It does not move because an envelope digest was injected into work-item identity — nothing of the sort happens. The two identities simply each own that one fact independently.

**`NO-ENVELOPE-IN-WORK-ITEM-IDENTITY`.** `local_task_envelope_sha256` **must remain** in T4 `extra_inputs` and **must not** be added to the initial-design work-item object, to `WORK_ITEM_KEYS`, to `WORK_ITEM_MATRIX`, or to any parallel work-item identity mechanism. The complete `local_task_envelope` stays only on the prompt-material side, exactly as §5.4b specifies. Neither side gains a new identity layer.

**Retry ownership is stable across envelope-only movement.** Because work-item identity does not move, the initial-design work item's retry series and its bounded output-retry budget do not move either when source or currentness facts move underneath it. **Envelope-only movement can therefore never reset, restart, or manufacture a fresh bounded output-retry ownership series** — precisely the weakening accepted §8.8 §28.2 item 2 names and avoids. What such movement does do is exactly what it should: the reconstruction of §5.4b.2 refuses the stale request under §5.4b.3, with zero provider contacts, and the earlier attempt's saved result is stale rather than reused.

### 5.5 Target path remains controller-owned — and how the first one is derived

Claude receives one exact target path and cannot choose or modify it.

**What exists, named exactly.** `parse_controlled_candidate_basename()` — the one place the grammar `<name>_v<major>_<minor>_CANDIDATE.md` lives; `is_new_candidate_path()` — lexical safe-path refusal, containment under `CANDIDATE_DIR` = `05_ACTIVE_CANDIDATE/`, no-symlink-component proof, real-root containment, target non-existence; `next_candidate_version_path()` with `is_exact_candidate_successor()` — the deterministic **successor** allocator. Accepted v1.11 §13.5 `PREP-TARGET-CONTROLLED` states the same discipline.

**What does not exist.** None derives a *first* target. `is_new_candidate_path()` only validates a path handed to it, and under accepted v1.11 that path came from the provider-backed T3 result's `target_path` (v1.11 §13.4); `next_candidate_version_path()` increments an existing candidate and cannot mint one. **With provider-backed T3 removed, no existing mechanism proposes the first candidate path**, so this amendment supplies exactly one — with no second naming or version subsystem.

**`NH_LOCAL_T3_INITIAL_TARGET_V1`**, reached only when the selected scope has no candidate at all:

1. take the exact basename of the controller-proved selected package root;
2. remove the exact terminal `.md`; then the exact terminal `_CANDIDATE` if present; then at most one terminal version component matching `_v[0-9]+(?:_[0-9]+)*$`;
3. require a non-empty remaining stem and keep it byte-for-byte;
4. append the fixed controller-owned non-semantic component `_NH_LIVE_LOOP_DESIGN`, then `_v1_0_CANDIDATE.md`, under `CANDIDATE_DIR`;
5. require the result to satisfy the existing `parse_controlled_candidate_basename()` grammar and the existing `is_new_candidate_path()` checks — re-proved at the final safe boundary before dispatch and again at exclusive creation;
6. if steps 1–5 do not yield exactly one safe path, T3 stops with a mechanical target-derivation contradiction.

Every check in step 5 is an existing one, and a root already named `<stem>_v1_0_CANDIDATE.md` derives `<stem>_NH_LIVE_LOOP_DESIGN_v1_0_CANDIDATE.md` rather than its own occupied path.

**Successor versioning is not redesigned.** Correction successors remain governed by the existing `next_candidate_version_path()` / `is_exact_candidate_successor()` mechanism exactly as it stands; this rule never runs for a correction, never renames, never increments. Claude is never asked to invent or adjust a filename, and an appeared target causes refusal, never renaming and never an overwrite.

### 5.6 T3 outcomes

Local T3 has only two outcomes:

1. **READY** — the canonical envelope is complete, current, unambiguous, and digest-bound; the loop may enter initial Claude design.
2. **NOT READY** — an existing proof is missing, stale, ambiguous, contradictory, or blocked; the loop reports the exact existing condition and launches no provider.

T3 does not create a model-authored `review_signal`. Any genuine question already discovered before T3 remains owned by the existing question path. If the local facts show clearance is not valid, T3 returns to or waits on the existing owner; it does not phrase a new question itself.

### 5.7 No durable T3 provider episode

New local T3 work creates no `provider_request_prepared`, `provider_dispatch_begun`, result custody, terminal, provider retry, provider reconciliation, or provider availability episode. It does not need a new work-item kind or provider-kind lifecycle row.

The envelope's reconstructable identity is carried forward in the existing initial Claude request. Normal authenticated operation records may record that the local phase completed under the existing controller-operation mechanism, but this amendment introduces no new journal event type and no separate envelope store.

---

## 6. CLAUDE DESIGN AND STOP BEHAVIOR

### 6.1 Claude candidate outcome

For `CANDIDATE`, Claude must:

- read the relevant sources supplied under the existing source/currentness rules;
- obey the exact package, authority, source, decision, dependency, target, and work-boundary bindings;
- independently design the best mechanical solution that satisfies all settled constraints;
- make no consequential Ness-facing choice;
- create only the one permitted versioned candidate inside the existing disposable workspace;
- leave every other file byte-identical;
- follow the existing Build-vs-Borrow requirement when its trigger applies;
- produce the existing bound plain-language acceptance explanation in the same call;
- return the existing candidate payload/path/hash/byte proofs and explanation material required by current admission.

The existing candidate-size, exact-path, payload decoding, byte count, digest, frozen-baseline rescan, exclusive creation, custody-before-promotion, and request-binding checks remain mandatory. **This arm preserves the existing/current candidate result contract and its same-call explanation behavior exactly as they stand**; the only change is that the old provider-produced-specification binding becomes the §5.4 envelope binding.

Under Ness's later decision (§2.4a), that same call produces the **bound semantically variable explanation material** required before the fresh audit is dispatched — the content stage accepted `v1_15` §7.1 already fixes, at §14 Phase A step A2. Everything `v1_15` settles is untouched: **part 7 remains controller-derived, part 8 remains controller-owned fixed material, the final assembly authors nothing and admits no provider, subprocess, or network wait, and the acceptance action itself invokes no model.** The same rule governs a correction call's explanation material; §7.4 governs the correction itself.

### 6.2 What Claude may decide

Claude may decide ordinary mechanics only when alternatives do not change unsettled Ness meaning or policy. Examples include internal state-machine arrangement, deterministic validation order, record-field plumbing, idempotency mechanics, ordinary path normalization, bounded retry encoding already required by policy, and test structure.

Claude's choice remains a candidate, not truth or authority. Codex may block it; Ness may reject it; later evidence may require correction.

### 6.3 What Claude may not decide

Claude must not:

- decide what Ness wants;
- choose policy, meaning, priorities, permissions, privacy boundaries, acceptance, or adoption;
- reopen a settled Ness decision;
- treat an unasked open question as permission;
- widen package scope or dependency order;
- alter authority or Map standing;
- select its own source set, package root, scope identity, or target filename;
- create extra files;
- touch the real checkout or production stores;
- implement, build, migrate, deploy, integrate, commit, or push;
- mark its output accepted, complete, authoritative, or installed.

### 6.4 Two locally validated, mutually exclusive result arms

Accepted v1.11 `INIT-ADMISSION` I1/I2 admit exactly one initial-design result shape — the candidate-producing key set of §14.5a. **A STOP cannot satisfy it**: it produces no path, payload, byte count or digest. v1.1 kept I1/I2 while also permitting a stop, which is a contradiction. The smallest correction is one second, disjoint shape held to the same exactness.

**`CANDIDATE` arm.** The existing/current candidate contract and same-call explanation behavior, unchanged (§6.1); I1/I2 apply to it as today, and I3–I7 and I10 in full.

**`STOP` arm — `NH_LOCAL_INITIAL_DESIGN_STOP_RESULT_V1`, version `1`** — exactly three keys, no more and no fewer:

| # | Key | Requirement |
|---|---|---|
| 1 | `result_schema_id` | exactly `NH_LOCAL_INITIAL_DESIGN_STOP_RESULT_V1` |
| 2 | `result_schema_version` | exactly `1` |
| 3 | `stop_review_signal` | exactly the existing five-key review-signal object — `issue_key`, `finding_key`, `signal_title`, `finding_evidence`, `source_evidence` — validated by the existing `validate_review_signal()` against the envelope's proved `required_source_paths`, and by nothing else |

That one field is existing review-signal material and carries exactly what a STOP must prove:

- **the exact blocking issue** — `issue_key`, `finding_key`, `signal_title`, under the existing bounded-key rules and the existing refusal of a label spelled like one of the controller's own identities;
- **the exact source/evidence binding** — `finding_evidence`, a non-empty bounded array, and `source_evidence`, existing proved-read source paths;
- **no candidate result** — the schema contains no candidate path, payload, byte count, digest, or explanation key at all;
- **package/scope binding** — proved by the controller, never the model, exactly as I8/I9 already require through the request's `required_inputs_sha256` and `prompt_material_sha256` over the §5.3 envelope, and as `record_review_signal()` already requires by deriving scope from the controller's proved binding and `scope_root_path`.

The arms are mutually exclusive at the earliest local validation boundary: the schema ids differ and the key sets are disjoint apart from `result_schema_id` and `result_schema_version`. **A mixed result remains invalid** — any candidate key beside a stop signal, or any stop signal beside a candidate key — and follows the existing bounded invalid-output route with exact validation feedback; a result matching neither schema fails the same way and creates nothing.

This creates **no new provider kind, no new provider lifecycle, no new result store, no second interview system, and no new journal event type.**

### 6.5 STOP custody, durable closure, and the existing question route

A Claude `STOP` never goes directly to Ness and is never treated as proof that a Ness question exists.

**Durable closure.** Accepted v1.11 §7.6a `CLOSURE-INITIAL-PENDING` keeps an `initial_design` custody pending until its downstream effect is proved, naming `candidate_custody_recorded` as that effect. A STOP produces no candidate, so it needs its own — and the existing carrier is already the right one. The admitted STOP result is custodied by the existing provider lifecycle, exactly as any initial-design result is. **`STOP-CLOSURE-EXACT`** then defines exactly when one `review_signal_recorded` closes one custodied STOP:

1. **Reconstruct, never remember.** From the exact saved STOP bytes plus the controller-proved package/scope/source binding, rebuild the complete expected review-signal material: the controller-derived `package_scope_id`, the controller-proved `scope_root_path` and candidate binding, the signal source, the existing route value, and the five saved signal fields `issue_key`, `finding_key`, `signal_title`, `finding_evidence`, `source_evidence`. That is the existing probe object the existing carrier already builds; no new material is invented.
2. **Derive the identity.** From exactly that material derive the expected existing `routed_signal_id`, through the existing `interview_routed_signal_id()` over the existing `routed_concern_fingerprint()` of the same material. A closing record must carry exactly that identity.
3. **Require full material equality.** Identity agreement alone does not close. Every reconstructed field of step 1 must equal the candidate record's field, field for field. **Matching issue key, finding key and scope is not sufficient.**
4. **Require correct order.** The closing `review_signal_recorded` must stand **after** the exact owning STOP custody event in the authenticated journal. **An identical signal that exists only before that custody event does not close this STOP** — it is a different, earlier act, and counting it would fabricate a completion this STOP never received.
5. **Exactly one closes.** Exactly one matching post-custody record closes the custody. Two or more post-custody records carrying that identity, or carrying the same reconstructed material, are contradictory and **fail closed**: the controller refuses rather than choosing between them, and appends nothing.
6. **Otherwise append exactly once.** If no matching post-custody record exists, the existing local saved-result processing consumes **those exact saved bytes** — never a re-asked model, never a re-derived signal — and appends exactly one record through the existing `record_review_signal()` path, then performs a **mandatory readback**: re-read and re-authenticate the appended event and re-prove steps 2–4 against it. An append that cannot be read back and re-proved is not a closure and is never counted as one.
7. **That record is the closure.** The re-proved `review_signal_recorded` is the durable downstream completion of that STOP custody, as `candidate_custody_recorded` is for a `CANDIDATE` custody.

The carrier already covers this case: its installed purpose names the review of a Claude specification stop, and a `claude_specification_stop_review` signal source already exists. **No event type, provider call, store, journal, marker, or second question route is added**, no STOP-review provider is launched, and every STOP-processing position makes **zero** provider calls. The adaptation is local and deterministic under the existing signal identity, evidence, source, and scope rules.

**On restart.** Saved STOP custody is reused and re-verified. If step 6's readback already succeeded, steps 2–4 find that exact record, the append count is **zero**, and **Claude is never rerun**. If the process died after custody and before any append, exactly one append occurs and is read back. Custody whose saved bytes cannot be re-verified keeps the existing behavior unchanged — the v1.11 §14.6 `CUSTODY-UNVERIFIABLE-HOLD` safety hold, zero new model calls, everything durable preserved: losing saved bytes is never permission to ask Claude again.

From there the existing route governs unchanged:

```text
review_signal_recorded
  -> question validation
  -> fresh independent question coverage
  -> durable Ness-question-ready boundary, if the question survives
  -> ask Ness
```

If validation finds the issue settled, mechanical, unsupported, duplicated, or outside scope, it does not reach Ness. If coverage finds another genuine gap, the existing targeted question path owns it. No new “Claude stop review” provider lifecycle or second interview system exists.

### 6.6 Recovery around Claude

If interruption occurs before the initial Claude request is durably prepared/dispatched, local T3 is recomputed and re-proved from current state. No provider outcome exists to reconcile.

Once the initial Claude request is durably prepared or may have been dispatched, the existing provider lifecycle owns every position. The envelope is reconstructed as bound input; the existing prepared/dispatched/custodied/terminal/reconcile/no-redispatch rules apply unchanged. This amendment creates no shortcut from an uncertain Claude outcome back to local T3.

---

## 7. FRESH INDEPENDENT CODEX AUDIT

### 7.1 Audit remains a separate fresh provider invocation

After a candidate and its same-call explanation are durably admitted and promoted through existing custody, the modern supervisor opens the existing fresh independent Codex design audit. This call remains separate from Claude because independence is a real safety property.

The audit is not merged into Claude's call and is not replaced by local checks.

### 7.2 What Codex must reconstruct

Codex receives the existing bound audit material, extended only as necessary to include/reconstruct the local T3 envelope identity. It independently checks the candidate against:

- governing authority and exact current source binding;
- the selected package/root/scope;
- validated and fresh-coverage question clearance;
- Ness's settled decisions and answers;
- dependency clearance;
- the exact local task-envelope identity and content;
- candidate bytes and target identity;
- the exact fixed bytes of the bound plain-language acceptance explanation, judged together with the exact candidate;
- Build-vs-Borrow evidence and claims where triggered;
- all applicable privacy, security, provenance, recovery, idempotency, no-duplicate, design-only, versioning, and no-overwrite requirements.

Codex must not treat the local envelope as an architectural specification to rubber-stamp. The envelope is the boundary. Codex reconstructs the actual requirements from sources and judges whether Claude's chosen mechanics satisfy them.

### 7.3 Required audit questions

The existing audit contract remains a real challenge. Codex checks scope, settled decisions, hidden choices, source completeness/currentness, end-to-end mechanics, authority/provenance/privacy/security/recovery/idempotency/no-duplicate rules, target/version/no-overwrite, Build-vs-Borrow where triggered, explanation accuracy, and fitness for the bounded design job.

### 7.4 Blocking audit result and correction

If Codex finds mechanical blockers, the **same audit result** carries the complete bounded mechanical correction instructions, with their finding identities and source/evidence bindings. **No separate Codex correction-specification call is opened.** That is Ness's later decision (§2.4a), and it supersedes Detailed Interview Decision v1.1 §15A only as to that separate provider call (§3.1).

The existing correction path remains:

```text
blocking fresh Codex audit with complete correction instructions
  -> one bounded Claude correction in a new versioned candidate
  -> fresh independent Codex re-audit
```

Every current correction lifetime cap, batch/round authorization, prior-candidate byte proof, target derivation, one-file disposable workspace, custody, exact-byte, and recovery rule remains, together with §15A's finding identities, evidence binding, ban on Claude substituting a different design solution, and mandatory fresh independent re-audit. A correction instruction cannot decide a Ness question. A discovered genuine question routes through the existing question path.

### 7.5 PASS remains non-acceptance

A Codex PASS proves only that the audited candidate passed the current independent design audit. It does not accept, adopt, integrate, implement, close, or install anything. The explicit Ness acceptance boundary remains exactly where the existing live loop places it.

---

## 8. HISTORICAL AND RECOVERY COMPATIBILITY

### 8.1 Historical provider-backed T3 records remain history

Existing records for `next_design_task_preparation` / `codex_next_design_task_preparation`, including prepared requests, dispatch records, custody, terminals, retries, operation completions, and any admitted prepared-task results, remain authentic historical evidence. They are never rewritten, deleted, normalized, re-headed, or converted into local envelopes.

Replay continues to recognize their original kind and original semantics. This amendment does not remove the historical schema rows needed to authenticate and explain them.

### 8.2 Installation boundary for old T3 episodes

A later installation of this accepted amendment may occur only at a durable safe boundary:

- no provider/controller operation is in flight;
- no open T3 provider request or unprocessed T3 result exists;
- the current journal and custody re-prove;
- the old worker retires under existing controller-identity/lease safety when the controller identity changes;
- exactly one fresh worker may resume after clean release.

If an old provider-backed T3 episode is still open, it must be resolved under the old accepted/current lifecycle before installation. It is not abandoned or reinterpreted merely to enable the new behavior.

### 8.3 Recovery before and after Claude dispatch

The only new recovery distinction is simple:

| Position | Owner |
|---|---|
| no initial Claude request exists | recompute/reprove local T3; no provider reconciliation exists |
| initial Claude request prepared but not dispatched | existing provider prepared-request rules |
| dispatch may have happened | existing reconcile-first/no-redispatch rule |
| `CANDIDATE` result custodied | existing saved-result processing; closure through the existing candidate custody; no provider rerun |
| `STOP` result custodied | existing saved-result processing over the same saved bytes; the existing `review_signal_recorded` appended once if still owed; no provider rerun (§6.5) |
| candidate custody or later audit/correction state exists | existing modern-supervisor path |

There is no separate envelope recovery state. Envelope reconstruction is an input proof to the existing initial Claude request and its recovery.

### 8.4 Idempotency and currentness

Repeated local T3 evaluation against identical authenticated inputs returns the identical canonical envelope and digest and opens no provider request. If any bound input changes, the old envelope cannot authorize Claude; the controller rebuilds from the newly proved state and derives a different envelope digest, and with it a different future provider-request identity (§5.4c).

If source/currentness, clearance, settled answers, dependency state, or target availability moves after T3 but before Claude dispatch, the request reconstruction fails or produces a different **provider-request** identity under existing rules, while `work_item_identity` stays exactly where its own governed fields put it (§5.4c). No stale envelope is silently used, and no envelope-only movement disturbs work-item-owned retry or episode ownership.

### 8.5 The continuation lineage, stated correctly

v1.9 and v1.10 are **historical intermediate versions** of the continuation lineage, preserved byte-identically with their own actual historical standings (§2.1). They are neither incorporated nor superseded as authority here, and they are not described as the current layer in either direction.

**v1.11 is the currently accepted continuation design** (§2.2), and it is the layer §3.2 supersedes against. v1.8's earlier acceptance stands as the historical fact it is, proved by its own receipt.

The corrections v1.9, v1.10 and v1.11 introduced are **not undone** by this amendment. `T1-ACTIONABLE-ROOT` (accepted v1.11 §9.3a) in particular is now part of the accepted layer rather than a separately pending item, and it coexists with this role split because package selection is outside this amendment's scope. The same is true of the B9 budget work, the T4 derived exhaustion field and its §7.4 guard, and `LOOP_NEEDS_USER_ACTION`.

---

## 9. SAFETY AND INVARIANTS PRESERVED

### 9.1 Completely unchanged mechanisms

This candidate does not redesign package selection; question discovery/validation/fresh coverage; the genuine-question standard; source-currentness or relevant-source closure — source currentness is owned by the separately accepted §8.8 package (§2.5), which this candidate binds to and never extends; Ness-answer preservation; transition binding outside T3; provider launch/custody/terminal/validation/retry/reconciliation/no-duplicate rules; lease/worker/supervisor/identity-retirement/maintenance pause; saved-result idempotency; candidate intent/custody/promotion/no-overwrite; Build-vs-Borrow; the same-call candidate-plus-explanation behavior; audit-embedded correction instructions, correction and re-audit; Ness-only acceptance; post-acceptance continuation; authority/Map integration; design/build boundaries; or dashboard projection.

### 9.2 Fail-closed conditions

Local T3 launches no provider and produces no usable envelope unless it exactly proves one package/root/scope, current authority/source closure, completed validation and fresh coverage, open clearance, current settled decisions, dependencies, one safe controller-derived target, the work boundary, and Build-vs-Borrow disposition.

Claude dispatch also refuses if reconstruction of any envelope input or digest differs. The response to an unknown is not “let Claude decide.” It is the existing exact blocker, waiting, recovery, or Ness-question route.

### 9.3 No authority transfer

Moving bounded mechanical design from pre-Claude Codex to Claude does not transfer authority. Mechanical design remains a proposed solution constrained by controller proofs and challenged by fresh Codex. Ness remains the only person who can settle meaning and accept/adopt.

The independent audit is strengthened in one respect: Codex now reconstructs and challenges Claude's solution rather than judging fidelity to its own earlier solution. This does not make Codex the acceptance authority.

### 9.4 No safety-by-prompt alone

The envelope does reach Claude as prompt material (§5.4b) — but it is not **merely** that. The same canonical object is digest-bound on both sides — `local_task_envelope_sha256` inside `required_inputs_sha256`, the exact canonical content inside `prompt_material_sha256` — cross-proved between them, and re-derived from authenticated state before dispatch and on every restart, so prompt bytes that are not the ones the request durably bound cannot be sent. Those are the two durable request inputs; `work_item_identity` is a separate, separately governed input and is not one of them (§5.4c). Controller-owned path, source, scope, currentness, custody, one-file, no-overwrite, and design-only rules remain enforced outside the model.

The move is a strengthening, not a relaxation: the operative design content Claude reads used to be **model-authored** prose validated after the fact, and is now a **controller-built** object proved before dispatch.

Model instructions supplement those deterministic controls; they do not replace them.

---

## 10. FOCUSED INSTALLATION TESTS

This candidate authorizes no implementation. If Ness later accepts it and separately authorizes installation, the smallest changed boundaries must pass the following focused proof without a new shadow loop or manufactured live provider campaign.

### 10.1 Local T3 tests

1. Cleared state produces one deterministic READY envelope, advances to initial design, and creates zero provider lifecycle records/calls.
2. Identical proved inputs reproduce the exact envelope/digest; any bound input change changes or refuses it.
3. Missing/ambiguous package, source, clearance, decision, dependency, target, boundary, or Build-vs-Borrow proof fails before provider preparation.
4. Existing grammar/containment/no-overwrite helpers own the path; the §5.5 rule derives exactly one safe first target or stops; caller/model targets and existing targets refuse; successor versioning still uses the existing allocator.
4a. The §5.3 envelope carries exactly its twelve keys, each bound to its named existing identity; an extra, missing, or unprovable field refuses.
4b. Every envelope field matches its accepted §8.8 owner: after a Q revalidation the **IA** fields do not move, the **EV** fields do, `standing_chain_sha256` stays global, and no field is derived from the effective validation wholesale.
4c. The initial-design request keeps accepted §8.8's three objects distinct, and its `extra_inputs` carries exactly `prepared_target_path`, `local_task_envelope_sha256` and `frozen_source_binding_sha256` — dropping the frozen source binding fails, and adding the complete envelope as a fourth key fails.
4d. The exact canonical envelope Claude receives is carried in the T4 prompt material and is covered by `prompt_material_sha256`; the T4 prompt `extra` is exactly `specialized_prompt_kind`, `prepared_target_path` and `local_task_envelope`.
4e. Changing envelope content without the matching envelope digest refuses before dispatch, with zero provider contacts.
4f. Changing `local_task_envelope_sha256` without matching canonical content refuses before dispatch, with zero provider contacts.
4g. Changing the prompt-bound envelope material without a matching `prompt_material_sha256` refuses before dispatch, with zero provider contacts.
4h. `required_inputs_sha256` and `prompt_material_sha256` remain distinct, are each independently reconstructed, and neither is derived from the other; a mismatch in either alone refuses.
4i. One changed envelope input moves the rebuilt object, `local_task_envelope_sha256`, `required_inputs_sha256` and `prompt_material_sha256` together, and the earlier attempt's saved result is stale rather than reused.
4j. No new local-T3 operation reads, requires, defaults to, or fabricates `mechanical_design_specification` or `prepared_specification_sha256`; a build in which the new path can consume either fails.
4k. An envelope-only **EV**/source change — changed `required_source_paths` or `source_manifest_sha256` with every initial-design work-item-owned field unchanged — changes the canonical envelope, `local_task_envelope_sha256`, `required_inputs_sha256`, `prompt_material_sha256` and the future `provider_request_identity`, and leaves `work_item_identity` **unchanged**.
4l. A genuine work-item-owned field change — a different controlled target, where the existing `WIM-INITIAL` rules permit that comparison — changes work-item identity **for the existing `target_candidate_path` rule**, not through any new envelope-digest dependency.
4m. `local_task_envelope_sha256` appears in no work-item structure: not in `WORK_ITEM_KEYS`, not in the initial-design work-item object, not in `WORK_ITEM_MATRIX`, and not in any parallel identity layer; the complete `local_task_envelope` appears only in prompt material.
4n. Envelope-only movement cannot reset or manufacture a fresh bounded output-retry ownership series: across such movement the initial-design work item's identity, retry series and bounded output-retry budget are all unchanged.
5. Existing binders/checkers are reused; no parallel source, authority, dependency, custody, replay, recovery, or allocator appears.

### 10.2 Claude, audit, and correction tests

6. `CANDIDATE` binds exact envelope/target, changes one disposable file, and includes the same-call explanation.
7. `STOP` carries exactly its three keys, has no candidate/explanation bytes, and is custodied; mixed and neither-schema forms fail with exact retry errors and create nothing.
7a. A prior identical signal that exists **only before** the STOP custody event does **not** close it.
7b. An exact post-custody record — expected `routed_signal_id` **and** full reconstructed material — closes it.
7c. A crash after custody and before any signal appends exactly one record and reads it back.
7d. A restart after a successful readback appends **zero** and reruns Claude **zero**.
7e. A duplicate or conflicting post-custody record of the same identity or the same material fails closed and appends nothing.
7f. Every STOP-processing case makes **zero** provider calls; saved bytes that cannot be re-verified hold under the existing safety hold with nothing appended.
8. Any envelope/package/source/decision/target mismatch preserves and refuses the result, creating no candidate.
9. Fresh Codex receives/reconstructs sources, envelope, candidate, explanation, and Build-vs-Borrow evidence without an earlier Codex solution.
10. A blocking audit carries complete correction instructions and schedules no separate specification call; correction plus fresh re-audit retains current caps, custody, evidence binding and explanation rules.
11. A hidden Ness choice enters the existing validation → fresh coverage → Ness path, never mechanical correction.

### 10.3 Historical, recovery, and compatibility tests

12. Historical provider-backed T3/T4 records replay with original meaning — including their own `mechanical_design_specification` and `prepared_specification_sha256` reconstruction — and are never converted, re-digested under the new envelope form, or rewritten.
13. Pre-Claude interruption recomputes local T3; post-dispatch interruption remains under existing provider recovery/no-redispatch.
14. Valid saved Claude results process without rerun and still must match the reconstructed envelope.
15. Controller identity, lease retirement, one-worker ownership, maintenance pause, and in-flight drain remain passing.
16. Separate question validation/coverage, Ness acceptance, accepted state, dependency-safe continuation, and the accepted v1.11 corrections — `T1-ACTIONABLE-ROOT` (§9.3a), the T4 derived exhaustion field and its §7.4 guard, and `LOOP_NEEDS_USER_ACTION` — all remain compatible and unregressed.

### 10.5 Directly relevant regression set

The existing provider lifecycle, no-duplicate, candidate custody, candidate path, Build-vs-Borrow, same-call explanation, audit-embedded correction, correction/re-audit, question validation/coverage, worker/lease, acceptance, and post-acceptance continuation tests must remain passing. Broad unrelated package or production tests are not required merely because this narrow role amendment is installed.

---

## 11. PROVIDER-CALL CONSEQUENCE

### 11.1 One normal call is removed

Under the current accepted clean-package structure, the normal path contains six serial provider calls when each stage is needed:

1. Codex next-package selection;
2. Codex question validation;
3. fresh Codex question coverage;
4. Codex T3 mechanical task specification;
5. Claude initial design with same-call acceptance explanation;
6. fresh independent Codex design audit, carrying complete correction instructions when it blocks.

After this amendment is accepted and installed, the normal path contains five:

1. Codex next-package selection;
2. Codex question validation;
3. fresh Codex question coverage;
4. Claude initial design with same-call acceptance explanation;
5. fresh independent Codex design audit, carrying complete correction instructions when it blocks.

The removed call is exactly the provider-backed T3 specification call. T3 itself remains and becomes local.

This candidate does not localize package selection and does not merge separate question validation with fresh coverage. Those are different policy questions and remain outside scope.

### 11.2 From a package already selected and question-cleared

From the durable boundary where the package is already selected and its question validation plus fresh coverage are complete, the clean design path becomes:

```text
local T3 (zero provider calls)
  -> one Claude design/explanation call
  -> one fresh Codex audit call
  -> Ness acceptance boundary
```

That boundary therefore requires two normal provider calls rather than three.

### 11.3 Real correction or newly discovered question

A real mechanical correction adds:

- one Claude correction call;
- one fresh Codex re-audit call.

No separate correction-specification call is added: under Ness's later decision (§2.4a) the blocking audit already carries the complete instructions (§7.4).

A real newly discovered Ness question adds only the provider work required by the existing question-validation and fresh-coverage path. The local T3 does not hide or shortcut it.

### 11.4 What is not promised

No fixed duration is promised. Package complexity, real questions/gaps, provider availability, corrections, and external research still add time. The proved consequence is one fewer serial provider call wherever provider-backed T3 formerly ran; the replacement is controller-scale local work. Quality and safety are not reduced.

---

## 12. ACCEPTANCE AND INSTALLATION BOUNDARY

### 12.1 Current standing

This v1.6 file is only a candidate. It does not supersede any current rule until Ness explicitly accepts the exact candidate identity. A future acceptance must identify the exact bytes/digest being accepted and must preserve this file without in-place rewriting.

### 12.2 What Ness acceptance would mean

If Ness accepts the exact candidate, only this narrow standalone role split and its named supersessions are accepted. All unmentioned rules remain, including every v1.11 rule not named in §3.2; v1.0, v1.1, v1.2, v1.3, v1.4 and v1.5 stay unaccepted history, preserved byte-identically; the continuation lineage keeps the standings §2.2 states; the accepted §8.8 package is bound, not extended; implementation remains separately unauthorized.

Acceptance does not itself edit the controller, restart a worker, alter A19, append a live journal event, install code, or launch a provider.

### 12.3 Separate installation boundary

Installation requires separate explicit authorization after acceptance and independent audit. It must occur at a safe durable maintenance boundary with no in-flight provider/controller operation and no unresolved historical T3 custody. Any controller identity change uses the existing clean worker-retirement and one-worker lease path.

Installation must preserve the exact live package/journal/custody state and resume from that durable state without repeating completed provider work. It must not restart a package, recreate questions, or convert historical T3 results into local envelopes.

### 12.4 Independent audit boundary

No Codex audit is launched by creating this file. Ness may inspect this candidate first. A later independent audit, if Ness requests it, must audit the exact file bytes then present and must not be represented as acceptance.

### 12.5 Final must-nevers

Implementation must never delete T3; let Claude choose package/scope/authority/sources/dependencies/path/policy; substitute prompt prose for controller enforcement; remove validation, fresh coverage, or fresh audit; add a T3/STOP provider lifecycle; rewrite history; bypass reconciliation/no-duplicate; weaken one-file custody/no-overwrite; treat PASS as acceptance; or enter build/production/integration/Git work.

The intended result is exactly one removed serial provider design call, one local deterministic envelope in its place, one independently designing Claude, one fresh independently challenging Codex, and Ness still in control of every consequential decision.

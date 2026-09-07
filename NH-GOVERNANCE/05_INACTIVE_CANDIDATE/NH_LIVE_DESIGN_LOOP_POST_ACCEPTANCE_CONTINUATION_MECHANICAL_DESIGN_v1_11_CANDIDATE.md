# NH_LIVE_DESIGN_LOOP_POST_ACCEPTANCE_CONTINUATION_MECHANICAL_DESIGN_v1_11_CANDIDATE.md

## §0 — STATUS BLOCK, PROVENANCE, AND SELF-DESCRIPTION

**Status:**
`CANDIDATE — NOT ACCEPTED — NOT ADOPTED — NOT AUTHORITATIVE — NOT INTEGRATED — NOT IMPLEMENTED.`

**Date:** August 23, 2026 (creation of this v1_11 candidate was explicitly authorized by Ness on August 23, 2026, as one narrow DESIGN-ONLY wiring correction).

**Intended repository placement:** `NH-GOVERNANCE/05_ACTIVE_CANDIDATE/` (this file's actual location; no other placement is claimed and no move is performed).

**What this file is.** One bounded **live-loop mechanical bridge design**: the smallest safe mechanism by which the local N.H Claude/Codex design loop, after Ness durably accepts one design package, **continues the overall design-completion loop** by selecting and establishing the next genuinely dependency-safe DESIGN package — without weakening, reinterpreting, or removing the acceptance that closed the previous package.

### 0.1 Actual predecessor — stated exactly, not inferred from the filename

**Correction base (immediate predecessor):** `NH-GOVERNANCE/05_ACTIVE_CANDIDATE/NH_LIVE_DESIGN_LOOP_POST_ACCEPTANCE_CONTINUATION_MECHANICAL_DESIGN_v1_10_CANDIDATE.md`

| | |
|---|---|
| SHA-256 | `fafc27314aa09b3b4c3a7f2128b7faf495f0a6d3bedab5976e7d0465216ede64` |
| bytes | `443,388` |
| lines | `3,608` |

All three values were independently recomputed from the actual v1_10 file on disk immediately before this file was written, and matched. **v1_10 is preserved byte-identically and is not edited, overwritten, moved, renamed, or re-headed by this file.**

**And one thing this file states plainly rather than letting the filename imply it: `v1_10` is NOT an accepted design.** It is a candidate awaiting an independent audit of the actual file and Ness's own decision. **The currently ACCEPTED standalone design for this package remains `v1_9`** — see §0.1a. Also preserved byte-identically and unedited: **v1_9** (SHA-256 `711b89d30d36130eb2e9506e817429a5813e700b7c62fbbff97b340dc82a12ed`, 380,415 bytes, 3,249 lines) and **v1_8** (SHA-256 `448daa63b4899d4639dc5b7612985cb34e97732dcf4cbeac2c224c54f8ae51e2`, 303,820 bytes, 2,826 lines), both recomputed from disk and matched.

#### 0.1a v1_9 is STILL the currently ACCEPTED standalone design — v1_10 is not, and this file does not pretend otherwise

**Two different things are true at once, and conflating them would be the easiest error in this whole lineage:**

| | File | Standing |
|---|---|---|
| **The accepted design of record** | `v1_9` | **the currently ACCEPTED standalone design** for this package |
| **The correction base of this file** | `v1_10` | a **NOT-ACCEPTED candidate** — the newest correction, awaiting independent audit and Ness's decision |
| **This file** | `v1_11` | a **NOT-ACCEPTED candidate** deriving from v1_10 |

**A correction chain is not an acceptance chain.** v1_10 corrected an IMPORTANT contradiction found in the accepted v1_9, and v1_11 corrects an IMPORTANT wiring gap found in v1_10 — but **neither v1_10 nor v1_11 has been accepted, and neither replaces v1_9 unless and until Ness explicitly accepts it.** Until that happens, **v1_9 remains the accepted standalone design of record**, and this file says so rather than copying forward wording that would imply otherwise.

**v1_9's acceptance, stated exactly.**

| Fact | Value |
|---|---|
| Accepted source | `NH-GOVERNANCE/05_ACTIVE_CANDIDATE/NH_LIVE_DESIGN_LOOP_POST_ACCEPTANCE_CONTINUATION_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` |
| Accepted source SHA-256 | `711b89d30d36130eb2e9506e817429a5813e700b7c62fbbff97b340dc82a12ed` |
| Accepted source bytes / lines | `380,415` / `3,249` |
| How it was accepted | Ness explicitly accepted **those exact bytes** on August 23, 2026, after ChatGPT independently audited the **ACTUAL file** and returned **PASS** |

That identity was independently recomputed from the actual file on disk immediately before this file was written, and matched.

**Therefore, exactly and without embellishment:**

- **v1_9 remains preserved byte-identically**, in its current location, and is not edited, patched, moved, renamed, re-headed, superseded in place, or re-described by this file. **Its internal status text remains historical bytes and is not rewritten** — exactly as the accepted receipts already do for their own accepted sources.
- **v1_9 remains the currently accepted standalone design of record**, and **that historical acceptance is real, did not disappear, and is not diminished here.**
- **v1_10 remains preserved byte-identically** (SHA-256 `fafc27314aa09b3b4c3a7f2128b7faf495f0a6d3bedab5976e7d0465216ede64`, 443,388 bytes, 3,608 lines), is not edited, patched, moved, renamed or re-headed, and **its internal status text is likewise not rewritten.** **v1_10 is a candidate and was never accepted, adopted, audited-PASS, integrated or implemented, and this file claims none of those things for it.**
- **v1_8 also remains preserved byte-identically**, together with the separate `PACKAGE_COMPLETE` closure record that names it (`NH-GOVERNANCE/04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DESIGN_LOOP_POST_ACCEPTANCE_CONTINUATION_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`, SHA-256 `940cf3a29b0d41836322e6a55dbe9c56d491e840848d6ec80c2d24b4a9663dd4`). **That receipt still names v1_8 and has not been updated to record the later v1_9 acceptance.** That is **bookkeeping lag, not an open Ness acceptance question** — the same shape §1.3 already records for the acceptance-button lineage — and **no receipt is created, amended, superseded or annotated by this file.**
- **A review of v1_10 exposed one further IMPORTANT mechanical defect inside it** (§0.2, §5 P-35): v1_10 states the T4 exhaustion stop correctly in §14.3 but **never wires it into the transition-state derivation or the loop-status precedence**, so an implementer following the state machine would still be routed back to `execute-initial-design`. That is a real mechanical **wiring** defect — **not** a cosmetic note and **not** a wording preference.
- **This file, v1_11, is a NEW CORRECTED CANDIDATE.** It has **not** been accepted by Ness. It is not adopted, not authoritative, not integrated, not implemented, and not `PACKAGE_COMPLETE`. **No ChatGPT audit PASS is claimed for it, and none is claimed for v1_10 either.**
- **v1_11 does not replace, retire, supersede, or reduce the accepted v1_9 unless and until Ness explicitly accepts v1_11** for this scope. Until that happens, **v1_9 remains the accepted standalone design of record**, and both v1_10 and v1_11 are candidates awaiting an independent audit of the actual file and Ness's own decision.
- **No authority, Master, Map, Defaults, `cursorrules`, Companion or Register integration is performed here**, and none is claimed, implied or anticipated. **No production restart is authorized by this file.**

**Preserved lineage.** `v1_0` (SHA-256 `6cfe8d07cce712d5fa8077fdb4930a53ac10c52d9cdc02551c15a316e4695ab0`), `v1_1` (SHA-256 `7ba76ef61d736cef07f83f4a814200bbc3776ff031cc4eb40230e7fa4e6843e3`), `v1_2` (SHA-256 `40f217aa018a9fecb4581e0a70004550b22e75234d94543813e7da0f0537f545`), `v1_3` (SHA-256 `78d57db9e4cc434161b05cb2c0945b9c5b8d22a3fb91ebb4e134543e3987701d`), `v1_4` (SHA-256 `7fd023c61fdcaf204c2394c28a15ae0f17c30c0e9ce3cb3c269c8b75490b9067`), `v1_5` (SHA-256 `80284a20da80a87d08617051d7a0207c3ef06bd4f902cfa28619bb1cf7c55f36`), `v1_6` (SHA-256 `f211ffd90a0ffc6732589d7442c925f2bcac7e7e0740bfb4abaea8d0d9852948`), `v1_7` (SHA-256 `747a045675c4db771e9ac9490343da82fb986bc9bf255aa42cb85b4a432c62c3`) `v1_8` (SHA-256 `448daa63b4899d4639dc5b7612985cb34e97732dcf4cbeac2c224c54f8ae51e2`), `v1_9` (SHA-256 `711b89d30d36130eb2e9506e817429a5813e700b7c62fbbff97b340dc82a12ed`) and `v1_10` (SHA-256 `fafc27314aa09b3b4c3a7f2128b7faf495f0a6d3bedab5976e7d0465216ede64`) all remain preserved unchanged. Their corrections were carried into v1_10 and are carried forward unchanged here.

### 0.2a The correction v1_11 applies — the whole of it *(new in v1_11)*

**Every substantive mechanic settled in v1_0 through v1_10 is preserved and is not redesigned.** v1_11 is a bounded **T4 exhaustion wiring** correction of one IMPORTANT mechanically incomplete wiring defect inside v1_10. It is deliberately the narrowest object that closes that gap, and it changes nothing else.

**The defect, stated exactly.** v1_10's §14.3 `INIT-EXHAUSTION-IS-NOT-A-CONSUMPTION` describes the T4 / `claude_initial_design` bounded invalid-output exhaustion stop **correctly**: no further initial-design request is dispatched on the exhausted condition; `close-open-consumption` is **not** owed; no `diagnosis_strategy_consumption_started` and no `diagnosis_strategy_consumption_terminated` is invented; the position is `LOOP_NEEDS_USER_ACTION` with a null `loop_next_command`; zero further Claude or provider calls occur on that exhausted condition; the position is restart-stable; and all durable request/result/history evidence is preserved. **That meaning is already settled and is NOT redesigned here.**

**But v1_10 never wired it.** `post_acceptance_transition_state()` (§17.2) carries **no** T4 exhaustion fact, and the §7.4 `loop_status()` precedence has **no** T4 guard. The T1 guards exist:

```
    if t.t1_custody_unverifiable:            return LOOP_SAFETY_HOLD, null
    if t.t1_output_retry_exhausted:          return LOOP_NEEDS_USER_ACTION, null
```

and the T4 fall-through does not:

```
    if t.initial_result_custody is None:     return LOOP_INITIAL_DESIGN_REQUIRED,
                                                    execute-initial-design
```

`initial_result_custody` is the newest custodied `claude_initial_design` terminal whose bytes re-verify **and** pass all ten `INIT-ADMISSION` checks (§17.2). **An exhausted run of `result_invalid` terminals produces no such custody**, so `t.initial_result_custody` is `None`, and the derivation returns `LOOP_INITIAL_DESIGN_REQUIRED` / `execute-initial-design` — **for ever**, on every restart, against a budget that is already spent.

**So §14.3 and the state machine describe two different systems.** An implementer following §14.3 stops honestly; an implementer following §7.4 and §17.2 keeps being told to run `execute-initial-design`. **A design in which the prose and the derivation disagree is mechanically incomplete, and that is IMPORTANT, not cosmetic** (§5 P-35).

| # | Correction | Sections rewritten |
|---|---|---|
| 1 | **The T4 derived exhaustion fact.** `post_acceptance_transition_state()` gains the derived field `initial_design_output_retry_exhausted` `[proposed]` — a **pure derivation** over the existing durable `claude_initial_design` evidence and the **same installed `bounded_output_retry_budget()`** that already governs the work item and episode. **No stored flag, no marker, no counter, no event, no second retry calculator, no second state source, and no new journal field.** | **§17.2**, §17.3, §24.1 |
| 2 | **The T4 guard in the loop-status precedence.** §7.4 gains one guard at the mechanically correct point — after the contradiction / established / stop-record / open-request handling that already outranks phase derivation, and **before** the `t.initial_result_custody is None` → `execute-initial-design` fall-through — returning `LOOP_NEEDS_USER_ACTION` with a null next command, **zero appends, zero provider calls, zero new request identities.** | **§7.4**, §24.1 |
| 3 | **The restart/recovery and implementation-map text made consistent with that wiring**, so an implementer following §18 or §24 cannot conclude that an exhausted T4 returns to `execute-initial-design`, and so §24's claim that the exhausted T1 and T4 positions are read-only derivations is **mechanically backed by an explicit field and guard rather than by prose alone.** | §14.3, §18 Row I, §18.1, §19.3, §24.1, §24.5 |
| 4 | **The focused disposable rehearsal specification that proves it** — available budget, exhausted budget, governed oversize-invalid, restart stability, and the two negative obligations that no test may satisfy the case by opening or closing a `diagnosis_strategy_consumption_*` transaction or by calling `close-open-consumption`. | §25 (**new `R115`**), §27 |

**What v1_11 deliberately does NOT change.** It does not redesign the T4 exhaustion **meaning** — that was settled in v1_10 §14.3 and is preserved verbatim in substance. It disables no legitimate bounded retry: **while the budget remains available, ordinary installed T4 retry and recovery semantics continue exactly as before.** It changes no accepted B9 retry value, retry count, timer, wait, backoff, deadline, real-change rule, episode meaning or exhaustion meaning; introduces **no** new loop state, **no** new journal event type, **no** new state store, and **no** eighth continuation execution command; leaves `close_open_consumption()` completely untouched in meaning, un-genericised, and used for neither T1 nor T4 exhaustion; and touches nothing in §9.6a / §9.6b / §9.6c, §9.7, `T1-ACTIONABLE-ROOT`, the four non-actionable classifications, `genuinely_open_for_ness`, the routed-signal semantics, the coverage stop, T2 Paths A/B/C, E1–E5, `INIT-ADMISSION` I1–I10, or the Accept transaction. **And it does not solve, reinterpret, re-anchor, weaken or close the separate §8.8 source-binding-drift item, which remains open exactly where v1_9 and v1_10 leave it** (§8.8, §26 item 1).

**No unrelated cleanup was performed.** Every substantive difference between v1_10 and v1_11 is one of the four rows above, or a mechanically necessary title / version / provenance / cross-reference update.

### 0.2 The correction v1_10 applied — preserved for lineage

**Every substantive mechanic settled in v1_0 through v1_9 is preserved and is not redesigned.** v1_10 is a bounded **T1 invalid-output exhaustion** correction of one IMPORTANT internal contradiction that a real live implementation attempt against the accepted v1_9 design exposed. It is deliberately the narrowest object that removes that contradiction, and it changes nothing else.

**The contradiction, stated exactly.** The accepted v1_9 design establishes — correctly, and each of these is preserved here — that a current-contract **actionable rootless** T1 result is **invalid output**; that it receives a `result_invalid` terminal; that the **installed bounded output-retry budget** governs it; that retries are therefore bounded; that no new selector identity may be opened endlessly; that the earlier-contract one-shot permission stays consumed; that provider uncertainty remains reconciliation-first; that retry exhaustion must stop honestly; that there are **exactly seven** continuation execution commands; and that **`close-open-consumption` is not one of those seven**.

It then states, in several places, that when the T1 invalid-output budget is **exhausted** the route is:

```
    -> close-open-consumption
```

**That is mechanically impossible for T1**, and the impossibility is in the accepted design's own wording and routing expectation — not in Ness's policy, and not in anything Ness is being asked to decide.

The installed `close_open_consumption()` is **not** a generic "close any provider failure" operation. It closes **an actual open `diagnosis_strategy_consumption_started` transaction** by appending `diagnosis_strategy_consumption_terminated`, and it requires the diagnosis-consumption identity, the diagnosis authority, the correction specification, the strategy fields and the blocking findings that only the correction machinery ever creates. It refuses outright — *"no unclosed consumption with a proved final outcome exists"* — when no such consumption is open.

A `next_package_selection` T1 review creates **none** of those things. Therefore:

- there is **no T1 diagnosis consumption to close**;
- calling `close-open-consumption` there would **truthfully refuse**;
- creating a diagnosis consumption merely to make that command callable would be **fabricated authority and fabricated state**;
- adding `close-open-consumption` as an **eighth** continuation execution command would contradict the accepted closed command set **and still would not create the missing diagnosis consumption.**

**That is a real internal mechanical contradiction, and it is IMPORTANT, not cosmetic.** It was reached by execution against the accepted design, not by reading alone (§3.5, §5 P-34).

| # | Correction | Sections rewritten |
|---|---|---|
| 1 | **`T1-INVALID-OUTPUT-EXHAUSTION-STOP` — the honest exhaustion stop.** While the installed bounded output-retry budget remains **available**, ordinary current-contract T1 output retry governs, unchanged. Once it is **exhausted**, the loop stops at `LOOP_NEEDS_USER_ACTION` with a null next command, **zero** further provider requests on the exhausted condition, **zero** owed appends, **no** `close-open-consumption` command owed, **no** invented diagnosis consumption, **no** new event type, **no** new state store and **no** eighth continuation execution command. The position is re-derived deterministically from existing durable evidence and is **restart-stable**. | **new §9.6a**, §7.4, §9.5a, §9.6, §9.7.4, §14.3, §17.2, §18 Row D / Row D.1, §18.1, §19.3 |
| 2 | **`T1-NOT-A-CONSUMPTION` — no fake "consumption", and no loss of the genuine one.** A T1 next-package-selection review is **not** a correction-strategy consumption. The fact that the installed correction/diagnosis recovery path uses `close-open-consumption` does **not** make that command a universal provider-terminal closer, and its legitimate installed use for the diagnosis/correction machinery is preserved and named rather than deleted. | **new §9.6a**, §7.5, §7.6a, §23 |
| 3 | **`T1-CUSTODY-UNVERIFIABLE` — the custody clarification, stated so it cannot be missed.** A durable `next_package_selection` custody whose exact bytes are part of authenticated provider-result evidence is protected **regardless of whether its matching terminal is `result_received`, `result_invalid`, or another terminal form that truthfully carries or requires saved custody.** Saved bytes that fail exact `engine.custodied_bytes()` re-verification are `provider_result_custody_unverifiable` → `LOOP_SAFETY_HOLD` → null next command → **zero** provider calls, and are **never** treated as absent merely because the terminal is `result_invalid`. **This is a clarification of v1_9's existing `R109`, `SEL-LEGACY-NOT-CUSTODY-LOSS`, `CUSTODY-UNVERIFIABLE-HOLD` and "losing saved evidence is never permission to manufacture replacement evidence" semantics — not a new concept, not a new policy, and no restoration mechanism.** | **new §9.6b**, §7.6a, §19.3, §23, §25 R109 |
| 4 | **The fail-closed and rehearsal coverage the above requires**, so the impossible route cannot be written again: §23 gains `R-5e` and `R-11c`; `R104`, `R107` and `R109` are corrected in place; and every affected cross-reference is corrected. | §20, §23, §24, §25 (`R104`, `R107`, `R109` corrected), §26, §27, §28 |

**What v1_10 deliberately does NOT change.** It does not redesign B9, does not change any B9 retry value, does not change B9's real-change meaning, and does not invent a new retry count, wait, timer, deadline or real-change category. It introduces **no** new loop state — the outward stop is v1_9's already-settled `LOOP_NEEDS_USER_ACTION`. It does not redesign §9.7, and the special earlier-contract one-shot is preserved exactly, still consumed at `provider_request_prepared`. It does not touch `T1-ACTIONABLE-ROOT`, the four non-actionable classifications, `genuinely_open_for_ness` as evidence only, the routed-signal semantics, the coverage stop, question validation, independent coverage review, the seven continuation execution commands, the four/three provider-contacting/provider-free split, the five continuation provider kinds, T2 Paths A/B/C, E1–E5, the transition bindings, the one worker lease, the Accept transaction, the initial-design route, `INIT-ADMISSION` I1–I10, the custody-unverifiable fail-closed behaviour, or the one-shot provider-request-prepared fence. **And it does not solve, reinterpret, re-anchor, weaken or close the separate §8.8 source-binding-drift item, which remains open exactly where v1_9 leaves it** (§8.8, §26 item 1).

Plus the smallest rehearsal corrections that prove each of the above (§25).

Everything v1_0 through v1_9 got right is preserved unchanged in substance; §27 lists it. **v1_11 preserves all of the above and adds only the wiring §0.2a describes.**

**What this file does not do.** It writes no code, edits no code, applies no patch. It creates no store, no marker, no journal event, no candidate other than itself, no closure record, and no acceptance. It performs no Git operation. It integrates nothing into `NH_MASTER-20_CORRECTED_v10.md` or the Design and Wiring Map. It assigns no controlled component ID and no Register ID. It marks nothing `PACKAGE_COMPLETE`, closes no dependency, authorizes no implementation or building, starts no next package, and accepts or adopts nothing — including itself. **It creates exactly one new file — itself — and modifies nothing.**

**Roles, unchanged and obeyed here.** Ness owns concept and meaning, policy and priorities, acceptance and adoption, and permission to begin building. ChatGPT independently audits the actual file. Claude drafts new versioned design candidates. Cursor codes only after the design is complete and Ness separately authorizes building. **This file is a Claude-drafted candidate awaiting an independent audit and Ness's explicit acceptance; neither is claimed, implied, or anticipated anywhere below.**

**Naming discipline.** These names are **LOCKED** — they exist in accepted design or installed code and are used verbatim:

`ACCEPTED_FOR_DESIGN_ONLY` · `PROVED_ACCEPTED` / `PROVED_NOT_ACCEPTED` / `UNRESOLVED` · `IDLE` / `WORKING` / `DIAGNOSING` / `WAITING_RECOVERING` / `NEEDS_NESS_DECISION` / `NEEDS_USER_ACTION` / `SAFETY_HOLD` / `READY_FOR_ACCEPTANCE` · `ness_candidate_acceptance_recorded` · `validation_recorded` · `question_coverage_review_recorded` · `review_signal_recorded` / `routed_issue_recorded` · `candidate_write_ahead_recorded` / `candidate_write_ahead_aborted` / `candidate_custody_recorded` · `piece3_provider_work_recorded` · `supervisor_operation_started` / `supervisor_operation_completed` · `provider_request_prepared` / `provider_dispatch_begun` / `provider_request_accepted` / `provider_result_custody_recorded` / `provider_request_terminal_recorded` / `provider_request_reconciled` · `package_scope_id` / `scope_root_path` / `package_source_binding` · `next-package` / `prepare-next-claude-task` / `execute-next-claude-task` / `process-custodied-provider-result` / `reconcile-provider-request` / `close-open-consumption` / `supervisor-operation-status` / `question-validation` / `question-coverage-review` / `acceptance-offer` / `record-ness-acceptance` / `declare-stranded-candidate` · `package_source_path` / `classification` / `controller_action` / `task_ready` / `target_path` / `mechanical_design_specification` / `not_ready_reason` / `whole_check_complete` / `source_paths_checked` · `prepare_claude_task` / `report_settled` / `wait_dependency` / `hold_for_question_validation` / `defer_future` / `defer_build` · `CANDIDATE_INTENT_ORIGIN_PREPARED` / `CANDIDATE_CUSTODY_ORIGIN_PROMOTED` / `CANDIDATE_CUSTODY_ORIGIN_RECOVERED` / `CANDIDATE_INTENT_ORIGIN_DECLARED`.

**Every other label introduced here is marked `[proposed]` at first use.** Exact spellings, prefixes, HTTP paths and display strings other than the locked names remain open only where §26 says so; §26 no longer parks choices this bridge itself can and must settle.

**Pseudocode notice.** Structured pseudocode below is **explanatory only** — not patch-ready, no complete function bodies, never to be pasted into any file.

---

## §1 — AUTHORITY AND SOURCE REGISTER

### 1.1 Governing authority order

1. `NH-GOVERNANCE/01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` — **governs every conflict.**
2. `NH-GOVERNANCE/01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` — the current authoritative Decision Defaults, **settled by Master V10 itself** (§10).
3. `NH-GOVERNANCE/01_AUTHORITATIVE/cursorrules`
4. `NH-GOVERNANCE/01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`
5. `NH-GOVERNANCE/02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`
6. Accepted standalone packages and their acceptance / closure records, within their own stated scopes.

Lower authorities never override higher ones. This file is subordinate to all of them and creates no authority of its own.

### 1.2 Workflow, plan and decision sources read

`03_WORKFLOW/NH_FULL_DESIGN_COMPLETION_WORKFLOW_v1_0.md` (§5 select the next dependency package; §6 pre-question full audit and the six-way classification; §7 one genuine concept decision; §14 package closes on Ness's acceptance; §15 repeat Phases 2–11) · `03_WORKFLOW/NH_REPLACEMENT_EIGHT_BUNDLE_DEPENDENCY_PLAN_v1_0_CANDIDATE.md` (the eight bundles; global execution rules; "priority is dynamic") · `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md` · `NESS_DESIGN_INPUTS/NH_LIVE_LOOP_AUTOMATIC_SUPERVISOR_DECISION_v1_0.md` (§2 the seven-step plain-language rule; §3 bounded continuation; §4 controller-owned states; §5 truthful blocker classification; §6 browser behaviour) · `NH_CHATGPT_PROJECT_INSTRUCTIONS_FULL_v1_2.md` (operating method; one package at a time; actual files over remembered descriptions).

### 1.3 The accepted package records — and the acceptance lineage, stated correctly

- **Addition 1 — Authority Integrity Control Plane.** `PACKAGE_COMPLETE` for `NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md`, SHA-256 `b39654a60744982d0e2f16c2bc3cd7a33f6ae47ff55b63b5b1dfffada719d709`, 3,260 lines, 282,955 bytes.
- **Addition 2 — Unified Durable Operation Kernel.** `PACKAGE_COMPLETE` for `NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md`, SHA-256 `1f9ea714f1a182c0857e80399850a3aeebcf4a50a32d5a200fce57a5d5f47ae3`, 1,686 lines, 343,868 bytes. Its §8 states that closure "does not automatically start Addition 3, Addition 4, Addition 5, whole-system consolidation, Master/Map integration, Register assignment, B-CYCLE completion, or implementation."

**The acceptance-button / acceptance-record lineage — recorded accurately, and NOT an open question.**

| Fact | Value |
|---|---|
| Source named by the older `PACKAGE_COMPLETE` receipt | `..._MECHANICAL_DESIGN_v1_14_CANDIDATE.md`, SHA-256 `c4f055f271cbeea246291986b1b11367fcfb1748466f346e642176df2b36b46a`, 2,324 lines, 401,581 bytes |
| Source Ness **later explicitly accepted** for the same standalone acceptance-button / acceptance-record scope | `..._MECHANICAL_DESIGN_v1_15_CANDIDATE.md`, SHA-256 `b10727441ddf7502ff7525c79b0b71043b559502660dcc7c3b9001f0633ffcc6`, 2,338 lines, 409,297 bytes |

The v1.15 SHA-256 above was independently recomputed from the actual file on disk and matches the identity Ness named.

Therefore:

- **v1.15 governs current downstream design wherever it differs from v1.14.** This bridge is downstream design, so v1.15 is the acceptance-design authority it is written against.
- **v1.14 remains preserved historical provenance**, together with the older `PACKAGE_COMPLETE` receipt that names it.
- **The older receipt has not yet been updated to record the later v1.15 acceptance. That is bookkeeping lag, not an open Ness acceptance question**, and this file does not treat it as one.
- v1.15's own internal status wording is not rewritten in place, exactly as the accepted receipts do for their own accepted sources.
- **No receipt is created or modified by this task.** Whether and when the receipt is brought up to date is ordinary later bookkeeping under the established workflow, and it is not a blocker for this bridge.

### 1.4 Controller and worker sources inspected

Read directly from disk and cited below by `file:line`: `controller/nh_loop.py` (46,557 lines) · `controller/nh_supervisor/` `constants.py` `schema.py` `identity.py` `replay.py` `status.py` `commands.py` `engine.py` `journal.py` `runtime.py` `lease.py` `scheduling.py` `provider.py` `classify.py` · `interview_ui/` `worker.py` `supervisor.py` `server.py` `production.py`.

**No file above was modified by the work that produced this candidate.**

### 1.5 The accepted predecessor and the live evidence this correction is derived from *(v1_9; re-registered in v1_10)*

Three further sources are part of this file's register, and every one of them was read **read-only**.

**(a) The accepted predecessor, and the receipt that has not yet caught up.**

| Source | Identity | Standing |
|---|---|---|
| `05_ACTIVE_CANDIDATE/NH_LIVE_DESIGN_LOOP_POST_ACCEPTANCE_CONTINUATION_MECHANICAL_DESIGN_v1_10_CANDIDATE.md` | SHA-256 `fafc27314aa09b3b4c3a7f2128b7faf495f0a6d3bedab5976e7d0465216ede64`, 443,388 bytes, 3,608 lines | **the exact correction base of this file** — and a **NOT-ACCEPTED candidate**: no Ness acceptance and no ChatGPT audit PASS is claimed for it; preserved byte-identically and not amended by this file |
| `05_ACTIVE_CANDIDATE/NH_LIVE_DESIGN_LOOP_POST_ACCEPTANCE_CONTINUATION_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` | SHA-256 `711b89d30d36130eb2e9506e817429a5813e700b7c62fbbff97b340dc82a12ed`, 380,415 bytes, 3,249 lines | **the currently accepted standalone design** for this package — Ness explicitly accepted these exact bytes after ChatGPT independently audited the **actual file** and returned **PASS**; preserved byte-identically and not amended by this file |
| `05_ACTIVE_CANDIDATE/NH_LIVE_DESIGN_LOOP_POST_ACCEPTANCE_CONTINUATION_MECHANICAL_DESIGN_v1_8_CANDIDATE.md` | SHA-256 `448daa63b4899d4639dc5b7612985cb34e97732dcf4cbeac2c224c54f8ae51e2`, 303,820 bytes, 2,826 lines | the earlier accepted standalone design; **preserved byte-identically and not amended by this file** |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DESIGN_LOOP_POST_ACCEPTANCE_CONTINUATION_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | SHA-256 `940cf3a29b0d41836322e6a55dbe9c56d491e840848d6ec80c2d24b4a9663dd4` | the separate accepted closure record; it still **names v1_8**; **untouched, byte-identical, and not amended by this file.** The lag between it and the later v1_9 acceptance is **bookkeeping, not an open Ness decision** (§0.1a) |

**(b) The real authenticated live evidence.** The authenticated interview journal at `nh_interview_state/nh_interview_journal.jsonl` and its head file were read read-only at the position recorded in §3.4 and re-proved unchanged at §3.5; the exact custodied T1 selection bytes carried by the authenticated `provider_result_custody_recorded` at `event_seq 88` were decoded and re-hashed by v1_9's work and are not re-decoded destructively here. **No event was appended, no state was written, no provider was contacted, no production process was started, and no controller was modified by the work that produced this candidate.**

**(b2) The installed bounded-retry calculation, read directly** *(new in v1_11)*. `controller/nh_supervisor/replay.py` — `Replay.bounded_output_retry_budget()` and the `output_retries_used()` count it consults — and `controller/nh_supervisor/commands.py` — the installed recovery routing that already calls that same function for an exhausted `result_invalid` — were read **read-only**, because §17.2's new T4 derived field must consume **exactly that installed calculation** and must not become a second retry calculator. **Neither file was modified.**

**(c) The installed correction/diagnosis machinery, read directly.** `controller/nh_supervisor/commands.py` — `close_open_consumption()` and the recovery routing that names it — and `controller/nh_supervisor/constants.py` — `SUPERVISOR_COMMANDS`, `CONTINUATION_NEW_EXECUTION_COMMANDS`, `CONTINUATION_INSTALLED_EXECUTION_COMMANDS`, `CONTINUATION_EXECUTION_COMMANDS` — and `controller/nh_supervisor/replay.py` — `bounded_output_retry_budget()` — were read read-only, because §9.6a's correctness depends on what those actually do rather than on what a design once said they would do. **None of them was modified.**

**One boundary stated plainly, and it applies twice.** A blocked implementation attempt against the accepted v1_8 design produced a written report containing a recommendation, and a later disposable implementation correction against the accepted v1_9 design produced a further written report of its own (§3.5). **Neither report is authority and neither is policy, and this file adopts neither's recommendation.** What they are used for here is exactly one thing: **evidence that the mechanical contradiction is real and was reached by execution.** The corrective rule below is derived from the accepted design's own mechanics, from the installed code's own refusal, and from Ness's settled decisions — not from either report.

---

## §2 — NESS'S SETTLED DECISIONS

Four decisions govern this design. **None of them is re-opened, re-asked, made conditional, or listed as open anywhere below.**

### 2.1 Continuation after acceptance — verbatim

> After one design package reaches ACCEPTED_FOR_DESIGN_ONLY, that acceptance
> finishes THAT PACKAGE'S current design workflow.
>
> It must NOT permanently stop the overall N.H design-completion loop.
>
> After acceptance is fully durable, the overall loop should automatically
> continue by finding the next real dependency-safe DESIGN package from current
> N.H sources.
>
> The loop should continue automatically through mechanical design work and stop
> for Ness only when:
>
> - a genuinely open Ness meaning/policy decision is required;
> - explicit Ness acceptance of another completed package is required;
> - a practical external user action is required;
> - an authority/safety conflict prevents safe continuation;
> - or continuation cannot safely be proved.
>
> Do not ask Ness this decision again.

### 2.2 The Accept transaction — verbatim

> The Accept GET/POST transaction itself must remain exactly acceptance-only.
>
> Pressing Accept must NOT:
> - select a package;
> - invoke Claude;
> - invoke Codex;
> - start another package;
> - alter Git;
> - perform integration or implementation.
>
> Post-acceptance continuation is a SEPARATE controller/worker operation that
> may occur only AFTER acceptance is durably committed and freshly proved.

### 2.3 The adopted Decision Defaults

> The currently adopted Decision Defaults are `NH_DECISION_DEFAULTS-S19_v2_2.md`.

This is not merely an instruction: it is what the highest authority in the project already says (§10.1).

### 2.4 The accepted acceptance-design source

> Ness later explicitly accepted
> `NH_NESS_DESIGN_ACCEPTANCE_RECORD_AND_UNDERSTANDABLE_ACCEPTANCE_SURFACE_MECHANICAL_DESIGN_v1_15_CANDIDATE.md`,
> SHA-256 `b10727441ddf7502ff7525c79b0b71043b559502660dcc7c3b9001f0633ffcc6`,
> for its standalone acceptance-button / acceptance-record scope.

---

## §3 — CURRENT REAL STATE THIS DESIGN PRESERVES

Every value below was read from the actual authenticated journal at `nh_interview_state/nh_interview_journal.jsonl` and from the actual N.H checkout.

**Reading order note *(new in v1_9)*.** §3.1 through §3.3 record **the acceptance and the package it belongs to**, exactly as they were established and exactly as they remain true: the acceptance is the event at `event_seq 84`, and nothing about it has changed. The authenticated journal has since advanced past that point, under the accepted design's own T1 selection route. **§3.4 records the current proved position and the exact preserved T1 selection result at that position**, because §9.7's transition rule is written about that real, preserved evidence. Neither section supersedes the other: §3.1–§3.3 are about the acceptance, §3.4 is about where the journal now stands.

### 3.1 The authenticated acceptance

| Fact | Value |
|---|---|
| `workflow_state` | `ACCEPTED_FOR_DESIGN_ONLY` |
| `acceptance_truth` | `PROVED_ACCEPTED` |
| `acceptance_disposition` | `ACCEPTED_FOR_DESIGN_ONLY` |
| authenticated `event_seq` | `84` |
| accepted candidate | `05_ACTIVE_CANDIDATE/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_6_CANDIDATE.md` |
| candidate SHA-256 | `7f62ee5af84cea0332eeb71d2665a66178a318deb7917e9814385b57737acf4c` |
| candidate bytes | `188,236` |
| fresh audit identity | `f9abf5e08af8441965b5049034dd22c73428fb0e6b74b3573c828af539cf18af` |
| acceptance identity | `acc_b0657b3efa34526ce485547fa56130218fd35a42b64f8904c144fb83f336f79c` |
| acceptance scope id | `NH_ACCEPTANCE_SCOPE_DESIGN_ONLY_V1` |
| acceptance action channel | `local_browser_post` |
| `package_scope_id` | `nullpkg_1ffc9ec7aae12b75ef50400da674812f` |
| `package_key` | `no_controlled_id_settled_yet` |
| `package_id` | `null` (controlled id genuinely open) |

No open provider requests. No open result custody. No current dependency. No current errors.

### 3.2 The package this acceptance belongs to

84 authenticated events. Exactly two `validation_recorded`, both under the same scope:

| `event_seq` | `scope_root_path` | seed evidence | `head_sha` |
|---|---|---|---|
| 1 | `…AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_0_CANDIDATE.md` | `current_worktree_candidate` | `ce3a38f43f287a56bd635ed836edf002a2db50a7` |
| 6 | same root + two `authenticated_custodied_successor` seeds (`v1_1`, `v1_2`) | `current_worktree_candidate` | `64af315f8185881d0350b29b7f93d5465dee57e7` |

The scope is derived from the bound source root because the controlled id is genuinely open (`interview_package_scope_id()`, `controller/nh_loop.py:25669`; prefix `nullpkg_` at `:25665`). The custody chain anchors on `v1_0` and runs to the accepted `v1_6`: 7 write-aheads, 1 abort, 6 custodies.

### 3.3 What this design promises about that state

The acceptance at `event_seq 84` is preserved exactly — not reinterpreted, not removed, not weakened, not made non-terminal for its own package. `PROVED_ACCEPTED` remains that package's governed truth. The accepted candidate and every earlier candidate remain byte-identical. The two validations, the audit, the PASS and the explanation records remain untouched authenticated history.

### 3.4 The current proved position, and the preserved earlier-contract T1 selection *(new in v1_9)*

Read read-only from the actual authenticated journal, its head file, and the installed read-only `supervisor-status` and `loop-status` projections. **Nothing below was appended, altered, replayed destructively, or re-dispatched.**

| Fact | Value |
|---|---|
| `workflow_state` | `ACCEPTED_FOR_DESIGN_ONLY` |
| `acceptance_truth` | `PROVED_ACCEPTED` |
| `authenticated_event_seq` | `90` |
| `open_provider_request_count` | `0` |
| `open_result_custody_count` | `0` |
| `errors` | `[]` |
| `journal_authentication_proved` | `true` |
| `authenticated_state_current` | `true` |
| `run_lease.lease_state` | `ABSENT_PROVED` |
| `run_lease.live_proved` | `false` |

The loop level currently reports `LOOP_SAFETY_HOLD` with `loop_next_command` null. **That hold is the accepted design behaving fail-closed, and it is strictly safer than proceeding.** This file does not alter it, does not clear it, and does not treat it as an error to be suppressed.

**The transition lineage at that position — six authenticated events, intact.**

| `event_seq` | type | fact |
|---|---|---|
| 85 | `supervisor_operation_started` | `continue-design-loop` under the accepted package's scope |
| 86 | `provider_request_prepared` | `provider_kind = codex_next_package_selection`, `work_item_kind = next_package_selection`, `result_schema_id = NH_NEXT_PACKAGE_SELECTION_LIFECYCLE_V1` |
| 87 | `provider_dispatch_begun` | one dispatch, serial 1 |
| 88 | `provider_result_custody_recorded` | 5,076 result bytes, `custody_readback_proved: true` |
| 89 | `provider_request_terminal_recorded` | `terminal_kind = result_received`, `terminal_evidence_kind = local_completion`, `provider_returncode = 0`, `result_schema_valid = true` |
| 90 | `supervisor_operation_completed` | `operation_outcome = ok` |

**The old provider request is definitively terminal and custodied — not uncertain.** Its `provider_request_identity` is durable, its dispatch has a durable terminal recording `result_received`, its result custody is durable and its bytes re-verify, and the read-only projection reports **zero** open provider requests and **zero** open result custodies. **There is nothing here to reconcile: the request completed and its answer was saved.**

**The custodied T1 result itself, decoded from the authenticated event-88 bytes and re-hashed:**

| Field | Value |
|---|---|
| `classification` | `genuinely_open_for_ness` |
| `controller_action` | `hold_for_question_validation` |
| `package_source_path` | **`null`** |
| `whole_check_complete` | `true` |
| `unknowns` | `[]` |
| `source_paths_checked` | 36 real, resolved, permitted repository paths |

**Those bytes were valid under the v1_8-era T1 result contract.** The installed validator permits a null `package_source_path` for any `controller_action` other than `prepare_claude_task`, and `hold_for_question_validation` is such an action. **The selector exercised a permission the accepted design granted it. This is not a bad reply, not a malformed reply, and not a selector defect** — it is the accepted contract working exactly as written, and running straight into the accepted design's own `SEL-ROOT-IDENTIFIES` requirement.

**What this file does with that evidence — and what it refuses to do with it.** The result is preserved. It is not deleted, not rewritten, not re-headed, and its `package_source_path` is not changed. **No root is inferred, derived, name-matched, or manufactured for it from `source_paths_checked` or from any other field**, and its `simple_explanation` is never used as a Ness question. §9.7 states the one bounded, current-contract rule that applies to it, and §5 P-33 states the finding it proves.

### 3.5 The same position, re-proved read-only — for v1_10, and again for v1_11 *(v1_10; re-proved in v1_11)*

Before one byte of this file was written, the real state above was **re-proved read-only** and had **not moved**. The same table was proved for v1_10 and proved again, unchanged, for v1_11.

| Fact | Value re-proved for v1_10 |
|---|---|
| `workflow_state` | `ACCEPTED_FOR_DESIGN_ONLY` |
| `acceptance_truth` | `PROVED_ACCEPTED` |
| `authenticated_event_seq` | `90` |
| `open_provider_request_count` | `0` |
| `open_result_custody_count` | `0` |
| `errors` | `[]` |
| `run_lease.lease_state` | `ABSENT_PROVED` |
| `run_lease.live_proved` | `false` |
| production | **stopped — no production process was running, and none was started** |

**The live controller still holds the installed Correction-5 bytes and therefore still reports the old `LOOP_SAFETY_HOLD`. This file does not alter that, does not clear it, does not install anything, and authorizes no production restart.**

**What the v1_11 work touched, exactly** *(new in v1_11)*: it read the actual v1_10 file, the actual authority and accepted files, and the installed controller sources **read-only**, and it created **one** new file — itself. **It appended no journal event, wrote no state, started no production process, ran `production.py` not at all, contacted no provider, installed no disposable build, and performed no Git operation.**

**The evidence that exposed the contradiction this file corrects.** A later disposable implementation correction against the accepted v1_9 design — carried out entirely outside the live controller, installing nothing — reached the exhausted T1 invalid-output position and found that the accepted design's stated route there could not be executed: the installed `close_open_consumption()` truthfully refuses when no `diagnosis_strategy_consumption_started` is open, and a `next_package_selection` review never opens one. That written report is **implementation evidence, not authority** (§1.5), it is **preserved unchanged**, and **nothing from it is installed by this file.**

**Two facts from that same work are recorded here because they are boundaries, not conclusions:**

- **`EVENT90_MIGRATION_REHEARSAL_ISOLATES_KNOWN_SOURCE_BINDING_DRIFT = YES`**
- **`EVENT90_REHEARSAL_PROVES_REAL_LIVE_DRIFT_CLEARED = NO`**

The separate §8.8 anchor-versus-newest source-binding drift was **deliberately isolated and explicitly not proved cleared** on the real live state. **v1_10 does not solve, reinterpret, re-anchor, weaken or close it** (§8.8, §26 item 1), and **this candidate does not authorize a production restart.**

---

## §4 — PROBLEM STATEMENT

A durable acceptance stops the whole local loop, permanently, in three places: the projection treats acceptance as globally terminal (`status.py:1533-1536`); the worker runs nothing at all in that state (`worker.py:74-85`); and the package binding anchors forever on the first package-bound validation (`nh_loop.py:46322-46336`). That is a correct implementation of the previous rule and an incorrect implementation of §2.1.

Two structural facts make the gap larger than deleting a line: the modern supervisor has no work item that creates a package's **first** candidate, and the only machinery that creates one lives in the older top-level path, which the worker environment routes away from.

The goal, exactly:

> **CURRENT PACKAGE:** accepted → terminal forever, for that package.
> **OVERALL LOOP:** accepted package → one separate, bounded continuation → dynamically select the next safe DESIGN package from current sources → prepare its exact bounded task → establish its own authenticated scope and first candidate durably → hand it to the modern supervisor → continue.

---

## §5 — CURRENT INSTALLED-PATH ANALYSIS

Each finding was confirmed by reading the actual installed file.

### P-1 — Acceptance is projected as globally terminal
`status.py:1531-1536`. Precedence 11.5 fires on the **governed** acceptance truth and sets `ACCEPTED_FOR_DESIGN_ONLY`, `next_command = None`. It sits above the PASS rule and below every safety, contradiction and journal-integrity refusal. **Correct and preserved** — it is about the bound package.

### P-2 — The worker treats the accepted state as the end of everything
`worker.py:74-85` (`NON_RUNNING_STATES`), `worker.py:221`, `worker.py:424-428` ("this workflow is terminal and no next package is started here").

### P-3 — `build_supervisor_context()` anchors on the FIRST package-bound validation, forever
`nh_loop.py:46322-46328` — the loop `break`s on the first match. Every `PackageBinding` field comes from that one event (`:46356-46372`). **Observable today:** the acceptance at seq 84 carries `head_sha ce3a38f4…` from validation seq 1, while validation seq 6 and the live checkout are at `64af315f…`.

### P-4 — The supervisor has no initial-candidate work item
`constants.py:123-137` lists eight kinds — `design_audit`, `correction_specification`, `correction_apply`, `correction_diagnosis`, `change_explanation_review`, `question_validation`, `coverage_review`, `acceptance_explanation_content`. `commands.py:1289-1298` dispatches them; every branch operates on `situation.candidate`.

### P-5 — Under the worker env, `execute-next-claude-task` never reaches the old initial-write path
`nh_loop.py:46523-46528`; `interview_ui/production.py` launches the real worker with `NH_SUPERVISOR_WORKER=1`.

### P-6 — `next-package` and `prepare-next-claude-task` are unreachable from the worker
Dispatched only as top-level commands (`nh_loop.py:46519-46522`); absent from `worker.py:82-98` `WORKER_COMMANDS`.

### P-7 — The selector's authority order names a Decision Defaults version that is not the current authoritative one
`NEXT_PACKAGE_PROMPT` authority line at `nh_loop.py:433` names `NH_DECISION_DEFAULTS-S19_v2_3.md`; the same literal recurs at `:734`, `:1310`, `:2001`, `:2427`, `:2595`, `:24275`, `:24553`, and in `EXACT_REQUIRED_FILES` at `:3265`.

### P-8 — A package binding needs a real source seed
`derive_package_source_binding()` (`nh_loop.py:26983`) binds through four ordered classes and refuses ambiguity. `prepare-next-claude-task` STEP 3 states the consequence (`nh_loop.py:8313-8317`): a package "that has never entered the interview at all has nothing to seed the binding with and fails closed here."

### P-9 — The live-checkout binding class is ambiguous in this checkout today
The real `NH-GOVERNANCE` worktree names **42 untracked paths, 38 of them active candidates**; `bind_one()` would refuse as ambiguous.

### P-10 — The supervisor's Piece-3 gate is real and **unscoped**
`supervisor_piece3_authorization_gate()` (`nh_loop.py:32309-32338`, call site `:32481`) requires an unconsumed `piece3_provider_work_recorded`; it constructs `Replay(events)` with **no scope**, and `Replay.__init__` treats a `None` scope as every event. Package A's authorization would satisfy package B's validation.

### P-11 — Supervisor Piece-3 routing is reachable only from a `possible_ness_choice` diagnosis
`status.py:1448-1496`. No installed projection routes a package that has never had a diagnosis to Piece-3 work.

### P-12 — The Accept transaction is already exactly acceptance-only
`server.py:700-800` calls only `acceptance-offer` (GET) and `record-ness-acceptance` (POST). `record_ness_acceptance()` (`commands.py:7282-7302`) states and enforces "appends exactly ONE `ness_candidate_acceptance_recorded` and no other event of any kind." The real journal confirms it: seq 84 is a single append.

### P-13 — The installed system is already multi-package aware
`authenticated_candidate_custody()` (`nh_loop.py:28191-28210`) returns `{package_scope_id: {...}}`; `Replay(events, package_scope_id)` scopes every projection; `evaluate_interview_clearance(package_scope_id)` is package-scoped and refuses clearance earned on another package (`nh_loop.py:40195-40206`).

### P-14 — The installed next-package result contract already proves what a selection needs *(new in v1_1 — basis of Correction 4)*
`NEXT_PACKAGE_ANALYSIS_REQUIRED_KEYS` (`nh_loop.py:388-413`) is: `classification`, `controller_action`, `package_id`, `package_title`, `package_source_path`, `simple_explanation`, `dependency`, `source_paths_checked`, `whole_check_complete`, `unknowns`.

`validate_next_package_analysis(text, errors, required_files)` (`nh_loop.py:5006`) already proves **all** of:

- strict decoding through `strict_json_loads`, so a duplicated key refuses the whole object rather than resolving to the last value (`:5056-5060`);
- the exact key set, types, and both enums;
- the required classification → action mapping (`:5105-5111`) over `NEXT_PACKAGE_ACTION_BY_CLASSIFICATION` (`:375-384`);
- every reported path resolves to a real permitted repository file, via `validate_source_paths()`;
- **governing-authority coverage**, via `check_required_source_coverage(resolved_paths, required_files, …)` against the controller's own preflight resolution — refusing outright when no controller-resolved authority set was supplied (`:5145-5155`);
- `package_source_path` is required when `controller_action == prepare_claude_task`, is a safe single line, **resolves to that exact same real permitted file** (`resolve_repo_source_path(source_path) != source_path` → refuse), and **appears in `source_paths_checked`** (`:5168-5201`);
- `whole_check_complete` is true.

**The installed root rule, stated exactly — and the boundary v1_9 moves.** The clause above is a faithful description of the **installed** validator, and it stays faithful here: the installed code requires a non-null `package_source_path` **only** when `controller_action == prepare_claude_task`, and its own comment says so — *"Null is permitted ONLY when `controller_action` is not `prepare_claude_task`; when it is, a null refuses rather than letting this controller guess which package was meant."*

**That installed permission is the contradiction v1_9 corrects.** `hold_for_question_validation` is exactly such an action, so the installed contract admits a rootless `genuinely_open_for_ness` result — while §9.3's `SEL-ROOT-IDENTIFIES` requires one exact proved root for **that same route**. The two cannot both hold.

| | Installed contract (described above, unchanged as a description) | **Corrected contract (§9.3a `T1-ACTIONABLE-ROOT`)** |
|---|---|---|
| `prepare_claude_task` | root **required** | root **required** — unchanged |
| `hold_for_question_validation` | root **permitted to be null** | **root REQUIRED and fully proved** |
| `report_settled`, `wait_dependency`, `defer_future`, `defer_build` | root permitted to be null | **unchanged** — no root requirement is invented for symmetry |

The rest of P-14 — the strict decoder, the exact key set, both enums, the classification→action mapping, `validate_source_paths()`, `check_required_source_coverage()` and `whole_check_complete` — is reused **exactly as installed** and is not weakened by the correction. §9.3a states the single strengthened requirement and nothing else.

The installed classification enum is exactly the six-way workflow classification plus one:

| `classification` | `controller_action` |
|---|---|
| `settled` | `report_settled` |
| `mechanically_implied` | `prepare_claude_task` |
| `mechanical_work` | `prepare_claude_task` |
| `waiting_on_another_choice` | `wait_dependency` |
| `genuinely_open_for_ness` | `hold_for_question_validation` |
| `future_non_blocking` | `defer_future` |
| `later_building_or_disk_work` | `defer_build` |

**v1_0's invented `NH_NEXT_PACKAGE_SELECTION_RESULT_V1` was therefore both incoherent with its own reuse claim and unnecessary.** §9 retains the installed contract.

### P-15 — The installed pipeline has an independent task-preparation stage between selection and Claude *(new in v1_1 — basis of Correction 2)*
`run_prepare_next_claude_task()` (`nh_loop.py:7603`) runs STAGE ONE (the `next-package` navigation review) and then, over a re-proved identical source state, **STAGE TWO**: `build_prepare_task_prompt(analysis, decision_binding)` → `run_codex_prepare_task(...)` → `extract_codex_agent_message` → `validate_prepared_task(task_message, analysis, required_files, errors)`.

The stage-two contract is `PREPARE_TASK_REQUIRED_KEYS` (`nh_loop.py:662-703`): `package_id`, `package_title`, **`package_source_path`** (which the code annotates: "THE SAME PROVED SOURCE ROOT THE FIRST STAGE NAMED. `package_title` is model prose, so on its own it let the two independent reviews agree about a name while describing different packages"), `classification`, `task_ready`, `not_ready_reason`, **`target_path`**, `simple_explanation`, `settled_basis`, `source_paths_checked`, `open_items`, **`mechanical_design_specification`**, **`review_signal`**, `whole_check_complete`, `unknowns`.

Around it: four source-state checks (`:8500-8562`); the possible-Ness branch that records a `review_signal_recorded` bound to the **proved root** and prepares no task (`:8586-8630`); the final target-path re-check `is_new_candidate_path(prepared["target_path"])` at the last safe boundary (`:8632-8646`); `finalize_claude_instruction(prepared, decision_binding, selected_scope, errors)` building the instruction from four validated bindings (`:8650-8700`); and a **final clearance re-proof** for the selected scope at the last boundary (`:8702-8720`).

**v1_0 went straight from selection to the Claude write and omitted every one of these.**

### P-16 — The installed durable provider lifecycle and its recovery table already exist *(new in v1_1 — basis of Correction 3)*
`_dispatch()` (`commands.py:790`) is documented as "Prepare, write-ahead, dispatch, observe, classify, custody, terminal": `engine.build_prepared_request` → `append_prepared` → `append_dispatch_begun` → `context.provider.dispatch(request)` → `_observe_and_close` → `append_result_custody` → `append_terminal`.

The custodied result is consumed by a **separate later command**, `process-custodied-provider-result`. For a Claude write, that is `_b6g_correction_apply()` (`commands.py:3180`), which decides what the transaction already did **before** any append and **before** any exclusive create, via `_correction_apply_resumption()` (`commands.py:3038`) and its four boundaries:

| Boundary | Meaning |
|---|---|
| `B0` | nothing of this transaction is durable yet — the ordinary path |
| `B7` | the write-ahead is durable, the candidate is not yet promoted |
| `B8` | the write-ahead is durable and the promoted file holds exactly the bytes it named |
| `B9` | custody is already committed for exactly this transaction |

Its own comment states the property Correction 3 needs: *"The custodied result above is the only input to any of it; no provider is contacted on any of these paths."*

And the installed recovery routing (`commands.py:617-655`) is already exactly the no-redispatch rule:

| Provider phase / evidence | recovery outcome | next |
|---|---|---|
| `none` / `prepared` (never dispatched) | `SAFE_TO_RETRY` | `execute-next-claude-task` |
| `dispatch_begun` / `accepted` (uncertain) | `WAIT` | **`reconcile-provider-request`** |
| … reconciled `absent_proved` | `SAFE_TO_RETRY` | `execute-next-claude-task` |
| … reconciled `lookup_unsupported` | `NEEDS_USER_ACTION` | none |
| … reconciled `found_terminal_result_unavailable` | `NEEDS_USER_ACTION` | none |
| `result_custodied` | `SAFE_TO_RESUME` | **`process-custodied-provider-result`** |
| terminal `result_received` + pending custody | `SAFE_TO_RESUME` | `process-custodied-provider-result` |

### P-17 — The local CLI transport supports no authoritative lookup *(new in v1_1)*
`NhCliProviderTransport.lookup()` (`nh_loop.py:46295-46296`) returns `LookupObservation(outcome="unsupported")`. `_lookup_condition()` (`commands.py:4791-4796`) maps an in-flight unknown with unsupported lookup to `in_flight_unknown_lookup_unsupported`, and `_RECONCILIATION_ROW` (`commands.py:4686-4687`) routes `lookup_unsupported` to row `C1`, dependency code `lookup_unsupported_by_capability_contract`, next state `NEEDS_USER_ACTION`, recovery `NEEDS_USER_ACTION`.

**This is the honest consequence and the design states it plainly:** for the local Claude/Codex CLI, an uncertain dispatch cannot be resolved by lookup, so it becomes a named practical action for a person — never a silent second call.

### P-18 — `_supervisor_candidate_file()` imposes no candidate-grammar requirement *(new in v1_1)*
`nh_loop.py:46521`-region helper: it requires a safely repository-relative path, no symlinked component, readability, `≤ MAX_CANDIDATE_BYTES` (8 MiB, `constants.py:53`), and an exact byte-length and SHA-256 match against the authenticated identity. **It does not require the path to be a candidate.** This is what makes §8.9's transitional binding possible without weakening anything.

### P-19 — Unverifiable custody is already a fail-closed safety hold, not a reason to re-ask *(new in v1_2 — basis of Blocker 1)*
`process_custodied_provider_result()` re-reads and re-verifies the saved bytes at boundary **B6c** via `engine.custodied_bytes(context, custody)` (`commands.py:2123`), which raises unless the re-read payload matches both the recorded `result_byte_length` and the recorded `result_sha256` (`engine.py:935-946`). On that refusal the controller records the dependency code `provider_result_custody_unverifiable` and completes the operation with `"safety_hold"` (`commands.py:2124-2147`), returning `recovered_workflow_state = "SAFETY_HOLD"` with the plain-language meaning:

> "N.H could not re-verify the exact bytes it had already saved, so it stopped rather than asking the model again."

The dependency table classifies that code as `authority_or_safety_conflict` / `work_item_bound` / `no_retry_fail_closed` / `manual_safety_review` → `SAFETY_HOLD` (`dependency.py:142-144`, row `C17` at `dependency.py:305-306`), carried on `supervisor_operation_completed`.

**v1_1's Row K contradicted this** by treating an unavailable custodied result as grounds to abort the pending candidate intent and return toward a fresh design run. §14.6 corrects it.

### P-20 — Strong Claude result checks exist only for `correction_apply` *(new in v1_2 — basis of Blocker 2)*
`_validate_result()` (`commands.py:1056-1072`) routes `design_audit` to `auditresult.check_schema_valid()`, `correction_apply` to `_claude_admission_checks()`, and `acceptance_explanation_content` to `_acceptance_explanation_admission_checks()`. **Every other work-item kind falls through to `_generic_result_schema(prepared, value)` alone.**

`_claude_admission_checks()` (`commands.py:1089-1136`) recomputes K1–K8 from the custodied bytes: K1 exact key set over `CLAUDE_RESULT_KEYS` plus schema id/version; K2 produced path equals `work_item["target_candidate_path"]`; K3 filename succession against the predecessor candidate; K4 base64 decodes and the declared length is an integer within `MAX_CANDIDATE_BYTES` equal to the decoded length; K5 declared digest equals `sha256_hex(payload)`; K6 the round triple equals the authorized triple; K7 the correction specification digest and blocking finding refs equal the work item's; K8 subsumed by K5.

**K3, K6 and K7 are correction-specific** — an initial design has no predecessor candidate, no authorized correction round, and no correction specification — so the contract cannot be reused unchanged. §14.5 states the initial-design contract.

### P-21 — The replay closure map has no row for the new read-only kinds *(new in v1_2 — basis of Blocker 3)*
`Replay.custodied_results_awaiting_processing()` (`replay.py:319-332`) keeps every `provider_result_custody_recorded` pending until `_downstream_recorded()` proves its work-item-specific downstream effect. `_downstream_recorded()` (`replay.py:333-…`) maps: `design_audit` → `mechanical_audit_recorded` / `mechanical_audit_unusable_recorded`; `correction_specification` → `correction_specification_recorded`; `correction_apply` → `diagnosis_strategy_consumption_completed` / `…_terminated` / `mechanical_no_progress_recorded` / `candidate_custody_recorded`; `change_explanation_review` and `acceptance_explanation_content` → `mechanical_change_explanation_recorded`; `question_validation` and `coverage_review` → `piece3_provider_work_recorded`; and `.get(kind, ())` for anything unmapped. A `result_invalid` terminal closes the custody by itself.

The comment on the `acceptance_explanation_content` row states the exact hazard: *"Without this row the custody of a processed preparation result would never be proved closed and the loop would re-enter processing forever."*

**`next_package_selection` and `next_design_task_preparation` have no row.** §7.6a specifies the rule.

### P-22 — Recovery binds the current package before it discovers the operation *(new in v1_2 — basis of Blocker 4)*
Three facts, read from the installed code:

1. `command_supervisor(name)` (`nh_loop.py:46425-46446`) calls `build_supervisor_context(errors)` **first** — which binds the CURRENT package — and only afterwards reads the stdin envelope.
2. `supervisor_operation_status(context, request)` (`commands.py:274-278`) receives that already-built context and constructs `Replay(events, context.binding.package_scope_id)` **before** it looks at `request["supervisor_operation_id"]`.
3. `process_custodied_provider_result(context)` (`commands.py:2059-2071`) takes **no envelope at all** — `STDIN_ENVELOPE_SUPERVISOR_COMMANDS` is only `supervisor-operation-status`, `record-semantic-scope-unlock`, `record-ness-acceptance` (`constants.py:1120-1123`) — and selects its work from `situation.pending_custody`, which is likewise scoped to the current package.

Therefore, while accepted package P remains current, a transition operation or a pending transition custody under Q is **invisible to recovery**. `reconstruct_original_envelope()` (`commands.py:204-240`) is the right discipline and is genuinely "the SOLE authority for every original envelope field" — but it runs after discovery, so it cannot solve discovery. §8.9 specifies the bootstrap order.

### P-23 — The generic result schema and the installed contracts are mutually exclusive *(new in v1_4 — basis of Correction 1)*
`_generic_result_schema(prepared, value)` (`commands.py`, immediately below `_validate_result`) requires exactly three things of any work-item kind that has no dedicated branch:

```
value["result_schema_id"]      == prepared.result_schema_id
value["result_schema_version"] == constants.RESULT_SCHEMA_VERSION
value["whole_check_complete"]  is True
```

The installed **next-package** contract `NEXT_PACKAGE_ANALYSIS_REQUIRED_KEYS` (`nh_loop.py:388-413`) carries `whole_check_complete` but **not** `result_schema_id` and **not** `result_schema_version`. The installed **prepared-task** contract `PREPARE_TASK_REQUIRED_KEYS` (`nh_loop.py:662-703`) is the same: `whole_check_complete`, no lifecycle keys.

And both installed validators refuse on an **exact** key set: `validate_next_package_analysis()` decodes through `strict_json_loads` and rejects any object whose key set differs, and `validate_prepared_task()` holds `PREPARE_TASK_REQUIRED_KEYS` the same way. **So the two requirements are mutually exclusive**: a result that satisfies the installed contract fails `_generic_result_schema()`, and a result carrying the two lifecycle keys to satisfy it is refused by the installed validator.

The consequence is precise and fatal to v1_3 as written: merely registering `next_package_selection` and `next_design_task_preparation` as work-item and provider kinds means a **valid** review result is classified `result_invalid` at B6d, receives an invalid terminal, consumes bounded output-retry budget, and **never reaches** the `SEL-ADMISSION` or prepared-task re-admission that v1_3 relies on. §9.5a and §13.6a correct it.

### P-24 — The two installed Piece-3 commands make blind, non-durable provider calls *(new in v1_4 — basis of Correction 2)*
`command_question_validation()` builds its prompt and then calls `run_codex_question_validation(prompt, errors)` (`nh_loop.py:41907`, definition at `:38929`), which is a direct `subprocess.run(["codex", "exec", …])`. `command_question_coverage_review()` does the same through `run_codex_question_coverage_review()` (`nh_loop.py:42744`, definition at `:39223`). Each then re-reads the source binding, compares it to the pre-call value, extracts the agent message, validates the payload, and appends its Piece-3 event.

**Neither path appends `provider_request_prepared`, `provider_dispatch_begun`, `provider_result_custody_recorded` or `provider_request_terminal_recorded`.** A crash after the request left the machine but before the durable append therefore leaves nothing to reconcile against, and the only way forward is a second model request for the same stage.

**And there is a second, sharper consequence.** `append_interview_event()` calls `supervisor_piece3_authorization_gate()` (`nh_loop.py:32481`, definition `:32309`), which refuses a supervisor-era `validation_recorded` or `question_coverage_review_recorded` unless replay proves an unconsumed `piece3_provider_work_recorded` carrying `result_schema_valid: true`. That authorization is produced **only** by `_b6f_piece3()` (`commands.py:4164-4192`) from a **custodied** `question_validation` or `coverage_review` provider result. The real journal is already supervisor-era — its 84 events are journal versions 4, 5 and 6, and `is_supervisor_era_version()` admits 5 and above (`replay.py:114-126`).

So for a newly selected package Q the two halves are not merely *better* wired together — **they must be**: the durable supervisor dispatch is what makes the authorization, and the authorization is what makes the Piece-3 append legal. v1_3 described both halves and never joined them. §12.3 corrects it.

### P-25 — The real supervisor prompt tells every provider to emit the two forbidden keys *(new in v1_5 — basis of Correction 1)*
`_supervisor_provider_prompt(material)` (`nh_loop.py:45974`) renders **one generic instruction for every supervisor provider kind**. Its second paragraph says, verbatim:

> "Return exactly one JSON object and no prose or code fence. It must **use `result_schema_id` and `result_schema_version` from the material**, set `whole_check_complete` to true where that field belongs, and satisfy the exact result contract implemented in `controller/nh_supervisor/auditresult.py` and `controller/nh_supervisor/commands.py`."

The only per-kind variation is an acceptance-explanation preamble. It is the input to all three transport branches (`nh_loop.py:46135`, `:46172`, `:46234`).

**That instruction is incompatible with the contracts v1_4 correctly chose.** `NEXT_PACKAGE_ANALYSIS_REQUIRED_KEYS` and `PREPARE_TASK_REQUIRED_KEYS` are **exact**-key contracts carrying neither lifecycle key, and their validators refuse any extra key. So a model obeying the prompt produces a reply the validator must reject, and a model obeying the contract disobeys the prompt.

**A dedicated B6d validator cannot fix this**, because the defect is upstream of validation: the provider was *instructed* to malform the object. §9.5b corrects the rendering.

### P-26 — The `extra_inputs` seam exists in the engine and is unwired at both ends *(new in v1_5 — basis of Correction 2)*
`engine.build_prepared_request(...)` (`engine.py:642`) **already accepts `extra_inputs=None`** and already threads it into `required_inputs_sha256(context, work_item_obj, extra_inputs)`. The plumbing exists. What does not exist is its use:

- `commands._dispatch(...)` (`commands.py:790`) accepts `extra_prompt` and **not** `extra_inputs`, and calls `build_prepared_request(..., extra_prompt=extra_prompt)` with no inputs extra;
- `nh_loop._supervisor_provider_material(context, request, errors)` (`:45687`) reconstructs `required_inputs_inventory(context, work_item)` with **no extra at all**, while reconstructing the prompt inventory *with* `context._current_prompt_extra`.

So v1_4's `SEL-AUTHORITY-BINDING-CARRIED` described a binding the installed call path can neither produce at dispatch nor re-prove at render. **The correction is therefore smaller than it first appears** — one parameter through one existing call, plus the matching reconstruction — and §9.5c states it exactly.

**One installed fact makes the equality rule easy and is worth naming:** `_supervisor_provider_material()` already recomputes **both** digests and refuses before a byte leaves the machine when either differs from the durable prepared record:

> `if prompt_digest != request.prompt_material_sha256 or required_digest != request.required_inputs_sha256: … "the rendered provider material does not match its durable digest"`

That is precisely the reconstruction-equality mechanism §9.5c needs; it does not have to be invented.

### P-27 — T2 would send the generic prompt and admit the wrong contract *(new in v1_5 — basis of Correction 3)*
The installed supervisor transport renders `_supervisor_provider_prompt(material)` for `gpt_question_validation` and `gpt_question_coverage_review` exactly as for every other kind — **not** `build_question_validation_prompt(...)` (`nh_loop.py:38701`) and **not** `build_question_coverage_review_prompt(binding_block)` (`:39206`).

And `_validate_result()` leaves both Piece-3 kinds on `_generic_result_schema()`, while the real payload contracts are exact-key sets that carry neither lifecycle key:

| Contract | Keys |
|---|---|
| `QUESTION_VALIDATION_REQUIRED_KEYS` (`nh_loop.py:21495`) | `package_id`, `package_title`, `whole_check_complete`, `enumeration_complete`, `source_paths_checked`, `page_index`, `page_count`, `total_issue_count`, `issues`, `unknowns` |
| `COVERAGE_REVIEW_REQUIRED_KEYS` (`nh_loop.py:24094`) | `whole_check_complete`, `coverage_review_complete`, `source_paths_checked`, `possible_gaps`, `unknowns` |

`validate_question_validation_payload()` (`:37519`) and `validate_question_coverage_review()` (`:39585`) both compute `missing`/`extra` against those exact sets (`:37569-37570`, `:39671-39672`), so a lifecycle key is refused as an extra key.

**Consequence:** as v1_4 stood, the custodied supervisor result could not be the same exact Piece-3 reply that the provider-free commit claims to re-validate — it would be a generic supervisor answer to a generic supervisor question. §12.3a and §12.3e correct it.

### P-28 — T2 position A has no usable command, and the custody bootstrap looks only for `initial_design` *(new in v1_5 — basis of Correction 4)*
Two concrete routing contradictions in v1_4:

**(a)** `main()` (`nh_loop.py:46531-46534`) dispatches `question-validation` and `question-coverage-review` **directly** to `command_question_validation()` and `command_question_coverage_review()`, **before** the `SUPERVISOR_COMMAND_SET` fallthrough, and that is true under `NH_SUPERVISOR_WORKER=1` as well. v1_4 correctly requires those public commands to keep their ordinary direct behaviour — so the continuation **cannot** use those names for a durable supervisor dispatch, and v1_4's loop table left position A as the placeholder `<durable piece3 dispatch>` with no settled command.

**(b)** *[historical description of the v1_4 defect; §8.9.2 has since been corrected to the closed set of §12.3c / §8.9.4 Path B.]* As v1_4 stood, `TB-CUSTODY-BOOTSTRAP` located "exactly one unfinished `initial_design` custody". A pending `question_validation` or `coverage_review` custody for Q therefore could not be discovered at all while P remained current — T2 position B was unreachable.

§12.3c and §8.9.2 correct both.

### P-29 — Q's transition binding was circular on the validation it creates *(new in v1_6 — basis of Correction 1)*
`build_supervisor_context()` (`nh_loop.py:46308`) can construct a `PackageBinding` only from an authenticated package-bound `validation_recorded` (§5 P-3), and v1_5 derived Q's transition binding from exactly that event: scope, key, id, branch, head, source binding, manifest, **`validation_set_id`** and standing.

But the continuation order is **T1 selects Q → T2 question-validation for Q → Q's first `validation_recorded`**. The binding v1_5 requires for the T2 dispatch is produced *by* that dispatch's own commit. **It is circular**, and the first Piece-3 operation of every new package would have had no binding to run under.

v1_5's `TB-BOUNDED-USE` compounded it by naming only "`prepare-next-design-task`, `execute-initial-design`, the T5 consumption, and their recovery" as permitted users of the transition binding — while §12.3 simultaneously required T2 to run under a Q context. §8.9 and §8.10 correct both.

### P-30 — The three new work-item kinds have no identity-matrix rows *(new in v1_6 — basis of Correction 2)*
`identity.WORK_ITEM_MATRIX` (`identity.py:106-292`) holds eleven rows keyed by `(work_item_kind, variant)`. `check_work_item_object()` (`:308-395`) resolves the row and, when none exists, returns:

> `"no Section 4.4 matrix row exists for (%s, %s): the combination fails closed"`

and `work_item_identity()` (`:396-401`) raises `IdentityError` on any check failure. **There is no row for `next_package_selection`, `next_design_task_preparation` or `initial_design`**, so all three would be unbuildable and every continuation dispatch would fail closed at identity derivation. §9.5d, §13.6c and §14.5b state the exact rows.

`WORK_ITEM_KEYS` (`:44-66`) is a fixed 21-key set; keys 1–7 are always required non-null, and the remaining fourteen are governed per row by the vocabulary `R` (non-null), `0` (must be null), `[]` (must be the empty list) and `N` (non-empty, sorted, unique).

### P-31 — The installed Piece-3 rows cannot express a first-package clearance *(new in v1_6 — basis of Correction 3)*
Both installed Piece-3 rows are identical in the three fields that matter:

```
("question_validation", None)   routed_signal_refs = N   validation_set_id = R   piece3_standing_sha256 = R
("coverage_review",     None)   routed_signal_refs = N   validation_set_id = R   piece3_standing_sha256 = R
```

and `engine.piece3_work_item(context, candidate, kind)` (`engine.py:337-342`) copies all three straight from the binding:

```
obj["routed_signal_refs"]     = sorted(set(context.binding.routed_signal_refs))
obj["validation_set_id"]      = context.binding.validation_set_id
obj["piece3_standing_sha256"] = context.binding.piece3_standing_sha256
```

That is correct for the route it was built for — a package already under interview, with routed signals and a prior validation set. **It cannot represent the automatic clearance of a freshly selected mechanical package**, which truthfully has **zero routed signals** and **no prior `validation_set_id`**, while having a controller-proved root and scope and a real current standing and source state.

The installed **direct** `question-validation` command already supports a package before its first validation — `controller_held_question_validation_package()` exists precisely for that (§13.2). **That capability must not be destroyed by manufacturing fake supervisor fields**, and §12.3g adds controlled variants instead.

### P-32 — `claude_initial_design` would be dispatched to Codex *(new in v1_6 — basis of Correction 4)*
`NhCliProviderTransport.dispatch()` (`nh_loop.py:46069-46084`) branches explicitly and then falls through:

```
if request.provider_kind == "claude_correction":              return self._dispatch_claude(...)
if request.provider_kind == "claude_acceptance_explanation":  return self._dispatch_claude_acceptance_explanation(...)
return self._dispatch_codex(request, material)
```

and `SUPERVISOR_CLAUDE_PROVIDER_KINDS` (`nh_loop.py:45643-45646`) contains exactly those two kinds, so `supervisor_endpoint_binding()` maps every other kind — including `claude_initial_design` — to `SUPERVISOR_CODEX_ENDPOINT`.

**Both halves therefore agree on the wrong answer**: the endpoint check `request.provider_endpoint_identity != expected_endpoint` would pass, and the initial design write would be sent to Codex. §14.7 wires it explicitly.

### P-33 — An actionable T1 result can be validly received and impossible to route *(new in v1_9 — basis of Corrections 1 and 2)*

This finding was not derived from reading code alone. **It was reached by execution, on the real authenticated journal, and its evidence is preserved at `event_seq 85`–`90` (§3.4).**

**(a) The two accepted statements that cannot both hold.**

1. **P-14 / the installed contract.** A T1 result whose `controller_action` is `hold_for_question_validation` may carry `package_source_path = null`, and the installed `validate_next_package_analysis()` returns **OK with zero errors** for it. The accepted design records this permission correctly.
2. **§9.3 `SEL-ROOT-IDENTIFIES`.** A package entering **either** mechanical continuation **or** possible-Ness Piece-3 validation requires the controller to hold **one exact proved package source root** — and the accepted design states, in the very next sentence, that the `genuinely_open_for_ness` route needs one *"as much as the mechanical one"*, because `review_signal_recorded` binds to `scope_root_path` and *"a Ness route with no proved root has nothing to bind to and must refuse."*

**(b) The mechanical consequence.** A rootless `genuinely_open_for_ness` result is therefore, under the accepted design simultaneously:

- **validly received** — it passes the installed validator, receives a valid `result_received` terminal, and is custodied as usable bytes; and
- **impossible to admit or route** — `SEL-ADMISSION` cannot prove a root, `SEL-ROOT-IDENTIFIES` refuses the Ness route without one, and `review_signal_recorded` has no `scope_root_path` to bind to.

**A result the controller must accept and can then do nothing with is a mechanical dead end, and an accepted design that produces one has an internal contradiction. This is IMPORTANT, not cosmetic.**

**(c) What it is not.** It is **not** provider uncertainty — the request completed and has a durable `result_received` terminal. It is **not** lost or unverifiable custody — the saved bytes re-verify exactly. It is **not** a corrupt or malformed reply — it is schema-valid under the contract it was produced against. It is **not** a selector failure — the selector used a permission the design granted. **None of the installed recovery, reconciliation or safety-hold routes is the right answer to it, because none of them is describing this condition.**

**(d) What must NOT be done about it, and why each is refused here.**

| Tempting resolution | Why it is refused |
|---|---|
| Relax the append guard so a null `scope_root_path` is acceptable when `package_id` is a real controlled id | It weakens an installed safety rule so that a signal the controller cannot place in one package is recorded anyway. `SEL-ROOT-IDENTIFIES` exists precisely to prevent that, and the fix would trade a mechanical contradiction for a scoping hazard. |
| Derive the root — or `source_evidence` — from `source_paths_checked` by matching `package_id` or a name | It makes **model-supplied prose operative as a path selector**, which every rule in §9.3 and `SEL-ADMISSION` proof 10 forbids. It also **manufactures evidence** the review never stated. |
| Treat the preserved result as uncertain, lost, or corrupt and re-dispatch its request identity | All three are factually false (c), and re-dispatch of a completed request identity is exactly what `PROV-NO-REDISPATCH` forbids. |
| Delete, rewrite, or re-head the preserved result so the condition disappears | It destroys truthful authenticated history to make a contradiction invisible. |

**(e) The corrections it requires.** Exactly two, and they are the smallest pair that removes the contradiction without weakening anything: **§9.3a `T1-ACTIONABLE-ROOT`** makes the contract require a proved root for **both** actionable actions, so this shape can never be validly received again; and **§9.7 `SEL-LEGACY-CONTRACT-REPLACEMENT`** states the one bounded, deterministically-consumed rule by which an already-completed earlier-contract result that is non-operative under the strengthened contract is preserved as history while the loop takes **one** fresh current-contract selection under a **new** request identity.

### P-34 — The T1 invalid-output exhaustion route named a command that cannot exist for T1 *(new in v1_10 — basis of the v1_10 correction)*

This finding, like P-33, was **not derived from reading a design alone. It was reached by execution** — by a disposable implementation correction built against the accepted v1_9 design, outside the live controller, installing nothing (§3.5).

**(a) What the accepted v1_9 design gets right, and which this file preserves without exception.** A current-contract actionable rootless T1 result is **invalid output**; it receives a `result_invalid` terminal; the **installed bounded output-retry budget** governs it; retries are therefore **bounded**; **no new selector identity** may be opened endlessly; the **earlier-contract one-shot permission stays consumed**; provider uncertainty remains **reconciliation-first**; retry exhaustion **must stop honestly**; there are **exactly seven** continuation execution commands; and **`close-open-consumption` is not one of those seven.** Every one of those statements is correct, is settled, and is carried forward unchanged.

**(b) The one statement that cannot hold.** v1_9 then says, in §9.5a `SEL-B6D-ACTIONABLE-ROOT-IS-INVALID-OUTPUT`, in §9.6's honest-stop list, in §9.7.4's consumption-fence table, in §9.7.4's `SEL-LEGACY-NO-LOOP` point 4, in §14.3's restart table, and in §25's `R107` position (e), that when the bounded output-retry budget is exhausted the route is `close-open-consumption`.

**(c) Why that is mechanically impossible.** The installed `close_open_consumption()` is **not** a generic "close any provider failure" operation:

| What the installed command actually requires | What a T1 `next_package_selection` review actually has |
|---|---|
| an **open `diagnosis_strategy_consumption_started`** transaction for the work item, reported by the installed consumption reconciliation as `open_requires_closure` | **none** — a navigation review opens no consumption |
| a **consumption identity** and its started-event sequence | **none** |
| a **diagnosis event sequence, diagnosis event digest and diagnosis strategy digest** | **none** — T1 has no diagnosis authority (`WIM-SELECTION` pins every one of those fields to `0`, §9.5d) |
| a **strategy novelty key** and **blocking finding references** | **none** — `blocking_finding_refs` is `[]` because nothing has been audited |
| a **correction specification digest** | **none** — correction-only authority, never placed on a non-correction work item |
| its append of **`diagnosis_strategy_consumption_terminated`**, carrying all of the above | **nothing truthful to put in it** |

The installed command therefore **refuses** — *"no unclosed consumption with a proved final outcome exists"* — and that refusal is correct behaviour, not a bug to be worked around.

**(d) What must NOT be done about it, and why each is refused here.**

| Tempting resolution | Why it is refused |
|---|---|
| Create a `diagnosis_strategy_consumption_started` for the T1 work item so the command becomes callable | It **fabricates authority and state**. There was no diagnosis, no strategy, no correction specification and no blocking finding; inventing the transaction to satisfy a command is exactly the manufactured evidence every rule in §23 and §28 forbids. |
| Weaken `close_open_consumption()` into a generic provider-terminal closer | It would let a navigation review's failure close, or appear to close, the correction machinery's real transactions — and it would strip the meaning out of the one command whose whole purpose is that a genuine consumption was genuinely terminated. |
| Add `close-open-consumption` as an **eighth** continuation execution command | It contradicts the accepted closed seven-command set (§7.5, §20.2, §24.8), **and it still would not create the missing diagnosis consumption** — the command would refuse exactly as before. The count is not the obstacle; the absent transaction is. |
| Dispatch one more selector request "to close things out" | The condition is precisely that the bounded budget is **exhausted**. Another request on the exhausted condition is the unbounded retry the accepted design exists to prevent (§9.7.4 `SEL-LEGACY-NO-LOOP`). |
| Let the loop fall through to `LOOP_SELECTION_REQUIRED` / `continue-design-loop` and rediscover the exhaustion each time | It is not a stop at all. It re-enters a command that can do nothing, for ever, and reports a position that is not the truth. |

**(e) What it is not.** It is **not** provider uncertainty — the request has a durable terminal. It is **not** lost or unverifiable custody — that is §9.6b, and it outranks this position. It is **not** the §9.7 earlier-contract condition — that requires validity **under a contract no longer in force**, which a currently-refused reply has never had (`SEL-LEGACY-NOT-A-NEW-LEGACY`). It is **not** a B9 question — B9's retry values, its exhaustion meaning and its real-change meaning are untouched here.

**(f) The correction it requires.** Exactly one, and it is the smallest object that removes the contradiction without weakening anything: **§9.6a `T1-INVALID-OUTPUT-EXHAUSTION-STOP`** states what actually happens when the installed bounded T1 output-retry budget is exhausted — the honest stop at `LOOP_NEEDS_USER_ACTION` with a null next command, re-derived from durable evidence, restart-stable, owing no append, owing no `close-open-consumption`, inventing no consumption, no event type, no store and no eighth command. **The legitimate installed use of `close-open-consumption` for the diagnosis/correction machinery is preserved and named, not deleted** (`T1-NOT-A-CONSUMPTION`).

### P-35 — The T4 exhaustion stop was stated correctly and never wired *(new in v1_11 — basis of the v1_11 correction)*

P-34 corrected the impossible `close-open-consumption` route for T1, and §14.3 `INIT-EXHAUSTION-IS-NOT-A-CONSUMPTION` corrected it for T4 as the same single contradiction appearing at the second work-item kind. **The T1 half was wired. The T4 half was not.**

**(a) What v1_10 states, correctly, and which this file preserves without exception.** §14.3 says that once the installed bounded output-retry budget for `claude_initial_design` is exhausted: no further initial-design request is dispatched on the exhausted condition; `close-open-consumption` is **not** owed; no `diagnosis_strategy_consumption_started` and no `diagnosis_strategy_consumption_terminated` is invented; the position is `LOOP_NEEDS_USER_ACTION` with a null `loop_next_command`; **zero** further Claude or provider calls occur on that exhausted condition; the position is **restart-stable**; and every durable request, terminal, custody and operation record is preserved. **That meaning is settled and is not redesigned here.**

**(b) What v1_10 never does.** It never carries that fact anywhere a machine could consume it:

| Where the fact would have to live | v1_10 |
|---|---|
| `post_acceptance_transition_state()` derived-field inventory (§17.2) | **absent** — the T1 pair `t1_custody_unverifiable` / `t1_output_retry_exhausted` exists; there is **no** T4 counterpart |
| `loop_status()` precedence (§7.4) | **absent** — two T1 guards exist before `t.selection is None`; there is **no** guard before the T4 fall-through |
| §18 restart matrix | **absent** — Row I covers prepared / dispatched / uncertain and sends the reader to "the §14.3 table in full"; no row states the exhausted restart position |
| §24.1 / §24.5 implementation map | **claims** the exhausted T1 **and T4** positions are read-only derivations — a claim only half-backed, because no T4 field or guard is specified anywhere |

**(c) The mechanical consequence.** §17.2 defines `initial_result_custody` as *the newest completed, custodied `claude_initial_design` terminal whose bytes re-verify **and** pass all ten `INIT-ADMISSION` checks re-run now.* A run of `result_invalid` terminals produces **no** such custody. So at the exhausted position the derivation reaches:

```
    if t.initial_result_custody is None:     return LOOP_INITIAL_DESIGN_REQUIRED,
                                                    execute-initial-design
```

and returns `execute-initial-design` — **against a budget that is already spent, on every entry and every restart, for ever.** An implementer following §14.3 stops honestly; an implementer following §7.4 and §17.2 does not. **Two parts of one accepted-track design describe two different systems, and the executable half is the wrong one.**

**(d) What it is not.** It is **not** a disagreement about what should happen — §14.3 already says what should happen, and this file agrees with it exactly. It is **not** a B9 question: no retry value, count, timer, wait, backoff, deadline, real-change rule, episode meaning or exhaustion meaning moves. It is **not** a reason to disable bounded retry: **while the budget remains available, ordinary installed T4 retry and recovery semantics must continue unchanged.** It is **not** a licence to add a loop state, an event type, a state store, an eighth command, or a second retry calculator. And it is **not** the T1 defect again — T1 was wired in v1_10 and is untouched here.

**(e) What must NOT be done about it, and why each is refused here.**

| Tempting resolution | Why it is refused |
|---|---|
| Store an "exhausted" flag, marker or counter on the transition, or in a new journal field | It is a **second source of truth** for something the durable record already proves, and it would not survive a restart honestly. The installed budget is the counter; nothing else may be. |
| Write a second retry calculator for T4 | The installed `bounded_output_retry_budget()` already governs this work item and episode, and the installed recovery table already consults it. A second calculation could disagree with the first, and then neither would be trustworthy. |
| Make `initial_result_custody` non-`None` for an invalid terminal so the fall-through stops firing | It would make an unusable result look like an admitted one, and `INIT-ADMISSION` exists precisely to prevent that. **Never** relax an admission proof to fix a routing gap. |
| Let `execute-initial-design` itself refuse when the budget is spent | The refusal would be truthful but the **reported position** would still be `LOOP_INITIAL_DESIGN_REQUIRED`, so the loop would keep selecting a command that can only refuse — the same "stop that is really a loop" §9.6a part E already forbids for T1. The projection must tell the truth **before** a command is chosen. |
| Add a new loop state for "T4 exhausted" | §9.6c already settled that this family of stops reports through the existing `LOOP_NEEDS_USER_ACTION`. A new state would be a second vocabulary for one meaning. |

**(f) The correction it requires.** Exactly one, and it is the smallest object that closes the gap without changing any settled meaning: **one derived field, `initial_design_output_retry_exhausted` `[proposed]` (§17.2), and one guard consuming it in the §7.4 precedence before the `execute-initial-design` fall-through** — plus the restart-matrix, implementation-map and rehearsal text that makes the document describe **one** mechanically executable rule (§14.3, §18 Row I, §24.1, §24.5, §25 `R115`). **The meaning §14.3 already states is preserved verbatim in substance; only its wiring is added.**

---

## §6 — PACKAGE-TERMINAL VERSUS LOOP-CONTINUING

### 6.1 Two different questions

| Question | Answered by | Binding |
|---|---|---|
| "What is the next safe command **for this package**?" | the installed package-bound projection | the **current-package binding** |
| "Does the **overall design loop** have a next package, and where is its transition?" | the loop-level projection `[proposed]` (§7.3) | the **transition binding** (§8.9) |

### 6.2 What stays exactly as installed

`ACCEPTED_FOR_DESIGN_ONLY` remains terminal for the accepted package — `next_command` stays `None` for that binding forever. `acceptance_truth` remains the governed three-way classification and `PROVED_ACCEPTED` remains permanent. `acceptance_required` remains derived from `READY_FOR_ACCEPTANCE`, with no second source of truth. Precedence 11.5 keeps its position. The Accept GET and POST remain acceptance-only.

### 6.3 What becomes true

> `ACCEPTED_FOR_DESIGN_ONLY` is no longer the permanent terminal of the overall worker. It becomes the one and only precondition under which a separate, bounded, loop-level continuation may begin — after acceptance is durably committed and **freshly re-proved**.

"Freshly re-proved" means, at every continuation boundary, all of:

1. a fresh authenticated `supervisor-status` whose `journal_authentication_proved` is true;
2. `acceptance_truth == PROVED_ACCEPTED`;
3. `workflow_state == ACCEPTED_FOR_DESIGN_ONLY`;
4. that report's `authenticated_event_seq` and `authenticated_tail_sha256` matching the journal the continuation then opens under the lock;
5. `authenticated_state_current` true.

Any failure means the continuation does not begin, nothing is appended, and the worker waits. **Continuation is never inferred from the absence of a reason to stop.**

---

## §7 — THE POST-ACCEPTANCE STATE MACHINE

### 7.1 The acceptance transaction — unchanged, and fenced

**Hard invariant `INV-ACCEPT`.** The `acceptance-offer` GET and `record-ness-acceptance` POST remain exactly what the accepted acceptance design (v1.15) specifies and what the installed controller does today. The Accept request must never select a package, invoke Claude, invoke Codex, prepare/dispatch/reconcile any provider request, append any event other than the one designed acceptance append (or, on a refusal, the one designed refusal record through the pre-existing carrier), start or establish another package, create or write-ahead any candidate, perform any Git operation, or perform integration, adoption, closure or implementation.

**No continuation code path may be reachable from the acceptance request** — a structural rule, not a runtime check: the continuation entry points in §24 must not be callable, directly or transitively, from `acceptance_offer()` or `record_ness_acceptance()`. Rehearsal R1 proves it.

### 7.2 The eight positions — corrected

v1_0 had five phases and went from selection straight to the Claude write. The corrected machine has eight, and the two new ones (T3, T4) are Corrections 2 and 3.

```
  T0  ACCEPTED_TERMINAL
        package P accepted, durable, freshly proved (§6.3)
         |
  T1  SELECTION
        ONE bounded read-only next-package review over current sources
        durable completion: a custodied, schema-valid selection result whose
        controller admission proof passes in full (§9.5)
         |
  T2  PACKAGE CLEARANCE
        Piece-3 question-validation + independent coverage review for Q
        durable completion: evaluate_interview_clearance(scope_Q) unlocked
         |
  T3  TASK PREPARATION                                      <-- CORRECTION 2
        ONE bounded read-only design-specification review over the SAME
        already-durable selection -- never a re-run of T1
        durable completion: a validated prepared task carrying the same proved
        root, a selectable classification, task_ready, an exact
        controller-validated NEW target candidate path, a validated
        mechanical_design_specification, a proved settled basis and source
        coverage, no review_signal, and a controller-constructed instruction
         |
  T4  INITIAL CLAUDE EXECUTION                              <-- CORRECTION 3
        ONE bounded Claude design run in a disposable copy of the frozen
        committed source, dispatched through the installed durable lifecycle:
           provider_request_prepared
        -> provider_dispatch_begun
        -> provider_result_custody_recorded
        -> provider_request_terminal_recorded
        durable completion: a custodied Claude result that passes the FULL
        §14.5 initial-design admission contract -- NOT merely a schema-valid
        one -- carrying the produced candidate identity and bytes
         |
  T5  CANDIDATE TRANSACTION
        candidate_write_ahead_recorded
        -> exclusive no-overwrite promotion
        -> anchored read-back
        -> candidate_custody_recorded
        consuming ONLY the custodied T4 bytes
         |
  T6  HANDOFF
        Q's establishment is complete under §8.4; the current-package binding
        moves from P to Q
         |
  T7  SUPERVISOR OWNERSHIP
        ordinary installed loop on Q: fresh audit, correction, diagnosis,
        recovery, PASS, acceptance offer
```

**T3 never re-runs T1.** The task-preparation stage consumes the exact already-durable, controller-proved selection. **T5 never re-runs T4.** The candidate transaction consumes the exact custodied Claude bytes.

### 7.3 The loop-level projection

`loop-status` `[proposed]` is a read-only controller command: it appends nothing, writes nothing, calls no provider, holds no lock beyond the ordinary authenticated read. It returns one `loop_state` `[proposed]` and at most one `loop_next_command` `[proposed]`:

| `loop_state` `[proposed]` | `loop_next_command` `[proposed]` | Position |
|---|---|---|
| `LOOP_NOT_APPLICABLE` | `null` | the current package is not terminal-accepted; the ordinary projection governs |
| `LOOP_SELECTION_REQUIRED` | `continue-design-loop` `[proposed]` | T0 → T1 |
| `LOOP_PACKAGE_CLEARANCE_REQUIRED` | `dispatch-piece3-provider-review` `[proposed]` | T2.a position A (§12.3c.A) — inventory absent/incomplete and no Q-scoped request made; the command derives the owed stage itself |
| `LOOP_COVERAGE_REVIEW_REQUIRED` | `dispatch-piece3-provider-review` `[proposed]` | T2.b position A — inventory complete, review not, and no Q-scoped request made |
| `LOOP_PIECE3_RESULT_PENDING` `[proposed]` | `process-custodied-provider-result` | T2 position B — a valid Piece-3 custody awaits its authorization |
| `LOOP_PIECE3_COMMIT_REQUIRED` `[proposed]` | `commit-piece3-provider-result` `[proposed]` | T2 position C — the scope-matched authorization exists and the Piece-3 event is still owed |
| `LOOP_TASK_PREPARATION_REQUIRED` | `prepare-next-design-task` `[proposed]` | T3 |
| `LOOP_INITIAL_DESIGN_REQUIRED` | `execute-initial-design` `[proposed]` | T4 |
| `LOOP_INITIAL_RESULT_PENDING` | `process-custodied-provider-result` | T5 (custodied result awaiting the candidate transaction) |
| `LOOP_TRANSITION_RECONCILE_REQUIRED` | `reconcile-provider-request` | an uncertain transition dispatch (§19.3) |
| `LOOP_NEEDS_NESS_DECISION` | `null` | the routed-signal path proved a genuine Ness question |
| `LOOP_NEEDS_USER_ACTION` | `null` | a practical external action is required |
| `LOOP_SAFETY_HOLD` | `null` | continuing would weaken a settled protection, or evidence is contradictory |
| `LOOP_WAITING_RECOVERING` | `null` | a bounded technical dependency or an interrupted operation is being recovered |
| `LOOP_DESIGN_CONTINUATION_COMPLETE` | `null` | the proved frontier is later building work, or no actionable DESIGN package exists |
| `LOOP_HANDOFF_COMPLETE` | `null` | T6 done; the ordinary projection governs |

### 7.4 Position derivation, as pseudocode

*Explanatory only.*

```
loop_status():
    fresh = authenticated_supervisor_status()             # §6.3, all five
    if not fresh.proved:                     return LOOP_WAITING_RECOVERING, null
    if fresh.workflow_state != ACCEPTED_FOR_DESIGN_ONLY
       or fresh.acceptance_truth != PROVED_ACCEPTED:
                                             return LOOP_NOT_APPLICABLE, null

    t = post_acceptance_transition_state()               # §17.2, lookup-first
    if t.contradiction:                      return LOOP_SAFETY_HOLD, null
    if t.established_complete:               return LOOP_HANDOFF_COMPLETE, null
    if t.stop_record is not None:            return t.stop_record.loop_state, null

    # an open transition provider request outranks every phase question
    if t.open_request is not None:
        return transition_recovery_position(t.open_request)   # §19.3 table

    # T1 saved evidence outranks the phase question, in this exact order.
    # Both are pure derivations over durable evidence: they append nothing,
    # call nothing, and return the same answer on every restart (§9.6a, §9.6b).
    if t.t1_custody_unverifiable:            return LOOP_SAFETY_HOLD, null
    if t.t1_output_retry_exhausted:          return LOOP_NEEDS_USER_ACTION, null

    if t.selection is None:                  return LOOP_SELECTION_REQUIRED,
                                                    continue-design-loop
    q = t.selection.scope
    if genuine_ness_question_open(q):        return LOOP_NEEDS_NESS_DECISION, null
    c = evaluate_interview_clearance(q)
    if not c.unlocked:
        # T2 positions A-D of §12.3c, derived here and never by the worker.
        stage = owed_piece3_stage(q, c)          # validation | coverage | none
        if stage is not None:
            if t.piece3_authorization(stage) is not None:
                                             return LOOP_PIECE3_COMMIT_REQUIRED,
                                                    commit-piece3-provider-result
            if t.piece3_custody_awaiting(stage) is not None:
                                             return LOOP_PIECE3_RESULT_PENDING,
                                                    process-custodied-provider-result
            if stage == "validation":        return LOOP_PACKAGE_CLEARANCE_REQUIRED,
                                                    dispatch-piece3-provider-review
                                             return LOOP_COVERAGE_REVIEW_REQUIRED,
                                                    dispatch-piece3-provider-review
                                             return LOOP_SAFETY_HOLD, null

    if t.prepared_task is None:              return LOOP_TASK_PREPARATION_REQUIRED,
                                                    prepare-next-design-task

    # T4 saved evidence outranks the phase question, exactly as the T1 pair
    # above does. A pure derivation over durable evidence: it appends nothing,
    # calls nothing, and returns the same answer on every restart (§14.3).
    # It sits HERE -- after the prepared task is proved, so the initial_design
    # work item is derivable -- and BEFORE the fall-through below, because an
    # exhausted run of result_invalid terminals yields no admissible custody,
    # so initial_result_custody is None and the fall-through would otherwise
    # return execute-initial-design against a budget that is already spent.
    if t.initial_design_output_retry_exhausted:
                                             return LOOP_NEEDS_USER_ACTION, null

    if t.initial_result_custody is None:     return LOOP_INITIAL_DESIGN_REQUIRED,
                                                    execute-initial-design
    if not t.initial_custody_committed:      return LOOP_INITIAL_RESULT_PENDING,
                                                    process-custodied-provider-result
                                             return LOOP_WAITING_RECOVERING, null
```

The final fall-through is deliberate: custody committed but establishment incomplete is a recovery position (§18 row J), not a success.

**The two T1 evidence guards, and why they sit exactly there** *(new in v1_10)*. They are placed **after** the open-request check and **before** `t.selection is None`, and the order between them is fixed:

- `t1_custody_unverifiable` first, because **safety outranks a practical stop**: saved bytes that no longer re-verify are a `LOOP_SAFETY_HOLD` a person resolves, and that answer must not be displaced by a milder one (`T1-CUSTODY-UNVERIFIABLE`, §9.6b);
- `t1_output_retry_exhausted` second, because without it an exhausted position falls through to `t.selection is None` and returns `LOOP_SELECTION_REQUIRED` / `continue-design-loop` — re-entering, for ever, a command whose only remaining move is refused. **That is not a stop; it is a loop that reports the wrong position** (`T1-INVALID-OUTPUT-EXHAUSTION-STOP`, §9.6a).

**Neither guard appends anything, dispatches anything, or introduces a loop state.** `LOOP_SAFETY_HOLD` and `LOOP_NEEDS_USER_ACTION` are both already in the §7.3 table, with a null `loop_next_command` in both cases.

**The T4 guard, and why it sits exactly there** *(new in v1_11)*. §14.3 already settled what an exhausted `claude_initial_design` budget means; v1_11 adds the one guard that makes the derivation actually say it (§5 P-35).

- **It sits AFTER** everything that already outranks a phase question — `t.contradiction`, `t.established_complete`, `t.stop_record`, `t.open_request`, the T1 pair, the genuine-Ness question, the clearance/Piece-3 stages, and `t.prepared_task is None`. Placing it after the prepared task is not cosmetic: **the `initial_design` work item is derivable only once an admitted prepared task exists** (§17.3a `WIM-INITIAL`), and a derivation that cannot name its work item cannot ask the installed budget about it.
- **It sits BEFORE** `t.initial_result_custody is None` → `execute-initial-design`, because that is the branch it exists to pre-empt. `initial_result_custody` requires bytes that re-verify **and** pass all ten `INIT-ADMISSION` checks (§17.2), and an exhausted run of `result_invalid` terminals produces none — so without the guard the derivation returns `LOOP_INITIAL_DESIGN_REQUIRED` / `execute-initial-design` for ever, against a spent budget.
- **An open T4 request still outranks it.** A prepared-but-undispatched, dispatched-uncertain or in-flight request is caught earlier by `t.open_request`, so this guard never displaces reconciliation-first recovery (`PROV-NO-REDISPATCH`, `INIT-NO-REDISPATCH`).
- **An unverifiable initial-design custody still outranks it.** `custody_unverifiable` is terminal for the transition and reaches `LOOP_SAFETY_HOLD` through the machinery §17.2 and §14.6 already describe (`CUSTODY-UNVERIFIABLE-HOLD`), and this guard neither displaces nor softens it. **Safety before a practical stop**, exactly as `t1_custody_unverifiable` precedes `t1_output_retry_exhausted`.
- **A valid admitted custody makes it irrelevant.** Where `initial_result_custody` is non-`None` the loop proceeds to T5 and the budget question does not arise.

**And it changes nothing while the budget remains available.** `initial_design_output_retry_exhausted` is false wherever the installed `bounded_output_retry_budget()` returns `available`, so **ordinary installed T4 retry and recovery semantics continue exactly as in v1_10** (§14.3). **This guard removes no retry; it ends one that is already over.**

### 7.5 The separate continuation operations

The continuation runs exactly this closed set of commands and no others. **The public `question-validation` and `question-coverage-review` are NOT in it** — they retain their ordinary operator and non-continuation behaviour only (`T2-PUBLIC-COMMANDS-UNCHANGED`, §12.3c.A).

| Command | Status | Reaches a provider? |
|---|---|---|
| `continue-design-loop` `[proposed]` (T1) | new | **yes** |
| `dispatch-piece3-provider-review` `[proposed]` (T2 position A) | new | **yes** |
| `process-custodied-provider-result` (T2 position B, T5) | installed | **no** — it consumes a custodied result |
| `commit-piece3-provider-result` `[proposed]` (T2 position C) | new | **no** — provider-free by construction |
| `prepare-next-design-task` `[proposed]` (T3) | new | **yes** |
| `execute-initial-design` `[proposed]` (T4) | new | **yes** |
| `reconcile-provider-request` (recovery) | installed | **no** — it performs an authoritative lookup and records; it never dispatches |

**Exact counts: FIVE new execution-command names and TWO installed ones; FOUR reach a provider and THREE do not.**

- New (5): `continue-design-loop`, `dispatch-piece3-provider-review`, `commit-piece3-provider-result`, `prepare-next-design-task`, `execute-initial-design`.
- Installed (2): `process-custodied-provider-result`, `reconcile-provider-request`.
- Provider-contacting (4): `continue-design-loop`, `dispatch-piece3-provider-review`, `prepare-next-design-task`, `execute-initial-design`.
- Provider-free (3): `commit-piece3-provider-result`, `process-custodied-provider-result`, `reconcile-provider-request`.

`loop-status` is a **new read-only CLI command** and is deliberately **not counted among the seven execution commands**, because it is write-incapable and dispatches nothing. Counting the CLI surface instead, this design adds **six** new CLI names: `loop-status` plus the five new execution commands. T6 is a consequence of the binding rule; T7 is the installed loop.

**`CONTINUATION-SET-CLOSED-AT-SEVEN`** *(restated in v1_10)*. The table above is the **whole** continuation execution set. **`close-open-consumption` is a registered installed supervisor command and is deliberately NOT one of the seven**, exactly as v1_9 settled and exactly as the installed `CONTINUATION_EXECUTION_COMMANDS` registry already records. **v1_10 does not add an eighth**, and no position reached by the continuation — including the exhausted T1 invalid-output position of §9.6a — owes one. Where a design or an implementation finds itself needing an eighth command to reach an honest stop, **the stop is what is missing, not the command** (§9.6a, §23 `R-5e`).

**Where `close-open-consumption` genuinely belongs, stated so it is not deleted by mistake** (`T1-NOT-A-CONSUMPTION`, §9.6a). It closes a real, open `diagnosis_strategy_consumption_started` transaction of the **installed correction/diagnosis machinery** — the supervisor's territory (§16.2) — by appending `diagnosis_strategy_consumption_terminated` with the diagnosis identity, the diagnosis and strategy digests, the strategy novelty key, the blocking-finding references and the correction specification that transaction actually carries. **That use is legitimate, is preserved unchanged, and is not weakened, genericised, re-scoped or removed by this file.**

Every one of them is:

- **lookup-first** — it re-reads the authenticated journal and returns an already-durable effect with **zero appends**;
- **idempotent** — re-entry from any crash position produces at most one transition's durable effect and never a second package or a second candidate;
- **crash-safe** — it runs under the installed supervisor operation envelope (`supervisor_operation_started` → work → `supervisor_operation_completed`), reconciled through the installed `supervisor-operation-status` and its six exact `recovery_outcome` strings;
- **append-only** — installed event types only (§7.6);
- **unreachable from the Accept request** — `INV-ACCEPT`;
- **bounded** — one open provider request at a time, under the installed episode and attempt caps, the installed timeouts, and the worker's `retry_series_key` backoff.

### 7.6 Journal events used — and why no new event type is required

| What must be durable | Existing carrier |
|---|---|
| a continuation operation began / ended, and any loop-level stop | `supervisor_operation_started` / `supervisor_operation_completed` (the latter already carries the full dependency slot) |
| each bounded provider call | `provider_request_prepared` → `provider_dispatch_begun` → (`provider_request_accepted`) → `provider_result_custody_recorded` → `provider_request_terminal_recorded`; `provider_request_reconciled` on an uncertain outcome |
| **which package was selected** | the **custodied selection result**, digest-bound by `result_custody_identity` on the terminal record — the installed pattern for a validated model result a later step consumes |
| **the prepared task** (target path, specification, settled basis) | the **custodied task-preparation result**, bound the same way |
| **the produced initial candidate bytes** | the **custodied Claude result**, bound the same way — exactly as `claude_correction` already works |
| a possible-Ness finding from selection or preparation | `review_signal_recorded` — its documented purpose, and it binds to `scope_root_path`, not to a candidate |
| the new package is established | `validation_recorded` |
| the inventory was independently challenged | `question_coverage_review_recorded` |
| Q's first candidate created and held | `candidate_write_ahead_recorded` + `candidate_custody_recorded` (+ `candidate_write_ahead_aborted` on abandonment) |

**Two candidates for a new event type were examined and rejected.** (a) A "selection recorded" event — the custodied digest-bound result already carries it, and a second record of the same fact is the "second source of truth" the installed design forbids. (b) Re-using `piece3_provider_work_recorded` to carry a selection — its `authorizes_event_type` key drives `Replay.piece3_provider_authorization()` (`replay.py:1021-1043`), which treats every unconsumed authorization as pending and returns `"contradiction"` on more than one pending; a selection authorizes nothing, so it would sit unconsumed forever and collide with the genuine question-validation authorization.

**What this design adds, all inside existing registries:**

- three work-item kinds `[proposed]`: `next_package_selection`, `next_design_task_preparation`, `initial_design`;
- three provider kinds `[proposed]`: `codex_next_package_selection`, `codex_next_design_task_preparation`, `claude_initial_design`, with their entries in `PROVIDER_KIND_BY_WORK_ITEM_KIND`, `WORK_ITEM_KIND_BY_PROVIDER_KIND`, `RESULT_SCHEMA_ID_BY_PROVIDER_KIND` and the engine template map;
- two enum values on existing enums: `CANDIDATE_INTENT_ORIGIN_INITIAL` and `CANDIDATE_CUSTODY_ORIGIN_INITIAL` `[proposed]`.

No second state store, no second journal, no second gate, no parallel dispatch table.

### 7.6a The custody closure rule for the three new work-item kinds *(Blocker 3)*

`Replay.custodied_results_awaiting_processing()` keeps a custody pending until `_downstream_recorded()` proves a work-item-specific downstream effect, and an unmapped kind never closes (P-21). The two read-only transition kinds genuinely have **no** downstream effect append — their custodied result *is* the durable output — so the read-side rule must say so explicitly rather than leaving them unmapped.

**`CLOSURE-READONLY`.** For `next_package_selection` and `next_design_task_preparation`, and for those two kinds only:

- a **completed `result_received` terminal together with its matching custody record is itself the closure.** No separate downstream effect append is owed, and none is invented;
- they **must not** remain in `custodied_results_awaiting_processing()` once that pair exists;
- they **must not** be routed through `process-custodied-provider-result` merely to manufacture an effect event — doing so would fabricate a record of something that did not happen;
- their custody/terminal pair is the **retained durable review output**, and it is the object `loop-status` re-reads;
- `loop-status` independently re-runs the full `SEL-ADMISSION` (§9.5) or the §13.6 preparation re-admission **every time it wants to use those bytes**;
- an admission failure or a staleness is handled by the loop-level rules (§9.5, §13.6) and **does not** make the custody "unfinished processing" — a stale-but-closed custody is history, not pending work;
- a `result_invalid` terminal continues to use the installed invalid-output and bounded-output-retry semantics, unchanged; the installed `_downstream_recorded()` already closes an invalid terminal by itself.

**`CLOSURE-INVALID-TERMINAL-IS-TERMINAL`** *(new in v1_10 — clarification, not a new rule)*. Because the invalid terminal closes itself, there is **no second closure transaction owed anywhere** for a `next_package_selection` whose terminal is `result_invalid`:

- the request/result is already terminal under its **own** lifecycle — **a `result_invalid` terminal is a terminal provider result**, not an unfinished one;
- the custody/terminal pair is **terminal-only closed** under the existing read-only closure semantics above;
- **no `diagnosis_strategy_consumption_started` exists**, so **no `diagnosis_strategy_consumption_terminated` is owed and none may be invented**;
- therefore **no `close-open-consumption` is owed for it**, at any budget position, and a design or build that says otherwise has named a command that would truthfully refuse (§9.6a, §5 P-34, §23 `R-5e`).

**And closed is not the same as absent.** The custody record and its saved bytes remain **authenticated provider-result evidence** and stay protected by `T1-CUSTODY-UNVERIFIABLE` (§9.6b) for as long as the durable record requires those bytes — **whatever the terminal form is.** *Closed* means nothing further is owed; it never means the evidence may be treated as though it were never received.

**`CLOSURE-INITIAL-PENDING`.** `initial_design` is deliberately **different**. Its valid custody **does** remain awaiting processing until the candidate transaction proves its downstream completion — the same shape the installed `correction_apply` row already uses, whose closure includes `candidate_custody_recorded` matched either by `provider_request_identity` or by `work_item_identity`. Until T5 commits that custody, the initial-design result is unfinished work and the loop knows it.

**Smallest exact extension.** This is a read-side mapping only: two entries added to the existing `downstream_types` dictionary would be the wrong shape, because those two kinds owe **no** event. The honest extension is a small explicit set beside that dictionary — `CLOSED_BY_TERMINAL_ONLY_WORK_ITEM_KINDS` `[proposed]` = {`next_package_selection`, `next_design_task_preparation`} — consulted in `_downstream_recorded()` before the `downstream_types` lookup, returning `True` when the terminal is a completed `result_received` for that request. `initial_design` gets an ordinary `downstream_types` row naming `candidate_custody_recorded`.

**No new journal event type, no new event body key, and no second store** are required by this rule. Required tests: §25 R25, R26, R27.

---

## §8 — THE CURRENT-PACKAGE BINDING RULE, AND THE TRANSITION BINDING

### 8.1 What the rule may read

Only the **authenticated** journal event list (after HMAC verification and replay) and **real current bytes** of files those events name, read through the installed anchored, no-symlink-followed readers. It may never read a filename, a version suffix, a directory listing order, a modification time, a commit message, model prose, or the ordering of files in `05_ACTIVE_CANDIDATE/`.

### 8.2 Step 1 — every package the journal proves

Let `V` be every authenticated `validation_recorded`. Group by `package_scope_id`. For each scope `S`, `anchor_validation(S)` is the **earliest** event in `S`.

Earliest **within** a scope is deliberate: `authenticated_candidate_custody()` already anchors each scope's chain on that scope's first bound candidate, and moving it would invalidate the chain. **The defect corrected is "earliest across all scopes", not "earliest within a scope".**

### 8.3 Step 2 — the anchor candidate, in two cases

- **Case A — the scope's bound root is itself a candidate.** `anchor_candidate(S) = validated_package_bound_candidate(anchor_validation(S))`. **Unchanged; AIC takes this case and nothing about it moves.**
- **Case B — the scope's bound root is not a candidate.** `anchor_candidate(S)` is the single candidate committed by that scope's `candidate_custody_recorded` whose matching write-ahead carries `intent_origin == CANDIDATE_INTENT_ORIGIN_INITIAL` `[proposed]`, whose `parent_candidate_*` equal the scope's bound root exactly, and whose `correction_round` is the initial round. Zero → the scope has no anchor yet and is **in transition**. Two or more → **contradiction, fail closed**.

### 8.4 Step 3 — establishment completeness

`S` is **established** when all of: `anchor_validation(S)` exists and is authenticated; `anchor_candidate(S)` exists under §8.3; the file at that path re-proves **now** to exactly its recorded `sha256` and `bytes`; and the scope's custody chain is internally consistent under the installed `authenticated_candidate_custody()` rules.

A scope that is not established is never current. **This is what stops an incomplete transition from selecting the wrong package.**

### 8.5 Step 4 — ordering and the single-transition fence

Order established scopes by `anchor_validation(S).event_seq` — controller-issued, monotonic, HMAC-authenticated, hash-chained, and the only ordering key used.

**`CPB-CURRENT`.** The current package is the established scope with the greatest `anchor_validation(S).event_seq`.

**`CPB-SINGLE-TRANSITION`.** At most one scope may be both (a) not established and (b) holding post-acceptance durable evidence — a `validation_recorded`, a transition provider request, a prepared task, an initial write-ahead, or a proved unconsumed selection. Two or more is a **contradiction, fail closed**: nothing is preferred, nothing dropped, nothing repaired.

**`CPB-ORDERING-SAFETY`.** A new scope may be established only while the previous current scope is terminal — `PROVED_ACCEPTED`, or a durably recorded loop-level stop for that package. Otherwise: contradiction, fail closed.

### 8.6 What this guarantees

| Requirement | How |
|---|---|
| old accepted history stays readable | nothing deleted or rewritten; `Replay(events, S_old)` still projects P in full |
| a newer package cannot inherit old scope state | every projection, question, signal, standing map, custody chain and dependency is keyed by `package_scope_id` (P-13) |
| an incomplete transition cannot make the wrong package current | §8.4 |
| duplicate or contradictory evidence fails closed | §8.3 Case B duplicate, `CPB-SINGLE-TRANSITION`, `CPB-ORDERING-SAFETY`, §23 |
| restart reaches the same package | pure function of the authenticated list plus byte re-proofs |
| no untrusted filename or version ordering decides authority | §8.1; the ordering key is `event_seq` |

### 8.7 Effect on the current real state

Applied to today's journal: one scope, Case A, anchor at validation seq 1, established. `CPB-CURRENT` returns **the same binding the installed code returns today, field for field.** The corrected rule changes nothing about the current state; it changes only what happens once a second scope exists.

### 8.8 One honest note, recorded and not repaired

Today's binding takes `branch`, `head_sha` and `source_binding_sha256` from validation seq 1, so the acceptance at seq 84 carries `head_sha ce3a38f4…` while the live checkout is at `64af315f…`. Whether a scope's binding should instead carry its **newest** validation's source facts is a real question about source-staleness semantics that would change installed behaviour for the already-accepted package. It is outside this bridge and is carried to §26.

### 8.9 The transition binding — how Q is worked on before it is current

T3, T4 and T5 must run **for Q** while **P is still the current package**. Those are two different bindings for two different purposes, and this design names them rather than blurring them.

| # | Binding | Derived from | Used by | Reported as current? |
|---|---|---|---|---|
| **1** | **P current established binding** | §8.2–§8.5, unchanged | `supervisor-status`, the UI, every ordinary supervisor command. **P remains the current accepted package until Q is fully established.** | **yes** |
| **2** | **Q pre-validation transition binding** `[proposed]` | §8.10 — the admitted T1 selection and controller-proved facts **only**; Q has no `validation_recorded` yet | **only** the first-Q Piece-3 operations that establish Q (§8.10) | **never** |
| **3** | **Q post-validation transition binding** | Q's first `validation_recorded` (scope, key, id, branch, head, source binding, manifest, validation set, standing) + `derive_settled_decision_binding(state, scope_Q, …)` + **round-zero = Q's proved bound root** | remaining T2 work where applicable, T3, T4, T5, and their recovery | **never** |
| **4** | **Q established current binding** | §8.4 establishment, once the initial candidate custody makes it true | ordinary modern-supervisor ownership begins | **yes** |

The transition binding is possible without weakening anything because `_supervisor_candidate_file()` imposes no candidate-grammar requirement (P-18): it requires a safely repository-relative, non-symlinked, readable file of at most 8 MiB whose bytes match the authenticated identity exactly. Q's bound root is exactly such a file, and binding round-zero to it is honest — the transition operations genuinely are rooted in that file and in no candidate, because Q has no candidate yet.

**`TB-NOT-CURRENT`.** The transition binding is never returned by `supervisor-status`, never shown as the current package in the UI, and never consulted by `status._project()`'s ordinary precedences. **An incomplete Q cannot steal the current binding.**

**`TB-BOUNDED-USE`.** A transition binding — pre-validation or post-validation — may only be constructed while `CPB-SINGLE-TRANSITION` holds and Q is the single in-transition scope, and each may only be used by the operations its own row names. Any other use is a contradiction. **Bindings 2 and 3 are never simultaneously usable**: binding 2 retires the instant Q's first `validation_recorded` is durable (`TB-PREVALIDATION-RETIRES`), and binding 3 does not exist before it.

**This corrects a v1_5 contradiction.** v1_5's `TB-BOUNDED-USE` named only `prepare-next-design-task`, `execute-initial-design`, the T5 consumption and their recovery, while §12.3 simultaneously required T2 to run under a Q context. T2's first stage runs under binding 2; its later stages and everything after run under binding 3.

### 8.10 The Q pre-validation transition binding *(Correction 1)*

P-29 shows the circularity: v1_5 derived Q's transition binding from the `validation_recorded` that T2 itself produces. Binding 2 exists to break it, and it is deliberately the narrowest object in this design.

**`TB-PREVALIDATION-EXISTS-WHEN`.** It may be constructed only when **all** of:

- exactly one T1 selection has passed the **full** `SEL-ADMISSION` (§9.5, all ten proofs);
- Q has **no** `validation_recorded` of any kind;
- P's acceptance is `PROVED_ACCEPTED` and freshly re-proved (§6.3);
- `CPB-SINGLE-TRANSITION` holds and Q is the single in-transition scope.

**`TB-PREVALIDATION-DERIVED-FROM`.** Every field comes from controller-proved facts and from nothing else:

| Field | Source |
|---|---|
| `package_scope_id`, `package_key`, `package_id` | derived by the controller from Q's proved bound root via `interview_package_scope_id()` / `interview_package_key()`; `package_id` is null unless a controlled id genuinely exists in source |
| `scope_root_path` | Q's proved source root from the admitted T1 selection, re-proved against real source |
| `branch`, `head_sha`, `source_binding_sha256`, `source_manifest_sha256`, `required_source_paths` | a **freshly frozen** source binding and manifest read at construction |
| `settled_decision_binding_sha256` | `derive_settled_decision_binding(state, scope_Q, …)` — legitimately empty for a package that has settled nothing with Ness, which is a real value and not a missing one |
| `piece3_standing_sha256` | the current interview standing chain, which is global rather than package-scoped and is therefore truthfully derivable before Q's first validation |
| `validation_set_id` | **null.** None exists. |
| `routed_signal_refs` | **empty**, unless genuine routed signals for scope_Q already exist, in which case exactly those |
| round-zero candidate (`candidate_path` / `sha256` / `bytes`) | **Q's proved source root**, permitted truthfully because `_supervisor_candidate_file()` imposes no candidate-grammar requirement (P-18) — it requires a safe repository-relative, non-symlinked, readable file of at most 8 MiB whose bytes match the authenticated identity exactly |
| the transition's permission | the authenticated P acceptance that permits exactly one transition |

**`TB-PREVALIDATION-INVENTS-NOTHING`.** It must **not** invent a `validation_set_id`; must **not** invent routed signals; must **not** invent a candidate; and must **not** invent a settled decision. Where a value does not exist, the honest null or empty form is carried, and §12.3g's matrix variants are what make that admissible.

**`TB-PREVALIDATION-NOT-CURRENT`.** It is **never** returned as current by `supervisor-status`, **never** fed into ordinary `status._project()`, and **never** shown as the current package in the UI. It is not an alternate current-package truth; P remains current throughout.

**`TB-PREVALIDATION-USES`.** It is usable **only** by the first-Q Piece-3 transition operations necessary to establish Q, and by nothing else:

```
  dispatch-piece3-provider-review                 (first Q question-validation)
  process-custodied-provider-result              (for that exact T2 result)
  commit-piece3-provider-result                  (that exact Piece-3 commit)
  recovery of those exact operations
```

**`TB-PREVALIDATION-RETIRES`.** The moment Q's first `validation_recorded` is durable, binding 2 **retires**. Every later operation — including Q's coverage-review stage — uses binding 3, derived from that validation in the ordinary way. A construction of binding 2 while a Q validation exists is a contradiction and fails closed.

**`TB-PREVALIDATION-RECOVERY`.** Recovery of an operation started under binding 2 rebuilds **that exact binding** from:

1. the authenticated `supervisor_operation_started` of that operation (`TB-RECOVERY-BINDS-THE-RECORD`, §8.9.1);
2. the exact admitted T1 selection evidence — the custodied selection bytes, re-admitted under all ten `SEL-ADMISSION` proofs;
3. a current re-proof of the source facts that start bound.

**No filename, no model-authored title and no caller-supplied scope may take part.** If that exact binding cannot be reconstructed — the selection is no longer admissible, the root's bytes moved, the source facts differ, or two selections are admissible — **fail closed**, nothing appended, no provider contacted.

### 8.9.1 Transition recovery must discover the operation BEFORE it chooses a context *(Blocker 4)*

v1_1 said `supervisor-operation-status` "must resolve its binding from the authenticated start event", and treated that as already installed. P-22 shows it is not: `command_supervisor()` builds the context — binding the **current** package — before it reads the envelope, and `supervisor_operation_status()` scopes its replay before it looks at the requested operation identity. `reconstruct_original_envelope()` is the correct discipline but runs **after** discovery, so it cannot solve discovery. While P is current, a Q-scoped transition operation is invisible.

**`TB-RECOVERY-BOOTSTRAP`.** For an **operation-specific** recovery request, the exact order is:

```
 1. READ AND STRUCTURALLY VALIDATE THE CALLER ENVELOPE FIRST -- before any
    context is built.
 2. The caller supplies ONLY the allowed fields: supervisor_operation_id,
    supervisor_command, and the three unlock_evidence_* fields, all present and
    NULL.  THE CALLER SUPPLIES NO PACKAGE BINDING, no scope, no root, no
    candidate, and no source facts.  A non-null unlock_evidence_* value is
    refused with nothing appended, exactly as installed.
 3. AUTHENTICATE THE JOURNAL GLOBALLY, UNSCOPED, FOR LOOKUP PURPOSES ONLY --
    HMAC verification and replay over the whole event list.  Unscoped here means
    "may be searched", never "may be acted on".
 4. LOCATE EXACTLY ONE supervisor_operation_started whose
    supervisor_operation_id equals the requested identity AND whose
    supervisor_command equals the requested command.
 5. ZERO matches, MORE THAN ONE match, or a command mismatch  ->  FAIL CLOSED.
    Nothing is preferred, nothing is guessed, nothing is appended.
 6. READ package_scope_id, source_binding_sha256, candidate_path,
    candidate_sha256, candidate_bytes AND work_item_identity ONLY from that
    authenticated start.
 7. PROVE that scope and those source/candidate facts correspond to an
    authenticated package record -- either an ESTABLISHED scope (§8.4) or the
    ONE in-transition scope permitted by CPB-SINGLE-TRANSITION (§8.5).  A scope
    matching neither  ->  FAIL CLOSED.
 8. BIND EXACTLY THE SCOPE THE AUTHENTICATED START RECORDED, and build the
    recovery context for it -- the current-package binding for an established
    scope, the transition binding (§8.9) for the in-transition scope.  The
    phase the operation belongs to NEVER decides the scope; only the record
    does.
 9. ONLY THEN construct the scoped Replay and run
    reconstruct_original_envelope().
10. The reconstructed pre-state digest P0, the H0 position and the operation
    identity must still match the recorded values EXACTLY, unchanged from the
    installed rule.  A mismatch  ->  FAIL CLOSED.
```

Steps 9 and 10 are the installed discipline, untouched. Steps 1–8 are what this design adds, and they add **discovery**, not authority: nothing the caller sends can choose a package, and nothing outside the authenticated start can supply a binding field.

**`TB-RECOVERY-BINDS-THE-RECORD`.** The invariant is not "bind Q" and it is not "bind P". It is:

> **Recovery never assumes a package. It binds exactly the `package_scope_id` recorded by the authenticated `supervisor_operation_started` event, and nothing else.**

An authenticated start recording an established scope stays that established scope. An authenticated start recording the single in-transition scope stays that scope. Anything else fails closed. The consequences follow from the record, not from the phase name:

| Operation | Whose start is it? | What recovery binds |
|---|---|---|
| **T1 `continue-design-loop`** | begins from the terminal-accepted package **P** — the only package that exists yet | **P**, because P is what its start records |
| **T2 `question-validation` / `question-coverage-review`** | Q, once Q is controller-proved from an admitted selection | **Q**, because Q is what its start records |
| **T3 `prepare-next-design-task`** | Q | **Q** |
| **T4 `execute-initial-design`** | Q | **Q** |
| **T5 `process-custodied-provider-result`** | Q, discovered through §8.9.2 (no caller envelope exists) | **Q** |

**`TB-NO-PREMATURE-Q`.** At T1 **Q does not exist**: no selection has been admitted, so there is nothing to derive a scope from. Recovery of an uncertain T1 selection dispatch therefore discovers the operation globally, proves its recorded scope is P, builds the **P** recovery context, and reconciles that exact request. **Q must not be inferred, named, guessed, or partially bound before a selector result has been durably received and admitted under all ten `SEL-ADMISSION` proofs (§9.5).** Only an admitted T1 result can identify Q.

v1_2's crash Row C said T1 recovery "binds Q, never P". That was impossible and is corrected here and in §18 Row C.

**`TB-RECOVERY-GENERIC-UNCHANGED`.** A `supervisor-operation-status` call carrying **no** operation identity keeps its installed behaviour exactly: the ordinary current-package context, the ordinary generic report. Only the operation-specific form takes the bootstrap above.

### 8.9.2 The pending-custody bootstrap — for `process-custodied-provider-result` ONLY

That command has **no caller-supplied operation identity at all** (P-22 fact 3) and selects its work from `situation.pending_custody`, which is current-package scoped. It therefore needs its own safe bootstrap, and it must not be given a caller-supplied binding to compensate.

**`TB-CUSTODY-BOOTSTRAP`.** The discovery happens **before** the context is built, not inside a command that has already been handed the wrong one. The later implementation must **not** build the ordinary current-package context for P and then try to discover Q inside `commands.py` — by then `situation.pending_custody` is already P-scoped and Q's pending custody is already invisible.

The exact order, for a transition invocation of `process-custodied-provider-result`:

```
 BEFORE ordinary current-package context construction:

 1. AUTHENTICATE AND READ THE JOURNAL FRESH -- HMAC verification and replay
    over the current event list, at this moment.
 2. FRESHLY DERIVE that the loop-level post-acceptance transition is active:
    the current package is terminal-accepted with acceptance_truth
    PROVED_ACCEPTED, and one transition is open (§17.2).
 3. LOCATE EXACTLY ONE unfinished TRANSITION custody whose work-item kind is
    in this CLOSED SET:
         question_validation
         coverage_review
         initial_design
    "Unfinished" means its closure is not yet proved -- the two Piece-3 kinds
    until their authorization is appended, initial_design under
    CLOSURE-INITIAL-PENDING.
 3b. THE KIND MUST AGREE WITH THE FRESHLY DERIVED LOOP POSITION:
         T2 validation position B  ->  question_validation ONLY
         T2 coverage   position B  ->  coverage_review     ONLY
         T5                        ->  initial_design      ONLY
     A custody of the wrong kind for the derived phase  ->  FAIL CLOSED.
 4. PROVE its package_scope_id is exactly the ONE in-transition scope
    permitted by CPB-SINGLE-TRANSITION (§8.5).
 5. PROVE its request / work-item / custody chain is authenticated and its
    continuation is genuinely unfinished.
 6. ZERO matches -> no work, fail closed.  MORE THAN ONE match at step 3, or a
    failure at step 3b or step 4  ->  FAIL CLOSED, nothing appended, no
    provider contacted.
 7. BUILD THE Q TRANSITION CONTEXT (§8.9) for that proved scope.
 8. ONLY THEN invoke process_custodied_provider_result(context).
```

**`TB-CUSTODY-NO-STALE-REPORT`.** `loop-status` and this command may share the **same pure derivation** (§17.2) — that is the point of deriving rather than storing. But the command **must re-run that proof against the current authenticated journal immediately before building its context**, and must never act on a previous `loop-status` response as authority. A worker's earlier report is evidence of what was true when it was produced; the journal may have moved since, and nothing about the checkout would show it. A stale report that names Q while the live journal no longer proves Q must cause the command to stop, not to proceed.

Q is bound **never** merely because P is the current package, and **never** from a filename, a directory listing, a model-authored title, a stale `loop-status` response, or any caller input — this command has no caller envelope at all, and it must not be given one to compensate.

**`TB-CUSTODY-CLOSED-SET`.** The selector and task-preparation custodies are **not** members of the pending set: they are terminal-only closed (`CLOSURE-READONLY`, §7.6a) and are never routed through `process-custodied-provider-result`. Only the three kinds named at step 3 may ever be found here.

The installed "exactly one custodied provider result must have an unfinished continuation" refusal remains, and is now evaluated against the correctly-bound scope rather than against whichever package happens to be current.

### 8.9.3 When no transition is active

When the loop level is **not** active — no terminal acceptance, or no open transition — `process-custodied-provider-result` and `supervisor-operation-status` keep their installed binding and behaviour **exactly**, including the installed context-construction order. The bootstraps of §8.9.1, §8.9.2 and §8.9.4 are reachable only during a real transition, and they change nothing about the ordinary loop.

### 8.9.4 The three T2 pre-context discovery paths, kept apart *(Correction 2)*

**`TB-CUSTODY-ONE-COMMAND`.** `TB-CUSTODY-BOOTSTRAP` (§8.9.2) belongs to `process-custodied-provider-result` and to **no other command**. Its precondition is an **unfinished** transition custody, and that precondition cannot hold for the other two Piece-3 commands:

- `dispatch-piece3-provider-review` runs **before** any Piece-3 custody exists;
- `commit-piece3-provider-result` runs **after** `_b6f_piece3()` has appended the authorization, at which point the installed `_downstream_recorded()` rule has already **closed** that custody — so an "unfinished custody" lookup would find nothing.

v1_6's §24.1 assigned that bootstrap to both of them. Each now has its own path. **`TB-CUSTODY-BOOTSTRAP` itself is not weakened**; it simply stops being claimed where it cannot apply.

All three paths run **before** any context is constructed, accept **no caller package, scope, stage, variant, authorization or custody identity**, and re-prove against the current authenticated journal rather than a previous `loop-status` response (`TB-CUSTODY-NO-STALE-REPORT`).

#### Path A — `dispatch-piece3-provider-review` (T2 position A)

Runs **before** a Piece-3 custody exists, so it must not require one.

```
 1. Freshly authenticate the journal.
 2. Freshly prove P is terminal-accepted and the post-acceptance transition is
    active.
 3. RE-ADMIT the exact T1 selection under all ten SEL-ADMISSION proofs (§9.5).
 4. Prove exactly ONE Q in-transition scope (CPB-SINGLE-TRANSITION).
 5. Derive the exact owed Piece-3 stage from CONTROLLER STATE ONLY
    (T2-STAGE-FROM-STATE): the stage whose event is still missing.
 6. Derive the correct Q transition binding for that stage:
        first Q question-validation  ->  PRE-VALIDATION binding 2   (§8.10)
        later coverage review        ->  POST-VALIDATION binding 3
 7. Build that context, then dispatch exactly one provider request.
```

**`TB-DISPATCH-NO-CUSTODY-PRECONDITION`.** It **must not** require a pending custody in order to dispatch. Zero or more than one admissible selection, zero or more than one in-transition scope, an unprovable owed stage, or an unconstructible binding → **fail closed**, nothing appended, no provider contacted.

#### Path B — `process-custodied-provider-result` (T2 position B, and T5)

**Keeps §8.9.2 exactly**: fresh authentication → derive the active transition → exactly one unfinished transition custody from the closed set `{question_validation, coverage_review, initial_design}` → the custody kind must agree with the freshly derived loop phase → prove it belongs to the one Q transition scope → build Q's correct transition context → then call the installed processing command.

#### Path C — `commit-piece3-provider-result` (T2 position C)

Runs **after** the authorization exists, when the custody is already closed. Its anchor is therefore the **authorization**, not a pending custody.

```
 1. Freshly authenticate the journal.
 2. Freshly derive the active transition and the exact owed Piece-3 COMMIT
    stage.
 3. Locate exactly ONE unconsumed, SCOPE-MATCHED
    piece3_provider_work_recorded for Q whose authorizes_event_type is the
    exact owed event.
 4. From that authenticated authorization, locate the exact named
    provider_request / result_custody / terminal evidence it references.
 5. Reconstruct and re-prove the correct Q transition binding from
    authenticated evidence (pre-validation binding 2 for the first
    validation commit; post-validation binding 3 for a coverage commit).
 6. REJECT: zero authorizations; duplicates; wrong scope; wrong stage;
    a custody that does not match the one the authorization names; stale
    evidence; or any contradiction  ->  FAIL CLOSED, nothing appended.
 7. Run the existing extracted provider-FREE Piece-3 commit logic.
 8. ZERO provider calls.
```

**`TB-COMMIT-BY-AUTHORIZATION`.** Path C never performs an "unfinished custody" lookup, because by construction there is none to find.

---

## §9 — THE SELECTION CONTRACT *(Correction 4)*

### 9.1 One selector, one contract — the installed one

v1_0 claimed "the same `NEXT_PACKAGE_PROMPT` text" and "the same strict result validation" while defining an incompatible `NH_NEXT_PACKAGE_SELECTION_RESULT_V1`. That is internally incoherent, and it is also unnecessary: P-14 shows the installed contract already proves everything the continuation needs.

**`SEL-INSTALLED-CONTRACT`.** The continuation selection uses:

- the installed `NEXT_PACKAGE_PROMPT`, with exactly **two** bounded corrections — its authority-order line names the current authoritative Decision Defaults (§10), and it states the actionable-root requirement (`T1-ACTIONABLE-ROOT-PROMPT`, §9.3a) *(second correction added in v1_9)*. **Both are text corrections inside the same installed builder; there is no second prompt builder** (`PROMPT-NO-SECOND-BUILDER`);
- the installed result key set `NEXT_PACKAGE_ANALYSIS_REQUIRED_KEYS`, **unchanged** — **no key is added, removed, renamed or made optional**, by this or any other rule in this file;
- the installed validator `validate_next_package_analysis(text, errors, required_files)`, supplied with the controller's own preflight-resolved authority set, with exactly **one** bounded strengthening — the non-null `package_source_path` requirement extends from `prepare_claude_task` alone to **both actionable actions** (`T1-ACTIONABLE-ROOT`, §9.3a) *(added in v1_9)*. **Every other proof it performs is unchanged, and the strengthening only ever refuses more; it admits nothing the installed validator refuses** (`SEL-B6D-STRENGTHENING-ONLY`);
- the installed classification → action mapping, **unchanged** — the same seven pairs, in the same directions.

**No new selection result schema is defined.** `NH_NEXT_PACKAGE_SELECTION_RESULT_V1` is withdrawn.

**Why this is the right reuse and not merely the cheap one:** stage two consumes the stage-one object directly — `build_prepare_task_prompt(analysis, decision_binding)` and `validate_prepared_task(task_message, analysis, …)` both take `analysis`, and stage two is required to return `package_source_path` **unchanged** and is cross-checked on it (P-15). A different selection schema would break the very seam Correction 2 restores.

### 9.2 What changes about the selection, and what does not

| Aspect | Installed `next-package` | Continuation T1 |
|---|---|---|
| prompt text | as installed | as installed, with two bounded text corrections: the authority line (§10) and the actionable-root requirement (`T1-ACTIONABLE-ROOT-PROMPT`, §9.3a) |
| result **key set** | as installed | **identical** — `NEXT_PACKAGE_ANALYSIS_REQUIRED_KEYS` is not changed in any way |
| result **validator** | as installed | the installed validator with **one** bounded strengthening: the non-null root requirement extends from `prepare_claude_task` alone to **both actionable actions** (`T1-ACTIONABLE-ROOT`, §9.3a). It only ever **refuses more** (`SEL-B6D-STRENGTHENING-ONLY`); the four non-actionable actions are unchanged |
| classification → action mapping | as installed | **identical** |
| invocation | direct top-level Codex call | the installed supervisor provider lifecycle, `work_item_kind = next_package_selection` `[proposed]` |
| durability | printed report only | `provider_result_custody_recorded` + `provider_request_terminal_recorded`, digest-bound |
| reachable from the worker | no (P-6) | yes, as `continue-design-loop` |
| bounded / backed off | command timeout | installed episode caps, attempt caps, timeouts, `retry_series_key` backoff |
| authorises anything | no | **no** — it is navigation, and T2/T3 still prove everything independently |

### 9.3 Mapping the installed fields into loop semantics

The controller reads exactly three fields as operative, and everything else stays evidence:

| Installed field | Loop meaning |
|---|---|
| `package_source_path` | **the one proved root** from which Q's `package_scope_id` is derived. This is the only field by which a selecting review can state which package it selected in a checkable form. |
| `classification` (and its required `controller_action`) | which route the loop takes (§9.4) |
| `package_id` | used **only** when a controlled id genuinely exists in source; otherwise explicit null, and no id is invented, no slug minted, no filename read as an identity |
| `package_title`, `simple_explanation`, `dependency`, `unknowns` | **evidence only.** `package_title` is model prose and identifies nothing. |
| `source_paths_checked` | the coverage proof the validator already measures |

**`SEL-ROOT-IDENTIFIES`.** For a package that must enter either mechanical continuation or possible-Ness Piece-3 validation, the controller must hold **one exact proved package source root**. `package_title` never identifies Q, on either route.

This matters for the `genuinely_open_for_ness` route as much as the mechanical one: a `review_signal_recorded` binds to `scope_root_path`, so a Ness route with no proved root has nothing to bind to and must refuse.

**`SEL-ROOT-IDENTIFIES` is unchanged by v1_9 and is not weakened.** What v1_9 corrects is the **contract that feeds it** — §9.3a — so that the result contract can no longer produce a reply this requirement must then refuse.

### 9.3a The actionable-root contract *(new in v1_9 — Correction 1)*

P-33 shows the exact defect: `SEL-ROOT-IDENTIFIES` demands a proved root on **both** routes, while the result contract required one on only **one** of them. A T1 result could therefore be validly received and impossible to route. **The contract is what moves; the requirement it serves does not.**

**`T1-ACTIONABLE-ROOT`.** A T1 selection result is **actionable** when its `controller_action` is either of exactly these two:

```
    prepare_claude_task
    hold_for_question_validation
```

**For an actionable result, `package_source_path` MUST be non-null and fully proved.** Null, absent, empty, whitespace-only, or unprovable is a **refusal** of the whole result — never a value the controller fills in, guesses, name-matches, derives, or carries as "to be determined".

**`T1-ACTIONABLE-ROOT-PROOFS`.** "Fully proved" means every one of the following, and they are exactly the proofs the installed validator and `SEL-ADMISSION` already perform for `prepare_claude_task` — **no new proof is invented, and none is dropped:**

| # | Proof | Owner |
|---|---|---|
| 1 | a **safe single-line** repository-relative path — no newline, no control character, no traversal, no symlinked component | installed `validate_source_paths()` / `resolve_repo_source_path()` |
| 2 | it **resolves to one exact permitted repository source** that really exists and is an ordinary regular file | installed resolution |
| 3 | it **equals its own canonical resolved path** — `resolve_repo_source_path(package_source_path) == package_source_path`, or the whole result refuses | installed rule (`nh_loop.py:5168-5201`) |
| 4 | it is **present in `source_paths_checked`** — the review must actually have read the root it names | installed rule |
| 5 | `source_paths_checked` passes **controller-owned governing-authority coverage** through `check_required_source_coverage()` against the controller's **own** preflight resolution, carried and re-matched under `SEL-AUTHORITY-BINDING-CARRIED` | installed rule + §9.5a |
| 6 | the review's **full check is complete** — `whole_check_complete` is true | installed rule |
| 7 | the controller **re-proves the root at admission and on every restart** — the root's `sha256` and byte length must still equal what they were when the selection was admitted, or the selection is **stale** | `SEL-ADMISSION` proofs 4–7, §9.5 |

**`T1-ACTIONABLE-ROOT-BOTH-LEVELS`.** The requirement holds at **both** proof levels of `SEL-TWO-LEVELS`, and neither substitutes for the other:

- **first-pass B6d** (§9.5a) — an actionable result with no proved root **never receives a valid `result_received` terminal** and is never custodied as usable bytes;
- **restart re-admission** (`SEL-ADMISSION`, §9.5) — an actionable result whose root no longer re-proves is **stale**, preserved as history, consumed by nothing.

**`T1-NONACTIONABLE-UNCHANGED`.** The four non-actionable classification/action pairs keep their installed semantics **exactly**, and **no root requirement is invented for them merely for symmetry**:

| `classification` | `controller_action` | Root requirement |
|---|---|---|
| `settled` | `report_settled` | **unchanged** — none added |
| `waiting_on_another_choice` | `wait_dependency` | **unchanged** — none added |
| `future_non_blocking` | `defer_future` | **unchanged** — none added |
| `later_building_or_disk_work` | `defer_build` | **unchanged** — none added |

None of those four routes a package into mechanical continuation or into question validation, so none of them needs a root to bind anything to, and inventing one would refuse honest answers the loop must be able to receive. **A higher rule that genuinely required a root for one of them would still govern; none does, and none is manufactured here.**

**`T1-ACTIONABLE-ROOT-NO-DERIVATION`.** Where an actionable result names no root, the controller **must not**:

- select one from `source_paths_checked` by name-matching `package_id`, `package_title`, or any other model-authored prose;
- select one from the governing-authority subset, the longest path, the newest file, the only candidate, or any other positional or heuristic rule;
- take one from a filename, a directory listing, a version suffix, a modification time, or a commit;
- accept one from a caller;
- carry a placeholder, a fallback label, or a shared scope identity that another package could also answer to.

**Every one of those is fabricated evidence.** The only admissible response is refusal.

**`T1-ACTIONABLE-ROOT-PROMPT`.** Because `PROMPT-BY-KIND` (§9.5b) sends the **installed** `NEXT_PACKAGE_PROMPT` semantics, the strengthened requirement must be visible to the reviewer in the bytes actually sent: the selection prompt states that **an actionable answer — `prepare_claude_task` or `hold_for_question_validation` — must name the exact `package_source_path` it selected, and that the non-actionable answers may leave it null.** This is a bounded correction of the same installed builder, inside the same `prompt_material_sha256` binding, and it creates **no second prompt builder** (`PROMPT-NO-SECOND-BUILDER`). A reviewer that genuinely cannot name a root has the four non-actionable answers and `whole_check_complete: false` available to it, and must use one of them rather than an actionable answer with no root.

### 9.4 Route by classification

| `classification` | `controller_action` | Continuation route |
|---|---|---|
| `mechanical_work`, `mechanically_implied` | `prepare_claude_task` | §12 mechanical route → T2 → T3 → T4 → T5 |
| `genuinely_open_for_ness` | `hold_for_question_validation` | §11 genuine-Ness route — **actionable: a proved root is REQUIRED** (`T1-ACTIONABLE-ROOT`, §9.3a; `SEL-ROOT-IDENTIFIES`, §9.3). It routes to **question validation only**, never to a design run and never to a direct question for Ness. |
| `settled` | `report_settled` | not selectable — completed history; the selection is not usable and the loop records the stop |
| `waiting_on_another_choice` | `wait_dependency` | not selectable — the named blocking dependency is preserved; `LOOP_WAITING_RECOVERING` or, where a person must act, `LOOP_NEEDS_USER_ACTION` |
| `future_non_blocking` | `defer_future` | not selectable — `LOOP_DESIGN_CONTINUATION_COMPLETE` if nothing else is actionable |
| `later_building_or_disk_work` | `defer_build` | **not selectable** — `LOOP_DESIGN_CONTINUATION_COMPLETE` (§22) |

**`SEL-ACTIONABLE-TWO-ROUTES`.** Exactly the first two rows are **actionable**, and they are the two `T1-ACTIONABLE-ROOT` governs. They are not the same route and are never collapsed into one: `prepare_claude_task` enters the **mechanical** route (§12), `hold_for_question_validation` enters the **question-validation** route (§11). **Both require a proved root; neither authorizes the other's destination.** The remaining four rows are **not selectable** and keep their installed semantics unchanged (`T1-NONACTIONABLE-UNCHANGED`).

**`SEL-FRONTIER`.** The selector returns the **actionable current design frontier** — not the next number, not the next filename, not the next item in any list. Priority is dynamic (workflow §5; eight-bundle global rule 1).

**`SEL-NO-HARDCODE`.** No package name, register id, addition number, bundle number or filename may be hard-coded in the selector, the controller, the worker, or the UI. Current source state is examined on **every** selection.

**`SEL-RESPECT-CLOSURE`.** Completed work is completed history. Addition 2 — Unified Durable Operation Kernel — already has a standalone `PACKAGE_COMPLETE` closure record on disk (§1.3). A selector walking the five-additions sequence positionally would start Addition 2 second. It must not: it must read the receipt, classify Addition 2 `settled` for its current standalone mechanical-design scope, and keep looking. **Equally it must not hard-code Addition 3** — whether Addition 3 is the frontier is answered from current files each time, and the answer may be some other package entirely.

**`SEL-SCOPE-HONESTY`.** A closure record closes exactly the scope it names. Addition 2's receipt closes "Addition 2's current standalone mechanical-design package only" and explicitly does not start Addition 3, complete any B-CYCLE, or authorize Register assignment. A narrow closure is never read as broad, and never as leaving its own scope open.

### 9.5 Controller admission — re-run on every restart, not just at first sight

**`SEL-ADMISSION`.** A custodied selector result is **not** operative merely because `result_schema_valid == true`. Every time the transition state is reconstructed from durable custody — first use, and every restart — the controller re-runs the **full** admission proof over the custodied bytes:

1. **Exact schema.** `validate_next_package_analysis()` over the custodied bytes, through the strict decoder, with the controller's own preflight-resolved authority set supplied. A duplicated key refuses the whole object.
2. **Classification / action pairing.** The pair must be one the installed mapping permits, and must be consistent.
3. **Route selectability.** The classification must be selectable for the route the loop is about to take (§9.4). `defer_build`, `defer_future`, `wait_dependency` and `report_settled` never admit a design run. **And selectable for *which* route is checked, not merely "selectable":** `prepare_claude_task` admits the mechanical route only, `hold_for_question_validation` admits the question-validation route only (`SEL-ACTIONABLE-TWO-ROUTES`, §9.4).
4. **A real, resolvable root for EVERY actionable result.** *(corrected in v1_9)* Where `controller_action` is `prepare_claude_task` **or** `hold_for_question_validation`, `package_source_path` must be non-null and must satisfy every one of `T1-ACTIONABLE-ROOT-PROOFS` (§9.3a): `resolve_repo_source_path(package_source_path) == package_source_path`; permitted repository file; no symlinked component; ordinary regular file. **A null or unprovable root on an actionable result refuses — it is never filled in, name-matched, derived, or carried forward** (`T1-ACTIONABLE-ROOT-NO-DERIVATION`). The four non-actionable actions are unchanged and gain no root requirement (`T1-NONACTIONABLE-UNCHANGED`).
5. **The root was actually read.** `package_source_path ∈ source_paths_checked` — for **both** actionable actions.
6. **Governing-authority coverage.** Re-measured through the same `check_required_source_coverage()` helper against the controller's own current preflight resolution — so a renamed or corrected authority file changes the requirement **with** the repository, not against it.
7. **Root bytes still re-prove.** The root's `sha256` and byte length must equal what they were when the selection was admitted. A change makes the selection **stale**.
8. **Derived scope differs from the accepted package.** `interview_package_scope_id(package_id, root) != scope_P`. Equality is a contradiction — a "next package" that is the package just accepted.
9. **`package_id` used only when settled.** Null is carried as null; nothing is invented to fill it.
10. **Model prose never becomes operative.** `package_title`, `simple_explanation`, `dependency` and `unknowns` are preserved as evidence and are never an instruction, a target path, a tool permission, an authority order, or a question to Ness.

**Only after all ten pass may a durable selector result become the current selection.** Points 3 and 6–8 are the continuation-specific additions; the rest is the installed validator re-run rather than remembered.

**`SEL-ADMISSION-NO-ACTIONABLE-ROOTLESS`** *(new in v1_9)*. There is **no** admission path, on any route, at any level, by which an actionable T1 result with no proved root becomes an admitted selection, an established scope, a review signal, a prepared task, a design run, or a question. Proof 4 refuses it, and nothing downstream may re-open what proof 4 refused. **An actionable rootless result is never `t.selection`.**

**Stale-selection handling.** A selection that was admitted and whose root later moved is not deleted and not rewritten: it is preserved as history, consumed by nothing, and the loop returns to `LOOP_SELECTION_REQUIRED`. A fresh selection episode may then be opened with a new request identity.

**Earlier-contract handling.** A durable T1 result that was **valid when it was received** under an earlier version of this contract, and that fails admission **only** because the strengthened `T1-ACTIONABLE-ROOT` requirement did not exist then, is a distinct and narrowly-bounded condition: it is neither ordinary staleness nor an ordinary refusal, and it has exactly one rule — **§9.7**. It is preserved unchanged, routes nothing, and consumes nothing.

### 9.5a The T1 first-pass admission branch (B6d) *(Correction 1)*

P-23 shows that a selection result cannot be left to `_generic_result_schema()`. It needs its own branch, and that branch must use the installed contract rather than a second one.

**`SEL-B6D-BRANCH`.** `_validate_result()` gains a dedicated branch for `work_item_kind == next_package_selection` `[proposed]`. That branch:

- validates the returned model object with the **existing** `validate_next_package_analysis()` semantics against the **existing** `NEXT_PACKAGE_ANALYSIS_REQUIRED_KEYS`;
- **additionally enforces `T1-ACTIONABLE-ROOT` (§9.3a)** — an actionable `controller_action` with a null or unprovable `package_source_path` is **not** schema-valid at B6d *(corrected in v1_9)*;
- **does not** add `result_schema_id` or `result_schema_version` to the model-authored object, and **does not** create a second next-package schema;
- returns `schema_valid` from that validation, so a valid installed result receives a valid `result_received` terminal instead of being stamped `result_invalid`.

**`SEL-B6D-ACTIONABLE-ROOT-IS-INVALID-OUTPUT`** *(new in v1_9; exhaustion route corrected in v1_10)*. An actionable rootless reply is an **invalid output**, and it takes the installed invalid-output route without exception: a `result_invalid` terminal, and the installed **bounded output-retry budget**. While that budget remains **available**, ordinary current-contract T1 output retry governs. Once it is **exhausted**, the position is the honest stop of **`T1-INVALID-OUTPUT-EXHAUSTION-STOP` (§9.6a)** — `LOOP_NEEDS_USER_ACTION`, null next command, zero further provider requests on the exhausted condition, and **no `close-open-consumption`, because a `next_package_selection` review opens no diagnosis consumption for that command to close** (§5 P-34). It is **not** a new selection episode, **not** a new request identity opened at will, and **never** the §9.7 earlier-contract condition — §9.7 applies only to a result that was **valid when received under an earlier contract**, never to one refused under the current one. This is what keeps a model that will not satisfy the contract from opening selector identities without end (§9.7 `SEL-LEGACY-NO-LOOP`).

**`SEL-B6D-STRENGTHENING-ONLY`.** This branch **only ever refuses more** than the installed validator; it never admits anything the installed validator refuses, adds no key to the model contract, and mutates `NEXT_PACKAGE_ANALYSIS_REQUIRED_KEYS` in no way (`SEL-LIFECYCLE-METADATA-STAYS-OUTSIDE`).

**`SEL-LIFECYCLE-METADATA-STAYS-OUTSIDE`.** The controller's own provider-request record may carry `result_schema_id` and `result_schema_version` as **lifecycle metadata** — `prepared.result_schema_id` is a controller-owned field of `provider_request_prepared`, not something the model states. Registering a schema id for the provider kind is therefore fine; **injecting those keys into the model-authored key set is not.** The same rule holds for T3 (§13.6a).

**`SEL-AUTHORITY-BINDING-CARRIED`.** `validate_next_package_analysis()` refuses outright when no controller-resolved governing-authority set is supplied, and measures coverage through `check_required_source_coverage(resolved_paths, required_files, …)`. That `required_files` object is the controller's **own preflight resolution** — it is not model output and must never be re-derived from the reply. The design therefore requires:

> The exact controller-resolved required-files binding the **prompt was built against** is carried into the prepared request as part of its `required_inputs_sha256` inventory — through `required_inputs_inventory()`'s `required_source_paths` and its `extra` slot — so it is **durable, authenticated and reconstructable** from the prepared record on any later process.
>
> **First-pass B6d validation and restart `SEL-ADMISSION` (§9.5 proof 6) must both measure authority coverage against that same carried binding**, re-resolved from the controller's own preflight at the moment of use and required to match the carried digest. A binding that no longer matches makes the result **stale** — preserved, consumed by nothing, and the phase re-entered — rather than silently validated against a different authority set.

**`SEL-TWO-LEVELS`.** The two proofs are **not** collapsed into one, and neither substitutes for the other:

| Level | When | Decides |
|---|---|---|
| **First-pass B6d** | inside `_observe_and_close()`, and again inside `process-custodied-provider-result` | only whether the provider result may receive a valid `result_received` terminal and be custodied as usable bytes |
| **Restart re-admission** (`SEL-ADMISSION`, §9.5) | every time `loop-status` or a continuation command wants to *use* those bytes | current root bytes, live authority coverage, scope inequality, route selectability, target freshness, decision binding — everything that can move after the result was produced |

A result that passes B6d has been *received honestly*. Only re-admission decides that it is *usable now*.

### 9.5b The provider-prompt rendering rule *(Correction 1)*

P-25 shows the generic supervisor prompt instructs every provider to emit two keys the T1 and T3 contracts forbid. The provider must never be told to produce a reply its own contract refuses.

**`PROMPT-BY-KIND`.** `_supervisor_provider_prompt()` gains one bounded, closed dispatch on `request.provider_kind`, and nothing else about it changes:

| Provider kind | Prompt bytes sent |
|---|---|
| `codex_next_package_selection` `[proposed]` | the **installed** `NEXT_PACKAGE_PROMPT` semantics — the same review contract and the same expected model result object the installed `next-package` review uses, carrying the two bounded text corrections of `SEL-INSTALLED-CONTRACT` (§9.1): the current authoritative Decision Defaults as authority #2 (§10.3), and the actionable-root requirement (`T1-ACTIONABLE-ROOT-PROMPT`, §9.3a) |
| `codex_next_design_task_preparation` `[proposed]` | the **installed** `build_prepare_task_prompt(analysis, decision_binding)` output — the same stage-two prepared-task contract |
| `gpt_question_validation` (installed kind) | the **installed** `build_question_validation_prompt(...)` output (§12.3e) |
| `gpt_question_coverage_review` (installed kind) | the **installed** `build_question_coverage_review_prompt(binding_block)` output (§12.3e) |
| **every other kind** | **unchanged** — the current generic instruction, byte for byte, including the acceptance-explanation preamble |

**`PROMPT-NO-LIFECYCLE-SENTENCE`.** The generic paragraph requiring `result_schema_id` and `result_schema_version` is **not prepended** to any of the four specialized prompts. The controller-owned lifecycle schema id and version remain what they already are: fields of `provider_request_prepared` and of the prepared record's own inventory. **They never become model-authored result fields**, for any of the four kinds (`SEL-LIFECYCLE-METADATA-STAYS-OUTSIDE`).

**`PROMPT-CONTROLLER-BUILT-AND-BOUND`.** The bytes actually sent are controller-built by the installed builders and are inside the request's `prompt_material_sha256` proof, through `prompt_material_inventory()`'s `extra` slot. `_supervisor_provider_material()` already recomputes that digest and refuses on mismatch before one byte leaves the machine, so a prompt that is not the one the request durably bound cannot be sent.

**`PROMPT-NO-SECOND-BUILDER`.** No second next-package prompt, no second task-preparation prompt, no second Piece-3 prompt. The installed builders are reused; only the selection of which builder runs is new.

### 9.5c The required-input binding, made reachable and reconstructable *(Correction 2)*

P-26 shows `build_prepared_request()` already accepts `extra_inputs` and that both ends are unwired. The correction is that seam and nothing more.

**`EXTRA-INPUTS-SEAM`.** One existing-lifecycle parameter is threaded through one existing call:

```
  commands._dispatch(..., extra_prompt=..., extra_inputs=...)      <- gains the kwarg
      -> engine.build_prepared_request(..., extra_inputs=...)      <- ALREADY accepts it
          -> engine.required_inputs_sha256(context, work_item, extra_inputs)
                                                                   <- ALREADY threads it
  nh_loop._supervisor_provider_material(context, request, errors)
      -> required_inputs_inventory(context, work_item, extra)      <- gains the same extra
      -> recomputes required_digest and REFUSES on mismatch        <- ALREADY does this
```

**No second request identity is invented.** `required_inputs_sha256` remains the authority, and it is already one of the seven inputs of `provider_request_identity`, so a changed extra changes the request identity — which is exactly the protection wanted.

**`EXTRA-INPUTS-CONTENT`.** What each kind binds:

| Stage | Extra input binds |
|---|---|
| **T1** `next_package_selection` | the exact controller-owned required-files / authority-coverage object the `NEXT_PACKAGE_PROMPT` validation is measured against, so that validation is reproducible |
| **T3** `next_design_task_preparation` | the above, **plus** the exact admitted T1 selection object, the selected root and scope, and the settled-decision material `validate_prepared_task()` requires |
| **T2** `question_validation` / `coverage_review` | the exact frozen pre-call Piece-3 source, pagination and standing requirement the real Piece-3 prompt was built from (§12.3e) |
| **T4** `initial_design` | unchanged from v1_4 — the prepared task's target path and specification digest (`INIT-ADMISSION` I8) |

**`EXTRA-INPUTS-RECONSTRUCTION`.** The design does not merely assert that the extra is durable. It states the one mechanically precise rule by which a later process obtains the same object:

> **Deterministic reconstruction, then digest equality.** Every value in the extra is **re-derived** by the controller from (a) the authenticated journal and (b) the frozen source evidence the prepared record already binds — never remembered, never carried in process state, never supplied by a caller. The reconstructed inventory is then hashed and **must equal the `required_inputs_sha256` in the durable prepared record**.
>
> This is the installed `_supervisor_provider_material()` check, extended to cover the extra it currently omits. Its refusal path already exists and already fires before dispatch.

**No new journal body field is introduced**, and the reason is stated rather than assumed: every value the extra needs is already derivable from evidence the journal authenticates — the package binding fields on the operation's own start, the frozen source binding and manifest digests, the admitted T1 selection's custodied bytes (themselves digest-bound by `result_custody_identity`), the settled-decision binding derived per scope, and the controller's own current preflight resolution of the authority set. Adding a body field would duplicate facts already provable and would create a second place for them to disagree.

**`EXTRA-INPUTS-STALE-NOT-SILENT`.** If reconstruction yields a **different** object — the authority set moved, the admitted selection changed, the frozen source is no longer the one bound, the standing or pagination position moved — the digest differs, and the saved result is **stale**: preserved as history, consumed by nothing, and its phase re-entered. **It is never silently accepted against the new inputs**, and the mismatch never becomes a reason to call the provider again inside the same request identity.

### 9.5d The `next_package_selection` work item *(Correction 2)*

P-30 shows a missing matrix row makes a kind unbuildable. This is its row.

**`WIM-SELECTION`.** One row, **variant `None`** — there is exactly one shape, so no variant name is needed and `check_work_item_object()`'s single-row resolution applies.

| Field | Requirement | Why |
|---|---|---|
| `blocking_finding_refs` | `[]` | nothing has been audited; there are no findings |
| `audit_identity` | `0` | no audit precedes a navigation review |
| `checkpoint_identity` | `0` | no batch checkpoint is involved |
| `diagnosis_event_sha256` | `0` | no diagnosis authority |
| `diagnosis_strategy_sha256` | `0` | same |
| `strategy_novelty_key` | `0` | same |
| `correction_specification_sha256` | `0` | **correction-only authority; never placed on a non-correction work item** |
| `target_candidate_path` | `0` | a selection produces no file and names no target |
| `authorized_next_lifetime_round` | `0` | not a correction round |
| `authorized_batch_number` | `0` | same |
| `authorized_round_in_batch` | `0` | same |
| `routed_signal_refs` | `[]` | a navigation review consumes no routed signal |
| `validation_set_id` | `0` | none exists; T1 runs before any Q validation |
| `piece3_standing_sha256` | `0` | selection is not a Piece-3 operation and carries no standing authority |

The shape is deliberately the `design_audit` / `acceptance_explanation_content` shape: one bound candidate, no findings, no target, no authority, no round authorisation.

**`WIM-SELECTION-BUILDER`.** One controller-owned builder, `next_package_selection_work_item(context, candidate)` `[proposed]`, returns the exact object above from `_base_work_item(context, candidate, "next_package_selection")` plus the null and empty fields, and returns `(obj, work_item_identity(obj))`. **There is no alternate identity path**: nothing else may construct this object or derive this identity.

Its bound candidate is **P's candidate** under P's current established binding — T1 runs from the terminal-accepted package (`TB-NO-PREMATURE-Q`), which is also why its identity can never collide with a T3 item bound to Q's root.

### 9.6 The honest stop

A single selector review may legitimately find no actionable frontier. That is an answer, not a failure to try harder.

- nothing actionable, or everything `future_non_blocking` → `LOOP_DESIGN_CONTINUATION_COMPLETE`, with the proved reason preserved;
- `later_building_or_disk_work` → `LOOP_DESIGN_CONTINUATION_COMPLETE` (§22);
- `waiting_on_another_choice` → the named dependency is preserved; `LOOP_WAITING_RECOVERING`, or `LOOP_NEEDS_USER_ACTION` where a person must act;
- a review that cannot complete its own check (`whole_check_complete` false, or a validator refusal) → `LOOP_WAITING_RECOVERING` with a durable dependency on the installed carrier and the worker's ordinary bounded backoff. It never becomes a hot re-selection loop: the retry series and the episode/attempt caps bound it exactly as they bound every other provider dependency, and repeated exhaustion routes to `LOOP_NEEDS_USER_ACTION` through the installed `provider_availability_episode_exhausted_recorded` path rather than to silence.
- an **actionable** reply that names no proved root (`T1-ACTIONABLE-ROOT`, §9.3a) → **not** an honest stop *in this list* and **not** a new selection episode: it is an **invalid output** on the installed bounded output-retry route (`SEL-B6D-ACTIONABLE-ROOT-IS-INVALID-OUTPUT`, §9.5a). While the budget remains available, ordinary bounded retry governs; **once it is exhausted the position becomes its own honest stop — `T1-INVALID-OUTPUT-EXHAUSTION-STOP` (§9.6a): `LOOP_NEEDS_USER_ACTION`, null next command, and no further request on the exhausted condition** — never an unbounded series of fresh selector identities *(corrected in v1_10: v1_9 routed this to `close-open-consumption`, which a `next_package_selection` review can never satisfy — §5 P-34)*.

**No stop is ever reported as a success, and a long-running or many-attempt selection never becomes a selection.**

### 9.6a T1 invalid-output exhaustion — the honest stop *(new in v1_10 — the v1_10 correction)*

§9.5a puts a contract-violating T1 reply on the installed bounded output-retry budget, and that is right. What v1_9 then said about the **end** of that budget was not: it named `close-open-consumption`, a command that a `next_package_selection` review can never satisfy, because it closes an open **diagnosis** consumption that such a review never opens (§5 P-34). **This section states what actually happens instead. It is the whole of the v1_10 correction, and it is deliberately the narrowest object that removes the contradiction.**

**`T1-INVALID-OUTPUT-EXHAUSTION-STOP`.** The rule has five parts, and all five are required.

#### A — While the installed bounded output-retry budget remains AVAILABLE

Nothing changes at all. Ordinary current-contract T1 output retry governs, and every existing rule applies to it unaltered:

- the existing request / retry / provider lifecycle rules govern the attempt;
- the **special §9.7 earlier-contract permission is NOT reopened** — it stays consumed at `provider_request_prepared` (`SEL-LEGACY-ONE-SHOT`, §9.7.4);
- **no second legacy replacement is created**, under any budget position (`SEL-LEGACY-NOT-A-NEW-LEGACY`);
- uncertainty remains **reconciliation-first** (`PROV-NO-REDISPATCH`, §19.3);
- **all existing caps, backoff and identity rules remain exactly as installed** — the per-episode attempt cap, the per-work-item episode machinery, the `retry_series_key` backoff, the execution timeout, the one-open-request rule, and the request-identity derivation.

**No retry count, wait, timer, deadline, real-change category or B9 policy is invented, altered or reinterpreted here** — see part C.

#### B — Once the installed bounded T1 output-retry budget is EXHAUSTED

The following are each forbidden, and each is forbidden for its own stated reason:

| Forbidden once exhausted | Why |
|---|---|
| **NO further selector/provider request is dispatched on the exhausted condition** | the condition *is* that the bounded budget ran out; one more request on it is precisely the unbounded retry the accepted design exists to prevent (`SEL-LEGACY-NO-LOOP`, §9.7.4) |
| **NO `close-open-consumption` command is owed** | there is no open diagnosis consumption for it to close, and it would truthfully refuse (§5 P-34) |
| **NO `diagnosis_strategy_consumption_started` is invented** | there was no diagnosis; manufacturing the transaction to make a command callable is fabricated state |
| **NO `diagnosis_strategy_consumption_terminated` is invented** | there is nothing truthful to terminate, and nothing truthful to put in its body |
| **NO fake correction specification, diagnosis identity, strategy identity or blocking-finding authority is manufactured** | `WIM-SELECTION` pins every one of those fields to `0` or `[]` **because none of them exists** (§9.5d); filling them in would be fabricated authority |
| **NO new event type is introduced** | §7.6's proof that the continuation needs none still holds, and this stop needs none |
| **NO new state store is introduced** | the position is derived, not stored (part C) |
| **NO eighth continuation execution command is introduced** | the set is closed at seven (`CONTINUATION-SET-CLOSED-AT-SEVEN`, §7.5), and an eighth would not create the missing consumption anyway |

**`T1-NOT-A-CONSUMPTION`.** The reason all of the above is coherent, stated once so a later implementer cannot re-derive the mistake:

> **A T1 next-package-selection review is NOT a correction-strategy consumption.**
>
> The fact that the installed correction/diagnosis recovery path uses `close-open-consumption` **does not make that command a universal provider-terminal closer.** It closes one specific, real, open transaction of the correction machinery, and its legitimate installed use there is **preserved, named and untouched** by this file (§7.5, §16.2).

The T1 request/result is **already terminal under its OWN lifecycle**: a `result_invalid` terminal **is** a terminal provider result. For `next_package_selection`, the custody/terminal pair is **terminal-only closed** under the existing read-only closure semantics (`CLOSURE-READONLY` and `CLOSURE-INVALID-TERMINAL-IS-TERMINAL`, §7.6a). **There is therefore no separate diagnosis-consumption closure transaction to perform, and nothing is left open by not performing one.**

The distinction, in one table, because this is the exact confusion that produced the defect:

| | Installed correction/diagnosis path | T1 `next_package_selection` |
|---|---|---|
| opens `diagnosis_strategy_consumption_started`? | **yes** — that is what it is for | **no**, never |
| holds a diagnosis identity, strategy digest, novelty key, blocking findings, correction specification? | **yes** | **no** — all `0` / `[]` by `WIM-SELECTION` |
| is `close-open-consumption` meaningful, callable and truthful? | **yes — preserved unchanged** | **no — it would refuse** |
| what closes its provider result? | the consumption's own termination, plus the installed lifecycle | the **terminal itself** (`CLOSURE-READONLY`) |
| what happens when its bounded output-retry budget is exhausted? | the installed correction-path behaviour, unchanged | **this section** |

#### C — The exhausted position is RE-DERIVED, never remembered

**`T1-EXHAUSTION-DERIVED`.** The position is a **pure derivation over existing durable evidence**, performed freshly on every entry and every restart, from exactly these sources and no others:

1. the **authenticated current-contract T1 request(s)** for this transition;
2. their **`provider_request_terminal_recorded`** outcome(s);
3. their **matching custody / evidence** where applicable;
4. the **installed `bounded_output_retry_budget()` calculation** for that work item, provider kind and episode — the same installed function the installed recovery table already consults;
5. the existing **`supervisor_operation_completed` / dependency evidence** those attempts already generated.

And from nothing else:

- **no process-memory flag**;
- **no marker**;
- **no mutable counter beyond the already-governing installed budget**;
- **no second source of truth**, and no second store.

It is carried in `post_acceptance_transition_state()` as the derived field `t1_output_retry_exhausted` `[proposed]` (§17.2) — **derived, never stored**, exactly as `legacy_replacement_consumed` already is.

#### D — What the loop reports, and what it must never claim

When that durable evidence proves **both**:

```
    latest relevant T1 output = invalid / oversize-invalid as governed
    AND
    bounded output-retry budget = exhausted
```

then the loop reports:

```
    loop_state        = LOOP_NEEDS_USER_ACTION
    loop_next_command = null
```

**No new loop state is invented** (§9.6c). The plain-language reason must say, in substance:

> **N.H received unusable next-package output through all currently allowed bounded attempts, so automatic selection stopped rather than opening another request.**

**`T1-EXHAUSTION-NO-FALSE-CLAIM`.** The report must **not** claim, in any wording, in any field, or in any UI surface:

- that a **diagnosis consumption was closed**;
- that **`close-open-consumption` ran**;
- that a **provider outcome is uncertain** — it is not; the terminal is durable;
- that the **old earlier-contract request reopened** — it did not, and it never can (`SEL-LEGACY-ONE-SHOT`);
- that the **package was selected** — none was;
- that the **design loop completed successfully** — it stopped.

A stop is a stop. It is neither a success nor a hidden failure, and §21.3 already forbids the UI from dressing it as either.

#### E — Restart stability

**`T1-EXHAUSTION-RESTART-STABLE`.** Because the position is derived (part C) rather than stored, a restart over **identical authenticated evidence** derives the **identical** `LOOP_NEEDS_USER_ACTION`, with:

- **zero appends**;
- **zero provider calls**;
- **zero new request identities**.

**And it must not repeatedly invoke `continue-design-loop` merely to rediscover the same exhausted condition.** That is exactly why the guard sits in §7.4 **before** the `t.selection is None` fall-through: without it the loop would return `LOOP_SELECTION_REQUIRED` / `continue-design-loop` for ever, re-entering a command whose only remaining move is refused, while reporting a position that is not the truth.

#### The B9 meaning this preserves, and does not redesign

**`T1-EXHAUSTION-IS-B9-EXHAUSTION`.** This stop is the accepted B9 exhaustion meaning applied at the one seam that needed it stated, and **nothing about B9 is changed**:

- retries **stop**;
- it **says why**;
- the **work and evidence stay preserved**;
- **unfinished state stays preserved**;
- **no fake success**;
- **no hidden failure**;
- **no endless retry**;
- **continuation after exhaustion requires the ordinary separately governed real-change / retry rules rather than repetition alone.**

**`T1-EXHAUSTION-NO-B9-REDESIGN`.** v1_10 invents **no** new retry count, wait, timer, deadline, real-change category or B9 policy; changes **no** accepted B9 retry value; and **does not redesign B9**. It reads the installed budget and reports the truth about where it ended.

### 9.6b Saved T1 result bytes are protected by their evidence, not by their terminal form *(new in v1_10 — clarification, not new policy)*

A live implementation correction against the accepted v1_9 design surfaced a second, smaller defect **against v1_9's own already-settled custody rule** rather than against a gap in it: a durable T1 custody whose saved bytes could not be re-verified could **silently read as absent**, after which the loop would ask a model again for an answer it had **already received and saved**. v1_9 already forbids exactly that. This subsection states the rule in the one form that makes the mistake unwritable.

**`T1-CUSTODY-UNVERIFIABLE`.** It applies to **EVERY** durable `next_package_selection` custody whose exact bytes are part of authenticated provider-result evidence — **regardless of whether its matching terminal is**:

```
    result_received
    result_invalid
    or another terminal form that truthfully carries or requires saved custody
```

Where such saved bytes are **required by the durable record** and **fail exact `engine.custodied_bytes()` re-verification** against the recorded `result_byte_length` and `result_sha256`:

```
   provider_result_custody_unverifiable
     -> LOOP_SAFETY_HOLD
     -> loop_next_command = null
     -> ZERO provider calls
```

**`T1-CUSTODY-NEVER-ABSENT`.** **The custody must NEVER be treated as absent merely because its terminal is `result_invalid`.** An invalid terminal says the **model's answer did not satisfy the contract**. It does not say the bytes were never received, and it does not say they may now be quietly forgotten. *Closed* (§7.6a `CLOSURE-INVALID-TERMINAL-IS-TERMINAL`) means **nothing further is owed**; it never means the evidence stops being evidence.

**Precedence, stated because two stops are now reachable from the same T1 position.** `T1-CUSTODY-UNVERIFIABLE` **outranks** `T1-INVALID-OUTPUT-EXHAUSTION-STOP`. Where a T1 custody fails re-verification, the answer is `LOOP_SAFETY_HOLD` — **not** the milder `LOOP_NEEDS_USER_ACTION` — and §7.4 evaluates the two guards in exactly that order. **Safety outranks a practical stop, and the §9.7 permission is not even derived while a T1 custody fails to re-verify**, so lost saved evidence can never become a loophole (`SEL-LEGACY-NOT-CUSTODY-LOSS`, §9.7.2).

**This is a CLARIFICATION of already-settled semantics, and introduces no new concept:**

| Already-settled source | What it already says |
|---|---|
| §25 `R109` | unverifiable custody `SAFETY_HOLD`s and **never** gains a replacement call |
| §9.7.2 `SEL-LEGACY-NOT-CUSTODY-LOSS` | the earlier-contract rule is **unavailable** where custody fails re-verification; losing saved evidence is never a licence to manufacture replacement evidence |
| §14.6 `CUSTODY-UNVERIFIABLE-HOLD` | once custody exists, an inability to re-verify those exact bytes is **not** provider absence, **not** permission to re-ask, and **not** cured by aborting anything |
| §19.3 | a result already received and saved whose bytes no longer re-verify is **not a reconciliation question at all** |
| §28 | *"losing saved evidence is never permission to manufacture replacement evidence"* |

**`T1-CUSTODY-NO-RESTORATION-INVENTED`.** **No restoration mechanism is invented, designed or authorized here.** §14.6 `CUSTODY-UNVERIFIABLE-RESUME` and §26 item 6 keep that question exactly where they left it: until a **separately accepted** mechanism exists, the position is a safety hold that a person resolves, and recovery may resume only from **those same bytes**.

### 9.6c No new loop state — the outward stop is the one already settled *(new in v1_10)*

**`T1-EXHAUSTION-NO-NEW-STATE`.** v1_10 introduces **no new `loop_state` value and no new `loop_next_command` value.** The §7.3 table is unchanged.

v1_9 already settled the outward behaviour this correction preserves: **repeated bounded selection/output failure eventually stops the automatic loop at `LOOP_NEEDS_USER_ACTION`** — see §9.6's dependency bullet, where repeated episode exhaustion already routes there through the installed `provider_availability_episode_exhausted_recorded` path. **That outward answer is not what v1_10 changes.**

**What v1_10 changes is exactly one thing: the impossible internal claim that `close-open-consumption` performs that closure.** The stop was already the right stop. The route named to reach it could not be executed, and now it is stated as what it is — a derived position, owing no command and no append.

**And what v1_10 refuses to change:** it does not invent a new retry count, wait, timer, deadline, real-change category or B9 policy; it does not redesign B9; it does not alter the accepted B9 retry values; and it does not touch the accepted B9 real-change meaning (§9.6a, `T1-EXHAUSTION-NO-B9-REDESIGN`).

### 9.7 The earlier-contract transition rule *(new in v1_9 — Correction 2)*

§9.3a removes the contradiction for every future T1 result. It does **not**, by itself, say what happens to a T1 result that **already exists**, was **already valid when it was received**, and is now mechanically non-operative. P-33(c) shows that none of the installed routes describes that condition. **This section states the one bounded rule that does, and it is deliberately the narrowest object in this correction.**

#### 9.7.1 What is preserved, absolutely

**`SEL-LEGACY-PRESERVE`.** The earlier-contract result and everything around it are **truthful authenticated history and are preserved exactly**:

- the `provider_request_prepared`, `provider_dispatch_begun`, `provider_result_custody_recorded`, `provider_request_terminal_recorded` and `supervisor_operation_completed` events are **not** deleted, rewritten, re-headed, superseded, back-dated, re-classified or annotated;
- the custodied **result bytes are not altered** and its **`package_source_path` is not changed** — a null stays null;
- the record continues to say exactly what is true: **the request completed; its result bytes were saved and re-verify; those bytes were valid under the contract in force when they were received.**

**`SEL-LEGACY-NO-ROOT-FABRICATION`.** No root is inferred, derived, name-matched, reconstructed, or manufactured for it — not from `source_paths_checked`, not from the governing-authority subset of that list, not from `package_id` or `package_title`, not from a filename, and not from any other field. **`source_evidence` is never derived from some different field and presented as though it were the selected root.** `T1-ACTIONABLE-ROOT-NO-DERIVATION` applies here without exception.

**`SEL-LEGACY-NO-SIGNAL`.** The earlier-contract result is **never routed into `review_signal_recorded`**, never becomes an admitted Q, never establishes a scope, never opens a Piece-3 stage, and **its `simple_explanation` is never used as, or turned into, a question for Ness.** It routes nothing at all.

#### 9.7.2 The condition — mechanically and durably distinguishable

**`SEL-LEGACY-CONDITION`.** The rule below is available **only** where the controller freshly proves **every one** of these, from the current authenticated journal and current byte re-proofs, at the moment of use:

| # | Required proof | Why it is here |
|---|---|---|
| **1** | the old provider request is **definitively completed** — a durable terminal recording `result_received` for that exact `provider_request_identity` — and its **result custody re-verifies now** through `engine.custodied_bytes()` against the recorded `result_byte_length` and `result_sha256` | separates this from every uncertain-outcome and lost-custody position |
| **2** | its result was **accepted under the earlier contract** — it received a valid `result_received` terminal, and re-running the **earlier** contract over the saved bytes still returns valid | proves this is a contract change, not a bad reply |
| **3** | it **fails current admission specifically and only** because an **actionable** `hold_for_question_validation` (or `prepare_claude_task`) result lacks the newly-required proved root — `T1-ACTIONABLE-ROOT` is the sole failing proof | a result failing for any other reason is **not** this condition |
| **4** | **no current-contract replacement T1 request for that transition exists — in ANY phase.** Not prepared, not dispatched, not custodied, and not terminal of any kind, valid or invalid. **Existence of the durable `provider_request_prepared` alone already fails this proof**, so a crash between preparing and dispatching can never re-open the permission | this is the consumption fence of §9.7.4 |
| **5** | the ordinary preconditions still hold — acceptance freshly re-proved (§6.3), `CPB-SINGLE-TRANSITION` holds, no open provider request, no contradiction under §23 | nothing here bypasses the ordinary gates |

**Zero, or any one of the five unprovable → the rule does not apply**, nothing is appended, and no provider is contacted.

**`SEL-LEGACY-NOT-UNCERTAINTY`.** This condition is **not** an uncertain provider outcome, and the two can never be confused: an uncertain outcome has **no** durable terminal, while proof 1 requires one. `PROV-NO-REDISPATCH` and §19.3 keep governing every uncertain dispatch **unchanged** — reconcile first, never a second call because the outcome is unknown.

**`SEL-LEGACY-NOT-CUSTODY-LOSS`.** It is **not** lost, unreadable or unverifiable custody, and the two can never be confused: proof 1 requires the saved bytes to **re-verify now**. Where they do not, `CUSTODY-UNVERIFIABLE-HOLD` (§14.6) governs **unchanged** — `SAFETY_HOLD`, zero replacement calls, every durable record preserved — and **this rule is unavailable**. **Losing saved evidence is still never a licence to manufacture replacement evidence, and this section creates no loophole in that.**

**`SEL-LEGACY-CONDITION-NOT-A-NAME`.** The condition is **contract state**, never a package name. **No package id, package title, addition number, bundle number, register id, filename, event sequence number or frontier is hard-coded** into it, in the controller, the worker, the selector prompt or the UI (`SEL-NO-HARDCODE`). A concrete earlier-contract lineage may be **recognised** by the proofs above for migration purposes — that is what proofs 1–4 do — but **the design rule is the contract-state condition and nothing else**, and it would apply identically to any other result that ever reached the same state.

#### 9.7.3 What the rule permits — exactly one thing

**`SEL-LEGACY-CONTRACT-REPLACEMENT`.** Where `SEL-LEGACY-CONDITION` is freshly proved, the controller may perform **one** ordinary current-contract T1 selection.

This is admissible for one reason, and the design states it rather than assuming it: **`next_package_selection` is a bounded READ-ONLY navigation review with no effect outside its own custodied result** (`PROV-READONLY-EFFECTFREE`, §19.3), and the old request is **PROVED COMPLETED** rather than uncertain. There is no in-flight request to duplicate, no side effect to repeat, and nothing to reconcile — the only open question is which package the loop is on, and that is exactly what a fresh read-only review answers.

**`SEL-LEGACY-NEW-IDENTITY`.** The replacement is a **new current-contract selection, not a re-dispatch**:

- the **old `provider_request_identity` is never reused, never re-dispatched, never re-opened, and never has a second dispatch, custody or terminal appended to it**;
- a **fresh provider request identity** is derived in the ordinary installed way, from the ordinary inputs, with its own prepared record, its own dispatch serial, its own custody and its own terminal;
- the old request's records stay exactly where they are, as history, for ever.

**`SEL-LEGACY-FRESH-FRONTIER`.** The replacement performs a **fresh current-source check** and is an ordinary `SEL-FRONTIER` selection in every respect. It **must not** assume, seed, prefer, pre-fill or carry forward the earlier result's `package_id`, `package_title`, `classification`, `controller_action`, `dependency` or `source_paths_checked`. **The earlier frontier is not present truth**, and the fresh selection may legitimately prove a **different** package, a different classification, or an honest non-actionable stop (§9.6). Its answer is whatever the current sources prove.

**`SEL-LEGACY-ORDINARY-AFTERWARDS`.** The replacement is, from the instant it is prepared, an **ordinary** current-contract T1 selection. Every ordinary rule applies to it with no exception and no softening: `PROMPT-BY-KIND`, `EXTRA-INPUTS-SEAM`, the dedicated B6d branch including `T1-ACTIONABLE-ROOT`, `SEL-ADMISSION`'s ten proofs, the installed bounded output-retry budget, the installed episode and attempt caps, the `retry_series_key` backoff, `PROV-NO-REDISPATCH`, reconciliation-first on uncertainty, and every §23 fail-closed rule.

#### 9.7.4 The consumption fence — why this can never loop

**`SEL-LEGACY-ONE-SHOT`.** The permission is consumed **deterministically, by durable evidence, not by a counter, a flag, a marker, a memory or a second store.**

> **The permission is consumed the moment any current-contract replacement T1 request for this transition becomes durable — that is, the moment its `provider_request_prepared` is appended.** Not when it is dispatched, not when it is custodied, and not when it terminates. **Existence is consumption.**

Binding the fence to the **earliest** durable record is deliberate, and the design states why: a fence tied to a terminal would re-open the permission at exactly the positions where re-opening is most dangerous — a crash after preparing, a crash after dispatching, an uncertain outcome — and would hand a second replacement to precisely the states that `PROV-NO-REDISPATCH` and `SEL-LEGACY-NOT-UNCERTAINTY` exist to refuse. **The first durable append closes it, permanently.**

`SEL-LEGACY-CONDITION` proof 4 is that fence, and it is evaluated by the same pure derivation on every entry and every restart (§17.2). Concretely:

| After the replacement attempt | Proof 4 | The rule |
|---|---|---|
| terminal `result_received`, valid and admitted | **fails** | consumed — the ordinary route continues (§9.8) |
| terminal `result_received`, valid, later **stale** | **fails** | consumed — ordinary stale-selection handling; `LOOP_SELECTION_REQUIRED` under the ordinary rules |
| terminal `result_invalid` / `result_oversize` — including an **actionable rootless** reply | **fails** | consumed — the installed **bounded output-retry** budget governs; **exhausted → the honest stop of `T1-INVALID-OUTPUT-EXHAUSTION-STOP` (§9.6a): `LOOP_NEEDS_USER_ACTION`, null next command, zero further requests on the exhausted condition, and no `close-open-consumption`** *(corrected in v1_10)* |
| dispatched, outcome **uncertain**, no terminal | **fails** *(a request exists)* | consumed — **`reconcile-provider-request` first**, never a second call |
| prepared, never dispatched | **fails** *(a request exists)* | consumed — `SAFE_TO_RETRY` under the **same** prepared identity |

**`SEL-LEGACY-NO-LOOP`.** The loop this fence exists to prevent is stated explicitly so a later implementation cannot reintroduce it:

```
   old rootless result
     -> fresh selection
       -> another bad result
         -> ANOTHER "fresh legacy replacement"
           -> another bad result
             -> ...
```

That sequence is **impossible under this design**, and each arrow is closed by a named rule:

1. **A second replacement is never available.** Proof 4 fails for ever once any replacement request exists (`SEL-LEGACY-ONE-SHOT`).
2. **A bad new result is never a new "legacy" result.** `SEL-LEGACY-CONDITION` proof 2 requires validity **under the earlier contract**; a reply refused under the **current** contract has never satisfied it (`SEL-LEGACY-NOT-A-NEW-LEGACY`).
3. **A bad new result never routes.** It is not admitted, no root is fabricated for it, and it becomes no signal and no question — exactly as for the earlier one.
4. **Repeated contract failure is bounded output-retry, not new identities.** `SEL-B6D-ACTIONABLE-ROOT-IS-INVALID-OUTPUT` puts it on the installed budget; **exhaustion reaches the honest stop of `T1-INVALID-OUTPUT-EXHAUSTION-STOP` (§9.6a) — `LOOP_NEEDS_USER_ACTION` with a null next command, owing no `close-open-consumption` and no append** *(corrected in v1_10)* — and repeated episode exhaustion likewise routes to `LOOP_NEEDS_USER_ACTION` through the installed `provider_availability_episode_exhausted_recorded` path (§9.6). **No new selector identity is opened merely because a model would not satisfy the contract**, and **no diagnosis consumption is created to give the stop a command to call.**
5. **Uncertainty is still reconciliation-first**, and custody-unverifiable is still `SAFETY_HOLD` with zero replacement calls.

**`SEL-LEGACY-NOT-A-NEW-LEGACY`.** A current-contract result that violates `T1-ACTIONABLE-ROOT` is **never** treated as an earlier-contract result, silently or otherwise. The earlier-contract condition is closed and cannot be re-entered: it is defined by a result that was valid **under a contract no longer in force**, and no result produced under the current contract can ever have that property.

#### 9.7.5 What the loop reports meanwhile

No new loop state is introduced. While `SEL-LEGACY-CONDITION` holds and no replacement request exists, the earlier-contract result is **not** `t.selection` (`SEL-ADMISSION-NO-ACTIONABLE-ROOTLESS`), so the ordinary derivation of §7.4 reaches `t.selection is None` and returns:

```
   LOOP_SELECTION_REQUIRED , continue-design-loop
```

with the earlier-contract result preserved and named in the honest detail. **That is the ordinary position for "no admitted selection", reached honestly** — the transition rule decides only that this one entry into it is permitted, bounded and consumed, and it invents no state, no command and no store.

### 9.8 After a valid replacement result *(new in v1_9)*

A current-contract replacement result that is admitted under all ten `SEL-ADMISSION` proofs — including `T1-ACTIONABLE-ROOT` — is an **ordinary admitted selection with no residual special standing whatsoever**. Its route is decided by §9.4 exactly as any other:

| Replacement result | Route — **unchanged from v1_8** |
|---|---|
| `mechanical_work` / `mechanically_implied` + `prepare_claude_task` + **proved root** | the existing §12 mechanical route, unchanged: T2 → T3 → T4 → T5 → T6 |
| `genuinely_open_for_ness` + `hold_for_question_validation` + **proved root** | the existing §11 genuine-Ness route, unchanged and in full: `review_signal_recorded` → independent question validation → independent question-coverage review → **only if still genuinely open** → `NEEDS_NESS_DECISION` |
| `settled` / `waiting_on_another_choice` / `future_non_blocking` / `later_building_or_disk_work` | the existing §9.4 and §9.6 stop / wait / defer semantics, unchanged |

**`SEL-LEGACY-NO-PRIVILEGE`.** A replacement selection receives **no** shortcut, no pre-cleared Piece-3 stage, no inherited scope, no inherited routed signal, no reduced admission and no elevated trust. It proves everything from the beginning, exactly as a first selection does. **The fact that it followed an earlier-contract result is history, and history authorizes nothing.**

---

## §10 — THE DECISION DEFAULTS AUTHORITY *(Correction 1A)*

### 10.1 Master V10 settles this — it is not an open Ness decision

`NH_MASTER-20_CORRECTED_v10.md`, the highest authority in the project, states it directly, at line 13:

> *★ [HISTORICAL — SUPERSEDED] The following instruction applied to the original Master 19 lineage and is no longer current: "The DECISION-DEFAULTS file should be regenerated as S18, synced to this master." **The current authoritative Defaults remain `NH_DECISION_DEFAULTS-S19_v2_2.md` until a future Master 20 adoption and separately authorized regeneration.***

and repeats it at line 5721:

> *[HISTORICAL — this filename is superseded; **the current authoritative Decision Defaults are `NH_DECISION_DEFAULTS-S19_v2_2.md`, which remain authoritative until Master 20 is explicitly adopted and a later Defaults regeneration is separately authorized**]*

The same file is named as authority #2 by the design-completion workflow, the eight-bundle plan, the five-additions decision package, and the preservation statements of the AIC and UDOK closure records.

**Therefore, and this is the correction v1_0 needed:**

- **v2_2 governs this bridge and its selector.**
- `NH_DECISION_DEFAULTS-S19_v2_3.md`'s on-disk self-description ("AUTHORITATIVE — ADOPTED BY NESS 2026-08-13") may be **reported as stale or competing artifact evidence**, which is exactly what an authority ledger is for.
- **Its mere presence does NOT create a genuine open Ness decision.** Master V10 has already answered the question.
- **Its mere presence does NOT place continuation in `LOOP_SAFETY_HOLD`.** v1_0's "safe default" was wrong: it would halt the loop over a question the governing authority already settled.
- **Ness is not asked which Defaults governs.**
- **Neither file is edited, deleted, moved, renamed, or re-headed.**

### 10.2 What still fails closed

Ordinary fail-closed authority handling is unchanged for anything genuinely unresolved. If a **new, higher-authority contradiction beyond the already-settled v2_2 status** is later proved — for example an adopted Master 20 plus a separately authorized Defaults regeneration, or two artifacts disagreeing about something Master V10 has not settled — then §23's ordinary rules apply in full: fail closed, preserve the conflicting evidence, surface the exact problem, choose no winner.

### 10.3 The concrete correction

**`AUTH-V22`.** The continuation selector, the task-preparation stage, and every operative prompt the continuation reaches must state the current authoritative Decision Defaults as authority #2. A later implementation corrects the literal at `nh_loop.py:433` and the same literal at `:734`, `:1310`, `:2001`, `:2427`, `:2595`, `:24275`, `:24553`, and reconciles the preflight required-file entry at `:3265`.

`AUTH-V22` corrects **the authority order the continuation operates under.** It does not adopt, de-adopt, supersede or reinterpret either Defaults file; it does not touch Master, Map, `cursorrules` or the Companion.

### 10.4 Preflight disposition

`EXACT_REQUIRED_FILES` (`nh_loop.py:3263-3271`) currently requires the basename `NH_DECISION_DEFAULTS-S19_v2_3.md` for the `nh_decision_defaults` key. Required behaviour:

- preflight requires the **current authoritative** Defaults basename (`v2_2`) to be present;
- preflight **may report** any other file in `01_AUTHORITATIVE/` claiming Decision Defaults authority as stale/competing artifact evidence, naming path and digest;
- preflight **does not fail** merely because such a file exists — presence is evidence, not a verdict — and **does not gate continuation on it**, because Master V10 has settled which file governs.

Because `check_required_source_coverage()` measures authority coverage against exactly this preflight resolution (P-14), correcting the entry corrects the selector's and the preparation stage's coverage requirement in the same act, with one implementation of the rule.

---

## §11 — THE GENUINE-NESS-DECISION ROUTE

### 11.1 The rules

**`NESS-NO-MANUFACTURE`.** Never manufacture an answer, never choose a default on Ness's behalf, never present a fake option, never re-ask a settled decision.

**`NESS-NO-DIRECT-ASK`.** A question is never composed from a model result directly. A selector's or preparation stage's possible-Ness finding is **evidence only** — not a question, not shown to Ness, unlocking nothing.

**`GOPEN-IS-EVIDENCE-ONLY`** *(stated explicitly in v1_9; the rule itself is unchanged)*. The raw selector classification `genuinely_open_for_ness` is **evidence that automatic mechanical handling must stop and the independent question-validation stage must run** — and it is nothing else. It **must never**:

- ask Ness anything, directly or by being rendered anywhere Ness sees it;
- become a question, or have a question composed from its `simple_explanation`, `dependency`, `package_title` or any other prose field;
- prepare a Claude design task;
- authorize Claude, a design run, or any mechanical continuation;
- bypass, shorten, pre-satisfy or substitute for Piece-3 validation;
- unlock a clearance, mint a validation set, or satisfy a coverage review.

This restates, at this one seam, exactly what Ness's detailed design-interview decision already settles: *"A model may signal ... `genuinely_open_for_ness` ... That signal is not itself permission to ask Ness. It means: stop automatic mechanical handling and perform the required independent question-validation/source-check stage."* **v1_9 changes none of that**, and §9.3a's stronger root requirement makes the route it feeds provable rather than making it easier to enter.

### 11.2 The exact route

**Entry precondition, stated first because it is now provable** *(corrected in v1_9)*. A `genuinely_open_for_ness` selection enters this route **only** after it has been admitted under all ten `SEL-ADMISSION` proofs, which now include `T1-ACTIONABLE-ROOT` (§9.3a). **An actionable rootless result never reaches the first line of the diagram below** — there is no admission path to it (`SEL-ADMISSION-NO-ACTIONABLE-ROOTLESS`), so `review_signal_recorded` always has the exact proved `scope_root_path` it must bind to, and the accepted refusal of a rootless signal never has to fire on a result the contract admitted.

```
selector returns classification genuinely_open_for_ness
  WITH ONE EXACT PROVED package_source_path        <-- T1-ACTIONABLE-ROOT (v1_9)
  (or the T3 preparation review returns a review_signal)
   |
   |  the controller records ONE review_signal_recorded  (installed event type)
   |    package_scope_id / package_key : Q's scope, derived by the CONTROLLER
   |                                     from Q's PROVED bound root
   |    scope_root_path                : Q's proved bound root -- never a
   |                                     candidate path a model named
   |    signal_source                  : the stage that found it
   |    finding_evidence               : the finding, inert
   |    route                          : awaiting question validation
   v
question-validation                  (installed command)
   |  ONE bounded read-only source check RE-CLASSIFIES the concern from the real
   |  sources. A routing signal is never carried through as a question. The
   |  controller composes the Ness-facing form itself, refuses a form that names
   |  implementation machinery, and refuses a duplicate form.
   v
question-coverage-review             (installed command)
   |  ONE fresh INDEPENDENT review challenges the completed inventory and must
   |  come back with nothing.
   v
only now:  LOOP_NEEDS_NESS_DECISION  -> the browser asks Ness ONE question
```

If question-validation classifies the concern as settled, implied, mechanical, dependent, future or later-implementation, **no question is created**, the signal resolves, and the loop continues on the mechanical route without Ness ever seeing it.

### 11.3 Why `review_signal_recorded` is the right carrier

Its documented reason for existing is exactly this case (`nh_loop.py:20387-20396`): a fresh review found something that may need Ness; it is not a question; it is not shown to Ness; it unlocks nothing; it normalises into the same pending-routing standing as `routed_issue_recorded` and passes through the same machinery, "so this is one interview system rather than two"; and its package scope comes from the controller's already-proved binding and `scope_root_path`, never from a candidate path a model named.

That last clause is also what makes it usable mid-transition: Q has no candidate, and the signal binds to a **root**. The installed T3 stage already uses it exactly this way (`nh_loop.py:8586-8630`, `REVIEW_SIGNAL_SOURCE_DESIGN_SPEC`), which is why §13 reuses that branch rather than writing another.

### 11.4 One question at a time, and after the answer

Eight-bundle global rule 3 stands: one genuine unresolved concept or policy question at a time unless Ness explicitly requests a batch. No second Ness-question path, no second question store, no second interview. After an answer, the installed behaviour governs unchanged: a standing-changing answer requires a fresh question-validation run, which receives Ness's exact preserved words, the option the controller read them as, and the consequences that currently stand, as inert validated context. Only when Q's own clearance is proved unlocked does the mechanical route resume.

### 11.5 Routed-signal identity and the coverage stop — preserved, cross-referenced, not redesigned *(new in v1_9)*

**This subsection introduces no new policy.** It exists because §9.3a and §9.7 both depend on these semantics, and a correction that leaves its own dependencies implicit is not internally self-consistent. **Every rule below is the already-settled behaviour, restated as a cross-reference so this file cannot drift from it.**

**`ROUTED-SIGNAL-INSTALLED-IDENTITY`.** `review_signal_recorded` carries and is located by **the installed routed signal identity that the event actually carries** — `routed_signal_id`. Any consumer that looks the signal up by a key the event does not carry finds nothing, and a genuinely routed question then reads as unrouted. **The identity the event carries is the identity every reader must use.** No second identity, no alias, no alternate key, and no second routing store.

**`ROUTED-SIGNAL-CURRENT-NOT-HISTORICAL`.** The signals that gate a package's first validation are the **currently unresolved** routed signals for that scope — the ones the installed clearance projection reports as awaiting validation. They are what select `first_package_validation_routed` over `first_package_validation_unrouted` (§12.3g B / A) and what the work item's `routed_signal_refs` carries. **Resolved historical routed signals do not remain blocking merely because their history exists**; history is history, and it is neither erased nor treated as an open obligation.

**`COVERAGE-TO-NESS-STOP`.** After a **current** question validation and a **current** independent question-coverage review have both run, and they genuinely leave a validated, deliverable Ness question standing for the package, **the loop stops at `NEEDS_NESS_DECISION`** (`LOOP_NEEDS_NESS_DECISION`, §7.3). It does not loop back into another coverage review, does not re-run coverage indefinitely, does not re-derive the same owed stage for ever, and does not treat the surviving question as an unfinished mechanical step. **Coverage is not endlessly repeated.**

**`NO-DESIGN-WHILE-NESS-PENDING`.** While a genuine Ness decision is pending for a package, **no Claude design call occurs for that package** — no task preparation, no initial design, no correction. The mechanical route resumes only when Q's own clearance is proved unlocked, on the installed gate, unchanged.

**`PIECE3-RULES-NOT-REOPENED`.** v1_9 **does not** redesign Piece-3, its identities, its variants, its authorization, its gate, its clearance projection, or its stop conditions. It adds no rule to them and removes none. Any defect found in a later *implementation* of the semantics above is an **implementation defect against already-settled behaviour**, and it is corrected against these rules — not by inventing new policy here.

---

## §12 — THE MECHANICAL ROUTE AND Q'S OWN SCOPE

### 12.1 When it applies

The selection's classification is `mechanical_work` or `mechanically_implied` (action `prepare_claude_task`), all ten `SEL-ADMISSION` proofs pass, and no genuine Ness question is open for Q.

### 12.2 Establishing Q's own authenticated scope

**`SCOPE-NEW`.** Q's `package_scope_id` is derived by the installed `interview_package_scope_id(package_id, scope_root_path)` from Q's own proved bound root — the controlled id where one genuinely exists in source, otherwise the `nullpkg_` digest of the root. Derived by the controller, from the controller's own proof, never from model output.

**`SCOPE-NO-INHERIT`.** Q must not reuse, inherit, or be satisfied by any of P's state:

| P's state | Why Q cannot use it |
|---|---|
| `package_scope_id` | Q's scope is derived from Q's root; equality with P's is a contradiction (`SEL-ADMISSION` 8) |
| work-item identity | derived over the binding, which includes the scope |
| acceptance | `acceptance_truth` is projected from `Replay(events, scope)`; Q's replay holds none of P's acceptance events |
| audit / PASS | `mechanical_audit_recorded` and `mechanical_pass_recorded` are scoped; Q starts with none |
| candidate identity / custody | Q's chain anchors on Q's own initial candidate (§8.3 Case B) and can never chain onto P's |
| Piece-3 clearance | `evaluate_interview_clearance(scope)` is package-scoped and already refuses clearance earned on another package |
| routed signals / questions / standing | keyed by `package_scope_id` |
| correction batch / lifetime rounds | scoped counters; Q starts at zero |

The installed scoping does most of this already (P-13). What this design adds is the **positive requirement to prove it**: at the moment Q's `validation_recorded` is appended, the controller must prove `scope_Q != scope_P` and that Q's replay holds no acceptance, no PASS, no audit and no custody — and must fail closed rather than proceed if any of that is untrue.

### 12.3 The clearance sequence (T2)

Each of the two Piece-3 stages is **one durable provider call followed by one provider-free commit** — never a durable supervisor review *and* a second direct Codex call for the same stage. §12.3a states the sequence, §12.3b the refactor that produces it, §12.3c the routing, §12.3d the recovery.

```
T2.a  question-validation for Q      -- dispatch, custody, authorize, commit
T2.b  coverage-review for Q          -- dispatch, custody, authorize, commit

T2.c  evaluate_interview_clearance(scope_Q) must prove unlocked:
        complete inventory for Q; every page recorded and reconciled; no
        material unknown unresolved; no genuine Ness question still blocking;
        no routing signal still unvalidated; no presented group awaiting an
        answer; no standing-changing answer awaiting revalidation; the checked
        source has not moved, re-proved from TODAY'S BYTES; every dependency a
        question in Q waits on settled in Q.
```

Every line of T2.c is the installed gate, unchanged and unweakened.

### 12.3a The durable T2 sequence *(Correction 2)*

P-24 shows the installed Piece-3 commands call Codex blindly, and that the installed authorization gate already demands what only a custodied provider result can produce. The correction wires the two halves together, **reusing the installed supervisor kinds `question_validation` and `coverage_review` and the provider kinds and templates already mapped to them**. No second provider lifecycle is built.

For **each** T2 stage, in this exact order:

```
 1. PREPARE (controller only, no provider).
    The controller derives and freeze-proves the exact Q package scope and root
    (§13.2 Class-0) and the exact pre-call source requirement the existing
    Piece-3 command already derives -- the same object, from the same code.

 2. DISPATCH ONE durable supervisor provider request under the EXISTING
    work-item kind (question_validation or coverage_review), sending the EXACT
    installed Piece-3 prompt for that stage -- never the generic supervisor
    prompt (§12.3e):
        provider_request_prepared
     -> provider_dispatch_begun
     -> ( provider_request_accepted, where the transport reports one )

 3. UNCERTAIN OUTCOME  ->  reconcile-provider-request FIRST.
    Never an automatic resend.  Local CLI lookup_unsupported ->
    NEEDS_USER_ACTION, exactly as §19.3 already designs.

 4. THE REPLY IS ADMITTED BY ITS OWN DEDICATED B6d BRANCH against the real
    Piece-3 payload contract (§12.3e), never by the generic three-key schema.
    VALID RESULT  ->  provider_result_custody_recorded
                   -> provider_request_terminal_recorded (result_received)

 5. process-custodied-provider-result consumes that exact custodied result and
    _b6f_piece3() appends the SCOPE-MATCHED piece3_provider_work_recorded
    (authorizes_event_type = validation_recorded or
     question_coverage_review_recorded, package_scope_id = scope_Q).

 6. ONLY THEN the Piece-3 COMMIT stage may run.

 7. The COMMIT stage re-reads and re-validates the SAME exact custodied result
    and appends exactly one:
         validation_recorded            (stage a)
      or question_coverage_review_recorded  (stage b)
    consuming the authorization from step 5.

 8. The COMMIT stage makes ZERO provider calls.
```

**`T2-ONE-CALL`.** There must never be a durable supervisor Codex review **and** a second direct `run_codex_question_validation()` or `run_codex_question_coverage_review()` for the same stage. One stage, one model request.

**`T2-AUTHORIZATION-OWNER`.** `_b6f_piece3()` remains the **only** producer of `piece3_provider_work_recorded`. The commit stage consumes an authorization; it never creates one, and it never appends a Piece-3 event without one.

**`T2-SCOPE-MATCHED`.** The authorization must carry `package_scope_id == scope_Q`, enforced by the strengthened gate of §23 R-4. **P's authorization can never satisfy Q's append**, and this is the seam where that would otherwise have happened.

### 12.3b The refactor: extract, do not duplicate *(Correction 2)*

**`T2-ONE-OWNER`.** The existing `command_question_validation()` and `command_question_coverage_review()` remain the **one owner** of every substantive rule they already implement:

pre-call source-requirement derivation · the source byte snapshot and its before/after stability comparison · package and root binding · pagination and enumeration state · question and review payload validation · source-path checking · material-unknown refusal · standing and question construction · Ness-facing form composition and its duplicate/mechanism refusals · append body construction · the tail compare-and-swap · and the final `validation_recorded` / `question_coverage_review_recorded` append.

**None of that is copied, reimplemented, or paralleled.** The extraction separates exactly two things and nothing else:

| Part | Contains | Becomes |
|---|---|---|
| **A — preparation and dispatch** | everything up to and including "the prompt is built", plus the pre-call frozen source requirement | the input to one durable supervisor provider request |
| **B — validation and commit** | everything from "a reply object is in hand" onward | the provider-free commit stage |

**`T2-COMMIT-RECONSTRUCTS`.** Part B must receive or reconstruct the exact pre-call controller-owned bindings **from durable authenticated evidence** — the prepared record, the custodied result, and the authenticated journal — and must **not** trust: a model-authored package title; remembered process state; a stale worker or `loop-status` report; or any caller-supplied source binding.

**`T2-STALE-NOT-RECALL`.** The commit position is not the dispatch position, and the design says so explicitly because one installed detail makes it sharp: `validate_question_validation_payload()` is given **the journal position the reply will be recorded at** (`len(state["_events"]) + 1`), which is what a first-time persistent concern's standing target is minted from. On a deferred commit that position has moved.

So the commit stage re-derives every position-dependent value at commit time and re-proves the whole set:

- the source binding and manifest still match what the dispatch froze;
- the package scope and root still bind as they did;
- the pagination / enumeration generation, segment and page are still the ones this reply answers;
- the standing state the reply was validated against has not moved;
- the authorization from step 5 is unconsumed and scope-matched.

**If any of those moved so that the saved result no longer belongs at the current commit position, the old result is PRESERVED and the stage fails closed as stale — it is never silently reused, and Codex is never called again to paper over it.** A fresh stage may then be opened as a new request identity, with the old one kept as history.

### 12.3c Routing *(Correction 2)*

`loop-status` derives the position; the worker never decides these facts itself. For each T2 stage:

| Position | Route |
|---|---|
| **A** — the required Q-scoped Piece-3 provider request has not been made | `dispatch-piece3-provider-review` `[proposed]` (§12.3c.A) |
| **B** — its valid custody awaits processing | `process-custodied-provider-result`, under the Q transition context proved by `TB-CUSTODY-BOOTSTRAP` (§8.9.2) |
| **C** — the matching Q-scoped `piece3_provider_work_recorded` exists and the Piece-3 event is still owed | the **provider-free commit** stage |
| **D** — the matching `validation_recorded` / `question_coverage_review_recorded` is durable | continue normally (the next T2 stage, or T2.c clearance) |

#### 12.3c.A — position A needs one exact new command

v1_4 left position A as a placeholder. P-28(a) shows why an installed name cannot fill it: `main()` dispatches `question-validation` and `question-coverage-review` **directly** to the two public commands, ahead of the supervisor fallthrough, and that is true under `NH_SUPERVISOR_WORKER=1` too. Since those public commands must keep their ordinary direct behaviour, the continuation cannot reuse their names for a durable supervisor dispatch.

**`T2-DISPATCH-COMMAND`.** Position A is `dispatch-piece3-provider-review` `[proposed]` — **one** command covering both Piece-3 stages. Its controller logic:

1. takes **§8.9.4 Path A** — **not** §8.9.2, which belongs to `process-custodied-provider-result` alone: freshly authenticate the journal; prove P terminal-accepted and the transition active; re-admit the exact T1 selection under all ten `SEL-ADMISSION` proofs; prove exactly one Q transition scope; and construct **binding 2** for a first Q question-validation or **binding 3** for a coverage review. **It must not require an unfinished custody** (`TB-DISPATCH-NO-CUSTODY-PRECONDITION`);
2. derives from controller state alone **which stage is currently owed** — the one whose event is still missing, `validation_recorded` or `question_coverage_review_recorded`;
3. dispatches exactly **one** supervisor work item of the correspondingly installed kind, `question_validation` or `coverage_review`, with the exact installed Piece-3 prompt (§12.3e).

**`T2-STAGE-FROM-STATE`.** The stage is decided by **controller state, never caller input**. The command accepts **no** caller-supplied package binding, scope, stage, or variant. A caller field attempting any of those is refused, not used. Its pre-context discovery is **Path A** of §8.9.4 — **not** the pending-custody bootstrap, whose precondition cannot hold before any custody exists (`TB-DISPATCH-NO-CUSTODY-PRECONDITION`).

It is added to `WORKER_COMMANDS` **and** to `PROVIDER_CONTACTING_COMMANDS` — it reaches a provider, so the installed retry series and backoff gate it. `loop-status` position A returns exactly this command.

**`T2-PUBLIC-COMMANDS-UNCHANGED`.** The ordinary public `question-validation` and `question-coverage-review` keep their existing non-continuation and operator behaviour, unchanged and unswitched. **No semantic switch is hidden behind `NH_SUPERVISOR_WORKER`**: one name keeps one meaning, and the continuation gets its own name.

#### 12.3c.B–D — the remaining positions

Position B is the installed `process-custodied-provider-result`, reached through the corrected `TB-CUSTODY-BOOTSTRAP` of §8.9.2. **Position C genuinely needs one new name**, and this design states why rather than leaving it implicit:

> The installed CLI names `question-validation` and `question-coverage-review` currently mean *"derive, call Codex, validate, append"* — one command covering both halves. Routing position C to those names would either re-run the provider call (violating `T2-ONE-CALL`) or silently change what the installed public command does, which would break every existing operator use of it. Overloading them on an environment variable or an implicit journal condition would make one name mean two different things depending on invisible state — exactly the ambiguity this controller refuses elsewhere.

The provider-free commit stage is therefore `commit-piece3-provider-result` `[proposed]` — one name, covering both stages, routed by the authorization's own `authorizes_event_type`, which already distinguishes `validation_recorded` from `question_coverage_review_recorded`. It appends exactly one Piece-3 event and makes zero provider calls. Its pre-context discovery is **Path C** of §8.9.4 — anchored on the unconsumed scope-matched authorization, **not** on a pending custody, which by then is already closed (`TB-COMMIT-BY-AUTHORIZATION`). `WORKER_COMMANDS` gains it; `PROVIDER_CONTACTING_COMMANDS` **does not**.

**`T2-NO-SECOND-PIECE3-SYSTEM`.** No second Piece-3 system, no second interview, no second question store, no second authorization, no second gate. The installed commands keep their public behaviour for the ordinary loop; the continuation reaches the same code through the extracted parts.

### 12.3d T2 crash positions *(Correction 2)*

| # | Durable position | Restart action | Never |
|---|---|---|---|
| **E1** | Piece-3 provider request **prepared**, never dispatched | `SAFE_TO_RETRY` — dispatch may begin under the same request identity | treat a prepared record as a call made |
| **E2** | **dispatched**, outcome uncertain | `WAIT` → `reconcile-provider-request` first; `absent_proved` → a **new** request identity; `lookup_unsupported` → `LOOP_NEEDS_USER_ACTION` | resend automatically; invent a terminal |
| **E3** | result **custodied**, authorization not yet appended | `process-custodied-provider-result` under the proved Q context; `_b6f_piece3()` appends the one scope-matched authorization | call Codex again; append a second authorization; let P's scope authorize Q |
| **E4** | `piece3_provider_work_recorded` **durable**, Piece-3 commit not yet appended | the provider-free commit stage re-validates the same custodied result at the current position and appends exactly one Piece-3 event | make any provider call; append a second Piece-3 event; consume an authorization twice; reuse a result whose position moved |
| **E5** | Piece-3 event **durable**, operation completion missing | the installed same-operation completion recovery appends only the missing matching completion | repeat the substantive append; re-authorize; re-dispatch |

Across all five: **no duplicate provider call on uncertainty; no lost custodied result; no duplicate authorization; no duplicate validation or coverage event; scope P can never authorize Q; source or standing drift makes the saved result stale and refused rather than silently reused; no question is manufactured; and no false success.**

**`T2-RECOVERY-OWNER-PER-POSITION`.** Restart reaches the same Q at every position, but **not through one bootstrap** — v1_7 wrongly claimed `TB-CUSTODY-BOOTSTRAP` governs all five. Each position has exactly one recovery owner:

| Position | Recovery owner | Never |
|---|---|---|
| **E1** — request prepared, never dispatched | ordinary operation and request recovery: `SAFE_TO_RETRY` under the **same prepared request identity**. **No pending-custody bootstrap** — no custody exists. | treat a prepared record as a call made |
| **E2** — dispatched, outcome uncertain | operation-specific **`TB-RECOVERY-BOOTSTRAP`** (§8.9.1) as needed to discover and bind the authenticated operation, then **`reconcile-provider-request` FIRST**. **No pending-custody bootstrap** — no custody exists yet. | redispatch on uncertainty; invent a terminal |
| **E3** — result custodied, authorization absent | **§8.9.2 / Path B `TB-CUSTODY-BOOTSTRAP`** — this is the one position where an unfinished Piece-3 custody genuinely exists — then `process-custodied-provider-result`, and `_b6f_piece3()` appends the one scope-matched authorization. | call the provider again; append a second authorization; let P's scope authorize Q |
| **E4** — authorization durable, Piece-3 event owed | **§8.9.4 Path C** — anchor on the one unconsumed scope-matched authorization, locate and re-prove the exact request / custody / terminal it names, run the provider-free commit. **No pending-custody lookup**: the custody is already closed. | make any provider call; append a second Piece-3 event; consume an authorization twice |
| **E5** — Piece-3 event durable, matching operation completion missing | **same-operation completion recovery only**, discovering and reconstructing the authenticated operation as `TB-RECOVERY-BOOTSTRAP` requires, appending **only** the missing matching completion. | redo the dispatch, the custody processing, the authorization, or the Piece-3 commit |

### 12.3e The real Piece-3 prompt and the real Piece-3 admission *(Correction 3)*

P-27 shows that, left as v1_4 stood, the durable T2 request would have sent a *generic supervisor* prompt and admitted it against a *generic three-key* schema — so the custodied result could not have been the Piece-3 reply the commit re-validates. Both halves are corrected, and both reuse installed code.

**A — the prompt.** `PROMPT-BY-KIND` (§9.5b) selects, for these two kinds, the exact controller-built prompt the existing direct command would have sent:

- `gpt_question_validation` → `build_question_validation_prompt(state, pagination, inventory, authenticated_identity, precall_source_requirement=…)`;
- `gpt_question_coverage_review` → `build_question_coverage_review_prompt(binding_block)`.

**`T2-ONE-MODEL-CALL-ONE-QUESTION`.** Codex is **not** asked a generic supervisor question first and the Piece-3 question second. There is **one** model call per stage, and the thing it is asked is the Piece-3 question. Those exact prompt bytes are bound by `prompt_material_sha256` through the prompt inventory's `extra` slot, and `_supervisor_provider_material()` re-derives and re-checks that digest before dispatch.

**B — the admission.** `_validate_result()` gains dedicated branches for the **existing** work-item kinds `question_validation` and `coverage_review`:

| Work-item kind | Validator and contract |
|---|---|
| `question_validation` | the installed `validate_question_validation_payload(...)` against `QUESTION_VALIDATION_REQUIRED_KEYS` |
| `coverage_review` | the installed `validate_question_coverage_review(...)` against `COVERAGE_REVIEW_REQUIRED_KEYS` |

**No lifecycle `result_schema_id` / `result_schema_version` is added to either model-authored Piece-3 payload**, and **no parallel validator is created**. First-pass validation is run against the **exact frozen controller-owned inputs the prompt was built from** — the pre-call source requirement, pagination position and standing state carried by `EXTRA-INPUTS-SEAM` and re-derived under `EXTRA-INPUTS-RECONSTRUCTION`.

**C — two proof levels, kept apart** exactly as for T1 and T3:

| Level | Decides |
|---|---|
| **B6d** | this exact reply is structurally and binding-valid enough to custody as `result_received` |
| **provider-free commit** | these saved bytes are still valid **for the current exact commit position** — source binding, manifest, scope, root, pagination generation/segment/page, standing, and the unconsumed scope-matched authorization (`T2-STALE-NOT-RECALL`) |

Neither substitutes for the other.

**D — `_b6f_piece3()`: ownership unchanged, field-source logic bounded-modified.** Stating this precisely, because v1_6 contradicted itself here:

- **Unchanged:** it remains the **sole owner and sole producer** of `piece3_provider_work_recorded`; the event type is unchanged; its authorization role is unchanged; and it still does **not** itself append `validation_recorded` or `question_coverage_review_recorded`.
- **Bounded modification:** its **value-source logic** must be extended for the controlled transition variants, because the installed function reads all three of `routed_signal_refs`, `validation_set_id` and `piece3_standing_sha256` straight from `context.binding` — and a pre-validation binding legitimately has no validation set (§8.10, §12.3h `PIECE3-AUTHORIZATION-TRUTHFUL`).

That is a change to **where three field values come from**, and nothing else. It is **not** a new authorization producer, **not** a second owner, and **not** a new or altered event schema.

**E — the commit.** `commit-piece3-provider-result` re-reads the exact custody named by the authorization and runs the **extracted existing** Piece-3 commit logic of §12.3b part B. **Zero provider calls.**

### 12.3g Controlled Piece-3 work-item variants *(Correction 3)*

P-31 shows the two installed rows demand a non-empty routed-signal list and a required `validation_set_id`, and that `piece3_work_item()` copies both from the binding. A first-Q clearance truthfully has neither. **The answer is controlled variants, not fabricated fields.**

**`PIECE3-PRESERVE-INSTALLED`.** The installed rows `("question_validation", None)` and `("coverage_review", None)` are **preserved exactly**, with their existing semantics, for the existing ordinary route. Nothing about that route changes, and `check_work_item_object()`'s single-row fallback still resolves `variant=None` to them.

**`PIECE3-VARIANTS`.** Three controlled variants are added — the smallest complete set the real paths require:

**A — `("question_validation", "first_package_validation_unrouted")` `[proposed]`**
Q's first question-validation for a mechanical or mechanically-implied selected package, with no routed signal.

| Field | Requirement | Why |
|---|---|---|
| `routed_signal_refs` | `[]` | **truthfully empty.** No routed signal exists, and none is invented. |
| `validation_set_id` | `0` | **no prior validation set exists**, and none is invented. The set this run creates is minted by the commit stage from its own enumeration, exactly as the installed direct path already does. |
| `piece3_standing_sha256` | `R` | real: the current interview standing chain, global rather than package-scoped, truthfully derivable before Q's first validation (§8.10) |
| every other variable field | `0` / `[]` as in the installed Piece-3 rows | no audit, no findings, no target, no correction authority, no rounds |

**B — `("question_validation", "first_package_validation_routed")` `[proposed]`**
Q's first question-validation where T1 or a later stage genuinely produced a possible-Ness routing signal for scope_Q.

Identical to A **except** `routed_signal_refs` = `N` — the real signal refs, sorted and unique. `validation_set_id` remains `0`: a routed signal does not create a prior validation set, and none is invented.

**C — `("coverage_review", "package_coverage_unrouted")` `[proposed]`**
Q's coverage review after its validation set exists, with no routed signals outstanding.

| Field | Requirement | Why |
|---|---|---|
| `routed_signal_refs` | `[]` | truthfully empty — a mechanical package can clear its inventory with nothing routed |
| `validation_set_id` | `R` | **now real**: Q's first `validation_recorded` exists, so the set is a proved value |
| `piece3_standing_sha256` | `R` | real |
| every other variable field | `0` / `[]` | as above |

**D — the existing routed Piece-3 path** keeps `(kind, None)` unchanged (`PIECE3-PRESERVE-INSTALLED`).

**`PIECE3-NO-FAKE-FIELDS`.** No fake routed signal is created to satisfy `identity.py`, and no fake `validation_set_id` is created. Where a value does not exist, the variant requires its honest null or empty form.

**`PIECE3-BINDING-BY-VARIANT`.** Variants A and B run under the **pre-validation** binding (§8.10); variant C runs under the **post-validation** binding; variant D runs under whatever ordinary binding its installed route already uses.

### 12.3h Variant selection, and truthful authorization *(Correction 3)*

**`PIECE3-VARIANT-FROM-STATE`.** `engine.piece3_work_item()` — or one bounded helper beside it — chooses the variant from **controller-proved state only**:

```
  is this a post-acceptance transition stage for the single in-transition scope?
      no   -> variant None            (installed route, unchanged)
      yes  -> does scope_Q have a durable validation_recorded?
                  no  -> does scope_Q hold genuine routed signals?
                             no  -> A  first_package_validation_unrouted
                             yes -> B  first_package_validation_routed
                  yes -> C  package_coverage_unrouted        (coverage stage)
                      or the installed routed row where routed signals stand
```

**No caller variant. No model variant. No environment-variable semantic switch.** `work_item_identity(obj, variant)` is called with the exact proved variant, and **restart reconstructs the same variant from the same authenticated evidence** (§17.3a). **If two variants appear possible, or none is provable: fail closed**, nothing appended, no provider contacted.

**`PIECE3-AUTHORIZATION-TRUTHFUL`.** `_b6f_piece3()` remains the **sole** producer of `piece3_provider_work_recorded` (`T2-AUTHORIZATION-OWNER`). What changes is a **bounded modification of its field-source logic** — and only that. The installed function writes

```
"routed_signal_refs":     sorted(set(context.binding.routed_signal_refs)),
"validation_set_id":      context.binding.validation_set_id,
"piece3_standing_sha256": context.binding.piece3_standing_sha256,
```

reading all three from the binding. Under a pre-validation binding the second of those is legitimately null, and under variants A and C the first is legitimately empty. The values must therefore come from the **proved work item and proved state** rather than from a blind binding read:

| Authorization | `routed_signal_refs` | `validation_set_id` | `piece3_standing_sha256` |
|---|---|---|---|
| **first Q validation** (variants A/B) | the work item's own — `[]` for A, the real refs for B | **`null`** — none exists, and none is invented | the real standing chain |
| **Q coverage** (variant C) | the work item's own — `[]` | the **real** set id from Q's first validation | the real standing chain |
| **ordinary installed Piece-3** (variant D) | unchanged | unchanged | unchanged |

The event's body key set is unchanged and no schema change is required: the installed schema fixes the required **key set**, not per-key nullability, so a present-and-null `validation_set_id` is schema-valid.

**`PIECE3-AUTH-STILL-SCOPE-MATCHED`.** `supervisor_piece3_authorization_gate()` must still scope-match Q (§23 R-4). **No P authorization may satisfy Q**, on any variant.

### 12.3f The connected T2 route, end to end

```
  Q Piece-3 stage owed
   -> loop-status returns  dispatch-piece3-provider-review
   -> controller freshly proves Q + the exact owed stage (from state, never input)
   -> the EXACT installed Piece-3 prompt is built for that stage
   -> provider_request_prepared          (prompt + inputs digests bound)
   -> provider_dispatch_begun
   -> ONE Codex call
   -> the exact Piece-3 reply gets its DEDICATED B6d admission
   -> provider_result_custody_recorded
   -> provider_request_terminal_recorded (result_received)
   -> loop-status sees one pending matching T2 custody
   -> process-custodied-provider-result pre-context bootstrap finds Q AND the
      correct kind (TB-CUSTODY-CLOSED-SET)
   -> _b6f_piece3 appends ONE scope-matched piece3_provider_work_recorded
   -> loop-status returns  commit-piece3-provider-result
   -> the commit re-reads the SAME custody + authorization
   -> the extracted existing provider-free Piece-3 validation/commit logic runs
   -> ONE validation_recorded  OR  ONE question_coverage_review_recorded
   -> ZERO second Codex calls
   -> restart at EVERY boundary derives the same position
```

**No second Piece-3 system**, no second interview, no second question store, no second authorization, no second gate (`T2-NO-SECOND-PIECE3-SYSTEM`).

### 12.4 The mechanical route's own stops

| Condition | Loop state |
|---|---|
| question-validation proves a genuine Ness question in Q | `LOOP_NEEDS_NESS_DECISION` |
| the T3 preparation review returns a `review_signal` | `LOOP_NEEDS_NESS_DECISION`, after §11.2's full route |
| a practical external action is required (unreachable provider account, missing external dependency, `lookup_unsupported`) | `LOOP_NEEDS_USER_ACTION` |
| continuing would weaken authority, privacy, provenance, custody, source fencing or version preservation | `LOOP_SAFETY_HOLD` |
| a bounded technical dependency is unavailable, or an operation is being recovered | `LOOP_WAITING_RECOVERING` |
| Q's root moved under the transition | selection stale → `LOOP_SELECTION_REQUIRED`, nothing rewritten |
| the proved frontier is building work | `LOOP_DESIGN_CONTINUATION_COMPLETE` |

**No stop is disguised as a design question, and no stop is reported as completion.**

---

## §13 — THE TASK-PREPARATION PHASE (T3) *(Correction 2)*

### 13.1 Why this phase exists

The installed pipeline is **not** selection → Claude. It is selection → **independent task preparation** → controller-constructed instruction → Claude (P-15). v1_0 omitted the middle stage, which is where the exact target path, the mechanical design specification, the settled basis, the source coverage and the possible-Ness escape all come from. Without it, Claude would be asked to derive the design for itself — precisely the role split the installed repair removed.

**`PREP-REQUIRED`.** No initial Claude design run may be dispatched for Q without a validated prepared task for Q. There is no path from T1 or T2 directly to T4.

### 13.2 Deciding **which** package is being worked

`controller_held_question_validation_package()` (`nh_loop.py:27801-27900`) already decides this from controller-held facts only, before any model call: one routed scope → that package; more than one → refuse as ambiguous; no routed scope → the live checkout names it, with the binder's own ambiguity refusal.

**`SEED-SELECTOR-CLASS`.** One new precedence class `[proposed]` is added to that same function — not a second function, not a second rule:

> **Class 0 — the controller's own proved continuation selection.** When (a) the current package is terminal-accepted, (b) no post-acceptance `validation_recorded` exists, and (c) exactly one durable continuation selection is held that passes all ten `SEL-ADMISSION` proofs — then the package being validated is that selection's package, and its scope and root come from the controller's own proof.

It sits **above** the live-checkout fallback and **below** the routed-scope rule, so ordinary discovery and ordinary revalidation are unchanged, and more than one admitted selection is ambiguous and refuses exactly as more than one routed scope does today.

**`SEED-SEED-CLASS`.** `derive_package_source_binding()` gains one seed class `[proposed]`, `selected_next_package_root`, reachable **only** on the Class-0 path, seeded **only** from the controller-proved selected root, and subject to every existing rule after it: exactly one root, real permitted file, bytes re-prove, `interview_package_scope_id()` derives the scope, any ambiguity refuses.

This is not a weakening. It is the same shape as the installed `authenticated_request` exception (`nh_loop.py:27032-27046`), which the code itself calls "a different question rather than a weaker answer": the binder's ordinary question is "which candidate is this worktree changing?" — genuinely unanswerable here (P-9) — while the continuation's question is "which package did this controller itself prove it selected?", which has exactly one authenticated answer.

### 13.3 The reuse seam — stage two, not a parallel engine

**`PREP-REUSE-STAGE-TWO`.** T3 reuses the installed stage-two mechanic. The smallest seam that exposes it without duplicating it:

> Extract, from `run_prepare_next_claude_task()`, the segment that begins after the first-stage analysis is in hand and runs through the final clearance re-proof, into one named internal function `[proposed]` — call it `run_design_task_preparation(analysis, decision_binding, selected_scope, bound_root, …)`. It contains **no new logic**: the same `build_prepare_task_prompt(analysis, decision_binding)`, the same review invocation, the same `extract_codex_agent_message`, the same `validate_prepared_task(task_message, analysis, required_files, errors)`, the same source-state checks around it, the same `review_signal` branch through `record_review_signal(..., REVIEW_SIGNAL_SOURCE_DESIGN_SPEC, ...)`, the same final `is_new_candidate_path(target_path)` re-check, the same `finalize_claude_instruction()`, and the same `reprove_selected_package_clearance()` at the final boundary.
>
> `run_prepare_next_claude_task()` then calls that function and behaves exactly as it does today — **the public `prepare-next-claude-task` command's behaviour is unchanged.** `prepare-next-design-task` `[proposed]` calls the same function with the **already-durable, already-admitted selection** in place of a fresh stage-one run, and stops.

**`PREP-NO-RESELECT`.** `prepare-next-design-task` must **not** re-run the T1 selector merely to obtain a stage-one object. The durable custodied selection is the stage-one object: it is the same installed `analysis` contract (§9.1), which is exactly why this reuse works.

**`PREP-NO-PARALLEL-ENGINE`.** No second task-preparation engine, no second prompt builder, no second prepared-task validator, no second instruction constructor.

### 13.4 What T3 must independently establish

The prepared task is usable only when every one of these is proved:

| Requirement | Installed mechanism |
|---|---|
| the **same exact selected package root** | `PREPARE_TASK_REQUIRED_KEYS` includes `package_source_path`, cross-checked against the stage-one value — because `package_title` is prose and two reviews can agree on a name while describing different packages |
| a **mechanical / mechanically-implied classification** | the prepared task's `classification`, checked against the installed mapping |
| **sufficient settled authority** | the `settled_basis` field, plus the settled-decision binding carried into the prompt and re-proved at the final boundary |
| **exact source coverage** | `source_paths_checked` re-resolved and measured through `check_required_source_coverage()` against the controller's own preflight authority set |
| an **exact mechanical design specification** | `validate_mechanical_design_specification(value, checked_paths, errors)` — every requirement grounded in a source path this same review proved it read |
| an **exact controller-validated target candidate path** | `target_path` must satisfy `is_new_candidate_path()` when validated **and again** at the final safe boundary, so a file that appeared during the review cannot still be reported as a new target |
| **no unresolved Ness blocker** | `review_signal` must be null; a non-null one records the signal, prepares no task, and routes to §11 |
| a **controller-constructed Claude instruction** | `finalize_claude_instruction()` — fixed controller-owned text over four validated bindings; only the validated specification is operative, and only for design content |
| **clearance still open for Q** | `reprove_selected_package_clearance(scope_Q, …)` at the final preparation boundary, against the journal as it stands then |

### 13.5 The target path

**`PREP-TARGET-CONTROLLED`.** The target candidate path is **proved by the controller**, in the one controlled candidate grammar `<name>_v<major>_<minor>_CANDIDATE.md` under `05_ACTIVE_CANDIDATE/`, and re-proved as a **new** path at the final safe boundary. Claude never guesses it, never proposes it, and never derives it from model prose; nothing downstream may substitute a different path; and an existing file at that path means the later exclusive create fails and the run stops with nothing written — never an overwrite.

### 13.6 Durability

The prepared task is made durable exactly as the selection is: by the installed provider lifecycle, as a custodied, digest-bound result (`work_item_kind = next_design_task_preparation` `[proposed]`). It is re-admitted from custody on every restart — the same discipline as `SEL-ADMISSION`, over the prepared-task contract:

1. the installed `validate_prepared_task()` over the custodied bytes, with the admitted selection as the cross-check object;
2. `task_ready` true and `not_ready_reason` null;
3. `package_source_path` identical to the admitted selection's root, and that root's bytes still re-prove;
4. classification selectable;
5. `target_path` still a **new** valid candidate path **now**;
6. `mechanical_design_specification` still valid, with every requirement grounded in a proved-read path;
7. `review_signal` null;
8. authority coverage still measured against the controller's current preflight resolution;
9. Q's clearance still unlocked, and the settled-decision binding digest unchanged since preparation;
10. the controller-constructed instruction rebuilt deterministically from the same four bindings and matching its recorded digest.

A failure of 3, 5, 8 or 9 makes the prepared task **stale**: it is preserved as history, consumed by nothing, and T3 is re-entered. A failure of 1, 2, 4, 6, 7 or 10 fails closed.

### 13.6a The T3 first-pass admission branch (B6d) *(Correction 1)*

**`PREP-B6D-BRANCH`.** `_validate_result()` gains a dedicated branch for `work_item_kind == next_design_task_preparation` `[proposed]`, using the **existing** `validate_prepared_task()` contract against `PREPARE_TASK_REQUIRED_KEYS`, and evaluated against exactly four controller-held objects:

1. **the exact already-admitted T1 selection** — the same `analysis` object `validate_prepared_task()` already takes as its cross-check, so stage two must return `package_source_path` unchanged and is held to it;
2. **the same controller-required authority files** — the carried binding of `SEL-AUTHORITY-BINDING-CARRIED`, re-resolved and matched, never re-derived from the reply;
3. **the same selected package root and scope** — Q's proved bound root and the scope derived from it;
4. **the same settled-decision binding** — the digest carried into the prompt, re-proved at use.

**No lifecycle schema keys are added to `PREPARE_TASK_REQUIRED_KEYS`**, and **no parallel prepared-task validator is created**. The provider record keeps its controller-owned `result_schema_id` as metadata, exactly as in §9.5a.

**`PREP-TWO-LEVELS`.** As in `SEL-TWO-LEVELS`: B6d decides only that the preparation result may be custodied as a valid `result_received`; the §13.6 re-admission, re-run on every restart, decides whether it is usable **now** — target path still new, root bytes still re-proving, clearance still unlocked, decision binding unchanged, `review_signal` null.

### 13.6b The T3 prompt and its bound inputs *(Correction 1 and 2)*

**`PREP-PROMPT-INSTALLED`.** The bytes sent for `codex_next_design_task_preparation` are the installed `build_prepare_task_prompt(analysis, decision_binding)` output, selected by `PROMPT-BY-KIND` (§9.5b). The generic lifecycle sentence is not prepended, so the model is asked for exactly `PREPARE_TASK_REQUIRED_KEYS` and nothing else — which is what §13.6a's dedicated B6d branch then validates.

**`PREP-INPUTS-BOUND`.** The `analysis` and `decision_binding` the prompt is built from are the **admitted T1 selection** and the **settled-decision binding for scope_Q**, both bound into the request through `EXTRA-INPUTS-SEAM` and both re-derived and digest-matched on reconstruction (`EXTRA-INPUTS-RECONSTRUCTION`). A preparation result produced against a different selection, root, scope or decision binding therefore carries a different `required_inputs_sha256` and a different `provider_request_identity`, and can never be mistaken for this one.

### 13.6c The `next_design_task_preparation` work item *(Correction 2)*

**`WIM-PREPARATION`.** One row, **variant `None`**.

| Field | Requirement | Why |
|---|---|---|
| `blocking_finding_refs` | `[]` | nothing audited |
| `audit_identity` | `0` | no audit precedes preparation |
| `checkpoint_identity` | `0` | no checkpoint |
| `diagnosis_event_sha256` | `0` | no diagnosis authority |
| `diagnosis_strategy_sha256` | `0` | same |
| `strategy_novelty_key` | `0` | same |
| `correction_specification_sha256` | `0` | **correction-only; the T3 `mechanical_design_specification` is a different object and is not this field** |
| `target_candidate_path` | `0` | **T3 *derives* the target; requiring it here would be circular** |
| `authorized_next_lifetime_round` | `0` | not a correction round |
| `authorized_batch_number` | `0` | same |
| `authorized_round_in_batch` | `0` | same |
| `routed_signal_refs` | `[]` | preparation consumes no routed signal; a signal it *finds* is recorded downstream (§11.2) |
| `validation_set_id` | `0` | T3's authority is the admitted T1 selection, carried by `extra_inputs`, not a validation set |
| `piece3_standing_sha256` | `0` | not a Piece-3 operation |

**`WIM-PREPARATION-BUILDER`.** `next_design_task_preparation_work_item(context, candidate)` `[proposed]`, returning `(obj, work_item_identity(obj))` and nothing else.

Its bound candidate is **Q's proved source root** under the post-validation transition binding, so its identity differs from the T1 item by kind **and** by candidate identity. The admitted T1 selection, the selected root and scope, and the settled-decision material are bound through `required_inputs_sha256`'s extra (§9.5c), **not** through work-item fields that do not exist for them.

---

## §14 — DURABLE INITIAL CLAUDE EXECUTION (T4) *(Correction 3)*

### 14.1 The contradiction being fixed

v1_0's Row F said: the process died after Claude returned but before any write-ahead, therefore "nothing durable happened", therefore a restart performs a fresh design run. That is a **redispatch of a provider request whose outcome is uncertain**, and it contradicts the very invariant v1_0 claimed to hold. It also contradicted v1_0's own §17.3.

**The design must never say "Claude returned, nothing durable was recorded, therefore restart just asks Claude again."**

### 14.2 The corrected mechanism — the installed lifecycle, used

Once an initial Claude request **may have been dispatched**, it is governed by exactly the same rules as every other uncertain provider request. The initial design run therefore uses the installed durable lifecycle (P-16) **before** any candidate write-ahead:

```
   build_prepared_request        -> provider_request_prepared
   append_dispatch_begun         -> provider_dispatch_begun
   context.provider.dispatch(request)     [ ONE bounded Claude run inside a
                                            disposable copy of the frozen
                                            committed source, outside N.H ]
   _observe_and_close            -> provider_result_custody_recorded
                                 -> provider_request_terminal_recorded
```

**`INIT-CUSTODY-BEFORE-PROMOTION`.** No candidate write-ahead, no exclusive create, and no promotion may occur before the Claude result is durably custodied with a schema-valid terminal. The candidate transaction (T5) consumes **only** those custodied bytes.

This is not a new mechanism: it is what `claude_correction` already does. The installed `NhCliProviderTransport` (`nh_loop.py:46200-46295`) already builds the disposable workspace, seeds it, runs the CLI under a bound, re-scans the workspace against a frozen baseline manifest, refuses if anything other than the single target moved, enforces `MAX_CANDIDATE_BYTES`, and returns a canonical result body carrying `produced_candidate_path`, `produced_candidate_sha256`, `produced_candidate_bytes` and `produced_candidate_payload_base64`. T4 uses that same transport shape under `work_item_kind = initial_design` `[proposed]` / `provider_kind = claude_initial_design` `[proposed]`, with the parent seed being **Q's proved bound root** rather than a predecessor candidate.

### 14.3 Restart behaviour — the exact table

This is the installed recovery routing (P-16), applied to T4 and stated as the rule:

| Durable position | What restart does | What it must never do |
|---|---|---|
| **no request was ever prepared** | start T4 normally | — |
| **prepared, never dispatched** (`phase == prepared`) | `SAFE_TO_RETRY` — dispatch may begin; no call has been made | treat a prepared record as a call |
| **dispatched, outcome uncertain** (`dispatch_begun` / `accepted`, no terminal) | `WAIT` → **`reconcile-provider-request` first** | **never redispatch**; never assume "probably nothing happened" |
| … reconciliation proves **authoritative absence** (`absent_proved`) | `SAFE_TO_RETRY` — and only now may a **new request identity** be opened; the old one stays as history | reuse the old request identity |
| … reconciliation returns **`lookup_unsupported`** (the local CLI case, P-17) | `NEEDS_USER_ACTION` → `LOOP_NEEDS_USER_ACTION`, naming the exact practical action | guess; redispatch; fabricate a terminal |
| … reconciliation returns **`found_terminal_result_unavailable`** | `NEEDS_USER_ACTION` | fabricate the result |
| … reconciliation **transiently failed** | `WAIT` under bounded backoff | hot-poll |
| **result custodied** (`phase == result_custodied`) | `SAFE_TO_RESUME` → `process-custodied-provider-result`: **reuse the exact custodied bytes**, no Claude call | call Claude again "to be sure" |
| **terminal `result_received`, custody pending** | `SAFE_TO_RESUME` → `process-custodied-provider-result` | dispatch anything |
| **terminal `result_invalid` / `result_oversize`** | bounded output-retry budget decides: `SAFE_TO_RETRY` while budget remains; **exhausted → the honest stop** — see `INIT-EXHAUSTION-IS-NOT-A-CONSUMPTION` below *(corrected in v1_10)* | exceed the budget; silently accept invalid bytes; **name a closure command that would refuse** |

**`INIT-EXHAUSTION-IS-NOT-A-CONSUMPTION`** *(new in v1_10)*. The row above previously read *"else `close-open-consumption`"*, copied from the **installed recovery routing** (P-16), which does return that command name for an exhausted `result_invalid`. **That string is a truthful description of what the installed recovery table emits, and it is not a rule this design may state as T4's route** — because `claude_initial_design`, exactly like `next_package_selection`, **opens no `diagnosis_strategy_consumption_started`**, so the installed `close_open_consumption()` would truthfully refuse for it too (§5 P-34, §9.6a `T1-NOT-A-CONSUMPTION`).

For T4, therefore, once the installed bounded output-retry budget is **exhausted**:

- **no further initial-design request is dispatched on the exhausted condition**;
- **no `close-open-consumption` is owed, and no diagnosis consumption is invented to make one callable**;
- the position is the same honest stop shape as §9.6a — **`LOOP_NEEDS_USER_ACTION`, `loop_next_command` null, zero further provider calls** — derived from the same durable evidence and the same installed `bounded_output_retry_budget()`, and **restart-stable** for the same reason;
- **everything durable is preserved**: the request records, the terminals, the operation history, and any pending candidate intent. Nothing is aborted, deleted or rewritten.

**No new loop state, no new event type, no new state store, no eighth continuation execution command, and no change to any B9 retry value or to B9's real-change meaning** (§9.6c). **This is the same single contradiction §9.6a corrects, appearing at the second work-item kind that inherits the same installed recovery string; it is corrected here for that reason and for no other, and no other part of T4 is reopened.**

**`INIT-EXHAUSTION-IS-WIRED`** *(new in v1_11)*. The rule above is **not prose the rest of this design leaves unimplemented.** v1_10 stated it here and never carried it into the derivation, so the state machine still routed an exhausted T4 back to `execute-initial-design` (§5 P-35). It is now carried by exactly one derived field and consumed at exactly one place, and **this paragraph and the derivation describe one mechanically executable rule**:

| Obligation | Where it is actually mechanised |
|---|---|
| the exhausted fact is **derived** from durable evidence and the **installed** budget | `initial_design_output_retry_exhausted` `[proposed]`, §17.2 `INIT-EXHAUSTION-DERIVED` |
| it is **consumed before** a design run can be selected again | the §7.4 guard, placed after `t.prepared_task is None` and **before** `t.initial_result_custody is None` → `execute-initial-design` |
| the reported position is **`LOOP_NEEDS_USER_ACTION` / null** | §7.4 guard return; §7.3 table unchanged (no new loop state) |
| **zero** further Claude/provider calls, **zero** appends, **zero** new request identities | §7.4 is read-only; §20.3 step 5 waits on a null next command |
| **restart-stable** | §17.2 `INIT-EXHAUSTION-NOT-STORED`; §18 Row I; §25 `R115` case D |
| **no** `close-open-consumption`, **no** invented diagnosis consumption | this subsection, §9.6a `T1-NOT-A-CONSUMPTION`, §23 `R-5e`, §25 `R115` cases E and F |

**And while the budget remains `available`, nothing above applies**: the ordinary installed T4 retry and recovery semantics of this section's table continue exactly as written. **The wiring ends a retry series that is already over; it removes no retry that is still owed.**

**`INIT-NO-REDISPATCH`.** Where a dispatched initial-design request's outcome is uncertain, the loop reconciles first and never re-dispatches. A new request identity is opened **only** after authoritative absence is proved. Where lookup is unsupported, the honest answer is a named practical action for a person — never a silent second call.

**`INIT-EXACT-BYTES`.** A restart that finds a custodied, schema-valid Claude result uses **those exact bytes** to create the candidate. It does not re-run Claude, does not re-derive the design, and does not accept different bytes for the same request.

### 14.4 What T4 may never do

The Claude run writes only inside the disposable workspace. The real checkout is never its working directory, is never added to its workspace, and stays read-only to it. The run performs no Git operation, decides no acceptance, names no target path (§13.5), alters no authority order, and authorizes no implementation.

### 14.5 The initial-design admission contract *(Blocker 2)*

v1_1 treated a `claude_initial_design` result as usable once it was "schema-valid". P-20 shows why that is not enough: `_validate_result()` gives strong checks to `design_audit`, `correction_apply` and `acceptance_explanation_content` only, and every other kind receives `_generic_result_schema()` alone. Registering `initial_design` without a dedicated contract would let T5 consume a result whose produced path is not the prepared target, whose payload is malformed, whose byte count or digest disagrees, whose payload is oversize, or which belongs to a different prepared task entirely.

The installed `claude_correction` protection pattern (K1–K8) is the right **shape**, and this design says plainly that it cannot be reused unchanged: **K3 (filename succession against a predecessor candidate), K6 (the authorized correction-round triple) and K7 (the correction-specification digest and blocking-finding refs) have no meaning for an initial design**, which has no predecessor candidate, no correction round and no correction specification. Pretending otherwise would be a false reuse.

**`INIT-ADMISSION`.** An initial-design result is admitted only when the controller proves, recomputing every value from the custodied bytes:

| # | Check | Meaning |
|---|---|---|
| **I1** | **Exact result key set** — no more, no fewer, over the **six** keys enumerated in §14.5a | a plausible extra field cannot ride along, and a correction result can never be mistaken for an initial-design one |
| **I2** | **Exact schema id and version** — `NH_CLAUDE_INITIAL_DESIGN_RESULT_V1` `[proposed]`, version 1 | a correction result can never be read as an initial-design result, or the reverse |
| **I3** | **`produced_candidate_path` equals the currently-admitted prepared task's controller-validated `target_path`, exactly** | the model cannot redirect the write |
| **I4** | **That target path is still the same controlled candidate path and is still safe for exclusive creation now** — `is_new_candidate_path()` re-proved at this boundary | a file that appeared meanwhile stops the run rather than being overwritten |
| **I5** | **`produced_candidate_payload_base64` decodes strictly** | malformed payloads never reach the promotion |
| **I6** | **`produced_candidate_bytes` is a non-negative integer (not a bool), at most `MAX_CANDIDATE_BYTES`, and exactly equal to the decoded payload length** | a declared length can never disagree with the bytes |
| **I7** | **`produced_candidate_sha256` equals `sha256_hex(decoded payload)`** | the digest is recomputed, never believed |
| **I8** | **The work-item / request binding proves this result belongs to the exact admitted T3 prepared task** — the request's `required_inputs_sha256` and `prompt_material_sha256` must equal the values recomputed now from the transition binding's `source_binding_sha256`, `source_manifest_sha256`, `settled_decision_binding_sha256` and `required_source_paths`, the work item's candidate identity (Q's proved bound root), and the prepared task's target path and specification digest carried as the extra input | a result produced for a different package, a different root, a different settled decision, or a different prepared task cannot be admitted |
| **I9** | **No model-authored title, name or path may substitute for any controller binding** — `package_title` and every other prose field are evidence only | prose never becomes identity |
| **I10** | **The exact admitted payload is the only payload T5 may write** | nothing may be re-derived, re-encoded, normalised or regenerated between admission and promotion |

**Where these run.** `INIT-ADMISSION` is the `initial_design` branch of `_validate_result()` — the same B6d position where `_claude_admission_checks()` runs for `correction_apply` — so it is evaluated on the custodied bytes both on the first pass through `_observe_and_close()` and again inside `process-custodied-provider-result`.

**Where these are RE-RUN.** They are re-run **in full, over the custodied bytes, immediately before T5 consumes them**, on every restart and every re-entry — never remembered from an earlier pass, and never inferred from `result_schema_valid` on the terminal record. I4 in particular must be re-proved at the promotion boundary, because a target path that was new when the result was produced may not be new now.

**A merely generic schema-valid result is never sufficient**, and a result that fails any of I1–I10 creates **no candidate**: it is preserved as history, consumed by nothing, and routed by the installed invalid-output semantics (§14.3's `result_invalid` row) rather than promoted.

### 14.5a The exact initial-design result key set

v1_2's I1 asserted an exact key set without stating it, which left a safety-critical schema choice to implementation. It is stated here, and it is **closed**.

**`INIT-RESULT-KEYS`.** The initial-design result object carries **exactly these six keys — no more and no fewer**:

| # | Key | Proved by |
|---|---|---|
| 1 | `result_schema_id` | I2 — must be exactly `NH_CLAUDE_INITIAL_DESIGN_RESULT_V1` `[proposed]` |
| 2 | `result_schema_version` | I2 — must be exactly `1` |
| 3 | `produced_candidate_path` | I3 (equals the prepared task's controller-validated `target_path`) and I4 (still a new, safely creatable controlled candidate path now) |
| 4 | `produced_candidate_sha256` | I7 — recomputed from the decoded payload, never believed |
| 5 | `produced_candidate_bytes` | I6 — a non-bool integer, at most `MAX_CANDIDATE_BYTES`, exactly equal to the decoded payload length |
| 6 | `produced_candidate_payload_base64` | I5 — must decode strictly; I10 — the decoded bytes are the only payload T5 may write |

**The five correction-specific fields of `CLAUDE_RESULT_KEYS` are deliberately EXCLUDED:**

| Excluded key | Why it has no truthful meaning here |
|---|---|
| `produced_lifetime_round` | an initial design is not a correction round; the round is derived from chain position, never read from a model field |
| `produced_batch_number` | there is no correction batch yet — Q's counters start at zero |
| `produced_round_in_batch` | same |
| `correction_specification_sha256` | there is no correction specification; the governing content authority is the **task-preparation** `mechanical_design_specification`, which is controller-validated at T3 |
| `blocking_finding_refs` | there are no blocking findings; nothing has been audited yet |

Including any of them would invite a model to state a value the controller would then have to either ignore or believe — and either outcome is worse than not asking for it.

**`INIT-RESULT-NO-DUPLICATED-BINDINGS`.** The result carries **no** package identity, no scope, no root, no settled-decision digest, no specification digest and no target-path restatement beyond key 3. Those bindings are proved through the **controller-owned** request and work-item hashes described by I8 — `required_inputs_sha256` and `prompt_material_sha256`, recomputed now from the transition binding's source facts, the work item's candidate identity (Q's proved bound root), and the prepared task's target path and specification digest carried as the request's extra input.

**They must not be duplicated as model-authored result fields.** A binding the model restates is a binding the model can misstate; a binding the controller recomputes is one it cannot. Key 3 is the single exception, and it exists only so I3 has something to compare against the controller's own target — it is checked for equality, never trusted as the target.

### 14.6 Unverifiable existing custody never reopens Claude *(Blocker 1)*

v1_1's Row K said that where a previously-custodied Claude result is genuinely unavailable, the pending candidate intent may be aborted and Q may return toward a fresh design run. **That is wrong, and it contradicts the installed controller** (P-19).

**`CUSTODY-UNVERIFIABLE-HOLD`.** Once `provider_result_custody_recorded` exists for an initial-design result, an inability to read or re-verify those exact custodied bytes:

- is **NOT** provider absence;
- is **NOT** permission to open another initial-design request;
- is **NOT** permission to return to T4;
- is **NOT** equivalent to a request that was never dispatched;
- is **NOT** cured by aborting the candidate write-ahead.

It follows the installed custody-unverifiable route exactly:

```
   engine.custodied_bytes() refuses  (length or digest does not re-verify)
     -> dependency code  provider_result_custody_unverifiable
        (authority_or_safety_conflict / no_retry_fail_closed /
         manual_safety_review, row C17, carried on
         supervisor_operation_completed)
     -> operation completes "safety_hold"
     -> recovered_workflow_state = SAFETY_HOLD
     -> LOOP_SAFETY_HOLD
     -> ZERO new Claude calls
```

**Everything durable is preserved exactly**: the custody record, the terminal, the operation history, and **the pending candidate write-ahead intent**. Nothing is aborted, deleted, rewritten, or re-declared, and the loop makes no further model call of any kind.

**`CUSTODY-UNVERIFIABLE-RESUME`.** If some **separately accepted future mechanism** can restore the exact saved custodied bytes — proved by the recorded `result_byte_length` and `result_sha256` — recovery may resume from **those same bytes only**. **This bridge does not invent such a mechanism, does not design one, and does not authorize one.** Until one exists and is separately accepted, the position is a safety hold that a person resolves.

The distinction that makes this coherent: **a request that was never dispatched, or whose absence is authoritatively proved, may be re-attempted** (§14.3). **A result that was already received and saved may not be re-obtained by asking again** — the saved bytes are the evidence, and losing evidence is never a licence to manufacture replacement evidence.

### 14.5b The `initial_design` work item *(Correction 2)*

**`WIM-INITIAL`.** One row, **variant `None`**.

| Field | Requirement | Why |
|---|---|---|
| `blocking_finding_refs` | `[]` | nothing audited yet |
| `audit_identity` | `0` | the fresh audit happens after T6, not before T4 |
| `checkpoint_identity` | `0` | no checkpoint |
| `diagnosis_event_sha256` | `0` | no diagnosis authority |
| `diagnosis_strategy_sha256` | `0` | same |
| `strategy_novelty_key` | `0` | same |
| `correction_specification_sha256` | `0` | **there is no correction specification; the T3 design specification rides `extra_inputs` (§14.5 I8) and is not this correction-only field** |
| **`target_candidate_path`** | **`R`** | **this genuinely belongs to the work item's authority**: T4 writes exactly one file at exactly the T3 controller-validated target, and `INIT-ADMISSION` I3 compares the produced path against `work_item["target_candidate_path"]` |
| `authorized_next_lifetime_round` | `0` | an initial design is not a correction round; Q's counters start at zero |
| `authorized_batch_number` | `0` | same |
| `authorized_round_in_batch` | `0` | same |
| `routed_signal_refs` | `[]` | consumes no routed signal |
| `validation_set_id` | `0` | not a Piece-3 operation |
| `piece3_standing_sha256` | `0` | same |

**`WIM-INITIAL-BUILDER`.** `initial_design_work_item(context, candidate, target_candidate_path)` `[proposed]`, returning `(obj, work_item_identity(obj))`. Its bound candidate is **Q's proved source root** (the parent seed); its `target_candidate_path` is the T3-validated target. No alternate identity path exists.

### 14.7 `claude_initial_design` is an actual Claude provider path *(Correction 4)*

P-32 shows that, left as v1_5 stood, both the endpoint map and the dispatch would have sent the initial design write to **Codex** — and would have agreed with each other while doing it, so the endpoint equality check would not have caught it.

**`INIT-CLAUDE-ROUTING`.** All of the following, together:

1. **`claude_initial_design` is added to `SUPERVISOR_CLAUDE_PROVIDER_KINDS`**, so `supervisor_endpoint_binding()` maps it to `SUPERVISOR_CLAUDE_ENDPOINT` — the local Claude endpoint — exactly as it maps the two installed Claude kinds.
2. **`NhCliProviderTransport.dispatch()` gains an explicit `claude_initial_design` branch** placed with the other Claude branches, **above** the `_dispatch_codex()` fallthrough. It is either its own branch or one explicitly parameterised Claude *write* branch whose behaviour is unambiguous for each kind it serves — never an implicit widening of `claude_correction`.
3. **`INIT-NEVER-CODEX`.** `claude_initial_design` must **never** reach `_dispatch_codex()`. A build in which it can is a wiring defect, and rehearsals **R92** (Claude endpoint and branch) and **R93** (zero Codex invocations) are what catch it.
4. It runs the **disposable-workspace Claude writer** — the same mechanics as the correction route: a disposable copy of the frozen committed source outside N.H, the real checkout never the working directory and read-only throughout.
5. Its **parent seed is Q's proved source root**, not a predecessor candidate.
6. Its **target path is the T3 controller-validated target**, carried by the work item (`WIM-INITIAL`).
7. **Exactly that one target may change** in the disposable workspace; the frozen-baseline rescan refuses if anything else moved.
8. Its result object contains **exactly the six `INIT-RESULT-KEYS`** settled in v1_5 §14.5a and **none** of the correction-specific round, specification or finding fields — proved by rehearsal **R94**.
9. Its endpoint, provider and request identities are all **reconstructable on restart** from the authenticated prepared record and the work-item rebuild of §17.3a.
10. **`claude_correction` and `claude_acceptance_explanation` behaviour is unchanged**, byte for byte, including the read-only tool list and deny rules of the acceptance-explanation route.

---

## §15 — THE CANDIDATE TRANSACTION (T5)

### 15.1 The sequence, consuming only custodied bytes

Modelled on, and reusing, the installed `_b6g_correction_apply()` transaction (`commands.py:3180`):

**T5 preconditions.** The candidate transaction may begin only when: the initial-design result passes **all ten** `INIT-ADMISSION` checks re-run now over the custodied bytes (§14.5); the bytes themselves re-verify through `engine.custodied_bytes()` (§14.6); the prepared task backing them is still admissible (§13.6); Q's clearance is still proved unlocked; and the transition binding was reached through `TB-CUSTODY-BOOTSTRAP` (§8.9.2). A failure of any one appends nothing.

```
  admitted custodied Claude result (T4)  --  INIT-ADMISSION re-proved
    |
    |  decide what this transaction already did, BEFORE any append and BEFORE
    |  any exclusive create -- the installed four-boundary resumption
    |    B0  nothing durable yet
    |    B7  write-ahead durable, file not promoted
    |    B8  write-ahead durable, file promoted with exactly those bytes
    |    B9  custody already committed for exactly this transaction
    v
  B0 -> candidate_write_ahead_recorded
          candidate_*        = the produced identity from the custodied result
          parent_candidate_* = Q's PROVED BOUND ROOT (path, sha256, bytes)
          intent_origin      = CANDIDATE_INTENT_ORIGIN_INITIAL   [proposed]
          correction_round   = the initial round, DERIVED from chain position
    |
  B0/B7 -> exclusive no-overwrite promotion  ->  anchored read-back
        -> candidate_custody_recorded
             custody_origin = CANDIDATE_CUSTODY_ORIGIN_INITIAL   [proposed]
    |
  B8 -> exactly one recovered custody, no second exclusive create
  B9 -> zero appends; the already-durable custody is returned
```

**`TXN-NO-PROVIDER`.** No provider is contacted on any path of this transaction. The custodied result is its only input — the property the installed function states in its own comment.

**`TXN-IDENTITY`.** At B8 the promoted file's `sha256` **and** byte length **and** payload must equal both the write-ahead's recorded identity and the retained provider result's bytes. Anything else is a different candidate and is **refused rather than adopted** — nothing is deleted, repaired, or regenerated.

### 15.2 The initial candidate's records

The installed `candidate_write_ahead_recorded` / `candidate_custody_recorded` bodies already carry `parent_candidate_path`, `parent_candidate_sha256`, `parent_candidate_bytes` and an origin enum, so the record shape needs nothing new. Only two enum values are added (§7.6). `authenticated_candidate_custody()`'s anchor derivation gains the §8.3 two-case rule so Q's chain anchors on this record; Case A packages — including AIC — are unaffected.

Exactly one initial write-ahead may be open for Q at a time, which the installed "one pending intent per chain" rule already enforces, and the promotion is an exclusive create that cannot overwrite.

### 15.3 Handoff (T6)

Once custody is committed and Q's establishment is complete under §8.4: `build_supervisor_context()` binds **Q** under the ordinary current-package rule; the transition binding is finished and is never used again; `situation.candidate` is Q's initial candidate; `status._project()` projects Q's own ordinary loop, starting at the fresh independent design audit of that candidate; and the worker returns to its ordinary command set, because `supervisor-status` no longer projects `ACCEPTED_FOR_DESIGN_ONLY`.

The desired ownership is achieved exactly:

```
next-package selection
  -> package clearance
    -> task preparation
      -> ONE durable Claude result
        -> exactly ONE safely established initial candidate
          -> modern supervisor owns fresh audit / correction / diagnosis / recovery
```

---

## §16 — THE MODERN-SUPERVISOR OWNERSHIP BOUNDARY

### 16.1 What the continuation owns

T1 through T5, for one transition at a time: one bounded selection review; Q's Piece-3 clearance through the installed commands; one bounded task-preparation review; one bounded Claude design run; one candidate transaction.

### 16.2 What the modern supervisor owns — unchanged

Everything from T6: the fresh independent design audit of Q's candidate; correction specification, correction application, and the batch/lifetime counters; the diagnosis checkpoint and the four-row possible-Ness table; provider request preparation, dispatch, custody, reconciliation, availability probes and episodes; semantic scope exhaustion and unlock; lookup-first crash recovery and the six `recovery_outcome` strings; the acceptance explanation preparation, the A5/A6 chain, `READY_FOR_ACCEPTANCE`, the acceptance offer and the acceptance record.

### 16.3 The boundary rules

**`OWN-NO-PARALLEL-LOOP`.** The old top-level monolithic execute path must never become a second long-running design loop beside the modern supervisor. After T5 returns, no further work is performed by any top-level path for Q — not one audit, not one correction round. `prepare-next-design-task` and `execute-initial-design` each perform one bounded stage and stop.

**`OWN-NO-SECOND-AUDITOR`.** The continuation never audits a candidate. The only audit of Q's initial candidate is the supervisor's own fresh independent audit, under the supervisor's binding, work item, request identity and audit identity.

**`OWN-NO-SECOND-GATE`.** The continuation reuses `evaluate_interview_clearance()` and adds no advisory copy. Master V10, the accepted AIC and UDOK designs, and `cursorrules` §1A all forbid a parallel implementation of gating logic; this design builds none.

**`OWN-NO-SECOND-STORE`.** No new state directory, lock, marker, journal or sidecar. The continuation's durable state is the existing authenticated journal plus the existing provider-result custody directory.

**`OWN-NO-SECOND-RECOVERY`.** The continuation reuses `supervisor-operation-status` and its six `recovery_outcome` strings, `reconcile-provider-request`, `process-custodied-provider-result`, the installed candidate transaction lock, the installed pending-write-ahead commit and abort recovery, and the installed lease. It invents no recovery authority.

---

## §17 — IDEMPOTENCY AND DUPLICATE PREVENTION

### 17.1 The principle

**Every continuation step is lookup-first: it asks the durable record what already happened before it does anything, and a step whose effect is already durable returns that effect with zero appends, however many times it is re-entered.**

### 17.2 The transition state, derived not stored

`post_acceptance_transition_state()` `[proposed]` is a pure derivation over the authenticated journal plus byte re-proofs and the retained custodied results. It stores nothing.

| Field `[proposed]` | Derived from |
|---|---|
| `terminal_acceptance` | the governed acceptance truth of the current package |
| `open_request` | any transition provider request without a terminal, with its phase |
| `selection` | the newest completed, custodied `codex_next_package_selection` terminal whose custodied bytes pass **all ten** `SEL-ADMISSION` proofs — **including proof 4's `T1-ACTIONABLE-ROOT` requirement for both actionable actions** *(corrected in v1_9)* — and which is unconsumed. An actionable rootless result is therefore **never** `selection` (`SEL-ADMISSION-NO-ACTIONABLE-ROOTLESS`). Its custody is **closed** by that completed terminal alone (`CLOSURE-READONLY`, §7.6a) and never counts as pending processing. |
| `legacy_contract_selection` `[proposed]` *(new in v1_9)* | a durable, completed, still-custody-verifiable T1 result that satisfies `SEL-LEGACY-CONDITION` proofs 1–3 (§9.7.2): completed with a `result_received` terminal, bytes re-verify now, valid under the **earlier** contract, and failing current admission **only** on `T1-ACTIONABLE-ROOT`. It is **evidence, never a selection**: it routes nothing, establishes no scope, and is preserved unchanged. Zero or more than one → contradiction. |
| `legacy_replacement_consumed` `[proposed]` *(new in v1_9)* | true when **any** current-contract replacement `next_package_selection` request for this transition exists — prepared, dispatched, custodied, or terminal of any kind. This is `SEL-LEGACY-CONDITION` proof 4, and it is the deterministic consumption fence of `SEL-LEGACY-ONE-SHOT` (§9.7.4). It is **derived from durable evidence on every entry and every restart**, never stored, never counted, never remembered, and never carried in a marker. |
| `prepared_task` | the newest completed, custodied `codex_next_design_task_preparation` terminal whose bytes pass **all ten** §13.6 re-admission proofs. Closed by its terminal alone (`CLOSURE-READONLY`); the `initial_design` custody is **not** (`CLOSURE-INITIAL-PENDING`). |
| `initial_result_custody` | the newest completed, custodied `claude_initial_design` terminal whose bytes re-verify through `engine.custodied_bytes()` **and** pass all ten `INIT-ADMISSION` checks re-run now (§14.5). A schema-valid terminal alone is **not** sufficient. A custody whose bytes do not re-verify does not become "absent": it sets `custody_unverifiable` (below). |
| `initial_design_output_retry_exhausted` `[proposed]` *(new in v1_11)* | true when the durable record proves **both** that the latest relevant `claude_initial_design` output for this transition is **invalid / oversize-invalid as governed**, **and** that the installed `bounded_output_retry_budget()` for that work item, provider kind and episode returns **`exhausted`**. This is the **derived carrier of the stop §14.3 already states** (`INIT-EXHAUSTION-IS-NOT-A-CONSUMPTION`), and §7.4 consumes it before the `initial_result_custody is None` fall-through. **See the derivation note below.** |
| `initial_intent_pending` | an unmatched initial-origin `candidate_write_ahead_recorded` for Q |
| `initial_custody_committed` | a `candidate_custody_recorded` completing that intent |
| `piece3_custody_awaiting(stage)` | the one valid custodied `question_validation` / `coverage_review` result for scope_Q whose authorization is not yet appended (T2 position B). It is a member of the `TB-CUSTODY-CLOSED-SET` pending set (§8.9.2 step 3) together with `initial_design`, and its kind must agree with the freshly derived loop position or the bootstrap fails closed. |
| `piece3_authorization(stage)` | the one unconsumed, **scope-matched** `piece3_provider_work_recorded` for scope_Q whose `authorizes_event_type` names this stage's event and whose Piece-3 event is still owed (T2 position C). An authorization carrying any other `package_scope_id` is not a match and is never consulted. |
| `stop_record` | a loop-level stop on the installed dependency slot of the newest continuation `supervisor_operation_completed` |
| `established_complete` | §8.4 |
| `custody_unverifiable` | an initial-design custody exists whose bytes fail `engine.custodied_bytes()` re-verification. This is **terminal for the transition** until a separately accepted restoration mechanism exists: `LOOP_SAFETY_HOLD`, zero model calls, every durable record and the pending candidate intent preserved (`CUSTODY-UNVERIFIABLE-HOLD`, §14.6). |
| `t1_custody_unverifiable` `[proposed]` *(new in v1_10)* | any durable `next_package_selection` custody whose exact saved bytes are required by the durable record and **fail `engine.custodied_bytes()` re-verification** — **whatever its terminal form is**, `result_received` or `result_invalid` alike, and covering **both** the preserved earlier-contract custody and any current-contract replacement custody, because both are the same work-item kind. `LOOP_SAFETY_HOLD`, null next command, **zero provider calls**; the §9.7 permission is **not even derived** while it holds (`T1-CUSTODY-UNVERIFIABLE`, `T1-CUSTODY-NEVER-ABSENT`, §9.6b). **Derived on every entry and every restart; never stored; and never read as absence.** |
| `t1_output_retry_exhausted` `[proposed]` *(new in v1_10)* | true when the durable record proves **both** that the latest relevant current-contract T1 output is invalid / oversize-invalid as governed, **and** that the installed `bounded_output_retry_budget()` for that work item, provider kind and episode returns `exhausted`. It is a **pure derivation** over the authenticated T1 request(s), their `provider_request_terminal_recorded` outcomes, their matching custody/evidence where applicable, that installed budget calculation, and the existing `supervisor_operation_completed` / dependency evidence those attempts generated — **and over nothing else.** **No process-memory flag, no marker, no mutable counter beyond the already-governing installed budget, and no second source of truth** (`T1-EXHAUSTION-DERIVED`, §9.6a). It is recomputed identically on every entry and every restart, exactly as `legacy_replacement_consumed` is. |
| `transition_scope` | the single in-transition `package_scope_id` proved under `CPB-SINGLE-TRANSITION`, **derived freshly from the current authenticated journal every time it is used** and never carried over from an earlier report (`TB-CUSTODY-NO-STALE-REPORT`). It is the only scope `TB-CUSTODY-BOOTSTRAP` may bind, and it is **absent until a T1 selection has been admitted** — before that there is no Q to bind (`TB-NO-PREMATURE-Q`). Zero or more than one → contradiction. `TB-RECOVERY-BOOTSTRAP` does not read this field at all: it binds the scope its authenticated operation start records (`TB-RECOVERY-BINDS-THE-RECORD`). |
| `contradiction` | any of §23's fail-closed conditions |

Because it is derived, a restart at any point recomputes the same position from the same journal.

**`INIT-EXHAUSTION-DERIVED`** *(new in v1_11)*. `initial_design_output_retry_exhausted` is a **pure derivation**, performed freshly on every entry and every restart, over **exactly** the durable evidence that already exists for the relevant `claude_initial_design` work item — and over nothing else:

1. the **authenticated `claude_initial_design` provider request(s)** for this transition, located through the ordinary work-item derivation (`WIM-INITIAL`, §14.5b; reconstruction per §17.3a);
2. their **`provider_request_terminal_recorded`** outcomes, and specifically whether the latest relevant one is `result_invalid` / `result_oversize_uncustodied` as governed;
3. their **matching custody / evidence where applicable**, re-verified through `engine.custodied_bytes()` exactly as the surrounding rules already require;
4. the **installed `bounded_output_retry_budget()` calculation** for that work item, provider kind and availability episode — **the same installed function the installed recovery table already consults for an exhausted `result_invalid`**, and the same one `t1_output_retry_exhausted` reads;
5. the existing **`supervisor_operation_completed` / dependency evidence** those attempts already generated and the continuation machinery already uses.

**`INIT-EXHAUSTION-NO-SECOND-CALCULATOR`.** It **must not** introduce a second retry calculator, a second budget, a second episode notion, or any recomputation of retry policy. It **reads** the installed budget and reports what that budget already says. **No accepted B9 retry value, retry count, timer, wait, backoff, deadline, real-change rule, episode meaning or exhaustion meaning is changed, reinterpreted, or re-derived by it.**

**`INIT-EXHAUSTION-NOT-STORED`.** It is **derived, never stored**, exactly as `legacy_replacement_consumed` and `t1_output_retry_exhausted` already are:

- **no stored flag**;
- **no marker**;
- **no mutable counter beyond the already-governing installed budget**;
- **no new journal event type and no new event body key**;
- **no new state store and no second source of truth**.

**Why that makes it restart-stable.** Nothing about the position lives in process memory, so a restart re-reads the same authenticated requests, the same terminals, the same custody evidence and the same installed budget, and therefore derives the **identical** answer — with **zero appends, zero provider calls and zero new request identities**. Re-entering the exhausted position any number of times cannot change it, and cannot cause a single dispatch (§25 `R115` case D).

**Precedence, stated so it cannot be inverted.** An **open** T4 request outranks it (caught earlier by `t.open_request`, so reconciliation-first still governs uncertainty). An **unverifiable** initial-design custody outranks it (`custody_unverifiable` → `CUSTODY-UNVERIFIABLE-HOLD` → `LOOP_SAFETY_HOLD`, §14.6) — **safety before a practical stop**, exactly as `t1_custody_unverifiable` precedes `t1_output_retry_exhausted`. A **valid admitted** custody makes it irrelevant, because the loop proceeds to T5. And while the budget is **available** it is simply false, so **ordinary installed T4 retry and recovery continue unchanged**.

### 17.3 The duplicate fences

| Duplicate risk | Fence |
|---|---|
| two continuation operations at once | the installed supervisor lease + the installed one-open-provider-request rule; a second entry sees the open request and reconciles rather than dispatching |
| a second package started | `CPB-SINGLE-TRANSITION` (§8.5) |
| a second `validation_recorded` creating a second scope | Q's scope derives from Q's root, so re-validating the same root yields the **same** scope — ordinary revalidation, not a second package. A validation naming a different root during an open transition is a contradiction |
| a repeated selector call | an admitted unconsumed selection short-circuits T1 with zero appends; an open request reconciles |
| **a repeated earlier-contract "replacement" selection** | `SEL-LEGACY-ONE-SHOT` (§9.7.4): proof 4 of `SEL-LEGACY-CONDITION` fails for ever once **any** replacement request for the transition exists, in any phase. The fence is a **derivation over durable evidence**, recomputed identically on every entry and every restart — no counter, no flag, no marker, no memory, no second store |
| **a bad replacement result re-entering the earlier-contract rule** | `SEL-LEGACY-NOT-A-NEW-LEGACY` (§9.7.4): the condition requires validity **under a contract no longer in force**, which no current-contract result can ever have. A contract-violating reply is bounded output-retry, never a new selector identity |
| **an exhausted T1 invalid-output position re-entering `continue-design-loop` for ever** *(new in v1_10)* | `T1-EXHAUSTION-RESTART-STABLE` (§9.6a) and the §7.4 guard: the exhausted position is derived **before** the `t.selection is None` fall-through and returns `LOOP_NEEDS_USER_ACTION` with a **null** next command, so the worker waits (§20.3 step 5) instead of re-invoking a command whose only remaining move is refused. **Zero appends, zero provider calls, identical answer on every restart** |
| **a lost T1 custody re-opening the selector** *(new in v1_10)* | `T1-CUSTODY-UNVERIFIABLE` (§9.6b): saved bytes that fail re-verification are `LOOP_SAFETY_HOLD`, **never absence**, whatever the terminal form. The loop never asks a model again for an answer it already received and saved |
| a repeated task-preparation call | an admitted prepared task short-circuits T3 |
| **a repeated Claude design call** | `INIT-NO-REDISPATCH` + the installed phase table (§14.3) |
| **an exhausted T4 invalid-output position re-selecting `execute-initial-design` for ever** *(new in v1_11)* | `INIT-EXHAUSTION-DERIVED` (§17.2) and the §7.4 T4 guard: the exhausted position is derived **before** the `initial_result_custody is None` fall-through and returns `LOOP_NEEDS_USER_ACTION` with a **null** next command, so the worker waits (§20.3 step 5) instead of re-selecting a design run against a spent budget. **Zero appends, zero provider calls, zero new request identities, identical answer on every restart** |
| a repeated initial candidate | the four-boundary resumption (B0/B7/B8/B9); one pending intent per chain; exclusive no-overwrite create; T5 refuses outright when Q already holds committed custody |
| a package silently skipped | every stop is durable and named; `CPB-SINGLE-TRANSITION` treats two unfinished transitions as a contradiction rather than dropping one |
| an accepted state lost | acceptance is append-only authenticated history; §23 R-1 refuses any continuation that would need to disturb it |
| continuation re-running after it happened | once Q is established, `loop-status` returns `LOOP_HANDOFF_COMPLETE` and the loop level is never consulted again for that acceptance |

### 17.3a Work-item reconstruction on restart *(Correction 2)*

`commands._rebuild_work_item()` (`commands.py:2302-2341`) re-derives a work-item object from the custody record's `work_item_identity` and handles `design_audit`, `acceptance_explanation_content`, `correction_specification` and `correction_apply`; anything else raises *"the custodied result names a work item this replay cannot re-derive"*. **It cannot currently reconstruct any of the three new kinds, nor the new Piece-3 variants.** Its exact extension:

| Kind | Reconstructed from |
|---|---|
| `next_package_selection` | the exact **P-scoped** selection work item under P's current established binding, rebuilt by `WIM-SELECTION-BUILDER` from that binding's candidate identity |
| `next_design_task_preparation` | the exact **admitted T1 selection** (re-admitted under all ten `SEL-ADMISSION` proofs) + Q's post-validation transition binding + the settled-decision and input binding, rebuilt by `WIM-PREPARATION-BUILDER` |
| `initial_design` | the exact **prepared T3 task** (re-admitted under the ten §13.6 proofs) + Q's transition binding + the controller-validated target, rebuilt by `WIM-INITIAL-BUILDER` |
| `question_validation` / `coverage_review` **variants** | the variant re-derived by `PIECE3-VARIANT-FROM-STATE` from the same authenticated evidence, then the object rebuilt and `work_item_identity(obj, variant)` recomputed |

**`WIM-REBUILD-IDENTITY-EQUALITY`.** In every case the reconstructed `work_item_identity` **must equal** the identity the custody or prepared record names. **A difference fails closed** — it would mean the authority carried into the dispatch and the authority this continuation would check are not proved to be the same authority.

**`WIM-REBUILD-NO-MEMORY`.** Reconstruction uses authenticated durable evidence and current byte re-proofs **only**. Never remembered process state, never a caller-supplied field, never a filename, never a model-authored title.

### 17.4 Concurrency

The continuation runs only under the installed supervisor lease, proved live before any new work starts. The single authenticated journal writer lock, the tail compare-and-swap, the high-water-mark revalidation under the writer's lock, and the candidate transaction lock all apply unchanged. **No continuation step introduces a check-then-write window.**

---

## §18 — CRASH AND RESTART MATRIX

Expanded from v1_0's ten rows to fourteen, covering the two new phases separately as Correction 3 requires. **The row count is unchanged in v1_10**: the two saved-evidence positions the exhaustion correction makes explicit are stated **inside Row D**, which already owns the durable-selection-result position, rather than as cosmetic new rows. **In every row: no duplicate provider call where the outcome is uncertain, no duplicate candidate, no skipped package, no lost accepted state, no false success.**

### Row A — acceptance durable, continuation not started
**Proved:** `PROVED_ACCEPTED`; no continuation operation. **Action:** `LOOP_SELECTION_REQUIRED`; `continue-design-loop` may run. **Never:** re-record acceptance; read the absence of continuation as failure; start more than one selection.

### Row B — selection request prepared, never dispatched
**Proved:** an unmatched start; `provider_request_prepared` with no `provider_dispatch_begun`. **Action:** `SAFE_TO_RETRY` — dispatch may begin under the same request identity. **Never:** treat a prepared record as a call made.

### Row C — selection request dispatched, outcome uncertain
**Proved:** `provider_dispatch_begun` (or `accepted`) with no terminal. **Action:** recovery discovery first — `TB-RECOVERY-BOOTSTRAP` (§8.9.1) locates the operation globally from its authenticated start and binds **exactly the scope that start records**. For a T1 selection that scope is **P**: `continue-design-loop` begins from the terminal-accepted package, and **at T1 no selection has been admitted, so Q does not yet exist** (`TB-NO-PREMATURE-Q`). The P recovery context is built, and the exact T1 request is reconciled — then the §14.3 table (`absent_proved` → retry with a **new** identity; `lookup_unsupported` / `found_terminal_result_unavailable` → `LOOP_NEEDS_USER_ACTION`; transient → bounded wait). **Never:** dispatch a second selector request; invent a terminal; **infer, name, guess or partially bind Q before a selector result has been durably received and admitted under all ten `SEL-ADMISSION` proofs**; assume a scope from the phase rather than reading it from the record.

### Row D — selection result custodied, not yet admitted
**Proved:** a completed `result_received` terminal with readable custody. That pair is the custody's **closure** (`CLOSURE-READONLY`, §7.6a): it is never pending processing and is never routed through `process-custodied-provider-result` to manufacture an effect. **Action:** the result reached this position only because the dedicated B6d branch of §9.5a admitted it against the installed contract — not `_generic_result_schema()`, which it could never satisfy (P-23). Now re-run **all ten** `SEL-ADMISSION` proofs over the custodied bytes, measuring authority coverage against the carried binding of `SEL-AUTHORITY-BINDING-CARRIED`, and proving `T1-ACTIONABLE-ROOT` for an actionable result. Pass → `LOOP_PACKAGE_CLEARANCE_REQUIRED`. Root moved → **stale**: preserved as history, consumed by nothing, `LOOP_SELECTION_REQUIRED` returns. **Actionable with no proved root → NOT admitted, on either route**: it is not a selection, it establishes no scope, it becomes no review signal, and no root is fabricated for it — if it is an **earlier-contract** result, Row D.1 governs; otherwise it is an invalid output on the installed bounded output-retry route (`SEL-B6D-ACTIONABLE-ROOT-IS-INVALID-OUTPUT`) *(corrected in v1_9)*. Any other failure → fail closed. **Never:** admit on `result_schema_valid` alone; re-run the selector while an admitted unconsumed selection stands; use a stale root; rewrite or delete a stale episode; **derive, name-match or manufacture a root for an actionable result that named none.**

**Row D, continued — the two saved-evidence positions this row can also reach** *(new in v1_10)*. Both are derived **before** the phase question of §7.4, in this order, and neither invents a state, an event, a store or a command:

**D — invalid output, budget still AVAILABLE.** **Proved:** a durable `result_invalid` terminal for the current-contract T1 request, and `bounded_output_retry_budget()` returns `available`. **Action:** ordinary current-contract bounded output retry, unchanged — the existing request/retry/provider lifecycle rules, the installed caps and backoff, reconciliation-first on uncertainty. **Never:** reopen the §9.7 permission; create a second legacy replacement; alter any cap, backoff or identity rule.

**D — invalid output, budget EXHAUSTED.** **Proved:** the same durable terminal, and `bounded_output_retry_budget()` returns `exhausted`. **Action:** `T1-INVALID-OUTPUT-EXHAUSTION-STOP` (§9.6a) — **`LOOP_NEEDS_USER_ACTION`, `loop_next_command` null, zero further provider requests on the exhausted condition, zero owed appends**, with the plain-language reason that N.H received unusable next-package output through all currently allowed bounded attempts and stopped rather than opening another request. Re-entering this position three times derives the identical answer with **zero appends and zero provider calls** (`T1-EXHAUSTION-RESTART-STABLE`). **Never:** dispatch again on the exhausted condition; **owe or call `close-open-consumption`**; invent a `diagnosis_strategy_consumption_started` or a `diagnosis_strategy_consumption_terminated`; manufacture a correction specification, diagnosis identity, strategy identity or blocking-finding authority; introduce a new event type, a new state store or an eighth continuation execution command; claim a consumption was closed, that the outcome is uncertain, that the old request reopened, that a package was selected, or that the loop completed successfully.

**D — saved T1 bytes no longer re-verify.** **Proved:** a durable T1 custody whose exact bytes the record requires and which fail `engine.custodied_bytes()` re-verification — **whatever its terminal form, `result_received` or `result_invalid` alike**, and for **either** the preserved earlier-contract custody **or** a current-contract replacement custody. **Action:** `provider_result_custody_unverifiable` → **`LOOP_SAFETY_HOLD`, null next command, zero provider calls** (`T1-CUSTODY-UNVERIFIABLE`, §9.6b). This **outranks** the exhaustion stop above. **Never:** treat the custody as absent because its terminal is `result_invalid`; ask a model again for an answer already received and saved; derive the §9.7 permission while it holds; invent a restoration mechanism.

### Row D.1 — an EARLIER-CONTRACT selection result is durable and non-operative *(new in v1_9)*
**Proved:** all five `SEL-LEGACY-CONDITION` proofs (§9.7.2) — the old request is definitively completed with a `result_received` terminal; its custody **re-verifies now**; the saved bytes were **valid under the earlier contract**; they fail current admission **only** on `T1-ACTIONABLE-ROOT`; and **no current-contract replacement request for this transition exists**. **Action:** the earlier result is **preserved exactly** and routes nothing (`SEL-LEGACY-PRESERVE`, `SEL-LEGACY-NO-SIGNAL`). The loop reports the ordinary `LOOP_SELECTION_REQUIRED` / `continue-design-loop` position, honestly detailed (§9.7.5), and **exactly one** current-contract selection may be taken — under a **new** provider request identity, with a **fresh** current-source check that may prove a **different** frontier (`SEL-LEGACY-NEW-IDENTITY`, `SEL-LEGACY-FRESH-FRONTIER`). From the moment that replacement request is prepared, every ordinary rule governs it (`SEL-LEGACY-ORDINARY-AFTERWARDS`). **Never:** re-dispatch or re-open the old request identity; append anything further to it; delete, rewrite or re-head it; **infer, derive, name-match or fabricate a root for it**; derive `source_evidence` from a different field and present it as the selected root; append a `review_signal_recorded` from it; turn its `simple_explanation` into a Ness question; treat it as an uncertain outcome; treat it as lost custody; **treat its custody as absent because a terminal was `result_invalid`** (`T1-CUSTODY-NEVER-ABSENT`, §9.6b) *(added in v1_10)*; **owe or call `close-open-consumption` for it, or for any exhausted T1 invalid-output position downstream of it** (`T1-NOT-A-CONSUMPTION`, §9.6a) *(added in v1_10)*; hard-code its package id, title, frontier or event position; or take a **second** replacement once proof 4 has failed (`SEL-LEGACY-ONE-SHOT`).

### Row E — package validation / clearance partially completed
**Proved:** some of {incomplete inventory; complete inventory without coverage review; coverage review recorded}. **Action:** `evaluate_interview_clearance(scope_Q)` decides which stage is owed, exactly as for any package; **within** an owed stage the five durable positions **E1–E5 of §12.3d** govern — prepared / dispatched-uncertain / custodied / authorized / event-durable — and are not repeated here. **Never:** treat a partial inventory as clearance; carry P's clearance to Q; skip the independent coverage review; append a Piece-3 event without a **scope-matched** unconsumed authorization (§23 R-4); make a second model call for a stage that already has a custodied result.

### Row F — clearance proved, task preparation not started
**Proved:** clearance unlocked for Q; no task-preparation request. **Action:** `LOOP_TASK_PREPARATION_REQUIRED`. **Never:** dispatch an initial design run without a prepared task (`PREP-REQUIRED`); re-run the selector to obtain a stage-one object (`PREP-NO-RESELECT`).

### Row G — task-preparation request prepared / dispatched / uncertain
**Proved:** as Rows B and C, for the preparation request. **Action:** identical rules, including `TB-RECOVERY-BOOTSTRAP` for discovery. Here the authenticated start records **Q** — Q was controller-proved from an admitted selection before T3 could begin — so recovery binds Q, and it does so **because the record says so**, not because the phase is T3. Then: prepared → retry; dispatched-uncertain → reconcile first, never redispatch; `lookup_unsupported` → `LOOP_NEEDS_USER_ACTION`. **Never:** redispatch on uncertainty; bind a scope the start does not record.

### Row H — task-preparation result custodied
**Proved:** a completed `result_received` terminal with readable custody — **closed** by that pair alone (`CLOSURE-READONLY`), never pending processing. **Action:** the result reached this position through the dedicated B6d branch of §13.6a, against the installed `validate_prepared_task()` contract. Now re-run all ten §13.6 re-admission proofs. Pass → `LOOP_INITIAL_DESIGN_REQUIRED`. Target path no longer new, root moved, clearance closed, or decision binding changed → **stale**: preserved, consumed by nothing, T3 re-entered. `review_signal` non-null → §11 route → `LOOP_NEEDS_NESS_DECISION`. **Never:** carry a stale target path into a design run; treat a preparation that found a possible-Ness choice as a task.

### Row I — initial Claude request prepared / dispatched / uncertain
**Proved:** as Rows B and C, for the `claude_initial_design` request. **Action:** `TB-RECOVERY-BOOTSTRAP` for discovery — its authenticated start records **Q**, and that record is why Q is bound — then the §14.3 table in full. **This is the row v1_0 got wrong.** Uncertain outcome → reconcile first; **never a fresh design run**; authoritative absence → new request identity; `lookup_unsupported` (the local CLI case) → `LOOP_NEEDS_USER_ACTION` naming the exact practical action. **Never:** "nothing durable happened, so ask Claude again".

**Row I, continued — the two invalid-output budget positions, stated explicitly** *(new in v1_11)*. Both are derived **before** the phase question of §7.4, and neither invents a state, an event, a store or a command. **An open request outranks both** (they are reached only once no T4 request is open), and **an unverifiable initial-design custody outranks both** (`CUSTODY-UNVERIFIABLE-HOLD`, Row K.2, §14.6) — safety before a practical stop.

**I — terminal `result_invalid` / `result_oversize`, budget still AVAILABLE.** **Proved:** a durable invalid/oversize terminal for the `claude_initial_design` request, and the installed `bounded_output_retry_budget()` returns `available`. **Action:** ordinary installed T4 retry and recovery, **unchanged** — the §14.3 table in full, the installed caps, the episode machinery, the `retry_series_key` backoff, `INIT-NO-REDISPATCH` and reconciliation-first on uncertainty. **Never:** exceed the budget; silently accept invalid bytes; treat an available budget as spent and stop early.

**I — terminal `result_invalid` / `result_oversize`, budget EXHAUSTED.** **Proved:** the same durable terminal, and `bounded_output_retry_budget()` returns `exhausted`; `initial_design_output_retry_exhausted` is therefore true (§17.2 `INIT-EXHAUSTION-DERIVED`). **Action:** the §7.4 T4 guard fires **before** the `initial_result_custody is None` fall-through and returns **`LOOP_NEEDS_USER_ACTION`, `loop_next_command` null** — with **zero further Claude or provider calls on the exhausted condition, zero appends, and zero new request identities.** Every durable record is preserved exactly: the request records, the terminals, any custody, the operation history, and any pending candidate intent. Re-entering this position over identical authenticated evidence derives the **identical** answer every time (§25 `R115` case D). **Never:** return `LOOP_INITIAL_DESIGN_REQUIRED`; select or dispatch `execute-initial-design`; open a new request identity; **owe or call `close-open-consumption`**; invent a `diagnosis_strategy_consumption_started` or a `diagnosis_strategy_consumption_terminated`; manufacture a correction specification, diagnosis identity, strategy identity or blocking-finding authority; relax `INIT-ADMISSION` so an unusable result looks admitted; introduce a new loop state, event type, state store or eighth continuation execution command; or claim that a consumption was closed, that the outcome is uncertain, that a candidate was created, or that the loop completed successfully.

**An implementer reading this row must not be able to conclude that an exhausted T4 returns to `execute-initial-design`.** It does not, and §7.4, §17.2 and §14.3 `INIT-EXHAUSTION-IS-WIRED` all say the same thing.

### Row J — initial Claude result custodied, no candidate write-ahead
**Proved:** a completed, custodied `claude_initial_design` terminal; no write-ahead for Q. The custody is **still pending processing** by `CLOSURE-INITIAL-PENDING` (§7.6a) — unlike the two read-only kinds, which are already closed. **Action:** the `initial_design` custody is genuinely unfinished here, so §8.9.2 / Path B applies: `TB-CUSTODY-BOOTSTRAP` runs its discovery **before any context is built** — fresh authenticated journal, transition freshly derived, exactly one unfinished `initial_design` custody, its scope proved to be the single in-transition scope — and only then is the Q transition context constructed; a previous `loop-status` report is never treated as authority (`TB-CUSTODY-NO-STALE-REPORT`); `engine.custodied_bytes()` re-verifies the saved bytes; **all ten `INIT-ADMISSION` checks are re-run** over them (§14.5), including I4's fresh proof that the target path is still new; only then does the candidate transaction enter at boundary **B0** using **those exact bytes**. **Never:** call Claude again; treat `result_schema_valid` as admission; accept different bytes; accept a result bound to a different prepared task; promote from process memory; bind the work from the current package's pending custody.

### Row K — candidate write-ahead durable, file absent (B7)
**Proved:** exactly one pending intent for Q; no file at its path.

**K.1 — the custodied result re-verifies.** The transaction resumes at **B7**: `INIT-ADMISSION` is re-run, then the promotion proceeds from the custodied bytes, read back, custody committed. **Never:** synthesise the file from the recorded digest alone; treat the intent as custody; open a second intent while one is pending; abort an intent that is not the pending one.

**K.2 — the custodied result does NOT re-verify (missing, unreadable, corrupt, wrong length, wrong digest).** *This is the row v1_1 got wrong.* The position is **`provider_result_custody_unverifiable` → `SAFETY_HOLD` → `LOOP_SAFETY_HOLD`, with zero new Claude calls** (`CUSTODY-UNVERIFIABLE-HOLD`, §14.6). The custody record, the terminal, the operation history **and the pending candidate write-ahead intent are all preserved exactly**. **Never:** treat unverifiable custody as provider absence; abort the pending intent in order to retry; open another initial-design request; return to T4; equate this with a request that was never dispatched. Recovery may resume only from those **same** bytes, and only through a separately accepted restoration mechanism that this bridge does not invent.

### Row L — file promoted, custody absent (B8)
**Proved:** a pending intent and a real file; the custodied result re-verifies (if it does not, Row K.2 governs and this row is not reached). **Action:** the `initial_design` custody is still unfinished here (no `candidate_custody_recorded` yet), so §8.9.2 / Path B applies: `TB-CUSTODY-BOOTSTRAP` performs its pre-context discovery and binds the proved transition scope, then boundary **B8** — the promoted file's `sha256`, byte length **and** payload must equal both the write-ahead's identity and the retained provider result; only then is exactly one recovered custody committed, with **no second exclusive create**. A mismatch **refuses custody and alters nothing**. **Never:** judge the file by its name; adopt the observed digest; delete or repair a mismatched file; re-run Claude to regenerate it.

### Row M — custody committed, handoff not yet observed (B9)
**Proved:** `candidate_custody_recorded` is durable for Q; §8.4 not yet satisfied, or the process died before the next `supervisor-status`.

**`ROW-M-NO-CUSTODY-BOOTSTRAP`.** This row must **not** use `TB-CUSTODY-BOOTSTRAP`, and v1_7's instruction to do so was mechanically impossible. Once `candidate_custody_recorded` is durable, the `initial_design` provider custody **has its downstream completion** under the installed `_downstream_recorded()` rule (`CLOSURE-INITIAL-PENDING` names exactly that event as its closure), so it is **no longer an unfinished custody** and §8.9.2 has nothing to discover. **The durable candidate custody is itself the evidence at B9; an unfinished provider custody is not required and does not exist.**

**Action:**

```
 1. Freshly authenticate the journal and derive the current transition state.
 2. Is the T5 process-custodied-provider-result supervisor operation itself
    incomplete -- its matching supervisor_operation_completed missing?
       yes -> recover THAT authenticated operation through operation-specific
              TB-RECOVERY-BOOTSTRAP / same-operation completion recovery, and
              append ONLY the missing completion.
       no  -> nothing is owed; proceed.
 3. Re-derive §8.4 establishment from the authenticated journal and current
    byte proofs -- a pure derivation, appending nothing.
 4. §8.4 complete      -> the next ordinary context binds Q.
    §8.4 not complete because bytes or chain evidence no longer prove it
                       -> LOOP_SAFETY_HOLD or LOOP_WAITING_RECOVERING with the
                          exact reason preserved (§18 row wording unchanged).
```

**Zero provider calls. Zero candidate recreation. Zero re-selection. Zero task preparation. Zero re-processing of a provider custody that is already closed.**

**Never:** invoke the pending-custody bootstrap; require an unfinished `initial_design` custody; re-seed; re-select; re-prepare; treat P as current again once Q is established; treat Q as current while Q is not established.

### Row N — handoff completed
**Proved:** Q established and bound; `supervisor-status` projects Q's ordinary state. **Action:** none. `loop-status` returns `LOOP_HANDOFF_COMPLETE`. **Never:** run any continuation command for P's acceptance again; re-enter the loop level for Q until Q itself reaches a terminal acceptance.

### 18.1 The invariants, restated

| Invariant | Rows |
|---|---|
| no duplicate provider call where the outcome is uncertain | C, G, **I** — reconcile first, always; §14.3; `INIT-NO-REDISPATCH` |
| **no provider call after a result was already saved** | **K.2** — unverifiable custody is `SAFETY_HOLD`, never absence; `CUSTODY-UNVERIFIABLE-HOLD` |
| **no candidate from an unadmitted result** | **J** — all ten `INIT-ADMISSION` checks re-run before T5; §14.5 |
| **a valid installed-contract result is never stamped invalid** | **D, H** — the dedicated B6d branches of §9.5a and §13.6a; P-23 |
| **an actionable T1 result with no proved root never becomes an admitted selection, a scope, a signal, or a question** | **D, D.1** — `T1-ACTIONABLE-ROOT` (§9.3a), `SEL-ADMISSION` proof 4, `SEL-ADMISSION-NO-ACTIONABLE-ROOTLESS`; P-33 |
| **no root is ever fabricated for a result that named none** | **D, D.1** — `T1-ACTIONABLE-ROOT-NO-DERIVATION`, `SEL-LEGACY-NO-ROOT-FABRICATION` |
| **an earlier-contract completed result is preserved, never re-dispatched, and permits at most ONE bounded current-contract replacement** | **D.1** — §9.7 `SEL-LEGACY-PRESERVE` / `-NEW-IDENTITY` / `-ONE-SHOT`; the fresh selection re-checks the frontier and may prove a different package |
| **the earlier-contract rule can never become a re-selection loop, and never a loophole for uncertainty or lost custody** | **D.1, C, K.2** — `SEL-LEGACY-NO-LOOP`, `SEL-LEGACY-NOT-A-NEW-LEGACY`, `SEL-LEGACY-NOT-UNCERTAINTY`, `SEL-LEGACY-NOT-CUSTODY-LOSS` |
| **bounded T1 output retry ends in a reachable, honest, restart-stable stop that owes no command and no append** | **D** — `T1-INVALID-OUTPUT-EXHAUSTION-STOP`, `T1-EXHAUSTION-DERIVED`, `T1-EXHAUSTION-RESTART-STABLE` (§9.6a); §7.4 guard; §23 `R-5e` |
| **no fake diagnosis consumption is ever created so that a closure command becomes callable** | **D, and §14.3 for T4** — `T1-NOT-A-CONSUMPTION` (§9.6a), `INIT-EXHAUSTION-IS-NOT-A-CONSUMPTION` (§14.3), §23 `R-5e` |
| **bounded T4 output retry likewise ends in a reachable, honest, restart-stable stop, and never re-selects a design run against a spent budget** | **I** — `INIT-EXHAUSTION-IS-WIRED` (§14.3), `INIT-EXHAUSTION-DERIVED` / `INIT-EXHAUSTION-NOT-STORED` (§17.2), the §7.4 T4 guard, §17.3, §25 `R115` |
| **an available T4 budget still retries exactly as installed — the stop ends a series that is over, it does not shorten one** | **I** — §14.3 table, §17.2 precedence note, §25 `R115` case A |
| **saved T1 result bytes are protected by their evidence, not by their terminal form** | **D, D.1** — `T1-CUSTODY-UNVERIFIABLE`, `T1-CUSTODY-NEVER-ABSENT` (§9.6b); §23 `R-11c`; R109 |
| **no second model call for one Piece-3 stage** | **E1–E5** — `T2-ONE-CALL`; reconcile-first at E2; the commit stage at E4 makes zero provider calls |
| **P can never authorize Q** | **E3, E4** — `T2-SCOPE-MATCHED`; §23 R-4 |
| **recovery binds the right package** | C, G, I, J, K, L, M — `TB-RECOVERY-BINDS-THE-RECORD`: the scope comes from the authenticated start, never from the phase. Row C binds **P** (Q does not exist yet); Rows G/I bind **Q** because their starts record Q. **The three custody-adjacent rows do NOT share one path:** Rows **J** and **L** may use §8.9.2 / Path B **while the `initial_design` custody genuinely remains unfinished**; Row **M** **must not**, because `candidate_custody_recorded` is already committed and that provider custody is therefore closed (`ROW-M-NO-CUSTODY-BOOTSTRAP`). Row M uses authenticated **same-operation completion recovery** where an operation completion is missing, and otherwise a **pure re-derivation** of the transition and §8.4 establishment that appends nothing. |
| no duplicate candidate | J, K, L, M — B0/B7/B8/B9; one pending intent; exclusive create |
| no skipped package | D, E, H, M — `CPB-SINGLE-TRANSITION`; every stop durable and named |
| no lost accepted state | every row — acceptance is append-only history; §23 R-1 |
| no false success | every row — a stop is a stop, a refusal is a refusal, neither is ever completion |

---

## §19 — PROVIDER-CALL RULES

### 19.1 Which provider calls the continuation may make

**Provider KINDS and provider-contacting COMMANDS are different counts, and this section states both.**

The continuation can reach exactly **FIVE provider kinds**, one open request at a time and no others:

| # | Provider kind | Reached by | Bound |
|---|---|---|---|
| 1 | `codex_next_package_selection` `[proposed]` | `continue-design-loop` | one bounded, read-only selection review per selection episode |
| 2 | `gpt_question_validation` (installed) | `dispatch-piece3-provider-review` | one bounded, read-only Piece-3 question-validation review per stage |
| 3 | `gpt_question_coverage_review` (installed) | `dispatch-piece3-provider-review` | one bounded, read-only coverage review per stage |
| 4 | `codex_next_design_task_preparation` `[proposed]` | `prepare-next-design-task` | one bounded, read-only task-preparation review per preparation episode |
| 5 | `claude_initial_design` `[proposed]` | `execute-initial-design` | one bounded Claude design run per initial-design episode, inside a disposable copy of the frozen committed source, outside N.H |

Those **five provider kinds** are reached through **four provider-contacting continuation commands**, because `dispatch-piece3-provider-review` derives the owed stage from controller state (`T2-STAGE-FROM-STATE`) and dispatches **exactly one** of kinds 2 and 3 — never both, and never a choice made by a caller.

The continuation makes no other model call. It runs no audit, no correction specification, no correction application, no diagnosis, and no explanation preparation — those belong to the supervisor (§16).

### 19.2 Bounds that apply to all five kinds

One open provider request at a time under the installed request identity and dispatch serial; the installed per-episode attempt cap and per-work-item episode machinery; the installed execution timeout and controller closure grace; the worker's `retry_series_key` backoff, which bounds **the work and not the reported state**, so an unreachable endpoint can never be polled in a hot loop; the installed availability-probe eligibility flag, which the worker may act on but never decide; and no provider call at all while the start gate is closed or the lease is not proved live.

### 19.3 Uncertain outcomes — one rule, for all five kinds

**`PROV-NO-REDISPATCH`.** Where a dispatched request's outcome is uncertain — timeout, killed process, unreadable result, missing terminal — the continuation **never re-dispatches**. It reconciles first, through the installed `reconcile-provider-request` lookup path, which asks what actually happened rather than asking again.

| Reconciliation outcome | Loop position |
|---|---|
| completed / `found_terminal` | resume from the custodied result |
| `absent_proved` | a **new request identity** may be opened; the old one stays as history |
| `lookup_transiently_failed` | `LOOP_WAITING_RECOVERING`, bounded backoff |
| **`lookup_unsupported`** (the local CLI case, P-17) | `LOOP_NEEDS_USER_ACTION`, naming the exact practical action |
| `found_terminal_result_unavailable` | `LOOP_NEEDS_USER_ACTION` |
| anything indeterminate | wait or hold — **never guess, never proceed on "probably nothing happened"** |

**And one position that is not a reconciliation question at all:** where a result was **already received and saved** and its custodied bytes no longer re-verify, there is nothing to reconcile — the request completed. That is `provider_result_custody_unverifiable` → `SAFETY_HOLD`, with zero further calls (`CUSTODY-UNVERIFIABLE-HOLD`, §14.6). **Losing saved evidence is never a licence to manufacture replacement evidence.**

**And one further position that is likewise not a reconciliation question** *(new in v1_9)*: where a **read-only T1 selection** request completed, its result was saved, its bytes **still re-verify**, and those bytes were **valid under an earlier version of the T1 contract** but are mechanically non-operative under the strengthened `T1-ACTIONABLE-ROOT` contract. There is nothing to reconcile there either — the request completed and its answer is intact and readable. **That is `SEL-LEGACY-CONDITION` → §9.7, and it is bounded to exactly one fresh current-contract selection under a new request identity.**

**And one last position that is not a reconciliation question either** *(new in v1_10)*: where a current-contract T1 request completed with a durable **`result_invalid`** terminal and the installed **bounded output-retry budget is exhausted**. There is nothing to reconcile there — the request completed and its answer is known to be unusable. **That is `T1-INVALID-OUTPUT-EXHAUSTION-STOP` → §9.6a: `LOOP_NEEDS_USER_ACTION`, null next command, zero further requests on the exhausted condition, and no `close-open-consumption`** — because a `next_package_selection` review opens no diagnosis consumption for that command to close (§5 P-34).

**The four positions are kept mechanically apart, and must never be conflated:**

| Position | Distinguishing durable evidence | Rule |
|---|---|---|
| **uncertain outcome** | **no** durable terminal for the request | reconcile first, never redispatch (`PROV-NO-REDISPATCH`) |
| **custody unverifiable** | terminal exists — **of any form, `result_received` or `result_invalid`**; saved bytes the record requires **fail** re-verification | `SAFETY_HOLD`, **zero** replacement calls (`CUSTODY-UNVERIFIABLE-HOLD`; for T1, `T1-CUSTODY-UNVERIFIABLE`, §9.6b) — **§9.7 is unavailable here**, and the custody is **never read as absence** |
| **earlier-contract, non-operative** | terminal exists; saved bytes **re-verify**; valid under the earlier contract; fail current admission **only** on `T1-ACTIONABLE-ROOT`; no replacement yet | **§9.7**, one bounded fresh selection, new identity, consumed deterministically |
| **current-contract invalid output, budget exhausted** *(new in v1_10; T4 wiring added in v1_11)* | a durable **`result_invalid`** terminal under the **current** contract, its custody re-verifying where the record requires it, and the installed `bounded_output_retry_budget()` returning **`exhausted`** | **§9.6a** for T1 (`t1_output_retry_exhausted`) and **§14.3 `INIT-EXHAUSTION-IS-WIRED`** for T4 (`initial_design_output_retry_exhausted`, §17.2) — in both cases the same honest stop: `LOOP_NEEDS_USER_ACTION`, null next command, **zero** further requests, **zero** owed appends, **no** `close-open-consumption`, **no** invented consumption, restart-stable |

Each is proved from durable evidence, not inferred from the others' absence, and **no failure of one ever grants the permission of another.** **Where two could be read at once, custody-unverifiable outranks the exhaustion stop** — safety before a practical stop (§9.6b, §7.4).

**`PROV-READONLY-EFFECTFREE`.** The four read-only review kinds (selection, question-validation, coverage review, task preparation) produce no effect outside their own custodied result. That is why a *new* episode after proved absence is safe. It is **not** a licence to redispatch on uncertainty: the rule above applies to all five kinds without exception, because an uncertain call is uncertain regardless of what a completed one would have done.

### 19.4 What no continuation provider call may ever do

Write into the real N.H checkout; run Git; decide acceptance; decide a package's status; compose a Ness-facing question; name or alter the target path; alter an authority order or a tool set; authorize implementation. The real checkout is never a provider's working directory and stays read-only to it.

---

## §20 — WORKER BEHAVIOR

### 20.1 During the Accept request

Unchanged and non-running. `READY_FOR_ACCEPTANCE` remains in `NON_RUNNING_STATES`, so no worker command runs while the offer stands, and the acceptance POST is the browser's request to the controller, not the worker's.

### 20.2 After acceptance is durable

**`ACCEPTED_FOR_DESIGN_ONLY` remains in `NON_RUNNING_STATES`**, so no ordinary supervisor command runs in that state, exactly as today. The accepted branch of `_step()` gains one bounded route `[proposed]`: after recovery reconciliation has run and returned nothing, the worker calls the read-only `loop-status` and may run **only** a command from the closed continuation set:

```
continue-design-loop                 [proposed]
dispatch-piece3-provider-review      [proposed]   -- reaches a provider (§12.3c.A)
commit-piece3-provider-result        [proposed]   -- provider-FREE (§12.3c)
prepare-next-design-task             [proposed]
execute-initial-design               [proposed]
process-custodied-provider-result    (installed)
reconcile-provider-request           (installed)
```

`dispatch-piece3-provider-review` is added to **both** `WORKER_COMMANDS` and `PROVIDER_CONTACTING_COMMANDS`, so the installed retry series and bounded backoff gate it like every other provider-reaching command.

`commit-piece3-provider-result` is added to `WORKER_COMMANDS` and **deliberately not** to `PROVIDER_CONTACTING_COMMANDS`: it makes zero provider calls (`T2-ONE-CALL`), so no retry series gates it.

**The public `question-validation` and `question-coverage-review` are deliberately NOT in the continuation set.** They keep their installed direct behaviour for the ordinary loop and for operator use (`T2-PUBLIC-COMMANDS-UNCHANGED`); the continuation reaches the same underlying logic through the two commands above.

**Exact registry effect.**

- `WORKER_COMMANDS` gains **all five** new execution commands: `continue-design-loop`, `dispatch-piece3-provider-review`, `commit-piece3-provider-result`, `prepare-next-design-task`, `execute-initial-design`.
- `PROVIDER_CONTACTING_COMMANDS` gains **exactly four**: `continue-design-loop`, `dispatch-piece3-provider-review`, `prepare-next-design-task`, `execute-initial-design`. It does **not** gain `commit-piece3-provider-result`.
- The **two installed** execution commands, `process-custodied-provider-result` and `reconcile-provider-request`, keep exactly the registrations the actual code already gives them; nothing here re-registers or re-classifies them.
- The public `question-validation` and `question-coverage-review` are **removed from the continuation set** (`T2-PUBLIC-COMMANDS-UNCHANGED`) and keep their installed behaviour for the ordinary loop and operator use.

### 20.3 Order of operations in the accepted branch

```
1. supervisor-status, proved                                    (installed)
2. recovery FIRST: reconcile_incomplete_operation(report)        (installed)
3. state == ACCEPTED_FOR_DESIGN_ONLY and acceptance_truth == PROVED_ACCEPTED?
     no  -> ordinary installed behaviour
4. loop-status (read-only)
5. loop_next_command is null            -> wait, with the loop_state's honest detail
6. loop_next_command not in the closed set -> SAFETY_HOLD, fail closed
7. provider-contacting and the backoff series is not eligible -> wait
8. start gate closed or lease not proved live -> wait
9. run exactly one continuation command; record the scheduling outcome
```

Steps 2, 7 and 8 are the installed gates, applied unchanged. Step 6 mirrors the installed refusal for an unknown next command.

**Step 5 is where both v1_10 stops land, and the worker gains nothing new to do** *(new in v1_10)*. An exhausted T1 invalid-output position returns `LOOP_NEEDS_USER_ACTION` with a **null** `loop_next_command` (§9.6a), and an unverifiable T1 custody returns `LOOP_SAFETY_HOLD` with a **null** one (§9.6b). Both therefore reach **step 5 and wait**, reporting the loop state's honest detail. **The worker runs no command, makes no provider call, appends nothing, and re-derives the same position on every pass** — it does not re-invoke `continue-design-loop` to rediscover an exhaustion the controller already derived (`T1-EXHAUSTION-RESTART-STABLE`). **`WORKER_COMMANDS` and `PROVIDER_CONTACTING_COMMANDS` gain nothing from this correction**, and **`close-open-consumption` is not added to the continuation set** (`CONTINUATION-SET-CLOSED-AT-SEVEN`, §7.5).

### 20.4 After the handoff

Once Q is established, `supervisor-status` no longer projects `ACCEPTED_FOR_DESIGN_ONLY`, step 3 fails, and the worker returns to its ordinary loop with no loop-level involvement. **The continuation route is unreachable except during a real transition.**

### 20.5 What the worker still never does

It composes no question, finding, correction, filename, candidate byte, route, PASS, acceptance, dependency class, binding, outcome fact, or identity of any kind. It decides no package and no target path. It reads the controller's answers and runs the command it is told to run, or waits. **The worker gains one branch and zero decisions.**

---

## §21 — UI BEHAVIOR

### 21.1 While a package is accepted and before the next is established

The UI may honestly show that package as accepted. The installed wording (`interview_ui/supervisor.py:288-302`) stays as written, with **one clause made conditional and only that one**: while a transition is genuinely in progress, "and no next package started" is no longer an unqualified truth, so the accepted card must not keep asserting it.

> *Accepted card (unchanged in substance):* "Ness accepted this exact candidate as a design. Nothing was adopted, integrated, implemented, marked PACKAGE_COMPLETE, closed, committed, or pushed."
>
> *Transition line (separate, present only while a transition is in progress) `[proposed]`:* "N.H is choosing and preparing the next design package from current sources. Nothing has been adopted, integrated, implemented, committed, or pushed."

**`UI-NO-REWRITE-HISTORY`.** Historical accepted-package cards are history: their wording is never rewritten, re-dated, re-scoped or re-interpreted. Only the **live** card for the currently-accepted package carries the transition line.

### 21.2 Once the new package is durably established

The UI may move to Q: its plain-language capability, its technical package, its framework/addition position **where proved by source**, its bundle placement **where settled or "not decided" where genuinely open**, its workflow state, and why Ness is or is not needed — the installed contract from Ness's live-loop decision §6, applied to a different package.

### 21.3 What the UI must never claim

Never that continuation is progress on the accepted package; never that a selection or a prepared task is a decision, an adoption, or an integration; never that a new package has started before its `validation_recorded` and initial custody are durable; never that the loop is "working" while it is holding, waiting, or stopped; never a next-package name the controller has not proved from source; never that acceptance caused any of it.

### 21.4 The change feed

The **What's changing** feed continues to carry only controller-confirmed, authenticated items — `controller_authenticated` true, a known feed item kind, a real `controller_event_sha256` — and through no other route. **No feed item is derived from a model asserting that its own work succeeded.**

---

## §22 — THE DESIGN-ONLY LIMIT

**`DESIGN-ONLY`.** Automatic continuation is automatic continuation of **DESIGN COMPLETION** only. It must never automatically enter, propose entering, or prepare the ground for: coding; implementation; production stores or markers; Register-C implementation; Master or Map integration; adoption; closure-record creation; Git add, commit, push, branch, tag or any other mutation; migration, deployment, go-live hardening or live-disk verification; creating `.nh_readings_store.jsonl` or `.nh_readings_production_authorized`; removing `.nh_roots.sealed`; or any Cursor instruction or patch.

**`DESIGN-ONLY-STOP`.** If the proved current frontier is later implementation or building work, the loop **stops** and reports `LOOP_DESIGN_CONTINUATION_COMPLETE` — design continuation is complete or deferred here — rather than building. That is a truthful terminal report about the design loop, not a claim that N.H is finished and not an authorization for anything.

This restates, at the one new automatic seam, what Master V10, the workflow's Phase-15 boundary, the eight-bundle plan's "work outside the eight bundles" and "no implementation authorization" sections, the five-additions package's timing sections, `cursorrules`, and every accepted closure record already require.

---

## §23 — FAIL-CLOSED RULES

Each rule names the condition and the response. In every case: **append nothing, change nothing, claim nothing, report the exact problem.**

**R-1 — Acceptance cannot be re-proved.** If `acceptance_truth` is not `PROVED_ACCEPTED` at any continuation boundary — including `UNRESOLVED` — no continuation step runs. `UNRESOLVED` remains `SAFETY_HOLD` with no command, no retry loop and no claim in either direction. Never continue on a remembered acceptance; never treat a refusal as an erasure of a committed acceptance.

**R-2 — The journal cannot be authenticated.** No continuation step runs; nothing is appended; the state is reported unreadable rather than assumed.

**R-3 — Two packages claim to be current.** More than one non-established scope holding post-acceptance evidence (`CPB-SINGLE-TRANSITION`), a scope established over a non-terminal current scope (`CPB-ORDERING-SAFETY`), or two Case-B anchors for one scope → `LOOP_SAFETY_HOLD`. Never prefer one, never drop one, never repair the record.

**R-4 — A Piece-3 authorization does not match the scope it would authorize.** A supervisor-era `validation_recorded` or `question_coverage_review_recorded` may be appended only when the unconsumed `piece3_provider_work_recorded` authorizing it carries the **same `package_scope_id`**. This closes P-10, where the installed gate builds an unscoped `Replay(events)` and would let package A's authorization satisfy package B's validation. A mismatch refuses the append. Never append first and fix the binding after.

**R-5 — A durable model result fails admission.** A custodied selection or prepared task that fails any of its re-admission proofs is not operative. A never-admissible result → `LOOP_SAFETY_HOLD`. A result made stale by moved bytes, a closed clearance, a changed decision binding, or a target path that is no longer new → preserved as history, consumed by nothing, and the owning phase is re-entered. Never normalise a path into existence; never substitute a similar file; never admit on `result_schema_valid` alone.

**R-5a — An ACTIONABLE T1 result names no proved root.** *(new in v1_9)* `controller_action` is `prepare_claude_task` or `hold_for_question_validation` and `package_source_path` is null, absent, empty, or fails any of `T1-ACTIONABLE-ROOT-PROOFS` (§9.3a) → **refuse the whole result.** At B6d it is an invalid output on the installed bounded output-retry route; at re-admission it is not a selection. **Never** fill the root in; never select one from `source_paths_checked`, the governing-authority subset, `package_id`, `package_title` or any other prose; never take one from a filename, listing order, timestamp or caller; never carry a placeholder or a shared fallback scope another package could answer to; and never let such a result establish a scope, become a `review_signal_recorded`, prepare a task, authorize a design run, or reach Ness. **The four non-actionable actions are unchanged and gain no root requirement** (`T1-NONACTIONABLE-UNCHANGED`).

**R-5b — The earlier-contract condition is not proved, or has already been consumed.** *(new in v1_9)* Any of `SEL-LEGACY-CONDITION`'s five proofs unprovable, two or more results claiming the condition, or a replacement request for the transition already existing in **any** phase → the §9.7 permission **does not apply**: nothing is appended, no provider is contacted, and the ordinary rules govern. **Never** take a second replacement; never re-open the fence; never substitute a counter, flag, marker or remembered state for the derivation (`SEL-LEGACY-ONE-SHOT`).

**R-5c — The earlier-contract rule is claimed for a position it does not describe.** *(new in v1_9)* Claiming §9.7 for an **uncertain** outcome (no durable terminal), for **unverifiable custody** (bytes that fail re-verification), for a **current-contract** result refused under `T1-ACTIONABLE-ROOT`, or for a result that fails admission for any reason **other** than the newly-required root, is a wiring defect → **fail closed**, nothing appended, **zero provider calls**. Reconciliation-first still governs uncertainty (`PROV-NO-REDISPATCH`); `SAFETY_HOLD` with zero replacement calls still governs unverifiable custody (`CUSTODY-UNVERIFIABLE-HOLD`); bounded output-retry still governs a contract-violating reply. **No failure of one position ever grants the permission of another** (§19.3).

**R-5d — A replacement selection is treated as privileged, or as pre-decided.** *(new in v1_9)* A replacement that skips or shortens `SEL-ADMISSION`, inherits a scope, a routed signal, a clearance or a prepared task, or is seeded with the earlier result's `package_id`, `package_title`, classification or frontier → **fail closed**. The fresh selection performs a **fresh current-source check** and may prove a different frontier (`SEL-LEGACY-FRESH-FRONTIER`, `SEL-LEGACY-NO-PRIVILEGE`, `SEL-NO-HARDCODE`).

**R-5e — A bounded output-retry exhaustion routed to a closure command that cannot apply.** *(new in v1_10)* Routing an exhausted `next_package_selection` — or `claude_initial_design` (§14.3) — invalid-output position to `close-open-consumption`, **or** creating a `diagnosis_strategy_consumption_started` / `diagnosis_strategy_consumption_terminated`, a correction specification, a diagnosis identity, a strategy identity or a blocking-finding authority in order to make such a command callable, **or** registering an eighth continuation execution command to carry it, is a **wiring defect** → **fail closed**, nothing appended, **zero provider calls**. The exhausted position is the honest stop of `T1-INVALID-OUTPUT-EXHAUSTION-STOP` (§9.6a): `LOOP_NEEDS_USER_ACTION`, null next command, no owed append. **Never** dispatch again on the exhausted condition; **never** fabricate a consumption to satisfy a command; **never** report that a consumption was closed, that the outcome is uncertain, that the old request reopened, that a package was selected, or that the loop completed successfully. **The legitimate installed use of `close-open-consumption` for a genuine open diagnosis consumption is preserved and must not be removed, genericised or weakened** (`T1-NOT-A-CONSUMPTION`, §7.5). A build that routes otherwise must fail its own rehearsals (R104, R107) rather than search for a transaction that was never opened.

**R-5f — An exhausted position that is not reachable, or not stable.** *(new in v1_10)* An exhausted T1 invalid-output position that falls through to `LOOP_SELECTION_REQUIRED` / `continue-design-loop`, that requires an append to be reported, that is remembered in a flag, marker, counter or second store rather than derived, or that returns a different answer on a second and third re-entry over identical authenticated evidence, is a **wiring defect** → **fail closed**. The position is derived from the authenticated requests, their terminals, their matching custody/evidence, the installed `bounded_output_retry_budget()` and the existing operation/dependency evidence — **and from nothing else** (`T1-EXHAUSTION-DERIVED`, `T1-EXHAUSTION-RESTART-STABLE`, §9.6a; §7.4 guard).

**R-6 — The selected package is the accepted package.** The derived scope equals the terminal-accepted scope → contradiction → `LOOP_SAFETY_HOLD`. Never re-open a package the loop has just closed.

**R-7 — The package binding is ambiguous.** More than one root, more than one routed scope, more than one admitted selection, or disagreement between the named root and the controller's own binder → refuse **before any provider is invoked**. Never ask a model to choose the package and then hold it to a closure it was never shown.

**R-8 — Clearance is not proved for the package about to be worked.** `evaluate_interview_clearance(scope_Q)` not unlocked, unlocked for a different scope, or unlocked without a statable settled-decision binding → no preparation and no design run. Never let clearance earned on one package authorise work on another.

**R-9 — No prepared task.** An initial design dispatch without a validated, currently-admissible prepared task for Q → refuse (`PREP-REQUIRED`). Never let Claude derive the design, the specification, or the target path for itself.

**R-6a — A pre-validation binding that cannot be constructed or reconstructed.** No admitted T1 selection, a Q that already holds a `validation_recorded`, two admissible selections, ambiguous roots, or a source fact that no longer re-proves → **fail closed** (`TB-PREVALIDATION-EXISTS-WHEN`, `TB-PREVALIDATION-RECOVERY`). Never fall back to P's binding for a Q operation; never accept a filename, model title or caller-supplied scope.

**R-6b — A missing or ambiguous identity-matrix row or variant.** A work-item kind or variant with no matrix row, or a state in which two Piece-3 variants appear possible or none is provable → **fail closed** at identity derivation, nothing appended, no provider contacted (`PIECE3-VARIANT-FROM-STATE`, P-30).

**R-6c — A fabricated Piece-3 field.** Manufacturing a routed signal or a `validation_set_id` merely to satisfy `identity.py` is prohibited (`PIECE3-NO-FAKE-FIELDS`). The honest null or empty form plus the correct variant is the only admissible route.

**R-6d — A work item whose reconstruction does not match.** A rebuilt `work_item_identity` differing from the identity the custody or prepared record names → **fail closed** (`WIM-REBUILD-IDENTITY-EQUALITY`).

**R-6e — A Claude kind dispatched to Codex.** `claude_initial_design` reaching `_dispatch_codex()`, or resolving to the Codex endpoint, is a wiring defect (`INIT-NEVER-CODEX`, P-32). The endpoint equality check cannot catch it, because both halves would agree on the wrong answer — only the explicit routing of §14.7 and its rehearsal do.

**R-6f — A T2 pre-context path used where its precondition cannot hold.** Requiring a pending custody for `dispatch-piece3-provider-review` (none exists yet) or for `commit-piece3-provider-result` (the custody is already closed) is a wiring defect (`TB-CUSTODY-ONE-COMMAND`, §8.9.4). Each command takes its own path: A, B or C.

**R-6g — A Piece-3 commit whose authorization evidence is not exactly one.** Zero authorizations, duplicates, wrong scope, wrong stage, an authorization whose named custody does not match, stale evidence, or any contradiction → **fail closed**, nothing appended, **zero provider calls** (§8.9.4 Path C step 6).

**R-6h — A recovery position routed to a bootstrap whose precondition cannot hold.** Requiring an unfinished custody at E1, E2, E4 or Row M is a wiring defect: at E1/E2 no custody exists yet, and at E4 / Row M the relevant custody is already closed by its own downstream completion (`T2-RECOVERY-OWNER-PER-POSITION`, `ROW-M-NO-CUSTODY-BOOTSTRAP`). Each position takes its one named owner, and a build that routes otherwise must fail its own rehearsals rather than search for evidence that cannot exist.

**R-7a — A provider prompt that contradicts its own result contract.** Rendering the generic supervisor instruction for `codex_next_package_selection`, `codex_next_design_task_preparation`, `gpt_question_validation` or `gpt_question_coverage_review` is a wiring defect (P-25, P-27): the model would be told to emit keys its exact-key contract refuses. `PROMPT-BY-KIND` is required; a build lacking it must fail its own rehearsals rather than burn output-retry budget on replies it forced to be invalid.

**R-7b — A rendered material that does not match its durable digest.** The installed refusal is preserved and extended to the extra: if the reconstructed prompt inventory or the reconstructed required-inputs inventory differs from the prepared record's `prompt_material_sha256` or `required_inputs_sha256`, **nothing is dispatched** and the saved result of an earlier attempt is stale rather than reused (`EXTRA-INPUTS-RECONSTRUCTION`, `EXTRA-INPUTS-STALE-NOT-SILENT`).

**R-7c — A caller trying to choose the Piece-3 stage or package.** `dispatch-piece3-provider-review` accepts no caller-supplied package binding and no stage override; either is refused, not used (`T2-STAGE-FROM-STATE`).

**R-7d — A transition custody of the wrong kind for the derived phase.** The pre-context bootstrap's closed set and phase agreement (§8.9.2 steps 3, 3b) refuse a `coverage_review` custody at a validation position, a `question_validation` custody at a coverage position, and an `initial_design` custody at either — **fail closed, nothing appended, no provider contacted**.

**R-8a — A Piece-3 commit without its scope-matched authorization.** The commit stage running with no unconsumed `piece3_provider_work_recorded`, or one whose `package_scope_id` is not `scope_Q`, or one whose `authorizes_event_type` names the other stage → **refuse the append**, nothing written (`T2-SCOPE-MATCHED`, R-4). Never create an authorization from the commit stage; never consume one twice.

**R-8b — A Piece-3 result whose commit position moved.** Source binding, manifest, scope, root, pagination generation/segment/page, or standing state no longer the ones the reply was validated against → the saved result is **preserved and refused as stale** (`T2-STALE-NOT-RECALL`). **Never** silently reuse it at a different position, and **never** call Codex again to paper over the drift — a fresh stage is a new request identity, with the old one kept as history.

**R-9a — An initial-design result that fails admission.** Any of `INIT-ADMISSION` I1–I10 failing (§14.5) → **no candidate is created**; the result is preserved as history, consumed by nothing, and routed by the installed invalid-output semantics. Never promote on `result_schema_valid` alone; never accept a produced path other than the prepared target; never accept a payload whose length or digest disagrees; never accept a result bound to a different prepared task.

**R-9b — A valid installed-contract result stamped invalid.** A `next_package_selection` or `next_design_task_preparation` result reaching `_generic_result_schema()` instead of its dedicated branch is a wiring defect, not a model failure (P-23). The dedicated branches of §9.5a and §13.6a are required; a build in which they are absent must fail its own rehearsals (R42, R44) rather than silently burn output-retry budget on valid results.

**R-10 — An uncertain provider outcome.** Reconcile first; never redispatch (`PROV-NO-REDISPATCH`, §19.3). Never fabricate a terminal; never proceed on "probably nothing happened".

**R-11 — A candidate identity does not match its intent.** The promoted file's `sha256`, byte length or payload differs from the write-ahead and the retained result → custody refused, nothing altered. Never adopt the observed digest; never delete or repair the file; never re-run the writer to regenerate it.

**R-11a — Custodied result bytes do not re-verify.** `engine.custodied_bytes()` refusing for an initial-design custody → `provider_result_custody_unverifiable` → `SAFETY_HOLD` → `LOOP_SAFETY_HOLD`, **zero new provider calls**, every durable record and the pending candidate intent preserved exactly (`CUSTODY-UNVERIFIABLE-HOLD`). Never treat it as provider absence; never abort the intent to enable a retry; never open another initial-design request; never return to T4.

**R-11b — Transition recovery cannot bind exactly one scope.** Zero or more than one matching authenticated operation start, a command mismatch, a start whose scope matches neither an established scope nor the single in-transition scope, or zero/more-than-one pending transition custody → **fail closed**, nothing appended (`TB-RECOVERY-BOOTSTRAP` steps 5 and 7, `TB-CUSTODY-BOOTSTRAP`). Never fall back to the current package; never accept a caller-supplied binding; never choose between two candidates for the scope.

**R-11c — A saved T1 result custody treated as absent.** *(new in v1_10)* A durable `next_package_selection` custody whose exact saved bytes are required by the durable record and which fail `engine.custodied_bytes()` re-verification, being skipped, swallowed, or read as "no result" — **for any terminal form, and specifically including `result_invalid`** — is a **wiring defect** → `provider_result_custody_unverifiable` → **`LOOP_SAFETY_HOLD`**, null next command, **zero provider calls**, every durable record preserved exactly (`T1-CUSTODY-UNVERIFIABLE`, `T1-CUSTODY-NEVER-ABSENT`, §9.6b). It covers **both** the preserved earlier-contract custody and any current-contract replacement custody, because both are the same work-item kind. **Never** treat it as provider absence; **never** ask a model again for an answer already received and saved; **never** derive the §9.7 permission while it holds (`SEL-LEGACY-NOT-CUSTODY-LOSS`); **never** weaken `engine.custodied_bytes()`; **never** delete or rewrite the custody; and **never** invent a restoration mechanism (`T1-CUSTODY-NO-RESTORATION-INVENTED`, §26 item 6). This rule **outranks** `R-5e`'s exhaustion stop: safety before a practical stop.

**R-12 — An earlier candidate moved.** Any already-held candidate fails its byte re-proof → the chain is not built on, no new candidate is created, nothing is repaired.

**R-13 — The source state moved under an operation.** Branch, HEAD or source binding is not the one the operation was computed against → refuse rather than complete against a source it did not read.

**R-14 — The lease cannot be proved live, or the start gate is closed.** No new continuation work starts. Nothing is taken over and nothing is changed.

**R-15 — A genuinely unresolved authority contradiction.** Ordinary fail-closed authority handling applies: preserve the conflicting evidence, surface the exact problem, choose no winner. **This does not include the Decision Defaults question, which Master V10 has already settled (§10) and which therefore neither stops the loop nor reaches Ness.**

**R-16 — The frontier is building work.** `LOOP_DESIGN_CONTINUATION_COMPLETE`, non-running, reported honestly. Never enter implementation (§22).

**R-17 — Anything unanticipated.** An unrecognised loop state or command, an event body failing its schema, an origin enum value replay does not know, or any contradiction between two authenticated records → `LOOP_SAFETY_HOLD`, append nothing, report the exact evidence. **Continuation is never the default answer to an unknown.**

---

## §24 — IMPLEMENTATION FILE IMPACT MAP

**No file below is modified by this candidate.** This is the map a later, separately authorized implementation would work from.

### 24.1 `controller/nh_loop.py`

| Area | Change | Nature |
|---|---|---|
| `build_supervisor_context()` (`:46308`), anchor loop (`:46322-46336`) | the §8 current-package rule; and construction of the §8.9 transition bindings for the transition operations that use them — `dispatch-piece3-provider-review`, `process-custodied-provider-result` (transition invocations), `commit-piece3-provider-result`, `prepare-next-design-task`, `execute-initial-design`, and the recovery of those exact operations | corrected selection; same fields, same proofs |
| `validated_package_bound_candidate()` (`:28096`) | §8.3 two-case anchor (Case A unchanged) | extension |
| `authenticated_candidate_custody()` (`:28191`) | §8.3 Case B anchor from the initial-origin write-ahead | extension |
| `CANDIDATE_INTENT_ORIGIN_*` (`:20771`), `CANDIDATE_CUSTODY_ORIGIN_*` (`:20754`) | one new value each (§15.2) | enum value addition |
| `controller_held_question_validation_package()` (`:27801`) | one new Class-0 precedence (§13.2) | precedence addition |
| `derive_package_source_binding()` (`:26983`) | one new seed class, reachable only from Class 0 | seed class addition |
| `supervisor_piece3_authorization_gate()` (`:32309`) | require scope match (R-4) | fail-closed strengthening |
| `NEXT_PACKAGE_PROMPT` authority line (`:433`) and the same literal at `:734`, `:1310`, `:2001`, `:2427`, `:2595`, `:24275`, `:24553` | `AUTH-V22` (§10.3) | authority-order correction |
| `NEXT_PACKAGE_PROMPT` root clause | **`T1-ACTIONABLE-ROOT-PROMPT`** (§9.3a): the same installed builder states that an **actionable** answer — `prepare_claude_task` **or** `hold_for_question_validation` — must name the exact `package_source_path` it selected, while the four non-actionable answers may leave it null. Bounded text correction inside the same builder and the same `prompt_material_sha256` binding; **no second prompt builder** (`PROMPT-NO-SECOND-BUILDER`). | bounded prompt correction |
| `validate_next_package_analysis()` (`:5006`), root block (`:5168-5201`) | **`T1-ACTIONABLE-ROOT`** (§9.3a): the non-null requirement extends from `prepare_claude_task` alone to **both actionable actions**. Every other proof — strict decoder, exact key set, both enums, the classification→action mapping, `validate_source_paths()`, `check_required_source_coverage()`, canonical-resolution equality, presence in `source_paths_checked`, `whole_check_complete` — is **unchanged**. The four non-actionable actions are **unchanged** and gain no root requirement. **This only ever refuses more; it admits nothing the installed validator refuses** (`SEL-B6D-STRENGTHENING-ONLY`). | fail-closed strengthening |
| `EXACT_REQUIRED_FILES` (`:3263`) | current authoritative Defaults basename; competing-artifact reporting that does **not** gate (§10.4) | preflight correction |
| `run_prepare_next_claude_task()` (`:7603`) | extract `run_design_task_preparation()` `[proposed]` (§13.3); the public command's behaviour unchanged | refactor, no behaviour change |
| `NhCliProviderTransport` (`:46200-46296`) | one further work-item shape for `claude_initial_design`, seeding the disposable workspace from Q's proved root instead of a predecessor candidate | extension of the installed transport |
| new: `loop-status` `[proposed]` | §7.3 read-only loop projection | new read-only command |
| new: `continue-design-loop` `[proposed]` | T1; and the one bounded earlier-contract entry of §9.7 — it is an **ordinary** T1 selection in every respect, distinguished only by the derived `SEL-LEGACY-CONDITION` that permitted this entry, and it opens a **new** provider request identity and **never** re-dispatches the old one | new command |
| `post_acceptance_transition_state()` `[proposed]` (§17.2) | two derived fields, `legacy_contract_selection` and `legacy_replacement_consumed` (§9.7, §17.2). **Both are pure derivations over the authenticated journal and current byte re-proofs, recomputed on every entry and every restart** — no counter, no flag, no marker, no second store, and no new journal event type or body key | derived-field addition |
| `post_acceptance_transition_state()` `[proposed]` (§17.2) | **two further derived fields, `t1_custody_unverifiable` and `t1_output_retry_exhausted`** (§9.6a, §9.6b, §17.2) *(new in v1_10)*. The second reads the **installed** `Replay.bounded_output_retry_budget()` — the same function the installed recovery table already consults — over the authenticated T1 request(s), their terminals and their matching custody/evidence. **Both are pure derivations recomputed on every entry and every restart**: no counter, no flag, no marker, no second store, no new journal event type, no new event body key, and **no mutable counter beyond the already-governing installed budget** | derived-field addition |
| `loop-status` `[proposed]` (§7.3, §7.4) | **two guards added to the position derivation, before the `t.selection is None` fall-through and in this order** *(new in v1_10)*: `t1_custody_unverifiable` → `LOOP_SAFETY_HOLD` / null, then `t1_output_retry_exhausted` → `LOOP_NEEDS_USER_ACTION` / null. **Read-only: both append nothing, dispatch nothing and hold no lock beyond the ordinary authenticated read.** No `loop_state` value and no `loop_next_command` value is added to the §7.3 table | read-only projection extension |
| `post_acceptance_transition_state()` `[proposed]` (§17.2) | **one further derived field, `initial_design_output_retry_exhausted`** (§14.3, §17.2) *(new in v1_11)*. It reads the **same installed** `Replay.bounded_output_retry_budget()` that `t1_output_retry_exhausted` and the installed recovery table already consult, over the authenticated `claude_initial_design` request(s), their terminals and their matching custody/evidence. **A pure derivation recomputed on every entry and every restart: no stored flag, no marker, no counter beyond the already-governing installed budget, no second retry calculator, no second state source, no new journal event type and no new event body key** (`INIT-EXHAUSTION-DERIVED`, `INIT-EXHAUSTION-NO-SECOND-CALCULATOR`, `INIT-EXHAUSTION-NOT-STORED`) | derived-field addition |
| `loop-status` `[proposed]` (§7.3, §7.4) | **one further guard** *(new in v1_11)*: `initial_design_output_retry_exhausted` → `LOOP_NEEDS_USER_ACTION` / null, placed **after** `t.prepared_task is None` (so the `initial_design` work item is derivable) and **before** `t.initial_result_custody is None` → `execute-initial-design` (the branch it exists to pre-empt). **Read-only: it appends nothing, dispatches nothing, opens no request identity, and adds no `loop_state` or `loop_next_command` value to the §7.3 table.** While the installed budget is `available` it is false and the ordinary T4 route is unchanged | read-only projection extension |
| new: `prepare-next-design-task` `[proposed]` | T3 | new command |
| new: `execute-initial-design` `[proposed]` | T4 | new command |
| `command_supervisor()` (`:46425-46446`) | **the construction ORDER is explicit, not an implementation guess, on two distinct paths.** (a) *Operation-specific recovery* (`supervisor-operation-status` carrying an operation id): the caller envelope is read and structurally validated **before** any context is built; the operation is discovered from the globally authenticated journal; **the scope its authenticated start records** is proved; and only then is the context built for that proved scope (`TB-RECOVERY-BOOTSTRAP` / `TB-RECOVERY-BINDS-THE-RECORD`, §8.9.1). (b) *A transition invocation of `process-custodied-provider-result`*, which carries **no envelope at all**: the pre-context discovery of §8.9.2 / §8.9.4 Path B runs **before** ordinary current-package context construction — fresh authenticated journal, transition freshly derived, **exactly one unfinished transition custody from the closed set `{question_validation, coverage_review, initial_design}`**, its **kind required to agree with the freshly derived loop phase**, its scope proved to be the single in-transition scope, fail closed on zero, on multiple, or on a wrong kind for the phase — and only then is the Q transition context built and the command invoked.
(c) *A transition invocation of `dispatch-piece3-provider-review`* takes **Path A** (§8.9.4): it runs before any Piece-3 custody exists and **must not** require one.
(d) *A transition invocation of `commit-piece3-provider-result`* takes **Path C** (§8.9.4): it is anchored on the one unconsumed scope-matched authorization, because by then the custody is already closed.
The no-operation-id `supervisor-operation-status` form, and every invocation while no transition is active, keep the installed order exactly (§8.9.3). | ordering correction |
| `command_question_validation()` (`:41599`) and `command_question_coverage_review()` | **extract two parts, duplicate nothing** (§12.3b): part A = everything through prompt construction plus the frozen pre-call source requirement; part B = everything from "a reply object is in hand" through the tail-CAS append. The public commands keep calling both parts in sequence and are **behaviourally unchanged** for the ordinary loop. The continuation reaches part A through the durable dispatch and part B through the provider-free commit. `run_codex_question_validation()` (`:38929`) and `run_codex_question_coverage_review()` (`:39223`) stay as the ordinary-loop transports and are **not** called on the continuation path. | refactor, no behaviour change |
| `build_supervisor_context()` — pre-validation path | construction of the **Q pre-validation transition binding** (§8.10) from the admitted T1 selection and controller-proved facts, with `validation_set_id` null, routed refs empty-or-real, and round-zero bound to Q's proved root. It is **never** returned as current and never reaches `status._project()`. | new bounded construction |
| `SUPERVISOR_CLAUDE_PROVIDER_KINDS` (`:45643-45646`) | gains `claude_initial_design`, so `supervisor_endpoint_binding()` maps it to `SUPERVISOR_CLAUDE_ENDPOINT` (§14.7 step 1) | registry addition |
| `NhCliProviderTransport.dispatch()` (`:46069-46084`) | an explicit `claude_initial_design` branch **above** the `_dispatch_codex()` fallthrough (§14.7 steps 2–3). `claude_correction` and `claude_acceptance_explanation` branches are unchanged. | explicit routing |
| `_supervisor_provider_prompt()` (`:45974`) | **`PROMPT-BY-KIND`** (§9.5b): one bounded closed dispatch on `provider_kind` selecting the installed builder for the four specialized kinds — `NEXT_PACKAGE_PROMPT` semantics, `build_prepare_task_prompt(...)`, `build_question_validation_prompt(...)`, `build_question_coverage_review_prompt(...)`. **Every other kind keeps the current generic instruction byte for byte**, acceptance-explanation preamble included. The generic lifecycle sentence is never prepended to the four. | bounded rendering rule |
| `_supervisor_provider_material()` (`:45687`) | reconstructs `required_inputs_inventory(context, work_item, extra)` **with** the extra it currently omits, and keeps its existing dual-digest refusal — which becomes the `EXTRA-INPUTS-RECONSTRUCTION` equality check (§9.5c). The prompt inventory already carries `context._current_prompt_extra`; the specialized prompt bytes ride the same `extra` slot so they are inside `prompt_material_sha256`. | reconstruction extension |
| new: `dispatch-piece3-provider-review` `[proposed]` | position A (§12.3c.A): proves Q, derives the owed stage from controller state, dispatches exactly one `question_validation` or `coverage_review` work item with the exact installed Piece-3 prompt. No caller stage or package input. | new command |
| new: `commit-piece3-provider-result` `[proposed]` | the provider-free Piece-3 commit (§12.3c), routed by the authorization's own `authorizes_event_type`; appends exactly one Piece-3 event; **zero provider calls** | new command |
| `main()` transition routing | the new Piece-3 commands are registered **above** the `SUPERVISOR_COMMAND_SET` fallthrough, alongside the existing direct names. **Each takes its OWN pre-context path (§8.9.4), and they are not interchangeable** (`TB-CUSTODY-ONE-COMMAND`): <br>• `dispatch-piece3-provider-review` → **Path A**. Runs **before** any Piece-3 custody exists; performs **no** pending-custody lookup. <br>• `process-custodied-provider-result` → **§8.9.2 / Path B**. Exactly one **unfinished** transition custody from the closed set `{question_validation, coverage_review, initial_design}`, with the kind required to agree with the freshly derived phase. <br>• `commit-piece3-provider-result` → **Path C**. Anchored on exactly one unconsumed scope-matched authorization and the exact request / custody / terminal evidence that authorization names; performs **no** pending-custody lookup. <br>**`command_question_validation()` and `command_question_coverage_review()` keep their existing direct dispatch and behaviour unchanged** (`T2-PUBLIC-COMMANDS-UNCHANGED`); no behaviour is switched on `NH_SUPERVISOR_WORKER`. | dispatch registration |
| `main()` dispatch (`:46495-46556`) | register the six new CLI names (`loop-status` plus the five new execution commands) **above** the `SUPERVISOR_COMMAND_SET` fallthrough, as `question-validation` already is. The two installed execution commands keep their existing dispatch. | dispatch registration |
| `USAGE` (`:3277`) | the **six** new CLI names: `loop-status`, `continue-design-loop`, `dispatch-piece3-provider-review`, `commit-piece3-provider-result`, `prepare-next-design-task`, `execute-initial-design` | text |

### 24.2 `controller/nh_supervisor/constants.py`

`WORK_ITEM_KINDS` (`:123`), `PROVIDER_KINDS` (`:138`), `PROVIDER_KIND_BY_WORK_ITEM_KIND` (`:155`), `WORK_ITEM_KIND_BY_PROVIDER_KIND` (`:165`), `RESULT_SCHEMA_ID_BY_PROVIDER_KIND` (`:169`): one entry each for the three new work-item kinds and their provider kinds. **`WORKFLOW_STATES` is not changed** — the loop states of §7.3 are loop-level, not workflow states.

### 24.3 `controller/nh_supervisor/schema.py`

Result-schema registration for the three new provider kinds — **provider-lifecycle schema ids only.** Registering a `result_schema_id` for a provider kind is controller-owned lifecycle metadata carried on `provider_request_prepared`; it **must not mutate the installed model-result key sets** `NEXT_PACKAGE_ANALYSIS_REQUIRED_KEYS` or `PREPARE_TASK_REQUIRED_KEYS`, which stay exactly as installed (`SEL-LIFECYCLE-METADATA-STAYS-OUTSIDE`, P-23). The initial-design result schema is the **exact six-key** contract of §14.5a — `result_schema_id`, `result_schema_version`, `produced_candidate_path`, `produced_candidate_sha256`, `produced_candidate_bytes`, `produced_candidate_payload_base64` — under `NH_CLAUDE_INITIAL_DESIGN_RESULT_V1` `[proposed]` version 1 (`INIT-ADMISSION` I1–I2). It is **not** `CLAUDE_RESULT_KEYS`: the five correction-specific keys are excluded (`INIT-RESULT-KEYS`). **The selection and preparation result *contracts* are the installed `next-package` analysis and prepared-task contracts (§9.1, §13.3); the Claude initial-design result contract is the installed produced-candidate result shape.** No event body key set is changed and **no event type is added** (§7.6).

### 24.4 `controller/nh_supervisor/engine.py`

`piece3_work_item()` (`:337-342`) gains the controller-derived variant selection of §12.3h and stops copying `validation_set_id` and `routed_signal_refs` blindly from the binding; the three new builders `next_package_selection_work_item()`, `next_design_task_preparation_work_item()` and `initial_design_work_item()` are added beside `design_audit_work_item()` (`:255`), each returning `(obj, work_item_identity(obj[, variant]))` with **no alternate identity path**. Prompt-template map entries for the three new provider kinds (`:354-355` pattern) and the work-item derivations, including the initial-design work item whose parent is Q's proved bound root and whose `target_candidate_path` is the prepared task's controller-validated target. The transport builds the initial-design result body with **exactly the six keys** of §14.5a and no others. `required_inputs_sha256()` / `required_inputs_inventory()` (`:395-403`) carry, in `required_source_paths` and the `extra` slot: the prepared task's target path and specification digest (making `INIT-ADMISSION` I8 provable) **and the controller-resolved required-files authority binding the prompt was built against** (making `SEL-AUTHORITY-BINDING-CARRIED` provable and reconstructable on restart). For the two Piece-3 kinds the `extra` slot likewise carries the frozen pre-call source requirement, so the provider-free commit can reconstruct it from durable evidence rather than remembering it. `custodied_bytes()` (`:935-946`) is **unchanged**. `build_prepared_request()` (`:642`) **already accepts `extra_inputs`** and needs no change; `required_inputs_inventory()` and `prompt_material_inventory()` (`:395-417`) already carry an `extra` slot, so the deterministic reconstruction of §9.5c adds no new inventory field and **injects no lifecycle key into any exact model contract**.

### 24.5 `controller/nh_supervisor/commands.py`

`_dispatch_simple()`-shaped paths for the selection and preparation work items; a `_b6g`-shaped consumption for the initial-design result that reuses the installed four-boundary resumption rather than reimplementing it (§15.1); registration in the command table (`:7448` pattern). **`_dispatch()` (`:790`) gains one keyword, `extra_inputs`, and forwards it to `engine.build_prepared_request(..., extra_inputs=...)`, which already accepts it (`EXTRA-INPUTS-SEAM`, P-26). No second request identity is created: `required_inputs_sha256` is already one of the seven inputs of `provider_request_identity`.**

**`_rebuild_work_item()` (`:2302-2341`) gains reconstruction for `next_package_selection`, `next_design_task_preparation`, `initial_design` and the three new Piece-3 variants (§17.3a), each through its one controller-owned builder, each with the identity-equality refusal. No alternate identity path is introduced.**

**`_b6f_piece3()` (`:4164-4192`) receives a bounded modification of its field-source logic so it carries truthful values per variant (§12.3h `PIECE3-AUTHORIZATION-TRUTHFUL`), while remaining the sole producer of `piece3_provider_work_recorded`. Its event body key set is unchanged and no schema change is required.**

**`_validate_result()` (`:1056-1072`) gains five dedicated branches, because the generic fallback is wrong for all five kinds:**
- `initial_design` → a new `_claude_initial_design_admission_checks()` `[proposed]` implementing `INIT-ADMISSION` I1–I10 (§14.5) against a new `INITIAL_DESIGN_RESULT_KEYS` `[proposed]` tuple of exactly the six keys of §14.5a — **not** a reuse of `_claude_admission_checks()` or `CLAUDE_RESULT_KEYS`, whose K3/K6/K7 and five extra keys are correction-specific;
- `next_package_selection` → the installed `validate_next_package_analysis()` semantics against the installed `NEXT_PACKAGE_ANALYSIS_REQUIRED_KEYS`, supplied with the carried authority binding, **and additionally enforcing `T1-ACTIONABLE-ROOT` so an actionable result with no proved root is not schema-valid at B6d and takes the installed invalid-output / bounded-output-retry route** (§9.5a, §9.3a). **No key is added to the model contract** (`SEL-LIFECYCLE-METADATA-STAYS-OUTSIDE`);
- `next_design_task_preparation` → the installed `validate_prepared_task()` contract against the installed `PREPARE_TASK_REQUIRED_KEYS`, cross-checked against the admitted T1 selection (§13.6a);
- `question_validation` → the installed `validate_question_validation_payload(...)` against `QUESTION_VALIDATION_REQUIRED_KEYS` (§12.3e);
- `coverage_review` → the installed `validate_question_coverage_review(...)` against `COVERAGE_REVIEW_REQUIRED_KEYS` (§12.3e).

**None of the five routes to `_generic_result_schema()`**, whose three required keys the four installed model contracts cannot carry (P-23, P-27). `_b6f_piece3()` remains the **sole producer** of `piece3_provider_work_recorded`, and its ownership, event type and authorization role are unchanged — but its **field-source logic is a bounded modification** (§12.3e D, §12.3h): the three Piece-3 fields come from the proved work item and proved state rather than from a blind `context.binding` read, because a pre-validation binding legitimately carries a null `validation_set_id`. It is **not** a new authorization producer and **not** a schema change. The continuation reaches it through the ordinary `process-custodied-provider-result` path for the installed `question_validation` / `coverage_review` kinds. The installed `provider_result_custody_unverifiable` → `safety_hold` route at `:2123-2147` is **used unchanged** and must not be softened for the initial-design kind (§14.6). `supervisor_operation_status()` (`:274-278`) receives a context already built for the scope its requested operation's authenticated start records (§8.9.1), so its `Replay(events, context.binding.package_scope_id)` at `:277` is correct by construction rather than by luck. `process_custodied_provider_result()` (`:2059-2071`) receives a context already built by the §8.9.2 / Path B pre-context discovery, so `situation.pending_custody` at `:2068` is already the right scope's — **the discovery must not be added inside this function, because by the time it runs the context is fixed.** The other two Piece-3 commands take **Path A** and **Path C** respectively and never perform a pending-custody lookup (`TB-CUSTODY-ONE-COMMAND`). Neither function is given a caller-supplied binding. When no transition is active both keep installed behaviour (§8.9.3). **`_b6f_piece3()` is not extended to any of the three NEW work-item kinds** — `next_package_selection`, `next_design_task_preparation` and `initial_design` are never routed into it (§7.6 rejection b). Its per-variant field-source extension applies only to the two installed Piece-3 kinds it already serves. **`close_open_consumption()` is NOT touched** *(new in v1_10)*: it keeps its exact installed precondition — an open `diagnosis_strategy_consumption_started` reported as `open_requires_closure` — its exact refusal when none exists, its exact `diagnosis_strategy_consumption_terminated` body, and its exact registration. **It is not genericised into a provider-terminal closer, not re-scoped to the three new work-item kinds, not weakened, and not removed** (`T1-NOT-A-CONSUMPTION`, §9.6a; §7.5). **It is not added to `CONTINUATION_EXECUTION_COMMANDS`**, which stays at exactly seven. The exhausted T1 and T4 invalid-output positions are **read-only derivations in the loop projection** and reach it not at all — and *(corrected in v1_11)* that claim is now **mechanically backed on both halves rather than asserted in prose**: T1 by `t1_output_retry_exhausted` and its §7.4 guard (§9.6a, §17.2), **and T4 by `initial_design_output_retry_exhausted` and its own §7.4 guard** (§14.3 `INIT-EXHAUSTION-IS-WIRED`, §17.2 `INIT-EXHAUSTION-DERIVED`, §24.1). **In v1_10 the T4 half of that sentence named wiring the document never specified (§5 P-35); it does now, and no implementation is authorized by saying so.** Where the installed recovery table's own `_recovery_outcome()` emits the string `close-open-consumption` for an exhausted `result_invalid`, that remains **installed behaviour this design does not alter**; what this design corrects is its own former claim that the string was T1's and T4's route (§5 P-34). `record_ness_acceptance()` and `acceptance_offer()` are **not touched**. `supervisor-operation-status` takes the §8.9.1 bootstrap (`TB-RECOVERY-BOOTSTRAP`); `process-custodied-provider-result` takes the §8.9.2 pending-custody bootstrap (`TB-CUSTODY-BOOTSTRAP`, Path B); `dispatch-piece3-provider-review` takes Path A; `commit-piece3-provider-result` takes Path C (§8.9.4).

### 24.6a `controller/nh_supervisor/identity.py`

`WORK_ITEM_MATRIX` (`:106-292`) gains **six** rows and loses none:

- `("next_package_selection", None)` — §9.5d `WIM-SELECTION`;
- `("next_design_task_preparation", None)` — §13.6c `WIM-PREPARATION`;
- `("initial_design", None)` — §14.5b `WIM-INITIAL`, the only new row with `target_candidate_path = R`;
- `("question_validation", "first_package_validation_unrouted")` — §12.3g A;
- `("question_validation", "first_package_validation_routed")` — §12.3g B;
- `("coverage_review", "package_coverage_unrouted")` — §12.3g C.

`("question_validation", None)` and `("coverage_review", None)` are **preserved byte-identically**. `WORK_ITEM_KEYS`, `WORK_ITEM_FORBIDDEN_KEYS`, `_ALWAYS_REQUIRED_WORK_ITEM_KEYS`, the `R`/`0`/`[]`/`N` vocabulary, `check_work_item_object()` and `work_item_identity()` are **unchanged** — the requirement vocabulary needs no mechanical extension, and no field is left to implementation guesswork.

One behavioural note the implementation must not disturb: `check_work_item_object()` resolves `variant=None` to the single row when a kind has exactly one. Adding variants to `question_validation` and `coverage_review` means those kinds now have several rows, so `variant=None` no longer auto-resolves for them — it resolves through the explicit `(kind, None)` row, which is exactly the installed row and is why the ordinary route is unaffected.

### 24.6 `controller/nh_supervisor/replay.py`

`_downstream_recorded()` gains: an explicit `CLOSED_BY_TERMINAL_ONLY_WORK_ITEM_KINDS` `[proposed]` set — `next_package_selection`, `next_design_task_preparation` — consulted **before** the `downstream_types` lookup and returning `True` for a completed `result_received` terminal on that request; and an ordinary `downstream_types` row for `initial_design` naming `candidate_custody_recorded` (§7.6a). The work-item-kind → effect-event map (`:388-391` pattern) gains the three kinds. `custodied_results_awaiting_processing()` is otherwise unchanged — the two read-only kinds stay terminal-only closed and the two Piece-3 kinds stay pending until their authorization is appended, which is exactly what `TB-CUSTODY-CLOSED-SET` relies on. `Replay` scoping is unchanged, and `piece3_provider_authorization()` is unchanged.

### 24.7 `controller/nh_supervisor/status.py`

`_project()` is **unchanged** — precedence 11.5 (`:1531-1536`) stays exactly as written, and the transition binding is never consulted by it (`TB-NOT-CURRENT`). The loop-level projection lives in `loop-status`.

### 24.8 `interview_ui/worker.py`

`WORKER_COMMANDS` gains **all five** new execution commands — `continue-design-loop`, `dispatch-piece3-provider-review`, `commit-piece3-provider-result`, `prepare-next-design-task`, `execute-initial-design`. `PROVIDER_CONTACTING_COMMANDS` gains **exactly four** of them: the same list **minus** `commit-piece3-provider-result`, which is provider-free by construction. The two installed execution commands keep the registrations the actual code already gives them. The public `question-validation` / `question-coverage-review` names are **removed from the continuation set** and keep their installed behaviour for the ordinary loop. The worker still decides nothing: `loop-status` names the command. `NON_RUNNING_STATES` keeps `ACCEPTED_FOR_DESIGN_ONLY`. The accepted branch of `_step()` gains the §20.3 route. `_non_running_detail()`'s accepted string is amended for the transition case. **This file carries the autonomy comment (§25.1).**

### 24.9 `interview_ui/supervisor.py`

`wording_for()` gains the transition line (§21.1); the snapshot gains the loop-level fields it must render. Historical wording unchanged.

### 24.10 `interview_ui/server.py`

A read-only render of the loop state where the UI needs it. **The acceptance GET and POST paths are not touched** (`INV-ACCEPT`).

### 24.11 Files that must NOT be touched

`NH_MASTER-20_CORRECTED_v10.md`; either Decision Defaults file; `cursorrules`; the Companion; the Design and Wiring Map; every workflow file; the five-additions decision package; **`v1_0` through `v1_9` of this bridge — including the accepted `v1_9` source, the earlier accepted `v1_8` source, and the separate `PACKAGE_COMPLETE` closure record that names `v1_8`**; every version of the acceptance-button design including v1.14 and v1.15 and its closure record; the AIC and UDOK accepted sources and closure records; every accepted standalone design and closure record; every historical candidate; the real journal, head, key and lock files; **the preserved earlier-contract selection request, its result custody and its terminal**; the real AIC candidate chain; **the preserved live implementation-correction evidence, which is evidence and not authority (§1.5) and is neither installed nor amended**.

**And one boundary this map does not cross** *(new in v1_10)*: `close_open_consumption()` itself is on this list in substance — it keeps its exact installed precondition, refusal, body and registration, and is **not** genericised, re-scoped, weakened or removed (§24.5, `T1-NOT-A-CONSUMPTION`). **Nothing in §24 authorizes an installation, and no production restart is authorized anywhere in this file.**

---

## §25 — DISPOSABLE REHEARSAL PLAN FOR LATER IMPLEMENTATION

Every rehearsal runs **offline, in a disposable copy, against a disposable journal and checkout**. None touches the real journal, the real state directory, the real N.H checkout, or a real provider. Providers are stubbed by a transport that fails loudly if contacted where a call is not expected.

### 25.1 The autonomy authorization, first

Before any rehearsal is written, the implementation must place, **at the exact new autonomous transition seam** — the `interview_ui/worker.py` branch that first runs a continuation command without a person — this exact comment:

```
# AUTONOMOUS: approved by user [2026-08-22]
```

`cursorrules` §10 requires it: "No new autonomous background task without an explicit `# AUTONOMOUS: approved by user [date]` comment." It records Ness's decision in §2.1 and **authorizes nothing else**: it must not be copied to any other seam, used to justify any other automation, or read as permission for an auto-start, a scheduled task, or an internet-facing route.

### 25.2 Rehearsals

| # | Rehearsal | Passes when |
|---|---|---|
| R1 | **Accept is still acceptance-only.** Drive the accept POST with a transport that raises on contact. | exactly one event appended; zero provider contacts; no candidate; no Git; no selection; no preparation |
| R2 | **Acceptance stays terminal for its own package.** | `next_command` null; `acceptance_truth` `PROVED_ACCEPTED`; `acceptance_required` false |
| R3 | **Binding parity on the real-shaped journal.** Run §8 against a disposable copy of the real journal **at whatever position it currently proves** — the fixture reads its length and tail from the copy it is given and asserts no fixed event count *(corrected in v1_9: the earlier wording fixed the journal at 84 events, which the real journal has since passed; a rehearsal that hard-codes a moving position tests the fixture, not the rule)*. | the same binding the installed code produces today, field for field, at that proved position |
| R4 | **Second package becomes current, first does not.** | `CPB-CURRENT` returns Q; P's history fully readable; Q's replay holds none of P's acceptance, PASS, audit or custody |
| R5 | **Incomplete transition does not steal the binding.** Q validated, prepared, even mid-Claude — but no custody. | current stays P at every step; `TB-NOT-CURRENT` holds |
| R6 | **Two transitions fail closed.** | `LOOP_SAFETY_HOLD`; nothing appended; both preserved |
| R7 | **Cross-scope Piece-3 authorization is refused.** | the append is refused (R-4); the journal is byte-identical afterwards |
| R8 | **No hard-coded package.** Grep the implementation for every package/addition/bundle/register literal, **including inside the §9.7 earlier-contract condition and any migration/transition helper**. | none appears in any selector, controller, worker or UI path; the earlier-contract condition is expressed purely as contract state — completed terminal, re-verifying custody, earlier-contract validity, the single failing `T1-ACTIONABLE-ROOT` proof, and the replacement fence — and names **no** package id, title, addition, bundle, register id, filename, frontier or event sequence number |
| R9 | **Closure evidence respected.** Fixture containing Addition 2's `PACKAGE_COMPLETE` receipt. | Addition 2 classified `settled` and not selected; Addition 3 not selected merely for being next |
| R10 | **Authority order.** Inspect the operative prompt bytes and the preflight set. | the current authoritative Defaults is authority #2; a competing artifact is reported and **does not** gate or reach Ness |
| R11 | **Selector contract coherence.** | one contract: the installed prompt, key set and validator; no second selection schema exists anywhere |
| R12 | **Admission is re-run, not remembered.** Admit a selection, then move the root's bytes, then restart. | the selection is stale, preserved, consumed by nothing; `LOOP_SELECTION_REQUIRED` returns; nothing rewritten |
| R13 | **Task preparation is required and reused.** Attempt an initial design dispatch with no prepared task. | refused (R-9); and the preparation path is the extracted stage-two function, with `prepare-next-claude-task` byte-for-byte unchanged in behaviour |
| R14 | **Target path and specification are proved before Claude.** | the dispatch carries a controller-validated new target path and a validated specification; Claude proposes neither |
| R15 | **Preparation possible-Ness escape.** Fixture where the specification cannot be stated without a Ness choice. | one `review_signal_recorded` bound to the proved root; no task prepared; no Claude call; `NEEDS_NESS_DECISION` only after validation **and** coverage review |
| R16 | **Claude result is custodied before any write-ahead.** | no `candidate_write_ahead_recorded` exists at any point before a schema-valid `provider_result_custody_recorded` + terminal |
| R17 | **Uncertain Claude outcome never redispatches.** Kill the process mid-dispatch; restart. | `reconcile-provider-request` runs first; with the CLI transport's unsupported lookup the position is `LOOP_NEEDS_USER_ACTION`; **zero** second Claude calls |
| R18 | **Restart from custodied Claude result uses exact bytes.** | the promoted file's sha256/bytes/payload equal the custodied result exactly; zero Claude calls |
| R19 | **Crash matrix A–N.** Kill at each of the fourteen positions, restart, assert. | every row's action happens and every row's "never" does not |
| R20 | **Idempotent re-entry.** Re-run each continuation command 3× at every position. | zero additional appends where the effect is already durable; B9 returns custody with zero appends |
| R21 | **Mechanical route end-to-end.** | one validation, one coverage review, one prepared task, one custodied Claude result, one candidate, one custody, then the supervisor's own fresh audit — and no audit or correction from any top-level path |
| R22 | **One writer, one promoter.** Instrument the promotion path. | exactly one code path creates the initial candidate; `command_execute_next_claude_task()` behaviour unchanged by the extraction |
| R23 | **Design-only limit.** Fixture whose frontier is building work. | `LOOP_DESIGN_CONTINUATION_COMPLETE`; no implementation; no Git; no production marker |
| R24 | **Ambiguity still refuses.** Disposable checkout with many untracked candidates and **no** admitted selection. | the live-checkout class fails closed exactly as today (P-9) |
| R25 | **Selector custody closes on its terminal.** Valid `codex_next_package_selection` custody + completed `result_received` terminal. | it is **not** in `custodied_results_awaiting_processing()`; `SEL-ADMISSION` still runs over its bytes; T2 may follow; `process-custodied-provider-result` is never invoked for it |
| R26 | **Task-preparation custody closes on its terminal.** Valid `codex_next_design_task_preparation` custody + terminal. | not pending processing; §13.6 re-admission still runs; T4 may follow; no effect event is manufactured |
| R27 | **Initial-design custody stays pending until T5.** Valid `claude_initial_design` custody + terminal. | it **does** remain pending processing; the candidate transaction consumes it; it closes only when `candidate_custody_recorded` proves the downstream completion |
| R28 | **Unverifiable saved custody holds, and never re-asks.** Saved initial-design custody exists → the result object is made missing/corrupt → restart. | `provider_result_custody_unverifiable`; `SAFETY_HOLD`; **zero** abort-to-retry transition; **zero** new Claude calls; the custody evidence, the terminal and the pending candidate write-ahead intent all remain preserved byte-identically |
| R29 | **Admission negative — wrong target.** `produced_candidate_path` ≠ the prepared `target_path`. | I3 fails; **no candidate created**; nothing promoted |
| R30 | **Admission negative — invalid base64.** | I5 fails; no candidate created |
| R31 | **Admission negative — wrong byte count.** Declared length ≠ decoded length. | I6 fails; no candidate created |
| R32 | **Admission negative — wrong SHA.** | I7 fails; no candidate created |
| R33 | **Admission negative — oversize payload.** Length > `MAX_CANDIDATE_BYTES`. | I6 fails; no candidate created |
| R34 | **Admission negative — bound to a different prepared task.** A result whose request inputs bind a different target/specification/scope. | I8 fails; no candidate created |
| R35 | **Admission negative — stale target at the promotion boundary.** Target path was new at production time, a file exists there now. | I4 fails at re-run; no overwrite; nothing promoted |
| R36 | **T1 selection recovery binds P, and never invents Q.** P accepted and current; the T1 selector dispatch is interrupted; restart. | the authenticated start is discovered globally and **proves P**; the **P** recovery context is built; the exact T1 request is reconciled; **Q is not inferred, named, guessed or partially bound anywhere** before a selector result is admitted; zero second selector dispatches |
| R37 | **Q transition recovery binds Q, from the record.** P accepted and current; Q already established as the one transition scope; a T3 or T4 operation is interrupted; restart. | the authenticated start **records Q**, so recovery builds the Q transition context; P is never bound; no duplicate call and no duplicate effect; the same run also proves the scope came from the record and not from the phase name |
| R38 | **Custody bootstrap discovers Q before context construction.** P current; Q has one pending unfinished `initial_design` custody. | `process-custodied-provider-result` freshly authenticates the journal, derives the active transition, finds the one unfinished custody, proves its scope, and builds the **Q** transition context **before** any ordinary current-package context exists; the exact custody is consumed; instrumenting the P-scoped path shows it is never constructed |
| R39 | **A stale `loop-status` report is never authority.** A prior `loop-status` response names Q; the journal then moves so that Q is no longer proved; the command runs. | the command re-proves against the **current** authenticated journal, refuses or stops as appropriate, and **never** acts on the stale report; zero appends; zero provider calls |
| R40 | **Ambiguous recovery evidence fails closed.** Two matching operation starts; or a start whose scope matches neither an established nor the single in-transition scope; or zero/two unfinished transition custodies; or a caller attempting to supply a package binding. | `SAFETY_HOLD` / refusal in every case; **zero appends**; **zero provider calls**; the caller-supplied field is refused rather than used |
| R41 | **The initial-design result key set is exactly six.** A result carrying any of `produced_lifetime_round`, `produced_batch_number`, `produced_round_in_batch`, `correction_specification_sha256` or `blocking_finding_refs`; and a result missing any of the six. | I1 fails in every case; **no candidate created**; and the schema registration is inspected to confirm it is not `CLAUDE_RESULT_KEYS` |
| R42 | **A valid installed next-package object reaches `result_received`.** A reply satisfying `NEXT_PACKAGE_ANALYSIS_REQUIRED_KEYS` exactly. | B6d admits it through the dedicated branch; the terminal is `result_received`, **not** `result_invalid`; no output-retry budget is consumed |
| R43 | **Lifecycle keys in the model object are refused.** The same reply plus `result_schema_id` and `result_schema_version`. | the installed exact-key validator refuses it; the schema registration is inspected to confirm the installed key set was not mutated |
| R44 | **A valid prepared-task object reaches `result_received`.** A reply satisfying `PREPARE_TASK_REQUIRED_KEYS` exactly. | B6d admits it through the dedicated branch; terminal `result_received` |
| R45 | **Lifecycle keys in the prepared-task object are refused.** | refused by the installed validator; `PREPARE_TASK_REQUIRED_KEYS` unmutated |
| R46 | **Wrong authority coverage, wrong package root, or wrong stage-one selection.** Three fixtures. | each fails **before** the result becomes operative — coverage measured against the carried binding, root proved against real source, stage-two `package_source_path` cross-checked against the admitted selection |
| R47 | **Restart still re-runs the full admission.** After a valid B6d pass, restart and re-enter. | all ten `SEL-ADMISSION` / §13.6 proofs run again over the custodied bytes; B6d admission alone never substitutes for them |
| R48 | **One Piece-3 stage, one model call.** Drive a full T2.a with a transport counter. | exactly one provider request for the stage; the commit stage contacts nothing; `run_codex_question_validation()` is never invoked on the continuation path |
| R49 | **Uncertain Piece-3 dispatch is reconciled, never resent.** Kill mid-dispatch; restart. | `reconcile-provider-request` runs first; with the CLI transport's unsupported lookup the position is `LOOP_NEEDS_USER_ACTION`; **zero** second Codex calls |
| R50 | **Authorization is scope-matched.** A `piece3_provider_work_recorded` under P's scope, with Q's Piece-3 event owed. | the commit is refused (R-8a / R-4); the journal is byte-identical afterwards |
| R51 | **The commit consumes the same custodied result and appends once.** Run positions C→D twice. | exactly one `validation_recorded` (or one `question_coverage_review_recorded`); the authorization is consumed once; zero provider calls; the second run appends nothing |
| R52 | **Position drift makes the saved result stale.** Move the source binding, or the pagination position, or the standing state between custody and commit. | the result is **preserved** and the stage fails closed as stale; no Piece-3 event is appended; **zero** Codex calls; a fresh stage would be a new request identity |
| R53 | **Crash positions E1–E5.** Kill at each; restart; assert. | every row's action happens and every row's "never" does not: no duplicate call, no lost custody, no duplicate authorization, no duplicate Piece-3 event, restart reaches the same Q, no manufactured question, no false success |
| R54 | **T1 prompt bytes match the T1 contract.** Capture the exact bytes sent for `codex_next_package_selection`. | they contain **no** instruction to emit `result_schema_id` / `result_schema_version`; the reply is an exact valid `NEXT_PACKAGE_ANALYSIS_REQUIRED_KEYS` object |
| R55 | **T3 prompt bytes match the T3 contract.** Same, for `codex_next_design_task_preparation`. | no lifecycle instruction; the reply is an exact `PREPARE_TASK_REQUIRED_KEYS` object |
| R56 | **The exact T1/T3 prompt bytes are inside `prompt_material_sha256`.** Alter one byte of the rendered prompt and re-render. | the digest differs and `_supervisor_provider_material()` refuses **before** dispatch; zero provider contacts |
| R57 | **The extra is genuinely in `required_inputs_sha256` and reconstructable.** Dispatch with an extra, then restart and re-render. | the recomputed inventory equals the durable digest; the request identity is unchanged; the same extra is obtained by derivation, never from process state |
| R58 | **Changed reconstruction is stale, never silently accepted.** Move the authority set, the admitted selection, or the frozen source between dispatch and re-render. | the digest differs; the saved result is preserved and refused as stale; **zero** provider calls; nothing is validated against the new inputs |
| R59 | **T2 validation gets the real Piece-3 prompt.** Capture the bytes sent for `gpt_question_validation`. | they are the `build_question_validation_prompt(...)` output, **not** the generic supervisor prompt |
| R60 | **T2 coverage gets the real coverage prompt.** | they are the `build_question_coverage_review_prompt(...)` output |
| R61 | **A valid `QUESTION_VALIDATION_REQUIRED_KEYS` reply reaches `result_received`.** And a second fixture adds the two lifecycle keys. | the valid reply is admitted by its dedicated branch; the lifecycle-key fixture is refused as an extra key by the installed validator |
| R62 | **A valid `COVERAGE_REVIEW_REQUIRED_KEYS` reply reaches `result_received`.** Same lifecycle-key negative. | admitted; the negative refused |
| R63 | **One T2 stage, one Codex invocation.** Drive a full stage with a transport counter. | exactly one invocation; the commit contacts nothing; no generic-then-Piece-3 double call |
| R64 | **`dispatch-piece3-provider-review` derives its own stage.** Run it with the validation stage owed, then with the coverage stage owed; then attempt a caller-supplied stage and package override. | the owed stage is chosen from controller state each time; both caller overrides are refused, not used |
| R65 | **The public Piece-3 commands are unchanged.** Invoke `question-validation` and `question-coverage-review` manually. | identical behaviour to the installed baseline; no dependence on `NH_SUPERVISOR_WORKER` |
| R66 | **A pending `question_validation` custody is found while P is current.** | the pre-context bootstrap finds it by the closed set, proves Q's scope and the phase agreement, and builds Q's context before any P context exists |
| R67 | **A pending `coverage_review` custody is likewise found.** | same |
| R68 | **A pending `initial_design` custody still works.** | T5 is unaffected by the widened closed set |
| R69 | **Wrong-kind or multiple transition custody fails closed.** A `coverage_review` custody at a validation position; two unfinished custodies; a selector custody offered as pending. | fail closed **before** context construction in every case; zero appends; zero provider calls; the selector custody is never a member of the pending set |
| R70 | **`_b6f_piece3()` appends exactly one Q-scoped authorization.** Re-enter position B three times. | one authorization; scope-matched; zero additional appends |
| R71 | **The commit reuses the exact saved reply.** Run positions C→D twice. | the same custodied bytes are consumed; **zero** provider calls; at most one Piece-3 event |
| R72 | **Crash after dispatch never causes a second Codex call.** Kill mid-dispatch at each T2 stage; restart. | reconcile-first; with the CLI transport's unsupported lookup the position is `LOOP_NEEDS_USER_ACTION`; zero second calls |
| R73 | **Crash after custody / authorization / commit resumes cleanly.** | no duplicate custody, no duplicate authorization, no duplicate Piece-3 event |
| R74 | **One Q pre-validation binding exists after T1 admission.** Admit a T1 selection; no Q validation yet. | exactly one pre-validation binding constructs; `validation_set_id` is null; routed refs empty; round-zero is Q's proved root |
| R75 | **The pre-validation binding is never reported as current.** Query `supervisor-status` and the UI throughout. | P is current at every point; the pre-validation binding never appears in a projection |
| R76 | **T2's first question-validation dispatches under it.** | the dispatch succeeds under binding 2; the work item takes variant A or B; no fake field is present |
| R77 | **It retires on Q's first `validation_recorded`.** Append the validation; re-derive. | binding 2 is no longer constructible; binding 3 takes over; a construction attempt of binding 2 fails closed |
| R78 | **Restart of a pre-validation T2 operation rebuilds the exact binding.** Kill mid-operation; restart. | rebuilt from the authenticated start + re-admitted T1 selection + current source re-proof; identical fields; no filename, title or caller input used |
| R79 | **No admitted selection and no validation → no Q binding.** | neither binding 2 nor binding 3 constructs; fail closed; nothing appended |
| R80 | **Two admitted selections or ambiguous roots → fail closed.** | refusal; zero appends; zero provider calls |
| R81 | **`next_package_selection` passes `identity.py` and re-derives after restart.** | the object validates against its matrix row; the identity is stable across restart |
| R82 | **`next_design_task_preparation` does the same.** | validates; identity stable |
| R83 | **`initial_design` does the same.** | validates with `target_candidate_path` non-null; identity stable |
| R84 | **Matrix negatives.** Remove a required field; add an illegal one; supply a value where the row requires null. | each fails closed at `check_work_item_object()`; no dispatch occurs |
| R85 | **First mechanical Q validation with ZERO routed signals and NO prior set.** | variant A resolves; a valid identity derives; **no routed signal and no `validation_set_id` is invented** |
| R86 | **First Q validation with a genuine routed signal.** | variant B resolves; refs are the real ones; `validation_set_id` is still null |
| R87 | **Q coverage review with ZERO routed signals.** | variant C resolves; `validation_set_id` is the real one from Q's first validation |
| R88 | **The ordinary routed Piece-3 route is unchanged.** Run the installed route against the installed baseline. | byte- and behaviour-compatible; `(kind, None)` rows untouched |
| R89 | **Variant selection is controller-derived.** Attempt a caller-supplied and a model-supplied variant; then construct a state where two variants would appear possible. | caller and model variants are refused or ignored as appropriate; the ambiguous state fails closed |
| R90 | **`_b6f_piece3()` writes one truthful Q-scoped authorization per variant.** | one authorization each; `validation_set_id` null for A/B and real for C; standing real; scope_Q in every case |
| R91 | **P authorization cannot satisfy Q.** | the gate refuses; the journal is byte-identical afterwards |
| R92 | **`claude_initial_design` resolves to the Claude endpoint and branch.** | `supervisor_endpoint_binding()` returns the local Claude endpoint; the explicit Claude branch runs |
| R93 | **`claude_initial_design` causes ZERO Codex invocations.** Instrument `_dispatch_codex()`. | it is never entered for this kind |
| R94 | **Its result has exactly six keys.** | the six `INIT-RESULT-KEYS`; no correction-specific round, specification or finding field |
| R95 | **Path A dispatches with no custody present.** Drive T2 position A with zero Piece-3 custodies in the journal. | the dispatch proceeds; it never performs a pending-custody lookup; the owed stage and binding are derived from controller state |
| R96 | **Path C is anchored on the authorization, not a custody.** Drive T2 position C after `_b6f_piece3()` has closed the custody. | the commit proceeds from the one unconsumed scope-matched authorization; no "unfinished custody" lookup occurs; **zero** provider calls |
| R97 | **Path C negatives.** Zero authorizations; two authorizations; wrong scope; wrong stage; an authorization whose named custody does not match; stale evidence. | fail closed in every case; zero appends; zero provider calls |
| R98 | **`_b6f_piece3()` ownership is unchanged while its field sources are not.** Inspect the produced event across all four variants. | one producer, one event type, no `validation_recorded` / `question_coverage_review_recorded` appended by it; and the three Piece-3 field values come from the proved work item and state, with a null `validation_set_id` under variants A and B |
| R99 | **Registry counts are exactly as designed.** Inspect `WORKER_COMMANDS` and `PROVIDER_CONTACTING_COMMANDS`. | five new execution names in the first; exactly four of them in the second; `commit-piece3-provider-result` absent from the second; the two installed execution commands unchanged |
| R100 | **Path routing is exactly A / B / C.** Instrument the pre-context discovery of each of the three Piece-3 commands. | `dispatch-piece3-provider-review` takes Path A, `process-custodied-provider-result` takes Path B, `commit-piece3-provider-result` takes Path C; **neither A nor C performs an unfinished-custody lookup** |
| R101 | **E1–E5 each take their exact recovery owner.** Kill at each of the five T2 positions; restart; instrument which recovery route runs. | E1 ordinary request retry under the same identity; E2 `TB-RECOVERY-BOOTSTRAP` then reconcile-first; E3 Path B then `_b6f_piece3()`; E4 Path C; E5 same-operation completion only. **No duplicate provider call, no duplicate authorization, no duplicate Piece-3 event** in any of the five |
| R102 | **B9 / Row M needs no unfinished provider custody.** Fixture: a valid `claude_initial_design` result was custodied; the candidate transaction completed through `candidate_custody_recorded`; the provider custody is therefore closed; handoff or operation completion has not yet been observed. | recovery does **not** call `TB-CUSTODY-BOOTSTRAP`; **no unfinished `initial_design` custody is required or sought**; the authenticated operation is completed if its completion is missing, otherwise establishment is simply re-derived; Q binds once §8.4 proves complete; **zero Claude calls; zero Codex calls; zero second candidate creation; zero re-selection; zero duplicate custody** |
| R103 | **No real state touched.** Byte-compare the real journal, head, key, lock and the whole `NH-GOVERNANCE` tree before and after the whole suite. | byte-identical |
| **R104** | **An actionable rootless `genuinely_open_for_ness` result is refused and never becomes a Q — and repeating it is bounded and ends honestly.** *(v1_9; extended in v1_10)* A current-contract T1 reply with `classification: genuinely_open_for_ness`, `controller_action: hold_for_question_validation`, `package_source_path: null`, `whole_check_complete: true` and a full, coverage-passing `source_paths_checked`. Drive it through B6d, then through restart re-admission. **Then repeat the same invalid reply until the installed bounded output-retry budget is exhausted.** | **refused at B6d** — not schema-valid, terminal `result_invalid`, the installed bounded output-retry budget consumed and no more; **never** an admitted selection; **no scope established**; **no `review_signal_recorded` appended**; **no root derived, name-matched or fabricated from `source_paths_checked`, `package_id` or `package_title`**; no question composed; no Claude call; the journal is byte-identical apart from the ordinary invalid-output records. **And on repetition** *(added in v1_10)*: the retries are **bounded** by the installed budget and never open a fresh selector identity; when the budget reaches `exhausted` the position is `T1-INVALID-OUTPUT-EXHAUSTION-STOP` — **`LOOP_NEEDS_USER_ACTION`, `loop_next_command` null, zero further provider requests on the exhausted condition, zero owed appends** — and **NOT** `close-open-consumption`: **no `close-open-consumption` is invoked or owed, no `diagnosis_strategy_consumption_started` or `diagnosis_strategy_consumption_terminated` is appended, no correction specification / diagnosis identity / strategy identity / blocking-finding authority is manufactured, no new event type, no new state store and no eighth continuation execution command appears**, and the reported reason claims no closed consumption, no uncertainty, no reopened old request, no selection and no successful completion |
| **R105** | **An actionable `genuinely_open_for_ness` result WITH a proved root is admitted — for question validation only.** *(new in v1_9)* The same reply with a real, resolvable, canonical `package_source_path` that is present in `source_paths_checked`. | admitted under all ten `SEL-ADMISSION` proofs; it enters **exactly** the §11 route — one `review_signal_recorded` bound to the proved `scope_root_path`, then independent question validation, then independent question-coverage review; **it does NOT prepare a Claude task, does NOT authorize a design run, and does NOT ask Ness anything**; `NEEDS_NESS_DECISION` is reachable **only** after both independent stages still leave a validated question standing |
| **R106** | **The real-shaped earlier-contract condition causes exactly ONE new selection request identity.** *(new in v1_9)* Fixture shaped like the real preserved lineage: a completed earlier-contract `next_package_selection` request with a durable `result_received` terminal, custody whose bytes **re-verify**, a rootless actionable `genuinely_open_for_ness` payload, and **no** replacement request. | **exactly one** new `next_package_selection` request identity is prepared; the **old `provider_request_identity` is not re-dispatched, not re-opened and receives no further append**; the old events and result bytes are **byte-identical afterwards**; **no root is fabricated**; **no `review_signal_recorded` is appended from the rootless result**; its `simple_explanation` appears in no question |
| **R107** | **Restart does not open a second replacement, at ANY phase of the first one.** *(new in v1_9)* Restart and re-enter the loop three times from each of **five** durable positions of the replacement request: (a) `provider_request_prepared` only, never dispatched; (b) dispatched, outcome uncertain, no terminal; (c) terminal `result_received`, valid and admitted; (d) terminal `result_received`, valid, later made **stale**; (e) terminal `result_invalid`. | in **all five**, `SEL-LEGACY-CONDITION` proof 4 **fails** — existence is consumption — the earlier-contract permission is **consumed**, and **no second replacement request is opened**; the ordinary rules govern instead: (a) `SAFE_TO_RETRY` under the **same** prepared identity, (b) **`reconcile-provider-request` first** and never a second dispatch, (c) the admitted route, (d) ordinary stale-selection handling, (e) **the installed bounded output retry while the budget remains `available`, and once it is `exhausted` the honest stop of `T1-INVALID-OUTPUT-EXHAUSTION-STOP` — `LOOP_NEEDS_USER_ACTION`, `loop_next_command` null, zero further provider calls, NO `close-open-consumption`, NO diagnosis consumption created, and NO second legacy replacement** *(corrected in v1_10)*; **zero additional provider calls** attributable to the earlier-contract rule in any of the five. **And the restart assertion for position (e) with the budget exhausted** *(added in v1_10)*: **re-enter the exhausted state three times → the identical `LOOP_NEEDS_USER_ACTION` with a null next command each time → zero appends → zero provider calls**, with the journal byte-identical across the three re-entries; the exhausted position is never re-derived by re-invoking `continue-design-loop`, and it is never carried in a flag, marker, counter or second store (`T1-EXHAUSTION-DERIVED`, `T1-EXHAUSTION-RESTART-STABLE`) |
| **R108** | **An uncertain replacement dispatch reconciles first and never duplicates.** *(new in v1_9)* Kill the process mid-dispatch of the replacement request; restart. | `reconcile-provider-request` runs **first**; with the local CLI transport's unsupported lookup the position is `LOOP_NEEDS_USER_ACTION`; **zero** second dispatches; the earlier-contract rule is **not** re-entered to justify one (`SEL-LEGACY-NOT-UNCERTAINTY`, R-5c) |
| **R109** | **Unverifiable custody still SAFETY_HOLDs and never gains a replacement call — whatever the terminal form is.** *(v1_9; extended in v1_10)* **Three** fixtures: (a) the **earlier-contract `result_received`** custody is made missing/corrupt; (b) the **current replacement `result_received`** custody is made missing/corrupt; **(c) the current replacement `result_invalid` custody is made missing/corrupt, where that invalid result has saved custody the durable record requires** *(added in v1_10)*. | in **all three**, `engine.custodied_bytes()` refuses → `provider_result_custody_unverifiable` → `SAFETY_HOLD` → **`LOOP_SAFETY_HOLD`** with a null next command; **zero** replacement or provider calls of any kind; **§9.7 is unavailable** because proof 1 fails; every durable record is preserved byte-identically. **And specifically for (c)** *(added in v1_10)*: **the saved evidence is NOT treated as absent merely because its terminal is `result_invalid`** (`T1-CUSTODY-NEVER-ABSENT`, §9.6b) — it does not silently read as "no result", the loop does not fall through to `LOOP_SELECTION_REQUIRED`, no model is asked again for an answer already received and saved, and this `LOOP_SAFETY_HOLD` **outranks** the exhaustion stop of §9.6a where both could otherwise be read at once. `engine.custodied_bytes()` is **not weakened**, the custody is **not** deleted or rewritten, and **no restoration mechanism is invented** |
| **R110** | **A valid replacement `genuinely_open_for_ness` + proved root takes exactly the existing §11 route.** *(new in v1_9)* | the §11 route runs unchanged and in full — one review signal bound to the proved root, independent validation, independent coverage — with **no** shortcut, **no** inherited clearance and **no** elevated trust (`SEL-LEGACY-NO-PRIVILEGE`); the route is byte-for-byte the accepted v1_8 route |
| **R111** | **A valid replacement mechanical result + proved root takes exactly the existing mechanical route.** *(new in v1_9)* | the §12 → T2 → T3 → T4 → T5 route runs unchanged, with every accepted admission, clearance, preparation, custody and promotion proof intact |
| **R112** | **The fresh selection may prove a DIFFERENT frontier, and nothing is hard-coded.** *(new in v1_9)* Give the replacement a source state in which the honest current frontier is a **different** package from the earlier result's, and a second fixture in which the honest answer is a **non-actionable** classification. | the replacement returns the frontier the **current sources** prove — a different package in the first fixture, an honest stop/wait/defer in the second; the earlier result's `package_id`, `package_title`, classification and `source_paths_checked` are **not** seeded, preferred or carried forward; grepping the implementation finds **no** package literal in the path (`SEL-LEGACY-FRESH-FRONTIER`, `SEL-NO-HARDCODE`) |
| **R113** | **The four non-actionable classifications are unchanged — no root requirement was invented for symmetry.** *(new in v1_9)* One valid reply for each of `settled` / `report_settled`, `waiting_on_another_choice` / `wait_dependency`, `future_non_blocking` / `defer_future` and `later_building_or_disk_work` / `defer_build`, each with `package_source_path: null`. | all four are **accepted** exactly as installed, receive valid terminals, and take their existing §9.4 / §9.6 stop, wait and defer semantics; none is refused for lacking a root; the installed validator's non-actionable behaviour is byte- and behaviour-compatible with the accepted baseline (`T1-NONACTIONABLE-UNCHANGED`) |
| **R115** | **The T4 / `claude_initial_design` bounded invalid-output exhaustion rule is actually wired, and only ends a series that is already over.** *(new in v1_11)* A disposable fixture for one established Q holding an **admitted prepared task** (so the `initial_design` work item is derivable) and a `claude_initial_design` request series. Drive **six** cases against `post_acceptance_transition_state()` and `loop-status`, instrumenting every dispatch, every append and every provider contact. **(A)** a `result_invalid` terminal with the installed `bounded_output_retry_budget()` returning **`available`**. **(B)** the same, with the budget **`exhausted`**. **(C)** a **governed oversize-invalid** initial-design output with the budget **`exhausted`**. **(D)** restart three times over **identical authenticated exhausted evidence**. **(E)** and **(F)** are negative obligations asserted across **all** of the above. | **(A)** `initial_design_output_retry_exhausted` is **false**; the ordinary installed T4 retry and recovery behaviour of §14.3 **remains available and unchanged** — the position still reaches `LOOP_INITIAL_DESIGN_REQUIRED` / `execute-initial-design` under the installed caps, episode machinery and `retry_series_key` backoff, and **no retry that is still owed is removed**. **(B)** `initial_design_output_retry_exhausted` is **true**; the §7.4 guard fires **before** the `initial_result_custody is None` fall-through; the result is **`LOOP_NEEDS_USER_ACTION` with `loop_next_command` null**; **ZERO `execute-initial-design` dispatches**; **ZERO provider calls of any kind on the exhausted condition**; **ZERO appends made merely to express the stop**; **ZERO new request identities**; and every durable request, terminal, custody, operation record and pending candidate intent is **byte-identical afterwards**. **(C)** the governed oversize-invalid output with an exhausted budget reaches **the same honest stop**, on the same guard, with the same five zeros. **(D)** each of the three restarts derives the **identical** `LOOP_NEEDS_USER_ACTION` / null position from the same authenticated evidence, with **ZERO new request identity, ZERO provider calls and ZERO appends**, and the journal **byte-identical across all three re-entries**; the position is never re-derived by re-selecting `execute-initial-design`, and it is never carried in a flag, marker, counter or second store (`INIT-EXHAUSTION-NOT-STORED`). **(E)** **no case may be satisfied by opening or closing a `diagnosis_strategy_consumption_*` transaction** — the fixture asserts that **no** `diagnosis_strategy_consumption_started` and **no** `diagnosis_strategy_consumption_terminated` exists or is appended in any of A–D, and that no correction specification, diagnosis identity, strategy identity or blocking-finding authority is manufactured. **(F)** **no case may be satisfied by calling `close-open-consumption`** — the fixture asserts the command is never invoked, never owed, and never named as the next command, and that `CONTINUATION_EXECUTION_COMMANDS` still holds exactly **seven** names. Across all six: **no new loop state, no new journal event type, no new state store, no eighth continuation execution command, and no second retry calculator** — the derivation consults the **installed** `bounded_output_retry_budget()` and nothing else (`INIT-EXHAUSTION-NO-SECOND-CALCULATOR`) |
| **R114** | **The T1 prompt states the actionable-root requirement, inside the same digest binding.** *(new in v1_9)* Capture the exact bytes sent for `codex_next_package_selection`; then alter one byte of the rendered prompt and re-render. | the bytes are the **installed** builder's output and state that an actionable answer must name its exact `package_source_path` while the non-actionable answers may leave it null; they still contain **no** instruction to emit `result_schema_id` / `result_schema_version`; there is **no second prompt builder**; and the altered render is refused by `_supervisor_provider_material()` **before dispatch** on the `prompt_material_sha256` mismatch, with zero provider contacts |

---

## §26 — OPEN ITEMS THAT REMAIN GENUINELY OPEN

v1_0 listed ten items; four of them were not genuinely open and were **removed** in v1_1, and that removal stands in v1_2:

- ~~which Decision Defaults file is adopted~~ — **settled by Master V10** (§10.1);
- ~~whether the acceptance-button design's accepted version is v1.14 or later~~ — **settled: Ness explicitly accepted v1.15** (§1.3, §2.4); the receipt lag is bookkeeping, not a decision;
- ~~whether a Decision-Defaults contradiction should hard-close the continuation gate~~ — **it must not** (§10.1);
- ~~exact literal names for every proposed label~~ — the names this bridge needs in order to be implementable are settled by this design itself and are no longer parked.

What genuinely remains:

1. **Whether a scope's binding should carry its newest validation's source facts** rather than its anchor's (§8.8). Changing it would alter installed behaviour for the already-accepted package. **Open — mechanical, outside this bridge.**
2. **Exact numeric bounds for the continuation's own episodes** — how many selection or preparation episodes may be attempted before the loop reports a stop, and the precise backoff shape for a review that cannot complete its own check. The installed episode and attempt caps already bound it; the specific numbers are a tuning choice. **Open — mechanical.**
3. **The plain-language capability text for a newly selected package** shown in the UI's persistent package context, and the honest source it may be derived from. **Open — mechanical, constrained by §21.3.**
4. **Whether a controlled component ID or Register ID exists for the continuation itself.** None is invented here. **Open.**
5. **Bundle placement for this bridge.** Not decided, and not decided here. **Open.**
6. **Whether any mechanism should exist to restore lost custodied provider-result bytes.** §14.6 deliberately invents none: an unverifiable custody is a safety hold a person resolves. Whether N.H should ever gain a separately accepted restoration mechanism, and on what evidence, is a real future question with its own owner. **Open — future, outside this bridge.**
7. **Everything the accepted AIC, UDOK and acceptance-design (v1.15) sources leave open** remains open with its proper owner and is not closed by implication by this file.

Items 1–6 are irrelevant to whether this bridge can be implemented; none of them blocks it.

**What v1_9 settled, and what it deliberately did not open** *(v1_9)*:

- **Settled there, mechanically:** the actionable-root contract (§9.3a) and the one bounded earlier-contract transition rule (§9.7). **Neither is a Ness question.** Ness is not asked how internal path or provenance plumbing works, which is exactly what the detailed design-interview decision reserves to mechanical work.
- **Item 6 remains open and untouched.** §9.7 deliberately does **not** invent, design or authorize a mechanism to restore lost custodied provider-result bytes, and it explicitly makes itself **unavailable** where custody fails re-verification (`SEL-LEGACY-NOT-CUSTODY-LOSS`). That question keeps its own owner.
- **No new open item is created by that correction.** The earlier-contract condition is closed by construction: it requires validity under a contract no longer in force, so it cannot recur (`SEL-LEGACY-NOT-A-NEW-LEGACY`).
- **One item is recorded as an implementation obligation rather than an open design question:** the semantics of §11.5 — the installed routed-signal identity, current-versus-historical routed signals, and the coverage-to-`NEEDS_NESS_DECISION` stop — are **already settled** and are not reopened. A later implementation that departs from them has an implementation defect, not a design gap, and it is corrected against §11.5.

**What v1_11 settled, and what it deliberately did not open** *(new in v1_11)*:

- **Settled here, mechanically:** how the already-settled T4 exhaustion stop is actually carried and consumed — one derived field (§17.2) and one guard (§7.4). **This is not a Ness question.** Ness is not asked how internal bookkeeping should work; v1_10 already settled the meaning, and v1_11 only wires it.
- **Nothing about that stop's meaning was reopened.** §14.3's statement of it is preserved in substance and cross-referenced, not redesigned.
- **Item 1 — the §8.8 anchor-versus-newest source-binding drift — remains open, untouched, and explicitly NOT closed by this correction**, exactly as v1_9 and v1_10 leave it. **This candidate authorizes no production restart.**
- **No new open item is created.** The exhausted T4 position is derived from evidence that already exists, reported through a loop state that already exists, and consumes an installed budget calculation that already exists.
- **The two implementation obligations recorded by v1_10 remain exactly as recorded** — the corrupted T1 `result_invalid` custody safety-hold, and the exact T1 review-signal lookup including `package_key`. **v1_11 neither discharges, expands, nor reopens them.**

**What v1_10 settled, and what it deliberately did not open** *(v1_10)*:

- **Settled here, mechanically:** what happens when the installed bounded T1 output-retry budget is exhausted (§9.6a), the fact that a T1 review is not a correction-strategy consumption (`T1-NOT-A-CONSUMPTION`), and the clarification that saved T1 result bytes are protected by their evidence rather than by their terminal form (§9.6b). **None of these is a Ness question.** Ness is not asked how this internal bookkeeping should work; the correction is mechanical and is settled mechanically.
- **Item 1 — the §8.8 anchor-versus-newest source-binding drift — remains open, untouched, and explicitly NOT closed by this correction.** v1_10 does **not** solve it, reinterpret it, re-anchor it, weaken it, or close it. The live implementation work that exposed the contradiction v1_10 corrects **deliberately isolated that drift and explicitly did not prove the real live drift cleared** (§3.5). **It remains a separate mechanical open item exactly where v1_9 leaves it, with its own owner, outside this bridge — and this candidate authorizes no production restart.**
- **Item 6 remains open and untouched by v1_10 as well.** §9.6b `T1-CUSTODY-NO-RESTORATION-INVENTED` invents, designs and authorizes **no** restoration mechanism for lost custodied bytes; it only states that lost bytes are a `LOOP_SAFETY_HOLD` and never an absence.
- **No new open item is created by this correction.** The exhausted position is derived from evidence that already exists, reported through a loop state that already exists, and owes nothing that does not already exist.
- **Two items are recorded as IMPLEMENTATION obligations, not new policy and not open design questions** *(new in v1_10)*. They belong to the **next disposable implementation correction after v1_10 is independently audited and accepted**, and neither expands this design:
  1. **The implementation must be corrected so that a corrupted T1 `result_invalid` custody safety-holds rather than disappearing.** The rule it must satisfy is §9.6b `T1-CUSTODY-UNVERIFIABLE` / `T1-CUSTODY-NEVER-ABSENT` and §23 `R-11c`, proved by R109 fixture (c). This is an implementation defect against already-settled semantics, not a design gap.
  2. **The exact T1 review-signal lookup must include every already-governing package/scope/identity field needed for exact equality — including the controller-derived `package_key` where the installed event carries or binds it.** The rules it must satisfy are §11.5 `ROUTED-SIGNAL-INSTALLED-IDENTITY` and `ROUTED-SIGNAL-CURRENT-NOT-HISTORICAL`, unchanged. **The routed-signal semantics are already settled and are NOT reopened, redesigned or expanded here** (`PIECE3-RULES-NOT-REOPENED`, §11.5).

---

## §27 — DESIGN-COMPLETE CHECKLIST

| # | Condition | Where |
|---|---|---|
| 1 | `v1_0` through `v1_8` are preserved byte-identically, and `v1_8`'s accepted closure record is untouched | §0.1, §0.1a, §1.5 |
| 2 | acceptance stays terminal for its own package | §6.2, §24.7 |
| 3 | acceptance transaction stays acceptance-only | §7.1 `INV-ACCEPT`, §24.5, R1 |
| 4 | the overall loop may continue after acceptance | §7.2, §7.3, §20 |
| 5 | continuation is a separate operation, never inside Accept | §7.1, §7.5 |
| 6 | continuation begins only after acceptance is durable and freshly proved | §6.3 |
| 7 | continuation is lookup-first, idempotent, crash-safe, append-only | §7.5, §17, §18 |
| 8 | no second store, journal, gate, recovery or long-running loop | §16.3 |
| 9 | no new journal event type; the proof is stated | §7.6 |
| 10 | current-package binding is deterministic and authenticated | §8 |
| 11 | first-validation-forever is explicitly corrected | P-3, §8.2, §24.1 |
| 12 | old accepted history readable; new package inherits nothing | §8.6, §12.2 |
| 13 | an incomplete Q cannot steal the current binding | §8.4, §8.9 `TB-NOT-CURRENT`, R5 |
| 14 | duplicate or contradictory current-package evidence fails closed | §8.5, R-3 |
| 15 | restart reaches the same package | §8.6, §17.2 |
| 16 | no filename or version ordering decides authority | §8.1 |
| 17 | **v2_2 is settled current authority; v2_3's presence asks Ness nothing and stops nothing** | §10.1, R-15, R10 |
| 18 | **v1.15 is recorded as later explicitly accepted; receipt lag is not a decision** | §1.3, §2.4 |
| 19 | selection is dynamic; no hard-coded package | §9.4, R8 |
| 20 | completed work is treated as completed history | `SEL-RESPECT-CLOSURE`, R9 |
| 21 | **the selector contract is internally coherent — one installed prompt, key set and validator** | §9.1, R11 |
| 22 | **restart re-runs the full admission proof, not only schema validity** | §9.5, §13.6, R12 |
| 23 | **task preparation exists between clearance and Claude** | §7.2 T3, §13, R13 |
| 24 | **task preparation reuses the installed stage-two mechanic** | §13.3, R13 |
| 25 | **exact target path and mechanical specification are proved before Claude** | §13.4, §13.5, R14 |
| 26 | a genuine Ness choice routes only through the installed Piece-3 path | §11, R15 |
| 27 | no question is manufactured from model output | §11.1 |
| 28 | **the Claude result is durable and custodied before any candidate write-ahead** | §14.2 `INIT-CUSTODY-BEFORE-PROMOTION`, R16 |
| 29 | **an uncertain Claude outcome never redispatches** | §14.3 `INIT-NO-REDISPATCH`, §19.3, R17 |
| 30 | **restart from a custodied Claude result uses the exact saved bytes** | §14.3 `INIT-EXACT-BYTES`, R18 |
| 31 | the new package gets a distinct authenticated scope | §12.2 |
| 32 | old acceptance / audit / PASS / custody cannot satisfy the new package | §12.2 |
| 33 | initial-candidate creation and promotion have exactly one owner | §15, R22 |
| 34 | the modern supervisor owns all later audit and correction | §16, R21 |
| 35 | crashes cannot duplicate selection, preparation, Claude calls or candidates | §18, §17.3, R19, R20 |
| 36 | the worker change is bounded and does not simply delete the state | §20.2 |
| 37 | UI stays honest and rewrites no history | §21 |
| 38 | later implementation remains forbidden | §22, R23 |
| 39 | the autonomy comment is specified exactly and bounded | §25.1 |
| 40 | fail-closed rules cover every named failure | §23 |
| 41 | the implementation file impact is explicit | §24 |
| 42 | a disposable rehearsal plan proves the invariants | §25 |
| 44 | **unverifiable saved custody can never cause a new provider request** | §14.6 `CUSTODY-UNVERIFIABLE-HOLD`, R-11a, Row K.2, R28 |
| 45 | **custody-unverifiable follows the installed `SAFETY_HOLD` route** | P-19, §14.6, R28 |
| 46 | **`initial_design` has its own strong admission contract, not a false K1–K8 reuse** | §14.5 `INIT-ADMISSION`, P-20, §24.5 |
| 47 | **wrong path / payload / length / hash / size / task binding cannot reach T5** | §14.5 I3–I8, §15.1 preconditions, R29–R35 |
| 48 | **selector and preparation custody have an exact closure rule and never stay pending forever** | §7.6a `CLOSURE-READONLY`, P-21, R25, R26 |
| 49 | **initial-design custody does stay pending until T5 completes** | §7.6a `CLOSURE-INITIAL-PENDING`, R27 |
| 50 | **operation-specific recovery discovers the operation before choosing its package context** | §8.9.1 `TB-RECOVERY-BOOTSTRAP`, P-22, §24.1 |
| 51 | **a Q transition operation is recoverable while P remains current** | §8.9.1, §8.9.2, R37, R38 |
| 52 | **caller input can never choose a package binding** | §8.9.1 step 2, §8.9.2, R-11b, R40 |
| 53 | **duplicate or ambiguous operation-start evidence fails closed** | §8.9.1 steps 5 and 7, §8.9.2 step 6, R-11b, R40 |
| 54 | **still no new journal event type, and the closure rule needs none** | §7.6, §7.6a |
| 55 | **the initial-design result key set is enumerated as exactly six keys** | §14.5a `INIT-RESULT-KEYS`, R41 |
| 56 | **no correction-specific result field is included** | §14.5a exclusion table, R41 |
| 57 | **I8 still binds the exact prepared task through controller-owned request hashes, not restated result fields** | §14.5 I8, `INIT-RESULT-NO-DUPLICATED-BINDINGS` |
| 58 | **recovery binds the scope its authenticated start records, never one inferred from the phase** | §8.9.1 `TB-RECOVERY-BINDS-THE-RECORD`, §18.1 |
| 59 | **T1 recovery binds P and never invents Q** | §8.9.1 `TB-NO-PREMATURE-Q`, §18 Row C, R36 |
| 60 | **T3/T4/T5 recovery binds Q only where the authenticated evidence proves Q** | §8.9.1 table, §18 Rows G/I, R37 |
| 61 | **`process-custodied-provider-result` discovers and re-proves its scope BEFORE ordinary context construction** | §8.9.2 steps 1–8, §24.1, §24.5, R38 |
| 62 | **a stale `loop-status` response is never authority** | §8.9.2 `TB-CUSTODY-NO-STALE-REPORT`, R39 |
| 63 | **ambiguous recovery evidence fails closed with zero appends and zero calls** | §8.9.2 step 6, R-11b, R40 |
| 64 | **the T1 selection result passes a dedicated installed-contract B6d validator** | §9.5a `SEL-B6D-BRANCH`, P-23, R42 |
| 65 | **the T3 preparation result passes a dedicated installed-contract B6d validator** | §13.6a `PREP-B6D-BRANCH`, R44 |
| 66 | **lifecycle schema metadata is never injected into either model-authored key set** | `SEL-LIFECYCLE-METADATA-STAYS-OUTSIDE`, §24.3, R43, R45 |
| 67 | **first-pass and restart admission use the same controller-owned authority binding** | `SEL-AUTHORITY-BINDING-CARRIED`, §24.4, R46, R47 |
| 68 | **the two proof levels are not collapsed into one** | `SEL-TWO-LEVELS`, `PREP-TWO-LEVELS`, R47 |
| 69 | **T2 no longer relies on a blind direct provider call in the automatic path** | §12.3a, §12.3b, P-24, R48 |
| 70 | **each T2 model request is durable before its result can be used** | §12.3a steps 2–4, R48, R49 |
| 71 | **an uncertain T2 dispatch is reconciled and never automatically resent** | §12.3d E2, R49 |
| 72 | **`_b6f_piece3()` remains the one owner of `piece3_provider_work_recorded`** | `T2-AUTHORIZATION-OWNER`, §24.5 |
| 73 | **Q's authorization is scope-matched before Q's Piece-3 append** | `T2-SCOPE-MATCHED`, R-4, R-8a, R50 |
| 74 | **the Piece-3 commit consumes the same custodied result and makes zero provider calls** | §12.3a steps 7–8, `T2-ONE-CALL`, R51 |
| 75 | **source, pagination or standing drift cannot silently reuse a stale result** | `T2-STALE-NOT-RECALL`, R-8b, R52 |
| 76 | **no duplicate authorization or Piece-3 event across crash and restart** | §12.3d E3–E5, R51, R53 |
| 77 | **the installed Piece-3 commands keep their public behaviour; nothing is duplicated** | §12.3b `T2-ONE-OWNER`, §24.1 |
| 78 | **no second Piece-3 system, interview, question store, authorization or gate** | `T2-NO-SECOND-PIECE3-SYSTEM` |
| 79 | **the T1/T3 prompt instructions match their exact model contracts** | §9.5b `PROMPT-BY-KIND`, P-25, R54, R55 |
| 80 | **lifecycle metadata stays outside every model-authored object** | `PROMPT-NO-LIFECYCLE-SENTENCE`, `SEL-LIFECYCLE-METADATA-STAYS-OUTSIDE`, R61, R62 |
| 81 | **the required-input extra is reachable, bound and deterministically reconstructable** | §9.5c `EXTRA-INPUTS-SEAM` / `EXTRA-INPUTS-RECONSTRUCTION`, P-26, R57 |
| 82 | **changed reconstruction makes the result stale, never silently accepted** | `EXTRA-INPUTS-STALE-NOT-SILENT`, R-7b, R58 |
| 83 | **no new journal body field, and the reason is proved** | §9.5c |
| 84 | **T2 sends the real Piece-3 prompts** | §12.3e A, P-27, R59, R60 |
| 85 | **T2 admits the real Piece-3 payload contracts** | §12.3e B, R61, R62 |
| 86 | **T2 position A has one exact worker command** | §12.3c.A `T2-DISPATCH-COMMAND`, R64 |
| 87 | **the stage is derived from controller state, never caller input** | `T2-STAGE-FROM-STATE`, R-7c, R64 |
| 88 | **the ordinary public Piece-3 commands are unchanged and unswitched** | `T2-PUBLIC-COMMANDS-UNCHANGED`, R65 |
| 89 | **T2 pending custodies are discoverable before context construction** | §8.9.2 `TB-CUSTODY-CLOSED-SET`, P-28(b), R66, R67 |
| 90 | **wrong-kind or multiple transition custody fails closed** | §8.9.2 steps 3b and 6, R-7d, R69 |
| 91 | **one Piece-3 stage causes exactly one provider call** | `T2-ONE-MODEL-CALL-ONE-QUESTION`, R63 |
| 92 | **Q's first validation is no longer circular on `validation_recorded`** | §8.10, P-29, R74 |
| 93 | **the pre-validation binding has one bounded purpose and is never current** | `TB-PREVALIDATION-USES` / `-NOT-CURRENT`, R75 |
| 94 | **it retires the moment Q's first validation is durable** | `TB-PREVALIDATION-RETIRES`, R77 |
| 95 | **all three new work-item kinds have exact matrix rows** | §9.5d, §13.6c, §14.5b, P-30, R81–R83 |
| 96 | **all three identities re-derive after restart** | §17.3a `WIM-REBUILD-IDENTITY-EQUALITY`, R81–R83 |
| 97 | **first mechanical Q validation needs no fake routed signal** | §12.3g A, `PIECE3-NO-FAKE-FIELDS`, R85 |
| 98 | **first Q validation needs no fake prior `validation_set_id`** | §12.3g A/B, R85, R86 |
| 99 | **coverage review can truthfully operate with zero routed signals** | §12.3g C, R87 |
| 100 | **the ordinary installed Piece-3 behaviour is intact** | `PIECE3-PRESERVE-INSTALLED`, R88 |
| 101 | **the Piece-3 variant is selected by controller state only** | `PIECE3-VARIANT-FROM-STATE`, R-6b, R89 |
| 102 | **`_b6f_piece3()` remains sole authorization owner and writes truthful values** | `PIECE3-AUTHORIZATION-TRUTHFUL`, R90 |
| 103 | **Q authorizations stay scope-matched** | `PIECE3-AUTH-STILL-SCOPE-MATCHED`, R-4, R91 |
| 104 | **`claude_initial_design` cannot fall through to Codex** | §14.7 `INIT-NEVER-CODEX`, R-6e, R92, R93 |
| 105 | **the initial design still emits exactly six result keys** | §14.5a, §14.7 step 8, R94 |
| 106 | **the final continuation command set is internally consistent** | §7.5, §20.2, §24.1, §24.8 |
| 107 | **`_b6f_piece3()`'s ownership is unchanged and its field-source logic is a stated bounded modification** | §12.3e D, §12.3h, §24.5, R98 |
| 108 | **the three T2 pre-context paths are separate and each is possible** | §8.9.4 `TB-CUSTODY-ONE-COMMAND`, R-6f, R95, R96, R97 |
| 109 | **the custody bootstrap uses the closed set with phase agreement, everywhere it is described** | §8.9.2, §24.1 |
| 110 | **execution-command counts agree in every section** | §7.5 (5 new / 2 installed; 4 provider-contacting / 3 provider-free), §20.2, §24.8, R99 |
| 111 | **provider kinds and provider-contacting commands are counted separately** | §19.1 (5 kinds through 4 commands) |
| 112 | **every rehearsal cross-reference resolves** | §7.6a (R25–R27), §14.7 (R92, R93, R94) |
| 113 | **§24.1's routing map names the three distinct paths, not one shared bootstrap** | §24.1, §8.9.4, R100 |
| 114 | **the dispatch command's step 1 points at Path A and requires no custody** | §12.3c.A, `TB-DISPATCH-NO-CUSTODY-PRECONDITION`, R100 |
| 115 | **each of E1–E5 names exactly one recovery owner** | §12.3d `T2-RECOVERY-OWNER-PER-POSITION`, R101 |
| 116 | **Row M / B9 uses no pending-custody bootstrap and appends nothing it does not owe** | §18 Row M `ROW-M-NO-CUSTODY-BOOTSTRAP`, R-6h, R102 |
| 117 | **Rows J, L and M are not blurred into one recovery path** | §18.1 |
| 118 | **every recovery position gives one mechanically possible answer** | §8.9.4, §12.3d, §18, §18.1, §23 R-6h |
| 119 | **an actionable T1 result requires a proved root on BOTH actionable actions** | §9.3a `T1-ACTIONABLE-ROOT`, §9.5 proof 4, §9.5a, P-14, P-33, R104, R105 |
| 120 | **no actionable rootless result can be validly received, admitted, scoped, signalled, routed or asked** | `SEL-ADMISSION-NO-ACTIONABLE-ROOTLESS`, `SEL-B6D-ACTIONABLE-ROOT-IS-INVALID-OUTPUT`, R-5a, §18 Row D, R104 |
| 121 | **no root is ever derived, name-matched or fabricated for a result that named none** | `T1-ACTIONABLE-ROOT-NO-DERIVATION`, `SEL-LEGACY-NO-ROOT-FABRICATION`, R-5a, R104, R106 |
| 122 | **the four non-actionable classifications are unchanged and gained no invented requirement** | `T1-NONACTIONABLE-UNCHANGED`, §9.4, R113 |
| 123 | **`genuinely_open_for_ness` still cannot ask Ness, authorize Claude, or bypass Piece-3** | `GOPEN-IS-EVIDENCE-ONLY`, `NESS-NO-DIRECT-ASK`, §11.2, R105, R110 |
| 124 | **the preserved earlier-contract result is preserved exactly and routes nothing** | §9.7.1 `SEL-LEGACY-PRESERVE` / `-NO-SIGNAL`, §3.4, §18 Row D.1, R106 |
| 125 | **the old provider request identity is never reused or re-dispatched** | `SEL-LEGACY-NEW-IDENTITY`, R-5b, R106 |
| 126 | **exactly one bounded fresh current-contract selection is possible for the proved condition** | §9.7.3, `SEL-LEGACY-CONDITION`, R106 |
| 127 | **that permission is consumed deterministically, from durable evidence, with no counter, flag, marker or store** | §9.7.4 `SEL-LEGACY-ONE-SHOT`, §17.2, §17.3, R107 |
| 128 | **no hot re-selection loop exists, and a bad new result is never a new "legacy" result** | `SEL-LEGACY-NO-LOOP`, `SEL-LEGACY-NOT-A-NEW-LEGACY`, R-5c, R107 |
| 129 | **uncertainty remains reconciliation-first, and never reaches the earlier-contract rule** | `SEL-LEGACY-NOT-UNCERTAINTY`, §19.3 table, `PROV-NO-REDISPATCH`, R108 |
| 130 | **unverifiable custody remains `SAFETY_HOLD` with zero replacement calls, and gains no loophole** | `SEL-LEGACY-NOT-CUSTODY-LOSS`, `CUSTODY-UNVERIFIABLE-HOLD`, R-5c, R109 |
| 131 | **the fresh selection re-checks the current frontier and may prove a different package** | `SEL-LEGACY-FRESH-FRONTIER`, `SEL-LEGACY-NO-PRIVILEGE`, R-5d, R112 |
| 132 | **nothing about the condition is hard-coded to a package, title, frontier or event position** | `SEL-LEGACY-CONDITION-NOT-A-NAME`, `SEL-NO-HARDCODE`, R8, R112 |
| 133 | **a valid replacement takes exactly the existing mechanical or genuine-Ness route, unchanged** | §9.8, R110, R111 |
| 134 | **the already-settled routed-signal and coverage-stop semantics are preserved, not redesigned** | §11.5 `ROUTED-SIGNAL-INSTALLED-IDENTITY` / `-CURRENT-NOT-HISTORICAL` / `COVERAGE-TO-NESS-STOP` / `NO-DESIGN-WHILE-NESS-PENDING` / `PIECE3-RULES-NOT-REOPENED` |
| 135 | **v1_8 is preserved byte-identically and its accepted standalone standing is stated accurately** | §0.1, §0.1a, §1.5 |
| 136 | **v1_9 claims no acceptance, adoption, authority, integration or implementation** | §0.1a, §0 status line, §28 |
| 137 | **no rehearsal claim contradicts the corrected contract, and no rehearsal hard-codes a moving journal position** | §25 R3 (corrected), R8 (extended), R104–R114 |
| 138 | **T1 invalid output remains BOUNDED** | §9.5a, §9.6a part A, §9.7.4 `SEL-LEGACY-NO-LOOP`, R104 |
| 139 | **T1 invalid-output exhaustion is mechanically REACHABLE — it names a position that can actually be reached and reported** | §9.6a part D, §7.4 guard, §18 Row D, §23 `R-5f`, R104, R107(e) |
| 140 | **its terminal position is RESTART-STABLE — identical answer, zero appends, zero provider calls, on every re-entry** | §9.6a part E `T1-EXHAUSTION-RESTART-STABLE`, §17.3, §23 `R-5f`, R107(e) restart assertion |
| 141 | **no fake diagnosis consumption is created, at any budget position, for any work-item kind** | §9.6a `T1-NOT-A-CONSUMPTION`, §14.3 `INIT-EXHAUSTION-IS-NOT-A-CONSUMPTION`, §23 `R-5e`, R104, R107 |
| 142 | **`close-open-consumption` remains available, unweakened, ONLY where a genuine installed consumption exists** | §7.5, §9.6a `T1-NOT-A-CONSUMPTION`, §16.2, §24.5, §23 `R-5e` |
| 143 | **no eighth continuation execution command is introduced — the set is still exactly seven** | §7.5 `CONTINUATION-SET-CLOSED-AT-SEVEN`, §20.2, §20.3, §24.5, §24.8, R99 |
| 144 | **no new journal event type is introduced by this correction** | §7.6, §9.6a part B, §24.1 |
| 145 | **no new state store is introduced by this correction** | §9.6a part C `T1-EXHAUSTION-DERIVED`, §17.2, §24.1 |
| 146 | **no provider call occurs after the exhausted T1 state merely to "close" it** | §9.6a part B, §19.3 fourth position, §23 `R-5e`, R104, R107(e) |
| 147 | **no second legacy replacement opens at any budget position, exhausted included** | §9.7.4 `SEL-LEGACY-ONE-SHOT` / `SEL-LEGACY-NOT-A-NEW-LEGACY`, §9.6a part A, R107 |
| 148 | **the B9 retry values are untouched, and B9's exhaustion and real-change meanings are preserved, not redesigned** | §9.6a `T1-EXHAUSTION-IS-B9-EXHAUSTION` / `T1-EXHAUSTION-NO-B9-REDESIGN`, §9.6c |
| 149 | **no new loop state, next-command value, retry count, wait, timer, deadline or real-change category is invented** | §9.6c `T1-EXHAUSTION-NO-NEW-STATE`, §7.3 table unchanged |
| 150 | **invalid-result custody loss can never look like result absence** | §9.6b `T1-CUSTODY-UNVERIFIABLE` / `T1-CUSTODY-NEVER-ABSENT`, §7.6a `CLOSURE-INVALID-TERMINAL-IS-TERMINAL`, §19.3, §23 `R-11c`, R109(c) |
| 151 | **the exhausted stop never claims a closed consumption, uncertainty, a reopened old request, a selection, or a successful completion** | §9.6a `T1-EXHAUSTION-NO-FALSE-CLAIM`, §21.3, §23 `R-5e` |
| 152 | **the special earlier-contract one-shot is preserved exactly and still consumed at `provider_request_prepared`** | §9.7 in full, §9.7.4 `SEL-LEGACY-ONE-SHOT`, §17.2, R106, R107 |
| 153 | **all accepted v1_9 mechanics outside this one contradiction are unchanged** | §0.2 "What v1_10 deliberately does NOT change", §27 rows 1–137 |
| 154 | **the separate §8.8 source-binding drift remains open, unsolved and not re-anchored, and no production restart is authorized** | §8.8, §3.5, §26 item 1, §28 |
| 155 | **v1_9 is preserved byte-identically and its accepted standalone standing is stated accurately, receipt lag included** | §0.1, §0.1a, §1.5, §28 |
| 156 | **v1_10 claims no acceptance, adoption, authority, integration or implementation** | §0.1a, §0 status line, §28 |
| 157 | **the T4 / `claude_initial_design` exhaustion stop is mechanically WIRED, not only stated** | §14.3 `INIT-EXHAUSTION-IS-WIRED`, §17.2 `INIT-EXHAUSTION-DERIVED`, §7.4 T4 guard, §24.1, R115 |
| 158 | **`post_acceptance_transition_state()` carries an explicit T4 derived exhaustion field** | §17.2 `initial_design_output_retry_exhausted`, §24.1 |
| 159 | **that field is a pure derivation — no stored flag, marker, counter, event, second state source or new journal field** | §17.2 `INIT-EXHAUSTION-NOT-STORED`, §24.1, R115(D) |
| 160 | **it consumes the SAME installed `bounded_output_retry_budget()` — no second retry calculator** | §17.2 `INIT-EXHAUSTION-NO-SECOND-CALCULATOR`, §24.1, R115 |
| 161 | **the §7.4 guard sits after `prepared_task` and BEFORE the `initial_result_custody is None` → `execute-initial-design` fall-through** | §7.4 pseudocode and guards note, §24.1, R115(B) |
| 162 | **exhausted T4 derives `LOOP_NEEDS_USER_ACTION` with a null next command** | §7.4, §14.3, §18 Row I, R115(B), R115(C) |
| 163 | **exhausted T4 produces zero further provider calls, zero appends and zero new request identities** | §14.3, §18 Row I, §20.3 step 5, R115(B)–(D) |
| 164 | **the exhausted T4 position is restart-stable over identical authenticated evidence** | §17.2 `INIT-EXHAUSTION-NOT-STORED`, §18 Row I, §17.3, R115(D) |
| 165 | **available-budget T4 retry is unchanged — the stop ends a series that is over, it shortens none** | §14.3 table, §17.2 precedence note, §18 Row I, R115(A) |
| 166 | **no `close-open-consumption` route is claimed for T4, and no diagnosis consumption is invented for it** | §14.3 `INIT-EXHAUSTION-IS-NOT-A-CONSUMPTION`, §23 `R-5e`, R115(E), R115(F) |
| 167 | **§18 covers the exhausted T4 restart position explicitly, so no implementer can conclude it returns to `execute-initial-design`** | §18 Row I continued, §18.1 |
| 168 | **§24 no longer claims wiring the document fails to specify** | §24.1 (field + guard rows), §24.5, §5 P-35 |
| 169 | **still no new loop state, no new journal event type, no new state store, and no eighth continuation execution command** | §7.3 table unchanged, §7.6, §7.5 `CONTINUATION-SET-CLOSED-AT-SEVEN`, §17.2, R115 |
| 170 | **B9 retry values, retry counts, timers, waits, backoff, deadlines, real-change rules, episode meaning and exhaustion meaning are all untouched** | §17.2 `INIT-EXHAUSTION-NO-SECOND-CALCULATOR`, §9.6a `T1-EXHAUSTION-NO-B9-REDESIGN`, §9.6c |
| 171 | **v1_10 is preserved byte-identically, and is accurately described as a NOT-ACCEPTED candidate** | §0.1, §0.1a, §1.5, §28 |
| 172 | **v1_9 remains the accepted standalone design of record, and no acceptance or audit PASS is claimed for v1_10 or v1_11** | §0.1a, §1.5, §0 status line, §28 |
| 43 | only genuinely open items stay open | §26 |

---

## §28 — MUST-NEVERS AND PRESERVATION STATEMENT

**It never weakens acceptance.** It does not remove, edit, reinterpret, re-date, re-scope or make conditional the acceptance at `event_seq 84`, or any other acceptance. It does not make acceptance non-terminal for its own package. It adds nothing to the acceptance request. It creates no second acceptance path, truth, or record.

**It never invents authority.** It creates no authority, adopts nothing, integrates nothing, decides no open policy. It does not adopt or de-adopt any Decision Defaults file — Master V10 already settled which governs, and this design reports that rather than deciding it. It assigns no controlled component ID or Register ID. It marks nothing `PACKAGE_COMPLETE` and creates or modifies no closure record.

**It never builds a parallel system.** No second dependency engine, no second task-preparation engine, no second Claude writer, no second promotion path, no second audit, no second interview, no second Ness-question route, no second state store, no second gate, no second recovery authority, and no second long-running design loop beside the modern supervisor.

**It never guesses.** Where evidence is ambiguous, contradictory, stale, unreadable, or unprovable, it fails closed, preserves the conflicting evidence, and reports the exact problem. It never prefers a winner, never repairs a record, never fabricates a terminal, and never treats "probably nothing happened" as proof — least of all about a provider call that may already have been made. **And it never manufactures replacement evidence for evidence it has lost:** a saved result whose bytes no longer re-verify stops the loop, it does not restart the model.

**It never fabricates a package root.** Where an actionable selection names no `package_source_path`, the answer is refusal. It does not select a root from `source_paths_checked`, from the governing-authority subset of that list, from `package_id`, from `package_title`, from a filename, from listing order, from a timestamp, or from a caller; it does not derive `source_evidence` from some other field and present it as the selected root; it does not carry a placeholder, a fallback label, or a shared scope identity another package could answer to; and it does not let such a result establish a scope, become a routed signal, prepare a task, authorize a design run, or reach Ness. **A root the controller cannot prove is a root the controller does not have.**

**It never rewrites the history it corrects.** The already-completed earlier-contract result is preserved exactly — its events, its custodied bytes and its null `package_source_path` — because it is truthfully what happened. It is not deleted, rewritten, re-headed, back-dated, re-classified, or annotated into a different answer; its request identity is never reused or re-dispatched; and it never becomes a review signal or a question. **Correcting a contract never means editing the evidence produced under the old one.**

**It never turns one bounded recovery into an unbounded loop.** The earlier-contract permission is a **single**, deterministically-consumed entry, fenced by durable evidence rather than by memory, and it is unavailable to uncertainty, to unverifiable custody, and to any result produced under the current contract. Where a model will not satisfy the contract, the answer is the installed bounded output-retry budget and then an honest stop — **never a fresh selector identity opened again and again.**

**It never invents a transaction so that a command becomes callable.** Where the bounded output-retry budget is exhausted, N.H stops and says so. It does **not** open a `diagnosis_strategy_consumption_started` that no diagnosis produced, does **not** append a `diagnosis_strategy_consumption_terminated` with nothing truthful in it, does **not** manufacture a correction specification, a diagnosis identity, a strategy identity or a blocking-finding authority, does **not** call — or claim to have called — `close-open-consumption` where no consumption is open, and does **not** register an eighth continuation execution command to carry a closure that is not owed. **A command that would truthfully refuse is not a route, and the answer to a missing stop is the stop — never a fabricated transaction to give a command something to close.** The legitimate installed use of `close-open-consumption`, for a genuine open diagnosis consumption of the correction machinery, is **preserved unweakened** and is not removed, genericised, re-scoped or borrowed.

**It never lets a stop become a loop that reports the wrong position.** The exhausted position is **derived from durable evidence on every entry and every restart** — never remembered in a flag, a marker, a counter beyond the already-governing installed budget, or a second store — and it is reported as `LOOP_NEEDS_USER_ACTION` with a **null** next command. It does not re-invoke `continue-design-loop` to rediscover what it already derived, does not dispatch again on the exhausted condition, and does not owe an append in order to be true. **Three re-entries over identical evidence give the identical answer, with zero appends and zero provider calls.**

**It never treats saved evidence as absent because the answer inside it was unusable.** A durable `next_package_selection` custody whose exact bytes the record requires is protected **whatever its terminal form** — `result_received`, `result_invalid`, or any other terminal that truthfully carries or requires saved custody. Bytes that no longer re-verify are `provider_result_custody_unverifiable` → `LOOP_SAFETY_HOLD` → null next command → **zero provider calls**, never "no result", never a reason to ask a model again for an answer it already gave, and never a loophole for the §9.7 permission. **An invalid terminal says the model's answer did not satisfy the contract. It never says the bytes were never received.** And no restoration mechanism is invented here.

**It never leaves a stated stop unwired.** A rule this design states in prose and never carries into the derivation is not a rule — it is a disagreement between two halves of one document, and the executable half wins. The T4 exhaustion stop is carried by **one derived field** and consumed at **one place** in the precedence, so an implementer following §14.3, §17.2, §7.4, §18 and §24 reaches the **same** answer. **It is never expressed by a stored flag, a marker, a counter beyond the installed budget, a new event, a new store, a second retry calculator, or a relaxed admission proof** — and it never fixes a routing gap by making an unusable result look admitted.

**It never ends a retry that is still owed.** The exhausted stop fires only where the **installed** `bounded_output_retry_budget()` already says `exhausted`. While that budget is `available`, ordinary installed T4 retry and recovery continue exactly as before. **The stop ends a series that is already over; it shortens none, and it changes no accepted B9 retry value, count, timer, wait, backoff, deadline, real-change rule, episode meaning or exhaustion meaning.**

**It never redesigns B9, and it never widens its own scope.** It changes no accepted B9 retry value, no B9 exhaustion meaning, and no B9 real-change meaning; it invents no retry count, wait, timer, deadline or real-change category; it introduces no new loop state, no new event type, no new state store and no eighth command. **And it does not touch the separate §8.8 anchor-versus-newest source-binding drift** — that remains a distinct mechanical open item, exactly where v1_9 leaves it, unsolved, un-re-anchored, unweakened and unclosed (§3.5, §26 item 1). **This candidate authorizes no production restart, installs nothing, and starts nothing.**

**It never turns a mechanical correction into a Ness question.** Ness is not asked which contract should require a root, how provenance plumbing should work, or what to do with an earlier-contract result. Those are mechanical, and they are settled mechanically here. `genuinely_open_for_ness` remains evidence that the independent question-validation stage must run — **never permission to ask Ness, never permission to authorize Claude, and never a question composed from model prose.**

**It never implements.** It writes no code, runs no code, mutates no Git, touches no production store, creates no marker, performs no migration, and authorizes no building. Reaching the end of design continuation is a report, not a permission.

**It never modifies an existing file.** The work that produced this candidate created exactly one new file — this one — and left every other file byte-identical, including **`v1_0` through `v1_10` of this bridge — the accepted `v1_9` source above all, and the `v1_10` correction base this file derives from — and the separate accepted `PACKAGE_COMPLETE` closure record that names `v1_8`**, the real journal, the real head, the real authenticated event 90 and the preserved earlier-contract request, custody and terminal, the live controller and worker sources (which still hold their installed bytes and still report the old `LOOP_SAFETY_HOLD`), the preserved live implementation-correction evidence, the real AIC candidate chain, every accepted package, every closure record, every authority file, the Master, the Map, both Defaults files, `cursorrules`, the Companion, the workflow files, the five-additions decision package, and every version of the acceptance-button design. **It started no production process, restarted no production, installed nothing, made no provider call of any kind, appended no journal event, wrote no state, and performed no Git operation.**

**It claims no acceptance.** This file is a candidate: not accepted, not adopted, not authoritative, not integrated, not implemented, not `PACKAGE_COMPLETE`. It awaits an independent audit of the actual file and Ness's explicit acceptance, neither of which is claimed, implied, or anticipated anywhere above.

---

*`NH_LIVE_DESIGN_LOOP_POST_ACCEPTANCE_CONTINUATION_MECHANICAL_DESIGN_v1_11_CANDIDATE.md` — a bounded **T4 exhaustion wiring** correction of `v1_10` (SHA-256 `fafc27314aa09b3b4c3a7f2128b7faf495f0a6d3bedab5976e7d0465216ede64`, 443,388 bytes, 3,608 lines), which is preserved unchanged, whose internal status text is not rewritten, and which is itself a **NOT-ACCEPTED candidate** — **no Ness acceptance and no ChatGPT audit PASS is claimed for v1_10 or for this file.** **The currently ACCEPTED standalone design for this package remains `v1_9`** (SHA-256 `711b89d30d36130eb2e9506e817429a5813e700b7c62fbbff97b340dc82a12ed`), likewise preserved unchanged. **Corrected here:** v1_10's §14.3 states the T4 / `claude_initial_design` bounded invalid-output exhaustion stop correctly — no further dispatch on the exhausted condition, no `close-open-consumption` owed, no diagnosis consumption invented, `LOOP_NEEDS_USER_ACTION` with a null next command, zero further provider calls, restart-stable, all durable evidence preserved — but **never wires it**: `post_acceptance_transition_state()` carries no T4 exhaustion fact and §7.4 has no T4 guard, so an exhausted run of `result_invalid` terminals yields no admissible custody, `initial_result_custody` is `None`, and the derivation returns `LOOP_INITIAL_DESIGN_REQUIRED` / `execute-initial-design` for ever against a spent budget (§5 P-35). v1_11 adds exactly **one derived field** — `initial_design_output_retry_exhausted` `[proposed]`, a pure derivation over the existing durable `claude_initial_design` evidence and the **same installed `bounded_output_retry_budget()`**, with no stored flag, marker, counter, event, second state source or second retry calculator (§17.2) — and exactly **one guard** consuming it in the §7.4 precedence, after `prepared_task` and **before** the `execute-initial-design` fall-through, returning `LOOP_NEEDS_USER_ACTION` with a null next command and **zero appends, zero provider calls and zero new request identities** (§7.4, §14.3 `INIT-EXHAUSTION-IS-WIRED`, §18 Row I, §24.1, §24.5), plus the focused disposable rehearsal `R115` that proves available-budget retry is unchanged, exhausted and governed-oversize budgets reach the honest stop, restart stability holds, and **no case may be satisfied by opening or closing a `diagnosis_strategy_consumption_*` transaction or by calling `close-open-consumption`.** **The T4 exhaustion meaning settled in v1_10 §14.3 is preserved and not redesigned; available-budget T4 retry is unchanged; `close_open_consumption()` is untouched in meaning, un-genericised, and used for neither T1 nor T4; and no new loop state, journal event type, state store or eighth continuation execution command is introduced. No accepted B9 retry value, count, timer, wait, backoff, deadline, real-change rule, episode meaning or exhaustion meaning is changed. Every accepted v1_9 mechanic and every v1_10 correction outside this wiring gap is unchanged, and the separate §8.8 source-binding drift remains a distinct mechanical open item, unsolved and unclosed, with no production restart authorized.** Status: `CANDIDATE — NOT ACCEPTED — NOT ADOPTED — NOT AUTHORITATIVE — NOT INTEGRATED — NOT IMPLEMENTED`. **It does not replace the accepted v1_9 unless and until Ness explicitly accepts v1_11.** Creates exactly one new file — itself — and modifies nothing. Makes no architecture change, performs no implementation, installs nothing, appends no journal event, writes no state, runs no provider, restarts no production, mutates no Git, creates or amends no closure or acceptance record, and authorizes no building.*

*Preserved for lineage — `v1_10`'s own closing statement: a bounded **T1 invalid-output exhaustion** correction of `v1_9` (SHA-256 `711b89d30d36130eb2e9506e817429a5813e700b7c62fbbff97b340dc82a12ed`, 380,415 bytes, 3,249 lines), which is preserved unchanged, whose internal status text remains historical bytes and is not rewritten, and which remains **the currently accepted standalone design** for this package — Ness explicitly accepted those exact bytes after ChatGPT independently audited the actual file and returned PASS. Also preserved unchanged: `v1_8` (SHA-256 `448daa63b4899d4639dc5b7612985cb34e97732dcf4cbeac2c224c54f8ae51e2`) and the separate `PACKAGE_COMPLETE` closure record that still names it (SHA-256 `940cf3a29b0d41836322e6a55dbe9c56d491e840848d6ec80c2d24b4a9663dd4`) — **that receipt has not been updated to record the later v1_9 acceptance, which is bookkeeping lag and not an open Ness decision, and no receipt is created or amended here** — together with `v1_7` (SHA-256 `747a045675c4db771e9ac9490343da82fb986bc9bf255aa42cb85b4a432c62c3`), `v1_6` (SHA-256 `f211ffd90a0ffc6732589d7442c925f2bcac7e7e0740bfb4abaea8d0d9852948`), `v1_5` (SHA-256 `80284a20da80a87d08617051d7a0207c3ef06bd4f902cfa28619bb1cf7c55f36`), `v1_4` (SHA-256 `7fd023c61fdcaf204c2394c28a15ae0f17c30c0e9ce3cb3c269c8b75490b9067`), `v1_3` (SHA-256 `78d57db9e4cc434161b05cb2c0945b9c5b8d22a3fb91ebb4e134543e3987701d`), `v1_2` (SHA-256 `40f217aa018a9fecb4581e0a70004550b22e75234d94543813e7da0f0537f545`), `v1_1` (SHA-256 `7ba76ef61d736cef07f83f4a814200bbc3776ff031cc4eb40230e7fa4e6843e3`) and `v1_0` (SHA-256 `6cfe8d07cce712d5fa8077fdb4930a53ac10c52d9cdc02551c15a316e4695ab0`). **Corrected here:** a real live implementation attempt against the accepted v1_9 design exposed one further IMPORTANT internal mechanical contradiction — v1_9 correctly bounds a contract-violating T1 reply on the installed output-retry budget, then routes the **exhaustion** of that budget to `close-open-consumption`, a command that closes an open **diagnosis** consumption a `next_package_selection` review never opens, and which would therefore truthfully refuse. v1_10 replaces that impossible route with the honest stop it always should have named (`T1-INVALID-OUTPUT-EXHAUSTION-STOP`, §9.6a): retries stay bounded; once the installed budget is exhausted the loop reports `LOOP_NEEDS_USER_ACTION` with a **null** next command, **zero** further provider requests on the exhausted condition and **zero** owed appends; the position is **re-derived from existing durable evidence** and is **restart-stable**; and **no diagnosis consumption is invented, no new event type, no new state store and no eighth continuation execution command is introduced.** The same single contradiction is corrected where it also reached T4 (`INIT-EXHAUSTION-IS-NOT-A-CONSUMPTION`, §14.3). **`close-open-consumption` keeps its legitimate installed use for a genuine open diagnosis consumption and is preserved unweakened** (`T1-NOT-A-CONSUMPTION`). v1_10 additionally clarifies — **as a clarification of already-settled semantics, not as new policy** — that a durable T1 result custody is protected by its evidence rather than by its terminal form, so saved bytes that fail exact re-verification are `LOOP_SAFETY_HOLD` with zero provider calls and are **never** read as absence merely because the terminal was `result_invalid` (`T1-CUSTODY-UNVERIFIABLE`, §9.6b). **No new loop state is invented; the outward stop is v1_9's already-settled `LOOP_NEEDS_USER_ACTION`. B9's retry values, exhaustion meaning and real-change meaning are untouched and B9 is not redesigned. The special §9.7 earlier-contract one-shot is preserved exactly and stays consumed at `provider_request_prepared`. The seven continuation execution commands remain exactly seven — four provider-contacting, three provider-free — across five continuation provider kinds. `genuinely_open_for_ness`, the routed-signal semantics, the coverage stop, `T1-ACTIONABLE-ROOT` and every other accepted v1_9 mechanic outside this one contradiction are unchanged. The separate §8.8 anchor-versus-newest source-binding drift remains a distinct mechanical open item, unsolved and unclosed, and no production restart is authorized.** Status: `CANDIDATE — NOT ACCEPTED — NOT ADOPTED — NOT AUTHORITATIVE — NOT INTEGRATED — NOT IMPLEMENTED`. **It does not replace the accepted v1_9 unless and until Ness explicitly accepts v1_10.** Creates exactly one new file — itself — and modifies nothing. Makes no architecture change, performs no implementation, installs nothing, appends no journal event, writes no state, runs no provider, restarts no production, mutates no Git, creates or amends no closure or acceptance record, and authorizes no building.*

# NH_NESS_DESIGN_ACCEPTANCE_RECORD_AND_UNDERSTANDABLE_ACCEPTANCE_SURFACE_MECHANICAL_DESIGN_v1_14_CANDIDATE.md

## §0 — STATUS BLOCK, PROVENANCE, AND SELF-DESCRIPTION

**Status:**
`DESIGN CANDIDATE — NOT ACCEPTED — NOT ADOPTED — NOT AUTHORITATIVE — NOT INTEGRATED — NOT IMPLEMENTED — NOT PACKAGE_COMPLETE.`

**Date:** August 21, 2026.

**Intended repository placement:** `NH-GOVERNANCE/05_ACTIVE_CANDIDATE/` (this file's actual location; no other placement is claimed and no move is performed).

**What this file is.** The current versioned standalone mechanical design candidate for the package that has been referred to across the accepted Authority Integrity Control Plane (AIC) receipt and the accepted Unified Durable Operation Kernel (UDOK) receipt as **"the parked acceptance-button / acceptance-record package"**, and that Ness's own live-loop decision record names as the missing piece behind `ACCEPTED_FOR_DESIGN_ONLY`:

> "This state may exist only after Ness explicitly performs the separately authorized acceptance action. Its exact recording and downstream effect require a separate accepted acceptance-record design. Until that design exists, the UI may show `READY_FOR_ACCEPTANCE` but must not manufacture or persist acceptance."
> — `NESS_DESIGN_INPUTS/NH_LIVE_LOOP_AUTOMATIC_SUPERVISOR_DECISION_v1_0.md` §4

This file **is that separate design, as a candidate only**. It is not that design accepted.

**What this file does.** It designs, in logical mechanical terms:

1. one **understandable acceptance surface** that must be proved and presented before an Accept action is even actionable;
2. one **explanation record** contract — carried by an **existing registered event type at a new body version**, never by a second new event type — with a two-stage append-only lifecycle, actual-predecessor binding, and staleness rules;
3. one **new authenticated journal event type** — `ness_candidate_acceptance_recorded` — appended exactly once by a successful explicit Ness browser action, and **the only new authenticated event type this design introduces** (§7.2, §9.1);
4. the **deterministic bindings, transaction, lock-time revalidation, idempotency, concurrency, and crash recovery** that make that single append safe;
5. the **replayed post-acceptance state** `ACCEPTED_FOR_DESIGN_ONLY`, and everything that state deliberately does **not** cause;
6. a **logical** local HTTP endpoint contract, a controller/server/browser trust boundary, a fail-closed matrix, an offline disposable test/fault matrix, and the open dependencies.

**What this file does not do.** It writes no code. It edits no code. It creates no store, no marker, no journal, no candidate, no receipt, and no acceptance. It performs no Git operation. It integrates nothing into `NH_MASTER-20_CORRECTED_v10.md` or the Design and Wiring Map. It assigns no controlled component ID and no Register ID. It does not mark anything `PACKAGE_COMPLETE`, does not close any dependency, does not authorize implementation or building, does not start a next package, and does not accept or adopt itself or anything else. **It creates exactly one new file — itself — and modifies nothing.**

**Roles, unchanged and obeyed here.** Ness owns concept and meaning, policy and priorities, acceptance and adoption, and permission to begin building. ChatGPT independently audits the actual file. Claude drafts new versioned design candidates. Cursor codes only after the design is complete and Ness separately authorizes building. **This file is a Claude-drafted candidate awaiting an independent audit and Ness's explicit acceptance; neither is claimed, implied, or anticipated anywhere below.**

**Naming discipline.** Exactly the following names are **LOCKED** by the instruction that produced this candidate and are used verbatim:

| Locked name | Kind |
|---|---|
| `ness_candidate_acceptance_recorded` | authenticated journal event type |
| `ACCEPTED_FOR_DESIGN_ONLY` | workflow state value |
| `acceptance_required = false` | post-acceptance projection value |
| `next_command = null` | post-acceptance projection value |
| `READY_FOR_ACCEPTANCE` | existing workflow state value (unchanged) |
| the eight explanation section titles of §6.2 | fixed section identifiers |

**Every other label in this file is a descriptive working label, marked `[proposed]` at first use.** Storage details, library choices, field spellings, thresholds, HTTP paths, prefixes, and display strings other than those above **remain open**.

**Version note (v1_1).** This is the second version of this package's candidate. Its **actual predecessor** is stated exactly, not inferred from the filename:

| Predecessor | Value |
|---|---|
| Path | `NH-GOVERNANCE/05_ACTIVE_CANDIDATE/NH_NESS_DESIGN_ACCEPTANCE_RECORD_AND_UNDERSTANDABLE_ACCEPTANCE_SURFACE_MECHANICAL_DESIGN_v1_0_CANDIDATE.md` |
| SHA-256 | `1c9e83d908d54a2ccfe2450d666855b49421e8d9d8e12e8c88b915fed759d7e1` |
| Bytes | 114,447 |
| Lines | 1,335 |
| Standing | **UNCHANGED.** v1_0 was not edited, overwritten, moved, renamed, or deleted in producing this file. v1_1 was created as a byte-for-byte copy of that exact source and then corrected. |

**What v1_1 is.** v1_1 is the **bounded mechanical correction** of the four defect packets of **fresh audit #1** — `NH-ACCEPT-001` (IMPORTANT), `NH-ACCEPT-002` (CRITICAL), `NH-ACCEPT-003` (CRITICAL), `NH-ACCEPT-004` (IMPORTANT) — and of nothing else. Each packet was applied within its own stated correction scope, and each packet's stated `MUST_NOT_CHANGE` list was obeyed.

| Packet | Corrected here | Correction, in one line |
|---|---|---|
| `NH-ACCEPT-001` | §6.5–§6.7, §7.1, §7.4, §7.7, §7.8, §11.3, §14 Phase A, §21 T-49, §22.3, §24 | The explanation is fixed as content **before** the final audit, that same audit judges it, the PASS binds that audit, and the **PASS-recording operation itself** appends the final explanation — so no step needs a command after `next_command = null`, and no later audit or PASS stales what Ness is shown. **This row is v1_1's own statement, recorded here as history. Its append order — pass event first, explanation second — is SUPERSEDED by the v1_2 note below, which reverses it. Its owner claim — that the PASS-recording operation itself appends the final explanation — is SUPERSEDED by the v1_3 note below, which gives that append its own operation, and any reading of this row that still places the final explanation inside the PASS operation is stale (§7.1b, §14 Phase A A5–A6, restated in v1_6). The remainder of the row stands.** |
| `NH-ACCEPT-002` | §0, §4.5, §7.1–§7.3, §9.1–§9.2, §14 Phases D–E, §15, §18, §19, §21, §22.3, §24 | The explanation is carried by an **existing registered event type at a new body version**, so `ness_candidate_acceptance_recorded` is the only new type; and every refused or failed click — including request-level refusals — receives **exactly one** permanent operational record through a named pre-existing same-journal carrier. |
| `NH-ACCEPT-003` | §4.1, §9.6, §11.1–§11.3, §12.3, §14 Phase E, §15 F-36, §21, §24 | One effect/commit rule stated against the **actual two-mark reader**, a complete-event-before-committed-mark window with one unambiguous standing, and an owned, named invocation of the existing write-enabled tail recovery. |
| `NH-ACCEPT-004` | §2.5, §22.3, §23, §24 | The genuinely absent v1.13 specification document is separated from the **installed and reachable** supervisor command protocol; the invented reachability blocker is removed. |

**What v1_1 deliberately carries forward unchanged.** Every correct v1_0 mechanic, the locked meaning of the browser action, the locked names, the authority order, the safety and fail-closed discipline, the open items, and the **design-only** status. v1_1 adds no architecture, no policy, no optional hardening, no unrelated cleanup, no implementation, no code, no test, no Git operation, no acceptance or adoption, no Master or Map integration, no Register assignment, no closure, and no `PACKAGE_COMPLETE`.

**Version note (v1_2) — Stage A re-correction of `NH-ACCEPT-001` only.** This is the third version of this package's candidate. Its **actual predecessor** is stated exactly, not inferred from the filename:

| Predecessor | Value |
|---|---|
| Path | `NH-GOVERNANCE/05_ACTIVE_CANDIDATE/NH_NESS_DESIGN_ACCEPTANCE_RECORD_AND_UNDERSTANDABLE_ACCEPTANCE_SURFACE_MECHANICAL_DESIGN_v1_1_CANDIDATE.md` |
| SHA-256 | `0c5555d80fa1fde88b3da1198234ede409efc6cde306ebd94b87753842f78ec9` |
| Bytes | 178,828 |
| Lines | 1,557 |
| Standing | **UNCHANGED.** v1_1 was not edited, overwritten, moved, renamed, or deleted in producing this file, and neither was v1_0. v1_2 was created as a byte-for-byte copy of v1_1 and then corrected. |

**What v1_2 is.** v1_2 is the **bounded Stage A re-correction of the single still-failing packet `NH-ACCEPT-001` (IMPORTANT)**, and of nothing else. **The v1_1 correction was ordered but not durable.** v1_1's §14 Phase A appended `mechanical_pass_recorded` at step A4 and the final-stage explanation record at step A5 — **two separate durable appends, in that order**. Because `status.py:1199-1204` projects `READY_FOR_ACCEPTANCE` with `next_command = None` from the pass event **alone** (`replay.pass_event()` is simply the newest `mechanical_pass_recorded`, `replay.py:1099-1101`), and because the worker runs nothing in that state (`worker.py:73-82`), **a process death between A4 and A5 left `READY_FOR_ACCEPTANCE` / `next_command = null` with no final explanation and no reachable owner to append one.** That is the same unreachable-offer defect the packet names, reached by a crash instead of by design.

**The v1_2 correction is one reordering, and it is mechanical.** The final-stage explanation record is appended **before** `mechanical_pass_recorded`, inside the same operation, binding the deterministic `pass_identity` that `_record_mechanical_pass()` already derives **before it appends anything** (`commands.py:1425-1441`). **The single append that flips the projection into the non-running state is therefore the last substantive append of the operation.** **This paragraph is v1_2's own statement, recorded here as history. Its reordering stands and is carried forward; its clause "inside the same operation" is SUPERSEDED by the v1_3 note below, which gives the final-stage append its own operation, because no reachable recovery can re-enter the original one.** No crash position can produce `READY_FOR_ACCEPTANCE` without a durable final explanation, because the event that produces `READY_FOR_ACCEPTANCE` is written last, and every position before it leaves the workflow in a **running** state whose owner already exists (`WORKING` / `execute-next-claude-task`, `status.py:1205-1209`).

| Packet | Corrected here in v1_2 | Correction, in one line |
|---|---|---|
| `NH-ACCEPT-001` | §6.5a–§6.7, §7.1, §7.4, §7.7, §7.8, §11.3 gates 10–15, §14 Phase A, §21 T-13a / T-49, §22.3 items 7 and 11, §24 items 23 and 27 | The final explanation record is appended **before** the PASS event inside the PASS-recording operation and binds the PASS's deterministic identity rather than a forward event reference, so the state-flipping append is last and the actionable offer is durable **before** control can enter an unowned non-running state. **This row is v1_2's own statement, recorded here as history. Its append order stands; its owner — "inside the PASS-recording operation" — and the same-operation gate it required are SUPERSEDED by the v1_3 note below.** |

**What v1_2 deliberately carries forward unchanged.** Everything else. The eight mandatory sections; design-only acceptance meaning; candidate-not-explanation truth; the explanation's subordination to evidence; the rule that mechanical validators never prove prose truth; no model on click; no provider selected; the exact candidate / audit / PASS / predecessor / source / scope binding; stale means disabled or refused; the post-acceptance state; the automatic-next-package separation; and no implementation. **v1_2 adds no architecture, no policy, no optional hardening, no unrelated cleanup, no new event type, no code, no test, no Git operation, no acceptance or adoption, no Master or Map integration, no Register assignment, no closure, and no `PACKAGE_COMPLETE`.** The corrections v1_1 made for `NH-ACCEPT-002`, `NH-ACCEPT-003`, and `NH-ACCEPT-004` are untouched.

**Provenance of this pass.** The identities in §2.3 and §2.4 were recomputed from the actual repository bytes in the session that produced v1_0 and are carried forward unchanged here, because neither v1_1 nor v1_2 corrects a claim that depends on them being re-derived. The actual code seams that the four packets cite — `controller/nh_loop.py`, `controller/nh_supervisor/schema.py`, `controller/nh_supervisor/constants.py`, `controller/nh_supervisor/commands.py`, `controller/nh_supervisor/journal.py`, `controller/nh_supervisor/engine.py`, `controller/nh_supervisor/replay.py`, `controller/nh_supervisor/feed.py`, and `interview_ui/server.py` — were **re-read from the actual bytes in this session** before each correction was written. No summary, no memory, no cached status note, and no model claim was used in place of the actual files.

**For the v1_2 pass specifically**, the four seams the reordering turns on were re-read from the actual bytes before it was written: `controller/nh_supervisor/commands.py:1396-1469` (the pass path, and the fact that `pass_identity` is derived at `:1425-1441` before `operation.start()` at `:1448`), `controller/nh_supervisor/engine.py:395-490` (`Operation.start` / `.append` / `.complete`), `controller/nh_supervisor/status.py:1199-1215` (precedence 12 and the ordinary-loop fallthrough), and `controller/nh_supervisor/replay.py:1099-1101` (`pass_event()`). **No new controller behaviour is assumed, and no file was changed.**

**Version note (v1_3) — Stage A re-correction of `NH-ACCEPT-001` only.** This is the fourth version of this package's candidate. Its **actual predecessor** is stated exactly, not inferred from the filename:

| Predecessor | Value |
|---|---|
| Path | `NH-GOVERNANCE/05_ACTIVE_CANDIDATE/NH_NESS_DESIGN_ACCEPTANCE_RECORD_AND_UNDERSTANDABLE_ACCEPTANCE_SURFACE_MECHANICAL_DESIGN_v1_2_CANDIDATE.md` |
| SHA-256 | `0e2771398ce8ab7847d37557534829ecef8702d1954bf6d1dff099454880f91c` |
| Bytes | 211,540 |
| Lines | 1,671 |
| Standing | **UNCHANGED.** v1_2 was not edited, overwritten, moved, renamed, or deleted in producing this file, and neither were v1_1 and v1_0. v1_3 was created as a byte-for-byte copy of v1_2 and then corrected. |

**What v1_3 is.** v1_3 is the **bounded Stage A re-correction of the single still-failing packet `NH-ACCEPT-001` (IMPORTANT)**, and of nothing else. **v1_2's reordering was right about placement and wrong about owner identity, and its own acceptance gate is what proves it wrong.**

**The exact v1_2 failure, stated against the installed bytes rather than against its own prose.** v1_2's §14 Phase A row P-3 said that after a crash between the final-explanation append and the pass append, the worker *"re-enters the pass path, re-derives the **identical** `p` … and proceeds to A6."* The re-entry is real, and the re-derived `p` is genuinely identical — but **the operation it runs under is not the original one, and cannot be**:

- `_record_mechanical_pass()` constructs a **new** `engine.Operation` and calls `operation.start()` on **every** entry (`commands.py:1444-1448`). There is no resume path, no reattachment to a prior start, and no branch that reuses an earlier operation.
- The operation's identity is derived, not carried: `engine.complete_envelope()` fills `input_envelope_sha256` and then `supervisor_operation_id` from the envelope's own fields (`engine.py:208-213`, `:187-205`, `:178-184`).
- One of those fields is `pre_state_sha256`, which `build_envelope()` computes as `state_binding_digest()` over a projection that **includes the journal's `authenticated_event_seq` and `authenticated_tail_sha256`** (`commands.py:94-125`).
- **The final-explanation append moves the tail.** Therefore the re-entry after P-3 derives a **different** `supervisor_operation_id` than the entry that wrote the explanation. This is not a risk or an edge case; it is arithmetic.

**Why that broke v1_2's own gate — and a second, more basic reason found while checking it.** v1_2 §11.3 gate 11b and §21 T-13a1 required the bound final-stage explanation record and the `mechanical_pass_recorded` event to carry **the same** `supervisor_operation_id`. After a P-3 crash they never can. **And in fact neither event carries that field at all:** the installed body key sets for `mechanical_pass_recorded` (`schema.py:705-723`) and `mechanical_change_explanation_recorded` (`schema.py:680-704`) do not include it, and `Operation.append()` does not add it (`engine.py:449-458`) — only `supervisor_operation_started` and `supervisor_operation_completed` carry it. **So v1_2's gate named a comparison that is unreadable, over values that would disagree if it were readable.** The outcome was strictly worse than the defect it replaced: **the PASS lands, the projection reaches `READY_FOR_ACCEPTANCE` / `next_command = null`, and the gate can never be satisfied — with no command left to run.** The first entry's `supervisor_operation_started` also stays unmatched. **A purported owner path that its own lock-time gate rejects is not an owner path**, and v1_3 does not repair it by asserting lookup-first harder.

**The v1_3 correction, in two mechanical moves and nothing else.**

1. **The owner is separated, so the append shape is identical on the first run and on every re-entry.** The final-stage explanation record is appended by its **own** ordinary supervisor operation `[proposed: the explanation-assembly operation]`, which starts, appends exactly that one record, and completes — **entirely before the PASS operation is constructed at all.** The PASS operation then starts over a journal in which that record is already durable, appends `mechanical_pass_recorded` as its **only** substantive append, and completes. Both run inside the same running window, whose projection is `WORKING` / `execute-next-claude-task` / `pass_audit_awaiting_gate` (`status.py:1205-1209`) for exactly as long as `replay.pass_event()` is null (§14 Phase A).
2. **Every ordering check is restated in terms of journal position — never in terms of an operation identity, which the records do not carry and recovery would not preserve.** The relation v1_3 proves is one the append-only authenticated chain always witnesses: **the bound explanation record's `event_seq` is strictly less than the pass event's, and no `mechanical_pass_recorded` in scope sits at or below the explanation record's position** (§11.3 gate 11b). An `event_seq` **is** the record of write order; it is invariant under re-entry, readable from every event, and true in every arrangement a crash can produce. The distinctness of the two operations remains a **write-order contract** of this design, discharged by the offline sequence and crash tests of §21 — **not asserted as a lock-time check of something the installed records cannot witness.**

**What the correction does not do.** It does not weaken the required invariant, does not make the two appends atomic, does not invent a resume, reattach, or operation-identity-carrying mechanism, does not add a mark, a store, a command, a dispatch path, or a recovery path, and does not move the audit. **The placement rule of v1_2 survives intact — the append that creates `READY_FOR_ACCEPTANCE` is still the last substantive append, and the offer is still durable before it.** What changes is who owns the append before it, and how the ordering is proved.

| Packet | Corrected here in v1_3 | Correction, in one line |
|---|---|---|
| `NH-ACCEPT-001` | §6.5a–§6.7, §7.1, §7.1a–§7.1b, §7.4, §7.7, §7.8, §11.3 gates 10–15, §14 Phase A, §21 T-13a / T-49, §22.3 items 7 and 11, §24 items 23 and 27 and the reachability limitation | The final explanation record is appended by its **own** operation that completes before the PASS operation starts, and the ordering is proved by journal position against the pass operation's own start — so every crash and re-entry position has an actually reachable owner **and** the records it leaves satisfy every lock-time gate. |

**What v1_3 deliberately carries forward unchanged.** Everything else. The eight mandatory sections; design-only acceptance meaning; candidate-not-explanation truth; the explanation's subordination to evidence; the rule that mechanical validators never prove prose truth; no model on click; no provider selected; the exact candidate / audit / PASS / predecessor / source / scope binding; stale means disabled or refused; the post-acceptance state; the automatic-next-package separation; and no implementation. **v1_3 adds no architecture, no policy, no optional hardening, no unrelated cleanup, no new event type, no code, no test, no Git operation, no acceptance or adoption, no Master or Map integration, no Register assignment, no closure, and no `PACKAGE_COMPLETE`.** The corrections v1_1 made for `NH-ACCEPT-002`, `NH-ACCEPT-003`, and `NH-ACCEPT-004` are untouched, and so is every part of v1_2 outside the owner and ordering-proof mechanics named above.

**Provenance of the v1_3 pass.** The seams this correction turns on were re-read from the actual bytes in this session before it was written, and nothing was taken from a summary, a memory, or a prior version's claim: `controller/nh_supervisor/commands.py:92-125` (`build_envelope`, and the fact that `pre_state_sha256` covers the authenticated tail), `:1396-1469` (the whole pass path, including the fresh `engine.Operation` and `operation.start()` at `:1447-1448`), `controller/nh_supervisor/engine.py:160-213` (the envelope field order, `input_envelope_sha256`, `supervisor_operation_id`, `complete_envelope`) and `:395-490` (`Operation.start` / `.append` / `.complete`, and `operation_id` reading straight from the envelope at `:405-407`), `controller/nh_supervisor/status.py:1199-1215` (precedence 12, the `pass_audit_awaiting_gate` row, and the ordinary-loop fallthrough), `controller/nh_supervisor/replay.py:986-1021` (`started_event`, `completed_event`, `unmatched_starts`) and `:1099-1101` (`pass_event()`) and `:1158-1200` (what `contradictions()` actually enumerates), `controller/nh_supervisor/schema.py:106-113` (`_b()` is a plain union, so a body key set is exactly what is listed) and `:680-723` (the installed key sets of `mechanical_change_explanation_recorded` and `mechanical_pass_recorded`, neither of which carries `supervisor_operation_id`), `controller/nh_supervisor/lease.py:438-464` (`IN_FLIGHT_CLOSURE_APPEND_TYPES`, which already contains the explanation carrier), and `interview_ui/worker.py:73-82` (`NON_RUNNING_STATES`). **No new controller behaviour is assumed, and no file was changed.**

**Version note (v1_4) — bounded correction of `NH-ACCEPT-V1_3-001` only.** This is the fifth version of this package's candidate. Its **actual predecessor** is stated exactly, not inferred from the filename:

| Predecessor | Value |
|---|---|
| Path | `NH-GOVERNANCE/05_ACTIVE_CANDIDATE/NH_NESS_DESIGN_ACCEPTANCE_RECORD_AND_UNDERSTANDABLE_ACCEPTANCE_SURFACE_MECHANICAL_DESIGN_v1_3_CANDIDATE.md` |
| SHA-256 | `7e126d83223994cb58560c6e4a4adad8bfc8e70ff146da25d0e030e90024be89` |
| Bytes | 253,029 |
| Lines | 1,776 |
| Standing | **UNCHANGED.** v1_3 was not edited, overwritten, moved, renamed, or deleted in producing this file, and neither were v1_2, v1_1, and v1_0. v1_4 was created as a byte-for-byte copy of v1_3 and then corrected. |

**What v1_4 is.** v1_4 is the **bounded mechanical correction of the single defect packet `NH-ACCEPT-V1_3-001` (IMPORTANT)**, and of nothing else. **v1_3 specified two incompatible event counts for one request class, so its own offline acceptance suite could not be satisfied.**

**The exact v1_3 contradiction, stated as the packet states it.** v1_3's normative design says every refused request appends exactly one operational refusal record; §15 F-29 classifies **a wrong method, or a GET/HEAD attempting mutation**, as exactly such a refusal; and §19 expressly includes method refusals in the authenticated refusal carrier. **But §21.4 T-45 required the same GET mutation attempt to append nothing at all** — *"a refused GET is not a press and receives no operational record either."* One request class, two counts. An implementation reading this package could not determine whether a rejected mutation attempt must be permanently recorded or must remain silent, and no implementation could pass both statements.

**The governing text this resolves against.** `NH_MASTER-20_CORRECTED_v10.md` §0B **FULL-TRANSPARENCY AND LIVING-RECORD LAW**: external inputs, rejections, and failures require permanent operational records. Master V10 §0B **ONE REAL OPERATION, ONE LOG**: one rejected mutation operation receives one permanent log, without a log-about-logging. **This candidate's own §14 D3, §15 preamble, and §19 already apply that rule correctly to request-level refusals; T-45 is the statement that contradicted them, and T-45 is what gives way.**

**The v1_4 correction, in one mechanical move.** The count is made single for that request class, and the two things v1_3 conflated are separated by name:

1. **A legitimate offer read is not a request of the mutation operation at all.** `GET /api/acceptance/offer` `[proposed]` is the read-only projection of §16.2 and Phase B of §14. It is refused nothing, it is not a press, and it **appends nothing, ever, however many times it is read** (§19, §21 T-46b). That was true in v1_3 and is unchanged.
2. **A GET or HEAD directed at the acceptance-record mutation route — or otherwise attempting mutation — is a request-level refusal like any other.** It fails closed, **appends zero acceptance events**, and — **where the authenticated journal can safely be appended to** — receives **exactly one** `supervisor_operation_completed` refusal record through the settled carrier of §19, by the single recording call of §14 Phase D3. It receives no `supervisor_operation_started`, no second record, and no record about that record.

**What the correction does not do.** It adds no event type, no carrier, no outcome code, no store, no endpoint, and no architecture. **The exactly-one-new-event-type rule, the `supervisor_operation_completed` refusal carrier and its completion-only shape, the no-log-about-logging rule, the successful-click count of exactly one acceptance event and no other event, zero mutation on GET/HEAD, zero appends from repeated legitimate offer reads, and the fail-safe exception where the journal or lock cannot safely record a refusal are all carried forward exactly as v1_3 states them.**

| Packet | Corrected here in v1_4 | Correction, in one line |
|---|---|---|
| `NH-ACCEPT-V1_3-001` | §9.2, §13.6, §14 Phase D D2–D3, §15 preamble and F-29, §16.1 and §16.4, §19, §21.4 T-45 / T-46a, §24 items 29, 31, 34, 47 | A wrong-method GET/HEAD mutation attempt is one request class with **one** event count everywhere: zero acceptance events and exactly one operational refusal record — and it is stated as distinct from a legitimate offer GET, which is a read and appends nothing. |

**What v1_4 deliberately carries forward unchanged.** Everything else. Design-only acceptance meaning; the locked names; the eight mandatory sections; the binding set; staleness; Phase-A ordering and its owner separation; crash recovery; idempotency; the terminal post-state; provider, Git, and writer isolation; and every deliberately open item, including the refusal-record volume question (§22.3 item 5). **v1_4 adds no architecture, no policy, no optional hardening, no unrelated cleanup, no new event type, no code, no test change beyond the two reconciled rows, no Git operation, no acceptance or adoption, no Master or Map integration, no Register assignment, no closure, and no `PACKAGE_COMPLETE`.** The corrections v1_1 made for `NH-ACCEPT-002`, `NH-ACCEPT-003`, and `NH-ACCEPT-004`, and everything v1_2 and v1_3 settled for `NH-ACCEPT-001`, are untouched.

**Provenance of the v1_4 pass.** This correction turns on **the candidate's own internal consistency and the governing §0B text**, not on new controller behaviour: the contradiction is between §15 F-29 / §19 and §21.4 T-45 inside this file. The refusal carrier it preserves is the installed `supervisor_operation_completed` type already cited at `controller/nh_supervisor/schema.py:740-756`, with the present-JSON-null start reference already emitted by `controller/nh_supervisor/engine.py:476-478` and the outcome set already fixed at `controller/nh_supervisor/constants.py:219-227` — **all cited unchanged from v1_1's own reading, and none of them re-derived, re-scoped, or extended here.** **No new controller behaviour is assumed, and no file was changed.**

**Version note (v1_6) — one coherent correction of four defect packets that are one lifecycle.** This is the sixth version of this package's candidate. Its **actual predecessor is v1_4, not the file whose name is one lower**, and it is stated exactly rather than inferred from the filename:

| Predecessor (the source this file was made from) | Value |
|---|---|
| Path | `NH-GOVERNANCE/05_ACTIVE_CANDIDATE/NH_NESS_DESIGN_ACCEPTANCE_RECORD_AND_UNDERSTANDABLE_ACCEPTANCE_SURFACE_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` |
| SHA-256 | `cfbd35a596bf0886a8286e9c9e7eae0d94be81ed5aa884f593623c9fec4bc26e` |
| Bytes | 270,827 |
| Lines | 1,834 |
| Standing | **UNCHANGED.** v1_4 was not edited, overwritten, moved, renamed, or deleted in producing this file, and neither were v1_3, v1_2, v1_1, and v1_0. v1_6 was created as a byte-for-byte copy of that exact source and then corrected. |

| Interrupted historical evidence (**not** a source) | Value |
|---|---|
| Path | `NH-GOVERNANCE/05_ACTIVE_CANDIDATE/NH_NESS_DESIGN_ACCEPTANCE_RECORD_AND_UNDERSTANDABLE_ACCEPTANCE_SURFACE_MECHANICAL_DESIGN_v1_5_CANDIDATE.md` |
| SHA-256 | `c9afb81bec1677782b2e008743082b0a6c9c34ab1d6429bf17bde1adc748f8d5` |
| Bytes | 281,599 |
| Lines | 1,859 |
| Standing | **UNCHANGED, AND PRESERVED EXACTLY AS INTERRUPTED HISTORICAL EVIDENCE.** v1_5 is an interrupted pass. **It is not this file's predecessor, was not used as a source, and none of its text was carried into v1_6.** It was not edited, overwritten, moved, renamed, or deleted. Its identity is recorded here so that the gap between v1_4 and v1_6 is a stated fact rather than a silence. |

**What v1_6 is.** v1_6 is the **bounded correction of four defect packets against v1_4** — `NH-ACCEPT-V1_4-001` (refusal accounting), `NH-ACCEPT-V1_4-002` (exact full pre-click head binding), `NH-ACCEPT-V1_4-003` (terminal acceptance must never disappear), `NH-ACCEPT-V1_4-004` (A5/A6 operation ownership) — **and of nothing else.**

**They are corrected as ONE lifecycle, not as four pasted patches, and the reason is mechanical rather than editorial.** The four packets are four positions on a single path from *what is offered* to *what is finally true*, and each one is only correct because of the next:

1. **The offer** is read under the **existing** journal lock so that what it publishes is one stable authenticated snapshot rather than a smear of several — and that read performs **no recovery and no mutation whatsoever** (`-001` Case A).
2. **What that stable snapshot binds** is the **entire** authenticated eight-field head plus one canonical complete-head digest — not a tail and two committed fields, which is what let a real head change slip past a stale check (`-002`).
3. **The press** re-reads and re-authenticates that entire head under the same lock and compares **every field and the digest exactly**, so any head movement at all — an intent-only advance included — stales the offer (`-002`).
4. **What each request then leaves behind is counted honestly**: a legitimate offer read appends nothing; a wrong-method mutation attempt is refused and, where the journal can safely be appended to, receives exactly one refusal record **which does move the journal and the head, and is said to**; where it cannot, nothing is appended and success is never claimed (`-001` Cases B and C).
5. **What is finally shown** is a governed terminal projection taken under that same lock, so acceptance is never exposed while a live writer still retains permission to remove it, and a truth that is genuinely neither proved nor disproved is reported as **unresolved** rather than as success or as denial (`-003`).
6. **And the whole path stands on a Phase A whose two operations are distinct** — A5 owns the final explanation and closes; only then is A6, the PASS operation, constructed (`-004`). Every stale sentence that still placed that append inside the PASS operation is corrected, because a lifecycle argument that names the wrong owner at its first step cannot be checked at its last.

**Cut any one of the six and the others stop being provable**: without the lock the snapshot is not stable, without the complete head the snapshot is not complete, without the complete comparison the press is not current, without honest counting the refusal record is a false statement about mutation, without the governed projection a proved-looking acceptance can still vanish, and without the correct owner the sequence that produces the offer cannot be traced at all.

| Packet | Corrected here in v1_6 | Correction, in one line |
|---|---|---|
| `NH-ACCEPT-V1_4-001` | §9.2, §11.2, §13.6, §14 Phase B and D2a–D3, §15 preamble / F-1 / F-29 / F-35 / F-36–F-36b, §16.1–16.5, §18 M-11, M-12, M-17, M-32, M-35, §19, §21, §24 items 29, 31, 34 | Three request classes are counted separately and honestly: a legitimate offer GET takes the existing lock for one stable snapshot with **tail recovery disabled and zero mutation and zero appends**; a wrong-method GET/HEAD at the record route is refused and — where the journal can safely be appended to — receives **exactly one** `supervisor_operation_completed`, **which mutates the journal and the head and says so**, while never touching acceptance state; and where the journal or lock cannot safely append, the same request is refused with **zero appends** and success is never claimed. |
| `NH-ACCEPT-V1_4-002` | §7.7, §8.2–§8.3, §9.3, §11.1, §11.3 gates 2a–2b and 27, §11.4, §12.3 K-2, §14 Phase B / E, §15 F-3, §16.2–§16.3, §21, §24 | The offer binds the **exact authenticated eight-field head** — `v`, `intent_generation`, `intent_number`, `intent_event_seq`, `intent_event_sha256`, `committed_event_seq`, `committed_event_sha256`, `head_auth_sha256` — plus one canonical complete-head digest over exactly that object; the press re-reads, re-authenticates, and compares **every field and the digest** under the lock, so a K-2 intent-only change stales the offer even though the event tail and both committed fields are unchanged. **The settled `ness_acceptance_identity` inputs are untouched, and journal position remains excluded from them for retry idempotency.** |
| `NH-ACCEPT-V1_4-003` | §9.6, §10.1, §10.3, §10.5, §11.1, §12.2–§12.5, §14 Phase B / E / F–F2, §15, §16.1–§16.5, §18 M-13, M-32, §19, §21, §24 | Raw journal replay and governed terminal projection are separated, and the externally visible truth is exactly three classifications — `PROVED_NOT_ACCEPTED`, `PROVED_ACCEPTED`, `UNRESOLVED`. Every governed acceptance or status reader takes the **existing** lock before projecting terminal acceptance, so **no governed reader can ever expose `ACCEPTED_FOR_DESIGN_ONLY` while a live writer still retains legal authority to remove that acceptance**; rollback is legal only for the active append attempt while it owns that lock and before terminal acceptance is exposable; and an unresolved truth is reported as unresolved, with no success, no false denial, no blind retry, no effect replay, and no extra refusal append. |
| `NH-ACCEPT-V1_4-004` | §0 the v1_1 trace row, §6.5a, §20 the `commands.py` row, §21, §24 | Every **active** sentence that still placed the final explanation append inside the PASS operation is corrected to the settled A5/A6 topology: A5 starts, appends exactly one final-stage explanation record, and completes; **only then** is A6 constructed; A6 starts, appends exactly one `mechanical_pass_recorded`, and completes; **A5's operation identity differs from A6's.** |

**What v1_6 deliberately carries forward unchanged.** Everything else. The authority order and the design-only meaning of acceptance; the eight mandatory understandable explanation sections and the independent semantic-audit requirement; every existing candidate / audit / PASS / source / predecessor / scope binding, extended only by the full head; the deterministic `ness_acceptance_identity` inputs exactly as §8.4 settles them; **exactly one new authenticated event type, `ness_candidate_acceptance_recorded`**; a successful click appending exactly one acceptance event and no companion operation event; the completion-only refusal carrier; lookup-first idempotency; the intent-before-record-before-committed ordering; the existing journal, head, lock, and tail-recovery authority with no second one of any of them; the A5/A6 normative topology; the event-sequence gate and the unmatched-start treatment; the final state `ACCEPTED_FOR_DESIGN_ONLY` / `acceptance_required = false` / `next_command = null`; the automatic next-package transition staying open and separate; and every provider, Git, implementation, Master, Map, Register, closure, `PACKAGE_COMPLETE`, Markdown, copy, and promotion non-authorization. **v1_6 adds no cleanup, no optional hardening, no speculative improvement, no unrelated architecture, and no new policy. It adds no second journal, store, head, mark, protocol, event type, or recovery authority. It writes no code, runs no test, touches no real journal, enables no button, integrates nothing, and closes nothing.**

**Provenance of the v1_6 pass.** This correction turns on **the candidate's own internal consistency, the installed two-mark head and lock behaviour this file already cites, and the governing §0B text** — not on new controller behaviour. The head fields, the head rule `intent ∈ {committed, committed + 1}` and the accepted `present == intent > committed` window are the ones already recorded at §4.1 from `controller/nh_loop.py:31241-31302`; the exclusive lock is the installed `acquire_interview_lock` (`:32184`); the recovery-enabled read and the one-suffix tail recovery are the installed `read_interview_journal(errors, allow_tail_recovery=True)` (`:31890`, `:31919-31927`) and `recover_interview_journal_tail()` (`:31944-32034`); the default non-recovering read is the installed `read_interview_journal(errors)` at `allow_tail_recovery=False` (`controller/nh_supervisor/journal.py:208-224`); the live rollback and post-write undo are `:32371-32390` and `:32397-32439`; the committed-but-unverified report is `:32502-32548`; and the refusal carrier remains the installed `supervisor_operation_completed` (`controller/nh_supervisor/schema.py:740-756`) with its present-JSON-null start reference (`controller/nh_supervisor/engine.py:476-478`) and its fixed outcome set (`controller/nh_supervisor/constants.py:219-227`). **Every one of these is cited unchanged from the readings this file already carries; none is re-derived, re-scoped, or extended, and no new controller behaviour is assumed. No file was changed, and v1_5 was neither read as a source nor altered.**

**Version note (v1_7) — micro-correction of four stale unconditional refusal statements.** This is the seventh version of this package's candidate. Its **actual predecessor** is stated exactly, not inferred from the filename:

| Predecessor (the source this file was made from) | Value |
|---|---|
| Path | `NH-GOVERNANCE/05_ACTIVE_CANDIDATE/NH_NESS_DESIGN_ACCEPTANCE_RECORD_AND_UNDERSTANDABLE_ACCEPTANCE_SURFACE_MECHANICAL_DESIGN_v1_6_CANDIDATE.md` |
| SHA-256 | `463c06e38ab98c70b8169eac7405e5e89c9f349274f87daa1f8ab7f32018aa7d` |
| Bytes | 378,463 |
| Lines | 2,219 |
| Standing | **UNCHANGED.** v1_6 was not edited, overwritten, moved, renamed, or deleted in producing this file, and neither were any earlier versions. v1_7 was created as a byte-for-byte copy of that exact source and then corrected. |

**What v1_7 is.** v1_7 is the **bounded correction of four stale unconditional refusal statements** in §4.5 D3a (line 420), §9.2 (line 961), §22.3 item 5 (line 2072), and Known limitations (line 2197), all of which must align with the canonical refusal protocol stated in §9.2. **None of these corrections changes any mechanic, gate, ordering, recovery, test, or refusal behaviour — only the statements that describe it.** The four statements previously said "every refusal receives a record" unconditionally; v1_7 aligns them with §9.2's explicit protocol: legitimate offer GET receives zero appends; ordinary appendable-route refusals receive exactly one completion-only supervisor_operation_completed record; journal/lock unsafe cases receive zero appends; unresolved possible-acceptance effects receive no additional refusal append until recovery proves truth.

**What v1_7 deliberately carries forward unchanged.** Everything else in v1_6, including every correction v1_6 made. **v1_7 adds no architecture, no policy, no refusal mechanic, no new event type, no code, no test, no Git operation, no acceptance or adoption, no Master or Map integration, no Register assignment, no closure, and no `PACKAGE_COMPLETE`.**

**Version note (v1_9) — micro-correction of one core rule statement.** This is the eighth version of this package's candidate. Its **actual predecessor** is stated exactly, not inferred from the filename:

| Predecessor (the source this file was made from) | Value |
|---|---|
| Path | `NH-GOVERNANCE/05_ACTIVE_CANDIDATE/NH_NESS_DESIGN_ACCEPTANCE_RECORD_AND_UNDERSTANDABLE_ACCEPTANCE_SURFACE_MECHANICAL_DESIGN_v1_8_CANDIDATE.md` |
| SHA-256 | `2ffbb196dfb179d973e1af428617006e9f6e2bc1f0f541a0ad4e1b2afda216ec` |
| Bytes | 381,467 |
| Lines | 2,233 |
| Standing | **UNCHANGED.** v1_8 was not edited, overwritten, moved, renamed, or deleted in producing this file, and neither were any earlier versions. v1_9 was created as a byte-for-byte copy of that exact source and then corrected. |

**What v1_9 is.** v1_9 is the **bounded correction of the single defect packet `NH-ACCEPT-V1_8-001` (IMPORTANT)**, and of nothing else. **The core rule that request outcome and acceptance truth are independent was stated in principle but not honoured in the outcome classifications.**

**The exact v1_8 defect, stated as the packet states it.** v1_8 correctly establishes in §11.1b that exactly three governed truths exist — `PROVED_NOT_ACCEPTED`, `PROVED_ACCEPTED`, `UNRESOLVED` — and that these are determined by the locked state of the authenticated journal, not by request success or failure. But §16.4 assigns the rows `refused_request`, `refused_conflict`, and `refused_not_ready` to `PROVED_NOT_ACCEPTED` unconditionally, without allowing the case where the existing terminal acceptance is already proved and durable, yet an invalid request arrives and is refused. **Such a request must be refused, yes; but the governed truth it reports back remains `PROVED_ACCEPTED` if the locked journal proves it.** The response says *"your request was invalid, and this acceptance still stands."* No response can claim both sides at once, and the request outcome is not the measure of the proof.

**The governing text this resolves against.** §11.1b **CORE RULE: REQUEST OUTCOME and ACCEPTANCE TRUTH are independent. A request may be REFUSED while the locked package truth still proves PROVED_ACCEPTED.** This candidate's own §14 Phase F2 already states the three separate truth cases that must report; §16.5 already mandates that every response state which of the three governed truths holds; **§16.4's outcome row should align with them rather than contradict them.**

**The v1_9 correction, in one statement pair and four row amendments.** The core rule is restated at §11.1b with explicit emphasis on independence, and the four outcome rows are corrected to allow the proved acceptance case:

1. **§11.1b:** A new opening sentence emphasizes that request refusal and acceptance truth are separate concerns, both determined by locked inspection but by different facts.
2. **§12.4:** A sentence is added clarifying that a conflicting-acceptance refusal preserves whatever acceptance truth the locked journal proves — including `PROVED_ACCEPTED` where an earlier valid acceptance stands.
3. **§14 Phase D2a–D3:** The refusal-handling text is clarified to separate "the request is refused" from "what the governed truth is" — refusal is about the request validity, truth is about the journal state.
4. **§14 Phase F2:** The table now explicitly shows the three possible governed truths for each row, including that a refused request may have `acceptance_truth = PROVED_ACCEPTED`.
5. **§16.4:** The `refused_request`, `refused_conflict`, and `refused_not_ready` rows are amended to show `PROVED_ACCEPTED` where the locked journal proves terminal acceptance, even though the request is refused.
6. **§16.5:** A clarifying sentence is added on the independence principle, so the response-discipline section names what the row amendments embody.
7. **§17.1–§17.4:** One sentence in §17.4 is clarified to confirm that the post-acceptance projection persists regardless of request outcome — it reports what the journal durably proves, not whether any particular request succeeded.

**What the correction does not do.** It does not change what constitutes a refusal, does not change how refusals are recorded, does not weaken any gate, does not alter any operational record, does not permit a successful append without proof, and does not move any terminal-permanence boundary. **It simply names the three truth cases in outcome rows where they were missing, so that a response can be both *"refused"* and *"PROVED_ACCEPTED"* without contradiction.** The row counts for refusal records are unchanged; the exact conditions for recording are unchanged; the three governed truth definitions are unchanged; and the terminal acceptance rule is unchanged.

| Packet | Corrected here in v1_9 | Correction, in one line |
|---|---|---|
| `NH-ACCEPT-V1_8-001` | §11.1b (opening rule), §12.4, §14 Phase D2a–D3 (refusal description), §14 Phase F2 (outcome truth row), §16.4 rows `refused_request`, `refused_conflict`, `refused_not_ready`, §16.5, §17.4 | Request outcome (refused or accepted) and acceptance truth (`PROVED_ACCEPTED`, `PROVED_NOT_ACCEPTED`, or `UNRESOLVED`) are determined by separate locked inspections; a refusal must still report whatever governed truth the authenticated journal proves, so `PROVED_ACCEPTED` may hold even when the request is refused. |

**What v1_9 deliberately carries forward unchanged.** Everything else in v1_8, including every correction v1_8 and v1_7 and v1_6 made. **v1_9 adds no architecture, no policy, no event type, no code, no test, no Git operation, no acceptance or adoption, no Master or Map integration, no Register assignment, no closure, and no `PACKAGE_COMPLETE`.** The refusal mechanics, the gate conditions, the operational record counts, the three truth classifications themselves, the terminal-acceptance permanence rule, and every other mechanic remain exactly as v1_8 (and v1_7 and v1_6) state.

**Provenance of the v1_9 pass.** This correction turns on **the candidate's own internal consistency** — the principle stated at §11.1b must align with what §16.4's outcome rows report, and both must be true. No new controller behaviour is assumed or cited; the correction is purely about applying the existing three-truth model uniformly across all response cases. **No file was changed.**

**Version note (v1_10) — micro-correction of three §16.4 refusal-count rows.** This is the ninth version of this package's candidate. Its **actual predecessor** is stated exactly, not inferred from the filename:

| Predecessor (the source this file was made from) | Value |
|---|---|
| Path | `NH-GOVERNANCE/05_ACTIVE_CANDIDATE/NH_NESS_DESIGN_ACCEPTANCE_RECORD_AND_UNDERSTANDABLE_ACCEPTANCE_SURFACE_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` |
| SHA-256 | `ba11896877b7ba6e25f328e551b0dbfbcb3d042455c77b4a938470953d99bda3` |
| Bytes | 391,429 |
| Lines | 2,273 |
| Standing | **UNCHANGED.** v1_9 was not edited, overwritten, moved, renamed, or deleted in producing this file, and neither were any earlier versions. v1_10 was created as a byte-for-byte copy of that exact source and then corrected. |

**What v1_10 is.** v1_10 is the **bounded micro-correction of the refusal-count text in three §16.4 outcome rows**, and of nothing else. **The §11.1b core rule — request outcome and acceptance truth are independent — requires that appendable refusals be recorded exactly once regardless of which proved truth holds, so the refusal-count columns must align accordingly.**

**The exact v1_9 incompleteness, stated as the packet states it.** v1_9 correctly establishes independence at §11.1b and allows `PROVED_ACCEPTED` outcomes for refused requests in the three rows. But the refusal-count descriptions still treat `PROVED_ACCEPTED` as a case where recording does not happen, or happens conditionally. Specifically:
- `refused_request` says: "**1** where ... the truth is `PROVED_NOT_ACCEPTED` ... **0** ... where the truth is `UNRESOLVED` or `PROVED_ACCEPTED`"
- `refused_conflict` says: "**1** where recording is safe **and** the truth is `PROVED_NOT_ACCEPTED` or `UNRESOLVED` without an acceptance possibly already existing; **0** otherwise"
- `refused_not_ready` says: "**1** where recording is safe and the truth is `PROVED_NOT_ACCEPTED`; **0** where it is `UNRESOLVED` or the truth is `PROVED_ACCEPTED`"

**But §11.1b states an appendable refusal must record exactly one completion-only `supervisor_operation_completed` regardless of whether the truth is `PROVED_ACCEPTED` or `PROVED_NOT_ACCEPTED`.** The governance principle and the outcome-row counts do not yet agree.

**The governing text this resolves against.** §11.1b **CORE RULE: REQUEST OUTCOME and ACCEPTANCE TRUTH are independent. A request may be REFUSED while the locked package truth still proves PROVED_ACCEPTED.** §9.2 Cases B and C establish that an **appendable** refusal records exactly one completion-only supervisor operation; a **non-appendable** refusal records zero. The distinction is appendability, not truth classification. The three governed truths determine what response is sent, not whether a refusal record is written.

**The v1_10 correction, in three row amendments.** The refusal-count text is aligned to state that appendable refusals record exactly one `supervisor_operation_completed` under either `PROVED_ACCEPTED` or `PROVED_NOT_ACCEPTED`; zero appends when unappendable or when truth is `UNRESOLVED`:

1. **§16.4 `refused_request` row:** the refusal-count column changes from "**1** where ... and the truth is `PROVED_NOT_ACCEPTED` ... **0** where they cannot or where the truth is `UNRESOLVED` or `PROVED_ACCEPTED`" to "**1** where the existing journal and lock can safely be appended to and the truth is `PROVED_NOT_ACCEPTED` or `PROVED_ACCEPTED` ... **0** where they cannot or where the truth is `UNRESOLVED`".
2. **§16.4 `refused_conflict` row:** the refusal-count column changes from "**1** where recording is safe **and** the truth is `PROVED_NOT_ACCEPTED` or `UNRESOLVED` without an acceptance possibly already existing; **0** otherwise" to "**1** where recording is safe and the truth is `PROVED_NOT_ACCEPTED` or `PROVED_ACCEPTED`; **0** where recording is unsafe or where the truth is `UNRESOLVED`".
3. **§16.4 `refused_not_ready` row:** the refusal-count column changes from "**1** where recording is safe and the truth is `PROVED_NOT_ACCEPTED`; **0** where it is `UNRESOLVED` or the truth is `PROVED_ACCEPTED`" to "**1** where recording is safe and the truth is `PROVED_NOT_ACCEPTED` or `PROVED_ACCEPTED`; **0** where recording is unsafe or where the truth is `UNRESOLVED`".

**What the correction does not do.** It does not change what constitutes an appendable refusal, does not change the behaviour of recording, does not weaken any gate, does not add an event type, and does not touch acceptance state preservation. **It aligns three outcome-row descriptions so the refusal-count text honours the §11.1b independence principle that v1_9 already stated.** All three truth classifications remain defined identically; all three refusal mechanics remain unchanged; and all three rows preserve the governed-truth column unchanged.

| Packet | Corrected here in v1_10 | Correction, in one line |
|---|---|---|
| `NH-ACCEPT-V1_9-001` | §16.4 rows `refused_request`, `refused_conflict`, `refused_not_ready` — refusal-count columns only | An appendable refusal records exactly one `supervisor_operation_completed` regardless of whether the proved truth is `PROVED_ACCEPTED` or `PROVED_NOT_ACCEPTED`; the refusal-count rows now state it uniformly across both cases instead of conditionally excluding one. |

**What v1_10 deliberately carries forward unchanged.** Everything else in v1_9, including every correction v1_9 and every earlier version made. The three governed truths, the request-outcome independence principle, the terminal-acceptance permanence rule, the appendability distinction, the completion-only carrier, the failure-to-record cases, and the unresolved-effect exception. **v1_10 adds no architecture, no policy, no event type, no code, no test, no Git operation, no acceptance or adoption, no Master or Map integration, no Register assignment, no closure, and no `PACKAGE_COMPLETE`.** Every other §16.4 row, every other section, and every other mechanic remain exactly as v1_9 states.

**Provenance of the v1_10 pass.** This correction turns on **the candidate's own internal consistency** — the §11.1b principle must align with what §16.4's outcome rows state about recording, and both must be true. No new controller behaviour is assumed or cited; the correction aligns three refusal-count descriptions to honour the independence principle v1_9 already established. **No file was changed.**

**Version note (v1_11) — bounded correction of `NH-ACCEPT-V1_10-001` only.** This candidate was created from the exact unchanged v1_10 candidate: `NH-GOVERNANCE/05_ACTIVE_CANDIDATE/NH_NESS_DESIGN_ACCEPTANCE_RECORD_AND_UNDERSTANDABLE_ACCEPTANCE_SURFACE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md`, SHA-256 `694fd3574905d1aa058f1d17da9157a138a19b29d4d067a61ef6e689c84990a7`, 397,891 bytes, 2,310 lines. Every earlier candidate, including interrupted v1_5, remains unchanged.

**What v1_11 corrects.** v1_11 corrects only the A5/A6 crash-and-re-entry boundary. If A5's final explanation or A6's mechanical PASS is already durable but that operation's matching completion is missing, recovery reconstructs the original authenticated operation envelope, reattaches the original authenticated start to the existing `Operation`, and appends only the missing matching `supervisor_operation_completed`. It never starts that operation again and never repeats the explanation or PASS. A6 cannot start before matching A5 completion is durable, and `READY_FOR_ACCEPTANCE` cannot be projected before matching A6 completion is durable.

**What v1_11 does not change.** It adds no event type, command, store, mark, journal, recovery authority, provider dispatch, implementation, Git action, acceptance, adoption, Master/Map integration, next-package transition, closure, or `PACKAGE_COMPLETE`. It uses the already-installed same-operation reattachment pattern and changes no settled acceptance meaning or safety boundary.

**Version note (v1_12) — bounded consistency/provenance correction after ChatGPT's independent audit of the actual v1_11 file.** v1_12 was created from the exact unchanged `NH_NESS_DESIGN_ACCEPTANCE_RECORD_AND_UNDERSTANDABLE_ACCEPTANCE_SURFACE_MECHANICAL_DESIGN_v1_11_CANDIDATE.md`, SHA-256 `772d30680fd3e08cd68a6fffc02aa1d1088109596151522a086401e58858e063`, 397,364 bytes, 2,316 lines. v1_12 changes only nine active stale self-description/readiness/recovery/provenance statements that remained after v1_11. It changes no acceptance mechanic. The controlling mechanic remains: matching A5 completion before A6 starts, and matching A6 completion before `READY_FOR_ACCEPTANCE`. Every earlier candidate, including interrupted v1_5, remains unchanged.

**Version note (v1_13) — bounded correction of the pre-effect unmatched-start / completed-pair contradiction found by ChatGPT's independent audit of the actual v1_12 file.** v1_13 was created from the exact unchanged `NH_NESS_DESIGN_ACCEPTANCE_RECORD_AND_UNDERSTANDABLE_ACCEPTANCE_SURFACE_MECHANICAL_DESIGN_v1_12_CANDIDATE.md`, SHA-256 `6e1a3cfb7a0aed8b819d4d3180d7fd46ae55ac8f7ef46b9a044a6412056e335d`, 397,781 bytes, 2,319 lines. v1_13 changes only the gate/test/provenance wording needed to distinguish historical pre-effect unmatched starts from the one effect-owning completed A5 pair and the one effect-owning completed A6 pair. It adds no recovery mechanism and changes no acceptance meaning.

**Version note (v1_14) — micro-correction of one stale P-3c crash-table state found by ChatGPT's independent audit of the actual v1_13 file.** v1_14 was created from the exact unchanged `NH_NESS_DESIGN_ACCEPTANCE_RECORD_AND_UNDERSTANDABLE_ACCEPTANCE_SURFACE_MECHANICAL_DESIGN_v1_13_CANDIDATE.md`, SHA-256 `cfcb10d9b40f945cab91bc9fc43d722235af8ae9555a537a6518558ec4e48e6c`, 400,833 bytes, 2,322 lines. The correction changes no acceptance mechanic, recovery mechanism, operation identity rule, or policy.

---

## §1 — PLAIN MEANING (everyday words first)

Right now, N.H's local design loop can get all the way to the end of a package by itself. It writes a candidate, has it audited, corrects it, has it audited again, and eventually the controller records a real PASS. Then it stops and says: *ready for you*.

And then nothing can happen. There is a card in the browser with a button on it, and the button is switched off. Its label literally says acceptance recording is not authorized yet. That is deliberate and correct: nothing in the system currently knows how to write down "Ness accepted this" safely, so nothing is allowed to pretend it did.

This file designs the missing piece — and it designs it around one worry, which is the whole reason the package exists:

> **A button that is easy to press is dangerous if what it means is hard to know.**

So the design is not "switch the button on". The design is:

**First, N.H must be able to explain the thing in ordinary language, and prove that the explanation belongs to exactly this file and exactly this passed check.** Eight plain sections: what this package does; what actually changed; what changed compared with the previous version; what this changes for N.H in real use; what did *not* change; what is still open; what the audit actually said; and what pressing Accept does and does not do. If that explanation is missing, or belongs to an older file, or belongs to an older check, the button is not offered at all. Not greyed out and clickable anyway — **not offered**.

**Second, pressing Accept means one small, exact thing and nothing more.** It means: *I accept this exact file, as a design, for design-only status.* It does not adopt anything into the main blueprint. It does not permit coding. It does not mark the package complete. It does not close anything that is still open. It does not call any model. It does not touch Git. It does not copy, move, promote, or generate any file. It does not start the next package.

**Third, the press is written down once, in the record N.H already keeps.** The system already has one authenticated, append-only, hash-chained, locked, crash-safe interview journal. Acceptance goes in there — one new kind of entry, appended once, bound to the exact file, the exact audit, the exact PASS, the exact explanation, and the exact position the record stood at when Ness pressed. **No second journal. No second store. No second acceptance system.**

**Fourth, if anything at all has moved, N.H refuses instead of guessing.** A newer candidate, a newer audit, a changed source, a new question, an open model request, an explanation that no longer matches — any of those and the press is refused, **no acceptance is written**, and the page says plainly that the record moved and must be read again. A refusal is not silence: N.H writes down, once, that a press was refused and why — because the living-record law counts a refusal as a real thing that happened, not as nothing.

**Fifth, after acceptance the loop stops for this package.** The state becomes `ACCEPTED_FOR_DESIGN_ONLY`. Nothing runs. No model is called. No file is written. The accepted candidate stays byte-for-byte what it was. Turning that acceptance into a receipt file, into the Master, into the Map, or into permission to build stays exactly where it is today: **separate, later, and Ness's.**

Three hard words used below, explained once:

- **Candidate** = a proposed version Ness has not adopted.
- **Closure record / receipt** = a separate Markdown file recording that Ness accepted something. **Pressing Accept does not create one.**
- **Binding** = the exact set of identities an entry is tied to, so that it can only ever mean one thing.

---

## §2 — AUTHORITY, OWNERS, AND THE SOURCES ACTUALLY READ

### 2.1 Authority order (obeyed in this order)

1. `NH-GOVERNANCE/01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` — **governs every conflict.**
2. `NH-GOVERNANCE/01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`
3. `NH-GOVERNANCE/01_AUTHORITATIVE/cursorrules`
4. `NH-GOVERNANCE/01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`
5. `NH-GOVERNANCE/02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` — **subordinate to the four above.**

Where the Defaults and Master V10 differ, **Master V10 governs**. Where the Map's register wording and an accepted package's own closure record disagree, **the accepted package and its closure record govern**. A candidate never replaces an adopted file until Ness explicitly adopts it.

Note on the Defaults: a later `NH_DECISION_DEFAULTS-S19_v2_3.md` exists in `01_AUTHORITATIVE/` and a `NH_DECISION_DEFAULTS-S19_v2_3_CANDIDATE.md` exists in `05_ACTIVE_CANDIDATE/`. **This file uses v2_2 as the adopted Defaults**, exactly as instructed and exactly as the ChatGPT project-instruction file names it. It makes no claim about v2_3's standing and does not adopt, promote, or reason from it.

### 2.2 Governing laws named, not restated as new authority

- **§0** — N.H never decides facts about Ness's life for him. Acceptance is Ness's act; nothing in this design may perform it, infer it, default it, or anticipate it.
- **§0A** — the DUMB / SMART separation and the membrane. Every check in this design is DUMB: a comparison of identities and a structural check of a record. **No check in this design judges whether prose is true.**
- **§0B** — the full-transparency and living-record law, quoted where it binds: *"ONE REAL OPERATION, ONE LOG. Every real event or operation receives one permanent log record. Merely creating that log does not create another automatic log about creating the log."* and *"NO DOUBLE EVIDENCE. A log proves that an operation occurred. It does not make the underlying information more correct, more certain, or more heavily supported merely because it was used or logged. One underlying record must not become several independent votes for itself."* Both bind §9 and §19 directly.
- **§7P** — authority boundaries. This design creates no authority and promotes nothing to authority.
- **§7Q / §25** — privacy and access. The acceptance record contains identities and Ness's own explicit action; it contains no third-party material and no Level 1 material.
- **`cursorrules` §1A** — *"Build a second or parallel implementation of any gating, promotion, or write-validation logic outside the designated modules for each layer"* is permanently prohibited. **This is the reason §9.6 forbids a second acceptance store, a second journal, a second high-water mark, and a second append path.**
- **`cursorrules` IDENTITY** — *"You propose. Ness approves. You implement. Never skip the approval step."* This design is a proposal.
- **Companion §11 / project instructions §11** — during design completion: no coding, no production store, no live N.H disk changes, no hidden Master or Map integration, no Register-C implementation, no Cursor build instructions.

### 2.3 Governing and design sources — identities recomputed from disk in the v1_0 pass, carried forward unchanged

| Path | SHA-256 | Bytes | Lines |
|---|---|---|---|
| `NH-GOVERNANCE/01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` | 506,934 | 5,736 |
| `NH-GOVERNANCE/01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696` | 37,048 | 314 |
| `NH-GOVERNANCE/01_AUTHORITATIVE/cursorrules` | `5050d08825b93acd72a79d07946e43c8cbe537e079517ccfe66bcae8e30e96e9` | 34,821 | 717 |
| `NH-GOVERNANCE/01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | `cdcc6134e273014472ad288dc349ce0c7c525638a73929f7dede52d30d040aeb` | 465,376 | 5,580 |
| `NH-GOVERNANCE/02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` | 286,256 | 899 |
| `NESS_DESIGN_INPUTS/NH_LIVE_LOOP_AUTOMATIC_SUPERVISOR_DECISION_v1_0.md` | `3d36b8c2ac592cd529e4f434f69d26f6c83c57cf3ebefba076261b08dd9ddd77` | 14,631 | 350 |
| `controller/NH_AUTOMATIC_SUPERVISOR_MECHANICAL_CHANGE_SPEC_v1_0_CANDIDATE.md` | `f23734d3f166b0005a06ad3cec7e3b8a0fb67221e2c0ad448cd26e921158330c` | 57,068 | 1,308 |
| `NH-GOVERNANCE/05_ACTIVE_CANDIDATE/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md` | `b39654a60744982d0e2f16c2bc3cd7a33f6ae47ff55b63b5b1dfffada719d709` | 282,955 | 3,260 |
| `NH-GOVERNANCE/04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | `937b90913bfd2578e5a195e33fb7e3e5f7523cd0a3c58d9124d412d85c1411fe` | 11,909 | 210 |
| `NH-GOVERNANCE/05_ACTIVE_CANDIDATE/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` | `1f9ea714f1a182c0857e80399850a3aeebcf4a50a32d5a200fce57a5d5f47ae3` | 343,868 | 1,686 |
| `NH-GOVERNANCE/04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | `91c52869fb1616f25a5193a5eeca7e70ba0bf0fa755c8ce5648719efae8f9b11` | 18,450 | 272 |

**The AIC and UDOK identities above match, byte for byte, the identities their own closure receipts record as the exact artifacts Ness accepted.** That is the evidence this design uses for "what an accepted artifact and its closure look like in this project" — §12.4 and §17 depend on it.

`/home/ness/NH_NOTEBOOK_COMPLETION_LAB_v1_4/immutable_source/NH_CHATGPT_PROJECT_INSTRUCTIONS_FULL_v1_2.md` was **read in full** (340 lines, nonempty, the exact copy). Its byte identity is deliberately **not** stated here: that path lies outside this session's permitted working directory, so no hash could be computed for it in this session, and **an unverified number is not written down as if it were verified.** Its §1 authority order, §2 roles, §9 "Claude must never" list, §10 independent-audit list, and §11 file-and-phase safety rules are obeyed throughout.

### 2.4 Code seams read, with identities recomputed from disk in the v1_0 pass, carried forward unchanged

These are **evidence about the current state**, not files this design edits. **v1_1 note:** the cited seams were re-read from the actual bytes in the v1_1 pass before every correction below; the identities in this table are the v1_0 pass's recomputed values and are **not** re-asserted as recomputed in the v1_1 pass. `controller/nh_supervisor/engine.py` and `controller/nh_supervisor/feed.py` were additionally read in the v1_1 pass and are cited below by line; **no identity is stated for them, because none was computed.**

| Path | SHA-256 | Bytes | Lines |
|---|---|---|---|
| `controller/nh_loop.py` | `1e3600f09d0b30f77586847ed7c1a85206834a385411ba08ae29e8422d552c69` | 2,130,262 | 45,958 |
| `controller/nh_supervisor/schema.py` | `7a700b7da72c1d12b98a370672d591c7f390dba02d61f4c30528e55f10ac496c` | 27,511 | 847 |
| `controller/nh_supervisor/replay.py` | `c75f7ee18e69addd18ee95dc91997b669146b8c0e207f6e8124e6514e5a265ca` | 52,806 | 1,266 |
| `controller/nh_supervisor/status.py` | `0c8dd731dad76ddff881929b03a88a6fb462ebfe16dc0aabbee73816b626252f` | 83,153 | 1,900 |
| `controller/nh_supervisor/constants.py` | `a5120f1fb409aac72bfeb261eebbc2895c2df3bf0d63e2c703d2baf662006ec3` | 23,400 | 793 |
| `controller/nh_supervisor/commands.py` | `bcbb3611f1da7df6bed437bdc77470ff12028337c76092001da86faf6d16cab9` | 229,962 | 5,227 |
| `controller/nh_supervisor/journal.py` | `1acd637fd38b33d97911dc566da01d8339b122f5d967e70f740dfb4085f9b4ef` | 15,533 | 418 |
| `controller/nh_supervisor/identity.py` | `5c5bf4e3c67a65950f7da4a83eb6a8f48b61d52e4b6485b77fbe28a326f3461d` | 29,404 | 871 |
| `controller/nh_supervisor/canonical.py` | `4f4cad66fbfe57026848b08afffba1d55a779f14817493f3b62c13bbf3f29fa6` | 4,322 | 136 |
| `interview_ui/server.py` | `28a4ed449cd2297a7d0f027857c638caaf6d5ac58a69483c405cdf4517e56cc6` | 35,717 | 850 |
| `interview_ui/supervisor.py` | `9f9d15a70e0cf15bec9eef2e53f1b9ca27beee208c1e65b8caf4f5025563bd31` | 17,644 | 436 |
| `interview_ui/worker.py` | `eba45d90b4eb2ffe663ea3d47863edf7f53c08ce81f734cfdb88bacfbd3a2f08` | 21,350 | 530 |
| `interview_ui/static/index.html` | `c62b879e5595e7ff97f769b522f0b81eff5714b6ffd062c82ff18fc9bb73a30a` | 11,243 | 226 |
| `interview_ui/static/app.js` | `fe758460394f8a7a4913df97e418b01c94326ed679c8361e11a123647d3b9e30` | 23,903 | 636 |
| `interview_ui/production.py` | `32d4c9ac2fa752a43dbd8b43fcb2bc866d1166a5008061b12412ad79b72ccc9f` | 9,354 | 235 |

**No file in either table is modified, moved, renamed, or deleted by this candidate.**

### 2.5 Honest statement of dependency standing

- **AIC (Addition 1)** is an **ACCEPTED** dependency by its own closure receipt, dated August 20, 2026, *"for its current standalone design scope only"*, and that receipt explicitly *"does not authorize the parked browser acceptance-button / acceptance-record / UI / controller package."* **This candidate belongs to that parked package's versioned design lineage, and it treats AIC exactly on those terms.**
- **UDOK (Addition 2)** is an **ACCEPTED** dependency by its own closure receipt, dated August 21, 2026, on the same terms, and it too excludes *"the parked acceptance-button package"*. UDOK v1_9 §3.4 names it in its own out-of-scope list. **This candidate consumes UDOK's durable-operation and lookup-first recovery discipline by reference and redesigns none of it.**
- **The automatic-supervisor mechanical change spec** (`controller/NH_AUTOMATIC_SUPERVISOR_MECHANICAL_CHANGE_SPEC_v1_0_CANDIDATE.md`) is, on its own face, *"MECHANICAL CHANGE SPECIFICATION CANDIDATE — NOT INSTALLED, NOT ACCEPTED, NOT GOVERNANCE"*. Its §14 states plainly: *"No acceptance endpoint is implemented by this change… its acceptance button remains unavailable until a separate accepted acceptance-record design exists."* **This candidate does not upgrade that spec's status and does not claim to be accepted merely because it is the design that spec waits for.**
- The installed `controller/nh_supervisor/__init__.py` docstring refers to `spec/NH_AUTOMATIC_SUPERVISOR_MECHANICAL_CHANGE_SPEC_v1_13_CANDIDATE.md`. **No `controller/spec/` directory and no v1_13 spec file exist on disk in this workspace.** That mismatch is recorded as an observed fact in §23 and is not resolved, repaired, or reasoned around here.

  **Two different things, kept apart (corrected in v1_1).** The absent v1.13 document and the installed command protocol are **not** the same question, and v1_0 wrongly ran them together:

  1. **The v1.13 specification document is genuinely absent.** That is a real **documentation and provenance gap**: the installed package names a specification that cannot be read. What v1.13 says about acceptance is unknown and is not assumed anywhere in this file.
  2. **The installed supervisor command protocol is reachable, today.** `controller/nh_supervisor/constants.py:771-783` registers `SUPERVISOR_COMMANDS` — `supervisor-status`, `supervisor-operation-status`, `diagnose-next-correction-batch`, `execute-next-claude-task`, `process-custodied-provider-result`, `close-open-consumption`, `reconcile-provider-request`, `probe-provider-availability`, `open-new-provider-episode`, `record-semantic-scope-unlock` — and `SUPERVISOR_COMMAND_SET`. `controller/nh_supervisor/commands.py:5216-5227` maps every one of them to a handler in the single `COMMAND_TABLE`. `controller/nh_loop.py:45946-45949` dispatches **generically**: any `command in nh_supervisor.constants.SUPERVISOR_COMMAND_SET` other than the separately handled `execute-next-claude-task` is routed to `command_supervisor(command)`. `interview_ui/server.py:471-477` already calls `run_controller("supervisor-status")`; its `except ControllerFailure` fallback is a tolerance for an older controller, **not** evidence that the command is unreachable on the installed one.

  **Therefore an absent specification document is not a reachability blocker, and v1_1 asserts none.** What is genuinely absent for this package is narrower and is stated as exactly that: **no acceptance command, no acceptance primitive, no acceptance HTTP endpoint, and no accepted-only state exist today** (§4.2). A later, separately authorized implementation of the acceptance command would be reached by the **existing** generic dispatch once it is registered in `SUPERVISOR_COMMANDS` and mapped in `COMMAND_TABLE` — **no new or parallel CLI dispatch path is required, and none is authorized.** Its exact spelling remains open (§22.3 item 11).

---

## §3 — FROZEN SCOPE AND NON-GOALS

### 3.1 In scope

1. The **understandable acceptance surface**: what must be proved, presented, and bound before an Accept action may be actionable at all (§6).
2. The **explanation record**: its logical content, its eight fixed parts, its append-only lifecycle and supersession, its actual-predecessor binding, and its staleness rules (§7).
3. The **acceptance binding set** and the **deterministic acceptance identity** (§8).
4. The **one new authenticated event type** `ness_candidate_acceptance_recorded`, its body, and its meaning (§9).
5. **Replay and state precedence**, and the exact post-commit projected state (§10, §17).
6. **Transaction, lock, revalidation-under-lock, idempotency, concurrency, and crash recovery** (§11, §12).
7. The **controller / server / browser trust boundary** and the click algorithm (§13, §14).
8. The **fail-closed matrix** (§15) and the **logical HTTP contract with its outcome set** (§16).
9. **Negative invariants and must-nevers** (§18), **§0B logging compliance** (§19).
10. A **reference-only** implementation-surface map (§20), an **offline disposable test/fault matrix** (§21), the **wiring delta and open dependencies** (§22), what could not be confirmed (§23), and a **completeness self-audit** (§24).

### 3.2 Out of scope, and untouched

- Any code change, anywhere. **No file listed in §2.4 is edited by this candidate.**
- Enabling the existing disabled button as a change in its own right (§4.4 explains why that alone would be a defect, not a fix).
- Any provider, model, endpoint, transport, prompt, or model-selection decision.
- Any Git operation, any repository move, any promotion, projection, copy, or generation of a Markdown receipt.
- Master V10 adoption, Design and Wiring Map adoption or integration, Register assignment, controlled component ID assignment, bundle placement.
- `PACKAGE_COMPLETE`, closure records, dependency closure, and the automatic transition to a next package (**explicitly left OPEN and SEPARATE** — §22.3).
- Adoption, implementation, coding, production stores, deployment, migration, or build authorization.
- Storage technology, serialization library, field spelling, HTTP path spelling, numeric thresholds, and display strings other than the locked names of §0.

### 3.3 The scope fence, in one sentence

**This design makes one press mean exactly one thing, prove that meaning before it is offered, write it down exactly once, and cause nothing else.**

---

## §4 — CURRENT-STATE DELTA (verified from the actual files, not assumed)

### 4.1 What already exists and works

| Fact | Where it is, on disk |
|---|---|
| Eight public workflow states, including `READY_FOR_ACCEPTANCE`, and **no accepted state** | `controller/nh_supervisor/constants.py:77-87` |
| `mechanical_pass_recorded` is appended only after a hard PASS gate, and its `pass_outcome` is the string `READY_FOR_ACCEPTANCE` | `controller/nh_supervisor/commands.py:1396-1469` |
| The PASS gate proves: no pending write-ahead, frozen envelope clean, no open provider request, no open result custody, no open availability probe, no open audit-usability retry, and no open consumption | `commands.py:1400-1424` |
| State projection precedence 12: a `mechanical_pass_recorded` event ⇒ `workflow_state = READY_FOR_ACCEPTANCE`, `next_command = None` | `controller/nh_supervisor/status.py:1199-1204` |
| `acceptance_required` is **derived**, not stored: `projected["workflow_state"] == "READY_FOR_ACCEPTANCE"` | `status.py:1711` |
| One authenticated, append-only, hash-chained, HMAC-authenticated, segment-rolling journal with **two marks** in one head — an **intent** mark written *before* the record it describes and a **committed** mark advanced *after* those bytes are durable — tail compare-and-swap under an exclusive lock, byte-exact rollback on a failed live append, one-suffix tail recovery for a dead-mid-append, and a full re-read/re-validate after commit | `controller/nh_loop.py:32131-32549`; intent mark `:32314-32334`; committed mark `:32460-32474` |
| The head's own rule: `intent ∈ {committed, committed + 1}`; `present < committed` is a deletion and is refused; `present > intent` is a foreign write and is refused; `present == committed` requires the committed digest to equal the last record; **`present == intent > committed` is the accepted interrupted-append window, and the record that landed must be exactly the one that was declared** | `controller/nh_loop.py:31241-31302` |
| `read_interview_journal(errors, allow_tail_recovery=False)` — read-only callers **fail closed** on an unterminated final line; only a caller that is about to write passes `allow_tail_recovery=True`, which takes the exclusive lock and calls `recover_interview_journal_tail()` | `controller/nh_loop.py:31890-31941` |
| `recover_interview_journal_tail()` — removes **one** unterminated trailing suffix, **only under the exclusive writer lock**, only when the prefix is a completely valid chain, by truncate-to-proved-length plus fsync plus byte-for-byte re-read; a **malformed but complete** final line is never touched | `controller/nh_loop.py:31944-32034` |
| The installed production gateway reads **without** tail recovery before appending: `NhLoopJournalGateway.read()` and `.append()` both call `read_interview_journal(errors)` with the default `allow_tail_recovery=False` | `controller/nh_supervisor/journal.py:208-224` |
| One supervisor-operation record interface — `Operation.start()` ⇒ `supervisor_operation_started`, `Operation.append(type, body)` for each substantive event, `Operation.complete(outcome, …)` ⇒ `supervisor_operation_completed` carrying `operation_outcome`, `controller_returncode`, `post_state_sha256` and a dependency slot; `supervisor_started_event_seq` is written as **present JSON null** when there is no start event | `controller/nh_supervisor/engine.py:395-490`, esp. `:476-478` |
| `OPERATION_OUTCOMES = ("ok", "dependency", "safety_hold", "needs_ness", "needs_user_action", "ready_for_acceptance")` | `controller/nh_supervisor/constants.py:219-227` |
| The PASS is recorded **inside one supervisor operation**: `operation.start()`, then `operation.append("mechanical_pass_recorded", body)`, then `operation.complete("ready_for_acceptance")` — so events already follow the pass event inside the same owned transition | `controller/nh_supervisor/commands.py:1442-1469` |
| Per-`(version, type)` body-key rows are built as a table — version-4 rows byte for byte, version-5 rows for the same and the supervisor types — so an **existing type may carry a new body version with a different key set without becoming a new event type** | `controller/nh_supervisor/schema.py:778-805` |
| Journal format, HMAC label, version-dependent auth material, envelope keys, and per-`(version, type)` body-key validation shared by the installed journal and the disposable rehearsal journal | `controller/nh_supervisor/journal.py:31-138, 269-417` |
| Deterministic derived identities: `SHA256(canonical_json([DOMAIN, OBJECT]))`, exact-key input objects, refusal on missing or extra inputs, family prefixes | `controller/nh_supervisor/identity.py:718-736`; `canonical.py:28-60`; `constants.py:676-689` |
| Per-`(version, type)` event body schemas, including `mechanical_pass_recorded` and `mechanical_audit_recorded` | `controller/nh_supervisor/schema.py:119-757` |
| Replay accessors: `tail()`, `pass_event()`, `newest_audit(candidate_sha256)`, open-request / open-custody projections | `controller/nh_supervisor/replay.py:51-55, 97-98, 239-260, 1081-1101` |
| The worker runs **nothing** in `READY_FOR_ACCEPTANCE`, and says so in words: *"waiting for separate explicit acceptance; nothing is accepted"* | `interview_ui/worker.py:73-82, 419-420` |
| The browser obtains workflow state only from a fresh, authenticated `supervisor-status`; it never reads the private operational journal as authority | `interview_ui/server.py:424-465` |
| The UI hard-codes `"acceptance_available": False` and the note *"Ready for acceptance is not acceptance. No acceptance endpoint exists in this candidate."* | `interview_ui/server.py:534-541` |
| The feed projection hard-codes `claims_acceptance: False` | `interview_ui/supervisor.py:435` |
| Localhost-only Host allow-list on every GET and POST | `interview_ui/server.py:700-702, 744-747, 801-804` |
| Strict JSON body handling: `Content-Type` must start `application/json`, length bounded by `MAX_REQUEST_BYTES = 32_768`, must decode to one JSON object | `interview_ui/server.py:40, 783-799` |
| A restrictive CSP with `default-src 'self'`, `script-src 'self'`, `frame-ancestors 'none'`, plus `nosniff`, `no-referrer`, `DENY`, `no-store` | `interview_ui/server.py:704-714` |
| The answer path validates an exact required/allowed field set and refuses unsupported fields | `interview_ui/server.py:663-671` |

### 4.2 What deliberately does not exist — preserved as fact, not treated as an oversight

1. **The acceptance button is deliberately disabled.** `interview_ui/static/index.html:193` is literally:
   `<button class="primary-button" type="button" disabled>Acceptance recording is not authorized yet</button>`
2. **There is no click handler for it.** `interview_ui/static/app.js` binds submit/click handlers for answers (`:505`), question presentation (`:566`), refresh (`:617`) and the tabs (`:618-628`). It touches the acceptance card exactly once, to show or hide it: `app.js:293-296`. **No listener is attached to that button anywhere.**
3. **There is no acceptance endpoint.** `do_POST` routes exactly two paths — `/api/questions/present` and `/api/answers` — and returns 404 for everything else (`server.py:801-813`).
4. **There is no acceptance command and no acceptance primitive in the controller.** The named-command chain (`nh_loop.py:45907-45945`) has no acceptance command; the usage block (`nh_loop.py:3278-3350`) lists none; `SUPERVISOR_COMMANDS` (`constants.py:771-783`) contains none; and `COMMAND_TABLE` (`commands.py:5216-5227`) maps none. **This is the absence of an acceptance command, not the absence of a way to reach supervisor commands:** `nh_loop.py:45946-45949` already dispatches every registered supervisor command generically (§2.5). What does not exist is the acceptance command itself.
5. **There is no accepted-only state.** `WORKFLOW_STATES` has eight members and `ACCEPTED_FOR_DESIGN_ONLY` is not one of them (`constants.py:77-86`).
6. **`READY_FOR_ACCEPTANCE` is already a non-running state.** It is in `NON_RUNNING_STATES` (`worker.py:73-82`) and its projection sets `next_command = None` (`status.py:1201-1203`).
7. **No acceptance store, marker, file, or side-channel exists**, and none is proposed.

### 4.3 A real ambiguity in the existing vocabulary, recorded so this design cannot inherit it

The word "accepted" already appears in the controller with **two unrelated provider-side meanings**:

- `PROVIDER_PHASES` includes the phase `"accepted"` — a provider endpoint accepted a request (`constants.py:142-150`).
- `ACCEPTANCE_AUTHORITIES = ("none", "provider_request_ref", "idempotency_echo")` — how a provider's acceptance of a request was evidenced (`constants.py:170`).

**Neither has anything to do with Ness accepting a design.** `ness_candidate_acceptance_recorded` is not `provider_request_accepted`, is not a provider phase, and is not a provider acceptance authority. §18 makes that a must-never; §9.4 makes the distinction part of the event's meaning.

### 4.4 Why "just enable the button" is a defect and not a fix

If the button were enabled and wired to any existing route, all of the following would be true at once, and every one of them is a real problem:

- Ness would be pressing a control whose meaning is nowhere proved, bound, or written down.
- The only existing write path with an authenticated envelope is `record-ness-answer` — a **question-answer** path, keyed to `question_id` and `form_generation`, whose own UI copy says *"Your answer is preserved exactly as shown here. It does not accept or adopt the design."* (`app.js:497`). **Routing acceptance through it would make a false record of a different kind of act.** §18 forbids it.
- Nothing would prove that what Ness read still describes what exists.
- Nothing would prevent a second press, a concurrent press, or a press replayed after a crash from writing twice.
- The projected state would still say `READY_FOR_ACCEPTANCE`, so the loop would not actually be terminal — and the UI would then be tempted to store acceptance somewhere else, which is exactly the second-store prohibition of `cursorrules` §1A.

**So the deliverable is not a button. It is a proved, bound, refusable, exactly-once record — of which the button is the last and least interesting part.**

### 4.5 The delta this design introduces (design-level only)

| # | Delta | Character |
|---|---|---|
| D1 | One explanation record, in the existing journal, with eight fixed plain-language parts and a full binding, carried in **two stages** by the **existing registered event type `mechanical_change_explanation_recorded` at a new body version** (§7.2) | new body version of an existing event type — **not** a new event type |
| D2 | One controller-proved **acceptance offer** `[proposed]` — a read-only projection that is either a complete actionable offer or an explicit refusal with a reason | new logical projection |
| D3 | One new authenticated event type `ness_candidate_acceptance_recorded` — **the only one this design introduces** | new event type (**locked name**) |
| D3a | Refusal recording (per §9.2 for complete protocol), carried by the **existing registered event type `supervisor_operation_completed` at a new body version** (§19) | new body version of an existing event type — **not** a new event type |
| D4 | One new projected workflow state `ACCEPTED_FOR_DESIGN_ONLY`, terminal and non-running | new state (**locked name**) |
| D5 | One new state-projection precedence rule, placed **above** the existing PASS rule | precedence insertion |
| D6 | One logical read-only offer endpoint and one logical POST endpoint | new local HTTP surface |
| D7 | A strict `Origin` check **in addition to** the existing Host allow-list | security addition (§13.4) |
| D8 | The acceptance card gains a real, controller-driven actionable state and an accepted state | UI behaviour |

**Every one of D1–D8 is a design statement. None of it is implemented, and this file changes no code.**

**Event-type inventory delta, stated as a count (v1_1).** Installed authenticated event types: the version-4 types plus `SUPERVISOR_EVENT_TYPES` (`schema.py:119-759`). This design adds **exactly one** name to that inventory — `ness_candidate_acceptance_recorded`. D1 and D3a add **no name**: they add body **versions** of types that are already registered, through the existing `{(version, type) → key set}` table (`schema.py:778-805`). **Any later reading of this design that requires a second new event type is a misreading of it and is refused by §18 M-9a.**

---

## §5 — THE LOCKED MEANING OF THE BROWSER ACTION

### 5.1 The single sentence

> **"Accept this exact candidate for design-only status."**

That is the entire meaning. It accepts **the exact candidate** — one path, one SHA-256, one byte count — and nothing else.

### 5.2 The fixed non-authorizations, owned by the controller

The following list is **controller-owned fixed text** `[proposed: acceptance_scope_text]`. It is not model prose, not editable by any model, not generated per candidate, and not paraphrased at render time. It is a constant of the controller, identified by `acceptance_scope_id` `[proposed]` and digested as `acceptance_scope_digest` `[proposed]`, and the digest is bound into every offer and into the committed event (§8.2).

**Pressing Accept does NOT:**

1. adopt anything into `NH_MASTER-20_CORRECTED_v10.md`;
2. adopt or integrate anything into the Design and Wiring Map;
3. implement, code, build, or authorize implementation, coding, or building;
4. mark anything `PACKAGE_COMPLETE`;
5. close any open dependency, open question, or open item;
6. call any model or provider, of any kind, at any point in the request;
7. perform any Git operation — no add, commit, push, merge, reset, checkout, clean, rebase, fetch, or remote change;
8. touch production N.H, any production store, any marker, or any live N.H disk state;
9. start, unlock, schedule, or authorize the next package;
10. generate, write, copy, move, rename, promote, or project **any** Markdown file — including a closure record or acceptance receipt;
11. assign a controlled component ID, a Register ID, or a bundle placement;
12. change the accepted candidate's bytes in any way.

### 5.3 The three words that are not the same

**Acceptance ≠ closure ≠ adoption ≠ integration ≠ implementation.**

- **Acceptance** (this design): Ness says *this exact file is accepted as a design, design-only*. One journal record.
- **Closure** (`PACKAGE_COMPLETE` receipt): a separate Markdown record, created separately, later, and only if Ness separately asks for it.
- **Adoption / integration**: putting an accepted rule into the Master or the Map. Separate, later, Ness's.
- **Implementation**: actual building or coding. Separate, later, Ness's, and additionally gated by `cursorrules` §7/§8.

Each arrow between them is a **separate act with its own authorization**. This design draws exactly the first one and explicitly refuses to draw the rest.

### 5.4 Where this text must appear

The fixed non-authorization list of §5.2 is **section 8 of the eight-part explanation** (§6.2). It is not a footnote, not a tooltip, and not hidden behind an expander. The simple view shows it.

---

## §6 — THE HARD UNDERSTANDABLE ACCEPTANCE SURFACE

### 6.1 The gate rule

> **Accept is actionable only after the controller has proved that a plain, everyday-language explanation exists, is complete, and is bound to this exact candidate and this exact usable PASS.**

"Actionable" means: the controller's offer projection reports `acceptance_actionable = true` `[proposed]`. If the explanation is absent, incomplete, unbound, bound to a different candidate, bound to a different audit, bound to a different PASS, bound to a wrong predecessor, or superseded, then `acceptance_actionable = false`, **no offer identity is issued**, and the surface presents the refusal reason in plain words instead of an Accept control.

**A disabled-looking control that can still be posted is not the design.** The server refuses a POST that carries no valid current offer identity (§16.4), so tampering with the page's JavaScript changes nothing.

### 6.2 The eight parts — fixed, distinct, and all required

The explanation record carries exactly these eight parts, under exactly these titles, each **present and nonempty**:

| # | Fixed title | What it must actually say |
|---|---|---|
| 1 | **WHAT THIS PACKAGE DOES** | In everyday words, the job this package performs for N.H. Not the filename restated. |
| 2 | **WHAT ACTUALLY CHANGED** | Every material design or mechanical change carried by this exact candidate, in normal language. Material means: something a person relying on N.H would behave differently about. |
| 3 | **WHAT CHANGED FROM PREVIOUS CANDIDATE** | The difference from the **actual** predecessor candidate, named by its real path and identity. **Where there is genuinely no predecessor, it says so honestly and says why** — it does not invent one, does not silently pick the newest same-named file, and does not leave the section empty. |
| 4 | **WHAT THIS CHANGES FOR N.H IN REAL USE** | The future behaviour or protection this creates, stated as future design behaviour, with the design-versus-implementation boundary made explicit: this is a design; nothing runs until it is separately built. |
| 5 | **WHAT DID NOT CHANGE** | What is deliberately unchanged — carried rules, preserved boundaries, untouched authority. |
| 6 | **WHAT IS STILL OPEN** | What remains genuinely open, with its owner, so acceptance cannot be mistaken for completion. |
| 7 | **AUDIT RESULT** | The simple, exact result of the independent audit. Real MINOR leftovers are **disclosed**, not hidden. An IMPORTANT or CRITICAL finding means the candidate is **not ready**, and no offer exists at all (§6.5). |
| 8 | **WHAT CLICKING ACCEPT MEANS** | The fixed scope sentence of §5.1 plus the twelve fixed non-authorizations of §5.2, verbatim from the controller-owned text. |

**Rules over the eight parts:**

- All eight are **required**. A missing part is a missing explanation, not a partial one.
- All eight are **distinct**. Two identical or near-identical parts fail the structural check (§6.6).
- Each part is **nonempty** after whitespace normalization.
- Part 8 is **not model prose**. It is the controller's fixed text, bound by `acceptance_scope_digest`. A model may never write, edit, shorten, soften, or extend it.
- **Parts 1–6 are the semantically variable prose** of this explanation (§6.4), always subordinate to evidence (§6.7). They are the parts an independent audit judges for material accuracy, and they are the parts fixed before that audit runs (§6.5a, §14 Phase A).
- **Part 7 is neither free prose nor a model summary.** It is the controller's **deterministic projection of the bound audit event's own recorded fields** (§6.5a). Nobody authors it, so nobody has to judge it: it says what the bound `mechanical_audit_recorded` event already says.

### 6.3 Simple view mandatory, technical view expandable, one binding

- **The simple view is mandatory.** All eight parts are rendered in plain language, in order, before the Accept control. It is never collapsed by default, never behind a tab, and never optional.
- **The technical view is expandable**, alongside. It carries the identities, digests, byte counts, event sequence numbers, and the raw structural facts.
- **Both views are rendered from the same explanation record and carry the same `acceptance_offer_binding_sha256` `[proposed]`.** They are two presentations of one bound record, never two sources. If they could ever disagree, the offer is invalid by construction, because there is only one record and one binding digest.
- **Both remain available after acceptance** (§17.4).

### 6.4 What understanding may never be inferred from

The following are **never** accepted as a substitute for a plain-language explanation, and their presence never makes Accept actionable:

- a SHA-256, a byte count, an event sequence number, or any identity string;
- a raw diff, a changed-section list, or a patch;
- a model's own summary asserting it did the work correctly;
- a defect packet, a finding list, or a correction specification;
- a state name, a status boolean, or a projection field;
- the mere existence of a PASS.

Each of those is legitimate **technical evidence** and belongs in the technical view. **None of them is an explanation.**

### 6.5 Audit severity and readiness

Using the project's own severity vocabulary (project instructions §6; interim-package rule §5):

| Severity | Effect on the offer |
|---|---|
| **PASS** | fit for this package's current job — offer may exist |
| **MINOR** | small wording or organization issue that does not block — offer may exist, **and every real MINOR leftover is disclosed in part 7** |
| **IMPORTANT** | a real current-package problem — **not ready**; no offer; the surface says what is unresolved |
| **CRITICAL** | authority, meaning, privacy, security, safety, or data-loss problem — **always blocks**; no offer |

**A hidden MINOR is a defect of this surface, not a convenience.** Part 7 must name real leftovers plainly; the AIC closure receipt's own non-blocking wording note is the worked example of how that reads in this project.

### 6.5a Why part 7 is derived, why the sequence is finite, and why its last append is the PASS

**Three separate things have to be true, and each version so far achieved one more of them.** A sequence that satisfies this design must be **finite** — it must terminate rather than owing an endless chain of audits — it must be **durable** — every crash position inside it must leave a state whose owner exists — and it must be **coherent**: the owner that recovery actually reaches must leave records that the design's own lock-time gates accept. **v1_1 made the sequence finite and left it non-durable. v1_2 made the append order durable and left it incoherent**, because it proved its ordering with a same-operation-identity check that the only reachable recovery cannot satisfy. §6.5a below states the finiteness argument, which v1_2 and v1_3 carry forward unchanged; the durability argument v1_2 added is stated next and is also carried forward; the coherence argument v1_3 adds is stated last and is mechanized in §7.1b, §11.3 gate 11b, and §14 Phase A.

**The circularity v1_0 contained.** v1_0 required (a) that the independent audit judge the explanation's material accuracy (§6.7, §21 T-49), and (b) that the explanation bind the exact final usable audit and the PASS (§7.4, §8.2), while §14 prepared the explanation **after** the PASS. Those cannot both hold by a terminating sequence: an audit cannot judge prose that does not exist yet, and an audit of the finished explanation would itself become the newest final audit — staling the explanation under §7.7, requiring a new PASS, and requiring a further explanation binding that new audit and PASS, without end. **v1_1 removes the circularity rather than tolerating it**, by separating the two things that were fused:

| Part | Kind | Who fixes it | When | Who judges it |
|---|---|---|---|---|
| 1–6 | semantically variable prose | controller preparation, optionally model-assisted (§7.8) | **before** the final audit runs | the **one** independent semantic audit, which reads the exact fixed bytes |
| 7 | deterministic projection of the bound audit event's own recorded fields | the controller, mechanically | **after** the audit, from that audit's own record | nobody — it asserts nothing the audit event does not already record |
| 8 | controller-owned fixed text | the controller, as a constant | always | nobody — it is bound by `acceptance_scope_digest` (§5.2) |

**Part 7's derivation is DUMB.** It renders, in the fixed title's plain-language frame, only values already recorded in the bound `mechanical_audit_recorded` event — its verdict, its findings and their severities and blocking flags, and its own recorded plain-language fields. It **adds no claim**, draws no conclusion, and is not composed by any model. Its exact rendering template is `[proposed]` and is controller-owned like §5.2's text; **what is settled is that no part of it is authored per candidate.**

**The consequence that matters:** the audit judges exactly the bytes Ness is later shown for parts 1–6, and the parts it did not judge are parts nobody authored. **So no second audit is owed, and the sequence terminates.** §14 Phase A states it as a numbered sequence, and §7.7 is written so that the final explanation record cannot be staled by the audit or the PASS it binds.

**The owner of that record is A5's own operation, and this sentence is corrected here rather than left to be inferred (v1_6).** Earlier versions of this paragraph said the final explanation record was *"appended by the very operation that records the PASS."* **That is stale and is withdrawn.** It was v1_1's and v1_2's owner claim, and v1_3 replaced it for a reason that is arithmetic rather than stylistic: `_record_mechanical_pass()` builds a **fresh** `engine.Operation` on every entry (`commands.py:1444-1448`) whose identity derives over a journal tail the explanation append has already moved (`engine.py:187-205`, `:208-213`; `commands.py:94-125`), so no recovery can re-enter the operation that wrote the explanation. **The settled topology is the one §7.1b and §14 Phase A state, and it is repeated here so that no reader of this section is left holding the old one:**

> **A5 starts → exactly one final explanation append → A5 completes → ONLY THEN is A6 constructed → A6 starts → exactly one mechanical PASS append → A6 completes. A5's operation identity differs from A6's operation identity, always, on the first run and after every crash and re-entry alike.**

**Nothing else about this section changes except the post-effect unmatched-start treatment corrected in v1_11.** The finiteness argument, the derivation of part 7, the event-sequence ordering gate, and lookup-first duplicate prevention remain as stated. An A5 start followed by its one final explanation but no matching completion, or an A6 start followed by its one PASS but no matching completion, is now owned by the installed same-operation completion-recovery pattern (§7.1b, §11.3 gates 11b–11d, §14 Phase A).

**The durability property v1_2 adds, and why it needs a specific append order.** Being inside one operation is **not** the same as being one durable act. `engine.Operation` is a discipline over a sequence of separate `journal.append()` calls (`engine.py:449-458`); each call is its own two-mark, fsynced, individually durable record, and **there is no multi-record atomic commit anywhere in the installed journal.** So "the same operation appends both" says nothing at all about what a crash between the two appends leaves behind. What decides that is **which append flips the projection**, and the answer is exact:

- The installed v1_10 baseline at `status.py:1199-1204` currently reaches `READY_FOR_ACCEPTANCE` when `replay.pass_event()` is non-null. **This design requires the later implementation of this package to strengthen that projection:** the bound `mechanical_pass_recorded` is necessary but is not sufficient; replay must also prove the exact matching A6 `supervisor_operation_completed`, carrying the same `supervisor_operation_id` and the original A6 `supervisor_started_event_seq`.
- A final explanation without matching A5 completion, or a PASS without matching A6 completion, remains runnable completion-recovery work and is NOT acceptance-ready. The existing recovery/write-capable supervisor path owns that work. `READY_FOR_ACCEPTANCE`, `next_command = null`, an actionable Accept surface, and provider/Claude substantive dispatch are all prohibited until the required matching completion is durable.

**Therefore the placement rule and the completion rule operate together.** The final explanation record is appended before `mechanical_pass_recorded`, and the PASS remains A6's last substantive append; but the matching A6 completion is the append that permits `READY_FOR_ACCEPTANCE`. Every fact the offer needs, including the completed A5/A6 ownership chain, must be durable before the non-running acceptance-ready projection may appear.

**The resulting crash classification has three Phase-A positions:** before the PASS, ordinary or A5 completion-recovery work remains; after the PASS but before matching A6 completion, A6 completion-recovery work remains and no offer exists; only after matching A6 completion may `READY_FOR_ACCEPTANCE` and an actionable offer exist. §14 Phase A tabulates those positions.

**The coherence property v1_3 adds, and why the owner had to be separated to get it.** A durable order is worth nothing if the recovery that the durability argument relies on produces records the design then refuses. **That is exactly what v1_2 did**, and it did it to itself:

- v1_2 put the final-stage append and the pass append **inside one `engine.Operation`**, and then proved the ordering with a gate requiring both events to carry the **same** `supervisor_operation_id` (v1_2 §11.3 gate 11b, §21 T-13a1).
- But the recovery v1_2 leaned on — the worker re-entering the pass path — **cannot re-enter the original operation.** `_record_mechanical_pass()` builds a fresh `engine.Operation` and calls `operation.start()` on every entry (`commands.py:1444-1448`); `operation_id` is simply read off the envelope (`engine.py:405-407`); and the envelope's `supervisor_operation_id` is derived from fields that include `pre_state_sha256` (`engine.py:187-205`, `:208-213`), which `build_envelope()` computes over a projection carrying the journal's **`authenticated_event_seq` and `authenticated_tail_sha256`** (`commands.py:94-125`). **The final-explanation append moves the tail, so the re-entry derives a different operation identity by construction.**
- **So v1_2's recovery path wrote a PASS its own gate 11b would reject, permanently, from a state with `next_command = null`.** It also left the first entry's `supervisor_operation_started` unmatched.

**The v1_3 owner separation remains, and v1_11 completes its crash boundary.** The final-stage explanation belongs to A5, and the PASS belongs to distinct A6. Journal position proves explanation-before-PASS ordering. Each operation's own start/completion pair is proved separately by matching `supervisor_operation_id` and `supervisor_started_event_seq`. After a post-effect crash, recovery reconstructs the original envelope, reattaches the original authenticated start, and appends only that same operation's missing completion. This preserves one explanation, one PASS, distinct A5/A6 identities, and a record shape accepted by every readiness gate (§7.1b, §11.3 gates 11b–11d, §14 Phase A).

### 6.6 The mechanical quality check — structure only, never truth

Before an offer may exist, the controller performs a **deterministic structural check** over the explanation record:

1. exactly the eight fixed titles are present, in order, once each;
2. every part is nonempty after whitespace normalization;
3. no two parts are identical or differ only by whitespace or punctuation;
4. no part consists **solely** of identifier-like tokens — hexadecimal digests, prefixed identities, file paths, byte counts, event sequence numbers, section labels, or diff jargon. Each part must contain at least a minimum number of ordinary words outside such tokens. **The exact thresholds are `[proposed]` and remain open**; what is settled is that a part made only of IDs, hashes, or diff jargon **fails**;
5. part 8 matches the controller's fixed scope text exactly, by digest;
6. part 3 either names a real predecessor identity that the record also binds, or carries the explicit "no predecessor" statement together with the honest reason (§7.6);
7. bounded length: each part and the whole record fit within the record bounds the journal already enforces (`INTERVIEW_EVENT_MAX_BYTES`, and the segment bound — `nh_loop.py:32212-32224`). An over-bound explanation is **refused, never truncated**;
8. **content identity across the two stages (v1_1).** `explanation_content_digest` recomputes over parts 1–6 as they actually stand, and equals, byte for byte, the digest fixed at the content stage and covered by the bound audit (§7.2, §14 Phase A steps A2–A3). **Parts 1–6 that changed after the audit read them fail this check, so the explanation on offer is always the explanation that was audited**;
9. **part 7 recomputes** from the bound `mechanical_audit_recorded` event by the controller's fixed derivation (§6.5a). A part 7 that does not recompute from the bound audit event fails;
10. **the bound `pass_identity` recomputes (v1_2).** The `pass_identity` the record binds recomputes, by the installed derivation and over the installed inputs (`commands.py:1425-1441`), to exactly the value the record carries. A record whose bound PASS identity does not recompute fails.

Checks 1–7 run at the **content stage**, over parts 1–6 and 8, before the audit. **Checks 1–10 run at the final stage, and the final stage runs — and completes — before the PASS operation is constructed and before `mechanical_pass_recorded` is appended (v1_2 placement, v1_3 owner)** — so a structural failure there means the PASS event is never written, the projection never leaves the ordinary running loop, and no unowned non-running state is entered (§7.1, §7.1b, §14 Phase A). Checks 1–10 run **again** under the lock at press time (§11.3 gates 10–15). A failure at any stage means **no explanation record and no offer**, never a partial one.

**Check 10 is what makes the pre-PASS placement safe.** The record binds the PASS by an identity that is a **pure deterministic function of facts that all exist before the PASS event is written** — package scope, source binding, candidate path/digest/length, the bound `audit_identity`, the terminal chain digest, the settled-decision binding, the validation set, and the coverage-review sequence (`commands.py:1425-1441`). Nothing in it depends on the pass event's own position or digest, so binding it early is a **statement about the PASS that is either exactly right or provably wrong**, never a guess — and §11.3 gate 11 proves it against the pass event that actually landed.

**This check is DUMB.** It proves shape, binding, and byte-identity across stages. It proves **nothing** about whether the words are true.

### 6.7 The boundary this design will not cross

> **A deterministic check over prose never establishes that the prose is accurate, complete, or understood.**

- The **mechanical validation** checks structure and binding. **It also checks nothing about ordering (v1_2):** ordering is not a property of a record, it is a property of the write sequence, and it is guaranteed by §7.1's placement contract and re-proved under the lock by §11.3, never inferred from the prose. **Narrowed in v1_3:** ordering is re-proved from **journal position** — the sequence numbers of the explanation record, the pass operation's start, and the pass event — and **never from an operation identity shared between two events**, because no such shared identity survives the reachable recovery (§6.5a, §7.1b, §11.3 gate 11b).
- The **independent semantic audit** — the project's existing independent-reviewer role — judges whether the explanation is materially accurate against the actual candidate. **Corrected in v1_1:** it judges **parts 1–6, as exact fixed bytes that already exist when it runs**, together with the candidate they describe, in **one** audit — the same final usable audit the PASS then binds (§14 Phase A). It is never asked to judge prose that did not yet exist, it is never asked to judge itself, and **no audit after it is owed**, because parts 7 and 8 are derived and fixed rather than authored (§6.5a). **Unchanged in v1_2:** the audit's position in the sequence is exactly where v1_1 put it. What v1_2 moves is the *append order of the two events that follow it*, and that move gives the audit nothing further to judge. **Unchanged again in v1_3:** separating the owner of the final-stage append from the owner of the pass append moves no bytes the audit reads, adds nothing authored, and creates no audit — it changes only which operation writes an already-fixed record, and in what order the two operations run.
- **Neither** proves that Ness read it, and neither proves that Ness understood it.
- **Free prose never overrides evidence and never overrides the fixed scope of §5.2.** Where prose and evidence could be read as disagreeing, the evidence and the fixed scope govern, and the offer is refused rather than reconciled by interpretation.
- **The click proves invocation after presentation.** It proves that the Accept action was invoked while a complete, bound, current explanation was the thing on offer. It does **not** prove reading, and it does **not** prove understanding. **This design never claims otherwise, and §9.4 writes that limitation into the meaning of the record itself.**

### 6.8 Package view and version view are preserved

The existing two-level context stays exactly as it is, before and after acceptance:

- **Package view** — plain-language capability name, technical package name, framework/addition position where proved by source, purpose, bundle placement (currently the source-bound literal *"Not decided yet"*, `server.py:255-264`), controlled component ID `OPEN - NONE`, Register ID `OPEN - NONE`.
- **Version view** — candidate filename and path, SHA-256, byte count, the lifetime/batch/round-in-batch triple, the parent identity where one exists.

**Acceptance adds a third fact — "accepted for design only, on this date, for this exact identity" — and removes neither of the first two.** Bundle placement is never inferred from a filename, and no ID is invented by acceptance.

---

## §7 — THE EXPLANATION RECORD

### 7.1 What it is

Authenticated, append-only journal records `[proposed: acceptance_explanation_record]` carrying the eight parts of §6.2 plus the complete binding. They live in the **same** authenticated interview journal as every other governed event.

**It exists in two stages, and both are before the offer exists (corrected in v1_1). Both are also before the PASS event is written (corrected in v1_2), and both are appended by operations that are not the PASS operation (corrected in v1_3).**

| Stage | What it fixes | When it is appended | Who owns the append |
|---|---|---|---|
| **Content stage** `[proposed: explanation_stage = "content_fixed"]` | parts 1–6 as exact bytes, part 8 by digest, `explanation_content_digest`, the candidate binding, the predecessor binding | on the ordinary correction/preparation path, **before the final audit work item is dispatched** | the same supervisor operation that records the candidate's change explanation for that candidate (§14 Phase A step A2) |
| **Final stage** `[proposed: explanation_stage = "acceptance_offer"]` | the identical parts 1–6 by content digest, the derived part 7, part 8, **plus** the audit binding and the PASS binding by deterministic `pass_identity` (§7.4) | **on the pass path, after `pass_identity` has been derived and BEFORE the PASS operation is constructed — so strictly before `mechanical_pass_recorded` and strictly before that event's own `supervisor_operation_started`** | **its own ordinary supervisor operation** `[proposed: the explanation-assembly operation]`, built through the existing `engine.Operation` interface, which starts, appends exactly this one record, and completes (§7.1b, §14 Phase A step A5) |

#### 7.1a The ordering contract (v1_2 placement, v1_3 owner) — stated as a rule, because it is the whole correction

> **The final-stage explanation record is appended before `mechanical_pass_recorded`, by an operation that is not the PASS operation and that completes before the PASS operation is constructed; and `mechanical_pass_recorded` is the last substantive append of the PASS operation.**

**Why it had to be stated this way, and why neither v1_1's nor v1_2's version was enough.** v1_1 placed the final stage *"inside the same operation, after the pass append"* and treated that as sufficient. It is not. **`engine.Operation` provides ordering and evidence, not atomicity**: `Operation.append()` is one ordinary `journal.append()` per event (`engine.py:449-458`), each with its own intent mark, its own fsynced record, and its own committed mark. **Two appends are two durable acts with a real window between them**, and the installed journal has no way to make them one. v1_2 fixed which of the two goes last, and then **spoiled the fix by proving the order with a same-operation-identity check that its own recovery cannot satisfy** (§6.5a; `commands.py:1444-1448` builds a new operation on every entry, and `engine.py:187-205` derives its identity over a tail that the explanation append has already moved). **v1_3 keeps the placement, drops the shared-identity claim, and gives the earlier append its own operation** — so the only question that matters stays the same, and the answer stays the same:

- The installed baseline currently projects `READY_FOR_ACCEPTANCE` from `mechanical_pass_recorded` alone (`status.py:1199-1204`, over `replay.pass_event()` at `replay.py:1099-1101`). **This package's implementation contract strengthens that projection:** the exact matching A6 completion is also mandatory.
- A PASS with no matching A6 completion is completion-recovery work, not readiness. The existing recovery/write-capable path reconstructs the original A6 envelope, attaches the original authenticated start to the existing `Operation`, and appends only its missing completion. Until that completion is durably proved, no actionable offer exists and no provider or substantive dispatch may run.
- **Nothing else in the sequence moves the projection at all (v1_3).** The final-stage record's carrier, `mechanical_change_explanation_recorded`, is consulted **nowhere** in the workflow derivation `_project()` (`status.py:979-1215`); the installed readers of that type are the change feed (`feed.py:44-52`), the provider-consumption closure map (`replay.py:302-327`), the schema tables, and the in-flight closure append set (`lease.py:438-464`). **So appending it leaves the projection exactly where it was — `WORKING` / `execute-next-claude-task` — which is what keeps an owner alive across the whole window.**

**Under v1_1's order, the window between the two appends was exactly the defect the packet describes**: a death there left `READY_FOR_ACCEPTANCE` / `next_command = null`, no final explanation, and **no reachable transition able to append one**. Under the v1_2 order that window cannot exist, because everything the offer needs is already durable when the world-changing append is made. **Under v1_3 that stays true, and the records left behind are additionally ones the lock-time gates accept** (§7.1b).

**Why the reordering is possible at all — and this is a fact about the installed code, not a request for new behaviour.** `_record_mechanical_pass()` derives `pass_identity` at `commands.py:1425-1441`, **before `operation.start()` at `:1448` and before any append**. Its inputs are the package scope, the source binding, the candidate path / digest / length, the bound `audit_identity`, the terminal chain digest, the settled-decision binding, the validation set id, and the coverage-review event sequence — **all of which already exist and are already fixed at that point.** So the explanation can bind the exact PASS identity without a forward reference to an event that has not been written (§7.4). **None of those inputs is a function of the journal tail, which is why `pass_identity` is stable across a crash and re-entry even though the operation identity is not** (§7.1b).

**What is deliberately not claimed.** This design does **not** claim the appends are atomic, does **not** claim a crash cannot occur between them, does **not** claim A5 and A6 share an operation, and does **not** invent a new event type, mark, store, command, journal, recovery authority, or two-phase commit. It consumes the installed same-operation reattachment pattern: `reconstruct_original_envelope(...)`, `Operation(...)`, `operation.started_event = original_start`, then `operation.complete(...)`. No substantive append is repeated. A completion-recovery command may run while the projection is not ready; `next_command = null` and the read-only actionable offer appear only after the matching A6 completion is durable.

**The click never creates either record, never edits either, and never triggers their creation.**

#### 7.1b The owner contract (v1_3) — who appends the final stage, and why it cannot be the PASS operation

> **The final-stage explanation record is appended by its own supervisor operation, which starts, appends exactly that one record, and completes — all while the projection is `WORKING` / `execute-next-claude-task`, and all before the PASS operation is constructed.**

**Why the PASS operation cannot own it, stated as arithmetic rather than as a preference.** v1_2 required the two events to share a `supervisor_operation_id`. That requirement fails twice over, and both failures are readable straight off the installed files.

**First failure — the field is not there to compare.** Neither of the two events v1_2's gate compared carries a `supervisor_operation_id` at all. The installed body key sets are explicit: `mechanical_pass_recorded` is `PACKAGE_SOURCE ∪ CANDIDATE ∪ {pass_identity, audit_identity, terminal_chain_sha256, settled_decision_binding_sha256, validation_set_id, coverage_review_event_seq, the six gate booleans, pass_outcome}` (`schema.py:705-723`), and `mechanical_change_explanation_recorded` is `PACKAGE_SOURCE ∪ CANDIDATE ∪ {parent triple, change_explanation_identity, blocking_finding_refs, correction_specification_sha256, diff_sha256, reviewer_result_sha256, source_paths_checked, plain_language_change, plain_language_real_use_effect, meaning_or_policy_changed, changed_sections, technical_summary, work_item_identity, provider_kind, provider_request_identity, result_custody_identity, provider_terminal_event_seq}` (`schema.py:680-704`). `Operation.append()` adds the type, the package/source standing, and the candidate body — **and no operation id** (`engine.py:449-458`). Only `supervisor_operation_started` and `supervisor_operation_completed` carry that field. **v1_2's gate 11b named a comparison that cannot be evaluated against the installed schema.**

**Second failure — even if the field existed, the values would differ.** The chain is short enough to check end to end:

| Step | Installed fact | Where |
|---|---|---|
| 1 | On an ordinary first entry, `_record_mechanical_pass()` builds a new `engine.Operation` and calls `operation.start()` (`commands.py:1444-1448`). On recovery from an authenticated A6 start followed by its one PASS and no matching completion, a fresh start is forbidden: the installed recovery pattern reconstructs the original envelope, builds `Operation(...)`, assigns `operation.started_event = original_start`, and calls only `operation.complete(...)` | `commands.py:1444-1448`; existing same-operation reattachment pattern in `commands.py` |
| 2 | `Operation.operation_id` is read straight off the envelope; the object carries no identity of its own | `engine.py:405-407` |
| 3 | The envelope's `supervisor_operation_id` is **derived** from thirteen envelope fields, one of which is `pre_state_sha256` | `engine.py:187-205`, `:208-213` |
| 4 | `build_envelope()` computes `pre_state_sha256` as `state_binding_digest()` over a projection that includes **`authenticated_event_seq` and `authenticated_tail_sha256`** | `commands.py:94-125` |
| 5 | The final-stage append **moves the tail** | by definition of an append-only chained journal |
| ⇒ | A fresh substantive re-entry would derive a different `supervisor_operation_id`; therefore it is forbidden after the original operation's substantive event is already durable. Same-operation completion recovery instead preserves the original A5 or A6 `supervisor_operation_id` and original `supervisor_started_event_seq`. A5 and A6 remain distinct from each other. | steps 1–5 and the installed reattachment pattern |

**So the same-operation gate was not merely fragile — it was unreadable, and it was false in precisely the position it was written to protect.** A PASS written by that recovery would be refused at lock time forever, from a state with `next_command = null`. **That is the packet's own unreachable-offer defect, re-created by the check meant to prevent it.**

**The right conclusion is not a better operation-identity check — it is that write order does not live in a record field at all.** Order lives in the append-only authenticated chain, and the chain already records it exactly: an event's `event_seq` **is** the statement that it was durable before every higher-numbered event. **v1_3 proves the ordering from that, and from nothing else** (§11.3 gate 11b). The distinctness of the two operations is a **write-order contract of this design**, discharged by the offline sequence and crash tests of §21 — **it is deliberately not asserted as a lock-time record check, because the installed records cannot witness it, and a gate must never claim to check what it cannot read.**

**What v1_3 requires instead, and what it does not require.**

- **Settled:** the final-stage record is appended by an ordinary supervisor operation on the existing `execute-next-claude-task` path, through the **existing** `engine.Operation.start()` / `.append()` / `.complete()` interface (`engine.py:421-490`). **No new command, no new dispatch path, no new event type, no new mark, and no new recovery mechanism.** The carrier type is already a member of the installed in-flight closure append set (`lease.py:438-464`), so no new append gate is needed to write it inside the loop's own working window.
- **Settled:** it **completes before the PASS operation is constructed**, so the PASS operation's envelope — and therefore its `supervisor_operation_id` and its `supervisor_operation_started` — is built over a journal in which the explanation record is **already durable**.
- **Settled:** the two operations are therefore **always distinct**, on the first run and after every crash position alike, and **no gate anywhere in this design asserts otherwise.**
- **Open, and marked so:** the explanation-assembly operation's exact envelope fields, work-item binding, and outcome string are `[proposed]` and are settled at implementation time (§20, §22.3 items 2 and 11). What is **not** open is its position, its single append, and the fact that it closes before the PASS operation opens.

**Why recovery is an owner instead of an assertion.** Lookup-first first locates the exact authenticated original start and its substantive event. Recovery then proves the original `pre_state_sha256`, `input_envelope_sha256`, `supervisor_operation_id`, command, work item, package, source and candidate bindings from the authenticated prefix. It reconstructs that original envelope through `reconstruct_original_envelope(...)`, constructs the existing `Operation(...)`, assigns `operation.started_event = original_start`, and invokes only `operation.complete(...)`.

For A5, recovery is permitted only when exactly one final explanation follows that A5 start, zero matching A5 completions exist, no second explanation exists, and no PASS exists. For A6, it is permitted only after the completed A5 chain is proved and when exactly one PASS follows that A6 start, zero matching A6 completions exist, and no second PASS exists. A matching completion that already exists is returned with zero append. Duplicate or mismatched starts, completions, commands, work items or bindings fail closed. Unproved completion truth also fails closed; it never causes another completion or substantive append.

The explanation and PASS remain located and de-duplicated by their settled bindings. Journal `event_seq` proves their order. The recovered completion preserves the original operation's `supervisor_operation_id` and `supervisor_started_event_seq`. A crash before the completion append lands leaves the same unmatched start and repeats only this proof; one complete authenticated completion lands at most once.

**The honest cost of the separation remains two distinct operation pairs.** v1_11 adds no third operation and no new event type. It requires an interrupted post-effect A5 or A6 operation to receive its own missing matching completion instead of being abandoned or replaced.

**This does not collide with §0B's one-operation-one-log rule, and the distinction is not a quibble.** That rule governs **the press** — one acceptance action, one permanent record, no record about a record (§18 M-35, §19). **Phase A contains no press.** A5 and A6 are two ordinary supervisor operations of the mechanical loop, each doing a distinct piece of work and each recording its own start and completion — which is what §0B asks of them, not something it forbids. **Nothing here creates a second record of one act**: the final-stage explanation record is appended exactly once, by exactly one operation, and the PASS exactly once by exactly one other.

### 7.2 Carrier: an existing registered type at a new body version, and the one-new-name rule

`ness_candidate_acceptance_recorded` is the **one and only new authenticated event type** this design introduces. **v1_0 broke that rule**: §7.2 required the explanation to be an authenticated journal event with its own `[proposed]` event-type label and its own per-`(version, type)` schema, which is a second newly designed authenticated event type however it is spelled. v1_1 removes it.

**The carrier is the existing registered event type `mechanical_change_explanation_recorded`** (`schema.py:680-704`), carried at a **new body version** through the mechanism the installed schema already provides: body keys are a `{(version, type) → key set}` table, built so that the same type name legitimately carries different key sets at different versions (`schema.py:778-805`). **A new body version of a registered type is not a new event type**, adds no name to the inventory, and needs no second store, no second schema mechanism, and no second append path.

What is **settled**:

- it is carried by the **existing** authenticated journal — **no second journal, no second store, no sidecar file, no database, no cache-as-authority**;
- it is carried by an **existing registered event type name**; the design introduces **no** second event type, named or unnamed;
- it is validated by the **existing** per-`(version, type)` body-key mechanism (`schema.py:778-805`; `journal.py:86-138`), at the new version row;
- it carries an explicit **stage/kind discriminator** `[proposed: explanation_stage]` whose values distinguish the correction-stage record, the content-stage record, and the final-stage record. **The discriminator is required, not optional**: without it the two kinds would be indistinguishable, which is the reinterpretation §7.3 forbids;
- the existing feed derivation indexes these records by `candidate_sha256` alone (`feed.py:44-52`). **The acceptance-stage records must be excluded from that index by their discriminator**, so an acceptance-stage record can never be substituted for the correction-stage record the feed means, and vice versa;
- it is **appended before** enablement, by the controller, on the mechanical path, in the two stages of §7.1;
- **exactly one** event is appended by a successful click, and that one event is the acceptance event — never an explanation record (§9.2).

**Three registered types therefore gain a new body version, and none gains a new name:** `mechanical_change_explanation_recorded` for the explanation's two stages; `mechanical_audit_recorded` for the `explanation_content_digest` the audit covered (§14 Phase A step A3); and `supervisor_operation_completed` for the refusal record (§19). **The added-name count of this design stays one** (§18 M-9a).

The **new body version number**, the discriminator's exact spelling, and the exact added key lists are `[proposed]` and remain open (§22.3 item 3).

### 7.3 It is the same carrier type, and never the same record

The correction-stage `mechanical_change_explanation_recorded` record already exists at the installed version and carries `plain_language_change`, `plain_language_real_use_effect`, `meaning_or_policy_changed`, `changed_sections`, `technical_summary`, bound to a parent/candidate pair.

That record is **per correction**: it explains one change from one parent to one child. **The acceptance explanation is per acceptance offer**: it explains the whole candidate as it now stands, in eight fixed parts, including the audit result and the fixed acceptance scope.

**Sharing a carrier type is not sharing a record, and v1_1 keeps every separation v1_0 required:**

- the two are distinguished **mechanically**, by the required `explanation_stage` discriminator and by the version row's key set — never by inference, filename, ordering, or resemblance;
- the correction-stage record may be **read as input evidence** when preparing the acceptance explanation;
- it may **never be reused, reinterpreted, promoted, or displayed as** the acceptance explanation, and no acceptance-stage record may ever be read as a correction-stage record;
- the acceptance offer **never** derives from it alone, and its `meaning_or_policy_changed` value never substitutes for part 5;
- an offer computed over a record whose discriminator is not the final acceptance stage is **refused, not adapted** (§15 F-10).

### 7.4 Content contract

| Element | Content |
|---|---|
| Element | Content stage | Final stage |
|---|---|---|
| `explanation_stage` `[proposed]` | `content_fixed` — **required discriminator** (§7.2) | `acceptance_offer` — **required discriminator** |
| `explanation_record_identity` `[proposed]` | deterministic derived identity (§8.4) | deterministic derived identity (§8.4) |
| `explanation_version` `[proposed]` | monotonically increasing integer within the bound scope; version 1 is the first | same numbering, same scope |
| `explanation_content_digest` `[proposed]` | digest over the canonical form of **parts 1–6 exactly as fixed** | **must equal** the content stage's value, byte for byte |
| `explanation_digest` `[proposed]` | digest over the canonical form of parts 1–6 and 8 plus the stage's binding | digest over the canonical form of all eight parts plus the full binding |
| the parts | parts 1–6 and part 8, each nonempty | all eight parts, each nonempty; part 7 derived (§6.5a) |
| candidate binding | `candidate_path`, `candidate_sha256`, `candidate_bytes` | identical values, re-proved |
| package/source binding | `package_key`, `package_scope_id`, `package_id`, `branch`, `head_sha`, `source_binding_sha256` | identical values, re-proved |
| audit binding | **explicit null** — the final usable audit does not exist yet, and none is invented | `audit_identity`, plus the audit event's `event_seq` and `event_sha256` — a **backward** reference to an event that already exists |
| PASS binding | **explicit null** — the PASS does not exist yet | `pass_identity` — **the deterministic identity, and only that (corrected in v1_2)**. **No `event_seq` and no `event_sha256`**: the `mechanical_pass_recorded` event is appended after this record, so no honest value for either exists here, and none is invented (§7.4a). **No operation identity either (v1_3)**: the carrier's installed body key set carries no `supervisor_operation_id` (`schema.py:680-704`), this design adds none, and no gate compares one (§7.1b, §11.3 gates 11b–11c) |
| content-stage back-reference `[proposed]` | not applicable | the content-stage record's `explanation_record_identity`, `event_seq` and `event_sha256` |
| predecessor binding | §7.6 | §7.6, re-proved |
| scope binding | `acceptance_scope_id`, `acceptance_scope_digest` | `acceptance_scope_id`, `acceptance_scope_digest` |
| supersession | `supersedes_explanation_identity` `[proposed]`, or explicit null | `supersedes_explanation_identity` `[proposed]`, or explicit null |
| preparation provenance | `preparation_kind` `[proposed]` ∈ {`controller_composed`, `model_assisted_controller_validated`}, plus, where model assistance was used, the identities of the work item / request / result custody that produced the draft | carried forward from the content stage unchanged; the final stage authors no prose and so introduces no new preparation provenance |

**The null audit and PASS bindings at the content stage are positive statements, not omissions.** They say: *this prose was fixed before any audit or PASS existed, and nothing is claimed about either.* A content-stage record that carries a non-null audit or PASS binding is a contradiction and fails closed. **No offer is ever computed from a content-stage record** (§7.3, §15 F-10).

#### 7.4a No forward event references, and why the exact PASS binding is not weakened (v1_2)

**A record may only bind an event that already exists when it is written.** v1_1's final stage carried the pass event's `event_seq` and `event_sha256`, which is only writable if the record is appended after the pass event — the very order that produced the crash window of §7.1a. **v1_2 removes the forward reference rather than the ordering fix**, and the required binding survives intact:

| What the packet requires the explanation to bind | Where it is bound in v1_2 | Is it exact? |
|---|---|---|
| the **exact final usable audit identity** | `audit_identity` + the audit event's `event_seq` and `event_sha256`, in the record itself | **Yes**, and unchanged from v1_1 — the audit already exists when the record is written |
| the **exact mechanical PASS identity** | `pass_identity`, in the record itself | **Yes.** `pass_identity` **is** the PASS's identity — it is what the installed pass path derives and what the pass event itself carries as its `pass_identity` field (`commands.py:1425-1441`, `:1449-1459`) |

**`pass_identity` is not a weaker binding than the event position — it is a stronger one.** It is a digest over the package scope, source binding, candidate path / digest / length, `audit_identity`, terminal chain digest, settled-decision binding, validation set, and coverage-review sequence. **Any change to any of those produces a different `pass_identity`**, so a record bound to one PASS can never be silently read against another. An `event_seq` is a position; `pass_identity` is a statement of what the PASS is *about*.

**What the record does not carry is proved elsewhere, not dropped.** The `mechanical_pass_recorded` event's own sequence and digest are:

- **re-proved under the lock** at §11.3 gate 11, which locates the pass event **by the bound `pass_identity`**, requires exactly one such event, and requires it to be the current pass event for this candidate;
- **carried in the acceptance event** (§8.2, §9.3), which is appended at click time when the pass event certainly exists and its position is certainly known;
- **published in the offer** (§16.2), which reads them from the journal at offer time rather than from the explanation record.

**So nothing that was proved in v1_1 is unproved in v1_2. What changed is which record carries the proof, and when.** A final-stage record that carries a pass `event_seq` or `event_sha256` is a **contradiction of the ordering contract** and fails closed exactly as a content-stage record with a non-null PASS binding does: it could only have been written after the pass event, which §7.1a forbids.

**And nothing that was proved in v1_2 is unproved in v1_3 (v1_3).** v1_3 removes exactly one v1_2 clause — the requirement that the explanation record and the pass event share a `supervisor_operation_id` — and it removes it because **the installed records carry no such field and the reachable recovery would not preserve its value if they did** (§7.1b). What that clause was reaching for was *"the explanation was durable before the PASS"*, and that is proved directly, from the one place write order actually lives: **the authenticated chain's own sequence numbers** (§11.3 gate 11b). Nothing about the exactness of the candidate, audit, `pass_identity`, predecessor, source, or scope binding is touched, and no binding is loosened.

### 7.5 Append-only lifecycle and supersession

1. **Append-only.** An explanation record is never edited, never rewritten, and never deleted. This is the same discipline the journal already enforces (`nh_loop.py:32543-32548` refuses any change to an earlier record).
2. **Supersession, not mutation.** A corrected or improved explanation is a **new** record at `explanation_version + 1`, naming its predecessor in `supersedes_explanation_identity`.
3. **Exactly one current explanation.** For one `{package_scope_id, candidate_sha256, audit_identity, pass_identity}` the current explanation is the highest-version record that binds all four **and** is not itself superseded. Two unsuperseded records at the same version for the same binding are a **contradiction ⇒ fail closed** (§15 row F-14). The newer one is never silently preferred.
4. **Superseded explanations remain history.** They stay readable, stay in the chain, and are never presented as current.
5. **A committed acceptance freezes nothing retroactively.** It binds the exact explanation identity, version, and digest that were on offer at the moment of the press, so a later superseding explanation can never change what Ness was shown.

### 7.6 Actual-predecessor binding, and honest absence

Part 3 must describe the difference from the **actual** predecessor. Therefore:

- The predecessor is the candidate the current candidate was actually derived from — the parent identity the controller already carries on the correction path (`parent_candidate_path`, `parent_candidate_sha256`, `parent_candidate_bytes` in `mechanical_change_explanation_recorded`), or the source identity a declared-stranded candidate was adopted against.
- A predecessor is **never** guessed from a filename, a version number, a directory listing, a modification time, or name similarity.
- The predecessor's identity is bound into the explanation record and re-proved at lock time (§11.3 step 12).
- **Where there is genuinely no predecessor** — a first candidate of a package — part 3 says so plainly, states the reason, and the record carries `predecessor_state = "none_stated"` `[proposed]` with null predecessor identity fields. **This is a positive statement, not an omission**, and the structural check requires it (§6.6 rule 6).
- **A wrong predecessor is a refusal, not a warning.** If the bound predecessor identity does not match the controller's own current parent evidence, `acceptance_actionable = false` and the press is refused (§15 row F-11).

### 7.7 Staleness

An explanation becomes **STALE**, and the offer is withdrawn or the press refused, when **any** bound element differs from what the controller re-proves:

| Bound element | Stale when |
|---|---|
| candidate | a newer candidate exists in scope, or the file on disk no longer recomputes to the bound path/SHA/bytes |
| audit | a newer audit exists for the candidate, the bound audit is not the exact final usable one, or a conflicting audit exists |
| PASS | **no** `mechanical_pass_recorded` carrying the bound `pass_identity` exists; or more than one does; or the current pass event for this candidate is not that one; or a later pass event exists; or the bound `pass_identity` no longer recomputes from the controller's own current inputs (§6.6 check 10) |
| source | `branch`, `head_sha`, or `source_binding_sha256` differ |
| settled decisions | `settled_decision_binding_sha256` differs |
| predecessor | the bound predecessor is not the controller's current parent evidence |
| scope text | `acceptance_scope_digest` differs from the controller's fixed text digest |
| explanation | a superseding explanation exists, or the record's own digest does not recompute, or `explanation_content_digest` no longer equals the content-stage value the bound audit read |
| journal position — **the complete authenticated head, not a summary of it (rewritten in v1_6)** | the authenticated event tail differs, **or any one of the eight authenticated head fields differs** — `v`, `intent_generation`, `intent_number`, `intent_event_seq`, `intent_event_sha256`, `committed_event_seq`, `committed_event_sha256`, `head_auth_sha256` — **or the canonical complete-head digest over exactly that eight-field object differs** (§8.2, §8.3, §11.4). **Every field is compared; none is treated as a summary of the others.** In particular a **K-2 intent-only change** — an intent mark advanced with no record bytes landed — moves `intent_generation`, `intent_number`, `intent_event_seq`, `intent_event_sha256` and `head_auth_sha256` while leaving the event tail and **both** committed fields untouched (§12.3 K-2). **That is a real change to the world the offer was computed over, so it stales the offer**, and v1_4's tail-and-high-water row could not see it |

**Any bound change ⇒ STALE ⇒ the control is not offered, and a posted press is refused with zero acceptance appends and one operational refusal record (§19).** Recovery is always the same and always safe: reload, read the fresh explanation, and press again if Ness still wishes to.

**What staleness may never mean (corrected in v1_1, restated for the v1_2 order, and for the v1_3 owner).** The audit and PASS rows above are tests against **later** events, and they are written so that the sequence of §14 Phase A cannot stale its own output:

- The final explanation record binds the audit `A`, which **already exists** when the record is appended, and the pass identity `p`, which has **already been derived** from `A` and the fixed candidate at that moment (§7.1a). So on arrival `A` is the exact final usable audit, and `p` is the identity of the only PASS the sequence will write: **neither row can be true of it on arrival.**
- **No audit of the final explanation record is owed or performed**, because the semantically variable content it carries is the exact content `A` already read (§6.5a, check 8 of §6.6). **A later audit is therefore never created merely by having produced an explanation**, and the endless "audit ⇒ new audit is now the final one ⇒ new PASS ⇒ new explanation" regress of v1_0 cannot start.
- **The PASS this sequence writes is the PASS the record already binds, so it does not stale it (v1_2).** `mechanical_pass_recorded` carries exactly `pass_identity = p`. The PASS row asks whether the pass event carrying `p` exists and is current; that append is what **makes** it true, not what falsifies it. **The append that follows the record is the append the record was waiting for.**
- **The events that separate them are not staleness rows either (v1_3).** Between the final-stage record and the pass event lie the explanation operation's own `supervisor_operation_completed` and the PASS operation's own `supervisor_operation_started`. Both are ordinary journal movement: they are **not** a newer candidate, a newer audit, a newer or conflicting PASS, a superseding explanation, a changed source or settled-decision binding, or a changed predecessor — **they match no row of the table above.** They move the tail, which is exactly what the journal-position row is for, and that row only ever governs an offer already rendered (§11.4); **no offer can exist in that interval at all**, because no pass event does.
- **The interval before the pass append is not a stale offer — it is no offer at all.** In that interval no `mechanical_pass_recorded` exists, so `replay.pass_event()` is null, so the projection is **not** `READY_FOR_ACCEPTANCE` (`status.py:1199-1204`) and §11.3 gate 4 and §15 F-4 refuse. **A final-stage record with no matching pass event is never offered, never presented, and never pressable** — it is simply a durable fact waiting for the append that completes it (§14 Phase A crash rows P-2 through P-3c).
- The matching A5 and A6 completion events are not newer audits, newer PASSes, or superseding explanations. They are required ownership evidence. Missing A5 completion withholds A6; missing A6 completion withholds `READY_FOR_ACCEPTANCE` and the actionable offer. Completion recovery moves the journal tail before any offer exists, so no previously valid offer is being preserved across that movement. Only after the complete A5/A6 chain is durable may the offer be computed (§11.3 gate 11d, §14 Phase A).

### 7.8 Model assistance is preparation only

- **Parts 1–6** — and only parts 1–6 — **may** later be prepared with model assistance. That is a **pre-acceptance preparation activity** on the ordinary mechanical path, and it happens at the **content stage**, before the final audit runs (§7.1, §14 Phase A step A2).
- **This design chooses no provider and no model** for that, and names none.
- Model assistance carries **no authority**: the controller validates structure and binding, the independent audit judges accuracy **against the exact fixed bytes**, and the record's `preparation_kind` states honestly how it was produced.
- **Part 7 is never model-produced** (corrected in v1_1). It is derived by the controller from the bound audit event's own recorded fields (§6.5a). A model may not compose it, summarize into it, soften it, or select which findings it names.
- **Part 8 is never model-produced.**
- **Nothing is prepared, drafted, or composed after the audit — and nothing at all is prepared after the PASS (v1_2).** The final stage assembles already-fixed bytes and already-recorded facts; it authors nothing, so it needs no model and no provider. **That is what makes it cheap enough and deterministic enough to run as one bounded supervisor operation on the pass path, before the PASS operation is constructed** (§7.1a, §7.1b). It is a fixed-cost assembly of things that already exist — not a preparation step, not a drafting step, and not a step whose duration depends on anything outside the journal.
- **Giving it its own operation does not make it a preparation step (v1_3).** It authors nothing either way; what changed is only which operation performs the append and in what order the two operations run. **The prohibition stands unchanged and unweakened: no provider call, no subprocess, no network wait, and no model of any kind may enter the final stage**, whichever operation owns it (§22.3 item 7).
- **The order matters here too, and it is the safe order.** Because the final stage is written **before** the pass event, a failure in it means the PASS is never recorded and the loop simply stays where it was. **The failure mode of the assembly step is "no PASS yet", never "READY_FOR_ACCEPTANCE with nothing to show".**
- **The HTTP click calls no model.** Not to compose, not to summarize, not to check, not to translate, not to classify. The acceptance request path contains **zero** provider calls and **zero** subprocess model invocations (§18 M-6, §21 T-27).
- If a safe explanation cannot be produced, the surface displays the verified technical facts, says plainly that a plain explanation is not currently available, and **offers no Accept control**. It never invents one. This mirrors the existing controller-owned fallback discipline (`constants.py:708-720`).

---

## §8 — BINDINGS AND DETERMINISTIC IDENTITIES

### 8.1 The derivation method (reused, not reinvented)

The existing method is used exactly as it stands: `digest = SHA256(canonical_json([DOMAIN_LABEL, EXACT_INPUT_OBJECT]))`, with canonical JSON meaning sorted keys, `(',', ':')` separators, `ensure_ascii=True`; inputs are an **exact** key set — missing or extra keys raise rather than silently derive; an optional ASCII family prefix is applied (`identity.py:718-728`; `canonical.py:28-45`; `constants.py:676-689`).

**No new hashing scheme, canonicalization, or identity algebra is invented.**

### 8.2 The acceptance binding set (minimum)

Every offer, and the committed event, binds at least:

| Group | Elements |
|---|---|
| **Package scope** | `package_key`, `package_scope_id`, `package_id` |
| **Source** | `branch`, `head_sha`, `source_binding_sha256`, `settled_decision_binding_sha256` |
| **Candidate** | `candidate_path`, `candidate_sha256`, `candidate_bytes` — **recomputed from the file on disk under the lock**, never carried forward from a report |
| **Audit** | `audit_identity`, audit `event_seq`, audit `event_sha256` — the exact final **usable** audit |
| **PASS** | `pass_identity`, pass `event_seq`, pass `event_sha256` — the exact `mechanical_pass_recorded` |
| **Explanation** | `explanation_record_identity`, `explanation_version`, `explanation_digest`, explanation `event_seq`, explanation `event_sha256` |
| **Predecessor** | `predecessor_candidate_path/sha256/bytes`, or `predecessor_state = "none_stated"` with nulls |
| **Scope** | `acceptance_scope_id`, `acceptance_scope_digest` |
| **Journal position — the authenticated event tail** | pre-click `authenticated_event_seq`, `authenticated_tail_sha256` |
| **Journal position — the COMPLETE authenticated head (rewritten in v1_6)** | **the exact eight-field authenticated head object as installed, every field, none omitted and none summarized**: `v`, `intent_generation`, `intent_number`, `intent_event_seq`, `intent_event_sha256`, `committed_event_seq`, `committed_event_sha256`, `head_auth_sha256` — **plus `pre_click_head_digest_sha256`** `[proposed]`, the canonical complete-head digest of §8.3a over exactly that object |
| **Controller** | `controller_executable_identity`, `terminal_chain_sha256` |
| **The act** | `ness_browser_action = true`, `acceptance_action_channel = "local_browser_post"` `[proposed]` |

**Why the whole head and not a summary of it (v1_6).** v1_4 bound the authenticated tail and the two committed fields, and called that "the journal position". **It is not the journal position; it is part of it.** The installed head carries eight fields and its own rule relates them — `intent ∈ {committed, committed + 1}` (`nh_loop.py:31241-31302`) — so a head can move in ways that leave every value v1_4 bound completely unchanged. The plain case is **K-2**: an intent mark advanced with no record bytes landed moves `intent_generation`, `intent_number`, `intent_event_seq`, `intent_event_sha256` and `head_auth_sha256`, and moves **neither** committed field and **not** the event tail (§12.3 K-2). **A world in which another writer has declared an append is not the world the offer was computed over**, and v1_4's binding could not tell the difference. Binding the exact eight-field object closes that, and it closes it by **reading more of a structure that already exists** — not by adding a field to the head, a second head, a second mark, or a new authentication.

### 8.3 The offer binding digest

`acceptance_offer_binding_sha256` `[proposed]` = digest over the canonical form of **the whole binding set of §8.2**, including the explanation identity/digest, the authenticated event tail, **the exact eight authenticated head fields, and `pre_click_head_digest_sha256`**.

- It is issued with the offer.
- It is echoed verbatim by the POST, **together with `pre_click_head_digest_sha256`** (§16.3).
- It is **recomputed by the controller under the lock** from the then-current world. **Any difference ⇒ STALE ⇒ refusal with zero acceptance appends** (and the one operational refusal record of §19, subject to §15's stated exceptions).

### 8.3a The canonical complete-head binding digest (v1_6)

`pre_click_head_digest_sha256` `[proposed]` is **one** digest over **one** exact object, derived by **the existing method of §8.1 and no other** — `SHA256(canonical_json([DOMAIN_LABEL, EXACT_INPUT_OBJECT]))`, sorted keys, `(',', ':')` separators, `ensure_ascii=True`, an **exact** key set that raises on a missing or extra key (`identity.py:718-728`; `canonical.py:28-45`).

The exact input object is the authenticated head as it actually is, and **exactly these eight keys, no more and no fewer**:

```
v
intent_generation
intent_number
intent_event_seq
intent_event_sha256
committed_event_seq
committed_event_sha256
head_auth_sha256
```

What is settled about it:

- **It is a digest over the head, not a replacement for the head.** The head remains the installed head, authenticated by the installed `head_auth_sha256` in the installed way. **No new head, no ninth field, no second mark, no second authentication, and no new canonicalization or identity algebra is introduced** (§8.1, §9.6, §18 M-9, M-10).
- **It is a convenience for exact comparison, never a substitute for one.** The lock-time proof compares **every one of the eight fields individually** *and* the digest (§11.3 gates 2a–2b). A matching digest never excuses an unmatched field, and an unmatched field is refused whatever the digest says.
- **It is included in the offer binding of §8.3**, published in the offer (§16.2), echoed by the POST (§16.3), recorded in the acceptance event (§9.3), and recomputed under the lock (§11.3).
- **It is never client authority.** Neither the eight fields nor this digest is believed because the browser sent them back; they are proved by the controller, under the lock, against the head as it then is (§13.3, §11.2).
- **The domain label and the exact field spellings are `[proposed]`** and settle at implementation time with §22.3 item 2. **What is not open is which eight fields are covered, that all eight are, and that the comparison is exact.**

**And this changes nothing about `ness_acceptance_identity`.** The complete head is a **binding** and a **staleness** fact, not an identity input. **Journal position stays excluded from the deterministic acceptance identity exactly as §8.4 settles it**, because a retry of the same act must derive the same identity even though the head has moved. **Binding more, and identifying by less, is the whole point of the separation** (§8.4).

### 8.4 The two derived identities

**Explanation identity** `[proposed]` — domain label `[proposed]`, inputs: `package_scope_id`, `source_binding_sha256`, `candidate_path`, `candidate_sha256`, `candidate_bytes`, `audit_identity`, `pass_identity`, `explanation_version`, `explanation_digest`.

**Acceptance identity** `[proposed: ness_acceptance_identity]`, family prefix `[proposed: acc_]` — domain label `[proposed]`, inputs **exactly**:

```
package_scope_id
source_binding_sha256
candidate_path
candidate_sha256
candidate_bytes
audit_identity
pass_identity
acceptance_scope_id
```

**Why exactly those, and why not more:**

- It must be **the same value for the same act**, so that a lost response, a reload, or a retry resolves to the existing record instead of writing a second one.
- Therefore it **excludes** every value that can legitimately move between two attempts at the same act: the journal tail and high-water numbers, any sequence number, any request or session identifier, any dispatch serial, any occurrence ordinal, and any clock reading. This mirrors the existing exclusion discipline (`identity.py:742-758`).
- It also **excludes** `explanation_record_identity` and `explanation_version`. If a superseding explanation were minted between two presses of the *same* act, including it would produce a *different* identity and would permit a **second acceptance of the same candidate** — the precise duplicate this design exists to prevent. The explanation is therefore **bound and recorded in full**, and is **additionally protected** by the stale rule (§7.7) and the conflict rule (§12.4), but it does not enter the identity.
- Conversely, **a different candidate, audit, pass, package scope, source binding, or scope text yields a different identity**, so a different act can never be absorbed into an existing record.

### 8.5 Identity ≠ authority

Deriving an identity proves nothing about correctness. An identity is a name. Every gate in §11.3 is a separate proof, and none of them is satisfied by the existence of a well-formed identity.

---

## §9 — THE ONE NEW EVENT TYPE: `ness_candidate_acceptance_recorded`

### 9.1 What it is

One authenticated, append-only record in the existing interview journal, appended **exactly once** by a successful explicit Ness browser action.

**It is the only new authenticated event type this design introduces.** Everything else this design records travels on an **already registered** type at a new body version: the explanation on `mechanical_change_explanation_recorded` (§7.2), the refusal record on `supervisor_operation_completed` (§19). Compared with the installed inventory (`schema.py:119-759` plus the version-4 types), the added-name count of this design is **one**.

### 9.2 Exactly one append on success, exactly one on refusal, never both

| Outcome of one request to the acceptance-record operation | Acceptance events appended | Other events appended | Total appends | Does the journal/head move? |
|---|---|---|---|---|
| **Success** | exactly 1 — `ness_candidate_acceptance_recorded` | **0** | **1** | **Yes** — one authenticated append, and the head advances with it |
| **Case B — any refusal or failure**, of every class in §15 — **including a request-level refusal, and including a wrong-method GET/HEAD mutation attempt (F-29)** — **where the existing journal and lock can safely be appended to** | **0** | exactly 1 — the operational refusal record of §19 | **1** | **Yes, and this is stated rather than glossed (v1_6).** The refusal record is a real authenticated append: **it mutates the journal and it moves the head.** What it never mutates is **acceptance state** |
| **Case C — the same request, where the existing journal or lock cannot safely be appended to** | **0** | **0** | **0** | **No.** The refusal is reported in plain words, **nothing is appended**, and **success is never claimed** (§15 F-35, §19, §21 T-45a) |
| **Neither success nor refusal — a live post-write acceptance whose truth is unresolved (v1_6)** | **0 further** — the acceptance event that may already be durable is **not** appended again | **0** — **no refusal record is written** | **0 further** | **Nothing further is written.** The existing record, if any, is preserved exactly (§11.1, §12.3 K-8, §15 F-36) |

**The unit of this table is one request directed at the acceptance-record operation, not one press (stated in v1_4).** A refused request need not have been a press to be a real refused operation: a wrong-method GET or HEAD aimed at the record route never becomes a press, and is counted on the Case B / Case C rows exactly like every other refusal class.

**Case A — a legitimate read of the offer endpoint — is not a row of this table at all.** It is the read-only projection of §16.2 and Phase B of §14. It is refused nothing, and it appends nothing however many times it is read (§19, §21 T-46b). **Corrected in v1_6:** that read does **take the existing journal lock**, for one stable authenticated snapshot, **with tail recovery disabled** — and it performs **zero journal mutation and zero event appends** and then releases the lock (§11.2, §13.6, §14 Phase B). **Taking a lock is not mutating**, and this design says both halves rather than only the convenient one.

**Three sentences this design must never be made to say, stated as prohibitions because each was reachable from v1_4's wording (v1_6):**

1. **Never say that an appendable refusal both appends a record and causes no journal mutation.** It appends; therefore it mutates the journal and moves the head. The true and narrower statement is that it **never mutates acceptance state** (§13.6, §18 M-17).
2. **Never say that every refusal always appends a record.** Where recording is unsafe, nothing is appended — Case C — and the refusal is still reported honestly (§15 F-35, §19).
3. **Never treat an unresolved live post-write acceptance as an ordinary refusal.** It is neither ordinary success nor ordinary refusal, and it receives **no additional refusal append while an acceptance may already exist**, because such a record would assert as refused an operation that may in fact have succeeded (§11.1, §12.3 K-8, §15 F-36, §18 M-32).

A successful click appends **one** event and no others. Specifically it does **not** additionally append: a supervisor operation started/completed pair for itself, an explanation event, an audit event, a pass event, a candidate custody or write-ahead event, a feed event, a dependency event, or a state-change event.

**A refused click appends no acceptance event, and never a partial or provisional one** — but it is not silent (corrected in v1_1). v1_0 required every refusal to append nothing at all, which contradicts Master §0B: rejections and failures are among the operations that must be permanently recorded, and a component without explicit mandatory operational recordkeeping is incomplete. §19 states the carrier, the count, and the classes.

This is `§0B`'s **ONE REAL OPERATION, ONE LOG** applied literally in both directions: a press that records acceptance is one real operation and receives one permanent record; an ordinary refused press is also one real operation and receives one permanent record (see cases 1–4 above for legitimate GET, journal/lock unsafe, and unresolved exceptions). **In neither case does creating that record create another record about creating it**, and in neither case do two records describe one press.

### 9.3 Body content (minimum)

The event body carries, at minimum, the **entire binding set of §8.2**, plus:

| Field `[proposed spellings]` | Meaning |
|---|---|
| `ness_acceptance_identity` | the deterministic identity of §8.4 |
| `acceptance_disposition` | the fixed value `ACCEPTED_FOR_DESIGN_ONLY` |
| `ness_browser_action` | `true` — an explicit Ness action in the local browser |
| `acceptance_action_channel` | `local_browser_post` |
| `acceptance_scope_id`, `acceptance_scope_digest` | the fixed non-authorization text actually shown |
| `explanation_record_identity`, `explanation_version`, `explanation_digest`, explanation `event_seq` / `event_sha256` | the exact explanation shown |
| `pre_click_authenticated_event_seq`, `pre_click_authenticated_tail_sha256` | the authenticated tail as of the offer |
| **the exact eight pre-click head fields (v1_6)** — `pre_click_head_v`, `pre_click_head_intent_generation`, `pre_click_head_intent_number`, `pre_click_head_intent_event_seq`, `pre_click_head_intent_event_sha256`, `pre_click_head_committed_event_seq`, `pre_click_head_committed_event_sha256`, `pre_click_head_auth_sha256` `[proposed spellings]` | **the complete authenticated head as of the offer, field by field** — the exact head that was revalidated under the lock immediately before this append (§8.2, §11.3 gates 2a–2b). **The two committed fields carry what v1_4 called the high-water mark; they are no longer the whole of what is recorded** |
| **`pre_click_head_digest_sha256` (v1_6)** | the canonical complete-head digest of §8.3a over exactly those eight fields |
| `acceptance_offer_binding_sha256` | the offer binding digest actually presented and echoed |
| `revalidation_outcome` | the fixed value recording that every §11.3 gate passed under the lock |

The final body key set is validated by the **existing** per-`(version, type)` schema mechanism; the exact key list is `[proposed]` and is the natural place for an implementation-time correction. **What is settled is that no element of §8.2 may be absent — the eight head fields and the complete-head digest included (v1_6).**

**The acceptance event therefore carries and references the exact complete pre-click head that was revalidated under the lock (v1_6)** — not a reconstruction of it, not a summary of it, and not the head as it stood when the page was rendered if that differed. **If they differed, the press was refused and no event exists to carry anything** (§11.3 gates 2a–2b, §15 F-3).

### 9.4 What this event means — and what it does not

**It means:** Ness, in the local browser, explicitly accepted the exact candidate named by its bound identity, for **design-only** status, while the bound explanation was the thing presented.

**It does not mean, and may never be read as meaning:**

- a provider accepted a request — it is **not** `provider_request_accepted`, **not** the provider phase `accepted`, and **not** any `ACCEPTANCE_AUTHORITIES` value (§4.3);
- a Ness answer to a question — it is **not** `answer_recorded` and **never** travels through `record-ness-answer`;
- adoption into Master or Map;
- `PACKAGE_COMPLETE`, closure, or a receipt;
- implementation approval, coding approval, or build authorization;
- that Ness read the explanation;
- that Ness understood the explanation;
- that the candidate is correct, complete, or true.

**It is a record of an act, not a verdict about content.**

### 9.5 No double evidence

Per §0B: this record proves the act occurred. It does **not** make the candidate more correct, does not strengthen the audit, does not add a vote to the PASS, and does not raise anyone's confidence in the design. The audit event, the pass event, the explanation event, and the acceptance event are **four records of four distinct real operations** — never four supporting votes for one claim.

### 9.6 One journal, one write path

The acceptance event is appended through the **existing** authenticated append path and nothing else:

- the same exclusive lock (`nh_loop.py:32184`, `acquire_interview_lock`);
- the same first-create-or-prove authentication key (`:32188-32205`);
- the same tail compare-and-swap (`:32226-32243`);
- the same mark verification under the writer's lock (`:32254-32263`);
- the same **two-mark ordering, stated as it actually is** (corrected in v1_1): the **intent** mark is written before the record it describes (`:32314-32334`), the record's bytes are written and fsynced (`:32363-32370`), and only then is the **committed** mark advanced to it (`:32460-32474`). v1_0 described this as a single "high-water mark written before the record", which is half of the real ordering and is the source of the crash ambiguity §11.1 and §12.3 now resolve;
- the same byte-exact rollback of a **live** failed write (`:32371-32390`), and the same `undo_this_record()` discipline for a post-write failure (`:32397-32439`);
- the same **one-suffix tail recovery** for a **dead**-mid-append, under the exclusive writer lock (`:31944-32034`), reached by the existing recovery-enabled read (`:31890`, `:31919-31927`) — never by a second repair path;
- the same post-commit re-read and full re-validation, and the same **committed-but-unverified** reporting when it fails (`:32502-32548`).

**No second store, no second journal, no second mark, no second append implementation, no second recovery path, no second acceptance gate.** This is `cursorrules` §1A applied directly.

**One journal, one write path — and one lock, on the reading side too (v1_6).** The same exclusive lock that governs the write also governs **every governed projection of terminal acceptance**, and this is a use of the installed lock, not a second one:

- **Every governed acceptance or status reader takes the existing exclusive interview lock (`acquire_interview_lock`, `nh_loop.py:32184`) before it may project terminal acceptance at all** (§10.1, §10.3, §11.1). It reads through the **existing** journal and the **existing** eight-field head; it creates no view, cache, snapshot store, or second projection authority.
- **A legitimate offer read takes that same lock for one stable authenticated snapshot, with tail recovery DISABLED, and performs zero mutation and zero appends** — the existing default read `read_interview_journal(errors)` at `allow_tail_recovery=False` (`journal.py:208-224`), taken inside the existing lock and released immediately (§11.2, §14 Phase B). **No new read function, no new lock, and no new recovery is introduced to do it.**
- **The recovery-enabled read remains exactly where v1_1 put it** — the acceptance/write-capable entry path's `read_interview_journal(errors, allow_tail_recovery=True)` (`:31890`, `:31919-31927`), reaching the existing one-suffix `recover_interview_journal_tail()` (`:31944-32034`). **That path is separately authorized and unchanged; the offer read is not it and never becomes it** (§14 Phase B, Phase E1).
- **Rollback authority is bounded by that same lock (v1_6).** The existing live rollback (`:32371-32390`) and the existing post-write `undo_this_record()` discipline (`:32397-32439`) are legal **only** for the active append attempt, **only** while it owns this lock, and **only** before terminal acceptance is exposable. **They are not a general power to remove a complete acceptance**, and no reader, retry, recovery, or later writer may invoke them against one (§11.1, §18 M-13).

**This adds no authority. It names which existing authority a reader must hold before it is allowed to say the word "accepted".**

### 9.7 Feed behaviour

The acceptance event belongs to the **non-feed** set: it must never become a "problem_found", "candidate_changed" or "audit_passed" card, and the feed's `claims_acceptance` projection stays hard-false (`supervisor.py:435`). Acceptance is displayed **only** from the replayed workflow state — never as a feed claim, and never on any model's authority.

---

## §10 — REPLAY AND STATE PRECEDENCE

### 10.1 The new precedence rule

One rule is inserted into the existing projection order, **above** the current PASS gating at precedence 12 (`status.py:1199-1204`):

> **Precedence 11.5 `[proposed numbering]` — acceptance is terminal.**
> If the governed acceptance truth of §11.1 is **`PROVED_ACCEPTED`** for the current package scope and the current candidate identity — that is, a valid `ness_candidate_acceptance_recorded` exists in scope, binds the current candidate identity, **and no live writer retains legal authority to remove it** — then:
> - `workflow_state = ACCEPTED_FOR_DESIGN_ONLY`
> - `next_command = null`
> - `reason = "ness_candidate_acceptance_recorded"` `[proposed]`
> and the projection returns immediately.

**The precondition on that rule is the whole of the v1_6 correction to this section, and it is a precondition on the projection, not a new event or a new state.** v1_4 wrote the rule as *"if a valid acceptance event exists"*, which is a question about **raw replay** — is this event authentic, complete, in scope, and correctly bound? That question has a true answer inside the window in which a live writer may still legally roll the event back (§11.1, §12.3 K-4a). **So v1_4's rule permitted a governed reader to project `ACCEPTED_FOR_DESIGN_ONLY` and then have that acceptance removed underneath it.** A terminal state that can disappear is not terminal.

**Two questions, kept apart from here on:**

| Question | Answered by | Answer |
|---|---|---|
| Is this event authentic, complete, in scope, and correctly bound? | **raw journal replay**, over the existing authenticated history | yes / no / contradiction — §10.3 |
| Is acceptance terminal, and safe to show as terminal? | **governed terminal projection**, under the existing exclusive lock | `PROVED_ACCEPTED` / `PROVED_NOT_ACCEPTED` / `UNRESOLVED` — §11.1 |

**Precedence 11.5 fires on the second question only.** Raw replay is a necessary input to it and is never a substitute for it. **This introduces no second journal, no second head, no second store, no second projection authority, and no second event type — it introduces a precondition, expressed over the machinery that already exists** (§9.6, §11.1).

**When the governed truth is `UNRESOLVED`, precedence 11.5 does not fire and no lower rule is allowed to answer in its place.** The projection is a **non-running safety condition** that claims neither acceptance nor non-acceptance, offers no Accept control, and says plainly that the truth is not currently provable (§10.5, §11.1, §12.5, §16.2). **`UNRESOLVED` is a derived condition of this projection — not a workflow state value, not a durable protocol, not an event type, and not a mark.** The locked value set is untouched: the only new state value this design introduces is still `ACCEPTED_FOR_DESIGN_ONLY` (§0, §4.5 D4).

**When the governed truth is `PROVED_NOT_ACCEPTED`, the projection is exactly what it would have been without any acceptance event** — the ordinary rules below precedence 11.5 apply unchanged, and nothing about this design's own state is claimed.

### 10.2 `acceptance_required` follows without a second source

`acceptance_required` is derived today as `projected["workflow_state"] == "READY_FOR_ACCEPTANCE"` (`status.py:1711`). Under the new state that expression is **false automatically**.

**This design deliberately keeps that single derivation and adds no second source of truth for `acceptance_required`.** A stored acceptance flag, a UI-side flag, or a second boolean would be exactly the parallel-gate proliferation `cursorrules` §1A prohibits.

### 10.3 Validity of an acceptance event during replay

An acceptance event is **valid for the current projection** only when all of the following hold:

1. it validates structurally and by authentication like any other event (`journal.py:86-138`);
2. its `package_scope_id` matches the current scope;
3. its bound candidate identity equals the current candidate identity;
4. the audit event and pass event it names exist at the named sequence numbers with the named digests;
5. the explanation event it names exists at the named sequence number with the named digest;
6. `acceptance_scope_digest` equals the controller's current fixed scope digest;
7. **(v1_6) it was read under the existing exclusive interview lock, held by this reader, over a journal and an eight-field head that both authenticate end to end.** A reader that does not hold that lock may establish 1–6 and **may not project terminal acceptance from them** (§9.6, §10.1, §11.1).

**Rules 1–6 are raw-replay validity, and rule 7 is what makes validity projectable (v1_6).** The separation matters because the two can disagree, and v1_4 had no way to say so:

| Situation | Rules 1–6 | Rule 7 | Governed truth |
|---|---|---|---|
| The event is authentic, complete, in scope, correctly bound, and the committed head durably names it | hold | holds | **`PROVED_ACCEPTED`** |
| The event is authentic and complete and the head's **intent** mark names it, and a live writer still owns the lock and may still legally roll it back | hold | **cannot hold** — the reader cannot take the lock | **not projectable at all**; to the writer itself the standing is **`UNRESOLVED`** until it is proved (§11.1, §12.3 K-4a) |
| The same complete event, after writer ownership has ended, verified stably under the lock this reader now holds | hold | holds | **`PROVED_ACCEPTED`**, and removal is thereafter forbidden (§11.1, §18 M-13) |
| The journal or the head cannot be authenticated without repair | cannot be established | — | **`UNRESOLVED`**; no repair is performed by a reader (§14 Phase B, §15 F-1) |

**A raw complete event in the `present == intent > committed` window may prove authenticity and completeness. It does not prove terminal acceptance while an active writer may roll it back**, and this design never lets one stand in for the other (§11.1).

### 10.4 Contradictions fail closed — the newest is never simply preferred

| Condition | Projection |
|---|---|
| Two acceptance events with **different** `ness_acceptance_identity` values in one package scope | **contradiction ⇒ fail closed**; state is recovery-required; neither is preferred, neither is erased, and no acceptance is claimed |
| An acceptance event binding a candidate that is **not** the current candidate | **contradiction ⇒ fail closed**; never silently ignored and never treated as acceptance of the current candidate |
| An acceptance event whose named audit / pass / explanation event does not exist or does not match | **contradiction ⇒ fail closed** |
| A `mechanical_pass_recorded` appearing **after** a valid acceptance for the same candidate | **contradiction ⇒ fail closed**; the acceptance is not reopened, rewritten, or revoked, and no second acceptance is created |
| A newer candidate appearing after a valid acceptance | the acceptance stands as history for its own exact identity; the current package state is **recovery-required**, and the new candidate is **never** treated as accepted |

In every row: **records are preserved exactly as they stand, the contradiction is recorded honestly, nothing is repaired silently, and no state claims success.** This is the same discipline UDOK states for membership contradictions and the same one `cursorrules` §9 requires for store writes.

### 10.5 Ordering relative to interrupting states

Acceptance is terminal for **this** workflow. It is projected above the PASS rule and below the existing safety, contradiction, and journal-integrity refusals: **an unauthenticated journal, an unproved projection, or a safety hold is always answered first.** Acceptance never overrides a safety refusal, and a safety refusal never erases a committed acceptance.

**Where `UNRESOLVED` sits in that order, stated so it is not mistaken for a new protocol (v1_6).** `UNRESOLVED` is not a rule of its own with a position of its own. It is **the result of precedence 11.5 failing to prove its precondition**, and it behaves exactly like the existing safety and integrity conditions that already sit above acceptance:

- it is answered **before** any ordinary lower rule, so nothing below it may supply a confident answer in its place;
- it is **non-running** — no command, no worker step, no scheduling, and no retry loop follows from it;
- it claims **neither** `ACCEPTED_FOR_DESIGN_ONLY` **nor** non-acceptance, and it never converts into either by waiting (§12.5, §18 M-32);
- it withholds the Accept control, because an offer computed over an unprovable world is not an offer (§14 Phase B, §16.2);
- it is resolved **only** by the existing recovery path proving one of the two proved classifications — never by this design writing anything (§12.5).

**It creates no durable record, no second workflow protocol, no event type, and no mark.** It is a derived condition of a projection, held for exactly as long as the journal and head cannot prove which of the two proved answers is true.

---

## §11 — TRANSACTION, LOCK, AND REVALIDATION UNDER THE LOCK

### 11.1 The transaction boundary

The acceptance transaction is exactly the existing single-event append transaction. It **begins** when the exclusive interview lock is acquired.

**The record boundary, stated once, against the actual reader (corrected in v1_1, and kept exactly as v1_1 states it).**

> **The acceptance event exists as a record from the moment the complete authenticated event's final newline is durable and the head's intent mark names it.**

This is not a preference; it is what the installed reader does. `check_interview_journal_head()` accepts `present == intent > committed` as a valid history and requires only that the record that landed be exactly the one that was declared (`nh_loop.py:31294-31302`). A journal in that window therefore **replays the acceptance event**. v1_0's §11.1 claimed instead that no acceptance exists until the committed mark advances (`:32460-32474`), while its own C-5 admitted a complete acceptance may survive that window. **Those were two answers to one question, and the reader only ever gives one.** v1_1 states the reader's answer, and v1_6 does not disturb it.

**What each mark actually means, then:**

| Mark | Written when | What it proves | What it is *not* |
|---|---|---|---|
| **intent** (`:32314-32334`) | **before** the record's bytes | this controller declared exactly this one record, and the reader will accept it if it landed complete | not a claim that the record exists |
| **committed** (`:32460-32474`) | **after** those bytes are durable | anything shorter than this is a **deletion**, and is refused | **not the record boundary**, and never was |

- **Before the record's final newline is durable: no acceptance record exists**, whatever else happened — an intent mark alone is a declaration, not a record, and §12.3 forbids ever writing from one.
- **From that newline onward: the record exists**, whatever else fails afterwards.

#### 11.1a The correction v1_6 makes: a record existing is not the same as acceptance being terminal

**What v1_4 got wrong, stated exactly.** v1_4 took the sentence above and used it as the answer to a **second, different** question — *may a governed reader now show `ACCEPTED_FOR_DESIGN_ONLY`?* — and answered yes throughout the `present == intent > committed` window. **But in that window the live writer that declared the record still holds the exclusive lock and still legally may remove it**: the installed live rollback restores the segment byte-for-byte (`:32371-32390`), and the installed post-write `undo_this_record()` discipline may undo the record when the committed mark cannot be advanced (`:32397-32439`, `:32475-32500`) — which v1_4's own §15 F-36b describes approvingly. **So v1_4 permitted a governed reader to publish a terminal acceptance that a live writer was still entitled to take away.** A terminal state that can disappear is not terminal, and this is the defect, stated as the mechanism rather than as a worry.

**The correction is a separation, not a new mechanism.** It uses **only** the existing journal, the existing eight-field head, the existing exclusive lock, the existing tail recovery, the existing rollback behaviour, and the existing authenticated history. **It creates no second journal, no second store, no second head, no second mark, no second protocol, no new event type, and no second recovery authority** (§9.6, §18 M-9, M-10).

| Layer | Question it answers | Evidence it uses |
|---|---|---|
| **Raw journal replay** | is this event authentic, complete, in scope, and correctly bound? | the existing authenticated history and the existing head rule (§10.3 rules 1–6) |
| **Governed terminal projection** | is acceptance terminal, and safe to expose as terminal? | the same evidence, **read under the existing exclusive lock held by this reader**, plus the rollback-legality rule below (§10.3 rule 7) |

#### 11.1b The three externally visible truth classifications

**CORE RULE: REQUEST OUTCOME AND ACCEPTANCE TRUTH ARE INDEPENDENT.** A request may be refused while the locked journal proves terminal acceptance stands. Conversely, an acceptance may be unresolvable in truth even when a request succeeds. Request validity (whether the POST echo, Origin, method, and fields are acceptable) and acceptance truth (what the authenticated history and head prove about the candidate's acceptance state) are determined by separate locked inspections, and a response must report whichever truth the journal proves, regardless of whether the request was valid.

**Exactly three, and no fourth.** Every governed reader, response, surface, and status answer of this design resolves to one of these and to nothing else:

| Classification | Holds when |
|---|---|
| **`PROVED_NOT_ACCEPTED`** | the **old prefix is durably proved** — the authenticated history and head prove that the exact pre-acceptance prefix stands — **and no complete acceptance event exists** in scope for this candidate |
| **`PROVED_ACCEPTED`** | **exactly one** complete, authenticated, correctly bound acceptance event is durably proved in scope for this candidate, **and no live writer retains legal authority to remove it** |
| **`UNRESOLVED`** | **neither** side is safely proved |

**`UNRESOLVED` is a derived non-running safety and result condition. It is not a second durable workflow protocol, not a workflow state value, not an event type, not a mark, and not a stored flag** (§10.1, §10.5). It is what a locked, honest reader says when the journal and head do not yet prove which of the two proved answers is true.

**While the truth is `UNRESOLVED`, all of the following hold at once:**

- **claim neither accepted nor not accepted** — the surface says the truth is not currently provable, in plain words;
- **Accept is unavailable** — no offer, no actionable control (§14 Phase B, §16.2);
- **no success response** is issued, ever;
- **no ordinary denial pretending certainty** is issued either — a refusal that says "not accepted" would be a claim, and the claim is exactly what is missing;
- **no blind retry** — a retry that assumed non-acceptance could write a second acceptance (§12.3, §12.5);
- **no effect replay** — nothing is re-run to "make it definite" (§12.5);
- **no extra refusal append while acceptance may already exist** — a refusal record would assert as refused an operation that may have succeeded (§9.2, §15 F-36, §19).

#### 11.1c The rollback rule, which is what makes `PROVED_ACCEPTED` safe

> **Rollback of an acceptance append is legal ONLY for the active append attempt, ONLY while that attempt owns the existing exclusive lock, and ONLY before terminal acceptance is exposable. There is no other rollback authority anywhere in this design.**

- **`PROVED_NOT_ACCEPTED` requires durable proof that the exact old prefix was restored** — not an intention to roll back, not a raised exception, not a log line. If the rollback happened but its durability cannot be proved, **the truth is `UNRESOLVED`**, not "not accepted" (§12.3 K-7).
- **Terminal acceptance becomes exposable — and removal is thereafter forbidden — at whichever of these comes first:**
  1. **the committed head durably names the event**, or
  2. **after writer ownership has ended, a locked stable verification proves the complete acceptance remains and cannot legally be removed** — that is, this reader holds the exclusive lock, the history and the whole eight-field head authenticate, and the record that landed is exactly the one the head declared (`:31294-31302`).
- **From that point the record is permanent to every actor**: no reader, retry, recovery, later writer, or contradiction handler may remove, amend, supersede, or truncate it (§18 M-13, §12.5).

**Why holding the lock is what proves "no live writer retains legal authority".** Rollback is legal only while owning this lock. A reader that holds it therefore knows that **no append attempt currently owns it**, so no attempt is currently entitled to roll anything back. A later attempt is not entitled either: it did not write this record, and lookup-first means it finds the existing acceptance and appends nothing (§12.1, §12.2). **The proof is exclusion by the installed lock, not an assumption about process liveness.**

#### 11.1d The two-mark positions and live writer behaviour, reconciled in one place

| Actual position | Governed truth | Why |
|---|---|---|
| A writer holds the exclusive lock and is mid-append | **no governed terminal visibility at all** | every governed reader needs that same lock and cannot obtain it; nothing is shown, and nothing false is shown (§9.6, §10.3 rule 7) |
| A rollback ran and the **exact old prefix is durably proved** | **`PROVED_NOT_ACCEPTED`** | the pre-acceptance world is proved, not assumed |
| A rollback ran but **its completion or its durability cannot be proved** | **`UNRESOLVED`** | an unproved restoration is not a proof of non-acceptance |
| Writer ownership has **ended**, and a **locked stable verification** finds the complete authenticated acceptance still standing, declared by the head | **`PROVED_ACCEPTED`** | no live writer retains legal authority to remove it; removal is forbidden from here on |
| The **committed head durably names the event** and the event is durably proved | **`PROVED_ACCEPTED`** | the strongest ordinary case, and the one v1_4 already handled correctly |
| The journal or the head is **unreadable, unauthenticatable, or otherwise unprovable** | **`UNRESOLVED`** | truth is never guessed in either direction (§12.3 K-10, §15 F-1) |
| A **response was lost**, from any position above | resolved **lookup-first, always** | the identity is deterministic; the answer is whatever the durable world proves, and no retry ever writes a second acceptance (§12.1, §12.3 K-6) |

**The response must match the standing, in every position (v1_1's rule, kept and made precise in v1_6).** A request whose record is durable and named by the head, and which a locked stable verification proves, is reported as **recorded** and a retry resolves to `already_recorded` by lookup (§12.2, §12.3 K-4b and K-5). **A request that cannot prove which side it is on is reported as unresolved** — never as a failure, never as a success, and never with an instruction to press again (§15 F-36, §16.4).

### 11.2 Read-then-lock-then-re-prove

The offer projection (§16.2) is **read-only**. **Nothing it computed is trusted at write time.** Everything is re-proved inside the lock, from the world as it is inside the lock.

**Corrected in v1_6 — "read-only" is not the same as "unlocked", and v1_4 conflated them.** The offer read now takes the **existing** exclusive interview lock, and the reason is not caution but arithmetic: the offer must publish **one stable authenticated snapshot** — the event tail **and** all eight head fields **and** the complete-head digest over exactly them (§8.2, §8.3a). Read without the lock, those values can be sampled across a concurrent append and published as a head that never existed. **A binding assembled from a head that never existed is worse than a stale one, because the lock-time comparison would then be comparing against a fiction.** And the governed truth of §11.1 cannot be projected without that lock at all (§10.3 rule 7).

**Exactly what the offer read does, and exactly what it must not do:**

| The offer read | Settled |
|---|---|
| Lock | **the existing exclusive interview lock** (`acquire_interview_lock`, `nh_loop.py:32184`) — **acquired only for one stable authenticated snapshot, and released immediately after it** |
| Read | **the existing default read** `read_interview_journal(errors)` at `allow_tail_recovery=False` (`journal.py:208-224`) |
| Tail recovery | **DISABLED — always, without exception.** The offer read never repairs, never truncates, never fsyncs, and never invokes `recover_interview_journal_tail()` |
| Journal mutation | **ZERO** |
| Event appends | **ZERO** — however many times the offer is read, actionable or not (§9.2 Case A, §19, §21 T-46b) |
| Head mutation | **ZERO** — no mark is written, advanced, rewritten, or repaired |
| If the journal or head cannot be authenticated **without** recovery | **return a non-actionable recovery-required / `UNRESOLVED` offer**: `acceptance_actionable = false`, one plain-language reason, **no offer identity**, **no partial offer**, and **acceptance remains unavailable**. **The GET performs no repair whatsoever** (§14 Phase B, §16.2, §15 F-1) |

**Why the offer GET may not repair, stated as a rule rather than as a preference.** Tail recovery is a **write** — it truncates the segment, fsyncs, and re-reads (`:31944-32034`). Letting a GET perform it would make a read route into a mutation route, which is exactly what §13.6 and §18 M-17 forbid, and would put a repair authority behind a request anyone in the local browser can issue by navigation or prefetch. **The repair stays where v1_1 put it: the already separately authorized recovery-enabled, write-capable entry path** (below, and §14 Phase E1). **An unrecoverable-looking journal is therefore reported by the offer, and repaired by the path that owns repair — never by the read that noticed it.**

**Taking the lock is not mutating, and neither claim is dropped in favour of the other (v1_6).** The offer read holds a lock and changes nothing. §9.2 Case A, §13.6, §14 Phase B, §16.1, and §19 all state both halves.

**The read that opens the transaction is the recovery-enabled one, and this design says which (corrected in v1_1).** The acceptance entry path reads the journal through the **existing** `read_interview_journal(errors, allow_tail_recovery=True)` (`nh_loop.py:31890`), which takes the exclusive writer lock and calls the existing `recover_interview_journal_tail()` before parsing (`:31919-31927`). That is the only sanctioned repair in the journal, it removes at most one unterminated trailing suffix, and it refuses rather than truncating when the prefix is not a completely valid chain or the final line is complete-but-malformed (`:31944-32034`).

**Why naming it is a correction and not an addition.** The installed production gateway reads **without** it: `NhLoopJournalGateway.read()` and `.append()` both call `read_interview_journal(errors)` at the default `allow_tail_recovery=False` (`journal.py:208-224`), which fails closed on an unterminated tail. v1_0 named no acceptance entry path that performed the recovery first, so a crash-interrupted append could leave the surface unable to read, recover, or proceed. **v1_1 assigns that step an owner** — the acceptance entry path, before replay and before lookup — and authorizes **no new recovery mechanism** to do it: the invocation already exists, and only the caller is being named.

### 11.3 The revalidation list — all of it, immediately before the append

Under the journal lock, immediately before appending, the controller **re-reads, replays, and re-validates**:

| # | Re-proved under the lock |
|---|---|
| 1 | the authenticated journal reads, validates, and authenticates end to end; every event's HMAC verifies with this controller's key |
| 2 | the head verifies against the history under the writer's lock — `intent ∈ {committed, committed + 1}`, no record shorter than committed, no record past intent, and the declared record matched where `present == intent > committed` (`nh_loop.py:31241-31302`) — and is **never repaired by overwriting** |
| 2a | **the ENTIRE head is re-read and re-authenticated under this lock, immediately, from the head as it now is (v1_6)** — all eight fields, `v`, `intent_generation`, `intent_number`, `intent_event_seq`, `intent_event_sha256`, `committed_event_seq`, `committed_event_sha256`, `head_auth_sha256`, with `head_auth_sha256` verifying over the others by the installed head authentication. **Nothing is carried forward from the offer read, and nothing is reconstructed from a subset.** A head that does not authenticate ⇒ refuse, `UNRESOLVED`, zero appends (§11.1, §15 F-1) |
| 2b | **the complete-head comparison is exact, field by field, and by digest (v1_6)**: **every one** of those eight fields equals the value the offer bound (§8.2), **and** `pre_click_head_digest_sha256` recomputed here by §8.3a over exactly that eight-field object equals the value the offer published and the POST echoed. **Any single difference in any single field, or in the digest, ⇒ STALE ⇒ refuse** (§15 F-3). **A matching digest never excuses an unmatched field, and no field is treated as a summary of any other.** **The case this gate exists for is K-2:** a valid intent-only change moves `intent_generation`, `intent_number`, `intent_event_seq`, `intent_event_sha256` and `head_auth_sha256` while leaving the event tail and **both** committed fields unchanged, so gate 3 alone cannot see it — **and it must stale the offer** (§12.3 K-2, §11.4) |
| 3 | the tail compare-and-swap holds: the record count and last digest are exactly what the offer was computed from |
| 4 | the projected state is `READY_FOR_ACCEPTANCE`, and that projection is valid only after gate 11d proves the complete matching A5/A6 operation chain; a PASS without matching A6 completion remains completion-recovery work and is not ready |
| 5 | `acceptance_required` is true |
| 6 | package key, package scope id, package id match the offer |
| 7 | branch, head SHA, and `source_binding_sha256` match the offer |
| 8 | `settled_decision_binding_sha256` matches the offer |
| 9 | the candidate file is re-read from disk and its **path, SHA-256, and byte count are recomputed** and match the offer exactly |
| 10 | the exact final **usable** audit is the bound one: identity, event sequence, digest, verdict `PASS`, schema-valid, source-stable, usability-proved |
| 11 | **the PASS is located by the identity the explanation binds, not by position (v1_2)**: **exactly one** `mechanical_pass_recorded` in scope carries the explanation's bound `pass_identity`; it **is** the current pass event for this candidate; its `audit_identity` is the bound audit; its event sequence and digest are what the offer published; and every PASS-gate boolean it recorded is still true. **Zero such events ⇒ refuse; two ⇒ contradiction ⇒ refuse** (§15 F-9) |
| 11a | **the bound `pass_identity` recomputes (v1_2)** by the installed derivation over the controller's own current inputs (`commands.py:1425-1441`) to exactly the value the explanation carries **and** the value the pass event carries. This is what proves the pre-PASS binding of §7.4a was right, rather than merely well-formed |
| 11b | **the ordering contract held, proved from journal position alone (rewritten in v1_3)**: (i) the bound final-stage explanation record's `event_seq` is **strictly less than** the pass event's `event_seq`; (ii) **no** `mechanical_pass_recorded` in this package scope sits at an `event_seq` **at or below** the bound explanation record's — so the explanation preceded **every** PASS in scope, not merely the one it binds; (iii) the bound explanation record's `event_seq` is **strictly greater than** both the bound audit event's and the named content-stage record's, so the prose binding genuinely followed the evidence it names. A final record at or after the pass event's position **contradicts §7.1a and is refused**, never accepted as an equivalent arrangement. **Every clause is an `event_seq` comparison over events already required to exist by gates 10, 11, 12 and 12b, and is therefore evaluable in every arrangement a crash can leave** (§7.1b) |
| 11c | **the v1_2 clause removed from gate 11b, recorded rather than dropped silently (v1_3)**: v1_2's gate 11b additionally required the explanation record and the pass event to carry **the same `supervisor_operation_id`**. That clause is **withdrawn**, for two independent reasons that are both facts about the installed files. **First, it is unreadable:** neither type's installed body key set contains `supervisor_operation_id` (`schema.py:680-704`, `:705-723`), and `Operation.append()` adds only the type, the package/source standing, and the candidate body (`engine.py:449-458`) — only `supervisor_operation_started` and `supervisor_operation_completed` carry that field. **Second, it is false wherever it mattered:** the only reachable recovery re-enters through a fresh `engine.Operation` (`commands.py:1444-1448`) whose identity derives over the moved journal tail (`engine.py:187-205`; `commands.py:94-125`), so the two identities necessarily differ. **A gate that cannot be evaluated — and that would refuse its own recovery if it could be — is removed, not reinterpreted.** Nothing it was reaching for is lost: the explanation-before-PASS ordering is proved by 11b, the PASS binding by 11 and 11a, and the prose identity by 12a–12d. **No gate compares the explanation event's operation identity with the PASS event's operation identity; neither substantive event carries one. Gate 11d instead compares each operation's authenticated start only with its own matching completion, which those existing event types do carry** |
| 11d | **the effect-owning completed operation chain is durable:** identify exactly one A5 start/completion pair that owns the one final explanation: that A5 start precedes the explanation, its matching A5 completion follows the explanation, and the completion carries the same `supervisor_operation_id` and that A5 start's `event_seq` as `supervisor_started_event_seq`. Only after that matching A5 completion may the effect-owning A6 pair begin. Identify exactly one A6 start/completion pair that owns the one PASS: that A6 start follows the matching A5 completion and precedes the PASS, and its matching A6 completion follows the PASS with the same A6 `supervisor_operation_id` and that A6 start's `event_seq` as `supervisor_started_event_seq`. **Pre-effect unmatched starts that produced neither the final explanation nor the PASS may remain preserved historical residue and are not counted as effect-owning pairs.** More than one qualifying effect-owning A5 pair, more than one qualifying effect-owning A6 pair, a substantive event owned by two candidate pairs, or any missing, duplicate, reordered or mismatched member of either qualifying pair refuses the offer. The required effect-owning order is A5 start < one final explanation < matching A5 completion < A6 start < one PASS < matching A6 completion |
| 12 | the current explanation is the bound one: `explanation_stage` is the final acceptance stage, identity, version, digest, event sequence, event digest — and it still binds this candidate, this audit, this `pass_identity`, and this predecessor |
| 12a | the bound explanation's `explanation_content_digest` **recomputes over parts 1–6 as they stand** and **equals** the content-stage record's value — so the prose on offer is byte-identical to the prose the bound audit read (§6.6 check 8) |
| 12b | the content-stage record the final record names **exists** at the named sequence with the named digest, and its own candidate binding is this candidate |
| 12c | the bound audit event's own record **covers that content digest** — the audit that is bound is the audit that read this exact prose, not merely an audit of the same candidate |
| 12d | **part 7 recomputes** from the bound audit event by the controller's fixed derivation (§6.5a), and part 8 matches the fixed scope text by digest |
| 12e | **the final-stage record carries no forward pass-event reference (v1_2)**: it has no pass `event_seq` and no pass `event_sha256`. A record carrying either could only have been written after the pass event, which §7.1a forbids ⇒ refuse |
| 13 | **no newer candidate** exists in scope |
| 14 | **no newer audit** exists for this candidate, and **no conflicting audit** exists |
| 15 | **no superseding explanation** exists, at either stage, for this binding |
| 16 | **no deliverable Ness question** is open and no open question group exists |
| 17 | **no changed settled-decision binding** and **no source change** since the offer |
| 18 | **no conflicting acceptance** exists (§12.4) |
| 19 | **no open provider request** |
| 20 | **no open provider result custody** |
| 21 | **no pending candidate write-ahead** |
| 22 | **no open consumption** |
| 23 | **no open provider availability probe** |
| 24 | **no open audit-usability retry** |
| 25 | `acceptance_scope_id` / `acceptance_scope_digest` equal the controller's fixed scope text, so the scope actually shown is the scope recorded |
| 26 | the request arrived with a localhost `Host` **and** a strict, exactly-matching `Origin` (§13.4) |
| 27 | `acceptance_offer_binding_sha256` recomputes, under the lock, to exactly the value posted — **and, since v1_6, that binding covers the eight exact head fields and `pre_click_head_digest_sha256` (§8.2, §8.3), so gate 27 and gate 2b agree by construction rather than by coincidence** |
| 28 | **the echoed values are treated as echo, never as authority (v1_6)**: the posted `acceptance_offer_binding_sha256` and `pre_click_head_digest_sha256` are compared against values the controller **recomputed here, under this lock, from the world as it now is**. **A posted value is never believed, never substituted for a recomputation, and never used to fill in a value the controller could not derive** (§13.3, §16.3) |

**Any single difference ⇒ fail closed, zero acceptance appends, no partial state, a plain-language refusal, and — where the journal and lock can safely record it — exactly one operational refusal record (§19); where they cannot, zero appends and no claim of success (§15 F-35).** Gates 19–24 are the same six conditions the existing PASS gate already proves (`commands.py:1400-1424`); they are re-proved here because time has passed since the PASS.

**And every one of these gates is proved from the world inside this lock (v1_6).** The offer read of §11.2 took the same lock for its own snapshot and released it; **nothing that read computed is authority here.** The head is re-read and re-authenticated (gates 2, 2a), compared whole (gate 2b), and the acceptance event then records the exact complete pre-click head that was revalidated here and nowhere else (§9.3).

### 11.4 The journal position is bound strictly — and "position" means the complete head (rewritten in v1_6)

The pre-click authenticated **event tail** and **the entire eight-field authenticated head**, plus the canonical complete-head digest over exactly that object, are part of the offer binding (§8.2, §8.3, §8.3a). **If the journal or the head moved at all between render and click, the offer is stale and the press is refused.**

**What v1_4 bound, and the gap it left.** v1_4 bound *"the pre-click authenticated tail and the head's committed mark"*. Those are three of the values that describe the world; the head has **eight** fields, and its own rule — `intent ∈ {committed, committed + 1}` (`nh_loop.py:31241-31302`) — allows it to move in a way that touches **none** of the three:

| Change | Event tail | `committed_event_seq` / `committed_event_sha256` | `intent_*` and `head_auth_sha256` | Seen by v1_4's binding? | Seen by v1_6's? |
|---|---|---|---|---|---|
| An ordinary committed append | moves | move | move | yes | yes |
| **A valid K-2 intent-only change** — a declared append whose record bytes never landed | **unchanged** | **unchanged** | **move** | **NO** | **yes ⇒ STALE** |

**The K-2 row is the defect, and it is not hypothetical: it is a valid history the installed head rule expressly accepts** (§12.3 K-2). Between the offer and the press, another writer declaring an append and dying is exactly the world in which the press should be recomputed rather than trusted — and v1_4's binding could not tell that it had happened. **v1_6 binds the whole head, compares every field, and stales on any difference** (§11.3 gates 2a–2b).

**The strictness and its trade are unchanged.** It is safe in practice because `READY_FOR_ACCEPTANCE` is a non-running state in which the worker executes no command (`worker.py:73-82`), so nothing ordinarily appends while an offer is outstanding. And it is **recoverable**: a refusal for a moved head or tail is never terminal — reloading produces a fresh offer over the fresh, wholly re-read head, and Ness may press again. **Widening what is bound makes the offer stale slightly more often and makes an accepted press mean strictly more; that is the direction this design takes deliberately.**

The more tolerant alternative — accept a moved tail if every intervening event is provably non-conflicting — was considered and **rejected for this version**, because it would require this design to enumerate and keep current a "harmless event" list, and a wrong entry on that list would be a silent acceptance over a changed world. **Strict equality with cheap recovery is the safer trade, and it is chosen here.** **The same reasoning rejects a "harmless head field" list (v1_6): all eight fields are compared, and none is exempted.**

**And none of this reaches the deterministic acceptance identity.** Journal position — tail and head alike — stays **excluded** from `ness_acceptance_identity`, because a retry of the same act must derive the same identity even though the world has moved (§8.4). **What is bound is what must be true for the press to be current; what is identified is what makes two presses the same act. v1_6 changes the first and leaves the second exactly as it was settled.**

### 11.5 One writer

Concurrency is handled by the machinery that already exists: an exclusive lock plus a tail compare-and-swap. **No new locking scheme, no advisory flag, no in-memory mutex-as-authority, and no "check then write" window is introduced.**

---

## §12 — IDEMPOTENCY, CONCURRENCY, AND CRASH RECOVERY

### 12.1 Lookup-first, always

Inside the lock, **before** any append is considered, the controller looks up whether an acceptance with this deterministic identity already exists in the authenticated history.

**Lookup precedes writing, always.** This is the accepted lookup-first discipline the project already applies to candidate custody, provider results, retry, reread, ingestion, and promotion — applied here.

### 12.2 The idempotency cases

| Case | Behaviour |
|---|---|
| **First valid click** | all gates pass ⇒ **exactly one append in total**, the acceptance event ⇒ response reports `recorded_now` `[proposed]` |
| **The same exact click twice** | the second lookup finds the existing acceptance with the identical identity **and** an identical bound record ⇒ **no append of any kind**; the existing record is returned; the response reports `already_recorded` `[proposed]`. **This is not a refusal and receives no refusal record** (§16.4, §19) |
| **Two concurrent identical clicks** | the lock serializes them; the first appends; the second finds the committed record and appends nothing. **Exactly one record exists.** The tail compare-and-swap is the backstop if the two ever raced outside the lookup |
| **Response lost, then retry or reload** | identical to the "same exact click twice" case: the existing record is found and returned, unchanged, with no append |
| **A different candidate** | derives a **different** identity, is never matched to the existing record, and is refused because the state is terminal (§17.2). **A different candidate is never absorbed into an existing acceptance** |
| **Conflicting same-pass material** | §12.4 |
| **The governed truth is `UNRESOLVED` (v1_6)** | **no append of any kind**, and **no refusal record while an acceptance may already exist**. The response is neither `recorded_now` nor an ordinary refusal: it reports the unresolved standing plainly (§16.4). **Reload and retry remain unresolved, with zero effect replay, until the existing recovery path proves one of the two proved classifications** (§11.1, §12.5) |

**Every row of this table is decided lookup-first, under the existing lock, against the governed truth of §11.1 — never against a raw replay alone (v1_6).** The two proved classifications drive the two ordinary answers, and the third drives no answer at all:

| Governed truth at lookup | What this request does |
|---|---|
| **`PROVED_ACCEPTED`** | returns the existing record, `already_recorded`, **zero appends**, **no new identity derived** |
| **`PROVED_NOT_ACCEPTED`** | proceeds through §11.3; if every gate passes, **exactly one** append |
| **`UNRESOLVED`** | **stops** — zero appends, no success, no ordinary denial, no blind retry, no effect replay |

### 12.3 Crash matrix (lookup-first; no effect replay; no false success)

**Rewritten in v1_1 against the actual two-mark writer and the actual reader; re-columned in v1_6 to separate raw replay from governed truth.** Every row states the crash position, what is durably on disk, **what the installed reader returns** (raw replay), **what the governed truth of §11.1 is**, who owns the recovery, and what a retry does. The row order is the write order of `append_interview_event()` (`nh_loop.py:32314-32474`).

**The fifth column changed meaning in v1_6, and this is the whole of the change to this table.** v1_4 asked *"does an acceptance exist?"* and answered it from raw replay alone. That question conflates two — *is the record real?* and *is acceptance terminal and safe to show?* — and the second is the one every governed reader, response, and surface actually needs (§11.1a). **The rows below therefore answer the second, and the fourth column keeps answering the first.**

| # | Crash position | Durably on disk | Raw replay — what the actual reader returns | **Governed truth (§11.1)** | Owned recovery | Retry |
|---|---|---|---|---|---|---|
| K-1 | **Before the intent mark** — including before the lock was taken | nothing new; head names the old record as both intent and committed | `present == committed`, committed digest matches the last record ⇒ valid history, old prefix (`:31278-31293`) | **`PROVED_NOT_ACCEPTED`** — the exact old prefix is durably proved and no complete acceptance exists | none needed | derives the same identity; lookup finds nothing; **appends once** |
| K-2 | **Intent mark only** — mark written, no record bytes landed | head has `intent == committed + 1`; journal still holds the old prefix | `present == committed < intent` ⇒ **valid**: the head rule allows `intent ∈ {committed, committed+1}` and `present == committed` is checked against the committed digest (`:31252-31258`, `:31278-31293`) | **`PROVED_NOT_ACCEPTED`** — an intent mark is a declaration, never a record, and the old prefix is durably proved | none needed; the next append overwrites the head | derives the same identity; lookup finds nothing; **appends once**. **And any offer outstanding across this position is STALE (v1_6):** the intent-only change moved `intent_generation`, `intent_number`, `intent_event_seq`, `intent_event_sha256` and `head_auth_sha256` while leaving the event tail and **both** committed fields untouched — **invisible to v1_4's binding, and caught by §11.3 gate 2b** (§7.7, §11.4) |
| K-3 | **Unterminated line** — the process died mid-append, a fragment without its final newline is on disk | the old prefix plus one unterminated fragment | a **read-only** read fails closed (`:31890-31901`); it does not guess | **`UNRESOLVED` until the existing recovery runs** — the prefix is not authenticatable end to end without repair, and **a reader never repairs**. After the owned recovery below completes, the exact old prefix is durably proved ⇒ **`PROVED_NOT_ACCEPTED`** | **`recover_interview_journal_tail()`, under the exclusive writer lock**, reached **only** through the already separately authorized recovery-enabled, write-capable entry path's `read_interview_journal(errors, allow_tail_recovery=True)` (§11.2; `:31919-31927`, `:31944-32034`). It truncates that one suffix to the proved length, fsyncs, and re-reads byte for byte; it refuses if the prefix is not a completely valid chain, and it **never touches a complete-but-malformed final line**. **An offer GET never performs it** (§11.2, §14 Phase B) | after recovery the world is K-1; lookup finds nothing; **appends once** |
| K-4a | **Complete event fsynced, committed mark not yet advanced — and the writing attempt STILL OWNS the exclusive lock** | the old prefix plus **one complete, authenticated, correctly chained acceptance event**; head still names the previous record as committed and this record as intent | `present == intent > committed` ⇒ **valid, and the event would be replayed**, provided the last record is exactly the declared one (`:31294-31302`) | **NOT PROJECTABLE — no governed reader can observe this position at all**, because every governed reader needs the lock this attempt holds (§9.6, §10.3 rule 7). To the writing attempt itself the standing is **`UNRESOLVED`** until it proves one side: **the live rollback and `undo_this_record()` remain legal to it here, and only here** (§11.1c) | the active attempt itself: it either advances the committed mark, or rolls back and **durably proves** the old prefix, or reports unresolved | **never blind.** Lookup-first, under the lock, against the governed truth — never against the raw replay of a window a live writer may still legally undo |
| K-4b | **The same complete event, after writer ownership has ENDED** — the process died, or otherwise released the lock, without advancing the committed mark | as K-4a | as K-4a | **`PROVED_ACCEPTED`.** A governed reader now holds the exclusive lock; the whole eight-field head and the history authenticate; the record that landed is exactly the one the head declared. **No live writer retains legal authority to remove it, so removal is forbidden from this point on** (§11.1c, §18 M-13) | none — there is nothing to repair. The next ordinary append writes a head naming the newer record and the window closes | lookup by deterministic identity **finds the record**; `already_recorded`; **zero appends** |
| K-5 | **Committed mark advanced** | the complete acceptance; head names it as both intent and committed | `present == committed`, digests match ⇒ valid; the event is replayed | **`PROVED_ACCEPTED`** — the committed head durably names the event | none | `already_recorded`; **zero appends** |
| K-6 | **Response lost** — any of K-4a, K-4b or K-5, with the caller never told | as that row | as that row | exactly as that row says — **and it is resolved lookup-first, always** | none | lookup by deterministic identity; `already_recorded` where the truth is `PROVED_ACCEPTED`; **zero appends**; **never re-derive a new identity** |
| K-7 | **Live write failure** (not a crash): the append raised while this process still holds the lock | possibly some bytes | not consulted; the writer acts first | **`PROVED_NOT_ACCEPTED` only where the rollback durably restored the exact old prefix and that restoration is proved.** Where the rollback, or its durability, cannot be proved ⇒ **`UNRESOLVED`** — an unproved restoration is never a proof of non-acceptance (§11.1c) | `rollback_partial_journal_append()` restores the segment byte-for-byte to its proved length inside the same `try` (`:32371-32390`), and the failure is reported. **This is the live path, it is legal only to the active attempt under this lock, and it is not what recovers a dead process** | on a **proved** rollback: derives the same identity, lookup finds nothing, **appends once**. On an **unproved** one: **unresolved — zero appends, no retry, no effect replay** |
| K-8 | **Post-write verification failure** after the record is durable and the mark names it | the complete acceptance | valid; the event is replayed | **`PROVED_ACCEPTED`** where the committed head durably names the event **and** a locked stable verification authenticates the history. Where that verification cannot authenticate it ⇒ **`UNRESOLVED`** — truth is not asserted from a re-read that failed | `committed_but_unverified()` — reported as *preserved, standing changed, do not re-run, inspect the journal* (`:32513-32527`). **The record is preserved exactly, in both sub-cases** | **never re-run blind**; a lookup-first retry answers `already_recorded` where the truth is proved, and reports the unresolved standing where it is not. **No refusal record is appended in the unresolved sub-case, because an acceptance may already exist** (§9.2, §15 F-36) |
| K-9 | Crash after commit, before the UI ever saw it | the complete acceptance | valid; the event is replayed | **`PROVED_ACCEPTED`** | none | reload; the governed projection reads `ACCEPTED_FOR_DESIGN_ONLY`; **never re-offer acceptance for the same candidate** |
| K-10 | The journal is unreadable, unauthenticated, chain-broken, or its final line is **complete but malformed** | whatever is readable | **refused** — and tail recovery deliberately does not touch it, because that is corruption, not an interrupted write (`:31965-31967`) | **`UNRESOLVED`** — and never guessed in either direction | none automatic | **fail closed, recovery-required**; no acceptance is claimed **and none is denied**; never write |
| K-11 | An acceptance record exists but its named audit / pass / explanation event does not, or does not match | both readable | valid history, contradictory content | **`UNRESOLVED`** — a contradiction is precisely "neither side safely proved" (§10.4) | none automatic | **fail closed** (§10.4); never repair silently |

**Read across rows K-1 to K-6 and the guarantee is the one this design owes:** every crash position leaves **either the old prefix or exactly one complete acceptance**, and every retry from every position yields **zero or one** total acceptance event — never two, and never a partial event.

**Read down the governed-truth column and the second guarantee, the one v1_4 did not have, is visible as a property of the table (v1_6): there is no row in which a governed reader may expose `ACCEPTED_FOR_DESIGN_ONLY` while a live writer still retains permission to remove that acceptance.** The only row where such permission exists is **K-4a**, and it is precisely the row no governed reader can observe, because the permission and the observation both require the same exclusive lock. **Terminal acceptance, once exposable, is permanent** (§11.1c, §18 M-13).

**C-3 through C-6 of v1_0 are superseded by K-2, K-3, K-4a/K-4b and K-6.** Two errors are corrected explicitly: v1_0's C-3 called a forward mark a state the tail recovery repairs — it is not, there is nothing on disk to recover, and the reader simply accepts the old prefix; and v1_0's C-4 attributed dead-process mid-line recovery to the live rollback — **it is `recover_interview_journal_tail()` under the writer lock, and only that** (K-3, K-7).

**Rule, stated separately because it is the one most often broken:** **a lost response is never a reason to write again.** It is resolved by lookup. This is UDOK's rule 13 applied to this surface, and **K-4b** is the row where it earns its keep: the acceptance record is real before the committed mark moves, so a retry that assumed otherwise would write a second one.

### 12.4 Conflicting same-pass material

If the deterministic identity matches an existing committed acceptance **but** any recorded bound element of that committed event differs from what the current request would bind — a different explanation identity, version or digest; a different `acceptance_scope_digest`; a different predecessor binding; different audit or pass event sequence numbers or digests; a different byte count — then:

- **no append occurs;**
- the request **fails closed** with an explicit conflicting-acceptance refusal;
- the committed record is **preserved exactly** and is neither amended nor superseded;
- the condition is surfaced as recovery-required, in plain words.

**It is never resolved by preferring the newer material, by writing a second acceptance, or by "updating" the first.**

**And it is never resolved by removing the first, either (v1_6).** Where the existing record is one whose terminal acceptance is already exposable — the committed head names it, or a locked stable verification proved it after writer ownership ended — **removal is forbidden to every actor**, and a conflict is surfaced rather than repaired (§11.1c, §18 M-13). The conflict itself is a refusal of this request, but the governed truth reported back is whatever the journal proves: if it proves terminal acceptance stands, then `PROVED_ACCEPTED` is reported even though the request was refused (§11.1b, §16.4). Where the governed truth of the existing record is `UNRESOLVED`, the conflict is reported as unresolved and **still nothing is written** (§11.1b).

### 12.5 What recovery never does

Recovery never replays the effect, never re-derives a fresh identity for the same act, never edits a prior record, never fabricates a missing audit / pass / explanation, never removes a committed acceptance, and never converts "unknown" into "accepted" or into "not accepted". Where the truth is genuinely unknown, the state stays **unresolved and non-terminal**, and says so.

**Which recovery, and what it is allowed to conclude (v1_6).** "Recovery" here is **the existing one and no other**: the same exclusive lock, the same journal, the same eight-field head, and the same one-suffix `recover_interview_journal_tail()` (`nh_loop.py:31944-32034`), reached **only** through the already separately authorized recovery-enabled, write-capable path's `read_interview_journal(errors, allow_tail_recovery=True)` (`:31890`, `:31919-31927`). **No second recovery authority is created, and the offer GET is never a way into it** (§11.2, §14 Phase B).

- **Recovery proves exactly one of three things** — `PROVED_NOT_ACCEPTED`, `PROVED_ACCEPTED`, or `UNRESOLVED` — and it asserts nothing else (§11.1b).
- **Recovery never writes a replacement acceptance merely to resolve uncertainty.** An acceptance event exists because Ness pressed, or it does not exist; it is never manufactured to make a projection definite. **That would be the exact defect this whole design exists to prevent, arriving through the repair path instead of the button** (§18 M-1, M-32).
- **After `PROVED_ACCEPTED`: lookup-first returns the existing acceptance with zero append.** Nothing is re-derived, nothing is re-run, nothing is superseded, and the record may not be removed (§12.1, §12.2, §18 M-13).
- **After `PROVED_NOT_ACCEPTED`: only a NEW explicit browser action may attempt acceptance.** Recovery does not press the button, does not re-press it, and does not resume an interrupted press. The world is simply back to one in which an offer may be computed and Ness may or may not press (§5.1, §14 Phase B).
- **After `UNRESOLVED`: retry and reload remain unresolved, with zero effect replay, until the existing recovery proves the truth.** Repeating the request changes nothing, appends nothing, and is never allowed to tip into either proved answer by repetition (§11.1b, §12.2).

**The honest cost, stated rather than buried:** an `UNRESOLVED` truth can persist until someone with the recovery-capable path resolves it, and this design deliberately provides no automatic escape from it. **An escape would have to guess, and a guess in either direction is the failure mode this section exists to forbid.**

---

## §13 — CONTROLLER, SERVER, AND BROWSER TRUST

### 13.1 The three layers and their authority

| Layer | May do | May never do |
|---|---|---|
| **Controller** | own the fixed scope text; prove the offer; validate the explanation's structure and binding; hold the lock; re-prove everything; append the one event; project the state | claim semantic truth about prose; accept anything on its own initiative |
| **UI server** | check Host and Origin; enforce JSON type, size and exact field set; pass the request to the controller; render the controller's answer | decide acceptance; validate the binding on its own; hold acceptance state; cache an offer as authority; fall back to another route when the controller refuses |
| **Browser / JavaScript** | render what the controller supplied; show the simple and technical views; post the exact offer echo when Ness presses | be authority for anything, in any respect |

### 13.2 The controller proves currency — not the page

The offer's currency is established by the controller **inside the lock at write time**, not by the page's freshness, not by its polling interval (currently 8 seconds — `app.js:632-636`), and not by any client-side comparison. **The page may be arbitrarily stale; the controller's refusal is what makes that safe.**

### 13.3 JavaScript is never authority

- The Accept control's enabled state is a **mirror** of the controller's `acceptance_actionable`.
- A tampered page that posts anyway is refused: the server requires a valid current offer identity and echo, and the controller re-proves everything under the lock.
- No client-side value — no candidate hash, no state string, no boolean, no digest computed in the browser — is ever accepted as evidence.
- Removing the `disabled` attribute in a developer console **accomplishes nothing.**

### 13.4 Host and strict Origin

**Current fact:** the server enforces a localhost `Host` allow-list on every request (`server.py:700-702, 744-747, 801-804`) and sets a restrictive CSP, but **there is no `Origin` check anywhere in `interview_ui/`** — verified by search across the package.

**This design requires both, for the acceptance POST:**

1. `Host` in the existing localhost allow-list — unchanged;
2. **`Origin` present and exactly equal** to this server's own bound origin (scheme, host, and the actual bound port). **Missing, empty, `null`, wildcard, mismatched scheme, mismatched host, or mismatched port ⇒ refuse.** No prefix matching, no suffix matching, no substring matching, no allow-list of extra origins.

`Sec-Fetch-Site: same-origin` may additionally be required `[proposed]`; it is **not** a substitute for the Origin check.

Rationale, stated plainly: the acceptance POST is the first state-changing request in this UI whose meaning is a governance act. A localhost Host check alone does not prevent a cross-origin page in the same browser from issuing a simple request to a local server.

### 13.5 Safe text rendering

- All explanation text is inserted as **text nodes only** — the existing `textContent` / `createTextNode` discipline (`app.js:76-78, 371-384`). **`innerHTML`, `insertAdjacentHTML`, and template-string HTML are forbidden for this content.**
- The existing CSP already forbids inline and third-party script (`server.py:710-714`) and is not weakened.
- Identity strings render inside a code element as text; they are never linkified, never executed, and never used to construct markup.
- The explanation is treated as untrusted text for rendering purposes **even though it passed the controller's structural check** — structure is not safety.

### 13.6 No GET mutation of acceptance state — stated exactly, in v1_6

**The rule, in the only form that is true of every case:**

> **No GET, HEAD, or navigation ever mutates acceptance state, and no GET or HEAD ever reserves acceptance.** The current server already keeps all acceptance mutation in `do_POST`; this design does not change that.

**Three request classes, three honest answers.** v1_4 stated two of them and blurred the third, and the blur was a sentence that could not be true:

| Class | Lock | Journal / head mutated? | Acceptance state mutated? | Appends |
|---|---|---|---|---|
| **A — a legitimate `GET` of the offer route** | **takes the existing exclusive lock**, for one stable authenticated snapshot, and releases it | **NO — zero mutation.** Tail recovery **DISABLED**; no truncation, no fsync, no mark written | no | **zero, always** (§11.2, §14 Phase B, §19, §21 T-46b) |
| **B — a `GET` or `HEAD` at the acceptance-record route, where the journal and lock can safely be appended to** | uses the **existing** writer/journal lock to append the refusal record | **YES — and v1_6 says so plainly.** The refusal record is a real authenticated append: **it mutates the journal and it moves the head** | **NO — never** | **exactly one** `supervisor_operation_completed` (§19); **zero** `supervisor_operation_started`; **zero** `ness_candidate_acceptance_recorded` |
| **C — the same request, where the journal or lock cannot safely be appended to** | none taken, or none obtainable | **NO** | **NO** | **zero.** The refusal is reported in plain words and **success is never claimed** (§15 F-35, §19, §21 T-45a) |

**The sentence v1_4 could not honestly hold, and why it is withdrawn.** v1_4 said of class B that it *"mutates nothing"* and simultaneously that it *"receives one permanent operational refusal record"*, resolving the tension with *"that record is the log of a refused operation, not a mutation of acceptance state."* **The second half of that is true and the first half is not.** An append is a mutation of the journal and of the head; calling it something else does not make the bytes stay still. **v1_6 keeps the true half and deletes the false one:**

- **What class B never mutates is acceptance state.** No acceptance event is appended, no acceptance is reserved, no offer is consumed, no lock is held open, and no projection changes. **`ACCEPTED_FOR_DESIGN_ONLY` is no closer after a thousand refused GETs than after none.**
- **What class B does mutate is the journal and the head**, exactly once, by exactly one refusal record. **This is stated in §9.2, §16.1, §18 M-17 and §19 in the same terms, so no reader can find a version of it that claims otherwise** (§21 T-46c).

**The dividing line remains the route, not the verb** (unchanged from v1_4): a `GET` at the **offer** route is a read; a `GET` or `HEAD` at the **record** route is an attempted mutation that failed closed. **What v1_6 adds is that a read takes a lock, and that a refusal record moves the journal** — two facts v1_4 left out on opposite sides of the same line.

---

## §14 — THE CLICK ALGORITHM

### Phase A — preparation (before any control exists; ordinary mechanical path)

**Rewritten in v1_1 as one finite, non-circular sequence; reordered in v1_2 to make it durable as well; re-owned in v1_3 to make its recovery coherent with its own gates.** Each step names the identity that exists when it begins and the operation that owns the transition. **No step requires a command to run after `next_command = null`; no crash position inside the sequence produces `next_command = null` without a durable actionable offer; and no crash position leaves records that any gate of §11.3 refuses.**

**The placement change v1_2 made remains, but v1_11 corrected the readiness boundary.** v1_1 ordered the last two substantive appends as *pass event, then final explanation*; v1_2 reversed them. The final explanation is therefore durable before the PASS. `mechanical_pass_recorded` remains A6's last **substantive** append, but **it is not sufficient to create `READY_FOR_ACCEPTANCE`**. The matching A6 `supervisor_operation_completed` is the required completion evidence that permits `READY_FOR_ACCEPTANCE`, `next_command = null`, and an actionable offer. A crash after PASS but before that completion therefore leaves runnable same-operation completion-recovery work, not an acceptance-ready state (§6.5a, §7.1a, §11.3 gate 11d).

**The one change v1_3 makes to this table, stated before the table so it cannot be missed.** v1_2 put both of those appends **inside one operation**, and row P-3 claimed the worker could re-enter that operation after a crash between them. **It cannot.** `_record_mechanical_pass()` builds a **fresh** `engine.Operation` on every entry (`commands.py:1444-1448`) whose identity derives over a journal tail that the final-explanation append has already moved (`engine.py:187-205`, `:208-213`; `commands.py:94-125`) — so the re-entry's PASS would land under a **different** operation identity, and v1_2's own gate 11b would then refuse the offer forever from a state with no command left to run. **v1_3 therefore splits the owner: step A5 is its own operation, which completes before step A6's operation is constructed.** The append order is unchanged; what changes is that **the shape after a crash is the same as the shape without one**, so every position below is both owned and acceptable to §11.3 (§6.5a, §7.1b, §11.3 gates 11b–11c).

| Step | What happens | Identity that exists at the start of the step | Operation that owns the transition |
|---|---|---|---|
| **A1** | The candidate's bytes are final and in custody. Its identity `C` = (`candidate_path`, `candidate_sha256`, `candidate_bytes`) is fixed and will not change again in this sequence. | `C` | the existing candidate-custody transaction; unchanged by this design |
| **A2** | The controller prepares **parts 1–6** against `C` — controller-composed, or model-assisted as preparation only (§7.8) — applies the content-stage structural check (§6.6 checks 1–7 over parts 1–6 and 8), computes `explanation_content_digest`, and appends the **content-stage** record: carrier `mechanical_change_explanation_recorded` at the new body version, `explanation_stage = content_fixed`, audit and PASS bindings **explicitly null** (§7.4). Failure ⇒ **no content record, no audit dispatch of the explanation, no offer later**, and the surface says a plain explanation is not currently available. | `C` | the same supervisor operation that records this candidate's change explanation, on the ordinary correction/preparation path — **before** the audit work item is dispatched |
| **A3** | **One** independent semantic audit runs. It reads the actual candidate `C` **and the exact fixed bytes of parts 1–6**, both of which already exist on disk and in the journal, and judges material accuracy. Its result is appended as `mechanical_audit_recorded` by the existing path, recording the `explanation_content_digest` it covered — **an added key on that already registered type at its new body version, not a new event type** (§7.2, §18 M-9a). This is the **final usable audit `A`**. An IMPORTANT or CRITICAL finding ⇒ the candidate is not ready, the loop continues to correction, and **no offer is ever computed** (§6.5). | `C`, content digest | the existing audit-recording operation; unchanged by this design |
| **A4** | The mechanical PASS gate runs over `A`. Every gate boolean and the consumption check pass (`commands.py:1400-1424`). The pass path derives `pass_identity` = `p` from the package scope, the source binding, `C`, `A`'s `audit_identity`, the terminal chain digest, the settled-decision binding, the validation set and the coverage-review sequence (`commands.py:1425-1441`). **`p` now exists as a value. No operation has started, no pass event has been appended, and the projection has not moved** — it is still `WORKING` / `execute-next-claude-task` / `pass_audit_awaiting_gate` (`status.py:1205-1209`). **None of `p`'s ten inputs is a function of the journal tail, so `p` is stable across any crash and re-entry from here on** (§7.1a). | `C`, content digest, `A` | the pass path, **before any operation exists** |
| **A5** | **Its own supervisor operation** `[proposed: the explanation-assembly operation]` starts, appends exactly one final-stage explanation, and completes. If a crash follows the explanation but precedes completion, recovery locates the exact authenticated A5 start, proves the one bound explanation and zero matching completions, reconstructs the original envelope, sets `operation.started_event = original_start`, and appends only the missing matching completion. It does not start A5 again or append another explanation. **A6 is prohibited until replay proves the matching A5 completion is durable.** | `C`, content digest, `A`, `p` | **its own `engine.Operation`**, completed before A6 |
| **A6** | **Only after the completed A5 chain is proved is the distinct PASS operation constructed and started.** It appends exactly one `mechanical_pass_recorded` = `P`, carrying `pass_identity = p` and binding `A`; this is its only substantive append. If a crash follows the PASS but precedes completion, recovery locates the exact authenticated A6 start, proves the completed A5 chain, the one matching PASS and zero matching A6 completions, reconstructs the original A6 envelope, sets `operation.started_event = original_start`, and appends only the missing matching completion. It does not start A6 again or append another PASS. **The projection remains runnable completion-recovery work and no actionable offer exists until A7 is durable.** | `C`, content digest, `A`, `p`, **final explanation** | **a second, distinct `engine.Operation`** — the PASS operation |
| **A7** | The PASS operation completes with `operation.complete("ready_for_acceptance")`. Replay re-reads and proves exactly one matching completion carrying A6's original `supervisor_operation_id` and original start `event_seq` as `supervisor_started_event_seq`. **Only this completed A5/A6 chain permits `READY_FOR_ACCEPTANCE`, `next_command = null`, and an actionable offer.** | all of the above | the PASS operation, closing |
| **A8** | From this moment the offer is a **read-only projection**, computable on any GET with no command, no worker step, and no scheduling (§16.2). The surface is reachable. | all of the above | none — no transition is required |

**The five properties this sequence is built to have, stated so they can be checked one by one:**

1. **Nothing is asked to judge what does not exist.** The audit at A3 reads bytes fixed at A2. The only parts it does not read are part 7, which is derived at A5 from A3's own record, and part 8, which is a controller constant.
2. **The offer is durable before the workflow enters the acceptance-ready non-running state.** The final explanation is appended and A5 completed before A6 starts; the PASS is appended and A6 completed before readiness exists. The ordering and both matching completions are the guarantee; no multi-event atomicity is claimed (§7.1a). A post-effect crash leaves completion-recovery work, not readiness.
3. **The sequence terminates.** A5 creates no new audit and no new PASS, and A6 creates exactly the PASS that A5 already bound, so §7.7's audit, PASS and explanation rows are all false of A5's output from the moment A6 lands (§7.7). There is no second audit to run, so there is no second PASS to record, so there is no second explanation to prepare.
4. **Nothing forward-references an event that does not exist.** Every binding A5 writes names something already on disk or already computed. **`p` is a derivation, not a promise** (§7.4a).
5. **Every reachable arrangement that becomes acceptance-ready passes every gate.** Journal position proves explanation-before-PASS ordering. Gate 11d additionally proves each operation's own authenticated start/completion pair. Recovery preserves the original A5 or A6 identity when completing that operation; it never compares A5's identity with A6's and never requires the explanation or PASS event to carry an operation identity. A partial chain remains non-actionable until completed.

#### Phase A crash positions — every position, its projection, its owner, and whether its records pass the gates (v1_2 table, split and re-owned in v1_3)

**This is the table v1_1 owed and did not state, at the granularity v1_2 did not reach.** The positions are the append boundaries of the sequence above — and because A5 and A6 are now two operations, the window v1_2 called P-3 is really **three** positions, which is precisely why its single-operation account of it could not be true. For each, three questions are asked, not two: *what does the installed projection say; who is able to act on it; and would the records left here pass §11.3?*

| # | Crash position | Durably on disk | Projection the installed code derives | Is an offer shown? | Owner that exists, and what it does | Gates, if a PASS later lands |
|---|---|---|---|---|---|---|
| **P-0** | before A2's append | nothing new | ordinary loop — `WORKING` / `execute-next-claude-task` (`status.py:1211-1214`) | no — and none is owed | **the worker.** Preparation re-runs from the top | n/a |
| **P-1** | after A2, before A3's audit event | content-stage record only | `WORKING` / `execute-next-claude-task` (the audit has not been recorded) | **no** — a content-stage record is never offered (§7.3, §15 F-10, T-13e) | **the worker.** The audit work item is dispatched as normal | n/a |
| **P-2** | after A3, before A5's operation starts | content record + audit `A` | `situation.audit.verdict == "PASS"` and `replay.pass_event()` is null ⇒ **`WORKING` / `execute-next-claude-task`** / `pass_audit_awaiting_gate` (`status.py:1205-1209`) | **no** — no pass event, so §11.3 gate 4 and §15 F-4 refuse | **the worker.** It re-enters the pass path, re-derives the **same** `p` from unchanged inputs, and runs A5 then A6 | **all pass** — the eventual records are the ordinary shape |
| **P-3a** | **inside A5: after its `supervisor_operation_started`, before its record** | content record + `A` + an unmatched start | still **`WORKING` / `execute-next-claude-task`** / `pass_audit_awaiting_gate` — the carrier is read nowhere in `_project()`, and no start event moves it either | **no** | **the worker.** It re-enters, re-derives the identical `p`, finds **no** final-stage record, and appends exactly one under a **new** explanation operation. The stale start stays unmatched and inert (§7.1b) | **all pass after the fresh effect-owning A5 completes.** Gate 11b proves the substantive ordering, and gate 11d identifies the fresh A5 start/completion pair that actually surrounds and owns the final explanation. The older pre-effect unmatched start owns no explanation and is preserved historical residue, so it is not a second qualifying A5 pair |
| **P-3b** | **inside A5: after its record, before its completion** | content record + `A` + **exactly one final explanation bound to `p`** + the original unmatched A5 start | **completion recovery required**; not `READY_FOR_ACCEPTANCE` | **no** | **the existing write-capable recovery path.** It locates the exact authenticated A5 start, proves the original envelope and one explanation with zero matching completions, reconstructs that envelope, sets `operation.started_event = original_start`, and appends only the missing matching A5 completion. It starts no second A5, appends no second explanation, and performs no provider or substantive dispatch. **Only after re-read proves that completion may A6 start.** | gate 11d passes only after the completion carries the original A5 `supervisor_operation_id` and `supervisor_started_event_seq` |
| **P-3c** | **inside A6: after an A6 `supervisor_operation_started`, before the pass append** | the **completed A5 chain** + one or more preserved pre-effect unmatched A6 starts from earlier crashes, including the current unmatched A6 start + **zero PASS events** | still **`WORKING` / `execute-next-claude-task`** / `pass_audit_awaiting_gate` | **no** | **the worker.** On re-entry it re-derives `p`, first proves the completed A5 chain, finds the existing final explanation, leaves every older pre-effect A6 start as preserved historical residue, and constructs a fresh A6 operation for the still-unperformed PASS. It appends no second explanation and reuses no old pre-effect start as the fresh operation's completion owner | **all pass after the fresh effect-owning A6 completes.** Gate 11b(i)–(iii) prove explanation-before-PASS ordering, and gate 11d identifies the fresh A6 start/completion pair that actually surrounds and owns the PASS. Older pre-effect unmatched A6 starts own no PASS and are not qualifying A6 pairs |
| **P-4** | after A6's PASS append, before A7's matching completion | the completed A5 chain + the original A6 start + exactly one PASS + zero matching A6 completions | **completion recovery required**; not `READY_FOR_ACCEPTANCE`; `next_command = null` is forbidden | **no — the PASS alone is insufficient** | **the existing write-capable recovery path.** It reconstructs the original A6 envelope, sets `operation.started_event = original_start`, and appends only the missing matching A6 completion. It starts no second A6, appends no second PASS, and performs no provider or substantive dispatch | gate 11d passes only after replay proves exactly one matching A6 completion carrying the original A6 `supervisor_operation_id` and `supervisor_started_event_seq` |
| **P-5** | after A7 | everything | `READY_FOR_ACCEPTANCE` / `next_command = null` | **yes** | none | **all pass** |

**Read down the last three columns together:** every position before matching A6 completion is either ordinary preparation or same-operation completion recovery. None exposes an actionable offer. Every position that reaches `READY_FOR_ACCEPTANCE` has the exact durable chain A5 start < one explanation < matching A5 completion < A6 start < one PASS < matching A6 completion, and that chain satisfies every lock-time gate. No row has `next_command = null` merely because the PASS exists, and no provider or substantive dispatch runs while completion recovery is outstanding.

**The re-entry at P-2 and P-3a–P-3c is idempotent, and this is stated rather than assumed.** `p` is a pure function of inputs that did not change across the crash — none of them the journal tail — so the re-run derives the same identity. Before appending at A5 the controller **looks up first** — the same lookup-first discipline §12.1 applies to acceptance — for an existing final-stage record bound to `{C, A, p}`:

- **identical `explanation_digest` ⇒ append nothing**, use the existing record, proceed to A6. **No supersession, no version bump, no second record.**
- **a record exists but differs materially ⇒ fail closed** (§7.5 rule 3, §15 F-14). It is never overwritten and never silently preferred.
- **no record ⇒ append exactly one**, as A5 describes.

**Lookup-first prevents duplicate substantive events; same-operation reattachment supplies the missing ownership completion.** Recovery must match the original operation and envelope exactly: `pre_state_sha256`, `input_envelope_sha256`, `supervisor_operation_id`, command, work item, package, source and candidate bindings all come from the authenticated original start and prefix. After that proof, `reconstruct_original_envelope(...)`, `Operation(...)`, `operation.started_event = original_start`, and `operation.complete(...)` append only the missing completion. A matching completion already present is returned with zero append. A mismatch, duplicate or unproved completion state fails closed. No explanation, PASS, start, provider request, Claude dispatch or other substantive effect is replayed.

**If an input did change across the crash** — a newer candidate, a moved source binding, a changed settled-decision binding — then `p` derives differently, the stranded record does not match, **and it is never used.** It stays in history as a superseded explanation (§7.5 rules 2 and 4), the loop returns to preparation for the changed world, and **no offer is ever computed from it** (§7.7, §15 F-8, F-18).

**If A2 or A5 fails, the failure is visible and bounded:** no explanation record exists at that stage, **no PASS is recorded**, no offer is computed, the surface states in plain words that a plain explanation is not currently available, and **no Accept control is presented** (§7.8, §15 F-10). It never proceeds with a partial explanation and never substitutes a correction-stage record for the acceptance explanation (§7.3).

### Phase B — the offer (read-only, and — corrected in v1_6 — read under the existing lock)

- **B0. Take the existing exclusive interview lock, for one stable authenticated snapshot only (v1_6).** The offer read takes the installed `acquire_interview_lock` (`nh_loop.py:32184`) and reads through the installed default read `read_interview_journal(errors)` at `allow_tail_recovery=False` (`journal.py:208-224`). **Tail recovery is DISABLED. Journal mutation is ZERO. Event appends are ZERO. No mark is written, advanced, or repaired.** The lock is released as soon as the snapshot is taken (§11.2, §13.6 class A).
- **B1.** From that one snapshot the controller computes, read-only: state, candidate identity from disk, the exact final usable audit, the exact PASS, the current **final-stage** explanation, its content-stage record, the predecessor evidence, the fixed scope text, the authenticated event tail, **and the complete eight-field authenticated head together with `pre_click_head_digest_sha256` (v1_6)** (§8.2, §8.3a).
- **B1a. The governed truth is projected here, under that same lock (v1_6).** If it is `PROVED_ACCEPTED`, the surface shows the accepted state and **no fresh offer for the same candidate** (§17.4, §21 T-33). If it is `UNRESOLVED`, go to B4. Only `PROVED_NOT_ACCEPTED` can lead to an actionable offer (§10.1, §11.1b).
- **B2.** If every condition holds, it returns a complete offer: the eight parts, the technical facts, `acceptance_actionable = true`, an `acceptance_offer_id` `[proposed]`, `acceptance_offer_binding_sha256`, **the eight head fields, and `pre_click_head_digest_sha256`** (§16.2).
- **B3.** Otherwise it returns `acceptance_actionable = false` with **one plain-language reason** and **no offer identity**.
- **B4. If the journal or the head cannot be authenticated without recovery, the offer is non-actionable and recovery-required, and NOTHING is repaired (v1_6).** The response is `acceptance_actionable = false`, one plain-language reason, **no offer identity**, **no partial offer**, and the governed truth **`UNRESOLVED`**. **Acceptance remains unavailable.** **The GET performs no repair of any kind** — no truncation, no fsync, no tail recovery, no mark write. The repair belongs to the already separately authorized recovery-enabled, write-capable path and is reached only there (§11.2, §12.3 K-3, §12.5, §15 F-1).

**Phase B appends nothing** — it is a read, and a read is not a real operation of the acceptance surface in the §0B sense. **No record is created for computing an offer**, whether the offer is actionable, refused, or recovery-required (§9.2 Case A, §19, §21 T-46b).

**Phase B does, however, take a lock, and v1_6 states that rather than leaving "read-only" to imply otherwise.** It takes the **existing** lock, holds it only for the snapshot, mutates nothing, and appends nothing. **"Takes the existing lock" and "mutates nothing" are both true, and this design says both** (§11.2, §13.6, §16.1, §19).

### Phase C — presentation

- **C1.** The page renders the simple view — all eight parts, in order, as text — and the expandable technical view, both from the same record and the same binding digest.
- **C2.** The Accept control is rendered actionable **only** when the controller said so.

### Phase D — the press

- **D1.** Ness presses. The page POSTs the exact echo (§16.3) — offer id, binding digest, candidate SHA, scope id and digest, explanation identity and digest, and the explicit confirmation flag — and nothing else.
- **D2.** The server checks Host, strict Origin, method, content type, size, JSON object shape, and the exact allowed field set.
- **D2a. What the method check covers, made explicit in v1_4; the lock and mutation facts made explicit in v1_6; the independence of request refusal and acceptance truth made explicit in v1_9.** Phase D is entered by **every** request aimed at the acceptance-record route, not only by a press. A `GET` or `HEAD` at that route — from a typed URL, a navigation, a prefetch, a tampered page, or any other source — fails the method check at D2 and **never reaches D4, never reaches Phase E, never takes the lock for an acceptance transaction, and never appends an acceptance event**. It is a request-level refusal of class F-29, and it takes the **same** D3 handoff as every other request-level refusal. **This request is invalid, but the acceptance truth the response reports is determined by what the locked journal proves, not by the request's invalidity** — if that journal proves terminal acceptance stands, the response says so, even though the request was refused (§11.1b, §16.4). **A `GET` of the offer route is not this case and never enters Phase D**: it is Phase B, a read-only projection that appends nothing — **and which does take the existing lock for one stable snapshot, with tail recovery disabled and zero mutation** (§11.2, §13.6, §16.1, §16.2).
- **D3. Corrected in v1_1 — a request-level refusal still reaches the controller, for recording only. Confirmed in v1_4 to cover the wrong-method GET/HEAD case with no exception. Counted honestly in v1_6, in all three of its cases.** v1_0 ended a failed request at the server with *"no controller call"*, so a refused press left **no permanent record anywhere**, contrary to Master §0B. Instead: the server **refuses the request** — it never proceeds toward an append of acceptance — and then makes **one** controller call whose only effect is to append the operational refusal record of §19, passing the refusal class it determined and the request facts it can safely state. **This is one call for every request-level class alike — F-27 through F-34, the wrong-method GET/HEAD class F-29 included, with no exception (v1_4).** It passes **no** rejected body, **no** unvalidated field, and **no** attacker-supplied text into the record (§19).

  **What that one call does, and does not do, in each of the three cases (v1_6):**

  | Case | The recording call | Journal / head | Acceptance state | Response |
  |---|---|---|---|---|
  | **B — the existing journal and lock can safely be appended to** | uses the **existing** writer/journal lock and appends **exactly one** `supervisor_operation_completed` (§19) — **zero** `supervisor_operation_started`, **zero** `ness_candidate_acceptance_recorded` | **mutated: the record is a real append and the head moves with it, and this design says so** (§9.2, §13.6, §18 M-17) | **never touched** | the refusal, in plain words |
  | **C — the existing journal or lock cannot safely be appended to** | is attempted and fails safely, **or is not attempted at all** | **not mutated — zero appends** | **never touched** | the refusal, in plain words. **Success is never claimed**, and the failure to record is never retried into a second record (§15 F-35, §19, §21 T-45a) |
  | **Neither a success nor a refusal — a live post-write acceptance whose truth is unresolved** | **is not made.** There is no refusal to record, because the operation may in fact have succeeded | **not mutated further** | **not touched further; the existing record is preserved exactly** | the unresolved standing, plainly — no success, no ordinary denial, no instruction to press again (§11.1, §12.3 K-8, §15 F-36, §16.4) |

  **The two things this step may never be made to say:** that an appendable refusal both appends and leaves the journal unmutated, and that every refusal always appends even where recording is unsafe. **Both are false, both were reachable from v1_4's wording, and both are refused here** (§9.2, §15 preamble).
- **D4.** For a request that passes D2, the server hands it to the controller for the acceptance path. **No model is called at any point in this path**, in either branch.

### Phase E — under the lock

- **E1. Recovery-enabled read first.** The controller enters through the existing `read_interview_journal(errors, allow_tail_recovery=True)` (`nh_loop.py:31890`, `:31919-31927`), which takes the exclusive writer lock and calls the existing `recover_interview_journal_tail()` before parsing, so an unterminated suffix left by a dead-mid-append is removed under the lock — at most one, only over a completely valid prefix, never over a complete-but-malformed line (§11.2, §12.3 K-3). A journal that cannot be read or recovered ⇒ **fail closed, zero appends** (§12.3 K-10).
- **E2.** The controller takes the exclusive journal lock for the append transaction.
- **E2a. Re-read and re-authenticate the ENTIRE head under this lock (v1_6)** — all eight fields, with `head_auth_sha256` verifying over the others — and recompute `pre_click_head_digest_sha256` by §8.3a. **Nothing is carried forward from Phase B's snapshot** (§11.3 gates 2, 2a).
- **E3. Lookup first**: does an acceptance with this deterministic identity already exist in the authenticated history? **This lookup reads the history the reader actually returns, including a complete event in the `present == intent > committed` window** (§11.1, §12.3 K-4a/K-4b). **It then resolves the governed truth of §11.1 under this lock (v1_6):** `PROVED_ACCEPTED` with an identical bound record ⇒ **return it, append nothing** (`already_recorded`); `PROVED_ACCEPTED` with material conflicts ⇒ **fail closed** (§12.4); `UNRESOLVED` ⇒ **stop — zero appends, no success, no ordinary denial, no blind retry, no effect replay, and no refusal record while an acceptance may already exist** (§11.1b, §12.2, §15 F-36); `PROVED_NOT_ACCEPTED` ⇒ continue to E4.
- **E4.** Run the entire revalidation list of §11.3 — **gates 2a, 2b and 27 included, so every one of the eight head fields and the complete-head digest must match the offer exactly** (§11.4). Any difference ⇒ **fail closed, zero acceptance appends**, and the refusal is recorded exactly once by §19 **where the journal and lock can safely record it, and not at all where they cannot** (§15 F-35).
- **E5.** Append **exactly one** `ness_candidate_acceptance_recorded` through the existing append path, with its full binding — **including the exact complete pre-click head revalidated at E2a and E4 (v1_6)** — intent mark, record bytes and fsync, committed mark, in the existing order (§9.3, §9.6).
- **E5a. Rollback authority begins and ends here (v1_6).** While this attempt owns this lock and before terminal acceptance is exposable, the existing live rollback (`:32371-32390`) and the existing `undo_this_record()` discipline (`:32397-32439`) are legal to **this attempt and to nothing else**. **From the moment the committed head durably names the event — or, if ownership ends first, from the moment a later locked stable verification proves the complete acceptance still stands — removal is forbidden to every actor, permanently** (§11.1c, §18 M-13).
- **E6.** Release the lock. **No governed terminal acceptance was visible to any reader while it was held, because every governed reader needs this same lock** (§9.6, §10.3 rule 7, §12.3 K-4a).

### Phase F — after

- **F1.** The controller replays and projects **under the existing lock (v1_6)**: where the governed truth is `PROVED_ACCEPTED`, `workflow_state = ACCEPTED_FOR_DESIGN_ONLY`, `acceptance_required = false`, `next_command = null` — exactly and only that (§10.1, §17.1). **Where it is `UNRESOLVED`, that state is not projected at all** and the non-running unresolved condition of §10.5 stands instead.
- **F2. The response reports the standing, and the standing is one of exactly three (rewritten in v1_6, with explicit truth statement for all outcomes added in v1_9).**

  | Request outcome | Governed truth | What the response says | Appends |
  |---|---|---|---|
  | **Request succeeds** | **`PROVED_ACCEPTED`** — the committed head durably names the event, or a locked stable verification proved the complete acceptance after writer ownership ended | the outcome and the committed identity: **an acceptance exists** (`recorded_now`, or `already_recorded` on a lookup-first retry) | the one acceptance event, or none on a retry |
  | **Request is refused** | **`PROVED_ACCEPTED`**, **`PROVED_NOT_ACCEPTED`**, or **`UNRESOLVED`** (determined independently by locked inspection) | **The refusal reason and the standing truth, both plainly.** If the journal proves terminal acceptance stands, the response says `PROVED_ACCEPTED` even though this request was invalid (§11.1b). If it proves non-acceptance, `PROVED_NOT_ACCEPTED`. If neither is proved, `UNRESOLVED`. | zero acceptance events; the §19 refusal record where it can safely be written and the truth is not `UNRESOLVED` with an acceptance possibly existing, none otherwise |
  | **Lookup-first finds existing acceptance** | **`PROVED_ACCEPTED`** | the outcome and the committed identity: **an acceptance already exists** (`already_recorded`) | zero — nothing was appended |
  | **Post-write verification fails** | **`PROVED_ACCEPTED`** or **`UNRESOLVED`** (determined by locked verification) | Where proved, the committed identity under `recorded_now` with the plain-language detail of `committed_but_unverified()`. Where not proved, **the unresolved standing, plainly** — no success, no ordinary denial, no retry instruction (§15 F-36). | the one acceptance event (prior to this step); zero further appends |

  **v1_4 answered the middle window — record durable, intent mark naming it, committed mark not advanced — as an ordinary recorded acceptance.** That is right **after writer ownership has ended and a locked stable verification proves it** (K-4b), and it is **wrong while the writing attempt still holds the lock and may still legally roll back** (K-4a). **v1_6 answers each of those two positions with what is actually true of it**, and answers "I cannot tell" where neither is true.
- **F3.** The page refreshes and shows the accepted state, still showing the package view, the version view, and the explanation.
- **F4. Nothing else happens.** No provider call, no writer, no next package, no Git, no integration, no implementation, no closure, no copy, no `PACKAGE_COMPLETE`.

---

## §15 — FAIL-CLOSED MATRIX

Every row: **zero acceptance appends, no partial state, no silent repair, a plain-language reason, and preservation of everything already recorded.**

**Corrected in v1_1 — "zero appends" is not the same as "no record".** v1_0's preamble said *zero appends*, which read together with M-12 and §19 meant a refused press left nothing permanent anywhere. Master §0B requires the opposite: rejections and failures are among the operations that must be permanently recorded. So every row below means exactly this, and the two halves are not interchangeable:

| | Acceptance events appended | Permanent operational record |
|---|---|---|
| **Every row of this matrix** | **zero — always, without exception** | **exactly one**, through the pre-existing carrier named in §19, **where the existing journal and lock can safely be appended to; zero where they cannot** (v1_6) |

**No row appends an acceptance event. No row appends two records. No row appends a record about that record.** The refusal record states the refusal class and the identities the controller itself proved; it never carries rejected request bytes (§19).

**Stated exactly in v1_6, because v1_4's preamble was reachable as an absolute and is not one.** The refusal-record count is **one where recording is safe, and zero where it is not** — and that is part of the rule rather than an asterisk on it. Nor is every non-success of this surface a refusal at all:

| Situation | Acceptance events | Refusal record | The claim made |
|---|---|---|---|
| **Any row below, where the existing journal and lock can safely be appended to** | **0** | **exactly 1**, through the §19 carrier. **That append mutates the journal and moves the head, and this design says so** (§9.2, §13.6, §18 M-17) | the refusal, plainly |
| **Any row below, where the existing journal or lock cannot safely be appended to** | **0** | **0** — nothing is appended | the refusal, plainly. **Success is never claimed** (F-35, §19, §21 T-23d, T-45a) |
| **Not a row of this matrix at all — a live post-write acceptance whose truth is `UNRESOLVED`** | **0 further** | **0 — no refusal record, because an acceptance may already exist** | **the unresolved standing.** Neither ordinary success nor ordinary refusal; no blind retry, no effect replay (§11.1b, F-36) |

**Two sentences are therefore forbidden anywhere in this candidate (v1_6):** *"every refusal always appends exactly one record"* — false wherever recording is unsafe — and *"an appendable refusal appends a record and causes no journal mutation"* — false because an append **is** a mutation of the journal and the head. **What an appendable refusal never mutates is acceptance state** (§9.2, §13.6, §21 T-46c).

**Confirmed in v1_4 — the matrix has no silent row, and F-29 is not an exception.** Every row above means the same two counts, and **no row of this matrix, and no test of §21, may assign a different count to a request class stated here.** In particular, **F-29 — a wrong method, or a GET/HEAD attempting mutation of the acceptance record — is an ordinary row of this matrix**: zero acceptance events, exactly one operational refusal record. v1_3's §21 T-45 said that one class appended nothing at all; **that statement is withdrawn, and this matrix is what stands** (§9.2, §14 Phase D2a–D3, §16.4, §19, §21 T-45). **The fail-safe case is stated where it belongs and nowhere else:** where the journal or the lock cannot safely record a refusal at all, the refusal is still reported in plain words and **nothing is appended** (§19, §15 F-35, §21 T-23d). **That case is about the journal's own availability, never about which class of request was refused** — F-29 is not exempted by it, and no class is (v1_6).

| # | Condition | Result |
|---|---|---|
| F-1 | Journal unreadable, unauthenticated, or fails HMAC — **or the eight-field head cannot be authenticated (v1_6)** | refuse; recovery-required; **governed truth `UNRESOLVED`** — **neither acceptance nor non-acceptance is claimed** (§11.1b, §12.3 K-10). **An offer GET in this condition returns a non-actionable recovery-required surface and performs no repair whatsoever** (§11.2, §14 Phase B4) |
| F-2 | High-water mark disagrees with the history under the writer's lock | refuse; **repaired by inspection, never by overwriting** |
| F-3 | **The authenticated event tail moved, OR any one of the eight head fields moved, OR the complete-head digest does not recompute (rewritten in v1_6)** | refuse — STALE; reload for a fresh offer. **Every field is compared; none is a summary of another** (§11.3 gate 2b, §11.4). **A valid K-2 intent-only change is a difference here even though the event tail and both committed fields are unchanged, and it stales the offer** (§7.7, §12.3 K-2) |
| F-4 | Projected state is not `READY_FOR_ACCEPTANCE` | refuse |
| F-5 | `acceptance_required` is not true | refuse |
| F-6 | Candidate file missing, unreadable, or recomputes to a different path/SHA/bytes | refuse |
| F-7 | A newer candidate exists in scope | refuse — STALE |
| F-8 | Bound audit is not the exact final usable audit, or a newer or conflicting audit exists | refuse — STALE |
| F-9 | Bound `mechanical_pass_recorded` is not the current one, or a PASS-gate boolean is no longer true | refuse |
| F-10 | Explanation missing, incomplete, structurally invalid, or unbound; or the only record present is a **content-stage** record, or a correction-stage record, rather than a final-stage acceptance explanation | refuse; **no offer is issued at all**; never adapted, never substituted (§7.3) |
| F-10a | The bound explanation's `explanation_content_digest` does not equal the content-stage digest the bound audit read, or the named content-stage record is missing or does not match | refuse — the prose on offer is not the prose that was audited |
| F-10b | Part 7 does not recompute from the bound audit event by the fixed derivation (§6.5a) | refuse |
| F-11 | Explanation binds a predecessor that is not the controller's current parent evidence | refuse |
| F-12 | A superseding explanation exists | refuse — STALE |
| F-13 | Explanation digest does not recompute | refuse |
| F-14 | Two unsuperseded explanations at the same version for one binding | contradiction ⇒ refuse |
| F-15 | `acceptance_scope_digest` differs from the controller's fixed text | refuse — the scope shown is not the scope recorded |
| F-16 | A deliverable Ness question or an open question group exists | refuse |
| F-17 | `settled_decision_binding_sha256` changed | refuse |
| F-18 | Branch, head SHA, or source binding changed | refuse |
| F-19 | An open provider request exists | refuse |
| F-20 | An open provider result custody exists | refuse |
| F-21 | A pending candidate write-ahead exists | refuse |
| F-22 | An open consumption exists | refuse |
| F-23 | An open provider availability probe exists | refuse |
| F-24 | An open audit-usability retry exists | refuse |
| F-25 | A conflicting acceptance exists (§12.4) | refuse; the committed record is preserved untouched |
| F-26 | An acceptance already exists for a **different** candidate in scope | refuse; never absorbed, never superseded |
| F-27 | Non-localhost `Host` | refuse |
| F-28 | Missing, empty, `null`, or mismatched `Origin` | refuse |
| F-29 | Wrong method, or a GET/HEAD attempting mutation — a `GET` or `HEAD` aimed at the acceptance-**record** route, or any other attempt to mutate outside `POST` | refuse; **GET/HEAD never mutates acceptance state**, and **zero acceptance events are appended**. **Where the existing journal and lock can safely be appended to:** exactly **one** `supervisor_operation_completed` through the carrier of §19, by the single recording call of §14 Phase D3, with **zero** `supervisor_operation_started` and no record about that record — **and that append does mutate the journal and move the head, which v1_6 states plainly instead of claiming the refusal mutates nothing** (§9.2 Case B, §13.6, §18 M-17). **Where they cannot:** **zero appends**, the refusal still reported in plain words, and **success never claimed** (§9.2 Case C, F-35, §21 T-45a). **Distinct from a legitimate `GET` of the offer route**, which is not a refusal at all, is not a row of this matrix, and appends nothing — **though it does take the existing lock for one stable snapshot, with tail recovery disabled and zero mutation** (§11.2, §13.6, §16.1, §16.2, §21 T-46b) |
| F-30 | Content type not `application/json` | refuse |
| F-31 | Body empty, over the size bound, non-UTF-8, non-JSON, or not one JSON object | refuse |
| F-32 | Missing required field, unsupported extra field, or wrong value type | refuse |
| F-33 | Offer identity unknown, expired, or not the current one | refuse |
| F-34 | Posted binding digest does not equal the digest recomputed under the lock | refuse — STALE |
| F-35 | Lock cannot be acquired, **or the existing journal cannot safely be appended to** | refuse; **never write without the lock**. **Extended in v1_6, in two directions.** *First, on the recording side:* this is the condition in which a refusal itself cannot be recorded — the refusal is still reported in plain words, **zero is appended**, no retry writes a second record, and **success is never claimed** (§9.2 Case C, §19, §21 T-23d, T-45a). *Second, on the reading side:* **the governed terminal projection needs this same lock, so without it no reader may project terminal acceptance either** — the truth is **`UNRESOLVED`** and is reported as unresolved, never as non-acceptance (§9.6, §10.3 rule 7, §11.1b) |
| F-35a | The journal ends in an unterminated suffix | **not a refusal by itself**: the owned, existing tail recovery runs under the writer lock at Phase E1 and the transaction proceeds over the restored prefix (§11.2, §12.3 K-3). It **becomes** a refusal only if the prefix is not a completely valid chain, or the final line is complete-but-malformed — corruption is never auto-repaired |
| F-36 | Any post-write verification fails **after** the record's bytes are durable | **the record is preserved exactly** (§11.1). The existing `committed_but_unverified()` discipline applies verbatim (`nh_loop.py:32513-32527`): reported as *preserved, standing changed, inspect the journal*, **never as an ordinary failure, never as an ordinary success, and never re-run blindly**. **Split by governed truth in v1_6:** where the committed head durably names the event **and** a locked stable verification authenticates the history ⇒ **`PROVED_ACCEPTED`**, and a lookup-first retry answers `already_recorded` (§12.3 K-8). Where it cannot ⇒ **`UNRESOLVED`** — the response reports the unresolved standing, **no success**, **no ordinary denial pretending certainty**, **no blind retry**, **no effect replay**, and **no refusal record is appended, because an acceptance may already exist** (§9.2, §11.1b, §16.4) |
| F-36a | A **live** append raises **before** the record's final newline is durable | the existing byte-exact rollback restores the segment (`:32371-32390`); reported as a failure, and a retry appends exactly once (§12.3 K-7). **Qualified in v1_6:** that rollback is legal **only** to this active attempt, **only** while it owns the existing lock, and **only** before terminal acceptance is exposable (§11.1c). **`PROVED_NOT_ACCEPTED` requires durable proof that the exact old prefix was restored**; where the rollback or its durability cannot be proved, the truth is **`UNRESOLVED`**, not "no acceptance exists" |
| F-36b | The committed mark cannot be advanced after the record is durable | the existing `undo_this_record()` discipline decides by **asking the disk which side of the rename landed** (`:32475-32500`) — and where the record stands, it is reported as standing. **Never truncated blindly.** **Bounded in v1_6:** this undo is the active attempt's authority under the existing lock and nothing more. **Once the committed head durably names the event, or once a locked stable verification proves the complete acceptance after writer ownership has ended, removal is forbidden to every actor** — no reader, retry, recovery, later writer, or contradiction handler may invoke it against a proved acceptance (§11.1c, §18 M-13). While this attempt still holds the lock, **no governed reader can observe the window at all** (§12.3 K-4a) |
| F-37 | Any model, provider, or subprocess invocation is attempted on this path | refuse; it is a design violation, not a fallback |

---

## §16 — THE LOGICAL HTTP CONTRACT

Logical only. Paths, field spellings, and status-code choices are `[proposed]`; the **behaviour** is settled.

### 16.1 Two operations, one direction

| Operation | Method | Character |
|---|---|---|
| read the offer | `GET /api/acceptance/offer` `[proposed]` | read-only; **never mutates and never reserves**; **appends nothing, however often it is read**; **takes the existing exclusive lock for one stable authenticated snapshot, with tail recovery DISABLED, and releases it (corrected in v1_6)** |
| record the acceptance | `POST /api/acceptance/record` `[proposed]` | the only operation of this design that may change **acceptance state** |

**Corrected in v1_6 — the offer row previously said "never locks", and that is the wrong half of the truth to keep.** The offer must publish one stable authenticated snapshot of the event tail **and** all eight head fields **and** the complete-head digest over exactly them (§8.2, §8.3a); sampled without the lock, those can describe a head that never existed. **So the read takes the existing lock, and mutates nothing.** Both halves are stated here, in §11.2, in §13.6, in §14 Phase B, and in §19 — **and no wording anywhere in this candidate may keep one and drop the other** (§21 T-46c).

**The two operations are distinguished by route as well as by method, and v1_4 states it rather than leaving it to be inferred.** The pairing above is the **only** legitimate one. A request that pairs them differently is not the other operation and is never treated as one:

| Request | What it is | Acceptance events | Operational refusal record | Journal / head moved? |
|---|---|---|---|---|
| `GET` at the **offer** route | the legitimate read-only projection of §16.2; **takes the existing lock, tail recovery disabled, zero mutation** | **0** | **0** — nothing was refused; a read is not an operation of this surface (§19) | **No** |
| `GET` or `HEAD` at the **record** route | a **wrong-method mutation attempt**; refused at §14 Phase D2, never reaching an acceptance transaction (§15 F-29) | **0** | **1**, through the settled carrier of §19, **where the existing journal and lock can safely be appended to**; **0** where they cannot (§9.2 Cases B and C) | **Yes where the record is written — the refusal append moves the journal and the head, and never touches acceptance state. No where nothing is written** |
| `POST` at the **record** route | the acceptance-record operation itself | **1** on success, **0** on any refusal | **0** on success; **1** on a refusal that can safely be recorded, **0** on one that cannot; **0** where the truth is `UNRESOLVED` and an acceptance may already exist | **Yes** on success and on a recorded refusal; **no** otherwise |

**No method other than `GET` at the offer route and `POST` at the record route is a legitimate request of this design**, and every other combination is a request-level refusal with the counts of §16.4.

### 16.2 Offer response (read-only)

**Computed from one stable authenticated snapshot taken under the existing lock, with tail recovery disabled and zero mutation (v1_6)** — §11.2, §14 Phase B0.

Either a complete offer:

- `acceptance_actionable: true`
- `acceptance_offer_id`, `acceptance_offer_binding_sha256`
- the eight explanation parts, in order, as plain text
- the technical facts: candidate path / SHA / bytes; audit identity, event sequence and digest; pass identity, event sequence and digest; explanation identity, version and digest; predecessor identity or the honest "none stated"; package and source binding; the pre-click authenticated event tail
- **the complete pre-click authenticated head (v1_6): all eight fields — `v`, `intent_generation`, `intent_number`, `intent_event_seq`, `intent_event_sha256`, `committed_event_seq`, `committed_event_sha256`, `head_auth_sha256` — and `pre_click_head_digest_sha256`, the canonical complete-head digest over exactly that object** (§8.2, §8.3a)
- `acceptance_scope_id`, `acceptance_scope_digest`, and the fixed scope text as part 8
- **`acceptance_truth: PROVED_NOT_ACCEPTED`** — an actionable offer can exist only over that governed truth (§10.1, §11.1b)

…or an explicit refusal:

- `acceptance_actionable: false`
- exactly one plain-language `reason`
- **no offer identity, and no partial offer**
- **`acceptance_truth` stating which of the three classifications holds (v1_6)**

…or, **new in v1_6 and not a new shape**, the **non-actionable recovery-required surface**, which is that same refusal shape with:

- `acceptance_actionable: false`, one plain-language reason, **no offer identity, no partial offer**
- **`acceptance_truth: UNRESOLVED`**
- and the honest statement that the journal or head cannot currently be authenticated without recovery, that **this read performed none**, and that **acceptance is unavailable until the existing recovery path proves the truth** (§11.2, §12.5, §14 Phase B4, §15 F-1)

**And where the governed truth is `PROVED_ACCEPTED`, there is no offer at all** — the surface shows the accepted state, and **never a fresh offer for the same candidate** (§17.4, §21 T-33).

**None of the published head values is ever client authority.** They are published so the press can echo them and so the controller can prove, under the lock, that the world did not move (§11.3 gates 2a–2b, 27, 28; §13.3).

### 16.3 Request contract

- exactly one JSON object;
- `Content-Type` beginning `application/json`;
- bounded length — the existing `MAX_REQUEST_BYTES = 32_768` bound is more than sufficient and is not raised;
- **exact field set**, in the style the answer path already enforces (`server.py:663-671`): required — `acceptance_offer_id`, `acceptance_offer_binding_sha256`, **`pre_click_head_digest_sha256` (added in v1_6)**, `candidate_sha256`, `acceptance_scope_id`, `acceptance_scope_digest`, `explanation_record_identity`, `explanation_digest`, `ness_action_confirmed` (which must be exactly boolean `true`). **No optional fields. Any unsupported field ⇒ refuse.**
- **The same offer and binding identity that were presented must be the ones posted**, **and the same complete-head digest (v1_6)**. A request that omits them, alters them, or invents them is refused.

**The echo is an echo, never an authority (v1_6).** The POST **echoes or references** the exact offer binding and the exact complete-head digest so that the controller can detect a mismatch — and the controller then **recomputes both under the lock, from the head and history as they then are**, and compares (§11.3 gates 2a, 2b, 27, 28). **A posted digest is never believed, never substituted for a recomputation, and never used to supply a value the controller could not derive for itself.** The eight head fields themselves need not be re-posted field by field; **the controller re-reads them from the head under the lock in every case, and compares each one against what the offer bound** (§11.3 gate 2b). **No client-side value is evidence, here or anywhere** (§13.3, §18 M-16).

### 16.4 Outcomes

| Outcome `[proposed]` | Meaning | Governed truth (§11.1) | Acceptance events appended | Operational refusal records appended |
|---|---|---|---|---|
| `recorded_now` | every gate passed; exactly one event committed | **`PROVED_ACCEPTED`** | **1** | 0 |
| `already_recorded` | the identical acceptance already exists — including from the durable-record window once writer ownership has ended and a locked stable verification proves it (§11.1, §12.3 K-4b) — and the existing record is returned | **`PROVED_ACCEPTED`** | **0** | 0 — nothing was refused and nothing new happened; **a lookup that finds an existing record is not a refusal** |
| `stale_offer` | a bound element moved — **the event tail, any one of the eight head fields, or the complete-head digest (v1_6)**; reload and read the fresh explanation | **`PROVED_NOT_ACCEPTED`** | **0** | **1** where recording is safe; **0** where it is not |
| `refused_conflict` | a conflicting acceptance or a contradiction stands | **`PROVED_ACCEPTED`**, **`PROVED_NOT_ACCEPTED`**, or **`UNRESOLVED`** — the governed truth is determined by locked inspection independent of the refusal (§11.1b, §12.4). If the journal proves terminal acceptance already stands, `PROVED_ACCEPTED` is reported even though this request was refused. | **0** | **1** where recording is safe and the truth is `PROVED_NOT_ACCEPTED` or `PROVED_ACCEPTED`; **0** where recording is unsafe or where the truth is `UNRESOLVED` (§9.2, §15 F-36) |
| `refused_not_ready` | state, PASS, audit, explanation, or an open-work gate refused | **`PROVED_ACCEPTED`**, **`PROVED_NOT_ACCEPTED`**, or **`UNRESOLVED`** — the governed truth is determined by locked inspection independent of the refusal (§11.1b). If the journal proves terminal acceptance stands, `PROVED_ACCEPTED` is reported even though this gate refused the press. | **0** | **1** where recording is safe and the truth is `PROVED_NOT_ACCEPTED` or `PROVED_ACCEPTED`; **0** where recording is unsafe or where the truth is `UNRESOLVED` (§9.2, §15 F-36) |
| `refused_request` | Host, Origin, method, content type, size, or field-set violation — **including a `GET` or `HEAD` aimed at the record route (§15 F-29)** — **recorded through the §14 Phase D3 handoff**, not dropped at the server | **`PROVED_ACCEPTED`**, **`PROVED_NOT_ACCEPTED`**, or **`UNRESOLVED`** — the governed truth is determined by locked inspection independent of the request validity (§11.1b, §14 Phase D2a). If the journal proves terminal acceptance stands, `PROVED_ACCEPTED` is reported even though this request was invalid. | **0** | **1** where the existing journal and lock can safely be appended to and the truth is `PROVED_NOT_ACCEPTED` or `PROVED_ACCEPTED` — **an append that moves the journal and the head, and never acceptance state**; **0** where they cannot or where the truth is `UNRESOLVED` (§9.2 Cases B and C, §13.6, §15 F-36) |
| `refused_unavailable` | the lock, the journal, or the controller is unavailable | **`UNRESOLVED`** where the truth cannot be projected without that lock; **`PROVED_NOT_ACCEPTED`** only where the old prefix is nonetheless durably proved | **0** | **1**, where the journal can be appended to at all; where it cannot, the refusal is reported in plain words and **nothing is appended** (§19) |
| **`unresolved_recovery_required`** `[proposed]` **(v1_6)** | **neither side is safely proved** — the journal or head cannot be authenticated, a rollback's durability cannot be proved, or a post-write verification leaves a durable record whose standing cannot be established (§11.1b, §12.3 K-3, K-7, K-8, K-10, K-11) | **`UNRESOLVED`** | **0** | **0 — none.** A refusal record would assert as refused an operation that may have succeeded (§9.2, §15 F-36) |

**There is no ninth outcome, and there is no partial success.** Every response says plainly **which of the three governed truths holds** — and `unresolved_recovery_required` is how it says the third one honestly.

**Why `unresolved_recovery_required` is a distinct code and not a flavour of an existing one (v1_6).** The unresolved standing is **neither a success nor an ordinary denial**: reporting it as `recorded_now` would claim an acceptance that may not exist, and reporting it as any `refused_*` code would claim a certainty about non-acceptance that is exactly what is missing. **v1_4 had no code that could carry "I cannot tell", so it was forced to choose one of two claims, and both are sometimes false.** This code adds **no** event type, carrier, store, mark, state value, or recovery authority — it is a response label for a condition §11.1 already derives. **Its exact spelling is `[proposed]`, like every other outcome string here (§22.3 item 2).**

**What a client may never do with it:** retry it blind, replay any effect, treat repetition as evidence for either answer, or render it as accepted or as not accepted (§11.1b, §12.5).

**One further outcome is still a report rather than a code (unchanged in substance, corrected in truth by v1_6).** Where the post-write verification fails after the record is durable, **and the committed head durably names the event and a locked stable verification authenticates the history**, the response reports **committed but unverified** under `recorded_now` with the plain-language detail the existing code already produces (`nh_loop.py:32513-32527`) — the acceptance **is** `PROVED_ACCEPTED`. **Where that verification cannot authenticate the history, the same failure is `unresolved_recovery_required` instead**, because then the acceptance is not proved. In neither case is it reported as a refusal, and in neither case is it an instruction to press again (§15 F-36).

**The v1_4 form of that paragraph is superseded and is not repeated.** v1_4 said the committed-but-unverified case always means *"the acceptance exists"* under `recorded_now`. **That is true only where the standing is actually proved**, and v1_6 states both branches instead (§11.1b, §12.3 K-8, §15 F-36).

**A legitimate offer read has no row in this table, and that is not an omission (v1_4).** This table is the outcome set of the **record** operation. Reading the offer is the separate read-only operation of §16.1 and §16.2; its answers are `acceptance_actionable: true` and `acceptance_actionable: false` — the latter including the non-actionable recovery-required surface of §16.2 — **none of which is an outcome code here, and none of which appends anything, however often it is read**. **Corrected in v1_6:** that read does take the existing lock for one stable authenticated snapshot, with tail recovery disabled and **zero mutation**; **taking a lock is not appending, and neither fact is dropped in favour of the other** (§11.2, §13.6, §14 Phase B).

**The only GET or HEAD that produces a row of this table is one aimed at the record route, and its row is `refused_request`** — zero acceptance events, and **one** operational refusal record where the existing journal and lock can safely be appended to, **zero** where they cannot (§9.2 Cases B and C, §15 F-29, F-35).

### 16.5 Response discipline

Responses carry no model prose, no invented explanation, and no claim beyond the outcome and the committed identity. The existing security headers and `no-store` caching apply unchanged. Request bodies are never written to the web-server access log — the existing log discipline (`server.py:694-698`) is preserved.

**Added in v1_6, because a response is where a truth claim is actually made; clarified in v1_9 to make explicit the independence of request outcome and acceptance truth:**

- **Every response of both operations states which of the three governed truths holds** — `PROVED_ACCEPTED`, `PROVED_NOT_ACCEPTED`, or `UNRESOLVED` — **and states nothing stronger than what was proved under the lock** (§11.1b).
- **REQUEST OUTCOME AND ACCEPTANCE TRUTH ARE INDEPENDENT.** A response saying "your request was refused" may truthfully also say "but this acceptance stands." The three governed truths are determined by locked inspection of the authenticated journal, not by whether the current request succeeded or failed. Even a refused request reports whichever truth the locked journal proves (§11.1b, §16.4).
- **A response never claims acceptance that a governed reader could not project**, and never claims non-acceptance that was not durably proved. **"I cannot tell" is a permitted answer here and is preferred to either false certainty** (§18 M-32).
- **A response never invites a blind retry of an unresolved standing**, and never implies that repeating the request will settle it. What settles it is the existing recovery path proving one of the two proved classifications (§12.5).
- **A response never describes an appended refusal record as leaving the journal unchanged.** Where a refusal was recorded, the journal and head moved; where it was not, nothing was appended and the refusal is still reported (§9.2, §13.6, §15 preamble).

---

## §17 — POST-ACCEPTANCE STATE

### 17.1 Exactly this, derived by replay

```
workflow_state    = ACCEPTED_FOR_DESIGN_ONLY
acceptance_required = false
next_command      = null
```

Derived by replaying the authenticated journal — **not stored as a flag, not cached, not remembered by the UI, and not held anywhere else.**

### 17.2 Terminal and non-running

- The state is **terminal for this workflow**: no command follows it.
- It is **non-running**: the worker executes nothing in it (it joins the existing non-running set — reference-only, §20).
- It is **not** a pause, **not** a wait, and **not** a hold. There is no next step inside this workflow.
- A second acceptance of the same candidate is impossible (§12.2). An acceptance of a different candidate in this scope is refused (§15 F-26).

### 17.3 The candidate is byte-identical

The accepted file is not rewritten, re-stamped, re-headed, annotated, moved, renamed, copied, or promoted. **Its internal `DESIGN CANDIDATE — NOT ACCEPTED` wording is not edited in place** — exactly as the AIC and UDOK receipts describe for their own accepted sources. The journal record is the acceptance; the file is untouched.

### 17.4 What the browser shows afterwards

- The package view and the version view remain (§6.8).
- The explanation remains readable, in both simple and technical views, still bound.
- The acceptance card states, from the projected state and not from any feed claim, that this exact candidate is accepted for **design-only** status, and repeats the fixed non-authorizations. **This projection is based on what the locked journal proves, not on whether the browser's current request succeeded** (§11.1b, §16.4). If the journal proves `PROVED_ACCEPTED`, the card shows the acceptance whether this page load's request was valid, invalid, refused, or a simple offer read (§14 Phase B, Phase D2a).
- The existing sentence *"Nothing has been accepted, adopted, integrated, implemented, committed, or pushed automatically"* remains **true**: the acceptance was not automatic, and nothing was adopted, integrated, implemented, committed, or pushed at all.

### 17.5 What does not happen — enumerated

**No** provider or model call. **No** writer, promotion, or candidate creation. **No** next package started, unlocked, or scheduled. **No** Git operation of any kind. **No** Master or Map integration. **No** Register or component ID assignment. **No** implementation, coding, or build authorization. **No** closure record, acceptance receipt, or any Markdown file generated or copied. **No** `PACKAGE_COMPLETE`. **No** dependency closed. **No** production or live N.H disk change.

### 17.6 The next-package transition stays OPEN and SEPARATE

Whether reaching `ACCEPTED_FOR_DESIGN_ONLY` should ever automatically begin a next package is **not decided by this design and is not designed here.** It remains an open item with its own owner (§22.3). Today, nothing follows acceptance.

---

## §18 — NEGATIVE INVARIANTS AND MUST-NEVERS

**M-1** Never accept anything on any model's authority, initiative, inference, default, or silence.
**M-2** Never make Accept actionable without a complete, current, bound eight-part explanation.
**M-3** Never infer understanding from a hash, an ID, a state value, a raw diff, a model summary, or a defect packet.
**M-4** Never claim that a deterministic check over prose proves the prose is true, accurate, complete, or understood.
**M-5** Never claim that a click proves reading or understanding — only invocation after presentation.
**M-6** Never call a model, provider, subprocess, or network endpoint on the acceptance request path.
**M-7** Never route acceptance through `record-ness-answer`, `answer_recorded`, or any question mechanism.
**M-8** Never confuse acceptance with a provider phase `accepted`, `provider_request_accepted`, or any `ACCEPTANCE_AUTHORITIES` value.
**M-9** Never create a second journal, store, marker, sidecar, cache-as-authority, or acceptance state outside the existing authenticated journal.
**M-9a** Never introduce a second new authenticated event type. `ness_candidate_acceptance_recorded` is the only added name; the explanation and the refusal record travel on **existing registered types at new body versions** (§7.2, §19). An unnamed, `[proposed]`-labelled, or "to be decided later" second event type is the same violation as a named one.
**M-10** Never create a second append path, a second high-water mark or committed mark, a second lock, a second tail-recovery mechanism, or a second acceptance gate.
**M-11** Never append more than one event for one click — **one** acceptance event when it succeeds, **one** operational refusal record when it is refused **and the existing journal and lock can safely record it**, and never both, and never two of either. **Stated in full in v1_6:** where recording is unsafe the count is **zero** and the refusal is still reported (§15 F-35); and where the truth is `UNRESOLVED` with an acceptance possibly already durable, the count is also **zero**, because that is not a refusal at all (§9.2, §11.1b, §15 F-36).
**M-12** Never append an acceptance event on any refusal, and never let a refusal cause a partial, provisional, or corrected acceptance record. **Corrected in v1_1:** this is not a rule that refusals go unrecorded — a refusal receives exactly one permanent operational record through the carrier of §19, because Master §0B requires failures and rejections to be permanently recorded. **Bounded in v1_6, so the rule is never read as an absolute it cannot be:** *"exactly one"* holds **where the existing journal and lock can safely be appended to**; where they cannot, **nothing is appended, the refusal is still reported in plain words, success is never claimed, and no retry writes a second record** (§9.2 Case C, §15 F-35, §19).
**M-12a** Never write rejected request bytes, unvalidated fields, or attacker-supplied text into the refusal record, and never let the volume of refusal records become the thing that decides whether a refusal is recorded.
**M-13** Never rewrite, amend, delete, or supersede a committed acceptance. **Extended in v1_6, because "committed" was the only case v1_4 protected:** **never remove a complete acceptance once terminal acceptance is exposable** — that is, once the committed head durably names the event, or once a locked stable verification proves the complete acceptance remains after writer ownership has ended. **Rollback and `undo_this_record()` are legal ONLY to the active append attempt, ONLY while it owns the existing exclusive lock, and ONLY before that point** (§11.1c, §14 Phase E5a). **No reader, retry, recovery, later writer, or contradiction handler may remove one, and no governed reader may ever expose `ACCEPTED_FOR_DESIGN_ONLY` while a live writer still retains permission to remove it** (§9.6, §10.1, §12.3 K-4a).
**M-14** Never resolve a contradiction by preferring the newest record.
**M-15** Never write from a remembered pre-lock read; always re-prove under the lock.
**M-16** Never trust a client-supplied value as evidence.
**M-17** Never mutate **acceptance state** on GET or HEAD, and never reserve acceptance on GET or HEAD. **Stated exactly in v1_6, because the shorter form was reachable as a claim this design cannot make:** a wrong-method `GET`/`HEAD` at the record route is refused, and where the existing journal and lock can safely record it, the one `supervisor_operation_completed` refusal record **does mutate the journal and does move the head** — it is a real append, and this design says so rather than describing it as no mutation. **What it never touches is acceptance state**: no acceptance event, no reservation, no consumed offer, no projection change (§9.2, §13.6, §15 F-29, §19). **And a legitimate offer `GET` mutates nothing at all, though it does take the existing lock for one stable snapshot with tail recovery disabled** (§11.2, §14 Phase B).
**M-18** Never accept a request without a localhost Host **and** a strict exactly-matching Origin.
**M-19** Never render explanation text as HTML; text nodes only.
**M-20** Never present a simple view and a technical view from different records or different bindings.
**M-21** Never invent, guess, or infer a predecessor; where there is none, say so.
**M-22** Never hide a real MINOR audit leftover; never offer acceptance over an IMPORTANT or CRITICAL finding.
**M-23** Never let free prose override evidence or the fixed scope.
**M-24** Never edit, shorten, soften, extend, or paraphrase the fixed non-authorization text.
**M-25** Never modify the accepted candidate's bytes, path, or name.
**M-26** Never generate, copy, project, move, promote, or delete any file as a consequence of acceptance.
**M-27** Never perform a Git operation.
**M-28** Never mark `PACKAGE_COMPLETE`, close a dependency, or create a closure record.
**M-29** Never adopt or integrate into Master or Map, and never assign a Register or component ID.
**M-30** Never authorize implementation, coding, or building.
**M-31** Never start, unlock, or schedule a next package.
**M-32** Never treat absence of a failure record as proof of success, and never convert unknown into accepted or into not-accepted. **Named in v1_6:** "unknown" is the governed truth **`UNRESOLVED`**, and it is **reported as unresolved** — never as `ACCEPTED_FOR_DESIGN_ONLY`, never as an ordinary denial pretending certainty, never resolved by a blind retry, never resolved by replaying an effect, and **never resolved by writing a replacement acceptance** (§11.1b, §12.5, §16.4). **`PROVED_NOT_ACCEPTED` requires durable proof that the exact old prefix stands; an unproved rollback is `UNRESOLVED`, not non-acceptance** (§11.1c).
**M-33** Never truncate an over-bound explanation; refuse it.
**M-34** Never use the acceptance record as additional evidence for the design's correctness (§0B no double evidence).
**M-35** Never log about the logging of the acceptance, and never log about the logging of a refusal (§0B one operation, one log). One press produces at most one record: **the acceptance record, or the refusal record, and never a record describing either of them.** A read that computes an offer is not an operation of this surface and produces **no record at all** — **and, stated in v1_6, that stays true even though the read takes the existing lock for one stable snapshot: taking a lock is not an operation to be logged, and no offer read is ever logged as one, actionable or not, however often it is read** (§11.2, §14 Phase B, §19, §21 T-46b). **Also stated in v1_6:** where a refusal cannot safely be recorded, **the absence of the record is not itself logged either** (§15 F-35, §19).
**M-36** Never let the acceptance event become a feed card, and never let `claims_acceptance` become true.
**M-37** Never edit any code file as part of this design.

---

## §19 — COMPONENT-SPECIFIC §0B LOGGING

- **One real operation, one log.** The press is one operation and receives exactly one permanent record — **and so is every other request aimed at the acceptance-record route, including one refused for its method before it could become a press (v1_4).** No record-about-the-record is created. **The offer read is a read-only projection and creates nothing** — reading is not an operation of this surface.

  **Three qualifications v1_6 adds, because "one operation, one log" was being read as more absolute than it can be:**

  1. **"One log" means one log where the log can safely be written.** Where the existing journal or lock cannot safely be appended to, the count is **zero** and the refusal is still reported in plain words (§9.2 Case C, §15 F-35). **Never say every refusal always appends.**
  2. **The log that is written is an append, and an append moves the journal and the head.** A refusal record is a real authenticated event: **it mutates the journal and the head, and never mutates acceptance state.** **Never say an appendable refusal both appends and causes no journal mutation** (§9.2 Case B, §13.6, §18 M-17).
  3. **Not every non-success is a refusal.** A live post-write acceptance whose governed truth is `UNRESOLVED` is **neither ordinary success nor ordinary refusal**, and it receives **no additional refusal append while an acceptance may already exist** — such a record would assert as refused an operation that may have succeeded (§11.1b, §12.3 K-8, §15 F-36).

- **The offer read takes the existing lock and still creates nothing (v1_6).** It acquires the installed `acquire_interview_lock` (`nh_loop.py:32184`) for **one stable authenticated snapshot**, reads through the installed default `read_interview_journal(errors)` at `allow_tail_recovery=False` (`journal.py:208-224`), **performs zero journal mutation and zero appends**, and releases the lock. **Tail recovery is DISABLED on that path, always.** **Holding a lock is not an operation to be logged, and no offer read is logged** — actionable, refused, or recovery-required, however many times it is read (§11.2, §14 Phase B, §18 M-35, §21 T-46b). **Where the journal or head cannot be authenticated without recovery, the offer returns a non-actionable recovery-required surface and performs no repair; the repair belongs to the already separately authorized recovery-enabled, write-capable path** (§12.3 K-3, §12.5, §15 F-1).
- **Refusals are recorded. Corrected in v1_1.** v1_0 said a refusal appends nothing and left refusal logging OPEN. That is not compatible with the governing text: `NH_MASTER-20_CORRECTED_v10.md` §0B expressly includes **rejections and failures** among the operations that must be permanently recorded, and states that a component without explicit mandatory operational recordkeeping is **incomplete and must not be adopted**. So this design decides it, here, and decides it without a second store and without a second event type:

  **The carrier: `supervisor_operation_completed`, an existing registered event type (`schema.py:740-756`), at a new body version.** It is the installed system's own record of *how a supervisor operation ended*: it already carries `supervisor_command`, `operation_outcome` from the fixed `OPERATION_OUTCOMES` set (`constants.py:219-227`), `controller_returncode`, `controller_report_sha256`, `post_state_sha256`, and a dependency slot. A refused acceptance attempt is exactly that — a supervisor operation that ended without doing what it was asked to do.

  **The count: exactly one record, and exactly which one.** A refused attempt does **no work between a beginning and an end** — it is refused at one point, having appended no acceptance event. Under §0B's *one real operation, one log*, its whole operational log is therefore **one `supervisor_operation_completed`**, and **zero `supervisor_operation_started`**: appending a start as well would be a second record of the same single refusal. `supervisor_started_event_seq` is written as **present JSON null**, which is the value the installed writer already emits when there is no start event (`engine.py:476-478`) — **no new shape and no new field is invented for it.** **And zero `ness_candidate_acceptance_recorded`, in every refusal class without exception** (§9.2, §15 preamble).

  **The lock that record is written under, and what writing it costs (v1_6).** The refusal record is appended through the **existing** writer/journal lock and the **existing** append path — no second lock, no second path, no second carrier (§9.6). **That append is a mutation: the journal changes and the head moves.** This design states that plainly wherever the record is described, and states alongside it the thing that is actually protected: **acceptance state is never mutated by it** — no acceptance event, no reservation, no consumed offer, no projection change (§9.2 Case B, §13.6, §18 M-17).

  **The outcome value.** The refusal class maps onto the **existing** `OPERATION_OUTCOMES` members; **no new outcome value is required and none is added.** The exact mapping is `[proposed]` — for example a stale offer or a not-ready gate maps naturally onto `needs_ness`, and a journal, lock, or contradiction refusal onto `safety_hold` — and remains open (§22.3 item 5).

  **What the record carries.** The refusal class, the package/source and candidate binding the controller itself proved, and the offer identity where one was validly presented. **It never carries the rejected body, an unvalidated field, or any attacker-supplied text** (§18 M-12a). Where the controller could prove nothing about the request — a request-level refusal — the record says that in its class, and states nothing it did not prove.

  **Request-level refusals are included.** Host, Origin, method, content-type, size, JSON-shape and field-set refusals (§15 F-27 to F-34) are recorded through this same carrier, by the single recording call of §14 Phase D3. v1_0's *"no controller call"* left exactly these unrecorded, which is the gap Master §0B forbids.

  **The method class is included with no exception, and v1_4 says so at the level of the individual request.** *Method* here means every wrong-method request aimed at the acceptance-record route, **`GET` and `HEAD` expressly among them** (§15 F-29). A rejected mutation attempt is a real external input that was rejected, which is precisely what Master V10 §0B's transparency law requires a permanent record of, and it is one real operation, so under *ONE REAL OPERATION, ONE LOG* it receives exactly **one** log **where the existing journal and lock can safely be appended to** — no start event, no second record, and no record about it — **and zero where they cannot, with the refusal still reported and success never claimed (v1_6)** (§9.2 Cases B and C, §15 F-35, §21 T-45a). **That one log is written through the existing writer/journal lock, and writing it moves the journal and the head; it never touches acceptance state** (§13.6, §18 M-17). **v1_3's §21 T-45 required that same class to append nothing; that requirement is withdrawn in v1_4, and this carrier and this count are what stand** (§9.2, §15 preamble and F-29, §16.4, §21 T-45).

  **What is *not* a refusal, and therefore not recorded here.** A legitimate `GET` of the offer route is a read-only projection. It is refused nothing, it is not a rejected external input, and it creates **no record at all** — not a refusal record, not an offer record, not a read record — **however many times it is read, and whether the offer it returns is actionable, refused, or recovery-required** (§14 Phase B, §16.2, §21 T-46b). **Nor does its taking the existing lock make it one (v1_6):** the lock is held for one stable authenticated snapshot, tail recovery is disabled, **zero is mutated and zero is appended**, and the lock is released. **The dividing line is the route the request was aimed at, not the verb alone:** a `GET` at the offer route is a read; a `GET` or `HEAD` at the record route is an attempted mutation that failed closed, and it is recorded exactly once **where recording is safe**.

  **What is also *not* a refusal, added in v1_6.** A live post-write acceptance whose governed truth is `UNRESOLVED` is **neither ordinary success nor ordinary refusal** (§11.1b). **It receives no refusal record while an acceptance may already exist**, because a refusal record would state that an operation was refused when it may in fact have succeeded — a false permanent record, which §0B's transparency law does not ask for and this design will not write. **Nothing is appended, the standing is reported honestly as unresolved, and the existing record — if there is one — is preserved exactly** (§12.3 K-8, §15 F-36, §16.4).

  **Where recording itself fails**, the refusal is still reported to Ness in plain words and **nothing is appended**. An unrecordable refusal is never upgraded into a success and never retried into a second record. **So the honest count for this design is "one where recording is safe, zero where it is not, and zero where there was no refusal to record" — never "always exactly one" (v1_6)** (§9.2, §15 preamble, §18 M-11, M-12).

  **No record about that record.** The refusal record is the log of the refusal. Nothing logs that it was written (§18 M-35).
- **No double evidence.** The acceptance record proves the act. It adds no weight to the audit, the PASS, the explanation, or the design.
- **Connected, not passive.** The acceptance record is bound to the audit, PASS, explanation, candidate, source, and journal position, so the whole act is reconstructable from durable truth alone.
- **Cooling.** Cooling rules for this record type are **not set here**; they are governed by §0B's cooling-rule governance and remain open with their proper owner. This record is a high-impact governance record and would sensibly stay active longer than routine operational logs — **but that is a rule for Ness to approve, not for this design to set.**
- **Privacy.** The record contains identities, digests, controller-owned fixed text, and Ness's own explicit action. It contains no third-party material, no Level 1 secret, and no credential. The eight parts are Ness-facing prose about N.H's own design.

---

## §20 — IMPLEMENTATION SURFACE — REFERENCE ONLY

**This section names where a later, separately authorized implementation would most plausibly touch. It is a map, not an instruction, not a plan, and not permission. No file below is edited by this candidate.**

| File | Plausible later relevance |
|---|---|
| `controller/nh_loop.py` | the acceptance command would be reached by the **existing** generic supervisor dispatch (`:45946-45949`) once registered, and would reuse the existing append, lock, two-mark, rollback, and tail-recovery machinery unchanged; the acceptance entry read is the existing `read_interview_journal(errors, allow_tail_recovery=True)` (`:31890`) |
| `controller/nh_supervisor/schema.py` | the body-key row for the acceptance event, and the **new body-version rows** for the existing explanation and operation-completed carriers, through the existing `{(version, type)}` table (`:778-805`) |
| `controller/nh_supervisor/constants.py` | the ninth workflow state value; the fixed scope text and its id; the identity family prefix; the non-feed set membership; registration of the acceptance command in `SUPERVISOR_COMMANDS` (`:771-783`) if a command is its shape |
| `controller/nh_supervisor/replay.py` | accessors for the acceptance and two-stage explanation events, and the contradiction projections of §10.4 |
| `controller/nh_supervisor/status.py` | the precedence-11.5 rule; the projected state; `acceptance_required` continues to follow from the single existing derivation |
| `controller/nh_supervisor/engine.py` | the existing `Operation.start()` / `.append()` / `.complete()` interface (`:421-490`), used at §14 Phase A step A5 for the explanation-assembly operation and at A6 for the PASS operation, and the existing completion record used as the refusal carrier of §19 — **used, not modified in shape** |
| `controller/nh_supervisor/feed.py` | the per-candidate explanation index (`:44-52`) distinguishing acceptance-stage records from correction-stage ones by their discriminator |
| `controller/nh_supervisor/commands.py` | the acceptance command's gate list, lookup-first step, and single append — **if a command is the right shape at all** — and the `COMMAND_TABLE` entry (`:5216-5227`); plus the pass path (`:1396-1469`), where `pass_identity` is derived before either A5 or A6 substantive work. A5 owns exactly one final explanation and A6 owns exactly one PASS. For a post-effect crash, consume the installed same-operation reattachment pattern already used in this module: reconstruct the original authenticated envelope, build `Operation(...)`, assign `operation.started_event = original_start`, and call only `operation.complete(...)`. Do not call `operation.start()` or repeat the substantive append. The status/readiness path must require matching A5 and A6 completions, and provider/substantive dispatch is prohibited while either recoverable completion remains outstanding |
| `interview_ui/server.py` | the offer and record routes; the strict Origin check; the exact field-set validation |
| `interview_ui/supervisor.py` | projection of the new state and the offer into the UI state |
| `interview_ui/worker.py` | the new state joins the non-running set |
| `interview_ui/static/index.html` | the acceptance card's actionable and accepted states |
| `interview_ui/static/app.js` | rendering the eight parts as text, the technical expander, and the single POST |

**Deliberately untouched unless a real dependency is separately proved:** `interview_ui/production.py`, every provider transport, all candidate-writing machinery, all audit-validation machinery, and everything Git.

**Additionally:** every `cursorrules` Protected File remains protected, `.env` / `.nh_pin.json` / vault / token / key material is never touched, no production store is created, and no marker is created — this design requires none of them.

---

## §21 — OFFLINE DISPOSABLE TEST AND FAULT MATRIX

All tests run **fully offline**, against a **disposable** journal segment and head, with **zero** provider calls and **zero** subprocess model invocations. The real controller, the real governance tree, and the real interview state must remain hash-identical throughout — the discipline the existing rehearsal already requires.

### 21.1 Offer and explanation

| # | Test | Must prove |
|---|---|---|
| T-1 | State is `READY_FOR_ACCEPTANCE` and everything is bound | an offer exists and is actionable |
| T-2 | Any state other than `READY_FOR_ACCEPTANCE` | **no offer at all** |
| T-3 | Explanation present and correctly bound | offer actionable; all eight parts returned in order |
| T-4 | Explanation absent | no offer; plain reason; no Accept control |
| T-5 | Explanation present but bound to an older candidate | stale; no offer |
| T-6 | Explanation present but bound to an older audit or an older PASS | stale; no offer |
| T-7 | A superseding explanation exists | the older one is never offered |
| T-8 | Explanation binds the wrong predecessor | refused |
| T-9 | Candidate genuinely has no predecessor | part 3 carries the honest "no predecessor" statement and passes |
| T-10 | Simple view and technical view compared | same candidate, same binding digest, same record |
| T-11 | A part is empty, duplicated, or made only of hashes/IDs/diff jargon | structural check fails; no offer |
| T-12 | Part 8 altered by one character | digest mismatch; no offer |
| T-13 | Over-bound explanation | refused, **not truncated** |
| T-13a | **Sequence trace, end to end:** run A1→A8 over a disposable journal and record each event and projection | the required durable order is A5 start < exactly one final explanation < matching A5 completion < A6 start < exactly one PASS < matching A6 completion < `READY_FOR_ACCEPTANCE`; A5 and A6 have distinct `supervisor_operation_id` values |
| T-13a1 | **Append-order and ownership test:** compare event sequences and the two start/completion pairs | explanation precedes PASS by `event_seq`; A5 completion matches only A5's original `supervisor_operation_id` and start sequence; A6 completion matches only A6's; no test compares an operation identity on the explanation with one on the PASS |
| T-13a1a | **A5 post-effect crash test:** crash after A5 start and one final explanation but before A5 completion | recovery reconstructs the original A5 envelope, attaches the original start, appends only the missing matching A5 completion, and proves it by reread; exactly one A5 start, one explanation and one matching completion exist; A6 does not start beforehand |
| T-13a1a1 | **A6 post-effect crash test:** crash after A6 start and one PASS but before A6 completion | recovery first proves the completed A5 chain, reconstructs the original A6 envelope, attaches the original start, appends only the missing matching A6 completion, and proves it by reread; exactly one A6 start, one PASS and one matching completion exist; readiness and Accept do not appear beforehand |
| T-13a1b | **Distinct-operation and same-operation-recovery test** | A5 identity differs from A6 identity; each recovered completion preserves its own original `supervisor_operation_id` and original start `event_seq` as `supervisor_started_event_seq`; the explanation and PASS events remain ordered by sequence and are not required to carry operation identities |
| T-13a2 | **No substantive replay test:** run both post-effect crash recoveries repeatedly, including a crash before the recovery completion append lands and a lost response after it lands | no second start, explanation or PASS is appended; before the completion lands retry redoes only lookup and proof; after one complete authenticated completion lands lookup-first returns it with zero append; unproved completion truth fails closed |
| T-13a3 | **Readiness and pre-effect-residue sweep across every Phase A position** | A6 never starts before matching effect-owning A5 completion; `READY_FOR_ACCEPTANCE`, `next_command = null`, and actionable Accept never appear before matching effect-owning A6 completion. P-3a may contain an older unmatched A5 start that owns no explanation, and P-3c may contain an older unmatched A6 start that owns no PASS; those pre-effect starts remain history and do not count as qualifying effect-owning pairs. Gate 11d proves exactly one completed A5 pair owning the explanation and exactly one completed A6 pair owning the PASS, and the complete qualifying six-event chain passes every §11.3 gate |
| T-13a3a | **Pre-effect orphan-start negative test:** construct one P-3a history and one P-3c history containing the preserved old unmatched start plus the later successful fresh operation | each history still produces exactly one final explanation, exactly one PASS, exactly one qualifying completed A5 pair and exactly one qualifying completed A6 pair; the old pre-effect start is not paired to the later completion and does not make gate 11d fail. A variant in which two completed pairs both qualify as owners of the same substantive effect MUST fail closed |
| T-13a4 | **Crash followed by changed or mismatched operation input** | candidate, source, command, work-item, envelope, start-sequence or operation-id mismatch fails closed; no stranded explanation or PASS is reused for another operation or binding |
| T-13a5 | **Recovery-dispatch priority test** | while a recoverable post-effect A5 or A6 start exists, the existing path performs lookup-first same-operation completion recovery before any provider, Claude or substantive dispatch; no new explanation, PASS, acceptance offer or event type is produced |
| T-13b | Parts 1–6 altered by one character after the audit read them, before the final stage | content-digest equality fails (§6.6 check 8); **no final record, no offer — and no PASS event, because A5 precedes A6** |
| T-13c | The audit runs and the final explanation is created; then look for what the design requires next | **no further audit is owed and none is dispatched**; the just-created explanation is **not** stale on arrival by any §7.7 row — including the PASS row, which the very next append satisfies rather than falsifies |
| T-13c1 | **Forward-reference test (v1_2):** inspect the final-stage record's fields | it carries `pass_identity` and **no** pass `event_seq` and **no** pass `event_sha256`; a synthetic record carrying either is **refused** at §11.3 gate 12e |
| T-13c2 | **PASS-identity recomputation test (v1_2):** recompute `pass_identity` from the installed inputs and compare against both the explanation record and the pass event | all three agree; a record whose bound `pass_identity` does not recompute is refused (§6.6 check 10, §11.3 gate 11a) |
| T-13d | Part 7 replaced with prose that the bound audit event does not support | part 7 fails to recompute; no offer (§15 F-10b) |
| T-13e | Only a content-stage record exists; ask for an offer | **no offer**; a content-stage record is never presented, never adapted, and never promoted (§7.3) |
| T-13f | A correction-stage `mechanical_change_explanation_recorded` exists for the same `candidate_sha256`; ask for an offer, and separately read the change feed | the correction-stage record is never offered as the acceptance explanation, **and** the acceptance-stage records never displace it in the feed's per-candidate index (`feed.py:44-52`) |

### 21.2 Binding and refusal

**Read every "zero" below as: zero acceptance events, and exactly one operational refusal record through the carrier of §19 — where the existing journal and lock can safely be appended to, which is the condition these runs are set up in (v1_6). The unappendable case is T-23d and T-45a, where the count is zero and the refusal is still reported without claiming success; and the unresolved case, which is not a refusal and receives no record, is T-23j(c) and T-30a4** (§9.2, §15 preamble).

| # | Test | Must prove |
|---|---|---|
| T-14 | Candidate file changed on disk after the offer | zero acceptance appends |
| T-15 | Newer candidate appears after the offer | zero acceptance appends |
| T-16 | Newer or conflicting audit appears | zero acceptance appends |
| T-17 | PASS event missing or superseded | zero acceptance appends |
| T-18 | Source binding or settled-decision binding changed | zero acceptance appends |
| T-19 | A pending candidate write-ahead exists | zero acceptance appends |
| T-20 | An open provider request, result custody, consumption, availability probe, or audit-usability retry exists | zero acceptance appends, one row per condition |
| T-21 | A deliverable Ness question appears | zero acceptance appends |
| T-22 | The scope digest shown differs from the controller's fixed text | zero acceptance appends |
| T-23 | **Mutation test:** render the offer, POST it, then mutate any bound element between render and the lock | the lock-time revalidation **refuses**; zero acceptance appends |
| T-23a | **Event-type inventory test (v1_1):** enumerate every `(version, type)` row this design requires and diff it against the installed inventory (`schema.py:119-759` plus the version-4 types) | the **only added type name is `ness_candidate_acceptance_recorded`**; every other row is a new **body version** of an already registered type; **no parallel store appears anywhere** |
| T-23b | **Refusal record count, per refusal class of §15**, one row each | **zero** acceptance events; **exactly one** `supervisor_operation_completed` refusal record; **no** `supervisor_operation_started` for it; **no** record about that record |
| T-23c | Refusal record contents inspected for every class | the refusal class and controller-proved identities only; **no rejected body, no unvalidated field, no attacker-supplied text** |
| T-23d | The recording call itself fails on a refusal | the refusal is still reported in plain words; **nothing is appended**; no retry writes a second record |
| T-23e | **Complete-head binding published and echoed (v1_6):** inspect an actionable offer, the POST it produces, and the committed acceptance event | the offer publishes **all eight** head fields — `v`, `intent_generation`, `intent_number`, `intent_event_seq`, `intent_event_sha256`, `committed_event_seq`, `committed_event_sha256`, `head_auth_sha256` — **and** `pre_click_head_digest_sha256`; the POST **echoes the offer binding and the complete-head digest**; the committed event **carries all eight fields and the digest**, and they are exactly the values revalidated under the lock (§8.2, §8.3a, §9.3, §16.2, §16.3) |
| T-23f | **Per-field head staleness sweep (v1_6):** eight runs, each mutating exactly **one** of the eight head fields between render and lock, plus one run mutating only the complete-head digest, plus one run mutating nothing | **each of the ten runs refuses as STALE**, with **zero acceptance appends** (§11.3 gate 2b, §15 F-3); the control run **succeeds**. **A matching digest never rescues an unmatched field, and no field is exempt** |
| T-23g | **The K-2 test — the case v1_4's binding could not see (v1_6):** render an offer, then produce a **valid intent-only head change** (an intent mark advanced with no record bytes landed), leaving the authenticated event tail and **both** committed fields byte-identical; then press | the head **authenticates** and the history is **valid** (`nh_loop.py:31241-31302`), **and the offer is STALE and the press is refused**, with zero acceptance appends. **Re-run against v1_4's binding — authenticated tail plus the two committed fields only — and it does not refuse**, which is exactly why the binding was widened (§7.7, §11.4, §12.3 K-2) |
| T-23h | **Head authentication failure at press time (v1_6):** make `head_auth_sha256` fail to verify over the other seven fields | refuse; **governed truth `UNRESOLVED`**; zero acceptance appends; **neither acceptance nor non-acceptance claimed** (§11.3 gate 2a, §15 F-1) |
| T-23i | **Identity-input isolation test (v1_6):** derive `ness_acceptance_identity` for the same act across two runs whose heads and tails differ | **the identity is identical in both runs.** The eight head fields, the complete-head digest, the tail, and every sequence number are **absent from the identity inputs**, so a retry of the same act still resolves to the existing record (§8.4, §12.2). **A variant that feeds any head value into the identity is itself a failure** |
| T-23j | **Refusal accounting, all three cases, one row each (v1_6):** (a) a refusal with the journal and lock appendable; (b) the same refusal with the journal or lock unappendable; (c) a live post-write acceptance whose truth is `UNRESOLVED` — journal diffed before and after in each | (a) **exactly one** `supervisor_operation_completed`, **zero** `supervisor_operation_started`, **zero** acceptance events — **and the journal and head demonstrably moved**, which the test asserts rather than denies; (b) **zero appends of any kind**, the refusal still reported, **success never claimed**; (c) **zero further appends and no refusal record**, the existing record preserved byte-for-byte, and the response neither a success nor an ordinary denial (§9.2, §15 preamble and F-35, F-36, §19) |

### 21.3 Recording, concurrency, and crash

| # | Test | Must prove |
|---|---|---|
| T-24 | One valid click, with the whole journal diffed before and after | **exactly one** appended event **in total** — the acceptance event — and **no other append of any kind**; correct binding; state becomes `ACCEPTED_FOR_DESIGN_ONLY` |
| T-25 | Two sequential identical clicks | one event total; second returns the existing record |
| T-26 | Two concurrent identical clicks | one winner; one event total; the loser appends nothing |
| T-26a | **Concurrent reader and writer (v1_6):** issue governed acceptance/status projections and legitimate offer reads continuously while one press runs from start to finish | **at no instant does any reader observe `ACCEPTED_FOR_DESIGN_ONLY` while the writing attempt still holds the lock and may still legally roll back**; readers either wait for the lock or report the pre-acceptance world; **the first governed reader to obtain the lock after the append is complete reports `PROVED_ACCEPTED`, and every later one agrees.** **No reader ever sees terminal acceptance appear and then disappear** (§9.6, §11.1c, §12.3 K-4a/K-4b) |
| T-26b | **Concurrent offer reads under load (v1_6):** issue many simultaneous offer reads across a concurrent append | **every offer published describes a head that actually existed** — the eight fields and the complete-head digest are internally consistent in every response, never a mixture of two heads; **zero appends and zero journal mutation from any of the reads**; **tail recovery never runs on any of them** (§11.2, §14 Phase B) |
| T-27 | Conflicting same-pass material against an existing acceptance | fails closed; zero acceptance appends; one refusal record; the committed record untouched |
| T-28 | A different candidate posted against an existing acceptance | never absorbed; refused |
| T-29 | **Crash before the intent mark** (§12.3 K-1) | the reader returns the old prefix as a valid history; **no acceptance**; a retry appends exactly once |
| T-29a | **Crash with the intent mark written and no record bytes** (K-2) | the reader accepts `present == committed < intent` and returns the old prefix; **no acceptance**; a retry appends exactly once; **nothing is ever written from the remembered intent** |
| T-30 | **Crash leaving an unterminated line** (K-3) | a read-only read **fails closed**; the acceptance entry path's `read_interview_journal(errors, allow_tail_recovery=True)` removes exactly that one suffix **under the writer lock** and the prefix returns byte for byte; **no acceptance**; a retry appends exactly once |
| T-30a | **Complete event fsynced, committed mark not yet advanced, after writer ownership has ENDED** (K-4b) — the row v1_0 got wrong and v1_4 got half-right | the actual reader accepts `present == intent > committed` and **replays the acceptance**; a governed reader **holding the existing lock** authenticates the whole eight-field head and the history, finds the record is exactly the one the head declared, and projects **`PROVED_ACCEPTED`** ⇒ `ACCEPTED_FOR_DESIGN_ONLY`; a retry finds it by identity and answers `already_recorded` with **zero appends**. **Removal is forbidden from this point on** (§11.1c, §18 M-13) |
| T-30a1 | **The same complete event while the writing attempt STILL HOLDS the lock (K-4a) — the row v1_4 got wrong (v1_6):** hold the writer lock open in that window and have a separate governed reader attempt an acceptance/status projection | **the governed reader cannot project terminal acceptance at all**, because it cannot obtain the lock; **it never returns `ACCEPTED_FOR_DESIGN_ONLY`**, and it never returns a confident non-acceptance either. Meanwhile the writing attempt **still legally may roll back** in this window (§11.1c). **Run the same scenario against v1_4's unlocked replay projection and it does expose `ACCEPTED_FOR_DESIGN_ONLY` — an acceptance that can then be removed. That is the defect, and this test is its witness** |
| T-30a2 | **Terminal-acceptance permanence sweep (v1_6):** from a `PROVED_ACCEPTED` position, attempt removal by every route this design knows — a reader, a retry, a re-entered writer, the recovery path, and the contradiction handler | **every route refuses.** The complete acceptance is preserved byte-for-byte in all five; **no rollback, no `undo_this_record()`, no truncation, no supersession, and no "repair" removes it** (§11.1c, §12.5, §18 M-13) |
| T-30a3 | **Rollback proof test (v1_6):** two runs of K-7 — one where the rollback durably restores the exact old prefix and that restoration is verified, one where the rollback's completion or durability cannot be proved | run one ⇒ **`PROVED_NOT_ACCEPTED`**, and a retry appends exactly once. Run two ⇒ **`UNRESOLVED`** — **not** reported as non-acceptance, **zero appends**, **no blind retry**, **no effect replay** (§11.1c, §12.3 K-7, §12.5) |
| T-30a4 | **Unresolved-truth sweep (v1_6):** produce each unresolved position — K-3 before recovery, K-7 unproved, K-8 unauthenticatable, K-10, K-11 — and read the response and the journal at each | each reports the **unresolved standing**: **no success response**, **no ordinary denial pretending certainty**, **no blind retry**, **no effect replay**, **zero appends**, **and no refusal record where an acceptance may already exist** (§9.2, §11.1b, §15 F-36, §16.4). Repeating the request at each position **changes nothing and appends nothing**, and never tips into either proved answer by repetition |
| T-30a5 | **Recovery conclusions test (v1_6):** run the existing recovery path from each unresolved position | it proves exactly one of **`PROVED_NOT_ACCEPTED`**, **`PROVED_ACCEPTED`**, or **`UNRESOLVED`**, and **never writes a replacement acceptance to resolve uncertainty**. After `PROVED_ACCEPTED`, lookup-first returns the existing acceptance with **zero appends**. After `PROVED_NOT_ACCEPTED`, **only a NEW explicit browser action** attempts acceptance — recovery never presses, re-presses, or resumes a press. After `UNRESOLVED`, retry and reload remain unresolved with **zero effect replay** (§12.5) |
| T-30b | **Complete-but-malformed final line** | tail recovery **does not touch it**; refuse; recovery-required; **never truncated as if it were an interrupted write** |
| T-31 | **Crash after the committed mark advanced**, before the response (K-5, K-9) | reload finds the existing acceptance; **no second append**; the accepted state is shown from durable truth |
| T-32 | **Response lost, then retry**, run once from the K-4b window and once from the K-5 window | in **both** windows the governed truth is `PROVED_ACCEPTED`, the existing record is returned, `already_recorded`, **zero appends**, and **no new identity is derived** (v1_6 names K-4b, because K-4a is the window in which the writing attempt still owns the lock and no governed reader can observe it) |
| T-32a | **Retry sweep:** retry from every row K-1 through K-6 | every position yields **zero or one** total acceptance event — **never two, never a partial event** |
| T-33 | Reload after acceptance | accepted state shown; **no fresh offer for the same candidate** |
| T-34 | Accepted state observed over time | non-running; no command runs; no scheduling |

### 21.4 Isolation and boundaries

| # | Test | Must prove |
|---|---|---|
| T-35 | Whole flow instrumented | **zero** provider calls, **zero** subprocess model invocations, **zero** network egress |
| T-36 | Whole flow instrumented | **zero** writer activity: no candidate created, promoted, copied, moved, renamed, or deleted |
| T-37 | Whole flow instrumented | **zero** Git invocations of any kind |
| T-38 | Whole flow instrumented | no governance file created or modified; no Markdown generated; no closure record; no `PACKAGE_COMPLETE` |
| T-39 | Before/after tree hashes | **only** the disposable journal segment and its head changed; nothing else in the tree |
| T-40 | Non-localhost `Host` | refused |
| T-41 | Missing / empty / `null` / mismatched-port / mismatched-scheme `Origin` | refused, one row each |
| T-42 | Wrong content type | refused |
| T-43 | Oversize body | refused |
| T-44 | Unsupported extra field, missing required field, wrong value type | refused, one row each |
| T-45 | **`GET` against the record path, and `HEAD` against the record path — one row each — and any other attempt to mutate outside `POST`; the journal diffed before and after, and the whole case then repeated against a disposable authenticated journal (rewritten in v1_4)** | **run with the existing journal and lock appendable — the unappendable case is T-45a (v1_6)** — each case: an **HTTP refusal**; **zero** `ness_candidate_acceptance_recorded`; **exactly one** `supervisor_operation_completed` refusal record; **no** `supervisor_operation_started` for it; **no** record about that record; **no** rejected body and **no** attacker-supplied text in what was appended; **no acceptance state mutated, and nothing reserved**. **The test asserts, rather than denies, that writing that one record moved the journal and the head (v1_6)** — the false form *"nothing mutated"* is what §13.6 withdrew (§9.2 Case B, §18 M-17). On the repeat: the chain still **authenticates end to end**, and the workflow is still **non-accepted**. **v1_3's row required this same class to append nothing at all; that requirement is withdrawn — it contradicted §15 F-29, §16.4, and §19, and no implementation could satisfy both** (§9.2, §14 Phase D2a) |
| T-45a | **The T-45 cases re-run with the journal or lock made unappendable (v1_4)** | the request is **still refused** and reported in plain words; **zero** acceptance events; **nothing appended**; **never reported as success** — the fail-safe exception of §19 and T-23d, unchanged and confined to journal availability |
| T-46 | Tampered page posts with `disabled` removed and no valid offer | refused |
| T-46a | **Every request-level refusal of T-40 to T-45 re-run with the journal diffed** (extended in v1_4 to include the wrong-method rows of T-45, which v1_3 excluded) | **zero** acceptance events **and exactly one** permanent operational refusal record each, through `supervisor_operation_completed` — the case v1_0's *"no controller call"* left with no record anywhere, and **the same count for every class, with no class exempted**. **Run with the journal and lock appendable (v1_6);** re-run with them unappendable and **every class alike appends zero**, still reports the refusal, and **never claims success** — the availability condition exempts no class either (§15 F-35, §21 T-23d, T-45a) |
| T-46b | The offer endpoint read repeatedly, actionable and refused | **zero appends of any kind**; reading creates no record. **Run against `GET /api/acceptance/offer` `[proposed]` specifically, and repeated, so the legitimate-read case is proved distinct from T-45's wrong-method case** (v1_4) |
| T-46b1 | **Offer-read lock and non-mutation test (v1_6):** instrument one legitimate offer read end to end, with the journal segment and head hashed before and after, and the read repeated many times | **the existing exclusive lock IS taken**, held only for one stable authenticated snapshot, and **released**; **tail recovery is never invoked** on this path, at any repetition; **the journal segment and the head are byte-identical before and after, every time**; **zero appends of any kind**. **Both halves must be asserted — that the lock was taken, and that nothing changed — and a variant asserting only one of them is itself a failure** (§11.2, §13.6, §14 Phase B, §19) |
| T-46b2 | **Offer read against a journal that cannot authenticate without recovery (v1_6):** present an unterminated trailing suffix, then read the offer | the response is **non-actionable and recovery-required**: `acceptance_actionable: false`, one plain-language reason, **no offer identity**, **no partial offer**, `acceptance_truth: UNRESOLVED`, **acceptance unavailable**; and the journal and head are **byte-identical before and after** — **no truncation, no fsync, no tail recovery, no mark written.** **The repair is performed only by the already separately authorized recovery-enabled, write-capable path, and only when that path runs** (§11.2, §12.3 K-3, §14 Phase B4, §15 F-1) |
| T-46c | **Static consistency check across the whole candidate (v1_4; extended in v1_6)** | **no** section, table, matrix row, invariant, or test assigns a **different** event count to one request class than §9.2 and §16.4 assign it; in particular **no statement anywhere assigns zero refusal records to a wrong-method `GET`/`HEAD` mutation attempt where recording is safe** (§9.2, §13.6, §14 Phase D2a–D3, §15 preamble and F-29, §16.1, §16.4, §19, §18 M-11, M-17, M-35). **Extended in v1_6 to four honesty checks, each of which must find zero occurrences:** (i) **no sentence says an appendable refusal both appends a record and causes no journal mutation**; (ii) **no sentence says every refusal always appends**, without the where-recording-is-safe qualification; (iii) **no sentence says the offer read never locks**, and **none says it mutates or appends**; (iv) **no sentence permits a governed reader to expose `ACCEPTED_FOR_DESIGN_ONLY` on raw replay alone**, without the lock and the governed truth of §11.1 |
| T-46d | **Truth-classification completeness check (v1_6)** | **exactly three** externally visible classifications exist — `PROVED_NOT_ACCEPTED`, `PROVED_ACCEPTED`, `UNRESOLVED` — **and no fourth appears anywhere**; every §12.3 crash row, every §15 row, every §16.4 outcome, and every response shape maps onto exactly one of them; **`UNRESOLVED` appears nowhere as a workflow state value, an event type, a mark, a stored flag, or a durable protocol** (§10.1, §10.5, §11.1b) |
| T-46e | **No-new-authority inventory check (v1_6)** | the corrections of v1_6 introduce **no** second journal, store, head, mark, protocol, event type, recovery authority, lock, canonicalization, or identity algebra. Diff the required inventory against §21 T-23a's result: **the added event-type name count is still exactly one — `ness_candidate_acceptance_recorded`**; the head is still the installed eight-field head; the lock is still `acquire_interview_lock`; the recovery is still the one-suffix `recover_interview_journal_tail()` reached only from the recovery-enabled write-capable path; and the digest method is still §8.1's (§8.3a, §9.6, §18 M-9, M-9a, M-10) |

### 21.5 End-to-end

| # | Test | Must prove |
|---|---|---|
| T-47 | Full offline browser → server → controller → disposable journal | **exactly one** `ness_candidate_acceptance_recorded` and **no other append**; provider calls **zero**; post-state exactly `ACCEPTED_FOR_DESIGN_ONLY` / `acceptance_required=false` / `next_command=null`; candidate byte-identical |
| T-48 | Quality check exercised end to end | the eight bound parts are present, distinct, nonempty, and not solely IDs/hashes/diff jargon |
| T-49 | **Independent semantic audit exercised, in its actual position (rewritten in v1_1; unchanged in position by v1_2 and v1_3)** | the audit is dispatched **once**, at Phase A step A3; it reads the actual candidate **and the exact fixed bytes of parts 1–6, which already exist when it runs**; its verdict is what the PASS then binds; **material accuracy is judged by that audit and by nothing mechanical**; **no deterministic check anywhere claims semantic truth**; and **no second audit is owed**, because the parts the audit did not read are derived (part 7) or controller-fixed (part 8), not authored |
| T-49a | **Regress test:** after T-49, look for any further audit, PASS, or explanation the design requires | **none exists**. The explanation on offer binds the audit that read it and the `pass_identity` of the PASS that bound that audit, and **no later audit or PASS is created by this sequence to stale it** |
| T-49b | **Ordering-does-not-reopen-the-audit test (v1_2; extended in v1_3):** confirm that the reordering of A5 and A6, **and the separation of their owners**, changed nothing the audit must judge | the audit at A3 reads the same bytes it read in v1_1; **nothing authored is added after it**; the reordering moves only the append positions of two events whose contents the audit was never asked to judge, and the owner split adds only an operation start and completion, which are **not** prose, **not** an audit, and **not** a PASS; **no second audit becomes owed by either change** |
| T-49c | **Reachability test, current v1_11/v1_12 rule:** from the final candidate bytes, trace forward and record, at each step, the projection, the operation or recovery owner, and whether the records so far satisfy §11.3 | the actionable offer is reached only after the durable chain A5 start < one final explanation < matching A5 completion < A6 start < one PASS < matching A6 completion. Before matching A6 completion the state remains ordinary work or same-operation completion-recovery work; provider/Claude substantive dispatch is prohibited while post-effect completion recovery is outstanding. `mechanical_pass_recorded` remains A6's last substantive append, but **matching A6 completion is the readiness gate**. No required command or recovery step appears after `next_command = null`, and no gate refuses any crash/recovery arrangement this sequence legitimately produces |

### 21.6 Fault-injection

| # | Fault | Must prove |
|---|---|---|
| X-1 | Lock unavailable | refuse; never write without the lock |
| X-2 | Either mark rolled back or edited — committed behind the history, or intent more than one past committed | refuse under the writer's lock (`nh_loop.py:31252-31277`); **never repaired by overwriting** |
| X-3 | An earlier journal record altered | refuse; the whole history fails authentication |
| X-4 | Authentication key absent or not owner-only | refuse |
| X-5 | **Live** write fails mid-line, this process still holding the lock | byte-exact rollback (`:32371-32390`); earlier records still readable; **no acceptance**; a retry appends exactly once. **This is the live path and is distinct from X-5a** |
| X-5a | **Dead** process left a mid-line fragment | **`recover_interview_journal_tail()` under the writer lock** removes exactly that one suffix (`:31944-32034`), reached by the entry read of §14 Phase E1; **no acceptance**; a retry appends exactly once. **Live rollback is never what recovers this** |
| X-6 | Directory fsync fails after segment creation | reported as a persistence failure; the existing `undo_this_record()` discipline applies (`:32441-32451`) |
| X-7 | Post-commit re-read fails, with the record durable and the mark naming it | A post-commit reread failure must not unconditionally cause retry to return `already_recorded`. State the already-settled three-way truth: **locked stable authenticated lookup proves one complete terminal acceptance** => `PROVED_ACCEPTED`; lookup-first may return existing/already-recorded; zero new acceptance appends. **Durable evidence proves the old prefix and no acceptance** => `PROVED_NOT_ACCEPTED`. **Neither side can be proved under locked stable authentication** => `UNRESOLVED`; do not say `already_recorded` or not accepted; zero effect replay, zero blind retry, recovery-required/non-running. A mere post-commit reread failure never automatically means `already_recorded` |
| X-7a | The committed-mark advance fails after the record is durable | Require durable proof: **active writer may attempt rollback only under settled rollback rules.** **Exact old prefix restored AND truncate/fsync/readback or existing required durability proof establishes it** => `PROVED_NOT_ACCEPTED`. **Rollback cannot be durably proved** => `UNRESOLVED`; claim neither side; no ordinary success or denial; no additional refusal append merely for uncertainty; no blind retry or acceptance effect replay. **Committed mark names acceptance, or later locked stable authentication proves complete acceptance remains and cannot be removed** => `PROVED_ACCEPTED`. Never equate rollback attempted with old prefix proved restored |
| X-8 | Disk full at append | refuse; no partial record survives |
| X-9 | Two unsuperseded explanations at one version | contradiction; no offer |
| X-10 | Two acceptance events with different identities in one scope | contradiction; fail closed; neither preferred, neither erased |

---

## §22 — WIRING DELTA AND OPEN DEPENDENCIES

### 22.1 Connections (design-level)

| Edge | Direction | Character |
|---|---|---|
| Browser → UI server | request | localhost only; Host + strict Origin; strict JSON |
| UI server → controller | invocation | no decision authority; passes through and renders the answer |
| Controller → authenticated journal | read / append | the **existing** locked, authenticated, append-only path |
| Controller → candidate file | read only | recomputes path / SHA / bytes; **never writes** |
| Controller → replay projection | read | state, precedence, contradictions |
| Explanation record → acceptance event | binding | identity, version, digest, event position |
| Audit + PASS events → acceptance event | binding | identity, event sequence, event digest |
| Acceptance event → projected state | replay | `ACCEPTED_FOR_DESIGN_ONLY` |

### 22.2 Deliberately absent edges

Acceptance → provider. Acceptance → Git. Acceptance → Master/Map. Acceptance → file writer. Acceptance → next package. Acceptance → closure record. Acceptance → implementation. **Each is absent by design, and each absence is a must-never in §18.**

### 22.3 Open items, left open with their owners

1. **Controlled component ID, Register ID, and bundle placement** for this package — open; none assigned; bundle remains *"Not decided yet"*.
2. **Final field spellings, event-body key list, domain labels, identity prefix, HTTP paths, and outcome-code strings** — open.
3. **The explanation carrier — settled in v1_1, with a bounded remainder.** **Settled:** the carrier is the existing registered event type `mechanical_change_explanation_recorded` at a **new body version**, and this design introduces **no second event type** (§7.2, §18 M-9a). **Still open:** the new body version number, the exact spelling of the `explanation_stage` discriminator, and the exact added key list. Only `ness_candidate_acceptance_recorded` is locked.
4. **Numeric thresholds** for the structural quality check (minimum words per part, token ratios, per-part length bounds) — open.
5. **Refusal recording — settled in v1_1, with a bounded remainder.** **Settled:** ordinary refused or failed clicks, including request-level refusals, receive **exactly one** permanent operational record, in the **same** authenticated journal, through the existing `supervisor_operation_completed` type at a new body version, with **no** paired start record and **no** new outcome value (§9.2, §19). **Still open:** the exact mapping of each refusal class onto the existing `OPERATION_OUTCOMES` members, the new body version number, and the added key list. Also open: any **rate or volume discipline** for refusal records — the path is already bounded by the localhost Host allow-list and the existing `MAX_REQUEST_BYTES` limit, and **no throttle, cap, or sampling is designed here**, because a cap that silently dropped refusal records would defeat the §0B rule this item exists to satisfy (§18 M-12a).
6. **Cooling rules** for the acceptance and explanation record types — open; §0B governs; Ness approves.
7. **Who prepares the explanation prose, with which provider or model** — open; **this design chooses none**. **Narrowed in v1_1:** what is now settled is *what* may be prepared and *when* — **parts 1–6 only**, at the content stage, **before** the final audit runs (§7.8, §14 Phase A step A2) — and that **part 7 is derived by the controller and part 8 is a controller constant, so neither is ever prepared by anyone**. **Narrowed further in v1_2, in one direction only:** the open provider question is confined to A2 and can never migrate into the PASS-recording window, because the final stage sits **before** the pass append (§7.1a). Whatever answer this item eventually receives, **it may not introduce a provider call, a subprocess, a network wait, or any other unbounded step into A5** — A5 assembles bytes that already exist. The provider, model, and preparation route for A2 remain open. **Restated for the v1_3 owner, with no change to the prohibition:** A5 now runs as its own bounded supervisor operation rather than inside the PASS operation (§7.1b). **That does not reopen this item and does not soften it.** A5 still authors nothing, and the ban on a provider call, a subprocess, a network wait, or any unbounded step inside it applies to the explanation-assembly operation exactly as it applied when the PASS operation held that append — **an operation of its own is not a licence to make it a preparation step.**
8. **Whether acceptance should ever automatically begin a next package** — **OPEN and SEPARATE**; nothing follows acceptance today.
9. **Any later projection, copy, closure record, or receipt derived from an acceptance record** — open, separate, later, and Ness's.
10. **Master/Map integration, Register-C work, and all implementation, coding, store, runtime, production, and migration work** — open and separately authorized.
11. **Whether the controller-side entry point is a CLI command, a library call, or something else** — open (§20 notes the question rather than settling it). **Corrected in v1_1:** this is open as a **shape** question, not a reachability question. Registered supervisor commands are already reached generically (`nh_loop.py:45946-45949`; §2.5), so *if* the entry point is a supervisor command, it needs registration in `SUPERVISOR_COMMANDS` and a `COMMAND_TABLE` entry and **no new dispatch path**. What is genuinely absent is the acceptance command itself, not a way to reach it. **What is settled** is that the ordering owner inside the controller is named: the final explanation record is appended on the pass path, before the pass event (§14 Phase A step A5), and the recovery-enabled journal read is the acceptance path's entry step (§14 Phase E1). **Settled further in v1_2, and this part is not open:** that append is placed **before** `mechanical_pass_recorded`, and the pass event is its operation's last substantive append (§7.1a, §11.3 gate 11b). **Corrected and settled further in v1_3, and this part is not open either:** that append is owned by **its own** supervisor operation, which completes before the PASS operation is constructed (§7.1b). **v1_2 named the PASS-recording operation as the explanation owner, and that was wrong.** A fresh substantive entry cannot reuse the original operation identity. **v1_11 does not do that:** after an A5 or A6 substantive event is already durable, it uses the installed same-operation reattachment pattern to reconstruct the original envelope, attach the original authenticated start, and append only that operation's missing completion. **The entry-point shape question does not reopen the ordering or the owner question** — both are properties of the pass path, which already exists and is already reached, and both hold whatever shape the separate acceptance entry point eventually takes. **No new dispatch path, no new command, no new event type, and no new recovery mechanism is required by the v1_3 owner**; it opens and closes one more operation through the interface the installed code already provides (`engine.py:421-490`). **Cross-reference added in v1_6, changing nothing about what this item settles or leaves open:** the settled A5/A6 owner and ordering are restated at §6.5a and corrected in the §20 `commands.py` row and the §0 v1_1 trace row, and are checked by §21 T-13a1a1; the offer read's use of the existing lock with tail recovery disabled and zero mutation is at §11.2 and §14 Phase B; the complete eight-field head binding is at §8.2, §8.3a and §11.3 gates 2a–2b; the governed terminal projection and the three truth classifications are at §10.1, §10.3 and §11.1; and the honest refusal counts are at §9.2, §15's preamble and §19. **None of those reopens the entry-point shape question, and none of them is settled by it** — the ordering, the owner, the lock discipline, the head binding, and the truth classification all hold whatever shape the separate acceptance entry point eventually takes.

**What this item leaves genuinely open:** the explanation-assembly operation's exact envelope fields, its work-item binding, and its outcome string remain `[proposed]` for implementation time. General unmatched-start reaping also remains separate. **What is not open is the post-effect A5/A6 case:** an authenticated A5 start followed by its one final explanation, or an authenticated A6 start followed by its one PASS, must receive the missing matching completion through the existing same-operation reattachment pattern before the sequence may advance. This is completion of the already-started operation, not general reaping and not a new recovery authority.
12. **The absent `spec/…v1_13` document** referenced by the installed package docstring — open, as a **documentation and provenance** item (§23 item 2). **Corrected in v1_1:** its absence is **not** a dependency, a blocker, or evidence about the installed command protocol, and this design asserts no reachability prerequisite on it (§2.5).

**Acceptance of this candidate would close none of the above by implication.**

---

## §23 — WHAT COULD NOT BE CONFIRMED FROM SOURCE

Stated honestly, because guessing here would be worse than not knowing:

1. **The ChatGPT project-instruction file's byte identity.** Read in full (340 lines, nonempty, the exact copy). Its SHA-256 and byte count could **not** be computed in this session because the path lies outside the permitted working directory. No number is fabricated for it.
2. **`spec/NH_AUTOMATIC_SUPERVISOR_MECHANICAL_CHANGE_SPEC_v1_13_CANDIDATE.md` does not exist on disk** in this workspace, although `controller/nh_supervisor/__init__.py` names it as the specification the package implements. The only supervisor spec present is the v1_0 candidate in `controller/`. **What v1_13 says about acceptance is unknown and is not assumed.** **This remains true and unresolved in v1_1.** What v1_1 adds is the boundary of what it means: this is a **documentation and provenance gap** — an installed package naming a specification that cannot be read. It says nothing about whether the installed code works, and nothing about whether the installed commands can be reached. Item 3 previously drew that second conclusion, and it was wrong.
3. **CORRECTED IN v1_1 — the previous item 3 was false, and is withdrawn.** v1_0 stated that no supervisor command is dispatched by the installed `nh_loop.py` CLI and that *"the acceptance surface designed here depends on that protocol being reachable"*, treating reachability as an unresolved external prerequisite. **The actual files say otherwise:**
   - `controller/nh_supervisor/constants.py:771-783` registers all ten supervisor commands in `SUPERVISOR_COMMANDS` and freezes them into `SUPERVISOR_COMMAND_SET`.
   - `controller/nh_supervisor/commands.py:5216-5227` maps every one of them to a handler in the single `COMMAND_TABLE`.
   - `controller/nh_loop.py:45946-45949` dispatches them **generically**: `if command in nh_supervisor.constants.SUPERVISOR_COMMAND_SET and command != "execute-next-claude-task": return command_supervisor(command)`. The named-command chain above it (`:45907-45945`) is not the whole dispatcher; v1_0 read it as though it were.
   - `interview_ui/server.py:471-477` already calls `run_controller("supervisor-status")`. Its `except ControllerFailure` fallback is tolerance for an older controller — its own comment says *"Repair31 does not have this command"* — and is **not** evidence that the command is unreachable on the installed one.

   **So there is no reachability prerequisite, and v1_1 asserts none.** The honest statement of what is missing is narrower and unchanged in substance: **the acceptance command, the acceptance primitive, the acceptance HTTP endpoint, and the accepted-only state do not exist today** (§4.2), and their exact spelling and shape remain open (§22.3 item 11). A later, separately authorized implementation would be reached by the **existing** dispatch; **no new or parallel CLI dispatch path is required, proposed, or authorized.**
4. **Whether the disabled acceptance button's exact label text should change** on implementation is a display decision, not a mechanic; it is not settled here.
5. **The Design and Wiring Map contains no entry for an acceptance button, acceptance record, or `ACCEPTED_FOR_DESIGN_ONLY`** — searched and not found. **No Map entry is invented, and no Map change is made.**
6. **Whether any accepted package elsewhere in N.H already defines a Ness-acceptance primitive** that this surface should consume rather than define: the accepted-designs folder was inspected and the closest records are the B-INT-8 *connection* acceptance routes, which concern connection acceptance, not design-candidate acceptance. **They are not treated as this design's owner, and they are not modified.**

---

## §24 — COMPLETENESS SELF-AUDIT

**Not a verdict.** Independent audit and Ness's explicit acceptance are pending and are not claimed, implied, or anticipated.

| # | Required element | Where |
|---|---|---|
| 1 | Status, provenance, candidate-only marking | §0 |
| 2 | Plain meaning in everyday words | §1 |
| 3 | Authority order, owners, sources actually read with recomputed identities | §2 |
| 4 | Frozen scope and non-goals | §3 |
| 5 | Current-state delta, from the actual files | §4 |
| 6 | Existing facts preserved: button deliberately disabled; no primitive, command, endpoint, accepted-only state, or click handler; `READY_FOR_ACCEPTANCE` non-running | §4.2, §4.1 |
| 7 | "Enable the button" refused as a fix; `record-ness-answer` refused as a route | §4.4, §18 M-7 |
| 8 | Locked meaning of the browser action, controller-owned | §5 |
| 9 | The twelve fixed non-authorizations | §5.2 |
| 10 | Acceptance ≠ closure ≠ adoption ≠ integration ≠ implementation | §5.3, §17.5 |
| 11 | Hard understandable surface; actionable only after a proved bound explanation | §6.1 |
| 12 | The eight distinct nonempty parts, with the exact fixed titles | §6.2 |
| 13 | Honest "no predecessor" handling | §6.2 part 3, §7.6 |
| 14 | Design-versus-implementation boundary in part 4 | §6.2 |
| 15 | MINOR disclosed; IMPORTANT/CRITICAL not ready | §6.5 |
| 16 | Simple view mandatory, technical expandable, same binding | §6.3 |
| 17 | No inference from hashes, IDs, state, diffs, model summaries, defect packets | §6.4 |
| 18 | Click proves invocation after presentation, not reading or understanding | §6.7, §9.4, §18 M-5 |
| 19 | Candidate is accepted, not the explanation | §5.1, §9.4 |
| 20 | Minimum binding set — **including, corrected in v1_6, the exact complete authenticated eight-field head and one canonical complete-head digest over exactly that object** | §8.2, §8.3, §8.3a |
| 20a | **The complete pre-click head is bound, published, echoed, recorded, and re-proved (v1_6):** the offer binds and publishes all eight head fields and the complete-head digest; the POST echoes the offer binding and that digest; the acceptance event carries the exact head revalidated under the lock; and immediately before the append the controller **re-reads and re-authenticates the entire head, recomputes the digest, and compares every field and the digest exactly**. **A valid K-2 intent-only change stales the offer even though the event tail and both committed fields are unchanged** | §7.7, §8.2, §8.3a, §9.3, §11.3 gates 2a, 2b, 27, 28, §11.4, §12.3 K-2, §14 Phase B / E2a / E4, §15 F-3, §16.2, §16.3, §21 T-23e, T-23f, T-23g, T-23h |
| 20b | **Echoed values are never client authority (v1_6):** every posted binding and head digest is compared against a value the controller recomputed under the lock from the world as it then is | §11.3 gates 27–28, §13.3, §16.3, §18 M-16 |
| 21 | Any bound change ⇒ STALE ⇒ disabled or refused | §7.7, §15 |
| 22 | Controller, not JS, proves currency | §13.2, §13.3 |
| 23 | Explanation exists before enablement, in two stages, both before the offer; the click calls no model; the final explanation belongs to completed A5, the PASS belongs to distinct A6, and **matching A6 completion — not PASS alone — permits `READY_FOR_ACCEPTANCE`**. Post-effect A5/A6 crashes are recovered by completing the same original operation without replaying the explanation or PASS | §7.1, §7.1a, §7.1b, §7.8, §11.3 gate 11d, §14 Phase A A2/A5–A7 and P-3b/P-4, §18 M-6 |
| 23a | One finite, durable, non-circular sequence from final candidate bytes to an actionable offer, with the owning operation named at every step | §14 Phase A, §21 T-13a |
| 23b | The exact prose on offer is the exact prose the bound audit read, proved by content-digest equality | §6.6 check 8, §11.3 gates 12a–12c, §15 F-10a, §21 T-13b |
| 23c | No later audit or PASS is created by that sequence, so the explanation is never stale on arrival | §6.5a, §7.7, §21 T-13c, T-49a |
| 23d | **Durability of the ordering and completion boundary:** `mechanical_pass_recorded` is A6's last substantive append, but the matching A6 completion is the evidence that permits `READY_FOR_ACCEPTANCE` / `next_command = null`. A crash after explanation or PASS but before its matching operation completion leaves owned same-operation completion-recovery work and never an actionable offer | §6.5a, §7.1a–§7.1b, §11.3 gates 4 and 11d, §14 Phase A crash rows P-0 … P-5, §21 T-13a1a, T-13a1a1, T-13a3 |
| 23d1 | **Coherence of ordering, ownership, and recovery:** every acceptance-ready history contains exactly one qualifying completed A5 pair owning the final explanation and exactly one qualifying completed A6 pair owning the PASS. Explanation-before-PASS ordering is proved by `event_seq`; each qualifying pair's completion is proved against its own start's `supervisor_operation_id` and `supervisor_started_event_seq`. A post-effect crash reattaches to the same original operation and appends only its missing completion. A pre-effect unmatched start that produced no substantive effect may remain preserved historical residue, is never paired to a later fresh operation's completion, and does not count as a second qualifying pair | §6.5a, §7.1b, §11.3 gates 11b–11d, §14 Phase A P-3a/P-3b/P-3c/P-4, §20, §21 T-13a1–T-13a3a |
| 23e | **The pre-PASS binding is exact and not a promise (v1_2):** the explanation binds `pass_identity`, which the installed pass path derives before any append; it carries **no forward event reference**; and the pass event's own sequence and digest are proved under the lock and carried by the acceptance event instead. **Narrowed in v1_3:** it carries **no operation reference either**, and no gate compares one | §7.4, §7.4a, §6.6 check 10, §11.3 gates 11, 11a, 11b, 11c, 12e, §21 T-13c1, T-13c2 |
| 23f | **Re-entry after a crash inside the sequence is idempotent, and — corrected in v1_3 — reachable:** the same `pass_identity` re-derives from inputs that contain no tail-dependent term, lookup-first finds the existing final record, exactly one final explanation and exactly one PASS exist in total, a changed input yields a different identity whose stranded record is never used, and **the records the re-entry writes satisfy every gate** | §14 Phase A crash rows P-2/P-3a/P-3b/P-3c and the re-entry rules, §7.1b, §7.5, §21 T-13a4, T-13a5 |
| 24 | Model assistance is preparation only, no authority | §7.8 |
| 25 | Free prose never overrides evidence or fixed scope | §6.7, §18 M-23 |
| 26 | Package view and version view preserved | §6.8, §17.4 |
| 27 | Mechanical validation checks structure/binding; **the one independent audit checks accuracy against the exact fixed prose, in its actual position in the sequence**; no semantic-truth claim; no second audit owed. **Unchanged in position by v1_2** — the reordering moves only the two appends that follow the audit, adds nothing authored after it, and therefore makes no second audit owed. **Unchanged again in v1_3** — separating the owner of the final-stage append adds only an operation start and completion, which are not prose, not an audit, and not a PASS; the audit still reads exactly the bytes fixed at A2, and **mechanical validation still claims nothing about truth, and now also claims nothing it cannot read** (§11.3 gate 11c) | §6.5a, §6.6, §6.7, §7.1b, §14 Phase A A3, §21 T-49, T-49a, T-49b |
| 28 | Exactly one new authenticated event type, named `ness_candidate_acceptance_recorded`, with the added-name count stated against the installed inventory; **the explanation and refusal carriers are existing registered types at new body versions, not new types** | §0, §4.5, §7.2, §9.1, §19, §18 M-9a, §21 T-23a |
| 29 | One successful click ⇒ **exactly one append in total**, with the full binding; one refused **request** ⇒ **zero acceptance events and exactly one permanent operational record** through a named pre-existing same-journal carrier, request-level refusals included — **and, corrected in v1_4, the wrong-method `GET`/`HEAD` mutation attempt is one of those classes and not an exception**; a legitimate offer read is not a refusal and appends nothing. **Qualified in v1_6, so the count is true in every case: "exactly one" holds where the existing journal and lock can safely be appended to; where they cannot the count is zero and the refusal is still reported without claiming success; and where the truth is `UNRESOLVED` with an acceptance possibly already durable there is no refusal record at all** | §9.2, §9.3, §13.6, §14 Phase D2a/D3, §15 preamble and F-29, F-35, F-36, §16.1, §16.4, §18 M-11, M-12, §19, §21 T-23b, T-23j, T-24, T-45, T-45a, T-46a, T-46b |
| 30 | Not `provider_request_accepted`, not `record-ness-answer`, not adoption, not `PACKAGE_COMPLETE`, not implementation approval | §9.4, §4.3 |
| 31 | §0B one operation / one log, applied to **both** a recorded acceptance and a recorded refusal; no record about a record; no double evidence; **mandatory operational recordkeeping present rather than left open**; **and, corrected in v1_4, a single event count per request class stated identically everywhere it is stated — one rejected mutation operation, one permanent log**. **Made honest in v1_6:** that log is an **append**, so it mutates the journal and the head and is never described as mutating nothing; it is written **where recording is safe** and omitted where it is not; and a case that is not a refusal at all receives no log | §9.2, §9.5, §13.6, §15 preamble, §16.1, §16.4, §19, §18 M-11, M-12, M-17, M-35, §21 T-23j, T-46c |
| 32 | Full revalidation under the lock, immediately before the append | §11.3 |
| 33 | Localhost Host plus strict Origin | §13.4, §11.3 #26 |
| 34 | Any difference ⇒ fail closed, zero acceptance appends, one operational refusal record — **for every row of the fail-closed matrix alike, F-29 included (v1_4)**, subject to the journal-availability case of §19 **and, added in v1_6, to the unresolved case, which is not a refusal and receives no record** | §11.3, §15 preamble, F-29, F-35, F-36, §19, §21 T-23j, T-45, T-45a |
| 34a | **A legitimate offer GET takes the existing lock for one stable authenticated snapshot, with tail recovery DISABLED, ZERO journal mutation, and ZERO event appends, and releases it — and where the journal cannot authenticate without recovery it returns a non-actionable recovery-required / `UNRESOLVED` surface and repairs nothing (v1_6)** | §9.2 Case A, §11.2, §13.6, §14 Phase B, §16.1, §16.2, §19, §21 T-46b, T-46b1, T-46b2 |
| 34b | **A wrong-method `GET`/`HEAD` at the record route is refused through the existing writer/journal lock with exactly one `supervisor_operation_completed`, zero `supervisor_operation_started`, and zero acceptance events where recording is safe — and that append is stated honestly as mutating the journal and the head while never mutating acceptance state; where recording is unsafe, zero is appended and success is never claimed (v1_6)** | §9.2 Cases B and C, §13.6, §14 Phase D2a–D3, §15 preamble, F-29, F-35, §16.1, §16.4, §18 M-11, M-12, M-17, §19, §21 T-23j, T-45, T-45a, T-46c |
| 34c | **Two sentences forbidden, and one case that is not a refusal (v1_6):** never that an appendable refusal both appends and causes no journal mutation; never that every refusal always appends where recording is unsafe; and a live post-write acceptance whose truth is unresolved is neither ordinary success nor ordinary refusal and receives **no** additional refusal append while acceptance may already exist | §9.2, §15 preamble and F-36, §16.4, §18 M-11, M-32, §19, §21 T-23j, T-30a4, T-46c |
| 34d | **Terminal acceptance can never disappear (v1_6):** raw journal replay and governed terminal projection are separated; **exactly three** externally visible truth classifications; **every governed acceptance or status reader takes the existing lock before projecting terminal acceptance**, so `ACCEPTED_FOR_DESIGN_ONLY` is never exposed while a live writer retains legal authority to remove it; a raw complete event in `present == intent > committed` may prove authenticity and completeness but not terminal acceptance while an active writer may roll it back | §9.6, §10.1, §10.3, §10.5, §11.1a–§11.1d, §12.3 K-4a/K-4b, §14 Phase B1a / E3 / E6 / F1–F2, §16.2, §16.4, §18 M-13, §21 T-30a, T-30a1, T-26a, T-46d |
| 34e | **The rollback rule (v1_6):** rollback is legal only for the active append attempt, only while it owns the existing lock, and only before terminal acceptance is exposable; `PROVED_NOT_ACCEPTED` requires durable proof that the exact old prefix was restored; an unproved rollback or unproved durability is `UNRESOLVED`; and once the committed head durably names the event, or a locked stable verification proves it after writer ownership ends, removal is forbidden to every actor | §11.1c, §12.3 K-7, K-8, §14 Phase E5a, §15 F-36a, F-36b, §18 M-13, §21 T-30a2, T-30a3 |
| 34f | **`UNRESOLVED` behaviour, in full (v1_6):** a derived non-running safety and result condition — not a second durable protocol, workflow state, event type, or mark — under which nothing is claimed either way, Accept is unavailable, no success response is issued, no ordinary denial pretends certainty, no blind retry occurs, no effect is replayed, and no extra refusal append is made while acceptance may already exist | §10.1, §10.5, §11.1b, §12.2, §12.5, §16.2, §16.4, §21 T-30a4, T-46d |
| 34g | **Recovery conclusions (v1_6):** the existing lock, journal, head and tail recovery, reached only through the already separately authorized recovery/write-capable path; the offer GET never recovers; recovery proves one of the three classifications and **never writes a replacement acceptance to resolve uncertainty**; after `PROVED_ACCEPTED` lookup-first returns the existing acceptance with zero append; after `PROVED_NOT_ACCEPTED` only a **new** explicit browser action may attempt acceptance; after `UNRESOLVED` retry and reload remain unresolved with zero effect replay | §11.2, §12.3 K-3, §12.5, §14 Phase B4 / E1, §21 T-30a5, T-46b2 |
| 34h | **A5/A6 ownership and post-effect crash recovery:** A5 start → exactly one final explanation → matching A5 completion → only then A6 start → exactly one mechanical PASS → matching A6 completion → only then `READY_FOR_ACCEPTANCE`; A5 and A6 identities differ, while each recovered completion preserves its own original operation identity and start sequence. Recovery uses the installed same-operation reattachment pattern, repeats no start or substantive event, and suppresses provider/substantive dispatch and Accept until completion | §6.5a, §7.1a–§7.1b, §7.7, §11.3 gates 4 and 11b–11d, §14 Phase A A5–A7 and P-3b/P-4, §20, §21 T-13a–T-13a5, §22.3 item 11 |
| 35 | Deterministic acceptance identity, and why its inputs are exactly those — **unchanged in v1_6, and journal position, the eight head fields, and the complete-head digest all remain excluded from it, so a retry of the same act still derives the same identity** | §8.4, §8.3a, §11.4, §21 T-23i |
| 36 | Same click twice; concurrent clicks; lost response; **and a crash matrix written against the actual two-mark writer and reader — before the intent mark, intent mark only, unterminated line, complete event before the committed mark advanced, committed mark advanced, response lost — each stating what the reader returns and whether an acceptance exists**. **Re-columned in v1_6: each row now states raw replay AND the governed truth, and the durable-record-before-committed-mark position is split into K-4a (writer still owns the lock — not projectable, and the only position where rollback remains legal) and K-4b (writer ownership ended — `PROVED_ACCEPTED`, removal thereafter forbidden)** | §11.1, §12.2, §12.3 K-1 to K-11, §21 T-29 to T-32a, T-30a1, T-26a |
| 36a | One effect/commit rule, consistent for every crash position, with the response matching the standing — **and, corrected in v1_6, the standing is one of the three governed truths, so a response never claims acceptance a governed reader could not project and never claims non-acceptance that was not durably proved** | §11.1, §14 Phase F2, §15 F-36 to F-36b, §16.4, §16.5 |
| 36b | The unterminated-tail recovery has a named, reachable, owned invocation under the writer lock — **the existing one**, not live rollback and not a new mechanism | §11.2, §14 Phase E1, §12.3 K-3, §21 T-30, X-5a |
| 37 | Conflicting same-pass material fails closed; a different candidate is never absorbed | §12.4, §12.2 |
| 38 | Existing append, **two-mark ordering as it actually is**, existing rollback, existing tail recovery, and lookup-first truth preserved; **no new store, no new mark, no new recovery path** | §4.1, §9.6, §11.2, §12.1 |
| 39 | Post-commit state exactly as locked | §17.1 |
| 40 | Terminal and non-running; candidate byte-identical | §17.2, §17.3 |
| 41 | No provider, writer, next package, Git, integration, implementation, closure, copy, `PACKAGE_COMPLETE` | §17.5 |
| 42 | Automatic next-package transition stays OPEN and SEPARATE | §17.6, §22.3 item 8 |
| 43 | Historical Markdown acceptance/closure evidence stays historical; the click generates and copies nothing | §5.2, §17.3, §17.5 |
| 44 | Explanation lifecycle: append-only, supersession, predecessor binding, stale rules | §7.5, §7.6, §7.7 |
| 45 | Controller fixed scope and prose boundary; controller-proved actionable offer | §5.2, §6.1, §6.7 |
| 46 | Logical endpoint only: strict JSON type/size/fields, **no GET mutation of acceptance state (stated exactly in v1_6)**, same offer identity **and complete-head digest** posted, Host+Origin, lock revalidation over the whole head, safe text rendering, simple+technical same binding, JS never authority | §16, §13 |
| 47 | Complete offline disposable test matrix, covering every required case — **and, corrected in v1_4, internally satisfiable: no two of its rows require different event counts for one request class, and the wrong-method `GET`/`HEAD` rows now assert the same count the normative sections assert**. **Extended in v1_6 to cover the four corrections and their honesty checks** | §21, and specifically §21.1 T-13a1a1; §21.2 T-23e to T-23j; §21.3 T-26a, T-26b, T-30a to T-30a5; §21.4 T-45, T-45a, T-46a, T-46b, T-46b1, T-46b2, T-46c, T-46d, T-46e |
| 48 | Fault matrix | §21.6 |
| 49 | Fail-closed matrix | §15 |
| 50 | Endpoint outcome set | §16.4 |
| 51 | Negative invariants and must-nevers | §18 |
| 52 | Implementation surface, reference only; production/provider/candidate-writing/audit/Git untouched | §20 |
| 53 | Wiring delta and open dependencies | §22 |
| 54 | What could not be confirmed | §23 |
| 55 | Only locked names used verbatim; every other label `[proposed]`; storage and library details open | §0, throughout |
| 56 | Exactly one new file created; no existing file modified, moved, renamed, or deleted | §0, §25 |

**Known limitations of this candidate, stated rather than hidden:**

- Exact field spellings, thresholds, HTTP paths, outcome strings, body version numbers, and the `explanation_stage` discriminator spelling are `[proposed]` and will need one bounded pass at implementation time.
- The strict journal-position binding (§11.4) is a deliberate safety trade that costs an occasional reload; the tolerant alternative is documented and rejected, not overlooked.
- **The v1.13 specification document named by `controller/nh_supervisor/__init__.py` is genuinely absent** (§23 item 2). That is a real documentation and provenance gap, and it is not repaired here. **It is not a dependency of this design and not a reachability prerequisite** — the previous version's claim to the contrary is withdrawn in §23 item 3.
- **The installed supervisor command protocol is reachable today** through the generic dispatch at `nh_loop.py:45946-45949` (§2.5). What does not exist is **this package's own** acceptance command, acceptance primitive, HTTP endpoint, and accepted-only state (§4.2). Building them is separate, later, and Ness's, and their exact shape is open (§22.3 item 11). **This candidate claims none of them exists today.** **Narrowed in v1_2, because reachability is where this package's own defect lived:** the reachability that matters for the acceptance *offer* is not command reachability at all — it is whether the offer's preconditions are durable **before** the workflow reaches a state in which no command runs. **v1_2's answer to that — placing the state-creating PASS append last — is historical and is superseded for readiness.** **Current rule (v1_11, restated in v1_12):** readiness requires the completed six-event A5/A6 chain — A5 start, its one final explanation, matching A5 completion, A6 start, its one mechanical PASS, matching A6 completion — and `mechanical_pass_recorded` alone does not create it. Durability before the non-running state also remains **necessary and not sufficient**: an offer whose preconditions are all durable is still unreachable if a lock-time gate refuses the arrangement that the recovery actually produces — **which is exactly what v1_2's same-operation gate did at crash row P-3b**, permanently, from a state with `next_command = null`. **So the reachability this design owes has two halves, and both are stated and tested: an owner exists at every position — post-effect A5/A6 crash positions are owned by same-operation completion recovery, which appends only the missing matching completion (§7.1b, §14 Phase A crash table P-3b/P-4) — and the records that owner writes pass every gate, so §11.3 gates 11b–11d must accept the recovered chain (§21 T-13a1b, T-13a3, T-49c).** **It remains true that this design's own command and endpoint do not exist, and nothing here builds, names, or authorizes them.**
- **The v1_2 ordering is stated as an ordering guarantee, not an atomicity guarantee, and the difference is deliberate.** The installed journal commits one record at a time (`engine.py:449-458`); **this candidate designs no multi-record atomic commit, no new mark, no new store, and no new recovery path, and it would be wrong to read one into §7.1a.** What is guaranteed is weaker and checkable: every crash position leaves a state whose owner already exists (§14 Phase A crash table). A future package that wanted true multi-record atomicity would be a separate, separately authorized design, and none is proposed here.
- **The v1_3 owner separation has a real cost, and v1_11 narrows which unmatched starts may remain inert.** The successful path still uses two distinct supervisor operations, so a crash can leave an unmatched start. **General pre-effect unmatched-start reaping remains a separate question:** for example, a start left before its operation produced its substantive event may remain historical residue under the existing rules. **But post-effect A5/A6 starts are no longer left inert:** an A5 start followed by its one final explanation, or an A6 start followed by its one PASS, is owned by the installed same-operation completion-recovery pattern and must receive its missing matching completion before the sequence advances. This is completion of the already-started operation, not general reaping and not a new recovery authority (§7.1b, §14 P-3b/P-4, §22.3 item 11).
- **v1_3 withdraws a check rather than adding one, and that is stated plainly rather than presented as strengthening.** v1_2's gate 11b required two events to share a `supervisor_operation_id`. **Neither event carries that field** (`schema.py:680-704`, `:705-723`; `engine.py:449-458`), so the check was never evaluable, and the recovery would have failed it if it were. What the withdrawn clause aimed at — that the explanation was durable before the PASS — is proved from `event_seq`, which is where an append-only chain actually records write order. **No other binding is loosened, and no gate is relaxed** (§7.4a, §11.3 gate 11c).
- The refusal-record volume question is stated and deliberately not solved (§22.3 item 5): ordinary refusals are recorded per §9.2, and no cap that could silently drop one is designed here.
- **v1_4 withdraws a test claim rather than adding a mechanism, and that is stated plainly rather than presented as strengthening.** v1_3's §21 T-45 required a wrong-method `GET`/`HEAD` mutation attempt to append **nothing at all**, while §15 F-29, §16.4, and §19 required that same class to append **exactly one** refusal record. Both could not hold, so the package's own offline suite was unsatisfiable for that class. **The normative sections are what stand, because they are what Master V10 §0B requires; T-45 is what gives way.** No new event type, carrier, outcome code, endpoint, or store was added to resolve it, and **the volume question above is exactly the open item this makes slightly larger — it is named, not quietly absorbed.**
- **This correction makes one request class louder, and that is a deliberate trade.** A route that is reachable by a stray navigation or a prefetch will now leave a permanent refusal record each time it is hit with the wrong method. **That is what §0B's transparency law asks for and this design does not second-guess it**, but the resulting volume, and any cooling rule over it, remain Ness's to set (§19 cooling, §22.3 item 5). **No cap, sampling rule, or deduplication is designed here, because any of them could silently drop a refusal.** **Sharpened in v1_6:** each of those refusal records is a real append, so **each one moves the journal and the head**. That is the actual cost of the transparency rule, it is stated rather than glossed as "mutates nothing", and it is one more reason the volume question genuinely belongs to Ness (§9.2, §13.6).
- **v1_6 states a cost the offer read did not previously admit: it takes the exclusive lock.** Publishing one stable authenticated snapshot of the whole head requires it (§11.2). **The read holds the lock only for that snapshot, mutates nothing, appends nothing, and never recovers a tail** — but it does mean the offer read can be made to wait behind a live writer, and that a stalled writer makes the offer temporarily unavailable rather than merely stale. **The alternative — an unlocked read that can publish a head no writer ever wrote — is worse, because the lock-time comparison would then be measuring against a fiction.** No lock-free snapshot mechanism, cache, or second reader path is designed here to soften it.
- **The strict binding widened in v1_6, and the extra staleness is real.** Binding all eight head fields means a valid intent-only change by any other writer stales an outstanding offer, where v1_4's tail-and-committed binding would not have noticed. **That is the point** — the world genuinely moved — but it does cost an occasional extra reload. **The tolerant alternative was rejected for exactly the reason §11.4 already rejects a "harmless event" list: a wrong entry on a "harmless head field" list would be a silent acceptance over a changed world.**
- **`UNRESOLVED` can persist, and v1_6 deliberately provides no automatic escape from it.** Where the journal or head cannot be authenticated, where a rollback's durability cannot be proved, or where a post-write verification leaves a durable record whose standing cannot be established, the truth stays unresolved until the **existing** recovery path proves one of the two proved classifications. **Retrying does not help, and is not meant to.** **An automatic escape would have to guess, and a guess in either direction — manufacturing an acceptance, or declaring non-acceptance — is precisely the failure this correction exists to prevent** (§11.1b, §12.5). **The operational question of who runs that recovery, and when, is not this design's to answer and is not answered here.**
- **v1_6 adds one response outcome code and nothing else to the response surface.** `unresolved_recovery_required` `[proposed]` exists because the unresolved standing is neither a success nor an ordinary denial, and v1_4 had no code that could carry "I cannot tell" without asserting something false. **It adds no event type, carrier, store, mark, workflow state, lock, or recovery authority**, and its spelling is `[proposed]` like every other outcome string (§16.4, §22.3 item 2).
- **v1_6 corrects stale ownership sentences rather than changing the mechanism they describe.** The A5/A6 topology is exactly what v1_3 settled; what v1_4 still carried in §6.5a and in the §20 `commands.py` row were sentences from before that settlement. **Correcting them changes no mechanic, no gate, no ordering proof, no recovery, and no test of the explanation/PASS sequence** — it makes the file say once what it already meant everywhere else (§21 T-13a1a1).

---

## §25 — DELIVERY STATEMENT

This candidate creates **exactly one new file — itself** — at `NH-GOVERNANCE/05_ACTIVE_CANDIDATE/NH_NESS_DESIGN_ACCEPTANCE_RECORD_AND_UNDERSTANDABLE_ACCEPTANCE_SURFACE_MECHANICAL_DESIGN_v1_14_CANDIDATE.md`.

Its exact unchanged source is `NH_NESS_DESIGN_ACCEPTANCE_RECORD_AND_UNDERSTANDABLE_ACCEPTANCE_SURFACE_MECHANICAL_DESIGN_v1_13_CANDIDATE.md`, SHA-256 `cfcb10d9b40f945cab91bc9fc43d722235af8ae9555a537a6518558ec4e48e6c`, 400,833 bytes, 2,322 lines.

The v1_13 source remains byte-identical. Every earlier candidate remains unchanged, including interrupted v1_5 as historical evidence. No authority file, accepted file, historical file, other candidate, closure record, code file, test file, store, marker, journal, or repository state is modified, moved, renamed, overwritten, or deleted by this candidate.

v1_14 performs no implementation, no controller change, no UI change, no test change, no real journal append, no provider call, no Git operation, no Master or Map integration, no Register assignment, no `PACKAGE_COMPLETE`, no closure, and no acceptance record.

**It is a DESIGN CANDIDATE. It is NOT ACCEPTED, NOT ADOPTED, NOT AUTHORITATIVE, NOT INTEGRATED, NOT IMPLEMENTED, and NOT `PACKAGE_COMPLETE`.** Independent ChatGPT audit and Ness's explicit acceptance remain required and are not claimed by this file.

Ness chooses what N.H means. This file only proposes how one press could be made to mean exactly one thing, provably, once.

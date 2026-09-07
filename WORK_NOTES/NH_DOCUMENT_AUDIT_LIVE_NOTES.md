# N.H Document Audit — Verified Live Notes

This file records verified facts from the current document-cleanup work.
Unverified model output is not recorded as fact.

## Safety boundary

- Never delete the `NH-GOVERNANCE` directory as a whole.
- Never broadly or recursively delete its contents.
- One exact file may be removed only after Ness states the reason and gives one explicit approval for that file.
- No loop or external model run is active during this document review.

## Current verified filesystem state

- `04_ACCEPTED_STANDALONE_DESIGNS`: 94 Markdown files.
- `05_ACTIVE_CANDIDATE`: 12 Markdown files.
- `99_HISTORICAL_CANDIDATES`: 0 files in the working tree.
- External desktop history folder: 67 Markdown files.
- Same-name duplicate pairs between `04` and `05`: 0.
- Git changes have not been committed.

## Completed actions

- The one historical file was copied to the Windows desktop and proved byte-identical before its working-tree copy was removed.
- A second recoverable copy of that historical file exists in a temporary quarantine.
- Eight byte-identical accepted/active duplicate files were rechecked immediately before action.
- Their accepted copies remain in `04`.
- Only their duplicate copies were moved out of `05` into a temporary quarantine.
- No other governance document was moved or removed.
- After Ness reviewed the first three audit items and gave explicit approval, the exact A1 v1.1 closure design, A4 v1.1 policy, and Authority Integrity Control Plane v1.10 design were moved from `05` to `04`.
- Their content identities were recomputed after the move and matched the pre-move identities exactly.
- No fourth document was moved.
- After Ness authorized one bulk evidence-based sort, B1 and five other
  proved-current accepted files were moved from `05` to `04`. Their contents
  were not changed.
- Sixty-six files explicitly proved to be superseded or historical were moved
  from `05` to the external desktop history folder. Every destination hash
  matched its pre-move source hash, and every source path is now absent.
- Twelve active, status, unaccepted, or evidence-conflicted files remain in
  `05`; none was moved by the historical cleanup.

## Read-only audit findings that still require Ness review

- Before the eight duplicate removals, the full `04`/`05` audit covered 180 Markdown files.
- `04` held 35 proved accepted design/candidate files, 2 files classified as historical by explicit records, and 48 acceptance/closure/blocker records.
- `05` held 21 candidates with acceptance proof, 2 current unaccepted candidates, 65 superseded or historical candidates, 3 candidates with conflicting evidence, and 4 direction/status documents that are not candidates.
- Removing the eight exact duplicate copies initially left 13 accepted candidates located only in `05`. Three of those were later moved to `04` after individual review and Ness's explicit approval, leaving 10 from that original set still in `05`.
- No bulk move is authorized. Every remaining proposed move must be shown to Ness first.

## Controller-test evidence

- Compilation passed.
- The three new history-exclusion tests passed.
- In the broader test file, 57 tests passed and 5 old live-fixture tests failed because they expected two validation records while the copied current state exposed one.
- Those five failures were not failures of the new history-exclusion assertions.

## Next review step

- Review the 12 files that remain in `05` as one bounded set.
- Do not move an unresolved file merely because its date or version number is
  newer.

## Item review 1 — A1 design closure

- File now in `04`: `NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md`.
- The separate closure record in `04` identifies this exact file, records its exact SHA-256, line count, and byte count, records ChatGPT PASS, records Ness's explicit acceptance, and declares the A1 standalone design scope `PACKAGE_COMPLETE`.
- The closure record explicitly says its later receipt overrides the candidate's older internal "awaiting audit" wording while preserving the candidate bytes unchanged.
- Central feature 1: the accepted replacement gold set contains eight frozen story-bearing cases and their contexts, annotations, evidence relationships, firmness records, themes, and failure boundaries.
- Central feature 2: design closure is a provenance seal over exact accepted file identities; it is not a runtime seal or a disk-store action.
- Central feature 3: future changes require a new versioned candidate, independent audit, and Ness acceptance; accepted content is never edited in place.
- Central feature 4: root checking, pinning, ingest, runtime sealing, executable benchmark work, coding, and testing remain separate implementation-stage work.
- Verified conclusion: this candidate has acceptance proof and was moved to `04` after Ness reviewed and explicitly approved this exact move. Its bytes are unchanged.

## Item review 2 — A4 relevance-mode declaration policy

- File now in `04`: `NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md`.
- The separate acceptance record in `04` explicitly accepts A4 v1.1, names the exact file and path, and records its SHA-256, line count, and byte count.
- Central feature 1: N.H uses one shared relevance language; a component may not invent a private meaning of "relevant".
- Central feature 2: every component must explicitly declare its relevance mode and the reason for using it.
- Central feature 3: every declaration must state what happens when relevance is uncertain; missing uncertainty behavior makes the declaration invalid.
- Central feature 4: relevance is purpose-scoped and is not truth, evidence strength, causation, authority, permission, or Ness's judgment.
- Verified conclusion: this candidate has acceptance proof and was moved to `04` after Ness reviewed and explicitly approved this exact move. Its bytes are unchanged.

## Item review 3 — Authority Integrity Control Plane

- File now in `04`: `NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md`.
- The package-complete closure record in `04` explicitly accepts the exact v1.10 file, records its SHA-256, line count, and byte count, and records an independent ChatGPT PASS.
- Central feature 1: verify the exact current governing files and their identities before a protected operation proceeds.
- Central feature 2: produce either one verified authority snapshot or one deterministic refusal; technical failure remains a separate unresolved state.
- Central feature 3: reuse an older verification only after the current inputs are proved unchanged; changed inputs require a successor verification generation.
- Central feature 4: prevent duplicate concurrent verification work while keeping each caller separately attached to the shared result.
- Verified conclusion: this candidate has acceptance proof and was moved to `04` after Ness reviewed and explicitly approved this exact move. Its bytes are unchanged.

## Item review 4 — B1 context-retrieval parameter architecture

- File currently in `05`: `NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md`.
- The separate acceptance record in `04` explicitly accepts B1 v1.0, names the exact path, and records its SHA-256, line count, and byte count.
- Central feature 1: positional retrieval and semantic retrieval remain two separate channels; semantic retrieval may not override positional retrieval.
- Central feature 2: retrieval settings are versioned per mode and require a valid A4 declaration; without one, retrieval does not run.
- Central feature 3: every retrieval run produces one append-only audit record with parameters, versions, selected items, provenance, limits, and an honest empty-versus-failure result.
- Central feature 4: safety ceilings override mode settings and prevent any mode from silently expanding retrieval limits.
- Verified conclusion: this candidate has acceptance proof but is still physically located in `05`; no move has been made.

## Item review 5 — Bundle 1 memory-reading foundation closeout

- File currently in `05`: `NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_CANDIDATE_v1_1.md`.
- The separate acceptance record in `04` identifies and accepts this exact file and path.
- Central feature 1: records the Bundle 1 package inventory and preserves the accepted standalone package boundaries.
- Central feature 2: records the A25 reread-mode assignment decision.
- Central feature 3: records bounded B9 retry values, including technical-attempt limits, early stop, and honest exhaustion behavior.
- Central feature 4: preserves the then-current A1 blocker rather than pretending the missing historical source had been recovered; later A1 closure evidence now exists separately.
- Verified conclusion: this candidate has acceptance proof but is still physically located in `05`; no move has been made.

## Item review 6 — Bundle 2 relevance and retrieval foundation

- File currently in `05`: `NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_v1_0_CANDIDATE.md`.
- Separate acceptance and package-complete closure records in `04` identify this exact file and accepted byte identity.
- Central feature 1: keeps current-situation material separate from older patterns and never treats a possible relation as proof.
- Central feature 2: lets understanding look broadly while requiring stronger current support before real-world action.
- Central feature 3: distinguishes a normal empty retrieval result from a system failure and applies bounded retry only to the failure path.
- Central feature 4: every retrieval operation has append-only logging, one operation identity, duplicate prevention, and crash/partial-result handling.
- Verified conclusion: this candidate has acceptance proof but is still physically located in `05`; no move has been made.

## Item review 7 — Bundle 3 story layer, people, themes, and clashes

- File currently in `05`: `NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md`.
- The acceptance record in `04` explicitly names and accepts this exact file. Its currently recalculated identity matches the receipt exactly: SHA-256 `3566cf0f917fb4f7eb329d9089f6e238fe4afbacbae2c73c8b2716e3397e7c2e`, 685 lines, 39,950 bytes.
- Central feature 1: clear person identity may be linked automatically; unclear identity stays pending, and similar names alone are never enough.
- Central feature 2: person links and merges preserve evidence and history; uncertain records are never silently merged.
- Central feature 3: themes organize tellings without turning organization into truth, and only Ness confirms proposed themes.
- Central feature 4: clashes stay visible beside the affected material and do not erase or rewrite the underlying readings, tellings, or history.
- Verified conclusion: this candidate has exact acceptance proof but is still physically located in `05`; no move has been made.

## Item review 8 — Bundle 4 living state, computed view, actions, and world model

- File currently in `05`: `NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md`.
- The acceptance record in `04` explicitly names and accepts this exact file. Its currently recalculated identity matches the receipt exactly: SHA-256 `0c9a201130d5811c838fea0d5655c8a98aac909afdc60024830204a690e77f97`, 1,399 lines, 84,568 bytes.
- Central feature 1: the Living State keeps dated, evidence-linked states without reducing Ness to one fixed label; several real positions may coexist.
- Central feature 2: the world model is separate from the self model and keeps active information separate from colder background information.
- Central feature 3: the Computed View is an internal, refreshable snapshot; it does not rewrite the underlying evidence or history.
- Central feature 4: actions use a four-level risk ladder, explicit permission, duplicate prevention, crash recovery, and honest reporting of whether the outside world changed.
- Verified conclusion: this candidate has exact acceptance proof but is still physically located in `05`; no move has been made.

## Item review 9 — Live design-loop continuation after acceptance

- File currently in `05`: `NH_LIVE_DESIGN_LOOP_POST_ACCEPTANCE_CONTINUATION_MECHANICAL_DESIGN_v1_8_CANDIDATE.md`.
- The package-complete closure record in `04` explicitly accepts this exact file. Its currently recalculated identity matches the receipt exactly: SHA-256 `448daa63b4899d4639dc5b7612985cb34e97732dcf4cbeac2c224c54f8ae51e2`, 2,826 lines, 303,820 bytes.
- Central feature 1: acceptance remains final for the current package, but a separate controlled transition may continue the overall loop to a later package.
- Central feature 2: continuation has distinct stages for selecting the next package, clearing its questions, preparing the task, producing the initial design, saving it, and handing ownership back to the normal supervisor.
- Central feature 3: every stage is lookup-first, bounded, crash-safe, append-only, and protected against duplicate provider calls.
- Central feature 4: an uncertain provider outcome is reconciled before any new request; the system never guesses that nothing happened and sends the work again.
- Later lineage evidence proves that v1.9 was accepted after v1.8. Therefore v1.8 remains accepted history but is not the current accepted version.
- Verified conclusion: do not move v1.8 as the current accepted design; no move has been made.

## Item review 10 — Live dual-model handoff placement and dependencies

- File currently in `05`: `NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_v1_1_CANDIDATE.md`.
- The acceptance record in `04` explicitly accepts this exact file. Its currently recalculated identity matches the receipt exactly: SHA-256 `5998098c86875721feb99bab7e3bb14435770e0d74be6541eab828aa9efee26e`, 360 lines, 18,846 bytes.
- Central feature 1: a heavier local model proposes deeper substance in the background, while one lighter local model is the only voice that speaks with Ness.
- Central feature 2: N.H validates both the heavy model's substance and the light model's expression before anything is presented.
- Central feature 3: Bundle 7 owns the human-facing model roles and voice behavior; Bundle 8 owns the complete connected handoff, recovery, retry, and synchronization mechanics.
- Central feature 4: search, heavy reasoning, and live expression remain three separate jobs; none of the models becomes N.H's authority.
- Verified conclusion: this candidate has exact acceptance proof but is still physically located in `05`; no move has been made.

## Item review 11 — Understandable design-acceptance surface, v1.14

- File currently in `05`: `NH_NESS_DESIGN_ACCEPTANCE_RECORD_AND_UNDERSTANDABLE_ACCEPTANCE_SURFACE_MECHANICAL_DESIGN_v1_14_CANDIDATE.md`.
- The package-complete closure record in `04` explicitly accepts this exact file. Its currently recalculated identity matches that receipt exactly: SHA-256 `c4f055f271cbeea246291986b1b11367fcfb1748466f346e642176df2b36b46a`, 2,324 lines, 401,581 bytes.
- Central feature 1: before acceptance is available, Ness must see one understandable surface containing eight distinct required parts.
- Central feature 2: accepting a design is separate from closing the package, adopting it into the Master or Map, and implementing it.
- Central feature 3: a successful acceptance action creates one bound acceptance record only; it does not call a model or start later work.
- Central feature 4: the controller rechecks the complete current journal position under a lock, so a changed or stale offer is refused rather than guessed current.
- Important later evidence: the post-acceptance continuation design states that Ness later accepted v1.15 and that v1.15 governs downstream design wherever it differs from v1.14; the separate receipt still names v1.14. Therefore v1.14 is proved accepted historically but is not safe to classify as the current version.
- Verified conclusion: do not move this file as a current accepted design until v1.15's standing and the lagging receipt are reviewed together; no move has been made.

## Item review 12 — Provenance-first multi-index memory fabric, v1.4

- File currently in `05`: `NH_PROVENANCE_FIRST_MULTI_INDEX_MEMORY_FABRIC_MECHANICAL_DESIGN_v1_4_CANDIDATE.md`.
- No separate acceptance or closure record naming this exact file was found in `04`.
- The authenticated interview journal does contain a `mechanical_audit_recorded` PASS for this exact identity and a later `ness_candidate_acceptance_recorded` event with `ACCEPTED_FOR_DESIGN_ONLY`. The file's currently recalculated identity is SHA-256 `84eee68e6a5dfd00d675797640937e960d99ff721ae255563ac7241b2c78780d`, 2,107 lines, 147,448 bytes, matching the journal identity.
- Central feature 1: indexes are derived and rebuildable ways to find preserved material; no index becomes memory, truth, identity, permission, or authority.
- Central feature 2: different retrieval and relationship channels stay separately typed and may not silently merge their meanings or ranks.
- Central feature 3: privacy and access checks happen before relevance, and the most protected raw material is structurally excluded from ordinary indexes and contexts.
- Central feature 4: building, validating, publishing, coverage registration, duplicate prevention, and crash recovery use explicit boundaries and owner records rather than guesses.
- Verified conclusion: runtime acceptance proof exists, but the separate `04` receipt is missing. Do not move it automatically until Ness reviews whether the authenticated journal acceptance is sufficient or a receipt must be created first; no move has been made.

## Item review 13 — Unified Durable Operation Kernel, v1.9

- File currently in `05`: `NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md`.
- The package-complete closure record in `04` explicitly accepts this exact file. Its currently recalculated identity matches the receipt exactly: SHA-256 `1f9ea714f1a182c0857e80399850a3aeebcf4a50a32d5a200fce57a5d5f47ae3`, 1,686 lines, 343,868 bytes.
- Central feature 1: this is shared, non-reasoning coordination machinery for operation identity, waiting, cancellation, checkpoints, recovery, stale-result rejection, and terminal evidence.
- Central feature 2: each real job keeps its own owner and meaning; the kernel carries and checks owner evidence but never replaces it or decides policy.
- Central feature 3: child work is registered within one generation, membership is closed against one exact head, and stale or contradictory work cannot silently commit.
- Central feature 4: recovery looks up durable owner truth before acting and never repeats an outside or stored effect merely because an acknowledgement was lost.
- Verified conclusion: this candidate has exact acceptance proof but is still physically located in `05`; no move has been made.

## Item review 14 — Future music understanding and service connections intake

- File currently in `05`: `NH_FUTURE_MUSIC_UNDERSTANDING_AND_MUSIC_SERVICE_CONNECTIONS_PACKAGE_INTAKE_v1_0_CANDIDATE.md`.
- Its own status explicitly says future package intake, not accepted, not adopted, not integrated, and not implemented. No acceptance record for this exact file was found in `04`.
- Central feature 1: future understanding of musical structure, style, mood, performance, and relationships among works.
- Central feature 2: discussion of exact musical moments and their links to Ness's memories and creative work, without turning preference into fact.
- Central feature 3: optional local music and service connections such as Spotify or YouTube, with privacy, account, permission, and disconnection boundaries.
- Central feature 4: it must begin only after Bundle 7 unless Ness explicitly changes that order.
- Verified conclusion: this is correctly located in `05` as future, unaccepted work; no move is proposed.

## Item review 15 — Claude design / Codex audit role-split amendment, v1.6

- File currently in `05`: `NH_LIVE_DESIGN_LOOP_CLAUDE_DESIGN_CODEX_AUDIT_ROLE_SPLIT_SUPERSESSION_v1_6_CANDIDATE.md`.
- Its own status explicitly says candidate, not accepted, not adopted, not authoritative, not installed, and not implemented. No acceptance record for this exact file was found in `04`.
- Central feature 1: the controller creates the bounded task locally without a model call.
- Central feature 2: Claude independently designs the mechanics inside that fixed task envelope.
- Central feature 3: a fresh Codex review reconstructs the requirements from sources and audits Claude's actual candidate.
- Central feature 4: Ness alone accepts or rejects; neither model gains authority or decides an open Ness choice.
- Verified conclusion: this is correctly located in `05` as current unaccepted work; no move is proposed.

## Item review 16 — Post-acceptance continuation, v1.9

- File currently in `05`: `NH_LIVE_DESIGN_LOOP_POST_ACCEPTANCE_CONTINUATION_MECHANICAL_DESIGN_v1_9_CANDIDATE.md`.
- Its currently recalculated identity is SHA-256 `711b89d30d36130eb2e9506e817429a5813e700b7c62fbbff97b340dc82a12ed`, 3,249 lines, 380,415 bytes.
- The later v1.11 file explicitly records that Ness accepted these exact v1.9 bytes after an independent PASS. The old receipt in `04` still names v1.8, so separate receipt bookkeeping is behind the later acceptance.
- Central feature 1: every actionable next-package result must carry one exact proved package source root.
- Central feature 2: a valid-looking result without that root is rejected instead of being admitted into a route the controller cannot complete.
- Central feature 3: one earlier-contract result may receive one fresh current-contract selection, with a new request identity and a fresh source check.
- Central feature 4: the replacement is one-shot and may not become a hot re-selection loop.
- Verified conclusion: later exact acceptance evidence exists, but the `04` receipt still points to v1.8. Do not move until the lagging receipt and lineage are reconciled; no move has been made.

## Item review 17 — Post-acceptance continuation, v1.11

- File currently in `05`: `NH_LIVE_DESIGN_LOOP_POST_ACCEPTANCE_CONTINUATION_MECHANICAL_DESIGN_v1_11_CANDIDATE.md`.
- Its currently recalculated identity is SHA-256 `1554a0802cc381666eab0e628ccca3adde025af03398e3c50a96dd522a89f548`, 3,801 lines, 485,472 bytes.
- The file itself says it was not accepted when written and that v1.9 was then the accepted version. A later v1.6 role-split candidate claims v1.11 was subsequently accepted, but no matching acceptance or closure record was found in `04`, and the referenced supporting accepted file is absent from this checkout.
- Central feature 1: preserves the continuation design and its v1.9 actionable-root correction.
- Central feature 2: preserves the bounded retry-exhaustion stop added in v1.10.
- Central feature 3: wires the initial-design exhaustion state into loop status so exhausted work cannot fall back into another model run.
- Central feature 4: keeps the exhausted position read-only, restart-stable, and free of invented journal operations.
- Verified conclusion: current acceptance is not proved strongly enough from the available files. Keep in `05` pending reconciliation; no move is proposed.

## Item review 18 — Understandable design-acceptance surface, v1.15

- File currently in `05`: `NH_NESS_DESIGN_ACCEPTANCE_RECORD_AND_UNDERSTANDABLE_ACCEPTANCE_SURFACE_MECHANICAL_DESIGN_v1_15_CANDIDATE.md`.
- Its currently recalculated identity is SHA-256 `b10727441ddf7502ff7525c79b0b71043b559502660dcc7c3b9001f0633ffcc6`, 2,338 lines, 409,297 bytes.
- The accepted post-acceptance continuation v1.8 explicitly records that Ness later accepted this exact v1.15 identity and that v1.15 governs downstream design where it differs from v1.14. The receipt in `04` still names v1.14.
- Central feature 1: preserves the mandatory eight-part understandable acceptance surface.
- Central feature 2: keeps acceptance separate from closure, adoption, integration, and implementation.
- Central feature 3: keeps one bound acceptance event, exact current-head rechecking, stale-offer refusal, and no model call on the acceptance action.
- Central feature 4: narrows one ordering check so an unrelated old PASS does not falsely block a fresh acceptance chain, while the fresh chain still requires its own bound PASS.
- Verified conclusion: exact later acceptance evidence exists, but the separate `04` receipt has not been updated from v1.14. Do not move either version until the lineage is reconciled; no move has been made.

## Item review 19 — A25 reread-mode assignment, v1.0

- File currently in `05`: `NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_0_CANDIDATE.md`.
- The later v1.2 file in `04` explicitly identifies v1.0 as preserved historical candidate provenance.
- Central feature 1: assigns the approved reread modes without changing B10's mechanics.
- Central feature 2: keeps the A25-to-B10 connection as separate later work.
- Central feature 3: adds no tuning value, implementation authority, or new trigger.
- Verified conclusion: v1.0 is historical, not the current accepted A25 design; no move has been made.

## Item review 20 — A25 reread-mode assignment, v1.1

- File currently in `05`: `NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_1_CANDIDATE.md`.
- The later v1.2 file in `04` explicitly identifies v1.1 as preserved historical candidate provenance and describes the narrow overlap correction made after it.
- Central feature 1: records that both existing reread modes may apply in a genuine overlap case.
- Central feature 2: keeps the two modes separate and creates no third mode.
- Central feature 3: leaves B10's accepted trigger vocabulary unchanged.
- Verified conclusion: v1.1 is historical; v1.2 is the later accepted file in `04`; no move has been made.

## Item review 21 — A26 identity and Personal Mode relationship, v1.0

- File currently in `05`: `NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_0_CANDIDATE.md`.
- The later v1.1 file in `04` explicitly identifies v1.0 as historical and explains that v1.0 overreached by choosing an identity precondition too early.
- Central feature 1: connects the identity system with Personal Mode.
- Central feature 2: preserves fingerprint, PIN, voice, and explicit opening as distinct factors.
- Central feature 3: leaves their exact working combination for later mechanical design.
- Verified conclusion: v1.0 is historical; v1.1 is the corrected accepted file in `04`; no move has been made.

## Item review 22 — A2 telling-object identity, v1.1

- File currently in `05`: `NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_1_CANDIDATE.md`.
- The later v1.8 file in `04` explicitly states that v1.0 through v1.7 are preserved as historical candidate provenance.
- Central feature 1: each telling is a separate immutable first-class record with a stable identity.
- Central feature 2: each telling remains linked to its parent reading and supporting roots.
- Central feature 3: later interpretations create new records instead of rewriting older ones.
- Verified conclusion: v1.1 is historical; v1.8 is the accepted later package in `04`; no move has been made.

## Item review 23 — A7 privacy, influence, and third-party use, v1.0

- File currently in `05`: `NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_0_CANDIDATE.md`.
- The later v1.1 file in `04` explicitly identifies v1.0 as historical and lists the four corrections applied after it.
- Central feature 1: separates visible suppression from removal of internal influence.
- Central feature 2: keeps sensitivity levels connected to their existing protections.
- Central feature 3: keeps raw secrets outside ordinary reading and model context.
- Central feature 4: closes A7 at the policy level while leaving mechanical work separate.
- Verified conclusion: v1.0 is historical; v1.1 is the corrected accepted file in `04`; no move has been made.

## Item reviews 24–33 — Authority Integrity Control Plane, v1.0 through v1.9

- Files currently in `05`: `NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_0_CANDIDATE.md` through `..._v1_9_CANDIDATE.md`.
- The accepted v1.10 file explicitly lists every version from v1.0 through v1.9 as preserved historical candidate provenance. It describes v1.10 as a corrected successor, not an edit of those earlier bytes.
- Review 24, v1.0: initial control-plane design; later v1.1 corrected unsafe cross-run reuse, an over-closed artifact taxonomy, and reopened retry values.
- Review 25, v1.1: added current-input re-proof and preserved accepted retry values; later v1.2 corrected the inability to distinguish transient read failure from deterministic refusal.
- Review 26, v1.2: separated retryable technical failure from deterministic refusal; later v1.3 corrected authority-version binding and content-blind generation identity.
- Review 27, v1.3: corrected the authority source and generation identity, but later v1.4 corrected the family key so successor generations stay in the same family.
- Review 28, v1.4: separated stable family identity from generation-varying inputs; later v1.5 corrected established-generation retry so it does not reopen sealed inputs.
- Review 29, v1.5: made established-generation retry resume after the sealed-input stage; later v1.6 corrected the authority source to the controller-proved set.
- Review 30, v1.6: aligned the authority source with the controller-bound evidence; later v1.7 corrected duplicate prevention so identical callers share one establishment episode.
- Review 31, v1.7: made pre-generation work caller-blind for duplicate prevention; later v1.8 supplied the missing durable-outcome mapping into accepted B9.
- Review 32, v1.8: supplied the six-way outcome routing; later v1.9 corrected factual claims about lineage, Git state, and production provenance without changing mechanics.
- Review 33, v1.9: corrected those provenance facts; later v1.10 narrowed one remaining unsupported claim about an aborted historical payload.
- Central feature 1 across the accepted successor: exact current authority inputs are proved before a protected operation proceeds.
- Central feature 2: unchanged work may be shared safely, while changed inputs open a linked successor generation.
- Central feature 3: technical failure, deterministic refusal, and successful verification stay distinct.
- Central feature 4: retries reuse the correct sealed basis and do not create duplicate committed outcomes.
- Verified conclusion: all ten files are historical predecessors of the accepted v1.10 file. No file has been moved.

## Item reviews 34–37 — B9 retry-values wiring, v1.0 through v1.3

- Files currently in `05`: `NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_0_CANDIDATE.md` through `..._v1_3_CANDIDATE.md`.
- The accepted v1.4 file in `04` carries the dated correction chain and explicitly preserves v1.0 through v1.3 as historical candidate provenance.
- Review 34, v1.0: initial wiring of Ness's retry values; v1.1 later corrected the real time limit, open-ended real-change examples, append-only consumption, source identity, and B24 boundary.
- Review 35, v1.1: added those five corrections; v1.2 later fixed the remaining open-list contradiction and made the substantive-retry deadline explicit.
- Review 36, v1.2: fixed those deadline and category rules; v1.3 later separated permanent attempt numbers from per-episode ordinals.
- Review 37, v1.3: added the per-episode numbering; v1.4 later corrected the first-attempt admission because gap and deadline evidence do not yet exist at that point.
- Central feature 1: retry attempts are bounded by both count and elapsed time.
- Central feature 2: unchanged inputs may continue under the same source identity; changed inputs open linked new work.
- Central feature 3: every consumption and admission record is append-only and has one winner.
- Central feature 4: protected or unrelated outcomes cannot open the B24 insufficiency path.
- Verified conclusion: v1.0 through v1.3 are historical predecessors of accepted v1.4. No file has been moved.

## Item reviews 38–39 — Bundle 3 completion, v1.0 and v1.1

- Files currently in `05`: `NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_0_CANDIDATE.md` and `..._v1_1_CANDIDATE.md`.
- The accepted v1.2 file records the dated sequence from v1.0 to v1.1 to v1.2 and explicitly says v1.0 and v1.1 remain unchanged as history.
- Review 38, v1.0: initial completion design for people, themes, and clashes.
- Review 39, v1.1: corrected clash permanence, theme actions, B-AFFIRM scope, consistency, and source inventory; v1.2 later corrected wording and provenance only.
- Central feature 1: clear person identity may link automatically; uncertainty remains pending.
- Central feature 2: themes organize material but never become truth by repetition.
- Central feature 3: clashes remain visible and are never silently resolved or used to rewrite history.
- Central feature 4: Ness's responses are separate events that affect what is shown as current.
- Verified conclusion: both files are historical predecessors of accepted v1.2. No file has been moved.

## Item reviews 40–45 — Claude design / Codex audit role split, v1.0 through v1.5

- Files currently in `05`: `NH_LIVE_DESIGN_LOOP_CLAUDE_DESIGN_CODEX_AUDIT_ROLE_SPLIT_SUPERSESSION_v1_0_CANDIDATE.md` through `..._v1_5_CANDIDATE.md`.
- v1.0 is dated August 27, 2026. Each later file identifies the exact preceding file as its correction base, and v1.6 records the exact identities of all six predecessors as preserved byte-identically.
- The sequence is therefore proved by explicit file-to-file lineage, not by the version number alone.
- Central feature 1: the controller prepares the bounded task and keeps identities, currentness, source bindings, and safety gates.
- Central feature 2: Claude designs the mechanics only inside that proved boundary.
- Central feature 3: a fresh Codex audit independently checks Claude's actual candidate.
- Central feature 4: Ness alone accepts or rejects, and open meaning cannot be turned into a mechanical choice.
- Verified conclusion: v1.0 through v1.5 are predecessor drafts. v1.6 is the latest file in this sequence, but v1.6 itself explicitly remains unaccepted. Therefore none of these six should move to `04`. No file has been moved.

## Item reviews 46–53 — Post-acceptance continuation, v1.0 through v1.7

- Files currently in `05`: `NH_LIVE_DESIGN_LOOP_POST_ACCEPTANCE_CONTINUATION_MECHANICAL_DESIGN_v1_0_CANDIDATE.md` through `..._v1_7_CANDIDATE.md`.
- The later v1.8 and v1.11 files record the exact identities of this complete predecessor chain and say the earlier bytes remain preserved unchanged.
- v1.8 is separately proved accepted, and v1.9 was accepted later for the same scope. Therefore v1.0 through v1.7 are not the current accepted design.
- Central feature 1: continue from one accepted package to the next through bounded, durable stages.
- Central feature 2: recover saved provider results before considering a new request.
- Central feature 3: validate and cover genuine questions before preparing design work.
- Central feature 4: keep package selection, question work, design creation, audit, and Ness acceptance as separate steps.
- Verified conclusion: reviews 46 through 53 are preserved predecessor drafts, not the current accepted design. No file has been moved.

## Item review 54 — Post-acceptance continuation, v1.10

- File currently in `05`: `NH_LIVE_DESIGN_LOOP_POST_ACCEPTANCE_CONTINUATION_MECHANICAL_DESIGN_v1_10_CANDIDATE.md`.
- The dated v1.11 file names v1.10 as its exact correction base and explicitly says v1.10 was not accepted at that time.
- Central feature 1: preserves the accepted v1.9 continuation mechanics.
- Central feature 2: adds a bounded stop when next-package selection repeatedly returns invalid output.
- Central feature 3: protects already-saved result bytes even when the terminal form is invalid.
- Central feature 4: does not invent a new retry policy or a new loop state.
- Verified conclusion: v1.10 is an unaccepted predecessor to v1.11 and must remain in `05`; no move has been made.

## Item review 55 — Live dual-model handoff placement, v1.0

- File currently in `05`: `NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_v1_0_CANDIDATE.md`.
- The accepted v1.1 file is dated July 12, 2026, names v1.0's exact identity, and explicitly preserves v1.0 as historical candidate provenance.
- Central feature 1: a heavier local model proposes substance in the background.
- Central feature 2: a lighter local model remains the only visible conversational voice.
- Central feature 3: N.H validates both outputs before presentation.
- Central feature 4: Bundle 7 owns the roles while Bundle 8 owns the complete handoff mechanics.
- Verified conclusion: v1.0 is historical; v1.1 is the accepted corrected version. No file has been moved.

## Item reviews 56–69 — Understandable acceptance surface, v1.0 through v1.13

- Files currently in `05`: `NH_NESS_DESIGN_ACCEPTANCE_RECORD_AND_UNDERSTANDABLE_ACCEPTANCE_SURFACE_MECHANICAL_DESIGN_v1_0_CANDIDATE.md` through `..._v1_13_CANDIDATE.md`.
- The dated v1.15 file carries the explicit predecessor path and identity for each correction round. The chain is therefore proved from the documents, not inferred from version numbers or filesystem dates.
- v1.14 has a separate exact acceptance receipt. Later accepted continuation evidence states that v1.15 was accepted for the same scope and governs where it differs.
- Central feature 1: Ness must receive one understandable eight-part surface before acceptance is actionable.
- Central feature 2: acceptance is separate from closure, adoption, integration, implementation, and next-package work.
- Central feature 3: the explicit acceptance action appends one bound event and calls no model.
- Central feature 4: current-head, candidate, source, audit, explanation, and operation-chain evidence are rechecked before acceptance.
- Verified conclusion: v1.0 through v1.13 are predecessor drafts, not the current accepted version. No file has been moved.

## Item reviews 70–73 — Provenance-first multi-index memory fabric, v1.0 through v1.3

- Files currently in `05`: `NH_PROVENANCE_FIRST_MULTI_INDEX_MEMORY_FABRIC_MECHANICAL_DESIGN_v1_0_CANDIDATE.md` through `..._v1_3_CANDIDATE.md`.
- The dated v1.4 file explicitly identifies v1.3 as its exact predecessor and states that v1.0 through v1.3 are preserved unchanged as history.
- Central feature 1: indexes are derived and rebuildable views, never the memory or the truth itself.
- Central feature 2: privacy and access checks happen before relevance and retrieval.
- Central feature 3: different relationship and retrieval channels keep separate meanings and ranks.
- Central feature 4: build, publish, query, recovery, and coverage use explicit identities and owner fences.
- Verified conclusion: v1.0 through v1.3 are historical predecessors. v1.4 has authenticated journal acceptance but lacks a separate receipt in `04`, as recorded in review 12. No file has been moved.

## Item reviews 74–82 — Unified Durable Operation Kernel, v1.0 through v1.8

- Files currently in `05`: `NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_0_CANDIDATE.md` through `..._v1_8_CANDIDATE.md`.
- The accepted v1.9 file carries exact predecessor identities and standings.
- v1.0, v1.1, and v1.2 are preserved historical predecessors.
- v1.3 is explicitly marked aborted and incomplete, with nothing carried forward from it.
- v1.4 and v1.5 are preserved historical predecessors.
- v1.6, v1.7, and v1.8 are explicitly marked interrupted and incomplete, not eligible for audit or acceptance, with nothing carried forward from them.
- Central feature 1: the kernel coordinates identities, generations, children, checkpoints, recovery, terminal evidence, and acknowledgement without deciding policy.
- Central feature 2: child membership is recorded before child work and closed against one exact membership head.
- Central feature 3: recovery reads owner truth first and never repeats an external or stored effect merely because acknowledgement was lost.
- Central feature 4: terminal results remain final, and contradictions preserve history while failing closed.
- Verified conclusion: none of v1.0 through v1.8 is the current accepted design; accepted v1.9 is recorded in review 13. No file has been moved.

## Item review 83 — A2 current-status pointer

- File currently in `05`: `NH_A2_CURRENT_STATUS_v1_1.md`.
- The file is dated July 1, 2026 and explicitly identifies itself as a navigation and status pointer, not an authority and not a design candidate.
- It correctly points to accepted A2 v1.8 and its closure record in `04`.
- It also contains old location statements about historical A2 files that no longer match the current working tree after the separately authorized history removal.
- Verified conclusion: this is a status pointer with stale location information, not a candidate to move into `04`. No file has been moved.

## Item review 84 — Decision Defaults v2.3 candidate

- File currently in `05`: `NH_DECISION_DEFAULTS-S19_v2_3_CANDIDATE.md`.
- Its own status explicitly says candidate, not adopted, and not authoritative, and says v2.2 remains active until Ness explicitly adopts a successor.
- Other later design files claim that v2.3 was adopted. No matching standalone adoption record was found in `04` during this audit.
- Central feature: it changes the working-role rule while carrying the rest of v2.2 forward.
- Verified conclusion: the standing is contradictory across documents. Keep it in `05` pending direct reconciliation; do not treat the date or filename as adoption proof. No file has been moved.

## Item review 85 — A19 Unreal Engine 5 local-world direction

- File currently in `05`: `NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_WONDER_RUNTIME_v1.md`.
- It is dated August 14, 2026 and records a Ness-selected technical direction, but explicitly says A19 is not package-complete, not integrated, and not implemented.
- Central feature 1: Unreal Engine 5 is the preferred local 3D runtime; N.H remains outside it.
- Central feature 2: Unreal is not memory or authority and cannot write directly into N.H memory.
- Central feature 3: Wonder remains labelled possibility rather than reality.
- Central feature 4: Blender remains an optional local creation tool.
- Verified conclusion: this is an approved direction and blueprint, not a completed accepted standalone design. Its present non-authoritative placement is consistent with its own status. No file has been moved.

## Item review 86 — Five framework capability additions

- File currently in `05`: `NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md`.
- It is dated August 4, 2026 and explicitly records a Ness-approved strategic direction, while saying the five mechanical packages are not all complete, integrated, or implemented.
- Central feature 1: Authority Integrity Control Plane.
- Central feature 2: Unified Durable Operation Kernel.
- Central feature 3: Provenance-First Multi-Index Memory Fabric.
- Central feature 4: bounded self-healing and governed tool-building capabilities remain later work.
- Verified conclusion: this is an approved strategic direction source, not a completed package to move into `04`. No file has been moved.

## Item review 87 — Live dual-model handoff decision

- File currently in `05`: `NH_DECISION_PACKAGE_LIVE_DUAL_MODEL_HANDOFF_v1.md`.
- It is dated July 1, 2026 and explicitly records a Ness-approved standalone concept that is not yet integrated into Master V10 or the working map.
- Central feature 1: a heavier local model performs deeper background analysis.
- Central feature 2: a lighter model is the single visible conversational carrier.
- Central feature 3: N.H validates both and remains the authority over both.
- Central feature 4: the light model may change wording but not meaning, certainty, or conclusions.
- Verified conclusion: this is an approved concept decision, not a completed integrated design package. Its current placement remains appropriate. No file has been moved.

## Full-list audit completion

- All 87 Markdown files currently present in `05_ACTIVE_CANDIDATE` have now been reviewed and recorded in this file.
- The audit was read-only. No file was moved, removed, renamed, or edited by the audit.
- Any next file-placement action requires a separate exact proposal and Ness's explicit approval.
